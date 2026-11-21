# -*- coding: utf-8 -*-
"""tools/b765_rulings.py -- b765, (R375)(4) to (9) and the author's words of 2026-11-21: THE TEXTS OF THE RULING ENTERED IN OPEN_TRAILS.

Carried in form from tools/b764_rulings.py's ledgers route (the texts read from the ferry bank between their marker lines and checked
against their lines; the file appended at its end, its bytes at HEAD a prefix of its new bytes; the controls before the write; the ledger
banked by line and sha256) by the Write tool, and committed before its run (N2). (R375)(12) writes neither REGISTRY, ERRATA nor the
register, so OPEN_TRAILS is the one file here; [R1] is entered in the act's trail record at the close, after (7)'s build, whose commits it
names (data/b765_misses.txt (9)).

  ledgers dry|write   appended at OPEN_TRAILS' end, no line moving, <DATE> the UTC date of the write: one dated head and under it, each a
                      paragraph of its own, in the ruling's order --
                      [C5] where H-RUNNER-RESTORE reads HELD, [C6] where it reads REFUTED or NOT SCORABLE, by the dispatch tool's own
                        reading (tools/b765_controls.py verdicts() over data/b765_dispatch_rows.json); under HELD, by the author's word on
                        the save on main (data/b765_author_words_preseal.txt :30-:36), [C5] gaining at its end the clause of the word of
                        2026-11-21 on the runner's cache, (iv) (:26), where a save on main is read, and [C5] as (R375) gives it where the
                        second save stopped as the first did; the write refused while the save on main is open;
                      [S1] from the statement's read, COMPILED; [S2] from the closing commit's restore-on read and its run's axioms file;
                      [W1] from data/b765_window.txt; [Q1] from data/b765_premise_positions.txt's foot; [M3] from data/b765_map_pair.txt;
                      [B2] from data/b765_held_branches.txt's reading; [H4] from the author's word of 2026-11-21, Route A (:12-:14), its
                        reason from data/b765_pi01_reading.txt's foot; [T1]; [T2]; [T3], its clause on W-ORD-H2-PI1 as that word gives it
                        (:15) and its upstream field from the step-zero read (data/b765_events.txt (10)).
                      Controls before the write, printed; the roster by tools/standing/orders.py's rule in memory, before and after,
                      printed and no condition. Bank: data/b765_ledgers.txt and .json, each appended text by line and sha256; the texts'
                      words printed by the dry run alone. A dry run before the pair's verdict composes the rest and refuses the write.

No PLACE-papers line is printed but the texts this tool composes; the account is counted, never printed; no git write.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b765_worklist as K   # noqa: E402

ACT, NL = 'b765', '\n'
PP, EF = K.PP, K.EF_DIR
FERRY = os.path.join(D, 'b765_ferry.txt')
FERRY_SHA = '3a563595f4360e14'   # ### data/b765_stepzero.txt :23: the ferry bank's sha256
WORDS = os.path.join(D, 'b765_author_words_preseal.txt')
WORDS_H4 = (12, 14)              # ### the word of Route A: '---- [H4] for OPEN_TRAILS, one line' at :12, its end marker at :14
WORDS_T3 = 15                    # ### the same word: [T3]'s clause on W-ORD-H2-PI1
WORDS_C5 = 26                    # ### the word on the runner's cache, (iv): [C5]'s gain at its end
OT = 'OPEN_TRAILS.md'
C1PP = 'd9c03949'                # ### PLACE-papers' one commit of the act before this write: the corrigendum (step 7)
WANT = dict(G2=(46, 50), C5=(54, 54), C6=(58, 58), S1=(62, 62), S2=(66, 66), S3=(70, 70), S4=(74, 74), W1=(78, 78), W2=(82, 82),
            Q1=(86, 86), M3=(90, 90), B2=(94, 94), R1=(98, 98), R2=(102, 102), T1=(106, 106), T2=(110, 110), T3=(114, 114))
FIELD = re.compile(r'<[A-Za-z][^<>\n]*>')
OUTER = '<for each of the four, carried on main by <declaration> | still owed under <order>>'   # ### [B2]'s field, nested
T3_OLD = "`W-ORD-H2-PI1` (:16563), the word given, the reading waiting on the author's choice of its source"
C6_WHY = {'EXIT 0': 'the planted build exited 0', 'DIFFERS': "the pair's axioms files differ",
          'STOPPED BOTH': 'the closing build from source stopped under the hold at both dispatches'}
STATEMENT_COMMIT = 'd540bc98'    # ### (5)(a)'s statement, compiled in dispatch 1 (run 44900549948)
CLOSING = '0ba9cd61'             # ### the act's closing Lean commit (data/b765_events.txt (54))
GAUSS = 'SIDEExplicitFormula.B321.GaussArchQSteps.gaussArchQ'
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
LBANK, LJSON = os.path.join(D, 'b765_ledgers.txt'), os.path.join(D, 'b765_ledgers.json')
BRANCHES = ('detection-region-b559', 'vendor-bulka-backport-b566', 'grh-weil-b569-held', 'challenge-b720-h2-sign-iff-rh')


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def today():
    return time.strftime('%Y-%m-%d', time.gmtime())


def git(repo, *a, raw=False):
    r = subprocess.run(['git', '-C', repo, *a], capture_output=True)
    return r.stdout if raw else r.stdout.decode('utf-8', 'replace')


def fsha(p):
    try:
        with open(p, 'rb') as f:
            return sha(f.read())[:16]
    except OSError:
        return 'ABSENT'


def put(path, text):
    with open(path + '.tmp', 'wb') as f:
        f.write(text.encode('utf-8'))
    os.replace(path + '.tmp', path)


def rdl(name):
    with open(os.path.join(D, name), encoding='utf-8') as f:
        return f.read().replace('\r', '').split(NL)


def ids():
    import b765_address_scan as SC
    return dict(name=SC.author_name(), orcid=SC.author_orcid(), address=SC.previous_address())


def account():
    """the account read from the relay's remote at run time (as tools/project_set.py reads it); counted in the texts, never printed."""
    import project_set as PS
    return PS.owner()


