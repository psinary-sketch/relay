# -*- coding: utf-8 -*-
"""b687_record.py -- THE ACT'S RECORD TOOL, b687 under (R297).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b687's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b686_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes --
### the branches route reading a remote branch and its ancestry this act --, the answers route, the command bank, the defects) in stages: the
### step-zero and Component 1 routes first; the late routes (seal hashes, repairs, root, scores, entry, trail) added at Component 4.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b687_record.py <route> [dry]`.
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
import b687_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank. Carried from b686_record.py with b687's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b687_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b687_findings.json': dict(entry_line=99999, title='stand-in'),
        'b687_trail.json': dict(line=99999),
        'b687_act_root.json': dict(root='0' * 64, previous='c51755ee' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b687's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b687_scanfile_%s.md' % tag)
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
    """a row of data/b687_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
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
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b687_rowgen_<stage>.txt."""
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
    L = ['b687 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b687_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R297)(6))
def branches(*a):
    """every branch (R297)(6) names, its tip read before any delete, its fate; the remote branch recut-spinor-b686 read at the remote (one
    ls-remote) with its tip printed as an ancestor of main at v0.1.1; any branch under the push-b686 prefix that --merged lists and the ruling
    does not name, reported and KEPT. data/b687_branches.txt (.json)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    anc = []
    for repo, b in K.DELETE_REMOTE:
        o = g(repo, 'ls-remote', '--heads', 'origin', b).split()
        tip = o[0] if o else ''
        main_tag = g(repo, 'rev-parse', K.SPINOR_TAG + '^{commit}').strip()
        main = g(repo, 'rev-parse', 'main').strip()
        is_anc = bool(tip) and grc(repo, 'merge-base', '--is-ancestor', tip, main) == 0
        anc.append(dict(repo=repo, branch=b, tip=tip, main=main, tag=K.SPINOR_TAG, tag_commit=main_tag, main_at_tag=main == main_tag, ancestor=is_anc))
        rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=is_anc, fate='DELETED'))
    named = set((r['repo'], r['branch']) for r in rows)
    extra = []
    for repo, _bs in K.DELETE:
        for x in g(repo, 'branch', '--merged', 'main', '--format=%(refname:short)').split(NL):
            x = x.strip()
            if x.startswith('push-b686') and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b687 -- STEP ZERO, (R297)(6): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; listed by `git branch --merged main --list <name>` (for the remote',
         '### branch: its tip an ancestor of main) ; fate. Deleted by name in the house form, each delete command naming one branch with no glob in',
         '### any half, one command per message, in sequence; no branch the ruling does not name.']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                               r['fate']) for r in rows]
    L += ['', '### the remote branch`s ancestry ((R297)(6)): ' + '; '.join(
        '%s %s at the remote %s ; main %s ; %s at %s (main at the tag %s) ; ANCESTOR OF MAIN %s' % (
            os.path.basename(x['repo']), x['branch'], x['tip'], x['main'][:12], x['tag'], x['tag_commit'][:12], x['main_at_tag'], x['ancestor'])
        for x in anc)]
    L += ['', '### branches under the push-b686 prefix that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d ; UNNAMED UNDER THE PREFIX %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows), len(extra))]
    put_txt('b687_branches.txt', L)
    put_json('b687_branches.json', dict(at=utc(), rows=rows, ancestry=anc, extra=[list(x) for x in extra]))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R297)(1)
WH = ('*Appended 2026-10-18 by b687 to b686’s entry (:9260), under `(R297)`(1) -- b686 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b686_closing.txt):*')
WB = (' “b686 closed: relay b0249275, PLACE-papers 9b9a7c6; suite 110 of 110; root c51755eea1318579…; 1 prompt answered; 2 defects” '
      '(data/b686_closing.txt :1), the closing pushed and read back at relay 3e547498 (data/b686_closing_push_out.txt). The citation check '
      '72 of 72 after the seat’s own check row was corrected (data/b686_citation_check.txt); b685’s weight line at FINDINGS :9258 with its '
      'head line quoted. The N4 scorer reads the suite banks and the scores bank and not the entry; the scores bank written once before the '
      'entry, N4 and S2 read at the close into data/b686_scores_close.json; the rule at data/b686_rules.txt row (1), the diff in '
      'data/b686_tool_repairs.txt. The three FOUNDATIONS cells (:628-:630) written by the generator alone at PLACE-papers f5111a2, v0.2.1 to '
      'v0.2.2; the distance 55 by b670’s method and 0 at the generator’s claim, as at b682 (data/b686_correspondence_after.txt :12). '
      'SIDE-spinor named at 3 by the larger table (15 rows against SIDE-li-map’s 13, data/b686_naming.txt :57), the workflow and the print '
      'list alone on main, both runner builds DERIVES with 15 prints equal line for line, merged at aca59d1 and tagged v0.1.1; the distance '
      '3 to 1, SpinorLeg.lean :21 “(salt-checked)” carried as R4. Suite 110 of 110 (89 standing, 21 over the act’s banks) pre-push and '
      'post-push, no declared failure; all eight scores HELD at the close; root c51755ee over 57 banks; '
      'mirror-refresh-2026-10-18-b686.zip CLEAN with the root line. Two defects, both the seat’s: (a) the partner copy’s differing lines '
      'given as 4 from a figure the generator stores, the live count 13, all 13 entered under `W-ORD-ONE-COPY` and the diff bank corrected; '
      '(b) a combine call piped into sed after the post-push suite, the third sed across acts, entered and counted in the command bank -- on '
      'which G-EDIT-ROUTE’s reading is extended at b687’s carry to the whole act’s command bank, the closing’s capture included. Nothing '
      'deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b687_record_lines.json', 'c1', entry=K.B686_ENTRY,
         check=[('FINDINGS.md', K.B686_ENTRY, '## '), ('OPEN_TRAILS.md', K.B686_TRAIL, '### b686')], dry=dry)


