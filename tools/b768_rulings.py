# -*- coding: utf-8 -*-
"""tools/b768_rulings.py -- b768, (R378)(7): THE TEXTS OF THE RULING ENTERED IN OPEN_TRAILS, BY GROUP.

Carried in form from tools/b767_rulings.py's ledgers route (the texts read from the ferry bank between their marker lines and checked
against their lines; the file appended at its end, its bytes at HEAD a prefix of its new bytes; the controls before the write; the ledger
banked by line and sha256) by the Write tool, and committed before its run (N2). (R378)(7) and (12) write neither REGISTRY, ERRATA, the
census, the register nor the two files of the map, so OPEN_TRAILS is the one file here.

  ledgers c2 dry|write   Component 2 (data/b768_ferry.txt :97: "THE LINES OF (7), [R2] and [A3]"; :41: "[A3] is entered, one line for
                         (a), (c), (d) and (e), and [R2] for (b)"), appended at OPEN_TRAILS' end, no line moving, <DATE> the UTC date of the
                         write: one dated head and under it, each a paragraph of its own, in the order of the ruling's texts --
                         [R2] (data/b768_ferry.txt :78), as written: W-ORD-NOVEMBER-RIDERS stands in OPEN_TRAILS from b767's [R1] with
                           its entry line in the form tools/standing/orderstate.py :26 reads, and (7)(b) gives it passages with its trigger
                           standing, so no entry line is composed and the order's status is not moved;
                         [A3] (data/b768_ferry.txt :82), as written; it names no order.
                         Neither text carries a field. Controls before the write, printed, among them a planted status word read by the
                         rule (a check that can fire); the roster by tools/standing/orders.py's rule in memory, before and after: no order
                         added and none moving. Bank: data/b768_ledgers_c2.txt and .json, each text by line and sha256; the texts' words
                         printed by the dry run alone.
[P1] or [P2], and [C7] or [C8], are a group this tool gains by an Edit committed before its run, where the steps' and the closing
build's reads give them.

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
import b768_worklist as K   # noqa: E402

ACT, NL = 'b768', '\n'
PP = K.PP
FERRY = os.path.join(D, 'b768_ferry.txt')
FERRY_SHA = 'f4cc3c93a7a435fd'   # ### data/b768_stepzero.txt :19: the ferry bank's sha256
OT = 'OPEN_TRAILS.md'
C1PP = '9c43f4bb'                # ### PLACE-papers' one commit of the act before this write: the corrigendum (step 6, data/b768_events.txt (41))
WANT = dict(P1=(62, 62), P2=(66, 66), C7=(70, 70), C8=(74, 74), R2=(78, 78), A3=(82, 82))
FIELD = re.compile(r'<[A-Za-z][^<>\n]*>')
RIDERS = 'W-ORD-NOVEMBER-RIDERS'
GROUPS = dict(c2=('R2', 'A3'))
PLANT_FROM, PLANT_TO = '` GAINS PASSAGES', '` DISCHARGED, GAINS PASSAGES'   # ### the planted status word, read in memory alone


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
    import b768_address_scan as SC
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
    head = ('**Dated head, %s, b768, `(R378)`(7): the lines the ruling orders for OPEN_TRAILS at Component 2** (relay '
            'data/b768_ferry.txt :41, :77-:79 and :81-:83), appended at the end of the file (its last line :%d), so that no line before '
            'them moves: the passages the order of the November riders gains, in two parts, by [R2]; the author’s rulings of 2026-11-23 '
            'and 2026-11-24 by [A3]. The lines of the proof and of the closing build from source are appended beneath them at Component 3 '
            'and after.' % (date, n_ot))
    paras = [head] + [E[k] for k in keys]
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    return dict(X=X, TP=TP, E=E, text=ot, new=base + NL + ot + NL, head=head, keys=keys, n_ot=n_ot, paras=paras)


def ledgers(group, mode):
    from standing import orders as O
    from standing import orderstate as OS
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
    riders_entry = [i + 1 for i, l in enumerate(bl) if (OS.ENTRYFORM.match(l) or [None, None])[1] == RIDERS]
    r2_status = O._status(O.mask(E['R2']), RIDERS)
    a3_names = sorted(set(O.NAME.findall(E['A3'])))
    planted = E['R2'].replace(PLANT_FROM, PLANT_TO, 1)
    p_status = O._status(O.mask(planted), RIDERS) if planted != E['R2'] else None
    p_after = dict(O.read(bl + [planted]))
    ctl = [('PLACE-papers` HEAD the corrigendum`s commit %s, the act`s one commit there before this write (%s)' % (C1PP, pp_head[:8]),
            pp_head.startswith(C1PP)),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('each text as entered equals the ruling`s, each whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq[k]) for k in C['keys'] if k in eq)), len(eq) == len(C['keys']) and all(eq.values())),
           ('neither text carries a field in the ruling (with fields %s), and no field is left in the appended text (%s)' % (
               fields_in or 'none', left or 'none'), not fields_in and not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('none of the texts in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('[R2]`s order %s in OPEN_TRAILS before the write, OPEN by the rule, its entry line in the form tools/standing/orderstate.py :26 reads '
            'at %s' % (RIDERS, ['%d' % x for x in riders_entry] or 'none'),
            RIDERS in before and st(before, RIDERS) == 'OPEN' and len(riders_entry) == 1),
           ('[R2] gives %s no status word by the rule (%s): its trigger stands and the order stays OPEN; [A3] names no order (%s)' % (
               RIDERS, r2_status or 'none', a3_names or 'none'), r2_status is None and not a3_names),
           ('PLANTED: [R2] with a status word set after the order`s name, read in memory alone, reads a status (%s) and moves the order to %s' % (
               p_status, st(p_after, RIDERS)), bool(p_status) and p_status[0] == 'CLOSED' and st(p_after, RIDERS) == 'CLOSED'),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: no order moving and none added (moved %s ; added %s)' % (
               [(n, st(before, n), st(after, n)) for n in moved] or 'none', added or 'none'), not moved and not added)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R378)(7), GROUP %s: [R2] AND [A3], OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, group.upper(), utc()), '',
         '### tools/b768_rulings.py ledgers %s; PLACE-papers HEAD %s; the texts from the ferry bank (data/b768_ferry.txt, sha256 %s); <DATE> %s;'
         % (group, pp_head[:8], FERRY_SHA, date),
         '### each text by line and sha256 here; no PLACE-papers line printed but the texts composed.', '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  open before %d -> after %d ; orders %d -> %d ; added %s' % (open_b, open_a, len(before), len(after), added or 'none'),
          '  statuses moving: %s' % ([(n, st(before, n), st(after, n)) for n in moved] or 'none')]
    first = C['n_ot'] + 2
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        C['n_ot'], len(nl_) - 1, first, sha(text)[:16], sha(base)[:16], sha(new)[:16])]
    rows = [('head', C['head'])] + [(k, E[k]) for k in C['keys']]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    P += ['', '### ### **THE LEDGERS, GROUP %s: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINES UNDER ONE HEAD ([R2], [A3]) ; CONTROLS %d OF %d '
          'AS WANTED ; %s.**' % (group.upper(), len(C['paras']) - 1, sum(1 for _w, o in ctl if o), len(ctl),
                                 ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(text)
        return 0 if ok else 1
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b768_ledgers_%s.txt' % group), os.path.join(D, 'b768_ledgers_%s.json' % group)
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
