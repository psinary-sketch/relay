# -*- coding: utf-8 -*-
"""standing/v1348.py -- THE CONTROLS OF v1.34.8 (W-ORD-LABEL-READER, OPEN_TRAILS :13605, placed HERE at b756 under (R366)(5)(i) and passed
by the author at the put: relay data/b756_orders_read.txt (3); data/b756_author_answers.txt :4, :18), in v1347.py's form: each instance read
through tools/standing/roster.py as it stood at BASE (relay dc8319ea, v1.34.7's own commit, executed from its blob) and through the reader on
disk; AS WANTED where the reader before fails the instance and the reader after passes it, or where both read it alike and alike is wanted.
THE COMPILE CONTROL RUNS FIRST. The free memory is printed before each control. Nothing is written to the relay or to PLACE-papers but this
bank; PLACE-papers is read at its HEAD, and a line of a paper is printed by path, number and digest, never quoted (data/b754_rules.txt (7)).
Written at b756 by the Write tool; no identifier of the author is read into any string here.

  (label)    roster.version_of: a version string is a document's label only where it sits on the document's own label line, never where it
             follows a kernel's name. THE ORDER'S CONTROL: ONE_PAGE_PROOF's kernel tag -- its first line carrying a version string after a
             kernel's name, read at PLACE-papers HEAD -- planted as a heading at the document's head (b639's misreading, OPEN_TRAILS :13605):
             before, the kernel's tag read as the label; after, the document's own label line, one line down. Beside it: the document as it
             stands read alike; constructed headings; b754's version cases (tools/b754_agenda.py :455-:460) read alike; every .md file at
             PLACE-papers HEAD read alike, and the roster's current editions at main unmoved.
  (version)  tools/standing/VERSION moved to v1.34.8.

  python -X utf8 -u tools/standing/v1348.py control [label|version ...] [--bank]
"""
import hashlib
import io
import os
import sys
import time
import types

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = 'dc8319ea'   # ### v1.34.7's own commit (b756 component 1): the reader before this change
OPP = 'day1/ONE_PAGE_PROOF.md'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import roster as RO             # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)


def old_roster():
    """tools/standing/roster.py as BASE left it, executed from its blob under another name, its own imports resolving on disk."""
    src = V.show(BASE, 'tools/standing/roster.py')
    if src is None:
        raise SystemExit('### roster.py NOT READ AT %s -- NO CONTROL' % BASE)
    m = types.ModuleType('roster_base')
    m.__file__ = os.path.join(S, 'roster.py')
    exec(compile(src, 'BASE:roster.py', 'exec'), m.__dict__)   # noqa: S102
    return m


