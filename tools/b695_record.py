# -*- coding: utf-8 -*-
"""b695_record.py -- THE ACT'S RECORD TOOL, b695 under (R305).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b695's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b694_record.py (and b693_record.py's re-cut routes) in stages: the helpers, the guarded landing, the
### readers, step zero's rowgen and branches routes and the answers route first (stage one); Component 1's weight line and corrigendum at
### Component 1; the re-cut routes at Component 2; the faces and spec routes at Component 3; the late routes at Component 4. Every python
### child is started as `python -X utf8`, no environment mapping passed.
### Routes: `python tools/b695_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
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
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b695_worklist as K          # noqa: E402

SP = K.SP
STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)
RELAY = ROOT
ACT, PREV = 'b695', 'b694'


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
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank (b694's, carried)."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b695_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b695_findings.json': dict(entry_line=99999, title='stand-in'),
        'b695_trail.json': dict(line=99999),
        'b695_act_root.json': dict(root='0' * 64, previous='012ffed6' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return _standins().get(name, {}) if STANDIN else {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def grc(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').returncode


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b695's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, '%s_scanfile_%s.md' % (ACT, tag))
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


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R305)(1)
WH = ('*Appended 2026-10-20 by b695 to b694’s entry (:9548), under `(R305)`(1) -- b694 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b694_closing.txt):*')
WB = (' “b694 closed: relay 0c1287a2, PLACE-papers 4a21fa9; suite 122 of 124; root 012ffed645f69af6…; 6 prompts answered; 12 defects” '
      '(data/b694_closing.txt :1), the closing 6e451686 pushed and read back at relay main (data/b694_closing_push_out.txt :5). The Weil-face '
      'witness at Q0 FOUND on b518’s notched window carried to wider widths: P − PR + A for Z_Q at the off-line zero ρ₀ = 0.95326… + 16.29021…i '
      'negative beyond its bound at every width from a = 32 to a = 192, the narrowest margin at a = 32, −7.7752874967979 ± 1.43e-18, positive '
      'at 14.1, 16 and 24 (data/b694_witness.txt :12-:20, :34); the identity control agreeing at all 34 cells over 182 certified zeros, |Z − S| '
      'between 3e-25 and 1e-12 (:8, :12-:28); the ζ control nonnegative beyond its bound at all 16 cells, read before any Q0 value; the centred '
      'family positive at every width as the phase reading predicted (:21-:28). The caveats as entered: the archimedean and zero-side tail '
      'bounds float bounds with a safety factor, some 18 orders beneath the margin, not balls (W-ORD-WITNESS-TAIL-BALLS, OPEN_TRAILS :15166); '
      'the zero tail resting on P3, derived and not compiled; nothing of the kernel; T1 the control’s wording defect, the midpoints agreeing to '
      '9e-33; b518’s float figure 2.33e-6 off against its 5.34e-8 bound, the identity holding on that window (W-ORD-B518-FLOAT, :15168). The '
      'closure step on SIDE-lv-conservation at d38f3e8, run 39465780735, its eight terminals at the standard three, prints equal, no module '
      'touched, no tag (data/b694_runner_SIDE-lv-conservation_after.txt :30); CLAUSE-DOMINANCE 1 of 2 faces kernels, SIDE-explicit-formula '
      'holding and SIDE-lv-conservation absent, its lakefile forbidding dependence on sister kernels, the clause reaching it through the faces '
      'page’s Correspondence row (data/b694_circuit_dominance.txt :7-:8, :12). b693’s weight line at :9540, the corrigendum at :9542, the deletes '
      'rule (data/b694_rules.txt row (1)), the closing tool’s look-up keyed to one form with its seeded control (data/b694_lookup_control.txt). '
      'The suite 123 of 124 before the push and 122 of 124 after, NOT CLEAN, neither failure declared: (k) G-RULE-BINARY-HASHES on the circuit '
      'figure’s hashes bank naming its PNG under b692’s path, (l) G-RULE-ONE-GIT-WRITE on three git writes in one message at 18:38:58Z, all '
      'landed and read back, nothing rewritten, left as they stand under data/b692_rules.txt row (1) (data/b694_defects.txt :43, :52; the '
      'corrigendum beneath). All eight scores HELD (data/b694_scores_close.json); the sealed tools 11 of 11 (data/b694_closing.txt :17); the '
      'root 012ffed6 over 77 banks (data/act_roots.txt :72); mirror-refresh-2026-10-20-b694.zip CLEAN with the root line. Twelve defects '
      '(a)-(l), (c)-(g) and (j) the navigator’s. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B694_ENTRY,
         check=[('FINDINGS.md', K.B694_ENTRY, '## The Weil-face witness at Q0 on the notched window'),
                ('OPEN_TRAILS.md', K.B694_TRAIL, '### b694')], dry=dry)


# ================================================================================ COMPONENT 2: THE NAMING, (R305)(3) (b693's tie route, carried)
LICENSED_NOW = 'b690_r3_licensed.txt'      # ### reading 3's per-document rows, b648 -> b680 -> b690
KROW = re.compile(r'^  (SIDE-[\w-]+) docstrings \(read at (\w+)\)\s+(\d+) ->\s+(\d+) ->\s+(\d+)\s+\[(.*?)\]')
CUTS_SINCE = (('SIDE-rcurve', 'b691_cut.txt', 33), ('SIDE-archimedean', 'b693_cut.txt', 28))   # ### the kernels cut since b690, by their banks
TSUM = re.compile(r'^### ### \*\*(SIDE-[\w-]+): ROWS (\d+) ; MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+) ;')


def read_table_sum(l):
    """a per-document table's summary line (data/b647_table_<kernel>.txt): returns (kernel, rows, matches, understates, overreaches,
    unlicensed)."""
    m = TSUM.match(l or '')
    if not m:
        raise ValueError('table summary of another shape: %r' % (l,))
    return (m.group(1),) + tuple(int(x) for x in m.groups()[1:])


READERS_TIE = ['read_table_sum']


def tie(*a):
    """data/b674_rules.txt row (2) printed verbatim (:8-:11) and b652's order (data/b652_ferry.txt :19) verbatim; then every kernel row of
    reading 3's licensed table (relay data/b690_r3_licensed.txt, b648 -> b680 -> b690) by line, each kernel cut since b690 replaced by its cut
    bank's line (b691 SIDE-rcurve, b693 SIDE-archimedean); the kernels by descending count; where several stand at the top count, b674's rule
    applied in its written order -- the OVERREACHES counts of each table's summary line, then the rows outside LICENSED/CITED of any kind, then
    the larger table -- each step printed; and only then the document named. data/b695_tie.txt (.json)."""
    rl = rdn('b674_rules.txt').split(NL)[7:11]
    if not rl or not rl[0].startswith('  (2) THE TIE-BREAK BEYOND THE COUNT'):
        sys.exit('### data/b674_rules.txt :8 DOES NOT CARRY ROW (2) -- NOTHING WRITTEN')
    order = rdn('b652_ferry.txt').split(NL)[18]
    if 'the next kernel by descending count' not in order:
        sys.exit('### data/b652_ferry.txt :19 DOES NOT CARRY b652`s ORDER -- NOTHING WRITTEN')
    lt = rdn(LICENSED_NOW).split(NL)
    over = {}
    for k, bank, ln in CUTS_SINCE:
        cl = rdn(bank).split(NL)
        m = re.search(r'%s RE-CUT: THE DISTANCE BEFORE (\d+), AFTER (\d+)' % re.escape(k), cl[ln - 1] if len(cl) >= ln else '')
        if not m:
            sys.exit('### data/%s :%d DOES NOT CARRY %s`s DISTANCE -- NOTHING WRITTEN' % (bank, ln, k))
        over[k] = (int(m.group(2)), 'relay data/%s :%d (cut, THE DISTANCE BEFORE %s, AFTER %s)' % ((bank, ln) + m.groups()))
    rows = []
    for i, l in enumerate(lt, 1):
        m = KROW.match(l)
        if m:
            k, now, src = m.group(1), int(m.group(5)), 'relay data/%s :%d' % (LICENSED_NOW, i)
            if k in over:
                now, src = over[k]
            rows.append(dict(kernel=k, line=i, row=l.strip(), now=now, source=src, table=m.group(6).split(' ')[0].replace('data/', '')))
    rows.sort(key=lambda r: -r['now'])
    top = [r for r in rows if r['now'] == rows[0]['now']] if rows and rows[0]['now'] > 0 else []
    steps = []
    for r in top:
        sl = [x for x in rdn(r['table']).split(NL) if x.startswith('### ### **%s: ROWS' % r['kernel'])]
        _k, n, mt, us, ov, ul = read_table_sum(sl[0] if sl else '')
        r.update(table_rows=n, overreaches=ov, any_kind=n - mt, summary=sl[0] if sl else '')
    cand = list(top)
    if len(cand) > 1:
        mo = max(r['overreaches'] for r in cand)
        steps.append('(i) THE OVERREACHES COUNTS: %s ; the greatest %d ; standing %s' % (
            ', '.join('%s %d' % (r['kernel'], r['overreaches']) for r in cand), mo, [r['kernel'] for r in cand if r['overreaches'] == mo]))
        cand = [r for r in cand if r['overreaches'] == mo]
    if len(cand) > 1:
        ma = max(r['any_kind'] for r in cand)
        steps.append('(ii) EQUAL OVERREACHES: THE ROWS OUTSIDE LICENSED/CITED OF ANY KIND: %s ; the greatest %d ; standing %s' % (
            ', '.join('%s %d' % (r['kernel'], r['any_kind']) for r in cand), ma, [r['kernel'] for r in cand if r['any_kind'] == ma]))
        cand = [r for r in cand if r['any_kind'] == ma]
    if len(cand) > 1:
        mr = max(r['table_rows'] for r in cand)
        steps.append('(iii) EQUAL OF ANY KIND: THE LARGER TABLE: %s ; the largest %d ; standing %s' % (
            ', '.join('%s %d rows' % (r['kernel'], r['table_rows']) for r in cand), mr, [r['kernel'] for r in cand if r['table_rows'] == mr]))
        cand = [r for r in cand if r['table_rows'] == mr]
    named = cand[0] if len(cand) == 1 else None
    L = ['b695 -- COMPONENT 2, (R305)(3): THE LICENSED TABLE`S NEXT DOCUMENT, b652`S ORDER AND b674`S TIE-BREAK RULE PRINTED BEFORE IT IS NAMED (%s)' % utc(), '',
         '### b652`S ORDER, VERBATIM FROM relay data/b652_ferry.txt :19:', '    ' + order, '',
         '### b674`S TIE-BREAK RULE, VERBATIM FROM relay data/b674_rules.txt :8-:11:'] + ['  ' + l for l in rl] + [
         '', '### THE KERNEL ROWS, VERBATIM (reading 3, relay data/%s, b648 -> b680 -> b690), A KERNEL CUT SINCE b690 BY ITS CUT BANK; rows are'
         % LICENSED_NOW, '### kernels: the count now | the row | the source of the count now, in descending count:']
    L += ['  %3d | %s | %s' % (r['now'], r['row'], r['source']) for r in rows]
    L += ['', '### THE ORDER APPLIED: the top count %s ; the kernels standing at it %s ; b674`s rule %s' % (
        rows[0]['now'] if rows else '### NONE', [r['kernel'] for r in top] or 'NONE',
        'NOT REACHED (one document at the top count, no tie)' if len(top) == 1 else 'REACHED: %d documents at the top count' % len(top))]
    L += ['### the tables of the kernels at the top count, their summary lines verbatim:'] + ['    relay data/%s : %s' % (r['table'], r['summary']) for r in top]
    L += ['### b674`s rule, step by step in its written order:'] + ['    ' + s for s in steps]
    L += ['', '### ### **THE NEXT DOCUMENT BY b652`S ORDER AND b674`S TIE-BREAK: %s (THE TOP COUNT %d, %d DOCUMENTS AT IT ; %s).**' % (
        named['kernel'], named['now'], len(top), 'DECIDED AT STEP %s' % ['(i)', '(ii)', '(iii)'][len(steps) - 1] if steps else 'NO TIE')
        if named else '### ### **NO DOCUMENT NAMED -- RAISED.**']
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('b695_tie.txt', L)
    put_json('b695_tie.json', dict(at=utc(), rule=rl, order=order, rows=rows, steps=steps, named=named['kernel'] if named else None))
    print(NL.join(L))


# ================================================================================ THE DISPATCH, THE RUNS AND THE PRINTS (b693's routes, carried)
STD3 = ('Classical.choice', 'Quot.sound', 'propext')


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def dispatch(*a):
    """`dispatch <kernel> <ref sha> <label> <target> [dry]`: ONE dispatch of build-module.yml at main with the ref input and the lake target;
    refused where data/b695_dispatches.json already carries the ref's tree (one dispatch per tree state). The run id read from the run list
    (the newest workflow_dispatch run created after the dispatch); a row banked."""
    kernel, ref, label, target = a[0], a[1], a[2], a[3]
    repo = 'psinary-sketch/' + kernel
    full = g('D:/' + kernel, 'rev-parse', ref).strip()
    tree = g('D:/' + kernel, 'rev-parse', full + '^{tree}').strip()
    j = jl('b695_dispatches.json') if os.path.isfile(os.path.join(D, 'b695_dispatches.json')) else {}
    rows = j.get('rows') or []
    seen = [r for r in rows if r.get('tree') == tree]
    if seen:
        sys.exit('### THE TREE %s IS ALREADY BUILT (run %s) -- NOT DISPATCHED' % (tree[:12], seen[0].get('run_id')))
    if not re.match(r'^[A-Za-z0-9_. ]+$', target):
        sys.exit('### THE TARGET %r IS OUTSIDE THE LAKE GRAMMAR -- NOT DISPATCHED' % target)
    print('  kernel %s ; ref %s ; tree %s ; target %s' % (kernel, full, tree, target))
    if 'dry' in a[4:]:
        return
    t0 = utc()
    rc, out, err = _gh('workflow', 'run', 'build-module.yml', '-R', repo, '--ref', 'main', '-f', 'ref=' + full, '-f', 'target=' + target)
    if rc != 0:
        sys.exit('### THE DISPATCH REFUSED: %s' % err[-400:])
    run_id = None
    for _i in range(12):
        time.sleep(5)
        rc, out, err = _gh('run', 'list', '-R', repo, '--workflow', 'build-module.yml', '--event', 'workflow_dispatch', '--limit', '5', '--json',
                           'databaseId,createdAt,status')
        new = [r for r in json.loads(out or b'[]') if r.get('createdAt', '') >= t0]
        if new:
            run_id = sorted(new, key=lambda r: r['createdAt'])[-1]['databaseId']
            break
    rows.append(dict(kernel=kernel, label=label, ref=full, tree=tree, target=target, dispatched=t0, run_id=run_id))
    put_json('b695_dispatches.json', dict(rows=rows))
    print('  dispatched %s ; run id %s' % (t0, run_id))


def runstatus(*a):
    """`runstatus <kernel> <run id>`: the run's status and conclusion, read once (a foreground read, no wait)."""
    rc, out, err = _gh('run', 'view', a[1], '-R', 'psinary-sketch/' + a[0], '--json', 'status,conclusion,updatedAt,headSha')
    print('  %s' % (out.decode('utf-8', 'replace').strip() or err.strip()))


