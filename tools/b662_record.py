# -*- coding: utf-8 -*-
"""b662_record.py -- THE ACT'S RECORD TOOL, b662 under (R272).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b662's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b661_record.py (the landing, the readers, the answers) and b659_record.py (the sentence rows, the plain
### comments, the grades, the cut planned on the blobs and its check, the cut bank, the runner); new here: the record lines of (R272)(1), (2),
### (4); the kernel's banked profiles read from its README (README.md :75-:101, short names, b647 having no print bank for this kernel). The
### late routes are added to this file by the Edit tool before the seal, each run before the face names it.
### Routes: `python tools/b662_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
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
import b662_worklist as K          # noqa: E402

STANDIN = bool(os.environ.get('B662_STANDIN'))


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
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'H2', 'S1', 'S2', 'S3')
    return {
        'b662_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b662_findings.json': dict(entry_line=99999, title='stand-in'),
        'b662_trail.json': dict(line=99999),
        'b662_act_root.json': dict(root='0' * 64, previous='9d223d09' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
        'b662_mirror.json': dict(zip='stand-in', manifest_md5='0' * 32),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b662's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b662_scanfile_%s.md' % tag)
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
    """a row of data/b662_runner_rows.json -- every key of RUNNER_KEYS present (None where a step did not reach it); returns the row's reading
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
    """a scores row: key N1..N5, H2 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text) -- the whole verdict, not its
    first word (b656's defect (e))."""
    if not re.match(r'^(N[1-5]|H2|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


def read_grade_row(k, row):
    """a row of the hand grades (data/b662_sentence_grades.json): block number k and [sentence number, the cell's quoted words];
    returns (k, n, words); raises on a row of another shape."""
    n, w = row
    ok_n = (isinstance(n, int) and n >= 1) or (isinstance(n, str) and re.match(r'^\d+(\.\d+)?$', n) is not None)
    if not ok_n or not isinstance(w, str) or not w.strip() or not str(k).isdigit():
        raise ValueError('grade row of another shape: %r' % (row,))
    return int(k), str(n), w


README_ROW = re.compile(r'^([A-Za-z_][\w\'.]*)\s+(?:\[([^\]]*)\]|\(axiom-free\))\s*$')


def read_print_row(line):
    """a row of the kernel's banked profiles (README.md :75-:101 at v0.4.1): `<short name>  [axioms]` or `<short name>  (axiom-free)`;
    returns (short name, sorted axioms); raises on a row of another shape."""
    m = README_ROW.match(line.strip())
    if not m:
        raise ValueError('print row of another shape: %r' % (line[:80],))
    return m.group(1), sorted(x.strip() for x in (m.group(2) or '').split(',') if x.strip())


CELL_FORMS = ('j₀ = ', 'NONE ≤ J_max', 'HYP-UNVERIFIED(')


def read_map_cell(r):
    """a cell of the J_max = D + 40 map bank (data/b662_detection_map_40.json, rows are cells): sigma and t strings, certs a non-empty list of
    [name, CERTIFIED or NOT CERTIFIED, why], a reading in one of the three forms of (R271)(4); returns (sigma, t, form, j0 or None);
    raises on a row of another shape."""
    if not isinstance(r, dict) or not isinstance(r.get('sigma'), str) or not isinstance(r.get('t'), str):
        raise ValueError('map cell of another shape')
    cs = r.get('certs')
    if not isinstance(cs, list) or not cs or not all(isinstance(c, list) and len(c) == 3 and c[1] in ('CERTIFIED', 'NOT CERTIFIED') for c in cs):
        raise ValueError('map cell without its certifications')
    rd_ = r.get('reading')
    form = [f for f in CELL_FORMS if isinstance(rd_, str) and rd_.startswith(f)]
    if len(form) != 1:
        raise ValueError('map cell reading of another form: %r' % (rd_,))
    j0 = r.get('j0') if form[0] == 'j₀ = ' else None
    if form[0] == 'j₀ = ' and not isinstance(j0, int):
        raise ValueError('map cell with an index and no j0')
    return r['sigma'], r['t'], ('j₀' if form[0] == 'j₀ = ' else form[0].strip(' =(')), j0


READERS = ('read_runner_row', 'read_score_row', 'read_head', 'read_grade_row', 'read_print_row', 'read_map_cell')


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R272)(1), (2), (4)
WH = ('*Appended 2026-10-13 by b662 to b661’s entry (:8485), under `(R272)`(1) -- b661 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b661_closing.txt):*')
FH = ('*Appended 2026-10-13 by b662 beneath the detection map’s line (:14070), under `(R272)`(2) -- THE EMPTY MAP AS A FINDING:*')
EH = ('### `W-ORD-E2-SEPARATION` -- A SEPARATION ESTIMATE FOR THE RATE’S CONSTANT, PRICED, NOT STARTED, appended 2026-10-13, b662, '
      'under the author’s ruling `(R272)`(2)')
CH = ('*Appended 2026-10-13 by b662 beneath W-ORD-CITATION-CHECK (:13840), under `(R272)`(4) -- W-ORD-CITATION-CHECK ACTED, A GATE STEP FROM '
      'b662:*')


def _weight():
    return ('\n' + WH + ' the binding at v0.28 whole (relay data/b661_e1cfg_binding.txt); the map (relay data/b661_detection_map.txt) -- Z₁ '
            'the four-point orbit plus ζ’s 649 zeros to height 1,000 at 200 bits, every hypothesis but hrate certified by name in all 20 cells, '
            'no HYP-UNVERIFIED, every cell NONE ≤ J_max, D rising with the kill set (8, 14, 28, 66 at t = 14.1, 29.6, 50, 100), θ within '
            '7.2·10⁻⁴ of 1 in every cell, set by the lowest genuine zero above t; the control outside the map (relay data/b661_map_control.txt): '
            'at (0.8, 29.6) hrate holds from j = 31 and the zero side there is below 0; H1 and H4 held, H2 held vacuously, H3 not scorable; '
            'the entry (FINDINGS :8485) saying hrate is sufficient, not necessary; relay 6cca73cf, PLACE-papers 13ee2d4, the root 9d223d09…, '
            'the suite 75 of 77 with G-AXIOM-CLAIM carried and G-SHARED-ADDITIVE on b660’s in-place rewrite of a line of '
            'data/b650_same_season_last_year.txt (7ebd1c4d), both declared; four defects, (a) and (b) the navigator’s, (c) and (d) the seat’s. '
            'Nothing deposited.\n')


def _finding():
    return ('\n' + FH + ' every cell of b661’s map read NONE ≤ J_max (relay data/b661_detection_map.txt, rows are cells). The compiled '
            'rate’s constant θ -- the largest offScore/M over the configuration’s points outside the tie and kill sets -- is set in every cell '
            'by the lowest genuine ordinate above t (14.13, 30.42, 52.97, 101.32 at t = 14.1, 29.6, 50, 100) and lies within 7.2·10⁻⁴ of 1; it '
            'moves with σ at fixed t by less than 5·10⁻⁶ (at t = 29.6, 0.9996784 at σ = 0.55 and 0.9996774 at σ = 0.9): it is set by the '
            'spacing to the nearest genuine zero, not by the hypothetical zero’s distance from the line, so the sufficient index does not '
            'separate σ = 0.55 from σ = 0.9. At the control cell (0.8, 29.6) the index is j = 31, the window’s power 2^32 (relay '
            'data/b661_map_control.txt); J_max = D + 8 = 22 fell short of it by 9 indices, 22 of 31 -- the navigator’s, banked (relay '
            'data/b662_defects.txt (c), (d)). This is b559’s (E2) (relay data/b559_constants.txt :153: θ has no bound below 1 in terms of the '
            'excluded zero) returned with a number. W-ORD-E2-SEPARATION entered beside it (next line).\n')


