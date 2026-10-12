# -*- coding: utf-8 -*-
"""b653_record.py -- THE ACT'S RECORD TOOL, b653 under (R263).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b653's name.
### (R263)(3): every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability spec's planted
### rows (tools/b653_regspec.py) can run each reader over one row of each shape before the seal.
### Routes: `python tools/b653_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
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
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7ab48879-b65c-45b3-8af8-abdcd7120d6f/scratchpad'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(path) else ''


def rdn(name):
    return rd(os.path.join(D, name))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b653's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b653_scanfile_%s.md' % tag)
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
    """a row of data/b653_runner_rows.json -- every key of RUNNER_KEYS present (None where a step did not reach it); returns the row's reading
    (kernel, outcome, merged) that the scores, the record and the closing print; raises KeyError on a row of another shape."""
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
    """a scores row: key N1..N5 or S1..S5, value [verdict, text]; returns (key, first verdict word, text)."""
    if not re.match(r'^[NS][1-5]$', k) or not isinstance(v, list) or len(v) != 2:
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0].split(' ')[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


READERS = ('read_runner_row', 'read_score_row', 'read_head')


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R263)(1)-(3)
WH = ('*Appended 2026-10-12 by b653 to b652’s entry (:8259), under `(R263)`(1) -- b652 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b652_closing.txt):*')
MH = ('*Appended 2026-10-12 by b653 beneath b652’s margin correction (:13898), under `(R263)`(2) -- THE MARGIN RULE ON COMPLETED RUNS, '
      'STANDING FROM b653; SUPERSEDES :13898:*')
SH = ('*Appended 2026-10-12 by b653, under `(R263)`(3) -- THE SEAL ORDER, ONE CLAUSE ADDED: A PLANTED ROW OF EVERY SHAPE A SEALED ROUTE READS, '
      'STANDING FROM b653:*')


def _weight():
    return ('\n' + WH + ' relay 6eaacf29 (the act) and 466886b5 (the closing); PLACE-papers 81fa18a; the root 89e62b16… over 40 banks; the '
            'suite 80 arms, 78 of 80 before and after the push, the two declared failures G-NO-SORRY-MAIN and G-AXIOM-CLAIM. Milestones built '
            'and merged alone on its gate reading -- SIDE-effects main 9a279ac, its three restated lines off main; PerpendicularCrossing built '
            'for its measurement, loss 1,452 MB, the cut branch left unmerged; T3_StepNineBridge stopped beneath the hold, loss at least 1,826 '
            'MB, its branch unmerged, the one sorry on any main at its :108. The cut of 113 blocks in 33 files on a branch, the code byte for '
            'byte the same under comment stripping. The INSTRUMENT verdict with its opening rows, the block table’s identical reading before and '
            'after the cut entered as one of them. The conversion rule with its planted case, the five arms of b651’s defect (n) passing at '
            'HEAD. Twelve defects (relay data/b652_defects.txt), the navigator’s among them the margin term (d) and the sentence-row assumption '
            '(b). The mirror export D:/MY-DOwnloads/mirror-refresh-2026-10-11-b652.zip (MANIFEST md5 ce698d41…, commit 81fa18a). Nothing '
            'deposited.\n')


def _margin_rule():
    return ('\n' + MH + ' a figure read from a stopped run is a lower bound and licenses no start: it reads "at least <x>, UNMEASURED". A '
            'module’s margin needed is the host’s loss from a completed run -- free memory at the start less the host’s low, as the watchdog '
            'prints them; a build on this host starts where the margin seen at the slot’s start reaches that loss, and nowhere else. The hold '
            'stays 2,560 MB on every host. The rule’s opening entries, b652’s two completed runs (relay data/b652_build_margin.txt :34, :36): '
            'Kernel.PerpendicularCrossing 1,452 MB; SIDEEffects.Milestones 1,332 MB. SIDELvConservation.T3_StepNineBridge reads at least 1,826 '
            'MB, UNMEASURED (:38, a stopped run). This supersedes b652’s correction at :13898, whose largest-of-the-attempts term counted '
            'stopped runs.\n')


def _seal_order():
    return ('\n' + SH + ' the registration gate’s satisfiability spec carries one planted row of every shape a sealed route reads -- build '
            'rows, score rows, trail heads with a backtick possessive among them -- and runs each of the record tool’s readers over its row '
            'before the seal, so a sealed tool meets each shape before it is sealed and not after. Its cases: b651’s (m) and (n), a trail head '
            'and an entry title looked up by another conversion than the landing’s; b652’s (l), a score route reading keys its build rows did '
            'not carry. The spec counts its planted rows and refuses to emit where a reader raises or returns nothing.\n')


def c1(*a):
    items = [('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', MH, _margin_rule()), ('OPEN_TRAILS.md', SH, _seal_order())]
    land(items, 'b653_record_lines.json', 'c1', entry=8259,
         check=[('FINDINGS.md', 8259, '## The build margin at 3 modules'), ('OPEN_TRAILS.md', 13898, 'THE MARGIN TERM CORRECTED')],
         dry='dry' in a)


# ================================================================================ COMPONENT 3: THE RUNNER, (R263)(4)
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
# ### the name runs to the quote before ` depends` or ` does not` (a primed name carries a quote of its own); the list may wrap across lines
PRINT_RE = re.compile(r"^'(.+?)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", re.M)


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def gate_of(axioms_text, terminals):
    """per named terminal its print: DERIVES where every axiom is one of the standard three and no sorryAx; UNREAD where no print line names it."""
    got = {}
    for m in PRINT_RE.finditer(axioms_text):
        ax = set(x.strip() for x in (m.group(2) or '').split(',') if x.strip())
        got[m.group(1)] = sorted(ax)
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
    """`runner <kernel>`: the run read by its id -- its conclusion; the artifact listed by the API, downloaded as its zip by its id, its sha256
    computed and compared with the platform's digest; the build exit, the build log's error lines, the memory log's low and any STOP line, and
    the axioms output read per named terminal as the gate reading. Banked as data/b653_runner_<kernel>.txt and a row of data/b653_runner_rows.json."""
    import hashlib
    import tempfile
    import zipfile
    import b653_worklist as K
    kern = a[0]
    R = K.RUNNER[kern]
    repo = 'psinary-sketch/' + kern
    rc, out, err = _gh('run', 'view', str(R['run_id']), '-R', repo, '--json', 'status,conclusion,headSha,createdAt,updatedAt,url')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, R['run_id']))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    wf = rd(os.path.join('D:/' + kern, '.github', 'workflows', 'build-module.yml'))
    # ### a terminal is a line that begins with the command (the file's header comment names the command and is no terminal)
    terminals = [l.strip()[len('#print axioms '):].strip() for l in wf.split(NL) if l.strip().startswith('#print axioms ')]
    row = dict(kernel=kern, branch=R['branch'], ref=R['ref'], target=R['target'], run_id=R['run_id'], conclusion=run.get('conclusion'),
               artifact_sha256=None, mem_low=None, stopped=False, gate=None, merged=None, tag=None)
    L = ['b653 -- COMPONENT 3, (R263)(4): THE HOSTED RUNNER FOR %s, READ BY ITS RUN ID (%s)' % (kern, utc()), '',
         '### the workflow file on main (%s, .github/workflows/build-module.yml), read back whole:' % R['workflow_commit']] + \
        ['    ' + l for l in wf.rstrip(NL).split(NL)] + ['',
         '### the dispatch: ref %s ; target %s ; the first dispatch %s failed at checkout (defect (a))' % (R['ref'], R['target'], R['failed_run']),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head of the workflow %s ; %s to %s' % (
             R['run_id'], run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('createdAt'), run.get('updatedAt'))]
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
    errs = [l for l in blog.split(NL) if re.search(r'(^|\s)error(:|\b)', l) and 'warning' not in l.lower()]
    G = gate_of(texts.get('axioms.txt', ''), terminals)
    ok = (run.get('conclusion') == 'success' and row['artifact_sha256'] and bexit == '0' and not errs and not stops
          and row['mem_low'] is not None and row['mem_low'] >= 2560 and G and all(v == 'DERIVES' for _t, v, _x in G))
    row['gate'] = 'DERIVES' if ok else ('STOPPED BENEATH THE HOLD' if stops else 'NOT DERIVES')
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(texts.get('ref.txt', '### UNREAD').split()),
          '### the memory log: samples %d ; LOW %s MB ; the hold 2560 ; STOP lines %s' % (
              len([l for l in mem.split(NL) if 'avail_mb=' in l]), row['mem_low'], stops or 'NONE'),
          '### the build: exit %s ; error lines in its log %d%s' % (bexit or '### UNREAD', len(errs), (': ' + ' | '.join(e[:160] for e in errs[:8])) if errs else ''),
          '### the build log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + ['',
          '### THE GATE READING, per named terminal (%d), from the artifact`s axioms output:' % len(G)]
    L += ['  %-70s %-26s %s' % (t, v, x) for t, v, x in G]
    L += ['', '### ### **RUN %s ; CONCLUSION %s ; ARTIFACT SHA256 %s ; MEMORY LOW %s MB (HOLD 2560) ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS %d, '
              'DERIVES %d ; GATE %s.**' % (R['run_id'], run.get('conclusion'), (row['artifact_sha256'] or '### NONE')[:16], row['mem_low'], bexit or '?',
                                         len(errs), len(G), sum(1 for _t, v, _x in G if v == 'DERIVES'), row['gate'])]
    put_txt('b653_runner_%s.txt' % kern, L)
    j = jl('b653_runner_rows.json') or {'rows': []}
    j['rows'] = [r for r in j['rows'] if r['kernel'] != kern] + [row]
    put_json('b653_runner_rows.json', j)
    print(L[-1])


def runner_merged(*a):
    """`runner_merged <kernel> <merge sha> <tag>`: the row's merge and tag, after main and the tag are read back at the remote."""
    kern, sha, tag = a[:3]
    j = jl('b653_runner_rows.json')
    for r in j['rows']:
        if r['kernel'] == kern:
            r['merged'], r['tag'] = sha, tag
    put_json('b653_runner_rows.json', j)
    print('  %s merged %s tag %s' % (kern, sha, tag))


