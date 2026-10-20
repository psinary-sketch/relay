# -*- coding: utf-8 -*-
"""b694_record.py -- THE ACT'S RECORD TOOL, b694 under (R304).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b694's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b693_record.py in stages: the helpers, the guarded landing, the readers, step zero's rowgen and branches
### routes and the answers route first (stage one); Component 1's weight line and corrigendum at Component 1; the circuit and witness routes
### at Components 2-3; the late routes at Component 4. Every python child is started as `python -X utf8`, no environment mapping passed.
### Routes: `python tools/b694_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
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
import b694_worklist as K          # noqa: E402

SP = K.SP
STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)
RELAY = ROOT
ACT, PREV = 'b694', 'b693'


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
    none a number any bank carries; a stand-in run writes no bank (b693's, carried)."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b694_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b694_findings.json': dict(entry_line=99999, title='stand-in'),
        'b694_trail.json': dict(line=99999),
        'b694_act_root.json': dict(root='0' * 64, previous='eb2323dc' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b694's)
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


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R304)(1)
WH = ('*Appended 2026-10-20 by b694 to b693’s entry (:9506), under `(R304)`(1) -- b693 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b693_closing.txt):*')
WB = (' “b693 closed: relay a96d5c38, PLACE-papers dba03d2; suite 121 of 122; root eb2323dc6295a480…; 4 prompts answered; 8 defects” '
      '(data/b693_closing.txt :1), the closing 48ca2540 pushed and read back at relay main (data/b693_closing_push_out.txt :5). The host rebooted '
      'between relay 0574078e (Components 0-3 done) and 91c2df0c (the resume bank, data/b693_resume.txt, committed alone), entered as an event; '
      'the act resumed from the tree and the banks in a new session and ran Components 4-5 after it. The four mid-act answers carried out: '
      'b692’s weight line with both triage figures (FINDINGS :9498); the closing tool reading its defects range from the bank, “(a)–(m)” on '
      'b692’s (data/b693_range_exercise.txt); the chain split by act, standing-b2 over b624-b658 carrying no arm and standing-b3 over b659-b693 '
      'running G-ACTROOT-VERIFY once over both halves, the boundary b658 -> b659 equal in both, the whole-chain control 70 of 70 AGREE and the '
      'three verdicts equal (data/b693_chain_control.txt); push-b693-root pushed alone by push_gated’s branch mode and read back at 59de04e1, '
      'main pushed from it (data/b693_root_branch_push_out.txt :9, data/b693_root_push_out.txt). The re-cut: SIDE-archimedean, 2 rows outside '
      'LICENSED/CITED to 0, tag v0.1.1, prints equal, 3 quoting lines each a residue carried (data/b693_cut.txt :28). The suite 121 of 122 before '
      'and after the push, G-DELETES-ONE-BRANCH failing all act and declared on the face, each of step zero’s eight deletes chained with '
      '“; echo EXIT $?” (data/b693_checks.txt, data/b693_checks_postpush.txt; data/b693_defects.txt (f) :33). The closing’s push-b693-root row '
      'printed ABSENT (data/b693_closing.txt :226) where ls-remote showed the branch at 59de04e1: the sealed closing tool looked the remote up '
      'under D:\\relay while its reads were stored under D:/relay (data/b693_defects.txt (h) :47; the corrigendum beneath). A transient empty '
      'remote read of SIDE-fano-darkness at the post-push standing-a run’s opening read, read directly and alone, entered as an event, the part '
      're-run alone. Eight defects (a)-(h) (data/b693_defects.txt :7-:54): (a) the faces page the generator now lists differently, found at '
      'step zero; (b) the navigator’s, two misses of the ruling; (c) stream redirects at the resume; (d) listings through a shell filter; (e) a '
      'bank read through an interpreter’s print; (f) the chained deletes; (g) three first forms of the carried suite and record tool caught by '
      'their own pre-run and repaired before the seal; (h) the closing row. The root eb2323dc over 71 banks (data/act_roots.txt); the entry at '
      'FINDINGS :9506 and the trail at OPEN_TRAILS :15138 carrying the root; the sealed tools 15 of 15 at the close (data/b693_closing.txt :21); '
      'mirror-refresh-2026-10-19-b693.zip CLEAN with the root line (data/b693_closing.txt :43). Nothing deposited.')


OH1 = ('*Appended 2026-10-20 by b694 beneath b693’s trail record (:15138), under the author’s word on `(R304)` -- `W-ORD-WITNESS-TAIL-BALLS` '
       'ENTERED:*')
OB1 = (' the two tail bounds of the Weil-face witness at Q0 (relay data/b694_witness.txt; tools/b694_witness_terms.py) -- the archimedean tail '
       'beyond R = 4000 (`tail_bound`) and the zero-side tail beyond 151.59 (`zero_tail`) -- computed as arb balls in place of float bounds with '
       'a safety factor of 1.01; the witness’s narrowest margin, at a = 32, is 7.7752874967979 against a radius of 1.43e-18 that the archimedean '
       'tail bound fills, the float bounds some 18 orders beneath the margin (relay data/b694_witness.txt :15; data/b694_witness_controls.txt '
       ':30-:32). Trigger “before any faces-page row carrying the witness is regenerated”. Status OPEN.')
OH2 = '*Appended 2026-10-20 by b694 beneath the line above, under the author’s word on `(R304)` -- `W-ORD-B518-FLOAT` ENTERED:*'
OB2 = (' b518’s float figure for its two-property window at Q0 at a = 14.106736 -- Z 681.322615776695 (relay data/b518_cells.jsonl :119) against '
       'its bound B 5.34e-08 (data/b518_report.txt :125) -- off by 2.33e-6 from the ball at b518’s own γ₀ 16.290216, 681.32261344334 with '
       'radius 3.64e-17, the identity holding on that window over the certified zeros (relay data/b694_witness_controls.txt :24-:26); b518’s '
       'sign stands; the b518 bank unedited; its cause (the float archimedean term, the float zero list) to be read at the reading act. Trigger '
       '“the reading act b700”. Status OPEN.')


def orders(*a):
    """the author's word after Component 3 (data/b694_author_answers.txt, the seventh word): W-ORD-WITNESS-TAIL-BALLS and W-ORD-B518-FLOAT
    entered at OPEN_TRAILS through the guarded landing; data/b694_orders_lines.json."""
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', OH1, NL + OH1 + OB1 + NL), ('OPEN_TRAILS.md', OH2, NL + OH2 + OB2 + NL)], '%s_orders_lines.json' % ACT, 'order',
         check=[('OPEN_TRAILS.md', K.B693_TRAIL, '### b693')], dry=dry)


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B693_ENTRY,
         check=[('FINDINGS.md', K.B693_ENTRY, '## SIDE-archimedean re-cut: 2 rows outside LICENSED/CITED to 0, v0.1.1'),
                ('OPEN_TRAILS.md', K.B693_TRAIL, '### b693')], dry=dry)


# ================================================================================ THE READERS, ONE PER ROW SHAPE A ROUTE READS ((R263)(3))
BRANCH_FATES = ('DELETED', 'KEPT', 'RAISED')


def read_branch_row(r):
    """a row of data/b694_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


