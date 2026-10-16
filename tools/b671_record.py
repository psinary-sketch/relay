# -*- coding: utf-8 -*-
"""b671_record.py -- THE ACT'S RECORD TOOL, b671 under (R281).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b671's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b670_record.py (the helpers, the landing, the readers, the answers, the late routes); new here: Component 1's
### record lines (b670's weight, the sequence line and its five triggers read from the ferry bank verbatim, the census items), and at their
### components the plan, the narrowing's banks, the map's reading and the landing. No kernel byte is written by any route.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b671_record.py <route> [dry]`.
"""
import calendar
import collections
import gzip
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
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b671_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'H1', 'H2', 'H3', 'H4', 'S1', 'S2', 'S3')
    return {
        'b671_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b671_findings.json': dict(entry_line=99999, title='stand-in'),
        'b671_trail.json': dict(line=99999),
        'b671_act_root.json': dict(root='0' * 64, previous='0c6086ef' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b671's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b671_scanfile_%s.md' % tag)
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
    """a scores row: key N1..N5, H1..H4 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text)."""
    if not re.match(r'^(N[1-5]|H[1-4]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


SQUARE_KEYS = ('kind', 'idx', 're', 'im', 'h', 'count')


def read_square_row(r):
    """a row of b667's certified squares or of this act's narrowed list: kind ON or OFF, its index, its centre (re, im as decimal strings),
    its half-width h and its count 1; returns (kind, idx); raises on a row of another shape or a count not 1."""
    if not isinstance(r, dict) or any(k not in r for k in SQUARE_KEYS) or r['kind'] not in ('ON', 'OFF') or r['count'] != 1:
        raise ValueError('square row of another shape or count: %r' % ((r.get('kind'), r.get('idx'), r.get('count')) if isinstance(r, dict) else r,))
    float(r['re'])
    float(r['im'])
    float(r['h'])
    return r['kind'], r['idx']


NARROW_READINGS = ('NARROWED', 'UNRESOLVED-AT-DEPTH')


def read_narrow_row(r):
    """a row of the narrowing log: a point (kind, idx), its depth reached, its reading NARROWED or UNRESOLVED-AT-DEPTH, and for ON points the
    two endpoint signs of its last interval (opposite, each excluding 0); raises otherwise."""
    if not isinstance(r, dict) or r.get('kind') not in ('ON', 'OFF') or not isinstance(r.get('depth'), int) or r.get('reading') not in NARROW_READINGS:
        raise ValueError('narrow row of another shape: %r' % ((r.get('kind'), r.get('idx')) if isinstance(r, dict) else r,))
    if r['kind'] == 'ON' and r['reading'] == 'NARROWED' and sorted(r.get('signs') or []) != [-1, 1]:
        raise ValueError('an on-line point narrowed without opposite certified signs: %s' % r.get('idx'))
    return r['kind'], r['idx'], r['reading']


RUNNER_KEYS = ('kernel', 'branch', 'ref', 'target', 'run_id', 'conclusion', 'artifact_sha256', 'mem_low', 'stopped', 'gate', 'merged', 'tag')


def read_runner_row(r):
    """a row of the last merged run's bank (b669's, read by the standing runner arms) -- every key of RUNNER_KEYS present; raises KeyError.
    Carried from b670_record.py :1171-:1185 unchanged."""
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


READERS = ['read_score_row', 'read_head', 'read_square_row', 'read_narrow_row', 'read_runner_row']


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R281)(1), (2), (8)
def _ruling():
    t = rdn('b671_ferry.txt')
    i, j = t.find('RULING (R281) BEGIN'), t.find('RULING (R281) END')
    if i < 0 or j < i:
        sys.exit('### THE FERRY BANK CARRIES NO (R281) -- NOTHING WRITTEN')
    return t[i:j]


def _clause(n):
    r = _ruling()
    m = re.search(r'\n\(%d\) (.*?)(?=\n\(%d\) |\Z)' % (n, n + 1), r, re.S)
    if not m:
        sys.exit('### (R281)(%d) NOT FOUND IN THE FERRY BANK -- NOTHING WRITTEN' % n)
    return m.group(1).strip()


def sequence_parts():
    """the sequence line, the author's words verbatim, and the five triggers, each read from (R281)(2) in the ferry bank and never retyped."""
    c = _clause(2)
    m = re.search(r'"(eventually, .*?build\.)"', c, re.S)
    trig = re.findall(r'\((T[1-5])\) (.*?)(?=; \(T[1-5]\) |\. Each later reading act)', c, re.S)
    if not m or [t for t, _x in trig] != ['T1', 'T2', 'T3', 'T4', 'T5']:
        sys.exit('### THE SEQUENCE LINE OR ITS FIVE TRIGGERS NOT READ FROM (R281)(2) -- NOTHING WRITTEN')
    return ' '.join(m.group(1).split()), [(t, ' '.join(x.split())) for t, x in trig]


PAIRS = None


def copy_pairs():
    """every document of PLACE-papers carrying an unversioned and a versioned copy, read from the tree at its HEAD."""
    import posixpath as pp
    files = set(g(PP, 'ls-files', '*.md').split())
    by = {}
    for f in files:
        d, b = pp.split(f)
        m = re.match(r'^(.*?)_v\d+(_\d+)*\.md$', b)
        if m:
            by.setdefault((d, m.group(1)), []).append(b)
    return sorted((pp.join(d, s + '.md'), sorted(v)) for (d, s), v in by.items() if pp.join(d, s + '.md') in files)


WH = ('*Appended 2026-10-14 by b671 to b670’s entry (:8733), under `(R281)`(1) -- b670 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b670_closing.txt), READING 1 OF 2 BANKED:*')
HS = ('*Appended 2026-10-14 by b671 beneath the research order after b668 (:14294), under `(R281)`(2) -- THE SEQUENCE LINE, THE AUTHOR’S '
      'WORDS VERBATIM, AND ITS FIVE TRIGGERS AS MEASURABLES:*')
HC = ('*Appended 2026-10-14 by b671 under `(R281)`(8) -- THE CENSUS ITEMS FROM THE MIRROR’S SORTING, AND `W-ORD-ONE-COPY`:*')
HB = ('### `W-ORD-BESSEL-BOUND-TIGHTEN` -- THE DERIVATIVE BOUND OF (3b) TIGHTENED, PRICED, NOT STARTED, appended 2026-10-14, b671, on the '
      'navigator’s note on the pricing')


def _bessel_order():
    return ('\n' + HB + '\n\n**Items.** The derivative bound of `(R277)`(3b) -- sup|∂_ν K| on the shifted contour, added to each Bessel factor`s '
            'ball -- tightened so that the enclosure of Z_Q on a segment accepts at tens of segments per side; at b667 the remedy`s ball is 131-507 '
            'times r·|Z_Q′| (relay data/b667_epstein_plan.txt :236), so a square`s count accepted a median 1314 segments whatever its size.\n\n'
            '**Reason.** The ratio does not change as a square shrinks, so every count on Q0 pays it; b671`s off-line narrowing is priced at about '
            'ten hours on it (relay data/b671_narrow_plan.txt).\n\n**Price:** one research act. **Trigger:** the next act that counts on Q0 after b671.\n')


def _weight():
    return ('\n' + WH + ' the ten acts b660–b669 read into relay data/b670_ten_acts.txt and data/b670_defects_by_kind.txt; the four readings as '
            'relay data/b670_state.txt writes them with their distances -- (i) 372 rows outside LICENSED or CITED over 33 agenda documents (607 at '
            'b648); (ii) 90 of 100 Correspondence rows behind their kernel’s current tag, each tag by one ls-remote per repository; (iii) the '
            '`(R183)`(3) ceiling sentence byte-equal at README :125, REGISTRY :960 and FINDINGS :6354, one sha256; (iv) 149 orders, 34 open, 46 '
            'done, 69 without a status word (W-ORD-STATUS-CELLS), 33 open and older than ten acts without a trigger met -- the state line “reading '
            '1 of 2 at b670”, no consistency claimed; the methods table at 9 READY of 12, the ζ-naming walk NOT READY with no failure mode '
            'recorded, the consumers section and the argument-principle certification NOT YET USED TWICE; relay data/b670_rules.txt rows 1–5; the '
            'ZFR search NOT LOCATED (11 entries, none carrying 7/8), its request without identifier; the branch chi-li-forward-b669 deleted outside '
            'the ferry’s list and accepted under rules row 4, chi-li-b669 at b804bf2; the TECHNE_TOOLKIT :507 line banked and withheld with history '
            'kept, N5 REFUTED in its letter; the order after b670 entered as placed; FINDINGS :8733, OPEN_TRAILS :14360, relay 87410d3c, '
            'PLACE-papers c740f56, root 0c6086ef… over 44 banks; the suite 85 of 85 before and after the push; nine defects, (a) the navigator’s, '
            '(i) the closing’s reading (iii) printed as a block of the ceiling bank and not its verdict line, entered after the closing; the mirror '
            'at mirror-refresh-2026-10-14-b670.zip CLEAN on three clauses with the root line. Nothing deposited.\n')


def _sequence():
    line_, trig = sequence_parts()
    return ('\n' + HS + ' “' + line_ + '” (relay data/b671_rules.txt row 1). **The five triggers, as measurables** (rows 2–6), each later '
            'reading act printing the five against this row: ' + '; '.join('(%s) %s' % (t, x) for t, x in trig) + '.\n')


def _census():
    pairs = copy_pairs()
    return ('\n' + HC + ' (a) PLACE-papers phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md carries b651’s `(R261)`(3)(d) line (:534, the '
            'ceiling on :355) that SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md does not, the two copies diverging after b558 (the unversioned copy’s '
            'last commit before b651’s). (b) Every document with an unversioned and a versioned copy in PLACE-papers at c740f56, %d by name: %s. '
            '**`W-ORD-ONE-COPY`** -- the question of the one copy of record for each; **Trigger:** “b672 the Correspondence generator”, the '
            'generator to write to the copy of record alone. (c) The b670 mirror’s MANIFEST version cells, as cell-refresh items: v0.4.0 for '
            'BALANCE_AND_POSITIVITY_v0_9_5.md, v0.2 for ENUMERA_v1_6.md and “-” for THE_KEYSTONE_CENSUS_v0_6.md, _v0_7.md and _v0_7_1.md.\n' % (
                len(pairs), '; '.join('%s (%s)' % (p, ', '.join(v)) for p, v in pairs)))


def rules_bank():
    line_, trig = sequence_parts()
    L = ['b671 -- THE RULES OF (R281)(2), BANKED VERBATIM FROM THE RULING (relay data/b671_ferry.txt) (%s): rows are rules, each with its source.' % K.DATE, '',
         'ROW 1 -- THE SEQUENCE LINE. Source: (R281)(2), the author`s words verbatim. Text:', '"%s"' % line_,
         'Entered on OPEN_TRAILS beneath the research order after b668 (:14294); each later reading act prints the five triggers against it.', '']
    for i, (t, x) in enumerate(trig, 2):
        L += ['ROW %d -- TRIGGER %s. Source: (R281)(2), verbatim. Text:' % (i, t), '"%s"' % x, '']
    return L


def c1(*a):
    dry = 'dry' in a
    if not dry:
        put_txt('b671_rules.txt', rules_bank())
    land([('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', HS, _sequence()), ('OPEN_TRAILS.md', HC, _census()),
          ('OPEN_TRAILS.md', HB, _bessel_order())], 'b671_record_lines.json', 'c1',
         entry=K.B670_ENTRY, check=[('FINDINGS.md', K.B670_ENTRY, '## The reading at b670'), ('OPEN_TRAILS.md', K.B670_TRAIL, '### b670'),
                                    ('OPEN_TRAILS.md', K.RESEARCH_ORDER, 'THE RESEARCH ORDER AFTER b668')], dry=dry)


# ================================================================================ THE AUTHOR'S ANSWERS (b670's route, carried with its repairs)
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID


def _session_rows():
    start = None
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8', errors='replace'), 1):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if start is None and K.ANCHOR in raw and o.get('type') == 'user' and not o.get('isCompactSummary'):
            start = i
        if start is not None:
            yield i, o, start


def answers(*a):
    """data/b671_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; every word of the author
    delivered between BEGIN and END after the ruling (pastes unwrapped from the host's wrapper), and the author's plain messages, verbatim."""
    calls, results, words, plain_, start = [], {}, [], [], None
    for i, o, st in _session_rows():
        start = st
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
                    plain_.append((i, t.strip()))
        texts = [re.sub(r'(?s)^\s*<pasted_content[^>]*>\s*(.*?)\s*</pasted_content[^>]*>\s*$', r'\1', t or '') for t in texts]
        ask = set(x[1] for x in calls)
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((i, c['id'], c['input'], o.get('timestamp')))
                ask.add(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask:
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')
                results[c.get('tool_use_id')] = (i, t, o.get('timestamp'))
                texts.append(t)
        for t in texts:
            for mm in re.finditer(r'(?s)(?:\A\s*|=")BEGIN\s*(.*?)\s*END(?=\s*\Z|")', t or ''):
                if K.ANCHOR not in mm.group(1) and 'RULING (' not in mm.group(1)[:20]:
                    words.append((i, mm.group(1)))
    if start is None:
        sys.exit('### THE ANCHOR IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    L, n = [], 0
    for i, cid, inp, ts in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d, %s)' % (cid, K.SESSION_ID, i, ts))
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
        W += ['### THE AUTHOR`S WORD (transcript line %d), BEGIN to END, verbatim:' % i] + w.replace('\r', '').split(NL) + ['']
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %d), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b671 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b671_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b671_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 2: THE PLAN, (R281)(3)-(5), IN THE b663 FORM WITH THE CONSUMERS SECTION
def _src(path, ln):
    """a source line, printed beside the figure it gives."""
    l = rd(os.path.join(ROOT, *path.split('/'))).split(NL)
    return l[ln - 1].strip() if 0 < ln <= len(l) else '### LINE ABSENT'


PLAN_W = '1e-24'            # ### w, fixed from the tolerance below with its margin (section 1); no number of the narrowing computed here
PLAN_DEPTH = 40             # ### ceil(log2(1e-12 / 1e-24)) = 40 halvings from b667's half-width to w


def plan(*a):
    """data/b671_narrow_plan.txt: rows are plan items, each figure beside its source line; arithmetic on banked figures only."""
    h4 = 'data/b667_h4_reading.txt'
    cert = 'tools/b667_epstein_certify.py'
    L = ['b671 -- COMPONENT 2, (R281)(3)-(5): THE PLAN FOR THE NARROWING, IN THE b663 FORM WITH THE CONSUMERS SECTION (%s)' % utc(), '',
         '### rows are plan items; every figure stands beside the line it is read from; nothing in this plan is a number of the narrowing -- the',
         '### only arithmetic is on figures b667 banked. Raised as the one prompt of (R281)(3) before any number.', '',
         '== 1. THE CONSUMER AND ITS TOLERANCE, NAMED BEFORE w IS FIXED ((R281)(3), (6) H4; N2)',
         '  the consumer: tools/b667_epstein_map_balls.py, its reader q0_list (:146-:155) taking each ON row as arb(im, h) and each OFF row as the',
         '  ball strings [re +/- h], [im +/- h]; run once on the narrowed list by a copy whose one changed line is the bank`s name (Component 4).',
         '  the tolerance, %s :13-:14: "%s %s"' % (h4, _src(h4, 13)[4:], _src(h4, 14)[4:]),
         '  the transfer from a point`s half-width to that relative width, %s :9-:10: "%s %s"' % (h4, _src(h4, 9)[4:], _src(h4, 10)[4:]),
         '  arithmetic: a half-width of 1e-12 gave a relative radius of 6.1e-9 in the dominant orbit`s scores, a transfer of 6.1e3; the tolerance',
         '  near 1e-18 in relative width asks a half-width at or below 1e-18 / 6.1e3 = 1.6e-22.',
         '  ### w = %s: two decimal orders below 1.6e-22 (1.6e-24), rounded down to the power of ten. Read on the tolerance figure`s own scale,' % PLAN_W,
         '  ### w is ten thousand times below 1e-18 / 100 = 1e-20, so H4`s "at or below that tolerance by two decimal orders" holds on either',
         '  ### scale. A reading for the author: the transfer of 6.1e3 is the b667 figure for the dominant orbit and is taken for every point.',
         '  depth: from b667`s half-width 1e-12 to w, %d halvings (2^40 = 1.1e12).' % PLAN_DEPTH, '',
         '== 2. Λ_Q IS REAL ON σ = ½ (N2: derived before any sign is read)',
         '  Λ_Q(s) = (2π/√23)^{−s} Γ(s) Z_Q(s), the record`s completed function (%s :219-:220 logg_q, :227-:229 lam_q).' % cert,
         '  (i) the functional equation Λ_Q(s) = Λ_Q(1 − s): Epstein`s, for the positive definite form Q0 = x² + xy + 6y² of discriminant −23;',
         '      its check at five points, data/b667_certify_run2.txt :22-:28: "%s".' % _src('data/b667_certify_run2.txt', 28),
         '  (ii) real coefficients: Z_Q(s) = Σ′ Q(x, y)^{−s} over integer pairs, each Q(x, y) a positive integer, so Z_Q(conj s) = conj Z_Q(s); the',
         '      factor (2π/√23)^{−s} has a positive base and Γ(conj s) = conj Γ(s), so Λ_Q(conj s) = conj Λ_Q(s).',
         '  (iii) on the line s = ½ + it: conj s = ½ − it = 1 − s, so Λ_Q(s) = Λ_Q(1 − s) = Λ_Q(conj s) = conj Λ_Q(s), and Λ_Q(½ + it) is real.',
         '  its trace in b667`s print: at s = 0.5 + 140i the imaginary part is a ball about zero, data/b667_certify_run2.txt :26 ("[+/- 3.80e-128]j").',
         '  in the run: each endpoint value`s imaginary ball is printed and must contain 0 (a check of the line, not a sign); the sign is the real',
         '  ball`s, read only when the real ball excludes 0.', '',
         '== 3. (M-on), ITS FIGURES ((R281)(4))',
         '  start: each ON row`s b667 square [im ± 1e-12] on σ = ½ (b667 count 1 in the square), its t-interval [im − 1e-12, im + 1e-12].',
         '  the endpoints: exact points ½ + i t_e (decimal strings at 40 digits); Λ_Q(½ + i t_e) by lam_q`s route at 200 bits, then the 400 rung',
         '  where the real ball contains 0, with the Bessel factor`s own 600-bit rung as b667 fixed it (%s :45-:50, (3a)-(3b)).' % cert,
         '  certified: both endpoint balls exclude 0 with opposite signs -- a zero of Λ_Q on the line in the interval, and by the square`s count 1',
         '  the square`s one zero; σ carried as the rational ½.',
         '  narrowed: the midpoint`s sign read the same way and the half with the sign change kept, to half-width w (depth %d); a midpoint whose' % PLAN_DEPTH,
         '  ball contains 0 at every rung prints UNRESOLVED-AT-DEPTH d and the point keeps its last certified interval.',
         '  where the starting endpoints do not show opposite signs: NO SIGN CHANGE printed, the point keeps its b667 square, UNRESOLVED stands.',
         '  price: about 42 evaluations a point, 146 points, b667`s median 0.13 s an evaluation (its ON rows: 130 s over a median 1024 segments)',
         '  -- about 6100 evaluations, near a quarter hour in one process.', '',
         '== 4. (M-off), ITS FIGURES ((R281)(4))',
         '  start: each OFF row`s b667 square [re ± 1e-12] × [im ± 1e-12] at count 1.',
         '  each depth: the square split at its centre into four quarters, each quarter`s count by b667`s segment form. square_count',
         '  (%s :301-:315) holds its segments per side as the module constant SQ_SEG = 4 (:61) and its depth as DEPTH_SQ = 16 (:65), so it' % cert,
         '  is CARRIED into the b671 script with both lifted to the head -- SEGS_PER_SIDE = 16, the starting segments per side, the width the',
         '  enclosure test consumes (the navigator`s note, (2)); DOUBLINGS_MAX = 16, the printed ceiling -- and its diff against b667`s banked',
         '  (data/b671_narrow_carry_diff.txt), no computation line changed. segment (:258-:281) takes its depth as an argument and halves a',
         '  segment whose enclosure is not accepted (its ball includes 0, or its radius exceeds half its midpoint`s modulus), each halving a',
         '  doubling of that segment`s count; it is carried beside square_count with one recording line added (the depth and the segment`s two',
         '  ends appended to the quarter`s log), every doubling printed with its depth and point; edge_arg, zq and the rungs imported unedited.',
         '  at the ceiling: the 400 rung once, then UNRESOLVED-AT-DEPTH printed, as b667. (3a)-(3d) in force through zq and its Bessel rungs.',
         '  the quarter at count 1 kept, the three at 0 printed.',
         '  a split line meeting the zero (a quarter whose count cannot be read): the depth printed and both split lines offset by an eighth of the',
         '  half-width, printed, once; unread again: UNRESOLVED-AT-DEPTH d, the point keeping its last square at count 1.',
         '  to half-width w (depth %d).' % PLAN_DEPTH,
         '  price, re-read on SEGS_PER_SIDE = 16: b667`s OFF squares started at 4 a side (16 on the contour) and accepted a median 1314 segments,',
         '  so the adaptive halving, not the start, set their cost; starting at 64 on the contour moves a quarter`s count by at most the 48 added',
         '  starting segments (under 4 per cent of 1314). 4 counts a depth, 40 depths, 17 points = about 2720 counts at b667`s median 100 s a',
         '  count -- about 75 process-hours, near ten hours on b667`s 8 processes (%s :70, the 2560 MB hold, 25 MB a process).' % cert,
         '  ### A READING, ON THE NAVIGATOR`S NOTE ON THE PRICING: the median of 1314 segments is not the segment count`s doing but the (3b)',
         '  ### remedy`s -- its ball is 131-507 times r·|Z_Q`| (data/b667_epstein_plan.txt :236: "%s"),' % _src('data/b667_epstein_plan.txt', 236)[:110],
         '  ### so the enclosure accepts a segment when its half-length r is below the distance to the zero by that factor, a ratio that does not',
         '  ### change as the square shrinks; the price stands. Entered on OPEN_TRAILS as `W-ORD-BESSEL-BOUND-TIGHTEN` (Component 1`s lines),',
         '  ### trigger "the next act that counts on Q0 after b671".', '',
         '  THE ORDER OF RUNS: C1, C2, the 146 on-line points, then the 17 off-line points.', '',
         '== 5. THE CONTROLS, CONCRETE ((R281)(5), the author`s word on the Hardy function)',
         '  (C1) ζ`s lowest three zeros by (M-on) on Λ(s) = π^{−s/2} Γ(s/2) ζ(s) (%s :223-:224 logg_z; real on the line by the same steps:' % cert,
         '       Λ(s) = Λ(1 − s) and real coefficients), each start interval taken from acb.zeta_zero(n)`s ball (n = 1, 2, 3), widened to ± 1e-12',
         '       about the ball`s midpoint and printed, narrowed to w, each final interval printed with the same call`s ball inside it; no',
         '       ordinate typed into any script or bank (the navigator`s note, (1); data/b671_defects.txt (c)) -- python-flint 0.9.0`s wrapped',
         '       calls acb.zeta, acb.lgamma and acb.zeta_zero; no Hardy function.',
         '  (C2) planted: ON row idx 0`s t-interval shifted by 10 · 1e-12 before (M-on), the endpoint signs printing NO SIGN CHANGE; OFF row',
         '       idx 0`s square (qE0, the dominant) shifted by 1e-9 in σ before (M-off), its count printing 0.',
         '  (C3) none new: b667`s region count N(R) = 180 (data/b667_epstein_counts.txt) stands as the completeness certificate.',
         '  C1 and C2 run and printed before any Q0 point (N3).', '',
         '== 6. THE ORDER AND THE HOST',
         '  one script, tools/b671_narrow.py, by the Write tool, w, the precisions, the rungs, the shifts, the depth, SEGS_PER_SIDE and',
         '  DOUBLINGS_MAX as constants at its head, b667`s square_count and segment carried in it (their diff banked), everything else imported,',
         '  read back whole; C1, C2, the ON points, the OFF points; detached, watched by one foreground check, the host`s low printed; no lean.',
         '  two runs: the first C1, C2 and the 146 on-line points (within the hour), banked and committed before the second starts; the second',
         '  the 17 off-line points, about ten hours detached on 8 processes under the hold with the single watcher, the host`s low printed when',
         '  it fires -- so a reap of the long run loses nothing banked (the navigator`s note on the pricing).', '',
         '== 7. THE CONSUMERS SECTION ((R278)(3), standing): each bank the act writes, its consumers, each consumer`s input tolerance',
         '  data/b671_epstein_zeros_narrowed.json.gz (rows are points: kind, idx, re, im, h, count, as b667`s rows, so the map`s reader reads it',
         '    unchanged) -- consumers: the map copy (tolerance: half-width at or below 1.6e-22, section 1); the kernel item for P1 and P2',
         '    (OPEN_TRAILS :14266, its data the balls); the suite (read_square_row). Both hashes in data/b671_epstein_zeros_narrowed_hashes.txt.',
         '  data/b671_narrow_log.txt (.json) (rows are points with their depth, reading and, ON, the two endpoint signs) -- consumers: the',
         '    landing`s H1, the suite (read_narrow_row); tolerance: every row read, none NOT READ.',
         '  data/b671_epstein_control_narrowed.txt (.json) -- consumers: H3, the dated line beneath data/b663_epstein_control.txt; tolerance: the',
         '    map`s own print, j₀ and the zero side with their balls.',
         '  data/b671_map_narrowed_diff.txt -- consumer: N4; tolerance: no computation line changed.',
         '  data/b671_narrow_carry_diff.txt (the carried square_count and segment against b667`s) -- consumer: the suite; tolerance: the two',
         '    constants lifted and the one recording line, no computation line changed.', '',
         '== 8. THE HYPOTHESES AS THE RUN READS THEM ((R281)(6))',
         '  H1 the log`s rows: every ON NARROWED with opposite endpoint signs, every OFF NARROWED at count 1 at every depth, UNRESOLVED counted.',
         '  H2 C1`s three intervals each containing acb.zeta_zero`s ordinate; C2 printing NO SIGN CHANGE and count 0.',
         '  H3 the map on the narrowed list: hQtie certified at every j to the control`s j, j₀ = 38, the zero side below zero -- else the finding.',
         '  H4 section 1 printed before w was fixed, w at or below the tolerance by two decimal orders.', '',
         '== 9. WHAT STOPS THE ACT AT THIS PLAN',
         '  the author`s word on the plan; no number of the narrowing is computed before it.']
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('b671_narrow_plan.txt', L)
    print('  data/b671_narrow_plan.txt %d lines' % len(L))


# ================================================================================ THE LATE ROUTES (b670's, carried; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
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


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    L = ['b671 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d.**' % (len(rows), len(hits), len(lean))]
    put_txt('b671_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b671_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


def kernels(*a):
    import b641_record as R41
    put_json('b671_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


DEFECT_ROW = re.compile(r'^    \(([a-z])\) ')


def _defect_short():
    out = []
    L = rdn('b671_defects.txt').split(NL)
    for i, l in enumerate(L):
        if DEFECT_ROW.match(l):
            j = i + 1
            while j < len(L) and L[j].startswith('    ') and not DEFECT_ROW.match(L[j]) and not L[j].startswith('    ###'):
                j += 1
            m = re.match(r'^\(([a-z])\) (.*?)\.(?= |$)', ' '.join(x.strip() for x in L[i:j]))
            if m:
                out.append(m.group(0)[:-1])
    return out


def defects(*a):
    t = rdn('b671_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b671_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b671_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b671_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b671_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands|'
                          r'mirror.*)\.(txt|json|md)$')


SHARED_APPENDED = ('data/b663_epstein_control.txt', 'data/b670_methods.txt')   # ### the dated lines of (R281)(7): named by this root, so shared


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b671_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)]
                  + list(SHARED_APPENDED))


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if not b_.endswith('.gz') and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b671_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b671'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b671_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith('.gz')][0]
    with tempfile.TemporaryDirectory(prefix='b671_ra_') as tmp:
        cp = os.path.join(tmp, os.path.basename(bank_))
        b_ = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b_[0] ^= 0x01
        open(cp, 'wb').write(bytes(b_))
        items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
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
    L = ['b671 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b671_root_arm.txt', L)
    put_json('b671_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b671 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b671_table_final.txt', L)
    put_json('b671_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b671_registration_2026-10-14.txt'
FACE = os.path.join(D, 'b671_registration_2026-10-14.txt')


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b671_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b671_regspec.py')], 'b671_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b671_satisfiable.json', '--emit', 'b671'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b671_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b671_census_stepzero.txt'), ('b327_faces_census.py', 'b671_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b671_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b671'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b671_reg_gate.txt', 'data/b671_reg_termscan.txt', 'data/b671_regspec_run.txt', 'data/audit_b671_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE PROGRESS TABLE (the navigator's answer on progress)
RUN2_LOG = os.path.join(K.SP, 'b671_run2.log')
RUN2_ERR = os.path.join(K.SP, 'b671_run2.err')
RUN2_START = '2026-10-14T23:05:28Z'
_DEPTH = re.compile(r'^  OFF (\d+) depth (\d+) : half-width (\S+) ; quarters \[([^\]]*)\] ; segments \[([^\]]*)\] ; doublings \[([^\]]*)\]')
_DBL = re.compile(r'^      doubling at depth (\d+) :')


def _free_mb():
    r = subprocess.run(['powershell', '-NoProfile', '-Command', '[int]((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1024)'],
                       capture_output=True, text=True)
    return (r.stdout or '').strip() or 'UNREAD'


def progress(*a):
    """a read of run 2's own records, no process touched: rows are points. What run 2 writes, and when: the log (scratchpad
    b671_run2.log) one line per point as it lands; data/b671_narrow_run2_points.jsonl one row per point as it lands, carrying its depth
    lines; narrow_off writes nothing while a point runs (its depth lines held in the worker until the point returns); no depth line
    carries a time; a depth line's segments and doublings are per quarter, summed over the quarter's four sides."""
    at = utc()
    free = _free_mb()
    log = rd(RUN2_LOG).split(NL)
    err = rd(RUN2_ERR)
    rows = [json.loads(l) for l in rd(os.path.join(D, 'b671_narrow_run2_points.jsonl')).split(NL) if l.strip()]
    banked = dict((r['idx'], r) for r in rows)
    q0 = dict((r['idx'], r) for r in json.loads(gzip.decompress(open(os.path.join(D, K.Q0_CERT), 'rb').read()).decode('utf-8'))['rows']
              if r['kind'] == 'OFF')
    src = rd(os.path.join(T, 'b671_narrow.py'))
    body = src[src.index('def narrow_off('):src.index('def task_off(')]
    writes = [w for w in ('print(', 'say(', '.write(', 'flush') if w in body]
    L = ['b671 -- RUN 2`S PROGRESS, READ FROM ITS OWN RECORDS (rows are points) (%s) ; host free %s MB ; the hold %d MB' % (at, free, K.HOLD), '',
         '### the navigator`s answer on progress, a read with no change to the run and no process touched. The records: the log (%d lines, '
         'one per landed point after a 3-line head), stderr (%d characters), data/b671_narrow_run2_points.jsonl (%d rows, one per landed point, '
         'its depth lines inside). narrow_off`s body (tools/b671_narrow.py) writes while a point runs: %s.' % (
             len([l for l in log if l.strip()]), len(err), len(rows), writes or 'NOTHING -- no print, say, write or flush'),
         '### so for a point still running, its last completed depth, that line`s time, its segments and doublings are NOT IN RUN 2`S RECORDS '
         '(held in the worker until it returns), and no projection is formed from them. No depth line carries a time, banked or running: the '
         'time of a line and the seconds of the last three depths are NOT RECORDED for any point; a banked point`s whole time is its row`s '
         'seconds, printed with seconds per depth as that whole over its depth lines (a depth read again after an offset counted twice) -- a '
         'mean, NOT the last three depths and not a projection.',
         '### segments and doublings are a quarter`s, summed over its four sides (CERT._stats in square_count, one st per quarter); per side is '
         'NOT RECORDED. A side past 1,024 segments can be excluded only where the quarter`s whole is at or below 1,024.', '']
    L.append('  %-6s %-24s %-22s %-6s %-26s %-14s %-22s %s' % ('point', 't (b667`s centre)', 'reading', 'depth', 'last accepted quarter: segs, dbls',
                                                             'seconds', 's / depth', 'a side past 1,024 segments'))
    for i in sorted(q0):
        t = q0[i]['im'][:22]
        if i not in banked:
            el = int(time.time() - calendar.timegm(time.strptime(RUN2_START, '%Y-%m-%dT%H:%M:%SZ')))
            L.append('  OFF %-2d %-24s %-22s %-6s %-26s %-14s %-22s %s' % (i, t, 'RUNNING', 'NOT IN RECORDS', 'NOT IN RECORDS',
                                                                          'running %d s' % el, 'NOT IN RECORDS', 'NOT IN RECORDS'))
            continue
        r = banked[i]
        ds = [m for m in (_DEPTH.match(l) for l in r['lines']) if m]
        last = None
        for m in ds:
            qs = [x.strip() for x in m.group(4).split(',')]
            if qs.count('1') == 1 and all(x in ('0', '1') for x in qs):
                k = qs.index('1')
                last = (int(m.group(2)), int(m.group(5).split(',')[k]), int(m.group(6).split(',')[k]))
        tot = [int(x) for m in ds for x in m.group(5).split(',')]
        first = next((int(m.group(2)) for m in ds if max(int(x) for x in m.group(5).split(',')) > 1024), None)
        past = 'NO (every quarter`s whole at or below 1,024)' if tot and max(tot) <= 1024 else (
            'NOT DECIDABLE (per side NOT RECORDED): a quarter`s whole first past 1,024 at narrowing depth %d, its largest %d' % (
                first, max(tot)) if tot else 'NO DEPTH LINE')
        L.append('  OFF %-2d %-24s %-22s %-6d %-26s %-14d %-22s %s' % (
            i, t, r['reading'], r['depth'], ('depth %d : %d, %d' % last) if last else 'NONE ACCEPTED', r['seconds'],
            '%.0f (mean over %d lines)' % (r['seconds'] / max(1, len(ds)), len(ds)), past))
    L += ['', '### ### **BANKED %d OF %d (NARROWED %d, UNRESOLVED-AT-DEPTH %d) ; RUNNING %d, THEIR FIGURES NOT IN RUN 2`S RECORDS ; host free %s MB '
          'at %s.**' % (len(banked), len(q0), sum(1 for r in rows if r['reading'] == 'NARROWED'),
                        sum(1 for r in rows if r['reading'] != 'NARROWED'), len(q0) - len(banked), free, at)]
    put_txt('b671_run2_progress.txt', L)
    print(NL.join(L))


ROUTES = {'c1': c1, 'answers': answers, 'plan': plan, 'commands': commands, 'kernels': kernels, 'defects': defects, 'root': root,
          'root_arm': root_arm, 'table_final': table_final, 'gatebanks': gatebanks, 'progress': progress}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b671_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