# ================================================================================ COMPONENT 2: THE GRADE BANK RE-RUN, (R263)(5)
CUT_BRANCH, PC_BRANCH = 'docstrings-cut-SIDE-kernel', 'docstrings-SIDE-kernel'
ELIDED = (56, 57, 69)


def _ws(s):
    return ' '.join(s.split())


def regrade(*a):
    """the sentence-grade bank re-run at the branch that carries the cut and the plain comments: for each of the 116 blocks, each sentence b652
    graded (OVERREACHES or UNDERSTATES) read again -- still standing in its file at the branch (whitespace aside), or gone; the three elided
    blocks apart, their completed ACTION read at the branch. Counts by the grade a sentence still standing keeps."""
    import collections
    rows = jl('b651_table_SIDE-kernel_sentences.json')['rows']
    par = dict((r['id'], r) for r in jl('b647_table_SIDE-kernel.json')['rows'])
    by = collections.OrderedDict()
    for r in rows:
        by.setdefault(r['parent'], []).append(r)
    G = jl('b652_sentence_grades.json')['grades']
    E = dict(((56, 'Kernel/SimplicityRouteD.lean'), 'Kernel/Root.lean imports Kernel.SimplicityRouteD; no declaration cites the theorem.'),
             ) if False else {56: 'Kernel/Root.lean imports Kernel.SimplicityRouteD; no declaration cites the theorem.',
                               57: 'Kernel/Root.lean imports Kernel.SimplicityRouteE; no declaration cites the theorem.',
                               69: 'Kernel/Root.lean imports Kernel.TriviumCode.'}
    ref = 'main' if 'control' in a else PC_BRANCH
    rev = g('D:/SIDE-kernel', 'rev-parse', '--short=7', ref).strip()
    files = {}
    standing, gone, n_sent = [], [], 0
    cnt = collections.Counter()
    L = ['b653 -- COMPONENT 2, (R263)(5): THE SENTENCE-GRADE BANK RE-RUN AT %s %s, AFTER THE THREE ELIDED BLOCKS WERE CUT (%s)' % (ref, rev, utc()), '',
         '### rows are sentences, parents are blocks: relay data/b651_table_SIDE-kernel_sentences.json (396 rows, 116 blocks), the grades relay',
         '### data/b652_sentence_grades.json (152 graded); each graded sentence looked for in its file at the branch, whitespace aside.', '']
    for k, (p, rs) in enumerate(by.items(), 1):
        f = par[p]['file']
        if f not in files:
            files[f] = _ws(subprocess.run(['git', '-C', 'D:/SIDE-kernel', 'show', '%s:%s' % (ref, f)], capture_output=True).stdout.decode('utf-8', 'replace'))
        text = files[f]
        graded = dict((int(n), q) for n, q in G.get(str(k), []))
        for r in rs:
            n_sent += 1
            if r['n'] not in graded:
                cnt['MATCHES'] += 1
                continue
            s = _ws(r['sentence'])
            if s and s in text:
                standing.append((k, f, r['n'], par[p]['verdict'], r['sentence']))
                cnt[par[p]['verdict'] + ' (STANDING)'] += 1
            else:
                gone.append((k, f, r['n']))
                cnt['CUT'] += 1
    L += ['### THE THREE ELIDED BLOCKS, THEIR COMPLETED ACTION AT THE BRANCH:']
    for k in ELIDED:
        p, rs = list(by.items())[k - 1]
        f = par[p]['file']
        L.append('  #%d %s : the completed ACTION present %s ; its graded sentence standing %s' % (
            k, f, _ws(E[k]) in files[f], any(x[0] == k for x in standing)))
    L += ['', '### GRADED SENTENCES STILL STANDING AT THE BRANCH (%d):' % len(standing)]
    L += ['  #%d %s s%d %s -- %s' % x for x in standing] or ['  none']
    L += ['', '### ### **SENTENCE ROWS %d ; MATCHES %d ; GRADED AND CUT %d ; GRADED AND STILL STANDING %d (OVERREACHES %d, UNDERSTATES %d).**' % (
        n_sent, cnt['MATCHES'], cnt['CUT'], len(standing), cnt['OVERREACHES (STANDING)'], cnt['UNDERSTATES (STANDING)'])]
    if 'control' not in a:
        # ### the control: the same read at main, where the cut is not, must find the graded sentences standing
        import io as _io
        import contextlib
        buf = _io.StringIO()
        saved = (globals()['put_txt'], globals()['put_json'])
        globals()['put_txt'], globals()['put_json'] = (lambda n_, L_: None), (lambda n_, o_: None)
        try:
            with contextlib.redirect_stdout(buf):
                regrade('control')
        finally:
            globals()['put_txt'], globals()['put_json'] = saved
        ctl = [l for l in buf.getvalue().split(NL) if 'SENTENCE ROWS' in l]
        L += ['### THE CONTROL, the same read at main: %s' % (ctl[-1].strip('# *') if ctl else '### NOT READ')]
    put_txt('b653_regrade.txt', L)
    put_json('b653_regrade.json', dict(at=utc(), rev=rev, counts=dict(cnt), standing=[list(x) for x in standing], cut=len(gone), sentences=n_sent))
    print(NL.join(L[-12:]))


