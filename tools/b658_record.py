# -*- coding: utf-8 -*-
"""b658_record.py -- THE ACT'S RECORD TOOL, b658 under (R268).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b658's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows (tools/b658_regspec.py) can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b657_record.py (the landing, the readers, the answers, the capture, the commands, the kernels' face, the
### defects, the seal hashes, the root and its arm, the table, the scores' form, the record, the desk, the components, the dry run) and from
### b654_record.py (the runner over SIDE-explicit-formula); new here: (R268)(2)'s splitter run before and after its repair (`msplit`), and
### (R268)(3)-(4)'s statement bank read and the landing point banked (`landing`).
### Routes: `python tools/b658_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
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
import b658_worklist as K          # noqa: E402

STANDIN = bool(os.environ.get('B658_STANDIN'))


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
        'b658_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b658_findings.json': dict(entry_line=99999, title='stand-in'),
        'b658_trail.json': dict(line=99999),
        'b658_act_root.json': dict(root='0' * 64, previous='c2efb920' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b658's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b658_scanfile_%s.md' % tag)
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
    """a row of data/b658_runner_rows.json -- every key of RUNNER_KEYS present (None where a step did not reach it); returns the row's reading
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
    """a scores row: key N1..N5 or S1..S5, value [verdict, text]; returns (key, the whole verdict, text) -- the whole verdict, not its first
    word (b656's defect (e))."""
    if not re.match(r'^[NS][1-5]$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


TRACE_ROW = re.compile(r'^  (H\d+[a-z]?)  (\S.*?) -- CONSUMED AT (RateIndex\.lean :\d+(?:, :\d+)*|NO LINE)(?: -- (.*))?$')


def read_trace_row(line):
    """a hypothesis row of data/b658_e1cfg_statement.txt: `  H<n>  <binder> -- CONSUMED AT RateIndex.lean :<line>[, :<line>...] -- <how>` or
    `... -- CONSUMED AT NO LINE -- <why>`; returns (id, binder, [lines], how); raises on a row of another shape."""
    m = TRACE_ROW.match(line)
    if not m:
        raise ValueError('trace row of another shape: %r' % (line[:80],))
    lines = [int(x) for x in re.findall(r':(\d+)', m.group(3))] if m.group(3) != 'NO LINE' else []
    return m.group(1), m.group(2), lines, m.group(4) or ''


READERS = ('read_runner_row', 'read_score_row', 'read_head', 'read_trace_row')


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R268)(1), (2)
WH = ('*Appended 2026-10-12 by b658 to b657’s entry (:8383), under `(R268)`(1) -- b657 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b657_closing.txt):*')
EH = ('*Appended 2026-10-12 by b658 beneath the b657 record (:14022), its cell-refresh line (:14036), under `(R268)`(2) -- TWO UNBALANCED '
      'EMPHASES FOR SIDE-lv-conservation’S CELL REFRESH:*')


def _weight():
    return ('\n' + WH + ' SIDE-lv-conservation -- 39 of 40 blocks read at main b4c55b9 into 298 rows, the 40th restated and listed; 78 rows '
            'graded by hand with the cell’s words verbatim, sixteen re-graded against the change banks on the author’s word (two stale sentences '
            'removed, T2_SDarkness s10 replaced by b648’s sentence, thirteen UNRESOLVED with reasons; RegisterPentagon s22 and PinnedGoal s1–s2 '
            'named for a later cell refresh); the h1_complete_at_Phi sentence now b648’s; the cut in 12 commits, code unchanged outside '
            'comments, 0 rows standing at the branch; run 38305820585, memory low 12,672 MB, T3’s eight terminals equal to b653’s profiles; '
            'merged alone at 8e3bc76, tag v0.13.0; the dry run a gate step at OPEN_TRAILS :14020, both records CLEAN before the lock, no '
            'post-seal entry or trail defect; relay 640df77a, PLACE-papers 3f0e33f, FINDINGS :8381 and :8383, OPEN_TRAILS :14022, the root '
            'c2efb920…; the suite 78 of 79, the SIDE-cosmo row declared; three defects (relay data/b657_defects.txt), (a) the splitter dropping '
            'a closing `**` or `*` after a period (two unbalanced emphases in ZeroActingPartial.lean, in comments alone); the mirror at '
            'mirror-refresh-2026-10-12-b657.zip (MANIFEST md5 6f676855…). Nothing deposited.\n')


def _emphases():
    (f1, l1, _w1), (_f2, l2, _w2) = K.EMPHASES
    return ('\n' + EH + ' at main %s (v0.13.0), %s :%d carries a lone closing `*` after “is not compiled.” (its doc block from :101) and :%d '
            'three `**`, the opening one before “Three facts juxtaposed.” never closed (its block from :107) -- b657’s cut planned on a splitter '
            'that dropped a closing mark after a period (relay data/b657_defects.txt (a)); comments alone, the code unchanged. Listed for the '
            'kernel’s cell refresh with RegisterPentagon s22 and PinnedGoal s1–s2, not edited at b658 (no kernel branch opens for two '
            'asterisks); the splitter repaired at b658 (relay tools/b647_record.py `_MSPLIT`, its planted test tools/test_msplit_b658.py, '
            'relay data/b658_msplit.txt).\n' % (K.LV_MAIN, f1, l1, l2))


