"""b712 -- THE STANDING REPORT TOOL, (R322)(3): data/b712_report.txt (.json). A REPORT, NOT AN ARM.

Rewritten whole by the Write tool at b712 from b711's throughstone report (tools/b711_report.py), carried forward under (R322)(3): "The
throughstone report of b711 carried forward as a standing report tool, data/b712_report.txt, its four footings KERNEL, CERTIFIED, REGISTERED,
HELD, its lines recomputed from the banks with path, line and sha256, its scores line printed after the root; it is a report and not an arm."
Two routes:
  bank    (before the root) each line's figures recomputed from the act's JSON banks, beside each its SOURCE -- the bank's path, the row cited
          by line, the bank's sha256 now and, where a hashes bank exists, as that bank records it -- the lines printed in footing order
          (KERNEL, CERTIFIED, REGISTERED, HELD), a footing no line stands on printed as NONE; written through the membrane to data/b712_report.txt
          and data/b712_report.json. Nothing else is written.
  scores  (after the root) the scores line: all eight from data/b712_scores_close.json, each HELD or BROKEN, and the root line from
          data/act_roots.txt; PRINTED ONLY -- no bank is written after the root (N4), and the membrane refuses one.
The tool decides nothing: no verdict is gated on its lines (no arm reads its exit code), and a line it cannot recompute prints as such.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
import b712_worklist as K          # noqa: E402

NL = '\n'
ACT = 'b712'
FOOTINGS = ('KERNEL', 'CERTIFIED', 'REGISTERED', 'HELD')
PP = K.PP
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace')


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace('\r', '') if os.path.exists(p) else ''


def jl(name):
    t = rd(name)
    return json.loads(t) if t else {}


def sha(name):
    p = os.path.join(D, name)
    return hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None


def line_of(name, needle):
    for i, l in enumerate(rd(name).split(NL), 1):
        if needle in l:
            return i
    return None


def seat(name, needle):
    """the line's SOURCE: the bank's path, the row cited by line (the first line carrying the needle), its sha256 now."""
    ln, now = line_of(name, needle), sha(name)
    return dict(bank='data/' + name, row=ln, sha256=now, ok=bool(now) and ln is not None,
                text='relay data/%s :%s ; sha256 %s' % (name, ln if ln is not None else '### NEEDLE NOT FOUND', (now or '### ABSENT')[:16]))


def lines():
    keys, seats = {}, []
    # ------------------------------------------------------------------ KERNEL: THE JOIN
    jg, jt = jl('%s_join_grade.json' % ACT), jl('%s_join_tag.json' % ACT)
    s1, s2 = seat('%s_join_grade.txt' % ACT, 'GRADE DERIVES'), seat('%s_join_tag.txt' % ACT, 'EQUAL')
    ax = (jg.get('axioms') or ['-'])[0]
    three = ax.endswith('[propext, Classical.choice, Quot.sound]')
    keys['JOIN'] = ('KERNEL -- THE JOIN BY CLOSURE: faces_join at SIDE-faces-join %s (tag object %s, peeled %s, at the remote %s/%s, read back %s), '
                    'run %s at ref %s, the lv pin %s (the port`s tip %s); its statement: %s; it names lv-conservation`s own Register4_positivity %s, '
                    'read equal at the deposit and the tip %s; #print axioms: %s -- the standard three %s; the grade %s. SOURCE %s ; %s.' % (
                        jt.get('tag'), (jt.get('object') or '')[:8], (jt.get('peeled') or '')[:8], (jt.get('remote_object') or '')[:8],
                        (jt.get('remote_peeled') or '')[:8], jt.get('ok'), jg.get('run_id'), (jg.get('ref') or '')[:8], (jg.get('pin') or '')[:8],
                        (jg.get('pin') == jg.get('tip')), ' '.join(x.strip() for x in jg.get('statement') or []), jg.get('names_lv'),
                        jg.get('regpos_equal'), ax, three, jg.get('grade'), s1['text'], s2['text']))
    seats += [s1, s2]
    # ------------------------------------------------------------------ KERNEL: THE PORT
    pj, p1 = jl('%s_port.json' % ACT), jl('%s_port_port1.json' % ACT)
    sp = seat('%s_port.txt' % ACT, '### ### **')
    built, mods = len(pj.get('built') or []), len(pj.get('modules') or [])
    art = pj.get('artifact') or {}
    fe1 = re.match(r'^error: SIDELvConservation/(\w+\.lean):(\d+):(\d+):', p1.get('first_error') or '')
    keys['PORT'] = ('KERNEL -- THE FORWARD PORT: SIDE-lv-conservation port-b707 at %s built %d of %d modules on run %s (artifact sha256 %s…, agreeing %s), '
                    'first error %s; the first dispatch, run %s at %s, held at %s; no grade claimed on the port (its print list absent at the tree, '
                    'b707`s reading). SOURCE %s.' % (
                        K.PORT_NEW_TIP[:8], built, mods, pj.get('run_id'), (art.get('sha256') or '')[:16], art.get('agree'),
                        pj.get('first_error') or 'NONE', p1.get('run_id'), K.PORT_EDIT1[:8],
                        ('%s :%s:%s' % fe1.groups()) if fe1 else '-', sp['text']))
    seats.append(sp)
    # ------------------------------------------------------------------ KERNEL: Register4_positivity READ EQUAL
    rp = jl('%s_regpos.json' % ACT)
    sr = seat('%s_regpos.txt' % ACT, 'EQUAL')
    keys['REGPOS'] = ('KERNEL -- Register4_positivity read at the deposit %s (:%s) and at the port`s tip %s (:%s), equal by statement %s, the file`s diff '
                      'lines %s: %s. SOURCE %s.' % ((rp.get('deposit') or '')[:8], rp.get('line_deposit'), (rp.get('tip') or '')[:8], rp.get('line_tip'),
                                                    rp.get('equal'), rp.get('file_diff_lines'), ' '.join(x.strip() for x in rp.get('decl_tip') or []), sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ KERNEL: THE RE-CUT'S PINS
    cj = jl('%s_recut_compile.json' % ACT)
    sc = seat('%s_recut_compile.txt' % ACT, '### ### **')
    pins = cj.get('pins') or []
    keys['PINS'] = ('KERNEL -- THE RE-CUT`S PINS: %d of %d standing at their tags (%s), the control one line off reading %s, the old pin 0bc21c0 = v1.3 %s '
                    'with the statement standing %s. SOURCE %s.' % (
                        sum(1 for p in pins if p.get('stands')), len(pins), ', '.join(sorted(set('%s %s' % (p['repo'], p['tag']) for p in pins))),
                        cj.get('control'), (cj.get('oldpin') or {}).get('commit', '')[:7] == (cj.get('oldpin') or {}).get('v13', '-')[:7],
                        (cj.get('oldpin') or {}).get('statement'), sc['text']))
    seats.append(sc)
    # ------------------------------------------------------------------ REGISTERED: THE -15 CONTROL AND ITS PRICE
    pr = jl('%s_price.json' % ACT)
    sg, sq = seat('%s_registrations.txt' % ACT, '### ### **REGISTRATIONS'), seat('%s_price.txt' % ACT, '### ### **')
    first = g(ROOT, 'log', '--format=%H', '--reverse', '%s..HEAD' % K.PRE_RELAY).split(NL)[0].strip()
    files_first = sorted(x for x in g(ROOT, 'show', '--name-only', '--format=', first).split(NL) if x.strip())
    keys['CONTROL'] = ('REGISTERED -- THE CLASS-NUMBER-2 CONTROL AT -15: data/b712_registrations.txt committed at %s, the act`s first relay commit %s '
                       'carrying %s; priced -- the first tier %.2f h, the second %.2f h, the seat`s act budget %.1f h, the cut %s; nothing of the -15 '
                       'zeros computed. SOURCE %s ; %s.' % (
                           K.REG_COMMIT[:8], first[:8] == K.REG_COMMIT[:8], files_first, pr.get('t1') or 0, pr.get('t2') or 0, pr.get('budget') or 0,
                           pr.get('cut'), sg['text'], sq['text']))
    seats += [sg, sq]
    # ------------------------------------------------------------------ REGISTERED: THE FACES ROW
    fl = g(PP, 'show', '%s:FACES_LEDGER.md' % K.C3_PP).replace('\r', '').split(NL)
    fln = next((i for i, l in enumerate(fl, 1) if l.startswith('## UPDATE') and '(b712)' in l), None)
    keys['FACES'] = ('REGISTERED -- THE FACES ROW: FACES_LEDGER.md :%s at PLACE-papers %s, its row naming faces_join, its grade and the peeled SHA %s: %s. '
                     'SOURCE PLACE-papers FACES_LEDGER.md :%s at %s.' % (
                         fln, K.C3_PP[:8], K.JOIN_TAG[2][:8], K.JOIN_TAG[2][:7] in NL.join(fl[(fln or 1) - 1:]) and 'DERIVES' in NL.join(fl[(fln or 1) - 1:]),
                         fln, K.C3_PP[:8]))
    # ------------------------------------------------------------------ REGISTERED: THE RE-CUT
    cu = jl('%s_recut_cut.json' % ACT)
    su, sd = seat('%s_recut_cut.txt' % ACT, '### ### **'), seat('%s_recut_diff.txt' % ACT, '### ### **')
    on_remote = bool(g(PP, 'ls-remote', 'origin', 'refs/heads/' + K.RECUT_BRANCH).strip())
    keys['RECUT'] = ('REGISTERED -- THE RE-CUT OF %s: on the branch %s at %s (at the remote %s: nothing published); the distance by the b670 method %s -> %s, '
                     'the held Correspondence cells %s, the MATCHES rows lost %s. SOURCE %s ; %s.' % (
                         K.RECUT_DOC, K.RECUT_BRANCH, K.RECUT_COMMIT[:8], on_remote, cu.get('before'), cu.get('after'),
                         ', '.join(':%d' % x for x in sorted(set(cu.get('held') or []))),
                         cu.get('matches_lost') or 'NONE', su['text'], sd['text']))
    seats += [su, sd]
    # ------------------------------------------------------------------ HELD
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished; no lv tag (W-ORD-LV-PORT-TAG at OPEN_TRAILS :%s for the author`s word); the Correspondence '
                    'cells of the re-cut held; the -15 source pin priced for b713; the faces ledger head`s :8 sentence for the author`s word.' % (
                        K.DRAFT, K.ORDER_LV_PORT_TAG))
    order = [('KERNEL', ['JOIN', 'PORT', 'REGPOS', 'PINS']), ('CERTIFIED', []), ('REGISTERED', ['CONTROL', 'FACES', 'RECUT']), ('HELD', ['HELD'])]
    out = []
    for ft, ks in order:
        if not ks:
            out.append('%s -- NONE: no certified computation this act (nothing of the -15 control computed).' % ft)
        out += [keys[k] for k in ks]
    return out, keys, seats, order


def bank():
    import act_membrane as MEM
    import b712_record as REC
    out, keys, seats, order = lines()
    bad = [s['bank'] for s in seats if not s['ok']]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE STANDING REPORT, (R322)(3): THE LINES IN FOOTING ORDER, EACH RECOMPUTED FROM ITS BANKS (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), each line`s figures recomputed from the act`s JSON',
         '### banks, its SOURCE the bank by path, row and sha256. A report, not an arm: no verdict reads it. The scores line is printed after the',
         '### root by `tools/b712_report.py scores`, and written nowhere.', '']
    L += ['  (%d) %s' % (i + 1, l) for i, l in enumerate(out)]
    L += ['', '### SOURCES NOT SEATED (a needle not found or a bank absent): %s' % (bad or 'NONE'),
          '### ### **THE STANDING REPORT: %d LINES IN FOOTING ORDER ; SOURCES %d, SEATED %d ; THE SCORES LINE AFTER THE ROOT.**' % (
              len(out), len(seats), len(seats) - len(bad))]
    J = dict(at=at, lines=out, keys=keys, seats=seats, unseated=bad, footing=dict(order))
    for name, b in (('%s_report.txt' % ACT, (NL.join(L) + NL).encode('utf-8')),
                    ('%s_report.json' % ACT, (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(b)
        os.replace(p + '.tmp', p)
    print(NL.join(L[6:]))


def dry():
    out, _k, seats, _o = lines()
    print(NL.join('  (%d) %s' % (i + 1, l) for i, l in enumerate(out)))
    print('### SOURCES NOT SEATED: %s' % ([s['bank'] for s in seats if not s['ok']] or 'NONE'))


def scores():
    sc = jl('%s_scores_close.json' % ACT)
    keys = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    word = dict(HELD='HELD', REFUTED='BROKEN')
    roots = [l for l in rd('act_roots.txt').split(NL) if l.startswith(ACT + ' ')]
    print('### THE ROOT: %s' % (roots[-1] if roots else '### NOT APPENDED -- the scores line waits on the root'))
    print('### THE SCORES (relay data/%s_scores_close.json, sha256 %s…): %s' % (ACT, (sha('%s_scores_close.json' % ACT) or '### ABSENT')[:16],
          ' ; '.join('%s %s' % (k, word.get((sc.get(k) or ['?'])[0], (sc.get(k) or ['?'])[0])) for k in keys)))
    print('### ### **SCORES %d OF %d HELD -- PRINTED AFTER THE ROOT, WRITTEN NOWHERE.**' % (sum(1 for k in keys if (sc.get(k) or [''])[0] == 'HELD'), len(keys)))


def diff():
    """data/b712_report_diff.txt: (R322)(3)'s carry -- this tool against b711's report at the act's base (tools/b711_report.py at relay
    K.PRE_RELAY), by difflib over the two texts; written through the membrane before the root."""
    import difflib
    import act_membrane as MEM
    import b712_record as REC
    old = g(ROOT, 'show', '%s:tools/b711_report.py' % K.PRE_RELAY).replace('\r', '').split(NL)
    new = io.open(os.path.abspath(__file__), encoding='utf-8').read().replace('\r', '').split(NL)
    body = list(difflib.unified_diff(old, new, 'tools/b711_report.py@%s' % K.PRE_RELAY[:8], 'tools/b712_report.py', lineterm=''))
    add = sum(1 for l in body if l.startswith('+') and not l.startswith('+++'))
    rem = sum(1 for l in body if l.startswith('-') and not l.startswith('---'))
    L = ['%s -- (R322)(3): THE STANDING REPORT TOOL CARRIED FORWARD, ITS DIFF AGAINST b711`S REPORT (%s)' % (ACT, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
         '', '### tools/b712_report.py against tools/b711_report.py at relay %s: +%d -%d. The control of its form: `scores` writes nothing (the membrane' % (K.PRE_RELAY[:8], add, rem),
         '### refuses after the root; the route opens no file for writing), `bank` writes data/b712_report.txt and .json alone.', ''] + body + [
         '', '### ### **THE REPORT TOOL`S DIFF: +%d -%d AGAINST b711`S.**' % (add, rem)]
    p = os.path.join(D, '%s_report_diff.txt' % ACT)
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('bank', 'dry', 'scores', 'diff'):
        print('usage: b712_report.py bank | dry | scores | diff')
        sys.exit(2)
    dict(bank=bank, dry=dry, scores=scores, diff=diff)[r]()