def _e2():
    return ('\n' + EH + '\n\n**Items.** A bound for zeroSide_neg_at_rate_cfg’s θ (SIDE-explicit-formula v0.28, Schema/RateIndexCfg.lean :140-:142) '
            'below 1 in terms of the hypothetical zero alone -- b559’s (E2): θ has no such bound while a genuine zero’s score nearly ties the '
            'dominant’s (relay data/b559_constants.txt :153-:159); CV grows as tie nodes approach; Nρ tends to 0 as a tie node approaches a kill '
            'node. E2 needs a lower bound on the separation of ζ’s zeros near the dominant’s score, or a route that does not interpolate on '
            'nodes; no compiled lemma and no ZeroConfig field carries it. **Price:** research grade, not one lemma (b559 :157-:158); the '
            'closed-form route (b554, OPEN_TRAILS :11332, C1-C5) priced at three of substance; b661’s banks give the number it must move -- θ '
            'within 7.2·10⁻⁴ of 1 at every cell, the index 31 at (0.8, 29.6). **Trigger:** the empty map as a finding (the line above). '
            '**Acted:** after the Epstein control, in the research order the author set at b660 (W-ORD-EPSTEIN-ZQ, then the Keiper face, '
            'then the χ-Li converse).\n')


def _citation():
    return ('\n' + CH + ' from this act, before the ferry is banked, the seat checks every path, line, bank, branch, tag, tool and named rule '
            'the ruling and ferry cite for existence at HEAD and prints the misses; a miss is raised to the author before the component that '
            'cites it runs, not repaired silently; the print is banked as data/bNNN_citation_check.txt and read by the suite; a gate step, no '
            'new standing arm (`(R272)`(4)). At b662: 59 cites, 54 OK, 5 misses (relay data/b662_citation_check.txt), raised in one prompt '
            'before Component 1, each recorded as the navigator’s (relay data/b662_defects.txt (a)-(d)). ACTED.\n')


def c1(*a):
    items = [('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', FH, _finding()), ('OPEN_TRAILS.md', EH, _e2()), ('OPEN_TRAILS.md', CH, _citation())]
    land(items, 'b662_record_lines.json', 'c1', entry=K.B661_ENTRY,
         check=[('FINDINGS.md', K.B661_ENTRY, '## The detection-index map at Z'),
                ('OPEN_TRAILS.md', K.MAP_LINE, 'THE DETECTION MAP RE-ENTERED'),
                ('OPEN_TRAILS.md', K.CITATION_LINE, 'W-ORD-CITATION-CHECK, ENTERED WITH ITS TRIGGER'),
                ('OPEN_TRAILS.md', K.B661_TRAIL, '### b661 — lane two, act eighty-eight')],
         dry='dry' in a)


