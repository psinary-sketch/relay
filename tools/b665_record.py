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


ROUTES = {'c1': c1, 'answers': answers, 'statement': statement}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b665_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
