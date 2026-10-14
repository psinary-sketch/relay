# -*- coding: utf-8 -*-
"""b670_record.py -- THE ACT'S RECORD TOOL, b670 under (R280).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b670's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b669_record.py (the helpers, the landing, the readers, the answers); new here: the weight line of (R280)(1),
### and at their components the ten-acts banks, the four readings, the methods table and the items. No kernel byte is written by any route.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b670_record.py <route> [dry]`.
"""
import collections
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
import b670_worklist as K          # noqa: E402

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
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b670_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b670_findings.json': dict(entry_line=99999, title='stand-in'),
        'b670_trail.json': dict(line=99999),
        'b670_act_root.json': dict(root='0' * 64, previous='613c17a9' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
        'b670_mirror.json': dict(zip='stand-in', manifest_md5='0' * 32),
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


def _ws(s):
    return ' '.join(s.split())


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b670's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b670_scanfile_%s.md' % tag)
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
    """a scores row: key N1..N5 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text) -- the whole verdict, not its first
    word (b656's defect (e))."""
    if not re.match(r'^(N[1-5]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


def read_act_row(r):
    """a row of data/b670_ten_acts.json: an act b660-b669 and its cells, each cell with its cite (a closing line, a bank name or a defect
    letter); returns (act, cells); raises on a row of another shape or a cell without a cite."""
    if not isinstance(r, dict) or not re.match(r'^b66\d$', r.get('act') or '') or not isinstance(r.get('cells'), dict) or not r['cells']:
        raise ValueError('act row of another shape: %r' % (r.get('act') if isinstance(r, dict) else r,))
    for k, c in r['cells'].items():
        if not isinstance(c, dict) or 'value' not in c or not c.get('cite'):
            raise ValueError('a cell without its cite: %s %s' % (r['act'], k))
    return r['act'], r['cells']


READINGS = ('READY', 'NOT READY', 'NOT YET USED TWICE')


def read_method_row(r):
    """a row of data/b670_methods.json: a method, the acts that used it, its banks, its recorded failure modes and its reading, each read from
    the three cells alone (relay data/b670_rules.txt row 2); raises on a row of another shape or a reading the cells do not give."""
    if not isinstance(r, dict) or not r.get('method') or not isinstance(r.get('acts'), list) or not isinstance(r.get('banks'), list) \
            or not isinstance(r.get('defects'), list) or r.get('reading') not in READINGS:
        raise ValueError('method row of another shape: %r' % (r.get('method') if isinstance(r, dict) else r,))
    want = 'NOT YET USED TWICE' if len(r['acts']) < 2 else ('READY' if r['banks'] and r['defects'] else 'NOT READY')
    if r['reading'] != want:
        raise ValueError('a reading the cells do not give: %s reads %s, the cells give %s' % (r['method'], r['reading'], want))
    return r['method'], r['reading']


def read_order_row(r):
    """a row of data/b670_work_orders.json: an order's name, its line, its entry act, its trigger, its status and its age in acts."""
    if not isinstance(r, dict) or not r.get('name') or not isinstance(r.get('line'), int) or not isinstance(r.get('age'), int) or 'status' not in r:
        raise ValueError('order row of another shape: %r' % (r.get('name') if isinstance(r, dict) else r,))
    return r['name'], r['status'], r['age']


READERS = ['read_score_row', 'read_head', 'read_act_row', 'read_method_row', 'read_order_row']


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R280)(1)
WH = ('*Appended 2026-10-14 by b670 to b669’s entry (:8707), under `(R280)`(1) -- b669 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b669_closing.txt), ITS CONVERSE OPEN ON ITS OWN BRANCH:*')


def _weight():
    return ('\n' + WH + ' liCoeffCfg, the Li coefficient over any zero configuration, with ζ’s LiCoeff its instance by rfl (liCoeff_eq_liCoeffCfg, '
            'H1), its summability from the configuration’s count field (HCount) and the generic forward half; the forward half at χ, '
            'grh_chi_imp_li_nonneg_chi, DERIVES at the standard three, its proof reaching 92 kernel declarations with none ζ-naming while the walk’s '
            'control on ζ’s own forward half finds one (H2); merged alone at SIDE-explicit-formula 115abfe, tag v0.31; the converse at χ stated and '
            'compiling with its proof open (H3) on branch chi-li-b669 at b804bf2, unmerged, no sorry on main -- V2, V3 and the two geometric-sum '
            'steps of V4’s Cesàro proof DERIVES on that branch, V4 the power-sum lemma open at Schema/LiConverseCfg.lean :129 and V5 the remainder '
            'bound open at :139, V5’s non-landing declared on the face against the route answer’s word; route (P) chosen, route (B) priced at the '
            'order of ξ_χ absent from Mathlib at de5ce8a9, every absence on a tightened search printed (H4); W-ORD-LI-CONVERSE-NATIVE named in the '
            'plan with trigger “S5 DERIVES”; no iff composed, no ceiling successor drafted; the (R279)(6) repair at FINDINGS :8703, b668’s weight '
            'at :8705, the entry at :8707, the trail at OPEN_TRAILS :14324; relay e527a09e, PLACE-papers 165a645, root 613c17a9…; the suite 82 of '
            '82 before and after the push; four defects, (a) the navigator’s (a bank’s unit named from a remembered shape). Nothing deposited.\n')


def c1(*a):
    land([('FINDINGS.md', WH, _weight())], 'b670_record_lines.json', 'c1', entry=K.B669_ENTRY,
         check=[('FINDINGS.md', K.B669_ENTRY, '## The Li coefficient over the configuration'), ('OPEN_TRAILS.md', K.B669_TRAIL, '### b669')],
         dry='dry' in a)