READERS = ['read_branch_row']


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b694_rowgen_<stage>.txt."""
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


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R304)(5))
def _remote_tip(repo, b):
    out = g(repo, 'ls-remote', 'origin', 'refs/heads/' + b)
    return out.split('\t')[0].strip() if '\t' in out else ''


def branches(*a):
    """every branch (R304)(5) names for step zero, its tip read before any delete, whether --merged lists it, its fate DELETED; the two remote
    branches read by one ls-remote each, in sequence; any branch of b693 that --merged lists and the ruling does not name, reported and KEPT.
    data/b694_branches.txt (.json)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    for repo, b in K.DELETE_REMOTE:
        tip = _remote_tip(repo, b)
        merged = bool(tip) and grc(repo, 'merge-base', '--is-ancestor', tip, 'main') == 0
        rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=merged, fate='DELETED'))
    named = set((r['repo'], r['branch']) for r in rows)
    extra = []
    for repo in sorted(set(r_ for r_, _bs in K.DELETE)):
        for x in g(repo, 'branch', '--merged', 'main', '--format=%(refname:short)').split(NL):
            x = x.strip()
            if (x.startswith('push-' + PREV) or x.endswith('-' + PREV)) and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R304)(5): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % (ACT, utc()), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; merged into main ; fate. The ten named deleted by name in the house',
         '### form after --merged lists each, each delete command naming one branch with no glob in any half, one command per message, in sequence,',
         '### nothing chained after any (data/b694_rules.txt row (1)).', '',
         '### THE TEN (R304)(5) NAMES:']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### branches of %s that --merged lists and the ruling does not name (reported and KEPT): %s' % (PREV, ', '.join(
        '%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **NAMED %d (MERGED %d) ; UNNAMED OF %s %d.**' % (len(rows), sum(1 for r in rows if r['merged']), PREV, len(extra))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[list(x) for x in extra]))
    print(NL.join(L[7:]))


# ================================================================================ THE ANSWERS BANK (b693's route, carried)
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
    """data/b694_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
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


# ================================================================================ COMPONENT 2: THE CLOSURE STEP ON THE RUNNER ((R304)(3); b692's routes, carried)
STD3 = ('propext', 'Classical.choice', 'Quot.sound')


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def dispatch(*a):
    """`dispatch <kernel> <ref sha> <label> <target> [dry]`: ONE dispatch of build-module.yml at main with the ref input and the lake target;
    refused where data/b694_dispatches.json already carries the ref's tree (one dispatch per tree state). The run id read from the run list
    (the newest workflow_dispatch run created after the dispatch); a row banked."""
    kernel, ref, label, target = a[0], a[1], a[2], a[3]
    repo = 'psinary-sketch/' + kernel
    full = g('D:/' + kernel, 'rev-parse', ref).strip()
    tree = g('D:/' + kernel, 'rev-parse', full + '^{tree}').strip()
    j = jl('%s_dispatches.json' % ACT)
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
    put_json('%s_dispatches.json' % ACT, dict(rows=rows))
    print('  dispatched %s ; run id %s' % (t0, run_id))


def runstatus(*a):
    """`runstatus <kernel> <run id>`: the run's status and conclusion, printed only (a foreground read, no wait)."""
    rc, out, err = _gh('run', 'view', a[1], '-R', 'psinary-sketch/' + a[0], '--json', 'status,conclusion,createdAt,updatedAt')
    print('  ' + (out.decode('utf-8', 'replace').strip() or err.strip()))


def _deps(ax):
    """the axioms output read per terminal: [(name, [axioms])], wrapped lists rejoined."""
    out = []
    for n, d in re.findall(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)",
                           re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax), re.M):
        out.append((n, [x.strip() for x in d.split('[', 1)[1].rstrip(']').split(',') if x.strip()] if d.startswith('depends') else []))
    return out


def _wf_list(kernel, ref):
    """the print list at the ref: print_targets.txt where it stands, else the workflow's own `#print axioms` lines (SIDE-lv-conservation's form)."""
    pt = subprocess.run(['git', '-C', 'D:/' + kernel, 'show', '%s:print_targets.txt' % ref], capture_output=True)
    if pt.returncode == 0:
        return [l.strip() for l in pt.stdout.decode('utf-8').split(NL) if l.strip()], 'print_targets.txt'
    wf = g('D:/' + kernel, 'show', '%s:.github/workflows/build-module.yml' % ref)
    return re.findall(r'^\s*#print axioms (\S+)\s*$', wf, re.M), '.github/workflows/build-module.yml`s #print axioms lines'


def read_runner_row(r):
    """a row of data/b694_runner_rows.json: the kernel, its label, the ref (40 hex), the run id and the gate; returns (kernel, label, gate)."""
    if not isinstance(r, dict) or not re.match(r'^SIDE-[\w-]+$', r.get('kernel') or '') or not re.match(r'^[\w-]+$', r.get('label') or '') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['kernel'], r['label'], r['gate']


READERS.append('read_runner_row')


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <tag> <note...>`: b692's route, carried: the run read by its id; the artifact listed, downloaded by
    its id into memory, its sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low;
    the axioms output banked whole, every name of the list matched to one printed line; the closure step's out/closure.jsonl.gz banked as
    data/b694_circuit_<kernel>_<tag>_<tip>.jsonl.gz beside its text hashes bank (data/b680_rules.txt row (1))."""
    import gzip
    import hashlib
    import io as _io
    import zipfile
    kernel, run_id, ref, label, tag, note = a[0], int(a[1]), a[2], a[3], a[4], ' '.join(a[5:])
    repo = 'psinary-sketch/' + kernel
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=kernel, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None, closure=None)
    L = ['%s -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (ACT, kernel, label.upper(), utc()), '',
         '### the dispatch: %s ; the ref input %s' % (note, ref),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt'))]
    T_, B_ = {}, {}
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
                    B_[n] = z.read(n)
                    if not n.endswith('.gz'):
                        T_[n] = B_[n].decode('utf-8', 'replace').replace(chr(13), '')
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
    tg, tg_src = _wf_list(kernel, ref)
    printed = [n for n, _d in deps]
    unmatched = [n for n in tg if n not in printed]
    outside = [(n, d) for n, d in deps if not set(d) <= set(STD3)]
    clog = T_.get('closure_log.txt', '').rstrip(NL)
    gzb = B_.get('closure.jsonl.gz')
    cl_rows, cl_head = 0, {}
    if gzb:
        txt = gzip.decompress(gzb).decode('utf-8')
        lines = [l for l in txt.split(NL) if l.strip()]
        cl_head = json.loads(lines[-1]) if lines and '"header"' in lines[-1] else {}
        cl_rows = len(lines) - (1 if cl_head else 0)
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d:' % (row['build_exit'], len(row['errors']))] + ['    ' + l for l in row['errors'][:40]] + [
          '### the log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + [
          '### the closure step: its log`s last lines:'] + ['    ' + l for l in clog.split(NL)[-8:]] + [
          '### the closure bank: %s' % (('out/closure.jsonl.gz %d bytes, sha256 %s ; records %d ; the header`s count %s ; programme modules %d' % (
              len(gzb), hashlib.sha256(gzb).hexdigest(), cl_rows, cl_head.get('records'), len(cl_head.get('modules') or []))) if gzb else '### NONE IN THE ARTIFACT'),
          '### the print step: the list (%s at the ref) %d names ; terminals printed %d ; every name printed once %s ; axiom-free %d ; '
          'sorryAx %d ; outside the standard three %d' % (
              tg_src, len(tg), len(deps), not unmatched and len(printed) == len(set(printed)) == len(tg), sum(1 for _n, d in deps if not d),
              sum(1 for _n, d in deps if 'sorryAx' in d), len(outside)),
          '### rows are terminals: name | the axioms printed | within the standard three:']
    L += ['  %-62s %s %s' % (n, d, 'STD3' if set(d) <= set(STD3) else '### OUTSIDE') for n, d in deps]
    L += ['  %-62s ### NOT PRINTED' % n for n in unmatched]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not unmatched and not outside
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    if gzb and row['artifact_sha256']:
        stem = '%s_circuit_%s_%s_%s' % (ACT, kernel, tag, ref[:7])
        p = os.path.join(D, stem + '.jsonl.gz')
        with open(p + '.tmp', 'wb') as fh:
            fh.write(gzb)
        os.replace(p + '.tmp', p)
        row['closure'] = dict(bank=stem + '.jsonl.gz', sha256=hashlib.sha256(gzb).hexdigest(), bytes=len(gzb), records=cl_rows)
        put_txt(stem + '_hashes.txt', [
            '%s -- THE CLOSURE BANK`S HASHES, %s AT %s (the tip %s), BY THE RUNNER (%s)' % (ACT, kernel, tag, ref, utc()), '',
            '### rows are binary banks this text bank roots (data/b680_rules.txt row (1)): the bank | sha256 | bytes | the run | the artifact.',
            '  data/%s.jsonl.gz | %s | %d | run %d | artifact %s sha256 %s' % (stem, row['closure']['sha256'], len(gzb), run_id, art.get('id'),
                                                                            row['artifact_sha256']),
            '', '### ### **RECORDS %d ; THE HEADER`S COUNT %s ; PROGRAMME MODULES %d ; THE REF %s.**' % (
                cl_rows, cl_head.get('records'), len(cl_head.get('modules') or []), ref)])
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; '
          'OUTSIDE THE STANDARD THREE %d ; CLOSURE RECORDS %d ; GATE %s.**' % (
              run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']),
              len(deps), len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), cl_rows, row['gate'])]
    read_runner_row(row)
    put_txt('%s_runner_%s_%s.txt' % (ACT, kernel, label), L)
    if row['artifact_sha256']:
        put_txt('%s_axioms_%s_%s.txt' % (ACT, kernel, label), ax.split(NL) if ax else ['### EMPTY'])
        put_txt('%s_closurelog_%s_%s.txt' % (ACT, kernel, label), clog.split(NL) if clog else ['### EMPTY'])
    j = jl('%s_runner_rows.json' % ACT)
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('%s_runner_rows.json' % ACT, dict(rows=rows))
    print(NL.join(L[:14] + L[-3:]))


