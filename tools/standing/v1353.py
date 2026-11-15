# -*- coding: utf-8 -*-
"""standing/v1353.py -- THE CONTROLS OF v1.35.3, (R366)(6): [H1]'S HELD PART, THE HANDOFF PAGE IN THE ARCHIVE, in v1352.py's form.
[H1] passed as (a) at b754 (relay data/b754_author_answers.txt :131): the handoff page joins the archive's roster and the Project set. The
roster is read from PLACE-papers' tree and the builder copied from PLACE-papers alone, so the part was held and carried ("the relay's
HANDOFF.md in the archive and the Project set by a second source", data/b754_rules.txt :107-:108). BEFORE is the tree as BASE left it (relay
aadd9d2d); AFTER the working tree. The builder and the verifier, beyond the ruling's (W) list, were banked first by the item route (row 1 of
data/b756_amendments.json, `amend.py pass [H1] ... --under=6`). THE COMPILE CONTROL RUNS FIRST; the free memory is printed before each
control. Nothing is written but this bank and files in temporary folders the controls make and the host removes; no build is run, no zip
written beside the mirror, tools/mirror_prevbuild.json not touched. Written at b756 by the Write tool.

  (second)   tools/standing/roster.py: the relay's page copied into a stage as the blob at the relay's HEAD under the builder's flat-name
             rule, its row and its MANIFEST line; a stage already holding the name refused with nothing written; the line read back, and
             read by no `@` the verifier's source-head matcher takes.
  (builder)  tools/mirror_build.ps1: parsed by PowerShell's own parser at BASE and on disk; its new block run alone by PowerShell into a
             temporary stage; its byte-order mark as BASE's.
  (verify)   tools/mirror_verify.py clause 3: an export carrying the page read CLEAN where its MANIFEST declares the second source, NOT CLEAN
             where it declares none or the page is missing; b755's export read as it was built.
  (manifest) tools/standing/manifest.py control_at_build: the page's zip entry read against the relay's blob at the declared commit.
  (project)  the Project set carries the page from b756, its bytes the relay's blob; b755's set unchanged.
  (amend)    tools/standing/amend.py pass: the clause ordering the item (--under), so row 1 reads (R366)(6) and not (5).
  (version)  tools/standing/VERSION moved to v1.35.3.

  python -X utf8 -u tools/standing/v1353.py control [second|builder|verify|manifest|project|amend|version ...] [--bank]
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import zipfile

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = 'aadd9d2d'   # ### the relay's HEAD before this change (b756 component 5, step 35)
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)
import v1345 as V45             # noqa: E402  (parse_errors)
import roster as RO             # noqa: E402
import mirror_verify as MV      # noqa: E402
import manifest as MF           # noqa: E402
import amend as AM              # noqa: E402

BUILDER = 'tools/mirror_build.ps1'


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.35.2): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.35.3): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def both(L, cls, what, at_base, on_disk, holds_base, holds_disk):
    ok = bool(holds_base) and bool(holds_disk)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.35.2): %s -> (alike at both is wanted)' % at_base,
          '      AFTER  (v1.35.3): %s -> %s' % (on_disk, 'PASSES' if ok else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def page():
    return A.git('relay', 'show', 'HEAD:HANDOFF.md') or b''


def prev_zip():
    prev = A.prev_of(A.current()['act'])
    out = A.jl('%s_mirror_build.json' % prev).get('out') or ''
    mz = re.search(r'^built: (.+)$', out, re.M)
    zp = mz.group(1).strip() if mz else None
    return prev, (zp if zp and os.path.isfile(zp) else None), A.jl('%s_mirror_build.json' % prev).get('pp_head')


# ================================================================================ (second)
def control_second():
    L, g, n = ['### (second): THE RELAY`S PAGE COPIED INTO THE BUILDER`S STAGE BY tools/standing/roster.py'], 0, 0
    pb = page()
    head = A.gs('relay', 'rev-parse', '--short', 'HEAD')
    has_old = 'def second_copy(' in (V.show(BASE, 'tools/standing/roster.py') or '')
    with tempfile.TemporaryDirectory(prefix='v1353_') as st:
        with open(os.path.join(st, 'A.md'), 'wb') as f:
            f.write(b'# a roster file\n')
        r = RO.second_copy(st)
        got = open(os.path.join(st, 'HANDOFF.md'), 'rb').read() if os.path.isfile(os.path.join(st, 'HANDOFF.md')) else None
        row = (r.get('rows') or [{}])[0]
        ok = (got == pb and len(r['rows']) == 1 and row.get('file') == 'HANDOFF.md' and row.get('bytes') == len(pb)
              and row.get('md5') == hashlib.md5(pb).hexdigest() and r.get('line') == 'Second source: the relay at commit %s (its HEAD): HANDOFF.md.' % head)
    n += 1
    g += case(L, 'second', 'a stage holding one roster file; the relay`s HANDOFF.md at HEAD %s (%d bytes, md5 %s)' % (head, len(pb), hashlib.md5(pb).hexdigest()[:12]),
              'roster.py carries a second source: %s' % has_old,
              'staged equal to the blob %s ; row %s ; line %r' % (got == pb, dict((k, row.get(k)) for k in ('file', 'bytes', 'version', 'commit')), r.get('line')),
              not has_old, ok)
    with tempfile.TemporaryDirectory(prefix='v1353_') as st:
        with open(os.path.join(st, 'HANDOFF.md'), 'wb') as f:
            f.write(b'x')
        try:
            RO.second_copy(st)
            refused, msg = False, 'copied'
        except SystemExit as e:
            refused, msg = True, str(e)[:90]
        kept = open(os.path.join(st, 'HANDOFF.md'), 'rb').read() == b'x'
    n += 1
    g += both(L, 'second', 'a stage already holding HANDOFF.md at the root (no parent to disambiguate): refused, the planted file kept',
              'the builder`s own collision rule (tools/mirror_build.ps1 :65-:67)', 'refused %s (%s) ; the planted file kept %s' % (refused, msg, kept), True, refused and kept)
    line = RO.second_line(head)
    man = 'Source: PLACE-papers @ `1234abc` (main). Export x. 2 files flat.\n%s\n' % line
    m1 = MV.HEAD.search(man)
    n += 1
    g += both(L, 'second', 'the line read back, and the verifier`s source-head matcher (tools/mirror_verify.py HEAD) over a MANIFEST carrying it',
              'no line', 'declared %s ; the head matcher reads %s ; over the line alone %s' % (RO.second_declared(man), m1.group(1) if m1 else None, MV.HEAD.search(line)),
              True, RO.second_declared(man) == ['HANDOFF.md'] and m1 and m1.group(1) == '1234abc' and MV.HEAD.search(line) is None and RO.second_declared('Source: x') is None)
    return L, g, n


# ================================================================================ (builder)
BLOCK = re.compile(r'(?ms)^\$secondJson = .*?^\}\n')


def control_builder():
    L, g, n = ['### (builder): THE BUILDER`S SECOND SOURCE (tools/mirror_build.ps1)'], 0, 0
    oldb = A.blob(BASE, BUILDER) or b''
    newb = open(os.path.join(RELAY, *BUILDER.split('/')), 'rb').read()
    old = oldb.decode('utf-8-sig', 'replace').replace('\r', '')
    new = newb.decode('utf-8-sig', 'replace').replace('\r', '')
    po, pn = V45.parse_errors(old), V45.parse_errors(new)
    n += 1
    g += both(L, 'builder', 'PowerShell`s own parser over the builder', 'parse errors %s' % po, 'parse errors %s' % pn, po == 0, pn == 0)
    m = BLOCK.search(new)
    block = m.group(0) if m else ''
    out, staged = '', None
    with tempfile.TemporaryDirectory(prefix='v1353_') as st:
        stage = os.path.join(st, 'stage')
        os.mkdir(stage)
        snip = os.path.join(st, 'snip.ps1')
        body = NL.join(["$rosterTool = '%s'" % os.path.join(S, 'roster.py'), "$stage = '%s'" % stage, '$rows = @()', block,
                        'Write-Output ("ROWS " + $rows.Count + " " + $rows[0].file + " " + $rows[0].bytes + " " + $rows[0].md5)',
                        'Write-Output ("LINE " + $second.line)'])
        with io.open(snip, 'w', encoding='utf-8-sig', newline='\r\n') as f:
            f.write(body + NL)
        r = subprocess.run(['powershell', '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Bypass', '-File', snip], capture_output=True, text=True,
                           encoding='utf-8', errors='replace')
        out = (r.stdout or '').strip()
        sp = os.path.join(stage, 'HANDOFF.md')
        staged = open(sp, 'rb').read() if os.path.isfile(sp) else None
    pb = page()
    want_rows = 'ROWS 1 HANDOFF.md %d %s' % (len(pb), hashlib.md5(pb).hexdigest())
    head = A.gs('relay', 'rev-parse', '--short', 'HEAD')
    n += 1
    g += case(L, 'builder', 'the new block run alone by PowerShell into a temporary stage (the lines from `$secondJson = ` to its loop`s close)',
              'the builder calls `roster.py second`: %s' % ('$rosterTool second $stage' in old),
              'block found %s ; printed %r ; the staged page equal to the blob %s' % (bool(block), out.replace(NL, ' | ')[:200], staged == pb),
              '$rosterTool second $stage' not in old,
              bool(block) and want_rows in out and ('LINE Second source: the relay at commit %s (its HEAD): HANDOFF.md.' % head) in out and staged == pb)
    n += 1
    g += case(L, 'builder', 'the line declared under the source line, the rows before the table', 'declared: %s' % ('$man += $second.line' in old),
              'declared after the source line: %s' % (re.search(r'(?m)^\$man \+= "Source: PLACE-papers @ .*\n\$man \+= \$second\.line$', new) is not None),
              '$man += $second.line' not in old, re.search(r'(?m)^\$man \+= "Source: PLACE-papers @ .*\n\$man \+= \$second\.line$', new) is not None)
    n += 1
    g += both(L, 'builder', 'the byte-order mark (PowerShell 5.1 reads a file without one in the host`s codepage)', 'BOM %s' % oldb.startswith(b'\xef\xbb\xbf'),
              'BOM %s' % newb.startswith(b'\xef\xbb\xbf'), True, newb.startswith(b'\xef\xbb\xbf') == oldb.startswith(b'\xef\xbb\xbf'))
    return L, g, n


# ================================================================================ (verify)
def control_verify():
    L, g, n = ['### (verify): CLAUSE 3 WITH THE SECOND SOURCE DECLARED (tools/mirror_verify.py)'], 0, 0
    names = MV.staged_names(RO.roster_at('main'))
    with_page = names + ['HANDOFF.md']
    rmain = RO.roster_at('main')
    old_c, _m = MV.clause3(with_page, paths=rmain)
    c_decl, _m = MV.clause3(with_page, paths=rmain + RO.second_paths(['HANDOFF.md']))
    c_miss, _m = MV.clause3(names, paths=rmain + RO.second_paths(['HANDOFF.md']))
    c_none, _m = MV.clause3(with_page, paths=rmain + RO.second_paths(None))
    src = rd(os.path.join(T, 'mirror_verify.py'))
    n += 1
    g += case(L, 'verify', 'an export carrying the roster at main and the page (%d names)' % len(with_page),
              'clause 3 over the roster alone: CLEAN %s' % old_c,
              'declared: CLEAN %s ; declared, the page missing: CLEAN %s ; not declared, the page carried: CLEAN %s ; main reads the declaration %s' % (
                  c_decl, c_miss, c_none, 'SR.second_paths(sec)' in src and 'sec = SR.second_declared(man)' in src),
              old_c is False, c_decl is True and c_miss is False and c_none is False and 'SR.second_paths(sec)' in src)
    prev, zp, bhead = prev_zip()
    n += 1
    if not zp or not bhead:
        g += both(L, 'verify', '%s`s export' % prev, 'ABSENT', 'ABSENT', False, False)
    else:
        z = zipfile.ZipFile(zp)
        pn = [x for x in z.namelist() if x != 'MANIFEST.md']
        pman = z.read('MANIFEST.md').decode('utf-8', 'replace')
        sec = RO.second_declared(pman)
        full = A.gs('pp', 'rev-parse', '--verify', '--quiet', bhead + '^{commit}')
        a, _m = MV.clause3(pn, paths=RO.roster_at(full, act=prev))
        b, _m = MV.clause3(pn, paths=RO.roster_at(full, act=prev) + RO.second_paths(sec))
        g += both(L, 'verify', '%s`s export (%d files) at its source head %s, read as it was built' % (prev, len(pn), (bhead or '')[:12]),
                  'clause 3 CLEAN %s' % a, 'the second source declared %s ; clause 3 CLEAN %s' % (sec, b), a is True, sec is None and b is True)
    return L, g, n


# ================================================================================ (manifest)
def planted_zip(d, name, man, files, entry):
    """an export as the builder makes it: each roster file at the build commit under the builder's flat name, the MANIFEST, the page."""
    p = os.path.join(d, name)
    with zipfile.ZipFile(p, 'w') as z:
        z.writestr('MANIFEST.md', man)
        for flat, b in files:
            z.writestr(flat, b)
        if entry is not None:
            z.writestr('HANDOFF.md', entry)
    return p


