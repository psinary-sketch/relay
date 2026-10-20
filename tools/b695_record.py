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


# ================================================================================ THE ROUTES
ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, c1=c1, tie=tie, dispatch=dispatch, runstatus=runstatus, runner=runner,
              prints=prints, quote=quote, cut=cut, facescheck=facescheck, faces=faces, trails=trails)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b695_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