# ================================================================================ COMPONENT 2: THE READER, IMPORTED UNCHANGED ((R304)(3))
def _reader():
    """tools/circuit_read.py imported and unedited (N5: the carry-time repair the one edit to a shared tool): its kernel table extended at runtime
    by SIDE-lv-conservation's library, its two writers pointed at this act's names (its `read` names its banks b692_..., so a run as it stands
    would overwrite b692's root-named banks -- b693's readfirst lesson, data/b693_tool_repairs.txt row (1))."""
    import circuit_read as CR
    CR.LIBS.setdefault('SIDE-lv-conservation', (('SIDELvConservation', ''),))
    put0, out0 = CR.put, CR.output

    def put_(name, lines):
        if not name.startswith('b692_'):
            sys.exit('### THE READER ASKED TO WRITE %s -- NOTHING WRITTEN' % name)
        lines = list(lines)
        if lines and lines[0].startswith('b692 -- '):
            lines[0] = '%s -- %s [the reader imported unchanged by tools/b694_record.py, its banks named for %s]' % (ACT, lines[0][8:], ACT)
        put0(ACT + name[4:], lines)

    CR.put = put_
    CR.output = lambda stem, *r: out0(ACT + stem[4:], *r)
    return CR


def circuit(*a):
    """`circuit <bank> <kernel> <tag> <tip> <main>`: the reader's `read` (SERIES, TERMINALS, SHORTS, WIDTH, LOAD, OUTPUT) over a closure bank,
    its banks data/b694_circuit_<kernel>_<tag>.txt (.dot, .png, _png_hashes.txt)."""
    CR = _reader()
    CR.read(*a[:5])


def prints(*a):
    """the print list at main before and after, line for line: before -- run 38305820585 at c230e6d, whose tree 59109b72 is main 8e3bc76's, its
    eight terminals' profiles (relay data/b657_runner_SIDE-lv-conservation.txt :118-:125); after -- this act's run, data/b694_axioms_SIDE-lv-
    conservation_after.txt; the list itself, the workflow's #print axioms lines at 8e3bc76 and at d38f3e8. data/b694_prints_SIDE-lv-conservation.txt."""
    kernel = 'SIDE-lv-conservation'
    bl_ = rdn('b657_runner_SIDE-lv-conservation.txt').split(NL)
    before = []
    for l in bl_[117:125]:
        m = re.match(r"^  (\S+)\s+(\[[^\]]*\])", l)
        if m:
            before.append((m.group(1), sorted(x.strip(" '") for x in m.group(2).strip('[]').split(','))))
    after = dict((n, sorted(d)) for n, d in _deps(rdn('%s_axioms_%s_after.txt' % (ACT, kernel))))
    l0, l1 = _wf_list(kernel, '8e3bc76')[0], _wf_list(kernel, 'd38f3e8')[0]
    rows = [(n, b, after.get(n)) for n, b in before]
    eq = len(before) == 8 and all(b == f for _n, b, f in rows) and l0 == l1
    L = ['%s -- THE PRINTS OF %s AT MAIN BEFORE AND AFTER THE CLOSURE STEP, LINE FOR LINE (%s)' % (ACT, kernel, utc()), '',
         '### before: run 38305820585 at c230e6d (tree 59109b72a76b, main 8e3bc76`s tree; relay data/b657_runner_SIDE-lv-conservation.txt :118-:125) ;',
         '### after: run 39465780735 at d38f3e8 (relay data/b694_axioms_SIDE-lv-conservation_after.txt) ; the list (the workflow`s #print axioms lines) at',
         '### 8e3bc76 %d names, at d38f3e8 %d names, equal %s. Rows are terminals: name | before | after | equal.' % (len(l0), len(l1), l0 == l1), '']
    L += ['  %-62s | %s | %s | %s' % (n, b, f, 'EQUAL' if b == f else '### DIFFER') for n, b, f in rows]
    L += ['', '### ### **BEFORE %d TERMINALS ; EACH PRINTED AFTER %s ; THE LIST EQUAL %s ; EQUAL LINE FOR LINE %s.**' % (
        len(before), all(f is not None for _n, _b, f in rows), l0 == l1, eq)]
    put_txt('%s_prints_%s.txt' % (ACT, kernel), L)
    print(NL.join(L[6:]))