# ================================================================================ COMPONENT 3: THE ORDERS, (R297)(5) AS AMENDED (data/b687_rules.txt row (1))
OH1 = ('*Appended 2026-10-19 by b687 beneath b686’s trail record (:14862), under `(R297)`(5) as the author’s word amends it -- '
       '`W-ORD-EPSTEIN-COUNT` (:14678; re-dated :14832) DISCHARGED-BY-DERIVATION:*')
OB1 = (' the four readings of its trigger made (relay data/b687_plan.txt; the author’s word on it, data/b687_author_answers.txt): (i) the ζ '
       'instance re-derived by b685’s steps on T ≥ e, a_e = 0.218287, b_e = 0, c_e = 1.731426, at or below Hasanalizade-Shen-Wong Cor 1.2 (9.3675; '
       '9.4925 as Bellotti-Wong correct it), Trudgian 2014 Cor 1, Platt-Trudgian 2015 Cor 1 and Backlund’s row at T = e, 10, 100, 1000, 10⁴, '
       'entered as a reading with its crossover heights (Platt-Trudgian 2015 below it beyond T ≈ 1.28e5; data/b687_matched.txt); (ii)-(iii) the '
       'Jensen step (6): J(T) ≤ S(T) and the counts at ρ′ = 1.4, 1.6, 1.8 within their bounds for ζ at T = 100, 1000, 10⁴ and for Z_Q at T = 50, '
       '100, 149 (data/b687_jensen_zeta.txt, data/b687_jensen_q0.txt), the literal inner count vacuous for ζ; (iv) 114 of 114 intermediate '
       'inequalities of steps (3), (5)-(7) holding with their margins (data/b687_steps.txt); C1 and C2 as planted (data/b687_controls.txt); '
       'the composition of b685’s (6) run: HCount’s N(t, t + 1) ≤ 10 log(|t| + 3) at every t > 149, the narrowest margin 41.98 '
       '(data/b687_composition.txt). P3: DERIVED — constants certified in balls, analytic steps sourced by line, intermediate inequalities '
       'checked against computed values at sample heights, the ζ instance inside the located bounds at matched range, not compiled '
       '(data/b687_p3_status.txt); the Q0 results of b675, b679, b683 re-read with it (data/b687_q0_reread.txt). Pins: data/b685_count.txt, '
       'data/b687_steps.txt. Status DISCHARGED-BY-DERIVATION.')
OH2 = ('*Appended 2026-10-19 by b687 beneath the line above, under `(R297)`(5) -- `W-ORD-EPSTEIN-COUNT-LEAN` ENTERED:*')
OB2 = (' a Lean statement of the derived count bound over a configuration given as the zeros of a function with a functional equation of '
       'Λ_Q’s shape, a right-edge bound and a growth bound, by the Jensen disc route the vendored ζ local count runs (Zeta23/RvM/LocalCount.lean '
       ':28-:37); its instance at Q0 needs Z_Q as a Lean function, a further act (relay data/b685_count_plan.txt section 5). Trigger “a research '
       'act after b690”. Status OPEN.')


def c3(*a):
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', OH1, NL + OH1 + OB1 + NL), ('OPEN_TRAILS.md', OH2, NL + OH2 + OB2 + NL)], 'b687_orders_lines.json', 'c3',
         entry=K.ORDER_LINE, check=[('OPEN_TRAILS.md', K.ORDER_LINE, '`W-ORD-EPSTEIN-COUNT` (:14678) RE-DATED'), ('OPEN_TRAILS.md', K.B686_TRAIL, '### b686')],
         dry=dry)


# ================================================================================ THE ANSWERS BANK (b686's route, carried)
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
    """data/b687_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
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
    for cid, (i, t, _ts) in results.items():      # ### a word opened by BEGIN with no END after it: noted, its text read in the RESULT line above
        for mm in re.finditer(r'="BEGIN(?:(?!END").)*?"(?=, "|\.\s|$)', t or '', re.S):
            if not re.search(r'END"\s*$', mm.group(0)):
                W += ['### NOTE (transcript line %s): a word opened by BEGIN and carrying NO END marker -- %r ... %r; the seat asked before acting '
                      '(the tail check), and the navigator`s answer reads it complete as received, the END dropped by the paste. Its text is the '
                      'RESULT line above.' % (i, mm.group(0)[2:80], mm.group(0)[-60:]), '']
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b687 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b687_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b687_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE COMMAND BANK (b686's route, carried)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402

SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')
SED = re.compile(r'(^|[;&|(]\s*|\s)sed\s')


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def sed_cmd(cmd):
    """data/b685_rules.txt row (2): a command carrying sed in any form, read outside quoted strings."""
    return SED.search(QUOTED.sub('""', cmd)) is not None


PREV_ACT, PREV_SESSION, PREV_ANCHOR = 'b686', '3bd076e1-80b3-48c6-919f-407447a1df25', 'RULING (R296) BEGIN'
SED_KIND = 'R sed in any form (data/b685_rules.txt row (2))'


def prev_capture():
    """(R297)(1), the carry-time repair of G-EDIT-ROUTE's reading (the navigator's answer on miss (b), option 1): the previous act's capture
    AFTER ITS POST-PUSH SUITE -- every command of b686's session (and its subagents) timestamped at or after the call that combined its
    post-push parts into data/b686_checks_postpush.txt, the closing's commands among them -- read at this act's step zero."""
    rows = ER.capture('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % PREV_SESSION, PREV_ANCHOR,
                      'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % PREV_SESSION)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV_ACT in r['cmd'] and '--combine' in r['cmd']]
    if not first:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE IS NOT IN ITS CAPTURE -- NOTHING READ')
    out = [dict(r, src='%s %s' % (PREV_ACT, r['src'])) for r in rows if r['ts'] >= first[0]]
    for i, r in enumerate(out):
        r['n'] = 'p%d' % (i + 1)
    return out


def edit_route_offences(rows):
    """the arm's offences, repaired: tools/edit_route.py's arms (unchanged) and, beside them, sed in any form (data/b685_rules.txt row (2)),
    read outside quoted strings; [(row, [(kind, text)])] for the offending rows."""
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


def delete_shape(cmd):
    """(R297)(6): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    return names, [ch for ch in '*?[' if ch in c]


