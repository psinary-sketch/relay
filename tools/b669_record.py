# -*- coding: utf-8 -*-
"""b669_record.py -- THE ACT'S RECORD TOOL, b669 under (R279).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b669's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### (R274)(4), standing: no constant here names a kernel file; the kernel files are read from the act's plan and landing banks through
### tools/b669_worklist.py's kernel_files(), the read printed.
### Carried by the Write tool from b668_record.py (the helpers, the landing, the readers, the answers) and b667_record.py (the research act's
### form); new here: the record repair of (R279)(6), the weight line of (R279)(1). Every python child is started as `python -X utf8`, no
### environment mapping passed. Routes: `python tools/b669_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
"""
import collections
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
import b669_worklist as K          # noqa: E402

STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)


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
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b669_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b669_findings.json': dict(entry_line=99999, title='stand-in'),
        'b669_trail.json': dict(line=99999),
        'b669_act_root.json': dict(root='0' * 64, previous='f716a8e4' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b669's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b669_scanfile_%s.md' % tag)
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
    """a row of data/b669_runner_rows.json -- every key of RUNNER_KEYS present (None where a step did not reach it); returns the row's reading
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
    """a scores row: key N1..N5 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text) -- the whole verdict, not its first
    word (b656's defect (e))."""
    if not re.match(r'^(N[1-5]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


LANDINGS = ('DERIVES', 'COMPILED, PROOF OPEN', 'NOT COMPILED')


def read_landing_row(r):
    """a row of data/b669_chi_li_landing.json: a declaration, its landing (one of LANDINGS) and, where open, its obstruction by file and line;
    returns (name, landing, obstruction); raises on a row of another shape."""
    if not isinstance(r, dict) or not r.get('name') or r.get('landing') not in LANDINGS:
        raise ValueError('landing row of another shape: %r' % (r,))
    ob = r.get('obstruction')
    if r['landing'] != 'DERIVES' and not (isinstance(ob, dict) and ob.get('file') and isinstance(ob.get('line'), int)):
        raise ValueError('an open landing without its obstruction by file and line: %r' % (r.get('name'),))
    return r['name'], r['landing'], ob


def read_kernel_files():
    """(R274)(4), standing: the act's kernel files as tools/b669_worklist.py's kernel_files() reads them from the plan and landing banks; returns
    [(file, [banks])]; raises when the read finds no file (no constant stands in for it)."""
    kf = K.kernel_files()
    if not kf or not all(isinstance(f, str) and f.endswith('.lean') and b for f, b in kf):
        raise LookupError('no kernel file read from the plan or landing bank')
    return kf


READERS = ['read_runner_row', 'read_score_row', 'read_head', 'read_landing_row', 'read_kernel_files']


# ================================================================================ STEP ZERO: THE RECORD REPAIR, (R279)(6)
RPH = ('*Appended 2026-10-14 by b669 to b668’s entry (:8677), under `(R279)`(6) -- THE N4 CELL’S POST-PUSH READING, ADDITIVE:*')


def _repair():
    sc = jl('b668_scores.json')
    n4 = (sc.get('N4') or ['?'])[0]
    pc = rdn('b668_checks_postpush.txt')
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) (\[[^\]]*\])', pc)
    if n4 != 'HELD' or not m:
        sys.exit('### THE SCORES BANK OR THE POST-PUSH SUITE DOES NOT READ AS THE RULING SAYS -- NOTHING WRITTEN (N4 %s)' % n4)
    return ('\n' + RPH + ' the entry’s scores line reads N4 PENDING, written before the suite ran at the close. Read after the post-push '
            'suite (relay data/b668_checks_postpush.txt: %s of %s arms passing, %s failing, %s -- the failure the face declared by name), N4 '
            'is %s: G-AXIOM-CLAIM at 0 contradictions before and after the merge, the suite failing no arm but the declared one (relay '
            'data/b668_scores.json, N4; data/b668_closing.txt). The entry is not edited; this line is additive.\n' % (
                m.group(2), m.group(1), m.group(3), m.group(4).replace("'", ''), n4))


def repair(*a):
    land([('FINDINGS.md', RPH, _repair())], 'b669_repair_lines.json', 'repair', entry=K.B668_ENTRY,
         check=[('FINDINGS.md', K.B668_ENTRY, '## SIDE-grh-transfer’s docstrings at 14')], dry='dry' in a)


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R279)(1)
WH = ('*Appended 2026-10-14 by b669 to b668’s entry (:8677), under `(R279)`(1) -- b668 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b668_closing.txt), ITS ONE DECLARED FAILURE NAMED:*')


def _weight():
    return ('\n' + WH + ' SIDE-grh-transfer -- six blocks into 57 sentence rows, 14 OVERREACHES cut in CharacterTopological.lean, GRHBridge.lean '
            'and Voice7Vendored.lean, one commit per file, each comment-stripped diff against main empty, no graded row standing; run '
            '38587853597 at the branch tip d487072, the artifact’s sha256 equal to the platform’s digest, 53 prints -- 21 equal to b555’s banked '
            'prints, 32 at the standard three or none -- the gate DERIVES; merged alone at 6e149db, tag v0.5.1 with the peeled SHA read back; '
            'G-AXIOM-CLAIM at 0 before and after; the commit 858cbf6 read from its diff as a SIDE-frobenius commit touching .gitignore and four '
            'logs and no .lean file, a census item at OPEN_TRAILS :14296; the ASCII chi/sigma cell item at :14298; the plan-form consumers section '
            'at :14290, the mid-act citation check at :14292 (its last print 4 of 4 OK), the research order at :14294, the trail at :14300; '
            'FINDINGS :8675 and :8677; relay bfc407e5, PLACE-papers f691545, root f716a8e4…; the suite 82 of 83 before and after the push with '
            'G-MERGES-ON-GATE declared by name -- the cut branch made from 858cbf6 before the workflow commit, the merged tree the built tree '
            'plus the workflow file, no .lean byte differing; five defects, (b) the navigator’s (two b670 items in the chat and in no bank); '
            'the entry’s N4 cell reading PENDING where the scores bank and the closing read HELD, repaired by an appended line at b669’s step '
            'zero; the mirror at mirror-refresh-2026-10-14-b668.zip CLEAN on three clauses. Nothing deposited.\n')


def c1(*a):
    land([('FINDINGS.md', WH, _weight())], 'b669_record_lines.json', 'c1', entry=K.B668_ENTRY,
         check=[('FINDINGS.md', K.B668_ENTRY, '## SIDE-grh-transfer’s docstrings at 14'), ('OPEN_TRAILS.md', K.B668_TRAIL, '### b668')],
         dry='dry' in a)