def readings(*a):
    """(R304)(3): the readings the author asked for after b692, printed again from the banks -- CLAUSE-DOMINANCE, WIDTH's pairs by name, LOAD's
    three highest -- for each faces kernel, each line cited by bank and line. data/b694_circuit_readings.txt."""
    def lines_of(name):
        return rdn(name).split(NL)

    def cite(name, pred):
        return [(i, l) for i, l in enumerate(lines_of(name), 1) if pred(l)]

    ef, lv = 'b692_circuit_SIDE-explicit-formula_v0.34.1.txt', 'b694_circuit_SIDE-lv-conservation_v0.13.0.txt'
    L = ['%s -- THE THREE READINGS PRINTED AGAIN FROM THE BANKS, (R304)(3) (%s)' % (ACT, utc()), '',
         '### rows are readings per faces kernel, each line read from its bank and cited by line; nothing recomputed here.', '']
    dm = cite('%s_circuit_dominance.txt' % ACT, lambda l: l.startswith('### ### **CLAUSE-DOMINANCE'))
    L += ['## CLAUSE-DOMINANCE   relay data/%s_circuit_dominance.txt :%d | %s' % (ACT, dm[0][0], dm[0][1].strip('# *'))]
    npairs = {}
    for kname, bank in (('SIDE-explicit-formula', ef), ('SIDE-lv-conservation', lv)):
        wl = lines_of(bank)
        h = [i for i, l in enumerate(wl) if l.startswith('## WIDTH -- theorem pairs')]
        pairs = []
        if h:
            for l in wl[h[0] + 2:]:
                if not l.strip():
                    break
                pairs.append(l.strip())
        ld = cite(bank, lambda l: l.startswith('### ### **RECORDS'))
        load3 = re.search(r'LOAD`S THREE HIGHEST (.+?)\.\*\*\s*$', ld[0][1]).group(1) if ld else '### NOT READ'
        L += ['', '## %s (relay data/%s)' % (kname, bank),
              '   WIDTH`s pairs at or under FEW = 5, by name (:%d-:%d), rows are pairs: meet | the one | the other:' % (h[0] + 3, h[0] + 2 + len(pairs))]
        npairs[kname] = len(pairs)
        L += ['     ' + p for p in pairs] or ['     NONE']
        L += ['   LOAD`s three highest (:%d): %s' % (ld[0][0], load3)]
    tm = cite(lv, lambda l: l.startswith('   PREMISE  liCriterion'))
    L += ['', '### the clause`s one meeting with SIDE-lv-conservation: no record of its compiled face in that kernel`s closure bank (the lakefile`s',
          '### federation line: no Lake dependency on a sister kernel), and among its main theorem`s TERMINALS the premise %s (relay data/%s :%d),' % (
              tm[0][1].split(':', 1)[0].replace('PREMISE', '').strip() if tm else '### NOT READ', lv, tm[0][0] if tm else 0),
          '### the open end the faces page`s correspondence row discharges on SIDE-explicit-formula`s side (relay data/b690_nodes_zeta.txt :126).']
    L += ['', '### ### **%s ; WIDTH AT FEW = 5: SIDE-explicit-formula %d PAIRS, SIDE-lv-conservation %d ; LOAD READ FOR BOTH.**' % (
        re.search(r'CLAUSE-DOMINANCE \d+ OF \d+', dm[0][1]).group(0), npairs['SIDE-explicit-formula'], npairs['SIDE-lv-conservation'])]
    put_txt('%s_circuit_readings.txt' % ACT, L)
    print(NL.join(L))


FACE = 'SIDEExplicitFormula.B321.h2_sign'
KERNEL_MAINS = (('SIDE-explicit-formula', 'b692_circuit_SIDE-explicit-formula_v0.34.1_4313875.jsonl.gz', 'SIDEExplicitFormula.B321.h2_sign_iff_rh',
                 'data/b690_nodes_zeta.txt :97 (the face h2_sign_iff_rh, a kernel row of :94-:164); b692`s closure bank'),
                ('SIDE-lv-conservation', None, 'residue_irreducible', 'data/b690_nodes_zeta.txt :126 (@corr SIDE-lv-conservation | residue_irreducible); '
                 'this act`s closure bank'))


def dominance(*a):
    """`dominance <lv bank>`: CLAUSE-DOMINANCE read whole over the faces kernels (data/b690_nodes_zeta.txt :94-:164, :126; the author`s answer
    at prompt 2): rows are faces kernels with the clause's compiled face named, the closure's reading HOLDS / ABSENT, the declaration through
    which it enters; the fraction printed. data/b694_circuit_dominance.txt."""
    CR = _reader()
    rows = []
    for kernel, bank, main, why in KERNEL_MAINS:
        bank = bank or a[0]
        recs, head = CR.load(bank)
        mains = [n for n in recs if n == main or n.endswith('.' + main)]
        if len(mains) != 1:
            sys.exit('### %s: THE MAIN THEOREM %s MATCHES %d RECORDS -- NOTHING WRITTEN' % (kernel, main, len(mains)))
        m = mains[0]
        cl = set(recs[m]['c'])
        holds = FACE in cl or FACE == m
        enters = ''
        if holds:
            direct = [x for x in recs[m]['c'] if x in recs and (x == FACE or FACE in recs[x]['c'])]
            enters = sorted(direct, key=lambda x: (x != FACE, len(recs[x]['c'])))[0] if direct else FACE
        face_rec = FACE in recs
        rows.append(dict(kernel=kernel, main=m, bank=bank, records=len(recs), holds=holds, enters=enters, face_a_record=face_rec,
                         closure=len(cl), why=why, modules=len(head.get('modules') or [])))
    n = sum(1 for r in rows if r['holds'])
    L = ['%s -- CLAUSE-DOMINANCE READ WHOLE, (R304)(3) AND THE AUTHOR`S ANSWER AT PROMPT 2 (%s)' % (ACT, utc()), '',
         '### the faces kernels: the kernels the faces page`s generator input names (relay data/b690_nodes_zeta.txt :94-:164, SIDE-explicit-formula`s',
         '### kernel rows; :126, SIDE-lv-conservation by its correspondence row); the clause`s compiled face %s (:95). Rows are faces kernels:' % FACE,
         '### the kernel | the face named | the main theorem | the closure`s reading HOLDS or ABSENT | the declaration through which it enters | the bank.', '']
    for r in rows:
        L.append('  %-24s | face %s | main %s | %s | %s | relay data/%s (records %d, programme modules %d, the main`s closure %d names ; the face a record '
                 'of the bank %s) | %s' % (r['kernel'], FACE, r['main'], 'HOLDS' if r['holds'] else 'ABSENT',
                                           ('enters through ' + r['enters']) if r['holds'] else 'enters through none',
                                           r['bank'], r['records'], r['modules'], r['closure'], r['face_a_record'], r['why']))
    L += ['', '### b692`s fraction re-read: %s (relay data/b692_circuit_dominance.txt :21).' % CR.rd(os.path.join(D, 'b692_circuit_dominance.txt')).strip().split(NL)[-1].strip('# *'),
          '', '### ### **CLAUSE-DOMINANCE %d OF %d FACES KERNELS (%s).**' % (n, len(rows), ' ; '.join('%s %s' % (r['kernel'], 'HOLDS' if r['holds'] else 'ABSENT')
                                                                                  for r in rows))]
    put_txt('%s_circuit_dominance.txt' % ACT, L)
    put_json('%s_circuit_dominance.json' % ACT, dict(at=utc(), rows=rows))
    print(NL.join(L[6:]))


# ================================================================================ THE CARRY-TIME REPAIRS BANK ((R304)(2))
def _fn_src(src, name):
    """a top-level def's source, from its `def` line to the next top-level statement."""
    L = src.split(NL)
    i = next((k for k, l in enumerate(L) if l.startswith('def %s(' % name)), None)
    if i is None:
        return []
    j = next((k for k in range(i + 1, len(L)) if L[k] and not L[k].startswith((' ', '#', ')'))), len(L))
    while j > i and not L[j - 1].strip():
        j -= 1
    return L[i:j]