IDENT = ('psinary', 'hotmail', 'seale', 'york', 'orcid', '0009-0008')


def outbound():
    """the act's outbound requests other than git: every WebSearch query, WebFetch URL and subagent prompt from the ruling's line on, read
    from the assistant lines of the session transcript, with the author's identifiers searched in each."""
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
    lean =[r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    mv = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'(^|&&\s*|;\s*)gh workflow run\b', QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'Start-Process|\bnohup\b|run_in_background', r['cmd'])]
    seds = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and sed_cmd(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    ob = outbound()
    L = ['b687 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE ((R297)(1), the repaired window): %s commands of session %s from %s, '
              'its offences printed whole (%d):' % (len(prev), PREV_SESSION[:8], prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
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
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R297)(6): one branch per command, no glob in any half): ' + ('; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git (web searches, subagent prompts and fetches), each with the author`s identifiers found in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; '
              'MOVE OR DELETE COMMANDS %d ; BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(mv), sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl),
                  len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    put_txt('b687_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b687_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        prev=dict(act=PREV_ACT, session=PREV_SESSION, rows=len(prev),
                                                  offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                        seds=[r['n'] for r in seds], moves_deletes=[r['n'] for r in mv],
                                        delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes], outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r in seds:
        print('  sed #%d: %s' % (r['n'], r['cmd'].split(NL)[0][:200]))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b687_defects.txt').split(NL)
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
    t = rdn('b687_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b687_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


# ================================================================================ THE LATE ROUTES (b686's, carried at Component 4 with b687's names)
RELAY = ROOT


def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection', 'SIDE-class-number-anomaly',
                                   'SIDE-spinor', 'SIDE-li-map']


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('b687_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (no kernel written in this act)' % len(ks))


def seal_hashes():
    import hashlib
    rec_ = jl('b687_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b687_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


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


ROOT_EXCLUDE = re.compile(r'^b687_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*)\.?(txt|json|md|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b687_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['b687 -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % utc(), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('b687_root_banks.txt', L)
    put_json('b687_root_banks.json', dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b687_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b687'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b687_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='b687_ra_') as tmp:
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
    L = ['b687 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b687_root_arm.txt', L)
    put_json('b687_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b687 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b687_table_final.txt', L)
    put_json('b687_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


# ================================================================================ THE SCORES: (N1)-(N5) OF THE FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and not the entry; the entry reads the scorer's bank. `scores` writes
# ### data/b687_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there, the bank it waits on named, and
# ### is read at the close by `scores close` into data/b687_scores_close.json, which no ledger line reads.
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b686_closing_push_out.txt', 'b670_work_orders.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
ENTRY_ARMS = ('G-ENTRY-SCORES-EQUAL', 'G-ENTRY-HEAD-STATUS')
ARM_ROW = re.compile(r'^  (G-[A-Z0-9-]+)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+(OK|### FAILS|.*)$')
B685_BANKS = ('data/b685_count.txt', 'data/b685_count.json', 'data/b685_count_controls.txt', 'data/b685_count_part1.json',
              'data/b685_count_part2.json', 'data/b685_count_part4.json', 'data/b685_count_plan.txt', 'tools/b685_count.py')


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s[:19] + 'Z', '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def _first_commit(repo, path):
    """the commit time of the first commit carrying a path (git log --diff-filter=A), or None."""
    t = g(repo, 'log', '--diff-filter=A', '--format=%ct', '--', path).split()
    return int(t[-1]) if t else None


def _arm_row(bank, arm):
    """an arm's row in a suite bank: (LIVE, NEG, POS, verdict) or None where the bank or the row is absent."""
    for l in rdn(bank).split(NL):
        m = ARM_ROW.match(l)
        if m and m.group(1) == arm:
            return m.group(2), m.group(3), m.group(4), m.group(5).strip()
    return None


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', 'FINDINGS.md', 'OPEN_TRAILS.md')
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _n1():
    cm = jl('b687_commands.json')
    ok = bool(cm) and not cm.get('local_lean')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches %d (relay data/b687_commands.txt, %d commands read)' % (
            cm.get('local_lean') if cm else '### UNREAD', len(cm.get('dispatches') or []), len(cm.get('rows') or [])))


def _plan_prompt():
    """the call that put the plan's prompt: the first call after the plan's commit whose questions carry "(R297)(3)"."""
    t_plan = _first_commit(RELAY, 'data/b687_plan.txt')
    for c in jl('b687_author_answers.json').get('calls') or []:
        ts = _iso(c.get('ts') or '')
        if ts and t_plan and ts >= t_plan:
            return t_plan, ts, _iso(c.get('result_ts') or '')
    return t_plan, None, None


def _n2():
    import hashlib
    plan = rdn('b687_plan.txt')
    t_plan, t_prompt, t_answer = _plan_prompt()
    parts = [jl('b687_readings_part%d.json' % k) for k in range(1, 7)]
    t_first = min([x for x in (_iso(p.get('at') or '') for p in parts) if x] or [0])
    quoted = all(x in plan for x in ('3fc4c89f', '274b3a0a14d79400', '97d9e70994b46f6a', '3362f66af9fa9373', 'Corollary 1.2, p. 2', 'Corollary 1, p. 2'))
    refut = plan.count('Refutation condition:') >= 4
    order = bool(t_plan and t_prompt and t_answer and t_first) and t_plan <= t_prompt <= t_answer <= t_first
    unchanged = []
    for p in B685_BANKS:
        r0 = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (K.PRE_RELAY, p)], capture_output=True)
        r1 = subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:%s' % p], capture_output=True)
        now = open(os.path.join(ROOT, *p.split('/')), 'rb').read()
        unchanged.append(r0.returncode == 0 and r0.stdout == r1.stdout and hashlib.sha256(now.replace(b'\r\n', b'\n')).digest()
                         == hashlib.sha256(r0.stdout.replace(b'\r\n', b'\n')).digest())
    ok = quoted and refut and order and all(unchanged)
    return ('HELD' if ok else 'REFUTED'), (
        'the located bounds quoted from their pinned sources in the plan (relay data/b687_plan.txt section 1, each PDF`s sha256): %s; every '
        'reading`s refutation condition stated in the plan (%d): %s; the plan committed, raised and answered before the first reading part '
        '(the plan`s commit, the prompt, the answer, the first part bank in that order): %s; b685`s count, control, part and plan banks and '
        'tools/b685_count.py unchanged at HEAD and in the tree against %s (%d of %d): %s' % (
            quoted, plan.count('Refutation condition:'), refut, order, K.PRE_RELAY, sum(unchanged), len(unchanged), all(unchanged)))


