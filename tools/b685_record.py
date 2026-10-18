# -*- coding: utf-8 -*-
"""b685_record.py -- THE ACT'S RECORD TOOL, b685 under (R295).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b685's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b684_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes --
### the branches route now reading remote rows and each cut branch's ancestry at its kernel's tag -- and the answers route); the later
### routes are added at their components. Every python child is started as `python -X utf8`, no environment mapping passed.
### Routes: `python tools/b685_record.py <route> [dry]`.
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
import b685_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank. Carried from b684_record.py with b685's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b685_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b685_findings.json': dict(entry_line=99999, title='stand-in'),
        'b685_trail.json': dict(line=99999),
        'b685_act_root.json': dict(root='0' * 64, previous='4c8935f8' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b685's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b685_scanfile_%s.md' % tag)
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
    """a row of data/b685_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
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
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b685_rowgen_<stage>.txt."""
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
    L = ['b685 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b685_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R295)(8))
def branches(*a):
    """every branch (R295)(8) names, its tip read before any delete, its fate; each cut branch's tip printed as an ancestor of its kernel's
    main at the new tag; any branch under the ruling's prefixes that --merged lists and the ruling does not name, reported and KEPT.
    data/b685_branches.txt (.json)."""
    rows, anc = [], []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    for repo, b, tag in K.DELETE_REMOTE:
        tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/remotes/origin/' + b).strip()
        merged = ('origin/' + b) in g(repo, 'branch', '-r', '--merged', 'main', '--list', 'origin/' + b)
        rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=merged, fate='DELETED'))
        tc = g(repo, 'rev-parse', tag + '^{commit}').strip()
        mn = g(repo, 'rev-parse', 'main').strip()
        a_ = grc(repo, 'merge-base', '--is-ancestor', tip, tc) == 0 if tip and tc else False
        anc.append(dict(repo=repo, branch=b, tip=tip, tag=tag, tag_commit=tc, main=mn, tag_at_main=tc == mn, ancestor=a_))
    named = set((r['repo'], r['branch']) for r in rows)
    extra = []
    for repo, _bs in K.DELETE:
        for x in g(repo, 'branch', '--merged', 'main', '--format=%(refname:short)').split(NL):
            x = x.strip()
            if x.startswith(K.PREFIXES) and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b685 -- STEP ZERO, (R295)(8): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; listed by `git branch [-r] --merged main --list <name>` ; fate.',
         '### Deleted by name in the house form, each delete command naming one branch with no glob in any half, one command per message, in',
         '### sequence; no branch the ruling does not name.']
    L += ['  %-28s %-34s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                               r['fate']) for r in rows]
    L += ['', '### each cut branch`s tip as an ancestor of its kernel`s main at the new tag (`git merge-base --is-ancestor <tip> <tag>`):']
    L += ['  %-28s %-34s tip %s ; tag %s at %s ; the tag at main %s ; ANCESTOR %s' % (os.path.basename(x['repo']), x['branch'], x['tip'][:12],
                                                                                     x['tag'], x['tag_commit'][:12], x['tag_at_main'], x['ancestor'])
          for x in anc]
    L += ['', '### branches under the prefixes %s that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join(K.PREFIXES), ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; CUT TIPS ANCESTORS OF THEIR TAGS %d OF %d ; TO BE DELETED %d ; UNNAMED '
          'UNDER THE PREFIXES %d.**' % (len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), sum(1 for x in anc if x['ancestor'] and x['tag_at_main']),
                                        len(anc), len(rows), len(extra))]
    put_txt('b685_branches.txt', L)
    put_json('b685_branches.json', dict(at=utc(), rows=rows, ancestry=anc, extra=[list(x) for x in extra]))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R295)(1)
WH = ('*Appended 2026-10-18 by b685 to b684’s entry (:9200), under `(R295)`(1) -- b684 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b684_closing.txt):*')
WB = (' “b684 closed: relay b6df52d7, PLACE-papers a2acff6; suite 107 of 107; root 4c8935f8f80c9eac…; 2 prompts answered; 5 defects” '
      '(data/b684_closing.txt :1), the closing pushed and read back at relay 4b97f382 (data/b684_closing_push_out.txt). The split rule row '
      'banked, “a suite PART over 450 s splits the next run”, beside b675 row 2 (data/b684_rules.txt row (1)); the suite in four parts, a '
      'part not starting beneath the 2,560 MB hold; `G-RULE-SUITE-PARTS` repaired at carry to read each act’s parts from the rules banks '
      '(data/b684_tool_repairs.txt). SIDE-class-number-anomaly cut 3 to 0, tagged v0.2.1; the residues applied on the author’s word with '
      'prints equal line for line -- SIDE-window v0.5.2, SIDE-trivium v0.1.2, SIDE-silence-principle v0.2.2 -- and R3b (the '
      'silence-principle introduction :7–:12) CARRIED for the next reading act’s census; three FOUNDATIONS cells naming '
      'SIDE-silence-principle v0.2.1 carried, not hand-written. N4 REFUTED -- four pre-push suite parts sent in one call, the call moved to '
      'the background past 598 s though no part passed 590 s, the sealed scorer reading HELD and corrected by the Edit tool with the '
      'scorer’s line quoted beside (data/b684_scores.json :16); N1–N3, N5, S1–S3 HELD. Five defects: (a) and (e) a reading sed typed, (b) '
      'the navigator’s phase rule cited for a part’s total, (c) the pre-push suite run twice for the N4 scorer’s bank, (d) the backgrounded '
      'call (data/b684_defects.txt). The mirror CLEAN. The rule rows banked at b685 (data/b685_rules.txt): one call per suite part, each its '
      'own message; and sed in no command, a reading one included. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b685_record_lines.json', 'c1', entry=K.B684_ENTRY,
         check=[('FINDINGS.md', K.B684_ENTRY, '## SIDE-class-number-anomaly re-cut'), ('OPEN_TRAILS.md', K.B684_TRAIL, '### b684')], dry=dry)


# ================================================================================ COMPONENT 4: THE LANDING, (R295)(7) AND THE NAVIGATOR'S ANSWER
ORDERS = 'b670_work_orders.txt'
ORDER_LINE, ORDER_ACT, ORDER_AGE = 14678, 'b680', 5
OH = ('*Appended 2026-10-18 by b685 beneath b684’s trail record (:14804), under `(R295)`(7) and the navigator’s answer on the landing -- '
      '`W-ORD-EPSTEIN-COUNT` (:14678) RE-DATED, P3 KEPT AS STATED:*')
OB = (' route (i) searched -- 10 candidates, 5 located, each bounding one L-function and none the sum Z_Q (relay data/b685_search.txt); route (ii) '
      'derived in Backlund’s form (relay data/b685_count_plan.txt, data/b685_count.txt): every condition of the plan’s steps (5)–(7) met at c = 1.7, '
      'r = 2.05, η = 0.2, the constants in balls a = 0.432571915432 ± 4.33e-41, b = 0, c = 1.26244217716 ± 1.26e-40 for T ≥ 149; the consistency '
      'reading and C2 as planned (data/b685_count_controls.txt). C1 on ζ by the same steps failed its second clause at T = 100, 1000, 10⁴ -- the '
      'derived bound (T ≥ 100) sharper than Hasanalizade-Shen-Wong Corollary 1.2 (T ≥ e) at each, which the author’s word reads as the signature '
      'of a dropped term -- so the act stopped before the composition: H4 NOT SCORABLE, H5 REFUTED as the word reads it; P3 kept “stated, not '
      'proved” (data/b685_p3_status.txt). The seat’s reading that no term was dropped stands in the controls bank as the seat’s. Trigger, three '
      'readings for a continuation act, none made in b685: (i) a matched-range comparison -- the ζ instance’s constants re-derived by the same '
      'steps on T ≥ e and compared at T = e, 10, 100 with Hasanalizade-Shen-Wong Corollary 1.2, Trudgian 2014 and Platt-Trudgian 2021, each '
      'located and quoted from its source, printed beside the T ≥ 100 comparison; (ii) a direct control on the Jensen step -- at T = 100, 1000 '
      'and 10⁴ the count of ζ zeros inside the Jensen disc (centre c = 1.7, radius r = 2.05) read from certified zeros against the bound step (6) '
      'assigns that disc, a disc holding more zeros than its bound refuting the step; (iii) the same for Z_Q at T = 50, 100, 149 from b681’s balls. '
      'Status OPEN.')
ORDER_ROW = re.compile(r'^  (W-ORD-[A-Z0-9-]+)\s+:(\d+)\s+(b\d+)\s+(\d+)\s+(OPEN|DISCHARGED|ACTED|NOT STATED|CLOSED)\s+:(\d+)\s+(.+?) \[:(\d+)\]$')


def read_order_row(line):
    """a row of the orders bank: order, entry line, act entered, age in acts, Status, the line of its last mark, the trigger or pin, and that
    line again; returns (order, Status, mark line)."""
    m = ORDER_ROW.match(line or '')
    if not m or m.group(6) != m.group(8):
        raise ValueError('order row of another shape: %r' % (line,))
    return m.group(1), m.group(5), int(m.group(6))


READERS.append('read_order_row')


def c4(*a):
    """(R295)(7) with the navigator's answer: the re-dating line on OPEN_TRAILS, then its row appended to the orders bank additively ((R254)(2))."""
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', OH, NL + OH + OB + NL)], 'b685_landing.json', 'c4',
         check=[('OPEN_TRAILS.md', ORDER_LINE, 'W-ORD-EPSTEIN-COUNT'), ('OPEN_TRAILS.md', K.B684_TRAIL, '### b684')], dry=dry)
    if dry:
        return
    ln = jl('b685_landing.json')['lines'][0]['line']
    rows = ['### Appended 2026-10-18 by b685 under (R295)(7) and the navigator`s answer on the landing (additive, (R254)(2)): W-ORD-EPSTEIN-COUNT '
            're-dated OPEN, P3 kept as stated; its Status cell filled and its line its mark.',
            '  %-44s :%d  %s   %-5d %-16s :%d  %s [:%d]' % ('W-ORD-EPSTEIN-COUNT', ORDER_LINE, ORDER_ACT, ORDER_AGE, 'OPEN', ln,
                                                            'readings (i)-(iii) of the line, for a continuation act', ln)]
    for r in rows[1:]:
        read_order_row(r)
    p = os.path.join(D, ORDERS)
    old = open(p, 'rb').read()
    sep = NL if old.endswith(b'\n') else NL + NL
    new = old + (sep + NL.join(rows) + NL).encode('utf-8')
    if not new.startswith(old):
        sys.exit('### THE ORDERS BANK APPEND IS NOT ADDITIVE -- NOTHING WRITTEN')
    open(p + '.tmp', 'wb').write(new)
    os.replace(p + '.tmp', p)
    print('  data/%s appended (%d bytes before, %d after)' % (ORDERS, len(old), len(new)))


