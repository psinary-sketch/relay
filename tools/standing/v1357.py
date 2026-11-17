# -*- coding: utf-8 -*-
"""standing/v1357.py -- THE CONTROLS OF v1.35.7, (R368)(1) AMENDED ON THE AUTHOR'S WORD: THE CLOSE'S READERS BOUNDED AT THE NEXT ACT'S
OPENING COMMIT, in v1356.py's form.

The author's words (relay data/b758_amendments.json row 1, data/b758_author_words_preseal.txt :6, transcript line 115131,
2026-11-17T00:31:28Z): "Option 3, as an amendment to (R368)(1) on the author's word: one standing change, VERSION moved, bounding the readers
behind N2, N4, N5 and S3 at the next act's opening commit (49c58344) when a close runs inside a later act. Its controls: b757's four scores
read HELD as at step [9]; a planted b757 commit after its lock still read as a violation. Then step [22] again, then [23] to [25]." BEFORE is
the composition record.tpl :3240 made at BASE (the readers called unbounded); AFTER is tools/standing/closebound.py's, which record.tpl :3240
now calls. b757's record tool is loaded as `fold.py record --act b757` loads it; no route runs and nothing is written but this bank.

  (bound)     the next act's opening commit read from git: b757's 49c58344 (b758's ACT_CURRENT_COMMIT), its parent ff65ccdb; b756's 0ff48304
              (b757's ACT_CURRENT_COMMIT); none for b758, whose close runs inside its own act; closebound.py absent at BASE.
  (step9)     b757's four scores: before, N2, N4, N5 and S3 REFUTED (the first [22]'s reading reproduced); after, each HELD, as
              data/b757_scores.json reads it at step [9]; the clauses that flipped printed.
  (rest)      N1, N3, S1 and S2 after equal to before, verdict and reading.
  (plant)     a b757 commit planted after b757's lock and before the base, touching tools/standing/act.py, put into the bounded reads beneath
              the bound: N4 REFUTED naming it; N2 REFUTED counting it among b757's commits under tools/standing/.
  (calls)     the relay git calls the four bounded readers send, as the bound rewrote them: none names HEAD, none reads the working tree or the
              index, none carries an option whose value stands as a separate word.
  (template)  record.tpl rendered for every act with a sections file at BASE's template and at the working one: the same line count, one
              line differing in each render, the scores line.
  (version)   tools/standing/VERSION moved to v1.35.7.

  python -X utf8 -u tools/standing/v1357.py control [bound|step9|rest|plant|calls|template|version ...] [--bank]
"""
import io
import json
import os
import re
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = 'ac6a0a77'   # ### the relay's HEAD before this change (b758 component 1, step 12, v1.35.6)
PLANT = 'b757' * 10
FOUR = ('N2', 'N4', 'N5', 'S3')
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import closebound as CB         # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import fold as F                # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)

_MEMO = {}


def case(L, k, what, before, after, ok_b, ok_a):
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if ok_b and ok_a else 0


def after(L, k, what, got, ok):
    L.append('  (%s) %s' % (k, what))
    L.append('      AFTER : %s -> %s' % (got, 'AS WANTED' if ok else 'NOT AS WANTED'))
    return 1 if ok else 0


def mod757():
    if 'M' not in _MEMO:
        F.install()
        cwd = os.getcwd()
        os.chdir(RELAY)
        try:
            _MEMO['M'] = F.load('b757', 'record', name='b757_record')
        finally:
            os.chdir(cwd)
    return _MEMO['M']


def wl(act):
    import importlib
    return importlib.import_module('%s_worklist' % act)


def unbounded():
    """the readings as BASE's :3240 composed them: every reader called as it stands."""
    if 'U' not in _MEMO:
        M = mod757()
        _MEMO['U'] = dict([('N1', M._n1()), ('N2', M._n2()), ('N3', M._n3()), ('N4', M._n4()), ('N5', M._n5())] + list(M._s_scores().items()))
    return _MEMO['U']


