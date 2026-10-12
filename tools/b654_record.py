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
    """a scores row: key N1..N5, value [verdict, text]; returns (key, first verdict word, text)."""
    if not re.match(r'^N[1-5]$', k) or not isinstance(v, list) or len(v) != 2:
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


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_'):
        print('usage: b654_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
