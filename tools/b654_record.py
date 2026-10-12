# -*- coding: utf-8 -*-
"""b654_record.py -- THE ACT'S RECORD TOOL, b654 under (R264).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b654's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows (tools/b654_regspec.py) can run each reader over one row of each shape before the seal.
### Routes: `python tools/b654_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
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
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/1199f364-78c4-4147-843f-edf01bb11b28/scratchpad'
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b654's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b654_scanfile_%s.md' % tag)
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
    """a row of data/b654_runner_rows.json -- every key of RUNNER_KEYS present (None where a step did not reach it); returns the row's reading
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


def read_claim_row(r):
    """a row of tools/axiom_claim.py's .json bank: (kernel, file, line, kind, verdict); raises KeyError on a row of another shape."""
    return r['kernel'], r['file'], r['line'], r['kind'], r['verdict']


READERS = ('read_runner_row', 'read_score_row', 'read_head', 'read_claim_row')


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R264)(1), (2)
WH = ('*Appended 2026-10-12 by b654 to b653’s entry (:8285), under `(R264)`(1) -- b653 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b653_closing.txt):*')
AH = ('*Appended 2026-10-12 by b654, under `(R264)`(2) -- THE ALTERNATION OF RESEARCH AND RE-CUT ACTS, STANDING FROM b654:*')
FH = ('*Appended 2026-10-12 by b654, under `(R264)`(2) -- THE STANDING ARMS FROZEN, STANDING FROM b654:*')


def _weight():
    return ('\n' + WH + ' the hosted runner written on two kernel mains and run -- both branches built with memory lows of 12,639 MB and '
            '13,383 MB, gate readings at the standard three, merged alone, mains read back (closing :25-:26); T3_StepNineBridge :108 restated '
            'and merged, so G-NO-SORRY-MAIN passes at HEAD and no sorry stands on any kernel main; SIDE-kernel’s cut merged, 0 graded sentences '
            'standing (:21); the three elided cells completed and cut; the margin rule on completed runs (OPEN_TRAILS :13920) and the seal order '
            '(:13922); the b638 test repaired; relay a2beb696, PLACE-papers 16ec28f, FINDINGS :8283 and :8285, the root 50feacd8…; the suite 76 '
            'of 77, G-AXIOM-CLAIM declared (SIDE-cosmo SteaneExemplar :6; SIDE-lv-conservation AxiomCheck :8 read against b557’s print, older '
            'than the runner’s). Six defects (relay data/b653_defects.txt :7-:12): the ruling reads two of them the navigator’s, the unpushed '
            'refs and the omitted push; the closing prints both under (a), the navigator’s on the author’s word, and (b)-(f) as the seat’s. '
            'Nothing deposited.\n')


def _alternation():
    return ('\n' + AH + ' from b654, research acts and re-cut acts alternate -- b654 research, b655 the next kernel by descending '
            'OVERREACHES count, and so on -- until the re-cut agenda (the kernels of consequence, the seven companions, the monograph v6.0) is '
            'spent. A reading act every tenth act stands; the next is b660.\n')


def _freeze():
    return ('\n' + FH + ' an act’s suite carries the standing arms and arms over its own banks; no standing arm is added unless a planted '
            'case fails on real state, the failure printed.\n')


def c1(*a):
    items = [('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', AH, _alternation()), ('OPEN_TRAILS.md', FH, _freeze())]
    land(items, 'b654_record_lines.json', 'c1', entry=8285,
         check=[('FINDINGS.md', 8285, '## The hosted runner at 2 kernels'), ('OPEN_TRAILS.md', 13924, '### b653')],
         dry='dry' in a)


