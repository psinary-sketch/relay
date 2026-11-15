# -*- coding: utf-8 -*-
"""standing/v1351.py -- THE CONTROLS OF v1.35.1, (R366)(6): THE FAULTS REPEATED IN TWO ACTS OR MORE, THE FIRST THREE BY COUNT (relay
data/b756_faults.txt), in v1350.py's form. BEFORE is the tree as BASE left it (relay 2c3acfca, v1.35.0's own commit); AFTER is the working
tree. THE COMPILE CONTROL RUNS FIRST; the free memory is printed before each control. Nothing is written but this bank; no ledger is read.
Written at b756 by the Write tool; no identifier of the author is read into any string here.

  (postseal)   carried (8), 23 acts: G-RULE-POSTSEAL-READ through tools/standing/postseal.py. At BASE wrap() took the bool predicate of
               tools/rule_arms.py ARMS and indexed it, so a passing reading raised TypeError (data/b755_checks_postpush.txt :89 PASS, :176
               the TypeError, :177 FAIL). Over a synthetic call trace: a passing trace through BASE's wrap raises, through the template's
               form reads True; a planted post-seal sed with a redirect reads False at both, the reading line now carrying the ordinal;
               checks.tpl's predicate and its reading line both read postseal.reading, the line-keyed region the same length.
  (carry)      b755 (n), 19 acts: a carried cite shifted to a bank absent from the tree. b755's own carry of its module reproduced by the
               code substitution at its tree (tools/acts/b754.py at relay 28255aea, the tree there): BASE prints nothing, the working
               carry.py prints the cite b755 (n) names (data/b754_attribution_plan.txt); b756's carry reproduced the same way, every cite
               printed; a planted shift to an absent bank printed, the act's own bank and an unchanged line not; the act carry tool and
               the standing carry both calling the print. G-BRANCHES-DELETED's needle wording, (n)'s second row, is no bank cite: the
               print does not reach it, and it stays the seat's read of the carried rows.
  (defectrow)  carried (6) and (12), 17 acts: the record's defect row of one prime. b754's bank read by b698's matcher (record.tpl :194)
               and by the foot's binding, against the tag scan; :194 unchanged, b754's override (MARK 7606fc9891fa) found once; the
               record rendered for b754, b755 and b756, the foot's binding in each.
  (version)    tools/standing/VERSION moved to v1.35.1.

  python -X utf8 -u tools/standing/v1351.py control [postseal|carry|defectrow|version ...] [--bank]
"""
import calendar
import io
import os
import re
import subprocess
import sys
import time
import types

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '2c3acfca'   # ### v1.35.0's own commit (b756 component 5): the tree before this change
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)
import fold as FD               # noqa: E402
import rule_arms as RA          # noqa: E402
from standing import postseal as PSL   # noqa: E402
from standing import carry as CR       # noqa: E402

