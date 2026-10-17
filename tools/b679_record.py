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


# ================================================================================ THE ANSWERS BANK (b678's route, carried)
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
    """data/b679_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
    every word of the author delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim."""
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
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((ln, c['id'], c['input'], o.get('timestamp')))
                ask.add(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask:
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
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b679 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b679_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b679_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE LATE ROUTES (b678's, carried; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def read_runner_row(r):
    """a row of data/b679_runner_rows.json: a run id (int), a 40-hex ref, a gate (DERIVES or NOT DERIVES); returns (run id, gate)."""
    if not isinstance(r, dict) or not isinstance(r.get('run_id'), int) or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') \
            or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (str(r)[:120],))
    return r['run_id'], r['gate']


ORDER_ROW = re.compile(r'^  (W-ORD-[A-Z0-9-]+)\s+:(\d+)\s+(b\d+)\s+(\d+)\s+(OPEN|DISCHARGED|ACTED|NOT STATED|CLOSED)\s+:(\d+)\s+(.+?) \[:(\d+)\]$')


def read_order_row(line):
    """a row of data/b670_work_orders.txt: the order, its entry line, its act, its age, its Status, its status line and its trigger or pin;
    returns (order, status, trigger)."""
    m = ORDER_ROW.match(line or '')
    if not m:
        raise ValueError('order row of another shape: %r' % ((line or '')[:120],))
    return m.group(1), m.group(5), m.group(7)


LANDING_ROW = re.compile(r'^  (SIDEExplicitFormula\.Schema\.Wide\.\S+)\s+(DERIVES|NOT DERIVES\S*)\s+(SIDEExplicitFormula/Schema/Wide/\S+\.lean:\d+)\s+\[')


def read_landing_row(line):
    """a row of data/b679_landing.txt: the declaration, its landing, its file and line; returns (name, landing)."""
    m = LANDING_ROW.match(line or '')
    if not m:
        raise ValueError('landing row of another shape: %r' % ((line or '')[:120],))
    return m.group(1), m.group(2)


READERS += ['read_runner_row', 'read_order_row', 'read_landing_row']


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


MOVE_OR_DELETE = re.compile(r'\bgit\s+(-C\s+\S+\s+)?(mv|rm)\b|\bgit\s+(-C\s+\S+\s+)?branch\s+-[dD]\b|--delete\b|(^|[;&|]\s*|\s)rm\s+-|Remove'
                            + r'-Item|\bos\.remove\b')


def delete_shape(cmd):
    """(R289)(8): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    return names, [ch for ch in '*?[' if ch in c]


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    mv = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'(^|&&\s*|;\s*)gh workflow run\b', QUOTED.sub('""', r['cmd']), re.M)]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    L = ['b679 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DISPATCHES AND THE MOVES AND DELETES (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES, ONE PER TREE STATE (%d):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R289)(8): one branch per command, no glob in any half): ' + '; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes)]
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; MOVE OR DELETE COMMANDS %d ; '
              'BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d.**' % (len(rows), len(hits), len(lean), len(disp), len(mv),
                                                                          sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl), len(shapes))]
    put_txt('b679_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b679_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], moves_deletes=[r['n'] for r in mv],
                                        delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle']


def kernels(*a):
    ks = [k for k in _kerns() if k != 'SIDE-explicit-formula']
    put_json('b679_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-explicit-formula, written by this act`s merge, read by N5 apart)' % len(ks))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b679_defects.txt').split(NL)
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
    t = rdn('b679_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b679_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b679_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b679_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def repairs(*a):
    """data/b679_tool_repairs.txt: rows are repairs with the defect they answer. Each tool carried from a sealed b678 copy is read against
    b678's seal hash (relay data/b678_seal_hashes.json) first, and its diff against that copy counted by hunks."""
    import hashlib
    seal = jl('b678_seal_hashes.json').get('tools') or {}
    rows = []
    for t8 in ('b678_citation.py', 'b678_closing.py', 'b678_reg_gate.py', 'b678_regspec.py', 'b678_tests.py', 'b678_worklist.py',
               'b678_record.py', 'b678_checks.py'):
        t9 = t8.replace('b678_', 'b679_')
        old, new = os.path.join(T, t8), os.path.join(T, t9)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
        rows.append((t8, t9, now, seal.get(t8), len(re.split(r'(?m)^(?=@@ )', d)[1:])))
    L = ['b679 -- COMPONENT 5, (R289)`S FERRY: THE CARRY-TIME READING OF THE TOOLS, AGAINST b678`S SEALED COPIES (%s)' % utc(), '',
         '### rows are the carried tools: b678`s sealed copy and its seal record; the hunks of the diff to b679`s copy. Every hunk is the act`s own',
         '### text -- its names, its banks, its sections and its predicates over this act`s banks -- save the repairs below, each with the defect',
         '### it answers.', '']
    for t8, t9, now, s, nh in rows:
        L.append('  %-20s -> %-20s b678 sealed %s ; the seal`s record %s ; %s ; hunks %d' % (t8, t9, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh))
    L += ['', '  REPAIR 1 -- THE BRANCH-DELETE SHAPE READS A REMOTE DELETE (answering (R289)(8)`s one remote deletion, which b678`s shape did not',
          '  read): tools/b679_record.py delete_shape counts `push origin --delete <name>` beside `branch -d <name>`, so N4 reads all nine deletes.',
          '  REPAIR 2 -- THE WALK`S BANKS NAMED BY REVISION (answering data/b679_defects.txt (e)): tools/b679_record.py walk writes a later tree',
          '  state`s walk under its revision, the first tree state`s bank kept as written.',
          '  REPAIR 3 -- THE WORD READER ADMITS A PREFIXED BEGIN (answering b679`s first answer, "(for the seat, verbatim):" and two CRs before',
          '  BEGIN, which b678`s reader did not bank as a word): tools/b679_record.py answers banks 3 words of 3 answers.',
          '', '### ### **REPAIRS 3 ; THE SEALED COPIES %s ; TOOLS CARRIED %d.**' % (
              'AGREE' if all(s == now for _a, _b, now, s, _n in rows) else '### DIFFER', len(rows))]
    put_txt('b679_tool_repairs.txt', L)
    print(NL.join(L[-(len(rows) + 10):]))


ROOT_EXCLUDE = re.compile(r'^b679_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands|'
                          r'mirror.*)\.(txt|json|md)$')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b679_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)]
                  + list(K.SHARED_APPENDED))


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if not b_.endswith('.gz') and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b679_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b679'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b679_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith('.gz')][0]
    with tempfile.TemporaryDirectory(prefix='b679_ra_') as tmp:
        cp_ = os.path.join(tmp, os.path.basename(bank_))
        b_ = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b_[0] ^= 0x01
        open(cp_, 'wb').write(bytes(b_))
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
    L = ['b679 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b679_root_arm.txt', L)
    put_json('b679_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b679 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b679_table_final.txt', L)
    put_json('b679_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b679_registration_2026-10-17.txt'
FACE = os.path.join(D, 'b679_registration_2026-10-17.txt')


def gatebanks(*a):
    """the gate's steps between the face and the lock (b665's order), each tool's output banked by this route, never by a shell redirect."""
    import gate_hash as G
    env = dict(os.environ, PYTHONIOENCODING='utf-8')

    def runb(args, out):
        r = subprocess.run([sys.executable] + args, capture_output=True, cwd=ROOT, env=env)
        b_ = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            open(p + '.tmp', 'wb').write(b_)
            os.replace(p + '.tmp', p)
        return r.returncode, b_.decode('utf-8', 'replace')
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b679_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b679_regspec.py')], 'b679_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b679_satisfiable.json', '--emit', 'b679'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b679_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b679_census_stepzero.txt'), ('b327_faces_census.py', 'b679_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b679_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b679'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b679_reg_gate.txt', 'data/b679_reg_termscan.txt', 'data/b679_regspec_run.txt', 'data/audit_b679_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES: (N1)-(N5) OF THE FERRY, THE SEAT'S (S1)-(S3)
import collections                 # noqa: E402
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b678_closing_push_out.txt', 'b670_work_orders.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')


def TRAIL_HEAD():
    return ('### b679 — lane two, act one hundred and six, the research act under (R289): the Li converse over the strip (−1/2, 3/2) with no '
            'real point in (−1/2, 0], v0.33; Q0 read against the widened class; the mirror resumed')


def _calls():
    return jl('b679_author_answers.json').get('calls') or []


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', *N5_PP)
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _verdict(name, needle):
    m = re.search(r'\*\*(.*' + re.escape(needle) + r'.*)\*\*', rdn(name))
    return m.group(1) if m else '### UNREAD'


def _n1():
    cm = jl('b679_commands.json')
    ok = bool(cm) and not cm.get('local_lean') and len(cm.get('dispatches') or []) == len(K.K_RUNS)
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b679_commands.txt, %d commands read); the builds on the hosted '
        'runner alone, dispatched %d times, one per tree state (runs %s)' % (cm.get('local_lean') if cm else '### UNREAD', len(cm.get('rows') or []),
                                                                              len(cm.get('dispatches') or []), ', '.join(str(r) for r, _t in K.K_RUNS)))