# ================================================================================ THE AUTHOR'S ANSWERS (b661's route, carried)
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
    """data/b662_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
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
    head = ['### b662 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b662_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b662_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 3: THE SENTENCE ROWS, THE PLAIN COMMENTS, THE GRADES
def _bank_line(bank_lines, rid_tail):
    for i, l in enumerate(bank_lines, 1):
        if l.startswith('  %s@%s:%s |' % (K.KERNEL, K.B647_REV, rid_tail)):
            return i
    return None


def sentences(*a):
    """(R272)(6), the b651 route as b657 and b659 ran it: the kernel's OVERREACHES, UNDERSTATES and UNLICENSED blocks of b647's bank (read at
    b3916cc) read into sentence rows at the kernel's main; a block whose text is not found at main is listed, not read;
    data/b662_table_<kernel>_sentences.txt and .json."""
    import b647_record as B7
    import licensed_table as LT
    N = _ws
    parents = [r for r in jl(K.PARENTS)['rows'] if r['verdict'] in ('OVERREACHES', 'UNDERSTATES', 'UNLICENSED')]
    bl = rdn(K.PARENTS.replace('.json', '.txt')).split(NL)
    ctx, orig = {}, LT.docstring_row

    def cap(rid, source, doc, *args, **kw):
        ctx.setdefault(N(doc), (source, args, kw))
        return orig(rid, source, doc, *args, **kw)
    LT.docstring_row = cap
    try:
        B7._kdoc_rows(K.KERNEL)
    finally:
        LT.docstring_row = orig
    rows, unread = [], []
    for p in parents:
        c = ctx.get(N(p['stated']))
        if c is None:
            unread.append(p)
            continue
        src, args, kw = c
        units = [s for s in B7._MSPLIT.split(p['stated'].strip()) if s.strip()]
        for j, u in enumerate(units, 1):
            r = orig('%s.s%d' % (p['id'], j), p['source'], u, *args, **kw)
            rows.append(dict(id=r['id'], parent=p['id'], parent_line=_bank_line(bl, p['source']), parent_verdict=p['verdict'], kind=p['kind'],
                             n=j, of=len(units), sentence=N(u), generated=r['verdict'], findings=r.get('findings') or [],
                             hand_needed=r.get('hand_needed'), at_main=src))
    import collections
    gc = collections.Counter(x['generated'] for x in rows)
    main = g(K.KD, 'rev-parse', '--short=7', 'main').strip()
    L = ['b662 -- COMPONENT 3, (R272)(6): %s`S OVERREACHES, UNDERSTATES AND UNLICENSED BLOCKS READ INTO SENTENCE ROWS (%s)' % (K.KERNEL, utc()), '',
         '### rows are sentences, parents are blocks. The parents: relay data/%s, its OVERREACHES, UNDERSTATES and UNLICENSED rows (%d), read at %s; '
         'the generator: b647_record._kdoc_rows at %s main %s, each block`s context captured and each unit read by licensed_table.docstring_row; the '
         'unit: b647_record._MSPLIT as b658 repaired it -- the b651 route. A GENERATED reading per sentence; the HAND reading per sentence is the '
         'grade bank`s.' % (K.PARENTS, len(parents), K.B647_REV, K.KERNEL, main),
         '### parents read %d ; parents not found at main %d (%s)' % (len(parents) - len(unread), len(unread),
                                                                       '; '.join('%s (%s)' % (u['source'], u['decl'] or u['kind']) for u in unread) or 'none'), '']
    cur = None
    for x in rows:
        if x['parent'] != cur:
            cur = x['parent']
            L += ['', '== %s (%s ; b647`s bank line :%s ; at main %s ; HAND %s ; %d sentences)' % (
                x['parent'].split(':', 1)[1], x['kind'], x['parent_line'], x['at_main'], x['parent_verdict'], x['of'])]
        L.append('  s%d %-11s %s' % (x['n'], x['generated'], x['sentence'][:600]))
    L += ['', '### ### **PARENT BLOCKS %d ; NOT FOUND AT MAIN %d ; SENTENCE ROWS %d ; GENERATED: %s ; HAND PER SENTENCE: the grade bank`s.**' % (
        len(parents) - len(unread), len(unread), len(rows), ', '.join('%s %d' % kv for kv in sorted(gc.items())))]
    put_txt('b662_table_%s_sentences.txt' % K.KERNEL, [l.replace('\r', '') for l in L])
    put_json(K.SENT, dict(at=utc(), main=main, rows=rows, unread=[u['id'] for u in unread]))
    print(NL.join(L[2:4] + L[-1:]))


# ### the needle of b650's finding (relay data/b650_resonances_navigator.txt :25; OPEN_TRAILS :13836), b655's
NEEDLE = re.compile(r'no off[- ]line zero|all (?:the )?(?:nontrivial |non-trivial )?zeros? (?:lie |are |sit )?on|zeros? on (?:the )?(?:critical line|'
                    r'σ ?= ?1/2|sigma ?= ?1/2|re ?s ?= ?1/2)|(?:\bRH\b|\bGRH\b|Riemann Hypothesis)\W{0,3}(?:holds|is (?:true|proved|proven|established))|'
                    r'(?:proves?|proof of|establish(?:es)?) (?:the )?(?:\bRH\b|\bGRH\b|Riemann Hypothesis)', re.I)


def _plain_blocks(text):
    """every plain block comment `/- ... -/` in a file (not `/--`, not `/-!`), with its first line; nesting followed."""
    out, i, n = [], 0, len(text)
    while i < n:
        j = text.find('/-', i)
        if j < 0:
            break
        if text.startswith('/--', j) or text.startswith('/-!', j):
            k, depth = j + 3, 1
        else:
            k, depth = j + 2, 1
        while k < n and depth:
            if text.startswith('/-', k):
                depth += 1
                k += 2
            elif text.startswith('-/', k):
                depth -= 1
                k += 2
            else:
                k += 1
        if not (text.startswith('/--', j) or text.startswith('/-!', j)):
            out.append((text[:j].count(NL) + 1, text[j:k]))
        i = k
    return out


def plain(*a):
    """(R272)(6): the kernel's plain block comments at its main scanned by the needle, then by a wider shape read by hand; `plain <hand reading>
    <asserting count>` banks the hand reading."""
    import b647_record as B7
    files = [f for f in g(K.KD, 'ls-files', '*.lean').split(NL) if f.strip()]
    nblocks, hits = 0, []
    for f in files:
        t = _show(K.KD, 'main', f) or ''
        for ln, b in _plain_blocks(t):
            nblocks += 1
            for s in B7._MSPLIT.split(_ws(b.strip('/-'))):
                if NEEDLE.search(s):
                    hits.append((f, ln, _ws(s)))
    ctl = [s for s in ('NO OFF-LINE ZERO EXISTS.', 'Therefore: all nontrivial zeros on σ = 1/2.', 'The Riemann Hypothesis holds.') if NEEDLE.search(s)]
    neg = [s for s in ('the zero side is negative', 'a zero of zeta off the line is excluded at the window') if NEEDLE.search(s)]
    L = ['b662 -- COMPONENT 3, (R272)(6): %s`S PLAIN BLOCK COMMENTS SCANNED BY THE NEEDLE (%s)' % (K.KERNEL, utc()), '',
         '### rows are plain block comments (`/-`, not `/--`, not `/-!`) of the kernel`s tracked .lean files at main %s; the needle: a sentence asserting '
         'the unsupported claim, b650`s finding (relay data/b650_resonances_navigator.txt :25, OPEN_TRAILS :13836) -- b655`s NEEDLE, carried.' % (
             g(K.KD, 'rev-parse', '--short=7', 'main').strip()),
         '### the needle`s controls: b650`s two sentences and a planted one read %d of 3 ; two sentences that assert nothing of the kind read %d of 2.' % (
             len(ctl), len(neg)),
         '### files %d ; plain block comments %d ; needle hits %d:' % (len(files), nblocks, len(hits))]
    L += ['  %s:%d -- %s' % h for h in hits] or ['  NONE']
    wide = []
    W = re.compile(r'\bRH\b|\bGRH\b|Riemann|critical line|off-line|nontrivial zero|zeros? of (?:ζ|zeta|L)', re.I)
    for f in files:
        t = _show(K.KD, 'main', f) or ''
        for ln, b in _plain_blocks(t):
            for s in B7._MSPLIT.split(_ws(b.strip('/-'))):
                if W.search(s):
                    wide.append((f, ln, _ws(s)))
    L += ['### THE WIDER SHAPE (RH, GRH, Riemann, the critical line, off-line, nontrivial zeros, zeros of zeta or L), read by hand: %d sentences' % len(wide)]
    L += ['  %s:%d -- %s' % (f, ln, s[:300]) for f, ln, s in wide]
    L += ['  the hand reading: %s' % (a[0] if a else '### NOT READ')]
    L += ['', '### ### **PLAIN BLOCK COMMENTS %d ; NEEDLE HITS %d ; CONTROLS %d OF 3 READ, %d OF 2 QUIET ; WIDER SHAPE %d, ASSERTING ROWS BY HAND %s.**' % (
        nblocks, len(hits), len(ctl), 2 - len(neg), len(wide), (a[1] if len(a) > 1 else '?'))]
    put_txt('b662_plain_comments.txt', L)
    put_json('b662_plain_comments.json', dict(at=utc(), files=len(files), blocks=nblocks, hits=[list(h) for h in hits], controls=[len(ctl), 2 - len(neg)],
                                              wide=len(wide), asserting=(a[1] if len(a) > 1 else None)))
    print(NL.join(L[3:]))


def blocks():
    """[(k, parent id, parent row, [sentence rows])] in the sentence bank's order, k from 1."""
    import collections
    s = jl(K.SENT)['rows']
    t = dict((r['id'], r) for r in jl(K.PARENTS)['rows'])
    by = collections.OrderedDict()
    for r in s:
        by.setdefault(r['parent'], []).append(r)
    return [(k, p, t[p], rs) for k, (p, rs) in enumerate(by.items(), 1)]


BULLET = re.compile(r'\s(?=· )')


def split_rows(rs, split):
    """the block's rows, keyed by sentence number as text; a sentence named in `split` read as its bullet rows `n.1`, `n.2`, ..."""
    out = []
    for r in rs:
        if str(r['n']) in split:
            for i, part in enumerate([p for p in BULLET.split(r['sentence']) if p.strip()], 1):
                out.append(dict(n='%d.%d' % (r['n'], i), sentence=_ws(part)))
        else:
            out.append(dict(n=str(r['n']), sentence=r['sentence']))
    return out


def _rows_of(k, rs0, G):
    """the block's rows as the grade bank reads them: the sentence rows, then the seat's joins (G['joins'][k] = [[a, b]]), its breaks (a row
    broken before each named marker, the pieces numbered n.1, n.2, ...: G['breaks'][k] = {n: [markers]}) and b655's bullet split (G['split']).
    Every marker must occur in its row, in order; the rows joined whitespace-wise always equal the block's sentences joined -- the check exits
    otherwise."""
    rows = [dict(n=str(r['n']), sentence=r['sentence']) for r in rs0]
    for a, b in (G.get('joins') or {}).get(str(k)) or []:
        ia = next(i for i, r in enumerate(rows) if r['n'] == str(a))
        ib = next(i for i, r in enumerate(rows) if r['n'] == str(b))
        if ib != ia + 1:
            sys.exit('### BLOCK %d: A JOIN OF ROWS NOT ADJACENT -- NOTHING WRITTEN' % k)
        rows[ia] = dict(n=str(a), sentence=rows[ia]['sentence'] + ' ' + rows[ib]['sentence'])
        del rows[ib]
    br = (G.get('breaks') or {}).get(str(k)) or {}
    out = []
    for r in rows:
        ms = br.get(r['n'])
        if not ms:
            out.append(r)
            continue
        s, parts, pos = r['sentence'], [], 0
        for m in ms:
            j = s.find(m, pos + 1)
            if j < 0:
                sys.exit('### BLOCK %d s%s: A BREAK MARKER NOT FOUND IN ORDER -- NOTHING WRITTEN: %r' % (k, r['n'], m))
            parts.append(s[pos:j])
            pos = j
        parts.append(s[pos:])
        out += [dict(n='%s.%d' % (r['n'], i), sentence=_ws(p)) for i, p in enumerate(parts, 1)]
    if _ws(' '.join(x['sentence'] for x in out)) != _ws(' '.join(x['sentence'] for x in rs0)):
        sys.exit('### BLOCK %d: THE ROWS DO NOT REJOIN TO THE BLOCK`S SENTENCES -- NOTHING WRITTEN' % k)
    return split_rows([dict(n=x['n'], sentence=x['sentence']) for x in out], (G.get('split') or {}).get(str(k)) or {}) \
        if (G.get('split') or {}).get(str(k)) else out