def _deps(ax):
    """the axioms output read per terminal: [(name, [axioms] or None for 'does not depend on any axioms')], wrapped lists rejoined."""
    out = []
    for n, d in re.findall(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)",
                           re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax), re.M):
        out.append((n, [x.strip() for x in d.split('[', 1)[1].rstrip(']').split(',') if x.strip()] if d.startswith('depends') else []))
    return out


def read_runner_row(r):
    """a row of data/b695_runner_rows.json: the kernel, its label, the ref (40 hex), the run id and the gate; returns (kernel, label, gate)."""
    if not isinstance(r, dict) or not re.match(r'^SIDE-[\w-]+$', r.get('kernel') or '') or not re.match(r'^[\w-]+$', r.get('label') or '') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['kernel'], r['label'], r['gate']


READERS_RUN = ['read_runner_row']


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <note...>`: the kernel's run read by its id; the artifact listed, downloaded by its id into
    memory, its sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP;
    the axioms output of the print step banked whole, every name of the list matched to one printed line, each terminal's axioms read against
    the standard three. data/b695_runner_<kernel>_<label>.txt, data/b695_axioms_<kernel>_<label>.txt and a row of data/b695_runner_rows.json."""
    import hashlib
    import io as _io
    import zipfile
    kernel, run_id, ref, label, note = a[0], int(a[1]), a[2], a[3], ' '.join(a[4:])
    repo = 'psinary-sketch/' + kernel
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=kernel, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None)
    L = ['b695 -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (kernel, label.upper(), utc()), '',
         '### the dispatch: %s ; the ref input %s' % (note, ref),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt'))]
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        L.append('### the artifact: id %s ; %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if digest and digest == sha else '### NOTHING READ FROM IT'))
        if digest and digest == sha:
            row['artifact_sha256'] = sha
            with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    row['mem_low'] = int(low[-1]) if low else None
    row['stopped'] = any(l.startswith('STOP ') for l in mem.split(NL))
    blog = T_.get('build.log', '')
    row['build_exit'] = T_.get('build_exit.txt', '').strip() or None
    row['errors'] = [l for l in blog.split(NL) if ': error' in l or l.startswith('error:')]
    ax = T_.get('axioms.txt', '').rstrip(NL)
    row['axioms_sha256'] = hashlib.sha256(ax.encode('utf-8')).hexdigest() if ax else None
    deps = _deps(ax)
    tg = [l.strip() for l in T_.get('print_targets.txt', '').split(NL) if l.strip()]
    printed = [n for n, _d in deps]
    unmatched = [n for n in tg if n not in printed]
    outside = [(n, d) for n, d in deps if not set(d) <= set(STD3)]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d:' % (row['build_exit'], len(row['errors']))] + ['    ' + l for l in row['errors'][:40]] + [
          '### the log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-8:]] + [
          '### the print step: the list (out/print_targets.txt) %d names ; terminals printed %d ; every name printed once %s ; axiom-free %d ; '
          'sorryAx %d ; outside the standard three %d ; refused %s' % (
              len(tg), len(deps), not unmatched and len(printed) == len(set(printed)) == len(tg), sum(1 for _n, d in deps if not d),
              sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), T_.get('axioms_refused.txt', '').strip() or 'NONE'),
          '### rows are terminals: name | the axioms printed | within the standard three:']
    L += ['  %-62s %s %s' % (n, d, 'STD3' if set(d) <= set(STD3) else '### OUTSIDE') for n, d in deps]
    L += ['  %-62s ### NOT PRINTED' % n for n in unmatched]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not unmatched and not outside
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; '
          'OUTSIDE THE STANDARD THREE %d ; GATE %s.**' % (
              run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']),
              len(deps), len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), row['gate'])]
    read_runner_row(row)
    put_txt('b695_runner_%s_%s.txt' % (kernel, label), L)
    if row['artifact_sha256']:
        put_txt('b695_axioms_%s_%s.txt' % (kernel, label), ax.split(NL) if ax else ['### EMPTY'])
        put_txt('b695_buildlog_%s_%s.txt' % (kernel, label), blog.rstrip(NL).split(NL))
    j = jl('b695_runner_rows.json') if os.path.isfile(os.path.join(D, 'b695_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('b695_runner_rows.json', dict(rows=rows))
    print(NL.join(L[:14] + L[-3:]))


def prints(*a):
    """`prints <kernel> <before bank> <after bank>`: the 'before' terminals' printed lines compared with the same names' lines in the 'after'
    bank, line for line by name; the raw axioms banks compared byte for byte beside. data/b695_prints_<kernel>.txt."""
    kernel, bb, ab = a[0], a[1], a[2]
    b, f = rdn(bb), rdn(ab)
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bd, fd = dict(_deps(b)), dict(_deps(f))
    diff = [(n, bd[n], fd.get(n)) for n in bd if fd.get(n) != bd[n]]
    new = [n for n in fd if n not in bd]
    L = ['b695 -- THE PRINTS OF %s BEFORE AND AFTER THE CUT, BY NAME AND LINE FOR LINE (%s)' % (kernel, utc()), '',
         '### before: relay data/%s (%d terminals) ; after: relay data/%s (%d terminals) ; the two banks equal line for line: %s ; rows are the '
         'terminals that differ:' % (bb, len(bd), ab, len(fd), b == f)] + (['    %s : %s | %s' % d for d in diff] or ['    NONE']) + [
        '### the names printed after and not before: %d' % len(new)] + ['    %s %s' % (n, fd[n]) for n in new]
    L += ['', '### ### **BEFORE %d TERMINALS ; EACH PRINTED AFTER %s ; DIFFERING %d ; NEW %d ; EQUAL LINE FOR LINE %s.**' % (
        len(bd), all(n in fd for n in bd), len(diff), len(new), b == f)]
    put_txt('b695_prints_%s.txt' % kernel, L)
    print(L[-1])


# ================================================================================ COMPONENT 2: THE QUOTATION SEARCH, data/b690_rules.txt row (2) (b693's route, carried)
# ### one distinctive substring per removed or changed line of the cut, each checked to stand in its own removed line before it is searched
QUOTE_NEEDLES = ('per-parameter κ vector over a Formation', 'every non-trivial interface', 'in a determined system has a structural witness',
                 'no mechanism for θ → κ(θ) = 0')
# ### the second shape, case-blind and shorter (b690's lesson: a case-exact needle misses a quote re-set in bold or another case), one per
# ### removed line by case-blind containment; both shapes' yields printed
QUOTE_WIDE = ('vector over a formation', 'non-trivial interface', 'determined system', 'κ(θ) = 0')
QUOTE_SETS = {'quote_interfaces': (QUOTE_NEEDLES, QUOTE_WIDE)}


def quote(*a):
    """`quote <kernel dir> <base> <tip> <bank stem>`: every line the cut removes or changes (the `-` lines of git diff base..tip, comments
    alone) read, one needle of the set assigned to each by containment and refused where a removed line carries none or a needle stands
    in no removed line; each needle searched with git grep -n -F at the tip across the kernel's whole tracked tree, in two shapes; every hit
    printed with its quoting line and entered as a residue; the control at the base. data/b695_<stem>.txt (.json)."""
    kd, base, tip, stem = a[0], a[1], a[2], a[3]
    needles, wide = QUOTE_SETS[stem]
    d = g(kd, 'diff', '--unified=0', base, tip)
    removed = [l[1:].rstrip(chr(13)) for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    removed = [l for l in removed if l.strip()]
    rows, unassigned = [], []
    for l in removed:
        nd = [n for n in needles if n in l]
        if not nd:
            unassigned.append(l)
        rows.append(dict(line=l, needle=nd[0] if nd else None))
    unused = [n for n in needles if not any(n in r['line'] for r in rows)]
    if unassigned or unused:
        sys.exit('### A REMOVED LINE WITHOUT A NEEDLE %s OR A NEEDLE IN NO REMOVED LINE %s -- NOTHING WRITTEN' % (unassigned, unused))
    for r in rows:
        w = [n for n in wide if n.lower() in r['line'].lower()]
        r['wide'] = w[0] if w else None
    wu = [n for n in wide if not any(n.lower() in r['line'].lower() for r in rows)]
    if any(r['wide'] is None for r in rows) or wu:
        sys.exit('### THE SECOND SHAPE: A REMOVED LINE WITHOUT A NEEDLE OR A NEEDLE IN NO REMOVED LINE %s -- NOTHING WRITTEN' % wu)
    hits = []
    for r in rows:
        out = g(kd, 'grep', '-n', '-F', r['needle'], tip, '--')
        r['hits'] = [x for x in out.split(NL) if x.strip()]
        out2 = g(kd, 'grep', '-n', '-i', '-F', r['wide'], tip, '--')
        r['hits_wide'] = [x for x in out2.split(NL) if x.strip()]
        hits += [(r['wide'], h) for h in r['hits_wide']]
    L = ['b695 -- THE QUOTATION SEARCH BEFORE THE MERGE, data/b690_rules.txt row (2), OVER %s (%s)' % (os.path.basename(kd), utc()), '',
         '### the cut: git diff %s..%s ; the lines it removes or changes %d ; one needle each, checked to stand in its own removed line; each searched' % (
             base, tip, len(rows)),
         '### with git grep -n -F at the tip %s across the kernel`s whole tracked tree. Rows are removed lines: needle | hits (file:line: the quoting' % tip,
         '### line):']
    for r in rows:
        L.append('  %-44s | %d hit(s) ; case-blind %-26r %d hit(s) | removed: %s' % (r['needle'], len(r['hits']), r['wide'], len(r['hits_wide']),
                                                                               r['line'].strip()[:100]))
        L += ['      %s' % h for h in r['hits_wide']]
    q = sorted(set(h.split(':', 2)[1] + ':' + h.split(':', 3)[2] for _n, h in hits))
    # ### the positive control (an ABSENT carries a control): each needle, both shapes, at the base, where its removed line still stands
    ctl = [(r['needle'], len([x for x in g(kd, 'grep', '-n', '-F', r['needle'], base, '--').split(NL) if x.strip()]),
            len([x for x in g(kd, 'grep', '-n', '-i', '-F', r['wide'], base, '--').split(NL) if x.strip()])) for r in rows]
    L += ['', '### THE CONTROL: each needle at the base %s, where the removed line stands (needle ; case-exact hits ; case-blind hits):' % base]
    L += ['  %-44s ; %d ; %d' % c for c in ctl]
    L += ['### the control %s' % ('FIRES FOR EVERY NEEDLE IN BOTH SHAPES' if all(c[1] and c[2] for c in ctl) else '### DOES NOT FIRE FOR EVERY NEEDLE')]
    L += ['', '### THE QUOTING LINES, DISTINCT (file:line): %s' % (', '.join(q) or 'NONE'),
          '### the yields: the case-exact shape %d hit(s) on %d line(s) ; the case-blind shape %d hit(s) on %d line(s)' % (
              sum(len(r['hits']) for r in rows), len(set(h.split(':', 3)[1] + ':' + h.split(':', 3)[2] for r in rows for h in r['hits'])),
              len(hits), len(q)),
          '', '### ### **REMOVED OR CHANGED LINES %d ; NEEDLES SEARCHED %d IN TWO SHAPES ; QUOTING LINES %d -- EACH ENTERED AS A RESIDUE.**' % (
              len(rows), len(rows), len(q))]
    put_txt('b695_%s.txt' % stem, L)
    put_json('b695_%s.json' % stem, dict(at=utc(), kernel=kd, base=base, tip=tip, rows=rows, hits=[list(h) for h in hits]))
    print(NL.join(L))


