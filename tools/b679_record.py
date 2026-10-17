# -*- coding: utf-8 -*-
"""b679_record.py -- THE ACT'S RECORD TOOL, b679 under (R289).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b679's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b678_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes, the
### branches route given (R289)(8)'s one remote row); the later routes are added at their components.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b679_record.py <route> [dry]`.
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
import b679_worklist as K          # noqa: E402

SP = K.SP
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
    none a number any bank carries; a stand-in run writes no bank. Carried from b678_record.py with b679's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b679_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b679_findings.json': dict(entry_line=99999, title='stand-in'),
        'b679_trail.json': dict(line=99999),
        'b679_act_root.json': dict(root='0' * 64, previous='d384fb97' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b679's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b679_scanfile_%s.md' % tag)
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


BRANCH_FATES = ('DELETED', 'KEPT')


def read_branch_row(r):
    """a row of data/b679_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


READERS = ['read_score_row', 'read_head', 'read_branch_row']


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b679_rowgen_<stage>.txt, the stage
    `stepzero` or, by argument, `after`."""
    stage = 'after' if 'after' in a else 'stepzero'
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
    L = ['b679 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % ('STEP ZERO' if stage == 'stepzero' else 'AFTER', utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b679_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R289)(8))
def branches(*a):
    """every branch (R289)(8) names, its tip read before any delete, its fate; the one remote deletion the ruling names (SIDE-silence-
    principle's recut-silence-principle-b678) read at the remote by one ls-remote and its tip printed as an ancestor of main 96b3098 or not.
    data/b679_branches.txt (.json)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    for repo, b in K.DELETE_REMOTE:
        out = g(repo, 'ls-remote', 'origin', 'refs/heads/' + b).split()
        tip = out[0] if out else ''
        anc = subprocess.run(['git', '-C', repo, 'merge-base', '--is-ancestor', tip, K.S_MAIN], capture_output=True).returncode == 0 if tip else False
        rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=anc, fate='DELETED'))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b679 -- STEP ZERO, (R289)(8): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; for a local row listed by `git branch --merged main --list <name>`,',
         '### for the remote row its tip an ancestor of main %s by `git merge-base --is-ancestor` ; fate. Deleted by name in the house form, each' % K.S_MAIN,
         '### delete command naming one branch with no glob in any half, one command per call, in sequence; no branch the ruling does not name.']
    L += ['  %-24s %-30s %-6s %s ; %s %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'],
                                                  'merged into main' if r['where'] == 'local' else 'ancestor of main %s' % K.S_MAIN, r['merged'],
                                                  r['fate']) for r in rows]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED OR ANCESTOR %d ; TO BE DELETED %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows))]
    put_txt('b679_branches.txt', L)
    put_json('b679_branches.json', dict(at=utc(), rows=rows))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R289)(1)-(3)
WH = ('*Appended 2026-10-17 by b679 to b678’s entry (:9022), under `(R289)`(1) -- b678 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b678_closing.txt):*')
WB = (' “b678 closed: relay 9ae206f5, PLACE-papers 935f8df, SIDE-silence-principle 96b3098 v0.2.1; suite 88 of 88; root d384fb97f3770665…; '
      '0 prompts answered; 2 defects” (data/b678_closing.txt :1), the closing pushed at relay 435ceb1f (data/b678_closing_push_out.txt :4). '
      'The readings as the banks print them: N1–N5 and S1–S3 HELD (:47–:54); the 36 Q0 sentences on 35 ledger lines answered by one generated '
      'corrigendum entry at FINDINGS :8977, “TO RE-CUT ROWS 36 ; HAND COUNT 36 ; WRITTEN 36 ; CARRIED 0” (:22), no ledger line rewritten or '
      'pinned, `W-ORD-Q0-CLASS-LINES` DISCHARGED at OPEN_TRAILS :14618, the one row at FINDINGS :4437 quoted through its closing backtick and '
      'said so in its row; SIDE-silence-principle named by b652’s order and b674’s tie-break, 48 rows against SIDE-bijection’s 30 at the '
      'count 4 each (:25; data/b678_cut.txt :14–:16), its workflow and a 58-name print list committed alone on main, the cut docstrings alone, '
      'both runner builds DERIVES with 58 prints equal line for line (runs 39055170313, 39055212218), merged 96b3098, tag v0.2.1, rows '
      'outside LICENSED/CITED 4 to 1 (:27), Theorem 8.1’s title and the header’s introduction carried as residues; the five Correspondence '
      'cells of FOUNDATIONS_OF_THE_SIDE_PROGRAMME :628–:630 not written, the generator’s reader not seeing the runner print banks, carried at '
      'OPEN_TRAILS :14620; the suite in three foreground parts, the longest 302 s (data/b678_checks_postpush.txt :7), relay '
      'data/b678_rules.txt row 1. Two defects, both the seat’s: (a) delete commands sent in parallel calls, (b) a push piped through tail '
      '(data/b678_defects.txt :5, :10), the rules as written and this act’s deletes one per message its repair. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b679_record_lines.json', 'c1', entry=K.B678_ENTRY,
         check=[('FINDINGS.md', K.B678_ENTRY, '## Q0 class lines'), ('OPEN_TRAILS.md', K.B678_TRAIL, '### b678')], dry=dry)