def _n2():
    plan = rdn('b679_strip_plan.txt')
    sec2 = plan[plan.find('== 2.'):plan.find('== 3.')]
    rows = re.findall(r'^    :(\d+) ', sec2, re.M)
    t_plan, t_lean = _git_ct(RELAY, K.PLAN_COMMIT), _git_ct(K.KE, K.K_RUNS[0][1])
    form = '== 0. THE FORM CHOSEN, WITH ITS REASON' in plan and 'A SECOND CONFIGURATION STRUCTURE' in plan
    beside = 'THE EXCLUSION\'S STATEMENT BESIDE IT: "∀ ρ ∈ Z.carrier, ρ.im = 0 → 0 < ρ.re"' in plan and 'LiConverseCfg.lean :231 "exact div_pos' in plan
    ok = form and beside and len(rows) == 22 and sorted(set(int(x) for x in rows)) == list(range(9, 31)) and t_plan and t_lean and t_plan < t_lean
    return ('HELD' if ok else 'REFUTED'), (
        'the plan (relay data/b679_strip_plan.txt, committed %s at %s) prints the form with its reason (== 0) %s and the exclusion`s statement beside '
        ':231 (== 1) %s before the first Lean write (the kernel commit %s at %s); the uses re-priced at == 2: %d rows, the bank`s rows :9-:30 each '
        'once %s' % (K.PLAN_COMMIT, time.strftime('%H:%M:%SZ', time.gmtime(t_plan)) if t_plan else '?', form, beside, K.K_RUNS[0][1][:7],
                     time.strftime('%H:%M:%SZ', time.gmtime(t_lean)) if t_lean else '?', len(rows),
                     sorted(set(int(x) for x in rows)) == list(range(9, 31))))