# ================================================================================ THE AUTHOR'S ANSWERS (b669's route, carried)
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
    """data/b670_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
    delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim."""
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
        # ### b670's repair: a paste delivered inside <pasted_content ...> ... </pasted_content ...> is read as its inner text (the wrapper
        # ### the host adds), so its BEGIN ... END is a whole pasted text
        texts = [re.sub(r'(?s)^\s*<pasted_content[^>]*>\s*(.*?)\s*</pasted_content[^>]*>\s*$', r'\1', t or '') for t in texts]
        ask = set(x[1] for x in calls)
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((i, c['id'], c['input'], o.get('timestamp')))
                ask.add(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask:
                # ### b670's repair: only the results of the seat's prompts are read for answer fields; another tool's print is not a word
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')
                results[c.get('tool_use_id')] = (i, t, o.get('timestamp'))
                texts.append(t)
        for t in texts:
            # ### a word is a whole pasted text or a whole answer field ("question"="BEGIN ... END"), never BEGIN and END inside other prose
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
    head = ['### b670 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b670_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b670_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ PART B: THE TEN ACTS, THE READINGS, THE METHODS, THE ITEMS
# ### COMPONENT 2, (R280)(2): rows are acts; each cell a value and its cite (closing, line, a needle the line must carry). The defects are not
# ### typed here: they are read from each closing's defect section by their lettered heads, the seat and the kind in the head's own words, and
# ### a bank's own cross-reference to an earlier kind (b653 (b)'s kind, b663's lesson, b505's trap ...) read from the defect's body.
def _cl(a):
    return 'data/b%s_closing.txt' % a[1:]


C = lambda a, ln, needle, value: dict(value=value, cite='%s :%d' % (_cl(a), ln), needle=needle)   # noqa: E731
TEN = {
    'b660': dict(lane=C('b660', 3, 'LANE THREE, ACT EIGHTY-SEVEN, THE READING ACT', 'LANE THREE, THE READING ACT'),
                 landed=C('b660', 4, 'NO BUILD, NO DEPOSIT, NO SEAL', 'NONE: no build, no deposit, no seal'),
                 hyp=C('b660', 1, 'b660 closed', 'NONE PUT: the closing carries no H row (29 lines)'),
                 orders=C('b660', 27, 'W-ORD-CITATION-CHECK', 'entered 0, discharged 0; W-ORD-CITATION-CHECK carried to b662 as a gate step')),
    'b661': dict(lane=C('b661', 3, 'LANE TWO, ACT EIGHTY-EIGHT, THE RESEARCH ACT', 'LANE TWO, THE RESEARCH ACT'),
                 landed=C('b661', 158, 'no kernel main moved', 'NONE: no kernel main moved, no merge, no tag; the map banked (data/b661_detection_map.txt)'),
                 hyp=C('b661', 37,'(H2) HELD, VACUOUS (H3) NOT SCORABLE', 'H1-H4: HELD 3 (H2 VACUOUS), REFUTED 0, NOT SCORABLE 1 (H3)'),
                 orders=C('b661', 163, 'W-ORD-CLOSE-PAIR-BENCH', 'entered 0, discharged 0; W-ORD-CLOSE-PAIR-BENCH named as the map`s reader')),
    'b662': dict(lane=C('b662', 3, 'LANE THREE, ACT EIGHTY-NINE, THE RE-CUT ACT', 'LANE THREE, THE RE-CUT ACT'),
                 landed=C('b662', 36, 'merged dd54a61 ; tag v0.4.2', 'SIDE-carrier-spec cut, merged dd54a61, tag v0.4.2'),
                 hyp=C('b662', 24, 'H1 HELD', 'H1-H4: HELD 4, REFUTED 0 (:24-:27)'),
                 orders=C('b662', 44, 'W-ORD-E2-SEPARATION :14132', 'entered 1 (W-ORD-E2-SEPARATION, OPEN_TRAILS :14132); the citation check acted (:14136)')),
    'b663': dict(lane=C('b663', 3, 'LANE TWO, ACT NINETY, THE RESEARCH ACT', 'LANE TWO, THE RESEARCH ACT'),
                 landed=C('b663', 47, 'the merge d00ab16 tag v0.29', 'the Q0 instance (SIDEExplicitFormula/Schema/EpsteinQ0.lean), merged d00ab16, tag v0.29'),
                 hyp=C('b663', 58, '(H1) HELD', 'H1-H4: HELD 4 (H3, H4 ON B1), REFUTED 0 (:58-:61; the first print`s H2 REFUTED a predicate defect, (i))'),
                 orders=C('b663', 44, 'W-ORD-EPSTEIN-CERTIFY OPEN_TRAILS :14158 ; W-ORD-FT-FIRST-ORDER :14162',
                          'entered 2 (W-ORD-EPSTEIN-CERTIFY :14158, W-ORD-FT-FIRST-ORDER :14162), each read with its trigger met (:224-:226)')),
    'b664': dict(lane=C('b664', 3, 'LANE THREE, ACT NINETY-ONE, THE RE-CUT ACT', 'LANE THREE, THE RE-CUT ACT'),
                 landed=C('b664', 29, 'merged 78bbcff ; tag v0.1.1', 'SIDE-effects cut, merged 78bbcff, tag v0.1.1'),
                 hyp=C('b664', 45, '(N1) HELD', 'NONE PUT: the scores are N1-N5 and S1-S3 alone'),
                 orders=C('b664', 40, 'the orders placed OPEN_TRAILS :14186, :14188', 'placed 2 (OPEN_TRAILS :14186, :14188); the file-constant rule :14190')),
    'b665': dict(lane=C('b665', 3, 'LANE TWO, ACT NINETY-TWO, THE RESEARCH ACT', 'LANE TWO, THE RESEARCH ACT'),
                 landed=C('b665', 36, 'MERGED 02bc85d ; TAG v0.30', 'the Keiper finite-n equality and the transform bound DERIVES, merged 02bc85d, tag v0.30'),
                 hyp=C('b665', 55, '(H1) HELD', 'H1-H3: HELD 3, REFUTED 0 (:55-:57)'),
                 orders=C('b665', 34, 'W-ORD-FT-FIRST-ORDER DISCHARGED at OPEN_TRAILS :14216', 'discharged 1 (W-ORD-FT-FIRST-ORDER, OPEN_TRAILS :14216)')),
    'b666': dict(lane=C('b666', 3, 'LANE THREE, ACT NINETY-THREE, THE RE-CUT ACT', 'LANE THREE, THE RE-CUT ACT'),
                 landed=C('b666', 29, 'merged ca04c8c ; tag v0.3.1', 'SIDE-cosmo cut, merged ca04c8c, tag v0.3.1'),
                 hyp=C('b666', 45, '(N1) HELD', 'NONE PUT: the scores are N1-N5 and S1-S3 alone'),
                 orders=C('b666', 40, 'the tie rule OPEN_TRAILS :14238', 'entered 0, discharged 0; the tie rule OPEN_TRAILS :14238')),
    'b667': dict(lane=C('b667', 3, 'LANE TWO, ACT NINETY-FOUR, THE RESEARCH ACT', 'LANE TWO, THE RESEARCH ACT'),
                 landed=C('b667', 216, 'no kernel main moved', 'NONE: no kernel main moved, no merge, no tag'),
                 hyp=C('b667', 42, '(H1)', 'H1-H5: HELD 4 (H1, H2, H3, H5), REFUTED 0, NOT SCORABLE 1 (H4, :52)'),
                 orders=C('b667', 63, ':14264 (W-ORD-EPSTEIN-BALL-WIDTH)', 'discharged 1 (W-ORD-EPSTEIN-CERTIFY`s data half, :14262); entered 2 '
                          '(W-ORD-EPSTEIN-BALL-WIDTH :14264; W-ORD-ROOT-BINARY-BANK :14268, :239); the kernel item :14266')),
    'b668': dict(lane=C('b668', 3, 'LANE THREE, ACT NINETY-FIVE, THE RE-CUT ACT', 'LANE THREE, THE RE-CUT ACT'),
                 landed=C('b668', 32, 'SIDE-grh-transfer merged 6e149db', 'SIDE-grh-transfer cut, merged 6e149db, tag v0.5.1 (the merged tree not the built tree, (c))'),
                 hyp=C('b668', 50, 'HELD', 'NONE PUT: the scores are N1-N5 and S1-S3 alone'),
                 orders=C('b668', 41, 'the research order :14294', 'entered 1 (the research order :14294); the plan form :14290; the mid-act check :14292')),
    'b669': dict(lane=C('b669', 3, 'LANE TWO, ACT NINETY-SIX, THE RESEARCH ACT', 'LANE TWO, THE RESEARCH ACT'),
                 landed=C('b669', 31, 'merged alone at 115abfe4, tag v0.31', 'liCoeffCfg and the forward half at χ, merged 115abfe, tag v0.31; '
                          'the converse on chi-li-b669 at b804bf2, unmerged'),
                 hyp=C('b669', 33, 'H1 HELD ; H2 HELD ; H3 HELD ; H4 HELD', 'H1-H4: HELD 4, REFUTED 0'),
                 orders=C('b669', 172, 'W-ORD-LI-CONVERSE-NATIVE, its trigger "S5 DERIVES"', 'entered 1 (W-ORD-LI-CONVERSE-NATIVE, trigger "S5 DERIVES", '
                          'in the plan`s consumers section)')),
}
XREF = re.compile(r"(b\d{3} \([a-z]\)'s kind|b\d{3}'s (?:kind|lesson|trap)|kind is b\d{3}'s|the navigator's one kind)")
HEAD = re.compile(r"^    \(([a-z]|b\d{3}-late)\) THE (SEAT|NAVIGATOR)'S")


def defect_rows(a):
    """the lettered defects of act a, from its closing's defect section (b660: its defects bank's two rows and its closing's (c))."""
    srcs = [('data/b660_defects.txt', None), (_cl(a), None)] if a == 'b660' else [(_cl(a), None)]
    out = []
    for src, _ in srcs:
        L = rd(os.path.join(ROOT, src)).split(NL)
        heads = [i for i, l in enumerate(L) if HEAD.match(l)]
        for k, i in enumerate(heads):
            j = i + 1
            while j < len(L) and L[j].startswith('    ') and not HEAD.match(L[j]) and not L[j].startswith('    ###'):
                j += 1
            m = HEAD.match(L[i])
            body = ' '.join(x.strip() for x in L[i:j])
            first = (body.split(': ', 1)[1] if ': ' in body else body).split('. ', 1)[0]     # ### the head words: the first sentence after the seat
            out.append(dict(act=a, letter=m.group(1), seat='THE %s`S' % m.group(2), kind=first.strip()[:240], cite='%s :%d' % (src, i + 1),
                            xref=sorted(set(XREF.findall(body)))))
    return out


def ten(*a):
    dry = 'dry' in a
    rows, bad, D_ = [], [], []
    for act in K.ACTS:
        L = rd(os.path.join(ROOT, _cl(act))).split(NL)
        cells = {}
        for k, c in TEN[act].items():
            ln = int(c['cite'].rsplit(':', 1)[1])
            if c['needle'] not in L[ln - 1]:
                bad.append('%s %s %s' % (act, k, c['cite']))
            cells[k] = dict(value=c['value'], cite=c['cite'])
        ds = defect_rows(act)
        D_ += ds
        head = L[0]
        tot = int(re.search(r'(\d+) defects', head).group(1))
        cells['defects'] = dict(value='%d: the seat`s %d, the navigator`s %d%s' % (
            len(ds), sum(d['seat'] == 'THE SEAT`S' for d in ds), sum(d['seat'] == 'THE NAVIGATOR`S' for d in ds),
            '' if len(ds) == tot else ' ### AGAINST THE HEAD LINE`S %d' % tot), cite='%s :1 ; the lettered rows below' % _cl(act))
        rows.append(dict(act=act, cells=cells))
        read_act_row(rows[-1])
    print('  cites read: %d ; needles missing: %s' % (sum(len(TEN[x]) for x in K.ACTS), bad or 'NONE'))
    print('  defects read: %d ; by seat %s' % (len(D_), dict(collections.Counter(d['seat'] for d in D_))))
    if bad:
        sys.exit('### A CELL`S CITE DOES NOT CARRY ITS NEEDLE -- NOTHING WRITTEN')
    T_ = ['b670 -- COMPONENT 2, (R280)(2): THE TEN ACTS b660-b669, READ FROM THEIR CLOSINGS (%s)' % K.DATE, '',
          '### the sources: the ten closings relay data/b660_closing.txt ... data/b669_closing.txt (rows are the closing record`s lines) and b660`s',
          '### defects bank data/b660_defects.txt (its (a), (b); its closing :19 names them). Rows below are acts; each cell is followed by its cite,',
          '### a closing line the record tool re-read for the cell`s needle before writing (tools/b670_record.py `ten`). Defects are counted from the',
          '### lettered rows of each closing`s defect section, set beside its head line`s total; their kinds are in data/b670_defects_by_kind.txt.', '']
    for r in rows:
        T_.append('=== %s' % r['act'])
        for k in ('lane', 'landed', 'hyp', 'defects', 'orders'):
            c = r['cells'][k]
            T_.append('  %-8s %s   [%s]' % (k, c['value'], c['cite']))
        T_.append('')
    land_ = sum(1 for r in rows if not r['cells']['landed']['value'].startswith('NONE'))
    T_ += ['### ### **ACTS 10 ; LANE TWO %d, LANE THREE %d ; ACTS THAT LANDED IN A KERNEL %d ; DEFECTS %d (THE SEAT`S %d, THE NAVIGATOR`S %d).**' % (
        sum('LANE TWO' in r['cells']['lane']['value'] for r in rows), sum('LANE THREE' in r['cells']['lane']['value'] for r in rows), land_,
        len(D_), sum(d['seat'] == 'THE SEAT`S' for d in D_), sum(d['seat'] == 'THE NAVIGATOR`S' for d in D_))]
    K_ = ['b670 -- COMPONENT 2, (R280)(2): THE DEFECTS OF b660-b669 BY KIND, THE KINDS IN THE BANKS` OWN WORDS (%s)' % K.DATE, '',
          '### rows are defects, one per row: act and letter, seat, the kind as the defect`s head words (its first sentence after the seat), its cite',
          '### (closing line), and, where the defect`s own text names an earlier kind, lesson or trap, that phrase verbatim. No kind is supplied by',
          '### this act: a defect whose text names no earlier kind is its own kind, in its own words.', '']
    for d in D_:
        K_.append('  %s (%s) %-16s %s   [%s]%s' % (d['act'], d['letter'], d['seat'], d['kind'], d['cite'],
                                                ('  ### NAMES: ' + ' ; '.join(d['xref'])) if d['xref'] else ''))
    xr = collections.Counter(x for d in D_ for x in d['xref'])
    K_ += ['', '### the kinds the banks themselves name across acts (each phrase as the defect`s text gives it, with its count):']
    K_ += ['  %-34s %d' % (x, n) for x, n in sorted(xr.items())] or ['  NONE']
    K_ += ['', '### ### **DEFECTS %d ; NAMING AN EARLIER KIND, LESSON OR TRAP %d ; OWN KIND (NAMING NONE) %d.**' % (
        len(D_), sum(1 for d in D_ if d['xref']), sum(1 for d in D_ if not d['xref']))]
    if dry:
        print(NL.join(T_[-14:]))
        print(NL.join(K_[5:]))
        return
    put_txt('b670_ten_acts.txt', T_)
    put_json('b670_ten_acts.json', dict(at=utc(), rows=rows, defects=D_))
    put_txt('b670_defects_by_kind.txt', K_)
    print(T_[-1])
    print(K_[-1])


# ### the sweep added to Component 2 by the navigator's answer on the four tabs: every "the author's ... at bNNN" / "as the author set at
# ### bNNN" in the rulings (R270)-(R280), each checked for a bank or ledger line; misses beneath rows 1-3 of data/b670_rules.txt.
SWEEP_PATS = (r"(?i)(?:the author|as the author)[^.;]{0,120}?\bat b\d{3}", r"(?i)author[`'’]s [^.;()]{0,60}?\bof b\d{3}")
SWEEP = [   # ### (ruling's act, a needle of the phrase, FOUND or MISS, the bank line read: (path, line, needle), text supplied or None)
    ('b660', "the author's word at b645", 'MISS', None,
     'THE NAVIGATOR`S, TEXT NOT HELD STANDING (the answer on the two decisions); no b645 bank or ledger line names the bench after the companions (data/b645_author_answers.txt, b645_ferry.txt, b645_closing.txt read: '
     'no "bench"); the lines that carry the bench`s order are b650`s, printed beside and not substituted: data/b650_author_answers.txt :8 '
     '(the author`s word on question 4, (R260)(4)) and OPEN_TRAILS :13848 ("Trigger: the author’s word after the companions’ re-cuts")'),
    ('b661', "W-ORD-CITATION-CHECK a gate step at b662", 'FOUND', (PP + '/OPEN_TRAILS.md', 14104, 'a gate step at b662’s step zero'),
     'the author`s word at b660 (data/b660_author_answers.txt :19); the ledger line OPEN_TRAILS :14104'),
    ('b662', "the author set at b660", 'FOUND', (PP + '/OPEN_TRAILS.md', 14104, 'W-ORD-EPSTEIN-ZQ (:13493) the research act after b661'),
     'the research order Epstein, Keiper, χ-Li: data/b660_author_answers.txt :19 ("Option 1: after b661`s map"); OPEN_TRAILS :14104'),
    ('b670', "the author set at b663", 'MISS', None, 'TEXT SUPPLIED by the navigator`s answer: ROW 1 above'),
    ('b670', "author's criteria of b663", 'MISS', None, 'TEXT SUPPLIED by the navigator`s answer: ROW 2 above'),
]


def sweep(*a):
    dry = 'dry' in a
    hits, out = [], []
    for n in range(660, 671):
        t = ' '.join(rd(os.path.join(D, 'b%d_ferry.txt' % n)).split())
        i = t.find('FERRY')
        r = t[:i] if i > 0 else t
        hs = [m.group(0) for p in SWEEP_PATS for m in re.finditer(p, r)]
        print('  (R%d) in data/b%d_ferry.txt: ruling %d characters ; hits %d' % (n - 390, n, len(r), len(hs)))
        hits += [('b%d' % n, h) for h in hs]
    un = [h for h in hits if not any(s[0] == h[0] and s[1] in h[1] for s in SWEEP)]
    nohit = [s[1] for s in SWEEP if not any(s[0] == h[0] and s[1] in h[1] for h in hits)]
    bad = []
    for act, ph, v, ref, _x in SWEEP:
        if ref and ref[2] not in rd(ref[0]).split(NL)[ref[1] - 1]:
            bad.append(ph)
    print('  hits %d ; entries %d ; hits without an entry %s ; entries without a hit %s ; bank lines not carrying their needle %s' % (
        len(hits), len(SWEEP), un or 'NONE', nohit or 'NONE', bad or 'NONE'))
    if un or nohit or bad:
        sys.exit('### THE SWEEP AND ITS ENTRIES DISAGREE -- NOTHING WRITTEN')
    out = ['', '=' * 80, 'THE SWEEP OF (R270)-(R280) (2026-10-14), added to Component 2 by the navigator`s answer on the four tabs: every "the author`s ... at',
           'bNNN" / "as the author set at bNNN" / "the author`s ... of bNNN" in the rulings (the text of data/b660_ferry.txt ... data/b670_ferry.txt',
           'before the word FERRY, whitespace joined), checked for a bank or ledger line (tools/b670_record.py `sweep`). Patterns: %s' % ' ; '.join(SWEEP_PATS), '']
    for act, ph, v, ref, x in SWEEP:
        out.append('  (R%d) "%s" -- %s%s ; %s' % (int(act[1:]) - 390, ph, v, (' at %s :%d' % (ref[0].replace(PP + '/', ''), ref[1])) if ref else '', x))
    miss = [s for s in SWEEP if s[2] == 'MISS']
    out += ['', '### ### **PHRASES %d ; FOUND %d ; MISSES %d (TEXT SUPPLIED %d, TEXT NOT HELD %d -- the (R270) b645 word, its act read at b650`s lines).**' % (
        len(SWEEP), len(SWEEP) - len(miss), len(miss), sum('TEXT SUPPLIED' in s[4] for s in miss), sum('TEXT SUPPLIED' not in s[4] for s in miss))]
    if dry:
        print(NL.join(out))
        return
    old = rdn('b670_rules.txt')
    if 'THE SWEEP OF (R270)' in old:
        sys.exit('### THE SWEEP IS ALREADY BENEATH THE RULES -- NOTHING WRITTEN')
    put_txt('b670_rules.txt', old.rstrip(NL).split(NL) + out)
    if not rdn('b670_rules.txt').startswith(old.rstrip(NL)):
        sys.exit('### THE RULES BANK`S PREFIX MOVED')
    print(out[-1])


# ================================================================================ COMPONENT 3 (i): THE LICENSED TABLE
# ### rules row 3 (rowgen diff and constellation mode at the start of a review pass) over the 19 roster tables of data/b586_corroboration.txt
# ### (OPEN_TRAILS :12092), the paths as that bank read them; the rowgen diff is tools/rowgen/diff_rowpin.py (build-free, by the paper's own pins;
# ### `rowgen.py diff` runs lean per terminal and is not run on this host); the count outside LICENSED or CITED is the OVERREACHES and UNLICENSED
# ### rows per agenda document as data/b648_recut_order.txt banks them, a cut bank's STANDING line replacing a document cut since.
CUT_BANKS = {   # ### kernel -> (cut bank, the line carrying its standing figure, needle)
    'SIDE-kernel': ('data/b653_closing.txt', None, 'GRADED AND STILL STANDING 0 (OVERREACHES 0, UNDERSTATES 0)'),   # ### cut at b652 (its bank
    # ### data/b652_sidekernel_cut.txt: BLOCKS CUT 113, BRANCH UNMERGED), the three elided cells cut and the grade bank re-run at b653
    'SIDE-global-section': ('data/b655_cut_SIDE-global-section.txt', 49, 'STANDING 0 (OVERREACHES 0, UNDERSTATES 0, UNLICENSED 0)'),
    'SIDE-lv-conservation': ('data/b657_cut_SIDE-lv-conservation.txt', 28, 'STANDING 0 (OVERREACHES 0, UNDERSTATES 0, UNLICENSED 0)'),
    'SIDE-structural-error-correction': ('data/b659_cut_SIDE-structural-error-correction.txt', 19, 'STANDING 0 (OVERREACHES 0, UNDERSTATES 0, UNLICENSED 0)'),
    'SIDE-carrier-spec': ('data/b662_cut_SIDE-carrier-spec.txt', 21, 'STANDING 0 (OVERREACHES 0, UNDERSTATES 0, UNLICENSED 0)'),
    'SIDE-effects': ('data/b664_cut_SIDE-effects.txt', 20, 'STANDING 0 (OVERREACHES 0, UNDERSTATES 0, UNLICENSED 0)'),
    'SIDE-cosmo': ('data/b666_cut_SIDE-cosmo.txt', 23, 'STANDING 0 (OVERREACHES 0, UNDERSTATES 0, UNLICENSED 0)'),
    'SIDE-grh-transfer': ('data/b668_cut_SIDE-grh-transfer.txt', 23, 'STANDING 0 (OVERREACHES 0, UNDERSTATES 0, UNLICENSED 0)'),
}
WITHHELD_LINES = ('TECHNE_TOOLKIT',)    # ### N5: nothing of TECHNE written; its counts printed, its flag lines (quoted text) not banked


def _standing_line(bank, ln, needle):
    L = rd(os.path.join(ROOT, bank)).split(NL)
    if ln:
        return ln if needle in L[ln - 1] else None
    hits = [i + 1 for i, l in enumerate(L) if needle in l]
    return hits[-1] if len(hits) == 1 else None


def roster():
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def agenda():
    out = []
    for l in rdn('b648_recut_order.txt').split(NL):
        if not l.startswith('  ') or '|' not in l:
            continue
        c = [x.strip() for x in l.split('|')]
        doc, kind, ov, ul, tog, by, bank = c[0], c[1], int(c[2]), int(c[3]), int(c[4]), c[5], c[6]
        row = dict(doc=doc, kind=kind, b648=ov + ul, bank=bank, now=ov + ul, by=bank, moved='')
        m = re.match(r'(SIDE-[\w-]+) docstrings \(read at ([0-9a-f]{7})\)', doc)
        if m and m.group(1) in CUT_BANKS:
            cb, ln, nd = CUT_BANKS[m.group(1)]
            got = _standing_line(cb, ln, nd)
            if got is None:
                sys.exit('### THE CUT BANK %s CARRIES NO STANDING-0 LINE -- NOTHING WRITTEN' % cb)
            row.update(now=0, by='%s :%d (cut, STANDING 0)' % (cb, got))
        elif doc.startswith('SIDE-lv-conservation CouplingsAtPhi.lean :415'):
            if '(h2:CouplingsAtPhi:415)' not in rdn('b657_sentence_grades.txt').split(NL)[294]:
                sys.exit('### THE h2 ROW IS NOT AT data/b657_sentence_grades.txt :295 -- NOTHING WRITTEN')
            row.update(now=0, by='data/b657_sentence_grades.txt :295 (graded in block #12) ; data/b657_cut_SIDE-lv-conservation.txt :28 (STANDING 0)')
        elif m:
            kd = 'D:/' + m.group(1)
            if os.path.isdir(kd):
                n = g(kd, 'rev-list', '--count', '%s..main' % m.group(2)).strip()
                row['moved'] = 'main %s commit(s) past the read pin' % n if n not in ('0', '') else 'main at the read pin'
            else:
                row['moved'] = 'NO LOCAL CLONE AT %s' % kd
        else:
            p = os.path.join(PP, doc.split(' (')[0])
            if by != '-' and os.path.exists(p):
                b = os.path.getsize(p)
                row['moved'] = 'bytes %d at HEAD against %s at the read%s' % (b, by, '' if str(b) == by else ' -- MOVED SINCE ITS READ')
            elif not os.path.exists(p):
                row['moved'] = 'NOT AT %s' % p
        out.append(row)
    return out


def licensed(*a):
    dry = 'dry' in a
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
    print('  constellation exit %d ; diff_rowpin exit %d ; %d s' % (con.returncode, dif.returncode, int(time.time() - t0)))
    cc = dict((m.group(1), [int(m.group(k)) for k in (2, 3, 4, 5)]) for m in re.finditer(
        r'=== (\S+) : (\d+) actionable, (\d+) provenance, (\d+) external, (\d+) historical ===', con.stdout))
    dd = dict((m.group(1), [int(m.group(k)) for k in (2, 3, 4, 5)]) for m in re.finditer(
        r'=== (\S+)\s+checked\s+(\d+) \| present-at-a-paper-pin\s+(\d+) \| STALE (\d+) \| unmapped (\d+) ===', dif.stdout))
    AG = agenda()

    def body(out, keep):
        res, skip = [], False
        for l in out.split(NL):
            if l.startswith('==='):
                skip = any(w in l for w in WITHHELD_LINES)
                res.append(l + ('   ### ITS FLAG LINES NOT BANKED (N5)' if skip else ''))
            elif not skip:
                res.append(l)
        return res
    head = ['b670 -- COMPONENT 3 (i), (R280)(3): THE LICENSED TABLE -- CONSTELLATION MODE AND A ROWGEN DIFF PER TABLE OVER THE 19 ROSTER TABLES, AND',
            'THE ROWS OUTSIDE LICENSED OR CITED PER AGENDA DOCUMENT (%s), reading 1 of 2 (relay data/b670_rules.txt rows 1 and 3)' % utc(), '',
            '### THE DOCUMENT SET, A: the 19 roster tables of relay data/b586_corroboration.txt :34 (OPEN_TRAILS :12092), each at the path that bank read,',
            '### at PLACE-papers HEAD %s:' % g(PP, 'rev-parse', '--short', 'HEAD').strip()]
    head += ['    %-36s %s' % (n, p) for n, p in R]
    head += ['### THE DOCUMENT SET, B: the agenda of relay data/b648_recut_order.txt (%d documents), each at the read its bank names:' % len(AG)]
    head += ['    %s' % r['doc'] for r in AG]
    head += ['', '### THE INSTRUMENTS: tools/rowgen/rowgen.py `constellation <root> <papers>` (a text read: stale versions, missing targets, pending',
             '### language against REGISTRY) and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the build-free rowgen diff: each backticked',
             '### terminal of a table row looked up at the paper`s own pins, git show only; the rounded-profile check needs lean and is NOT EXERCISED).',
             '### `rowgen.py diff` itself calls lean for every terminal and is not run on this host (the ferry: no lean).', '',
             '=' * 100, '### A. PER ROSTER TABLE: constellation [actionable, provenance, external, historical] ; rowgen diff [checked, present, STALE, unmapped]']
    tabA = []
    for n, p in R:
        b = os.path.basename(p)
        c, d_ = cc.get(b), dd.get(b)
        tabA.append(dict(doc=n, path=p, constellation=c, diff=d_))
        head.append('  %-36s constellation %s ; rowgen diff %s' % (n, c or '### NOT READ', d_ or '### NOT READ'))
    nr = [x['doc'] for x in tabA if not x['constellation'] or not x['diff']]
    actn = sum(x['constellation'][0] for x in tabA if x['constellation'])
    stale = sum(x['diff'][2] for x in tabA if x['diff'])
    unm = sum(x['diff'][3] for x in tabA if x['diff'])
    head += ['### ### **ROSTER TABLES 19 ; READ BY BOTH %d ; CONSTELLATION ACTIONABLE %d ; ROWGEN DIFF STALE %d, UNMAPPED %d.**' % (
        19 - len(nr), actn, stale, unm), '',
        '=' * 100, '### B. PER AGENDA DOCUMENT: OVERREACHES + UNLICENSED at b648 -> now, with the bank that gives "now" and the document`s movement since its read']
    for r in AG:
        head.append('  %-62s %4d -> %4d   [%s]%s' % (r['doc'][:62], r['b648'], r['now'], r['by'], ('  ### ' + r['moved']) if r['moved'] else ''))
    tot = sum(r['now'] for r in AG)
    mv = [r['doc'] for r in AG if 'MOVED' in r['moved'] or ('commit(s) past' in r['moved'])]
    head += ['### ### **AGENDA DOCUMENTS %d ; ROWS OUTSIDE LICENSED OR CITED %d (AT b648 %d) ; DOCUMENTS AT ZERO %d ; DOCUMENTS MOVED SINCE THEIR READ AND '
             'NOT RE-READ BY THIS ACT %d.**' % (len(AG), tot, sum(r['b648'] for r in AG), sum(1 for r in AG if r['now'] == 0), len(mv)), '',
             '=' * 100, '### THE CONSTELLATION PRINT, WHOLE (exit %d):' % con.returncode] + body(con.stdout + con.stderr, True) + [
             '', '### THE ROWGEN DIFF PRINT, WHOLE (exit %d):' % dif.returncode] + body(dif.stdout + dif.stderr, True)
    print(NL.join([l for l in head if l.startswith('  ') and ('constellation' in l)][:19]))
    print(NL.join([l for l in head if l.startswith('### ### **')]))
    if nr or con.returncode or dif.returncode:
        print('### NOT READ: %s' % nr)
    if dry:
        return
    put_txt('b670_licensed_table.txt', head)
    put_json('b670_licensed_table.json', dict(at=utc(), roster=tabA, agenda=AG, total=tot, moved=mv, actionable=actn, stale=stale, unmapped=unm))


# ================================================================================ COMPONENT 3 (ii): THE CORRESPONDENCE TABLES AGAINST THE CURRENT TAGS
# ### per roster table (data/b586_corroboration.txt: its heading line at PLACE-papers 7e9b771, re-found at HEAD by its text), every table row
# ### with a backticked commit: each commit resolved in the kernels that bank lists for the document, and set against that kernel's current tag
# ### (git describe --tags --abbrev=0 main, peeled): AT THE TAG (the tag's commit or a descendant), BEHIND (a proper ancestor of it), or
# ### UNRESOLVED (in none of the listed kernels). A row is behind when any of its commits is behind.
B586_PIN = '7e9b771'
ALLK = sorted(x for x in os.listdir('D:/') if x.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', x, '.git')))
HEX7 = re.compile(r'`([0-9a-f]{7,40})`')


def _tag(k):
    kd = 'D:/' + k
    t = g(kd, 'describe', '--tags', '--abbrev=0', 'main').strip()
    return (t, g(kd, 'rev-parse', '--short', t + '^{commit}').strip()) if t else ('NO TAG', '')


def _anc(kd, a, b):
    return subprocess.run(['git', '-C', kd, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0


def corr(*a):
    dry = 'dry' in a
    L = rdn('b586_corroboration.txt').split(NL)
    meta = dict((l.split('|')[1].strip(), [x.strip() for x in l.split('|')]) for l in L if l.startswith('| ') and not l.startswith('| document'))
    tags, out, tot = {}, [], collections.Counter()
    for n, p in roster():
        c = meta[n]
        m = re.search(r'from :(\d+)', c[3])
        ks = [k.strip() for k in c[5].split(',') if k.strip().startswith('SIDE-')]
        old = _show(PP, B586_PIN, p) or ''
        cur = rd(os.path.join(PP, p)).split(NL)
        hl = old.split(NL)[int(m.group(1)) - 1].strip() if m and old else ''
        at = [i for i, l in enumerate(cur) if l.strip() == hl] if hl else []
        if not hl or len(at) != 1:
            out.append(dict(doc=n, heading=hl, found=len(at), rows=[], kernels=ks))
            continue
        i0 = at[0]
        lev = len(hl) - len(hl.lstrip('#'))
        j = i0 + 1
        while j < len(cur) and not (cur[j].startswith('#') and 0 < len(cur[j]) - len(cur[j].lstrip('#')) <= max(lev, 1)):
            j += 1
        tb = re.match(r'^:(\d+)', c[7])      # ### b586's tier-block line, read above it: the table ends there where it is re-found
        if tb:
            tl = old.split(NL)[int(tb.group(1)) - 1].strip()
            tat = [i for i in range(i0 + 1, len(cur)) if cur[i].strip() == tl] if tl else []
            if tat and tat[0] < j:
                j = tat[0]
        rows = []
        for i in range(i0 + 1, j):
            l = cur[i]
            if not l.lstrip().startswith('|'):
                continue
            pins = HEX7.findall(l)
            if not pins:
                continue
            res = []
            for q in pins:
                hit = [k for k in ks if subprocess.run(['git', '-C', 'D:/' + k, 'cat-file', '-e', q + '^{commit}'], capture_output=True).returncode == 0]
                if not hit:      # ### the second shape: every local kernel clone, the hit marked as outside b586's list for the document
                    hit = [k + '*' for k in ALLK if k not in ks and subprocess.run(['git', '-C', 'D:/' + k, 'cat-file', '-e', q + '^{commit}'],
                                                                                capture_output=True).returncode == 0]
                if not hit:
                    res.append((q, None, 'UNRESOLVED', '-'))
                    continue
                k = hit[0].rstrip('*')
                if k not in tags:
                    tags[k] = _tag(k)
                tc = tags[k][1]
                st = 'NO TAG' if not tc else ('AT THE TAG' if _anc('D:/' + k, tc, q) else ('BEHIND' if _anc('D:/' + k, q, tc) else 'OFF THE TAG`S LINE'))
                pt = g('D:/' + k, 'describe', '--tags', '--abbrev=0', q).strip() or 'NO TAG AT OR BEFORE IT'    # ### the table's tag
                res.append((q, hit[0], st, pt))
            sts = [r[2] for r in res]
            row = 'BEHIND' if 'BEHIND' in sts else ('UNRESOLVED' if all(s == 'UNRESOLVED' for s in sts) else
                                                  ('AT THE TAG' if all(s in ('AT THE TAG', 'UNRESOLVED') for s in sts) else sts[0]))
            rows.append(dict(line=i + 1, pins=res, reading=row))
            tot[row] += 1
        out.append(dict(doc=n, path=p, heading=hl, found=1, at=i0 + 1, end=j, rows=rows, kernels=ks))
    T_ = ['b670 -- COMPONENT 3 (ii), (R280)(3): THE CORRESPONDENCE TABLES AGAINST EACH KERNEL`S CURRENT TAG (%s), reading 1 of 2' % utc(), '',
          '### the tables: the 19 roster documents of relay data/b586_corroboration.txt, each table`s heading read at PLACE-papers %s at the line that' % B586_PIN,
          '### bank names and re-found at HEAD %s by its whole text; a row is a table line carrying a backticked commit. The kernels`' % g(PP, 'rev-parse', '--short', 'HEAD').strip(),
          '### current tags (main, local, the clones the census reads):']
    remote = {}
    if not dry:     # ### the read-first: each kernel's current tag by ls-remote, one call per repository, its print kept
        for k in sorted(tags):
            r = subprocess.run(['git', '-C', 'D:/' + k, 'ls-remote', '--tags', 'origin'], capture_output=True, text=True, encoding='utf-8', errors='replace')
            refs = dict((l.split('\t')[1], l.split('\t')[0]) for l in r.stdout.split(NL) if '\t' in l)
            t = tags[k][0]
            sha = refs.get('refs/tags/%s^{}' % t) or refs.get('refs/tags/%s' % t)
            remote[k] = dict(rc=r.returncode, refs=len(refs), sha=(sha or '')[:7],
                             reading=('AGREE' if sha and sha.startswith(tags[k][1]) else ('TAG ABSENT AT THE REMOTE' if r.returncode == 0 and refs else
                                                                                       ('NO TAGS AT THE REMOTE (exit 0, 0 refs)' if r.returncode == 0 else
                                                                                        'NO READ (exit %d; absent or private)' % r.returncode))))
    T_ += ['    %-34s %s at %s ; at the remote (ls-remote --tags, one call): %s' % (
        k, t[0], t[1], ('%s %s' % (remote[k]['sha'], remote[k]['reading'])) if k in remote else 'NOT READ IN A DRY RUN') for k, t in sorted(tags.items())]
    T_ += ['', '=' * 100, '### ROWS ARE KERNELS: the kernel ; the tables` tags (each cited commit`s nearest tag at or before it, git describe) with their',
           '### commit counts ; main`s tag ; the commits AT THE TAG / BEHIND it (a `*` on a kernel in the rows below: resolved outside b586`s list)']
    per = collections.defaultdict(list)
    for d in out:
        for r in d['rows']:
            for q, k, s, pt in r['pins']:
                if k:
                    per[k.rstrip('*')].append((pt, s))
    for k in sorted(per):
        tt = collections.Counter(pt for pt, _s in per[k])
        ss = collections.Counter(s for _pt, s in per[k])
        T_.append('  %-34s tables` tags %s ; main`s tag %s ; %s' % (k, dict(tt), tags[k][0], dict(ss)))
    T_ += ['', '=' * 100, '### THE TABLES, EVERY ROW WITH A COMMIT (line ; the row`s reading ; each commit, its kernel, its reading, its tag):']
    for d in out:
        if not d['found'] == 1:
            T_.append('=== %-34s ### TABLE HEADING NOT RE-FOUND AT HEAD (found %d): %r' % (d['doc'], d['found'], d['heading'][:80]))
            continue
        cn = collections.Counter(r['reading'] for r in d['rows'])
        T_.append('=== %-34s %s :%d-:%d ; rows with a commit %d ; %s' % (d['doc'], d['path'], d['at'], d['end'], len(d['rows']), dict(cn) or 'NONE'))
        for r in d['rows']:
            if d['doc'] in WITHHELD_LINES:
                continue
            T_.append('    :%-5d %-12s %s' % (r['line'], r['reading'], ' ; '.join('%s %s %s %s' % (q, k or '-', s, pt) for q, k, s, pt in r['pins'])))
    nf = [d['doc'] for d in out if d['found'] != 1]
    T_ += ['', '### ### **TABLES 19 ; RE-FOUND AT HEAD %d ; ROWS WITH A COMMIT %d ; AT THE TAG %d ; BEHIND %d ; UNRESOLVED %d ; OTHER %d.**' % (
        19 - len(nf), sum(tot.values()), tot['AT THE TAG'], tot['BEHIND'], tot['UNRESOLVED'],
        sum(v for k, v in tot.items() if k not in ('AT THE TAG', 'BEHIND', 'UNRESOLVED')))]
    print(NL.join(l for l in T_ if l.startswith('===') or l.startswith('### ### **')))
    if dry:
        return
    put_txt('b670_correspondence.txt', T_)
    put_json('b670_correspondence.json', dict(at=utc(), tags=tags, remote=remote, tables=out, counts=dict(tot)))


# ================================================================================ COMPONENT 3 (iii): THE CEILING SENTENCE AT ITS THREE PLACEMENTS
# ### the sentence read: the latest ceiling sentence that README and REGISTRY both carry and a FINDINGS line records as placed at both --
# ### (R183)(3)'s, README :125, REGISTRY :960, FINDINGS :6354 ("placed at README.md :125 and REGISTRY.md :960"). Each placement's sentence is
# ### taken by that placement's own delimiters (the italic run after "Supportable ...:" in README and REGISTRY; the italic run after
# ### "placed at README.md :N and REGISTRY.md :M:" in FINDINGS) and hashed alone; the pairs README-REGISTRY of every earlier ceiling sentence
# ### printed beside it.
SUP = re.compile(r"Supportable[^*]*?: \*(.+?)\*")
PLACED = re.compile(r"placed at README\.md :(\d+) and REGISTRY\.md :(\d+): \*(.+?)\*")
CEIL = (('README.md', 125), ('REGISTRY.md', 960), ('FINDINGS.md', 6354))


def ceiling(*a):
    import hashlib
    dry = 'dry' in a
    rows = []
    for f, ln in CEIL:
        l = rd(os.path.join(PP, f)).split(NL)[ln - 1]
        if f == 'FINDINGS.md':
            m = PLACED.search(l)
            s = m.group(3) if m and (int(m.group(1)), int(m.group(2))) == (CEIL[0][1], CEIL[1][1]) else None
        else:
            m = SUP.search(l)
            s = m.group(1) if m and "ruling `(R183)`(3)" in l else None
        if s is None:
            sys.exit('### %s :%d DOES NOT CARRY THE SENTENCE BY ITS DELIMITERS -- NOTHING WRITTEN' % (f, ln))
        b = s.encode('utf-8')
        rows.append(dict(placement='%s :%d' % (f, ln), bytes=len(b), sha256=hashlib.sha256(b).hexdigest()))
    eq = len(set(r['sha256'] for r in rows)) == 1
    # ### the control: one byte changed in the README sentence moves its hash
    ctl = hashlib.sha256(rows and (SUP.search(rd(os.path.join(PP, 'README.md')).split(NL)[124]).group(1) + ' ').encode('utf-8')).hexdigest() != rows[0]['sha256']
    pairs = []
    R_ = rd(os.path.join(PP, 'README.md')).split(NL)
    G_ = rd(os.path.join(PP, 'REGISTRY.md')).split(NL)
    for ln in range(100, 140):
        mm = re.search(r"ruling `\((R\d+)\)`", R_[ln - 1])
        sm = SUP.search(R_[ln - 1])
        if not (mm and sm):
            continue
        gl = [j + 1 for j in range(900, min(len(G_), 1000)) if re.search(r"ruling `\(%s\)`" % mm.group(1), G_[j]) and SUP.search(G_[j])]
        gs = SUP.search(G_[gl[0] - 1]).group(1) if gl else None
        pairs.append('  (%s) README :%d ; REGISTRY %s ; %s' % (mm.group(1), ln, (':%d' % gl[0]) if gl else 'NO LINE :901-:1000 CARRIES ITS RULING AND A "Supportable ...: *" RUN',
                                                            'BYTE-EQUAL' if gs == sm.group(1) else ('UNEQUAL' if gs else 'README ALONE BY THIS MATCHER')))
    T_ = ['b670 -- COMPONENT 3 (iii), (R280)(3): THE CEILING SENTENCE BYTE FOR BYTE AT README, REGISTRY AND THE FINDINGS RECORD OF ITS PLACEMENT (%s),' % utc(),
          'reading 1 of 2', '',
          '### the sentence: (R183)(3)`s, the latest ceiling sentence placed at both README and REGISTRY and recorded so in FINDINGS (:6354, "the author`s',
          '### sentence, placed at README.md :125 and REGISTRY.md :960"); the later README sentences ((R232)(3) :127, (R245)(5)(ii) :129) stand at README',
          '### alone (listed below). PLACE-papers HEAD %s. Each placement`s sentence taken by its own delimiters and hashed alone (UTF-8).' % g(PP, 'rev-parse', '--short', 'HEAD').strip(),
          '', '### ROWS ARE PLACEMENTS:']
    T_ += ['  %-20s bytes %4d ; sha256 %s' % (r['placement'], r['bytes'], r['sha256']) for r in rows]
    T_ += ['  the control: one byte appended to the README sentence moves its hash: %s' % ctl, '',
           '### every ceiling sentence of README :100-:140 against REGISTRY:'] + pairs
    T_ += ['', '### ### **THE CEILING SENTENCE %s AT THREE PLACEMENTS ; HASHES %d DISTINCT.**' % ('EQUAL' if eq else 'UNEQUAL', len(set(r['sha256'] for r in rows)))]
    print(NL.join(T_[7:]))
    if dry or not ctl:
        return
    put_txt('b670_ceiling.txt', T_)
    put_json('b670_ceiling.json', dict(at=utc(), rows=rows, equal=eq, control=ctl))


# ================================================================================ COMPONENT 3 (iv): THE WORK-ORDER QUEUE
# ### every W-ORD name on OPEN_TRAILS: its entry line (the first line naming it), its entry act (the bNNN on that line, else the nearest act
# ### head above it), its trigger (the first "Trigger" phrase on a line naming it, within 200 characters after the name or on its entry
# ### block's lines), its status (the last status word within 160 characters after the name on any line), its age in acts (670 less the
# ### entry act). Every cell carries its line; a status the screen cannot find reads NOT STATED with the last line naming the order.
WORD = re.compile(r"W-ORD-[A-Z0-9][A-Z0-9-]*[A-Z0-9]")
# ### the second shape (b670, after the first left 84 of 149 NOT STATED): the ledger's lower-case and phrase forms beside the capitals --
# ### "priced and not started", "filed and not run", "not filed", "RUN", "RESOLVED" -- each printed with its yield; OPEN, RUN and HELD in
# ### capitals only (their lower-case forms are prose words).
STATUS = re.compile(r"\b(DISCHARGED|RETIRED|CLOSED|ACTED|SUPERSEDED|WITHDRAWN|STRUCK|NOT STARTED|STARTED|STAYS|HELD|OPEN|PRICED|RE-DATED|"
                    r"RUN|RESOLVED|TRIGGER MET|"
                    r"(?i:its trigger met|trigger met|priced and not started|priced, not started|filed and not run|not filed|not started|"
                    r"discharged|retired|acted|withdrawn|superseded|re-dated|resolved))\b")
DONE_RE = re.compile(r'(?i)^(discharged|retired|closed|acted|superseded|withdrawn|struck|run|resolved|not filed)$')


def read_queue():
    L = rd(OT).split(NL)
    acthead = re.compile(r'^### (b\d{3}) ')
    orders = collections.OrderedDict()
    last_act = None
    for i, l in enumerate(L, 1):
        m = acthead.match(l)
        if m:
            last_act = m.group(1)
        for mm in WORD.finditer(l):
            n = mm.group(0)
            o = orders.get(n)
            if o is None:
                b = re.findall(r'\b(b\d{3})\b', l)
                ea = b[0] if b else last_act
                o = orders[n] = dict(name=n, line=i, act=ea, act_from='the entry line' if b else 'the act head above it',
                                     trigger=None, status='NOT STATED', status_line=None, last_line=i, lines=0)
            o['lines'] += 1
            o['last_line'] = i
            w = l[mm.end():mm.end() + 160]
            sm = list(STATUS.finditer(w))
            if sm:
                o['status'], o['status_line'] = sm[0].group(1), i
            if o['trigger'] is None:
                tm = re.search(r'(?i)\*{0,2}trigger:?\*{0,2}:? ?([^.;]{3,160})', l[mm.start():mm.start() + 400] if i != o['line'] else l)
                if tm:
                    o['trigger'] = (tm.group(1).strip(), i)
    for o in orders.values():
        if o['trigger'] is None:          # ### the entry block: the lines after the entry line up to the next head
            for j in range(o['line'], min(o['line'] + 12, len(L))):
                if j > o['line'] and L[j].startswith('#'):
                    break
                tm = re.search(r'(?i)\*\*trigger:?\*\*:? ?([^.;]{3,160})', L[j])
                if tm:
                    o['trigger'] = (tm.group(1).strip(), j + 1)
                    break
        o['age'] = 670 - int(o['act'][1:]) if o['act'] else -1
        o['open'] = o['status'] != 'NOT STATED' and not DONE_RE.match(o['status'])     # ### a status not read is not counted open or done
    return list(orders.values())


ITEMS = [   # ### (R280)(5): the census and cell-refresh items the ten closings name, each at its closing line (act, line, needle, the item)
    ('b657', 20, 'ROWS LISTED UNRESOLVED WITH THEIR REASONS', 'SIDE-lv-conservation`s rows listed UNRESOLVED (13), not cut, by the author`s word'),
    ('b662', 183, 'Axiom profiles at v0.4.1', 'SIDE-carrier-spec`s README heading "Axiom profiles at v0.4.1", one patch behind v0.4.2; no relay print bank'),
    ('b664', 170, 'the five Milestones.lean blocks restated at b648', 'SIDE-effects` five Milestones.lean blocks, UNRESOLVED-NO-CELL, owing cells'),
    ('b665', 173, 'K4, GammaRZetaValues', 'the Keiper face`s open part K4, GammaRZetaValues'),
    ('b666', 175, 'untagged Steane merge (c5cba30)', 'SIDE-cosmo`s main moved past v0.3 by the untagged Steane merge c5cba30 (tag v0.3.1 at b666)'),
    ('b667', 226, 'decimal literals', 'SIDE-explicit-formula Schema/EpsteinQ0.lean`s decimal literals (the kernel item for P1 and P2)'),
    ('b668', 183, '858cbf6, one commit past v0.5.0 untagged', 'SIDE-grh-transfer`s 858cbf6, one commit past v0.5.0, untagged (tag v0.5.1 at b668)'),
    ('b668', 185, 'in ASCII beside the', 'SIDE-grh-transfer`s six ACTION cells writing chi, chibar and sigma in ASCII'),
]


def orders(*a):
    dry = 'dry' in a
    Q = read_queue()
    IT = []
    for act, ln, nd, what in ITEMS:
        if nd not in rdn('%s_closing.txt' % act).split(NL)[ln - 1]:
            sys.exit('### data/%s_closing.txt :%d DOES NOT CARRY %r -- NOTHING WRITTEN' % (act, ln, nd))
        IT.append(dict(item=what, cite='data/%s_closing.txt :%d' % (act, ln), act=act, age=670 - int(act[1:])))
    for o in Q:
        read_order_row(o)
    op = [o for o in Q if o['open']]
    old = [o for o in op if o['age'] > 10 and not re.match(r'(?i)^(its )?trigger met$|^re-dated$', o['status'])]
    T_ = ['b670 -- COMPONENT 3 (iv), (R280)(3): THE WORK-ORDER QUEUE, EVERY W-ORD ON OPEN_TRAILS WITH ITS ENTRY ACT, TRIGGER, STATUS AND AGE (%s),' % utc(),
          'reading 1 of 2', '',
          '### the ledger: PLACE-papers OPEN_TRAILS.md at HEAD %s, %d lines. Rows are orders, in the order of their entry lines. The reader is' % (
              g(PP, 'rev-parse', '--short', 'HEAD').strip(), len(rd(OT).split(NL))),
          '### tools/b670_record.py `orders` (read_queue): entry = the first line naming the order; entry act = the bNNN on that line, else the act',
          '### head above it; trigger = the first "Trigger" phrase near the name or in its entry block; status = the last status word within 160',
          '### characters after the name on any line naming it (NOT STATED where none); age = 670 less the entry act. A status word is the ledger`s;',
          '### this act names none. OPEN = a status other than DISCHARGED, RETIRED, CLOSED, ACTED, SUPERSEDED, WITHDRAWN, STRUCK, RUN, RESOLVED,',
          '### "not filed" (any case). The matcher`s two shapes and their yields: the first (capitals and four lower-case verbs) left 84 of 149',
          '### NOT STATED; the second (the phrase forms, RUN, RESOLVED) is the one run here, its residue printed whole beneath the table.', '',
          '  %-44s %-7s %-6s %-5s %-16s %-8s %s' % ('order', 'entry', 'act', 'age', 'status', 'at', 'trigger [line]')]
    for o in Q:
        T_.append('  %-44s :%-6d %-6s %-5d %-16s %-8s %s' % (o['name'], o['line'], o['act'] or '-', o['age'], o['status'],
                                                           (':%d' % o['status_line']) if o['status_line'] else ':%d' % o['last_line'],
                                                           ('%s [:%d]' % (o['trigger'][0][:90], o['trigger'][1])) if o['trigger'] else 'NO TRIGGER PHRASE FOUND'))
    sc = collections.Counter(o['status'] for o in Q)
    LL = rd(OT).split(NL)
    T_ += ['', '### THE ORDERS WHOSE STATUS THE READER CANNOT FIND -- A FINDING OF THE READING, NOT REPAIRED IN THIS ACT (the navigator`s answer on',
           '### the two decisions): each by its last line naming it (200 characters about the name); carried by W-ORD-STATUS-CELLS, trigger "the',
           '### next re-cut act`s step zero" -- each to carry a status word on its own line, the author`s strike on the list:']
    for o in Q:
        if o['status'] == 'NOT STATED':
            l = LL[o['last_line'] - 1]
            i = l.find(o['name'])
            T_.append('  %-44s :%-6d %s' % (o['name'], o['last_line'], ' '.join(l[max(0, i - 60):i + 140].split())))
    ns = [o for o in Q if o['status'] == 'NOT STATED']
    T_ += ['', '### THE CENSUS AND CELL-REFRESH ITEMS THE TEN CLOSINGS NAME ((R280)(5)), each at its closing line, its age in acts (670 less the act):']
    T_ += ['  %-6s age %-3d %-26s %s' % (x['act'], x['age'], '[%s]' % x['cite'], x['item']) for x in IT]
    T_ += ['', '### status words as read: %s' % dict(sc),
           '### the open orders older than ten acts whose status is neither a trigger met nor a re-dating (rules row 1`s steadiness clause): %d' % len(old),
           '### beside them, the orders whose status the reader did not find, older than ten acts: %d of %d' % (sum(o['age'] > 10 for o in ns), len(ns)),
           '', '### ### **ORDERS %d ; OPEN %d ; DONE %d ; STATUS NOT STATED %d ; OPEN AND OLDER THAN TEN ACTS WITHOUT A TRIGGER MET OR A RE-DATING %d.**' % (
               len(Q), len(op), len(Q) - len(op) - len(ns), len(ns), len(old))]
    print(NL.join(T_[-5:]))
    if dry:
        return Q
    put_txt('b670_work_orders.txt', T_)
    put_json('b670_work_orders.json', dict(at=utc(), orders=Q, open=len(op), total=len(Q), old=[o['name'] for o in old], items=IT))


# ================================================================================ COMPONENT 4: THE METHOD-READINESS TABLE
# ### rows are the methods (R280)(4) names; the ten closings name no other as a method (the word "method" once, data/b666_closing.txt :171,
# ### "the isolation method", the argument-principle certification's row; the control: the same search finds it in data/b670_ferry.txt). Cells: the acts that used it, read from relay data/ bank names (a regex over
# ### `bNNN_<name>`, or a bank's own line where the name alone does not mark the method); the banks, by name; the failure modes, by defect
# ### letter, each a defect head read by hand (data/bNNN_defects.txt, line cited); the reading from the three cells alone (rules row 2).
METHODS = [
    ('the E0 gate reading', dict(name=r'_e0(_chi)?\.txt$|_e0_gate\.txt$', also=[('b663', 'data/b663_epstein_instance.txt', 'INTERFACES by the E0 rule')]),
     [('b663', 'e', 'data/b663_defects.txt', 26, 'A GRADE READ AS A PRINT'),
      ('b664', 'b663-late', 'data/b664_defects.txt', 6, 'A RULED TOOL EDIT WITHOUT EVERY TEST RUN AFTER IT')]),
    ('the sentence-row grade bank and the mechanical cut', dict(name=r'_sentence_grades\.txt$|_cut_SIDE-[\w-]+\.txt$|_sidekernel_cut\.txt$'),
     [('b652', 'b', 'data/b652_defects.txt', 8, 'A CUT WRITTEN AS IF THE SENTENCE ROWS CARRIED HAND GRADES'),
      ('b655', 'a', 'data/b655_defects.txt', 7, 'A CUT PLANNER THAT LEFT A LINE OF ONE SPACE'),
      ('b657', 'a', 'data/b657_defects.txt', 6, 'A CUT PLANNER THAT DROPS EMPHASIS MARKS'),
      ('b668', 'c', 'data/b668_defects.txt', 17, 'THE CUT BRANCH MADE BEFORE THE WORKFLOW COMMIT')]),
    ('the runner build with the artifact hash', dict(name=r'_runner_rows\.json$'),
     [('b653', 'a', 'data/b653_defects.txt', 7, 'A REMOTE RUNNER SENT AFTER REFS THAT LIVED ON ONE HOST'),
      ('b659', 'a', 'data/b659_defects.txt', 6, 'A WORKFLOW PLACED WHERE A DISPATCH CANNOT FIND IT'),
      ('b662', 'f', 'data/b662_defects.txt', 24, 'A DISPATCH AT A REF THAT DOES NOT CARRY THE WORKFLOW')]),
    ('the citation check at step zero and mid-act', dict(name=r'_citation_check\.txt$'),
     [('b663', 'f', 'data/b663_defects.txt', 30, 'TWO PREDICATES OF THE CITATION TOOL WRONG ON THEIR FIRST RUN'),
      ('b668', 'a', 'data/b668_defects.txt', 7, 'THE CITATION TOOL READ ITS OWN PRINT AS THE PASTE'),
      ('b669', 'b', 'data/b669_defects.txt', 9, "THE MID-ACT CHECK'S LEDGER PATTERN TOOK ONE OF THE ANSWER'S TWO LINES")]),
    ('the consumers section', dict(name=r'_plan\.txt$', line='THE CONSUMERS SECTION'), []),
    ('the argument-principle certification', dict(name=r'_epstein_counts\.txt$'), []),
    ('the detection map', dict(name=r'_detection_map(_40)?\.txt$|_map_diff\.txt$|_map_balls_diff\.txt$'),
     [('b662', 'a', 'data/b662_defects.txt', None, 'A CONSTANT THE SCRIPT DOES NOT HAVE, AND A CAP BELOW D'),
      ('b663', 'k', 'data/b663_defects.txt', None, "THE CARRIED SCRIPT CHANGED LINES OUTSIDE THE PLAN'S LIST")]),
    ('the dry-run gate step', dict(name=r'_reg_gate\.txt$', line='DRY-RUN STEP'),
     [('b642', 'g', 'data/b642_defects.txt', 9, 'TWO DRY RUNS WROTE INTO RELAY DATA'),
      ('b644', 'o', 'data/b644_defects.txt', 17, 'TWO DRY RUNS LANDED')]),
    ('the act root', dict(name=r'_act_root\.txt$'),
     [('b662', 'h', 'data/b662_defects.txt', 34, "A PRE-ROOT PUSH BEFORE THE TABLE'S FILES WERE COMMITTED")]),
    ('the mirror export', dict(name=r'_mirror\.txt$', line='mirror-refresh'),
     [('b537', 'b', 'data/b537_defects.txt', 7, 'THE HEAD BLOCK WENT TO THE MANIFEST`S END, NOT ITS HEAD'),
      ('b576', 'd', 'data/b576_defects.txt', 5, 'THE SEALED FACE`S WRITE LIST OMITS A WRITE OF THE MIRROR BUILDER')]),
    # ### rows (11) and (12), added by the navigator's answer on the methods table (prompt 2), their cells read the same way
    ('the sealed suite (the standing arms frozen, the act`s arms over its own banks, the hashes compared at the close)',
     dict(name=r'_seal_hashes\.json$'),
     [('b663', 'o', 'data/b663_defects.txt', 68, 'A CONSTANT NAMING THE WRONG FILE, FOUND AFTER THE SEAL'),
      ('b666', 'd', 'data/b666_defects.txt', 21, 'AN EMPTY PRINT READ AS OUTSIDE THE STANDARD THREE'),
      ('b667', 'l', 'data/b667_defects.txt', 60, "N2'S PRINTED TEXT COUNTS EVERY CALL BUT TIMES THE ROUTE'S LAST")]),
    ('the ζ-naming walk (the declaration closure counted for ζ objects)', dict(name=r'^b572_lemmas\.txt$|_zeta_walk\.txt$'), []),
]


def methods(*a):
    dry = 'dry' in a
    files = sorted(f for f in os.listdir(D) if re.match(r'^b\d{3}_', f))
    rows, bad = [], []
    for name, spec, defs in METHODS:
        banks = [f for f in files if re.search(spec['name'], f) and (('line' not in spec) or spec['line'] in rdn(f))]
        acts = sorted(set(f[:4] for f in banks) | set(x[0] for x in spec.get('also', [])))
        for act, p, nd in spec.get('also', []):
            if nd not in rd(os.path.join(ROOT, p)):
                bad.append('%s %s' % (name, p))
            banks.append(os.path.basename(p))
        dd = []
        for act, letter, p, ln, head in defs:
            L = rd(os.path.join(ROOT, p)).split(NL)
            hits = [i + 1 for i, l in enumerate(L) if re.match(r'^ *\(%s\) ' % re.escape(letter), l) and head in ' '.join(L[i:i + 2])]
            if not hits:
                bad.append('%s %s (%s)' % (name, act, letter))
                continue
            dd.append('%s (%s) %s :%d' % (act, letter, p, hits[0]))
        r = dict(method=name, acts=acts, banks=sorted(set(banks)), defects=dd)
        r['reading'] = 'NOT YET USED TWICE' if len(acts) < 2 else ('READY' if r['banks'] and dd else 'NOT READY')
        read_method_row(r)
        rows.append(r)
    ctl = ('method' in rd(os.path.join(D, 'b670_ferry.txt')), sum(bool(re.search(r'\bmethods?\b', rdn('b%d_closing.txt' % n))) for n in range(660, 670)))
    print('  cells not carrying their needle: %s ; "method" in the ten closings: %d (the control in the ferry: %s)' % (bad or 'NONE', ctl[1], ctl[0]))
    if bad or not ctl[0]:
        sys.exit('### A CELL DID NOT READ -- NOTHING WRITTEN')
    T_ = ['b670 -- COMPONENT 4, (R280)(4): THE METHOD-READINESS TABLE (%s), per relay data/b670_rules.txt row 2 (the navigator`s text of the' % utc(),
          'b663 criteria): READY when used in at least two acts, its inputs and outputs banked by name, and at least one failure mode recorded as a',
          'lettered defect; otherwise NOT READY, or NOT YET USED TWICE where the act count alone fails.', '',
          '### rows are methods: the ten (R280)(4) names. "method" stands in %d of the ten closings (the control, the ferry: %s): data/b666_closing.txt' % ctl,
          '### :171, "the isolation method" of b667, which is the argument-principle certification`s row; the closings name no other.',
          '### rows 11 and 12 added by the navigator`s answer on the methods table (relay data/b670_author_answers.txt). The sealed suite`s acts',
          '### are read from its hash records: b660 sealed nothing (data/b660_closing.txt :4, "NO SEAL"), so nine of the ten carry one. The',
          '### ζ-naming walk`s acts are b572 and b669 (data/b596_lemmas.txt is the walk for the proportion of simple zeros, another method); no',
          '### lettered defect head names a failure of it, so its defect cell is empty and it reads NOT READY on that cell alone.',
          '### ACTS: the bNNN of every relay bank whose name marks the method (and, where named below, whose text carries the method`s line);',
          '### BANKS: those banks by name (first, last and count); DEFECTS: lettered defect heads read by hand, each bank and line cited.', '']
    for r in rows:
        T_ += ['=== %s -- %s' % (r['method'], r['reading']),
               '    acts %d: %s' % (len(r['acts']), ' '.join(r['acts']) if len(r['acts']) <= 14 else '%s ... %s' % (' '.join(r['acts'][:6]), ' '.join(r['acts'][-6:]))),
               '    banks %d: %s' % (len(r['banks']), ', '.join(r['banks']) if len(r['banks']) <= 4 else 'data/%s ... data/%s' % (r['banks'][0], r['banks'][-1])),
               '    defects %d: %s' % (len(r['defects']), ' ; '.join(r['defects']) or 'NONE RECORDED'), '']
    c = collections.Counter(r['reading'] for r in rows)
    T_ += ['### ### **METHODS %d ; READY %d ; NOT READY %d ; NOT YET USED TWICE %d.**' % (len(rows), c['READY'], c['NOT READY'], c['NOT YET USED TWICE'])]
    print(NL.join(l for l in T_ if l.startswith('===') or l.startswith('### ### **')))
    if dry:
        return
    put_txt('b670_methods.txt', T_)
    put_json('b670_methods.json', dict(at=utc(), rows=rows, counts=dict(c)))


# ================================================================================ COMPONENT 5: ITEM 1'S TRIGGER (a), ONE SEARCH
# ### one request to the arXiv listing API (export.arxiv.org/api/query) by the claim's words -- "zero-free region" and "Siegel" in the
# ### abstract, newest first, fifty entries -- with no header but the library's own (no name, address or account of the author; the headers
# ### sent are printed); the request and the print banked whatever they hold; an entry is a candidate only where its own abstract carries
# ### "7/8" beside a zero-free region, its identifier then entered; otherwise NOT LOCATED. Run once: a second run refuses.
ZFR_URL = ('https://export.arxiv.org/api/query?search_query=abs:%22zero-free%20region%22%20AND%20abs:Siegel'
           '&sortBy=submittedDate&sortOrder=descending&start=0&max_results=50')


def zfr(*a):
    import urllib.request
    import xml.etree.ElementTree as ET
    if os.path.exists(os.path.join(D, 'b670_zfr_search.txt')):
        sys.exit('### THE ONE SEARCH HAS RUN (data/b670_zfr_search.txt) -- NOT SENT AGAIN')
    req = urllib.request.Request(ZFR_URL)
    sent = dict(req.header_items())
    if 'dry' in a:
        print('  would send GET %s ; headers added by the tool: %s (urllib adds Host, Accept-Encoding identity, User-Agent Python-urllib, '
              'Connection close)' % (ZFR_URL, sent or 'NONE'))
        return
    t0 = utc()
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            status, body = r.status, r.read().decode('utf-8', 'replace')
            rh = dict(r.getheaders())
    except Exception as e:
        status, body, rh = 'ERROR %r' % e, '', {}
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    ents = []
    try:
        root = ET.fromstring(body)
        for e in root.findall('a:entry', ns):
            ab = ' '.join((e.findtext('a:summary', '', ns) or '').split())
            ti = ' '.join((e.findtext('a:title', '', ns) or '').split())
            ents.append(dict(id=e.findtext('a:id', '', ns), published=e.findtext('a:published', '', ns), title=ti,
                             hit=bool(re.search(r'7\s*/\s*8|\\frac\{7\}\{8\}|seven.eighths', ab + ' ' + ti, re.I))))
            ents[-1]['abstract'] = ab
    except ET.ParseError as e:
        ents = []
        body = body + '\n### THE PRINT DID NOT PARSE: %r' % e
    hits = [x for x in ents if x['hit']]
    T_ = ['b670 -- COMPONENT 5, (R280)(5): ITEM 1`S TRIGGER (a), ONE SEARCH OF THE arXiv LISTING API BY THE CLAIM`S WORDS (%s)' % t0, '',
          '### THE CLAIM, as relay data/b668_b670_items.txt :5 holds it: a zero-free region σ > 7/8 for ζ and a family of L-functions, with Siegel zeros excluded.',
          '### THE REQUEST: GET %s' % ZFR_URL,
          '###   headers set by the tool: %s ; the library adds Host, Accept-Encoding, User-Agent (Python-urllib/%d.%d) and Connection, nothing else:' % (
              sent or 'NONE', sys.version_info[0], sys.version_info[1]),
          '###   no name, address, account or identifier of the author in the URL, the headers or a body (a GET carries none).',
          '### THE RESPONSE: status %s ; %d bytes ; entries %d ; the response headers: %s' % (status, len(body), len(ents),
                                                                                       dict((k, v) for k, v in rh.items() if k.lower() in ('content-type', 'date'))),
          '### AN ENTRY IS A CANDIDATE where its own title or abstract carries 7/8: %d.' % len(hits), '',
          '### THE ENTRIES (identifier ; published ; candidate ; title):']
    T_ += ['  %s ; %s ; %s ; %s' % (x['id'], x['published'][:10], 'CANDIDATE' if x['hit'] else '-', x['title']) for x in ents]
    for x in hits:
        T_ += ['', '### THE CANDIDATE %s, its abstract verbatim as the print carries it:' % x['id'], '  ' + x['abstract']]
    T_ += ['', '### ### **ONE REQUEST ; ENTRIES %d ; CANDIDATES %d ; %s.**' % (
        len(ents), len(hits), ('IDENTIFIER %s' % ', '.join(x['id'] for x in hits)) if hits else 'NOT LOCATED'),
           '', '### THE PRINT, WHOLE (the Atom feed as received):'] + body.replace('\r', '').split(NL)
    put_txt('b670_zfr_search.txt', T_)
    print(NL.join(T_[2:9]))
    print(T_[T_.index('### THE PRINT, WHOLE (the Atom feed as received):') - 2])


ROUTES = {'c1': c1, 'answers': answers, 'ten': ten, 'sweep': sweep, 'licensed': licensed, 'corr': corr, 'ceiling': ceiling, 'orders': orders,
          'methods': methods, 'zfr': zfr}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b670_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