def idcount(text, I, acct):
    low = text.lower()
    return dict(name=low.count(I['name'].lower()), orcid=low.count(I['orcid'].lower()), address=low.count(I['address'].lower()),
                github=low.count('github.com/'), account=low.count(acct.lower()) if acct else -1)


def at_head(path):
    b = git(PP, 'show', 'HEAD:' + path, raw=True)
    with open(os.path.join(PP, *path.split('/')), 'rb') as f:
        w = f.read()
    if not b or b != w:
        die('%s: ITS WORKING FILE IS NOT ITS BYTES AT HEAD (%d, %d bytes)' % (path, len(b), len(w)))
    if b'\r' in b or not b.endswith(b'\n'):
        die('%s: CARRIAGE RETURNS OR NO FINAL LINE END' % path)
    return b.decode('utf-8')


# ================================================================================ THE TEXTS
def ferry():
    with open(FERRY, 'rb') as f:
        b = f.read()
    if sha(b)[:16] != FERRY_SHA:
        die('THE FERRY BANK IS NOT ITS STEP-ZERO BYTES (sha256 %s)' % sha(b)[:16])
    return b.decode('utf-8').split(NL)


def texts(L):
    """{key: (first line, last line, text)} for each piece between '---- [K] ...' and '---- end [K]'; the lines checked against WANT."""
    out = {}
    for i, l in enumerate(L):
        m = re.match(r'^---- \[([A-Z]\d*)\] ', l)
        if m:
            k = m.group(1)
            j = L.index('---- end [%s]' % k, i)
            out[k] = (i + 2, j, NL.join(L[i + 1:j]))
    got = dict((k, (a, b)) for k, (a, b, _t) in out.items())
    if got != WANT:
        die('THE RULING`S TEXTS NOT AT THEIR LINES: %s' % sorted(set(got.items()) ^ set(WANT.items())))
    return out


