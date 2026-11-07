# -*- coding: utf-8 -*-
"""standing/v1250.py -- THE CONTROLS OF v1.25.0 ((R355)(2)(i)-(vii)), in v1240.py's form: each instance read through the route as it stood before the
repair and through the repaired route; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with no failing side.
THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). The route before the repair is read from the blob at BASE (b744's
closing), not from disk. The free memory is read and printed before each control. Each class may be run alone, one per call, in the foreground;
`--bank` writes the whole set, every class run in the one call. Written at b745 by the Write tool.

  python -X utf8 -u tools/standing/v1250.py control [rowid|hold|b3|exempt|subject|repeat|version ...] [--bank]
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = '\n'
BASE = '7d448774'   # ### b744's closing, the toolset as v1.24.0 left it
HOLD = 2560
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import hold as HD               # noqa: E402
import hook as HK               # noqa: E402
import repeat as RP             # noqa: E402
import rowid as RI              # noqa: E402
import subjects as SJ           # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def base_src(rel):
    return _git('show', '%s:%s' % (BASE, rel))


def free_line():
    import b703_checks as C3
    mb = C3.free_mb()
    return '  free %s MB at %s, the hold %d %s' % (mb, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), HOLD, 'MET' if isinstance(mb, int) and mb >= HOLD else '### NOT MET')


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.24.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.25.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.25.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def _reg(ref):
    return _git('show', '%s:REGISTRY.md' % ref, repo=PP)


def control_rowid():
    L, g, n = ['### (rowid) (R355)(2)(i), b743`s [B1]-[B3] (PLACE-papers 9b4af2c, 1d94177, 488b4d0), repaired by the author`s amendment at b744 (0d51a02): THE ROW`S ID'], 0, 0
    old_hook = base_src('tools/standing/hook.py')
    for c in ('9b4af2c', '1d94177', '488b4d0'):
        b, nw = _reg(c + '^'), _reg(c)
        ad = [x[1] for x in RI.added(b, nw)]
        rf = RI.refusals(b, nw)
        n += 1
        g += case(L, 'rowid', 'b743`s row at %s (%s), replayed against REGISTRY at its parent' % (c, ', '.join(ad)),
                  'the hook at %s names no ID rule (ROWID %s, rowid %s): the row committed and pushed' % (BASE, 'ROWID' in old_hook, 'rowid' in old_hook),
                  'refused: %s' % ('; '.join('%s -- %s' % (i, w) for _l, i, w in rf) or 'NOTHING REFUSED'),
                  'ROWID' not in old_hook, bool(rf) and [i for _l, i, _w in rf] == ad)
    b, nw = _reg('0d51a02^'), _reg('0d51a02')
    rf = RI.refusals(b, nw)
    n += 1
    g += guard(L, 'rowid', 'b744`s renumbered rows at 0d51a02 (%s), against REGISTRY at its parent' % ', '.join(x[1] for x in RI.added(b, nw)),
               'refused %d' % len(rf), not rf and len(RI.added(b, nw)) == 3)
    nx = RI.next_id(_reg('9b4af2c^'), '1.5c')
    n += 1
    g += guard(L, 'rowid', 'the next 1.5c ID before b743`s sitting, from the file`s maximum over every table (the table the rows joined ended at 1.5c-15)',
               nx, nx == '1.5c-21')
    # ### the hook's route: a scratch clone named PLACE-papers, REGISTRY at 9b4af2c^ committed, b743's [B1] form staged, the commit command judged
    tmp = tempfile.mkdtemp(prefix='v1250_')
    try:
        rp = os.path.join(tmp, 'PLACE-papers')
        os.makedirs(rp)
        run = lambda *a: subprocess.run(['git', '-C', rp] + list(a), capture_output=True, text=True)   # noqa: E731
        run('init', '-q')
        run('config', 'user.email', 'control@localhost')
        run('config', 'user.name', 'control')
        io.open(os.path.join(rp, 'REGISTRY.md'), 'w', encoding='utf-8', newline='').write(_reg('9b4af2c^'))
        run('add', 'REGISTRY.md')
        run('commit', '-q', '-m', 'base')
        io.open(os.path.join(rp, 'REGISTRY.md'), 'w', encoding='utf-8', newline='').write(_reg('9b4af2c'))
        run('add', 'REGISTRY.md')
        j = HK.judge('Bash', {'command': 'git -C "%s" commit -m "b743 sitting [B1], passed"' % rp.replace('\\', '/')}, RELAY)
        io.open(os.path.join(rp, 'REGISTRY.md'), 'w', encoding='utf-8', newline='').write(_reg('0d51a02'))
        run('add', 'REGISTRY.md')
        j2 = HK.judge('Bash', {'command': 'git -C "%s" commit -m "renumbered"' % rp.replace('\\', '/')}, RELAY)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    n += 1
    g += case(L, 'rowid', 'the hook on a PLACE-papers commit command, b743`s [B1] form staged over REGISTRY at 9b4af2c^ (a scratch clone, removed after)',
              'the hook at %s: no ROWID kind, the commit allowed' % BASE, 'judged %s' % ((j[0] + ': ' + j[1][:110]) if j else 'ALLOWED'),
              'ROWID' not in old_hook, bool(j) and j[0] == 'ROWID')
    n += 1
    g += guard(L, 'rowid', 'the same hook, REGISTRY at 0d51a02 (1.5c-16 to -18 renumbered 1.5c-21 to -23) staged instead', 'judged %s' % (j2[0] if j2 else 'ALLOWED'),
               j2 is None)
    d = RI.dups(io.open(os.path.join(PP, 'REGISTRY.md'), encoding='utf-8-sig').read())
    L.append('  (rowid) FOUND, NOT A CASE: REGISTRY.md at PLACE-papers HEAD holds %d IDs more than once, older than the rule and not this act`s to repair: %s' % (
        len(d), ', '.join(sorted(d))))
    return L, g, n


def control_hold():
    L, g, n = ['### (hold) (R355)(2)(ii), b744 events (3), THE TOOLS` [CLAIM ; NEW]: THE HOLD AT THE ROOT AND EVERY RECORD ROUTE'], 0, 0
    old_rec = base_src('tools/standing/fold/record.tpl')
    new_rec = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    ev = io.open(os.path.join(D, 'b744_events.txt'), encoding='utf-8').read()
    fig = '2360' in ev.replace(',', '')
    r = HD.refuses('record root_arm', hold=HOLD, free=2360)
    n += 1
    g += case(L, 'hold', 'b744`s `record root_arm` replayed at its free memory, 2,360 MB (data/b744_events.txt (3) carries the figure: %s), the hold 2,560 MB' % fig,
              'record.tpl at %s: its dispatch reads no free memory (standing.hold %s, free_mb %s); the route ran' % (BASE, 'standing.hold' in old_rec, 'free_mb' in old_rec.split("if __name__ == '__main__':")[-1]),
              'hold.refuses: %s; the template`s dispatch asks it before every route (%s)' % ('REFUSED, exit 3' if r else 'RAN', 'standing.hold' in new_rec.split("if __name__ == '__main__':")[-1]),
              'standing.hold' not in old_rec, r and 'standing.hold' in new_rec.split("if __name__ == '__main__':")[-1])
    r2 = HD.refuses('record root_arm', hold=HOLD, free=3000)
    n += 1
    g += guard(L, 'hold', 'the same route at 3,000 MB, above the hold', 'hold.refuses: %s' % ('REFUSED' if r2 else 'RUNS'), not r2)
    r3 = HD.refuses('record step', hold=HOLD, free=2559)
    n += 1
    g += guard(L, 'hold', 'a record route other than the root`s (`record step`) at 2,559 MB, one beneath the hold', 'hold.refuses: %s' % ('REFUSED' if r3 else 'RUNS'), r3)
    return L, g, n


def control_b3():
    L, g, n = ['### (b3) (R355)(2)(iii), b744 events (2): STANDING-b3 AFTER ITS FOUR CHAIN PARTS'], 0, 0
    names = ['b744_chain_half_a%d_prevrun.json' % q for q in (1, 2, 3, 4)]
    old_ck = base_src('tools/standing/fold/checks.tpl')
    new_ck = io.open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    ab = RP.b3_absent(names, lambda nm: False)   # ### the state at 03:11:34Z, b3 sent before b2a-b2d: none of the four written
    n += 1
    g += case(L, 'b3', 'b744`s sequence replayed: `--prev --part standing-b3` with the four prev-run half banks unwritten (%s)' % ', '.join(names),
              'checks.tpl at %s: b3 joins whatever it reads (b3_absent %s); the halves empty, G-ACTROOT-VERIFY failed' % (BASE, 'b3_absent' in old_ck),
              'b3 refuses itself, exit 4: absent %d of 4 (the template calls b3_absent: %s)' % (len(ab), 'b3_absent' in new_ck),
              'b3_absent' not in old_ck, len(ab) == 4 and 'b3_absent' in new_ck)
    ab2 = RP.b3_absent(names, lambda nm: os.path.exists(os.path.join(D, nm)))
    n += 1
    g += guard(L, 'b3', 'the same four banks as b744`s re-run wrote them (present in data/ now)', 'absent %d: b3 runs' % len(ab2), not ab2)
    return L, g, n


def _steps_at(ref):
    t = _git('show', '%s:data/b744_steps.json' % ref)
    return json.loads(t) if t.strip() else {}


def control_exempt():
    L, g, n = ['### (exempt) (R355)(2)(iv), b744 events (4): THE EXEMPT SET OF repeat.py :133 AND EVERY COMMIT`S ROW OR EXEMPTION PRINTED'], 0, 0
    fs = [l for l in _git('show', '--name-only', '--format=', 'da9910f9').split(NL) if l.strip()]
    ns = {}
    exec(compile(base_src('tools/standing/repeat.py'), 'repeat@%s' % BASE, 'exec'), ns)
    old = ns['bookkeeping_only'](fs, 'b744')
    new = RP.bookkeeping_only(fs, 'b744')
    n += 1
    g += case(L, 'exempt', 'relay da9910f9 replayed before its own row was written (it carries %s)' % ', '.join(fs),
              'bookkeeping_only at %s: %s -- a commit needing a row, none written: G-SEALED-AFTER-COMPONENTS FAILED at standing-a2' % (BASE, old),
              'bookkeeping_only: %s -- exempt, printed as EXEMPT' % new, not old, new)
    fs2 = fs + ['data/b744_defects.txt']
    n += 1
    g += guard(L, 'exempt', 'the same files with a bank of the act`s beside them', 'bookkeeping_only: %s -- needs its row' % RP.bookkeeping_only(fs2, 'b744'),
               not RP.bookkeeping_only(fs2, 'b744'))
    rows = (_steps_at('7d448774').get('rows') or [])
    rows_less = [r for r in rows if not (r.get('commit') or '').startswith('da9910f9')]
    log = [tuple(x.split('\t')) for x in _git('log', '--format=%H\t%s\t%cI', 'b41fa006..7d448774').strip().split(NL) if x]
    fo = RP.files_of(RELAY, PP)
    pr = RP.row_or_exemption(rows_less, [('relay', log)], fo, 'b744')
    noro = [x for x in pr if x[2].startswith('NO ROW')]
    L.append('  (exempt) THE PRINT, b744`s relay commits against its step rows less da9910f9`s (the state the event read):')
    L += ['      relay %s %s' % (h[:8], w) for _r, h, w in pr]
    n += 1
    g += guard(L, 'exempt', 'every b744 relay commit printed with its row or its exemption, none NO ROW', 'rows %d ; EXEMPT %d ; NO ROW %d' % (
        sum(1 for x in pr if x[2].startswith('ROW')), sum(1 for x in pr if x[2].startswith('EXEMPT')), len(noro)), not noro)
    return L, g, n


def control_subject():
    L, g, n = ['### (subject) (R355)(2)(v), b744 events (5): THE STEP-ROW SUBJECT COMPOSED FROM THE STAGED STEP BANK'], 0, 0
    subj = _git('log', '-1', '--format=%s', 'f5ff3680').strip()
    ad = SJ.step_rows_added(_steps_at('f5ff3680^'), _steps_at('f5ff3680'))
    words = SJ.step_rows_words(ad)
    ck = SJ.step_rows_check(subj, ad)
    old_hook = base_src('tools/standing/hook.py')
    n += 1
    g += case(L, 'subject', 'relay f5ff3680`s subject "%s"' % subj,
              'the hook at %s reads seal, lock and gate subjects alone (step_subject_faults %s): the subject ran' % (BASE, 'step_subject_faults' in old_hook),
              'step_rows_check: %s' % ('; '.join(ck) or 'NO FAULT'), 'step_subject_faults' not in old_hook, bool(ck))
    regen = 'b744 record: ' + words
    n += 1
    g += guard(L, 'subject', 'f5ff3680`s subject regenerated by the composer from the rows it adds (%d)' % len(ad), '"%s" ; check: %s' % (
        regen, '; '.join(SJ.step_rows_check(regen, ad)) or 'NO FAULT'), bool(words) and not SJ.step_rows_check(regen, ad))
    return L, g, n


def control_repeat():
    L, g, n = ['### (repeat) (R355)(2)(vi): THE REPEAT INSTANCES OF b744 EVENTS (1) AND (6)'], 0, 0
    ev = io.open(os.path.join(D, 'b744_events.txt'), encoding='utf-8').read()
    j = HK.judge('PowerShell', {'command': 'Get-ChildItem data/b743_prevrun_* | Select-Object Name'}, RELAY)
    n += 1
    g += guard(L, 'repeat', '(1) a PowerShell listing carrying a pipe (events (1), REPEAT b743 (c)): the hook`s PIPE row working', 'judged %s ; events (1) REPEAT %s' % (
        j[0] if j else 'ALLOWED', "(1) THE SEAT'S [CLOSE ; REPEAT b743 (c)]" in ev), bool(j) and j[0] == 'PIPE')
    n += 1
    g += guard(L, 'repeat', '(6) the post-push part sent without --rerun-postpush (events (6), REPEAT b743 (14)): the suite`s self-refusal working, the instance printed',
               'events (6) REPEAT %s ; carries --rerun-postpush %s' % ("(6) THE SEAT'S [CLOSE ; REPEAT b743 (14)]" in ev, '--rerun-postpush' in ev),
               "(6) THE SEAT'S [CLOSE ; REPEAT b743 (14)]" in ev)
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R355)(2)(vii): THE STANDING VERSION PRINTED, ITS CONTROLS TALLIED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    old = base_src('tools/standing/VERSION').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', old, ver, old == 'v1.24.0', ver == 'v1.25.0')
    return L, g, n


CONTROLS = {'rowid': control_rowid, 'hold': control_hold, 'b3': control_b3, 'exempt': control_exempt, 'subject': control_subject,
            'repeat': control_repeat, 'version': control_version}
ORDER = ('rowid', 'hold', 'b3', 'exempt', 'subject', 'repeat', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.25.0, (R355)(2)(i)-(vii): THE ROW`S ID, THE HOLD AT THE ROOT AND EVERY RECORD ROUTE, b3 AFTER ITS CHAIN '
           'PARTS, THE EXEMPT SET AND EVERY COMMIT`S ROW OR EXEMPTION, THE STEP-ROW SUBJECT, THE REPEAT INSTANCES, THE VERSION (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each repair`s instances through both routes; the free memory read before each; written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### the instances read at their commits; each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    for k in names:
        out.append(free_line())
        try:
            L, g, c = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
    out.append('### ### **v1.25.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1250.txt' % act), NL.join(out))
        print('written data/%s_standing_v1250.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