def pp_lines(rel, rev='HEAD'):
    """a PLACE-papers file's lines at `rev`, read through act.blob as roster.text_at reads them; None where it does not stand."""
    b = A.blob(rev, rel, 'pp')
    return None if b is None else b.decode('utf-8', 'replace').replace('\r', '').split(NL)


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def vs(r):
    k, v = r
    return '(:%s, %s)' % (k, 'v' + '.'.join(map(str, v)) if v else None)


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.7): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.34.8): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def both(L, cls, what, at_base, on_disk, holds_base, holds_disk):
    """a case wanted alike at both readers."""
    ok = bool(holds_base) and bool(holds_disk)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.7): %s -> (alike at both is wanted)' % at_base,
          '      AFTER  (v1.34.8): %s -> %s' % (on_disk, 'PASSES' if ok else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


# ================================================================================ (label)
def control_label():
    L, g, n = ['### (label): W-ORD-LABEL-READER, A VERSION STRING AFTER A KERNEL`S NAME IS NOT THE DOCUMENT`S LABEL (roster.version_of)'], 0, 0
    OR = old_roster()
    head = (A.gs('pp', 'rev-parse', '--short=8', 'HEAD') or '').strip()
    O = pp_lines(OPP)
    if not O:
        raise SystemExit('### %s NOT READ AT PLACE-papers HEAD -- NO CONTROL' % OPP)
    kt = next((k for k, l in enumerate(O, 1) if any(RO.after_kernel(l, m.start()) for m in RO.VSTR.finditer(l))), None)
    if not kt:
        raise SystemExit('### NO LINE OF %s CARRIES A VERSION STRING AFTER A KERNEL`S NAME -- NO CONTROL' % OPP)
    tag = next(tuple(int(x) for x in m.group(1).split('.')) for m in RO.VSTR.finditer(O[kt - 1]) if RO.after_kernel(O[kt - 1], m.start()))
    k0, v0 = RO.version_of(O)
    planted = ['## ' + O[kt - 1]] + O
    bo, bn = OR.version_of(planted), RO.version_of(planted)
    n += 1
    g += case(L, 'label', 'THE ORDER`S CONTROL: %s at PLACE-papers %s, its kernel tag (its line :%d, digest %s, the first of the file carrying a '
              'version string after a kernel`s name) planted as a heading at the document`s head' % (OPP, head, kt, digest(O[kt - 1])),
              'version_of %s, the kernel`s tag v%s read as the label' % (vs(bo), '.'.join(map(str, tag))),
              'version_of %s, the document`s own label line (:%s unplanted) one line down' % (vs(bn), k0),
              bo == (1, tag), bool(k0) and bn == (k0 + 1, v0) and v0 != tag)
    ao = OR.version_of(O)
    n += 1
    g += both(L, 'label', '%s as it stands at PLACE-papers %s: its own label line read alike' % (OPP, head), 'version_of %s' % vs(ao),
              'version_of %s' % vs((k0, v0)), bool(ao[1]), ao == (k0, v0))
    for lines, want_old, want_new, what in (
            (['# ONE PAGE PROOF', '', '## The proof at SIDE-kernel v1.7'], (3, (1, 7)), (None, None),
             'the orders read`s planted heading (tools/b756_orders.py :145): no label on the heading, none read'),
            (['# SIDE-kernel v1.7, the paper v2.1'], (1, (1, 7)), (1, (2, 1)), 'a heading carrying a kernel`s tag first: the next version string read'),
            (['## At `SIDE-explicit-formula` v0.38'], (1, (0, 38)), (None, None), 'a kernel`s name in backticks before its tag'),
            (['## SIDE-kernel’s tag v1.7'], (1, (1, 7)), (None, None), 'a kernel`s name, a possessive and the word tag before its tag'),
            (['## SIDE-lv-conservation main v0.10.0', '', 'v0.4, 2026-08-01'], (1, (0, 10, 0)), (3, (0, 4)),
             'a kernel`s name and the word main before its tag: the read goes on to the label line below')):
        o_, n_ = OR.version_of(lines), RO.version_of(lines)
        n += 1
        g += case(L, 'label', 'CONSTRUCTED: %s' % what, 'version_of %s' % vs(o_), 'version_of %s' % vs(n_), o_ == want_old, n_ == want_new)
    alike = [(['**v5.18, 2026-10-03** — x'], (5, 18)), (['# THE KEYSTONE CENSUS v0.8.3'], (0, 8, 3)), (['**Version:** 1.1.3'], (1, 1, 3)),
             (['no version here', 'nor here'], None), (['# head'] + ['x'] * 50 + ['*v0.8.3, 2026-10-27 -- a', '*v0.8.2, 2026-10-20 -- b'], (0, 8, 3)),
             (['**v0.4, 2026-08-01** — h'] + ['x'] * 50 + ['*v0.9, 2026-10-27 -- a'], (0, 4)),
             (['# THE PAPER v2.1 at SIDE-kernel v1.7'], (2, 1)), (['## Kernel v1.2 notes'], (1, 2))]
    ro = [OR.version_of(x)[1] for x, _w in alike]
    rn = [RO.version_of(x)[1] for x, _w in alike]
    n += 1
    g += both(L, 'label', 'CONSTRUCTED: b754`s version cases (tools/b754_agenda.py :455-:460) and two headings whose label comes first, read alike',
              ro, rn, ro == [w for _x, w in alike], rn == [w for _x, w in alike])
    md = [p for p in RO.main_tree('HEAD') if p.endswith('.md')]
    differ = []
    for p in md:
        x = pp_lines(p) or []
        if OR.version_of(x) != RO.version_of(x):
            differ.append(p)
    n += 1
    g += both(L, 'label', 'RECORD: every .md file at PLACE-papers %s (%d) read by both readers: the files where they differ' % (head, len(md)),
              '%d files read' % len(md), 'differ %d %s' % (len(differ), differ or ''), bool(md), not differ)
    t0 = time.time()
    r_old, r_new = OR.roster_at('main'), RO.roster_at('main')
    n += 1
    g += both(L, 'label', 'RECORD: the roster at main with rule (13) applied (roster_at, the act %s): its entries and their order' % A.current()['act'],
              '%d entries' % len(r_old), '%d entries ; equal %s ; %.1f s' % (len(r_new), r_old == r_new, time.time() - t0), bool(r_old), r_old == r_new)
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.34.7', ver == 'v1.34.8')
    return L, g, n


CONTROLS = dict(label=control_label, version=control_version)
ORDER = ('label', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.34.8, W-ORD-LABEL-READER: A VERSION STRING AFTER A KERNEL`S NAME IS NOT THE DOCUMENT`S LABEL (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each instance through both readers; the free memory read before each; '
           'written through tools/standing/figbank.py; a line of a paper by path, number and digest', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case through both readers, the reader before read from %s' % BASE, '']
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
    out.append('### ### **v1.34.8: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1348.txt' % act), NL.join(out))
        print('written data/%s_standing_v1348.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