# ================================================================================ THE ANSWERS BANK (b684's route, carried)
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
    """data/b685_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
    every word of the author delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim. Tool calls are
    read from the assistant lines alone (b683's trap: the api-request-blob lines carry copies of earlier calls)."""
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
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b685 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b685_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b685_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE LATE ROUTES (b684's, carried; every row read through READERS)
import collections                 # noqa: E402
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


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
    """(R295)(8): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    return names, [ch for ch in '*?[' if ch in c]


def outbound():
    """the act's outbound requests other than git: every WebSearch query and every subagent prompt from the ruling's line on, read from the
    assistant lines of the session transcript, with the author's identifiers searched in each."""
    out = []
    for i, o, _st, _sid in _session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') in ('WebSearch', 'Agent', 'WebFetch'):
                inp = c.get('input') or {}
                text = inp.get('query') or inp.get('prompt') or inp.get('url') or ''
                out.append(dict(line=i, tool=c['name'], ts=o.get('timestamp'), text=text))
    ident = ('psinary', 'hotmail', 'seale', 'york', 'orcid', '0009-0008')
    for r in out:
        r['identifiers'] = [w for w in ident if w in r['text'].lower()]
    return out


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    mv = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'(^|&&\s*|;\s*)gh workflow run\b', QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'Start-Process|\bnohup\b|run_in_background', r['cmd'])]
    seds = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'(^|[;&|(]\s*|\s)sed\s', QUOTED.sub('""', r['cmd']))]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    ob = outbound()
    L = ['b685 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (%d):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN (%d):' % len(detach)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R295)(8): one branch per command, no glob in any half): ' + '; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes)]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git (web searches, subagent prompts and fetches), each with the author`s identifiers found in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; '
              'MOVE OR DELETE COMMANDS %d ; BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), len(lean), len(disp), len(detach), len(seds), len(mv), sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl),
                  len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    put_txt('b685_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b685_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                        seds=[r['n'] for r in seds], moves_deletes=[r['n'] for r in mv],
                                        delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes], outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection', 'SIDE-class-number-anomaly']


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('b685_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (no kernel written in this act)' % len(ks))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b685_defects.txt').split(NL)
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
    t = rdn('b685_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b685_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b685_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b685_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


REPAIRS = [
    ('THE COUNT TOOL`S P5 WITHOUT THE COMPOSITION (answering the navigator`s answer on the landing, relay data/b685_author_answers.txt):',
     'tools/b685_count.py, written whole by the Write tool and run for P1, P2 and P4, was edited by the Edit tool before P5 so that P5 reads no',
     'part-3 bank where C1`s second clause stopped the act, scores H4 NOT SCORABLE, banks the composition section as NOT RUN and enters the',
     'seat`s reading of (Z1)`s π/4 as the seat`s in the controls bank; P1, P2 and P4 code unchanged by it.'),
    ('THE COUNT TOOL`S BANK WRITER`S FORMAT STRING (answering its own first P5 run, which stopped with a TypeError after the bottom edge and',
     'C2 were read and before any bank was written): one argument too many in the header line`s format; removed by the Edit tool, P5 re-run',
     'whole (the bottom edge read again, its ball equal).'),
    ('THE STANDING SET FOR b685 (answering no defect: the act`s objects): the standing arms are b684`s face`s (G2) arms less b684`s act arms,',
     'the twenty rule arms among them; the runner arms read the last merged runs, b684`s (this act dispatches none); the step-zero arms read',
     'this act`s banks -- eighteen branches with four remote rows, four processes named -- and the instruments arm takes in b684`s sealed tools,',
     'tools/rule_arms.py, b667`s route and b671`s segment route, which the count tool imports unedited.'),
]