# ================================================================================ COMPONENT 2: THE CUT BANK, (R305)(3) (b693's route, carried)
CUT = dict(kernel='SIDE-interfaces', table='b647_table_SIDE-interfaces.txt', base='58854f0', main='c8bd217', tip='69b143b', tag=K.NEXT_TAG,
           prior=K.PRIOR_TAG, workflow='9b4c484', targets='58854f0', before=39487947819, after=39488049232)
# ### each quoting line's reading, by hand after the search (data/b695_quote_interfaces.txt): (file, line) -> its disposition
RESIDUE_READ = {
    ('Interfaces/ConnectionRequiresStructure.lean', 9): 'CARRIED AS IT STANDS -- the comment over NontrivialInterface, "not all parameters are '
                                                        'dark", the def`s own body (not IsAllDark), not a quote of the removed claim; the '
                                                        'second shape`s needle "non-trivial interface" meets it',
    ('Interfaces/ConnectionRequiresStructure.lean', 20): 'CARRIED AS IT STANDS -- the comment over connection_requires_structure, "under the '
                                                         'INTERFACETS bimodality hypothesis", the theorem`s own hypothesis h_bimodality; it '
                                                         'says what the cut`s new bullet says, not the removed "in a determined system"',
    ('Interfaces/InterfaceSplit.lean', 13): 'CARRIED AS IT STANDS -- the head block`s quotation of its source`s Proposition 1 ("for any '
                                            'non-trivial interface f : A -> B ... at least one parameter is non-conservative"), a different '
                                            'claim from the removed one, carried as data by the Interface structure`s collapse field; the '
                                            'head block a MATCHES row at b647 (data/b647_table_SIDE-interfaces.txt :19)',
    ('README.md', 59): 'CARRIED AS IT STANDS -- the README`s line for connection_requires_structure, "under the INTERFACETS bimodality '
                       'hypothesis (every parameter has kappa < 0.45 or kappa >= 0.75), any non-trivial interface produces at least one '
                       'structural witness", the theorem`s own reach; outside the docstring rows the cut reaches',
}


def _norm(t):
    return ' '.join(t.replace('--', ' ').replace('—', ' ').split())


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def cut(*a):
    """data/b695_cut.txt (.json): the document named by data/b695_tie.txt; the commits on its main (the workflow and the print list alone, the
    cut on recut-interfaces-b695, the merge, the tag); the before and after runs and the prints; the distance before and after by the b670
    method -- each non-MATCHES row of its b647 table read whole, its ACTION's text (the words after `RE-CUT:`) searched, whitespace normalized,
    in the file at the merge and at the base; the quotation search's quoting lines each entered as a residue with its line and its reading;
    the generator's dry reading (cells held)."""
    k = CUT['kernel']
    kd = 'D:/' + k
    mainc = g(kd, 'rev-parse', '--short=7', 'main').strip()
    tb = rdn(CUT['table'])
    blocks = re.findall(r'(?ms)^  (%s@\w+:(\S+):(\d+)) \| (OVERREACHES|UNDERSTATES|UNLICENSED) \|.*?\n      ACTION   RE-CUT: (.*?)$' % re.escape(k), tb)
    rows = []
    for rid, f, ln, verdict, action in blocks:
        src = _show(kd, mainc, f) or ''
        src0 = _show(kd, CUT['base'], f) or ''
        rows.append(dict(row=rid, file=f, line=int(ln), verdict=verdict, action=action.strip(), applied=_norm(action) in _norm(src),
                         applied_at_base=_norm(action) in _norm(src0)))
    before = sum(1 for r in rows if not r['applied_at_base'])
    after = sum(1 for r in rows if not r['applied'])
    q = jl('b695_quote_interfaces.json')
    qlines = sorted(set((h.split(':')[1], int(h.split(':')[2]), h.split(':', 3)[3]) for _n, h in q.get('hits') or []), key=lambda x: (x[0], x[1]))
    unread = [(f, ln) for f, ln, _t in qlines if (f, ln) not in RESIDUE_READ]
    if unread:
        sys.exit('### A QUOTING LINE WITHOUT ITS HAND READING %s -- NOTHING WRITTEN' % unread)
    tie_v = ([x for x in rdn('b695_tie.txt').split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]
    cd = ([x for x in rdn('b695_correspondence_dry.txt').split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]
    tag_peel = g(kd, 'rev-parse', CUT['tag'] + '^{commit}').strip()
    prior_peel = g(kd, 'rev-parse', CUT['prior'] + '^{commit}').strip()
    tag_msg = g(kd, 'tag', '-l', '--format=%(contents:subject)', CUT['tag']).strip()
    mt, tt = g(kd, 'rev-parse', mainc + '^{tree}').strip(), g(kd, 'rev-parse', CUT['tip'] + '^{tree}').strip()
    parents = g(kd, 'rev-list', '--parents', '-n', '1', mainc).split()
    pv = ([x for x in rdn('b695_prints_%s.txt' % k).split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]
    L = ['b695 -- COMPONENT 2, (R305)(3): THE RE-CUT OF %s, ITS DISTANCE, ITS RESIDUES (%s)' % (k, utc()), '',
         '### the document: %s, named by b652`s order and b674`s tie-break at step (iii), the larger table (relay data/b695_tie.txt: %s)' % (
             k, tie_v.strip('#* ')),
         '### the commits on its main: the workflow %s alone, the print list %s alone (the Mathlib form, carried from SIDE-archimedean`s 79a8527),'
         % (CUT['workflow'], CUT['targets']),
         '### pushed by push_gated (relay data/b695_interfaces_main_push_out.txt); the cut %s on recut-interfaces-b695 (comments only: the root' % CUT['tip'],
         '### module`s header, the ACTION verbatim), pushed alone by push_gated`s branch mode named --scratch (relay data/b695_interfaces_cut_push_out.txt);',
         '### the merge %s by --no-ff, its parents %s, the merged tree %s the built tree %s (%s); the tag %s peeled to %s, its message %r naming the'
         % (mainc, ' '.join(p[:7] for p in parents[1:]), mt[:12], tt[:12], 'EQUAL' if mt == tt else '### DIFFER', CUT['tag'], tag_peel[:12], tag_msg),
         '### prior tag %s = %s (relay data/b695_interfaces_merge_push_out.txt)' % (CUT['prior'], prior_peel[:7]),
         '### the runs: before %d at main %s, after %d at the tip %s (relay data/b695_runner_%s_before.txt, _after.txt); the prints: %s' % (
             CUT['before'], CUT['targets'], CUT['after'], CUT['tip'], k, pv.strip('#* ')),
         '', '### THE DISTANCE BY THE b670 METHOD: each non-MATCHES row of relay data/%s, its ACTION`s text searched, whitespace normalized, in the' % CUT['table'],
         '### file at the base %s and at the merge %s:' % (CUT['base'], mainc)]
    L += ['  %s | %s | ACTION applied at the base %s ; at the merge %s | %s' % (r['row'], r['verdict'], r['applied_at_base'], r['applied'], r['action'][:110])
          for r in rows]
    L += ['', '### THE RESIDUES (data/b690_rules.txt row (2); relay data/b695_quote_interfaces.txt, two shapes): each quoting line, the line verbatim,',
          '### its reading by hand:']
    L += ['  R-%d  %s :%d | %s | %s' % (i, f, ln, RESIDUE_READ[(f, ln)], t[:180]) for i, (f, ln, t) in enumerate(qlines, 1)]
    L += ['', '### THE CORRESPONDENCE CELLS (relay data/b695_correspondence_dry.txt, the generator run dry): %s' % cd.strip('#* '),
          '', '### ### **%s RE-CUT: THE DISTANCE BEFORE %d, AFTER %d ; TAG %s ; %s ; QUOTING LINES %d, EACH A RESIDUE CARRIED AS IT STANDS ; THE '
          'CORRESPONDENCE CELLS HELD.**' % (k, before, after, CUT['tag'], 'PRINTS EQUAL' if 'EQUAL LINE FOR LINE True' in pv else '### PRINTS NOT EQUAL',
                                             len(qlines))]
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('b695_cut.txt', L)
    put_json('b695_cut.json', dict(at=utc(), kernel=k, rows=rows, before=before, after=after, residues=[list(x) for x in qlines], main=mainc,
                                   tip=CUT['tip'], tag=CUT['tag'], tag_peel=tag_peel, merged_tree=mt, built_tree=tt, run_before=CUT['before'],
                                   run_after=CUT['after']))
    print(NL.join(L))


# ================================================================================ COMPONENT 3: THE FACES ROW, (R305)(4) AND THE AUTHOR'S WORD AT PROMPT 1
CAVEAT_OPEN = 'tail bounds float with a safety factor, not balls (W-ORD-WITNESS-TAIL-BALLS)'
TAIL_FROM = 'negative beyond its bound at a = 32'


def facescheck(*a):
    """the author's word at prompt 1 (data/b695_author_answers.txt): one check printed before any write -- the successor's tail, from
    "negative beyond its bound at a = 32" to its end (data/b695_faces_rows.txt :19), against (R305)(4)'s caveat as the banked ruling words it
    (data/b695_ferry.txt, the quotation opening with the caveat's first words), character for character; and the glossary's spelling of the
    autocorrelation (THE_CLAUSE_AND_ITS_COMPILED_FACES.md, the classK entry) against the row's. data/b695_faces_check.txt."""
    fl = rdn('b695_ferry.txt').split(NL)
    fi = [i for i, l in enumerate(fl, 1) if CAVEAT_OPEN in l]
    m = re.search(r'“(%s.*?)”' % re.escape(CAVEAT_OPEN), fl[fi[0] - 1]) if len(fi) == 1 else None
    rows = rdn('b695_faces_rows.txt').split(NL)
    row = rows[18] if len(rows) > 18 else ''
    tail = row[row.index(TAIL_FROM):] if TAIL_FROM in row else ''
    cav = m.group(1) if m else ''
    carries = bool(cav) and (cav + '.') in tail and tail.endswith(cav + '.')
    page = rd(os.path.join(PP, K.FACES_PAGE)).split(NL)
    gl = [(i, l) for i, l in enumerate(page, 1) if l.startswith('- **classK**')]
    gspell = re.search(r'of the form (\S+ \S+ \S+) with', gl[0][1]).group(1) if len(gl) == 1 else ''
    rspell = re.search(r'k = (\S+ \S+ \S+) with h even', row).group(1) if re.search(r'k = (\S+ \S+ \S+) with h even', row) else ''
    L = ['b695 -- COMPONENT 3, (R305)(4): THE CHECK THE AUTHOR`S WORD AT PROMPT 1 ORDERS, PRINTED BEFORE ANY WRITE (%s)' % utc(), '',
         '### the caveat as (R305)(4) words it, read from relay data/b695_ferry.txt :%s (the quotation opening %r):' % (fi[0] if fi else '?', CAVEAT_OPEN),
         '    ' + cav,
         '### the successor`s tail, from %r to its end, read from relay data/b695_faces_rows.txt :19:' % TAIL_FROM,
         '    ' + tail,
         '### the tail ends with the caveat character for character, its closing period the line`s own: %s ; the caveat`s characters (U+2019 %d, U+2014 %d) '
         'equal in both: %s' % (carries, cav.count('’'), cav.count('—'), cav.count('’') == tail.count('’') and cav.count('—') == tail.count('—')),
         '', '### the autocorrelation: the glossary writes %r (PLACE-papers %s :%s, the classK entry) ; the row writes %r -> amended to the glossary`s'
         % (gspell, K.FACES_PAGE, gl[0][0] if gl else '?', rspell),
         '### spelling as the author`s word orders, that one spelling and nothing else', '',
         '### ### **THE CAVEAT CARRIED VERBATIM %s ; THE GLOSSARY`S SPELLING %r, THE ROW`S %r.**' % (carries, gspell, rspell)]
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('b695_faces_check.txt', L)
    print(NL.join(L))


CARRIED_ROW = '| keystone naming a node | `phase1.5/method/INSTRUMENTS.md` |'   # ### b693 (a)'s carried row (data/b693_defects.txt :7-:11)


def faces(*a):
    """b690's form (tools/b690_record.py :401-:456), carried: the control (b690's list re-emits the committed page byte for byte) and the
    emission of data/b695_nodes_zeta.txt, both by tools/chain_page.py --from-output data/b643_probe_out_zeta.txt into the scratchpad (no
    lean); the diff printed; with `write`, the control and the emission clean first, the page written by the generator itself (its --out the
    page), read back equal to the emission, and the diff banked as data/b695_faces_diff.txt."""
    import difflib
    import hashlib
    page = os.path.join(PP, K.FACES_PAGE)
    probe = os.path.join(ROOT, *K.PROBE.split('/'))

    def emit(nodes, out):
        r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'chain_page.py'), '--nodes', os.path.join(ROOT, *nodes.split('/')),
                            '--probe-dir', SP, '--out', out, '--from-output', probe], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.returncode, ((r.stdout or '') + (r.stderr or '')).strip().split(NL)[-1:]
    committed = open(page, 'rb').read()
    head = g(PP, 'show', 'HEAD:' + K.FACES_PAGE).encode('utf-8')
    cpath, npath = os.path.join(SP, 'b695_faces_control.md'), os.path.join(SP, 'b695_faces_emit.md')
    rc0, t0 = emit(K.NODES, cpath)
    ctl = open(cpath, 'rb').read() if os.path.exists(cpath) else b''
    control = rc0 == 0 and ctl == committed
    rc1, t1 = emit(K.NODES_NEW, npath)
    new = open(npath, 'rb').read() if os.path.exists(npath) else b''
    d = list(difflib.unified_diff(committed.decode('utf-8').split(NL), new.decode('utf-8').split(NL), 'committed', 'b695', n=0, lineterm=''))
    add = sum(1 for l in d if l.startswith('+') and not l.startswith('+++'))
    rem = sum(1 for l in d if l.startswith('-') and not l.startswith('---'))
    ca, cb = committed.decode('utf-8').split(NL), new.decode('utf-8').split(NL)
    real = [(i1 + 1, i2, j1 + 1, j2) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ca, cb, autojunk=False).get_opcodes() if op != 'equal']
    written, back = False, False
    # ### the author's word at prompt 2 (data/b695_author_answers.txt): regenerate with the row, where the control's emission differs from the
    # ### committed page in the one keystone row b693 (a) carried and in nothing else; `withrow` names that word, and is refused otherwise
    cl = ctl.decode('utf-8').split(NL)
    cops = [(op, i1, i2, j1, j2) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ca, cl, autojunk=False).get_opcodes() if op != 'equal']
    carried_only = len(cops) == 1 and cops[0][0] == 'insert' and cl[cops[0][3]:cops[0][4]] == [CARRIED_ROW]
    if 'write' in a:
        if rc1 != 0 or not (control or ('withrow' in a and carried_only)):
            sys.exit('### THE CONTROL OR THE EMISSION FAILED -- THE PAGE IS NOT WRITTEN (control %s ; the one carried row alone %s)' % (control, carried_only))
        rc2, t2 = emit(K.NODES_NEW, page)
        written = rc2 == 0
        back = open(page, 'rb').read() == new
    old_l = rdn(os.path.basename(K.NODES)).split(NL)
    new_l = rdn(os.path.basename(K.NODES_NEW)).split(NL)
    row = new_l[K.NODES_ROW - 1]
    cav = 'tail bounds float with a safety factor, not balls (W-ORD-WITNESS-TAIL-BALLS); the zero tail on P3, derived and not compiled; a ' \
          'numerical reading at a certified object, consistent with Weil’s criterion at an instance with zeros off the line — not a theorem about Q0'
    L = ['b695 -- COMPONENT 3, (R305)(4): THE WEIL-FACE LINE THROUGH THE GENERATOR, ON THE AUTHOR`S WORD AT PROMPT 1 (%s)' % utc(), '',
         '### the generator: relay tools/chain_page.py --from-output relay %s (no elaboration; no lean on this host)' % K.PROBE,
         '### the control: b690`s list (relay %s) re-emits the committed page byte for byte: %s (%d bytes ; exit %d ; the committed page equal to HEAD`s '
         'blob %s)' % (K.NODES, control, len(ctl), rc0, committed.replace(b'\r\n', b'\n') == head.replace(b'\r\n', b'\n')),
         '### the control`s differences from the committed page: %s ; the one keystone row b693 (a) carried and nothing else: %s (relay '
         'data/b695_faces_control.txt; the author`s word at prompt 2: regenerate with the row, N4 not met as worded and met in substance)' % (
             '; '.join('%s :%d-:%d -> :%d-:%d %r' % (op, i1 + 1, i2, j1 + 1, j2, cl[j1:j2]) for op, i1, i2, j1, j2 in cops) or 'NONE', carried_only),
         '### the new list: relay %s (b690`s %d lines and one more, the successor at :%d beneath the Li-face line, every other line unchanged); '
         'emitted %d bytes, exit %d, sha256 %s' % (K.NODES_NEW, len(old_l) - 1, K.NODES_ROW, len(new), rc1, hashlib.sha256(new).hexdigest()[:16]),
         '### the diff, committed page -> b695 emission (lines added %d, removed %d; with difflib`s autojunk off the lines that differ, committed -> '
         'b695: %s):' % (add, rem, '; '.join(':%d-:%d -> :%d-:%d' % r for r in real))] + ['    ' + l for l in d] + [
         '', '### the page written by the generator and read back equal to the emission: %s' % (back if 'write' in a else 'NOT YET (dry)'),
         '### the row carries (R305)(4)`s caveat verbatim, the glossary`s h ⋆ h~ and no backtick: %s ; the page carries the caveat verbatim: %s' % (
             cav in row and 'h ⋆ h~' in row and '`' not in row, cav in new.decode('utf-8')), '',
         '### the three lines of the diff, each by its cause: :3 the list`s name (b690 -> b695) ; :193 b693 (a)`s carried keystone row, taken up at '
         'this regeneration ; :733 -> :734 the backmatter paragraph, the Weil-face line appended (R305)(4)', '',
         '### ### **CONTROL EQUAL %s (ITS ONE DIFFERENCE THE CARRIED ROW %s) ; LINES ADDED %d ; REMOVED %d ; PAGE WRITTEN %s.**' % (
             control, carried_only, add, rem, written and back)]
    if 'write' in a:
        put_txt('b695_faces_diff.txt', L)
    print(NL.join(L[2:6] + L[-5:]))


