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
    import shutil
    import tempfile
    pre = a[0] if a else 'HEAD~1'
    import b647_record as NEW
    d = tempfile.mkdtemp(prefix='b658_ms_')
    old_path = os.path.join(d, 'b647_record.py')
    open(old_path, 'wb').write(subprocess.run(['git', '-C', ROOT, 'show', '%s:tools/b647_record.py' % pre], capture_output=True).stdout)
    out = {}
    for name, path in (('before', old_path), ('after', os.path.join(T, 'b647_record.py'))):
        r = subprocess.run([sys.executable, os.path.join(T, 'test_msplit_b658.py'), path], capture_output=True, text=True, encoding='utf-8',
                           errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'), cwd=ROOT)
        cases = [l for l in (r.stdout or '').split(NL) if re.match(r'^  \(\d+\) ', l)]
        fails = [re.match(r'^  (\(\d+\))', c).group(1) for c in cases if not c.rstrip().endswith('PASS')]
        out[name] = dict(rc=r.returncode, cases=len(cases), failing=fails, last=(r.stdout or '').strip().split(NL)[-1], output=r.stdout)
    shutil.rmtree(d)
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


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in globals() or not callable(globals()[sys.argv[1]]):
        print('usage: b658_record.py <route> [args]')
        sys.exit(2)
    globals()[sys.argv[1]](*sys.argv[2:])