def cut(rows, graded, action, bullets=False, premise=None, row_actions=None):
    """the mechanical rule (b655's, b657's): a graded OVERREACHES or UNDERSTATES row replaced in place by the ACTION (by its sentences), an
    UNLICENSED one removed, MATCHES untouched; then a sentence repeating one already in the block dropped; a graded row named in `row_actions`
    replaced by its own ACTION span (a verbatim span of the block's ACTION), whatever its verdict. Returns (kept, dropped, note)."""
    import b647_record as R47
    row_actions = row_actions or {}
    act = action[len('RE-CUT: '):] if action.startswith('RE-CUT: ') else action
    abul = [p for p in BULLET.split(act.strip()) if p.strip()]
    out, gi = [], 0
    for r in rows:
        gr = graded.get(r['n'])
        if gr is None:
            out.append((r['n'], r['sentence']))
        elif r['n'] in row_actions:
            ra = row_actions[r['n']]
            ra = ra[len('RE-CUT: '):] if ra.startswith('RE-CUT: ') else ra
            out.append((r['n'], _ws(ra)))
        elif gr == 'UNLICENSED':
            continue
        elif bullets:
            out.append((r['n'], _ws(abul[min(gi, len(abul) - 1)])))
            gi += 1
        else:
            out += [(r['n'], x) for x in R47._MSPLIT.split(act.strip()) if x.strip()]
    note = ''
    keep_at = {}
    if premise:
        c, p = str(premise['conclusion']), str(premise['premise'])
        pos_p = next((i for i, (n, _x) in enumerate(out) if n == p), None)
        csent = [x for n, x in out if n == c]
        if csent and pos_p is not None:
            idx = [i for i, (_n, x) in enumerate(out) if _ws(x) == _ws(csent[0])]
            after = [i for i in idx if i > pos_p]
            keep_at[_ws(csent[0])] = after[0] if after else idx[0]
            note = 'the conclusion row s%s drawn on the premise row s%s; it stands after its premise' % (c, p)
    kept, dropped, seen = [], [], set()
    slots = []
    for i, (_n, x) in enumerate(out):
        w = _ws(x)
        if w in keep_at:
            if i == keep_at[w]:
                kept.append(x)
                slots.append((_n, x, True))
            else:
                dropped.append(x)
                slots.append((_n, x, False))
            continue
        if w in seen:
            dropped.append(x)
            slots.append((_n, x, False))
            continue
        seen.add(w)
        kept.append(x)
        slots.append((_n, x, True))
    cut.slots = slots
    return kept, dropped, note


def _bank_line_text(bank, line):
    """one line of a relay bank, as the bank has it (the re-grade's cell, (R267)(3)'s change-bank rule)."""
    t = rd(os.path.join(ROOT, *bank.split('/'))).split(NL)
    if not (0 < line <= len(t)):
        sys.exit('### %s HAS NO LINE %d -- NOTHING WRITTEN' % (bank, line))
    return t[line - 1]


def _row_cells(k, q):
    """per block k: {sentence number: (verdict, LICENSED cell, ACTION span or None, source)} for its graded rows: a re-grade's bank line, else the
    parent's cells with the row's own ACTION span where the grades name one."""
    G = jl(K.GRADES)
    ra = (G.get('row_actions') or {}).get(str(k)) or {}
    out = {}
    for n, e in ((G.get('regrade') or {}).get(str(k)) or {}).items():
        if e['verdict'] != 'UNRESOLVED':
            out[n] = (e['verdict'], _bank_line_text(e['bank'], e['line']), ('RE-CUT: ' + e['action']) if e.get('action') else None,
                      'relay %s :%d' % (e['bank'], e['line']))
    for n in ra:
        out[n] = (q['verdict'], q['licensed'], ra.get(n), 'the parent block')
    return out