def _n3():
    st, jz, jq, ct = rdn('b687_steps.txt'), rdn('b687_jensen_zeta.txt'), rdn('b687_jensen_q0.txt'), rdn('b687_controls.txt')
    rows = [l for l in st.split(NL) if l.startswith(('  ζ ', '  Z_Q '))]
    balls = all(l.count('±') >= 3 and '| margin ' in l for l in rows) and bool(rows)
    drows = [l for l in (jz + NL + jq).split(NL) if l.startswith('  T = ')]
    dballs = bool(drows) and all('±' in l and 'margin' in l for l in drows)
    planted = '**C1 AS PLANTED ; C2 AS PLANTED' in ct
    held = '114 OF 114 INTERMEDIATE INEQUALITIES HOLD' in st
    ok = balls and dballs and planted
    return ('HELD' if ok else 'REFUTED'), (
        'every intermediate inequality`s row a ball with its bound, computed value and margin (relay data/b687_steps.txt, %d rows): %s, %s; every '
        'disc row with its count, its bound as a ball and its margin (relay data/b687_jensen_zeta.txt, data/b687_jensen_q0.txt, %d rows): %s; the '
        'controls as planned (relay data/b687_controls.txt): %s' % (len(rows), balls, '114 of 114 holding' if held else '### NOT ALL HOLDING', len(drows),
                                                                   dballs, planted))


def _n4():
    """data/b686_rules.txt row (1): N4 read from the suite banks -- the act arms G-ENTRY-HEAD-STATUS (the landed entry's head line in (R297)(5)'s
    words, no sentence of the act's lines calling P3 proved or compiled) and G-ENTRY-SCORES-EQUAL, each row in the pre-push and the post-push
    bank -- and the status bank; no ledger line."""
    pre = [_arm_row('b687_checks.txt', a_) for a_ in ENTRY_ARMS]
    post = [_arm_row('b687_checks_postpush.txt', a_) for a_ in ENTRY_ARMS]
    stb = K.P3_WORDS in rdn('b687_p3_status.txt')
    good = lambda r: r is not None and r[0] == 'PASS' and r[3] == 'OK'   # noqa: E731
    if any(r is None for r in post):
        return 'PENDING', ('waits on the post-push suite bank (relay data/b687_checks_postpush.txt); the pre-push rows of %s: %s; the status bank '
                           'carrying (R297)(5)`s words %s; the third case of (R297)(5) struck by the author`s word (data/b687_rules.txt row (1)), no '
                           'prompt of it' % (', '.join(ENTRY_ARMS), ['%s' % ' '.join(r) if r else '### NOT YET RUN' for r in pre], stb))
    ok = stb and all(good(r) for r in pre + post)
    return ('HELD' if ok else 'REFUTED'), (
        'the entry`s head line in (R297)(5)`s words and no sentence of the act calling P3 proved or compiled, read by %s in the pre-push suite (%s) '
        'and the post-push suite (%s), relay data/b687_checks.txt and data/b687_checks_postpush.txt; the status bank relay data/b687_p3_status.txt '
        'carrying the words %s; the third case struck by the author`s word, no prompt of it; N4 read from these banks and no ledger line' % (
            ' and '.join(ENTRY_ARMS), '; '.join(' '.join(r) for r in pre if r), '; '.join(' '.join(r) for r in post), stb))