# ================================================================================ THE AUTHOR'S ANSWERS (b668's route, carried; BEGIN read with or
# ================================================================================ without a line break after it)
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
    """data/b669_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
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
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((i, c['id'], c['input'], o.get('timestamp')))
            if isinstance(c, dict) and c.get('type') == 'tool_result':
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')
                results[c.get('tool_use_id')] = (i, t, o.get('timestamp'))
                texts.append(t)
        for t in texts:
            # ### a word is a whole pasted text or a whole answer field ("question"="BEGIN ... END"), never BEGIN and END inside other prose
            for mm in re.finditer(r'(?s)(?:\A\s*|=")BEGIN\s*(.*?)\s*END(?=\s*\Z|")', t or ''):
                if K.ANCHOR not in mm.group(1) and 'RULING (' not in mm.group(1)[:20]:
                    words.append((i, mm.group(1)))
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
    head = ['### b669 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b669_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b669_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 2: THE PLAN, (R279)(3), IN THE b663 FORM WITH (R278)(3)'S
# ================================================================================ CONSUMERS SECTION
KREV = 'v0.30'
SEARCHES = [
    # ### (where, label, pattern, paths) -- each run as `git grep -n -i -E <pattern> <rev> -- <paths>`, its yield printed
    ('kernel', 'a configuration-level Li coefficient', r'^(noncomputable )?def [A-Za-z_]*(li_?coeff|licoeff)[A-Za-z_]*\b', ('SIDEExplicitFormula', 'Zeta23')),
    ('kernel', 'a χ-Li declaration (a Li name and a chi name in one declaration name)', r'^(def|theorem) ([A-Za-z_]*li[_A-Z][A-Za-z_]*chi|[A-Za-z_]*chi[A-Za-z_]*_li_)[A-Za-z_]*\b', ('SIDEExplicitFormula', 'Zeta23')),
    ('kernel', 'a χ-seam declaration', r'^(def|structure|theorem) [A-Za-z_]*[Ss]eam[A-Za-z_]*', ('SIDEExplicitFormula/Chi',)),
    ('kernel', 'the generic summability over a configuration with a local count', r'^theorem (zero_sum_inv_sq_gen|EF_zero_sum_summable_gen)\b', ('Zeta23',)),
    ('kernel', 'a strict modulus lemma |1 - 1/ρ| > 1 off the line (V2)', r'^theorem [A-Za-z_]*(norm|abs)_one_sub_inv[A-Za-z_]*(gt|lt|ne)', ('SIDEExplicitFormula', 'Zeta23')),
    ('kernel', 'a power-sum lemma (V4)', r'(power.?sum|turan|turán)', ('SIDEExplicitFormula', 'Zeta23')),
    ('mathlib', 'a Turán-type power-sum inequality (V4)', r'(turan|turán)', ('Mathlib',)),
    ('mathlib', 'a power-sum inequality by name (V4)', r'^(theorem|lemma) [A-Za-z_]*(power_?sum|powerSum)[A-Za-z_]*\b', ('Mathlib',)),
    ('mathlib', 'a Pringsheim theorem (B, the Pringsheim step)', r'pringsheim', ('Mathlib',)),
    ('mathlib', 'a Hadamard factorization (B, the product)', r'(hadamard.?factori|canonical.?product|weierstrass.?(product|factori))', ('Mathlib',)),
    ('mathlib', 'a growth or order bound for the completed L-function (B)', r'completedLFunction[A-Za-z_]*(isBigO|bound|growth|order|le_exp|norm_le)', ('Mathlib',)),
    ('mathlib', 'a finite-order entire function notion (B)', r'(finite.?order|order.?of.?growth|EntireOfFiniteOrder)', ('Mathlib',)),
    ('mathlib', 'the completed L-function of a Dirichlet character', r'^@\[pp_nodot\] noncomputable def completedLFunction|^noncomputable def completedLFunction', ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean',)),
    ('mathlib', 'its differentiability (χ ≠ 1)', r'^lemma differentiable_completedLFunction\b', ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean',)),
    ('mathlib', 'its functional equation (primitive χ)', r'^theorem completedLFunction_one_sub\b', ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean',)),
    ('mathlib', 'L(1, χ) ≠ 0 (B, φ(0) ≠ 0)', r'^(theorem|lemma) LFunction_apply_one_ne_zero\b', ('Mathlib',)),
    ('mathlib', 'the geometric sum (V4, a Cesàro-mean proof)', r'^(theorem|lemma) geom_sum_eq\b', ('Mathlib',)),
    # ### the second shapes, tightened after the wide shapes' hits were read by hand (HAND READING below)
    ('mathlib', 'TIGHTENED: a Turán-type inequality on sums of powers', r'(turan|turán).*(power|sums? of powers|exponential sum)', ('Mathlib',)),
    ('mathlib', 'TIGHTENED: a Hadamard or Weierstrass factorization of an entire function', r'(hadamard|weierstrass).{0,40}(entire|genus|product of zeros|zeros of)', ('Mathlib',)),
    ('mathlib', 'TIGHTENED: an order-of-growth notion for entire functions', r'(order.?of.?growth|EntireOfFiniteOrder|growth.?order)', ('Mathlib',)),
]
HAND_READING = [
    '  HAND READING OF THE WIDE SHAPES (every file of each wide yield read by its path, the hits by their lines):',
    '    `(turan|turán)` -- 3 files, all Turán GRAPHS: Mathlib/Combinatorics/SimpleGraph/CompleteMultipartite.lean, .../Extremal/Turan.lean,',
    '      .../Extremal/TuranDensity.lean; no power-sum inequality.',
    '    `(hadamard.?factori|canonical.?product|weierstrass.?(product|factori))` -- 2 files: Mathlib/CategoryTheory/Limits/Sifted.lean (a',
    '      canonical product of categories) and Mathlib/RingTheory/PowerSeries/WeierstrassPreparation.lean (Weierstrass preparation for power',
    '      series); no factorization of an entire function. (Mathlib/Analysis/Complex/Hadamard.lean is the three-lines theorem.)',
    '    `power_sum` declarations -- 2, both cardinal arithmetic (Mathlib/SetTheory/Cardinal/Defs.lean :453, :464).',
    '    `(finite.?order|order.?of.?growth|EntireOfFiniteOrder)` -- finite ORDER in order theory, group elements, power series and probability',
    '      (Mathlib/Order/Interval/Finset 7 files, Mathlib/Order 6, Mathlib/GroupTheory 4, ...); the growth alternatives alone yield nothing.',
    '      A first tightened shape carried a `finiteOrder` alternative and yielded 550, every one `LocallyFiniteOrder` (an order-theory class);',
    '      the alternative is dropped, `order.?of.?growth`, `EntireOfFiniteOrder` and `growth.?order` each yield 0.',
    '    the χ-Li shape -- 13 kernel hits, every one a `line`, `lit` or `limit` name (Chi/FullLine.lean, Chi/VerticalLine.lean, Chi/Statement.lean,',
    '      Chi/Main.lean, Chi/FullLineAssembly.lean, Chi/ZeroSumLimit.lean); no χ-Li declaration.',
    '    the configuration-level Li coefficient shape -- 2 kernel hits, LiWeil.lean :243 LiCoeff (ζ) and Registers.lean :29 B321.liCoeff (ζ).',
]


def _search(where, pat, paths):
    if where == 'kernel':
        out = g(K.KD, 'grep', '-n', '-i', '-E', pat, KREV, '--', *paths)
        rows = [l[len(KREV) + 1:] for l in out.split(NL) if l.strip()]
    else:
        out = g(K.MATHLIB, 'grep', '-n', '-i', '-E', pat, 'HEAD', '--', *paths)
        rows = [l[len('HEAD') + 1:] for l in out.split(NL) if l.strip()]
    return rows


PLAN_KERNEL_FILES = ['SIDEExplicitFormula/Schema/LiCfg.lean', 'SIDEExplicitFormula/Chi/LiForward.lean', 'SIDEExplicitFormula/Schema/LiConverseCfg.lean']


def plan(*a):
    """(R279)(3): the census by search printed; the statements traced; the two routes priced, each missing fact's search printed; the
    consumers section; the preferred route named with its reason. data/b669_chi_li_plan.txt (.json). No Lean is written by this route."""
    mrev = g(K.MATHLIB, 'rev-parse', 'HEAD').strip()
    krev = g(K.KD, 'rev-parse', '--short=7', KREV + '^{commit}').strip()
    res = []
    for where, label, pat, paths in SEARCHES:
        rows = _search(where, pat, paths)
        res.append(dict(where=where, label=label, pattern=pat, paths=list(paths), hits=len(rows), first=rows[:4]))
    L = ['b669 -- COMPONENT 2, (R279)(3): THE PLAN -- THE LI COEFFICIENT OVER THE CONFIGURATION; THE FORWARD HALF AT χ; THE CONVERSE PRICED ON TWO '
         'ROUTES (%s)' % utc(), '',
         '### rows are statements and priced facts. The kernel: SIDE-explicit-formula at %s (= main, %s); Mathlib at %s (the kernel`s lake-manifest pin,'
         ' the package checkout read by git grep). No Lean is written before the author`s word; no lean runs on this host.' % (KREV, krev, mrev[:8]),
         '', '== 1. THE CENSUS AND THE SEARCHES, PRINTED (`git grep -n -i -E <pattern> <rev> -- <paths>`; yield, then the first hits)']
    for r in res:
        L.append('  %-7s %-78s yield %3d   pattern %r over %s' % (r['where'], r['label'][:78], r['hits'], r['pattern'], ', '.join(r['paths'])))
        L += ['            %s' % x[:170] for x in r['first']]
    L += [''] + HAND_READING + ['',
          '### THE CENSUS READ (the searches above and the read-first, relay data/b669_readfirst.txt):',
          '  C1 LiCoeff -- SIDEExplicitFormula/LiWeil.lean :243, `(1/2) Σ′ ρ : zetaZeroConfig.carrier, m_ρ Re (pairTerm n ρ)`, its summability',
          '     pair_summable (:188) through WeilEF.zero_sum_inv_sq zetaSeam -- the ζ instance alone. Registers.lean :29 `B321.liCoeff` is a second',
          '     ζ-only form (the upper half-plane, its summability not proved). No configuration-level Li coefficient exists.',
          '  C2 No χ-Li declaration exists (the χ-Li search`s hits are all `line` and `lit` names). The χ-Li converse is priced at OPEN_TRAILS',
          '     :11732 (b570) and :11796 (b574, REMAINDER 1), the author`s word on the order cite.',
          '  C3 chiZeroConfig -- Chi/ZeroConfig.lean :225, hypothesis-free beyond primitivity and χ ≠ 1; its carrier the zeros of LFunction χ in the',
          '     OPEN strip (IsNontrivialZeroChi), its reflection ρ ↦ 1 − ρ̄ the fields reflect_mem and mult_reflect. No χ-seam declaration exists:',
          '     the instance is built from Mathlib`s LFunction directly. Its count: chiZeroConfig_local_count (Chi/LocalCount.lean :218); its',
          '     WeilConfig: chiWeilConfig (Schema/Instances.lean :51); its strip form: rh_strip_chi_iff_grh_chi (Chi/CriterionForward.lean :44),',
          '     GRH_chi (GRHWeil.lean :53) the strip form over LFunction χ.',
          '  C4 h2_sign_chi_iff_grh_chi -- Chi/CriterionConverse.lean :270 (also at v0.14 :270); li_nonneg_iff_rh -- LiCriterionBridge.lean :179',
          '     (also at v0.9), its converse Bulka`s through li_coeff_eq_taylorCoeff (:149).',
          '  C5 Zeta23`s ZeroConfig (Defs.lean :136) carries NO growth field; its docstring puts the local count in PaperInputs. The growth field',
          '     the ruling names is WeilConfig`s `count : ∃ A₀, B321.HCount toZeroConfig A₀` (Schema/Config.lean :24, HCount RestBound.lean :44:',
          '     `1 ≤ A₀ ∧ ∀ t, N(t, t + 1) ≤ A₀ log(|t| + 3)`), which zero_sum_inv_sq_gen (Zeta23/WeilEF/ZeroSummability.lean :121) consumes.',
          '  C6 Bulka`s modules (relay data/b569_bulka_generic.txt): 22 GENERIC (FunctionsOfOneComplexVariable, Hadamard.*), 11 ζ-SPECIFIC',
          '     (:30 Lc.LiCriterion.Basic, :69 Fidelity, :72 GenusOnePairedSumFormula, :80 HadamardBridge, :81 HadamardSummabilityBridge, :84',
          '     Pringsheim, :88 RHBridge, :99 ReverseDirection, :101 XiGrowth, :112 XiOrderBridge, :113 Lc.XiZeros).',
          '',
          '== 2. THE STATEMENTS, EVERY TERM TRACED (to a Mathlib name at the pin, a kernel name at %s, or a definition the branch introduces)' % KREV,
          '  S1 `def liCoeffCfg (Z : Zeta23.ZeroConfig) (n : ℕ) : ℝ := (1 / 2) * ∑′ ρ : Z.carrier, (Z.mult ρ : ℝ) * (LiWeil.pairTerm n ρ).re`',
          '     -- terms: Zeta23.ZeroConfig (Defs.lean :136), its carrier and mult; LiWeil.pairTerm (LiWeil.lean :63); tsum, Complex.re (Mathlib).',
          '     Lean`s tsum is 0 on an unsummable family; the convergence hypothesis is the configuration`s growth field:',
          '  S1s `theorem liCoeffCfg_summable (Z) {A₀ : ℝ} (hc : B321.HCount Z A₀) (n : ℕ) : Summable (fun ρ : Z.carrier => (Z.mult ρ : ℝ) *',
          '     (LiWeil.pairTerm n ρ).re)` -- pair_summable`s argument with zero_sum_inv_sq_gen Z in place of zero_sum_inv_sq zetaSeam (B321.HCount,',
          '     LiWeil.pairTerm_norm_le :177, Zeta23.ZeroConfig.finite_window, .strip).',
          '  S2 `theorem liCoeff_eq_liCoeffCfg (n : ℕ) : LiWeil.LiCoeff n = liCoeffCfg Zeta23.zetaZeroConfig n` -- the ζ-equality lemma (H1); the',
          '     same expression, so `rfl` is the expected proof.',
          '  S3 `theorem online_imp_liCoeffCfg_nonneg (Z) : (∀ ρ ∈ Z.carrier, ρ.re = 1 / 2) → ∀ n, 0 ≤ liCoeffCfg Z n` -- the generic forward half:',
          '     tsum_nonneg with LiWeil.pairTerm_re_nonneg_of_re_half (LiWeil.lean :109, algebra over ℂ, no ζ); no summability needed.',
          '  S4 `theorem grh_chi_imp_li_nonneg_chi (χ : DirichletCharacter ℂ N) (hχ : χ.IsPrimitive) (h1 : χ ≠ 1) : GRH_chi χ → ∀ n : ℕ, 0 ≤',
          '     liCoeffCfg (chiZeroConfig χ hχ h1) n` -- the forward half at χ (H2): S3 with rh_strip_chi_iff_grh_chi (Chi/CriterionForward.lean :44);',
          '     its proof consumes the configuration and no ζ object (the b564 walk re-run on the branch, its count printed).',
          '  S5 `theorem li_nonneg_cfg_imp_online (Z) {A₀ : ℝ} (hc : B321.HCount Z A₀) (hs : B321.HStrip Z) : (∀ n, 0 ≤ liCoeffCfg Z n) → ∀ ρ ∈',
          '     Z.carrier, ρ.re = 1 / 2` -- the generic converse (route P); HStrip (RestBound.lean :40, the open strip) excludes ρ = 0, where the',
          '     term is 0 by Lean`s 0⁻¹ = 0 and could not register an off-line point.',
          '  S6 `theorem li_nonneg_chi_imp_grh_chi (χ hχ h1) : (∀ n : ℕ, 0 ≤ liCoeffCfg (chiZeroConfig χ hχ h1) n) → GRH_chi χ` -- the converse at χ',
          '     (H3): S5 at chiZeroConfig with chiZeroConfig_local_count (its HCount) and the open strip of IsNontrivialZeroChi, then',
          '     rh_strip_chi_iff_grh_chi. Every term a Mathlib name at the pin (DirichletCharacter, IsPrimitive, LFunction) or a kernel name at %s.' % KREV,
          '  S7 (where S4 and S6 both land DERIVES) `theorem li_nonneg_chi_iff_grh_chi (χ hχ h1) : (∀ n, 0 ≤ liCoeffCfg (chiZeroConfig χ hχ h1) n) ↔',
          '     GRH_chi χ`, composed on the same branch; the ceiling sentence`s successor drafted in the landing bank for the author`s word.',
          '  The pairing: liCoeffCfg pairs each point with its conjugate inside the term (pairTerm), not across the carrier; Re (liTerm n ρ̄) = Re',
          '  (liTerm n ρ), so the coefficient is Σ m_ρ Re (1 − (1 − 1/ρ)^n) for any carrier, conjugation-stable or not -- χ`s carrier is not (its',
          '  conjugates are χ⁻¹`s zeros, Chi/ZeroConfig.lean`s (4)); the converse uses the configuration`s own symmetry ρ ↦ 1 − ρ̄ (reflect_mem).',
          '',
          '== 3. THE CONVERSE, PRICED ON TWO ROUTES',
          '  (B) BULKA`S ROUTE CARRIED TO χ (FINDINGS :6136; relay data/b569_bulka_generic.txt, its converse reading at the bank`s end):',
          '    B1 ξ_χ := completedLFunction χ (Mathlib DirichletContinuation.lean :224), entire for χ ≠ 1 (:250 differentiable_completedLFunction);',
          '       its functional equation :284 completedLFunction_one_sub pairs χ with χ⁻¹, not χ with itself. PRESENT.',
          '    B2 ξ_χ of order at most one (the growth bound the Hadamard product needs): ABSENT -- Mathlib holds no growth or order bound for',
          '       completedLFunction and no order-of-growth notion (searches above: yield %s, and the tightened shape %s; the wide shape`s %s are' % (
              res[10]['hits'], res[19]['hits'], res[11]['hits']),
          '       finite orders in algebra, by the hand reading); Bulka`s XiGrowth and XiOrderBridge (ζ-SPECIFIC)',
          '       prove it for ζ from ζ`s own bounds; the χ-analogue needs the vertical growth of LFunction χ and Stirling in the strip.',
          '    B3 the Hadamard product of ξ_χ: Bulka`s generic Hadamard.* modules, given B2; Mathlib holds none (the tightened shape yields %s; the' % res[18]['hits'],
          '       wide shape`s %s hits are a categorical product and power-series preparation, by the hand reading; Mathlib/Analysis/Complex/' % res[9]['hits'],
          '       Hadamard.lean is the three-lines theorem). PRESENT GENERICALLY, CONDITIONAL ON B2.',
          '    B4 φ_χ(0) = ξ_χ(1) ≠ 0: LFunction_apply_one_ne_zero (yield %s) with the Gamma factor at 1. PRESENT.' % res[15]['hits'],
          '    B5 the identification Re (Taylor coefficient of φ_χ′/φ_χ) = liCoeffCfg (chiZeroConfig χ hχ h1) n through the Hadamard product -- the',
          '       χ-analogue of li_coeff_eq_taylorCoeff, from Bulka`s HadamardBridge, HadamardSummabilityBridge and GenusOnePairedSumFormula',
          '       (ζ-SPECIFIC); for χ the coefficient λ_n(χ) is complex and only its real part converges absolutely (Re (1/ρ) = β/|ρ|²), so the',
          '       identification is of real parts. ABSENT; three modules to carry.',
          '    B6 the Pringsheim step (Pringsheim, ReverseDirection :335): ζ-SPECIFIC by naming (3 lines), generic in substance; Mathlib holds no',
          '       Pringsheim theorem (yield %s). A carry with riemannXi replaced by an abstract entire φ with φ(0) ≠ 0.' % res[8]['hits'],
          '    B7 the zero transport and the reflection (ReverseDirection :400; Basic :1668 pairedZero): at χ the reflection is reflect_mem, a field.',
          '    PRICE (B): B2 (an analytic number theory input absent from Mathlib: the order of ξ_χ) and the carry of at least seven ζ-specific',
          '    modules (XiGrowth, XiOrderBridge, HadamardBridge, HadamardSummabilityBridge, GenusOnePairedSumFormula, Pringsheim, ReverseDirection).',
          '  (P) THE BOMBIERI-LAGARIAS ROUTE ON THE CONFIGURATION (OPEN_TRAILS :11609, (V1)-(V4); at χ :11732, :11796):',
          '    V1 reflection stability with multiplicity: the fields reflect_mem and mult_reflect of ZeroConfig (Defs.lean :143-:144); at χ',
          '       chi_reflect_zero, chi_mult_reflect. COMPILED.',
          '    V2 an off-line point has an orbit member with |1 − 1/ρ′| > 1: |1 − 1/ρ|² − 1 = (1 − 2β)/(β² + γ²); ABSENT by name (kernel search',
          '       above, yield %s); one elementary lemma.' % res[4]['hits'],
          '    V3 the dominant set is finite: |1 − 1/ρ|² ≥ 1 + η bounds β² + γ² ≤ 1/η, and finite_window (Defs.lean :146) leaves finitely many',
          '       points; one lemma.',
          '    V4 the power-sum lemma: for finitely many w_k with |w_k| = 1, w_k ≠ 1, and multiplicities m_k ≥ 1, Re Σ m_k w_k^n ≤ −c for infinitely',
          '       many n with a fixed c > 0. ABSENT: no Turán-type inequality in Mathlib (the tightened shape yields %s; the wide shape`s %s hits are' % (
              res[17]['hits'], res[6]['hits']),
          '       Turán graphs) and no power-sum inequality by name (its %s declarations are cardinal arithmetic), nor in the kernel (yield %s).' % (
              res[7]['hits'], res[5]['hits']),
          '       A self-contained proof by Cesàro means:',
          '       the mean of S_n = Σ m_k w_k^n over n < M tends to 0 (geom_sum_eq, yield %s), its mean square stays at least a fixed c₀ > 0 (the' % res[16]['hits'],
          '       diagonal), so a positive proportion of n carries Re S_n ≤ −c₀/(4 Σ m_k). The lemma of substance.',
          '    V5 the remainder: the points off the dominant set contribute o(r_max^n) -- the second-order bound LiWeil.rem_bound (2^n, too coarse',
          '       when r_max < 2) refined to (1 + δ)^n for |1/ρ| ≤ δ, with the summability S1s; one lemma. (Not itemised at :11609; named here.)',
          '    PRICE (P): V2, V3, V5 elementary lemmas over ℂ on the configuration and V4 the lemma of substance; no analytic number theory input;',
          '    generic over every ZeroConfig with a count and an open strip -- χ`s, ζ`s and the family`s alike.',
          '  THE PREFERRED ROUTE: (P). REASON: every fact it misses is elementary analysis over ℂ on the configuration`s own fields and its count,',
          '  where (B) misses an analytic number theory input absent from Mathlib (B2, the order of ξ_χ) before its seven module carries; and (P)',
          '  lands generically (S5), so χ`s converse is S5`s instance. The attempt states S5 and S6 and proves V1-V3 and V5 as far as the runner',
          '  allows; V4 is the expected open point, banked by file and line if open.',
          '',
          '== 4. THE KERNEL FILES OF THE ATTEMPT ((R274)(4); read by the worklist from this bank`s JSON, key kernel_files), on branch %s:' % K.BRANCH]
    L += ['  ' + f for f in PLAN_KERNEL_FILES]
    L += ['  the dispatch`s target: the modules by name (the root SIDEExplicitFormula.lean imports a list; a new module it does not import must be',
          '  named in the target for the print step`s import), print_targets.txt on the branch, one dispatch at main with the branch tip as the ref.',
          '',
          '== 5. THE CONSUMERS SECTION ((R278)(3), OPEN_TRAILS :14290): each bank the act writes, its consumers, each consumer`s input tolerance',
          '  data/b669_chi_li_plan.txt/.json -- the author (the one prompt); tools/b669_worklist.py kernel_files() (key kernel_files: relative .lean',
          '     paths, exact, read as written); the suite (needles by section); the record`s title. Tolerance: the file names exact; no figure.',
          '  data/b669_chi_li_landing.txt/.json -- the record tool`s read_landing_row (a row: name, landing in DERIVES | COMPILED, PROOF OPEN | NOT',
          '     COMPILED, an open row`s obstruction {file, line: int}); the suite; the FINDINGS title; the ceiling-successor draft for the author`s',
          '     word; a later act`s order for an open declaration: none named (the author`s word names it). Tolerance: one landing per declaration.',
          '  data/b669_runner_rows.json, data/b669_runner_SIDE-explicit-formula.txt -- read_runner_row (RUNNER_KEYS, every key present), the',
          '     suite. Tolerance: the artifact`s sha256 equal to the platform`s digest before any reading; the memory low against the 2,560 MB hold.',
          '  data/b669_prints_SIDE-explicit-formula.txt -- the reference from here for a later gate (axiom_claim.prints_in_text reads `name [axioms]`',
          '     rows). Tolerance: the print text as Lean prints it; the standard three {propext, Classical.choice, Quot.sound} or none; sorryAx none.',
          '  print_targets.txt on the branch -- build-module.yml`s print step: one name per line, [A-Za-z0-9_.\'] only, a public name in a module',
          '     the target imports; a private name refused (b666 (b)). Tolerance: every name printed or the run read NOT DERIVES.',
          '  data/b669_zeta_walk.txt -- H2 and N4 (the forward half`s ζ-naming count). Tolerance: the count printed; zero wanted.',
          '  data/b669_tests_*, data/b669_citation_check.*, data/b669_ferry*, data/b669_defects.*, data/b669_readfirst.txt, data/b669_stepzero.txt',
          '     -- the suite`s standing arms, by the needles their predicates name. Tolerance: as b668`s carried predicates read them.',
          '  FINDINGS :8703, :8705 and the act`s later lines -- the one conversion`s look-ups (conv). Tolerance: the head line exact through conv.',
          '  The generic converse S5, where it lands -- ζ`s configuration is its second instance beside χ`s, a consumer of S5 with no tolerance: it',
          '     would give li_nonneg_iff_rh`s converse from the kernel`s own objects beside the vendored route, which stays as it is this act;',
          '     entered as a later act`s order by name, W-ORD-LI-CONVERSE-NATIVE, its trigger "S5 DERIVES" (the author`s word on the route).',
          '  No precision, width or numeric file form is fixed in this act: the attempt is Lean on the runner; no figure is banked as a bound.',
          '',
          '== 6. THE AUTHOR`S WORD ON THE ROUTE (relay data/b669_author_answers.txt; its mid-act check in data/b669_citation_check.txt)',
          '  Route (P). V4 stated as its own generic lemma -- for a finite set of distinct complex numbers of modulus 1 with positive integer',
          '  multiplicities and no member equal to 1, the real part of the power sum is at or below −c for infinitely many n, c > 0 named from the',
          '  multiplicities -- naming no ζ object and no configuration (the walk counts it at zero); attempted by the Cesàro-mean proof (the mean of',
          '  the power sum tending to 0, the mean of its square modulus to the sum of the squared multiplicities). Where V4 lands DERIVES, S5 and S6',
          '  follow on the same branch and the split rule applies declaration by declaration; where V4 lands open, S5`s branch stays unmerged with',
          '  V4 the obstruction by file and line and S1-S4 merged alone at v0.31. The finite dominant set: the kernel`s exists for the power-window',
          '  score (PowerWindow.lean :368, :398, :403), not for |1 − 1/ρ|; V3 is written for Li`s score and the kernel`s set cited as its nearest fact.',
          '',
          '### ### **CENSUS SEARCHES %d ; STATEMENTS S1-S7 ; ROUTES 2 PRICED ; PREFERRED (P) ; KERNEL FILES %d ; NO LEAN WRITTEN.**' % (
              len(res), len(PLAN_KERNEL_FILES))]
    put_txt('b669_chi_li_plan.txt', L)
    put_json('b669_chi_li_plan.json', dict(at=utc(), kernel=K.KERNEL, rev=KREV, mathlib=mrev, searches=res, kernel_files=PLAN_KERNEL_FILES,
                                           preferred='P', branch=K.BRANCH))
    print(NL.join(L[4:6 + 2 * len(res)]))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE ζ-NAMING WALK ON THE BRANCH (b564's pattern)
ZETA_ID = re.compile(r'\b(?:riemannZeta\w*|completedRiemannZeta\w*|\w*riemannZeta\w*|zeta_\w+|\w+_riemannZeta\w*)\b')   # ### b564_record.py :454
DECL_RE = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(?:noncomputable\s+)?(theorem|def|abbrev|structure|instance|lemma)\s+([^\s(:{\[]+)', re.M)


def _strip_comments(t):
    t = re.sub(r'/-[\s\S]*?-/', ' ', t)
    return NL.join(l.split('--', 1)[0] for l in t.split(NL))


def _decl_index(rev):
    """every declaration of the kernel's source trees (SIDEExplicitFormula/, Zeta23/) at `rev`: short name -> [(file, line, code)], the code
    the comment-stripped text from its head to the next declaration's head."""
    idx = collections.defaultdict(list)
    files = [f for f in g(K.KD, 'ls-tree', '-r', '--name-only', rev, '--', 'SIDEExplicitFormula', 'Zeta23').split(NL) if f.endswith('.lean')]
    for f in files:
        t = (_show(K.KD, rev, f) or '')
        heads = [(m.start(), m.group(2)) for m in DECL_RE.finditer(t)]
        for i, (pos, name) in enumerate(heads):
            end = heads[i + 1][0] if i + 1 < len(heads) else len(t)
            idx[name.split('.')[-1]].append((f, t[:pos].count(NL) + 1, _strip_comments(t[pos:end])))
    return idx