REPAIR_FNS = ('repo_key', '_ls', 'read_remotes', 'remote_refs', 'remote_tag')


def repairs(*a):
    """data/b694_tool_repairs.txt: rows are repairs with the defect they answer; each diff beneath its row (difflib, unified, over the functions
    the repair touches, b693's sealed copy against this act's), and the row that printed ABSENT beside its repaired form."""
    import difflib
    import hashlib
    old, new = rd(os.path.join(T, 'b693_closing.py')), rd(os.path.join(T, 'b694_closing.py'))
    ob, nb = [hashlib.sha256(open(os.path.join(T, n), 'rb').read()).hexdigest()[:16] for n in ('b693_closing.py', 'b694_closing.py')]
    sealed = (jl('b693_seal_hashes.json').get('tools') or {}).get('b693_closing.py', '')
    o_lines, n_lines = [], []
    for f in REPAIR_FNS:
        o_lines += _fn_src(old, f) + ['']
        n_lines += _fn_src(new, f) + ['']
    o_row = [l for l in old.split(NL) if 'push-b693-root' in l and 'remote_refs' in l]
    n_row = [l for l in new.split(NL) if 'push-b693-root' in l and 'remote_refs' in l]
    diff = list(difflib.unified_diff(o_lines + o_row, n_lines + n_row, 'tools/b693_closing.py (the look-up, sealed %s)' % sealed[:16],
                                     'tools/b694_closing.py (the look-up, this act)', lineterm=''))
    lc = rdn('b694_lookup_control.txt')
    ctl = re.findall(r'(?m)^### ### \*\*(.*)\*\*$', lc)
    L = ['%s -- THE CARRY-TIME REPAIRS, UNDER (R304)(2) AND THE AUTHOR`S ANSWERS AT PROMPTS 1 AND 6 (%s)' % (ACT, utc()), '',
         '### rows are repairs with the defect they answer: the tool ; the blob before -> after ; what it answers ; the form ; the reading.',
         '### Each diff beneath its row, written by this route (difflib over the functions the repair touches).', '',
         '  (1) tools/b694_closing.py, carried from tools/b693_closing.py (sha256 %s, its seal %s; this act`s copy %s) -- ANSWERS b693 (h) (relay' % (
             ob, 'AGREE' if sealed[:16] == ob else '### DIFFER', nb),
         '      data/b693_defects.txt :47-:54): the sealed closing`s row asked the remote reads for D:\\relay (its ROOT, by os.path) where they were',
         '      stored under D:/relay, and printed push-b693-root ABSENT (data/b693_closing.txt :226). THE FORM (the author`s answer at prompt 1): one',
         '      key, repo_key(), \'D:/\' + the path below the drive, applied at the store (read_remotes) and at every look-up (remote_refs,',
         '      remote_tag), so D:\\relay, D:/relay and /d/relay (the push tool`s capture form) resolve to one key; the rest of the tool b693`s',
         '      form with b694`s act text. THE READING (data/b694_lookup_control.txt, the author`s answer at prompt 6): %s.' % (ctl[-1].rstrip('.') if ctl else '### NOT RUN'),
         '']
    L += ['      ' + l for l in diff]
    L += ['', '### ### **REPAIRS 1 ; THE CLOSING TOOL`S LOOK-UP UNDER ONE KEY ; THE SEALED b693 COPY %s ; DIFF LINES %d ; THE CONTROL AS WANTED %s.**' % (
        'AGREE' if sealed[:16] == ob else '### DIFFER', len(diff), 'THE CONTROL AS WANTED True' in lc)]
    put_txt('%s_tool_repairs.txt' % ACT, L)
    print(NL.join(L[-1:]))


# ================================================================================ THE DEFECTS BANK (b693's route and its row reader, carried)
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


# ================================================================================ THE CAPTURE AND THE COMMANDS (b693's, carried; ONE SESSION)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
# ### the previous act's window: b693's resume session, from the call that combined its post-push parts to that session's end (the author's /clear)
PREV_ACT, PREV_SESSION, PREV_ANCHOR = 'b693', '88ac42e2-47ac-48cb-ad82-03a97a19ab1e', 'RESUME b693 after a host reboot'


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


def prev_capture():
    """G-EDIT-ROUTE's window over the previous act: b693's resume session from the call that combined its post-push parts into
    data/b693_checks_postpush.txt to the session's end."""
    path = '%s/%s.jsonl' % (PROJ, PREV_SESSION)
    rows = ER.capture(path, PREV_ANCHOR, '%s/%s/subagents' % (PROJ, PREV_SESSION))
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV_ACT in r['cmd'] and '--combine' in r['cmd']]
    if not first:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE IS NOT IN ITS SESSION`S CAPTURE -- NOTHING READ')
    out = [dict(r, src='%s %s' % (PREV_ACT, r['src'])) for r in rows if first[0] <= r['ts']]
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
    """(R304)(5) and the ferry: a delete command names one branch and carries no glob and no variable in any half; b693's reader, carried."""
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
    disp = [r for r in sh_ if re.search(r'(^|&&\s*|;\s*)gh workflow run\b|b694_record\.py dispatch [^\s;]+ [^\s;]+ [^\s;]+ [^\s;]+\s*(?:;|$)',
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
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (b693, the session %s, from its post-push combine to the session`s end): %d '
              'commands from %s, its offences printed whole (%d):' % (PREV_SESSION[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
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
    L += ['', '### THE COMMANDS PIPING INTO A SHELL FILTER (head, tail, wc, grep and the like), read outside quoted strings -- this act`s defect (a) '
              'among them (%d):' % len(pipes)] + (['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in pipes] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT RUN AN INTERPRETER`S ONE-LINE PROGRAM (python -c), each its first line (%d):' % len(pyreads)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:220]) for r in pyreads] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R304)(5) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
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


# ================================================================================ THE LATE ROUTES (b693's, carried with b694's names)
def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection', 'SIDE-class-number-anomaly',
                                   'SIDE-spinor', 'SIDE-li-map', 'SIDE-rcurve', 'SIDE-archimedean']


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('%s_kernels_face.json' % ACT, dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-lv-conservation read after its closure commit d38f3e8, its push branch standing; none written after this read)' % len(ks))


def seal_hashes():
    import hashlib
    rec_ = (jl('%s_seal_hashes.json' % ACT).get('tools') or {}) if os.path.isfile(os.path.join(D, '%s_seal_hashes.json' % ACT)) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


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