def words():
    """the author's words of 2026-11-21: [H4]'s text, [T3]'s clause, [C5]'s gain -- each at its line, refused where it is not."""
    L = rdl('b765_author_words_preseal.txt')
    a, b = WORDS_H4
    if not L[a - 1].startswith('---- [H4] for OPEN_TRAILS') or L[b - 1] != '---- end [H4]' or b - a != 2:
        die('[H4] NOT AT data/b765_author_words_preseal.txt :%d-:%d' % WORDS_H4)
    h4 = L[a]
    t3 = L[WORDS_T3 - 1]
    if not t3.startswith('In [T3] of (R375), the clause on W-ORD-H2-PI1 reads: "'):
        die('THE WORD`S [T3] CLAUSE NOT AT :%d' % WORDS_T3)
    c5 = L[WORDS_C5 - 1]
    if not c5.startswith('(iv) [C5] gains at its end: "'):
        die('THE WORD`S (iv) NOT AT :%d' % WORDS_C5)
    return h4, t3[t3.index('"') + 1:t3.rindex('"')], c5[c5.index('"') + 1:c5.rindex('"')]


def templates(X, W):
    """each key's template as entered: the ruling's text, [C5] with the word's (iv) at its end, [T3] with the word's clause, [H4] the word's."""
    h4, t3c, c5g = W
    c5 = X['C5'][2]
    if not c5.endswith('.'):
        die('[C5] DOES NOT END WITH A FULL STOP')
    t3 = X['T3'][2]
    if T3_OLD not in t3:
        die('[T3]`S CLAUSE ON W-ORD-H2-PI1 NOT IN THE RULING`S TEXT AS READ')
    tp = dict((k, X[k][2]) for k in ('C6', 'S1', 'S2', 'W1', 'Q1', 'M3', 'B2', 'T1', 'T2'))
    tp.update(C5=c5[:-1] + '; ' + c5g + '.', T3=t3.replace(T3_OLD, t3c, 1), H4=h4)
    return tp


def pattern(tpl):
    t = tpl.replace(OUTER, 'QQOUTERQQ', 1)
    pat = re.escape(t)
    for ph in sorted(set(FIELD.findall(t)), key=len, reverse=True):
        pat = pat.replace(re.escape(ph), '(.+?)')
    return pat.replace('QQOUTERQQ', '(.+?)')


def fill(tpl, values):
    t = tpl
    for ph, v in values:
        if ph not in t:
            die('THE FIELD %r NOT IN ITS TEMPLATE' % ph)
        t = t.replace(ph, v, 1)
    return t


# ================================================================================ THE FIELDS, FROM THE BANKS
def runner():
    """the dispatch tool's own reading: (key, values, why, the runs cited) or (None, ..) while the pair is open. Under HELD the save on main is
    read as the author's word on the save on main orders it (data/b765_author_words_preseal.txt :30-:36, amendment row 3): a save read, from
    the second save where it was sent, [C5] with the word's (iv) and the save's commit in its field ('C5'); the second save stopped as the
    first did, [C5] as (R375) gives it, without the clause of (iv) ('C5R'), the save carried by name with its stop in the closing message."""
    import b765_controls as C
    rows = C._rows()
    v = C.verdicts(rows)
    h, pr = v['h'], v['pair']
    if h[0] == 'HELD':
        main_ = git(EF, 'rev-parse', 'refs/remotes/origin/main').strip()
        base_ = [('<commit>', str(pr['commit'])[:8]), ('<hash>', str(pr['sha'])[:16]), ('<commit>', main_[:8])]
        prun = [str(x) for x in pr.get('runs') or ()]
        if v['save_on_main'] == 'AS WANTED':
            sr = v['save_on_main_read'] or {}
            return ('C5', base_ + [('<commit>', str(sr.get('built_ref') or '')[:8])], 'HELD, the save on main AS WANTED (run %s)' % sr.get('run'), v,
                    prun + [str(sr.get('run'))])
        if v['mainsave'] == 'STOPPED' and v['mainsave2'] == 'STOPPED':
            return ('C5R', base_, 'HELD, the save on main STOPPED at both its dispatches (runs %s and %s): [C5] as (R375) gives it, by the author`s '
                    'word on the save on main' % ((v['mainsave_read'] or {}).get('run'), (v['mainsave2_read'] or {}).get('run')), v,
                    prun + [str((v['mainsave_read'] or {}).get('run')), str((v['mainsave2_read'] or {}).get('run'))])
        return None, [], 'H-RUNNER-RESTORE HELD, THE SAVE ON MAIN %s, THE SECOND %s' % (v['mainsave'], v['mainsave2']), v, []
    if h[0] in ('REFUTED', 'NOT SCORABLE'):
        k = 'EXIT 0' if v['planted'] == 'EXIT 0' else 'DIFFERS' if pr['state'] == 'DIFFERS' else 'STOPPED BOTH' if v['stopped_both'] else None
        if not k:
            die('H-RUNNER-RESTORE %s BY A READING [C6] DOES NOT NAME: %s' % (h[0], h[1]))
        opt = '<the planted build exited 0 | the pair\'s axioms files differ | the closing build from source stopped under the hold at both dispatches>'
        return 'C6', [(opt, C6_WHY[k])], '%s, %s' % (h[0], h[1]), v, []
    return None, [], 'H-RUNNER-RESTORE %s (%s)' % (h[0], h[1]), v, []