def grades(*a):
    """(R272)(6): data/b662_sentence_grades.txt from the hand grades (data/b662_sentence_grades.json), every quoted word read as a verbatim
    substring of the row's LICENSED cell before anything is written; each row ACTION span read as a verbatim span of the block's ACTION; the cut
    plan beside it."""
    G = jl(K.GRADES)
    gr = G['grades']
    comp = G.get('completed') or {}
    L = ['b662 -- COMPONENT 3, (R272)(6): %s`S SENTENCE ROWS GRADED BY HAND, BOUND TO THE PARENT BLOCK`S HAND CELLS; BANKED FOR THE AUTHOR`S '
         'STRIKE BEFORE ANY EDIT (%s)' % (K.KERNEL, utc()), '',
         '### the rule (b652`s, (R265)(2), as (R267)(3) and (R272)(6) carry it): a sentence row is graded OVERREACHES, UNDERSTATES or UNLICENSED where',
         '### the parent block`s HAND LICENSED or CITED cell names, quotes or paraphrases that sentence`s claim, the grade citing the cell`s words beside',
         '### it; a sentence those cells do not reach stays MATCHES; a block whose cells reach no sentence is UNRESOLVED, not cut; an ACTION carrying',
         '### "..." is UNRESOLVED-CELL. The grade is the parent`s verdict. Where a block`s ACTION re-cuts several items, a graded row may carry its own',
         '### span of that ACTION (verbatim). The sources: relay data/%s, data/%s (b647, read at %s); the blocks read at main %s (unmoved since b647: no' % (
             K.SENT, K.PARENTS, K.B647_REV, K.K_MAIN),
         '### change bank, no re-grade); the hand grades: data/%s.' % K.GRADES,
         '### Below each block: the block as the mechanical rule leaves it -- graded rows replaced in place, repeats dropped and printed.', '']
    n_rows = n_graded = n_unres = n_drop = n_cell = 0
    by_v, J, unres = {}, [], []
    SPLIT, PREM = G.get('split') or {}, G.get('premise') or {}
    UNACT = G.get('unacted') or {}
    n_unact = 0
    for k, p, q, rs0 in blocks():
        split = (SPLIT.get(str(k)) or {})
        rs = _rows_of(k, rs0, G)
        n_rows += len(rs)
        cells = _row_cells(k, q)
        un = UNACT.get(str(k)) or {}
        for n, (w, why) in un.items():
            if w not in q['licensed'] or n not in [r['n'] for r in rs]:
                sys.exit('### BLOCK %d s%s: AN UNACTED ROW`S WORDS NOT IN THE CELL, OR NO SUCH ROW -- NOTHING WRITTEN' % (k, n))
        rg = (G.get('regrade') or {}).get(str(k)) or {}
        for n, e in rg.items():
            bl = _bank_line_text(e['bank'], e['line'])
            if e['words'] not in bl or n not in [r['n'] for r in rs]:
                sys.exit('### BLOCK %d s%s: A RE-GRADED ROW`S WORDS NOT ON ITS BANK LINE, OR NO SUCH ROW -- NOTHING WRITTEN' % (k, n))
        mine = dict((n, w) for _k, n, w in (read_grade_row(k, x) for x in gr.get(str(k), [])))
        for n, w in mine.items():
            lic = cells[n][1] if n in cells else q['licensed']
            if w not in lic:
                sys.exit('### BLOCK %d s%s: A QUOTED WORD NOT IN ITS LICENSED CELL -- NOTHING WRITTEN: %s' % (k, n, w))
        far = [n for n in mine if n not in [r['n'] for r in rs]]
        if far:
            sys.exit('### BLOCK %d: A GRADED ROW THE BLOCK DOES NOT HAVE -- NOTHING WRITTEN: %s' % (k, far))
        action = q['action']
        for n, c in cells.items():
            if c[3] == 'the parent block' and c[2] is not None:
                span = c[2][len('RE-CUT: '):] if c[2].startswith('RE-CUT: ') else c[2]
                if span not in action:
                    sys.exit('### BLOCK %d s%s: A ROW ACTION NOT A VERBATIM SPAN OF THE BLOCK`S ACTION -- NOTHING WRITTEN' % (k, n))
        v = q['verdict']
        L.append('== #%d %s (b647`s bank line :%s ; at main %s ; %s ; HAND %s ; %d sentence rows%s)' % (
            k, p.split(':', 1)[1], rs0[0]['parent_line'], rs0[0].get('at_main'), q['kind'], v, len(rs),
            ('; s%s read as its bullet rows' % ', s'.join(split)) if split else ''))
        L.append('   LICENSED : ' + q['licensed'])
        L.append('   ACTION   : ' + q['action'])
        elided_by_rows = False
        if '...' in q['action']:
            n_cell += 1
            c = comp.get(str(k))
            if c:
                L.append('   ### UNRESOLVED-CELL: the ACTION carries "..."; completed from the block`s own LICENSED words for the strike: %s' % c)
                span = c[len('RE-CUT: '):] if c.startswith('RE-CUT: ') else c
                if span.rstrip('.') not in q['licensed']:
                    sys.exit('### BLOCK %d: A COMPLETION NOT A SPAN OF THE LICENSED CELL -- NOTHING WRITTEN' % k)
                L.append('   ### the completion is a verbatim span of the LICENSED cell; words from outside it 0.')
                action = c
            else:
                elided_by_rows = True
                L.append('   ### UNRESOLVED-CELL: the ACTION carries "..."; each graded row takes its own verbatim span of the ACTION`s words after the '
                         'elision, for the strike (no completion composed).')
        graded, row_actions = {}, {}
        for r in rs:
            if r['n'] in mine:
                c = cells.get(r['n'])
                rv = c[0] if c else v
                graded[r['n']] = rv
                if c and c[2] is not None:
                    row_actions[r['n']] = c[2]
                n_graded += 1
                by_v[rv] = by_v.get(rv, 0) + 1
                L.append('  s%-4s %-11s %s' % (r['n'], rv, r['sentence']))
                L.append('        %-11s cell: "%s"%s' % ('', mine[r['n']], (' (%s)' % c[3]) if c and c[3] != 'the parent block' else ''))
                if r['n'] in row_actions:
                    L.append('        %-11s its ACTION: %s' % ('', row_actions[r['n']]))
            elif r['n'] in rg and rg[r['n']]['verdict'] == 'UNRESOLVED':
                n_unact += 1
                e = rg[r['n']]
                L.append('  s%-4s %-11s %s' % (r['n'], 'MATCHES', r['sentence']))
                L.append('        ### UNRESOLVED, RE-GRADED AT MAIN %s against relay %s :%d ("%s"): %s' % (
                    K.K_MAIN, e['bank'], e['line'], e['words'], e['reason']))
            elif r['n'] in un:
                n_unact += 1
                L.append('  s%-4s %-11s %s' % (r['n'], 'MATCHES', r['sentence']))
                L.append('        ### REACHED BY THE CELL ("%s"), NO ACTION TEXT FOR THIS ROW -- NOT CUT, RAISED FOR THE STRIKE: %s' % tuple(un[r['n']]))
            else:
                L.append('  s%-4s %-11s %s' % (r['n'], 'MATCHES', r['sentence']))
        if elided_by_rows and [n for n in graded if n not in row_actions]:
            sys.exit('### BLOCK %d: AN ELIDED ACTION AND A GRADED ROW WITHOUT ITS OWN SPAN -- NOTHING WRITTEN' % k)
        if not graded:
            n_unres += 1
            unres.append(k)
            L.append('   ### UNRESOLVED: %s; not cut.' % ('every row the cells reach is listed above, with its reason' if (un or rg)
                                                        else 'no sentence the cells reach'))
            J.append(dict(k=k, parent=p, file=q['file'], line=q['line'], unresolved=True))
            L.append('')
            continue
        prem = PREM.get(str(k))
        kept, dropped, note = cut(rs, graded, action, bullets=bool(split), premise=prem, row_actions=row_actions)
        n_drop += len(dropped)
        L.append('   -> THE BLOCK AFTER THE CUT (%d sentences; repeats dropped %d):' % (len(kept), len(dropped)))
        L += ['        ' + x for x in kept] + ['        ### DROPPED AS A REPEAT: ' + x for x in dropped]
        J.append(dict(k=k, parent=p, file=q['file'], line=q['line'], bank_line=rs0[0]['parent_line'], verdict=v, graded=sorted(graded),
                      verdicts=graded, row_actions=row_actions, action=action, completed=('...' in q['action']), kept=kept, dropped=dropped,
                      sentences=[r['sentence'] for r in rs0], split=sorted(split), premise=prem))
        L.append('')
    pl = jl('b662_plain_comments.json')
    unread = jl(K.SENT).get('unread') or []
    L.append('### PARENT BLOCKS NOT FOUND AT MAIN (listed, not graded): %s' % ('; '.join(unread) or 'NONE'))
    L.append('### PLAIN-COMMENT ROWS (relay data/b662_plain_comments.txt): %s' % ('; '.join('%s:%d -- %s' % tuple(h) for h in pl.get('hits') or []) or 'NONE'))
    L.append('### ROWS LISTED UNRESOLVED WITH THEIR REASONS (not cut): %d' % n_unact)
    n_cut = len([b for b in J if b.get('kept') is not None])
    files = sorted(set(b['file'] for b in J if b.get('kept') is not None))
    L.append('### ### **PARENT BLOCKS %d ; SENTENCE ROWS %d ; GRADED %d (%s) ; MATCHES %d ; UNRESOLVED BLOCKS %d (%s) ; UNRESOLVED-CELL %d ; '
             'NOT FOUND AT MAIN %d ; BLOCKS TO CUT %d IN %d FILES ; REPEATS DROPPED BY THE RULE %d ; PLAIN-COMMENT ROWS %d.**' % (
                 len(J), n_rows, n_graded, ', '.join('%s %d' % kv for kv in sorted(by_v.items())), n_rows - n_graded, n_unres,
                 ', '.join('#%d' % e for e in unres) or 'none', n_cell, len(unread), n_cut, len(files), n_drop, len(pl.get('hits') or [])))
    put_txt('b662_sentence_grades.txt', L)
    put_json('b662_sentence_cut_plan.json', dict(at=utc(), blocks=J))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE CUT PLANNED ON THE BLOBS (b655's, b659's, carried)