ORDERS = 'b670_work_orders.txt'
ORDER = 'W-ORD-CORRESPONDENCE-RUNNER-BANKS'
OH = ('*Appended 2026-10-17 by b679 beneath the five Correspondence cells’ line (:14620), under `(R289)`(3) -- THE ORDER '
      '`W-ORD-CORRESPONDENCE-RUNNER-BANKS` ENTERED:*')
OB = (' that relay tools/correspondence_gen.py’s reader be extended to the runner print banks, so that a kernel’s profile cell reads its '
      'print bank at the kernel’s last tag where one exists. Trigger: the re-cut act after b680. Consumers: the five Correspondence cells '
      'of FOUNDATIONS_OF_THE_SIDE_PROGRAMME :628–:630 that b678 did not write and carried at :14620 (relay data/b678_closing.txt :170). '
      'Status OPEN. Its row in relay data/b670_work_orders.txt, appended additively.')


def c1order(*a):
    """(R289)(3): the order on OPEN_TRAILS beneath the carried cells' line, then its row appended to the orders bank additively ((R254)(2))."""
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', OH, NL + OH + OB + NL)], 'b679_record_lines_order.json', 'c1order',
         check=[('OPEN_TRAILS.md', K.NINE_KERNELS_LINE, 'nine-kernels')], dry=dry)
    if dry:
        return
    ol = jl('b679_record_lines_order.json')['lines'][0]['line']
    rows = ['### Appended 2026-10-17 by b679 under (R289)(3) (additive, (R254)(2)): W-ORD-CORRESPONDENCE-RUNNER-BANKS entered, its Status cell '
            'filled and its line its pin.',
            '  %-44s :%d  %s   %-5d %-16s :%d  %s [:%d]' % (ORDER, ol, 'b679', 0, 'OPEN', ol, 'the re-cut act after b680', ol)]
    p = os.path.join(D, ORDERS)
    old = open(p, 'rb').read()
    sep = NL if old.endswith(b'\n') else NL + NL
    new = old + (sep + NL.join(rows) + NL).encode('utf-8')
    if not new.startswith(old):
        sys.exit('### THE ORDERS BANK APPEND IS NOT ADDITIVE -- NOTHING WRITTEN')
    open(p + '.tmp', 'wb').write(new)
    os.replace(p + '.tmp', p)
    print('  data/%s appended (%d bytes before, %d after): %s' % (ORDERS, len(old), len(new), rows[1].strip()[:120]))


# ================================================================================ COMPONENT 3: THE RUNS ON THE HOSTED RUNNER (b678's runner, carried)
def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def _deps(ax):
    return re.findall(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)",
                      re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax), re.M)


