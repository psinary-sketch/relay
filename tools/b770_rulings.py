# -*- coding: utf-8 -*-
"""tools/b770_rulings.py -- b770, (R380)(7), (6), (4) and (13): THE TEXTS OF THE RULING ENTERED IN OPEN_TRAILS, BY GROUP.

Carried in form from tools/b768_rulings.py's ledgers route (the texts read from the ferry bank between their marker lines and checked
against their lines; the file appended at its end, its bytes at HEAD a prefix of its new bytes; the controls before the write; the ledger
banked by line and sha256) by the Write tool, and committed before its run (N2). (R380)(12) writes neither REGISTRY, ERRATA, the census,
the register nor SPIRAL_MAP.md, so OPEN_TRAILS is the one file here.

  ledgers c2 dry|write   Component 2 (data/b770_ferry.txt :119: "THE RULINGS, [A5], per (7)"; :31: "THE RULINGS, each by the author's
                         ratification of this clause, are entered as [A5], one line"), appended at OPEN_TRAILS' end, no line moving, <DATE>
                         the UTC date of the write: one dated head and under it --
                         [A5] (data/b770_ferry.txt :52), as written; it names one order, W-ORD-LI-INDEX at its (k), with no status word,
                           so the order stays OPEN: (6) reads it at this act and [I1] or [I2] gives its entry later in Component 2.
                         The text carries no field. Controls before the write, printed, among them a planted status word read by the rule
                         (a check that can fire); the roster by tools/standing/orders.py's rule in memory, before and after: no order added
                         and none moving. Bank: data/b770_ledgers_c2.txt and .json, the text by line and sha256; its words printed by the
                         dry run alone.
  ledgers c2i dry|write  Component 2 ((6), data/b770_ferry.txt :29: "Where the tool's three sentences agree with that reading, [I1] is
                         entered ...; where one does not, [I2] is entered"): [I1] where data/b770_li_index.json reads AS READ, else [I2], its
                         fields filled from that bank (for 5938, 10034 and 5101 in turn, its primary cite's path and line and its defining
                         sentence's opening; for [I2] the figures failing), appended beneath [A5]'s dated head at OPEN_TRAILS' end with no
                         head of its own (the head says the index banks' line is appended beneath it). The bank committed and unmodified
                         before the write, read as a control. Bank: data/b770_ledgers_c2i.txt and .json. Added by an Edit committed before
                         its run (b770, after tools/b770_li_index.py's write).
  ledgers c2s dry|write  Component 2 ((7), data/b770_ferry.txt :31: "[S5] is entered"): [S5], its fields filled from
                         data/b770_recut_inputs.json's s5 (after the author's answer, data/b770_author_answers.txt) and the agenda's items,
                         appended beneath [I1] with no head of its own. [S5] names no order: its planted control sets an order's name with a
                         status word into it, read in memory alone. The inputs and agenda banks committed and unmodified before the write,
                         read as controls. Bank: data/b770_ledgers_c2s.txt and .json. Added by an Edit committed before its run (b770, after
                         the inputs bank's write).
  ledgers c3 dry|write   Component 3's end ((4), data/b770_ferry.txt :25: "Each compiled theorem is read at its statement by the E0 gate
                         before it is entered"): [Z1], [U1], [D1] and [L1] (data/b770_ferry.txt :56, :64, :72, :80), each where its step
                         compiles, under one dated head appended at OPEN_TRAILS' end beneath [S5], no line moving: <commit> the act's last
                         restored read exiting 0 by tools/b770_controls.py verdicts() over data/b770_dispatch_rows.json (the bank committed
                         and unmodified, a control); <name> and <names> the step's theorems, each COMPILED in that read; <the print> their
                         axioms print from the read. Every theorem of the act (ACT_NAMES, (b) to (g)) found once by its declaration line
                         among the act's six files at the commit, read at its statement (from its name to its first `:=`) and graded by
                         tools/e0_rule.py grade(head, 'theorem'), its lexicon extended in this tool by the one Prop the act declares as a
                         premise (E0_EXTENSION, the shared file not edited); the position each text states read against the gate; [D1]'s
                         premises read; [Z1]'s import closure read with a control that holds the folder, and its "two proofs of one
                         statement" read against zq_offline_zero's statement; the plan's kind printed beside the gate (a reading, no
                         control). (f) and (g) take no line (data/b770_author_words_preseal.txt :8). A step not COMPILED holds the group:
                         its CARRIED text comes by a later Edit. Bank: data/b770_ledgers_c3.txt and .json. Added by an Edit committed
                         before its run (b770, after dispatch 6's read).
  ledgers c4 dry|write   Component 4 ((4) MAIN AND THE TAG, data/b770_ferry.txt :25; (5) :27): [C11] where tools/b770_controls.py
                         verdicts() over data/b770_dispatch_rows.json (committed and unmodified, a control) reads the closing build from
                         source and its one repeat each stopped under the hold, <commit> the closing Lean commit, <ids> their runs and
                         <figures> their runners' lows; [C10] where it reads the pair's axioms files differing, the source build's sha256
                         first; neither, a refusal (main moves, no line). Appended beneath [L1] with no head of its own (the c3 head names
                         it), no line moving; the order the text names OPEN by tools/standing/orders.py's rule after it and no other order
                         moving; a planted pair read as the decision's failure. Bank: data/b770_ledgers_c4.txt and .json. Added by an Edit
                         committed before its run (b770, after dispatch 7's read).
The later texts -- each of (4)'s CARRIED texts -- are groups this tool gains by an Edit committed before its run; their lines are checked
here already (WANT).

No line of the papers` repository is printed but the texts this tool composes; the account is counted, never printed; no git write.
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
import b770_worklist as K   # noqa: E402

ACT, NL = 'b770', '\n'
PP = K.PP
FERRY = os.path.join(D, 'b770_ferry.txt')
FERRY_SHA = '98b6e4d17af39cce'   # ### data/b770_stepzero.txt :12: the ferry bank's sha256
OT = 'OPEN_TRAILS.md'
C1PP = '11fe9707'                # ### the papers` repository's one commit of the act before this write: the corrigendum (step 12, data/b770_events.txt (52))
# ### each text of the ruling by its first and last line in the ferry bank (data/b770_ferry.txt :49-:105), read by texts() at every run
WANT = dict(A5=(52, 52), Z1=(56, 56), Z2=(60, 60), U1=(64, 64), U2=(68, 68), D1=(72, 72), D2=(76, 76), L1=(80, 80), L2=(84, 84),
            C10=(88, 88), C11=(92, 92), I1=(96, 96), I2=(100, 100), S5=(104, 104))
FIELD = re.compile(r'<[A-Za-z][^<>\n]*>')
LI_INDEX = 'W-ORD-LI-INDEX'      # ### the one order [A5] names, at its (k) (data/b770_ferry.txt :52)
GROUPS = dict(c2=('A5',), c2i=('I1',), c2s=('S5',), c3=('Z1', 'U1', 'D1', 'L1'), c4=('C10', 'C11'))   # ### c2i: [I1], or [I2] where data/b770_li_index.json reads NOT AS READ (set at run time)
# ### the papers` repository's HEAD before each group's write: c2 after the corrigendum (step 12), c2i after [A5] (step 29), c2s after [I1] (step 38),
# ### c3 after [S5] (step 44), c4 after [Z1] to [L1] (step 55)
PP_BEFORE = dict(c2=C1PP, c2i='f945cbd9', c2s='c599930d', c3='a0ac08c9', c4='c0146cf4')
CLAUSE = dict(c2='7', c2i='6', c2s='7', c3='4', c4='4')
# ### the planted status word set after the order's name in each text, read in memory alone; [S5] names no order, so its plant sets one into it
PLANTS = dict(A5=(LI_INDEX + ' is read', LI_INDEX + ' CLOSED, is read'), I1=('`%s` READ' % LI_INDEX, '`%s` CLOSED, READ' % LI_INDEX),
              I2=('`%s` READ' % LI_INDEX, '`%s` CLOSED, READ' % LI_INDEX),
              S5=('no keystone written.', 'no keystone written; `%s` CLOSED.' % LI_INDEX))
NAMES_WANT = dict(A5=[LI_INDEX], I1=[LI_INDEX], I2=[LI_INDEX], S5=[])   # ### the orders each text names
LI_JSON = os.path.join(D, 'b770_li_index.json')
LI_REL = 'data/b770_li_index.json'
S5_REL, AG_REL = 'data/b770_recut_inputs.json', 'data/b770_sitting_agenda.json'


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


def ids():
    import b770_address_scan as SC
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


def pattern(tpl):
    pat = re.escape(tpl)
    for ph in sorted(set(FIELD.findall(tpl)), key=len, reverse=True):
        pat = pat.replace(re.escape(ph), '(.+?)')
    return pat


def fill(tpl, vals):
    """the template with its fields filled in reading order by `vals`, one value a field."""
    parts, fields = FIELD.split(tpl), FIELD.findall(tpl)
    if len(fields) != len(vals):
        die('THE FIELDS (%d) AND THE VALUES (%d) DIFFER IN NUMBER' % (len(fields), len(vals)))
    return ''.join(p + (vals[i] if i < len(vals) else '') for i, p in enumerate(parts))


def opening(s, n=200):
    """a defining sentence's opening: the sentence whole to n characters, its closing stop taken off; else cut at a word and marked."""
    s = s.strip().rstrip('.')
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + ' ...'