def base_manifest():
    """BASE's tools/standing/manifest.py, run as it stood (its control_at_build reading the roster's files alone)."""
    import types
    m = types.ModuleType('manifest_base')
    m.__file__ = os.path.join(S, 'manifest.py')   # ### its sys.path line reads it
    exec(compile(V.show(BASE, 'tools/standing/manifest.py'), 'manifest.py@' + BASE, 'exec'), m.__dict__)   # noqa: S102
    return m


def control_manifest():
    L, g, n = ['### (manifest): THE MANIFEST CONTROL READS THE PAGE AGAINST THE RELAY`S BLOB (tools/standing/manifest.py control_at_build)'], 0, 0
    pb = page()
    head = A.gs('relay', 'rev-parse', '--short', 'HEAD')
    build = A.gs('pp', 'rev-parse', 'HEAD')
    roster = RO.roster_at(build)
    flats = MV.staged_names(roster)
    files = [(f, A.blob(build, p, 'pp') or b'') for f, p in zip(flats, roster)]
    rows = ['| %s | %d | `%s` | - | - |' % (f, len(b), hashlib.md5(b).hexdigest()) for f, b in files]
    rows.append('| HANDOFF.md | %d | `%s` | - | - |' % (len(pb), hashlib.md5(pb).hexdigest()))
    man = 'Source: PLACE-papers @ `%s` (main).\n%s\n\n%s\n' % (build[:7], RO.second_line(head), NL.join(rows))
    MB = base_manifest()
    with tempfile.TemporaryDirectory(prefix='v1353_') as d:
        zg = planted_zip(d, 'good.zip', man, files, pb)
        zb = planted_zip(d, 'bad.zip', man, files, b'x')
        zn = planted_zip(d, 'nodecl.zip', man.replace(RO.second_line(head) + NL, ''), files, pb)
        good, bad, nodecl = MF.control_at_build(zg, build), MF.control_at_build(zb, build), MF.control_at_build(zn, build)
        old_bad = MB.control_at_build(zb, build)
    pr = lambda c: [r[4] for r in c['rows'] if r[0] == 'HANDOFF.md'] or 'NONE'   # noqa: E731
    roster_ok = sum(1 for r in good['rows'] if r[0] != 'HANDOFF.md' and r[4] == 'AS WANTED')
    n += 1
    g += case(L, 'manifest', 'planted exports of the roster at PLACE-papers HEAD %s (%d files, flat-named as the builder names them) with the page; the page equal, '
              'altered, or carried with no line declared' % (build[:8], len(files)),
              'BASE`s control over the export with the page altered: ok %s, the page`s row %s' % (old_bad['ok'], pr(old_bad)),
              'the roster`s rows AS WANTED %d of %d ; the page equal: row %s, ok %s ; altered: row %s, ok %s ; not declared: the page`s row %s, ok %s' % (
                  roster_ok, len(files), pr(good), good['ok'], pr(bad), bad['ok'], pr(nodecl), nodecl['ok']),
              old_bad['ok'] is True and pr(old_bad) == 'NONE',
              roster_ok == len(files) and pr(good) == ['AS WANTED'] and good['ok'] is True and pr(bad) == ['NOT AS WANTED'] and bad['ok'] is False
              and pr(nodecl) == 'NONE' and nodecl['ok'] is True)
    return L, g, n


