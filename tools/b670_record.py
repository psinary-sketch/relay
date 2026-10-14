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


# ================================================================================ COMPONENT 5: THE ITEMS ON OPEN_TRAILS
H5 = ('*Appended 2026-10-14 by b670 under `(R280)`(5) -- ITEM 1, EXTERNAL-ZFR-7/8, AS relay data/b668_b670_items.txt :5 HOLDS IT, ITS TRIGGER (a) '
      'ATTEMPTED ONCE:*',
      '*Appended 2026-10-14 by b670 under `(R280)`(5) -- ITEM 2, THE TWO RELATIVE-ENTROPY QUESTIONS, THE FLAG CARRIED:*',
      '### `W-ORD-STATUS-CELLS` -- A STATUS WORD ON ITS OWN LINE FOR EACH ORDER THE QUEUE READER CANNOT READ, PRICED, NOT STARTED, appended '
      '2026-10-14, b670, on the navigator`s answer on the two decisions',
      '*Appended 2026-10-14 by b670 under `(R280)`(8) as amended by the navigator`s note on the progress report -- THE ORDER AFTER b670, THE '
      'AUTHOR’S PLACEMENT, STRIKEABLE:*')


def c5(*a):
    it = rdn('b668_b670_items.txt').split(NL)
    claim = it[4]
    if not claim.startswith('EXTERNAL-ZFR-7/8'):
        sys.exit('### data/b668_b670_items.txt :5 IS NOT ITEM 1 -- NOTHING WRITTEN')
    z = rdn('b670_zfr_search.txt')
    res = re.search(r'### ### \*\*ONE REQUEST ; ENTRIES (\d+) ; CANDIDATES (\d+) ; ([^*]+)\.\*\*', z)
    if not res:
        sys.exit('### THE SEARCH BANK CARRIES NO RESULT LINE -- NOTHING WRITTEN')
    wo = json.load(io.open(os.path.join(D, 'b670_work_orders.json'), encoding='utf-8'))
    ns = [o for o in wo['orders'] if o['status'] == 'NOT STATED']
    t1 = (NL + H5[0] + ' ' + claim + ' **Trigger (a), attempted once at b670:** one request to the arXiv listing API by the claim`s words '
          '("zero-free region" and "Siegel" in the abstract, newest first, fifty entries), no identifier of the author in it; %s entries, '
          '%s carrying 7/8 -- %s (relay data/b670_zfr_search.txt, the request and the print whole). Nothing else of the claim is entered.' % (
              res.group(1), res.group(2), res.group(3)) + NL)
    t2 = (NL + H5[1] + ' as relay data/b668_b670_items.txt :7-:9 holds it: "the two relative-entropy questions (not yet in any relay bank at '
          'b668; their source the author`s chat record)". The flag alone is carried; no question is supplied by the seat.' + NL)
    t3 = (NL + H5[2] + NL + NL + '**Items.** The %d orders whose status the b670 queue reader cannot find, each listed by the line last naming '
          'it under its own heading in relay data/b670_work_orders.txt; each to carry a status word on its own line, the author`s strike on '
          'the list.' % len(ns) + NL + NL + '**Reason.** The work-order queue is the fourth reading of the pair (relay data/b670_rules.txt row 1); '
          'a status the reader cannot find cannot be read as steady or aged.' + NL + NL + '**Price:** one step. **Trigger:** the next re-cut '
          'act`s step zero.' + NL)
    t4 = (NL + H5[3] + ' ' + K.NEXT_ACTS + '. The (R280)(8) wording "b672 the re-cut act on the next kernel by count" stands superseded '
          'by this line (relay data/b670_author_answers.txt, the navigator`s note on the progress report); the next kernels by count after '
          'the eight cut, SIDE-window and SIDE-trivium at 5 each (relay data/b647_table_kernels.txt :25, :24), the tie rule at :14238 deciding.' + NL)
    land([('OPEN_TRAILS.md', H5[0], t1), ('OPEN_TRAILS.md', H5[1], t2), ('OPEN_TRAILS.md', H5[2], t3), ('OPEN_TRAILS.md', H5[3], t4)],
         'b670_items_lines.json', 'c5', check=[('OPEN_TRAILS.md', K.B669_TRAIL, '### b669')], dry='dry' in a)