def _n3():
    rows = []
    for l in rdn('b679_landing.txt').split(NL):
        try:
            rows.append(read_landing_row(l))
        except ValueError:
            pass
    lj = jl('b679_landing.json')
    pc = _verdict('b679_prints_compare.txt', 'v0.32 NAMES')
    main_sorry = [f for f in K.WIDE_FILES if re.search(r'\bsorry\b', _strip_lean_comments(_show(K.KE, 'main', f) or ''))]
    ok = len(rows) == 20 and all(x[1] == 'DERIVES' for x in rows) and not lj.get('sorry') and not main_sorry and 'EQUAL 29 ; DIFFERING 0' in pc
    return ('HELD' if ok else 'REFUTED'), (
        'each declaration one landing banked with the runner`s gate reading: %d rows, DERIVES %d (relay data/b679_landing.txt, run %d); sorry in the '
        'three files on main %s; the v0.32 prints: %s (relay data/b679_prints_compare.txt)' % (
            len(rows), sum(1 for x in rows if x[1] == 'DERIVES'), K.K_RUNS[-1][0], main_sorry or 'NONE', pc))


def _n4():
    wv = _verdict('b679_zeta_walk_%s.txt' % K.K_TIP[:7], 'DECLARATIONS REACHED')
    mv = _verdict('b679_q0_membership.txt', 'HYPOTHESES READ')
    lj = dict((r['name'].split('.')[-1], r['landing']) for r in jl('b679_landing.json').get('rows') or [])
    cm = jl('b679_commands.json')
    shapes = [s for s in cm.get('delete_shapes') or [] if s['deletes']]
    named = [b for _r, bs in K.DELETE for b in bs] + [b for _r, b in K.DELETE_REMOTE]
    del_ok = bool(shapes) and all(len(s['deletes']) == 1 and not s['globs'] for s in shapes) and sorted(d for s in shapes for d in s['deletes']) == sorted(named)
    ok = 'ζ-NAMING 0 ' in wv and 'H4 HELD' in mv and lj.get('c2_not_excl') == 'DERIVES' and del_ok
    return ('HELD' if ok else 'REFUTED'), (
        'the walk where S5` lands: "%s" (relay data/b679_zeta_walk_%s.txt); Q0`s membership from the balls and the (3c) bound, each row with its '
        'source: "%s" (relay data/b679_q0_membership.txt); the planted control fails the exclusion: Wide.c2_not_excl %s; the step-zero deletes '
        '%d commands, one branch each and no glob %s, the branches %s against the ruling`s %s (relay data/b679_commands.txt)' % (
            wv, K.K_TIP[:7], mv[:220], lj.get('c2_not_excl'), len(shapes), del_ok, sorted(d for s in shapes for d in s['deletes']), sorted(named)))