def _norm_map(text):
    out, idx, prev_ws = [], [], False
    for i, ch in enumerate(text):
        if ch.isspace():
            if not prev_ws:
                out.append(' ')
                idx.append(i)
            prev_ws = True
        else:
            out.append(ch)
            idx.append(i)
            prev_ws = False
    return ''.join(out), idx


def _wrap(text, indent, width=118):
    import textwrap
    return ('\n' + indent).join(textwrap.wrap(text, width - len(indent), break_long_words=False, break_on_hyphens=False)) or ''


def _code_only(t):
    out, i, depth, n = [], 0, 0, len(t)
    while i < n:
        if t.startswith('/-', i):
            depth += 1
            i += 2
            continue
        if depth and t.startswith('-/', i):
            depth -= 1
            i += 2
            continue
        if depth:
            i += 1
            continue
        if t.startswith('--', i):
            j = t.find(NL, i)
            i = n if j < 0 else j
            continue
        if t[i] == '"':
            j = i + 1
            while j < n and t[j] != '"':
                j += 2 if t[j] == chr(92) else 1
            out.append(t[i:j + 1])
            i = j + 1
            continue
        out.append(t[i])
        i += 1
    return ' '.join(''.join(out).split())


def _emph_parity(t):
    """per comment block: the parity of `**` and of a lone `*` (b657's defect (a), b658's repair: a cut must not unbalance emphasis). A lone `*`
    with whitespace on both sides (a multiplication, `2 * S`) opens and closes nothing in CommonMark and is not counted."""
    out = []
    for m in re.finditer(r'/-.*?-/', t, re.S):
        b = m.group(0)
        out.append((t[:m.start()].count(NL) + 1, b.count('**') % 2, len(re.findall(r'(?<!\*)(?<!\s)\*(?!\*)|(?<!\*)\*(?!\*)(?!\s)', b)) % 2))
    return out


def _plans():
    """per graded block: (k, q, rows, slots) -- the rows read as the grade bank reads them, the cut's slot outputs."""
    G = jl(K.GRADES)
    gr, comp, SPLIT, PREM = G['grades'], G.get('completed') or {}, G.get('split') or {}, G.get('premise') or {}
    out = []
    for k, p, q, rs0 in blocks():
        split = SPLIT.get(str(k)) or {}
        rs = _rows_of(k, rs0, G)
        cells = _row_cells(k, q)
        mine = dict((n, w) for _k, n, w in (read_grade_row(k, x) for x in gr.get(str(k), [])))
        graded = dict((r['n'], (cells[r['n']][0] if r['n'] in cells else q['verdict'])) for r in rs if r['n'] in mine)
        row_actions = dict((n, c[2]) for n, c in cells.items() if n in graded and c[2] is not None)
        if not graded:
            continue
        action = (comp.get(str(k)) or q['action']) if '...' in q['action'] else q['action']
        cut(rs, graded, action, bullets=bool(split), premise=PREM.get(str(k)), row_actions=row_actions)
        out.append((k, q, rs, cut.slots))
    return out


def plan_cut(*a):
    """(R272)(6): the cut planned on the kernel's main blobs at K_MAIN, b655's planner: every row of a graded block located in order in its file by
    its whitespace-collapsed text from the block's line at main; each changed row replaced in its span by its slot's kept output, wrapped at the
    line's indent; one edit per block. The planned file checked: its comment-stripped code equal to main's; the emphasis parity of every comment
    block unmoved."""
    files, edits, fails = {}, [], []
    S = dict((r['parent'], r) for r in jl(K.SENT)['rows'])
    for k, q, rs, slots in _plans():
        f = q['file']
        if f not in files:
            files[f] = (_show(K.KD, K.K_MAIN, f) or '').replace(chr(13), '')
        text = files[f]
        at = S[q['id']].get('at_main') or ''
        m = re.search(r':(\d+)$', at)
        line0 = int(m.group(1)) if m else q['line']
        start_line_off = sum(len(l) + 1 for l in text.split(NL)[:line0 - 1])
        norm, idx = _norm_map(text)
        nstart = next(i for i, ri in enumerate(idx) if ri >= start_line_off)
        spans, pos = {}, nstart
        for r in rs:
            s = _ws(r['sentence'])
            j = norm.find(s, pos)
            if j < 0:
                fails.append('#%d s%s not found' % (k, r['n']))
                break
            spans[r['n']] = (idx[j], idx[j + len(s) - 1] + 1)
            pos = j + len(s)
        if len(spans) != len(rs):
            continue
        out_by = {}
        for n, x, keep in slots:
            out_by.setdefault(n, []).append((x, keep))
        changed = [r['n'] for r in rs if [x for x, kp in out_by.get(r['n'], []) if kp] != [r['sentence']]]
        if not changed:
            continue
        reg0 = min(spans[n][0] for n in changed)
        reg1 = max(spans[n][1] for n in changed)
        new = text[reg0:reg1]
        for n in sorted(changed, key=lambda n_: -spans[n_][0]):
            s0, s1 = spans[n]
            line_start = text.rfind(NL, 0, s0) + 1
            indent = re.match(r'[ \t]*', text[line_start:]).group(0)
            repl = ' '.join(x for x, kp in out_by.get(n, []) if kp)
            repl = _wrap(repl, indent) if repl else ''
            a0, a1 = s0 - reg0, s1 - reg0
            if not repl:
                if a0 > 0:
                    while a0 > 0 and new[a0 - 1].isspace():
                        a0 -= 1
                else:
                    while a1 < len(new) and new[a1].isspace():
                        a1 += 1
            new = new[:a0] + repl + new[a1:]
        old = text[reg0:reg1]
        if text.count(old) != 1:
            fails.append('#%d region not unique in %s' % (k, f))
        edits.append(dict(k=k, file=f, line=line0, old=old, new=new, changed=changed))
    planned = {}
    for f, t in files.items():
        nt = t
        for e in [x for x in edits if x['file'] == f]:
            nt = nt.replace(e['old'], e['new'], 1)
        planned[f] = nt
    code_bad = [f for f in files if _code_only(files[f]) != _code_only(planned[f])]
    emph_bad = [f for f in files if [x[1:] for x in _emph_parity(files[f])] != [x[1:] for x in _emph_parity(planned[f])]]
    L = ['b662 -- COMPONENT 4, (R272)(6): THE CUT PLANNED ON %s`S MAIN BLOBS AT %s (%s)' % (K.KERNEL, K.K_MAIN, utc()), '',
         '### from relay data/b662_sentence_grades.txt (rows are sentences, parents are blocks) and its hand grades; each graded block`s rows located in',
         '### order in its file from the block`s line at main; each changed row replaced in its span by its slot`s kept output, wrapped at the line`s',
         '### indent; one edit per block.',
         '### files %d ; edits %d ; rows located %s ; regions not unique %s ; files whose comment-stripped code differs from main`s %s ; files whose '
         'comment blocks` emphasis parity moves %s' % (
             len(files), len(edits), 'ALL' if not [x for x in fails if 'not found' in x] else fails,
             [x for x in fails if 'unique' in x] or 'NONE', code_bad or 'NONE', emph_bad or 'NONE'), '']
    for e in edits:
        L += ['== #%d %s:%d (rows changed %s)' % (e['k'], e['file'], e['line'], ', '.join('s' + n for n in e['changed'])),
              '   OLD: ' + e['old'].replace(NL, ' | ')[:1600], '   NEW: ' + e['new'].replace(NL, ' | ')[:1600], '']
    L += ['### ### **FILES %d ; EDITS %d ; LOCATION FAILURES %d ; CODE OUTSIDE COMMENTS CHANGED IN %d FILES ; EMPHASIS PARITY MOVED IN %d FILES.**' % (
        len(files), len(edits), len(fails), len(code_bad), len(emph_bad))]
    put_txt('b662_cut_plan.txt', L)
    put_json('b662_cut_edits.json', dict(at=utc(), main=K.K_MAIN, edits=edits, planned_sha={f: __import__('hashlib').sha256(t.encode('utf-8')).hexdigest()
                                                                                           for f, t in planned.items()}, fails=fails, code_bad=code_bad,
                                         emph_bad=emph_bad))
    print(NL.join(L[5:6] + L[-1:]))