def walk(*a):
    """(R279)(4), H2 and N4: the forward half's proof walked through the kernel's source at the branch tip -- from
    grh_chi_imp_li_nonneg_chi, every identifier of a declaration's comment-stripped code that names a kernel declaration (by its last
    component; an over-reach, never an under-reach) followed transitively; each reached declaration read by b564's ζ pattern (ZETA_ID,
    b564_record.py :454). data/b669_zeta_walk.txt (.json)."""
    rev = a[0] if a else K.BRANCH
    idx = _decl_index(rev)

    def _walk(root):
        seen, queue, order = {root}, [root], []
        while queue:
            n = queue.pop(0)
            for f, ln, code in idx.get(n, []):
                order.append((n, f, ln, sorted(set(ZETA_ID.findall(code)))))
                for tok in set(re.findall(r"[A-Za-z_][A-Za-z0-9_'.₀-₉]*", code)):
                    s = tok.split('.')[-1]
                    if s in idx and s not in seen:
                        seen.add(s)
                        queue.append(s)
        return order
    root = 'grh_chi_imp_li_nonneg_chi'
    order = _walk(root)
    ctl = _walk('rh_imp_li_nonneg')            # ### the control: ζ's own forward half must reach a ζ-naming declaration
    ctl_z = [x for x in ctl if x[3]]
    zn = [x for x in order if x[3]]
    L = ['b669 -- COMPONENT 3: THE ζ-NAMING WALK OF THE FORWARD HALF AT χ, ON THE BRANCH (%s)' % utc(), '',
         '### rows are declarations, in the order the walk reaches them: from %s at %s (%s), every identifier of a reached declaration`s '
         'comment-stripped code that is a kernel declaration`s name (SIDEExplicitFormula/, Zeta23/; matched by its last component, so a '
         'shared short name over-reaches and never under-reaches) followed; each reached declaration read by b564`s ζ pattern %r.' % (
             root, rev, g(K.KD, 'rev-parse', '--short=7', rev).strip(), ZETA_ID.pattern), '']
    L += ['  %-48s %s:%d %s' % (n, f, ln, ('ζ-NAMING ' + ', '.join(z[:4])) if z else '') for n, f, ln, z in order]
    L += ['', '### THE CONTROL: the same walk from LiWeil.rh_imp_li_nonneg (ζ`s forward half) reaches %d declarations, ζ-naming %d -- %s; the '
          'matcher fires where ζ is consumed.' % (len(ctl), len(ctl_z), ', '.join('%s %s:%d %s' % (n, f, ln, z[:2]) for n, f, ln, z in ctl_z[:4]) or '### NONE')]
    L += ['', '### ### **DECLARATIONS REACHED %d ; ζ-NAMING %d%s ; THE CONTROL %d.**' % (
        len(order), len(zn), (' -- ' + ', '.join(sorted(set(x[0] for x in zn)))) if zn else '', len(ctl_z))]
    put_txt('b669_zeta_walk.txt', L)
    put_json('b669_zeta_walk.json', dict(at=utc(), rev=rev, root=root, reached=len(order), zeta=[dict(name=n, file=f, line=ln, ids=z) for n, f, ln, z in zn],
                                         order=[[n, f, ln] for n, f, ln, _z in order]))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE RUNNER (b668's, carried; no banked prints for
# ================================================================================ the act's new names, so every print is read at the standard three)
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
ERR_RE = re.compile(r'^(?:error: )?(\S+\.lean):(\d+):(\d+): error: (.*)$', re.M)


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def runner(*a):
    """`runner <run id> <ref> <workflow commit> [<branch>]`: the run read by its id; the artifact listed, downloaded by its id into memory, its
    sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP; every
    print of print_targets.txt at the ref read at the standard three or none, sorryAx named. Banked as data/b669_runner_<kernel>[_<tag>].txt
    and a row of data/b669_runner_rows.json (rows keyed by run id; an earlier run's row kept)."""
    import hashlib
    import zipfile
    import b569_record as R9
    run_id, ref, wfc = int(a[0]), a[1], a[2]
    branch = a[3] if len(a) > 3 else K.BRANCH
    kern = K.KERNEL
    repo = 'psinary-sketch/' + kern
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    pt = [l.strip() for l in (_show(K.KD, ref, 'print_targets.txt') or '').split(NL) if l.strip()]
    row = dict(kernel=kern, branch=branch, ref=ref, target=None, run_id=run_id, conclusion=run.get('conclusion'),
               artifact_sha256=None, mem_low=None, stopped=False, gate=None, merged=None, tag=None)
    L = ['b669 -- COMPONENT 3, (R279)(4): THE HOSTED RUNNER FOR %s, READ BY ITS RUN ID (%s)' % (kern, utc()), '',
         '### the workflow on main: %s (build-module.yml, b658`s form; the print step imports each module of the target)' % wfc,
         '### print_targets.txt at the ref: %d names' % len(pt),
         '### the dispatch: at main, the ref input %s (the tip of %s)' % (ref, branch),
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
    P = dict((k_, sorted(v_)) for k_, v_ in R9.prints_axioms(T_.get('axioms.txt', '')).items())
    axerr = [l for l in T_.get('axioms.txt', '').split(NL) if ': error' in l]
    row['target'] = ' '.join(T_.get('ref.txt', '').split()[:1]) and None
    gate_rows = []
    for n in pt:
        ax = P.get(n)
        if ax is None:
            gate_rows.append((n, ax, '### NOT PRINTED'))
        elif 'sorryAx' in ax:
            gate_rows.append((n, ax, 'SORRYAX'))
        else:
            gate_rows.append((n, ax, 'STANDARD THREE OR NONE' if set(ax) <= STD3 else '### OUTSIDE THE STANDARD THREE'))
    good = [r for r in gate_rows if r[2] == 'STANDARD THREE OR NONE']
    ok = (run.get('conclusion') == 'success' and row['artifact_sha256'] and bexit == '0' and not errs and not stops and row['mem_low'] is not None
          and row['mem_low'] >= K.HOLD and len(pt) > 0 and len(good) == len(pt) and not axerr)
    row['gate'] = 'DERIVES' if ok else ('STOPPED BENEATH THE HOLD' if stops else 'NOT DERIVES')
    row['errors'] = [list(e) for e in errs]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: samples %d ; LOW %s MB ; the hold %d ; STOP lines %s' % (
              len([l for l in mem.split(NL) if 'avail_mb=' in l]), row['mem_low'], K.HOLD, stops or 'NONE'),
          '### the build: exit %s ; error lines %d ; the log`s last lines:' % (bexit or '### UNREAD', len(errs))] + \
        ['    ' + l for l in blog.rstrip(NL).split(NL)[-8:]] + ['    %s:%d:%d: %s' % e for e in errs[:40]] + [
          '### the print step: error lines %d%s ; names refused %s' % (len(axerr), (' -- ' + ' | '.join(axerr[:4])) if axerr else '',
                                                                       T_.get('axioms_refused.txt', '').strip() or 'NONE'),
          '### THE GATE READING PER TERMINAL (no banked print for the act`s new names: each read at the standard three or none, sorryAx named):'] + \
        ['  %-58s %-44s %s' % (n, ax if ax is not None else '### NOT PRINTED', v) for n, ax, v in gate_rows] + [
          '', '### ### **RUN %s ; CONCLUSION %s ; ARTIFACT SHA256 %s ; MEMORY LOW %s MB (HOLD %d) ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS %d, PRINTED %d, '
          'AT THE STANDARD THREE OR NONE %d, SORRYAX %d ; GATE %s.**' % (
              run_id, run.get('conclusion'), (row['artifact_sha256'] or '### NONE')[:16], row['mem_low'], K.HOLD, bexit or '### UNREAD', len(errs),
              len(pt), sum(1 for r in gate_rows if r[1] is not None), len(good), sum(1 for r in gate_rows if r[2] == 'SORRYAX'), row['gate'])]
    tag = 'run%d' % run_id
    put_txt('b669_runner_%s_%s.txt' % (kern, tag), L)
    if row['artifact_sha256']:
        put_txt('b669_axioms_%s.txt' % tag, T_.get('axioms.txt', '').rstrip(NL).split(NL))
        put_txt('b669_build_log_%s.txt' % tag, blog.rstrip(NL).split(NL))
    j = jl('b669_runner_rows.json') if os.path.isfile(os.path.join(D, 'b669_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if r.get('run_id') != run_id] + [row]
    gr = dict(j.get('gate_rows') or {})
    gr[str(run_id)] = [list(r) for r in gate_rows]
    put_json('b669_runner_rows.json', dict(rows=rows, gate_rows=gr, workflow_commit=wfc))
    print(L[-1])
    for e in errs[:20]:
        print('  ERROR %s:%d:%d: %s' % e)


# ================================================================================ COMPONENT 3: THE LANDING, ONE ROW PER DECLARATION
def _sorry_lines(rev, f):
    t = _show(K.KD, rev, f) or ''
    return [i for i, l in enumerate(t.split(NL), 1) if re.search(r'(?<![A-Za-z_])sorry(?![A-Za-z_])', l.split('--', 1)[0])]


def landing(*a):
    """`landing <run id> <ref>`: each print target of the run's ref landed on its own reading -- DERIVES (printed, at the standard three or
    none, the build clean), COMPILED, PROOF OPEN (printed with sorryAx; the obstruction: the declaration's own `sorry` by file and line,
    else the first `sorry` of a declaration of the same file its code names), NOT COMPILED (not printed; the first error line). Each row
    read back through read_landing_row. data/b669_chi_li_landing.txt (.json; file_list the act's kernel files)."""
    run_id, ref = a[0], a[1]
    j = jl('b669_runner_rows.json')
    rr = [r for r in j.get('rows') or [] if str(r.get('run_id')) == run_id][0]
    gate_rows = j['gate_rows'][run_id]
    idx = _decl_index(ref)
    errs = rr.get('errors') or []
    rows = []
    for n, ax, v in gate_rows:
        short = n.split('.')[-1]
        loc = [(f, ln, code) for f, ln, code in idx.get(short, []) if f.startswith('SIDEExplicitFormula/')]
        f, ln, code = loc[0] if loc else ('?', 0, '')
        if v == 'STANDARD THREE OR NONE' and rr.get('artifact_sha256') and not errs:
            rows.append(dict(name=n, landing='DERIVES', axioms=ax, file=f, line=ln, obstruction=None))
        elif v == 'SORRYAX':
            own = [x for x in _sorry_lines(ref, f) if ln <= x < ln + code.count(NL) + 1]
            if own:
                ob = dict(file=f, line=own[0], why='its own sorry')
            else:
                called = [s for s in set(re.findall(r"[A-Za-z_][A-Za-z0-9_'.]*", code)) if s.split('.')[-1] in idx and s.split('.')[-1] != short]
                cand = []
                for s in called:
                    for f2, ln2, code2 in idx[s.split('.')[-1]]:
                        cand += [(f2, x, s.split('.')[-1]) for x in _sorry_lines(ref, f2) if ln2 <= x < ln2 + code2.count(NL) + 1]
                cand.sort()
                ob = dict(file=cand[0][0], line=cand[0][1], why='the sorry of %s, which its proof names' % cand[0][2]) if cand else dict(file=f, line=ln, why='sorryAx printed; no sorry line found')
            rows.append(dict(name=n, landing='COMPILED, PROOF OPEN', axioms=ax, file=f, line=ln, obstruction=ob))
        else:
            e0 = errs[0] if errs else [f, ln, 0, v]
            rows.append(dict(name=n, landing='NOT COMPILED', axioms=ax, file=f, line=ln, obstruction=dict(file=e0[0], line=int(e0[1]), why=str(e0[3])[:200])))
    for r in rows:
        read_landing_row(r)
    c = collections.Counter(r['landing'] for r in rows)
    L = ['b669 -- COMPONENT 3, (R279)(4): EACH DECLARATION LANDED ON ITS OWN READING (%s)' % utc(), '',
         '### rows are declarations: the name, its landing, its file and line at %s (%s), its printed axioms, and where open the obstruction by '
         'file and line. The run: %s (relay data/b669_runner_%s_run%s.txt).' % (ref[:8], K.BRANCH, run_id, K.KERNEL, run_id), '']
    for r in rows:
        L.append('  %-58s %-22s %s:%s  %s' % (r['name'], r['landing'], r['file'], r['line'], r['axioms']))
        if r['obstruction']:
            L.append('  %-58s %-22s OBSTRUCTION %s:%s (%s)' % ('', '', r['obstruction']['file'], r['obstruction']['line'], r['obstruction']['why']))
    L += ['', '### ### **DECLARATIONS %d ; %s.**' % (len(rows), ' ; '.join('%s %d' % kv for kv in sorted(c.items())))]
    files = sorted(set(r['file'] for r in rows if r['file'] != '?'))
    put_txt('b669_chi_li_landing.txt', L)
    put_json('b669_chi_li_landing.json', dict(at=utc(), run_id=int(run_id), ref=ref, rows=rows, file_list=files))
    print(NL.join(L[3:]))


def merged(*a):
    """`merged <run id> <merge sha> <tag> <open branch>`: the merge of the DERIVES run's tree recorded on its runner row and in the landing
    bank -- the tag's peeled SHA read back, the merged tree against the built tree, the merged declarations (the run's print list), the open
    branch's tip read locally and its remote tracking ref, and no sorry on main in the merged files."""
    run_id, sha, tag, ob = a[0], a[1], a[2], a[3]
    j = jl('b669_runner_rows.json')
    for r in j['rows']:
        if str(r['run_id']) == run_id:
            r['merged'], r['tag'] = sha, tag
            built = r['ref']
    peeled = g(K.KD, 'rev-parse', '%s^{commit}' % tag).strip()
    tree_eq = g(K.KD, 'rev-parse', sha + '^{tree}').strip() == g(K.KD, 'rev-parse', built + '^{tree}').strip()
    names = [l.strip() for l in (_show(K.KD, built, 'print_targets.txt') or '').split(NL) if l.strip()]
    files = sorted(x for x in g(K.KD, 'diff', '--name-only', K.KREV if hasattr(K, 'KREV') else 'v0.30', sha).split(NL) if x.endswith('.lean'))
    sorry = [l for l in g(K.KD, 'grep', '-n', '-w', 'sorry', sha, '--', *files).split(NL) if l.strip()] if files else []
    otip = g(K.KD, 'rev-parse', ob).strip()
    j['merge'] = dict(run_id=int(run_id), sha=sha, tag=tag, peeled=peeled, tree_equal=tree_eq, built=built, names=names, files=files,
                      sorry_on_main=sorry, open_branch=ob, open_tip=otip, open_remote=g(K.KD, 'rev-parse', 'origin/' + ob).strip())
    put_json('b669_runner_rows.json', j)
    lj = jl('b669_chi_li_landing.json')
    lj['merge'] = j['merge']
    put_json('b669_chi_li_landing.json', lj)
    lt = rdn('b669_chi_li_landing.txt').rstrip(NL).split(NL)
    lt += ['', '### THE MERGE ((R279)(4), the split): the DERIVES declarations of LiCfg.lean and LiForward.lean (%s) on their own branch from main,' % (
               ', '.join(n.split('.')[-1] for n in names)),
           '### built alone (run %s, DERIVES), merged alone at %s, tagged %s, peeled %s read back; the merged tree the built tree %s; sorry on main in the' % (
               run_id, sha[:8], tag, peeled[:8], tree_eq),
           '### merged files %s ; the converse`s branch %s at %s (the remote %s), unmerged, its open declarations above with their obstructions;' % (
               sorry or 'NONE', ob, otip[:8], j['merge']['open_remote'][:8]),
           '### the next lemma of substance: (V4) powerSum_re_le_neg_infinitely, SIDEExplicitFormula/Schema/LiConverseCfg.lean :129 at %s, with (V5)' % otip[:8],
           '### remainder_le :139 open beside it; V2, V3 and V4`s two Cesàro steps DERIVES on that branch, held with its file.',
           '### ### **MERGED %d DECLARATIONS AT %s, TAG %s ; THE CONVERSE OPEN AT V4 (:129) AND V5 (:139) ON %s.**' % (len(names), sha[:8], tag, ob)]
    put_txt('b669_chi_li_landing.txt', lt)
    print(NL.join(lt[-6:]))


# ================================================================================ THE HYPOTHESES OF (R279)(4), SCORED ON THEIR PRINTED LINES
def _land_rows():
    return dict((r['name'].split('.')[-1], r) for r in (jl('b669_chi_li_landing.json').get('rows') or []))


def hyp(*a):
    """(R279)(4) H1-H4, each read off a printed line: data/b669_hypotheses.txt (.json)."""
    lr = _land_rows()
    wj = jl('b669_zeta_walk.json')
    pj = jl('b669_chi_li_plan.json')
    s = dict((x['label'], x['hits']) for x in pj.get('searches') or [])
    miss = [('B2, an order-of-growth notion (tightened)', 'TIGHTENED: an order-of-growth notion for entire functions'),
            ('B2, a growth bound for completedLFunction', 'a growth or order bound for the completed L-function (B)'),
            ('B3, a Hadamard or Weierstrass factorization (tightened)', 'TIGHTENED: a Hadamard or Weierstrass factorization of an entire function'),
            ('B6, a Pringsheim theorem', 'a Pringsheim theorem (B, the Pringsheim step)'),
            ('V4, a Turán-type inequality on sums of powers (tightened)', 'TIGHTENED: a Turán-type inequality on sums of powers'),
            ('V2, a strict modulus lemma in the kernel', 'a strict modulus lemma |1 - 1/ρ| > 1 off the line (V2)'),
            ('V4, a power-sum lemma in the kernel', 'a power-sum lemma (V4)')]
    found = [('B1, completedLFunction', 'the completed L-function of a Dirichlet character'), ('B1, its differentiability', 'its differentiability (χ ≠ 1)'),
             ('B1, its functional equation', 'its functional equation (primitive χ)'), ('B4, L(1, χ) ≠ 0', 'L(1, χ) ≠ 0 (B, φ(0) ≠ 0)')]
    h1 = lr.get('liCoeff_eq_liCoeffCfg', {})
    h2 = lr.get('grh_chi_imp_li_nonneg_chi', {})
    h3 = lr.get('li_nonneg_chi_imp_grh_chi', {})
    mg = (jl('b669_chi_li_landing.json').get('merge') or {})
    H = {
        'H1': ('HELD' if h1.get('landing') == 'DERIVES' and 'liCoeff_eq_liCoeffCfg' in ' '.join(mg.get('names') or []) else 'REFUTED',
               'liCoeff_eq_liCoeffCfg %s at %s (Schema/LiCfg.lean :%s), merged at v0.31' % (h1.get('landing'), h1.get('axioms'), h1.get('line'))),
        'H2': ('HELD' if h2.get('landing') == 'DERIVES' and wj.get('zeta') == [] and wj.get('reached', 0) > 0 else 'REFUTED',
               'grh_chi_imp_li_nonneg_chi %s at %s; the ζ-naming walk on the branch: %s declarations reached, ζ-naming %d (relay data/b669_zeta_walk.txt, '
               'its control from rh_imp_li_nonneg firing)' % (h2.get('landing'), h2.get('axioms'), wj.get('reached'), len(wj.get('zeta') or []))),
        'H3': ('HELD' if h3.get('landing') in ('DERIVES', 'COMPILED, PROOF OPEN') else 'REFUTED',
               'li_nonneg_chi_imp_grh_chi compiled at χ (%s, Schema/LiConverseCfg.lean :%s on %s), every term a Mathlib name at the pin or a kernel or '
               'branch definition; its landing as (4) fixes: %s, the obstruction %s' % (h3.get('landing'), h3.get('line'), K.BRANCH, h3.get('landing'),
                                                                                         (h3.get('obstruction') or {}).get('line'))),
        'H4': ('HELD' if all(s.get(lab) == 0 for _w, lab in miss) and all(s.get(lab, 0) >= 1 for _w, lab in found) else 'REFUTED',
               'missing, each by a printed search yielding 0: %s; found and cited: %s (relay data/b669_chi_li_plan.txt section 1)' % (
                   '; '.join('%s %s' % (w, s.get(lab)) for w, lab in miss), '; '.join('%s %s' % (w, s.get(lab)) for w, lab in found))),
    }
    L = ['b669 -- THE HYPOTHESES OF (R279)(4), EACH READ OFF A PRINTED LINE (%s)' % utc(), ''] + \
        ['  (%s) %s -- %s' % (k, v[0], v[1]) for k, v in sorted(H.items())] + \
        ['', '### ### **%s.**' % ' ; '.join('%s %s' % (k, v[0]) for k, v in sorted(H.items()))]
    put_txt('b669_hypotheses.txt', L)
    put_json('b669_hypotheses.json', dict((k, list(v)) for k, v in H.items()))
    print(L[-1])


# ================================================================================ THE LATE ROUTES (b668's, carried; every row read through READERS)
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
    L = ['b669 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
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
    put_txt('b669_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b669_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


def kernels(*a):
    import b641_record as R41
    put_json('b669_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


DEFECT_ROW = re.compile(r'^    \(([a-z])\) ')


def _defect_short():
    out = []
    for l in rdn('b669_defects.txt').split(NL):
        m = re.match(r'^    \(([a-z])\) ([^.]*)\.', l)
        if m:
            out.append(m.group(0).strip()[:-1])
    return out


def defects(*a):
    t = rdn('b669_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b669_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b669_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b669_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b669_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b669_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b669_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b669'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b669_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    with tempfile.TemporaryDirectory(prefix='b669_ra_') as tmp:
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
    L = ['b669 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b669_root_arm.txt', L)
    put_json('b669_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b669 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b669_table_final.txt', L)
    put_json('b669_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b669_registration_2026-10-14.txt'
FACE = os.path.join(D, 'b669_registration_2026-10-14.txt')


def gatebanks(*a):
    """the gate's steps between the face and the lock (b665's order), each tool's output banked by this route, never by a shell redirect."""
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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b669_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b669_regspec.py')], 'b669_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b669_satisfiable.json', '--emit', 'b669'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b669_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b669_census_stepzero.txt'), ('b327_faces_census.py', 'b669_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b669_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b669'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b669_reg_gate.txt', 'data/b669_reg_termscan.txt', 'data/b669_regspec_run.txt', 'data/audit_b669_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b668_closing_push_out.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
K_PRE = '02bc85d'           # ### SIDE-explicit-formula main before the act (= v0.30)


def TRAIL_HEAD():
    return ('### b669 — lane two, act ninety-six, the research act under (R279): b668 at its weight; the Li coefficient over the configuration; '
            'the forward half at χ merged at v0.31; the converse on route (P) open at the power-sum lemma')


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime((s or '')[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


def _calls():
    return jl('b669_author_answers.json').get('calls') or []


def _call_by_header(h):
    ids = [b.split(' ', 1)[0] for b in re.split(r'^### CALL tool-use id ', rdn('b669_author_answers.txt'), flags=re.M)[1:]
           if re.search(r'^### PROMPT \d+ \(%s\)' % re.escape(h), b, re.M)]
    return [c for c in _calls() if c.get('id') in ids]


def _first_kernel_ct():
    """the first kernel byte of the act: the first commit on the act's branches or on main after K_PRE."""
    ts = []
    for ref in (K.BRANCH, 'chi-li-forward-b669', 'main'):
        for l in g(K.KD, 'log', '--reverse', '--format=%ct', '%s..%s' % (K_PRE, ref)).split(NL):
            if l.strip():
                ts.append(int(l))
                break
    return min(ts) if ts else None


def _plan_ct():
    for l in g(RELAY, 'log', '--reverse', '--format=%ct %s', K.PRE_RELAY + '..HEAD', '--', 'data/b669_chi_li_plan.txt').split(NL):
        if l.strip():
            return int(l.split(' ', 1)[0])
    return None


def _n2():
    pj = jl('b669_chi_li_plan.json')
    pt = rdn('b669_chi_li_plan.txt')
    rc = _call_by_header('Route')
    ans = _iso(rc[0].get('result_ts')) if rc else None
    kct, pct = _first_kernel_ct(), _plan_ct()
    secs = all(x in pt for x in ('== 2. THE STATEMENTS, EVERY TERM TRACED', '== 3. THE CONVERSE, PRICED ON TWO ROUTES', '== 5. THE CONSUMERS SECTION'))
    ok = bool(pj.get('searches')) and secs and pct and kct and ans and pct < kct and ans < kct
    return ('HELD' if ok else 'REFUTED'), (
        'the plan (relay data/b669_chi_li_plan.txt): %d searches printed, each yield beside its pattern, the wide shapes hand-read and three '
        'tightened; every statement`s terms traced (section 2); the consumers section present (section 5); the plan first committed at %s, the '
        'author`s word on the route at %s, the first kernel byte at %s' % (
            len(pj.get('searches') or []), time.strftime('%H:%M:%SZ', time.gmtime(pct)) if pct else '?',
            time.strftime('%H:%M:%SZ', time.gmtime(ans)) if ans else '?', time.strftime('%H:%M:%SZ', time.gmtime(kct)) if kct else '?'))


def _n3():
    lj = jl('b669_chi_li_landing.json')
    rows = lj.get('rows') or []
    mg = lj.get('merge') or {}
    names = [r['name'] for r in rows]
    one = len(names) == len(set(names)) > 0
    for r in rows:
        read_landing_row(r)
    open_on_main = [r['name'] for r in rows if r['landing'] != 'DERIVES' and r['name'] in (mg.get('names') or [])]
    ok = one and not mg.get('sorry_on_main') and not open_on_main and mg.get('tree_equal') and mg.get('peeled', '').startswith(mg.get('sha', 'x')[:7])
    return ('HELD' if ok else 'REFUTED'), (
        'each of %d declarations one landing (relay data/b669_chi_li_landing.txt): %s; the open ones with their obstruction by file and line; '
        'the DERIVES ones merged alone (%s, tag %s, the merged tree the built tree %s); sorry on main %s; open declarations on main %s' % (
            len(rows), dict(collections.Counter(r['landing'] for r in rows)), (mg.get('sha') or '?')[:8], mg.get('tag'), mg.get('tree_equal'),
            mg.get('sorry_on_main') or 'NONE', open_on_main or 'NONE'))


def _n4():
    hj = jl('b669_hypotheses.json')
    wj = jl('b669_zeta_walk.json')
    ok = (hj.get('H1') or ['?'])[0] == 'HELD' and wj.get('zeta') == [] and wj.get('reached', 0) > 0
    return ('HELD' if ok else 'REFUTED'), ('H1 %s; the forward half`s ζ-naming walk on the branch: %s declarations reached, ζ-naming %d, its control '
                                           'firing (relay data/b669_zeta_walk.txt)' % ((hj.get('H1') or ['?'])[0], wj.get('reached'), len(wj.get('zeta') or [])))


def _n5():
    face = jl('b669_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b669_|audit_b669_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    mg = (jl('b669_chi_li_landing.json').get('merge') or {})
    km = [l for l in g(K.KD, 'log', '--first-parent', '--format=%h %p', K_PRE + '..main').split(NL) if l.strip()]
    km_ok = [l.split()[0] for l in km] == [(mg.get('sha') or 'x')[:7]] and len(km[0].split()) == 3
    k_files = sorted(x for x in g(K.KD, 'diff', '--name-only', K_PRE, 'main').split(NL) if x.strip())
    want_k = sorted(['print_targets.txt'] + (mg.get('files') or []))
    rr = [x for x in k_files if x in ('README.md', 'REGISTRY.md')]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b669_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ok = others_ok and not pp_beyond and not kinds_beyond and not differ and km_ok and not new_arms and k_files == want_k and not rr
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); %s`s main written by the merge under Component 4 alone '
            '(first-parent commits since %s: %s ; %s), its files against %s: %s; README and REGISTRY unwritten %s; every kernel as the face read '
            'it %s; standing arms added: %s (the act`s arms over its own banks %d); sealed tools not agreeing %s; PLACE-papers beyond FINDINGS and '
            'OPEN_TRAILS: %s; relay files of a kind beyond the banks, the tools, the root list and b668`s push-out bank: %s; no identifier of the '
            'author in any outbound request (git pushes, remote reads, the runner`s dispatches with a ref and a target, the artifacts` downloads)' % (
                K.DRAFT, K.KERNEL, K_PRE, [l.split()[0] for l in km], 'AS RULED' if km_ok else '### OTHERWISE', K_PRE, k_files, not rr, others_ok,
                new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE'))


def scores(*a):
    TF, RA = jl('b669_table_final.json'), jl('b669_root_arm.json')
    _r, _n, sh = seal_hashes()
    cm = jl('b669_commands.json')
    print('  (R274)(4): the kernel files, read from the plan and landing banks: %s' % read_kernel_files())
    S = {
        'N1': (('HELD' if cm and not cm.get('local_lean') else 'REFUTED'),
               'commands of this act that run lean or lake on this host: %s (relay data/b669_commands.txt); the builds on the hosted runner alone' % (
                   cm.get('local_lean') if cm else '### UNREAD')),
        'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    put_json('b669_scores.json', dict((k2, list(v)) for k2, v in S.items()))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))


NEXT_LINE = 'b670, per `(R279)`(7), the reading act as `(R278)`(5) orders it; b671 W-ORD-EPSTEIN-BALL-WIDTH'


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'


def _landing_word(name):
    r = _land_rows().get(name) or {}
    return {'DERIVES': 'DERIVES', 'COMPILED, PROOF OPEN': 'compiled, its proof open', 'NOT COMPILED': 'not compiled'}.get(r.get('landing'), '?')


def _title():
    tag = ((jl('b669_chi_li_landing.json').get('merge') or {}).get('tag')) or 'v0.31'
    return ('## The Li coefficient over the configuration, ζ’s LiCoeff as its instance; the forward half at χ %s; the converse at χ on the P route '
            '%s; %s' % (_landing_word('grh_chi_imp_li_nonneg_chi'), _landing_word('li_nonneg_chi_imp_grh_chi'), tag))


def _finding_text():
    S, rl, J = jl('b669_scores.json'), jl('b669_record_lines.json'), jl('b669_act_root.json')
    hj = jl('b669_hypotheses.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b669_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}]
    rp = (jl('b669_repair_lines.json').get('lines') or []) + [{}]
    lj = jl('b669_chi_li_landing.json')
    mg = lj.get('merge') or {}
    c = collections.Counter(r['landing'] for r in lj.get('rows') or [])
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    mids = re.findall(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    wj = jl('b669_zeta_walk.json')
    rows = jl('b669_runner_rows.json').get('rows') or []
    e = ['', _title(), '',
         '*Filed at b669 on the author’s ruling `(R279)` and the author’s word (%d questions in %d calls). Banks: relay '
         '`data/b669_citation_check.txt`, `data/b669_chi_li_plan.txt`, `data/b669_zeta_walk.txt`, `data/b669_chi_li_landing.txt`, '
         '`data/b669_hypotheses.txt`, `data/b669_act_root.txt`.*' % (n_ans, len(_calls())), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed -- the ten-acts bank`s unit, raised and '
         'answered (the χ-Li converse traced from OPEN_TRAILS :11732 and :11796); the mid-act check of `(R278)`(4) over %d answers, the last %s of %s '
         'OK.' % (cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', len(mids), mids[-1][1] if mids else '?',
                 mids[-1][0] if mids else '?'), '',
         '**The record lines** (`(R279)`(1), (6)): b668 at its weight (FINDINGS :%s); b668’s N4 cell read at its post-push reading, HELD, '
         'by an appended line (:%s).' % (ls[0].get('line'), rp[0].get('line')), '',
         '**The plan** (`(R279)`(3)): the census by search printed -- no configuration-level Li coefficient, no χ-Li declaration, no χ-seam '
         'declaration; ZeroConfig carries no growth field, the growth field the WeilConfig count; the statements S1-S7 traced; the converse priced '
         'on Bulka’s route carried to χ (the order of ξ_χ absent from Mathlib, seven ζ-specific modules to carry) and on the Bombieri-Lagarias '
         'route over the configuration (V2, V3, V5 elementary, V4 the power-sum lemma absent); the consumers section; the author’s word: route P.', '',
         '**The attempt** (`(R279)`(4)): on branch chi-li-b669, %d declarations, run %s read by its id, the artifact’s sha256 agreeing with the '
         'platform’s digest, the build clean; DERIVES %d, compiled with the proof open %d. The forward half grh_chi_imp_li_nonneg_chi DERIVES, its '
         'proof walked through the kernel: %s declarations reached, none ζ-naming. V2 and V3 DERIVES; V4, the power-sum lemma, stated as a lemma of '
         'finite sums and open at its own line, with V5 open beside it, so the generic converse and its instance at χ are compiled with the proof '
         'open.' % (len(lj.get('rows') or []), rows[0].get('run_id') if rows else '?', c.get('DERIVES', 0), c.get('COMPILED, PROOF OPEN', 0),
                    wj.get('reached')), '',
         '**The merge** (`(R279)`(4), the split): the Li coefficient over the configuration, its summability from the count, the ζ-equality and the '
         'forward half, generic and at χ, on their own branch, built alone (run %s, DERIVES), merged alone at %s, tagged %s, the peeled SHA read '
         'back, the merged tree the built tree; the converse’s branch unmerged, no sorry on main. %s.' % (
             mg.get('run_id'), (mg.get('sha') or '?')[:7], mg.get('tag'), ', '.join('%s %s' % (k, (hj.get(k) or ['?'])[0]) for k in ('H1', 'H2', 'H3', 'H4'))), '',
         '**The root.** b669 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b560’s Li coefficient, b564’s pricing of the converse, b569’s reading of '
         'Bulka’s modules and the χ-configuration of W-ORD-GRH-WEIL; it is re-read by the act that takes up the power-sum lemma, and by '
         'W-ORD-LI-CONVERSE-NATIVE when the generic converse lands. It strengthens the programme’s offering of statements a reader can check: the Li '
         'coefficient now stands over every zero configuration with ζ’s as one instance, and its forward half at a primitive character is '
         'compiled at the standard three.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; the forward half assumes GRH_chi, and the converse is compiled with '
         'its proof open.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) V5 open beside V4, where the author’s word ordered V2, V3 and V5 proved -- V2 and V3 DERIVES, V5 compiled with its proof '
              'open at its own line; (2) V2, V3 and V4’s two Cesàro steps DERIVES but held on the converse’s branch with its file, the split merging '
              'S1-S4 alone as the word on an open V4 orders; (3) the finite dominant set of V3 written for Li’s score, the kernel’s power-window set '
              '(PowerWindow.lean :398-:403) another set; (4) the forward half at χ written over chiZeroConfig’s carrier with rh_strip_chi_iff_grh_chi’s '
              'argument, not its import, the dispatch`s target the new modules by name')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b669_scores.json', 'b669_findings.json', 'b669_record_lines.json', 'b669_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b669_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}]
    rp = (jl('b669_repair_lines.json').get('lines') or []) + [{}]
    mg = (jl('b669_chi_li_landing.json').get('merge') or {})
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R279) ratified.** (1) b668 at its weight. (2) The Li coefficient over the configuration, ζ’s LiCoeff its instance. (3) The plan with '
             'its consumers section. (4) The forward half at χ landed DERIVES and merged; the converse on route P compiled with its proof open. (5) No '
             'bench number in a keystone. (6) The record repair. (7) The act after: b670.', '',
             '**Entered:** FINDINGS.md:%s (b668’s weight), :%s (the N4 repair), :%s (the entry); this record.' % (
                 ls[0].get('line'), rp[0].get('line'), fj.get('entry_line')), '',
             '**Act root:** b669 `%s` (previous `%s`, b668’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d calls (relay data/b669_author_answers.txt): the order cite at step zero and the one prompt '
             'of `(R279)`(3), before any Lean; none after the root.' % (n_ans, len(_calls())), '',
             '**The open converse:** branch %s at %s (unmerged); the next lemma of substance V4, powerSum_re_le_neg_infinitely, '
             'SIDEExplicitFormula/Schema/LiConverseCfg.lean :129, V5 :139 beside it; W-ORD-LI-CONVERSE-NATIVE, its trigger “S5 DERIVES”, named in the plan.' % (
                 mg.get('open_branch'), (mg.get('open_tip') or '?')[:8]), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b669_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b669_scores.json')
    L = ['=' * 104, 'b669 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b669_hypotheses.txt').rstrip(NL).split(NL) + [''] + rdn('b669_defects.txt').rstrip(NL).split(NL)
    put_txt('b669_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b669_scores.json', 'b669_findings.json', 'b669_trail.json', 'b669_record_lines.json', 'b669_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}]
    rp = (jl('b669_repair_lines.json').get('lines') or []) + [{}]
    mg = (jl('b669_chi_li_landing.json').get('merge') or {})
    L = ['b669 -- THE COMPONENTS, BANKED UNDER (R279).', '',
         '### COMPONENT 0 : the citation check (data/b669_citation_check.txt), step zero (data/b669_ferry.txt, data/b669_stepzero.txt, '
         'data/b669_tests_stepzero.txt, data/b669_readfirst.txt), the record repair FINDINGS :%s ; push-out relay %s' % (rp[0].get('line'), K.STEPZERO),
         '### COMPONENT 1 : b668`s weight FINDINGS :%s' % ls[0].get('line'),
         '### COMPONENT 2 : the plan (data/b669_chi_li_plan.txt), the author`s word on the route (data/b669_author_answers.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the attempt on %s (data/b669_runner_rows.json, data/b669_zeta_walk.txt, data/b669_chi_li_landing.txt) ; N3 %s ; N4 %s' % (
             K.BRANCH, S['N3'][0], S['N4'][0]),
         '### COMPONENT 4 : the merge %s, tag %s, the open branch %s at %s' % ((mg.get('sha') or '?')[:8], mg.get('tag'), mg.get('open_branch'),
                                                                               (mg.get('open_tip') or '?')[:8]),
         '### COMPONENT 5 : the dry-run step (data/b669_reg_gate.txt), the seal (data/b669_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b669_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b669_findings.json', dict(title=t))
    j = jl('b669_findings.json')
    j['entry_line'] = ln
    put_json('b669_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b669_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written (B669_STANDIN) -- converted by conv and run through the screens their landing runs, the needles the face
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


ROUTES = {'repair': repair, 'c1': c1, 'answers': answers, 'plan': plan, 'walk': walk, 'runner': runner, 'landing': landing, 'merged': merged,
          'hyp': hyp, 'commands': commands, 'kernels': kernels, 'defects': defects, 'root': root, 'root_arm': root_arm, 'table_final': table_final,
          'gatebanks': gatebanks, 'scores': scores, 'desk': desk, 'components': components, 'findings': findings, 'trail': trail, 'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b669_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