def statement_field():
    import b765_controls as C
    st = [r for r in C._rows() if r.get('kind') == 'read' and r.get('item') == 'statement']
    ok = [r for r in st if (r.get('statement') or [''])[0] == 'COMPILED' and str(r.get('built_ref') or '').startswith(STATEMENT_COMMIT)]
    return (STATEMENT_COMMIT, ok[0].get('run')) if ok else (None, None)


def gauss_field():
    """the closing commit's restore-on read, exit 0, and its run's axioms file: gaussArchQ's line within the standard three."""
    import b765_controls as C
    rd = [r for r in C._rows() if r.get('kind') == 'read' and str(r.get('built_ref') or '').startswith(CLOSING) and r.get('restore_input') == 'on'
          and r.get('build_exit') == '0' and r.get('item') != 'planted']
    if not rd:
        return None
    r = rd[-1]
    p = os.path.join(C._art(r['run']), 'axioms.txt')
    with open(p, encoding='utf-8', errors='replace') as f:
        t = f.read()
    ax = C.axioms_of(t).get(GAUSS)
    if ax is None or not set(ax) <= set(STANDARD) or hashlib.sha256(t.replace('\r', '').encode('utf-8')).hexdigest() != r.get('axioms_sha256'):
        return None
    return dict(run=r['run'], name=GAUSS, commit=CLOSING, print='[%s]' % ', '.join(ax))


def window_field(X):
    L = rdl('b765_window.txt')
    m = [re.match(r'^  M 16 d 3 \(REGISTERED\): S (-?[\d.]+ \+- [\d.e+-]+) ; .*; nonzero c_j (\d+) of (\d+) ; .*; the ball HELD ;', l) for l in L]
    m = [x for x in m if x]
    held = '  H-SPLINE-WINDOW: HELD' in L
    s = re.search(r'THE SENTENCES\. HELD: "(.+?)" REFUTED:', X['G2'][2])
    if not m or not held or not s:
        return None
    sent = s.group(1)
    if not sent.endswith('.'):
        return None
    return dict(ball=m[0].group(1), n=m[0].group(2), sentence=fill(sent[:-1], [('<ball>', m[0].group(1)), ('<n>', m[0].group(2))]))


def premise_field():
    L = rdl('b765_premise_positions.txt')
    m = [re.match(r'^### ### \*\*PREMISES 18: A HYPOTHESIS BY DESIGN (\d+), DERIVED (\d+), OF THE HYPOTHESIS`S STRENGTH (\d+), NONE OF THESE COMPILED (\d+) ; '
                  r'THE CONTROL AS WANTED ; NO ORDER RETIRED\.\*\*$', l) for l in L]
    m = [x for x in m if x]
    if not m or sum(int(x) for x in m[-1].groups()) != 18:
        return None
    return m[-1].groups()


def map_field():
    L = rdl('b765_map_pair.txt')
    n = [re.match(r'^  the two files differ in (\d+) lines \((\d+) of SPIRAL_MAP_v0_7\.md and (\d+) of SPIRAL_MAP\.md\), in (\d+) ranges$', l) for l in L]
    a = [re.match(r'^  a reader of SPIRAL_MAP_v0_7\.md alone does not see the (\d+) lines of SPIRAL_MAP\.md in them, written by (.+)$', l) for l in L]
    n, a = [x for x in n if x], [x for x in a if x]
    if not n or not a:
        return None
    acts = [w.split()[0] for w in a[0].group(2).split(', ') if re.match(r'^b\d+ \d+$', w)]
    if not acts:
        return None
    return dict(n=n[0].group(1), acts=acts, words=', '.join(acts[:-1]) + ' and ' + acts[-1] if len(acts) > 1 else acts[0])