def logging_run(log, real):
    def run0(cmd, *a, **k):
        if isinstance(cmd, (list, tuple)) and len(cmd) > 3 and cmd[0] == 'git' and cmd[1] == '-C' and CB._same(cmd[2], RELAY):
            log.append([str(x) for x in cmd[3:]])
        return real(cmd, *a, **k)
    return run0


def bounded():
    """the readings as closebound.scores composes them at `scores close` for b757, with every relay call the bound sends logged."""
    if 'B' not in _MEMO:
        M = mod757()
        log = []
        _MEMO['B'] = CB.scores(M.__dict__, M.R, 'b757', True, run0=logging_run(log, subprocess.run))
        _MEMO['LOG'] = log
    return _MEMO['B']


def clause(text, pats):
    out = []
    for p in pats:
        m = re.search(p, text or '')
        out.append(m.group(0)[:260] if m else '(%s: not found)' % p[:30])
    return ' | '.join(out)


PATS = dict(N2=[r'the act`s commits under tools/standing/ those two and no other \([^)]*\): \w+'],
            N4=[r'the commits after it \(relay\) \d+, touching the face, a tool or a bank tracked at the lock commit: [^;]*;',
                r'working tree`s changes to them: [^;]*;'],
            N5=[r'shared tools edited beyond the membrane [^;]*;', r'sealed tools not agreeing: [^;]*;', r'relay files beyond the face`s \(W\) list: [^;]*;'],
            S3=[r'the sealed tools` hashes \{[^}]*\}'])


def control_bound():
    L, gd, n = ['### (bound): THE NEXT ACT`S OPENING COMMIT, READ FROM GIT'], 0, 0
    o757 = CB.opening('b757', wl('b757').PRE_RELAY, RELAY)
    o756 = CB.opening('b756', wl('b756').PRE_RELAY, RELAY)
    o758 = CB.opening('b758', wl('b758').PRE_RELAY, RELAY)
    w758, w757 = wl('b758').ACT_CURRENT_COMMIT, wl('b757').ACT_CURRENT_COMMIT
    par = A.git('relay', 'rev-parse', '49c58344^').decode().strip()
    at_base = subprocess.run(['git', '-C', RELAY, 'cat-file', '-e', '%s:tools/standing/closebound.py' % BASE], capture_output=True).returncode
    n += 1
    gd += case(L, 'bound', 'b757`s close inside b758', 'tools/standing/closebound.py at %s: %s' % (BASE, 'ABSENT' if at_base else 'PRESENT'),
               ('the next act %s, its opening commit %s, the base %s, the cut %s ; b758`s ACT_CURRENT_COMMIT %s ; 49c58344`s parent %s' % (
                   o757[0], o757[1][:8], o757[2][:8], time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(o757[3])), w758, par[:8])) if o757 else 'NONE',
               at_base != 0, bool(o757) and o757[0] == 'b758' and o757[1].startswith(w758) and o757[2] == par)
    n += 1
    gd += after(L, 'bound', 'b756`s close inside a later act (the first act after b756`s PRE_RELAY to name another act)',
                ('the next act %s, its opening commit %s, the base %s ; b757`s ACT_CURRENT_COMMIT %s' % (o756[0], o756[1][:8], o756[2][:8], w757))
                if o756 else 'NONE', bool(o756) and o756[0] == 'b757' and o756[1].startswith(w757))
    n += 1
    gd += after(L, 'bound', 'b758`s close inside its own act (data/act_current.json names b758)', 'bound %s' % (o758,), o758 is None)
    return L, gd, n


def control_step9():
    L, gd, n = ['### (step9): b757`S FOUR SCORES, BEFORE AND AFTER, AGAINST STEP [9] (data/b757_scores.json)'], 0, 0
    s9 = json.load(io.open(os.path.join(D, 'b757_scores.json'), encoding='utf-8'))
    U, B = unbounded(), bounded()
    for k in FOUR:
        n += 1
        gd += case(L, k, '%s, step [9] %s' % (k, s9[k][0]),
                   '%s -- %s' % (U[k][0], clause(U[k][1], PATS[k])), '%s -- %s' % (B[k][0], clause(B[k][1], PATS[k])),
                   U[k][0] == 'REFUTED', B[k][0] == 'HELD' and B[k][0] == s9[k][0] and 'READ BOUNDED' in B[k][1])
    return L, gd, n