# ================================================================================ COMPONENT 3: THE TRAIL LINES, (R305)(4)-(5)
OH1 = ('*Appended 2026-10-20 by b695 beneath `W-ORD-WITNESS-TAIL-BALLS` (:15166), under `(R305)`(4) -- THE TRIGGER RE-READ, THE LINE ABOVE '
       'UNCHANGED:*')
OB1 = (' the trigger “before any faces-page row carrying the witness is regenerated” is re-read as “before the tail-bound caveat is removed '
       'from the row”. The Weil-face line at Q0 was regenerated at b695 on the author’s word (PLACE-papers THE_CLAUSE_AND_ITS_COMPILED_FACES.md '
       ':734, from relay data/b695_nodes_zeta.txt :168; data/b695_faces_diff.txt) carrying the caveat “tail bounds float with a safety factor, '
       'not balls (W-ORD-WITNESS-TAIL-BALLS)” verbatim; the order’s work -- the archimedean and zero-side tail bounds as arb balls, the '
       'witness re-read -- is the condition for removing that caveat, not for the row. Status OPEN.')
OH2 = ('*Appended 2026-10-20 by b695 beneath `W-ORD-H2-BRIDGE` (:10257), under `(R305)`(5) -- THE b694 READING, BY PATH AND LINE:*')
OB2 = (' CLAUSE-DOMINANCE read at b694 over the faces kernels the page names: SIDE-explicit-formula HOLDS, the clause’s compiled face h2_sign in '
       'its main theorem’s closure; SIDE-lv-conservation ABSENT, its main theorem’s closure (27 names of 608 records) not holding the clause, its '
       'lakefile forbidding dependence on a sister kernel, the clause reaching it only through the faces page’s Correspondence row (relay '
       'data/b694_circuit_dominance.txt :7-:8, :12; data/b690_nodes_zeta.txt :126). The eleventh row of the circuit specification, '
       'CORRESPONDENCE-DOMINANCE (relay data/b695_circuit_spec.txt :53-:64), ties that ABSENT to this order as one question: whether a kernel’s '
       'compiled face is the clause’s statement under the Correspondence row, by statement identity read from both print banks, '
       'HOLDS-BY-CORRESPONDENCE or DIFFERS with the differing binder named -- a spec row, no tool built.')


def trails(*a):
    """the trigger re-read beneath W-ORD-WITNESS-TAIL-BALLS's line and the b694 reading beneath W-ORD-H2-BRIDGE's, through the guarded
    landing; data/b695_trail_lines.json."""
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', OH1, NL + OH1 + OB1 + NL), ('OPEN_TRAILS.md', OH2, NL + OH2 + OB2 + NL)], '%s_trail_lines.json' % ACT, 'c3trail',
         check=[('OPEN_TRAILS.md', 15166, 'W-ORD-WITNESS-TAIL-BALLS'), ('OPEN_TRAILS.md', 10257, 'W-ORD-H2-BRIDGE'),
                ('OPEN_TRAILS.md', K.B694_TRAIL, '### b694')], dry=dry)


# ================================================================================ THE READERS, ONE PER ROW SHAPE A ROUTE READS ((R263)(3))
BRANCH_FATES = ('DELETED', 'KEPT', 'RAISED')