TAGROW = re.compile(r"^ {4}\(([a-z]+[`'\u2019]*)\) [^\[\n]*\[(?:CLAIM|CLOSE)", re.M)


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.35.0): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.35.1): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def both(L, cls, what, at_base, on_disk, holds_base, holds_disk):
    ok = bool(holds_base) and bool(holds_disk)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.35.0): %s -> (alike at both is wanted)' % at_base,
          '      AFTER  (v1.35.1): %s -> %s' % (on_disk, 'PASSES' if ok else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def base_module(rel, name):
    m = types.ModuleType(name)
    m.__file__ = os.path.join(RELAY, *rel.split('/'))
    exec(compile(V.show(BASE, rel), 'BASE:' + rel, 'exec'), m.__dict__)   # noqa: S102
    return m


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')


def upto(t, needle):
    return next((i for i, l in enumerate(t.split(NL)) if l.startswith(needle)), None)


# ================================================================================ (postseal)
def trace(cmd):
    return dict(n=756, act='b756', seal_ct=calendar.timegm(time.strptime('2026-11-15T20:00:00Z', '%Y-%m-%dT%H:%M:%SZ')),
                calls=[dict(mid='m1', tid='t1', ts='2026-11-15T21:00:00Z', cmd=cmd, out='')])


def control_postseal():
    L, g, n = ['### (postseal): G-RULE-POSTSEAL-READ THROUGH ITS READING, NOT A BOOL WRAPPED AS A TUPLE'], 0, 0
    OLD = base_module('tools/standing/postseal.py', 'postseal_base')
    pred = next(p for nm, _r, p, _pl in RA.ARMS if nm == PSL.ARM)
    good = trace('python -X utf8 -u tools/standing/peek.py FINDINGS.md 1 40')
    try:
        r0 = 'returned %r' % (OLD.wrap(pred, 'b756')(good),)
        raised = False
    except TypeError as e:
        r0, raised = 'raised TypeError: %s' % e, True
    r1 = PSL.reading(RA, good, 'b756')
    n += 1
    g += case(L, 'postseal', 'a passing trace (one post-seal read of the entry by the reader, no filter, no redirect): the arm`s own reading %s' % (RA.reading(PSL.ARM, good)[:3],),
              'BASE`s wrap over ARMS` predicate: %s' % r0, 'the template`s form postseal.reading(...)[0]: %s ; the reading %s' % (r1[0], r1[3][:120]),
              raised, r1[0] is True and r1[3] == RA.reading(PSL.ARM, good)[3])
    bad = trace('sed -n 1p FINDINGS.md > /dev/null')
    o2 = OLD.wrap(pred, 'b756')(bad)
    r2 = PSL.reading(RA, bad, 'b756')
    n += 1
    g += case(L, 'postseal', 'PLANTED: a post-seal sed over the entry with a redirect',
              'the predicate %r ; the reading line RA.reading`s alone, no ordinal: %s' % (o2, 'FAILURE BY THE SUITE BANKS' in RA.reading(PSL.ARM, bad)[3]),
              'the predicate %r ; the reading line carries the ordinal: %s' % (r2[0], r2[3][r2[3].find(' ; THE ARM'):][:110]),
              o2 is False and 'FAILURE BY THE SUITE BANKS' not in RA.reading(PSL.ARM, bad)[3],
              r2[0] is False and 'FAILURE BY THE SUITE BANKS (LIVE FAILING before at b720' in r2[3])
    ct, cb = rd(os.path.join(S, 'fold', 'checks.tpl')), V.show(BASE, 'tools/standing/fold/checks.tpl')
    pred_new = "(lambda R: PSL.reading(RA, R, '⟪ACT⟫')[0]) if nm == PSL.ARM" in ct
    line_new = "PSL.reading(RA, S['ra'], '⟪ACT⟫') if nm == PSL.ARM else RA.reading(nm, S['ra'])" in ct
    n += 1
    g += case(L, 'postseal', 'checks.tpl: the predicate and the reading line through postseal.reading; PSL.wrap no longer called',
              'PSL.wrap called %d ; PSL.reading %d' % (cb.count('PSL.wrap('), cb.count('PSL.reading(')),
              'PSL.wrap called %d ; the predicate %s ; the reading line %s' % (ct.count('PSL.wrap('), pred_new, line_new),
              cb.count('PSL.wrap(') == 1 and cb.count('PSL.reading(') == 0, ct.count('PSL.wrap(') == 0 and pred_new and line_new)
    a, b = upto(cb, 'def main():'), upto(ct, 'def main():')
    n += 1
    g += both(L, 'postseal', 'checks.tpl`s line-keyed region (the acts before b735 key their overrides by line), to the part route`s main',
              ':%s' % a, ':%s' % b, a is not None, a == b)
    return L, g, n


# ================================================================================ (carry)
def tree(commit):
    out = subprocess.run(['git', '-C', RELAY, 'ls-tree', '-r', '--name-only', commit, '--', 'data'], capture_output=True, text=True).stdout
    return set(x.strip() for x in out.split(NL) if x.strip())


def subs_of(bank):
    m = re.search(r'the act names` substitution alone \(([^)]*)\)', rd(os.path.join(D, bank)))
    if not m:
        raise SystemExit('relay data/%s carries no substitution line' % bank)
    return [tuple(x.split(' -> ')) for x in m.group(1).split(', ')]


def control_carry():
    L, g, n = ['### (carry): A CARRIED CITE SHIFTED TO A BANK ABSENT FROM THE TREE, PRINTED AT THE CARRY'], 0, 0
    OLD = base_module('tools/standing/carry.py', 'carry_base')
    subs = subs_of('b755_carry_acts.txt')
    src = V.show('28255aea', 'tools/acts/b754.py')
    dst = CR.substitute_code(src, subs)
    have = tree('28255aea')
    ab = CR.shifted_absent(src, dst, 'b755', lambda p: p in have)
    names = sorted(set(p for _i, p, _s in ab))
    n += 1
    g += case(L, 'carry', 'b755`s carry of its module reproduced (tools/acts/b754.py at relay 28255aea, the code substitution %s, the tree there, %d banks)' % (
        ', '.join('%s -> %s' % s for s in subs), len(have)),
        'BASE`s carry.py prints such cites: %s' % hasattr(OLD, 'shifted_absent'),
        'printed %d cites of %d banks: %s ; b755 (n)`s data/b754_attribution_plan.txt among them %s' % (len(ab), len(names), names, 'data/b754_attribution_plan.txt' in names),
        not hasattr(OLD, 'shifted_absent'), 'data/b754_attribution_plan.txt' in names)
    subs6 = subs_of('b756_carry_acts.txt')
    src6 = V.show('b19867ac', 'tools/acts/b755.py')
    have6 = tree('b19867ac')
    ab6 = CR.shifted_absent(src6, CR.substitute_code(src6, subs6), 'b756', lambda p: p in have6)
    names6 = sorted(set(p for _i, p, _s in ab6))
    n += 1
    g += both(L, 'carry', 'b756`s carry of its module reproduced (tools/acts/b755.py at relay b19867ac, the tree there): every cite printed, each read against the act',
              'none printed', 'printed %d cites of %d banks: %s' % (len(ab6), len(names6), names6), True, all(p not in have6 for p in names6))
    s = NL.join(["a = 'data/b100_plan.txt'", "b = 'data/b101_own.txt'", "c = 'data/b090_gone.txt'"])
    d = NL.join(["a = 'data/b101_plan.txt'", "b = 'data/b102_own.txt'", "c = 'data/b090_gone.txt'"])
    pl = CR.shifted_absent(s, d, 'b102', lambda p: p in ('data/b100_plan.txt',))
    n += 1
    g += case(L, 'carry', 'PLANTED: a cite shifted from b100`s bank to b101`s (absent), the act`s own bank (b102), an unchanged line citing an absent bank',
              'no print', 'printed %s' % [(i, p) for i, p, _s in pl], True, [(i, p) for i, p, _s in pl] == [(1, 'data/b101_plan.txt')])
    ct = rd(os.path.join(T, 'b756_carry.py'))
    cs = rd(os.path.join(S, 'carry.py'))
    calls = (ct.count('CR.shifted_absent('), ct.count('CR.absent_lines('), cs.count('shifted_absent(old, new, act'), cs.count('absent_lines(absent)'))
    n += 1
    g += case(L, 'carry', 'the act carry tool (tools/b756_carry.py, carried to the next act by the standing carry) and the standing carry`s own route call the print',
              'the act tool %d, %d ; carry.py %d' % (V.show(BASE, 'tools/b756_carry.py').count('shifted_absent'), V.show(BASE, 'tools/b756_carry.py').count('absent_lines'),
                                                   V.show(BASE, 'tools/standing/carry.py').count('shifted_absent')),
              'the act tool shifted_absent %d, absent_lines %d ; carry.py carry() %d, %d' % calls, True, all(calls))
    return L, g, n


# ================================================================================ (defectrow)
FOOT = 'DEFECT_ROW = R.DEFECT_ROW = P3.DEFECT_ROW = P7.DEFECT_ROW = re.compile(r"^    \\(([a-z]\'*)\\) ")'


def control_defectrow():
    L, g, n = ['### (defectrow): THE RECORD`S DEFECT ROW WITH ANY NUMBER OF PRIMES, BOUND AT THE FOOT'], 0, 0
    m = re.search(r'^DEFECT_ROW = re\.compile\(r"(.*)"\)', rd(os.path.join(T, 'b698_record.py')), re.M)
    one = re.compile(m.group(1))
    rt = rd(os.path.join(S, 'fold', 'record.tpl'))
    fm = re.search(r'^DEFECT_ROW = R\.DEFECT_ROW = P3\.DEFECT_ROW = P7\.DEFECT_ROW = re\.compile\(r"(.*)"\)$', rt, re.M)
    anyp = re.compile(fm.group(1)) if fm else None
    t = rd(os.path.join(D, 'b754_defects.txt')).split(NL)
    tags = len(TAGROW.findall(NL.join(t)))
    a = sum(1 for l in t if one.match(l))
    b = sum(1 for l in t if anyp and anyp.match(l))
    n += 1
    g += case(L, 'defectrow', 'b754`s defects bank, %d rows by the tag scan (relay data/b754_defects.txt; b754 (m`` ) read 51 of 63)' % tags,
              'b698`s matcher (record.tpl :194, %r): %d rows' % (m.group(1), a), 'the foot`s binding (%r): %d rows' % (fm.group(1) if fm else None, b),
              a < tags, b == tags)
    rb = V.show(BASE, 'tools/standing/fold/record.tpl')
    l194 = (rt.split(NL)[193], rb.split(NL)[193])
    tpl = rt.splitlines(keepends=True)
    try:
        hit = FD.find_mark(tpl, '7606fc9891fa', 1, 'record')
    except Exception as e:  # noqa: BLE001
        hit = 'REFUSED %s' % e
    n += 1
    g += both(L, 'defectrow', 'record.tpl :194 as at BASE, b754`s override (MARK 7606fc9891fa, carried in b755`s and b756`s modules) found once',
              ':194 %r' % l194[1], ':194 equal %s ; the mark at %s' % (l194[0] == l194[1], hit), True, l194[0] == l194[1] and hit == (194, 194))
    out = []
    for act in ('b754', 'b755', 'b756'):
        try:
            r = FD.render(act, 'record')
            txt = r if isinstance(r, str) else ''.join(r) if isinstance(r, (list, tuple)) else str(r)
            i_foot, i_main = txt.find(FOOT), txt.find("if __name__ == '__main__':")
            out.append((act, 'rendered', i_foot > 0 and i_main > i_foot))
        except Exception as e:  # noqa: BLE001
            out.append((act, 'REFUSED %s' % str(e)[:80], False))
    n += 1
    g += case(L, 'defectrow', 'the record rendered for b754, b755 and b756 at the working template, the foot`s binding before the main guard in each',
              'BASE`s foot binds nothing: %s' % (FOOT not in rb), '%s' % out, FOOT not in rb, all(x[2] for x in out))
    a2, b2 = upto(rb, 'MIRROR_FOLDER_ROLE = '), upto(rt, 'MIRROR_FOLDER_ROLE = ')
    n += 1
    g += both(L, 'defectrow', 'record.tpl`s line-keyed region, to the foot`s first binding', ':%s' % a2, ':%s' % b2, a2 is not None, a2 == b2)
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.35.0', ver == 'v1.35.1')
    return L, g, n


CONTROLS = dict(postseal=control_postseal, carry=control_carry, defectrow=control_defectrow, version=control_version)
ORDER = ('postseal', 'carry', 'defectrow', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.35.1, (R366)(6): THE FAULTS REPEATED IN TWO ACTS OR MORE, THE FIRST THREE BY COUNT (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'written through tools/standing/figbank.py; no ledger line printed; the order and the counts from relay data/b756_faults.txt', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before and after, the tools before read from %s' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, g, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
        per.append('(%s) %d of %d' % (k, g, c))
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.35.1: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1351.txt' % act), NL.join(out))
        print('written data/%s_standing_v1351.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
