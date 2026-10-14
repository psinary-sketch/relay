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


# ================================================================================ PART B: THE PLAN, THE LANDING, THE LATE ROUTES (written at their
# ================================================================================ components)
ROUTES = {'repair': repair, 'c1': c1, 'answers': answers}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b669_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