def read_branch_row(r):
    """a row of data/b695_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


READERS = ['read_branch_row'] + READERS_TIE + READERS_RUN


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b695_rowgen_<stage>.txt."""
    stage = a[0] if a and a[0] not in ('dry',) else 'stepzero'
    R = roster()
    paths = [os.path.join(PP, p) for _n, p in R]
    miss = [p for p in paths if not os.path.exists(p)]
    if len(R) != 19 or miss:
        sys.exit('### THE ROSTER IS NOT 19 PATHS AT HEAD: %d, missing %s' % (len(R), miss))
    t0 = time.time()
    con = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'rowgen', 'rowgen.py'), 'constellation', PP] + paths,
                         capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=500)
    dif = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'rowgen', 'diff_rowpin.py'), os.path.join(T, 'rowgen', 'namemap.json')] + paths,
                         capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=500)
    secs = int(time.time() - t0)
    co, do = (con.stdout or '') + (con.stderr or ''), (dif.stdout or '') + (dif.stderr or '')
    tail = lambda t: [l for l in t.replace(chr(13), '').split(NL) if l.strip()][-12:]   # noqa: E731
    L = ['%s -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (ACT, stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('%s_rowgen_%s.txt' % (ACT, stage), L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R305)(6))
# ### the deletes ran before this route was written (data/b695_defects.txt (a)); each tip is read from git's own reply to the delete, as banked
# ### by hand in data/b695_branches.txt, and resolved to its full name by rev-parse (the commits stand on main)
def branches(*a):
    """data/b695_branches.json from data/b695_branches.txt's rows: each branch (R305)(6) names, its tip as git's delete reply gave it, resolved
    to 40 hex; merged into main read again as the tip's ancestry; fate DELETED."""
    rows = []
    t = rdn('b695_branches.txt')
    for repo, bs in K.DELETE:
        for b in bs:
            m = re.search(r'branch -d %s \| Deleted branch %s \(was ([0-9a-f]{7,40})\)\.' % (re.escape(b), re.escape(b)),
                          NL.join(l for l in t.split(NL) if os.path.basename(repo).split('-')[0] in l or repo.split('/')[-1] in l))
            short = m.group(1) if m else ''
            tip = g(repo, 'rev-parse', '--verify', '--quiet', short + '^{commit}').strip() if short else ''
            merged = bool(tip) and grc(repo, 'merge-base', '--is-ancestor', tip, 'main') == 0
            local_now = bool(g(repo, 'branch', '--list', b).strip())
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED' if not local_now else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[]))
    print(NL.join('  %-24s %-24s %s merged %s %s' % (os.path.basename(r['repo']), r['branch'], r['tip'][:12], r['merged'], r['fate']) for r in rows))


# ================================================================================ THE ANSWERS BANK (b694's route, carried)
def _session_rows():
    for sid, anc in ((K.SESSION_ID, K.ANCHOR),) + K.SESSIONS_AFTER:
        start = None
        for i, raw in enumerate(io.open('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, encoding='utf-8', errors='replace'), 1):
            try:
                o = json.loads(raw)
            except ValueError:
                continue
            if start is None and anc in raw.replace('’', "'") and o.get('type') == 'user' and not o.get('isCompactSummary'):
                start = i
            if start is not None:
                yield i, o, start, sid
        if start is None and sid != K.SESSION_ID:
            sys.exit('### THE ANCHOR %r IS NOT A USER LINE OF SESSION %s -- NOTHING WRITTEN' % (anc, sid))


def answers(*a):
    """data/b695_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
    every word of the author delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim; a word opened by
    BEGIN with no END noted (b689's route)."""
    calls, results, words, plain_, start = [], {}, [], [], None
    for i, o, st, sid in _session_rows():
        start = st if sid == K.SESSION_ID else start
        ln = i if sid == K.SESSION_ID else '%s:%d' % (sid[:8], i)
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
                    plain_.append((ln, t.strip()))
        texts = [re.sub(r'(?s)^\s*<pasted_content[^>]*>\s*(.*?)\s*</pasted_content[^>]*>\s*$', r'\1', t or '') for t in texts]
        ask = set(x[1] for x in calls)
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion' and o.get('type') == 'assistant':
                calls.append((ln, c['id'], c['input'], o.get('timestamp')))
                ask.add(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask and o.get('type') == 'user':
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')
                results[c.get('tool_use_id')] = (ln, t, o.get('timestamp'))
                texts.append(t)
        for t in texts:
            for mm in re.finditer(r'(?s)(?:\A\s*|="|="\(for the seat, verbatim\):\s*)BEGIN\s*(.*?)\s*END(?=\s*\Z|")', t or ''):
                if K.ANCHOR not in mm.group(1) and 'RULING (' not in mm.group(1)[:20]:
                    words.append((ln, mm.group(1)))
    if start is None:
        sys.exit('### THE ANCHOR IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    L, n = [], 0
    for i, cid, inp, ts in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %s, %s)' % (cid, K.SESSION_ID, i, ts))
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
        W += ['### THE AUTHOR`S WORD (transcript line %s), BEGIN to END, verbatim:' % i] + w.replace('\r', '').split(NL) + ['']
    for cid, (i, t, _ts) in results.items():
        for mm in re.finditer(r'="BEGIN(?:(?!END").)*?"(?=, "|\.\s|$)', t or '', re.S):
            if not re.search(r'END"\s*$', mm.group(0)):
                W += ['### NOTE (transcript line %s): a word opened by BEGIN and carrying NO END marker -- %r ... %r; its text is the RESULT line '
                      'above.' % (i, mm.group(0)[2:80], mm.group(0)[-60:]), '']
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### %s -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                ACT, n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('%s_author_answers.txt' % ACT, [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('%s_author_answers.json' % ACT, dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                                for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE CARRY-TIME READING (the ferry's Component 4): the repairs bank
def _fn_src(src, name):
    L = src.split(NL)
    i = next((k for k, l in enumerate(L) if l.startswith('def %s(' % name)), None)
    if i is None:
        return []
    j = i + 1
    while j < len(L) and (not L[j] or L[j][0] in ' \t#' or L[j].startswith(')')):
        j += 1
    while j > i + 1 and not L[j - 1].strip():
        j -= 1
    return L[i:j]


def repairs(*a):
    """data/b695_tool_repairs.txt: rows are repairs with the defect or order they answer, each diff beneath its row (difflib, unified, over the
    function the repair touches, the carried copy against this act's). The suite, gate, spec and closing tools are carried from b694's with this
    act's names and banks; the two rows below are the changes to a carried route's logic."""
    import difflib
    rec4 = rd(os.path.join(T, 'b694_record.py'))
    rec0 = rd(os.path.join(T, 'b690_record.py'))
    me = rd(os.path.join(T, 'b695_record.py'))
    d1 = list(difflib.unified_diff(_fn_src(rec4, 'prev_capture'), _fn_src(me, 'prev_capture'), 'tools/b694_record.py prev_capture (sealed at b694)',
                                   'tools/b695_record.py prev_capture (this act)', lineterm=''))
    d2 = list(difflib.unified_diff(_fn_src(rec0, 'faces'), _fn_src(me, 'faces'), 'tools/b690_record.py faces (sealed at b690)',
                                   'tools/b695_record.py faces (this act)', lineterm=''))
    L = ['%s -- THE CARRY-TIME READING, THE FERRY`S COMPONENT 4: THE REPAIRS TO CARRIED ROUTES (%s)' % (ACT, utc()), '',
         '### rows are repairs with the defect or order they answer: the tool and route ; what it answers ; the form. Each diff beneath its row,',
         '### written by this route (difflib over the function the repair touches). The suite, gate, spec and closing tools are carried from b694`s',
         '### with this act`s names, banks and arms; no shared tool is edited.', '',
         '  (1) tools/b695_record.py prev_capture, carried from tools/b694_record.py -- ANSWERS the ferry`s G-EDIT-ROUTE window ("the previous act',
         '      after its post-push suite") where both acts run in ONE session (b97f6790): b694`s window ran from its post-push combine to the',
         '      session`s end, which here would take this act`s own commands into the previous act`s. THE FORM: the window from b694`s post-push',
         '      combine to the timestamp of the user line carrying (R305)`s anchor, exclusive.', '']
    L += ['      ' + l for l in d1] + ['']
    L += ['  (2) tools/b695_record.py faces, carried from tools/b690_record.py -- ANSWERS the author`s word at prompt 2 (relay',
          '      data/b695_author_answers.txt; data/b695_faces_control.txt): the control`s emission differed from the committed page in the one',
          '      keystone row b693 (a) carried. THE FORM: the write refused unless the control is byte for byte OR, under `withrow`, its one',
          '      difference is exactly that row (an insertion of CARRIED_ROW and nothing else); the control`s differences printed; the caveat and',
          '      the glossary`s spelling read in the new list`s row.', '']
    L += ['      ' + l for l in d2] + ['']
    L += ['### ### **REPAIRS 2 ; THE PREVIOUS ACT`S WINDOW BOUNDED AT THIS ACT`S ANCHOR ; THE PAGE WRITE UNDER THE CARRIED ROW ON THE AUTHOR`S WORD ; '
          'DIFF LINES %d ; NO SHARED TOOL EDITED.**' % (len(d1) + len(d2))]
    put_txt('%s_tool_repairs.txt' % ACT, L)
    print(L[-1])


# ================================================================================ THE DEFECTS BANK (b694's route and its row reader, carried)
DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short(act=ACT):
    out = []
    L = rdn('%s_defects.txt' % act).split(NL)
    for i, l in enumerate(L):
        if DEFECT_ROW.match(l):
            j = i + 1
            while j < len(L) and L[j].startswith('    ') and not DEFECT_ROW.match(L[j]) and not L[j].startswith('    ###'):
                j += 1
            m = re.match(r"^\(([a-z]'?)\) (.*?)\.(?= |$)", ' '.join(x.strip() for x in L[i:j]))
            if m:
                out.append(m.group(0)[:-1])
    return out


def defects(*a):
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


# ================================================================================ THE CAPTURE AND THE COMMANDS (b694's, carried; ONE SESSION FOR BOTH ACTS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
# ### the previous act's window: b694 ran in this same session; from the call that combined its post-push parts to this act's anchor line
PREV_ACT, PREV_SESSION, PREV_ANCHOR = 'b694', K.SESSION_ID, 'RULING (R304) BEGIN'


def _bg_calls():
    out = set()
    for _i, o, _st, _sid in _session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and (c.get('input') or {}).get('run_in_background'):
                out.add((o.get('timestamp'), (c.get('input') or {}).get('command')))
    return out


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    rows.sort(key=lambda r: r['ts'])
    bg = _bg_calls()
    for i, r in enumerate(rows):
        r['n'] = i + 1
        r['bg'] = (r.get('ts'), r.get('cmd')) in bg
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')
SED = re.compile(r'(^|[;&|(]\s*|\s)sed\s')
PY_PRINT_READ = re.compile(r'python[^\n]*\s-c\s')
REDIRECT_ANY = re.compile(r'(?<![<>=\-\w])(?:\d?>>?|&>)(?!&)\s*\S')
PIPE_FILTER = re.compile(r'\|\s*(?:head|tail|wc|grep|cut|sort|uniq|awk|less|more|tr)\b')
SED_KIND = 'R sed in any form (data/b685_rules.txt row (2))'


def local_lean(cmd):
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def sed_cmd(cmd):
    return SED.search(QUOTED.sub('""', cmd)) is not None


def _anchor_ts(anchor, session=SESSION):
    for ln in io.open(session, encoding='utf-8', errors='replace'):
        if anchor in ln:
            try:
                j = json.loads(ln)
            except ValueError:
                continue
            if j.get('type') == 'user' and not j.get('isCompactSummary'):
                return j.get('timestamp')
    return None


def prev_capture():
    """G-EDIT-ROUTE's window over the previous act: b694, in this same session, from the call that combined its post-push parts into
    data/b694_checks_postpush.txt to the user line carrying this act's anchor (data/b695_tool_repairs.txt row (1))."""
    rows = ER.capture(SESSION, PREV_ANCHOR, SUBAGENTS)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV_ACT in r['cmd'] and '--combine' in r['cmd']]
    end = _anchor_ts(K.ANCHOR)
    if not first or not end:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE OR THIS ACT`S ANCHOR IS NOT IN THE SESSION`S CAPTURE -- NOTHING READ')
    out = [dict(r, src='%s %s' % (PREV_ACT, r['src'])) for r in rows if first[0] <= r['ts'] < end]
    for i, r in enumerate(out):
        r['n'] = 'p%d' % (i + 1)
    return out


def edit_route_offences(rows):
    out = []
    for r in rows:
        o = list(ER.offences(r['cmd']))
        if r['tool'] in ('Bash', 'PowerShell') and sed_cmd(r['cmd']) and not any(k.startswith('S sed') for k, _ in o):
            o.append((SED_KIND, r['cmd'].split(NL)[0][:120]))
        if o:
            out.append((r, o))
    return out


MOVE_OR_DELETE = re.compile(r'\bgit\s+(-C\s+\S+\s+)?(mv|rm)\b|\bgit\s+(-C\s+\S+\s+)?branch\s+-[dD]\b|--delete\b|(^|[;&|]\s*|\s)rm\s+-|Remove'
                            + r'-Item|\bos\.remove\b')
REDIRECT_NULL = re.compile(r'\d?>\s*/dev/null')
SHELL_VAR = re.compile(r'\$(?:\?|\{[^}]*\}|[A-Za-z_]\w*|\d)')


def delete_shape(cmd):
    """(R305)(6) and the ferry: a delete command names one branch and carries no glob and no variable in any half; b693's reader, carried."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    vs = SHELL_VAR.findall(c)
    return names, [ch for ch in '*?[' if ch in SHELL_VAR.sub('', c)], vs


def chained_after(cmd):
    """data/b694_rules.txt row (1): anything chained after a delete in the same command (`;`, `&&`, `||`, `|`), read outside quoted strings."""
    c = QUOTED.sub('""', cmd)
    m = re.search(r'(--delete\s+\S+|branch\s+-[dD]\s+\S+)', c)
    return bool(m) and bool(re.search(r'[;&|]', c[m.end():]))


IDENT = ('psinary', 'hotmail', 'seale', 'york', 'orcid', '0009-0008')


def outbound():
    out = []
    for i, o, _st, _sid in _session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') in ('WebSearch', 'Agent', 'WebFetch'):
                inp = c.get('input') or {}
                text = inp.get('query') or inp.get('prompt') or inp.get('url') or ''
                out.append(dict(line=i, tool=c['name'], ts=o.get('timestamp'), text=text))
    for r in out:
        r['identifiers'] = [w for w in IDENT if w in r['text'].lower()]
    return out


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = edit_route_offences(rows)
    prev = prev_capture()
    phits = edit_route_offences(prev)
    sh_ = [r for r in rows if r['tool'] in ('Bash', 'PowerShell')]
    lean = [r for r in sh_ if local_lean(r['cmd'])]
    mv = [r for r in sh_ if MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in sh_ if re.search(r'(^|&&\s*|;\s*)gh workflow run\b|b695_record\.py dispatch [^\s;]+ [^\s;]+ [^\s;]+ [^\s;]+\s*(?:;|$)',
                                        QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in sh_ if (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
    seds = [r for r in sh_ if sed_cmd(r['cmd'])]
    nulls = [r for r in sh_ if REDIRECT_NULL.search(QUOTED.sub('""', r['cmd']))]
    redir = [r for r in sh_ if REDIRECT_ANY.search(QUOTED.sub('""', r['cmd']))]
    pipes = [r for r in sh_ if PIPE_FILTER.search(QUOTED.sub('""', r['cmd']))]
    pyreads = [r for r in sh_ if PY_PRINT_READ.search(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    chained = [r['n'] for r in mv if delete_shape(r['cmd'])[0] and chained_after(r['cmd'])]
    halves = dict((r['n'], len([x for x in re.split(r'&&|\|\||;|\|', QUOTED.sub('""', r['cmd'])) if x.strip()])) for r in mv)
    ob = outbound()
    L = ['%s -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % (ACT, utc()), '',
         '### the source: the seat`s session %s from its first user line carrying %r, with its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (b694, this same session %s, from its post-push combine to this act`s '
              'anchor): %d commands from %s, its offences printed whole (%d):' % (PREV_SESSION[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES, BY THE RECORD TOOL`S dispatch ROUTE (%d):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN, BY THEIR TEXT OR THE TOOL`S run_in_background PARAMETER (%d):' % len(
        detach)] + (['  #%d %s%s' % (r['n'], '[run_in_background] ' if r.get('bg') else '', r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT ONTO /dev/null, read outside quoted strings (%d):' % len(nulls)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], r['cmd'].split(NL)[0][:200]) for r in nulls] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT OF ANY STREAM, read outside quoted strings (%d):' % len(redir)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in redir] or ['  NONE'])
    L += ['', '### THE COMMANDS PIPING INTO A SHELL FILTER (head, tail, wc, grep and the like), read outside quoted strings (%d):' % len(pipes)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in pipes] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT RUN AN INTERPRETER`S ONE-LINE PROGRAM (python -c), each its first line (%d):' % len(pyreads)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:220]) for r in pyreads] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R305)(6) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
              'nothing chained after): ' + ('; '.join('#%d deletes %s, halves %d, globs %s, variables %s, chained after %s' % (
                  n, d, halves.get(n, 0), gl or 'none', vs or 'none', n in chained) for n, d, gl, vs in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git (web searches, subagent prompts and fetches), each with the author`s identifiers found in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    good = sum(1 for n, d, gl, vs in shapes if len(d) == 1 and not gl and not vs and n not in chained)
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; REDIRECTS ONTO /dev/null %d ; '
              'REDIRECTS OF ANY STREAM %d ; PIPES INTO A SHELL FILTER %d ; ONE-LINE PROGRAMS %d ; MOVE OR DELETE COMMANDS %d ; BRANCH DELETES OF ONE '
              'BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(nulls), len(redir), len(pipes), len(pyreads), len(mv), good, len(shapes), len(ob),
                  sum(1 for r in ob if r['identifiers']))]
    put_txt('%s_commands.txt' % ACT, [l.replace('\r', '') for l in L])
    put_json('%s_commands.json' % ACT, dict(at=utc(), anchor=K.ANCHOR, rows=rows,
                                           offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                           prev=dict(act=PREV_ACT, session=PREV_SESSION, rows=len(prev),
                                                     offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                           local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                           seds=[r['n'] for r in seds], null_redirects=[r['n'] for r in nulls], redirects=[r['n'] for r in redir],
                                           pipes=[r['n'] for r in pipes], py_programs=[r['n'] for r in pyreads], moves_deletes=[r['n'] for r in mv],
                                           delete_shapes=[dict(n=n, deletes=d, globs=gl, variables=vs, halves=halves.get(n), chained=n in chained)
                                                          for n, d, gl, vs in shapes],
                                           outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


# ================================================================================ THE LATE ROUTES (b694's, carried with b695's names)
def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection', 'SIDE-class-number-anomaly',
                                   'SIDE-spinor', 'SIDE-li-map', 'SIDE-rcurve', 'SIDE-archimedean', 'SIDE-interfaces']


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('%s_kernels_face.json' % ACT, dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-interfaces read after its merge c8bd217 and tag v0.2.1; none written after this read)' % len(ks))


def seal_hashes():
    import hashlib
    rec_ = (jl('%s_seal_hashes.json' % ACT).get('tools') or {}) if os.path.isfile(os.path.join(D, '%s_seal_hashes.json' % ACT)) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def root_banks_state(banks, rev='HEAD'):
    import hashlib
    head = g(ROOT, 'rev-parse', rev).strip()
    rem = (g(ROOT, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    rows = []
    for b in banks:
        st = g(ROOT, 'status', '--porcelain', '--', b).strip()
        r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (head, b)], capture_output=True)
        p = os.path.join(ROOT, *b.split('/'))
        now = open(p, 'rb').read() if os.path.exists(p) else None
        eq = r.returncode == 0 and now is not None and hashlib.sha256(r.stdout).hexdigest() == hashlib.sha256(now).hexdigest()
        rows.append(dict(bank=b, status=st or 'clean', at_head=r.returncode == 0, equal=eq))
    return dict(head=head, remote=rem, rows=rows, clean=all(x['status'] == 'clean' and x['equal'] for x in rows) and bool(rows),
                pushed=bool(head) and head == rem)


ROOT_EXCLUDE = re.compile(r'^b695_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*|close_sentence)\.?(txt|json|md|jsonl|)$')
BINARY = ('.gz', '.png')
SHARED_APPENDED = ('data/b675_corrigenda.txt',)


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('%s_' % ACT) and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['%s -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % (ACT, utc()), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('%s_root_banks.txt' % ACT, L)
    put_json('%s_root_banks.json' % ACT, dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/%s_seal_hashes.json' % ACT in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', ACT] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('%s_act_root.json' % ACT)
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='%s_ra_' % ACT) as tmp:
        cp_ = os.path.join(tmp, os.path.basename(bank_))
        b_ = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b_[0] ^= 0x01
        with open(cp_, 'wb') as fh:
            fh.write(bytes(b_))
        items2 = [('%s %s' % (bank_, AR.sha256_file(cp_)) if it.split()[0] == bank_ else it) for it in J['items']]
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
    L = ['%s -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % (ACT, utc()), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '-')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('%s_root_arm.txt' % ACT, L)
    put_json('%s_root_arm.json' % ACT, dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    before = _rows_state(json.loads(_show(ROOT, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['%s -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (ACT, utc(), r.returncode, g(ROOT, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('%s_table_final.txt' % ACT, L)
    put_json('%s_table_final.json' % ACT, dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                              gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


def _g2_of(path):
    t = rd(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _standing():
    import b694_worklist as K694
    return sorted(set(_g2_of(os.path.join(D, 'b694_registration_2026-10-20.txt'))) - set(K694.ACT_ARMS))


def standing(*a):
    """the standing arms b695 carries: b694's face's (G2) arms less b694's act arms (R264)(2); printed only."""
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


def armsecs(*a):
    st = _standing()
    rows, phases, runs = [], {}, {}
    for p in K.PARTS:
        j = jl('%s_arm_seconds_%s.json' % (ACT, p))
        phases[p] = j.get('phases') or {}
        runs[p] = j.get('run_secs')
        for nm, s in (j.get('arms') or {}).items():
            rows.append(dict(arm=nm, part=p, secs=s, standing=nm in st))
    srows = sorted([r for r in rows if r['standing']], key=lambda r: -r['secs'])
    miss = sorted(set(st) - set(r['arm'] for r in srows))
    L = ['%s -- THE STANDING ARMS` SECONDS AT HEAD, BY PART, FROM THE PRE-RUN (%s): the per-part seconds of the six parts' % (ACT, utc()), '',
         '### the source: data/b695_arm_seconds_<part>.json, written by tools/b695_checks.py at its pre-run, each arm`s seconds the sum of its',
         '### three readings (LIVE on the sources, NEG on a copy, POS on a mutated copy); each part`s run seconds and its phases -- the sources',
         '### built once for all its arms -- printed beside, not divided among them. standing-b2 carries no arm and is clocked by its run alone.',
         '### Rows are standing arms, slowest first:']
    L += ['  %-46s %-11s %8.3f s' % (r['arm'], r['part'], r['secs']) for r in srows]
    L += ['', '### THE PARTS` SECONDS: ' + ' | '.join('%s %s s' % (p, runs[p]) for p in K.PARTS),
          '### THE PARTS` PHASES (seconds): ' + ' | '.join('%s: %s' % (p, '; '.join('%s %.0f' % kv for kv in ph.items())) for p, ph in phases.items()),
          '### the standing arms not clocked: %s' % (miss or 'NONE'),
          '', '### ### **STANDING ARMS CLOCKED %d OF %d ; THE THREE SLOWEST %s ; THEIR SECONDS SUMMED %.1f.**' % (
              len(srows), len(st), ', '.join('%s (%s, %.2f s)' % (r['arm'], r['part'], r['secs']) for r in srows[:3]) or 'NONE',
              sum(r['secs'] for r in srows))]
    put_txt('%s_arm_seconds.txt' % ACT, L)
    put_json('%s_arm_seconds.json' % ACT, dict(at=utc(), rows=srows, phases=phases, run_secs=runs, standing=len(st), clocked=len(srows), missing=miss,
                                              slowest=[r['arm'] for r in srows[:3]]))
    print(L[-1])


# ================================================================================ THE SCORES: (N1)-(N5) OF (R305)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and commits and not the entry; the entry reads the scorer's bank. `scores`
# ### writes data/b695_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there and is read at the close.
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b694_closing_push_out.txt', 'b675_corrigenda.txt')
KI = 'D:/SIDE-interfaces'
KERNEL_COMMITS = ('9b4c484', '58854f0', '69b143b', 'c8bd217')
CAVEAT = ('tail bounds float with a safety factor, not balls (W-ORD-WITNESS-TAIL-BALLS); the zero tail on P3, derived and not compiled; a '
          'numerical reading at a certified object, consistent with Weil’s criterion at an instance with zeros off the line — not a theorem about Q0')


def read_score_row(k, v):
    """a scores row: key N1..N5 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text)."""
    if not re.match(r'^(N[1-5]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


READERS += ['read_score_row', 'read_head']


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _iso_epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime((s or '')[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', 'FINDINGS.md', 'OPEN_TRAILS.md')
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _files_of(repo, rev):
    return sorted(x for x in g(repo, 'show', '--name-only', '--pretty=format:', rev).split(NL) if x.strip())


def _vl(name):
    return ([x for x in rdn(name).split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]


def _n1():
    cm = jl('%s_commands.json' % ACT)
    rows = jl('%s_runner_rows.json' % ACT).get('rows') or []
    arts = len(rows) == 2 and all(r.get('artifact_sha256') and r.get('gate') == 'DERIVES' for r in rows) \
        and sorted(r.get('label') for r in rows) == ['after', 'before']
    ok = bool(cm) and not cm.get('local_lean') and arts
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b695_commands.txt, %d commands read); runner rows %d, each run '
        'read by its id with the artifact`s sha256 equal to the platform`s before any reading, both DERIVES: %s' % (
            cm.get('local_lean') if cm else 'unread', len(cm.get('rows') or []), len(rows), arts))


def _n2():
    tj = jl('%s_tie.json' % ACT)
    tie_t = _iso_epoch(tj.get('at'))
    wf_t = _git_ct(KI, KERNEL_COMMITS[0])
    named = tj.get('named') == 'SIDE-interfaces' and bool(tj.get('steps'))
    tie_ok = named and bool(tie_t) and bool(wf_t) and tie_t <= wf_t
    fr = rdn('%s_faces_rows.txt' % ACT)
    rows_t = _git_ct(ROOT, 'a5d64b5d')
    page_t = _git_ct(PP, 'c354650')
    both = '(A) DRAFTED AT b694' in fr and '(B) THE LI-FACE LINE AT Q0 AS THE PAGE CARRIES IT' in fr and '(C) THE SUCCESSOR' in fr
    fd = rdn('%s_faces_diff.txt' % ACT)
    fd_t = _iso_epoch((re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', fd.split(NL)[0] if fd else '') or [None, ''])[1])
    rows_ok = both and bool(rows_t) and bool(fd_t) and bool(page_t) and rows_t <= fd_t and rows_t <= page_t
    return ('HELD' if tie_ok and rows_ok else 'REFUTED'), (
        'the order and b674`s tie-break with the table rows printed from the banks (relay data/b695_tie.txt at %s, its steps %d, the document %s) '
        'before the first commit on the named kernel (SIDE-interfaces %s at %s): %s; the faces rows printed, b694`s drafted row, the Li-face line '
        'and the successor (relay data/b695_faces_rows.txt, committed at a5d64b5d, %s) before the page was written (the diff bank at %s, '
        'PLACE-papers c354650 at %s): %s' % (tj.get('at'), len(tj.get('steps') or []), tj.get('named'), KERNEL_COMMITS[0], wf_t, tie_ok, rows_t, fd_t,
                                             page_t, rows_ok))


def _n3():
    cj = jl('%s_cut.json' % ACT)
    dist = bool(cj) and cj.get('after') is not None and cj.get('after') <= cj.get('before', -1)
    pr = 'EQUAL LINE FOR LINE True' in _vl('%s_prints_SIDE-interfaces.txt' % ACT)
    qj = jl('%s_quote_interfaces.json' % ACT)
    q_t = _iso_epoch(qj.get('at'))
    m_t = _git_ct(KI, KERNEL_COMMITS[3])
    qv = _vl('%s_quote_interfaces.txt' % ACT)
    quote_ok = bool(q_t) and bool(m_t) and q_t < m_t and re.search(r'QUOTING LINES \d+', qv) is not None
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    cells_ok = all(x in K.PP_WRITTEN for x in pp_ch)
    ok = dist and pr and quote_ok and cells_ok
    return ('HELD' if ok else 'REFUTED'), (
        'the distance by the b670 method before %s, after %s (relay data/b695_cut.json): at or below %s; the before and after prints equal line for '
        'line (relay data/b695_prints_SIDE-interfaces.txt): %s; the quotation search at %s before the merge %s at %s, its hit count printed (%s): %s; '
        'PLACE-papers files changed %s, no Correspondence document among them: %s' % (
            cj.get('before'), cj.get('after'), dist, pr, qj.get('at'), KERNEL_COMMITS[3], m_t,
            (re.search(r'QUOTING LINES \d+', qv) or [''])[0] if re.search(r'QUOTING LINES \d+', qv) else '### NOT READ', quote_ok, pp_ch, cells_ok))


def _n4():
    page = _show(PP, 'HEAD', K.FACES_PAGE) or ''
    carries = CAVEAT in page
    fd = rdn('%s_faces_diff.txt' % ACT)
    ctl_true = 'CONTROL EQUAL True' in fd
    ctl_carried = 'ITS ONE DIFFERENCE THE CARRIED ROW True' in fd and 'PAGE WRITTEN True' in fd
    if carries and ctl_true:
        v = 'HELD'
    elif carries and ctl_carried:
        v = 'NOT MET AS WORDED; MET IN SUBSTANCE'
    else:
        v = 'REFUTED'
    return v, (
        'the regenerated page`s Weil-face line carries (R305)(4)`s caveats verbatim (PLACE-papers %s at HEAD): %s; the control re-emitted the current '
        'page byte for byte before the generator wrote: %s -- its one difference the keystone row b693 (a) carried, the author`s word at prompt 2 '
        'entering N4 as not met as worded and met in substance, the navigator`s wording the defect (relay data/b695_faces_control.txt, '
        'data/b695_faces_diff.txt, data/b695_defects.txt (c)): %s' % (K.FACES_PAGE, carries, ctl_true, ctl_carried))


def _kernels_moved():
    t0 = _iso_epoch(_anchor_ts(K.ANCHOR) or '')
    moved, tags = [], []
    for k in dict.fromkeys(_kerns()):
        p = 'D:/' + k
        for l in g(p, 'log', '--format=%h %ct', 'main').split(NL)[:40]:
            x = l.split()
            if len(x) == 2 and x[1].isdigit() and t0 and int(x[1]) > t0:
                moved.append((k, x[0]))
        for l in g(p, 'for-each-ref', '--format=%(refname:short) %(creatordate:unix)', 'refs/tags').split(NL):
            x = l.split()
            if len(x) == 2 and x[1].isdigit() and t0 and int(x[1]) > t0:
                tags.append((k, x[0]))
    return t0, moved, tags


def _amended_after(repo, lock):
    out = []
    for l in g(repo, 'reflog', '--date=unix', '--format=%gd %gs').split(NL):
        m = re.match(r'HEAD@\{(\d+)\} (commit \(amend\).*)$', l.strip())
        if m and lock and int(m.group(1)) >= lock:
            out.append(m.group(2)[:60])
    return out


def _one_git_write():
    """the standing rule arm G-RULE-ONE-GIT-WRITE's own reading over this act's session (tools/rule_arms.py, imported unedited)."""
    import rule_arms as RA
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    try:
        S = RA.sources(ACT, SESSION, K.ANCHOR, K.PARTS, lock, K.PRE_RELAY, K.PRE_PP)
        ok, n, b, note = RA.reading('G-RULE-ONE-GIT-WRITE', S)
    except Exception as e:
        return False, 'the rule arm raised %s' % type(e).__name__
    return ok, note[:200]


def _n5():
    import rule_arms as RA
    import b694_worklist as K694
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    t0, moved, tags = _kernels_moved()
    beyond_main = [m for m in moved if not (m[0] == 'SIDE-interfaces' and m[1][:7] in KERNEL_COMMITS)]
    tags_beyond = [t for t in tags if t != ('SIDE-interfaces', K.NEXT_TAG)]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN + (K.FACES_PAGE,)]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b695_', x)]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b695_|audit_b695_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    arms_added = sorted(set(RA.NAMES) - set(K694.STANDING_ADDED) - set(_g2_of(os.path.join(D, 'b694_registration_2026-10-20.txt'))))
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock)) if lock else []
    ob = jl('%s_commands.json' % ACT).get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    wf_ident = [w for w in IDENT if w in g(KI, 'show', 'main:.github/workflows/build-module.yml').lower()]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    chained = [d['n'] for d in (jl('%s_commands.json' % ACT).get('delete_shapes') or []) if d.get('chained')]
    gw_ok, gw_note = _one_git_write()
    ok = k_ok and not beyond_main and not tags_beyond and not pp_beyond and not kinds_beyond and not shared_tools and not differ and not arms_added \
        and not amended and not ident and not wf_ident and not pat and not chained and gw_ok
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; kernel main commits '
            'since the act began beyond SIDE-interfaces` four (%s): %s; tags made since the act began beyond v0.2.1: %s; no standing arm added '
            '(tools/rule_arms.py`s names beyond b694`s face): %s; shared tools edited: %s; sealed tools not agreeing: %s; commits amended after the seal: '
            '%s; deletes with anything chained after: %s; one git write per message (G-RULE-ONE-GIT-WRITE`s reading: %s): %s; PLACE-papers beyond '
            'FINDINGS, OPEN_TRAILS and the faces page: %s; relay files of a kind beyond the act`s banks and tools, the corrigenda bank, the table, '
            'the root list and b694`s push-out bank: %s; "patent" in the lines written: %s; outbound requests other than git %d, an identifier of the '
            'author in %s; in SIDE-interfaces` workflow file: %s' % (
                K.DRAFT, k_ok, ', '.join(KERNEL_COMMITS), beyond_main or 'NONE', tags_beyond or 'NONE', arms_added or 'NONE', shared_tools or 'NONE',
                differ or 'NONE', amended or 'NONE', chained or 'NONE', gw_note, gw_ok, pp_beyond or 'NONE', kinds_beyond or 'NONE', pat or 'NONE',
                len(ob), [r['line'] for r in ident] or 'NONE', wf_ident or 'NONE'))


def _s_scores():
    import collections
    TF, RA_ = jl('%s_table_final.json' % ACT), jl('%s_root_arm.json' % ACT)
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b695_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b695_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def scores(*a):
    """`scores [dry]` writes data/b695_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b695_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('%s_scores_close.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('%s_scores.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def scores_line(S):
    """the entry's scores line, composed from the scores bank alone (the act arm G-ENTRY-SCORES-EQUAL composes it the same way and compares)."""
    return '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.'


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
def TRAIL_HEAD():
    return ('### b695 — lane two, act one hundred and twenty-two, the re-cut act under (R305): b694 at its weight; the post-seal failures by '
            'corrigendum; SIDE-interfaces cut under the quotation rule; the Weil-face line at Q0 regenerated; the eleventh spec row')


def _calls():
    return jl('%s_author_answers.json' % ACT).get('calls') or []


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _figs():
    """the figures the title and the entry carry, each read from its bank by a needle that passes a dotted name and leaves a closing period."""
    cut = jl('%s_cut.json' % ACT)
    qv = _vl('%s_quote_interfaces.txt' % ACT)
    ql = re.search(r'QUOTING LINES (\d+)', qv)
    pv = _vl('%s_prints_SIDE-interfaces.txt' % ACT)
    pt = re.search(r'BEFORE (\d+) TERMINALS', pv)
    tv = _vl('%s_tie.txt' % ACT)
    ts = re.search(r'DECIDED AT STEP (\(\w+\))', tv)
    fd = _vl('%s_faces_diff.txt' % ACT)
    reg = 'PAGE WRITTEN True' in fd
    return dict(before=cut.get('before'), after=cut.get('after'), tag=cut.get('tag') or K.NEXT_TAG, quoting=int(ql.group(1)) if ql else None,
                terminals=int(pt.group(1)) if pt else None, step=ts.group(1) if ts else '', regen=reg, main=cut.get('main') or '',
                tip=cut.get('tip') or '')


def _title():
    f = _figs()
    rows = '%s row%s' % (f['before'], '' if f['before'] == 1 else 's')
    return ('## SIDE-interfaces re-cut: %s outside LICENSED/CITED to %s, %s; the Weil-face line at Q0 %s; CORRESPONDENCE-DOMINANCE specified; '
            'b694’s post-seal failures by corrigendum' % (rows, f['after'], f['tag'], 'regenerated with its caveats' if f['regen'] else 'held'))


def _finding_text():
    """the FINDINGS entry, composed before the root: its scores line from the scores bank alone (data/b686_rules.txt row (1)); the root is
    carried by the trail record."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    corr_ = _rl_lines('%s_corrigendum_landing.json' % ACT) + ['-']
    tl_ = _rl_lines('%s_trail_lines.json' % ACT) + ['-', '-']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'SIDE-interfaces’s root module header claimed more than its declarations reach: a conservation profile over a Formation, and a '
         'structural witness for every non-trivial interface in a determined system. Its one row outside LICENSED/CITED (relay '
         'data/b647_table_SIDE-interfaces.txt :10) is cut to the declarations’ own reach -- the profile over a finite parameter type, the witness '
         'under the INTERFACETS bimodality hypothesis, the Parametric Mechanism Theorem as kappa = 0 -- comments only, the prints of its %s '
         'theorems equal line for line before and after, the distance %s to %s, tagged %s.' % (f['terminals'], f['before'], f['after'], f['tag']), '',
         '*Filed at b695 on the author’s ruling `(R305)` and the author’s words at its prompts; %d questions put. Banks: relay `data/b695_tie.txt`, '
         '`data/b695_cut.txt`, `data/b695_quote_interfaces.txt`, `data/b695_prints_SIDE-interfaces.txt`, `data/b695_correspondence_dry.txt`, '
         '`data/b695_faces_rows.txt`, `data/b695_faces_check.txt`, `data/b695_faces_control.txt`, `data/b695_faces_diff.txt`, '
         '`data/b695_circuit_spec.txt`, `data/b695_corrigendum.txt`.*' % n_ans, '',
         '**The naming** (`(R305)`(3)): b652’s order and b674’s tie-break rule were printed verbatim with the kernel rows of reading 3 before the '
         'document was named. Three kernels stood at one row outside: SIDE-interfaces and SIDE-simplicity at one OVERREACHES each, '
         'SIDE-substrate-cluster at none; equal of any kind, the larger table named SIDE-interfaces, six rows to five, decided at step %s.' % f['step'], '',
         '**The cut**: the build workflow and the print list each alone on main, a before run at main and an after run at the cut’s tip, each '
         'dispatched once for its tree and read by its run id with the artifact’s sha256 first, both DERIVES at the standard three; the cut on '
         'recut-interfaces-b695, merged --no-ff at %s with the merged tree the built tree, tagged %s naming v0.2.' % (f['main'], f['tag']), '',
         '**The quotation search** (data/b690_rules.txt row (2)): before the merge, one needle per removed line in two shapes across the '
         'kernel’s tracked tree, the control firing at the base for every needle; %s quoting lines, each read by hand and carried as it '
         'stands -- two comments over the theorem’s own hypothesis, the head block’s quotation of its source’s Proposition 1, and the README’s '
         'line for the theorem. No Correspondence cell names the kernel; none was written.' % f['quoting'], '',
         '**The Weil-face line** (`(R305)`(4)): b694’s drafted row, the Li-face line at Q0 and a successor were printed before the page was '
         'touched and raised as one prompt; on the author’s word the successor’s caveat was checked character for character and the '
         'autocorrelation written as the glossary writes it, h ⋆ h~. The control re-emitted the page with one line more, the keystone row b693 '
         'carried to this regeneration; on the author’s second word the page was written by the generator from the new list with that row '
         'taken up (PLACE-papers THE_CLAUSE_AND_ITS_COMPILED_FACES.md :734). The order’s trigger was re-read beneath its line (OPEN_TRAILS :%s).' % tl_[0], '',
         '**The eleventh spec row** (`(R305)`(5)): CORRESPONDENCE-DOMINANCE, for a faces kernel whose lakefile bars the clause from its closure, '
         'HOLDS-BY-CORRESPONDENCE or DIFFERS by statement identity read from both print banks; a spec row, no tool built; W-ORD-H2-BRIDGE '
         'annotated with the b694 reading (OPEN_TRAILS :%s).' % tl_[1], '',
         '**The corrigendum** (`(R305)`(2)): b694’s two post-seal failures, G-RULE-BINARY-HASHES on a hashes bank naming its PNG under b692’s '
         'path and G-RULE-ONE-GIT-WRITE on three git writes in one message, each by its cause (FINDINGS :%s), the sealed face and the bank '
         'unedited. b694 at its weight (FINDINGS :%s).' % (corr_[0], c1_[0]), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed; %d answers checked before they were '
         'acted on.' % (cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b647’s licensed table and b690’s reading 3, b693’s cut, b694’s '
         'witness and dominance banks and b692’s circuit spec; it is re-read by b696, which takes W-ORD-WITNESS-TAIL-BALLS or '
         'CORRESPONDENCE-DOMINANCE’s build on the author’s word. It strengthens the programme’s offering of a located clause: one more kernel '
         'whose header says only what it compiles, and the Weil face standing beside the Li face at Q0 on the faces page with its caveats in place.', '',
         '**Carried to:** b696 (the research act on the author’s word); `W-ORD-WITNESS-TAIL-BALLS`; `W-ORD-B518-FLOAT` (b700); `W-ORD-H2-BRIDGE`; '
         'the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) b674`s tie-break read in its written order -- the OVERREACHES counts first, then any kind, then the larger table -- SIDE-substrate-cluster '
              'standing at one row outside by its UNLICENSED row and none OVERREACHES; (2) the cut the ACTION`s words verbatim in the header`s bullets, '
              'the rest of the header unchanged; (3) the successor row carrying the caveat in (R305)(4)`s own characters and the rest in the Li-face '
              'line`s straight form; (4) the previous act`s command window bounded at this act`s anchor, both acts in one session')


def _trail_text():
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    corr_ = _rl_lines('%s_corrigendum_landing.json' % ACT) + ['-']
    tl_ = _rl_lines('%s_trail_lines.json' % ACT) + ['-', '-']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R305) ratified.** (1) b694 at its weight. (2) The corrigendum for its post-seal failures. (3) The re-cut. (4) The witness`s faces '
             'row. (5) The eleventh spec row. (6) The branches. (7) The readfirst bank. (8) The draft held at v5. (9) The act after.', '',
             '**Entered:** FINDINGS.md:%s (b694`s weight), :%s (the corrigendum), :%s (the entry); OPEN_TRAILS :%s (the trigger re-read) and :%s '
             '(W-ORD-H2-BRIDGE annotated); the faces page :734; this record.' % (c1_[0], corr_[0], fj.get('entry_line'), tl_[0], tl_[1]), '',
             '**Act root:** b695 `%s` (previous `%s`, b694`s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s (relay data/b695_author_answers.txt); none after the root.' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The kernels:** SIDE-interfaces -- the workflow 9b4c484 and the print list 58854f0 alone on main; the cut 69b143b on '
             'recut-interfaces-b695; the merge c8bd217 --no-ff; v0.2.1 naming v0.2; runs 39487947819 and 39488049232 read by their run ids.', '',
             '**The banks:** the naming relay data/b695_tie.txt; the cut relay data/b695_cut.txt, data/b695_quote_interfaces.txt, '
             'data/b695_prints_SIDE-interfaces.txt, data/b695_correspondence_dry.txt; the faces relay data/b695_faces_rows.txt, data/b695_faces_check.txt, '
             'data/b695_faces_control.txt, data/b695_faces_diff.txt, data/b695_nodes_zeta.txt; the spec relay data/b695_circuit_spec.txt; the corrigendum '
             'relay data/b695_corrigendum.txt.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b695_closing.txt).', '',
             '**The open orders:** `W-ORD-WITNESS-TAIL-BALLS` (before the tail-bound caveat is removed from the row, re-read at :%s); `W-ORD-B518-FLOAT` '
             '(the reading act b700); `W-ORD-H2-BRIDGE` (annotated at :%s); `W-ORD-EPSTEIN-COUNT-LEAN` and the regularity-uses bank (b696, on the '
             'author`s word).' % (tl_[0], tl_[1]), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b695_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S, C = jl('%s_scores.json' % ACT), jl('%s_scores_close.json' % ACT)
    L = ['=' * 104, '%s -- THE DESK.' % ACT, '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s%s' % (
        k2, S[k2][0], S[k2][1], ('  ### AT THE CLOSE: %s -- %s' % (C[k2][0], C[k2][1])) if (S[k2][0] == 'PENDING' and C.get(k2)) else '')
        for k2 in SCORE_KEYS]
    L += [''] + rdn('%s_defects.txt' % ACT).rstrip(NL).split(NL)
    put_txt('%s_desk_notes.txt' % ACT, L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('%s_scores.json' % ACT, '%s_findings.json' % ACT, '%s_trail.json' % ACT, '%s_act_root.json' % ACT))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    corr_ = _rl_lines('%s_corrigendum_landing.json' % ACT) + ['-']
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R305).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b695_citation_check.txt), step zero (data/b695_ferry.txt, data/b695_readfirst.txt, '
         'data/b695_stepzero.txt, data/b695_tests_stepzero.txt, data/b695_rowgen_stepzero.txt, data/b695_branches.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b694`s weight FINDINGS :%s, the corrigendum :%s (data/b695_corrigendum.txt), the corrigenda bank rows (9) and (10)' % (
             c1_[0], corr_[0]),
         '### COMPONENT 2 : the naming (data/b695_tie.txt), the cut (data/b695_cut.txt, data/b695_quote_interfaces.txt, '
         'data/b695_prints_SIDE-interfaces.txt) ; N2 %s ; N3 %s' % (S['N2'][0], S['N3'][0]),
         '### COMPONENT 3 : the faces rows and the page (data/b695_faces_rows.txt, data/b695_faces_diff.txt), the spec row (data/b695_circuit_spec.txt) ; '
         'N4 %s' % S['N4'][0],
         '### COMPONENT 4 : the carry-time reading (data/b695_tool_repairs.txt), the dry-run steps (data/b695_reg_gate.txt), the seal '
         '(data/b695_seal_hashes.json), the suite in six parts, the per-part seconds (data/b695_arm_seconds.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 5 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('%s_components.txt' % ACT, L)
    print(NL.join(L[2:]))


def _land_one(path, head, e, bank, extra):
    if odd_lines(e):
        sys.exit('### ODD BACKTICKS -- NOTHING WRITTEN: %s' % odd_lines(e)[:3])
    guard_absent(path, head)
    r = append_to(path, e)
    ln = read_head(path, head)
    put_json(bank, dict(extra, line=ln, head=head, append=r, at=utc()))
    return ln


def findings(*a):
    t, e = _finding_text()
    e = conv(e)
    dry = 'dry' in a
    cells_, fired = screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells_)
        return
    if not os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, '%s_findings.json' % ACT, dict(title=t))
    j = jl('%s_findings.json' % ACT)
    j['entry_line'] = ln
    put_json('%s_findings.json' % ACT, j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = conv(_trail_text())
    dry = 'dry' in a
    cells_, fired = screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells_)
        return
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(OT, TRAIL_HEAD(), e, '%s_trail.json' % ACT, {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


FACE_REL = 'data/b695_registration_2026-10-20.txt'
FACE = os.path.join(D, 'b695_registration_2026-10-20.txt')


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them, converted by conv and run
    through the screens their landing runs, the needles the face names read in each; DRY-RUN STEP : CLEAN only when both screens are quiet and
    every needle is found. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = conv(text)
        print('  %s (the screens):' % which)
        cells_, fired = screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = _face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells_ and not fired and nd and not miss
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells_ or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


def gatebanks(*a):
    """the gate's steps between the face and the lock (b665's order), each tool's output banked by this route, never by a shell redirect."""
    import gate_hash as G

    def runb(args, out):
        r = subprocess.run([sys.executable, '-X', 'utf8'] + args, capture_output=True, cwd=ROOT)
        b_ = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            with open(p + '.tmp', 'wb') as fh:
                fh.write(b_)
            os.replace(p + '.tmp', p)
        return r.returncode, b_.decode('utf-8', 'replace')
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], '%s_reg_termscan.txt' % ACT)
    rc2, t2 = runb([os.path.join(T, '%s_regspec.py' % ACT)], '%s_regspec_run.txt' % ACT)
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/%s_satisfiable.json' % ACT, '--emit', ACT], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_%s_reg_satisfiable.txt' % ACT).split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', '%s_census_stepzero.txt' % ACT), ('b327_faces_census.py', '%s_faces_census_stepzero.txt' % ACT),
                      ('b303_pins.py', '%s_pins_stepzero.txt' % ACT)):
        rc, t = runb([os.path.join(T, tool), ACT], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/%s_reg_gate.txt' % ACT, 'data/%s_reg_termscan.txt' % ACT, 'data/%s_regspec_run.txt' % ACT, 'data/audit_%s_reg_satisfiable.txt' % ACT):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b694's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % MIRROR_TAG
STAGE = os.path.join(os.environ.get('TEMP', SP), 'mirror-build-%s' % MIRROR_TAG)


def mbuild(*a):
    if os.path.exists(ZIP) or os.path.exists(STAGE):
        sys.exit('### THE ZIP OR ITS STAGE EXISTS -- NOT STARTED')
    loc, rem = g(PP, 'rev-parse', 'HEAD').strip(), (g(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    if loc != rem:
        sys.exit('### PLACE-papers HEAD %s IS NOT THE REMOTE MAIN %s -- NOT STARTED' % (loc[:12], rem[:12]))
    t0 = time.time()
    r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(ROOT, 'tools', 'mirror_build.ps1'), '-DateTag',
                        MIRROR_TAG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_json('%s_mirror_build.json' % ACT, dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != ACT:
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT %s`s -- NOTHING WRITTEN' % (last[0], ACT))
    line = 'Act root: %s %s' % (last[0], last[1])
    man_p = os.path.join(STAGE, 'MANIFEST.md')
    raw = open(man_p, 'rb').read()
    if b'Act root: ' in raw:
        sys.exit('### THE ROOT LINE IS IN THE STAGED MANIFEST ALREADY -- REFUSING TO WRITE IT TWICE')
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    sep = '\r\n' if '\r\n' in text else '\n'
    out = text.rstrip('\r\n') + sep + sep + line + sep
    before = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    with open(man_p, 'wb') as fh:
        fh.write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('%s_mirror_root.json' % ACT, dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_txt('%s_mirror_verify.txt' % ACT, (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
    print(r.stdout[-600:])


def mbank(*a):
    import zipfile
    import b616_record as R6
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    commits = sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', NL.join(l for l in ls if '|' in l))))
    zb = open(ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('%s_mirror_verify.txt' % ACT)
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['%s -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % (ACT, utc()),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b695 (the last export b694`s, D:/MY-DOwnloads/mirror-refresh-2026-10-20-b694.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


# ================================================================================ THE ROUTES
ROUTES = dict(repairs=repairs, defects=defects, commands=commands, kernels=kernels, rootbanks=rootbanks, root=root, root_arm=root_arm,
              table_final=table_final, armsecs=armsecs, scores=scores, desk=desk, components=components, findings=findings, trail=trail,
              drycheck=drycheck, gatebanks=gatebanks, mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank, standing=standing,
              rowgen=rowgen, branches=branches, answers=answers, c1=c1, tie=tie, dispatch=dispatch, runstatus=runstatus, runner=runner,
              prints=prints, quote=quote, cut=cut, facescheck=facescheck, faces=faces, trails=trails)
_ROUTES_EARLY = dict(rowgen=rowgen, branches=branches, answers=answers, c1=c1, tie=tie, dispatch=dispatch, runstatus=runstatus, runner=runner,
              prints=prints, quote=quote, cut=cut, facescheck=facescheck, faces=faces, trails=trails)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b695_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
