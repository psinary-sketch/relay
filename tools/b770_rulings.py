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
The later texts -- [I1] or [I2] for (6), [S5] for (7), each of (4)'s pair of texts and [C10] or [C11] -- are groups this tool gains by an
Edit committed before its run; their lines are checked here already (WANT).

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
GROUPS = dict(c2=('A5',))
PLANT_FROM, PLANT_TO = LI_INDEX + ' is read', LI_INDEX + ' CLOSED, is read'   # ### the planted status word, read in memory alone


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


# ================================================================================ THE LEDGER
def compose(group, date, base):
    X = texts(ferry())
    TP = dict((k, X[k][2]) for k in X)
    keys = GROUPS[group]
    E = dict((k, TP[k]) for k in keys)
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b770, `(R380)`(7): the line the ruling orders for OPEN_TRAILS at Component 2** (relay '
            'data/b770_ferry.txt :31 and :51-:53), appended at the end of the file (its last line :%d), so that no line before it moves: '
            'the author’s rulings of 2026-11-26 by [A5]. The lines of the two index banks and of the sitting are appended beneath it in '
            'Component 2, and those of the statements and of the closing build from source at Component 3 and after.' % (date, n_ot))
    paras = [head] + [E[k] for k in keys]
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    return dict(X=X, TP=TP, E=E, text=ot, new=base + NL + ot + NL, head=head, keys=keys, n_ot=n_ot, paras=paras)


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
    a5_names = sorted(set(O.NAME.findall(E['A5'])))
    a5_status = dict((n, O._status(O.mask(E['A5']), n)) for n in a5_names)
    planted = E['A5'].replace(PLANT_FROM, PLANT_TO, 1)
    p_status = O._status(O.mask(planted), LI_INDEX) if planted != E['A5'] else None
    p_after = dict(O.read(bl + [planted]))
    ctl = [('the papers` repository`s HEAD the corrigendum`s commit %s, the act`s one commit there before this write (%s)' % (C1PP, pp_head[:8]),
            pp_head.startswith(C1PP)),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('the text as entered equals the ruling`s, whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq[k]) for k in C['keys'] if k in eq)), len(eq) == len(C['keys']) and all(eq.values())),
           ('the text carries no field in the ruling (with fields %s), and no field is left in the appended text (%s)' % (
               fields_in or 'none', left or 'none'), not fields_in and not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('the text not in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('[A5]`s one order %s in OPEN_TRAILS before the write, OPEN by the rule (the orders [A5] names: %s)' % (LI_INDEX, a5_names or 'none'),
            a5_names == [LI_INDEX] and LI_INDEX in before and st(before, LI_INDEX) == 'OPEN'),
           ('[A5] gives the order it names no status word by the rule (%s): it stays OPEN' % (
               ' '.join('%s %s' % (n, s or 'none') for n, s in sorted(a5_status.items())) or 'none'),
            bool(a5_status) and not any(a5_status.values())),
           ('PLANTED: [A5] with a status word set after the order`s name, read in memory alone, reads a status (%s) and moves the order to %s' % (
               p_status, st(p_after, LI_INDEX)), bool(p_status) and p_status[0] == 'CLOSED' and st(p_after, LI_INDEX) == 'CLOSED'),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: no order moving and none added (moved %s ; added %s)' % (
               [(n, st(before, n), st(after, n)) for n in moved] or 'none', added or 'none'), not moved and not added)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R380)(7), GROUP %s: [A5], OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, group.upper(), utc()), '',
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
    rows = [('head', C['head'])] + [(k, E[k]) for k in C['keys']]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    P += ['', '### ### **THE LEDGERS, GROUP %s: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINE UNDER ONE HEAD ([A5]) ; CONTROLS %d OF %d '
          'AS WANTED ; %s.**' % (group.upper(), len(C['paras']) - 1, sum(1 for _w, o in ctl if o), len(ctl),
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
                            head=[nl_.index(C['head']) + 1, sha(C['head'])[:16]], keys=list(C['keys']),
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
