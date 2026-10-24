# -*- coding: utf-8 -*-
"""b709_report.py -- THE TWO CHECKS BEFORE THE ROOT AND THE SIX REPORT LINES, WRITTEN AFTER THE AUTHOR`S WORD AT THE ROOT (b709).

### data/b708_rules.txt row (1), carried: an act`s closing report tool is not among the tools sealed at Component 5; it is written by the Write
### tool after the author`s word at the root`s prompt names the report`s lines, run before the act root is computed so that the root names its
### bank, and the sealed closing tool prints the report`s lines from that bank. The author`s word at the root (data/b709_citation_check.txt, the
### check of 2026-10-24T20:42:56Z): "option 1 with one line added and two checks before it. Before the root: (i) b378`s lock-gate bank, overwritten
### by a stray call and restored, is shown byte-equal to its committed blob: git diff of that path against HEAD is printed empty, and its sha256 is
### printed beside the sha256 of the blob at HEAD, equal. If they are not equal, the root holds and the bank`s path is raised. (ii) The lean run
### behind N1 is printed by its test file, its command line and its time, and entered in the defects bank with how a test came to invoke lean on
### this host. Then the unsealed report tool, written by the Write tool, prints the ferry`s five lines and a sixth: the extended certified list of
### Q0`s zeros, from height 150 to the top reached, with its counts of on-line zeros and off-line pairs and its band count closed, and pairs 11
### and 15 entered as beyond reach at 325 with their required heights."
### Each line is read from its TEXT bank by the row`s own figures through the sealed record tool`s readers (imported, not edited); no compressed
### bank is opened here. Check (i) reads git`s diff and the two sha256 digests itself; where they differ this tool exits 3 and writes no report,
### and the root holds. UNSEALED: tools/b709_worklist.py SEALED names no report tool. Writes data/b709_report.txt and data/b709_report.json.
"""
import hashlib
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
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b709_worklist as K   # noqa: E402
import b709_record as REC   # noqa: E402  ### sealed, imported for its readers (_grid_read, _pairs_read) and nothing else

B378 = 'data/b378_lockgate.json'


def rd(n):
    p = os.path.join(D, n)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def jl(n):
    try:
        return json.load(io.open(os.path.join(D, n), encoding='utf-8'))
    except Exception:
        return {}


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(*a):
    r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True)
    return r.returncode, r.stdout


def check_i():
    """(i) b378`s lock-gate bank byte-equal to its committed blob: the diff against HEAD empty, the two sha256 digests equal."""
    rc, diff = git('diff', 'HEAD', '--', B378)
    work = open(os.path.join(ROOT, *B378.split('/')), 'rb').read()
    rc2, blob = git('show', 'HEAD:' + B378)
    h_work, h_head = hashlib.sha256(work).hexdigest(), hashlib.sha256(blob).hexdigest()
    ok = rc == 0 and diff == b'' and rc2 == 0 and h_work == h_head and work == blob
    lines = ['  (i) %s against HEAD: `git diff HEAD -- %s` printed %s (%d bytes of diff)' % (B378, B378, 'EMPTY' if diff == b'' else '### A DIFF', len(diff)),
             '      sha256 of the working file  %s (%d bytes)' % (h_work, len(work)),
             '      sha256 of the blob at HEAD  %s (%d bytes)' % (h_head, len(blob)),
             '      EQUAL %s -- %s' % (ok, 'the bank stands at its committed bytes; the root may be computed' if ok else '### NOT EQUAL: THE ROOT HOLDS, THE PATH RAISED')]
    return ok, lines, dict(path=B378, diff_bytes=len(diff), sha256_work=h_work, sha256_head=h_head, equal=ok)