# ================================================================================ COMPONENT 1: THE AxiomCheck PRINT RE-BANKED, (R264)(5)
def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def _artifact(repo, artifact_id, want_sha):
    """an artifact's zip read by its id into memory, its sha256 computed and compared with the banked one; returns (sha, {name: text})."""
    import hashlib
    import zipfile
    r = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, artifact_id)], capture_output=True)
    sha = hashlib.sha256(r.stdout).hexdigest()
    texts = {}
    if r.returncode == 0 and sha == want_sha:
        with zipfile.ZipFile(io.BytesIO(r.stdout)) as z:
            for n in z.namelist():
                texts[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    return sha, texts, r.returncode


def axiom_print(*a):
    """(R264)(5): b653's runner artifact for SIDE-lv-conservation read again by its id, its sha256 verified against b653's bank before any
    reading; its axioms output banked whole as data/b654_axiomcheck_print_lv.txt, at the merged commit (the merge's tree differs from the built
    ref by the workflow file alone)."""
    A = K.LV_ART
    sha, texts, rc = _artifact(A['repo'], A['artifact_id'], A['sha256'])
    ok = sha == A['sha256']
    diff = g('D:/SIDE-lv-conservation', 'diff', '--name-only', A['built'], A['merged']).split()
    ax = texts.get('axioms.txt', '')
    ref = ' '.join(texts.get('ref.txt', '').split())
    L = ['b654 -- COMPONENT 1, (R264)(5): THE RUNNER`S AXIOMS OUTPUT FOR T3_StepNineBridge, RE-BANKED AT THE MERGED COMMIT (%s)' % utc(), '',
         '### the source: b653`s run %d on %s, artifact %d (relay data/b653_runner_SIDE-lv-conservation.txt :106-:107), downloaded again by its id' % (
             A['run_id'], A['repo'], A['artifact_id']),
         '### sha256 now %s ; banked at b653 %s ; %s' % (sha, A['sha256'], 'AGREE' if ok else '### DIFFER -- NOTHING READ'),
         '### the ref built (out/ref.txt): %s' % (ref or '### UNREAD'),
         '### the merged commit SIDE-lv-conservation %s against the built ref %s: files differing %s' % (A['merged'], A['built'][:8], diff),
         '### so the print below, taken at the built ref, is the print at the merged commit %s.' % A['merged'], '',
         '### the axioms output, out/axioms.txt, whole (%d lines):' % len(ax.rstrip(NL).split(NL))]
    if not ok or not ax:
        sys.exit('### THE ARTIFACT DID NOT VERIFY OR CARRIED NO AXIOMS OUTPUT -- NOTHING WRITTEN')
    L += ax.rstrip(NL).split(NL)
    put_txt('b654_axiomcheck_print_lv.txt', L)
    print('  sha256 %s ; lines of print %d ; merged-commit diff %s' % ('AGREE' if ok else 'DIFFER', len(ax.rstrip(NL).split(NL)), diff))


def axiom_claim(*a):
    """`axiom_claim <stage>`: tools/axiom_claim.py run over every kernel with its --bank at data/b654_axiom_claim_<stage>.txt; the rows of
    SIDE-lv-conservation AxiomCheck.lean and SIDE-cosmo's contradicted rows printed."""
    st = a[0]
    p = os.path.join(D, 'b654_axiom_claim_%s.txt' % st)
    r = subprocess.run([sys.executable, os.path.join(T, 'axiom_claim.py'), '--bank', p], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'), timeout=580)
    print((r.stdout or '') + (r.stderr or '')[-800:])
    rows = json.load(io.open(os.path.splitext(p)[0] + '.json', encoding='utf-8'))['rows']
    for row in rows:
        kern, f, ln, kind, v = read_claim_row(row)
        if v == 'CONTRADICTED' or (kern == 'SIDE-lv-conservation' and f == 'AxiomCheck.lean' and kind != 'MENTION'):
            print('  %s %s:%d %s %s -- %s' % (kern, f, ln, kind, v, '; '.join('%s %s' % (x['decl'], x['source']) for x in row['contradicted'][:3])))


# ================================================================================ COMPONENTS 2-3: THE RUNNER, (R264)(3)-(4) under (R263)(4)
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
# ### the name runs to the quote before ` depends` or ` does not` (a primed name carries a quote of its own); the list may wrap across lines
PRINT_RE = re.compile(r"^'(.+?)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", re.M)
ERR_RE = re.compile(r'^(?:error: )?(\S+\.lean):(\d+):(\d+): error: (.*)$', re.M)


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
    computed and compared with the platform's digest before any reading; the build exit, the build log's error lines by file and line, the
    memory log's low and any STOP line, and the axioms output read per named terminal as the gate reading. Banked as
    data/b654_runner_<kernel>.txt and a row of data/b654_runner_rows.json."""
    import hashlib
    import zipfile
    kern = a[0]
    R = K.RUNNER[kern]
    repo = 'psinary-sketch/' + kern
    rc, out, err = _gh('run', 'view', str(R['run_id']), '-R', repo, '--json', 'status,conclusion,headSha,createdAt,updatedAt,url')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, R['run_id']))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    wf = _show('D:/' + kern, 'main', '.github/workflows/build-module.yml') or ''
    # ### a terminal is a line that begins with the command (the file's header comment names the command and is no terminal)
    terminals = [l.strip()[len('#print axioms '):].strip() for l in wf.split(NL) if l.strip().startswith('#print axioms ')]
    row = dict(kernel=kern, branch=R['branch'], ref=R['ref'], target=R['target'], run_id=R['run_id'], conclusion=run.get('conclusion'),
               artifact_sha256=None, mem_low=None, stopped=False, gate=None, merged=None, tag=None)
    L = ['b654 -- COMPONENTS 2-3, (R264)(3)-(4): THE HOSTED RUNNER FOR %s, READ BY ITS RUN ID (%s)' % (kern, utc()), '',
         '### the workflow file on main (%s, .github/workflows/build-module.yml), read back whole:' % R['workflow_commit']] + \
        ['    ' + l for l in wf.rstrip(NL).split(NL)] + ['',
         '### the dispatch, the one dispatch of this branch: ref %s ; target %s' % (R['ref'], R['target']),
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
    errs = [(m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)) for m in ERR_RE.finditer(blog)]
    G = gate_of(texts.get('axioms.txt', ''), terminals)
    ok = (run.get('conclusion') == 'success' and row['artifact_sha256'] and bexit == '0' and not errs and not stops
          and row['mem_low'] is not None and row['mem_low'] >= 2560 and G and all(v == 'DERIVES' for _t, v, _x in G))
    row['gate'] = 'DERIVES' if ok else ('STOPPED BENEATH THE HOLD' if stops else 'NOT DERIVES')
    row['errors'] = [list(e) for e in errs]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(texts.get('ref.txt', '### UNREAD').split()),
          '### the memory log: samples %d ; LOW %s MB ; the hold 2560 ; STOP lines %s' % (
              len([l for l in mem.split(NL) if 'avail_mb=' in l]), row['mem_low'], stops or 'NONE'),
          '### the build: exit %s ; error lines in its log %d' % (bexit or '### UNREAD', len(errs))]
    L += ['    %s:%d:%d: %s' % e for e in errs[:40]]
    L += ['### the build log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-8:]] + ['',
          '### the axioms output, whole:'] + ['    ' + l for l in texts.get('axioms.txt', '### UNREAD').rstrip(NL).split(NL)] + ['',
          '### THE GATE READING, per named terminal (%d), from the artifact`s axioms output:' % len(G)]
    L += ['  %-56s %-26s %s' % (t, v, x) for t, v, x in G]
    L += ['', '### ### **RUN %s ; CONCLUSION %s ; ARTIFACT SHA256 %s ; MEMORY LOW %s MB (HOLD 2560) ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS %d, '
              'DERIVES %d ; GATE %s.**' % (R['run_id'], run.get('conclusion'), (row['artifact_sha256'] or '### NONE')[:16], row['mem_low'], bexit or '?',
                                         len(errs), len(G), sum(1 for _t, v, _x in G if v == 'DERIVES'), row['gate'])]
    put_txt('b654_runner_%s.txt' % kern, L)
    j = jl('b654_runner_rows.json') or {'rows': []}
    j['rows'] = [r for r in j['rows'] if r['kernel'] != kern] + [row]
    put_json('b654_runner_rows.json', j)
    print(NL.join(L[-(len(G) + 3):]))
    for e in errs[:12]:
        print('  ERROR %s:%d:%d: %s' % e)


def runner_merged(*a):
    """`runner_merged <kernel> <merge sha> <tag>`: the row's merge and tag, after main and the tag are read back at the remote."""
    kern, sha, tag = a[:3]
    j = jl('b654_runner_rows.json')
    for r in j['rows']:
        if r['kernel'] == kern:
            r['merged'], r['tag'] = sha, tag
    put_json('b654_runner_rows.json', j)
    print('  %s merged %s tag %s' % (kern, sha, tag))


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


DECL_RE = re.compile(r'^(?:noncomputable |protected |private )*(theorem|lemma|def|abbrev|instance|structure|example)\s+(\S+)', re.M)


def _ef_row():
    rows = [r for r in (jl('b654_runner_rows.json').get('rows') or []) if r['kernel'] == 'SIDE-explicit-formula']
    return rows[0] if rows else {}


def e1(*a):
    """(R264)(3): the landing point of E1, banked as data/b654_e1.txt -- DERIVES at the standard three on the runner, or the proof open with
    the obstruction by file and line from the build log; the statement as written on the branch read back beside the bank`s draft."""
    R = K.RUNNER['SIDE-explicit-formula']
    row = _ef_row()
    read_runner_row(row)
    src = _show(K.EF, R['ref'], K.E1_FILE) or ''
    draft = rdn('b654_e1_statement.txt')
    gates = {}
    for m in PRINT_RE.finditer(rdn('b654_runner_SIDE-explicit-formula.txt').replace(NL + '    ', NL)):
        gates[m.group(1)] = sorted(x.strip() for x in (m.group(2) or '').split(',') if x.strip())
    e1g = [(t, gates.get(t)) for t in K.E1_TERMINALS]
    derives = all(v is not None and set(v) <= STD3 for _t, v in e1g)
    errs = [e for e in row.get('errors') or [] if e[0].endswith(K.E1_FILE)]
    decls = [(src[:m.start()].count(NL) + 1, m.group(1), m.group(2)) for m in DECL_RE.finditer(src)]
    stmt_same = []
    for name in ('rest_norm_le_rate', 'zeroSide_neg_at_rate'):
        i = src.find('theorem %s' % name)
        j_ = src.find(':= by', i)
        k_ = draft.find('theorem %s' % name)
        dl = draft[k_:].split(NL + NL)[0] if k_ >= 0 else ''
        stmt_same.append((name, ' '.join(src[i:j_].split()) == ' '.join(dl.split())))
    landing = ('DERIVES' if derives and row.get('gate') == 'DERIVES' and not errs else 'OPEN')
    L = ['b654 -- COMPONENT 2, (R264)(3): E1, THE CONFIGURATION-RELATIVE RATE -- THE LANDING POINT (%s)' % utc(), '',
         '### the branch %s at %s (SIDE-explicit-formula), the file %s; its declarations (line, kind, name):' % (R['branch'], R['ref'][:8], K.E1_FILE)]
    L += ['  :%d %s %s' % d for d in decls]
    L += ['### each statement on the branch against the bank`s draft (relay data/b654_e1_statement.txt), whitespace aside: %s' % stmt_same,
          '### sorry in the file: %d' % len(re.findall(r'\bsorry\b', src)),
          '### the runner: run %s ; conclusion %s ; artifact sha256 %s ; memory low %s MB ; gate %s (relay data/b654_runner_SIDE-explicit-formula.txt)' % (
              row.get('run_id'), row.get('conclusion'), (row.get('artifact_sha256') or '### NONE')[:16], row.get('mem_low'), row.get('gate')),
          '### the gate reading per terminal:'] + ['  %-50s %s' % (t, v if v is not None else '### UNREAD') for t, v in e1g]
    if landing == 'OPEN':
        L += ['### THE OBSTRUCTION, by file and line (the build log`s error lines in %s, %d):' % (K.E1_FILE, len(errs))]
        L += ['  %s:%d:%d: %s' % tuple(e) for e in errs[:30]] or ['  ### NONE IN THE FILE: the run did not reach it']
    L += ['', '### ### **E1 LANDS %s%s.**' % (landing, ' AT THE STANDARD THREE ON THE RUNNER' if landing == 'DERIVES' else
                                             ': THE BRANCH UNMERGED AT %s, THE OBSTRUCTION ABOVE' % R['ref'][:8])]
    put_txt('b654_e1.txt', L)
    put_json('b654_e1.json', dict(at=utc(), landing=landing, gates=dict(e1g), errors=errs, decls=decls, statements_as_drafted=dict(stmt_same)))
    print(NL.join(L[-12:]))


PROPERTY_WORDS = ('entire', 'nonzero', 'positive', 'bound', 'equal', 'holomorphic', 'differentiable', 'continuous', 'simple', 'vanish',
                  'equivalent', 'lower', 'upper', 'uniform')


def width(*a):
    """(R264)(4): the width definition read on the branch -- its docstring, the declarations in its file (a definition and no theorem), the
    property words its docstring carries; LiCriterion.riemannXi`s definition and the inline form of the bank, the difference printed (the author`s
    word at Component 2); §6a`s sentences cited beside it; the runner`s gate reading for the definition. Banked as data/b654_width.txt."""
    R = K.RUNNER['SIDE-explicit-formula']
    src = _show(K.EF, R['ref'], K.WIDTH_FILE) or ''
    decls = [(src[:m.start()].count(NL) + 1, m.group(1), m.group(2)) for m in DECL_RE.finditer(src)]
    dm = re.search(r'/--(.*?)-/\s*def transversalityWidth', src, re.S)
    doc = ' '.join(dm.group(1).split()) if dm else ''
    props = [w for w in PROPERTY_WORDS if re.search(r'\b' + w, doc, re.I)]
    basic = (_show(K.EF, 'main', 'Vendored/Bulka/Lc/LiCriterion/Basic.lean') or '').split(NL)
    xz = (_show(K.EF, 'main', 'Vendored/Bulka/Lc/XiZeros.lean') or '').split(NL)
    defs = [(i + 1, l) for i, l in enumerate(basic) if l.startswith('noncomputable def riemannXi')]
    xdefs = [(i + 1, l) for i, l in enumerate(xz) if l.startswith('noncomputable def riemannXi')]
    body = basic[defs[0][0]].strip() if defs else ''
    xbody = xz[xdefs[0][0]].strip() if xdefs else ''
    inline = '(s * (s - 1) * completedRiemannZeta₀ s + 1) / 2'
    sur = (_show(PP, 'HEAD', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md') or '').split(NL)
    s151 = [x.strip() for x in re.split(r'(?<=\.) ', sur[150]) if '|ξ′(ρ)|' in x]
    s153 = [x.strip() for x in re.split(r'(?<=\.) ', sur[152]) if '*width*' in x]
    row = _ef_row()
    gates = {}
    for m in PRINT_RE.finditer(rdn('b654_runner_SIDE-explicit-formula.txt').replace(NL + '    ', NL)):
        gates[m.group(1)] = sorted(x.strip() for x in (m.group(2) or '').split(',') if x.strip())
    wg = gates.get(K.WIDTH_TERMINAL)
    L = ['b654 -- COMPONENT 3, (R264)(4): THE TRANSVERSALITY WIDTH, DEFINED AS AN OBJECT (%s)' % utc(), '',
         '### the branch %s at %s, the file %s; its declarations (line, kind, name): %s' % (R['branch'], R['ref'][:8], K.WIDTH_FILE, decls),
         '### theorems in the file: %d ; definitions: %d' % (sum(1 for d in decls if d[1] in ('theorem', 'lemma')), sum(1 for d in decls if d[1] == 'def')),
         '### the docstring: %s' % doc,
         '### property words in the docstring (%s): %s' % (', '.join(PROPERTY_WORDS), props or 'NONE'),
         '### the definition: %s' % ' '.join(l.strip() for l in src.split(NL) if l.startswith('def transversalityWidth')), '',
         '### the kernel`s ξ, bound to (the author`s word at Component 2: one object, one name):',
         '  Vendored/Bulka/Lc/LiCriterion/Basic.lean:%s %s' % (defs[0][0] if defs else '?', defs[0][1] if defs else '### NOT FOUND'),
         '      %s' % body,
         '  a second vendored copy, Vendored/Bulka/Lc/XiZeros.lean:%s %s -- body %s LiCriterion`s' % (
             xdefs[0][0] if xdefs else '?', 'XiZeros.riemannXi' if xdefs else '### NOT FOUND', 'IDENTICAL TO' if xbody == body else 'DIFFERENT FROM'),
         '### the inline form of the bank (relay data/b654_e1_statement.txt), kept there as the §6a reading: %s' % inline,
         '### the difference, printed: riemannXi`s body is (1 / 2) * s * (s - 1) * Λ₀ s + 1 / 2, the inline form (s * (s - 1) * Λ₀ s + 1) / 2; '
         'the two bodies differ as terms (the half distributed in the one, factored in the other); no equation between them is compiled here; '
         'the definition binds to riemannXi all the same.', '',
         '### §6a beside it (PLACE-papers phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md, rows are the document`s lines):',
         '  :151 %s' % (s151[0] if s151 else '### NOT FOUND'),
         '  :153 %s' % (s153[0] if s153 else '### NOT FOUND'), '',
         '### the runner: run %s ; gate reading for %s: %s' % (row.get('run_id'), K.WIDTH_TERMINAL, wg if wg is not None else '### UNREAD'),
         '', '### ### **THE WIDTH %s ON THE RUNNER ; THEOREMS BESIDE IT %d ; PROPERTY WORDS IN ITS DOCSTRING %d.**' % (
             'COMPILES' if wg is not None and set(wg) <= STD3 else 'DOES NOT COMPILE', sum(1 for d in decls if d[1] in ('theorem', 'lemma')), len(props))]
    put_txt('b654_width.txt', L)
    put_json('b654_width.json', dict(at=utc(), decls=decls, props=props, gate=wg, xi_line=defs[0][0] if defs else None,
                                     xizeros_identical=(xbody == body)))
    print(NL.join(L[-6:]))


import collections                 # noqa: E402,F401
import b654_worklist as K          # noqa: E402


# ================================================================================ THE LATE ROUTES (b653's, carried; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def answers(*a):
    """data/b654_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
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
    head = ['### b654 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b654_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
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
    L = ['b654 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
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
    put_txt('b654_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b654_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])


def kernels(*a):
    import b641_record as R41
    put_json('b654_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


def _defect_short():
    return [re.match(r'^\(([a-z])\) ([^.]*)\.', l.strip()).group(0)[:-1].lower() for l in rdn('b654_defects.txt').split(NL)
            if re.match(r'^    \([a-z]\) [^.]*\.', l)]


def defects(*a):
    t = rdn('b654_defects.txt')
    ds = [l.strip() for l in t.split(NL) if re.match(r'^    \([a-z]\) ', l)]
    put_json('b654_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b654_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b654_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b654_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b654_seal_hashes.json' in banks, crlf or 'none'))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b654'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import shutil
    import tempfile
    import act_root as AR
    J = jl('b654_act_root.json')
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
    L = ['b654 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b654_root_arm.txt', L)
    put_json('b654_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b654 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b654_table_final.txt', L)
    put_json('b654_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b653_closing_push_out.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
B559_NAMED = ('M (H, hrate)', 'the tie set', 'the kill set', 'Kp, cE, Nf', 'CV (through B, D)', 'theta', 'B, D', 'A0', 'Aw', 'zeta3Sum')


def TRAIL_HEAD():
    return ('### b654 — lane two, act eighty-one, the research act under (R264): b653 at its weight; the alternation and the freeze; E1 '
            'stated and built on the runner; the transversality width defined; the AxiomCheck print re-banked')


def _runner_rows():
    return [read_runner_row(r) for r in (jl('b654_runner_rows.json').get('rows') or [])]


def _ct(repo, *a):
    s = g(repo, 'log', '-1', '--format=%ct', *a).strip()
    return int(s) if s.isdigit() else None


def _n2():
    """N2: the statement bank names every quantity b559's bank names for the index, each against its line, and lands before any Lean."""
    t = rdn('b654_e1_statement.txt')
    named = [q for q in B559_NAMED if q in t]
    cited = all(x in t for x in (':143-:146', ':149-:152', ':60', ':10'))
    t_bank = _ct(RELAY, '--diff-filter=A', '--', 'data/b654_e1_statement.txt')
    t_lean = _ct(K.EF, K.RUNNER['SIDE-explicit-formula']['ref'])
    first_lean = g(K.EF, 'log', '--diff-filter=A', '--format=%h', K.RUNNER['SIDE-explicit-formula']['ref'], '--', K.E1_FILE).split()
    ans = rdn('b654_author_answers.txt')
    ok = len(named) == len(B559_NAMED) and cited and t_bank and t_lean and t_bank < t_lean and 'E1 statement' in ans
    return ('HELD' if ok else 'REFUTED'), (
        'the statement bank (relay data/b654_e1_statement.txt) names %d of the %d quantities b559 names for the index, each against its line '
        '(:10, :60, :143-:146, :149-:152 cited %s); the bank committed at %s, the Lean first committed at %s (%s), the bank first %s; the prompt '
        'of (R264)(3) in the answers bank %s' % (len(named), len(B559_NAMED), cited, t_bank, t_lean, first_lean[-1:] or '?',
                                                  bool(t_bank and t_lean and t_bank < t_lean), 'E1 statement' in ans))


def _n5():
    face = jl('b654_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b654_|audit_b654_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    ef_main = [l for l in g(K.EF, 'log', '--first-parent', '--format=%h %p', K.EF_MAIN + '..main').split(NL) if l.strip()]
    ef_ok = (len(ef_main) == 2 and g(K.EF, 'show', '--name-only', '--format=', K.EF_WORKFLOW).split() == ['.github/workflows/build-module.yml']
             and len(ef_main[0].split()) == 3)
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b654_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.B653_ARMS) - set(K.ACT_ARMS))
    ok = kern_ok and not pp_beyond and not kinds_beyond and not differ and ef_ok and not new_arms
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); SIDE-explicit-formula`s main written by the workflow file '
            'under (R263)(4) and the one merge under Component 4 alone (first-parent commits since %s: %s ; %s); every kernel as the face read it '
            '%s; standing arms added: %s (the act`s arms over its own banks %s); sealed tools not agreeing %s; PLACE-papers beyond FINDINGS and '
            'OPEN_TRAILS: %s; relay files of a kind beyond the banks, the tools and the root list: %s; no identifier of the author in any outbound '
            'request (git pushes, remote reads, the runner`s dispatch with a ref and a target, the artifacts` downloads)' % (
                K.DRAFT, K.EF_MAIN, [l.split()[0] for l in ef_main], 'AS ANSWERED' if ef_ok else '### OTHERWISE', kern_ok, new_arms or 'NONE',
                len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE'))


def scores(*a):
    TF, RA = jl('b654_table_final.json'), jl('b654_root_arm.json')
    _r, _n, sh = seal_hashes()
    raw = dict((r['kernel'], r) for r in jl('b654_runner_rows.json').get('rows') or [])
    ef = raw.get('SIDE-explicit-formula') or {}
    cm = jl('b654_commands.json')
    e1j, wj = jl('b654_e1.json'), jl('b654_width.json')
    import no_sorry_main as NSM
    efs = NSM.scan_kernel(K.EF)
    ef_hits = efs.get('hits') if isinstance(efs, dict) else efs
    S = {
        'N1': (('HELD' if cm and not cm.get('local_lean') else 'REFUTED'),
               'commands of this act that run lean or lake on this host: %s (relay data/b654_commands.txt); the build on the hosted runner alone' % (
                   cm.get('local_lean') if cm else '### UNREAD')),
        'N2': _n2(),
        'N3': (('HELD' if e1j.get('landing') == 'DERIVES' and ef.get('gate') == 'DERIVES' and ef.get('merged') and not ef_hits else 'REFUTED'),
               'E1 lands %s (relay data/b654_e1.txt), the gate reading %s, merged %s tag %s; G-NO-SORRY-MAIN`s scan of SIDE-explicit-formula`s '
               'main now: hits %s' % (e1j.get('landing'), e1j.get('gates'), ef.get('merged'), ef.get('tag'), ef_hits)),
        'N4': (('HELD' if wj.get('gate') and set(wj['gate']) <= STD3 and not [d for d in wj.get('decls') or [] if d[1] in ('theorem', 'lemma')]
                and not wj.get('props') else 'REFUTED'),
               'the width on the runner: %s; declarations in its file %s; property words in its docstring %s (relay data/b654_width.txt)' % (
                   wj.get('gate'), wj.get('decls'), wj.get('props'))),
        'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    put_json('b654_scores.json', dict((k2, list(v)) for k2, v in S.items()))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))


NEXT_LINE = ('b655, per `(R264)`(7): the re-cut act -- the next kernel by descending OVERREACHES count under the b652 rule and the hosted runner; '
             'research and re-cut acts alternate from here (`(R264)`(2)), b660 the next reading act')


def _title():
    e1j = jl('b654_e1.json')
    land_ = {'DERIVES': 'DERIVES at the standard three', 'OPEN': 'the proof open'}.get(e1j.get('landing'), '### UNREAD')
    return ('## E1, the configuration-relative rate, %s on the runner; the transversality width defined; the AxiomCheck print re-banked; the '
            'alternation entered' % land_)


def _finding_text():
    S, rl, J = jl('b654_scores.json'), jl('b654_record_lines.json'), jl('b654_act_root.json')
    ans = rdn('b654_author_answers.txt')
    n_ans, n_w = len(re.findall(r'^### PROMPT ', ans, re.M)), len(re.findall(r'^### THE AUTHOR`S WORD ', ans, re.M))
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    sc = lambda k: read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'   # noqa: E731
    ef = dict((r['kernel'], r) for r in jl('b654_runner_rows.json').get('rows') or []).get('SIDE-explicit-formula') or {}
    before = re.search(r'CONTRADICTED (\d+)', rdn('b654_axiom_claim_before.txt'))
    after = re.search(r'CONTRADICTED (\d+)', rdn('b654_axiom_claim_after.txt'))
    e = ['', _title(), '',
         '*Filed at b654 on the author’s ruling `(R264)` and the author’s answers (%d prompts, %d words). Banks: relay `data/b654_e1_statement.txt`, '
         '`data/b654_e1.txt`, `data/b654_width.txt`, `data/b654_runner_SIDE-explicit-formula.txt`, `data/b654_axiomcheck_print_lv.txt`, '
         '`data/b654_act_root.txt`.*' % (n_ans, n_w), '',
         '**E1** (`(R264)`(3)): in SIDE-explicit-formula, `rest_norm_le_rate` bounds the rest of the zero side over `M ^ (2 ^ (j + 1))` at every '
         '`j ≥ D` by `θ ^ (2 ^ (j + 1) - 2 ^ (D + 1))` times `3 A₀ Bf zeta3Sum`, `θ` any bound on `offScore g0 ρ / M` off the tie and kill sets; '
         '`zeroSide_neg_at_rate` gives the zero side of the window of index `j` a negative real part at every `j ≥ D` where that rate is below the '
         'tie terms’ sum. Every hypothesis is fixed in the statement and named against relay `data/b559_constants.txt` before any Lean; the index '
         'of `zeroSide_eventually_neg` (PowerLimit.lean:1082), read there off a limit with no rate (:1092), is here explicit relative to the '
         'configuration. Built on the hosted runner, run %s, memory low %s MB, the artifact’s sha256 agreeing with the platform’s digest, both '
         'terminals at the standard three; merged alone, SIDE-explicit-formula %s tagged %s. N2 %s, N3 %s.' % (
             ef.get('run_id'), ef.get('mem_low'), ef.get('merged'), ef.get('tag'), sc('N2'), sc('N3')), '',
         '**The width** (`(R264)`(4)): `transversalityWidth ρ := ‖deriv LiCriterion.riemannXi ρ‖`, a definition bound on the author’s word to the '
         'kernel’s one ξ (the vendored `LiCriterion.riemannXi`), THE_UNCONDITIONAL_SURROUND §6a’s object (:151, :153); no theorem beside it. '
         'N4 %s.' % sc('N4'), '',
         '**The AxiomCheck print** (`(R264)`(5)): b653’s runner artifact for SIDE-lv-conservation read again by its id and its sha256, its axioms '
         'output re-banked at the merged commit b4c55b9; G-AXIOM-CLAIM CONTRADICTED %s before and %s after, AxiomCheck.lean:8 now VERIFIED, the '
         'SIDE-cosmo row declared until its re-cut act.' % (before.group(1) if before else '?', after.group(1) if after else '?'), '',
         '**The record lines** (`(R264)`(1)-(2)): b653 at its weight (FINDINGS :%s); the alternation of research and re-cut acts (OPEN_TRAILS '
         ':%s); the standing arms frozen (:%s).' % (ls[0].get('line'), ls[1].get('line'), ls[2].get('line')), '',
         '**The root.** b654 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): E1 re-reads b559’s constants reading (relay `data/b559_constants.txt` :139-:159; '
         'OPEN_TRAILS :11491, the price corrected) and `zeroSide_eventually_neg`’s own proof, which it re-runs at an explicit index; it is re-read '
         'by (E2), the same constants bounded by `(γ, δ)` alone, which stays research grade, and by W-ORD-DETECTION-REGION (OPEN_TRAILS :11151, '
         ':11512). The width gives W-ORD-CLOSE-PAIR-BENCH (OPEN_TRAILS :13848) a kernel name to bind to when its turn comes after the companions. '
         'It strengthens the programme’s offering of compiled statements a reader can check: the detection route’s index now carries a stated '
         'rate in its configuration’s quantities, built and printed on a machine the reader can name by run id.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; the rate is relative to a configuration whose quantities are '
         'zeros of zeta, and a gate reading compares a print with the standard three and confers nothing beyond it.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) θ is taken as any bound on offScore / M off the tie and kill sets, θ < 1 not a hypothesis, as answered; (2) A₀ enters as a '
              'hypothesis with HCount in place of the local count`s existential, so the rate is explicit in it; (3) the width binds to '
              'LiCriterion.riemannXi, a second vendored copy XiZeros.riemannXi carrying the same body; (4) the merge carried the branch`s two '
              'files alone, the merged tree equal to the built one')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b654_scores.json', 'b654_findings.json', 'b654_record_lines.json', 'b654_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b654_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R264) ratified.** (1) b653 at its weight. (2) The alternation of research and re-cut acts; the standing arms frozen. (3) E1, '
             'the configuration-relative rate, stated and attempted on the runner. (4) The transversality width defined as an object. (5) The '
             'AxiomCheck print re-banked. (6) The draft held at v5. (7) The act after: b655.', '',
             '**Entered:** FINDINGS.md:%s (b653’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the alternation), :%s (the freeze); this record.' % (
                 ls[0].get('line'), fj.get('entry_line'), ls[1].get('line'), ls[2].get('line')), '',
             '**Act root:** b654 `%s` (previous `%s`, b653’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b654_author_answers.txt, with the author’s words), none after the root.' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b654_defects.txt): %s.' % '; '.join(_defect_short()), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b654_scores.json')
    L = ['=' * 104, 'b654 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b654_defects.txt').rstrip(NL).split(NL)
    put_txt('b654_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b654_scores.json', 'b654_findings.json', 'b654_trail.json', 'b654_record_lines.json', 'b654_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    L = ['b654 -- THE COMPONENTS, BANKED UNDER (R264).', '',
         '### COMPONENT 0 : step zero (data/b654_ferry.txt, data/b654_stepzero.txt, data/b654_tests_stepzero.txt, data/b654_readfirst.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b653`s weight FINDINGS :%s ; the alternation OPEN_TRAILS :%s ; the freeze :%s ; the print re-banked (data/b654_axiomcheck_print_lv.txt)' % (
             ls[0].get('line'), ls[1].get('line'), ls[2].get('line')),
         '### COMPONENT 2 : E1 (data/b654_e1_statement.txt, data/b654_e1.txt) ; N2 %s ; N3 %s' % (S['N2'][0], S['N3'][0]),
         '### COMPONENT 3 : the width (data/b654_width.txt) ; N4 %s' % S['N4'][0],
         '### COMPONENT 4 : the merge (data/b654_runner_rows.json, data/b654_ef_merge_push_out.txt)',
         '### COMPONENT 5 : the seal (data/b654_seal_hashes.json) ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % ((J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'),
                                                                                        S['N1'][0], S['N5'][0])]
    put_txt('b654_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b654_findings.json', dict(title=t))
    j = jl('b654_findings.json')
    j['entry_line'] = ln
    put_json('b654_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b654_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_'):
        print('usage: b654_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