ROOT_EXCLUDE = re.compile(r'^b694_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*|close_sentence|witness_units)\.?(txt|json|md|jsonl|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('%s_' % ACT) and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


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
         '### the source: data/b694_arm_seconds_<part>.json, written by tools/b694_checks.py at its pre-run, each arm`s seconds the sum of its',
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


# ================================================================================ THE SCORES: (N1)-(N5) OF (R304)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and commits and not the entry; the entry reads the scorer's bank. `scores`
# ### writes data/b694_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there and is read at the close.
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b693_closing_push_out.txt')


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


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', 'FINDINGS.md', 'OPEN_TRAILS.md')
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _files_of(repo, rev):
    return sorted(x for x in g(repo, 'show', '--name-only', '--pretty=format:', rev).split(NL) if x.strip())


def _vl(name):
    return ([x for x in rdn(name).split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]


def witness_units():
    """the witness's units as the committed binary bank carries them (relay data/b694_witness.json.gz, rooted through its text hashes bank)."""
    import gzip
    p = os.path.join(D, 'b694_witness.json.gz')
    if not os.path.isfile(p):
        return []
    return json.loads(gzip.decompress(open(p, 'rb').read()).decode('utf-8')).get('units') or []


def _n1():
    cm = jl('%s_commands.json' % ACT)
    rows = jl(K.RUNNER_ROWS).get('rows') or []
    arts = len(rows) == len(K.RUNNER_LABELS) and all(r.get('artifact_sha256') and r.get('gate') == 'DERIVES' for r in rows)
    hb = rdn(K.CLOSURE_BANK.replace('.jsonl.gz', '_hashes.txt'))
    clo = bool(rows) and rows[0].get('closure') and rows[0]['closure'].get('sha256', '') in hb and rows[0]['artifact_sha256'] in hb
    ok = bool(cm) and not cm.get('local_lean') and arts and clo
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b694_commands.txt, %d commands read); runner rows %d, the run read '
        'by its id with the artifact`s sha256 equal to the platform`s before any reading, DERIVES: %s; the closure bank`s hashes bank naming the '
        'gz`s sha256 and the artifact`s (relay data/%s): %s' % (cm.get('local_lean') if cm else 'unread', len(cm.get('rows') or []), len(rows), arts,
                                                                  K.CLOSURE_BANK.replace('.jsonl.gz', '_hashes.txt'), bool(clo)))


def _n2():
    U = witness_units()
    plan_t = _git_ct(ROOT, K.STEPZERO_BANKS)
    plan_in = 'data/b694_witness_plan.txt' in _files_of(ROOT, K.STEPZERO_BANKS)
    calls = jl('%s_author_answers.json' % ACT).get('calls') or []
    prompt_t = _iso_epoch(calls[0].get('ts')) if calls else None
    terms = [u for u in U if u.get('route') in ('zeta', 'q0', 'c2', 'rung')]
    first_term = min((_iso_epoch(u.get('at')) or 10 ** 12) for u in terms) if terms else None
    plan_ok = plan_in and bool(plan_t) and bool(prompt_t) and bool(first_term) and plan_t <= prompt_t <= first_term
    ck = dict(((u['fam'], u['a']), _iso_epoch(u.get('at'))) for u in U if u.get('route') == 'classk' and u.get('member'))
    ck_ok = bool(terms) and all((u['fam'], u['a']) in ck and ck[(u['fam'], u['a'])] <= (_iso_epoch(u.get('at')) or 0)
                                for u in terms if u.get('route') in ('zeta', 'q0'))
    return ('HELD' if plan_ok and ck_ok else 'REFUTED'), (
        'the plan committed (relay %s at %s, data/b694_witness_plan.txt among its files: %s) before the prompt raising it (the first call at %s) '
        'and before the first term (%s): %s; every width`s classK membership banked before its terms (%d term units, each with a member unit at '
        'or before it): %s' % (K.STEPZERO_BANKS, plan_t, plan_in, prompt_t, first_term, plan_ok, len(terms), ck_ok))


def _n3():
    pr = 'EQUAL LINE FOR LINE True' in _vl('%s_prints_SIDE-lv-conservation.txt' % ACT)
    diff = g('D:/' + K.LV, 'diff', '--name-only', K.LV_BEFORE, K.LV_CLOSURE, '--', 'SIDELvConservation', 'lakefile.lean', 'lean-toolchain',
             'lake-manifest.json', 'AxiomCheck.lean', 'AxiomCheck_pairing.lean', 'PinnedGoal.lean').strip()
    tags = g('D:/' + K.LV, 'tag', '--points-at', K.LV_CLOSURE).strip()
    v13 = g('D:/' + K.LV, 'rev-parse', '--short=7', 'v0.13.0^{commit}').strip()
    files = _files_of('D:/' + K.LV, K.LV_CLOSURE)
    ok = pr and diff == '' and tags == '' and v13 == K.LV_BEFORE and files == ['.github/workflows/build-module.yml', 'CircuitClosure.lean']
    return ('HELD' if ok else 'REFUTED'), (
        'the prints at main before and after equal line for line (relay data/b694_prints_SIDE-lv-conservation.txt): %s; git diff %s %s over the '
        'kernel`s source modules: %s; tags at %s: %s; v0.13.0 at %s; the closure commit`s files %s' % (
            pr, K.LV_BEFORE, K.LV_CLOSURE, diff or 'EMPTY', K.LV_CLOSURE, tags or 'NONE', v13, files))


def _n4():
    U = witness_units()
    z = [u for u in U if u.get('route') == 'zeta']
    q = [u for u in U if u.get('route') == 'q0']
    from decimal import Decimal
    zneg = [(u['fam'], u['a']) for u in z if not (Decimal(u['S'][0]) - Decimal(u['S'][1]) > 0)]
    zt = max((_iso_epoch(u.get('at')) or 0) for u in z) if z else None
    qt = min((_iso_epoch(u.get('at')) or 10 ** 12) for u in q) if q else None
    before = bool(z) and len(z) == 16 and not zneg and bool(qt) and zt <= qt
    wb = rdn('b694_witness.txt')
    sent = 'nothing' in wb and 'claimed of the kernel either way' in ' '.join(wb.split()) and re.search(r'margin 7\.7752874967979 \+- ', wb) is not None
    return ('HELD' if before and sent else 'REFUTED'), (
        'the zeta control at 16 widths, each ball wholly above 0 (none otherwise: %s), the last at %s before the first Q0 term at %s: %s; the '
        'witness reading a sentence about the computation with its margin as a ball and nothing claimed of the kernel (relay data/b694_witness.txt): '
        '%s' % (zneg or 'NONE', zt, qt, before, sent))


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


def _n5():
    import rule_arms as RA
    import b693_worklist as K693
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    t0, moved, tags = _kernels_moved()
    allowed = set((k, c[:7]) for k, cs in K.KERNEL_COMMITS.items() for c in cs)
    beyond_main = [m for m in moved if (m[0], m[1][:7]) not in allowed]
    tags_beyond = [t for t in tags if t not in K.KERNEL_TAGS]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b694_', x)]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b694_|audit_b694_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA) or x in K.SHARED_APPENDED)]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    arms_added = sorted(set(RA.NAMES) - set(K693.STANDING_ADDED) - set(_g2_of(os.path.join(D, 'b693_registration_2026-10-19.txt'))))
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock)) if lock else []
    ob = jl('%s_commands.json' % ACT).get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    wf_ident = [w for w in IDENT if w in g('D:/' + K.LV, 'show', 'main:.github/workflows/build-module.yml').lower()]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    chained = [d['n'] for d in (jl('%s_commands.json' % ACT).get('delete_shapes') or []) if d.get('chained')]
    ok = k_ok and not beyond_main and not tags_beyond and not pp_beyond and not kinds_beyond and not shared_tools and not differ and not arms_added \
        and not amended and not ident and not wf_ident and not pat and not chained
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; kernel main commits '
            'since the act began beyond the closure step`s one (%s): %s; tags made since the act began: %s; no standing arm added (tools/rule_arms.py`s '
            'names beyond b693`s face): %s; shared tools edited (the carry-time repair is the act`s closing tool): %s; sealed tools not agreeing: %s; '
            'commits amended after the seal: %s; deletes with anything chained after: %s; PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; relay '
            'files of a kind beyond the act`s banks and tools, the corrigenda and orders banks, the table, the root list and b693`s push-out bank: '
            '%s; "patent" in the lines written: %s; outbound requests other than git %d, an identifier of the author in %s; in SIDE-lv-conservation`s '
            'workflow file: %s' % (
                K.DRAFT, k_ok, K.LV_CLOSURE, beyond_main or 'NONE', tags_beyond or 'NONE', arms_added or 'NONE', shared_tools or 'NONE',
                differ or 'NONE', amended or 'NONE', chained or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE', pat or 'NONE', len(ob),
                [r['line'] for r in ident] or 'NONE', wf_ident or 'NONE'))