def check_ii():
    """(ii) the lean run behind N1: the test file, its command line and its time, from the tests bank and the reader`s source."""
    t = rd('b709_tests_stepzero.txt')
    row = re.search(r'^  test_elab_reader_b634\.py\s+exit (\d+) ; (.*?) ; (\d+) s', t, re.M)
    c1 = re.search(r'^  the call: started (\w+) ; exit (\w+) ; (\d+) s ; free before (\d+) MB ; lowest (\d+) MB', t, re.M)
    c2 = re.search(r'^  the kernel`s call: started (\w+) ; exit (\w+) ; (\d+) s ; free before (\d+) MB ; in (\S+)', t, re.M)
    src = io.open(os.path.join(T, 'b634_elab.py'), encoding='utf-8', errors='replace').read().split(NL)
    popen = [(i + 1, l.strip()) for i, l in enumerate(src) if "'lake', 'env', 'lean'" in l]
    stamp = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', t.split(NL)[0])
    d = rd('b709_defects.txt')
    entered = 'HOW A TEST CAME TO INVOKE LEAN ON THIS HOST' in d
    ok = bool(row) and bool(c1) and bool(c2) and bool(popen) and entered
    lines = ['  (ii) the lean run behind N1: the test file tools/test_elab_reader_b634.py (run by tools/b709_tests.py, part 5 of 7 at step zero; the bank written %s)' % (stamp.group(1) if stamp else '-'),
             '      its command line: tools/b634_elab.py `call` runs %s in the kernel`s checkout by subprocess -- %s' % (
                 "['lake', 'env', 'lean', <generated file>]", ' ; '.join(':%d %s' % (n, l[:110]) for n, l in popen) or '### NOT FOUND'),
             '      its time: the test %s s, exit %s (%s) ; the first call %s s (started %s, exit %s, free before %s MB, lowest %s MB) in D:/SIDE-explicit-formula ; the kernel`s call %s s (started %s, exit %s, free before %s MB) in %s' % (
                 row.group(3) if row else '-', row.group(1) if row else '-', row.group(2) if row else '-',
                 c1.group(3) if c1 else '-', c1.group(1) if c1 else '-', c1.group(2) if c1 else '-', c1.group(4) if c1 else '-', c1.group(5) if c1 else '-',
                 c2.group(3) if c2 else '-', c2.group(1) if c2 else '-', c2.group(2) if c2 else '-', c2.group(4) if c2 else '-', c2.group(5) if c2 else '-'),
             '      entered in the defects bank with how a test came to invoke lean on this host (relay data/b709_defects.txt (c)): %s' % entered]
    return ok, lines, dict(test='tools/test_elab_reader_b634.py', seconds=int(row.group(3)) if row else None, call1=c1.groups() if c1 else None,
                           call2=c2.groups() if c2 else None, popen_lines=popen, entered=entered)