# ================================================================================ THE LATE ROUTES (b669's, carried; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID
RUNNER_KEYS = ('kernel', 'branch', 'ref', 'target', 'run_id', 'conclusion', 'artifact_sha256', 'mem_low', 'stopped', 'gate', 'merged', 'tag')


def read_runner_row(r):
    """a row of the last merged run's bank (b669's, read by the standing runner arms) -- every key of RUNNER_KEYS present; raises KeyError."""
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


READERS += ['read_runner_row']


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
    L = ['b670 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
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
    put_txt('b670_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b670_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


def kernels(*a):
    import b641_record as R41
    put_json('b670_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


DEFECT_ROW = re.compile(r'^    \(([a-z])\) ')


def _defect_short():
    out = []
    L = rdn('b670_defects.txt').split(NL)
    for i, l in enumerate(L):
        if DEFECT_ROW.match(l):           # ### the row joined across its wrapped lines, cut at its first sentence's end, not a path's dot
            j = i + 1
            while j < len(L) and L[j].startswith('    ') and not DEFECT_ROW.match(L[j]) and not L[j].startswith('    ###'):
                j += 1
            m = re.match(r'^\(([a-z])\) (.*?)\.(?= |$)', ' '.join(x.strip() for x in L[i:j]))
            if m:
                out.append(m.group(0)[:-1])
    return out


def defects(*a):
    t = rdn('b670_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b670_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b670_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b670_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b670_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands|'
                          r'mirror.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b670_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b670_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b670'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b670_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    with tempfile.TemporaryDirectory(prefix='b670_ra_') as tmp:
        cp = os.path.join(tmp, os.path.basename(bank_))
        b = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b[0] ^= 0x01
        open(cp, 'wb').write(bytes(b))
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
    L = ['b670 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b670_root_arm.txt', L)
    put_json('b670_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b670 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b670_table_final.txt', L)
    put_json('b670_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b670_registration_2026-10-14.txt'
FACE = os.path.join(D, 'b670_registration_2026-10-14.txt')


def gatebanks(*a):
    """the gate's steps between the face and the lock (b665's order), each tool's output banked by this route, never by a shell redirect."""
    import gate_hash as G
    env = dict(os.environ, PYTHONIOENCODING='utf-8')

    def runb(args, out):
        r = subprocess.run([sys.executable] + args, capture_output=True, cwd=ROOT, env=env)
        b = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            open(p + '.tmp', 'wb').write(b)
            os.replace(p + '.tmp', p)
        return r.returncode, b.decode('utf-8', 'replace')
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b670_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b670_regspec.py')], 'b670_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b670_satisfiable.json', '--emit', 'b670'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b670_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b670_census_stepzero.txt'), ('b327_faces_census.py', 'b670_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b670_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b670'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b670_reg_gate.txt', 'data/b670_reg_termscan.txt', 'data/b670_regspec_run.txt', 'data/audit_b670_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES, (N1)-(N5) OF THE FERRY AND THE SEAT'S (S1)-(S3)
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b669_closing_push_out.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
CONSISTENT = re.compile(r'(?i)\bconsistent\b')
AUTHOR_IDS = ('psinary', 'hotmail', '@', 'orcid', '0009-0008', 'Seale', 'seale')


def TRAIL_HEAD():
    return ('### b670 — lane one, act ninety-seven, the reading act under (R280): b669 at its weight; the ten acts b660–b669; the four readings, '
            'reading 1 of 2; the method-readiness table; the b670 items')


def _calls():
    return jl('b670_author_answers.json').get('calls') or []


def _ledger_adds():
    out = []
    for f, pre in (('FINDINGS.md', K.PRE_PP), ('OPEN_TRAILS.md', K.PRE_PP)):
        old = _show(PP, pre, f) or ''
        now = rd(os.path.join(PP, f))
        out.append(now[len(old):] if now.startswith(old) else now)
    return NL.join(out)


def _techne_leak():
    """lines of this act's banks naming TECHNE_TOOLKIT beyond its name in the document set and its count lines (N5)."""
    bad = []
    for f in sorted(os.listdir(D)):
        if f.startswith('b670_') and os.path.isfile(os.path.join(D, f)) and f.endswith(('.txt', '.md')):
            for i, l in enumerate(rdn(f).split(NL), 1):
                if 'TECHNE' in l and not re.search(r'TECHNE_TOOLKIT(\.md)?\s+(phase1\.5/method/TECHNE_TOOLKIT\.md|constellation \[|: \d+ actionable|checked\s+\d|'
                                                   r'phase1\.5/method/TECHNE_TOOLKIT\.md :\d+-:\d+ ; rows with a commit)', l) \
                        and 'WITHHELD_LINES' not in l and 'TECHNE_TOOLKIT`s quoted lines' not in l and "TECHNE_TOOLKIT's quoted lines" not in l \
                        and 'nothing of TECHNE' not in l.lower() and 'Nothing of TECHNE' not in l and 'TECHNE-Core' not in l and 'TECHNE`s' not in l:
                    bad.append('%s :%d' % (f, i))
    return bad


def _n2():
    tj, mj = jl('b670_ten_acts.json'), jl('b670_methods.json')
    bad = []
    for r in tj.get('rows') or []:
        try:
            read_act_row(r)
        except Exception as e:
            bad.append(str(e))
    for d in tj.get('defects') or []:
        if not d.get('cite') or not d.get('kind'):
            bad.append('%s (%s)' % (d.get('act'), d.get('letter')))
    for r in mj.get('rows') or []:
        try:
            read_method_row(r)
        except Exception as e:
            bad.append(str(e))
        if not r['acts'] or not all(re.match(r'^b\d{3} \([a-z0-9-]+\) data/', x) for x in r['defects']):
            bad.append(r['method'])
    ok = len(tj.get('rows') or []) == 10 and len(mj.get('rows') or []) == 12 and not bad
    return ('HELD' if ok else 'REFUTED'), (
        'the ten-acts bank (relay data/b670_ten_acts.txt): %d acts, %d cells, every cell with a closing line read for its needle; the defects by '
        'kind (relay data/b670_defects_by_kind.txt): %d defects, each kind the defect`s own head words, each with its line; the methods table '
        '(relay data/b670_methods.txt): %d rows, every act read from a bank name, every failure mode a defect letter with its bank and line, '
        'every reading from the three cells alone (rules row 2); cells not reading: %s' % (
            len(tj.get('rows') or []), sum(len(r['cells']) for r in tj.get('rows') or []), len(tj.get('defects') or []), len(mj.get('rows') or []),
            bad or 'NONE'))


def _n3():
    st = rdn('b670_state.txt')
    figs = all(x in st for x in ('(i)   the licensed table', '(ii)  the Correspondence tables', '(iii) the ceiling sentence', '(iv)  the work-order queue'))
    banks = all(rdn(b) for b in ('b670_licensed_table.txt', 'b670_correspondence.txt', 'b670_ceiling.txt', 'b670_work_orders.txt'))
    line_ = 'STATE: reading 1 of 2 at b670' in st and 'reading 2 of 2 at b680' in st
    texts = [('data/b670_state.txt', st), ('the ledger lines appended', _ledger_adds())]
    for f in ('b670_ten_acts.txt', 'b670_methods.txt', 'b670_licensed_table.txt', 'b670_correspondence.txt', 'b670_ceiling.txt', 'b670_work_orders.txt',
              'b670_defects.txt', 'b670_stepzero.txt', 'b670_readfirst.txt'):
        texts.append(('data/' + f, rdn(f)))
    said = ['%s :%d' % (n, i) for n, t in texts for i, l in enumerate(t.split(NL), 1) if CONSISTENT.search(l)]
    ok = figs and banks and line_ and not said
    return ('HELD' if ok else 'REFUTED'), (
        'the four readings printed as figures with their banks (relay data/b670_licensed_table.txt, data/b670_correspondence.txt, '
        'data/b670_ceiling.txt, data/b670_work_orders.txt) and beneath them the state line "reading 1 of 2 at b670", b680 the second, with the '
        'four distances (relay data/b670_state.txt) %s; lines of this act`s banks and ledger lines carrying the word "consistent": %s (rules '
        'row 1`s quoted text in data/b670_rules.txt not counted, a rule and not a statement of this act)' % (figs and banks and line_, said or 'NONE'))


def _n4():
    z = rdn('b670_zfr_search.txt')
    req = [l for l in z.split(NL) if l.startswith('### THE REQUEST:') or l.startswith('###   headers set by the tool')]
    ids = [w for w in AUTHOR_IDS if any(w in l for l in req)]
    ok = len(req) == 2 and not ids and '### THE PRINT, WHOLE' in z and '### ### **ONE REQUEST ;' in z
    res = re.search(r'\*\*ONE REQUEST ; ([^*]+)\.\*\*', z)
    return ('HELD' if ok else 'REFUTED'), (
        'the one search`s request (relay data/b670_zfr_search.txt): its URL and the headers set by the tool read for %s: %s; its print banked '
        'whole, %s' % ('/'.join(AUTHOR_IDS), ids or 'NONE FOUND', res.group(1) if res else '### NO RESULT LINE'))


def _n1():
    cm = jl('b670_commands.json')
    face = jl('b670_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    unmoved = bool(face) and all(now[k] == list(v) for k, v in face.items())
    loc = g(K.KE, 'rev-parse', '--short=7', K.OPEN_BRANCH).strip()
    rem = g(K.KE, 'rev-parse', '--short=7', 'origin/' + K.OPEN_BRANCH).strip()
    ok = bool(cm) and not cm.get('local_lean') and unmoved and loc == rem == K.OPEN_TIP
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b670_commands.txt); every kernel`s main, tags, branches and '
        'status as the face read them %s; %s at %s locally and %s at its remote-tracking ref (the one ls-remote of the closing reads it at the '
        'remote)' % (cm.get('local_lean') if cm else '### UNREAD', unmoved, K.OPEN_BRANCH, loc, rem))


def _n5():
    face = jl('b670_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b670_|audit_b670_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b670_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    leak = _techne_leak()
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = others_ok and not pp_beyond and not kinds_beyond and not differ and not new_arms and not leak and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); no kernel main written, every kernel as the face read it %s; '
            'standing arms added: %s (the act`s arms over its own banks %d); sealed tools not agreeing %s; PLACE-papers beyond FINDINGS and '
            'OPEN_TRAILS: %s; relay files of a kind beyond the banks, the tools, the root list and b669`s push-out bank: %s; lines of this act`s banks '
            'naming TECHNE_TOOLKIT beyond its name and counts: %s; "patent" in the ledger lines: %s; the mirror export written outside every tree' % (
                K.DRAFT, others_ok, new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE',
                leak or 'NONE', pat or 'NONE'))


def scores(*a):
    TF, RA = jl('b670_table_final.json'), jl('b670_root_arm.json')
    _r, _n, sh = seal_hashes()
    S = {
        'N1': _n1(), 'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    put_json('b670_scores.json', dict((k2, list(v)) for k2, v in S.items()))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))


NEXT_LINE = ('b671 W-ORD-EPSTEIN-BALL-WIDTH; b672 the Correspondence generator, a tooling act in the re-cut slot; b673 V4 and V5 on chi-li-b669; '
             'b674 the re-cut act on the kernel the tie rule picks between SIDE-window and SIDE-trivium, then the document with the most rows outside '
             'LICENSED or CITED, alternating with research acts; b680 reading 2 of 2 -- `(R280)`(8) as amended by the navigator’s note (OPEN_TRAILS :14358)')


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'


def _figs():
    lt, co, ce, wo, me = (jl(n_) for n_ in ('b670_licensed_table.json', 'b670_correspondence.json', 'b670_ceiling.json', 'b670_work_orders.json',
                                            'b670_methods.json'))
    mc = collections.Counter(r['reading'] for r in me.get('rows') or [])
    return dict(n=lt.get('total', '?'), m=(co.get('counts') or {}).get('BEHIND', '?'), rows=sum((co.get('counts') or {}).values()) if co else '?',
                eq='equal' if ce.get('equal') else 'unequal', k=wo.get('open', '?'), t=wo.get('total', '?'), old=len(wo.get('old') or []),
                ns=sum(1 for o in wo.get('orders') or [] if o.get('status') == 'NOT STATED'), r=mc.get('READY', 0), s=len(me.get('rows') or []),
                nr=mc.get('NOT READY', 0), ny=mc.get('NOT YET USED TWICE', 0))


def _title():
    f = _figs()
    return ('## The reading at b670: ten acts b660–b669; the licensed table at %s rows outside LICENSED or CITED, Correspondence %s rows behind, '
            'the ceiling %s at three placements, %s orders open of %s; %s methods READY of %s; reading 1 of 2' % (
                f['n'], f['m'], f['eq'], f['k'], f['t'], f['r'], f['s']))


def _finding_text():
    S, rl, J, il = jl('b670_scores.json'), jl('b670_record_lines.json'), jl('b670_act_root.json'), jl('b670_items_lines.json')
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b670_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}]
    il_ = dict((x.get('head', ''), x.get('line')) for x in il.get('lines') or [])     # ### the whole head: the four share their first words
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    mids = re.findall(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    tj = jl('b670_ten_acts.json')
    zr = re.search(r'\*\*ONE REQUEST ; ENTRIES (\d+) ; CANDIDATES (\d+) ; ([^*]+)\.\*\*', rdn('b670_zfr_search.txt'))
    e = ['', _title(), '',
         '*Filed at b670 on the author’s ruling `(R280)` and the navigator’s answers (%d questions in %d calls, and the pasted answers). Banks: '
         'relay `data/b670_ten_acts.txt`, `data/b670_defects_by_kind.txt`, `data/b670_rules.txt`, `data/b670_licensed_table.txt`, '
         '`data/b670_correspondence.txt`, `data/b670_ceiling.txt`, `data/b670_work_orders.txt`, `data/b670_state.txt`, `data/b670_methods.txt`, '
         '`data/b670_zfr_search.txt`, `data/b670_act_root.txt`.*' % (n_ans, len(_calls())), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed -- the pair of readings and the method '
         'criteria named from the chat, and the count of the kernels cut, each raised and answered (the texts supplied as rules rows 1-2, the count '
         'eight); the mid-act checks of `(R278)`(4), %d prints, the last %s of %s OK, four of them run after their answers were acted on (defect (e)).' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', len(mids), mids[-1][1] if mids else '?',
             mids[-1][0] if mids else '?'), '',
         '**The record lines** (`(R280)`(1)): b669 at its weight (FINDINGS :%s).' % ls[0].get('line'), '',
         '**The ten acts** (`(R280)`(2)): b660-b669 read from their closings, every cell cited to a closing line and re-read for its needle; %d '
         'defects, the seat’s %d and the navigator’s %d, each kind in its own head words, six naming an earlier kind; the sweep of `(R270)`-`(R280)` '
         'for the author’s word at an act: five phrases, two found, three missed (two texts supplied, one, the `(R270)` b645 word, not held).' % (
             len(tj.get('defects') or []), sum(d['seat'] == 'THE SEAT`S' for d in tj.get('defects') or []),
             sum(d['seat'] == 'THE NAVIGATOR`S' for d in tj.get('defects') or [])), '',
         '**The four readings** (`(R280)`(3)), reading 1 of 2: (i) %s rows outside LICENSED or CITED across the 33 agenda documents (607 at b648), '
         'constellation mode and the build-free rowgen diff over the 19 roster tables; (ii) %s of %s Correspondence rows behind their kernel’s '
         'current tag, each tag read by one ls-remote; (iii) the `(R183)`(3) ceiling sentence %s at README :125, REGISTRY :960 and FINDINGS :6354, '
         'one sha256; (iv) %s orders, %s open, %s with no status word the reader finds, %s open and older than ten acts without a trigger met. The '
         'distances from the pair’s bar: %s, %s, 0, %s and %s; b680 prints the same four beside them. No consistency is read from one reading.' % (
             f['n'], f['m'], f['rows'], f['eq'], f['t'], f['k'], f['ns'], f['old'], f['n'], f['m'], f['old'], f['ns']), '',
         '**The methods** (`(R280)`(4), rules row 2): %s methods, READY %s, NOT READY %s (the ζ-naming walk, no failure mode recorded), NOT YET USED '
         'TWICE %s (the consumers section, the argument-principle certification).' % (f['s'], f['r'], f['nr'], f['ny']), '',
         '**The items** (`(R280)`(5)): EXTERNAL-ZFR-7/8 entered as the items bank holds it (OPEN_TRAILS :%s), its trigger (a) attempted by one '
         'request with no identifier of the author: %s entries, %s carrying 7/8, %s; the two relative-entropy questions carried as a flag (:%s); '
         'W-ORD-STATUS-CELLS entered (:%s); the order after b670 as the author placed it (:%s).' % (
             il_.get(H5[0]), zr.group(1) if zr else '?', zr.group(2) if zr else '?', zr.group(3) if zr else '?', il_.get(H5[1]),
             il_.get(H5[2]), il_.get(H5[3])), '',
         '**The root.** b670 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b660’s ten acts, b586’s roster census, b648’s re-cut order and the '
         'cut banks of b652-b668; it is re-read by b680, the second reading of the pair, which prints the same four distances, and by the act that '
         'gives the 69 orders their status words. It strengthens the programme’s offering of a corpus a reader can audit: every figure here stands '
         'with the bank and the line it is read from.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; this act wrote no kernel byte.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the review-pass rule found at OPEN_TRAILS :12092, so the sweep keeps three misses where the note on the progress report '
              'reduces it by one (data/b670_defects.txt, the seat’s note beside (a)); (2) the dry-run gate step’s failure modes, b642 (g) and b644 (o), '
              'recorded before `(R267)`(2) made it a gate step; (3) the sealed suite’s acts read from its hash records, b660 sealing nothing; (4) '
              'reading (ii) counts a row behind when any commit it cites is a proper ancestor of its kernel’s current tag')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b670_scores.json', 'b670_findings.json', 'b670_record_lines.json', 'b670_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b670_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}]
    f = _figs()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R280) ratified.** (1) b669 at its weight. (2) The ten acts b660-b669 from their closings, the defects by kind, the sweep. (3) The four '
             'readings and the state line, reading 1 of 2. (4) The method-readiness table. (5) The b670 items. (6) No kernel byte. (7) The mirror. (8) '
             'The acts after, as amended.', '',
             '**Entered:** FINDINGS.md:%s (b669’s weight), :%s (the entry); OPEN_TRAILS.md:14346-:14358 (the items, W-ORD-STATUS-CELLS, the order '
             'after b670); this record.' % (ls[0].get('line'), fj.get('entry_line')), '',
             '**Act root:** b670 `%s` (previous `%s`, b669’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d calls (relay data/b670_author_answers.txt): the four tabs at step zero, the state line '
             'of `(R280)`(3), the methods table of `(R280)`(4); none after the root.' % (n_ans, len(_calls())), '',
             '**The state, reading 1 of 2:** (i) %s rows outside LICENSED or CITED; (ii) %s rows behind; (iii) the ceiling %s; (iv) %s orders older '
             'than ten acts open without a trigger met and %s without a status word; b680 the second reading.' % (f['n'], f['m'], f['eq'], f['old'], f['ns']), '',
             '**The open converse:** branch %s at %s, kept, unmerged; V4 and V5 at b673.' % (K.OPEN_BRANCH, K.OPEN_TIP), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b670_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b670_scores.json')
    L = ['=' * 104, 'b670 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b670_state.txt').rstrip(NL).split(NL) + [''] + rdn('b670_defects.txt').rstrip(NL).split(NL)
    put_txt('b670_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b670_scores.json', 'b670_findings.json', 'b670_trail.json', 'b670_record_lines.json', 'b670_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}]
    f = _figs()
    L = ['b670 -- THE COMPONENTS, BANKED UNDER (R280).', '',
         '### COMPONENT 0 : the citation check (data/b670_citation_check.txt), step zero (data/b670_ferry.txt, data/b670_stepzero.txt, '
         'data/b670_tests_stepzero.txt, data/b670_readfirst.txt), the rules (data/b670_rules.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b669`s weight FINDINGS :%s' % ls[0].get('line'),
         '### COMPONENT 2 : the ten acts (data/b670_ten_acts.txt), the defects by kind (data/b670_defects_by_kind.txt), the sweep (data/b670_rules.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the four readings (data/b670_licensed_table.txt %s, data/b670_correspondence.txt %s, data/b670_ceiling.txt %s, '
         'data/b670_work_orders.txt %s of %s open), the state line reading 1 of 2 (data/b670_state.txt) ; N3 %s' % (
             f['n'], f['m'], f['eq'], f['k'], f['t'], S['N3'][0]),
         '### COMPONENT 4 : the methods table (data/b670_methods.txt) READY %s of %s' % (f['r'], f['s']),
         '### COMPONENT 5 : the items (data/b670_zfr_search.txt ; OPEN_TRAILS :14346-:14358) ; N4 %s' % S['N4'][0],
         '### COMPONENT 6 : the dry-run step (data/b670_reg_gate.txt), the seal (data/b670_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 7 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b670_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b670_findings.json', dict(title=t))
    j = jl('b670_findings.json')
    j['entry_line'] = ln
    put_json('b670_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b670_trail.json', {})
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


# ================================================================================ THE MIRROR, AT THE CLOSE ((R280)(7), the b655 form; b668's routes, carried)
import hashlib as _hl   # noqa: E402

MIRROR_TAG = '2026-10-14-b670'
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
    put_json('b670_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b670':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b670`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b670_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b670_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b670_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b670 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b670_mirror.txt', L)
    put_json('b670_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:8]:
        print(l[:240])


ROUTES = {'c1': c1, 'answers': answers, 'ten': ten, 'sweep': sweep, 'licensed': licensed, 'corr': corr, 'ceiling': ceiling, 'orders': orders,
          'methods': methods, 'zfr': zfr, 'c5': c5, 'mbuild': mbuild, 'mroot': mroot, 'mverify': mverify, 'mbank': mbank, 'commands': commands, 'kernels': kernels, 'defects': defects, 'root': root,
          'root_arm': root_arm, 'table_final': table_final, 'gatebanks': gatebanks, 'scores': scores, 'desk': desk, 'components': components,
          'findings': findings, 'trail': trail, 'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b670_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