def repairs(*a):
    """data/b685_tool_repairs.txt: rows are repairs with the defect they answer. Each tool carried from a sealed b684 copy is read against
    b684's seal hash (relay data/b684_seal_hashes.json) first, and its diff against that copy counted by hunks; tools/rule_arms.py read
    against b684's seal record (unedited in this act); the count tool's edits after its first runs shown as a diff against its first commit."""
    import hashlib
    seal = jl('b684_seal_hashes.json').get('tools') or {}
    rows = []
    for t0 in ('b684_citation.py', 'b684_closing.py', 'b684_reg_gate.py', 'b684_regspec.py', 'b684_tests.py', 'b684_worklist.py',
               'b684_record.py', 'b684_checks.py'):
        t1 = t0.replace('b684_', 'b685_')
        old, new = os.path.join(T, t0), os.path.join(T, t1)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
        rows.append((t0, t1, now, seal.get(t0), len(re.split(r'(?m)^(?=@@ )', d)[1:])))
    ra_now = hashlib.sha256(open(os.path.join(T, 'rule_arms.py'), 'rb').read()).hexdigest()
    first = (g(ROOT, 'log', '--diff-filter=A', '--format=%h', '--', 'tools/b685_count.py').split() or [''])[-1]
    cd = g(ROOT, 'diff', '--unified=1', first, 'HEAD', '--', 'tools/b685_count.py').replace(chr(13), '') if first else ''
    L = ['b685 -- COMPONENT 5, (R295)`S FERRY: THE CARRY-TIME READING OF THE TOOLS, AGAINST b684`S SEALED COPIES (%s)' % utc(), '',
         '### rows are the carried tools: b684`s sealed copy and its seal record; the hunks of the diff to b685`s copy. Every hunk is the act`s own',
         '### text -- its names, its banks, its sections and its predicates over this act`s banks -- save the repairs below, each with the defect',
         '### it answers.', '']
    for t0, t1, now, s, nh in rows:
        L.append('  %-20s -> %-20s b684 sealed %s ; the seal`s record %s ; %s ; hunks %d' % (t0, t1, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh))
    L.append('  %-20s    the standing instrument, unedited in this act: %s ; b684`s seal record %s ; %s' % (
        'rule_arms.py', ra_now[:16], (seal.get('rule_arms.py') or '### NONE')[:16], 'AGREE' if seal.get('rule_arms.py') == ra_now else '### DIFFER'))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### THE DIFF OF tools/b685_count.py SINCE ITS FIRST COMMIT (%s), WHOLE (repairs 1 and 2 are committed with the tool at 27de5eab; '
          'empty where the first commit carries them):' % first] + (['    ' + l for l in cd.rstrip(NL).split(NL)] if cd.strip() else ['    (no diff: the tool`s first '
                                                                                                                                   'commit carries both repairs)'])
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d.**' % (
        len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n in rows) and seal.get('rule_arms.py') == ra_now else '### DIFFER', len(rows))]
    put_txt('b685_tool_repairs.txt', L)
    print(L[-1])


