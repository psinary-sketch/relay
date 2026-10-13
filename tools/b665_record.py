# -*- coding: utf-8 -*-
"""b665_record.py -- THE ACT'S RECORD TOOL, b665 under (R275).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b665's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### (R274)(4), standing: no constant here names a kernel file; the kernel files are read from the act's banks through
### tools/b665_worklist.py's kernel_files(), the read printed.
### Carried by the Write tool from b664_record.py (the helpers, the guarded landing, the readers, the answers); new here: the record line of
### (R275)(1). The later routes (the statement bank, the attempt, the runner, the landings, the control, the caveat, the merge, the seal's
### banks, the root, the scores, the record) are added by the Edit tool before the seal, each run before the face names it.
### Routes: `python tools/b665_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b665_worklist as K          # noqa: E402

STANDIN = bool(os.environ.get('B665_STANDIN'))


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(path) else ''


def rdn(name):
    return rd(os.path.join(D, name))


def put_json(name, obj):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'H1', 'H2', 'H3', 'S1', 'S2', 'S3')
    return {
        'b665_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b665_findings.json': dict(entry_line=99999, title='stand-in'),
        'b665_trail.json': dict(line=99999),
        'b665_act_root.json': dict(root='0' * 64, previous='1bd81723' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return _standins().get(name, {}) if STANDIN else {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def _ws(s):
    return ' '.join(s.split())


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b665's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b665_scanfile_%s.md' % tag)
    R3._write(p, allt.encode('utf-8'))
    sc = R3._scan(p)
    clean = R3._clean(sc)
    ticks = odd_lines(allt)
    unread = [x for x in ('### NOT', 'None', ' ? ', '`?`') if x in allt]
    outside = [n for n in R41.OAI_NEEDLES if n in allt]
    stems = [s for s in ('gap', 'blind') if re.search(r'\b' + s, allt, re.I)]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks by line: %s ; unread figures: %s ; outside names: %s ; '
          'stems: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', outside or 'NONE',
                         stems or 'NONE'))
    if not clean:
        print(sc[-1500:])
    fired = bool(any(nd.values()) or not clean or ticks or unread or outside or stems)
    return [tuple(c) for c in cells], fired


def land(items, bank, tag, entry=None, check=(), expect_cells=(), dry=True):
    for f, ln, needle in check:
        L = rd(FIND if f == 'FINDINGS.md' else OT).split(NL)
        if needle not in L[ln - 1]:
            sys.exit('### %s :%d DOES NOT CARRY %r -- NOTHING WRITTEN' % (f, ln, needle))
    items = [(f, h, conv(t)) for f, h, t in items]
    cells, fired = screens(items, tag, dry)
    if dry:
        for f, h, t in items:
            print('----', f, NL + t)
        return
    if cells != [tuple(x) for x in expect_cells] or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    n = {'FINDINGS.md': len(rd(FIND).split(NL)), 'OPEN_TRAILS.md': len(rd(OT).split(NL))}
    want = {}
    for f, h, t in items:
        want[h] = n[f] + 1 if rd(FIND if f == 'FINDINGS.md' else OT).endswith(NL) else n[f] + 2
        n[f] += len(t.strip(NL).split(NL)) + 1
    for f, h, _t in items:
        guard_absent(FIND if f == 'FINDINGS.md' else OT, h)
    out = []
    for f, h, t in items:
        path = FIND if f == 'FINDINGS.md' else OT
        r = append_to(path, t)
        got = line_of(path, h)
        out.append(dict(file=f, head=h, line=got, append=r))
        if got != want[h]:
            put_json(bank, dict(entry=entry, lines=out, at=utc(), stopped=True))
            sys.exit('### %s LANDED AT :%s, NOT :%d -- STOPPED' % (h[:60], got, want[h]))
    put_json(bank, dict(entry=entry, lines=out, at=utc()))
    print('  ' + ' ; '.join('%s :%s' % (x['file'], x['line']) for x in out))


# ================================================================================ THE READERS, ONE PER ROW SHAPE A ROUTE READS ((R263)(3))
RUNNER_KEYS = ('kernel', 'branch', 'ref', 'target', 'run_id', 'conclusion', 'artifact_sha256', 'mem_low', 'stopped', 'gate', 'merged', 'tag')


def read_runner_row(r):
    """a row of data/b665_runner_rows.json -- every key of RUNNER_KEYS present (None where a step did not reach it); returns the row's reading
    (kernel, outcome, merged); raises KeyError on a row of another shape."""
    missing = [k for k in RUNNER_KEYS if k not in r]
    if missing:
        raise KeyError('runner row without %s' % missing)
    if r['stopped']:
        outcome = 'STOPPED BENEATH THE HOLD ON THE RUNNER'
    elif r['conclusion'] != 'success':
        outcome = 'RUN %s' % (r['conclusion'] or 'NOT CONCLUDED')
    else:
        outcome = 'GATE %s' % (r['gate'] or 'UNREAD')
    return dict(kernel=r['kernel'], outcome=outcome, merged=r['merged'], low=r['mem_low'], above_hold=(r['mem_low'] is not None and r['mem_low'] >= 2560))


def read_score_row(k, v):
    """a scores row: key N1..N5, H1..H3 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text) -- the whole verdict, not its
    first word (b656's defect (e))."""
    if not re.match(r'^(N[1-5]|H[1-3]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


LANDING_POINTS = ('DERIVES', 'COMPILED, PROOF OPEN', 'NOT COMPILED')


def read_landing_row(row):
    """a lemma's landing row (data/b665_landings.json): name, file, landing point (one of LANDING_POINTS), the gate's prints and, where open,
    the obstruction's file and line; returns (name, point, where); raises on a row of another shape."""
    for k in ('name', 'file', 'point', 'prints', 'obstruction'):
        if k not in row:
            raise KeyError('landing row without %s' % k)
    if row['point'] not in LANDING_POINTS:
        raise ValueError('landing point not in the vocabulary: %r' % row['point'])
    if row['point'] != 'DERIVES' and not row['obstruction']:
        raise ValueError('an open landing without its obstruction line')
    return row['name'], row['point'], row['obstruction'] or row['file']


def read_kernel_files():
    """(R274)(4), standing: the act's kernel files as tools/b665_worklist.py's kernel_files() reads them from the act's banks; returns
    [(file, [banks])]; raises when the read finds no file (no constant stands in for it)."""
    kf = K.kernel_files()
    if not kf or not all(isinstance(f, str) and f.endswith('.lean') and b for f, b in kf):
        raise LookupError('no kernel file read from the act`s banks')
    return kf


READERS = ['read_runner_row', 'read_score_row', 'read_head', 'read_landing_row', 'read_kernel_files']


# ================================================================================ COMPONENT 1: THE RECORD LINE, (R275)(1)
WH = ('*Appended 2026-10-13 by b665 to b664’s entry (:8563), under `(R275)`(1) -- b664 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b664_closing.txt):*')


def _weight():
    return ('\n' + WH + ' SIDE-effects, the next kernel by count (7 at relay data/b647_table_kernels.txt :10, its main moved to 9a279ac): 2 '
            'blocks at main read into 20 sentence rows, 4 OVERREACHES cut in one commit; the five restated Milestones blocks UNRESOLVED-NO-CELL, '
            'listed for the cell refresh; the workflow put on main in b654’s form beside build.yml, run 38431820497 with 34 prints at the '
            'standard three or none, the kernel’s relay print bank opened, the README’s "Axiom-free" (:28) and "0 axioms beyond ZFC" (:103) '
            'checked against it and not contradicted; merged at 78bbcff, tag v0.1.1. test_met_b646.py’s case (2) made a prefix plus ruled '
            'entries by name; the suite and the scorer reading the act’s kernel files from its cut bank. Relay efdd9309, PLACE-papers b1a2bab, '
            'FINDINGS :8561 and :8563, OPEN_TRAILS :14186-:14194, the root 1bd81723… over 46 banks; the suite 82 of 83 with the SIDE-cosmo row '
            'alone declared; five defects, (a) and (b) the navigator’s; the child-process encoding reading (python -X utf8) standing as the '
            'face declared it; the mirror at mirror-refresh-2026-10-13-b664.zip. Nothing deposited.\n')


def c1(*a):
    items = [('FINDINGS.md', WH, _weight())]
    land(items, 'b665_record_lines.json', 'c1', entry=K.B664_ENTRY,
         check=[('FINDINGS.md', K.B664_ENTRY, "## SIDE-effects’ docstrings"), ('OPEN_TRAILS.md', K.B664_TRAIL, '### b664')],
         dry='dry' in a)


# ================================================================================ THE AUTHOR'S ANSWERS (b664's route, carried)
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID


def _session_rows():
    start = None
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8', errors='replace'), 1):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if start is None and K.ANCHOR in raw and o.get('type') == 'user' and not o.get('isCompactSummary'):
            start = i
        if start is not None:
            yield i, o, start


def answers(*a):
    """data/b665_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
    delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim."""
    calls, results, words, plain_, start = [], {}, [], [], None
    for i, o, st in _session_rows():
        start = st
        m = o.get('message') or {}
        cs = m.get('content')
        att = o.get('attachment') or {}
        texts = []
        if att.get('type') == 'queued_command' and isinstance(att.get('prompt'), str):
            texts = [att['prompt']]
        elif o.get('type') == 'user' and not o.get('isCompactSummary'):
            texts = [cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']
            for t in texts:
                if t and not t.lstrip().startswith(('<', 'BEGIN', 'RULING')) and len(t) < 400 and i > st:
                    plain_.append((i, t.strip()))
        for t in texts:
            for mm in re.finditer(r'(?ms)^BEGIN\s*\n(.*?)\nEND\s*$', t or ''):
                if K.ANCHOR not in mm.group(1):
                    words.append((i, mm.group(1)))
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((i, c['id'], c['input'], o.get('timestamp')))
            if isinstance(c, dict) and c.get('type') == 'tool_result':
                t = c.get('content')
                results[c.get('tool_use_id')] = (i, ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t, o.get('timestamp'))
    if start is None:
        sys.exit('### THE ANCHOR IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    L, n = [], 0
    for i, cid, inp, ts in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d, %s)' % (cid, K.SESSION_ID, i, ts))
        for k, q in enumerate(inp.get('questions', []), 1):
            n += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT', None))
        L += ['RESULT (transcript line %s, %s): %s' % (r[0], r[2], r[1]), '']
    W, seen = [], set()
    for i, w in words:
        if w in seen:
            continue
        seen.add(w)
        W += ['### THE AUTHOR`S WORD (transcript line %d), BEGIN to END, verbatim:' % i] + w.replace('\r', '').split(NL) + ['']
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %d), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b665 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b665_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b665_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 2: THE STATEMENTS, (R275)(2)-(3), BEFORE ANY LEAN
EFK = 'SIDEExplicitFormula/'
ML_ = K.MATHLIB
# ### every term either statement uses, traced to its declaration by file and line: (term, repo, file, the declaration's pattern, what it is)
TRACE_K = [
    ('LiWeil.LiCoeff', K.KD, EFK + 'LiWeil.lean', r'^def LiCoeff\b', 'the programme`s Li coefficient, a sum over the genuine zeros of ζ (kernel)'),
    ('LiCriterionBridge.li_coeff_eq_taylorCoeff', K.KD, EFK + 'LiCriterionBridge.lean', r'^theorem li_coeff_eq_taylorCoeff\b',
     'LiCoeff (n + 1) = (taylorCoeff riemannXi n).re (kernel, v0.9)'),
    ('LiCriterion.taylorCoeff', K.KD, 'Vendored/Bulka/Lc/LiCriterion/Basic.lean', r'^noncomputable def taylorCoeff\b',
     'the n-th Taylor coefficient at 0 of logDeriv (phi f) (vendored, Bulka)'),
    ('LiCriterion.phi', K.KD, 'Vendored/Bulka/Lc/LiCriterion/Basic.lean', r'^noncomputable def phi\b', 'phi f z = f (1 / (1 - z)) (vendored)'),
    ('LiCriterion.riemannXi', K.KD, 'Vendored/Bulka/Lc/LiCriterion/Basic.lean', r'^noncomputable def riemannXi\b',
     'ξ(s) = ½ s (s − 1) completedRiemannZeta₀ s + ½ (vendored)'),
    ('Keiper.taylorAt', K.KD, EFK + 'Keiper.lean', r'^def taylorAt\b', 'iteratedDeriv k f a / k! (kernel, b601)'),
    ('Keiper.xiLogCoeff', K.KD, EFK + 'Keiper.lean', r'^def xiLogCoeff\b', 'taylorAt (logDeriv riemannXi) 1 k (kernel)'),
    ('Keiper.zetaLogCoeff', K.KD, EFK + 'Keiper.lean', r'^def zetaLogCoeff\b', 'taylorAt (logDeriv riemannZeta₁) 1 k (kernel)'),
    ('Keiper.gammaRLogCoeff', K.KD, EFK + 'Keiper.lean', r'^def gammaRLogCoeff\b', 'taylorAt (logDeriv Gammaℝ) 1 k (kernel)'),
    ('Keiper.keiperA', K.KD, EFK + 'Keiper.lean', r'^def keiperA\b', '(-1)^k + zetaLogCoeff k + gammaRLogCoeff k (kernel)'),
    ('Keiper.keiperSum', K.KD, EFK + 'Keiper.lean', r'^def keiperSum\b', 'SUM_{k <= n} C(n + 1, k + 1) keiperA k (kernel)'),
    ('Keiper.KeiperTaylor', K.KD, EFK + 'Keiper.lean', r'^def KeiperTaylor\b', 'forall n, taylorCoeff riemannXi n = keiperSum n (kernel)'),
    ('Keiper.stieltjes', K.KD, EFK + 'Keiper.lean', r'^def stieltjes\b',
     'the n-th Stieltjes constant, (-1)^n riemannZeta₀^(n)(1) -- a kernel definition by derivative (b601), named'),
    ('Keiper.stieltjes_zero', K.KD, EFK + 'Keiper.lean', r'^theorem stieltjes_zero\b', 'stieltjes 0 = γ (kernel, from Mathlib`s limit)'),
    ('Keiper.binomialTransform_holds (K1)', K.KD, EFK + 'KeiperIdentities.lean', r'^theorem binomialTransform_holds\b', 'K1 (kernel, v0.26)'),
    ('Keiper.logDerivSplit_holds (K2)', K.KD, EFK + 'KeiperIdentities.lean', r'^theorem logDerivSplit_holds\b', 'K2 (kernel, v0.26)'),
    ('Keiper.stieltjesLog_holds (K3)', K.KD, EFK + 'KeiperIdentities.lean', r'^theorem stieltjesLog_holds\b',
     'K3: zetaLogCoeff in the Stieltjes constants, coefficient by coefficient (kernel, v0.26)'),
    ('Keiper.GammaRZetaValues (K4)', K.KD, EFK + 'Keiper.lean', r'^def GammaRZetaValues\b', 'K4: gammaRLogCoeff in ζ(k + 2) -- OPEN since b641'),
    ('riemannZeta₀', ML_, 'Mathlib/NumberTheory/Harmonic/ZetaAsymp.lean', r'^noncomputable def riemannZeta₀\b', 'Mathlib at de5ce8a9'),
    ('riemannZeta₁', ML_, 'Mathlib/NumberTheory/Harmonic/ZetaAsymp.lean', r'^noncomputable def riemannZeta₁\b', '1 + (s − 1) riemannZeta₀ s, Mathlib'),
    ('Gammaℝ', ML_, 'Mathlib/Analysis/SpecialFunctions/Gamma/Deligne.lean', r'^noncomputable def Gammaℝ\b', 'π^(−s/2) Γ(s/2), Mathlib'),
    ('riemannZeta_residue_one', ML_, 'Mathlib/NumberTheory/LSeries/RiemannZeta.lean', r'^lemma riemannZeta_residue_one\b', 'b589`s first, Mathlib'),
    ('tendsto_riemannZeta_sub_one_div', ML_, 'Mathlib/NumberTheory/Harmonic/ZetaAsymp.lean', r'^theorem _root_.tendsto_riemannZeta_sub_one_div\b',
     'b589`s second (γ as the constant term), Mathlib'),
    ('Real.eulerMascheroniConstant', ML_, 'Mathlib/NumberTheory/Harmonic/EulerMascheroni.lean', r'def eulerMascheroniConstant\b', 'γ, Mathlib'),
]
TRACE_T = [
    ('B321.plateau', K.KD, EFK + 'TwoPropertyWindow.lean', r'^def plateau\b', 'the plateau, ramp fraction F, half-width L (kernel)'),
    ('B321.plateau_contDiff', K.KD, EFK + 'TwoPropertyWindow.lean', r'^theorem plateau_contDiff\b', 'C^n for every n (kernel, compiled)'),
    ('B321.plateau_even', K.KD, EFK + 'TwoPropertyWindow.lean', r'^theorem plateau_even\b', 'even (kernel, compiled)'),
    ('B321.plateau_eq_one', K.KD, EFK + 'TwoPropertyWindow.lean', r'^theorem plateau_eq_one\b', '1 on [-(1-F)L, (1-F)L] (kernel, compiled)'),
    ('B321.plateau_support_Icc', K.KD, EFK + 'PowerWindow.lean', r'^theorem plateau_support_Icc\b', 'support in [-L, L] (kernel, compiled)'),
    ('B321.plateau_nonneg', K.KD, EFK + 'PowerWindow.lean', r'^theorem plateau_nonneg\b', '0 <= plateau (kernel, compiled)'),
    ('Schema.detectorBase', K.KD, EFK + 'Schema/Detector.lean', r'^def detectorBase\b', 'plateau (1/2) (baseWidth ρ): the detector`s base'),
    ('Schema.baseWidth', K.KD, EFK + 'Schema/Detector.lean', r'^def baseWidth\b', '1 / (4 (‖γ(ρ)‖ + 1)) -- Detector.lean :33'),
    ('Schema.half_pos`, half_lt_one`, baseWidth_pos', K.KD, EFK + 'Schema/Detector.lean', r'^theorem baseWidth_pos\b',
     'the base`s parameter hypotheses, compiled'),
    ('Zeta23.paperFT', K.KD, 'Zeta23/Defs.lean', r'^def paperFT\b', '∫ f(u) e^{izu} du'),
    ('Zeta23.gammaOf', K.KD, 'Zeta23/Defs.lean', r'^def gammaOf\b', '(ρ − 1/2) / i'),
    ('Zeta23.ZeroConfig.strip', K.KD, 'Zeta23/Defs.lean', r'^  strip :', '0 <= Re ρ <= 1 for every configuration point'),
    ('B321.phiC', K.KD, EFK + 'PairTerm.lean', r'^def phiC\b', 'the real window as a complex function'),
    ('B321.offScore', K.KD, EFK + 'PowerWindow.lean', r'^def offScore\b', '‖paperFT (phiC g) (gammaOf ρ)‖'),
    ('B321.paperFT_decay', K.KD, EFK + 'DecayBound.lean', r'^theorem paperFT_decay\b',
     '‖paperFT (phiC g) z‖ ‖z‖^p <= (∫ |g^(p)|) e^{L |Im z|}, g C^p supported in [-L, L] (kernel, compiled)'),
    ('B321.gammaOf_re`, gammaOf_im`', K.KD, EFK + 'RestBound.lean', r"^theorem gammaOf_im'", 'Re γ(ρ) = Im ρ, Im γ(ρ) = −(Re ρ − 1/2) (kernel)'),
    ('Real.smoothTransition', ML_, 'Mathlib/Analysis/SpecialFunctions/SmoothTransition.lean', r'^def smoothTransition\b|smoothTransition \(x : ℝ\)',
     'Mathlib`s closed-form transition, monotone'),
]
FILES_PLANNED = [EFK + 'KeiperFinite.lean', EFK + 'FirstOrderBound.lean']


def _trace(rows):
    out = []
    for term, repo, f, pat, what in rows:
        n = None
        for i, l in enumerate(rd(os.path.join(repo, *f.split('/'))).split(NL), 1):
            if re.search(pat, l):
                n = i
                break
        out.append((term, '%s :%s' % (f, n) if n else None, what))
    return out


def _stieltjes_search():
    """the Mathlib search for higher Stieltjes constants, run live at the pin, bounded to Mathlib/ (git grep), printed whole by count and residue."""
    r = subprocess.run(['git', '-C', ML_, 'grep', '-n', '-i', 'stieltjes', '--', 'Mathlib/*.lean'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    hits = [l for l in r.stdout.split(NL) if l.strip()]
    measure = re.compile(r'stieltjesFunction|Stieltjes (measure|function|outer|transform)|Measure\.Stieltjes|stieltjesOfMeasurableRat|'
                         r'RatStieltjes|MeasurableStieltjes|stieltjes_id|Stieltjes measures|StieltjesFunction', re.I)
    residue = [l for l in hits if not measure.search(l)]
    pin = g(ML_, 'rev-parse', '--short=8', 'HEAD').strip()
    files = sorted(set(l.split(':', 1)[0] for l in hits))
    return pin, hits, residue, files


def statement(*a):
    tk, tt = _trace(TRACE_K), _trace(TRACE_T)
    pin, hits, residue, files = _stieltjes_search()
    miss = [t for t, w, _x in tk + tt if not w]
    L = ['b665 -- COMPONENT 2: THE STATEMENTS, (R275)(2)-(3), DRAFTED IN A BANK BEFORE ANY LEAN (%s)' % utc(), '',
         '### SIDE-explicit-formula at main %s (= v0.29); Mathlib at %s. No Lean file is written before the author`s word on the prompt of '
         '(R275)(2)-(3); the files planned (the act`s kernel files, read from this bank by tools/b665_worklist.py`s kernel_files()): %s.' % (
             g(K.KD, 'rev-parse', '--short=7', 'main').strip(), pin, ', '.join(FILES_PLANNED)), '',
         '=' * 100, '### (I) THE KEIPER FINITE-n EQUALITY, (R275)(2). Planned file SIDEExplicitFormula/KeiperFinite.lean, namespace '
         'SIDEExplicitFormula.Keiper, importing SIDEExplicitFormula.KeiperIdentities.', '=' * 100, '',
         '  (K-a) theorem keiperTaylor_holds : KeiperTaylor',
         '        -- forall n, LiCriterion.taylorCoeff LiCriterion.riemannXi n = keiperSum n, at every n (b601 proved n = 0 only, keiperTaylor_zero).',
         '  (K-b) theorem liCoeff_succ_eq_keiperSum (n : ℕ) : LiWeil.LiCoeff (n + 1) = (keiperSum n).re',
         '        -- THE FINITE-n EQUALITY: λ_{n+1} = Re SUM_{k <= n} C(n + 1, k + 1) ((-1)^k + zetaLogCoeff k + gammaRLogCoeff k).', '',
         '  THE BENCH`S FORM, TRACED (not a separate statement): b589`s Keiper route (relay data/b589_three_way.txt :3) computes λ_N = N SUM_{j=1..N}',
         '  C(N-1, j-1) η_j with η_j the Taylor coefficients of log ξ at s = 1. With N = n + 1: xiLogCoeff k, the Taylor coefficient of (log ξ)` = ξ`/ξ,',
         '  is (k + 1) η_{k+1}, and C(n + 1, k + 1) (k + 1) = (n + 1) C(n, k), so SUM_k C(n + 1, k + 1) xiLogCoeff k = N SUM_{j=1..N} C(N-1, j-1) η_j:',
         '  the bench`s sum term for term. K2 (logDerivSplit_holds) puts xiLogCoeff k = keiperA k, the bench`s three parts: 1/s, (s - 1) ζ(s) and Γℝ.', '',
         '  THE CONSTANTS. zetaLogCoeff carries the Stieltjes constants through K3 (stieltjesLog_holds: (k + 1) poleCoeff (k + 1) = SUM_i poleCoeff i',
         '  zetaLogCoeff (k - i), poleCoeff (i + 1) = (-1)^i stieltjes i / i!); stieltjes n is the kernel`s definition by derivative (Keiper.lean :47),',
         '  named, and stieltjes 0 = γ (stieltjes_zero, through Mathlib`s limit). Mathlib names no higher Stieltjes constant (the search below), and',
         '  (K-b) needs none by name: they live inside zetaLogCoeff. gammaRLogCoeff carries ζ(k + 2) and log π only through K4 (GammaRZetaValues),',
         '  OPEN since b641 (relay data/b641_keiper_status.txt (K4)): so the equality is stated in the kernel`s Taylor coefficients, which every',
         '  term below names, and not in ζ-values -- the prompt puts the choice.', '',
         '  THE PROOF`S SHAPE: (K-a) from K1 (binomialTransform_holds n) and K2 (logDerivSplit_holds k), the first conjunct of b601`s',
         '  keiperTaylorIdentity_of (Keiper.lean :133-:137) with its two used fields proved; (K-b) li_coeff_eq_taylorCoeff n, then (K-a) at n.',
         '  b589`s two lemmas at de5ce8a9 (riemannZeta_residue_one, RiemannZeta.lean :242; tendsto_riemannZeta_sub_one_div, ZetaAsymp.lean :342)',
         '  enter through the kernel`s stieltjes_zero and the residue of riemannZeta₁ (Keiper.lean :54, :65) -- the γ term, already compiled.', '',
         '### EVERY TERM, TRACED (H1: a Mathlib name at de5ce8a9 or a named definition):']
    L += ['  %-48s %s -- %s' % (t, w or '### NOT FOUND', x) for t, w, x in tk]
    L += ['', '### THE SEARCH FOR HIGHER STIELTJES CONSTANTS IN MATHLIB AT %s (git grep -n -i stieltjes -- Mathlib/*.lean, run live):' % pin,
          '  hits %d in %d files ; after the measure-theoretic objects (StieltjesFunction, Stieltjes measures, stieltjesOfMeasurableRat, the '
          'Stieltjes transform) are set aside: %d' % (len(hits), len(files), len(residue))]
    L += ['    ' + x for x in residue] or ['    NONE -- no Stieltjes constant by name; γ alone, as Real.eulerMascheroniConstant']
    L += ['', '=' * 100, '### (II) THE TRANSFORM BOUND, (R275)(3) -- b663`s B1 as a kernel lemma. Planned file SIDEExplicitFormula/FirstOrderBound.lean, '
          'namespace SIDEExplicitFormula.B321, importing SIDEExplicitFormula.PowerWindow.', '=' * 100, '',
          '  (T-a) theorem plateau_deriv_abs_integral (F L : ℝ) (hF0 : 0 < F) (hF1 : F < 1) (hL : 0 < L) :',
          '          ∫ u, |deriv (plateau F L hF0 hF1 hL) u| = 2',
          '        -- the total variation: the rise 0 to 1 and the fall 1 to 0.',
          '  (T-b) theorem paperFT_plateau_first_order (F L : ℝ) (hF0 : 0 < F) (hF1 : F < 1) (hL : 0 < L) (z : ℂ) :',
          '          ‖Zeta23.paperFT (phiC (plateau F L hF0 hF1 hL)) z‖ * ‖z‖ ≤ 2 * Real.exp (L * |z.im|)',
          '        -- b663`s derivation line (relay data/b663_epstein_plan.txt :160), |paperFT g0 z| ≤ 2 e^{ℓ|Im z|}/|z|, in product form (no z ≠ 0).',
          '  (T-c) theorem offScore_plateau_first_order (F L : ℝ) (hF0 : 0 < F) (hF1 : F < 1) (hL : 0 < L) (ρ : ℂ) (h0 : 0 ≤ ρ.re) (h1 : ρ.re ≤ 1) :',
          '          offScore (plateau F L hF0 hF1 hL) ρ * |ρ.im| ≤ 2 * Real.exp (L / 2)',
          '        -- B1 at strip points as b663 wrote it (:156, offScore g0 ρ ≤ 2 e^{ℓ/2}/|Im ρ|; the form 2e^{ℓ/2}/|z| at :107).', '',
          '  THE WINDOW AND ITS HYPOTHESES (H2): the statements range over the kernel`s plateau at every ramp fraction F and half-width L; their',
          '  hypotheses are the plateau`s own parameter ranges (0 < F < 1, 0 < L), and for (T-c) the strip, which every configuration point',
          '  carries (ZeroConfig.strip). The detector`s base detectorBase ρ = plateau (1/2) (baseWidth ρ) meets them by the compiled half_pos`,',
          '  half_lt_one` and baseWidth_pos (Detector.lean); b663`s g0 = plateau (1/2) ℓ at qE0 by the same two and its ℓ > 0. No hypothesis the',
          '  window does not already satisfy by a compiled lemma.', '',
          '  THE PROOF`S SHAPE: (T-b) paperFT_decay 1 (DecayBound.lean :63) at plateau_contDiff and plateau_support_Icc, iteratedDeriv 1 = deriv,',
          '  then (T-a). (T-c) (T-b) at z = gammaOf ρ: |Im γ(ρ)| = |Re ρ − 1/2| ≤ 1/2 (gammaOf_im`), |Im ρ| ≤ ‖γ(ρ)‖ (gammaOf_re`), the lines of',
          '  zero_weight (PowerLimit.lean :813-:832). (T-a), the substance: on u ≥ 0 the plateau is smoothTransition ((L − u)/(F L)) (the other',
          '  factor is 1 there), antitone by Mathlib`s smoothTransition monotonicity, so its derivative is ≤ 0 on (0, L); |deriv| is even',
          '  (plateau_even); the integral is over [−L, L] (the derivative`s support), twice the integral over [0, L] of −deriv, which is',
          '  plateau 0 − plateau L = 1 − 0 by the fundamental theorem (plateau_eq_one at 0; the support at L).', '',
          '### EVERY TERM, TRACED (H2: each the kernel`s, compiled, or Mathlib`s):']
    L += ['  %-48s %s -- %s' % (t, w or '### NOT FOUND', x) for t, w, x in tt]
    L += ['', '### ### **TERMS TRACED %d ; NOT FOUND %d %s ; STIELTJES HITS %d, CONSTANTS BY NAME %d ; FILES PLANNED %d.**' % (
        len(tk) + len(tt), len(miss), miss or '', len(hits), len(residue), len(FILES_PLANNED))]
    if miss:
        print(NL.join(L[-12:]))
        sys.exit('### A TERM IS NOT TRACED -- NOTHING WRITTEN')
    put_txt(K.STATEMENT_BANK + '.txt', L)
    put_json(K.STATEMENT_BANK + '.json', dict(at=utc(), kernel_main=g(K.KD, 'rev-parse', '--short=7', 'main').strip(), mathlib=pin,
                                              files=FILES_PLANNED, trace_keiper=tk, trace_bound=tt, stieltjes_hits=len(hits),
                                              stieltjes_residue=residue))
    print(NL.join(L[-3:]))


# ================================================================================ COMPONENT 3: THE RUNNER, READ BY ITS RUN ID; THE LANDINGS
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
ERR_RE = re.compile(r'^(?:error: )?(\S+\.lean):(\d+):(\d+): error: (.*)$', re.M)
SORRY_RE = re.compile(r'^(?:warning: )?(\S+\.lean):(\d+):(\d+): (?:warning: )?declaration uses .sorry.', re.M)
# ### the two lemmas of (R275)(4), each its declarations as the statement bank names them (the author's word: each its own declaration)
LEMMAS = [('the Keiper finite-n equality', 'SIDEExplicitFormula/KeiperFinite.lean',
           ['SIDEExplicitFormula.Keiper.keiperTaylor_holds', 'SIDEExplicitFormula.Keiper.liCoeff_succ_eq_keiperSum']),
          ('the transform bound', 'SIDEExplicitFormula/FirstOrderBound.lean',
           ['SIDEExplicitFormula.B321.plateau_deriv_abs_integral', 'SIDEExplicitFormula.B321.paperFT_plateau_first_order',
            'SIDEExplicitFormula.B321.offScore_plateau_first_order'])]
TARGET = 'SIDEExplicitFormula.KeiperFinite SIDEExplicitFormula.FirstOrderBound'


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def _decl_line(src, name):
    short = name.rsplit('.', 1)[1]
    for i, l in enumerate(src.split(NL), 1):
        if re.match(r'^theorem %s\b' % re.escape(short), l):
            return i
    return None


def runner(*a):
    """`runner <run id> <ref> <stage>`: the run read by its id; the artifact listed, downloaded by its id into memory, its sha256 against the
    platform's digest BEFORE any reading; the build's exit, its error lines and its sorry warnings, the memory log's low and any STOP; every print
    of print_targets.txt at the ref; per declaration and per lemma the landing point (DERIVES at the standard three with no sorryAx; COMPILED,
    PROOF OPEN with sorryAx printed, the obstruction the sorry warning's file and line; NOT COMPILED where no print). The stage names the tree
    state ('explore' -- the fallback form; 'merge' -- the stripped tree, the author's word). Banked as data/b665_runner_<stage>.txt, a row of
    data/b665_runner_rows.json and, for the stage's landings, data/b665_landings.json."""
    import hashlib
    import zipfile
    import b569_record as R9
    run_id, ref, stage = int(a[0]), a[1], a[2]
    repo = 'psinary-sketch/' + K.KERNEL
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    pt = [l.strip() for l in (_show(K.KD, ref, 'print_targets.txt') or '').split(NL) if l.strip()]
    kf = read_kernel_files()
    srcs = dict((f, _show(K.KD, ref, f) or '') for f, _b in kf)
    row = dict(kernel=K.KERNEL, branch=K.BRANCH, ref=ref, target=TARGET, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None,
               mem_low=None, stopped=False, gate=None, merged=None, tag=None, stage=stage)
    L = ['b665 -- COMPONENT 3, (R275)(4): THE HOSTED RUNNER FOR %s, STAGE %s, READ BY ITS RUN ID (%s)' % (K.KERNEL, stage.upper(), utc()), '',
         '### the act`s kernel files, read from its banks and from no constant: %s' % '; '.join('%s (from %s)' % (f, ', '.join(b)) for f, b in kf),
         '### print_targets.txt at the ref: %d names' % len(pt),
         '### the dispatch: at main, the ref input %s (the branch %s at that commit) ; target %s' % (ref, K.BRANCH, TARGET),
         '### the run: id %s ; %s ; %s %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('workflowName'), run.get('event'), run.get('status'), run.get('conclusion'), run.get('headSha'),
             run.get('headBranch'), run.get('createdAt'), run.get('updatedAt'))]
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        row['artifact_sha256'] = sha
        L.append('### the artifact: id %s ; name %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if digest and digest == sha else ('### DIFFER' if digest else 'no digest to compare -- NOTHING READ FROM IT')))
        if not digest or digest != sha:
            row['artifact_sha256'] = None
        else:
            with zipfile.ZipFile(io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    row['mem_low'] = int(low[-1]) if low else None
    stops = [l for l in mem.split(NL) if l.startswith('STOP ')]
    row['stopped'] = bool(stops)
    blog = T_.get('build.log', '')
    bexit = T_.get('build_exit.txt', '').strip()
    errs = [(m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)) for m in ERR_RE.finditer(blog)]
    sorries = sorted(set((m.group(1), int(m.group(2))) for m in SORRY_RE.finditer(blog)))
    P = dict((k_, sorted(v_)) for k_, v_ in R9.prints_axioms(T_.get('axioms.txt', '')).items())
    axerr = [l for l in T_.get('axioms.txt', '').split(NL) if ': error' in l]
    per = [(n, P.get(n)) for n in pt]
    readable = bool(row['artifact_sha256']) and not stops
    land_rows = []
    for lem, f, names in LEMMAS:
        src = srcs.get(f, '')
        for n in names:
            ax = P.get(n)
            dl = _decl_line(src, n)
            if ax is None:
                point = 'NOT COMPILED'
            elif set(ax) <= STD3 and 'sorryAx' not in ax:
                point = 'DERIVES'
            else:
                point = 'COMPILED, PROOF OPEN'
            obs = None
            if point != 'DERIVES':
                nxt = [_decl_line(src, m) for m in names if (_decl_line(src, m) or 0) > (dl or 0)]
                end = min(nxt) if nxt else 10 ** 9
                own = [(ff, ln) for ff, ln in sorries if ff.endswith(f.rsplit('/', 1)[1]) and (dl or 0) <= ln < end]
                errs_own = [(ff, ln) for ff, ln, _c, _m in errs if ff.endswith(f.rsplit('/', 1)[1]) and (dl or 0) <= ln < end]
                hits = own + errs_own
                obs = ('%s :%s' % (f, ', :'.join(str(ln) for _ff, ln in hits))) if hits else (
                    '%s :%s (the declaration; its open step reached through a declaration it uses)' % (f, dl))
            land_rows.append(dict(lemma=lem, name=n, file=f, decl_line=dl, point=point, prints=ax, obstruction=obs))
    lem_points = []
    for lem, f, names in LEMMAS:
        pts = [r['point'] for r in land_rows if r['lemma'] == lem]
        lem_points.append((lem, 'DERIVES' if all(p == 'DERIVES' for p in pts) else ('NOT COMPILED' if 'NOT COMPILED' in pts else 'COMPILED, PROOF OPEN')))
    ok = (run.get('conclusion') == 'success' and readable and bexit == '0' and not errs and row['mem_low'] is not None and row['mem_low'] >= K.HOLD
          and len(pt) > 0 and not axerr)
    row['gate'] = ('STOPPED BENEATH THE HOLD' if stops else ('BUILT' if ok else 'NOT BUILT'))
    row['errors'] = [list(e) for e in errs]
    row['sorry_warnings'] = [list(s) for s in sorries]
    row['lemma_points'] = lem_points
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: samples %d ; LOW %s MB ; the hold %d ; STOP lines %s' % (
              len([l for l in mem.split(NL) if 'avail_mb=' in l]), row['mem_low'], K.HOLD, stops or 'NONE'),
          '### the build: exit %s ; error lines %d ; sorry warnings %d ; the log`s last lines:' % (bexit or '### UNREAD', len(errs), len(sorries))] + \
        ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + ['    ERROR %s:%d:%d: %s' % e for e in errs[:30]] + \
        ['    SORRY WARNING %s:%d' % s for s in sorries] + [
          '### the print step: error lines %d%s' % (len(axerr), (' -- ' + ' | '.join(axerr[:4])) if axerr else ''),
          '### THE PRINTS, PER TERMINAL (the standard three: propext, Classical.choice, Quot.sound):'] + \
        ['  %-62s %s' % (n, ax if ax is not None else '### NOT PRINTED') for n, ax in per] + [
          '', '### THE LANDING POINT PER DECLARATION ((R275)(4); the author`s word: each its own declaration, read per statement):'] + \
        ['  %-56s %-22s %s' % (r['name'].rsplit('.', 1)[1], r['point'], ('obstruction ' + r['obstruction']) if r['obstruction'] else
                               'decl %s :%s' % (r['file'], r['decl_line'])) for r in land_rows] + [
          '', '### THE LANDING POINT PER LEMMA:'] + ['  %-34s %s' % lp for lp in lem_points] + [
          '', '### ### **STAGE %s ; RUN %s ; CONCLUSION %s ; ARTIFACT SHA256 %s ; MEMORY LOW %s MB (HOLD %d) ; BUILD EXIT %s ; ERROR LINES %d ; '
          'SORRY WARNINGS %d ; TERMINALS %d, PRINTED %d ; %s.**' % (
              stage.upper(), run_id, run.get('conclusion'), (row['artifact_sha256'] or '### NONE')[:16], row['mem_low'], K.HOLD,
              bexit or '### UNREAD', len(errs), len(sorries), len(pt), sum(1 for _n, ax in per if ax is not None),
              ' ; '.join('%s %s' % lp for lp in lem_points))]
    put_txt('b665_runner_%s.txt' % stage, L)
    j = jl('b665_runner_rows.json')
    rows_ = [r for r in (j.get('rows') or []) if r.get('stage') != stage] + [row]
    put_json('b665_runner_rows.json', dict(j, rows=rows_, kernel_files=[f for f, _b in kf]))
    lj = jl('b665_landings.json')
    lj[stage] = dict(run_id=run_id, ref=ref, rows=land_rows, lemmas=lem_points)
    put_json('b665_landings.json', lj)
    print(NL.join(L[-(len(land_rows) + len(lem_points) + 6):]))


def landings(*a):
    """the landing point of each lemma, one bank each ((R275)(4)): data/b665_keiper.txt and data/b665_transform_bound.txt, read from
    data/b665_landings.json through read_landing_row -- the exploratory tree's reading and the merge tree's beside it, the merge tree's the
    landing (the author's word: the stripped tree, dispatched once more, is the tree that merges)."""
    lj = jl('b665_landings.json')
    rr = jl('b665_runner_rows.json')
    runs = dict((r['stage'], r) for r in rr.get('rows') or [])
    out = {}
    for (lem, f, names), bank in zip(LEMMAS, (K.KEIPER_BANK, K.TB_BANK)):
        L = ['b665 -- COMPONENT 3, (R275)(4): THE LANDING POINT OF %s (%s)' % (lem.upper(), utc()), '',
             '### the statement: relay data/b665_keiper_statement.txt, section %s; the file %s on branch %s of %s' % (
                 '(I)' if 'Keiper' in lem else '(II)', f, K.BRANCH, K.KERNEL)]
        pts = {}
        for stage in ('explore', 'merge'):
            s = lj.get(stage) or {}
            r = runs.get(stage) or {}
            L += ['', '### STAGE %s -- run %s at %s (artifact sha256 %s, the platform`s digest agreeing; memory low %s MB; build exit 0 read in the '
                  'runner bank data/b665_runner_%s.txt):' % (stage.upper(), s.get('run_id'), (s.get('ref') or '')[:7], (r.get('artifact_sha256') or '### NONE')[:16],
                                                              r.get('mem_low'), stage)]
            for row in [x for x in s.get('rows') or [] if x['lemma'] == lem]:
                n, p, w = read_landing_row(row)
                L.append('  %-56s %-22s prints %s ; %s' % (n.rsplit('.', 1)[1], p, row['prints'], ('obstruction ' + w) if p != 'DERIVES' else
                                                           'decl %s :%s' % (row['file'], row['decl_line'])))
            pts[stage] = dict(s.get('lemmas') or []).get(lem)
        L += ['', '### ### **%s : EXPLORE %s ; MERGE %s -- THE LANDING POINT: %s.**' % (lem.upper(), pts.get('explore'), pts.get('merge'), pts.get('merge'))]
        if pts.get('merge') != 'DERIVES':
            L.append('### the obstruction, the next lemma of substance, by file and line: see the rows above; the branch unmerged.')
        put_txt(bank, L)
        out[lem] = pts.get('merge')
        print(L[-1])
    return out


def attempt(*a):
    """`attempt <explore sha> <merge sha>`: data/b665_attempt.json -- the branch's two tree states (the exploratory tree in the fallback form,
    the stripped merge tree), each commit's files, the branch tip at the remote as the push read it; the files the act wrote on the kernel
    (file_list), read by kernel_files()."""
    ex, mg = a[0], a[1]
    fl = lambda c: sorted(x for x in g(K.KD, 'show', '--name-only', '--format=', c).split(NL) if x.strip())   # noqa: E731
    files = sorted(set(fl(ex)) | set(fl(mg)))
    src = dict((f, _show(K.KD, mg, f) or '') for f in files if f.endswith('.lean'))
    j = dict(at=utc(), branch=K.BRANCH, base=K.K_MAIN, explore=dict(sha=ex, files=fl(ex)), merge=dict(sha=mg, files=fl(mg)),
             file_list=files, sorry_in_merge_tree=dict((f, len(re.findall(r'\bsorry\b', s))) for f, s in src.items()),
             parent_of_merge=g(K.KD, 'rev-parse', mg + '^').strip())
    put_json(K.ATTEMPT_BANK, j)
    print('  explore %s %s ; merge %s %s ; parent of merge %s ; sorry in the merge tree %s' % (ex[:7], fl(ex), mg[:7], fl(mg), j['parent_of_merge'][:7],
                                                                                      j['sorry_in_merge_tree']))


# ================================================================================ COMPONENT 4: H3, THE CONTROL ON THE STATEMENT'S BINDING
def _keiper_rhs(prec, N=12):
    """the compiled right side, keiperSum n = SUM_{k <= n} C(n + 1, k + 1) keiperA k for n = 0..N-1, in arb at `prec` bits:
    keiperA k = (-1)^k + zetaLogCoeff k + gammaRLogCoeff k, each the Taylor coefficient at s = 1 its kernel name says --
    zetaLogCoeff from (s - 1) ζ(s) = 1 + SUM_m (-1)^m γ_m / m! (s - 1)^(m+1) (arb's Stieltjes constants), its logarithmic derivative's
    series by exact series division in balls; gammaRLogCoeff from logDeriv Γℝ(s) = -½ log π + ½ ψ(s/2), the k-th coefficient
    ψ^(k)(1/2) / (2 k! 2^k) (arb's polygamma), plus -½ log π at k = 0."""
    from flint import acb, ctx
    from math import comb, factorial
    old = ctx.prec
    ctx.prec = prec
    try:
        M = N + 2
        F = [acb(1)] + [acb(-1) ** m * acb.stieltjes(m) / factorial(m) for m in range(M)]
        dF = [F[i + 1] * (i + 1) for i in range(M)]
        Q = []
        for k in range(N):
            s = dF[k] - sum((F[k - i] * Q[i] for i in range(k)), acb(0))
            Q.append(s / F[0])
        lp = acb.pi().log()
        G = [(-lp / 2 if k == 0 else acb(0)) + acb(0.5).polygamma(k) / (2 * factorial(k) * acb(2) ** k) for k in range(N)]
        A = [acb(-1) ** k + Q[k] + G[k] for k in range(N)]
        out = []
        for n in range(N):
            v = sum((comb(n + 1, k + 1) * A[k] for k in range(n + 1)), acb(0))
            out.append((v.real.mid(), v.real.rad(), v.imag.abs_upper(), v.real.str(40, radius=True)))
        return out
    finally:
        ctx.prec = old


def control(*a):
    """H3 ((R275)(4), the author's word): where the Keiper equality lands DERIVES, keiperSum n for n = 0..11 (λ_1..λ_12) recomputed from the
    compiled statement's right side in arb at 200 bits, the 400-bit rung taken where a comparison does not decide at 200; compared per n with
    b589's KEIPER column within its floor plus the ball radius plus the banked decimal's own half-unit (the bank holds the 70-digit run rounded
    to its printed digits -- a reading, declared), and with its ZERO column within that column's floor. A KEIPER disagreement refutes H3 (the
    binding); a ZERO disagreement alone is a datum about b589's bench. Banked as data/b665_keiper_control.txt (.json)."""
    from decimal import Decimal
    from flint import arb
    lj = jl('b665_landings.json')
    kp = dict((jl('b665_landings.json').get('merge') or {}).get('lemmas') or []).get('the Keiper finite-n equality')
    if kp != 'DERIVES':
        sys.exit('### THE KEIPER EQUALITY DID NOT LAND DERIVES (%s) -- H3 NOT RUN, NOTHING WRITTEN' % kp)
    bench = jl('b589_three_way.json').get('rows') or []
    if len(bench) != 12:
        sys.exit('### b589`s bench rows read: %d, not 12 -- NOTHING WRITTEN' % len(bench))

    def half_unit(s):
        d = Decimal(s)
        return Decimal(1).scaleb(d.as_tuple().exponent) / 2

    def compare(prec):
        from flint import ctx
        R = _keiper_rhs(prec)
        rows = []
        # ### the comparisons at the control's own precision (b665's defect (c): _keiper_rhs restores the context's precision on return, and
        # ### the first run compared at 53 bits)
        old = ctx.prec
        ctx.prec = prec
        try:
            return _rows(R, rows)
        finally:
            ctx.prec = old

    def _rows(R, rows):
        for (mid, rad, im, txt), b in zip(R, bench):
            kv = arb(b['keiper'])
            hu = arb(str(half_unit(b['keiper'])))
            tol_k = arb(b['floor_k']) + rad + hu
            dk = abs(mid - kv)
            dz = abs(mid - arb(repr(b['zero'])))
            tol_z = arb(b['floor_z']) + rad
            okk = bool(dk <= tol_k) if (dk <= tol_k or dk > tol_k) else None
            okz = bool(dz <= tol_z) if (dz <= tol_z or dz > tol_z) else None
            rows.append(dict(n=b['n'], value=txt, rad=rad.str(3), im_upper=im.str(3), keiper=b['keiper'], d_keiper=dk.str(3),
                             tol_keiper=tol_k.str(3), half_unit=str(half_unit(b['keiper'])), agree_keiper=okk, zero=b['zero'], d_zero=dz.str(3),
                             tol_zero=tol_z.str(3), agree_zero=okz))
        return rows
    rows, prec = compare(200), 200
    if any(r['agree_keiper'] is None or r['agree_zero'] is None for r in rows):
        rows, prec = compare(400), 400
    L = ['b665 -- COMPONENT 4, (R275)(4) H3: THE COMPILED FACE AGAINST THE NUMERICAL ONE, A CONTROL ON THE STATEMENT`S BINDING, NOT ON THE THEOREM (%s)' % utc(),
         '',
         '### the statement: liCoeff_succ_eq_keiperSum n : LiCoeff (n + 1) = (keiperSum n).re, DERIVES at the standard three (relay data/b665_keiper.txt,',
         '### run %s at %s). The right side recomputed from its kernel names in arb (python-flint): zetaLogCoeff from arb`s Stieltjes constants through' % (
             (lj.get('merge') or {}).get('run_id'), ((lj.get('merge') or {}).get('ref') or '')[:7]),
         '### the series log-derivative of (s - 1) ζ(s); gammaRLogCoeff from ½(ψ(s/2) - log π) through arb`s polygamma at 1/2; at %d bits%s.' % (
             prec, ' (the 400-bit rung taken: a comparison did not decide at 200)' if prec == 400 else ' (the 400-bit rung not needed: every comparison decided)'),
         '### b589`s bench (relay data/b589_three_way.json, rows n = 1..12; the text bank :7-:18): KEIPER at 70 digits banked as a decimal of 31 significant',
         '### digits, floor 1e-45; ZERO (Lambda_N + T2) with its floor. THE READING, DECLARED: the KEIPER tolerance is the floor plus the ball radius',
         '### plus the banked decimal`s own half-unit in its last place, since the bank holds the run rounded to its printed digits.',
         '### Rows are n: λ_n here (ball) | KEIPER banked | |difference| | tolerance | agree | ZERO banked | |difference| | its floor + radius | agree.', '']
    for r in rows:
        L.append('  n=%-3d %s ; |Im| <= %s' % (r['n'], r['value'], r['im_upper']))
        L.append('        KEIPER %s ; |d| %s ; tol %s (half-unit %s) ; %s' % (r['keiper'], r['d_keiper'], r['tol_keiper'], r['half_unit'],
                                                                           'AGREE' if r['agree_keiper'] else '### DISAGREE'))
        L.append('        ZERO   %r ; |d| %s ; tol %s ; %s' % (r['zero'], r['d_zero'], r['tol_zero'], 'AGREE' if r['agree_zero'] else 'differs (a datum)'))
    nk = sum(1 for r in rows if r['agree_keiper'])
    nz = sum(1 for r in rows if r['agree_zero'])
    # ### THE CONTROLS ON THE COMPARISON ITSELF (a pass is evidence only when the same comparison refuses a wrong binding): (i) λ_n from a wrong
    # ### binding -- keiperSum with gammaRLogCoeff dropped at every k (its first form dropped only k >= 1 and could not fire at n = 1, where
    # ### keiperSum 0 has no such term); (ii) the right side shifted by 1e-28, twenty half-units.
    from flint import ctx as _ctx
    from math import comb as _comb
    _old = _ctx.prec
    _ctx.prec = prec
    try:
        R = _keiper_rhs(prec)
        from flint import acb as _acb
        from math import factorial as _fac
        lp = _acb.pi().log()
        G1 = [(-lp / 2 if k == 0 else _acb(0)) + _acb(0.5).polygamma(k) / (2 * _fac(k) * _acb(2) ** k) for k in range(12)]
        wrong = [R[n][0] - arb(sum((_comb(n + 1, k + 1) * G1[k].real for k in range(0, n + 1)), arb(0))) for n in range(12)]
        c1 = sum(1 for n, b in enumerate(bench) if not (abs(wrong[n] - arb(b['keiper'])) <= arb(b['floor_k']) + R[n][1] + arb(str(half_unit(b['keiper'])))))
        c2 = sum(1 for n, b in enumerate(bench) if not (abs(R[n][0] + arb('1e-28') - arb(b['keiper'])) <= arb(b['floor_k']) + R[n][1] + arb(str(half_unit(b['keiper'])))))
    finally:
        _ctx.prec = _old
    L += ['', '### THE CONTROLS ON THE COMPARISON: (i) a wrong binding (gammaRLogCoeff dropped at every k) DISAGREES WITH KEIPER AT %d OF 12 n ; '
          '(ii) the right side shifted by 1e-28 DISAGREES AT %d OF 12 n -- each must refuse at 12 for the comparison to have teeth: %s.' % (
              c1, c2, 'IT HAS' if c1 == 12 and c2 == 12 else '### IT DOES NOT')]
    L += ['', '### ### **H3 %s -- KEIPER AGREES AT %d OF 12 n ; ZERO AGREES AT %d OF 12 n (printed beside, refuting nothing) ; PRECISION %d BITS.**' % (
        'HELD' if nk == 12 else 'REFUTED', nk, nz, prec)]
    put_txt(K.CONTROL_BANK, L)
    put_json(K.CONTROL_BANK.replace('.txt', '.json'), dict(at=utc(), prec=prec, rows=rows, keiper_agree=nk, zero_agree=nz, held=(nk == 12)))
    print(NL.join(L[-14:]))


DH = ('*Appended 2026-10-13 by b665 beneath the transform-bound order (:14162, named there W-ORD-FT-FIRST-ORDER), under `(R275)`(4) -- '
      'W-ORD-FT-FIRST-ORDER DISCHARGED:*')


def _discharge():
    tb = rdn(K.TB_BANK)
    if 'THE LANDING POINT: DERIVES' not in tb:
        sys.exit('### THE TRANSFORM BOUND DID NOT LAND DERIVES -- THE ORDER IS NOT DISCHARGED, NOTHING WRITTEN')
    lj = jl('b665_landings.json').get('merge') or {}
    return ('\n' + DH + ' the order’s item -- for the plateau base g0 = plateau (1/2) ℓ and z ≠ 0, ‖paperFT (phiC g0) z‖ ≤ 2 e^{ℓ |Im z|} / ‖z‖ -- is '
            'SIDE-explicit-formula’s paperFT_plateau_first_order, ‖paperFT (phiC (plateau F L)) z‖ · ‖z‖ ≤ 2 e^{L |Im z|} at every ramp fraction F '
            'and half-width L, with plateau_deriv_abs_integral (∫ |plateau′| = 2) and offScore_plateau_first_order (b663’s B1 at strip points), '
            'SIDEExplicitFormula/FirstOrderBound.lean, each DERIVES at the standard three on the hosted runner (run %s at %s; relay '
            'data/b665_transform_bound.txt). b663’s hθ line re-read “certified on the kernel lemma” in a dated line beneath relay '
            'data/b663_epstein_control.txt; the READ caveat on b663’s negative control falls; the banked-not-ball-certified caveat stands until '
            'W-ORD-EPSTEIN-CERTIFY (b667).\n' % (lj.get('run_id'), (lj.get('ref') or '')[:7]))


def c4(*a):
    land([('OPEN_TRAILS.md', DH, _discharge())], 'b665_discharge_line.json', 'c4', entry=K.FT_LINE,
         check=[('OPEN_TRAILS.md', K.FT_LINE, 'W-ORD-FT-FIRST-ORDER')], dry='dry' in a)


def merged(*a):
    """`merged <merge sha> <tag>`: the merge stage's row carries the merge and its tag, after main and the tag are read back at the remote by
    push_gated.sh (its capture data/b665_merge_push_out.txt); the merge's parents, the merged tree against the built tree, the tag's peel and
    the sorry count of the act's kernel files at main, read here; banked as data/b665_merge.txt and into data/b665_runner_rows.json."""
    sha, tag = a[:2]
    j = jl('b665_runner_rows.json')
    built = None
    for r in j['rows']:
        if r['stage'] == 'merge':
            r['merged'], r['tag'] = sha, tag
            built = r['ref']
    parents = g(K.KD, 'log', '-1', '--format=%P', sha).split()
    t_main, t_built = g(K.KD, 'rev-parse', sha + '^{tree}').strip(), g(K.KD, 'rev-parse', (built or '') + '^{tree}').strip()
    peel = g(K.KD, 'rev-parse', '%s^{commit}' % tag).strip()
    kf = read_kernel_files()
    sorry_main = dict((f, len(re.findall(r'\bsorry\b', _show(K.KD, sha, f) or ''))) for f, _b in kf)
    cap = rdn('b665_merge_push_out.txt')
    j['merge'] = dict(sha=sha, parents=parents, tree_equal=(t_main == t_built and bool(t_main)), tag=tag, tag_peeled=peel, sorry_main=sorry_main,
                      push_done='DONE -- main and 1 tag(s) pushed and read back' in cap)
    put_json('b665_runner_rows.json', j)
    L = ['b665 -- COMPONENT 5, (R275)(4)-(5): THE MERGE (%s)' % utc(), '',
         '### %s main %s, parents %s (the kernel`s main before the act %s; the merge tree %s), merged alone' % (K.KERNEL, sha[:7], ' '.join(p[:7] for p in parents),
                                                                                                         K.K_MAIN, (built or '')[:7]),
         '### the merged tree against the built tree (run 38452047820): %s' % ('EQUAL' if j['merge']['tree_equal'] else '### NOT EQUAL'),
         '### the tag %s, made by push_gated.sh at the read-back, peeled %s ; the capture: %s' % (tag, peel[:7], 'DONE, main and the tag read back'
                                                                                               if j['merge']['push_done'] else '### NOT DONE'),
         '### sorry in the act`s kernel files at main: %s' % sorry_main,
         '### ### **MERGED %s ; TAG %s PEELED %s ; MERGED TREE = BUILT TREE %s ; SORRY ON MAIN %d.**' % (sha[:7], tag, peel[:7], j['merge']['tree_equal'],
                                                                                                     sum(sorry_main.values()))]
    put_txt('b665_merge.txt', L)
    print(L[-1])


# ================================================================================ THE LATE ROUTES (b664's, carried; every row read through READERS)
import collections                 # noqa: E402
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call (the hosted runner's)."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    L = ['b665 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d.**' % (len(rows), len(hits), len(lean))]
    put_txt('b665_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b665_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])


def kernels(*a):
    import b641_record as R41
    put_json('b665_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


DEFECT_ROW = re.compile(r'^    \(([a-z])\) ')


def _defect_short():
    out = []
    for l in rdn('b665_defects.txt').split(NL):
        m = re.match(r'^    \(([a-z])\) ([^.]*)\.', l)
        if m:
            out.append(m.group(0).strip()[:-1])
    return out


def defects(*a):
    t = rdn('b665_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b665_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b665_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b665_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')
# ### the prior bank this act appended to by ruling ((R275)(4): the dated line beneath b663's control), named by this root so it is a shared
# ### additive file from here (tools/additive_shared.py: a path named by more than one root)
ROOT_SHARED = ('data/b663_epstein_control.txt',)


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b665_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)]
                  + list(ROOT_SHARED))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b665_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b665'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b665_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    with tempfile.TemporaryDirectory(prefix='b665_ra_') as tmp:
        cp = os.path.join(tmp, os.path.basename(bank_))
        b = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b[0] ^= 0x01
        open(cp, 'wb').write(bytes(b))
        items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    late = []
    for it in J['items']:
        p = it.split()
        if p[0].startswith('data/'):
            fp = os.path.join(ROOT, *p[0].split('/'))
            if not os.path.exists(fp) or AR.sha256_file(fp) != p[1]:
                late.append('%s changed' % p[0])
            elif os.path.getmtime(fp) > J.get('at_epoch', 0) + AR.ORDER_SLACK:
                late.append('%s written after the root' % p[0])
    L = ['b665 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b665_root_arm.txt', L)
    put_json('b665_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    before = _rows_state(json.loads(_show(RELAY, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b665 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b665_table_final.txt', L)
    put_json('b665_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


def gatebanks(*a):
    """the gate's steps between the face and the lock (b664's order), each tool's output banked by this route, never by a shell redirect."""
    import gate_hash as G
    env = dict(os.environ, PYTHONIOENCODING='utf-8')

    def runb(args, out):
        r = subprocess.run([sys.executable] + args, capture_output=True, cwd=ROOT, env=env)
        b = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            open(p + '.tmp', 'wb').write(b)
            os.replace(p + '.tmp', p)
        return r.returncode, b.decode('utf-8', 'replace')
    face_rel = 'data/b665_registration_2026-10-13.txt'
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', face_rel], 'b665_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b665_regspec.py')], 'b665_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b665_satisfiable.json', '--emit', 'b665'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b665_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b665_census_stepzero.txt'), ('b327_faces_census.py', 'b665_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b665_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b665'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    fa = os.path.join(ROOT, *face_rel.split('/'))
    for r in ('data/b665_reg_gate.txt', 'data/b665_reg_termscan.txt', 'data/b665_regspec_run.txt', 'data/audit_b665_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, fa)[:16], G.matches(ra, fa)[0]))


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
HK = ('H1', 'H2', 'H3')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + HK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b664_closing_push_out.txt', 'b663_epstein_control.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
FACE = os.path.join(D, 'b665_registration_2026-10-13.txt')


def TRAIL_HEAD():
    return ('### b665 — lane two, act ninety-two, the research act under (R275): b664 at its weight; the Keiper finite-n equality and the '
            'transform bound stated in one bank, attempted on the runner, landed each on its own reading')


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime((s or '')[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


def _calls():
    return jl('b665_author_answers.json').get('calls') or []


def _ct_first(repo, pre, prefix=None):
    """the commit time of the first commit in `repo` after `pre` (whose subject opens with `prefix`, if given)."""
    for l in g(repo, 'log', '--reverse', '--format=%ct %s', pre + '..HEAD' if repo == RELAY else pre + '..main').split(NL):
        if l.strip() and (prefix is None or l.split(' ', 1)[1].startswith(prefix)):
            return int(l.split(' ', 1)[0])
    return None


def _first_kernel_ct():
    """the first kernel byte of the act: the first commit on the branch or on the kernel's main after K_MAIN."""
    ts = []
    for ref in (K.BRANCH, 'main'):
        for l in g(K.KD, 'log', '--reverse', '--format=%ct', '%s..%s' % (K.K_MAIN, ref)).split(NL):
            if l.strip():
                ts.append(int(l))
                break
    return min(ts) if ts else None


def _n2():
    sj = jl(K.STATEMENT_BANK + '.json')
    st_ct = _ct_first(RELAY, K.PRE_RELAY, 'b665 Component 2')
    aj = _calls()
    ans = _iso(aj[0].get('result_ts')) if aj else None
    kct = _first_kernel_ct()
    traced = (sj.get('trace_keiper') or []) + (sj.get('trace_bound') or [])
    missing = [t for t, w, _x in traced if not w]
    st = rdn(K.STATEMENT_BANK + '.txt')
    printed = 'THE SEARCH FOR HIGHER STIELTJES CONSTANTS IN MATHLIB AT' in st and sj.get('stieltjes_hits', 0) > 0
    ok = bool(traced) and not missing and printed and st_ct and kct and st_ct < kct and ans and ans < kct
    return ('HELD' if ok else 'REFUTED'), (
        'every term of both statements traced in relay data/b665_keiper_statement.txt: %d traced, not found %s; the Mathlib search for Stieltjes '
        'constants printed there (%d hits at %s, %d constants by name); the bank committed at %s, the author`s word at %s, the first kernel byte '
        'on the branch at %s' % (len(traced), missing or 'NONE', sj.get('stieltjes_hits', 0), sj.get('mathlib', '?'), len(sj.get('stieltjes_residue') or []),
                                 time.strftime('%H:%M:%SZ', time.gmtime(st_ct)) if st_ct else '?', time.strftime('%H:%M:%SZ', time.gmtime(ans)) if ans else '?',
                                 time.strftime('%H:%M:%SZ', time.gmtime(kct)) if kct else '?'))


def _lemma_points(stage='merge'):
    lj = jl('b665_landings.json').get(stage) or {}
    return dict(lj.get('lemmas') or [])


def _n3():
    pts = _lemma_points()
    mj = jl('b665_runner_rows.json').get('merge') or {}
    banks = [rdn(K.KEIPER_BANK), rdn(K.TB_BANK)]
    one = all(b.count('THE LANDING POINT: ') == 1 for b in banks)
    open_ = [k for k, v in pts.items() if v != 'DERIVES']
    rows = (jl('b665_landings.json').get('merge') or {}).get('rows') or []
    for r in rows:
        read_landing_row(r)
    ok = len(pts) == 2 and one and sum((mj.get('sorry_main') or {1: 1}).values()) == 0 and (not open_ or not mj.get('sha')) \
        and all(r['point'] == 'DERIVES' or r['obstruction'] for r in rows)
    return ('HELD' if ok else 'REFUTED'), (
        'each lemma one landing point, banked with the runner`s gate reading (relay data/b665_keiper.txt, data/b665_transform_bound.txt): %s; '
        'open lemmas %s, so no split was needed; sorry on main %s; the merged tree the built tree %s' % (
            '; '.join('%s %s' % kv for kv in pts.items()), open_ or 'NONE', mj.get('sorry_main'), mj.get('tree_equal')))


def _n4():
    pts = _lemma_points()
    ct = rdn(K.B663_CONTROL)
    dated = '### DATED LINE, 2026-10-13, b665 under (R275)(4)' in ct and 're-read "certified on the kernel lemma"' in ct
    pre = _show(RELAY, K.PRE_RELAY, 'data/' + K.B663_CONTROL) or ''
    prefix = bool(pre) and ct.startswith(pre)
    dl = jl('b665_discharge_line.json')
    ln = ((dl.get('lines') or [{}])[0]).get('line')
    otl = rd(OT).split(NL)
    disc = bool(ln) and 'W-ORD-FT-FIRST-ORDER DISCHARGED' in otl[ln - 1] if ln and ln <= len(otl) else False
    if pts.get('the transform bound') != 'DERIVES':
        return 'HELD VACUOUS', 'the transform bound did not land DERIVES; nothing to re-read'
    ok = dated and prefix and disc
    return ('HELD' if ok else 'REFUTED'), (
        'the transform bound DERIVES: the b663 hθ line re-read on the kernel lemma in a dated line beneath relay data/b663_epstein_control.txt '
        '(%s; the bank before the act its prefix %s); the order read DISCHARGED at OPEN_TRAILS :%s (%s)' % (
            'present' if dated else '### ABSENT', prefix, ln, disc))


def _n5():
    face = jl('b665_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b665_|audit_b665_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    km = [l for l in g(K.KD, 'log', '--first-parent', '--format=%h %p', K.K_MAIN + '..main').split(NL) if l.strip()]
    km_ok = [l.split()[0] for l in km] == [K.MERGE] and len(km[0].split()) == 3
    k_files = sorted(x for x in g(K.KD, 'diff', '--name-only', K.K_MAIN, 'main').split(NL) if x.strip())
    want_k = sorted(['print_targets.txt'] + [f for f, _b in read_kernel_files()])
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b665_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ok = others_ok and not pp_beyond and not kinds_beyond and not differ and km_ok and not new_arms and k_files == want_k
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); %s`s main written by the merge under Component 5 alone '
            '(first-parent commits since %s: %s ; %s), its files against %s: %s (the kernel files read from the act`s banks and print_targets.txt); '
            'every kernel as the face read it %s; standing arms added: %s (the act`s arms over its own banks %d); sealed tools not agreeing %s; '
            'PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; relay files of a kind beyond the banks, the tools, the root list, b664`s push-out '
            'bank and the dated line beneath b663`s control: %s; no identifier of the author in any outbound request (git pushes, remote reads, '
            'the runner`s two dispatches with a ref and a target, the artifacts` downloads)' % (
                K.DRAFT, K.KERNEL, K.K_MAIN, [l.split()[0] for l in km], 'AS RULED' if km_ok else '### OTHERWISE', K.K_MAIN, k_files, others_ok,
                new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE'))


ALLOWED_HYP = {'0 < F', 'F < 1', '0 < L', '0 ≤ ρ.re', 'ρ.re ≤ 1'}


def _hyps(src, name):
    """the binders of a theorem's statement at main, its hypotheses (named binders whose type is a Prop) read from the source text."""
    m = re.search(r'^theorem %s\b(.*?):=' % re.escape(name), src, re.M | re.S)
    if not m:
        return None
    sig = m.group(1)
    return [t.strip() for _n, t in re.findall(r'\((h\w*) : ([^)]*)\)', sig)]


def _h1():
    sj = jl(K.STATEMENT_BANK + '.json')
    tk = sj.get('trace_keiper') or []
    miss = [t for t, w, _x in tk if not w]
    pts = _lemma_points()
    ok = bool(tk) and not miss and sj.get('mathlib') == K.MATHLIB_PIN and pts.get('the Keiper finite-n equality') == 'DERIVES'
    return ('HELD' if ok else 'REFUTED'), (
        'every term of the Keiper statement traced to a Mathlib name at %s or a named definition: %d traced, not found %s (relay '
        'data/b665_keiper_statement.txt, section (I)); the Stieltjes constants the kernel`s named stieltjes, needed by no term of (K-b)' % (
            sj.get('mathlib', '?'), len(tk), miss or 'NONE'))


def _h2():
    src = _show(K.KD, 'main', 'SIDEExplicitFormula/FirstOrderBound.lean') or ''
    hs = dict((n, _hyps(src, n)) for n in ('plateau_deriv_abs_integral', 'paperFT_plateau_first_order', 'offScore_plateau_first_order'))
    beyond = dict((n, [h for h in (v or []) if h not in ALLOWED_HYP]) for n, v in hs.items())
    sj = jl(K.STATEMENT_BANK + '.json')
    base = [w for t, w, _x in sj.get('trace_bound') or [] if 'baseWidth_pos' in t]
    ok = all(v is not None for v in hs.values()) and not any(beyond.values()) and bool(base and base[0])
    return ('HELD' if ok else 'REFUTED'), (
        'the transform bound`s hypotheses at main, per statement: %s; beyond the plateau`s parameter ranges and the strip: %s; the detector`s base '
        'meets them by the compiled half_pos`, half_lt_one` and baseWidth_pos (%s), every configuration point by ZeroConfig.strip' % (
            '; '.join('%s %s' % (n, v) for n, v in hs.items()), dict((n, v) for n, v in beyond.items() if v) or 'NONE', base[0] if base else '?'))


def _h3():
    cj = jl(K.CONTROL_BANK.replace('.txt', '.json'))
    ct = rdn(K.CONTROL_BANK)
    teeth = 'IT HAS.' in ct
    if _lemma_points().get('the Keiper finite-n equality') != 'DERIVES':
        return 'HELD VACUOUS', 'the Keiper equality did not land DERIVES; H3 not run'
    ok = bool(cj) and cj.get('held') and cj.get('keiper_agree') == 12 and teeth
    return ('HELD' if ok else 'REFUTED'), (
        'λ_1..λ_12 recomputed from the compiled right side in arb at %s bits: KEIPER agrees at %s of 12 n within its floor, the ball radius and '
        'the banked decimal`s half-unit; ZERO at %s of 12 within its floor (a datum); the comparison`s two planted controls refusing at 12 of 12: '
        '%s (relay data/b665_keiper_control.txt) -- a control on the statement`s binding, not on the theorem' % (
            cj.get('prec'), cj.get('keiper_agree'), cj.get('zero_agree'), teeth))


def scores(*a):
    TF, RA = jl('b665_table_final.json'), jl('b665_root_arm.json')
    _r, _n, sh = seal_hashes()
    cm = jl('b665_commands.json')
    print('  the kernel files, read from the act`s banks: %s' % read_kernel_files())
    S = {
        'N1': (('HELD' if cm and not cm.get('local_lean') else 'REFUTED'),
               'commands of this act that run lean or lake on this host: %s (relay data/b665_commands.txt); the build on the hosted runner alone' % (
                   cm.get('local_lean') if cm else '### UNREAD')),
        'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(), 'H1': _h1(), 'H2': _h2(), 'H3': _h3(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    put_json('b665_scores.json', dict((k2, list(v)) for k2, v in S.items()))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))


NEXT_LINE = 'b666, per `(R275)`(6), the re-cut act on the next kernel by count under `(R265)`’s form; b667 W-ORD-EPSTEIN-CERTIFY'


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'


def _title():
    pts = _lemma_points()
    tb = pts.get('the transform bound')
    mj = jl('b665_runner_rows.json').get('merge') or {}
    return ('## The Keiper finite-n equality %s; the transform bound %s, b663’s READ caveat %s; %s' % (
        pts.get('the Keiper finite-n equality', 'unread'), tb or 'unread', 'fallen' if tb == 'DERIVES' else 'standing', mj.get('tag') or K.NEXT_TAG))


def _finding_text():
    S, rl, J = jl('b665_scores.json'), jl('b665_record_lines.json'), jl('b665_act_root.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b665_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}]
    rows = jl('b665_runner_rows.json')
    rr = dict((r['stage'], r) for r in rows.get('rows') or [])
    mj = rows.get('merge') or {}
    cc = re.search(r'CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    sj = jl(K.STATEMENT_BANK + '.json')
    cj = jl(K.CONTROL_BANK.replace('.txt', '.json'))
    dl = ((jl('b665_discharge_line.json').get('lines') or [{}])[0]).get('line')
    ex, mg = rr.get('explore') or {}, rr.get('merge') or {}
    e = ['', _title(), '',
         '*Filed at b665 on the author’s ruling `(R275)` and the author’s word (%d questions in %d call). Banks: relay '
         '`data/b665_citation_check.txt`, `data/b665_keiper_statement.txt`, `data/b665_runner_explore.txt`, `data/b665_runner_merge.txt`, '
         '`data/b665_keiper.txt`, `data/b665_transform_bound.txt`, `data/b665_keiper_control.txt`, `data/b665_merge.txt`, `data/b665_act_root.txt`.*' % (
             n_ans, len(_calls())), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed.' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?'), '',
         '**The record line** (`(R275)`(1)): b664 at its weight beneath its entry (FINDINGS :%s).' % ls[0].get('line'), '',
         '**The statements** (`(R275)`(2)-(3)), drafted in one bank before any Lean, %d terms traced by file and line: the finite-n equality '
         'LiCoeff (n + 1) = Re keiperSum n in the kernel’s Taylor coefficients -- the bench’s η-form traced there as the same sum, the Stieltjes '
         'constants the kernel’s own definition by derivative, Mathlib naming none (%d hits at %s, none a Stieltjes constant); and b663’s B1 over '
         'the kernel’s plateau at every ramp fraction and half-width, its hypotheses the plateau’s parameter ranges and the strip. N2 %s; H1 %s; H2 %s.' % (
             len((sj.get('trace_keiper') or []) + (sj.get('trace_bound') or [])), sj.get('stieltjes_hits', 0), sj.get('mathlib', '?'),
             _sv(S, 'N2'), _sv(S, 'H1'), _sv(S, 'H2')), '',
         '**The attempt** (`(R275)`(4), on the author’s word): both lemmas on keiper-b665, five declarations; the exploratory tree, each proof '
         'step in a fallback form, run %s; every declaration compiled with no sorryAx, the fallbacks stripped, the stripped tree run %s -- the '
         'artifact’s sha256 agreeing with the platform’s digest each time, memory low %s and %s MB. The Keiper finite-n equality DERIVES; the '
         'transform bound DERIVES, all three statements at the standard three. N3 %s.' % (
             ex.get('run_id'), mg.get('run_id'), ex.get('mem_low'), mg.get('mem_low'), _sv(S, 'N3')), '',
         '**The control** (H3): λ_1..λ_12 recomputed from the compiled right side in arb at %s bits agree with b589’s Keiper column at %s of 12 n, '
         'within its floor, the ball radius and the banked decimal’s half-unit; the zero-sum column agrees at %s of 12 within its floor; the '
         'comparison refuses a wrong binding and a 1e-28 shift at every n. A control on the statement’s binding, not on the theorem. H3 %s.' % (
             cj.get('prec'), cj.get('keiper_agree'), cj.get('zero_agree'), _sv(S, 'H3')), '',
         '**The caveat**: b663’s hθ line above T = 150 re-read “certified on the kernel lemma” in a dated line beneath relay '
         '`data/b663_epstein_control.txt`; the READ caveat on b663’s negative control falls; W-ORD-FT-FIRST-ORDER DISCHARGED (OPEN_TRAILS :%s); '
         'the banked-not-ball-certified caveat stands until W-ORD-EPSTEIN-CERTIFY. N4 %s.' % (dl, _sv(S, 'N4')), '',
         '**The merge** (`(R275)`(5)): merged alone, SIDE-explicit-formula %s tagged %s, the merged tree the built tree, no sorry on main. N5 %s.' % (
             mj.get('sha', '?')[:7], mj.get('tag'), _sv(S, 'N5')), '',
         '**The root.** b665 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b601’s Keiper face and b642’s three identities, b589’s three-way '
         'bench and its pricing, and b663’s plan and control; it is re-read by b667’s certification and by the Keiper face’s next act, whose '
         'open part is K4 (the ζ-values of Γℝ’s coefficients). It strengthens the programme’s offering of statements a reader can check: the '
         'Li coefficient at every n is now equal, in a compiled statement, to Keiper’s finite sum in the kernel’s named coefficients, bound '
         'to the numerical bench to thirty digits; and the bound b663 took as read is a kernel lemma.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds, locates any zero, or gives the sign of any λ_n; the equality is between two '
         'expressions for the same coefficient, and the bound is a property of one window.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the stripped tree dispatched once more as the merge tree’s build, the ferry’s "one dispatch" read as one per tree state '
              '(the author’s word); (2) H3’s KEIPER tolerance carries the banked decimal’s half-unit, b589 having banked its 70-digit run '
              'rounded to 31 digits; (3) the bench’s η-form traced in the bank, not compiled; (4) the dated line beneath b663’s control makes '
              'that bank a file this root names, so it is additive from here; (5) the Stieltjes constants the kernel’s own definition by '
              'derivative, the ruling’s series definition not needed by any term')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b665_scores.json', 'b665_findings.json', 'b665_record_lines.json', 'b665_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b665_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}]
    dl = ((jl('b665_discharge_line.json').get('lines') or [{}])[0]).get('line')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R275) ratified.** (1) b664 at its weight. (2) The Keiper finite-n equality stated before any Lean. (3) The transform bound stated '
             'over the kernel’s window. (4) Both attempted on the runner, each landed on its own reading, H1-H3 scored. (5) No bench number in '
             'a keystone; the draft held at v5. (6) The act after: b666.', '',
             '**Entered:** FINDINGS.md:%s (b664’s weight), :%s (the entry); OPEN_TRAILS.md:%s (W-ORD-FT-FIRST-ORDER DISCHARGED); this record.' % (
                 ls[0].get('line'), fj.get('entry_line'), dl), '',
             '**Act root:** b665 `%s` (previous `%s`, b664’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d call (relay data/b665_author_answers.txt): the one prompt of `(R275)`(2)-(3), before '
             'any Lean; none after the root.' % (n_ans, len(_calls())), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b665_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b665_scores.json')
    L = ['=' * 104, 'b665 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b665_defects.txt').rstrip(NL).split(NL)
    put_txt('b665_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b665_scores.json', 'b665_findings.json', 'b665_trail.json', 'b665_record_lines.json', 'b665_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}]
    rows = jl('b665_runner_rows.json')
    rr = dict((r['stage'], r) for r in rows.get('rows') or [])
    mj = rows.get('merge') or {}
    dl = ((jl('b665_discharge_line.json').get('lines') or [{}])[0]).get('line')
    L = ['b665 -- THE COMPONENTS, BANKED UNDER (R275).', '',
         '### COMPONENT 0 : the citation check (data/b665_citation_check.txt), step zero (data/b665_ferry.txt, data/b665_stepzero.txt, '
         'data/b665_tests_stepzero.txt, data/b665_readfirst.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b664`s weight FINDINGS :%s' % ls[0].get('line'),
         '### COMPONENT 2 : the statements (data/b665_keiper_statement.txt), the one prompt (data/b665_author_answers.txt) ; N2 %s ; H1 %s ; H2 %s' % (
             S['N2'][0], S['H1'][0], S['H2'][0]),
         '### COMPONENT 3 : the attempt -- run %s (explore), run %s (merge) ; data/b665_keiper.txt, data/b665_transform_bound.txt ; N3 %s' % (
             (rr.get('explore') or {}).get('run_id'), (rr.get('merge') or {}).get('run_id'), S['N3'][0]),
         '### COMPONENT 4 : the control (data/b665_keiper_control.txt) ; the dated line beneath data/b663_epstein_control.txt ; the order DISCHARGED '
         'OPEN_TRAILS :%s ; H3 %s ; N4 %s' % (dl, S['H3'][0], S['N4'][0]),
         '### COMPONENT 5 : merged %s tag %s (data/b665_merge.txt) ; N5 %s' % ((mj.get('sha') or '')[:7], mj.get('tag'), S['N5'][0]),
         '### COMPONENT 6 : the dry-run step (data/b665_reg_gate.txt), the seal (data/b665_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 7 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s' % ((J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'),
                                                                                    S['N1'][0])]
    put_txt('b665_components.txt', L)
    print(NL.join(L[2:]))


def _land_one(path, head, e, bank, extra):
    if odd_lines(e):
        sys.exit('### ODD BACKTICKS -- NOTHING WRITTEN: %s' % odd_lines(e)[:3])
    guard_absent(path, head)
    r = append_to(path, e)
    ln = read_head(path, head)
    put_json(bank, dict(extra, line=ln, head=head, append=r))
    return ln


def findings(*a):
    t, e = _finding_text()
    e = conv(e)
    dry = 'dry' in a
    cells, fired = screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells)
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b665_findings.json', dict(title=t))
    j = jl('b665_findings.json')
    j['entry_line'] = ln
    put_json('b665_findings.json', j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = conv(_trail_text())
    dry = 'dry' in a
    cells, fired = screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells)
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b665_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written (B665_STANDIN) -- converted by conv and run through the screens their landing runs, the needles the face
    names read in each; prints DRY-RUN STEP : CLEAN and exits 0 only when both screens are quiet and every needle is found. Writes no bank."""
    face = rd(a[0] if a else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = conv(text)
        print('  %s (the screens):' % which)
        cells, fired = screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = _face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells and not fired and nd and not miss
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


ROUTES = {'c1': c1, 'answers': answers, 'statement': statement, 'runner': runner, 'landings': landings, 'attempt': attempt, 'control': control,
          'c4': c4, 'merged': merged, 'commands': commands, 'kernels': kernels, 'defects': defects, 'root': root, 'root_arm': root_arm,
          'table_final': table_final, 'gatebanks': gatebanks, 'scores': scores, 'desk': desk, 'components': components, 'findings': findings,
          'trail': trail, 'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b665_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