def _n5():
    face = jl('b687_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b687_|audit_b687_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import importlib
    argv, sys.argv = sys.argv, sys.argv[:1]
    try:
        CH = importlib.import_module('b687_checks')
    finally:
        sys.argv = argv
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ob = jl('b687_commands.json').get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = k_ok and not pp_beyond and not kinds_beyond and not differ and not new_arms and not ident and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it, no kernel main written: %s; '
            'standing arms added: %s (the act`s arms over its own banks %d); sealed tools not agreeing %s; PLACE-papers beyond FINDINGS and '
            'OPEN_TRAILS: %s; relay files of a kind beyond the act`s banks and tools, the table, the root list, b686`s push-out bank and the orders '
            'bank`s appended rows: %s; "patent" in the lines written: %s; outbound requests: the seat`s git reads and pushes at github.com and %d '
            'web searches, subagent prompts and fetches (relay data/b687_commands.txt), an identifier of the author in %s' % (
                K.DRAFT, k_ok, new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE', pat or 'NONE',
                len(ob), [r['line'] for r in ident] or 'NONE'))


def _s_scores():
    import collections
    TF, RA_ = jl('b687_table_final.json'), jl('b687_root_arm.json')
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b687_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b687_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def scores(*a):
    """`scores [dry]` writes data/b687_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads N4 and the
    readings that waited into data/b687_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:700]))
    if 'dry' in a:
        return
    if close:
        put_json('b687_scores_close.json', dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, 'b687_scores.json')):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('b687_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def scores_line(S):
    """the entry's scores line, composed from the scores bank alone (the act arm G-ENTRY-SCORES-EQUAL composes it the same way and compares)."""
    return '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.'


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
def TRAIL_HEAD():
    return ('### b687 — lane two, act one hundred and fourteen, the research act under (R297): the b685 derivation tested at matched range, in the '
            'Jensen disc and at every intermediate step, for ζ and for Z_Q')


def _calls():
    return jl('b687_author_answers.json').get('calls') or []


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _readings():
    R = jl('b687_readings.json')
    p1 = jl('b687_readings_part1.json')
    return R, p1


def _title():
    R, p1 = _readings()
    a_e = (p1.get('a_e') or ['?'])[0][:8]
    c_e = (p1.get('c_e') or ['?'])[0][:8]
    hv = dict((h, v) for h, v, _w in R.get('hypotheses') or [])
    within = 'within' if hv.get('H2') == 'HELD' else 'over'
    return ('## The b685 derivation tested: matched-range constants a_e = %s, c_e = %s against HSW, Trudgian, Platt–Trudgian at T = e, 10, 100; '
            'the Jensen disc %s its bound at every sampled height for ζ and Z_Q; %s of %s intermediate inequalities holding; P3 %s' % (
                a_e, c_e, within, R.get('steps_hold', '?'), R.get('steps', '?'), K.P3_WORDS))