def root_banks_state(banks, rev='HEAD'):
    """G-ROOT-BANKS-COMMITTED's reading (standing from (R291)(4)): for every bank the root names, its git status, whether HEAD carries it and
    whether HEAD's blob equals the working file; HEAD against the remote main (one ls-remote)."""
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


ROOT_EXCLUDE = re.compile(r'^b685_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*)\.?(txt|json|md|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b685_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['b685 -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % utc(), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('b685_root_banks.txt', L)
    put_json('b685_root_banks.json', dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b685_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b685'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b685_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='b685_ra_') as tmp:
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
    L = ['b685 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b685_root_arm.txt', L)
    put_json('b685_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b685 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b685_table_final.txt', L)
    put_json('b685_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b685_registration_2026-10-18.txt'
FACE = os.path.join(D, 'b685_registration_2026-10-18.txt')


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b685_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b685_regspec.py')], 'b685_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b685_satisfiable.json', '--emit', 'b685'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b685_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b685_census_stepzero.txt'), ('b327_faces_census.py', 'b685_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b685_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b685'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b685_reg_gate.txt', 'data/b685_reg_termscan.txt', 'data/b685_regspec_run.txt', 'data/audit_b685_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES: (N1)-(N5) OF THE FERRY, THE SEAT'S (S1)-(S3)
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b684_closing_push_out.txt', 'b670_work_orders.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
VL = re.compile(r'### ### \*\*(.*?)\*\*')
READFIRST_COMMIT = 'f89f961b'                      # ### the readfirst bank (HCount quoted, its inequality at Q0) committed before any search
PLAN_COMMITS = ('3dc1d4f5', 'e86ad1f3')            # ### the statement, search and plan banks, then the plan's restated step, before the word


def TRAIL_HEAD():
    return ('### b685 — lane two, act one hundred and twelve, the research act under (R295): the count law P3 at Q0 read, searched and derived in '
            'Backlund’s form, its constants in balls; C1 against ζ failing its second clause, the composition not run, P3 kept as stated')


def _calls():
    return jl('b685_author_answers.json').get('calls') or []


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', 'FINDINGS.md', 'OPEN_TRAILS.md')
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s[:19] + 'Z', '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def _n1():
    cm = jl('b685_commands.json')
    ok = bool(cm) and not cm.get('local_lean')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches %d (relay data/b685_commands.txt, %d commands read)' % (
            cm.get('local_lean') if cm else '### UNREAD', len(cm.get('dispatches') or []), len(cm.get('rows') or [])))


def _first_search():
    ob = jl('b685_commands.json').get('outbound') or []
    ts = [_iso(r['ts']) for r in ob if r.get('tool') in ('WebSearch', 'Agent') and r.get('ts')]
    return min([t for t in ts if t] or [None]) if ts else None


def _n2():
    t_rf, t_search = _git_ct(RELAY, READFIRST_COMMIT), _first_search()
    calls = _calls()
    t_word = _iso(calls[1]['result_ts']) if len(calls) > 1 and calls[1].get('result_ts') else None
    t_plan = [_git_ct(RELAY, c) for c in PLAN_COMMITS]
    t_p1 = _iso(jl('b685_count_part1.json').get('at') or '')
    rf = rdn('b685_readfirst.txt')
    plan = rdn('b685_count_plan.txt')
    quoted = 'def HCount (Z : Zeta23.ZeroConfig) (A₀ : ℝ) : Prop :=' in rf and 'N(t, t + 1) ≤ 10 log(|t| + 3) for every real t' in rf
    steps = [s for s in ('(1) THE ARGUMENT PRINCIPLE', '(2) THE MAIN TERM', '(3) THE RIGHT EDGE', '(4) THE BOTTOM EDGE', '(5) THE TOP EDGE',
                         '(6) THE JENSEN INTEGRAL', '(7) THE GROWTH BOUND', '(8) THE CONSTANTS', '(9) THE WINDOWS') if s in plan]
    sourced = all(x in plan for x in ('(S1)', '(Z1)', '(S3)', '(M3)')) and len(steps) == 9
    order = bool(t_rf and t_search and t_rf < t_search) and bool(t_word and all(t_plan) and all(t < t_word for t in t_plan)) and bool(t_p1 and t_word < t_p1)
    ok = quoted and sourced and order
    return ('HELD' if ok else 'REFUTED'), (
        'HCount quoted from the Lean (RestBound.lean :42-:45) and its inequality at Q0 written out in relay data/b685_readfirst.txt, committed at '
        '%s before the first search: %s (the statement bank itself written after the search began, defect (d)); every step of the plan sourced '
        'to a source read in this act, steps %d of 9 with their (S1), (Z1), (S3), (M3) cites: %s; the plan committed (%s) before the author`s '
        'word and the first constant (P1`s bank) after it: %s' % (READFIRST_COMMIT, bool(t_rf and t_search and t_rf < t_search), len(steps), sourced,
                                                                  ', '.join(PLAN_COMMITS), bool(t_word and all(t_plan) and all(t < t_word for t in t_plan)
                                                                                                and t_p1 and t_word < t_p1)))


def _n3():
    cj = jl('b685_count.json')
    ctl = rdn('b685_count_controls.txt')
    a_, c_ = cj.get('a') or ['', ''], cj.get('c') or ['', '']
    balls = bool(a_[1]) and bool(c_[1]) and bool((cj.get('C0') or ['', ''])[1])
    comp = cj.get('composition')
    read = '(C1) ζ by the same steps' in ctl and '(C2) planted' in ctl and 'C2 PASS' in ctl and 'C1 FAIL' in ctl
    if comp is None:
        return ('NOT SCORABLE', 'every constant a ball with its radius printed: %s (a %s ± %s, c %s ± %s); the composition`s narrowest margin and '
                'meeting height: NOT READ -- the composition not run, C1`s second clause failing and the author`s word stopping the act before it '
                '(relay data/b685_count.txt section 3); C1 and C2 read as planned: %s (relay data/b685_count_controls.txt)' % (
                    balls, a_[0][:14], a_[1], c_[0][:14], c_[1], read))
    return ('HELD' if balls and read else 'REFUTED'), 'the composition read (relay data/b685_count.txt section 3)'


def _n4():
    fj = jl('b685_findings.json')
    e = fj.get('entry_line')
    ls = rd(FIND).split(NL)
    head = ''
    if e:
        for l in ls[e:e + 6]:
            if l.strip():
                head = l
                break
    adds = _ledger_adds()
    bad = [m.group(0) for m in re.finditer(r'.{0,24}\b(proved|compiled)\b', adds) if not re.search(r'(not|nor|or) (proved|compiled)$', m.group(0))
           and not re.search(r'(not proved|stated, not proved)', m.group(0))]
    ok = bool(head) and 'is not derived in this act' in head and 'stated, not proved' in head and not bad
    return ('HELD' if ok else 'REFUTED'), (
        'the entry`s head line (FINDINGS :%s) states the premise`s status in the words of (R295)(7) as the navigator`s answer sets them: %s; '
        'sentences of the act`s ledger lines calling P3 proved or compiled: %s' % (
            (e + 2) if e else '?', bool(head) and 'is not derived in this act' in head and 'stated, not proved' in head, bad or 'NONE'))


def _n5():
    face = jl('b685_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b685_|audit_b685_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import importlib
    argv, sys.argv = sys.argv, sys.argv[:1]
    try:
        CH = importlib.import_module('b685_checks')
    finally:
        sys.argv = argv
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ob = jl('b685_commands.json').get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = k_ok and not pp_beyond and not kinds_beyond and not differ and not new_arms and not ident and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); no kernel main written, every kernel as the face read it %s; '
            'standing arms added: %s (the act`s arms over its own banks %d); sealed tools not agreeing %s; PLACE-papers beyond FINDINGS and '
            'OPEN_TRAILS: %s; relay files of a kind beyond the act`s banks and tools, the table, the root list, the orders bank and b684`s push-out '
            'bank: %s; "patent" in the lines written: %s; outbound requests: the seat`s git reads and pushes at github.com and %d web searches, '
            'subagent prompts and fetches (relay data/b685_commands.txt), an identifier of the author in %s' % (
                K.DRAFT, k_ok, new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE', pat or 'NONE',
                len(ob), [r['line'] for r in ident] or 'NONE'))