def branch_field():
    L = rdl('b765_held_branches.txt')
    i = L.index('## THE READING')
    got = {}
    for l in L[i + 1:]:
        m = re.match(r'^  ([\w-]+): (.+)$', l)
        if m and m.group(1) in BRANCHES:
            got[m.group(1)] = m.group(2)
    if sorted(got) != sorted(BRANCHES) or '  no branch removed' not in L[i + 1:]:
        return None
    d = re.match(r'^carried on main by (\d+) of its (\d+) declarations \(([^)]*)\); (.+?) still owed under (W-ORD-[A-Z0-9-]+)$', got[BRANCHES[0]])
    if not d:
        return None
    parts = ['%s carried on main by %s of its %s declarations (%s) and its other %d (%s) still owed under %s' % (
        BRANCHES[0], d.group(1), d.group(2), d.group(3), int(d.group(2)) - int(d.group(1)), d.group(4), d.group(5))]
    parts += ['%s %s' % (b, got[b]) for b in BRANCHES[1:]]
    return '; '.join(parts)


def pi01_reason():
    L = rdl('b765_pi01_reading.txt')
    ok = any(l.startswith('### ### **ADDRESSES NAMED 2 ; REACHED AND READ 1 ; NOT REACHED 1.**') for l in L)
    return 'an address was not reached' if ok else None


def upstream_field():
    ev = NL.join(rdl('b765_events.txt'))
    ok = 'the pin\'s commit is held in it and\n     is an ancestor of HEAD' in ev or "the pin's commit is held in it and is an ancestor of HEAD" in ev.replace(NL + '     ', ' ')
    return 'present at its pin' if ok else None


# ================================================================================ THE LEDGER
def compose(date, base):
    X = texts(ferry())
    W = words()
    TP = templates(X, W)
    rk0, rvals, rwhy, rv, rruns = runner()
    rk = rk0
    if rk0 == 'C5R':
        # ### the author's word on the save on main, a second stop: [C5] as (R375) gives it, its text at the ferry's :54 unchanged
        TP['C5'] = X['C5'][2]
        rk = 'C5'
    c5form = ('the ruling`s, without the clause of the word`s (iv)' if rk0 == 'C5R' else 'with the word`s (iv) at its end') if rk == 'C5' else None
    wcite = ':12-:15' + (', :26' if rk0 == 'C5' else '') + (', :30-:36' if rk == 'C5' else '')
    st, st_run = statement_field()
    ga = gauss_field()
    wi = window_field(X)
    pm = premise_field()
    mp = map_field()
    br = branch_field()
    pi = pi01_reason()
    up = upstream_field()
    E, miss = {}, []
    if rk:
        E[rk] = fill(TP[rk], rvals)
    else:
        miss.append('[C5]/[C6]: %s' % rwhy)
    if st:
        E['S1'] = fill(TP['S1'], [('<commit>', st)])
    else:
        miss.append('[S1]: no statement read COMPILED at %s' % STATEMENT_COMMIT)
    if ga:
        E['S2'] = fill(TP['S2'], [('<name>', ga['name']), ('<commit>', ga['commit']), ('<print>', ga['print'])])
    else:
        miss.append('[S2]: no read of %s within the standard three at %s' % (GAUSS, CLOSING))
    if wi:
        E['W1'] = fill(TP['W1'], [('<the HELD sentence of [G2]>', wi['sentence'])])
    else:
        miss.append('[W1]: the window not read HELD')
    if pm:
        E['Q1'] = fill(TP['Q1'], [('<n>', x) for x in pm])
    else:
        miss.append('[Q1]: the positions` foot not read')
    if mp:
        E['M3'] = fill(TP['M3'], [('<n>', mp['n']), ('<the acts>', mp['words'])])
    else:
        miss.append('[M3]: the map`s figures not read')
    if br:
        E['B2'] = TP['B2'].replace(OUTER, br, 1) if OUTER in TP['B2'] else die('[B2]`S FIELD NOT IN ITS TEMPLATE')
    else:
        miss.append('[B2]: the held branches` reading not read')
    if pi:
        E['H4'] = fill(TP['H4'], [('<the forms of the texts differ | an address was not reached>', pi)])
    else:
        miss.append('[H4]: the reading`s foot not read as NOT REACHED')
    E['T1'], E['T2'] = TP['T1'], TP['T2']
    if up:
        E['T3'] = fill(TP['T3'], [('<present at its pin | absent>', up)])
    else:
        miss.append('[T3]: the upstream read not found')
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b765, `(R375)`(4) to (9) and the author’s words of 2026-11-21: the lines the ruling orders for OPEN_TRAILS** '
            '(relay data/b765_ferry.txt :53-:115; data/b765_author_words_preseal.txt %s), appended at the end of the file after b764’s '
            'trail (its last line :%d) and before this act’s own trail, so that no line of the trail moves: the runner’s cache by its outcome; the '
            'statement of the control’s failure; Gauss’s integral for the archimedean term; the window banked as data; the four readings beside the '
            'dispatches; the three lines of the author’s word of 2026-11-20. The line of the project’s mirror repository is entered in this act’s '
            'trail, after the repository is written at the close.' % (date, wcite, n_ot))
    order = ['C5', 'C6', 'S1', 'S2', 'W1', 'Q1', 'M3', 'B2', 'H4', 'T1', 'T2', 'T3']
    paras = [head] + [E[k] for k in order if k in E]
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    return dict(X=X, TP=TP, E=E, miss=miss, text=ot, new=base + NL + ot + NL, head=head, order=order, runner=(rk0, rwhy, rruns), v=rv,
                st_run=st_run, ga=ga, wi=wi, pm=pm, mp=mp, n_ot=n_ot, c5form=c5form, wcite=wcite)