def _finding_text():
    """the FINDINGS entry, composed before the root: its scores line from the scores bank alone (data/b686_rules.txt row (1)); the root is
    carried by the trail record."""
    S = jl('b687_scores.json')
    R, p1 = _readings()
    comp = R.get('composition') or {}
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b687_author_answers.txt'), re.M))
    c1 = _rl_lines('b687_record_lines.json') + ['?']
    oc = _rl_lines('b687_orders_lines.json') + ['?', '?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    cross = p1.get('crossover') or {}
    xpt = (cross.get('PT15|e') or {}).get('T', '?')
    xtr = (cross.get('TR14|e') or {}).get('T', '?')
    mg = ((comp.get('narrowest') or {}).get('margin') or [None])[0]
    marg = ('%.4f' % float(mg)) if mg else '?'
    e = ['', _title(), '',
         'P3 at Q0 -- HCount’s N(t, t + 1) ≤ 10 log(|t| + 3) -- stands DERIVED — constants certified in balls, analytic steps sourced by line, '
         'intermediate inequalities checked against computed values at sample heights, the ζ instance inside the located bounds at matched range, '
         'not compiled: the four readings b685’s order named found no step of its Backlund derivation refuted, and its composition holds HCount’s '
         'inequality at every t > 149 with the narrowest margin %s.' % marg, '',
         '*Filed at b687 on the author’s ruling `(R297)` and the author’s word on the plan, which struck `(R297)`(5)’s third case (relay '
         'data/b687_rules.txt row (1)); %d questions put. Banks: relay `data/b687_plan.txt`, `data/b687_matched.txt`, `data/b687_jensen_zeta.txt`, '
         '`data/b687_jensen_q0.txt`, `data/b687_steps.txt`, `data/b687_controls.txt`, `data/b687_composition.txt`, `data/b687_p3_status.txt`, '
         '`data/b687_q0_reread.txt`.*' % n_ans, '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed, both the navigator’s and raised before the '
         'components that cite them. b686 at its weight (FINDINGS :%s), its head line quoted; G-EDIT-ROUTE’s reading extended at carry to the '
         'previous act’s capture after its post-push suite and to sed in any form.' % (cc.group(1) if cc else '?', cc.group(2) if cc else '?',
                                                                                      cc.group(3) if cc else '?', c1[0]), '',
         '**Reading (i), matched range:** the ζ instance re-derived by b685’s steps on T ≥ e gives a_e = %s, b_e = 0, c_e = %s, at or below '
         'Hasanalizade-Shen-Wong Corollary 1.2 (9.3675, and 9.4925 as Bellotti-Wong correct it), Trudgian 2014 Corollary 1, Platt-Trudgian 2015 '
         'Corollary 1 (read in place of the 2021 paper the order named, which states no such bound) and Backlund’s row at T = e, 10, 100, 1000 and '
         '10⁴; entered as a reading beside the others, the crossovers printed -- Platt-Trudgian 2015 below the derived bound beyond T ≈ %s, '
         'Trudgian 2014 beyond T ≈ %s.' % ((p1.get('a_e') or ['?'])[0][:8], (p1.get('c_e') or ['?'])[0][:8], xpt, xtr), '',
         '**Readings (ii)-(iii), the Jensen step:** for ζ at T = 100, 1000, 10⁴ (at the derivation’s c = 1.5, r = 1.98, and at c = 1.7, r = 2.05 '
         'beside it) and for Z_Q at T = 50, 100, 149 (b681’s balls, their partners, and the band (150, 151.59] counted by b667’s argument principle, '
         'two zeros on the line), the Jensen sum over certified zeros stays below the step’s bound S(T) and the counts at ρ′ = 1.4, 1.6, 1.8 below '
         'theirs; the literal inner disc of radius c − ½ holds no zero at any height, vacuous for ζ, whose zeros it cannot enter.', '',
         '**Reading (iv), every step:** %s of %s intermediate inequalities of steps (3) and (5)-(7) hold at the sampled heights with their margins '
         '(the narrowest the envelope on the Jensen circle, 0.058); Z_Q at σ > 2.5 read by a lattice sum with its tail bound, checked against '
         'b667’s route. The controls read as planned: the doubled disc’s bound and count grow; the planted Γ inequality fails at every height.' % (
             R.get('steps_hold', '?'), R.get('steps', '?')), '',
         '**The orders:** `W-ORD-EPSTEIN-COUNT` DISCHARGED-BY-DERIVATION (OPEN_TRAILS :%s), pinned by relay data/b685_count.txt and '
         'data/b687_steps.txt; `W-ORD-EPSTEIN-COUNT-LEAN` entered (:%s), trigger “a research act after b690”; the Q0 results of b675, b679 and '
         'b683 re-read with P3’s new status (relay data/b687_q0_reread.txt).' % (oc[0], oc[1]), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b685’s derivation (relay data/b685_count_plan.txt) and b681’s '
         'narrowed zeros, and is re-read by the act that writes `W-ORD-EPSTEIN-COUNT-LEAN`, and by b689, whose strip-free Li converse takes P3 at '
         'this status. It strengthens the programme’s offering of a zero-count law for Z_Q at D = −23 whose every step has been tested against '
         'computed values at sampled heights, not only derived.', '',
         '**Carried to:** `W-ORD-EPSTEIN-COUNT-LEAN` (a research act after b690); b689 (the strip-free Li converse, the w = 1 split); the band '
         'squares’ form and the lattice route, the seat’s, for the author’s reading (relay data/b687_defects.txt (g), (h)); the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the band (150, 151.59] counted in twelve resumable squares of side 0.53 and its two zeros located on the line by b671’s (M-on) '
              'form, not by quartering (defect (g)); (2) Z_Q at σ > 2.5 read by a lattice sum with an elementary tail bound, outside b667’s route, '
              'checked against it at three points (defect (h)); (3) the literal inner disc vacuous for ζ, H2 read on J(T) and three radii by the '
              'navigator’s answer; (4) H5 run on H2-H4 by the author’s word, the matched-range sharpness entered as a reading with its crossovers')


def _trail_text():
    S, J = jl('b687_scores.json'), jl('b687_act_root.json')
    fj = jl('b687_findings.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b687_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b687_record_lines.json') + ['?']
    oc = _rl_lines('b687_orders_lines.json') + ['?', '?']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R297) ratified.** (1) b686 at its weight. (2) The object. (3) The readings. (4) The controls. (5) The landing, as the author’s word '
             'amends it. (6) The branches. (7) The read-first bank. (8) The draft held at v5. (9) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b686’s weight), :%s (the entry); OPEN_TRAILS.md:%s, :%s (the orders); this record.' % (
                 c1[0], fj.get('entry_line'), oc[0], oc[1]), '',
             '**Act root:** b687 `%s` (previous `%s`, b686’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s (relay data/b687_author_answers.txt); none after the root.' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**P3:** %s (relay data/b687_p3_status.txt).' % K.P3_WORDS, '',
             '**The readings:** relay data/b687_matched.txt, data/b687_jensen_zeta.txt, data/b687_jensen_q0.txt, data/b687_steps.txt, '
             'data/b687_controls.txt, data/b687_composition.txt.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b687_closing.txt).', '',
             '**The open orders:** `W-ORD-EPSTEIN-COUNT-LEAN` (a research act after b690); `W-ORD-LEDGER-SPLIT-RESOLVER` (on the author’s word); '
             '`W-ORD-CHAIN-PAGE-B638-CASES`; `W-ORD-PRINT-TARGETS`; `W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; '
             '`W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; `W-ORD-ROOT-BINARY-BANK`.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b687_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S, C = jl('b687_scores.json'), jl('b687_scores_close.json')
    L = ['=' * 104, 'b687 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s%s' % (
        k2, S[k2][0], S[k2][1], ('  ### AT THE CLOSE: %s -- %s' % (C[k2][0], C[k2][1])) if (S[k2][0] == 'PENDING' and C.get(k2)) else '')
        for k2 in SCORE_KEYS]
    L += [''] + rdn('b687_defects.txt').rstrip(NL).split(NL)
    put_txt('b687_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b687_scores.json', 'b687_findings.json', 'b687_trail.json', 'b687_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b687_record_lines.json') + ['?']
    oc = _rl_lines('b687_orders_lines.json') + ['?', '?']
    L = ['b687 -- THE COMPONENTS, BANKED UNDER (R297).', '',
         '### COMPONENT 0 : the citation check (data/b687_citation_check.txt), step zero (data/b687_ferry.txt, data/b687_readfirst.txt, '
         'data/b687_stepzero.txt, data/b687_tests_stepzero.txt, data/b687_rowgen_stepzero.txt, data/b687_branches.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b686`s weight FINDINGS :%s ; G-EDIT-ROUTE`s reading extended at carry (data/b687_tool_repairs.txt) ; N4 %s' % (c1[0], S['N4'][0]),
         '### COMPONENT 2 : the plan (data/b687_plan.txt), the located bounds quoted, one prompt, the author`s word (data/b687_rules.txt row (1)) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the readings (data/b687_matched.txt, data/b687_jensen_zeta.txt, data/b687_jensen_q0.txt, data/b687_steps.txt, '
         'data/b687_controls.txt, data/b687_composition.txt), P3 (data/b687_p3_status.txt), the re-reading (data/b687_q0_reread.txt), the orders '
         'OPEN_TRAILS :%s, :%s ; N3 %s' % (oc[0], oc[1], S['N3'][0]),
         '### COMPONENT 4 : the carry-time reading (data/b687_tool_repairs.txt), the dry-run steps (data/b687_reg_gate.txt), the seal '
         '(data/b687_seal_hashes.json), the suite in four parts ; S3 %s' % S['S3'][0],
         '### COMPONENT 5 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('b687_components.txt', L)
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
    cells_, fired = screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells_)
        return
    if not os.path.isfile(os.path.join(D, 'b687_scores.json')):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b687_findings.json', dict(title=t))
    j = jl('b687_findings.json')
    j['entry_line'] = ln
    put_json('b687_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b687_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


FACE_REL = 'data/b687_registration_2026-10-19.txt'
FACE = os.path.join(D, 'b687_registration_2026-10-19.txt')


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written -- converted by conv and run through the screens their landing runs, the needles the face names read in
    each; prints DRY-RUN STEP : CLEAN and exits 0 only when both screens are quiet and every needle is found. Writes no bank."""
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
    env = dict(os.environ, PYTHONIOENCODING='utf-8')

    def runb(args, out):
        r = subprocess.run([sys.executable] + args, capture_output=True, cwd=ROOT, env=env)
        b_ = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            open(p + '.tmp', 'wb').write(b_)
            os.replace(p + '.tmp', p)
        return r.returncode, b_.decode('utf-8', 'replace')
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b687_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b687_regspec.py')], 'b687_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b687_satisfiable.json', '--emit', 'b687'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b687_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b687_census_stepzero.txt'), ('b327_faces_census.py', 'b687_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b687_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b687'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b687_reg_gate.txt', 'data/b687_reg_termscan.txt', 'data/b687_regspec_run.txt', 'data/audit_b687_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b686's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '2026-10-19-b687'
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
    put_json('b687_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b687':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b687`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b687_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b687_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b687_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b687 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b687 (the last export b686`s, D:/MY-DOwnloads/mirror-refresh-2026-10-18-b686.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b687_mirror.txt', L)
    put_json('b687_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


# ================================================================================ THE CARRY-TIME READING ((R297)(1); Component 1 and Component 4)
REPAIRS = [
    ('G-EDIT-ROUTE`S READING EXTENDED (answering b686 defect (b) and this act`s (a), under (R297)(1) and the navigator`s answer on miss (b),',
     'option 1; relay data/b687_author_answers.txt): b686`s arm (tools/b686_checks.py :1045, predicate `edit_route_ok` :582-:583) read',
     'ER.scan over its own act`s capture alone, and tools/edit_route.py`s (S) arm reads `sed -i` alone -- so b686`s combine piped into',
     '`sed -n 0p` after its post-push suite, and this act`s five `sed -n` reads, were no offence. b687`s reading, written once in the shared',
     'writer (tools/b687_record.py `prev_capture`, `edit_route_offences`) and read by both the command bank and the arm: (1) the WINDOW -- this',
     'act`s whole capture through the closing, and the previous act`s capture from the call that combined its post-push parts on (its',
     'closing`s commands among them), read at step zero; (2) the OFFENCES -- tools/edit_route.py`s arms unchanged, and beside them sed in any',
     'form (data/b685_rules.txt row (2)), read outside quoted strings. The arm then FAILS for b687 on defect (a) (five commands) and reads',
     'b686`s (b) in the previous act`s window; it is declared on the face by name, and the capture is not trimmed. The diff of the',
     'command bank`s reading and of the arm`s predicate against b686`s sealed copies is printed whole below.'),
    ('THE STANDING SET FOR b687 (answering no defect: the act`s objects): the standing arms are b686`s face`s (G2) arms less b686`s act arms,',
     'the twenty rule arms among them; the runner arms read the last merged runs (b686`s SIDE-spinor runs; this act dispatches none); the',
     'step-zero arms read this act`s banks -- nine branches, one remote row.'),
]


def _fn_src(src, name):
    """a top-level function's source, from its `def` line to the next top-level line; '' where the tool carries no such function."""
    if ('\ndef %s(' % name) not in src:
        return ''
    i = src.index('\ndef %s(' % name) + 1
    m = re.search(r'\n(?=\S)', src[i + 1:])
    return src[i:i + 1 + m.start() + 1] if m else src[i:]


def repairs(*a):
    """data/b687_tool_repairs.txt: rows are repairs with the defect they answer. Each tool carried from a sealed b686 copy is read against
    b686's seal hash (relay data/b686_seal_hashes.json) first, and its diff against that copy counted by hunks (NOT YET CARRIED where the
    act has not written it); tools/rule_arms.py and tools/edit_route.py read against the last seal record naming them (unedited in this act);
    the arm's reading's diff against b686's sealed copies printed whole."""
    import difflib
    import hashlib
    seal = jl('b686_seal_hashes.json').get('tools') or {}
    rows = []
    for t0 in ('b686_citation.py', 'b686_closing.py', 'b686_reg_gate.py', 'b686_regspec.py', 'b686_tests.py', 'b686_worklist.py',
               'b686_record.py', 'b686_checks.py'):
        t1 = t0.replace('b686_', 'b687_')
        old, new = os.path.join(T, t0), os.path.join(T, t1)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        ex = os.path.exists(new)
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8',
                           errors='replace').stdout if ex else ''
        rows.append((t0, t1, now, seal.get(t0), len(re.split(r'(?m)^(?=@@ )', d)[1:]), ex))
    inst = {}
    for t in ('rule_arms.py', 'edit_route.py'):
        nowh = hashlib.sha256(open(os.path.join(T, t), 'rb').read()).hexdigest()
        acts = [x for x in ('b686', 'b685', 'b684', 'b683', 'b682', 'b681') if (jl('%s_seal_hashes.json' % x).get('tools') or {}).get(t)]
        inst[t] = (nowh, acts[0] if acts else None, (jl('%s_seal_hashes.json' % acts[0])['tools'][t]) if acts else None,
                   g(ROOT, 'log', '-1', '--format=%h %cI', '--', 'tools/' + t).strip())
    s6r, s7r = rd(os.path.join(T, 'b686_record.py')), rd(os.path.join(T, 'b687_record.py'))
    s6c, s7c = rd(os.path.join(T, 'b686_checks.py')), rd(os.path.join(T, 'b687_checks.py'))
    nd = []
    for (a6, f6), (a7, f7), s6, s7 in ((('b686_record.py', 'commands'), ('b687_record.py', 'commands'), s6r, s7r),
                                       (('b686_record.py', '(none)'), ('b687_record.py', 'prev_capture'), s6r, s7r),
                                       (('b686_record.py', '(none)'), ('b687_record.py', 'edit_route_offences'), s6r, s7r),
                                       (('b686_checks.py', 'edit_route_ok'), ('b687_checks.py', 'edit_route_ok'), s6c, s7c)):
        nd += list(difflib.unified_diff(_fn_src(s6, f6).split(NL) if f6 != '(none)' else [], _fn_src(s7, f7).split(NL) if s7 else [],
                                        '%s %s (sealed)' % (a6, f6), '%s %s%s' % (a7, f7, '' if s7 else ' (NOT YET CARRIED)'), n=1, lineterm=''))
    L = ['b687 -- COMPONENT 1 AND COMPONENT 4, (R297)`S FERRY: THE CARRY-TIME READING OF THE TOOLS, AGAINST b686`S SEALED COPIES (%s)' % utc(), '',
         '### rows are repairs with the defect they answer, after the carried tools: b686`s sealed copy and its seal record; the hunks of the diff',
         '### to b687`s copy. Every hunk is the act`s own text -- its names, its banks, its sections and its predicates over this act`s banks --',
         '### save the repairs below.', '']
    for t0, t1, now, s, nh, ex in rows:
        L.append('  %-20s -> %-20s b686 sealed %s ; the seal`s record %s ; %s ; hunks %s' % (t0, t1, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh if ex else 'NOT YET CARRIED'))
    for t, (nowh, act, sh, last) in inst.items():
        clean = grc(ROOT, 'diff', '--quiet', 'HEAD', '--', 'tools/' + t) == 0 and grc(ROOT, 'merge-base', '--is-ancestor', last.split()[0], K.PRE_RELAY) == 0
        if sh is None:      # ### no seal record names it: unedited read as the working file equal to HEAD, its last commit before the act
            inst[t] = (nowh, act, nowh if clean else None, last)
        L.append('  %-20s    the standing instrument, unedited in this act: %s ; the last seal record naming it (%s`s) %s ; %s ; its last commit %s%s' % (
            t, nowh[:16], act or 'NONE', (sh or '### NONE')[:16], 'AGREE' if inst[t][2] == nowh else '### DIFFER', last,
            (' ; read by the tree: the working file equal to HEAD and its last commit before the act %s' % clean) if sh is None else ''))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### THE DIFF OF THE COMMAND BANK`S READING AND OF THE ARM`S PREDICATE AGAINST b686`S SEALED COPIES (tools/b686_record.py sha256 %s, '
          'tools/b686_checks.py sha256 %s), WHOLE:' % ((seal.get('b686_record.py') or '### NONE')[:16], (seal.get('b686_checks.py') or '### NONE')[:16])]
    L += ['    ' + l for l in nd]
    carried = sum(1 for r in rows if r[5])
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d OF %d ; THE ARM`S DIFF LINES %d.**' % (
        len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n, _e in rows) and all(v[0] == v[2] for v in inst.values()) else '### DIFFER',
        carried, len(rows), len(nd))]
    put_txt('b687_tool_repairs.txt', L)
    print(L[-1])


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, c3=c3, answers=answers, commands=commands, defects=defects, repairs=repairs,
              kernels=kernels, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final, scores=scores, desk=desk,
              components=components, findings=findings, trail=trail, drycheck=drycheck, gatebanks=gatebanks, mbuild=mbuild, mroot=mroot,
              mverify=mverify, mbank=mbank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b687_record.py %s [dry]' % ' | '.join(ROUTES))
        sys.exit(2)
    fn(*sys.argv[2:])