def main():
    ok1, L1, j1 = check_i()
    ok2, L2, j2 = check_ii()
    head = ['%s -- THE TWO CHECKS BEFORE THE ROOT AND THE SIX REPORT LINES, BY THE UNSEALED REPORT TOOL AFTER THE AUTHOR`S WORD AT THE ROOT (%s)' % ('b709', utc()), '',
            '### THE TWO CHECKS BEFORE THE ROOT (the author`s word at the root`s prompt, data/b709_citation_check.txt, the check of 2026-10-24T20:42:56Z):'] + L1 + L2 + ['']
    if not ok1:
        head += ['### ### **CHECK (i) NOT EQUAL -- THE ROOT HOLDS ; %s RAISED ; NO REPORT WRITTEN.**' % B378]
        print(NL.join(head))
        return 3
    G, Pz = REC._grid_read(), REC._pairs_read()
    fr, fb = G['fam']['rho0'], G['fam']['band']
    line1 = ('the onset per family with its rung and eigenvalue (relay data/b709_grid.txt): the band zero`s family -- the rung log %s (%s) at a = %s +- %s, lambda_min %s +- %s, '
             'Lambda_Q(%s) = 0 (no Q0 term enters there), the nearest entering rungs log %s (%d points below) and log %s (%d points above), %d negative readings of %d points; '
             'rho_0`s family -- the midpoint between log %s and log %s at a = %s +- %s, lambda_min %s +- %s, the rung log %s one half-step below it read %s, '
             'the nearest entering rungs log %s (%d points below) and log %s (%d points above), %d negative readings of %d points; the hypothesis %s / %s and the falsifier '
             '%s / %s (band / rho_0), each vacuous as worded' % (
                 fb.get('rung', '-'), fb.get('rung_pow', '-'), fb.get('a', '-'), fb.get('a_err', '-'), fb.get('lam', '-'), fb.get('lam_err', '-'), fb.get('rung', '-'),
                 fb.get('below', '-'), fb.get('below_pts', 0), fb.get('above', '-'), fb.get('above_pts', 0), fb.get('neg', 0), fb['rows'],
                 fr.get('mid_lo', '-'), fr.get('mid_hi', '-'), fr.get('a', '-'), fr.get('a_err', '-'), fr.get('lam', '-'), fr.get('lam_err', '-'), fr.get('rung_below', '-'),
                 fr.get('read_at_rung', '-'), fr.get('below', '-'), fr.get('below_pts', 0), fr.get('above', '-'), fr.get('above_pts', 0), fr.get('neg', 0), fr['rows'],
                 fb['hyp'], fr['hyp'], fb['fal'], fr['fal']))
    line2 = ('the zeta control`s lambda_min beside its tail bound (relay data/b709_grid.txt, (C2), tools/b696_witness_balls.py`s certified archimedean tails of the three windows): '
             'at the band`s onset point %s, zeta lambda_min %s +- %s %s, tails %s ; at rho_0`s onset point %s, zeta lambda_min %s +- %s %s, tails %s ; positive beyond its bound at '
             'every point of both families (%d of %d and %d of %d), the largest tail ball %.2e (band) and %.2e (rho_0)' % (
                 fb.get('name', '-'), fb.get('zeta_lam', '-'), fb.get('zeta_err', '-'), fb.get('zeta_flag', '-'), ' '.join(fb.get('tails', ())) or '-',
                 fr.get('name', '-'), fr.get('zeta_lam', '-'), fr.get('zeta_err', '-'), fr.get('zeta_flag', '-'), ' '.join(fr.get('tails', ())) or '-',
                 fb['zeta_pos'], fb['rows'], fr['zeta_pos'], fr['rows'], fb['tails_max'], fr['tails_max']))
    line3 = ('the twelve ratios n*/predicted (relay data/b709_pairs.txt, the registration`s falsifier [0.67, 1.5]): %s ; computed %d, within %d, outside %d, beyond reach %d ; '
             'the falsifier %s' % (
                 ' ; '.join('pair %d %s' % (r['idx'], ('%s (n* %s, predicted %s)' % (r['ratio'], r['nstar'], r['predicted'])) if r['ratio'] else ('beyond reach at height %d, T0` > %s needed' % (r['height'], r['need'])))
                            for r in Pz['rows']), len(Pz['within']) + len(Pz['outside']), len(Pz['within']), len(Pz['outside']), len(Pz['beyond']),
                 'HELD over the pairs computed' if not Pz['outside'] else 'REFUTED on %s' % Pz['outside']))
    pj = jl('b709_port.json')
    line4 = ('the port`s modules built and next failing line (relay data/b709_port.txt, run %s on port-b707 at %s, conclusion %s, the artifact %s agreeing with the platform`s digest): '
             'modules built %d of %d -- %s ; the module held %s ; the next failing line %s (%s) ; the lines after it %s ; remaining %d ; the print step %s ; grade claimed %s' % (
                 pj.get('run_id'), K.PORT_TIP[:8], (pj.get('run') or {}).get('conclusion'), ((pj.get('artifact') or {}).get('sha256') or '-')[:16],
                 len(pj.get('built') or []), len(pj.get('modules') or []), ', '.join(pj.get('built') or []), ', '.join(pj.get('held') or []),
                 (pj.get('first_error') or '-').replace('error: ', '').split(': ')[0], ((pj.get('kinds') or [['', '-']])[0][1]),
                 ' ; '.join('%s -- %s' % (e.replace('error: ', '').split(': ')[0], k) for e, k in (pj.get('kinds') or [])[1:]), len(pj.get('remaining') or []),
                 pj.get('print_step'), pj.get('grade_claimed')))
    figs = rd('b709_standing_figures.txt')
    fr_ = dict((k, (a_, b_)) for k, a_, b_ in re.findall(r'^  (correspondence|readme|partners|pins)\s+b709 (\S+) ; b708 (\S+) ;', figs, re.M))
    line5 = ('the four standing arms` figures beside b708`s (relay data/b709_standing_figures.txt, by tools/b706_standing_figures.py over b706`s roster against data/b708_standing_figures.json, '
             'both kernels on main at the read): %s' % ' ; '.join('%s %s (b708 %s)' % (k, fr_.get(k, ('-', '-'))[0], fr_.get(k, ('-', '-'))[1]) for k in ('correspondence', 'readme', 'partners', 'pins')))
    beyond = [r for r in Pz['rows'] if r['verdict'].startswith('beyond reach')]
    line6 = ('the extended certified list of Q0`s zeros (relay data/b709_pairs.txt, THE EXTENSION BY BAND; b667`s engine, the Bessel rung at 2000 bits): from height 150 to the top reached, %s '
             '(the author`s bound of 2026-10-24) ; %d bands, every one COMPLETE with N = on-line + 2 x off-line, closed ; new on-line zeros %s by certified sign changes of Lambda_Q ; '
             'new off-line pairs %s located by Newton on point values ; representatives %s ; the bands: %s ; pairs %s entered as beyond reach at height %d with their required heights: %s' % (
                 Pz['height'], len(Pz['bands']), Pz['new_on'], Pz['new_off'], Pz['reps'],
                 ' ; '.join('[%s, %s] N %d on %d off %d %s' % (b['lo'], b['hi'], b['n'], b['on'], b['off'], b['status']) for b in Pz['bands']),
                 ', '.join(str(r['idx']) for r in beyond), K.PAIRS_BOUND, ' ; '.join('pair %d T0` > %s' % (r['idx'], r['need']) for r in beyond)))
    lines = [line1, line2, line3, line4, line5, line6]
    L = head + ['### rows are the six lines (the ferry`s Component 6 five and the author`s sixth at the root), each read from its text bank by this unsealed tool',
                '### (data/b708_rules.txt row (1), carried); the sealed closing prints them from this bank.', ''] + ['  (%d) %s' % (i + 1, l) for i, l in enumerate(lines)] + [
        '', '### ### **CHECKS 2 (i EQUAL %s ; ii PRINTED AND ENTERED %s) ; LINES 6 ; THE BAND`S ONSET %s a = %s ; rho_0`S ONSET %s a = %s ; ZETA POSITIVE AT EVERY POINT %s ; '
        'PAIRS WITHIN %d OF %d COMPUTED, BEYOND REACH %d ; MODULES BUILT %d OF %d, NEXT %s ; THE LIST TO %s, %d BANDS CLOSED, ON-LINE %s, OFF-LINE PAIRS %s ; THE FIGURES %s AGAINST b708`S %s.**' % (
            ok1, ok2, fb.get('name', '-'), fb.get('a', '-'), fr.get('name', '-'), fr.get('a', '-'), fb['zeta_pos'] == fb['rows'] and fr['zeta_pos'] == fr['rows'],
            len(Pz['within']), len(Pz['within']) + len(Pz['outside']), len(Pz['beyond']), len(pj.get('built') or []), len(pj.get('modules') or []),
            (pj.get('first_error') or '-').replace('error: ', '').split(': ')[0], Pz['height'], len(Pz['bands']), Pz['new_on'], Pz['new_off'],
            ', '.join('%s %s' % (k, fr_.get(k, ('-', '-'))[0]) for k in ('correspondence', 'readme', 'partners', 'pins')),
            ', '.join(fr_.get(k, ('-', '-'))[1] for k in ('correspondence', 'readme', 'partners', 'pins')))]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b709_report.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    j = dict(at=utc(), checks=dict(i=j1, ii=j2), lines=lines, band=dict(name=fb.get('name'), a=fb.get('a'), lam=fb.get('lam'), rung=fb.get('rung')),
             rho0=dict(name=fr.get('name'), a=fr.get('a'), lam=fr.get('lam'), mid=(fr.get('mid_lo'), fr.get('mid_hi'))),
             pairs=dict(within=Pz['within'], outside=Pz['outside'], beyond=[r['idx'] for r in beyond], height=Pz['height'], bands=len(Pz['bands']), new_on=Pz['new_on'], new_off=Pz['new_off']),
             port=dict(built=len(pj.get('built') or []), modules=len(pj.get('modules') or []), next=pj.get('first_error')), figures=fr_)
    pj_ = os.path.join(D, 'b709_report.json')
    with open(pj_ + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(pj_ + '.tmp', pj_)
    print(NL.join(L))
    return 0 if (ok1 and ok2) else 1


if __name__ == '__main__':
    sys.exit(main())