def li_fill():
    """(key, values, the bank) for [I1] or [I2] from data/b770_li_index.json: for 5938, 10034 and 5101 in turn, its primary cite's path and
    line and its defining sentence's opening; for [I2] the figures failing after them."""
    with open(LI_JSON, encoding='utf-8') as f:
        J = json.load(f)
    key = 'I1' if J['reading'] == 'AS READ' else 'I2'
    vals = []
    for fig in ('5938', '10034', '5101'):
        c = J['cites'][J['primary'][fig]]
        vals += ['%s :%d' % (c['path'], c['want']), opening(c['sentence'])]
    if key == 'I2':
        vals.append(', '.join(J['failing']))
    return key, vals, J


def s5_fill():
    """[S5]'s seven fields in reading order from data/b770_recut_inputs.json's s5 and the agenda's items: <n>, <k>, <c>, <b>, <c | none>,
    the passed items and the struck items, each item by its number and its act."""
    with open(os.path.join(RELAY, S5_REL), encoding='utf-8') as f:
        s = json.load(f)['s5']
    with open(os.path.join(RELAY, AG_REL), encoding='utf-8') as f:
        acts = dict((i['n'], i['act']) for i in json.load(f)['items'])

    def lst(ns):
        return ', '.join('%d %s' % (n, acts[n]) for n in ns) or 'none'
    return [str(s['n']), str(s['k']), str(s['c']), str(s['b']), str(len(s['asked'])) if s['asked'] else 'none', lst(s['passed']), lst(s['struck'])]


# ================================================================================ THE LEDGER
def compose(group, date, base):
    X = texts(ferry())
    TP = dict((k, X[k][2]) for k in X)
    keys = GROUPS[group]
    fills = {}
    if group == 'c2i':
        key, vals, _J = li_fill()
        keys = (key,)
        fills[key] = vals
    if group == 'c2s':
        fills['S5'] = s5_fill()
    E = dict((k, fill(TP[k], fills[k]) if k in fills else TP[k]) for k in keys)
    n_ot = len(base.split(NL)) - 1
    head = None
    if group == 'c2':
        head = ('**Dated head, %s, b770, `(R380)`(7): the line the ruling orders for OPEN_TRAILS at Component 2** (relay '
                'data/b770_ferry.txt :31 and :51-:53), appended at the end of the file (its last line :%d), so that no line before it moves: '
                'the author’s rulings of 2026-11-26 by [A5]. The lines of the two index banks and of the sitting are appended beneath it in '
                'Component 2, and those of the statements and of the closing build from source at Component 3 and after.' % (date, n_ot))
    paras = ([head] if head else []) + [E[k] for k in keys]
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    return dict(X=X, TP=TP, E=E, text=ot, new=base + NL + ot + NL, head=head, keys=keys, n_ot=n_ot, paras=paras, fills=fills)