def runner(*a):
    """`runner <run id> <ref>`: SIDE-explicit-formula's run read by its id; the artifact listed, downloaded by its id into memory, its sha256
    against the platform's digest BEFORE any reading; the build's exit and error lines (each with file and line), the memory log's low and
    any STOP; the axioms output banked whole, every name of the list matched to one printed line, and the gate per terminal (DERIVES at the
    standard three). data/b679_runner_run<id>.txt, data/b679_axioms_run<id>.txt and a row of data/b679_runner_rows.json."""
    import hashlib
    import io as _io
    import zipfile
    run_id, ref = int(a[0]), a[1]
    rc, out, err = _gh('run', 'view', str(run_id), '-R', K.K_REPO, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (K.K_REPO, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(run_id=run_id, ref=ref, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None, stopped=False, build_exit=None,
               errors=[], axioms_sha256=None)
    L = ['b679 -- COMPONENT 3, (R289)(6): THE HOSTED RUNNER FOR SIDE-explicit-formula, READ BY ITS RUN ID (%s)' % utc(), '',
         '### the dispatch: at main %s (build-module.yml), the ref input %s (strip-variant-b679) ; the target `%s`' % (K.KREV, ref, K.K_TARGET),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt'))]
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (K.K_REPO, art['id'])], capture_output=True)
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
    std = {'propext', 'Classical.choice', 'Quot.sound'}
    axs = lambda d: set(x.strip() for x in d.split('[', 1)[1].rstrip(']').split(',') if x.strip()) if '[' in d else set()   # noqa: E731
    gate = [(n, 'DERIVES' if axs(d) <= std else 'NOT DERIVES: ' + d) for n, d in deps]
    row['gate_rows'] = gate
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d:' % (row['build_exit'], len(row['errors']))] + ['    ' + l for l in row['errors'][:60]] + [
          '### the log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-8:]] + [
          '### the print step: the list (out/print_targets.txt) %d names ; terminals printed %d ; every name printed once %s ; unmatched %s ; '
          'sorryAx %d ; refused %s' % (len(tg), len(deps), not unmatched and len(printed) == len(set(printed)) == len(tg), unmatched or 'NONE',
                                       sum(1 for _n, d in deps if 'sorryAx' in d), T_.get('axioms_refused.txt', '').strip() or 'NONE'),
          '### the gate per terminal (DERIVES: the printed axioms within the standard three, no sorryAx):'] + [
          '  %-62s %s' % (n, gv) for n, gv in gate]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not unmatched and all(gv == 'DERIVES' for _n, gv in gate)
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    L += ['', '### ### **RUN %s ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; GATE %s.**' % (
        run_id, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']), len(deps),
        len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), row['gate'])]
    put_txt('b679_runner_run%d.txt' % run_id, L)
    if row['artifact_sha256']:
        put_txt('b679_axioms_run%d.txt' % run_id, (ax or '### NO AXIOMS OUTPUT').split(NL))
        put_txt('b679_buildlog_run%d.txt' % run_id, blog.rstrip(NL).split(NL))
    j = jl('b679_runner_rows.json') if os.path.isfile(os.path.join(D, 'b679_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if r.get('run_id') != run_id] + [row]
    put_json('b679_runner_rows.json', dict(rows=rows))
    print(NL.join(L[:8] + L[-3:]))


def prints(*a):
    """`prints <run id>`: the 29 v0.32 names' printed lines at the run against b673's run at the v0.32 tree (relay data/b673_axioms_run38960681935.txt),
    name by name; data/b679_prints_compare.txt."""
    run_id = int(a[0])
    b, f = dict(_deps(rdn(K.V032_PRINTS))), dict(_deps(rdn('b679_axioms_run%d.txt' % run_id)))
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    rows = [(n, b[n], f.get(n)) for n in b]
    diff = [r for r in rows if r[1] != r[2]]
    L = ['b679 -- COMPONENT 3, N3: THE v0.32 DECLARATIONS` PRINTS BEFORE AND AFTER, NAME BY NAME (%s)' % utc(), '',
         '### before: relay data/%s (b673`s run 38960681935, the tree merged as e36ea31 = v0.32), %d names ; after: relay data/b679_axioms_run%d.txt' % (
             K.V032_PRINTS, len(b), run_id), '### rows are the v0.32 names: EQUAL or the two lines:']
    L += ['  %-62s %s' % (n, 'EQUAL' if x == y else 'DIFFER: %s | %s' % (x, y)) for n, x, y in rows]
    L += ['', '### ### **v0.32 NAMES %d ; PRINTED AFTER %d ; EQUAL %d ; DIFFERING %d.**' % (len(rows), sum(1 for r in rows if r[2]), len(rows) - len(diff), len(diff))]
    put_txt('b679_prints_compare.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 3: THE ζ-NAMING WALK ON S5' (b669's, carried)
ZETA_ID = re.compile(r'\b(?:riemannZeta\w*|completedRiemannZeta\w*|\w*riemannZeta\w*|zeta_\w+|\w+_riemannZeta\w*)\b')   # ### b564_record.py :454
DECL_RE = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(?:noncomputable\s+)?(theorem|def|abbrev|structure|instance|lemma)\s+([^\s(:{\[]+)', re.M)


def _strip_lean_comments(t):
    t = re.sub(r'/-[\s\S]*?-/', ' ', t)
    return NL.join(l.split('--', 1)[0] for l in t.split(NL))


def _decl_index(rev):
    """every declaration of the kernel's source trees (SIDEExplicitFormula/, Zeta23/) at `rev`: short name -> [(file, line, code)]."""
    import collections
    idx = collections.defaultdict(list)
    files = [f for f in g(K.KE, 'ls-tree', '-r', '--name-only', rev, '--', 'SIDEExplicitFormula', 'Zeta23').split(NL) if f.endswith('.lean')]
    for f in files:
        t = (_show(K.KE, rev, f) or '')
        heads = [(m.start(), m.group(2)) for m in DECL_RE.finditer(t)]
        for i, (pos, name) in enumerate(heads):
            end = heads[i + 1][0] if i + 1 < len(heads) else len(t)
            idx[name.split('.')[-1]].append((f, t[:pos].count(NL) + 1, _strip_lean_comments(t[pos:end])))
    return idx


def walk(*a):
    """(R289)(6), H3 and N4: S5' walked through the kernel's source at the branch tip, b669's text walk (tools/b669_record.py :559-:621):
    from li_nonneg_cfg_imp_online (its short name, so v0.32's namesake is reached too -- an over-reach, never an under-reach), every
    identifier of a reached declaration's comment-stripped code that names a kernel declaration by its last component followed transitively;
    each reached declaration read by b564's ζ pattern. The control: the walk from LiWeil.rh_imp_li_nonneg reaches ζ. data/b679_zeta_walk.txt."""
    rev = a[0]
    idx = _decl_index(rev)

    def _walk(root):
        seen, queue, order = {root}, [root], []
        while queue:
            n = queue.pop(0)
            for f, ln, code in idx.get(n, []):
                order.append((n, f, ln, sorted(set(ZETA_ID.findall(code)))))
                for tok in set(re.findall(r"[A-Za-z_][A-Za-z0-9_'.₀-₉]*", code)):
                    s = tok.split('.')[-1]
                    if s in idx and s not in seen:
                        seen.add(s)
                        queue.append(s)
        return order
    root = 'li_nonneg_cfg_imp_online'
    order = _walk(root)
    ctl = _walk('rh_imp_li_nonneg')
    ctl_z = [x for x in ctl if x[3]]
    zn = [x for x in order if x[3]]
    wide = [x for x in order if x[1].startswith('SIDEExplicitFormula/Schema/Wide/')]
    L = ['b679 -- COMPONENT 3, (R289)(6): THE ζ-NAMING WALK OF S5`, ON THE BRANCH (%s)' % utc(), '',
         '### rows are declarations, in the order the walk reaches them: from %s at %s (%s), every identifier of a reached declaration`s '
         'comment-stripped code that is a kernel declaration`s name (SIDEExplicitFormula/, Zeta23/; matched by its last component, so a '
         'shared short name over-reaches -- v0.32`s namesakes among them -- and never under-reaches) followed; each reached declaration read by '
         'b564`s ζ pattern %r.' % (root, rev, g(K.KE, 'rev-parse', '--short=7', rev).strip(), ZETA_ID.pattern), '']
    L += ['  %-48s %s:%d %s' % (n, f, ln, ('ζ-NAMING ' + ', '.join(z[:4])) if z else '') for n, f, ln, z in order]
    L += ['', '### THE CONTROL: the same walk from LiWeil.rh_imp_li_nonneg (ζ`s forward half) reaches %d declarations, ζ-naming %d -- %s.' % (
        len(ctl), len(ctl_z), ', '.join('%s %s:%d %s' % (n, f, ln, z[:2]) for n, f, ln, z in ctl_z[:4]) or '### NONE')]
    L += ['', '### ### **DECLARATIONS REACHED %d (IN Schema/Wide/ %d) ; ζ-NAMING %d%s ; THE CONTROL %d.**' % (
        len(order), len(wide), len(zn), (' -- ' + ', '.join(sorted(set(x[0] for x in zn)))) if zn else '', len(ctl_z))]
    tag = '' if rev.startswith('eb1e208') else '_' + g(K.KE, 'rev-parse', '--short=7', rev).strip()   # ### the first tree state's bank kept as written
    put_txt('b679_zeta_walk%s.txt' % tag, L)
    put_json('b679_zeta_walk%s.json' % tag, dict(at=utc(), rev=rev, root=root, reached=len(order), zeta=[dict(name=n, file=f, line=ln, ids=z) for n, f, ln, z in zn],
                                         order=[[n, f, ln] for n, f, ln, _z in order]))
    print(L[-1])


def landing(*a):
    """`landing <run id> <rev>`: (R289)(6): each declaration of the three Wide files with its landing (the run's gate per terminal), its file
    and line at <rev>, and its printed axioms; the controls with (H6) and (H6b); the split rule's reading. data/b679_landing.txt (.json)."""
    run_id, rev = int(a[0]), a[1]
    row = [r for r in jl('b679_runner_rows.json').get('rows', []) if r.get('run_id') == run_id]
    if not row or not row[0].get('artifact_sha256'):
        sys.exit('### THE RUN %d IS NOT READ WITH AN AGREEING ARTIFACT -- NOTHING WRITTEN' % run_id)
    row = row[0]
    deps = dict(_deps(rdn('b679_axioms_run%d.txt' % run_id)))
    gate = dict((n, gv) for n, gv in row['gate_rows'])
    where = {}
    for f in K.WIDE_FILES:
        for i, l in enumerate((_show(K.KE, rev, f) or '').split(NL), 1):
            m = re.match(r'^(?:theorem|def|structure)\s+(\S+)', l)
            if m:
                where['SIDEExplicitFormula.Schema.' + ('' if m.group(1) == 'WideConfig' else 'Wide.') + m.group(1)] = '%s:%d' % (f, i)
    names = [n for n in deps if '.Schema.Wide.' in n]
    sorry = [f for f in K.WIDE_FILES if re.search(r'\bsorry\b', _strip_lean_comments(_show(K.KE, rev, f) or ''))]
    L = ['b679 -- COMPONENT 3, (R289)(6): EACH DECLARATION LANDED ON ITS OWN READING (%s)' % utc(), '',
         '### rows are declarations: the name, its landing, its file and line at %s (strip-variant-b679), its printed axioms, and where open the' % rev[:7],
         '### obstruction by file and line. The run: %d (relay data/b679_runner_run%d.txt), artifact sha256 %s AGREE; the gate DERIVES at the' % (
             run_id, run_id, row['artifact_sha256'][:16]),
         '### standard three [propext, Classical.choice, Quot.sound] or within them, no sorryAx. The structure WideConfig itself carries no print',
         '### (a structure, not a terminal); its fields are read by every row.', '']
    for n in names:
        L.append('  %-58s %-12s %-50s %s' % (n, gate.get(n, '### UNREAD'), where.get(n, '### NOT FOUND AT THE REV'), deps[n].replace('depends on axioms: ', '')))
    nd = sum(1 for n in names if gate.get(n) == 'DERIVES')
    L += ['', '### THE CONTROLS: (H6) Wide.c2_not_excl %s -- C2 (-1/4, 5/4) fails HExcl, so S5` does not apply to it; (H6b) Wide.c2b_nonneg_offline %s '
          '-- C2b (0, 1): every coefficient nonnegative with 1 off the line, the exclusion`s half at 0 necessary.' % (
              gate.get('SIDEExplicitFormula.Schema.Wide.c2_not_excl'), gate.get('SIDEExplicitFormula.Schema.Wide.c2b_nonneg_offline')),
          '### THE v0.32 DECLARATIONS: relay data/b679_prints_compare.txt (the 29 names` prints against b673`s run 38960681935).',
          '### `sorry` in the three files at %s (comments stripped): %s.' % (rev[:7], sorry or 'NONE'),
          '### THE SPLIT RULE ((R279)(4), relay data/b669_ferry.txt :11): %s' % (
              'every declaration DERIVES, so the branch merges whole and no declaration is left open.' if nd == len(names) else
              '### OPEN DECLARATIONS STAY ON THE BRANCH: ' + ', '.join(n for n in names if gate.get(n) != 'DERIVES')),
          '', '### ### **DECLARATIONS %d ; DERIVES %d ; OPEN %d ; SORRY IN THE FILES %d.**' % (len(names), nd, len(names) - nd, len(sorry))]
    put_txt('b679_landing.txt', L)
    put_json('b679_landing.json', dict(at=utc(), run_id=run_id, rev=rev, rows=[dict(name=n, landing=gate.get(n), where=where.get(n), axioms=deps[n])
                                                                           for n in names], sorry=sorry))
    print(L[-1])


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'c1order': c1order, 'runner': runner, 'prints': prints, 'walk': walk,
          'landing': landing}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b679_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
