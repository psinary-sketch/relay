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


import collections                 # noqa: E402,F401
import b654_worklist as K          # noqa: E402


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_'):
        print('usage: b654_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