def control_rest():
    L, gd, n = ['### (rest): N1, N3, S1 AND S2, BEFORE AND AFTER'], 0, 0
    U, B = unbounded(), bounded()
    for k in ('N1', 'N3', 'S1', 'S2'):
        n += 1
        gd += after(L, k, '%s read as before' % k, 'before %s, after %s ; the readings equal %s' % (U[k][0], B[k][0], list(U[k]) == list(B[k])),
                    list(U[k]) == list(B[k]))
    return L, gd, n


def injector(lc, lct, base, real):
    """a b757 commit planted after the lock commit `lc` and before the base, touching tools/standing/act.py, put into the relay reads the
    bound sends (beneath it: the bound rewrites, then this reads)."""
    def run0(cmd, *a, **k):
        r = real(cmd, *a, **k)
        if not (isinstance(cmd, (list, tuple)) and len(cmd) > 3 and cmd[0] == 'git' and cmd[1] == '-C' and CB._same(cmd[2], RELAY)):
            return r
        args = [str(x) for x in cmd[3:]]
        txt = isinstance(r.stdout, str)
        s = r.stdout if txt else (r.stdout or b'').decode('utf-8', 'replace')
        if args[:1] == ['log'] and '--reverse' in args and any(x.endswith('..' + base) for x in args):
            lines = s.split(NL)
            fmt = ([x for x in args if x.startswith('--format=')] or ['--format=%H'])[0]
            row = PLANT + (' %d' % (lct + 1) if '%ct' in fmt else '')
            idx = next((i for i, l in enumerate(lines) if l.split(' ')[0] and lc.startswith(l.split(' ')[0])), None)
            if idx is not None:
                lines.insert(idx + 1, row)
            elif 'tools/standing' in args:
                lines.insert(len([l for l in lines if l.strip()]), row)   # ### b757's standing commits all precede its lock
            else:
                return r
            s = NL.join(lines)
        elif args[:1] == ['show'] and PLANT in args:
            s = 'tools/standing/act.py\n'
        elif args[:2] == ['log', '-1'] and PLANT in args:
            s = '%d\n' % (lct + 1)
        elif args[:1] == ['rev-parse'] and PLANT in args:
            s = PLANT + '\n'
        else:
            return r
        return subprocess.CompletedProcess(r.args, 0, s if txt else s.encode('utf-8'), r.stderr)
    return run0


def control_plant():
    L, gd, n = ['### (plant): A b757 COMMIT PLANTED AFTER ITS LOCK, BEFORE THE BASE, TOUCHING tools/standing/act.py'], 0, 0
    import lockdate as LD
    M = mod757()
    lc = LD.lock_of('b757', D)
    lct = LD.lock_epoch(lc, RELAY)
    b = CB.bound('b757', M.K, M.ROOT)
    b.run0 = injector(lc, lct, b.base, subprocess.run)
    v4 = b.read(M.__dict__, M.R, M._n4)
    v2 = b.read(M.__dict__, M.R, M._n2)
    n += 1
    gd += after(L, 'plant', 'N4 bounded, the lock commit %s (%s), the planted commit %s.. at the lock`s time + 1 s' % (
        lc[:8], time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(lct)), PLANT[:8]),
                '%s -- %s' % (v4[0], clause(v4[1], PATS['N4'])), v4[0] == 'REFUTED' and ('%s tools/standing/act.py' % PLANT[:8]) in v4[1])
    n += 1
    gd += after(L, 'plant', 'N2 bounded, the planted commit among b757`s commits under tools/standing/',
                '%s -- %s' % (v2[0], clause(v2[1], PATS['N2'])), v2[0] == 'REFUTED' and PLANT[:8] in v2[1])
    return L, gd, n


def _shape(a):
    """a call's shape: commits masked, a tool path after a commit masked, the paths after `--` masked."""
    cut = a.index('--') if '--' in a else len(a)
    w = [x if x.startswith('--format') else re.sub(r'(<sha>):\S+', r'\1:<path>', re.sub(r'[0-9a-f]{7,40}', '<sha>', x)) for x in a[:cut]]
    return ' '.join(w + (['--', '<paths>'] if cut < len(a) else []))