# ================================================================================ (project)
def control_project():
    L, g, n = ['### (project): THE PROJECT SET CARRIES THE PAGE FROM b756'], 0, 0
    pb = page()
    r6, b6, _bd, _c, _f, _m = RO.project('main', 'b756', with_cuts=False)
    r5, b5, _bd, _c, _f, _m = RO.project('main', 'b755', with_cuts=False)
    row6 = [r for r in r6 if r[0] == 'HANDOFF.md']
    n += 1
    g += case(L, 'project', 'roster.py project at main, for b756 and for b755 (the cuts apart)', 'the set carries the page: %s' % ('second_rows()' in (V.show(BASE, 'tools/standing/roster.py') or '')),
              'b756 row %s ; b755 rows with the page %d ; the totals %d and %d, their difference %d against the blob`s %d' % (
                  row6[0][:2] if row6 else None, len([r for r in r5 if r[0] == 'HANDOFF.md']), b6, b5, b6 - b5, len(pb)),
              'second_rows()' not in (V.show(BASE, 'tools/standing/roster.py') or ''),
              bool(row6) and row6[0][1] == len(pb) and not [r for r in r5 if r[0] == 'HANDOFF.md'] and b6 - b5 == len(pb))
    return L, g, n


# ================================================================================ (amend)
def control_amend():
    L, g, n = ['### (amend): THE ITEM ROUTE`S ROW NAMES THE CLAUSE ORDERING THE ITEM'], 0, 0
    r6 = AM.pass_row('R366', '[H1]', 'w', 'c', ['relay/x'], 't', '6')['clause']
    r5 = AM.pass_row('R366', '[X]', 'w', 'c', ['relay/x'], 't')['clause']
    j = json.load(io.open(os.path.join(D, 'b756_amendments.json'), encoding='utf-8'))
    row1 = (j.get('rows') or [{}])[0]
    n += 1
    g += case(L, 'amend', 'pass_row and the banked row 1 of data/b756_amendments.json', 'the clause fixed at (5): %s' % ("'(%s)(5)%s passed" in (V.show(BASE, 'tools/standing/amend.py') or '')),
              'under 6: %r ; by default: %r ; row 1: %r widening %s' % (r6[:28], r5[:27], (row1.get('clause') or '')[:28], row1.get('widens')),
              "'(%s)(5)%s passed" in (V.show(BASE, 'tools/standing/amend.py') or ''),
              r6.startswith('(R366)(6)[H1] passed') and r5.startswith('(R366)(5)[X] passed') and (row1.get('clause') or '').startswith('(R366)(6)[H1] passed')
              and row1.get('widens') == ['relay/tools/mirror_build.ps1', 'relay/tools/mirror_verify.py'])
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.35.2', ver == 'v1.35.3')
    return L, g, n


CONTROLS = dict(second=control_second, builder=control_builder, verify=control_verify, manifest=control_manifest, project=control_project,
                amend=control_amend, version=control_version)
ORDER = ('second', 'builder', 'verify', 'manifest', 'project', 'amend', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.35.3, (R366)(6): [H1]`S HELD PART, THE HANDOFF PAGE IN THE ARCHIVE (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'written through tools/standing/figbank.py; no ledger line printed; no build run and no zip written beside the mirror', '',
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
    out.append('### ### **v1.35.3: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1353.txt' % act), NL.join(out))
        print('written data/%s_standing_v1353.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