def scores(*a):
    TF, RA_ = jl('b685_table_final.json'), jl('b685_root_arm.json')
    _r, _n, sh = seal_hashes()
    S = {
        'N1': _n1(), 'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:700]))
    if 'dry' in a:
        return
    put_json('b685_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _title():
    return ('## The count law for Z_Q at D = −23: HCount at Q0 not derived, C1 against ζ failing its second clause and the composition not run; '
            'the Li-face test and the detection reading at Q0 re-read on P3 stated, not proved')


def _finding_text():
    S, J = jl('b685_scores.json'), jl('b685_act_root.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b685_author_answers.txt'), re.M))
    c1 = _rl_lines('b685_record_lines.json') + ['?']
    c4 = _rl_lines('b685_landing.json') + ['?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    e = ['', _title(), '',
         'P3 -- HCount at Q0, N(t, t + 1) ≤ 10 log(|t| + 3) for every real t over Q0’s zeros in the open strip (−1/2, 3/2) -- is not derived in this '
         'act and stays stated, not proved: the derivation in Backlund’s form ran with its constants in balls, but its ζ instance came out sharper than '
         'Hasanalizade, Shen and Wong’s Corollary 1.2 at T = 100, 1000 and 10⁴, which the author’s word reads as a failure of the derivation, so the act '
         'stopped before the composition. What would decide it are three readings for a continuation act: (i) the ζ instance re-derived on T ≥ e and '
         'compared at matched range with the located bounds; (ii) the Jensen step controlled directly against certified ζ zeros in its disc; (iii) the '
         'same for Z_Q from b681’s balls.', '',
         '*Filed at b685 on the author’s ruling `(R295)`%s. Banks: relay `data/b685_p3.txt`, `data/b685_search.txt`, `data/b685_count_plan.txt`, '
         '`data/b685_count.txt`, `data/b685_count_controls.txt`, `data/b685_p3_status.txt`, `data/b685_q0_reread.txt`, `data/b685_act_root.txt`.*' % (
             (' and the author’s and navigator’s answers (%d questions)' % n_ans) if n_ans else ''), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed -- a name, an hA row and a count field, each '
         'raised before the statement and entered as the navigator’s. b684 at its weight (FINDINGS :%s).' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', c1[0]), '',
         '**The statement** (`(R295)`(3)): HCount quoted from RestBound.lean :44 with Wide.HCount beside it, the inequality asked of Q0’s zeros in '
         'the open strip; the certified region covers −150 ≤ t ≤ 149, every window there holding at most 4 zeros against 10 log 3, the list’s '
         'own constant 0.878; the remainder t > 149 (relay data/b685_p3.txt).', '',
         '**The search** (`(R295)`(4)): ten candidates read at their sources -- Trudgian 2015, Bennett-Martin-O’Bryant-Rechnitzer 2021, '
         'Hasanalizade-Shen-Wong 2021, Grenié-Molteni, Zaman, Lee 2012 and 2018, Mukhopadhyay-Rajkumar-Srinivas, Bombieri-Hejhal -- five located, '
         'each bounding one L-function, none the sum Z_Q = (2/3)[ζ_K + L(s, χ) + L(s, χ̄)]; route (ii) stood (relay data/b685_search.txt).', '',
         '**The derivation** (`(R295)`(5)): Backlund’s form on Λ_Q’s half path, every step sourced and the plan raised before any constant; on the '
         'author’s word every condition met at c = 1.7, r = 2.05, η = 0.2, the constants a = 0.432572 ± 4.33e-41, b = 0, c = 1.262442 ± 1.26e-40 '
         'for T ≥ 149 and C₀ = 0.977462 ± 9.77e-41 (relay data/b685_count.txt).', '',
         '**The controls** (`(R295)`(6)): C1 on ζ by the same steps contains N(T) at T = 100, 1000 and 10⁴ and is sharper than Corollary 1.2 at '
         'each -- FAIL as the word reads it; C2’s planted constant moves N_Q(150)’s interval to [208.83, 216.29], away from the certified 180, '
         'its shift 32.985022 equal to the expected; the true interval [176.14, 183.00] holds 180 (relay data/b685_count_controls.txt).', '',
         '**The landing** (`(R295)`(7), the navigator’s answer): P3 kept stated, not proved (relay data/b685_p3_status.txt); the Q0 results of b675, '
         'b679 and b683 re-read with no status moved (relay data/b685_q0_reread.txt); `W-ORD-EPSTEIN-COUNT` re-dated OPEN at OPEN_TRAILS :%s with '
         'the three readings as its trigger.' % c4[0], '',
         '**The root.** b685 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b675’s, b679’s and b683’s Q0 results through the premise they share, '
         'and is re-read by the continuation act its readings name. It strengthens the programme’s offering of results at Q0 that name their '
         'premise and its status in the sentence that states them, with the derivation’s figures banked for the reading that would move it.', '',
         '**Carried to:** `W-ORD-EPSTEIN-COUNT` (readings (i)-(iii)); `W-ORD-EPSTEIN-COUNT-LEAN`, priced in the plan, not entered; the draft held '
         'at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the count field read as absent and Wide.HCount printed beside RestBound.lean :44, on the navigator’s answer; (2) the ζ-specific '
              'chain of (Z1)’s Theorem 1.3 read as ζ’s growth construction and not imposed at c ≥ 3/2, the conditions of (Z1) Propositions 3.1-3.2 '
              'and (S3) Proposition 5.4 imposed; (3) C1’s second clause compared as R + 7/8 against (Z1)’s bound on |N(T) − (T/2π) log(T/2πe)|; '
              '(4) the seat’s reading that no term was dropped entered as the seat’s; (5) G-RULE-HEAD-LINE-QUOTED declared failing, (R295)(1) '
              'not quoting b684’s head line')