def _planned(f):
    j = jl('b662_cut_edits.json')
    t = (_show(K.KD, j['main'], f) or '').replace(chr(13), '')
    for e in [x for x in j['edits'] if x['file'] == f]:
        t = t.replace(e['old'], e['new'], 1)
    return t


def planned_text(*a):
    """`planned_text <file>`: prints the planned text of a cut file whole, for the seat to read before writing it by the Edit tool."""
    sys.stdout.write(_planned(a[0]))


def check_file(*a):
    """`check_file <file> [head]`: the working file (CR stripped) or the branch head's blob against the planned text, and its comment-stripped
    code against main's. Prints one line; exits 1 on a difference."""
    import hashlib
    f = a[0]
    want = _planned(f)
    if len(a) > 1 and a[1] == 'head':
        got = (_show(K.KD, K.CUT_BRANCH, f) or '')
        where = 'blob at %s' % K.CUT_BRANCH
    else:
        got = io.open(os.path.join(K.KD, f), encoding='utf-8', newline='').read().replace(chr(13), '')
        where = 'working file'
    main = (_show(K.KD, K.K_MAIN, f) or '').replace(chr(13), '')
    same, code = got == want, _code_only(got) == _code_only(main)
    print('  %-48s %s %s planned (sha %s) ; code outside comments %s main`s' % (
        f, where, 'EQUALS' if same else '### DIFFERS FROM', hashlib.sha256(got.encode('utf-8')).hexdigest()[:12],
        'EQUAL TO' if code else '### DIFFERENT FROM'))
    if not (same and code):
        sys.exit(1)


def _regrade(ref):
    """every graded row of the grade bank looked for in its file at `ref`, whitespace aside: standing or gone, by its verdict; gone when its
    sentence occurs fewer times in the file at `ref` than at main (b657's defect (b)); at main itself every graded row stands."""
    import collections
    G = jl(K.GRADES)
    files, mains, standing = {}, {}, []
    cnt = collections.Counter()
    for k, q, rs, _slots in _plans():
        cells = _row_cells(k, q)
        mine = set(n for _k, n, _w in (read_grade_row(k, x) for x in G['grades'].get(str(k), [])))
        f = q['file']
        if f not in files:
            files[f] = _ws(_show(K.KD, ref, f) or '')
            mains[f] = _ws(_show(K.KD, K.K_MAIN, f) or '')
        for r in rs:
            if r['n'] not in mine:
                cnt['MATCHES'] += 1
                continue
            v = cells[r['n']][0] if r['n'] in cells else q['verdict']
            s = _ws(r['sentence'])
            if s in files[f] and files[f].count(s) >= mains[f].count(s):
                standing.append((k, f, r['n'], v, r['sentence']))
                cnt[v + ' (STANDING)'] += 1
            else:
                cnt['CUT'] += 1
    return cnt, standing


def cut_bank(*a):
    """(R272)(6): data/b662_cut_<kernel>.txt -- the branch, its commits one per file, each head blob against the plan and its comment-stripped code
    against main's, printed per file, and the grade bank re-run at the branch with its control at main."""
    gk = lambda *x: g(K.KD, *x)   # noqa: E731
    log = [l.split(' ', 1) for l in gk('log', '--reverse', '--format=%h %s', K.K_MAIN + '..' + K.CUT_BRANCH).split(NL) if l.strip()]
    plan = jl('b662_cut_edits.json')
    pf = sorted(set(e['file'] for e in plan['edits']))
    rows, bad, extra = [], [], []
    for h, s in log:
        fs = [x for x in gk('show', '--name-only', '--format=', h).split(NL) if x.strip()]
        f = fs[0] if len(fs) == 1 else None
        if f is None:
            bad.append('%s touches %d files' % (h, len(fs)))
            continue
        if f not in pf:
            extra.append((h, f))
            continue
        head = _show(K.KD, K.CUT_BRANCH, f) or ''
        main = (_show(K.KD, K.K_MAIN, f) or '').replace(chr(13), '')
        eq, code = head == _planned(f), _code_only(head) == _code_only(main)
        if not (eq and code):
            bad.append(f)
        ks = [e['k'] for e in plan['edits'] if e['file'] == f]
        rows.append('  %s  %-48s blocks %-22s blob %s ; the comment-stripped diff against main %s' % (
            h, f, ', '.join('#%d' % k for k in ks), 'EQUALS THE PLAN' if eq else '### DIFFERS', 'EMPTY' if code else '### NOT EMPTY'))
    after, st = _regrade(K.CUT_BRANCH)
    ctl, st0 = _regrade(K.K_MAIN)
    L = ['b662 -- COMPONENT 4, (R272)(6): %s`S DOCSTRINGS CUT ON THE BRANCH %s (%s)' % (K.KERNEL, K.CUT_BRANCH, utc()), '',
         '### the grades: relay data/b662_sentence_grades.txt (rows are sentences, parents are blocks; the author`s word at Component 3); the plan:',
         '### data/b662_cut_plan.txt; one commit per file by the Edit tool, each working file checked against the plan before its commit; the',
         '### branch from main %s.' % K.K_MAIN, '',
         '### THE COMMITS (rows are commits, one per file):'] + rows + [
         '### the branch`s other commits (not a cut file, each touching one file): %s' % (['%s %s' % x for x in extra] or 'NONE'),
         '', '### COMMITS %d ; FILES IN THE PLAN %d ; CUT COMMITS TOUCHING ONE FILE %d ; FAULTS %s' % (len(log), len(pf), len(rows), bad or 'NONE'),
         '', '### THE GRADE BANK RE-RUN AT THE BRANCH (each graded row looked for in its file, whitespace aside):',
         '  ' + ', '.join('%s %d' % kv for kv in sorted(after.items())),
         '  graded rows still standing: %s' % (['#%d %s s%s %s' % x[:4] for x in st] or 'NONE'),
         '### THE CONTROL, the same read at main %s: ' % K.K_MAIN + ', '.join('%s %d' % kv for kv in sorted(ctl.items())), '',
         '### ### **CUT COMMITS %d IN %d FILES ; GRADED ROWS CUT %d ; STANDING %d (OVERREACHES %d, UNDERSTATES %d, UNLICENSED %d) ; AT MAIN STANDING %d ; '
         'FAULTS %d.**' % (len(rows), len(pf), after.get('CUT', 0), len(st), after.get('OVERREACHES (STANDING)', 0), after.get('UNDERSTATES (STANDING)', 0),
                           after.get('UNLICENSED (STANDING)', 0), len(st0), len(bad))]
    put_txt('b662_cut_%s.txt' % K.KERNEL, L)
    put_json('b662_cut_%s.json' % K.KERNEL, dict(at=utc(), commits=[x[0] for x in log], cut_commits=len(rows), extra=[list(x) for x in extra], files=len(pf),
                                                faults=bad, after=dict(after), standing=[list(x) for x in st], control=dict(ctl), control_standing=len(st0)))
    print(NL.join(L[-8:]))


