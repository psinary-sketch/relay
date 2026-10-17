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


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'c1order': c1order}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b679_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