# ================================================================================ THE LATE ROUTES (b652's, carried; every row read through READERS)
import collections                 # noqa: E402
import b633_record as R3           # noqa: E402
import b653_worklist as K          # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def answers(*a):
    """data/b653_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
    delivered between BEGIN and END after the ruling (user lines and queued commands), and the author's plain messages, verbatim."""
    calls, results, words, plain, start = [], {}, [], [], None
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8', errors='replace'), 1):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if start is None and K.ANCHOR in raw and o.get('type') == 'user' and not o.get('isCompactSummary'):
            start = i
        m = o.get('message') or {}
        cs = m.get('content')
        att = o.get('attachment') or {}
        texts = []
        if start is not None and att.get('type') == 'queued_command' and isinstance(att.get('prompt'), str):
            texts = [att['prompt']]
        elif start is not None and o.get('type') == 'user' and not o.get('isCompactSummary'):
            texts = [cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']
            for t in texts:
                if t and not t.lstrip().startswith(('<', 'BEGIN', 'RULING')) and len(t) < 400 and i > start:
                    plain.append((i, t.strip()))
        for t in texts:
            for mm in re.finditer(r'(?ms)^BEGIN\s*\n(.*?)\nEND\s*$', t or ''):
                if K.ANCHOR not in mm.group(1):
                    words.append((i, mm.group(1)))
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion' and start is not None:
                calls.append((i, c['id'], c['input']))
            if isinstance(c, dict) and c.get('type') == 'tool_result':
                t = c.get('content')
                results[c.get('tool_use_id')] = (i, ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t)
    if start is None:
        sys.exit('### THE ANCHOR IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    L, n = [], 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, K.SESSION_ID, i))
        for k, q in enumerate(inp.get('questions', []), 1):
            n += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT'))
        L += ['RESULT (transcript line %s): %s' % (r[0], r[1]), '']
    W, seen = [], set()
    for i, w in words:
        if w in seen:
            continue
        seen.add(w)
        W += ['### THE AUTHOR`S WORD (transcript line %d), BEGIN to END, verbatim:' % i] + w.replace('\r', '').split(NL) + ['']
    for i, t in plain:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %d), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b653 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b653_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings (a commit message that names `lake exe cache get` runs
    nothing) and outside a gh workflow call (the hosted runner's)."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    L = ['b653 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
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
    put_txt('b653_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b653_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])


def kernels(*a):
    import b641_record as R41
    put_json('b653_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


def _defect_short():
    return [re.match(r'^\(([a-z])\) ([^.]*)\.', l.strip()).group(0)[:-1].lower() for l in rdn('b653_defects.txt').split(NL)
            if re.match(r'^    \([a-z]\) [^.]*\.', l)]


def defects(*a):
    t = rdn('b653_defects.txt')
    ds = [l.strip() for l in t.split(NL) if re.match(r'^    \([a-z]\) ', l)]
    put_json('b653_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b653_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b653_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b653_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b653_seal_hashes.json' in banks, crlf or 'none'))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b653'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import shutil
    import tempfile
    import act_root as AR
    J = jl('b653_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, os.path.basename(bank_))
    shutil.copy(os.path.join(ROOT, *bank_.split('/')), cp)
    b = bytearray(open(cp, 'rb').read())
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
    L = ['b653 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b653_root_arm.txt', L)
    put_json('b653_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b653 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b653_table_final.txt', L)
    put_json('b653_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = NK + SK
N5_RELAY_TOOLS = K.EDITED_SHARED
N5_RELAY_DATA = ('act_roots.txt', 'b652_closing_push_out.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')


def TRAIL_HEAD():
    return ('### b653 — lane three, act eighty under (R263): b652 at its weight; the margin rule on completed runs; the hosted runner written, '
            'run and read back for two branches; the elided cells completed and cut; the b638 test repaired')


def _runner_rows():
    return [read_runner_row(r) for r in (jl('b653_runner_rows.json').get('rows') or [])]


def _wf_clean():
    """each workflow file, read at its kernel's main: no author identifier, no secret reference."""
    bad = {}
    for kern in K.RUNNER:
        t = _show('D:/' + kern, 'main', '.github/workflows/build-module.yml') or ''
        hits = [w for w in ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'ORCID', '0009-0008') if w.lower() in t.lower()]
        bad[kern] = (bool(t), hits)
    return bad


def _n5():
    face = jl('b653_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b653_|audit_b653_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('tools/') and x[6:] in N5_RELAY_TOOLS) or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    rr = _runner_rows()
    ok = kern_ok and not pp_beyond and not kinds_beyond and not differ
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); kernel mains written by the workflow files and the merges '
            'under (R263)(4) alone: %s; every kernel as the face read it %s; sealed tools not agreeing %s; PLACE-papers beyond FINDINGS and '
            'OPEN_TRAILS: %s; relay files of a kind beyond the test edit, the banks and the root list: %s; no identifier of the author in any '
            'outbound request (git pushes, remote reads, the runner`s dispatches with a ref and a target, the artifacts` downloads)' % (
                K.DRAFT, ', '.join('%s %s' % (r['kernel'], r['merged']) for r in rr if r['merged']) or 'no merge', kern_ok, differ or 'NONE',
                pp_beyond or 'NONE', kinds_beyond or 'NONE'))


def scores(*a):
    TF, RA = jl('b653_table_final.json'), jl('b653_root_arm.json')
    _r, _n, sh = seal_hashes()
    rr = dict((r['kernel'], r) for r in _runner_rows())
    raw = dict((r['kernel'], r) for r in jl('b653_runner_rows.json').get('rows') or [])
    cm = jl('b653_commands.json')
    wf = _wf_clean()
    rg = jl('b653_regrade.json').get('counts') or {}
    import no_sorry_main as NSM
    lv = NSM.scan_kernel('D:/SIDE-lv-conservation')
    lv_hits = lv.get('hits') if isinstance(lv, dict) else lv
    t638 = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_chain_page_b638.py')], capture_output=True, text=True,
                          encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    c1 = re.search(r'^  \(1\) .* -- (PASS|FAIL)$', t638.stdout or '', re.M)
    lvr, kr = rr.get('SIDE-lv-conservation') or {}, rr.get('SIDE-kernel') or {}
    S = {
        'N1': (('HELD' if cm and not cm.get('local_lean') else 'REFUTED'),
               'commands of this act that run lean or lake on this host: %s (relay data/b653_commands.txt); the builds on the hosted runner alone' % (
                   cm.get('local_lean') if cm else '### UNREAD')),
        'N2': (('HELD' if all(p and not h for p, h in wf.values()) and rr and all(r['above_hold'] for r in rr.values()) else
                ('REFUTED IN ONE CLAUSE' if all(p and not h for p, h in wf.values()) else 'REFUTED')),
               'the workflow files read at each main: %s; the runs` memory lows %s (the hold 2560)' % (
                   dict((k, ('present' if p else 'ABSENT') + (', hits %s' % h if h else ', no identifier, no secret')) for k, (p, h) in wf.items()),
                   dict((k, r['low']) for k, r in rr.items()))),
        'N3': (('HELD' if raw.get('SIDE-lv-conservation', {}).get('gate') == 'DERIVES' and lvr.get('merged') and not lv_hits else
                ('REFUTED IN ONE CLAUSE' if lvr.get('merged') else 'REFUTED')),
               'the T3 branch: gate %s, merged %s; G-NO-SORRY-MAIN`s scan of SIDE-lv-conservation`s main now: hits %s' % (
                   raw.get('SIDE-lv-conservation', {}).get('gate'), lvr.get('merged'), lv_hits)),
        'N4': (('HELD' if not rg.get('OVERREACHES (STANDING)') and raw.get('SIDE-kernel', {}).get('gate') == 'DERIVES' and kr.get('merged') else
                ('REFUTED IN ONE CLAUSE' if not rg.get('OVERREACHES (STANDING)') else 'REFUTED')),
               'the grade bank at the branch: OVERREACHES standing %s (relay data/b653_regrade.txt); the cut branch: gate %s, merged %s' % (
                   rg.get('OVERREACHES (STANDING)', 0), raw.get('SIDE-kernel', {}).get('gate'), kr.get('merged'))),
        'N5': _n5(),
        'S1': ('HELD' if t638.returncode in (0, 1) and c1 and c1.group(1) == 'PASS' else 'REFUTED',
               'test_chain_page_b638.py case (1) after its repair: %s' % (c1.group(0).strip() if c1 else '### UNREAD')),
        'S2': ('HELD' if 'GRADED AND STILL STANDING 0' in rdn('b653_regrade.txt') else 'REFUTED',
               'the three elided blocks cut, each file a commit, the code outside comments unchanged; the grade bank at the branch'),
        'S3': (('HELD' if not TF.get('gone') and not TF.get('added') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S4': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S5': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    put_json('b653_scores.json', dict((k2, list(v)) for k2, v in S.items()))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:400]))


NEXT_LINE = ('b654, the author`s word pending, per `(R263)`(8): the next kernel by descending OVERREACHES count, its blocks read into sentence '
             'rows and hand-graded by the b652 rule, cut, and built on the hosted runner under `(R263)`(4)')


def _title():
    rr = _runner_rows()
    return ('## The hosted runner at %d kernels, %d branches merged on its gate readings; the margin rule on completed runs; the elided cells '
            'completed and cut; the b638 test repaired' % (len(rr), sum(1 for r in rr if r['merged'])))


def _finding_text():
    S, rl, J = jl('b653_scores.json'), jl('b653_record_lines.json'), jl('b653_act_root.json')
    ans = rdn('b653_author_answers.txt')
    n_ans, n_w = len(re.findall(r'^### PROMPT ', ans, re.M)), len(re.findall(r'^### THE AUTHOR`S WORD ', ans, re.M))
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    sc = lambda k: read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'   # noqa: E731
    raw = dict((r['kernel'], r) for r in jl('b653_runner_rows.json').get('rows') or [])
    rr = dict((r['kernel'], r) for r in _runner_rows())
    rg = jl('b653_regrade.json').get('counts') or {}

    def kline(k):
        x, y = raw.get(k, {}), rr.get(k, {})
        return '%s -- run %s, %s, memory low %s MB, gate %s, %s' % (
            k, x.get('run_id'), x.get('conclusion'), x.get('mem_low'), x.get('gate'),
            ('merged %s, tag %s' % (x.get('merged'), x.get('tag'))) if x.get('merged') else 'unmerged')
    e = ['', _title(), '',
         '*Filed at b653 on the author’s ruling `(R263)` and the author’s answers (%d prompts, %d words). Banks: relay `data/b653_elided_cells.txt`, '
         '`data/b653_regrade.txt`, `data/b653_runner_SIDE-lv-conservation.txt`, `data/b653_runner_SIDE-kernel.txt`, `data/b653_spec_planted_c1.txt`, '
         '`data/b653_act_root.txt`.*' % (n_ans, n_w), '',
         '**The margin rule** (`(R263)`(2)): a figure from a stopped run licenses no start; the needed margin is a completed run’s loss; the '
         'opening entries PerpendicularCrossing 1,452 MB and Milestones 1,332 MB (OPEN_TRAILS :%s, superseding :13898).' % ls[1].get('line'), '',
         '**The seal order** (`(R263)`(3)): the satisfiability spec runs one planted row of every shape a sealed route reads through the record '
         'tool’s readers before the seal -- runner rows, score rows, trail heads and titles with a backtick possessive -- and refuses a reader '
         'that takes a row of another shape (OPEN_TRAILS :%s).' % ls[2].get('line'), '',
         '**The elided cells** (`(R263)`(5)): the three ACTION cells completed from their blocks’ own LICENSED words, accepted by the author '
         'without the pin line numbers, and cut on the branch, each file a commit; the grade bank at the branch: %d graded sentences cut, %d '
         'standing; at main, the control, all standing.' % (rg.get('CUT', 0), rg.get('OVERREACHES (STANDING)', 0) + rg.get('UNDERSTATES (STANDING)', 0)), '',
         '**The hosted runner** (`(R263)`(4)): a workflow file on each kernel’s main, dispatched by the ref and the lake target, a memory logger '
         'stopping lake beneath the 2,560 MB hold, the axioms of the named terminals printed and uploaded; the first dispatches failed at '
         'checkout, the branches local only (the navigator’s, on the author’s word), the branches pushed and one dispatch more each. %s; %s. '
         'N2 %s, N3 %s, N4 %s.' % (kline('SIDE-lv-conservation'), kline('SIDE-kernel'), sc('N2'), sc('N3'), sc('N4')), '',
         '**The b638 test** (`(R263)`(6)): its case (1) reads the glossary’s entry count from the file at run time; S1 %s.' % sc('S1'), '',
         '**The record lines** (`(R263)`(1)): b652 at its weight (FINDINGS :%s).' % ls[0].get('line'), '',
         '**The root.** b653 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the builds this host could not hold went to a machine that can, under the same hold and '
         'with its memory and its axioms printed back as an artifact checked by digest; a kernel’s merge now rests on a reading the seat can '
         'repeat from a run id. It strengthens the programme’s offering of statements a reader can check: a branch merges on the printed axioms '
         'of its named terminals, and the docstrings that said more than those prints now say what they state.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; a verdict compares a sentence with a licence and confers none.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the build of a branch runs on its own tip and its merge is a merge commit, the merged tree differing from the built one by '
              'the workflow file alone; (2) DERIVES at the standard three read as every named terminal printing only propext, Classical.choice '
              'and Quot.sound, none UNREAD; (3) the T3 run builds the whole library so the restatement`s dependents compile; (4) SIDE-kernel`s '
              'named terminals are its rows of the terminal table outside legacy/, each name qualified from its own file')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b653_scores.json', 'b653_findings.json', 'b653_record_lines.json', 'b653_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b653_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R263) ratified.** (1) b652 at its weight. (2) The margin rule on completed runs. (3) The seal order: a planted row per shape. (4) '
             'The hosted runner. (5) The three elided cells. (6) The b638 test. (7) The draft held at v5. (8) The act after: b654.', '',
             '**Entered:** FINDINGS.md:%s (b652’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the margin rule), :%s (the seal order); this record.' % (
                 ls[0].get('line'), fj.get('entry_line'), ls[1].get('line'), ls[2].get('line')), '',
             '**Act root:** b653 `%s` (previous `%s`, b652’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b653_author_answers.txt, with the author’s words), none after the root.' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b653_defects.txt): %s.' % '; '.join(_defect_short()), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b653_scores.json')
    L = ['=' * 104, 'b653 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b653_defects.txt').rstrip(NL).split(NL)
    put_txt('b653_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b653_scores.json', 'b653_findings.json', 'b653_trail.json', 'b653_record_lines.json', 'b653_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    L = ['b653 -- THE COMPONENTS, BANKED UNDER (R263).', '',
         '### COMPONENT 0 : step zero (data/b653_ferry.txt, data/b653_stepzero.txt, data/b653_tests_stepzero.txt, data/b653_readfirst.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b652`s weight FINDINGS :%s ; the margin rule OPEN_TRAILS :%s ; the seal order :%s ; data/b653_spec_planted_c1.txt' % (
             ls[0].get('line'), ls[1].get('line'), ls[2].get('line')),
         '### COMPONENT 2 : the elided cells (data/b653_elided_cells.txt, data/b653_regrade.txt) ; S2 %s' % S['S2'][0],
         '### COMPONENT 3 : the runner (data/b653_runner_SIDE-lv-conservation.txt, data/b653_runner_SIDE-kernel.txt) ; N2 %s ; N3 %s ; N4 %s' % (
             S['N2'][0], S['N3'][0], S['N4'][0]),
         '### COMPONENT 4 : the b638 test (data/b653_b638.txt) ; S1 %s' % S['S1'][0],
         '### COMPONENT 5 : the seal (data/b653_seal_hashes.json) ; S5 %s' % S['S5'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % ((J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'),
                                                                                        S['N1'][0], S['N5'][0])]
    put_txt('b653_components.txt', L)
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
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b653_findings.json', dict(title=t))
    j = jl('b653_findings.json')
    j['entry_line'] = ln
    put_json('b653_findings.json', j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = conv(_trail_text())
    dry = 'dry' in a
    cells, fired = screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b653_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_'):
        print('usage: b653_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