# ================================================================================ COMPONENT 4: THE RUNNER, (R272)(6) under (R263)(4)
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
PRINT_RE = re.compile(r"^'(.+?)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", re.M)
ERR_RE = re.compile(r'^(?:error: )?(\S+\.lean):(\d+):(\d+): error: (.*)$', re.M)


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def _prints(text):
    return [(m.group(1), sorted(x.strip() for x in (m.group(2) or '').split(',') if x.strip())) for m in PRINT_RE.finditer(text)]


def _banked_prints(targets):
    """the kernel's banked profiles: its README's rows at the worklist's lines (main b3916cc), each through read_print_row; every short name
    mapped to the one print target ending in it. Returns ({full name: axioms}, [short names not mapped or mapped twice])."""
    f, a0, a1 = K.README_PROFILES
    out, bad = {}, []
    for l in (_show(K.KD, K.K_MAIN, f) or '').split(NL)[a0 - 1:a1]:
        if l.strip():
            n, ax = read_print_row(l)
            hits = [t for t in targets if t == n or t.endswith('.' + n)]
            if len(hits) != 1:
                bad.append(n)
                continue
            out[hits[0]] = ax
    return out, bad


def runner(*a):
    """`runner`: the run read by its id; the artifact listed, downloaded by its id into memory, its sha256 against the platform's digest before
    any reading; the build's exit and error lines, the memory log's low and any STOP, every print against the banked profile terminal by
    terminal. Banked as data/b662_runner_<kernel>.txt and a row of data/b662_runner_rows.json."""
    import hashlib
    import zipfile
    kern = K.KERNEL
    R = K.RUNNER[kern]
    repo = 'psinary-sketch/' + kern
    rc, out, err = _gh('run', 'view', str(R['run_id']), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, R['run_id']))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    wf = _show(K.KD, R['workflow_commit'], '.github/workflows/build-module.yml') or ''
    pt = [l.strip() for l in (_show(K.KD, R['ref'], 'print_targets.txt') or '').split(NL) if l.strip()]
    row = dict(kernel=kern, branch=R['branch'], ref=R['ref'], target=R['target'], run_id=R['run_id'], conclusion=run.get('conclusion'),
               artifact_sha256=None, mem_low=None, stopped=False, gate=None, merged=None, tag=None)
    L = ['b662 -- COMPONENT 4, (R272)(6): THE HOSTED RUNNER FOR %s, READ BY ITS RUN ID (%s)' % (kern, utc()), '',
         '### the workflow file on main (%s, put where absent under (R263)(4), the file alone), read back whole:' % R['workflow_commit']] + \
        ['    ' + l for l in wf.rstrip(NL).split(NL)] + ['', '### print_targets.txt at the ref: %d names' % len(pt), '',
         '### the refused call, before the dispatch: %s -- it ran nothing; the reason: the cut branch was cut from %s, before the workflow went '
         'onto main (relay data/b662_defects.txt (f)).' % (R['refused'], K.K_MAIN),
         '### the one dispatch, on the author`s word: at %s, the ref input %s (the cut branch`s tip) ; target %s' % (R['dispatched_at'], R['ref'], R['target']),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             R['run_id'], run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt'))]
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        row['artifact_sha256'] = sha
        L.append('### the artifact: id %s ; name %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if digest and digest == sha else ('### DIFFER' if digest else 'no digest to compare')))
        if digest and digest != sha:
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
    P = _prints(T_.get('axioms.txt', ''))
    B, unmapped = _banked_prints(pt)
    per = []
    for n, ax in P:
        b = B.get(n)
        per.append((n, ax, b, set(ax) <= STD3 and 'sorryAx' not in ax, b is not None and b == ax))
    missing = sorted(set(B) - set(n for n, _a in P))
    ok = (run.get('conclusion') == 'success' and row['artifact_sha256'] and bexit == '0' and not errs and not stops and row['mem_low'] is not None
          and row['mem_low'] >= K.HOLD and len(P) == len(B) == len(pt) > 0 and not missing and not unmapped and all(s and e for _n, _a, _b, s, e in per))
    row['gate'] = 'DERIVES' if ok else ('STOPPED BENEATH THE HOLD' if stops else 'NOT DERIVES')
    row['errors'] = [list(e) for e in errs]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: samples %d ; LOW %s MB ; the hold %d ; STOP lines %s' % (
              len([l for l in mem.split(NL) if 'avail_mb=' in l]), row['mem_low'], K.HOLD, stops or 'NONE'),
          '### the build: exit %s ; error lines %d ; the log`s last lines:' % (bexit or '### UNREAD', len(errs))] + \
        ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + ['    %s:%d:%d: %s' % e for e in errs[:30]] + [
          '### names refused by the print step: %s' % (T_.get('axioms_refused.txt', '').strip() or 'NONE'),
          '### THE BANKED PROFILES: the kernel`s README.md :%d-:%d at %s ("Axiom profiles at v0.4.1"), short names mapped to print targets: %d ; '
          'not mapped or mapped twice: %s ; no relay print bank exists for this kernel (listed for the next census)' % (
              K.README_PROFILES[1], K.README_PROFILES[2], K.K_MAIN, len(B), unmapped or 'NONE'),
          '### THE GATE READING PER TERMINAL (the run`s print ; the banked profile):'] + \
        ['  %-66s %-30s %s ; banked %s ; %s' % (n, ax, 'STANDARD THREE OR NONE' if s else '### NOT', b, 'EQUAL' if e else '### DIFFERENT')
         for n, ax, b, s, e in per] + ['  banked terminals not printed: %s' % (missing or 'NONE'), '',
          '### ### **RUN %s ; CONCLUSION %s ; ARTIFACT SHA256 %s ; MEMORY LOW %s MB (HOLD %d) ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS %d, AT THE '
          'STANDARD THREE OR NONE %d, EQUAL TO THE BANKED PROFILES %d ; GATE %s.**' % (
              R['run_id'], run.get('conclusion'), (row['artifact_sha256'] or '### NONE')[:16], row['mem_low'], K.HOLD, bexit or '### UNREAD', len(errs),
              len(P), sum(1 for x in per if x[3]), sum(1 for x in per if x[4]), row['gate'])]
    put_txt('b662_runner_%s.txt' % kern, L)
    j = jl('b662_runner_rows.json') or {'rows': []}
    j['rows'] = [r for r in (j.get('rows') or []) if r['kernel'] != kern] + [row]
    put_json('b662_runner_rows.json', j)
    print(L[-1])
    for e in errs[:12]:
        print('  ERROR %s:%d:%d: %s' % e)


def runner_merged(*a):
    """`runner_merged <merge sha> <tag>`: the row's merge and tag, after main and the tag are read back at the remote."""
    sha, tag = a[:2]
    j = jl('b662_runner_rows.json')
    for r in j['rows']:
        if r['kernel'] == K.KERNEL:
            r['merged'], r['tag'] = sha, tag
    put_json('b662_runner_rows.json', j)
    print('  %s merged %s tag %s' % (K.KERNEL, sha, tag))


ROUTES_EARLY = ('c1', 'answers', 'sentences', 'plain', 'grades', 'plan_cut', 'planned_text', 'check_file', 'cut_bank', 'runner', 'runner_merged')

if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith(('_', 'read_')):
        print('usage: b662_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