def c1(*a):
    items = [('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', EH, _emphases())]
    land(items, 'b658_record_lines.json', 'c1', entry=8383,
         check=[('FINDINGS.md', 8383, '## SIDE-lv-conservation’s docstrings at 78 sentence rows cut of 298'),
                ('OPEN_TRAILS.md', 14022, '### b657 — lane three, act eighty-four'),
                ('OPEN_TRAILS.md', K.CELL_REFRESH_LINE, '**Rows a later cell refresh reaches**')],
         dry='dry' in a)


# ================================================================================ (R268)(2): THE SPLITTER, BEFORE AND AFTER ITS REPAIR
OLD_SPLIT = re.compile(r'(?<=[.!?])["\'*)\]]*\s+(?=\S)')   # ### the split as b647 wrote it (tools/b647_record.py :846 before the repair)


def _blocks(text):
    return [(text[:m.start()].count(NL) + 1, _ws(m.group(0).strip('/-'))) for m in re.finditer(r'/-.*?-/', text, re.S)]


def _lost(split, t):
    us = [s for s in split.split(t.strip()) if s.strip()]
    return len(re.sub(r'\s', '', t)) - len(re.sub(r'\s', '', ''.join(us)))


def msplit(*a):
    """(R268)(2): the planted test run against the splitter before the repair (b647_record.py at relay `pre`, the commit before the repair) and
    after it (the working file); and the real state: every comment block of ZeroActingPartial.lean at SIDE-lv-conservation b4c55b9 (the text
    b657's cut was planned on), the characters each split loses. Banked as data/b658_msplit.txt and .json."""
    import tempfile
    pre = a[0] if a else 'HEAD~1'
    import b647_record as NEW
    out = {}
    with tempfile.TemporaryDirectory(prefix='b658_ms_') as d:
        old_path = os.path.join(d, 'b647_record.py')
        open(old_path, 'wb').write(subprocess.run(['git', '-C', ROOT, 'show', '%s:tools/b647_record.py' % pre], capture_output=True).stdout)
        for name, path in (('before', old_path), ('after', os.path.join(T, 'b647_record.py'))):
            r = subprocess.run([sys.executable, os.path.join(T, 'test_msplit_b658.py'), path], capture_output=True, text=True, encoding='utf-8',
                               errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'), cwd=ROOT)
            cases = [l for l in (r.stdout or '').split(NL) if re.match(r'^  \(\d+\) ', l)]
            fails = [re.match(r'^  (\(\d+\))', c).group(1) for c in cases if not c.rstrip().endswith('PASS')]
            out[name] = dict(rc=r.returncode, cases=len(cases), failing=fails, last=(r.stdout or '').strip().split(NL)[-1], output=r.stdout)
    pat_old = OLD_SPLIT.pattern
    if NEW._MSPLIT.pattern == pat_old:
        sys.exit('### THE SPLITTER IS NOT REPAIRED IN THE WORKING FILE -- NOTHING WRITTEN')
    src = _show(K.LV, 'b4c55b9', K.EMPHASES[0][0])
    real = [(ln, _lost(OLD_SPLIT, t), _lost(NEW._MSPLIT, t)) for ln, t in _blocks(src)]
    real = [x for x in real if x[1] or x[2]]
    L = ['b658 -- COMPONENT 1, (R268)(2): THE SENTENCE SPLITTER REPAIRED ON PLANTED CASES, RUN BEFORE AND AFTER (%s)' % utc(), '',
         '### the defect: b647`s split (relay tools/b647_record.py :846, `_MSPLIT`) took a closing quote, asterisk or bracket after . ! or ? as',
         '### part of the gap between sentences, so the mark belonged to neither unit and b657`s cut, planned on the units, dropped it: two',
         '### unbalanced emphases at SIDE-lv-conservation main %s, %s :%d and :%d (relay data/b657_defects.txt (a)).' % (
             K.LV_MAIN, K.EMPHASES[0][0], K.EMPHASES[0][1], K.EMPHASES[1][1]),
         '### the repair (the Edit tool): the split takes the whitespace alone, a fixed-width look-behind for . ! or ? followed by up to four',
         '### closing marks, so the marks stay with their sentence and the split points are the old ones (five or more marks: no split).',
         '###   before: %s' % pat_old, '###   after:  %s' % NEW._MSPLIT.pattern,
         '### the planted test, tools/test_msplit_b658.py (new, the Write tool); rows are its numbered cases.', '',
         '### BEFORE (b647_record.py at relay %s): cases %d ; failing %s ; exit %d ; %s' % (
             pre, out['before']['cases'], out['before']['failing'] or 'none', out['before']['rc'], out['before']['last']),
         '### AFTER (b647_record.py repaired): cases %d ; failing %s ; exit %d ; %s' % (
             out['after']['cases'], out['after']['failing'] or 'none', out['after']['rc'], out['after']['last']), '',
         '### THE REAL STATE: the comment blocks of %s at SIDE-lv-conservation b4c55b9 (the text b657 planned its cut on) where a split' % K.EMPHASES[0][0],
         '### loses a character other than whitespace (block`s first line | characters lost before | after):']
    L += ['  :%d | %d | %d' % x for x in real] or ['  (no block loses a character under either split)']
    summary = '### ### **BEFORE %d OF %d PASSING ; AFTER %d OF %d PASSING ; REAL-STATE BLOCKS LOSING A MARK: BEFORE %d, AFTER %d.**' % (
        out['before']['cases'] - len(out['before']['failing']), out['before']['cases'],
        out['after']['cases'] - len(out['after']['failing']), out['after']['cases'],
        sum(1 for x in real if x[1]), sum(1 for x in real if x[2]))
    L += ['', summary]
    L += ['', '### THE TWO RUNS, WHOLE:', '=== before'] + out['before']['output'].rstrip(NL).split(NL) + ['=== after'] + out['after']['output'].rstrip(NL).split(NL)
    put_txt('b658_msplit.txt', L)
    put_json('b658_msplit.json', dict(at=utc(), pre=pre, before_pattern=pat_old, after_pattern=NEW._MSPLIT.pattern, real=real,
                                      **{k: {kk: vv for kk, vv in v.items() if kk != 'output'} for k, v in out.items()}))
    print(summary)


# ================================================================================ THE LATE ROUTES (b657's, carried; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


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
    """data/b658_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
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
    head = ['### b658 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b658_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b658_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


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
    L = ['b658 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
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
    put_txt('b658_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b658_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE RUNNER, READ BY ITS RUN ID (b654's, carried)
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
PRINT_RE = re.compile(r"^'(.+?)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", re.M)
ERR_RE = re.compile(r'^(?:error: )?(\S+\.lean):(\d+):(\d+): error: (.*)$', re.M)
CFG_FILE = 'SIDEExplicitFormula/Schema/RateIndexCfg.lean'


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def _prints(text):
    got = {}
    for m in PRINT_RE.finditer(text):
        got[m.group(1)] = sorted(x.strip() for x in (m.group(2) or '').split(',') if x.strip())
    return got


def gate_of(axioms_text, terminals):
    """per named terminal its print: DERIVES where every axiom is one of the standard three and no sorryAx; UNREAD where no print line names it."""
    got = _prints(axioms_text)
    out = []
    for t in terminals:
        ax = got.get(t)
        if ax is None:
            out.append((t, 'UNREAD', None))
        elif 'sorryAx' in ax or not set(ax) <= STD3:
            out.append((t, 'NOT AT THE STANDARD THREE', ax))
        else:
            out.append((t, 'DERIVES', ax))
    return out


def runner(*a):
    """the one run read by its id -- its conclusion; the artifact listed by the API, downloaded as its zip by its id into memory, its sha256
    computed and compared with the platform's digest before any reading; the build exit, the build log's error lines by file and line, the
    memory log's low and any STOP line, and the axioms output read per name of the branch's print_targets.txt as the gate reading; ζ's two
    prints against b654's banked run. Banked as data/b658_runner_SIDE-explicit-formula.txt and a row of data/b658_runner_rows.json."""
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
    wf = _show(K.EF, R['ref'], '.github/workflows/build-module.yml') or ''
    pt = _show(K.EF, R['ref'], 'print_targets.txt') or ''
    terminals = [l.strip() for l in pt.split(NL) if l.strip()]
    row = dict(kernel=kern, branch=R['branch'], ref=R['ref'], target=R['target'], run_id=R['run_id'], conclusion=run.get('conclusion'),
               artifact_sha256=None, mem_low=None, stopped=False, gate=None, merged=None, tag=None)
    L = ['b658 -- COMPONENT 3, (R268)(4): THE HOSTED RUNNER FOR %s, READ BY ITS RUN ID (%s)' % (kern, utc()), '',
         '### the workflow file at the branch (%s, .github/workflows/build-module.yml, the dispatch at the branch on the author`s word), read back whole:' % R['ref'][:8]] + \
        ['    ' + l for l in wf.rstrip(NL).split(NL)] + ['', '### print_targets.txt at the branch (%d names):' % len(terminals)] + ['    ' + t for t in terminals] + ['',
         '### the dispatch, the one dispatch of this branch: ref %s ; target %s' % (R['ref'], R['target']),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             R['run_id'], run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt'))]
    texts = {}
    if art:
        rc2 = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rc2.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        row['artifact_sha256'] = sha
        L.append('### the artifact: id %s ; name %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if digest and digest == sha else ('### DIFFER' if digest else 'no digest to compare')))
        if digest and digest != sha:
            row['artifact_sha256'] = None
        else:
            with zipfile.ZipFile(io.BytesIO(rc2.stdout)) as z:
                for n in z.namelist():
                    texts[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = texts.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    row['mem_low'] = int(low[-1]) if low else None
    stops = [l for l in mem.split(NL) if l.startswith('STOP ')]
    row['stopped'] = bool(stops)
    bexit = texts.get('build_exit.txt', '').strip()
    blog = texts.get('build.log', '')
    errs = [(m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)) for m in ERR_RE.finditer(blog)]
    G = gate_of(texts.get('axioms.txt', ''), terminals)
    ok = (run.get('conclusion') == 'success' and row['artifact_sha256'] and bexit == '0' and not errs and not stops
          and row['mem_low'] is not None and row['mem_low'] >= 2560 and G and all(v == 'DERIVES' for _t, v, _x in G))
    row['gate'] = 'DERIVES' if ok else ('STOPPED BENEATH THE HOLD' if stops else 'NOT DERIVES')
    row['errors'] = [list(e) for e in errs]
    b654 = _prints(rdn('b654_runner_SIDE-explicit-formula.txt').replace(NL + '    ', NL))
    now = _prints(texts.get('axioms.txt', ''))
    zeta = [(t, b654.get(t), now.get(t)) for t in K.ZETA_TERMINALS]
    row['zeta_unchanged'] = all(x is not None and x == y for _t, x, y in zeta)
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(texts.get('ref.txt', '### UNREAD').split()),
          '### the memory log: samples %d ; LOW %s MB ; the hold 2560 ; STOP lines %s' % (
              len([l for l in mem.split(NL) if 'avail_mb=' in l]), row['mem_low'], stops or 'NONE'),
          '### the build: exit %s ; error lines in its log %d' % (bexit or '### UNREAD', len(errs))]
    L += ['    %s:%d:%d: %s' % e for e in errs[:40]]
    L += ['### the build log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-8:]] + ['',
          '### the print file the run assembled (out/Axioms.lean):'] + ['    ' + l for l in texts.get('Axioms.lean', '### UNREAD').rstrip(NL).split(NL)] + [
          '### names refused by the print step: %s' % (texts.get('axioms_refused.txt', '').strip() or 'NONE'), '',
          '### the axioms output, whole:'] + ['    ' + l for l in texts.get('axioms.txt', '### UNREAD').rstrip(NL).split(NL)] + ['',
          '### ζ`S TWO PRINTS against b654`s run 38259645524 (relay data/b654_runner_SIDE-explicit-formula.txt): ' + ' ; '.join(
              '%s %s' % (t.split('.')[-1], 'UNCHANGED' if x is not None and x == y else 'b654 %s, now %s' % (x, y)) for t, x, y in zeta), '',
          '### THE GATE READING, per name of print_targets.txt (%d), from the artifact`s axioms output:' % len(G)]
    L += ['  %-62s %-26s %s' % (t, v, x) for t, v, x in G]
    L += ['', '### ### **RUN %s ; CONCLUSION %s ; ARTIFACT SHA256 %s ; MEMORY LOW %s MB (HOLD 2560) ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS %d, '
              'DERIVES %d ; ζ`S PRINTS %s ; GATE %s.**' % (R['run_id'], run.get('conclusion'), (row['artifact_sha256'] or '### NONE')[:16], row['mem_low'],
                                                       bexit or '### UNREAD', len(errs), len(G), sum(1 for _t, v, _x in G if v == 'DERIVES'),
                                                       'UNCHANGED' if row['zeta_unchanged'] else 'CHANGED OR UNREAD', row['gate'])]
    put_txt('b658_runner_%s.txt' % kern, L)
    j = jl('b658_runner_rows.json') or {'rows': []}
    j['rows'] = [r for r in j.get('rows', []) if r['kernel'] != kern] + [row]
    put_json('b658_runner_rows.json', j)
    print(NL.join(L[-(len(G) + 3):]))
    for e in errs[:12]:
        print('  ERROR %s:%d:%d: %s' % e)


def runner_merged(*a):
    """`runner_merged <merge sha> <tag>`: the row's merge and tag, after main and the tag are read back at the remote."""
    sha, tag = a[:2]
    j = jl('b658_runner_rows.json')
    for r in j['rows']:
        if r['kernel'] == K.KERNEL:
            r['merged'], r['tag'] = sha, tag
    put_json('b658_runner_rows.json', j)
    print('  %s merged %s tag %s' % (K.KERNEL, sha, tag))


DECL_RE = re.compile(r'^(?:noncomputable |protected |private )*(theorem|lemma|def|abbrev|instance|structure|example)\s+(\S+)', re.M)


def landing(*a):
    """(R268)(4): the landing point, banked as data/b658_e1cfg.txt -- DERIVES at the standard three on the runner with the ζ instance closing by
    rfl (or by one application, the fallback named by the author, and which of the two closed), or the statement compiled with the proof open,
    the obstruction by file and line from the build log; the statements on the branch read back beside the bank`s draft."""
    R = K.RUNNER[K.KERNEL]
    rows = [r for r in (jl('b658_runner_rows.json').get('rows') or []) if r['kernel'] == K.KERNEL]
    row = rows[0] if rows else {}
    read_runner_row(row)
    src = _show(K.EF, R['ref'], CFG_FILE) or ''
    draft = rdn('b658_e1cfg_statement.txt')
    gates = _prints(rdn('b658_runner_SIDE-explicit-formula.txt').replace(NL + '    ', NL))
    names = [l.strip() for l in (_show(K.EF, R['ref'], 'print_targets.txt') or '').split(NL) if l.strip()]
    new = [t for t in names if t.startswith('SIDEExplicitFormula.Schema.')]
    g = [(t, gates.get(t)) for t in new]
    derives = bool(g) and all(v is not None and set(v) <= STD3 for _t, v in g)
    errs = [e for e in row.get('errors') or [] if e[0].endswith(CFG_FILE)]
    decls = [(src[:m.start()].count(NL) + 1, m.group(1), m.group(2)) for m in DECL_RE.finditer(src)]
    stmt_same = []
    for name in ('rest_norm_le_rate_cfg', 'zeroSide_neg_at_rate_cfg', 'rest_norm_le_rate_cfg_zeta', 'zeroSide_neg_at_rate_cfg_zeta'):
        i = src.find('theorem %s ' % name)
        if i < 0:
            i = src.find('theorem %s' % name + NL)
        j_ = src.find(':= by', i) if i >= 0 else -1
        j2 = src.find(':= rfl', i) if i >= 0 else -1
        end = min(x for x in (j_, j2) if x >= 0) if i >= 0 and (j_ >= 0 or j2 >= 0) else -1
        k_ = draft.find('theorem %s' % name)
        dl = draft[k_:].split(NL + NL)[0] if k_ >= 0 else ''
        dl = dl.split(':= rfl')[0]
        stmt_same.append((name, i >= 0 and end > i and ' '.join(src[i:end].split()) == ' '.join(dl.split())))
    zeta_form = 'rfl' if re.search(r'zeroSide_neg_at_rate_cfg_zeta :\s*\n?\s*@zeroSide_neg_at_rate_cfg zetaWeilConfig = @B321\.zeroSide_neg_at_rate := rfl', src) \
        else 'one application'
    land_ = 'DERIVES' if derives and row.get('gate') == 'DERIVES' and not errs and row.get('zeta_unchanged') else 'OPEN'
    L = ['b658 -- COMPONENT 3, (R268)(4): E1 OVER A CONFIGURATION -- THE LANDING POINT (%s)' % utc(), '',
         '### the branch %s at %s (SIDE-explicit-formula), the file %s; its declarations (line, kind, name):' % (R['branch'], R['ref'][:8], CFG_FILE)]
    L += ['  :%d %s %s' % d for d in decls]
    L += ['### each statement on the branch against the bank`s draft (relay data/b658_e1cfg_statement.txt section 4), whitespace aside: %s' % stmt_same,
          '### sorry in the file: %d' % len(re.findall(r'\bsorry\b', src)),
          '### the ζ instance written as: %s (the author`s word: rfl tried first, the one application the fallback)' % zeta_form,
          '### the runner: run %s ; conclusion %s ; artifact sha256 %s ; memory low %s MB ; ζ`s prints %s ; gate %s (relay data/b658_runner_SIDE-explicit-formula.txt)' % (
              row.get('run_id'), row.get('conclusion'), (row.get('artifact_sha256') or '### NONE')[:16], row.get('mem_low'),
              'unchanged' if row.get('zeta_unchanged') else 'CHANGED OR UNREAD', row.get('gate')),
          '### the gate reading per new terminal:'] + ['  %-62s %s' % (t, v if v is not None else '### UNREAD') for t, v in g]
    if land_ == 'OPEN':
        L += ['### THE OBSTRUCTION, by file and line (the build log`s error lines in %s, %d):' % (CFG_FILE, len(errs))]
        L += ['  %s:%d:%d: %s' % tuple(e) for e in errs[:30]] or ['  ### NONE IN THE FILE: the run did not reach it']
    L += ['', '### ### **E1-CFG LANDS %s%s.**' % (land_, (' AT THE STANDARD THREE ON THE RUNNER, THE ζ INSTANCE BY %s' % zeta_form.upper())
                                                    if land_ == 'DERIVES' else ': THE BRANCH UNMERGED AT %s, THE OBSTRUCTION ABOVE' % R['ref'][:8])]
    put_txt('b658_e1cfg.txt', L)
    put_json('b658_e1cfg.json', dict(at=utc(), landing=land_, zeta_form=zeta_form, gates=dict(g), errors=errs, decls=decls,
                                     statements_as_drafted=dict(stmt_same), tip=R['ref']))
    print(NL.join(L[-14:]))


# ================================================================================ COMPONENT 5: THE FACE`S BANKS, THE ROOT, THE SCORES, THE RECORD
import collections   # noqa: E402


def kernels(*a):
    import b641_record as R41
    put_json('b658_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


def _defect_short():
    return [re.match(r'^\(([a-z])\) ([^.]*)\.', l.strip()).group(0)[:-1] for l in rdn('b658_defects.txt').split(NL)
            if re.match(r'^    \([a-z]\) [^.]*\.', l)]


def defects(*a):
    t = rdn('b658_defects.txt')
    ds = [l.strip() for l in t.split(NL) if re.match(r'^    \([a-z]\) ', l)]
    put_json('b658_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b658_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b658_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b658_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b658_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b658'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b658_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    with tempfile.TemporaryDirectory(prefix='b658_ra_') as tmp:
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
    L = ['b658 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b658_root_arm.txt', L)
    put_json('b658_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b658 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b658_table_final.txt', L)
    put_json('b658_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b657_closing_push_out.txt')
N5_RELAY_TOOLS = ('b647_record.py', 'test_msplit_b658.py')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
N5_EF = ['.github/workflows/build-module.yml', 'SIDEExplicitFormula/Schema/RateIndexCfg.lean', 'print_targets.txt']
FACE = os.path.join(D, 'b658_registration_2026-10-12.txt')


def TRAIL_HEAD():
    return ('### b658 — lane two, act eighty-five, the research act under (R268): b657 at its weight; the splitter repaired; E1 over a '
            'configuration stated in a bank, built on the runner and merged, ζ the instance by rfl')


def _ct(repo, *a):
    s = g(repo, 'log', '-1', '--format=%ct', *a).strip()
    return int(s) if s.isdigit() else None


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime((s or '')[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


def trace_check():
    """every hypothesis row of the statement bank read through read_trace_row, and each cited line of RateIndex.lean at v0.27 read for its
    binder; returns (rows, [(id, lines missing the binder)])."""
    src = (_show(K.EF, K.EF_TAG, 'SIDEExplicitFormula/RateIndex.lean') or '').split(NL)
    tok = {'H1': 'H', 'H2': 'Q', 'H3': 'B', 'H4': 'D', 'H5': 'hQtie', 'H6': 'hQb', 'H7': 'θ', 'H8': 'hθ', 'H9': 'hA', 'H10': 'j', 'H11': 'hrate'}
    rows, bad = [], []
    for l in rdn('b658_e1cfg_statement.txt').split(NL):
        if not l.startswith('  H'):
            continue
        i, b, ls, _h = read_trace_row(l)
        rows.append(i)
        t = tok.get(i)
        miss = [n for n in ls if not t or n > len(src) or not re.search(r'(?<![\w.])' + re.escape(t) + r'(?![\w₀])', src[n - 1])]
        if miss or not ls:
            bad.append((i, miss))
    return rows, bad


def _first_lean_ct():
    """the first commit on the branch that writes a .lean file: the first Lean byte of the act."""
    for l in g(K.EF, 'log', '--reverse', '--format=%H %ct', K.EF_MAIN + '..' + K.RUNNER[K.KERNEL]['ref']).split(NL):
        if l.strip():
            h, ct = l.split()
            if any(f.endswith('.lean') for f in g(K.EF, 'show', '--name-only', '--pretty=format:', h).split(NL)):
                return int(ct)
    return None


def _n2():
    rows, bad = trace_check()
    aj = jl('b658_author_answers.json').get('calls') or []
    last_ans = max((_iso(c.get('result_ts')) or 0) for c in aj) if aj else None
    fl = _first_lean_ct()
    ok = len(rows) == 11 and not bad and last_ans and fl and last_ans < fl and len(aj) == 1
    return ('HELD' if ok else 'REFUTED'), (
        'hypothesis rows of the statement bank %d, each read through its reader and each cited line of RateIndex.lean at %s carrying its binder: '
        '%s; the one prompt answered at %s, the first Lean byte (the branch`s first .lean commit) at %s -- the answer first %s' % (
            len(rows), K.EF_TAG, 'ALL' if not bad else 'NOT %s' % bad, time.strftime('%H:%M:%SZ', time.gmtime(last_ans)) if last_ans else '?',
            time.strftime('%H:%M:%SZ', time.gmtime(fl)) if fl else '?', bool(last_ans and fl and last_ans < fl)))


def _n3():
    lj = jl('b658_e1cfg.json')
    rr = dict((r['kernel'], r) for r in jl('b658_runner_rows.json').get('rows') or []).get(K.KERNEL) or {}
    ri_same = _show(K.EF, 'main', 'SIDEExplicitFormula/RateIndex.lean') == _show(K.EF, K.EF_TAG, 'SIDEExplicitFormula/RateIndex.lean')
    cfg_main = _show(K.EF, 'main', CFG_FILE) or ''
    sorry_main = len(re.findall(r'\bsorry\b', cfg_main))
    ok = (lj.get('landing') == 'DERIVES' and lj.get('zeta_form') in ('rfl', 'one application') and rr.get('zeta_unchanged')
          and ri_same and cfg_main and sorry_main == 0 and rr.get('merged') and all((lj.get('statements_as_drafted') or {}).values()))
    return ('HELD' if ok else 'REFUTED'), (
        'the landing point banked: %s, the ζ instance by %s, the statements as drafted %s; zeroSide_neg_at_rate`s print against b654`s run %s, '
        'RateIndex.lean at main equal to %s`s %s; sorry in the configuration file at main %d; merged %s tag %s' % (
            lj.get('landing'), lj.get('zeta_form'), lj.get('statements_as_drafted'), 'UNCHANGED' if rr.get('zeta_unchanged') else '### CHANGED OR UNREAD',
            K.EF_TAG, ri_same, sorry_main, rr.get('merged'), rr.get('tag')))


def _n4():
    mj = jl('b658_msplit.json')
    b, a_ = mj.get('before') or {}, mj.get('after') or {}
    ok = a_.get('cases') == 7 and a_.get('failing') == [] and a_.get('rc') == 0 and b.get('rc') == 1 and b.get('failing') \
        and sum(1 for x in mj.get('real') or [] if x[1]) > 0 and not any(x[2] for x in mj.get('real') or [])
    return ('HELD' if ok else 'REFUTED'), (
        'the planted test after the repair %s of %s passing (exit %s); on its positive control, the splitter before the repair at relay %s: '
        'failing %s (exit %s); at SIDE-lv-conservation b4c55b9 blocks losing a mark before %d, after %d (relay data/b658_msplit.txt)' % (
            (a_.get('cases') or 0) - len(a_.get('failing') or []), a_.get('cases'), a_.get('rc'), mj.get('pre'), b.get('failing'), b.get('rc'),
            sum(1 for x in mj.get('real') or [] if x[1]), sum(1 for x in mj.get('real') or [] if x[2])))


def _n5():
    face = jl('b658_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b658_|audit_b658_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA)
                                                or (x.startswith('tools/') and x[6:] in N5_RELAY_TOOLS))]
    km = [l for l in g(K.EF, 'log', '--first-parent', '--format=%h %p', K.EF_MAIN + '..main').split(NL) if l.strip()]
    rr = dict((r['kernel'], r) for r in jl('b658_runner_rows.json').get('rows') or []).get(K.KERNEL) or {}
    km_ok = len(km) == 1 and len(km[0].split()) == 3 and km[0].split()[0] == rr.get('merged')
    ef_files = sorted(x for x in g(K.EF, 'diff', '--name-only', K.EF_MAIN, 'main').split(NL) if x.strip())
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b658_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ok = others_ok and not pp_beyond and not kinds_beyond and not differ and km_ok and not new_arms and ef_files == sorted(N5_EF)
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); SIDE-explicit-formula`s main written by the one merge under '
            'Component 4 alone (first-parent commits since %s: %s ; %s), its files against %s: %s; every kernel as the face read it %s; standing '
            'arms added: %s (the act`s arms over its own banks %d); sealed tools not agreeing %s; PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; '
            'relay files of a kind beyond the banks, the tools, the splitter and its test and the root list: %s; no identifier of the author in any '
            'outbound request (git pushes, remote reads, the runner`s dispatch with a ref and a target, the artifact`s download)' % (
                K.DRAFT, K.EF_MAIN, [l.split()[0] for l in km], 'AS RULED' if km_ok else '### OTHERWISE', K.EF_MAIN, ef_files, others_ok,
                new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE'))


def scores(*a):
    TF, RA = jl('b658_table_final.json'), jl('b658_root_arm.json')
    _r, _n, sh = seal_hashes()
    cm = jl('b658_commands.json')
    S = {
        'N1': (('HELD' if cm and not cm.get('local_lean') else 'REFUTED'),
               'commands of this act that run lean or lake on this host: %s (relay data/b658_commands.txt); the build on the hosted runner alone' % (
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
    put_json('b658_scores.json', dict((k2, list(v)) for k2, v in S.items()))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))


NEXT_LINE = ('b659, per `(R268)`(6), the re-cut act on the next kernel by descending OVERREACHES count under `(R265)`’s form; b660 the reading act')


def _title():
    lj = jl('b658_e1cfg.json')
    land_ = lj.get('landing') or 'its landing point'
    return '## E1 over a configuration: %s on the runner, ζ the instance by %s; the splitter repaired' % (
        land_, lj.get('zeta_form') or 'rfl')


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'


def _finding_text():
    S, rl, J, lj = jl('b658_scores.json'), jl('b658_record_lines.json'), jl('b658_act_root.json'), jl('b658_e1cfg.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b658_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    rr = dict((r['kernel'], r) for r in jl('b658_runner_rows.json').get('rows') or []).get(K.KERNEL) or {}
    mj = jl('b658_msplit.json')
    e = ['', _title(), '',
         '*Filed at b658 on the author’s ruling `(R268)`, the author’s three answers and the one prompt (%d). Banks: relay '
         '`data/b658_e1cfg_statement.txt`, `data/b658_e1cfg.txt`, `data/b658_runner_SIDE-explicit-formula.txt`, `data/b658_msplit.txt`, '
         '`data/b658_act_root.txt`.*' % n_ans, '',
         '**The statement** (`(R268)`(3)): E1’s two statements carried from `zetaZeroConfig` to any `WeilConfig`, reading its points and '
         'multiplicities alone -- the setup `PWSetup C.toZeroConfig g0 L M`, the local count as the hypothesis `hA` with its constant `A₀` '
         '(the kernel holding ζ’s existentially), the same `hrate` over `sT_cfg`, the conclusion over `zeroSide_cfg C`; every hypothesis '
         'traced in the bank to the RateIndex.lean lines that consumed it, before any Lean. No excluded-zero hypothesis: the rate proof takes '
         'none, and `hrate` forces the tie set non-empty (the clause struck as the navigator’s). N2 %s.' % _sv(S, 'N2'), '',
         '**The attempt** (`(R268)`(4)): `rest_norm_le_rate_cfg`, `zeroSide_neg_at_rate_cfg` and `dominant_summable_hcount` in a new file, '
         'SIDEExplicitFormula/Schema/RateIndexCfg.lean, the ζ proof carried with Converse.lean’s twins; the ζ instances '
         '`@zeroSide_neg_at_rate_cfg zetaWeilConfig = @B321.zeroSide_neg_at_rate` and the rest’s likewise, by %s; RateIndex.lean unedited. '
         'One dispatch at the branch, run %s, the artifact’s sha256 agreeing with the platform’s digest, memory low %s MB; the eight names of '
         'print_targets.txt at the standard three, ζ’s two prints unchanged from b654’s run; merged alone, SIDE-explicit-formula %s tagged %s. '
         'N3 %s.' % (lj.get('zeta_form'), rr.get('run_id'), rr.get('mem_low'), rr.get('merged'), rr.get('tag'), _sv(S, 'N3')), '',
         '**The runner’s print list** (the author’s word, standing under `(R263)`(4)): the print step reads its names from print_targets.txt '
         'at the kernel’s root; the branch carried the edit and the file, the dispatch was at the branch, and the merge carried both to main.', '',
         '**The splitter** (`(R268)`(2)): b647’s sentence split now keeps a closing quote, asterisk or bracket after a period with its sentence, '
         'the split points unchanged; its planted test %s of 7 after the repair and %s of 7 before it; the two unbalanced emphases in '
         'ZeroActingPartial.lean listed for SIDE-lv-conservation’s cell refresh (OPEN_TRAILS :%s). N4 %s.' % (
             7 - len((mj.get('after') or {}).get('failing') or []), 7 - len((mj.get('before') or {}).get('failing') or []), ls[1].get('line'),
             _sv(S, 'N4')), '',
         '**The record lines** (`(R268)`(1)): b657 at its weight (FINDINGS :%s).' % ls[0].get('line'), '',
         '**The root.** b658 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this statement re-reads b654’s rate (relay `data/b654_e1.txt`) and b656’s binding '
         '(relay `data/b656_e1_binding.txt`, O-1 to O-3), and answers O-2 -- E1 now has a compiled form over a general configuration; it is '
         're-read by the map of `(R266)`(4), which returns as a research act bound to this theorem. It strengthens the programme’s offering of '
         'statements a reader can check: the rate is a theorem about any configuration with a local count, ζ’s is its instance by definition, '
         'and the build runs on a machine the reader can name by run id.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; the configuration theorem is an implication from its hypotheses, '
         'and a gate reading compares a print with the standard three and confers nothing beyond it.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the statement over `WeilConfig` reading `C.toZeroConfig` alone, the summability from the hypothesis `hA`, not the '
              'structure`s count field; (2) the ζ instance as an rfl equation between the configuration theorem at `zetaWeilConfig` and the ζ '
              'theorem; (3) the gate reading the eight names of print_targets.txt, ζ’s two prints compared with b654’s run; (4) the splitter’s '
              'look-behind taking up to four closing marks, the split points the old ones')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b658_scores.json', 'b658_findings.json', 'b658_record_lines.json', 'b658_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b658_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R268) ratified.** (1) b657 at its weight. (2) The splitter repaired, the two emphases listed for the cell refresh. (3) E1 over a '
             'configuration stated in a bank, every hypothesis traced; the excluded-zero clause struck as the navigator’s on the author’s word. '
             '(4) The attempt on the runner, the print list from print_targets.txt on the author’s word, standing under `(R263)`(4). (5) The '
             'draft held at v5. (6) The act after: b659.', '',
             '**Entered:** FINDINGS.md:%s (b657’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the two emphases); this record.' % (
                 ls[0].get('line'), fj.get('entry_line'), ls[1].get('line')), '',
             '**Act root:** b658 `%s` (previous `%s`, b657’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b658_author_answers.txt, with the author’s words), the statement alone, before any Lean; '
             'none after the root.' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**The runner’s print list, standing:** every kernel’s runner takes its print list from print_targets.txt at its next use; '
             'SIDE-explicit-formula’s from b658.', '',
             '**Defects** (relay data/b658_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b658_scores.json')
    L = ['=' * 104, 'b658 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b658_defects.txt').rstrip(NL).split(NL)
    put_txt('b658_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b658_scores.json', 'b658_findings.json', 'b658_trail.json', 'b658_record_lines.json', 'b658_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    L = ['b658 -- THE COMPONENTS, BANKED UNDER (R268).', '',
         '### COMPONENT 0 : step zero (data/b658_ferry.txt, data/b658_stepzero.txt, data/b658_tests_stepzero.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b657`s weight FINDINGS :%s ; the two emphases OPEN_TRAILS :%s ; the splitter repaired (data/b658_msplit.txt) ; N4 %s' % (
             ls[0].get('line'), ls[1].get('line'), S['N4'][0]),
         '### COMPONENT 2 : the statement (data/b658_e1cfg_statement.txt), the one prompt (data/b658_author_answers.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the attempt on the runner (data/b658_runner_SIDE-explicit-formula.txt), the landing point (data/b658_e1cfg.txt) ; N3 %s' % S['N3'][0],
         '### COMPONENT 4 : the merge, SIDE-explicit-formula %s tag %s (data/b658_ef_merge_push_out.txt)' % (
             (dict((r['kernel'], r) for r in jl('b658_runner_rows.json').get('rows') or []).get(K.KERNEL) or {}).get('merged'), K.NEXT_TAG),
         '### COMPONENT 5 : the dry-run step (data/b658_reg_gate.txt), the seal (data/b658_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % ((J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'),
                                                                                        S['N1'][0], S['N5'][0])]
    put_txt('b658_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b658_findings.json', dict(title=t))
    j = jl('b658_findings.json')
    j['entry_line'] = ln
    put_json('b658_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b658_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written (B658_STANDIN) -- converted by conv and run through the screens their landing runs, the needles the face
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


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in globals() or not callable(globals()[sys.argv[1]]):
        print('usage: b658_record.py <route> [args]')
        sys.exit(2)
    globals()[sys.argv[1]](*sys.argv[2:])