def _n5():
    face = jl('b679_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    k_writes = [l for l in g(K.KE, 'log', '--first-parent', '--format=%h', '%s..main' % K.KREV).split(NL) if l.strip()]
    k_files = sorted(set(x for x in g(K.KE, 'diff', '--name-only', K.KREV, 'main').split(NL) if x.strip()))
    k_ok = k_files == sorted(K.K_FILES) and len(k_writes) == 1 and g(K.KE, 'rev-parse', '--short=7', K.K_NEXT_TAG + '^{commit}').strip() == K.K_MERGE
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b679_|audit_b679_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b679_checks as CH
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = others_ok and k_ok and not pp_beyond and not kinds_beyond and not differ and not new_arms and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); SIDE-explicit-formula`s main written by the one merge %s '
            '(first-parent commits since %s: %d), the files %s, the tag %s %s; every other kernel as the face read it %s; PLACE-papers beyond '
            'FINDINGS and OPEN_TRAILS (README and REGISTRY among them): %s; standing arms added: %s (the act`s arms over its own banks %d); sealed '
            'tools not agreeing %s; relay files of a kind beyond the act`s tools and banks, the table, the root list, b678`s push-out bank and the '
            'orders bank`s appended row: %s; "patent" in the lines written: %s; outbound requests: the seat`s git reads and pushes, its two '
            'dispatches and its run and artifact reads at github.com, so no identifier of the author placed in a request; the mirror zip outside '
            'every repository' % (K.DRAFT, K.K_MERGE, K.KREV, len(k_writes), k_files, K.K_NEXT_TAG, k_ok, others_ok, pp_beyond or 'NONE',
                                  new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', kinds_beyond or 'NONE', pat or 'NONE'))


def scores(*a):
    TF, RA = jl('b679_table_final.json'), jl('b679_root_arm.json')
    _r, _n, sh = seal_hashes()
    S = {
        'N1': _n1(), 'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:700]))
    if 'dry' in a:
        return
    put_json('b679_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _onset():
    j = jl('b679_onset.json')
    return j.get('n_star', '?'), j.get('on_sub', '?'), j.get('neg_on', '?')


def _title():
    ns, _o, _n = _onset()
    return ('## The Li converse over the strip (−1/2, 3/2) with no real point in (−1/2, 0]: V5\' DERIVES, the composition\' DERIVES, S5\' DERIVES, '
            '%s; Q0 inside the widened class on its certified balls and the (3c) bound, T-COUNT assumed; n*\' = %s against n_obs = 10034' % (K.K_NEXT_TAG, ns))


def _finding_text():
    S, J = jl('b679_scores.json'), jl('b679_act_root.json')
    ns, on_sub, neg_on = _onset()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b679_author_answers.txt'), re.M))
    c1 = _rl_lines('b679_record_lines.json') + ['?']
    co = _rl_lines('b679_record_lines_order.json') + ['?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    mv = jl('b679_q0_membership.json')
    nb = len(mv.get('balls') or [])
    e = ['', _title(), '',
         'The kernel’s Li converse now holds over a wider class than its zero configurations: a configuration in the open strip (−1/2, 3/2) whose '
         'real points have positive real part, under the local count, with every Li coefficient nonnegative, lies on the line '
         '(Wide.li_nonneg_cfg_imp_online, %s, DERIVES at the standard three, the ζ-naming walk from it at 0); every v0.32 declaration stands, its '
         'print unchanged. Q0 meets that class on its certified balls, the (3c) bound and its real segment, the local count assumed, so b675’s '
         'negative coefficient at n_obs = 10034, certified under that assumption, before the bound’s onset n*\' = %s, is a test of a kernel bound against a certified '
         'object and not a statement about Q0’s zeros. Nothing here proves RH or GRH.' % (K.K_NEXT_TAG, ns), '',
         '*Filed at b679 on the author’s ruling `(R289)`%s. Banks: relay `data/b679_strip_plan.txt`, `data/b679_landing.txt`, '
         '`data/b679_prints_compare.txt`, `data/b679_zeta_walk_%s.txt`, `data/b679_q0_membership.txt`, `data/b679_onset.txt`, '
         '`data/b679_act_root.txt`; the tools `tools/b679_q0_membership.py`, `tools/b679_onset.py`.*' % (
             (' and the navigator’s answers (%d questions)' % n_ans) if n_ans else '', K.K_TIP[:7]), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed -- the narrowed ball bank cited as .json, '
         'present as .json.gz, raised and answered (read with its hashes compared). b678 at its weight (FINDINGS :%s); '
         '`W-ORD-CORRESPONDENCE-RUNNER-BANKS` entered OPEN (OPEN_TRAILS :%s).' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', c1[0], co[0]), '',
         '**The statement** (`(R289)`(5)): a second structure, WideConfig, its strip field the open strip (−1/2, 3/2), the exclusion a named '
         'hypothesis HExcl beside it -- the type itself excludes Q0 at v0.32 (Zeta23/Defs.lean :142), and a parameter on it would change every '
         'v0.32 declaration over it. The 22 uses b676 listed re-priced: 2 unchanged in form, 3 by a constant, 17 by a new lemma, and LiConverseCfg.lean '
         ':231 closed by HExcl, the weakest pointwise premise there, since each real point of (−1/2, 0) is the dominant point of a two-point '
         'configuration. The split of the dominant set at w = 1, which would drop that half, entered as a later act’s candidate.', '',
         '**The attempt** (`(R289)`(6)): three new files on strip-variant-b679, two tree states, one dispatch each (runs %s); the first named its '
         'summability with ζ’s short name and the text walk followed it (22 ζ-naming), the second renamed it alone and the walk reads 0 of 278; '
         '49 of 49 terminals DERIVES, the 29 v0.32 prints equal; merged as %s, tag %s. The controls: C2, a point at the excluded 1/(1 − R), fails '
         'HExcl (Wide.c2_not_excl); C2b, the points 0 and 1, has every coefficient nonnegative with 1 off the line (Wide.c2b_nonneg_offline), '
         'so the half at 0 is necessary.' % (' and '.join(str(r) for r, _t in K.K_RUNS), K.K_MERGE, K.K_NEXT_TAG), '',
         '**The readings** (`(R289)`(7)): HExcl at Q0 by the route the author named, checked: Z_Q positive on (1, 3/2], Λ_Q(s) = Λ_Q(1 − s) with '
         'Γ negative on (−1, 0), Z_Q(0) = −1, and %d balls on [−1/2, 0] each negative; the band count 0 beside it. n*\' = %s with the widened '
         'constants (unchanged from v0.32’s), n_obs = 10034 below it; along V4’s subsequence in the window, %s n, NEG %s. The faces line drafted '
         'in the landing bank for the author’s word.' % (nb, ns, on_sub, neg_on), '',
         '**The root.** b679 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b675’s observation and b676’s strip-uses bank against the kernel’s '
         'own statement, and b667’s certification against the widened class; it is re-read by any act that applies the Li converse to an object '
         'outside the closed strip, and by the faces page where the author gives the word. It strengthens the programme’s offerings of a kernel '
         'statement whose class an object of the record meets, and of a certified computation read as a test of a compiled bound.', '',
         '**Carried to:** the split of the dominant set at w = 1 (the plan bank, == 11); the faces line, for the author’s word; T-COUNT for Q0, '
         'still assumed; the mirror resumed at this act and carried in the ferry form; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the form a second structure, by the type’s field and the v0.32 declarations a parameter would change (relay '
              'data/b679_strip_plan.txt == 0); (2) the summability renamed apart from the short name of ζ’s summability, a second tree state, so the '
              'carried walk reads the proof and not a namesake; (3) HExcl at Q0 read on [−1/2, −1/4] by the functional equation’s form, where the '
              'direct route’s Γ(s − ½) pole meets ζ(−2) = 0; (4) the root module’s import list not written, the build naming its modules by the target')


def _trail_text():
    S, J = jl('b679_scores.json'), jl('b679_act_root.json')
    fj = jl('b679_findings.json')
    ns, on_sub, neg_on = _onset()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b679_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b679_record_lines.json') + ['?']
    co = _rl_lines('b679_record_lines_order.json') + ['?']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R289) ratified.** (1) b678 at its weight. (2) The mirror resumed. (3) The Correspondence reader`s order. (4)-(7) The strip '
             'variant: the statement, the plan, the attempt, the landing. (8) The branches. (9) The read-first bank. (10) The draft held at v5. '
             '(11) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b678’s weight), :%s (the entry); OPEN_TRAILS.md:%s (`W-ORD-CORRESPONDENCE-RUNNER-BANKS`, OPEN, trigger '
             'the re-cut act after b680); this record.' % (c1[0], fj.get('entry_line'), co[0]), '',
             '**Act root:** b679 `%s` (previous `%s`, b678’s; relay data/act_roots.txt), computed after the last bank it names, every one of them '
             'LF.' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d call%s (relay data/b679_author_answers.txt); none after the root.' % (
                 n_ans, len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The kernel:** SIDE-explicit-formula main %s, tag %s; runs %s; 20 declarations DERIVES; walk 0 ζ-naming.' % (
                 K.K_MERGE, K.K_NEXT_TAG, ' and '.join(str(r) for r, _t in K.K_RUNS)), '',
             '**The readings:** Q0 in the widened class, T-COUNT assumed (relay data/b679_q0_membership.txt); n*\' %s, n_obs 10034; on V4’s '
             'subsequence %s n, NEG %s (relay data/b679_onset.txt).' % (ns, on_sub, neg_on), '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b679_closing.txt).', '',
             '**The open orders:** `W-ORD-EPSTEIN-BALL-WIDTH` (b681, the narrowing act); `W-ORD-MAP-ANGLE-FORM` (after it); '
             '`W-ORD-CORRESPONDENCE-RUNNER-BANKS` (the re-cut act after b680); `W-ORD-CHAIN-PAGE-B638-CASES`; `W-ORD-PRINT-TARGETS`; '
             '`W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; `W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; the ledger split at the '
             'b680 reading act.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b679_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b679_scores.json')
    L = ['=' * 104, 'b679 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b679_defects.txt').rstrip(NL).split(NL)
    put_txt('b679_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b679_scores.json', 'b679_findings.json', 'b679_trail.json', 'b679_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b679_record_lines.json') + ['?']
    co = _rl_lines('b679_record_lines_order.json') + ['?']
    L = ['b679 -- THE COMPONENTS, BANKED UNDER (R289).', '',
         '### COMPONENT 0 : the citation check (data/b679_citation_check.txt), step zero (data/b679_ferry.txt, data/b679_readfirst.txt, '
         'data/b679_stepzero.txt, data/b679_tests_stepzero.txt, data/b679_rowgen_stepzero.txt, data/b679_branches.txt) ; N4 %s' % S['N4'][0],
         '### COMPONENT 1 : b678`s weight FINDINGS :%s ; W-ORD-CORRESPONDENCE-RUNNER-BANKS OPEN_TRAILS :%s ; the mirror omission defect (a)' % (c1[0], co[0]),
         '### COMPONENT 2 : the plan (data/b679_strip_plan.txt), one prompt (data/b679_author_answers.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the attempt on strip-variant-b679, runs %s (data/b679_runner_run*.txt), the walk (data/b679_zeta_walk_%s.txt), the '
         'landing (data/b679_landing.txt) ; N1 %s ; N3 %s' % (', '.join(str(r) for r, _t in K.K_RUNS), K.K_TIP[:7], S['N1'][0], S['N3'][0]),
         '### COMPONENT 4 : the merge %s, tag %s (data/b679_merge_push_out.txt) ; Q0`s membership (data/b679_q0_membership.txt) ; the onset '
         '(data/b679_onset.txt)' % (K.K_MERGE, K.K_NEXT_TAG),
         '### COMPONENT 5 : the carry-time reading (data/b679_tool_repairs.txt), the dry-run steps (data/b679_reg_gate.txt), the seal '
         '(data/b679_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N5'][0])]
    put_txt('b679_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b679_findings.json', dict(title=t))
    j = jl('b679_findings.json')
    j['entry_line'] = ln
    put_json('b679_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b679_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written -- converted by conv and run through the screens their landing runs, the needles the face names read in
    each; prints DRY-RUN STEP : CLEAN and exits 0 only when both screens are quiet and every needle is found. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
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


# ================================================================================ THE MIRROR, AT THE CLOSE ((R289)(2); the b670 form, b674's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '2026-10-17-b679'
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
    put_json('b679_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b679':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b679`s -- NOTHING WRITTEN' % last[0])
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
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('b679_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b679_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b679_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b679 -- THE MIRROR-REFRESH EXPORT ((R289)(2)), BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b675 through b679 (the last export b674`s, D:/MY-DOwnloads/mirror-refresh-2026-10-17-b674.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b679_mirror.txt', L)
    put_json('b679_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'c1order': c1order, 'runner': runner, 'prints': prints, 'walk': walk,
          'mbuild': mbuild, 'mroot': mroot, 'mverify': mverify, 'mbank': mbank,
          'landing': landing, 'answers': answers, 'commands': commands, 'kernels': kernels, 'defects': defects, 'repairs': repairs,
          'root': root, 'root_arm': root_arm, 'table_final': table_final, 'gatebanks': gatebanks, 'scores': scores, 'desk': desk,
          'components': components, 'findings': findings, 'trail': trail, 'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b679_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
