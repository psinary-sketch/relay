# -*- coding: utf-8 -*-
"""standing/v1352.py -- THE CONTROLS OF v1.35.2, (R366)(6): THE FAULTS REPEATED IN TWO ACTS OR MORE, THE NEXT BY COUNT (relay
data/b756_faults.txt), in v1351.py's form. BEFORE is the tree as BASE left it (relay 7fae9822, v1.35.1's own commit); AFTER is the working
tree. THE COMPILE CONTROL RUNS FIRST; the free memory is printed before each control. Nothing is written but this bank; no ledger line is
printed. Written at b756 by the Write tool; no identifier of the author is read into any string here.

  (editroute)  carried (11), 12 acts (b646-b711): G-EDIT-ROUTE retired at b719 (tools/standing/arms.py RETIRED) and its detail line still
               printing offences as an open gate (b754's "counts 3 sed offences"): the line says the arm is retired and not run.
  (ranahead)   carried (10), 8 acts: G-NOTHING-RAN-AHEAD's failure named no commit. tools/standing/ranahead.py reads the arm's clauses and
               returns what failed; over planted faces and logs it agrees with the arm (checks.tpl nothing_ahead_ok, read from the
               template and run) at each case; the suite prints it beside the arm.
  (deletefree) carried (9), 5 acts: G-DELETE-FREE failed on the lock gate's cleanup of its own temporary folder (tools/b756_lockgate.py
               :60-:64, :83, :97). b756's tools read by BASE's arm and by tools/standing/deletefree.py; planted removals of a tempfile path,
               a function's parameter so passed, a path not temporary, a shell delete; the arm's own plant still failing.
  (shared)     b755 (o), 3 acts: a shared tool committed without act_current's shared_edits. The one-call tool's new clause over b755's
               step-zero commit (relay 9171e0e2) replayed, and over planted staged sets; amend.py's `shared --staged`.
  (subject)    b755 (b), at b756 (d): the corpus controls read at PLACE-papers HEAD against lines fixed at 04fef04e; at HEAD 7 of 8, at the
               pin 8 of 8, the control route reading the pin.
  (scanheading) b755 (e), at b756 (b): the address scan's exception heading and BYLINE_FILES read from the act's own ferry at run time; at
               BASE a constant the carry shifts. The three ferries b754, b755, b756 read as their N5 lines say.
  (gitwrite)   the carried faults (1) and (2): RUNS_COMMIT read a compile of the tool as its run and a run inside a PowerShell block as none;
               the two forms of b754 (b') and (n'), and the forms that must stay a run, and a read naming the tool that must not.
  (version)    tools/standing/VERSION moved to v1.35.2.

  python -X utf8 -u tools/standing/v1352.py control [editroute|ranahead|deletefree|shared|subject|scanheading|gitwrite|version ...] [--bank]
"""
import io
import json
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
BASE = '7fae9822'   # ### v1.35.1's own commit (b756 component 5): the tree before this change
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)
import act_close as AC          # noqa: E402
import b703_checks as C3        # noqa: E402
import deletefree as DF         # noqa: E402
import ranahead as RAH          # noqa: E402
import gitwrite as GW           # noqa: E402
import commit as CM             # noqa: E402
import subject as SJ            # noqa: E402
from standing import arms as STA   # noqa: E402


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.35.1): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.35.2): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def both(L, cls, what, at_base, on_disk, holds_base, holds_disk):
    ok = bool(holds_base) and bool(holds_disk)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.35.1): %s -> (alike at both is wanted)' % at_base,
          '      AFTER  (v1.35.2): %s -> %s' % (on_disk, 'PASSES' if ok else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')


def upto(t, needle):
    return next((i for i, l in enumerate(t.split(NL)) if l.startswith(needle)), None)


def ctpl():
    return rd(os.path.join(S, 'fold', 'checks.tpl')), V.show(BASE, 'tools/standing/fold/checks.tpl')


# ================================================================================ (editroute)
def control_editroute():
    L, g, n = ['### (editroute): G-EDIT-ROUTE`S DETAIL LINE WHERE THE ARM IS RETIRED'], 0, 0
    ct, cb = ctpl()
    k = 'RETIRED by tools/standing/arms.py since b719 and not run'
    n += 1
    g += case(L, 'editroute', 'the detail line of checks.tpl (the arm in tools/standing/arms.py RETIRED: %s)' % ('G-EDIT-ROUTE' in STA.RETIRED),
              'the line says the arm is retired: %s' % (k in cb), 'the line says the arm is retired where it is: %s' % (k in ct and "if 'G-EDIT-ROUTE' in STA.RETIRED" in ct),
              k not in cb, k in ct and 'G-EDIT-ROUTE' in STA.RETIRED)
    a, b = upto(cb, 'def main():'), upto(ct, 'def main():')
    n += 1
    g += both(L, 'editroute', 'checks.tpl`s line-keyed region, to the part route`s main (the three checks.tpl changes of this version among them)', ':%s' % a, ':%s' % b, a is not None, a == b)
    return L, g, n


# ================================================================================ (ranahead)
def arm_fn():
    ct, _cb = ctpl()
    m = re.search(r'(?ms)^def nothing_ahead_ok\(.*?(?=^\S)', ct)
    ns = {'AC': AC, '__import__': __import__}
    exec(compile(m.group(0), 'checks.tpl:nothing_ahead_ok', 'exec'), ns)   # noqa: S102
    return ns['nothing_ahead_ok']


def control_ranahead():
    L, g, n = ['### (ranahead): G-NOTHING-RAN-AHEAD`S FAILURE NAMING ITS COMMITS'], 0, 0
    arm = arm_fn()
    steps = [dict(phase='gate', repo='relay', commit='aaaaaaa1'), dict(phase='component 1', repo='relay', commit='bbbbbbb2')]
    logs = [('aaaaaaa1ffff', 'b999 gate', 100), ('bbbbbbb2ffff', 'b999 component 1', 50), ('ccccccc3ffff', 'b999 component 2', 60)]
    face_ok = '## (0) WHAT RAN AHEAD OF THIS SEAL\n  bbbbbbb2 ; ccccccc3\n'
    face_miss = '## (0) WHAT RAN AHEAD OF THIS SEAL\n  bbbbbbb2\n'
    cases = (('no section (0)', 'nothing', 200), ('every commit declared', face_ok, 200), ('one commit undeclared', face_miss, 200), ('no lock time', face_ok, None))
    rows = []
    for nm, face, lock in cases:
        a = arm(face, lock, logs, steps)
        u = RAH.undeclared(face, lock, logs, steps)
        rows.append((nm, a, u, (a is True and u == []) or (a is False and (u is None or len(u) > 0))))
    n += 1
    g += case(L, 'ranahead', 'four planted states: the arm`s bool beside the reading`s commits (None where the arm fails before reading any)',
              'the arm alone: %s ; tools/standing/ranahead.py at BASE: %s' % ([(nm, a) for nm, a, _u, _k in rows], bool(V.show(BASE, 'tools/standing/ranahead.py'))),
              'the reading: %s' % [(nm, u) for nm, _a, u, _k in rows],
              not V.show(BASE, 'tools/standing/ranahead.py'), all(k for *_x, k in rows) and rows[2][2] == [('ccccccc3', 'b999 component 2')])
    ct, cb = ctpl()
    n += 1
    g += case(L, 'ranahead', 'the suite prints the reading beside the arm (checks.tpl, after the part route`s main)',
              'printed: %s' % ("__import__('ranahead').line(" in cb), 'printed where the part runs the arm: %s' % ("__import__('ranahead').line(" in ct and "if 'G-NOTHING-RAN-AHEAD' in names:" in ct),
              "__import__('ranahead').line(" not in cb, "__import__('ranahead').line(" in ct and "if 'G-NOTHING-RAN-AHEAD' in names:" in ct)
    return L, g, n


# ================================================================================ (deletefree)
def control_deletefree():
    L, g, n = ['### (deletefree): G-DELETE-FREE WITH A TEMPORARY FOLDER`S CLEANUP SET APART'], 0, 0
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b756_') and f.endswith('.py'))
    Sx = dict(tooltext=dict((f, C3.strip_prose(rd(f))) for f in tools))
    old = C3.no_delete(Sx)
    hits_old = [os.path.basename(f) for f, t in Sx['tooltext'].items() if DF.PAT.search(t)]
    new = DF.ok(Sx)
    n += 1
    g += case(L, 'deletefree', 'b756`s tools (%d, tools/b756_*.py, prose stripped as the suite strips it)' % len(tools),
              'tools/b703_checks.py no_delete %s ; the tools with a delete word %s' % (old, hits_old),
              'deletefree.ok %s ; the words left counting %s ; the lock gate`s cleanup set apart %s' % (
                  new, DF.found(Sx), sorted(DF.temp_cleanups(rd(os.path.join(T, 'b756_lockgate.py'))))),
              old is False and hits_old == ['b756_lockgate.py'], new is True)
    planted = NL.join(['import os, shutil, tempfile', 'tmp = tempfile.mkdtemp()', 'shutil.rmtree(tmp)',
                       'def _rm(path):', '    shutil.rmtree(path)', '_rm(tmp)',
                       'with tempfile.TemporaryDirectory() as d:', '    os.rmdir(d)',
                       'def gone(p):', '    os.remove(p)', "gone('data/x.txt')", "os.remove('data/y.txt')"])
    apart = DF.temp_cleanups(planted)
    want = {'shutil.rmtree(tmp)', 'shutil.rmtree(path)', 'os.rmdir(d)'}
    p_old = C3.no_delete(dict(tooltext={'p.py': planted}))
    p_hits = [l.strip() for l in planted.split(NL) if DF.PAT.search(l)]
    p_left = [l.strip() for l in planted.split(NL) if DF.PAT.search(l) and l.strip() not in apart]
    n += 1
    g += case(L, 'deletefree', 'PLANTED: removals of a tempfile path, a function`s parameter every call passes one, a TemporaryDirectory`s name; a parameter passed a data path, a data path',
              'no_delete %s ; counted %s' % (p_old, p_hits), 'set apart %s ; counted %s' % (sorted(apart), p_left),
              p_old is False and len(p_hits) == 5, apart == want and p_left == ['os.remove(p)', "os.remove('data/y.txt')"])
    sh = dict(tooltext={'x.py': 'os.system("git branch -D old")', 'y.py': 'rm -rf build'})
    s_hits = sorted(f for f, t in sh['tooltext'].items() if DF.PAT.search(t))
    s_new = sorted(f for f, _l in DF.found(sh, read=lambda p: ''))
    n += 1
    g += both(L, 'deletefree', 'a shell delete in a tool still counts (a branch`s -D, a rm -rf)', 'no_delete %s ; counted %s' % (C3.no_delete(sh), s_hits),
              'deletefree.ok %s ; counted %s' % (DF.ok(sh, read=lambda p: ''), s_new),
              C3.no_delete(sh) is False and s_hits == ['x.py', 'y.py'], DF.ok(sh, read=lambda p: '') is False and s_new == ['x.py', 'y.py'])
    pl = dict(Sx, tooltext=dict(Sx['tooltext'], x='os' + '.remove(p)'))
    n += 1
    g += both(L, 'deletefree', 'the arm`s own plant (checks.tpl :1814, `x` holding os.remove(p))', 'no_delete %s' % C3.no_delete(pl), 'deletefree.ok %s' % DF.ok(pl),
              C3.no_delete(pl) is False, DF.ok(pl) is False)
    ct, cb = ctpl()
    n += 1
    g += case(L, 'deletefree', 'checks.tpl :1813 reads the arm through deletefree.ok', "no_delete(S) %s" % ("lambda S: no_delete(S)," in cb),
              "deletefree.ok %s" % ("lambda S: __import__('deletefree').ok(S)," in ct), "lambda S: no_delete(S)," in cb, "lambda S: __import__('deletefree').ok(S)," in ct)
    return L, g, n


# ================================================================================ (shared)
def control_shared():
    L, g, n = ['### (shared): A SHARED TOOL STAGED WITH act_current`s shared_edits NAMING IT'], 0, 0
    names = [x for x in subprocess.run(['git', '-C', RELAY, 'show', '--name-only', '--format=', '9171e0e2'], capture_output=True, text=True).stdout.split(NL) if x.strip()]
    ac = json.loads(V.show('9171e0e2', 'data/act_current.json') or '{}')
    r = CM.shared_refusal('b755', names, ac.get('shared_edits'))
    OLD = types.ModuleType('commit_base')
    has_old = 'def shared_refusal(' in V.show(BASE, 'tools/standing/commit.py')
    n += 1
    g += case(L, 'shared', 'b755`s step-zero commit replayed (relay 9171e0e2: %s ; act_current`s shared_edits there %s)' % (names, ac.get('shared_edits')),
              'the one-call tool carries the clause: %s (the commit landed)' % has_old, 'refused: %s' % (r or 'NONE')[:150], not has_old, bool(r) and 'tools/mirror_prevbuild.json' in r)
    p = [('named', ['tools/mirror_prevbuild.json'], ['tools/mirror_prevbuild.json'], False), ('the act`s own', ['tools/b756_faults.py', 'tools/acts/b756.py', 'tools/standing/VERSION'], [], False),
         ('a bank', ['data/b756_events.txt'], [], False), ('unnamed', ['tools/b677_citation.py'], ['tools/mirror_prevbuild.json'], True)]
    res = [(nm, bool(CM.shared_refusal('b756', ns, ls))) for nm, ns, ls, _w in p]
    n += 1
    g += both(L, 'shared', 'PLANTED staged sets: a shared tool named, the act`s own files, a bank, a shared tool unnamed', 'no clause',
              'refused %s' % res, True, [x for _nm, x in res] == [w for *_y, w in p])
    am = rd(os.path.join(S, 'amend.py'))
    cm = rd(os.path.join(S, 'commit.py'))
    n += 1
    g += case(L, 'shared', 'amend.py `shared --staged` and the run`s call of the clause',
              'staged_shared %s ; run() calls %s' % ('def staged_shared(' in V.show(BASE, 'tools/standing/amend.py'), 'staged_shared_refusal(repo, act, names)' in V.show(BASE, 'tools/standing/commit.py')),
              'staged_shared %s ; --staged read %s ; run() calls %s' % ('def staged_shared(' in am, "'--staged' in argv" in am, 'bad = staged_shared_refusal(repo, act, names)' in cm),
              'def staged_shared(' not in V.show(BASE, 'tools/standing/amend.py'),
              'def staged_shared(' in am and "'--staged' in argv" in am and 'bad = staged_shared_refusal(repo, act, names)' in cm)
    return L, g, n


# ================================================================================ (subject)
def control_subject():
    L, g, n = ['### (subject): THE CORPUS CONTROLS READ AT THE COMMIT THEY WERE WRITTEN AGAINST'], 0, 0
    a_ok, a_L = SJ.control_corpus(ref='HEAD')
    b_ok, b_L = SJ.control_corpus(ref=SJ.CORPUS_PIN)
    fa = next((l for l in a_L if l.startswith('### THE CORPUS`S CONTROLS')), '')
    fb = next((l for l in b_L if l.startswith('### THE CORPUS`S CONTROLS')), '')
    src = rd(os.path.join(S, 'subject.py'))
    n += 1
    g += case(L, 'subject', 'the corpus controls of tools/standing/subject.py', 'read at PLACE-papers HEAD: %s' % fa, 'read at %s: %s ; the control route reads the pin %s' % (
        SJ.CORPUS_PIN, fb, 'control_corpus(ref=CORPUS_PIN)' in src), not a_ok, b_ok and 'control_corpus(ref=CORPUS_PIN)' in src)
    return L, g, n


# ================================================================================ (scanheading)
def control_scanheading():
    L, g, n = ['### (scanheading): THE ADDRESS SCAN`S EXCEPTION READ FROM THE ACT`S OWN FERRY'], 0, 0
    base = V.show(BASE, 'tools/b756_address_scan.py')
    hb = next((l for l in base.split(NL) if "'## THE EXCEPTION" in l), '')
    tool = rd(os.path.join(T, 'b756_address_scan.py'))
    hn = next((l for l in tool.split(NL) if "'## THE EXCEPTION" in l), '')
    m = types.ModuleType('scan_now')
    m.__file__ = os.path.join(T, 'b756_address_scan.py')
    src_fn = re.search(r'(?ms)^def ruling_byline\(.*?(?=^\S)', tool).group(0)
    exec(compile('import os, re\nNL = "\\n"\n' + src_fn, 'b756_address_scan.py:ruling_byline', 'exec'), m.__dict__)   # noqa: S102
    reads = [(a, m.ruling_byline(a)) for a in ('b754', 'b755', 'b756')]
    n += 1
    g += case(L, 'scanheading', 'the heading and BYLINE_FILES: a constant the carry shifts, or the act`s own ruling read at run time',
              'the heading names a ruling in its code: %s' % bool(re.search(r'\(R\d{3}\)`S N5', hb)),
              'the heading names none in its code: %s ; the three ferries read %s' % (not re.search(r'\(R\d{3}\)`S N5', hn), reads),
              bool(re.search(r'\(R\d{3}\)`S N5', hb)),
              not re.search(r'\(R\d{3}\)`S N5', hn) and reads == [('b754', ('R364', True)), ('b755', ('R365', False)), ('b756', ('R366', False))])
    return L, g, n


# ================================================================================ (gitwrite)
def control_gitwrite():
    L, g, n = ['### (gitwrite): THE ONE-CALL TOOL`S RUN READ BY ITS INTERPRETER`S FLAGS, A POWERSHELL BLOCK READ PAST'], 0, 0
    old, new = GW.RUNS_COMMIT_V121, GW.RUNS_COMMIT

    def runs(rx, cmd):
        return any(rx.match(c) for c in GW.commands(cmd))
    b1 = 'python -X utf8 -u -m py_compile tools/standing/commit.py'
    n1 = 'python -X utf8 -u "D:/x/flag.py" "w"; if ($?) { python -X utf8 -u tools/standing/commit.py relay add data/x.txt }'
    n += 1
    g += case(L, 'gitwrite', 'b754 (b`): a compile of the tool (data/b754_defects.txt :36)', 'a run: %s' % runs(old, b1), 'a run: %s' % runs(new, b1), runs(old, b1), not runs(new, b1))
    n += 1
    g += case(L, 'gitwrite', 'b754 (n`): a run inside a PowerShell block (data/b754_defects.txt :135-:137)', 'a run: %s' % runs(old, n1), 'a run: %s' % runs(new, n1), not runs(old, n1), runs(new, n1))
    stay = ['cd /d/relay && python -X utf8 -u "C:/s/flag754.py" "w" && python -X utf8 -u tools/standing/commit.py relay add data/x.txt',
            '& "C:\\Py\\python.exe" -X utf8 -u tools\\standing\\commit.py relay add data/x.txt',
            'python tools/standing/commit.py relay "component 5" "words"', 'python -X utf8 -u tools/standing/commit.py relay delete push-b756-record']
    sr = [(runs(old, c), runs(new, c)) for c in stay]
    n += 1
    g += both(L, 'gitwrite', 'the forms that are runs: bash after the flag read, PowerShell`s quoted interpreter, bare python, the delete route', '%s' % [a for a, _b in sr],
              '%s' % [b for _a, b in sr], all(a for a, _b in sr), all(b for _a, b in sr))
    rd_ = 'python -X utf8 -u tools/standing/peek.py tools/standing/commit.py 1 40'
    n += 1
    g += case(L, 'gitwrite', 'a read naming the tool (peek.py over commit.py)', 'a run: %s' % runs(old, rd_), 'a run: %s' % runs(new, rd_), runs(old, rd_), not runs(new, rd_))
    gw = rd(os.path.join(S, 'gitwrite.py'))
    n += 1
    g += both(L, 'gitwrite', 'the pattern stands in gitwrite.py as written (tools/standing/v1340.py`s delread control asks it there)', 'True',
              '%s' % (GW.RUNS_COMMIT.pattern in gw), True, GW.RUNS_COMMIT.pattern in gw)
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.35.1', ver == 'v1.35.2')
    return L, g, n


CONTROLS = dict(editroute=control_editroute, ranahead=control_ranahead, deletefree=control_deletefree, shared=control_shared,
                subject=control_subject, scanheading=control_scanheading, gitwrite=control_gitwrite, version=control_version)
ORDER = ('editroute', 'ranahead', 'deletefree', 'shared', 'subject', 'scanheading', 'gitwrite', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.35.2, (R366)(6): THE FAULTS REPEATED IN TWO ACTS OR MORE, THE NEXT BY COUNT (%s)' % (
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
    out.append('### ### **v1.35.2: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1352.txt' % act), NL.join(out))
        print('written data/%s_standing_v1352.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