def ledgers(group, mode):
    from standing import orders as O
    date = today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    C = compose(group, date, base)
    E, new, TP, text = C['E'], C['new'], C['TP'], C['text']
    I, acct = ids(), account()
    eq = dict((k, bool(re.fullmatch(pattern(TP[k]), v, re.S)) and (NL + v + NL) in (NL + text + NL)) for k, v in E.items())
    fields_in = sorted(k for k in C['keys'] if FIELD.findall(TP[k]))
    left = sorted(set(FIELD.findall(text)))
    ticks = [k + 1 for k, l in enumerate(text.split(NL)) if l.count('`') % 2]
    st = lambda R, n: (R.get(n) or {}).get('status')   # noqa: E731
    bl, nl_ = base.split(NL), new.split(NL)
    before, after = dict(O.read(bl)), dict(O.read(nl_))
    moved = sorted(n for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    open_b = sum(1 for n in before if st(before, n) == 'OPEN')
    open_a = sum(1 for n in after if st(after, n) == 'OPEN')
    hf = O.hand_flags(nl_)
    in_hand = [i + 1 for i in range(C['n_ot'], len(hf)) if hf[i]]
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(text, I, acct)
    present = [k for k, v in E.items() if v in base]
    k0 = C['keys'][0]
    a5_names = sorted(set(O.NAME.findall(E[k0])))
    a5_status = dict((n, O._status(O.mask(E[k0]), n)) for n in a5_names)
    planted = E[k0].replace(PLANTS[k0][0], PLANTS[k0][1], 1)
    p_status = O._status(O.mask(planted), LI_INDEX) if planted != E[k0] else None
    p_after = dict(O.read(bl + [planted]))
    extra = []
    if group == 'c2i':
        tracked = git(RELAY, 'show', 'HEAD:' + LI_REL, raw=True)
        with open(LI_JSON, 'rb') as f:
            wb = f.read()
        extra = [('the index bank %s committed at HEAD and its working file equal to it (%d bytes)' % (LI_REL, len(wb)),
                  bool(tracked) and tracked == wb),
                 ('[A5] the last line of OPEN_TRAILS before the write, so [%s] stands beneath its dated head' % k0,
                  [l for l in bl if l.strip()][-1:] == [TP['A5']])]
    if group == 'c2s':
        for rel in (S5_REL, AG_REL):
            tracked = git(RELAY, 'show', 'HEAD:' + rel, raw=True)
            with open(os.path.join(RELAY, rel), 'rb') as f:
                wb = f.read()
            extra.append(('the bank %s committed at HEAD and its working file equal to it (%d bytes)' % (rel, len(wb)), bool(tracked) and tracked == wb))
        last = [l for l in bl if l.strip()][-1:]
        extra.append(('[I1] as entered the last line of OPEN_TRAILS before the write, so [S5] stands beneath [A5]`s dated head after it',
                      bool(last) and bool(re.fullmatch(pattern(TP['I1']), last[0], re.S))))
    ctl = [('the papers` repository`s HEAD %s, the act`s last commit there before this write (%s)' % (PP_BEFORE[group], pp_head[:8]),
            pp_head.startswith(PP_BEFORE[group])),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('the text as entered equals the ruling`s, whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq[k]) for k in C['keys'] if k in eq)), len(eq) == len(C['keys']) and all(eq.values())),
           ('each text with fields in the ruling filled from its bank (with fields %s ; filled %s), and no field left in the appended text '
            '(%s)' % (fields_in or 'none', sorted(C['fills']) or 'none', left or 'none'), fields_in == sorted(C['fills']) and not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('the text not in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('[%s] names the orders wanted (%s), %s in OPEN_TRAILS before the write, OPEN by the rule (the orders [%s] names: %s)' % (
               k0, NAMES_WANT[k0] or 'none', LI_INDEX, k0, a5_names or 'none'),
            a5_names == NAMES_WANT[k0] and LI_INDEX in before and st(before, LI_INDEX) == 'OPEN'),
           ('[%s] gives the orders it names no status word by the rule (%s): each stays as it stood' % (
               k0, ' '.join('%s %s' % (n, s or 'none') for n, s in sorted(a5_status.items())) or 'it names none'),
            (not NAMES_WANT[k0] and not a5_status) or (bool(a5_status) and not any(a5_status.values()))),
           ('PLANTED: [%s] with a status word set after the order`s name, read in memory alone, reads a status (%s) and moves the order to %s' % (
               k0, p_status, st(p_after, LI_INDEX)), bool(p_status) and p_status[0] == 'CLOSED' and st(p_after, LI_INDEX) == 'CLOSED'),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: no order moving and none added (moved %s ; added %s)' % (
               [(n, st(before, n), st(after, n)) for n in moved] or 'none', added or 'none'), not moved and not added)] + extra
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R380)(%s), GROUP %s: %s, OPEN_TRAILS, APPENDED AT ITS END (%s)' % (
        ACT, CLAUSE[group], group.upper(), ' '.join('[%s]' % k for k in C['keys']), utc()), '',
         '### tools/b770_rulings.py ledgers %s; the papers` repository at HEAD %s; the texts from the ferry bank (data/b770_ferry.txt, sha256 %s);'
         % (group, pp_head[:8], FERRY_SHA),
         '### <DATE> %s; the text by line and sha256 here; no line of the papers` repository printed but the text composed.' % date, '',
         '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  open before %d -> after %d ; orders %d -> %d ; added %s' % (open_b, open_a, len(before), len(after), added or 'none'),
          '  statuses moving: %s' % ([(n, st(before, n), st(after, n)) for n in moved] or 'none')]
    first = C['n_ot'] + 2
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        C['n_ot'], len(nl_) - 1, first, sha(text)[:16], sha(base)[:16], sha(new)[:16])]
    rows = ([('head', C['head'])] if C['head'] else []) + [(k, E[k]) for k in C['keys']]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    P += ['', '### ### **THE LEDGERS, GROUP %s: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINE %s (%s) ; CONTROLS %d OF %d '
          'AS WANTED ; %s.**' % (group.upper(), len(C['keys']), 'UNDER ONE HEAD' if C['head'] else 'BENEATH [A5]`S DATED HEAD',
                                 ' '.join('[%s]' % k for k in C['keys']), sum(1 for _w, o in ctl if o), len(ctl),
                                 ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(text)
        return 0 if ok else 1
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b770_ledgers_%s.txt' % group), os.path.join(D, 'b770_ledgers_%s.json' % group)
    if os.path.exists(lb) or os.path.exists(lj):
        die('THE BANK STANDS ALREADY')
    if any(idcount(NL.join(P), I, acct).values()):
        die('AN IDENTIFIER OR THE ACCOUNT IN THE BANK')
    with open(os.path.join(PP, OT), 'wb') as f:
        f.write(new.encode('utf-8'))
    if fsha(os.path.join(PP, OT)) != sha(new)[:16]:
        die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    put(lb, NL.join(P) + NL)
    put(lj, json.dumps(dict(at=utc(), act=ACT, group=group, date=date, pp_head=pp_head,
                            file=dict(path=OT, lines_before=C['n_ot'], lines_after=len(nl_) - 1, first_new=first, sha_before=sha(base)[:16],
                                      sha_after=sha(new)[:16], text_sha=sha(text)[:16], prefix=new.startswith(base)),
                            entered=dict((k, [nl_.index(v) + 1, sha(v)[:16]]) for k, v in E.items()),
                            head=[nl_.index(C['head']) + 1, sha(C['head'])[:16]] if C['head'] else None, keys=list(C['keys']),
                            fills=C['fills'],
                            roster=dict(before_open=open_b, after_open=open_a, added=added, moved=[[n, st(before, n), st(after, n)] for n in moved]),
                            controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; %s and .json' % os.path.relpath(lb, RELAY).replace(os.sep, '/'))
    return 0


# ================================================================================ GROUP c3: [Z1], [U1], [D1], [L1]
DROWS_REL = 'data/b770_dispatch_rows.json'
DROWS = os.path.join(RELAY, DROWS_REL)
STD3 = '[propext, Classical.choice, Quot.sound]'
AX3 = {'propext', 'Classical.choice', 'Quot.sound'}
STEP_ITEMS = ('b', 'c', 'd', 'e', 'f', 'g')
# ### each text of (4) with its step and the theorems whose names fill it, in reading order (data/b770_ferry.txt :56, :64, :72, :80)
C3_TEXTS = (('Z1', 'b', ('SIDEExplicitFormula.Schema.ZQ.zq_offline_from_coefficients', 'SIDEExplicitFormula.Schema.online_imp_zeroSideQ_nonneg')),
            ('U1', 'c', ('SIDEExplicitFormula.positive_iff_forall_upto', 'SIDEExplicitFormula.positiveUpto_mono',
                         'SIDEExplicitFormula.h2_sign_upto_iff', 'SIDEExplicitFormula.control_not_positiveUpto',
                         'SIDEExplicitFormula.control_not_positiveUpto_of_le')),
            ('D1', 'd', ('SIDEExplicitFormula.familyConfig_h2_sign', 'SIDEExplicitFormula.positivity_of_premises')),
            ('L1', 'e', ('SIDEExplicitFormula.Window.cQ_least_negative',)))
# ### the position each text states, read against the E0 gate: [Z1] "Its position: DERIVED." of its closing statement (the lemma takes no
# ### position in it); [U1] "Their position: DERIVED."; [D1] "its grade is INTERFACES on those named premises"; [L1] "Its position: DERIVED."
POSITION = {'SIDEExplicitFormula.Schema.ZQ.zq_offline_from_coefficients': 'DERIVES',
            'SIDEExplicitFormula.positive_iff_forall_upto': 'DERIVES', 'SIDEExplicitFormula.positiveUpto_mono': 'DERIVES',
            'SIDEExplicitFormula.h2_sign_upto_iff': 'DERIVES', 'SIDEExplicitFormula.control_not_positiveUpto': 'DERIVES',
            'SIDEExplicitFormula.control_not_positiveUpto_of_le': 'DERIVES',
            'SIDEExplicitFormula.familyConfig_h2_sign': 'INTERFACES', 'SIDEExplicitFormula.positivity_of_premises': 'INTERFACES',
            'SIDEExplicitFormula.Window.cQ_least_negative': 'DERIVES'}
D1_PREMISES = {'RiemannHypothesis', 'DirichletHypothesis'}   # ### (4)(d): Mathlib's RiemannHypothesis and the act's one proposition
# ### the plan's kind for each theorem (data/b770_plan.txt :51, :57, :86, :105, :123, :139, :151), printed beside the gate: a reading, no control
PLAN_KIND = {'SIDEExplicitFormula.Schema.online_imp_zeroSideQ_nonneg': ('DERIVES', 51),
             'SIDEExplicitFormula.Schema.ZQ.zq_offline_from_coefficients': ('DERIVES', 57),
             'SIDEExplicitFormula.positive_iff_forall_upto': ('DERIVES', 86), 'SIDEExplicitFormula.positiveUpto_mono': ('DERIVES', 86),
             'SIDEExplicitFormula.h2_sign_upto_iff': ('DERIVES', 86), 'SIDEExplicitFormula.control_not_positiveUpto': ('DERIVES', 86),
             'SIDEExplicitFormula.control_not_positiveUpto_of_le': ('DERIVES', 86),
             'SIDEExplicitFormula.familyConfig_h2_sign': ('INTERFACES', 105), 'SIDEExplicitFormula.positivity_of_premises': ('INTERFACES', 105),
             'SIDEExplicitFormula.Window.cq_nonneg_ok': ('DERIVES', 123), 'SIDEExplicitFormula.Window.cQ_least_negative': ('DERIVES', 123),
             'SIDEExplicitFormula.Schema.ZQ.OffZero.zq_offline_zero_located': ('DERIVES', 139),
             'SIDEExplicitFormula.Schema.ZQ.zq_ne_zero_of_real_one_lt': ('DERIVES', 151)}
SP4 = ('SIDEExplicitFormula/Schema/ZQ/OffZero/SP4.lean', 'SIDEExplicitFormula.Schema.ZQ.OffZero.zq_offline_zero')
LOCATED = 'SIDEExplicitFormula/Schema/ZQ/OffZero/Located.lean'   # ### the closure's control: a file of the act whose closure holds the folder
DECL_RE = re.compile(r'^(?:@\[[^\]\n]*\]\s*)?(?:(?:protected|private|nonrec)\s+)*(?:theorem|lemma)\s+([^\s(\[{:]+)')
NS_RE, SEC_RE, END_RE = re.compile(r'^namespace\s+(\S+)\s*$'), re.compile(r'^section(?:\s+\S+)?\s*$'), re.compile(r'^end(?:\s+\S+)?\s*$')
DIGITS = re.compile(r'\d{8,}')
# ### the E0 rule's lexicon extended in this tool, the shared tools/e0_rule.py not edited (tools/b768_rulings.py :290-:297's form): the one
# ### Prop this act declares and binds as a premise, read at its declaration line at the commit
E0_EXTENSION = {'DirichletHypothesis': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/Composition.lean :27 (def, b770, (R380)(4)(d): '
                                                'the premise stated as one proposition)')}
E0_EXT_DECL = {'DirichletHypothesis': ('SIDEExplicitFormula/Composition.lean', 27, 'def DirichletHypothesis : Prop :=')}
QUALIFIED_NOTE = ('the rule`s restriction reader (tools/e0_rule.py restriction_case, :404-:413) matches a RESTRICTIONS head written as '
                  'itself, so a binder typed by the qualified `B321.classK k` reads as a premise where `classK k` reads as a restriction')
_EXT = {}


def masked(s):
    """each run of eight digits or more replaced by its length, so that no datum enters a printed row."""
    return DIGITS.sub(lambda m: '#%d-digits' % len(m.group(0)), str(s))


def e0_extend():
    """the extension laid over the shared lexicon once; returns the keys the shared lexicon held before it (wanted none)."""
    import e0_rule as E0
    if 'held' not in _EXT:
        _EXT['held'] = sorted(k for k in E0_EXTENSION if k in E0.LEXICON)
        E0.LEXICON.update(E0_EXTENSION)
    return _EXT['held']


def ax_within(ax):
    s = str(ax or '').strip()
    if not (s.startswith('[') and s.endswith(']')):
        return False
    return set(x.strip() for x in s[1:-1].split(',') if x.strip()) <= AX3


def gate_ok(gates):
    return bool(gates) and all(g['line'] and g['grade'] not in ('NOT READ', 'UNCLASSED') for g in gates)


def decls(src):
    """{full name: [line, ...]} for each theorem or lemma of a Lean source, its namespaces read from `namespace`, `section` and `end`."""
    stack, out = [], {}
    for i, l in enumerate(src.split(NL)):
        m = NS_RE.match(l)
        if m:
            stack.append(m.group(1))
            continue
        if SEC_RE.match(l):
            stack.append(None)
            continue
        if END_RE.match(l):
            if stack:
                stack.pop()
            continue
        m = DECL_RE.match(l)
        if m:
            out.setdefault('.'.join([s for s in stack if s] + [m.group(1)]), []).append(i + 1)
    return out


def head_at(src, line):
    """the statement at a declaration line, from its name to its first `:=`, its whitespace folded."""
    L = src.split(NL)
    m = DECL_RE.match(L[line - 1])
    start = sum(len(x) + 1 for x in L[:line - 1]) + m.end()
    end = src.find(':=', start)
    return src[start:end] if end > 0 else ''


def e0_at(src, line):
    """the theorem's statement at its declaration line graded by tools/e0_rule.py, with the types of the hypotheses the grade read."""
    import e0_rule as E0
    e0_extend()
    head = head_at(src, line)
    try:
        g, why, read = E0.grade(head, 'theorem')
    except Exception as ex:   # noqa: BLE001
        g, why, read = 'UNCLASSED', ' '.join(str(ex).split())[:300], []
    return dict(line=line, grade=g, why=' '.join(str(why).split()), prem=[' '.join(str(t).split()) for _n, t in read])


def nlist(ns):
    b = ['`%s`' % n for n in ns]
    return b[0] if len(b) == 1 else ', '.join(b[:-1]) + ' and ' + b[-1]


def pos_ok(gates):
    G = dict((g['name'], g) for g in gates)
    return all(n in G and G[n]['grade'] == want for n, want in POSITION.items())


def d1_ok(gates):
    G = dict((g['name'], g) for g in gates)
    rows = [G.get(n) for n in C3_TEXTS[2][2]]
    return (all(r and r['grade'] == 'INTERFACES' and r['prem'] and set(r['prem']) <= D1_PREMISES for r in rows)
            and set(rows[-1]['prem']) == D1_PREMISES)


def c3_read():
    import b770_controls as C
    with open(DROWS, encoding='utf-8') as f:
        R = json.load(f)
    lk = C.verdicts(R)['last_kernel']
    if not lk:
        return dict(miss='no restored read exiting 0 in %s' % DROWS_REL)
    commit = str(lk.get('built_ref'))[:8]
    st = dict((x[0], (x[1], x[2])) for x in (lk.get('names') or []))
    built = str(lk.get('build_exit')) == '0' and lk.get('verdict') == 'KERNEL' and bool(lk.get('built_equal'))
    disp = [r for r in R if r.get('kind') == 'dispatch' and r.get('kernel') == C.EF]
    dn = [r.get('n') for r in disp if int(r['run']) == int(lk['run'])]
    later = [r.get('n') for r in disp if dn and r.get('n', 0) > dn[0] and r.get('item') in STEP_ITEMS]
    closing = [r for r in disp if r.get('item') == 'closing']
    pt = set(x.strip() for x in git(C.KPATH, 'show', '%s:print_targets.txt' % commit).split(NL) if x.strip())
    srcs = dict((p, git(C.KPATH, 'show', '%s:%s' % (commit, p)).replace('\r', '')) for p in C.LEAN_FILES)
    where = {}
    for p, s in srcs.items():
        for full, lines in decls(s).items():
            for ln in lines:
                where.setdefault(full, []).append((p, ln))
    gates = []
    for full in C.ACT_NAMES:
        loc = where.get(full, [])
        e = e0_at(srcs[loc[0][0]], loc[0][1]) if len(loc) == 1 else {}
        state, ax = st.get(full, (None, None))
        gates.append(dict(name=full, path=loc[0][0] if len(loc) == 1 else ('NOT FOUND' if not loc else 'IN %d PLACES' % len(loc)),
                          line=e.get('line'), grade=e.get('grade', 'NOT READ'), why=e.get('why', ''), prem=e.get('prem', []), state=state,
                          axioms=ax, plan=PLAN_KIND.get(full, (None, None))))
    ext = [(k, p, ln, p in srcs and len(srcs[p].split(NL)) >= ln and srcs[p].split(NL)[ln - 1] == want)
           for k, (p, ln, want) in sorted(E0_EXT_DECL.items())]
    sp4 = git(C.KPATH, 'show', '%s:%s' % (commit, SP4[0])).replace('\r', '')
    d4 = decls(sp4).get(SP4[1], [])
    zb = where.get(C3_TEXTS[0][2][0], [])
    heads = (' '.join(head_at(sp4, d4[0]).split()) if len(d4) == 1 else None,
             ' '.join(head_at(srcs[zb[0][0]], zb[0][1]).split()) if len(zb) == 1 else None, d4[0] if len(d4) == 1 else None)
    kg = C.import_graph(C.KPATH, commit, ['*.lean'], C.kmodule)
    held = sorted(m for m in C.kernel_closure(C.file_imports(srcs[C.NO_OFFZERO[0]]), kg) if m.startswith(C.NO_OFFZERO[1]))
    ctl_held = sorted(m for m in C.kernel_closure(C.file_imports(srcs[LOCATED]), kg) if m.startswith(C.NO_OFFZERO[1]))
    return dict(lk=lk, commit=commit, built=built, dn=dn[0] if dn else None, later=later, closing=closing, gates=gates, ext=ext,
                held_ext=e0_extend(), pt_act=sorted(n for n in C.ACT_NAMES if n in pt), act=sorted(C.ACT_NAMES),
                read_names=sorted(st), heads=heads, offzero=(C.NO_OFFZERO, held, ctl_held), files=len([p for p in srcs if srcs[p]]))


def ledgers_c3(mode):
    from standing import orders as O
    group, date = 'c3', today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    X = texts(ferry())
    TP = dict((k, X[k][2]) for k in X)
    r = c3_read()
    if r.get('miss'):
        die('[Z1] TO [L1]: %s' % r['miss'])
    gates = r['gates']
    G = dict((g['name'], g) for g in gates)
    E, fills, miss = {}, {}, []
    for key, item, names in C3_TEXTS:
        bad = [n for n in names if G[n]['state'] != 'COMPILED']
        if bad:
            miss.append('[%s] of (4)(%s): not COMPILED in the read: %s' % (key, item, ', '.join(bad)))
            continue
        axs = [str(G[n]['axioms']) for n in names]
        pr = axs[0] if len(set(axs)) == 1 else '; '.join('`%s` %s' % (n, G[n]['axioms']) for n in names)
        vals = (['`%s`' % names[0], r['commit'], '`%s`' % names[1], axs[0]] if key == 'Z1' else [nlist(names), r['commit'], pr])
        fills[key], E[key] = vals, fill(TP[key], vals)
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b770, `(R380)`(4): the lines the ruling orders for OPEN_TRAILS where the statements of (4) compile** (relay '
            'data/b770_ferry.txt :25, :55-:57, :63-:65, :71-:73 and :79-:81), appended at the end of the file (its last line :%d), so that no '
            'line before them moves: each compiled theorem of the Lean of this act read at its statement by the E0 gate (relay tools/e0_rule.py) '
            'before it is entered, its name in print_targets.txt at its commit and its axioms print banked (relay data/b770_dispatch_rows.json '
            'and data/b770_ledgers_c3.txt). The two statements of the author’s word amending (4), (f) and (g), take no line here (relay '
            'data/b770_author_words_preseal.txt :8). Where the closing build from source and the restored build print different axioms files, '
            '[C10] is appended beneath it; where the closing build and its repeat each stop under the hold, [C11].' % (date, n_ot))
    keys = tuple(k for k in GROUPS[group] if k in E)
    paras = [head] + [E[k] for k in keys]
    text = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    new = base + NL + text + NL
    I, acct = ids(), account()
    eq = dict((k, bool(re.fullmatch(pattern(TP[k]), v, re.S)) and (NL + v + NL) in (NL + text + NL)) for k, v in E.items())
    left = sorted(set(FIELD.findall(text)))
    ticks = [k + 1 for k, l in enumerate(text.split(NL)) if l.count('`') % 2]
    st = lambda R_, n: (R_.get(n) or {}).get('status')   # noqa: E731
    bl, nl_ = base.split(NL), new.split(NL)
    before, after = dict(O.read(bl)), dict(O.read(nl_))
    moved = sorted((n, st(before, n), st(after, n)) for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    hf = O.hand_flags(nl_)
    in_hand = [i + 1 for i in range(n_ot, len(hf)) if hf[i]]
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(text, I, acct)
    present = [k for k, v in E.items() if v in base]
    last = [l for l in bl if l.strip()][-1:]
    tracked = git(RELAY, 'show', 'HEAD:' + DROWS_REL, raw=True)
    with open(DROWS, 'rb') as f:
        wb = f.read()
    grades, axs_ = {}, {}
    for g in gates:
        grades[g['grade']] = grades.get(g['grade'], 0) + 1
        axs_[str(g['axioms'])] = axs_.get(str(g['axioms']), 0) + 1
    plant_gate = gate_ok([dict(gates[0], line=None, grade='NOT READ')] + gates[1:]) if gates else True
    plant_pop = (r['act'] + ['SIDEExplicitFormula.b999_planted']) == r['read_names']
    plant_pos = pos_ok([dict(g, grade='INTERFACES') if g['name'] == C3_TEXTS[1][2][0] else g for g in gates])
    nz, held, ctl_held = r['offzero']
    h_sp4, h_zb, sp4_line = r['heads']
    names_c3 = [n for _k, _i, ns in C3_TEXTS for n in ns]
    lk = r['lk']
    differ = [g for g in gates if g['plan'][0] != g['grade']]
    ctl = [('the papers` repository`s HEAD %s, the act`s last commit there before this write (%s)' % (PP_BEFORE[group], pp_head[:8]),
            pp_head.startswith(PP_BEFORE[group])),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('each text as entered equals the ruling`s with its fields filled, each whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq[k]) for k in GROUPS[group] if k in eq)), len(eq) == len(GROUPS[group]) and all(eq.values())),
           ('every text of the group composed (%s)' % ('; '.join(miss) or 'none missing'), not miss),
           ('no field left in the appended text (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('none of the texts in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('[S5] as entered the last line of OPEN_TRAILS before the write, so the dated head of (4) stands beneath it',
            bool(last) and bool(re.fullmatch(pattern(TP['S5']), last[0], re.S))),
           ('the dispatch rows bank %s committed at HEAD and its working file equal to it (%d bytes)' % (DROWS_REL, len(wb)),
            bool(tracked) and tracked == wb),
           ('THE RUN: dispatch %s read, built at %s equal with exit 0, KERNEL (run %s)' % (r['dn'], r['commit'], lk.get('run')), r['built']),
           ('<commit> the act`s last restored read exiting 0 by verdicts(): dispatch %s at %s; no step dispatched after it (%s); the closing '
            'build rows %d' % (r['dn'], r['commit'], r['later'] or 'none', len(r['closing'])), bool(r['commit']) and not r['later']),
           ('each text`s theorems COMPILED in the read, their axioms within %s (%s)' % (STD3, ' '.join(
               '%s %s' % (k, all(G[n]['state'] == 'COMPILED' and ax_within(G[n]['axioms']) for n in ns)) for k, _i, ns in C3_TEXTS)),
            all(G[n]['state'] == 'COMPILED' and ax_within(G[n]['axioms']) for n in names_c3)),
           ('THE POPULATION: the act`s %d theorems (ACT_NAMES, (b) to (g)) each in print_targets.txt at %s (%d) and equal both ways to the names '
            'the read gives (%d)' % (len(r['act']), r['commit'], len(r['pt_act']), len(r['read_names'])),
            r['pt_act'] == r['act'] and r['read_names'] == r['act']),
           ('THE E0 RULE`S LEXICON extended in this tool, tools/e0_rule.py not edited: %s a Prop, read at its declaration line at the commit (%s), '
            'none held by the shared lexicon before (held: %s)' % (', '.join(sorted(E0_EXTENSION)), ' '.join(
                '%s :%d %s' % (k, ln, ok_) for k, _p, ln, ok_ in r['ext']) or 'none', r['held_ext'] or 'none'),
            len(r['ext']) == len(E0_EXTENSION) and all(x[3] for x in r['ext']) and not r['held_ext']),
           ('THE E0 GATE: each of the %d theorems found once by its declaration line among the %d files of the act at the commit, read at its '
            'statement and graded (%s)' % (len(gates), r['files'], ', '.join('%s %d' % kv for kv in sorted(grades.items()))), gate_ok(gates)),
           ('each COMPILED in the read, its axioms within %s, sorryAx in none (the prints: %s)' % (
               STD3, '; '.join('%s %d' % kv for kv in sorted(axs_.items()))),
            bool(gates) and all(g['state'] == 'COMPILED' and ax_within(g['axioms']) for g in gates)),
           ('THE POSITIONS THE TEXTS STATE, read by the gate: [Z1]`s closing statement, [U1]`s five and [L1]`s one DERIVES, [D1]`s two '
            'INTERFACES (%s)' % ' '.join('%s %s' % (n.split('.')[-1], G[n]['grade'] if n in G else 'ABSENT') for n in POSITION), pos_ok(gates)),
           ('[D1]: each statement binds its named premises and nothing else, the premises the gate read within %s and the joined statement '
            'binding both (%s)' % (sorted(D1_PREMISES), '; '.join('%s %s' % (n.split('.')[-1], G[n]['prem']) for n in C3_TEXTS[2][2])), d1_ok(gates)),
           ('[Z1]: its file`s import closure holds no module under %s (held %s), read through the kernel`s import graph at the commit; the '
            'control %s`s closure holding %d' % (nz[1], held or 'none', LOCATED.split('/')[-1], len(ctl_held)), not held and bool(ctl_held)),
           ('[Z1]: two proofs of one statement: %s`s statement equal by its words to %s`s (%s :%s)' % (
               C3_TEXTS[0][2][0].split('.')[-1], SP4[1].split('.')[-1], SP4[0].split('/')[-1], sp4_line), bool(h_sp4) and h_sp4 == h_zb),
           ('PLANTED: a gate row with no statement read as the gate`s failure, a planted name as the population`s, and a [U1] theorem read '
            'INTERFACES as the positions` (%s, %s, %s)' % ('FAILED' if not plant_gate else 'PASSED', 'DIFFER' if not plant_pop else 'EQUAL',
                                                          'FAILED' if not plant_pos else 'PASSED'),
            not plant_gate and not plant_pop and not plant_pos),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: no order moving and none added (moved %s ; added %s)' % (moved or 'none', added or 'none'), not moved and not added)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R380)(4), GROUP C3: %s, OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, ' '.join('[%s]' % k for k in GROUPS[group]), utc()), '',
         '### tools/b770_rulings.py ledgers c3; the papers` repository at HEAD %s; the texts from the ferry bank (data/b770_ferry.txt, sha256 %s),'
         % (pp_head[:8], FERRY_SHA),
         '### the fields from %s (sha256 %s) and SIDE-explicit-formula at %s; <DATE> %s; each text by line and sha256 here; no line of'
         % (DROWS_REL, fsha(DROWS), r['commit'], date),
         '### the papers` repository printed but the texts composed; each run of eight digits or more in a gate row masked by its length.', '',
         '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE E0 GATE (tools/e0_rule.py grade(head, \'theorem\'), the head the statement from the name to its first `:=`, read at %s)'
          % r['commit']]
    P += [masked('  %-62s %s :%s ; GRADE %s ; %s ; %s %s' % (g['name'], g['path'], g['line'], g['grade'], g['why'] or '-', g['state'], g['axioms']))
          for g in gates]
    P += ['', '## THE PLAN`S KIND BESIDE THE GATE (data/b770_plan.txt; a reading, no control): equal %d, differing %d' % (
        len(gates) - len(differ), len(differ))]
    P += ['  DIFFER %s: the plan :%s %s, the gate %s (%s)' % (g['name'], g['plan'][1], g['plan'][0], g['grade'], masked(g['why'])) for g in differ]
    if any('B321.classK' in g['why'] for g in differ):
        P += ['  ### the cause read: ' + QUALIFIED_NOTE + '; the shared rule not edited, the gate`s grade standing, printed for the navigator']
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  orders %d -> %d ; statuses moving %s ; added %s' % (len(before), len(after), moved or 'none', added or 'none')]
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        n_ot, len(nl_) - 1, n_ot + 2, sha(text)[:16], sha(base)[:16], sha(new)[:16])]
    rows = [('head', head)] + [(k, E[k]) for k in keys]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    P += ['', '### ### **THE LEDGERS, GROUP C3: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINES UNDER ONE HEAD (%s) ; THE E0 GATE %d OF %d READ ; '
          'THE PLAN`S KIND DIFFERING %d ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
              len(keys), ' '.join('[%s]' % k for k in keys), sum(1 for g in gates if g['line']), len(gates), len(differ),
              sum(1 for _w, o in ctl if o), len(ctl), ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(text)
        return 0 if ok else 1
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b770_ledgers_c3.txt'), os.path.join(D, 'b770_ledgers_c3.json')
    if os.path.exists(lb) or os.path.exists(lj):
        die('THE BANK STANDS ALREADY')
    if any(idcount(NL.join(P), I, acct).values()):
        die('AN IDENTIFIER OR THE ACCOUNT IN THE BANK')
    with open(os.path.join(PP, OT), 'wb') as f:
        f.write(new.encode('utf-8'))
    if fsha(os.path.join(PP, OT)) != sha(new)[:16]:
        die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    put(lb, NL.join(P) + NL)
    put(lj, json.dumps(dict(at=utc(), act=ACT, group=group, date=date, pp_head=pp_head,
                            file=dict(path=OT, lines_before=n_ot, lines_after=len(nl_) - 1, first_new=n_ot + 2, sha_before=sha(base)[:16],
                                      sha_after=sha(new)[:16], text_sha=sha(text)[:16], prefix=new.startswith(base)),
                            entered=dict((k, [nl_.index(v) + 1, sha(v)[:16]]) for k, v in E.items()), head=[nl_.index(head) + 1, sha(head)[:16]],
                            keys=list(keys), fills=fills, run=lk.get('run'), commit=r['commit'],
                            e0=[dict((x, masked(g[x]) if x == 'why' else g[x]) for x in ('name', 'path', 'line', 'grade', 'why', 'prem', 'state', 'axioms', 'plan'))
                                for g in gates],
                            differ=[g['name'] for g in differ], controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; %s and .json' % os.path.relpath(lb, RELAY).replace(os.sep, '/'))
    return 0


# ================================================================================ GROUP c4: [C10] or [C11]
C4_ORDER = {'C10': 'W-ORD-RUNNER-CACHE', 'C11': 'W-ORD-SOURCE-BUILD'}   # ### the order each text names (data/b770_ferry.txt :88, :92)


def c4_read(R):
    """verdicts() over the rows, the closing build's dispatch rows, and the reads of the build from source and of its repeat."""
    import b770_controls as C
    v = C.verdicts(R)
    disp = [r for r in R if r.get('kind') == 'dispatch' and r.get('kernel') == C.EF]
    reads = dict((int(r['run']), r) for r in R if r.get('kind') == 'read' and r.get('kernel') == C.EF)
    cl = [r for r in disp if r.get('item') == 'closing']
    offs = C._offs(disp, reads, cl[0]) if cl else []
    rep = [r for r in disp if r.get('item') == 'repeat']
    return v, cl, rep, offs, disp


def mb(x):
    return '{:,} MB'.format(x) if isinstance(x, int) else '%s MB' % x


def ledgers_c4(mode):
    import copy
    import b770_controls as C
    from standing import orders as O
    group, date = 'c4', today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    X = texts(ferry())
    TP = dict((k, X[k][2]) for k in X)
    with open(DROWS, encoding='utf-8') as f:
        R = json.load(f)
    v, cl, rep, offs, disp = c4_read(R)
    lk = v['last_kernel'] or {}
    commit = str(lk.get('built_ref'))[:8]
    if v['stopped_both']:
        key = 'C11'
        vals = [commit, ' and '.join(str(o.get('run')) for o in offs), ' and '.join(mb(o.get('runner_low_mb')) for o in offs)]
    elif v['pair']['state'] == 'DIFFERS':
        key = 'C10'
        shas = v['pair']['shas']   # ### (the restored build's, the build from source's); the text reads the source build's first
        vals = [str(v['pair']['commit'])[:8], str(shas[1])[:16], str(shas[0])[:16]]
    else:
        die('[C10] OR [C11]: NEITHER STANDS BY verdicts(): %s ; the pair %s %s' % (v['main'], v['pair']['state'], v['pair'].get('where')))
    order = C4_ORDER[key]
    text = fill(TP[key], vals)
    new = base + NL + text + NL
    n_ot = len(base.split(NL)) - 1
    I, acct = ids(), account()
    left = sorted(set(FIELD.findall(text)))
    ticks = [k + 1 for k, l in enumerate(text.split(NL)) if l.count('`') % 2]
    st = lambda R_, n: (R_.get(n) or {}).get('status')   # noqa: E731
    bl, nl_ = base.split(NL), new.split(NL)
    before, after = dict(O.read(bl)), dict(O.read(nl_))
    moved = sorted((n, st(before, n), st(after, n)) for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    hf = O.hand_flags(nl_)
    in_hand = [i + 1 for i in range(n_ot, len(hf)) if hf[i]]
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(text, I, acct)
    last = [l for l in bl if l.strip()][-1:]
    tracked = git(RELAY, 'show', 'HEAD:' + DROWS_REL, raw=True)
    with open(DROWS, 'rb') as f:
        wb = f.read()
    off_on = [r for r in disp if r.get('restore') == 'off']
    on_n = [r for r in disp if r.get('item') in STEP_ITEMS]
    Rp = copy.deepcopy(R)
    if key == 'C11':
        for r in Rp:
            if r.get('kind') == 'read' and offs and int(r.get('run', 0)) == int(offs[-1]['run']):
                r['verdict'], r['build_exit'] = 'KERNEL', '0'
        plant = C.verdicts(Rp)['stopped_both']
        plant_w = 'the repeat`s read planted as exiting 0 reads the pair not stopped twice'
        pair_ok = (len(cl) == 1 and len(rep) == 1 and len(offs) == 2 and all(o.get('verdict') == C.STOPPED and o.get('build_exit') == '143'
                                                                           and o.get('built_equal') and o.get('built_ref') == lk.get('built_ref')
                                                                           and o.get('restore_input') == 'off' for o in offs)
                   and str(v['main']).startswith('[C11]'))
        pair_w = ('THE PAIR BY verdicts(): the closing build (dispatch %s, run %s) and its one repeat (dispatch %s, run %s) each read %s with the exit '
                  'file 143, the restore off, built equal at %s, the lows %s ; the decision: %s' % (
                      cl[0].get('n') if cl else None, cl[0].get('run') if cl else None, rep[0].get('n') if rep else None,
                      rep[0].get('run') if rep else None, C.STOPPED, commit, ' and '.join(mb(o.get('runner_low_mb')) for o in offs), v['main']))
    else:
        for r in Rp:
            if r.get('kind') == 'read' and offs and int(r.get('run', 0)) == int(offs[-1]['run']):
                r['axioms_sha256'] = v['pair']['shas'][0]
        plant = C.verdicts(Rp)['pair']['state'] == 'DIFFERS'
        plant_w = 'the build from source`s axioms sha256 planted equal to the restored build`s reads the pair not differing'
        pair_ok = v['pair']['state'] == 'DIFFERS' and str(v['main']).startswith('[C10]') and str(v['pair']['commit']) == str(lk.get('built_ref'))
        pair_w = 'THE PAIR BY verdicts(): %s ; the decision: %s' % (v['pair']['where'], v['main'])
    ctl = [('the papers` repository`s HEAD %s, the act`s last commit there before this write (%s)' % (PP_BEFORE[group], pp_head[:8]),
            pp_head.startswith(PP_BEFORE[group])),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('[%s] as entered equals the ruling`s with its fields filled (%s)' % (key, ' | '.join(vals)), bool(re.fullmatch(pattern(TP[key]), text, re.S))),
           ('no field left in the appended text (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('neither [C10] nor [C11] in OPEN_TRAILS before the write', not any(re.search(pattern(TP[k]), base, re.S) for k in ('C10', 'C11'))),
           ('[L1] as entered the last line of OPEN_TRAILS before the write, so the line stands beneath the dated head of (4)',
            bool(last) and bool(re.fullmatch(pattern(TP['L1']), last[0], re.S))),
           ('the dispatch rows bank %s committed at HEAD and its working file equal to it (%d bytes)' % (DROWS_REL, len(wb)),
            bool(tracked) and tracked == wb),
           (pair_w, pair_ok),
           ('<commit> the act`s closing Lean commit, the last restored read exiting 0 (dispatch run %s at %s), the closing build dispatched at it (%s)' % (
               lk.get('run'), commit, str(cl[0].get('sha'))[:8] if cl else None), bool(cl) and cl[0].get('sha') == lk.get('built_ref')),
           ('THE CAP ((R380)(4)): dispatches %d of %d, the restore on %d of %d, the restore off %d (the closing build and at most one repeat)' % (
               len(disp), K.MAX_DISPATCHES, len(on_n), C.ON_CAP, len(off_on)),
            len(disp) <= K.MAX_DISPATCHES and len(on_n) <= C.ON_CAP and len(off_on) <= 2),
           ('PLANTED: %s (%s)' % (plant_w, 'NOT AS THE PAIR' if not plant else 'AS THE PAIR'), not plant),
           ('THE ORDER [%s] NAMES, %s: OPEN by the rule after the write (before %s, after %s)' % (key, order, st(before, order), st(after, order)),
            order in after and st(after, order) == 'OPEN'),
           ('the roster: no order but %s moving and none added (moved %s ; added %s)' % (order, moved or 'none', added or 'none'),
            all(m[0] == order for m in moved) and not added),
           ('the appended line outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R380)(4), GROUP C4: [%s], OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, key, utc()), '',
         '### tools/b770_rulings.py ledgers c4; the papers` repository at HEAD %s; the text from the ferry bank (data/b770_ferry.txt, sha256 %s);'
         % (pp_head[:8], FERRY_SHA),
         '### the fields from %s (sha256 %s) by tools/b770_controls.py verdicts(); <DATE> %s; no line of the papers` repository printed but the'
         % (DROWS_REL, fsha(DROWS), date),
         '### text composed.', '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  orders %d -> %d ; statuses moving %s ; added %s' % (len(before), len(after), moved or 'none', added or 'none')]
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended line at :%d (sha256 %s) | the file`s sha256 %s -> %s' % (
        n_ot, len(nl_) - 1, n_ot + 2, sha(text)[:16], sha(base)[:16], sha(new)[:16])]
    P += ['', '### ### **THE LEDGERS, GROUP C4: OPEN_TRAILS APPENDED, NO LINE MOVING ; [%s] ; %s ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
        key, v['main'], sum(1 for _w, o in ctl if o), len(ctl), ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(text)
        return 0 if ok else 1
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b770_ledgers_c4.txt'), os.path.join(D, 'b770_ledgers_c4.json')
    if os.path.exists(lb) or os.path.exists(lj):
        die('THE BANK STANDS ALREADY')
    if any(idcount(NL.join(P), I, acct).values()):
        die('AN IDENTIFIER OR THE ACCOUNT IN THE BANK')
    with open(os.path.join(PP, OT), 'wb') as f:
        f.write(new.encode('utf-8'))
    if fsha(os.path.join(PP, OT)) != sha(new)[:16]:
        die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    put(lb, NL.join(P) + NL)
    put(lj, json.dumps(dict(at=utc(), act=ACT, group=group, date=date, pp_head=pp_head, key=key, fills=vals, order=order, main=v['main'],
                            file=dict(path=OT, lines_before=n_ot, lines_after=len(nl_) - 1, line=n_ot + 2, sha_before=sha(base)[:16],
                                      sha_after=sha(new)[:16], text_sha=sha(text)[:16], prefix=new.startswith(base)),
                            runs=[o.get('run') for o in offs], controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; %s and .json' % os.path.relpath(lb, RELAY).replace(os.sep, '/'))
    return 0


def main(argv):
    if len(argv) != 3 or argv[0] != 'ledgers' or argv[1] not in GROUPS or argv[2] not in ('dry', 'write'):
        sys.exit(__doc__)
    if argv[1] == 'c3':
        return ledgers_c3(argv[2])
    if argv[1] == 'c4':
        return ledgers_c4(argv[2])
    return ledgers(argv[1], argv[2])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