def _s_scores():
    import collections
    TF, RA_ = jl('%s_table_final.json' % ACT), jl('%s_root_arm.json' % ACT)
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b694_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b694_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def scores(*a):
    """`scores [dry]` writes data/b694_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b694_scores_close.json."""
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
    return ('### b694 — lane two, act one hundred and twenty-one, the research act under (R304): b693 at its weight; the closing tool`s look-up '
            'repaired; the deletes rule; the circuit reading completed over the carried faces kernel; the Weil-face witness at Q0')


def _calls():
    return jl('%s_author_answers.json' % ACT).get('calls') or []


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _figs():
    """the figures the title and the entry carry, each read from its bank by a needle that passes a dotted name and leaves a closing period."""
    wv = _vl('b694_witness.txt')
    fw = re.search(r'FOUND AT WIDTHS ([\d, ]+?) ; THE NARROWEST MARGIN AT a = (\d+), ([\d.]+) \+- ([\d.e+-]+?) ;', wv)
    wb = rdn('b694_witness.txt')
    top = re.search(r'^  N \| 192 .*? S (-[\d.]+) \+- ', wb, re.M)
    cv = _vl('b694_witness_controls.txt')
    c3 = re.search(r'C3 (\d+) OF (\d+) AGREE', cv)
    c1 = re.search(r'C1 (\d+) OF (\d+) NONNEGATIVE', cv)
    dm = re.search(r'CLAUSE-DOMINANCE (\d+) OF (\d+) FACES KERNELS', _vl('%s_circuit_dominance.txt' % ACT))
    cl = re.search(r'STOOD AT (\w+)', _vl('%s_corrigendum.txt' % ACT))
    i = lambda m, k: int(m.group(k)) if m else None   # noqa: E731
    return dict(widths=fw.group(1) if fw else '', narrow_a=fw.group(2) if fw else '', margin=fw.group(3) if fw else '', margin_rad=fw.group(4) if fw else '',
                widest=top.group(1) if top else '', c3=(i(c3, 1), i(c3, 2)), c1=(i(c1, 1), i(c1, 2)), dom=(i(dm, 1), i(dm, 2)),
                branch=cl.group(1) if cl else '')


def _title():
    f = _figs()
    a0 = f['widths'].split(',')[0].strip() if f['widths'] else ''
    a1 = f['widths'].split(',')[-1].strip() if f['widths'] else ''
    return ('## The Weil-face witness at Q0 on the notched window: P − PR + A negative beyond its bound at a = %s to %s, the narrowest margin %s at '
            'a = %s, the identity met at %s of %s cells, ζ nonnegative at every width, the centred family its counterpart; CLAUSE-DOMINANCE %s of %s; '
            'b693’s ABSENT row by corrigendum; the deletes rule' % (a0, a1, f['margin'], f['narrow_a'], f['c3'][0], f['c3'][1], f['dom'][0], f['dom'][1]))