def _trail_text():
    S, J = jl('b685_scores.json'), jl('b685_act_root.json')
    fj = jl('b685_findings.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b685_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b685_record_lines.json') + ['?']
    c4 = _rl_lines('b685_landing.json') + ['?']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R295) ratified.** (1) b684 at its weight. (2) The object. (3) The statement. (4) The search. (5) The derivation. (6) The composition '
             'and the controls. (7) The landing. (8) The branches. (9) The read-first bank. (10) The draft held at v5. (11) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b684’s weight), :%s (the entry); OPEN_TRAILS :%s (`W-ORD-EPSTEIN-COUNT` re-dated); this record.' % (
                 c1[0], fj.get('entry_line'), c4[0]), '',
             '**Act root:** b685 `%s` (previous `%s`, b684’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d call%s (relay data/b685_author_answers.txt); none after the root.' % (
                 n_ans, len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The count:** a = 0.432572, b = 0, c = 1.262442 for T ≥ 149, balls (relay data/b685_count.txt); C1 FAIL on its second clause, C2 '
             'PASS (relay data/b685_count_controls.txt); the composition not run.', '',
             '**The landing:** P3 kept stated, not proved (relay data/b685_p3_status.txt); `W-ORD-EPSTEIN-COUNT` OPEN, its trigger readings (i)-(iii).', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b685_closing.txt).', '',
             '**The open orders:** `W-ORD-EPSTEIN-COUNT` (readings (i)-(iii)); `W-ORD-LEDGER-SPLIT-RESOLVER` (on the author’s word); '
             '`W-ORD-CHAIN-PAGE-B638-CASES`; `W-ORD-PRINT-TARGETS`; `W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; '
             '`W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; `W-ORD-ROOT-BINARY-BANK`.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b685_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b685_scores.json')
    L = ['=' * 104, 'b685 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b685_defects.txt').rstrip(NL).split(NL)
    put_txt('b685_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b685_scores.json', 'b685_findings.json', 'b685_trail.json', 'b685_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b685_record_lines.json') + ['?']
    c4 = _rl_lines('b685_landing.json') + ['?']
    L = ['b685 -- THE COMPONENTS, BANKED UNDER (R295).', '',
         '### COMPONENT 0 : the citation check (data/b685_citation_check.txt), step zero (data/b685_ferry.txt, data/b685_readfirst.txt, '
         'data/b685_stepzero.txt, data/b685_tests_stepzero.txt, data/b685_rowgen_stepzero.txt, data/b685_branches.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b684`s weight FINDINGS :%s ; the two rule rows (data/b685_rules.txt)' % c1[0],
         '### COMPONENT 2 : the statement (data/b685_p3.txt), the search (data/b685_search.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the plan (data/b685_count_plan.txt at %s), raised as one prompt' % ', '.join(PLAN_COMMITS),
         '### COMPONENT 4 : the count (data/b685_count.txt), the controls (data/b685_count_controls.txt), the landing (data/b685_p3_status.txt, '
         'data/b685_q0_reread.txt, OPEN_TRAILS :%s) ; N3 %s ; N4 %s' % (c4[0], S['N3'][0], S['N4'][0]),
         '### COMPONENT 5 : the carry-time reading (data/b685_tool_repairs.txt), the dry-run steps (data/b685_reg_gate.txt), the seal '
         '(data/b685_seal_hashes.json), the suite in four parts ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N5'][0])]
    put_txt('b685_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b685_findings.json', dict(title=t))
    j = jl('b685_findings.json')
    j['entry_line'] = ln
    put_json('b685_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b685_trail.json', {})
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


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b684's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '2026-10-18-b685'
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
    put_json('b685_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b685':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b685`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b685_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b685_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b685_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b685 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b685 (the last export b684`s, D:/MY-DOwnloads/mirror-refresh-2026-10-18-b684.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b685_mirror.txt', L)
    put_json('b685_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, c4=c4, answers=answers, mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank,
              commands=commands, kernels=kernels, defects=defects, repairs=repairs,
              rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final, gatebanks=gatebanks, scores=scores,
              desk=desk, components=components, findings=findings, trail=trail, drycheck=drycheck)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b685_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
