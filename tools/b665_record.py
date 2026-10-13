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


ROUTES = {'c1': c1, 'answers': answers, 'statement': statement, 'runner': runner, 'landings': landings, 'attempt': attempt, 'control': control,
          'c4': c4, 'merged': merged}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b665_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