def _finding_text():
    """the FINDINGS entry, composed before the root: its scores line from the scores bank alone (data/b686_rules.txt row (1)); the root is
    carried by the trail record."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'A window in classK gives the explicit-formula form of Z_Q, the Epstein zeta of Q0 = x² + xy + 6y², a value below zero beyond its bound. '
         'The off-line zero is b681’s ball OFF 0, ρ₀ = 0.95326… + 16.29021…i with half-width 1e-30; the window is b518’s notched B-spline window, '
         'h = (γ₀² + D²)(cos(γ₀u) φ) with γ₀ the ball’s centre and φ the order-6 B-spline on [−log a, log a], k = h ⋆ h̃. In balls at 128 bits, '
         'P − PR + A is negative beyond its bound at a = %s; the narrowest margin is %s with radius %s at a = %s, and the value at a = 192 is %s. '
         'It is positive at a = 14.106736, 16 and 24.' % (f['widths'], f['margin'], f['margin_rad'], f['narrow_a'], f['widest']), '',
         '*Filed at b694 on the author’s ruling `(R304)` and the author’s words at its prompts; %d questions put. Banks: relay '
         '`data/b694_witness_plan.txt`, `data/b694_witness_plan_amendment.txt`, `data/b694_witness_concentration.txt`, `data/b694_witness.txt`, '
         '`data/b694_witness_controls.txt`, `data/b694_witness_hashes.txt`, `data/b694_circuit_dominance.txt`, `data/b694_closure_step.txt`, '
         '`data/b694_circuit_readings.txt`, `data/b694_corrigendum.txt`, `data/b694_lookup_control.txt`, `data/b694_rules.txt`.*' % n_ans, '',
         '**The witness** (`(R304)`(4)): the plan was banked and raised before any term; on the author’s answer the family’s concentration was '
         'printed first, ĥ zero at γ₀ by the notch with its peaks beside it, and both families ran on one ladder of eight widths, the notched as '
         'the witness reading and the centred as its counterpart. Each width’s classK membership (even, C², compact support, the autocorrelation '
         'form) was printed before its terms. P is ĥ at ±i/2 squared and summed; PR runs over every n ≤ a² with Λ_Q from the Dirichlet inversion '
         'of r_Q/2; A is the kernel’s archimedean form with Z_Q’s own bracket, 2 Re ψ(1/2 + ir) − 2 log(2π/√23). The phase of ĥ(γ₀ − iδ)² is '
         '178.406 degrees for the notched family and 0 for the centred one, which is why only the notch turns the off-line pair negative.', '',
         '**The identity**: at every cell the zero side over the certified zeros below 151.59 -- b681’s 163 balls, the 17 partners, the band’s two '
         '-- agrees with P − PR + A within the tail beyond, %s of %s cells, ζ and Q0, both families and b518’s own window: the three terms are '
         'Z_Q’s and not ζ’s.' % f['c3'], '',
         '**The ζ control**: the identical windows at ζ read P − PR + A nonnegative beyond the bound at %s of %s cells, all of them read before any '
         'Q0 value was entered. **The centred family**, ĥ peaked at γ₀, reads positive at every width.' % f['c1'], '',
         '**The caveats**: the archimedean tail beyond r = 4000 and the zero-side tail beyond 151.59 are float bounds with a safety factor, not '
         'balls, some 18 orders beneath the margin (`W-ORD-WITNESS-TAIL-BALLS`); the Q0 zero-side tail rests on P3’s count, derived and not '
         'compiled; the 256-bit rung’s ball overlaps the 128-bit ball with midpoints agreeing to 9.1e-33, and the control’s wording -- inside -- '
         'cannot hold where both radii are the one tail bound. b518’s two-property family re-read at its own γ₀ is positive, as b518 read it, '
         'its float figure 2.33e-6 from the ball beyond its stated bound (`W-ORD-B518-FLOAT`). This is a sentence about a computation on a '
         'certified object without an Euler product: nothing is claimed of the kernel either way.', '',
         '**The circuit reading** (`(R304)`(3)): the faces kernel b692 carried, SIDE-lv-conservation, given the closure step -- the script and '
         'the step alone on main, one run read by its id, the artifact’s sha256 first, 608 records, the prints equal line for line, no source '
         'module and no tag touched. CLAUSE-DOMINANCE %s of %s faces kernels: SIDE-explicit-formula HOLDS, the face entering h2_sign_iff_rh '
         'directly; SIDE-lv-conservation ABSENT -- its lakefile requires Mathlib alone and forbids a sister dependence, so the clause’s compiled '
         'face is no constant of its environment, and the clause reaches it only through the faces page’s Correspondence row, which discharges '
         'its premise liCriterion on SIDE-explicit-formula’s side.' % f['dom'], '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed, each miss raised before the component that '
         'cites it; %d answers and words checked before they were acted on. b693 at its weight (FINDINGS :%s).' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, c1_[0]), '',
         '**The corrigendum and the repair** (`(R304)`(2)): b693’s closing row for push-b693-root, printed ABSENT where the branch stood at %s, '
         'corrected by one generated entry (FINDINGS :%d), the closing record unedited; the closing tool’s look-up repaired at carry time to one '
         'key at the store and every look-up, its control run over b693’s banked read-back. **The deletes rule**: a delete command stands alone '
         'in its message with nothing chained after it (relay data/b694_rules.txt row (1)), the ten branches of step zero deleted so.' % (
             f['branch'], K.CORRIGENDUM_LINE), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b518’s two-property window, b675’s Li-face bench, b681’s balls, '
         'b687’s band and b692’s circuit banks; it is re-read by b695, which raises the witness’s faces row, and by the reading act that takes '
         '`W-ORD-B518-FLOAT`. It strengthens the programme’s offering of a located clause by setting the Weil face beside the Li face at Q0: a '
         'certified object off the line on which the clause’s form reads negative, as the Li face’s coefficient did at b675.', '',
         '**Carried to:** b695 (the re-cut act; the witness’s faces row drafted in relay data/b694_faces_rows.txt); `W-ORD-WITNESS-TAIL-BALLS`; '
         '`W-ORD-B518-FLOAT` (b700); the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the window`s centre parameter read as the envelope`s centre with h^ zero at gamma_0, both families run on the author`s word; '
              '(2) C2 read at b518`s own gamma_0 16.290216 beside the plan`s centre; (3) the identity counted at every cell as the reading`s gate; '
              '(4) the reader imported with its writers pointed at this act`s names; (5) k(log n) at a knot sum compared in exact rationals of L; '
              '(6) the closing`s look-up control seeded from b693`s banked read-back')


def _trail_text():
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R304) ratified.** (1) b693 at its weight. (2) The repair and the deletes rule. (3) The circuit reading completed. (4) The Weil-face '
             'witness at Q0. (5) The branches. (6) The readfirst bank. (7) The draft held at v5. (8) The act after.', '',
             '**Entered:** FINDINGS.md:%s (b693’s weight), :%d (the corrigendum), :%s (the entry); OPEN_TRAILS :%d and :%d (the two orders); this '
             'record.' % (c1_[0], K.CORRIGENDUM_LINE, fj.get('entry_line'), K.ORDER_LINES[0], K.ORDER_LINES[1]), '',
             '**Act root:** b694 `%s` (previous `%s`, b693’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s (relay data/b694_author_answers.txt); none after the root.' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The kernels:** SIDE-lv-conservation -- the closure step d38f3e8 alone on main; run 39465780735 read by its run id; no tag.', '',
             '**The banks:** the witness relay data/b694_witness_plan.txt, data/b694_witness_plan_amendment.txt, data/b694_witness_concentration.txt, '
             'data/b694_witness.txt, data/b694_witness_controls.txt, data/b694_witness_hashes.txt (the .gz beside it); the circuit relay '
             'data/b694_closure_step.txt, data/b694_circuit_dominance.txt, data/b694_circuit_readings.txt; the repair relay data/b694_tool_repairs.txt, '
             'data/b694_lookup_control.txt; the corrigendum relay data/b694_corrigendum.txt; the rule relay data/b694_rules.txt.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b694_closing.txt).', '',
             '**The open orders:** `W-ORD-WITNESS-TAIL-BALLS` (before any faces-page row carrying the witness is regenerated); `W-ORD-B518-FLOAT` (the '
             'reading act b700); `W-ORD-EPSTEIN-COUNT-LEAN` and the regularity-uses bank (b696, on the author’s word).', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b694_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
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
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R304).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b694_citation_check.txt), step zero (data/b694_ferry.txt, data/b694_readfirst.txt, '
         'data/b694_stepzero.txt, data/b694_tests_stepzero.txt, data/b694_rowgen_stepzero.txt, data/b694_branches.txt, data/b694_rules.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b693`s weight FINDINGS :%s, the corrigendum :%d (data/b694_corrigendum.txt), the look-up repair and its control '
         '(data/b694_tool_repairs.txt, data/b694_lookup_control.txt)' % (c1_[0], K.CORRIGENDUM_LINE),
         '### COMPONENT 2 : the closure step (data/b694_closure_step.txt), CLAUSE-DOMINANCE (data/b694_circuit_dominance.txt), the readings '
         '(data/b694_circuit_readings.txt) ; N3 %s' % S['N3'][0],
         '### COMPONENT 3 : the witness (data/b694_witness_plan.txt, data/b694_witness.txt, data/b694_witness_controls.txt) ; N2 %s ; N4 %s' % (
             S['N2'][0], S['N4'][0]),
         '### COMPONENT 4 : the carry-time reading (data/b694_tool_repairs.txt), the dry-run steps (data/b694_reg_gate.txt), the seal '
         '(data/b694_seal_hashes.json), the suite in six parts, the per-part seconds (data/b694_arm_seconds.txt) ; S3 %s' % S['S3'][0],
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


FACE_REL = 'data/b694_registration_2026-10-20.txt'
FACE = os.path.join(D, 'b694_registration_2026-10-20.txt')


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


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b693's routes, carried)
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
         '### THE SPAN: every roster and ledger change of b694 (the last export b693`s, D:/MY-DOwnloads/mirror-refresh-2026-10-19-b693.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


def _g2_of(path):
    t = rd(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _standing():
    import b693_worklist as K693
    return sorted(set(_g2_of(os.path.join(D, 'b693_registration_2026-10-19.txt'))) - set(K693.ACT_ARMS))


def standing(*a):
    """the standing arms b694 carries: b693's face's (G2) arms less b693's act arms (R264)(2); printed only."""
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


ROUTES = dict(defects=defects, commands=commands, kernels=kernels, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              armsecs=armsecs, scores=scores, desk=desk, components=components, findings=findings, trail=trail, drycheck=drycheck,
              gatebanks=gatebanks, mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank,
              orders=orders, standing=standing, rowgen=rowgen, branches=branches, answers=answers, repairs=repairs, c1=c1, dispatch=dispatch, runstatus=runstatus, runner=runner,
              circuit=circuit, dominance=dominance, prints=prints, readings=readings)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b694_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
