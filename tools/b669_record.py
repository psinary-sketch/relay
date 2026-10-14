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
            for mm in re.finditer(r'(?s)BEGIN\s*(.*?)\s*END(?!\w)', t or ''):
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
          '  No precision, width or numeric file form is fixed in this act: the attempt is Lean on the runner; no figure is banked as a bound.',
          '',
          '### ### **CENSUS SEARCHES %d ; STATEMENTS S1-S7 ; ROUTES 2 PRICED ; PREFERRED (P) ; KERNEL FILES %d ; NO LEAN WRITTEN.**' % (
              len(res), len(PLAN_KERNEL_FILES))]
    put_txt('b669_chi_li_plan.txt', L)
    put_json('b669_chi_li_plan.json', dict(at=utc(), kernel=K.KERNEL, rev=KREV, mathlib=mrev, searches=res, kernel_files=PLAN_KERNEL_FILES,
                                           preferred='P', branch=K.BRANCH))
    print(NL.join(L[4:6 + 2 * len(res)]))
    print(L[-1])


ROUTES = {'repair': repair, 'c1': c1, 'answers': answers, 'plan': plan}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b669_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