def ledgers(mode):
    from standing import orders as O
    date = today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    C = compose(date, base)
    E, new, TP = C['E'], C['new'], C['TP']
    I, acct = ids(), account()
    eq = {}
    for k, v in E.items():
        eq[k] = bool(re.fullmatch(pattern(TP[k]), v, re.S)) and (NL + v + NL) in (NL + C['text'] + NL)
    left = sorted(set(m for m in FIELD.findall(C['text'])))
    ticks = [k + 1 for k, l in enumerate(C['text'].split(NL)) if l.count('`') % 2]
    import b765_controls as CT
    runs_known = set(str(r.get('run')) for r in CT._rows() if r.get('kind') == 'read')
    rk, rwhy, rruns = C['runner']
    st = lambda R, n: (R.get(n) or {}).get('status')   # noqa: E731
    before = dict(O.read(base.split(NL)))
    after = dict(O.read(new.split(NL)))
    moved = sorted(n for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    open_b = sum(1 for n in before if st(before, n) == 'OPEN')
    open_a = sum(1 for n in after if st(after, n) == 'OPEN')
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(C['text'], I, acct)
    present = [k for k, v in E.items() if v in base]
    ctl = [('PLACE-papers` HEAD the corrigendum`s commit %s, the act`s one commit there before this write (%s)' % (C1PP, pp_head[:8]), pp_head.startswith(C1PP)),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('each text as entered equals the ruling`s with its fields filled ([C5] %s, [T3] with the word`s clause, [H4] '
            'the word`s), each whole in the appended text: %s' % (C['c5form'] or 'not entered', ' '.join('%s %s' % (k, eq[k]) for k in sorted(eq))),
            bool(eq) and all(eq.values())),
           ('every text of the order composed (%s)' % ('; '.join(C['miss']) or 'none missing'), not C['miss']),
           ('no field left in the appended text (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('none of the texts in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('the runner`s line by the dispatch tool`s reading: %s, [%s] ; each run it cites a read row of data/b765_dispatch_rows.json (%s)' % (
               rwhy, rk or 'NONE', rruns or 'none'), bool(rk) and all(x in runs_known for x in rruns)),
           ('[S1]: the statement read COMPILED at %s (run %s)' % (STATEMENT_COMMIT, C['st_run']), 'S1' in E),
           ('[S2]: %s within the standard three at %s (run %s), the axioms file`s sha256 its read row`s' % (GAUSS, CLOSING, (C['ga'] or {}).get('run')), 'S2' in E),
           ('[W1]: H-SPLINE-WINDOW HELD at M 16 d 3, the ball %s with %s coefficients (data/b765_window.txt)' % ((C['wi'] or {}).get('ball'), (C['wi'] or {}).get('n')), 'W1' in E),
           ('[Q1]: the positions` foot %s, summing to 18 (data/b765_premise_positions.txt)' % (C['pm'],), 'Q1' in E),
           ('[M3]: %s lines, the acts of SPIRAL_MAP.md alone %s (data/b765_map_pair.txt)' % ((C['mp'] or {}).get('n'), (C['mp'] or {}).get('acts')), 'M3' in E)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R375)(4) TO (9) AND THE AUTHOR`S WORDS OF 2026-11-21: OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, utc()), '',
         '### tools/b765_rulings.py ledgers; PLACE-papers HEAD %s; the texts from the ferry bank (data/b765_ferry.txt :%d-:%d) and the author`s words bank'
         % (pp_head[:8], WANT['C5'][0], WANT['T3'][1]),
         '### (data/b765_author_words_preseal.txt %s), the fields from the act`s banks, the runner`s line by tools/b765_controls.py`s reading of'
         % C['wcite'],
         '### data/b765_dispatch_rows.json (sha256 %s); <DATE> %s; [R1] entered in the act`s trail at the close; each text by line and sha256 here.'
         % (fsha(os.path.join(D, 'b765_dispatch_rows.json')), date), '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed; no condition)',
          '  open before %d -> after %d ; orders %d -> %d ; added %s' % (open_b, open_a, len(before), len(after), [(n, st(after, n)) for n in added] or 'none'),
          '  statuses moving: %s' % ([(n, st(before, n), st(after, n)) for n in moved] or 'none')]
    nl_ = new.split(NL)
    first = C['n_ot'] + 2
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        C['n_ot'], len(nl_) - 1, first, sha(C['text'])[:16], sha(base)[:16], sha(new)[:16])]
    P += ['', '## THE PARAGRAPHS BY LINE: head :%d (sha256 %s) ; ' % (nl_.index(C['head']) + 1, sha(C['head'])[:16]) + ' ; '.join(
        '%s :%d (sha256 %s)' % (k, nl_.index(E[k]) + 1, sha(E[k])[:16]) for k in C['order'] if k in E)]
    keys = [k for k in C['order'] if k in E]
    P += ['', '### ### **THE LEDGERS: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINES UNDER ONE HEAD (%s) ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
        len(keys), ', '.join(keys), sum(1 for _w, o in ctl if o), len(ctl), ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(C['text'])
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    if os.path.exists(LBANK):
        die('THE BANK STANDS ALREADY')
    if any(idcount(NL.join(P), I, acct).values()):
        die('AN IDENTIFIER OR THE ACCOUNT IN THE BANK')
    with open(os.path.join(PP, OT), 'wb') as f:
        f.write(new.encode('utf-8'))
    if fsha(os.path.join(PP, OT)) != sha(new)[:16]:
        die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    put(LBANK, NL.join(P) + NL)
    put(LJSON, json.dumps(dict(at=utc(), act=ACT, date=date, pp_head=pp_head, file=dict(path=OT, lines_before=C['n_ot'], lines_after=len(nl_) - 1,
                                                                                         first_new=first, sha_before=sha(base)[:16], sha_after=sha(new)[:16],
                                                                                         text_sha=sha(C['text'])[:16], prefix=new.startswith(base)),
                               entered=dict((k, [nl_.index(t) + 1, sha(t)[:16]]) for k, t in E.items()), head=[nl_.index(C['head']) + 1, sha(C['head'])[:16]],
                               runner=dict(key=rk, why=rwhy, runs=rruns), keys=keys,
                               roster=dict(before_open=open_b, after_open=open_a, added=added, moved=[[n, st(before, n), st(after, n)] for n in moved]),
                               controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; data/b765_ledgers.txt and .json')


def main(argv):
    what, mode = (argv + ['', ''])[:2]
    if what != 'ledgers' or mode not in ('dry', 'write'):
        sys.exit(__doc__)
    ledgers(mode)


if __name__ == '__main__':
    main(sys.argv[1:])