def control_calls():
    """the four readers read bounded once more, the bound found first and unlogged (its own read of PRE_RELAY..HEAD for the opening commit
    is the bound's, not a reader's), then every relay call beneath it logged."""
    L, gd, n = ['### (calls): THE RELAY CALLS THE BOUNDED READERS SENT, AS THE BOUND REWROTE THEM'], 0, 0
    M = mod757()
    b = CB.bound('b757', M.K, M.ROOT)
    log = []
    b.run0 = logging_run(log, subprocess.run)
    for fn in (M._n2, M._n4, M._n5, lambda: M._s_scores()['S3']):
        b.read(M.__dict__, M.R, fn)
    head = [a for a in log if any(x == 'HEAD' or x.endswith('..HEAD') or x.startswith('HEAD') for x in a)]
    work = [a for a in log if a[:1] == ['status'] or (a[:1] == ['diff'] and len([x for x in a[1:] if not x.startswith('-')]) == 0)]
    sep = [a for a in log if any(x in ('-n', '--max-count', '--skip', '--since', '--until', '--author', '--grep') for x in a)]
    kinds = sorted(set(_shape(a) for a in log))
    n += 1
    gd += after(L, 'calls', 'the calls beneath the bound %d (the bound`s rewrites %d), their shapes %d: %s' % (
        len(log), b.calls, len(kinds), ' ; '.join(kinds)[:2400]),
                'naming HEAD %d %s ; reading the working tree or the index %d ; an option with a separate value %d' % (
                    len(head), head[:2], len(work), len(sep)),
                bool(log) and not head and not work and not sep)
    return L, gd, n


def control_template():
    L, gd, n = ['### (template): record.tpl RENDERED FOR EVERY ACT WITH A SECTIONS FILE, AT BASE`S TEMPLATE AND AT THE WORKING ONE'], 0, 0
    t0 = V.show(BASE, 'tools/standing/fold/record.tpl')
    t1 = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8', newline='').read()
    acts = sorted(f[:-3] for f in os.listdir(os.path.join(T, 'acts')) if f.endswith('.py') and f[:1] == 'b')
    bad, ones = [], 0
    for a in acts:
        try:
            r0, r1 = F.render(a, 'record', tpl=t0).split(NL), F.render(a, 'record', tpl=t1).split(NL)
        except Exception as e:  # noqa: BLE001
            bad.append('%s raised %s' % (a, type(e).__name__))
            continue
        dl = [i + 1 for i in range(min(len(r0), len(r1))) if r0[i] != r1[i]]
        if len(r0) == len(r1) and len(dl) == 1 and 'standing.closebound' in r1[dl[0] - 1]:
            ones += 1
        else:
            bad.append('%s lines %d/%d differing %s' % (a, len(r0), len(r1), dl[:4]))
    n += 1
    gd += case(L, 'template', 'record.tpl: lines %d at BASE, %d now' % (len(t0.split(NL)), len(t1.split(NL))),
               'BASE`s template, every act rendered (%d)' % len(acts),
               'renders differing in one line, the scores line, with the same line count: %d of %d ; others %s' % (ones, len(acts), bad or 'NONE'),
               len(t0.split(NL)) == len(t1.split(NL)), ones == len(acts) and not bad)
    return L, gd, n


def control_version():
    L, gd, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    gd += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.35.6', ver == 'v1.35.7')
    return L, gd, n


CONTROLS = dict(bound=control_bound, step9=control_step9, rest=control_rest, plant=control_plant, calls=control_calls,
                template=control_template, version=control_version)
ORDER = ('bound', 'step9', 'rest', 'plant', 'calls', 'template', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.35.7, (R368)(1) AMENDED: THE CLOSE`S READERS BOUNDED AT THE NEXT ACT`S OPENING COMMIT (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY CASE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before (record.tpl :3240 at %s: the readers called unbounded) and after (tools/standing/closebound.py)' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, gd, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, gd, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + gd, tn + c
        per.append('(%s) %d of %d' % (k, gd, c))
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.35.7: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1357.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
