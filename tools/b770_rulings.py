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
The later texts -- each of (4)'s pair of texts and [C10] or [C11] -- are groups this tool gains by an Edit committed before its run; their
lines are checked here already (WANT).

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
GROUPS = dict(c2=('A5',), c2i=('I1',), c2s=('S5',))   # ### c2i: [I1], or [I2] where data/b770_li_index.json reads NOT AS READ (set at run time)
# ### the papers` repository's HEAD before each group's write: c2 after the corrigendum (step 12), c2i after [A5] (step 29), c2s after [I1] (step 38)
PP_BEFORE = dict(c2=C1PP, c2i='f945cbd9', c2s='c599930d')
CLAUSE = dict(c2='7', c2i='6', c2s='7')
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


def main(argv):
    if len(argv) != 3 or argv[0] != 'ledgers' or argv[1] not in GROUPS or argv[2] not in ('dry', 'write'):
        sys.exit(__doc__)
    return ledgers(argv[1], argv[2])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
