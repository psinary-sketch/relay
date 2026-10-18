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


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, c4=c4, answers=answers)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b685_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
