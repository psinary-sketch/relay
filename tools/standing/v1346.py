# -*- coding: utf-8 -*-
"""standing/v1346.py -- THE CONTROLS OF v1.34.6 ((R365)(2)(iii), THE MIRROR'S FOLDER BY ROLE, with b755's amendment row 1, the one-call
tool's act phases 'component 5' and 'component 6' inside the same change; the amendment row 2 reading N5's folder clause), in v1345.py's form:
each instance read through the route as it stood at BASE (relay 0b477b49, v1.34.5's own commit, read from its blobs) and through the route on
disk; AS WANTED where the old route fails the instance and the new passes it. THE COMPILE CONTROL RUNS FIRST. The free memory is printed
before each control. No write reaches the relay or PLACE-papers: the mirror cases run mbank's source from each template over a planted export
in a temporary folder, its two writes captured in memory, the folder removed after; no planted path is printed, only whether a line holds it.
Written at b755 by the Write tool; no identifier of the author is read into any string here.

  (phases)   the one-call tool's act phases (tools/standing/commit.py ACT_PHASES, act_check): 'component 5' and 'component 6' refused at BASE
             and taken on disk; 'component 7' refused on disk; every phase of BASE kept in its order; every phase data/act_current.json's
             components name taken (gate, lock and seal the tool's own subject routes).
  (mirror)   tools/standing/fold/record.tpl: mbank's bank line and json name the export by its file name and its folder by role
             (MIRROR_FOLDER_ROLE), the reads above the binding taking the full path; the span line names the last export by its file name;
             the closing's mirror line (tools/standing/fold/closing.tpl, unchanged) over each bank; the act's record render compiles.
  (version)  tools/standing/VERSION moved to v1.34.6.

  python -X utf8 -u tools/standing/v1346.py control [phases|mirror|version ...] [--bank]
"""
import contextlib
import io
import os
import re
import shutil
import sys
import tempfile
import time
import types
import zipfile

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '0b477b49'   # ### v1.34.5's own commit (b754 component 3, [M2]): the routes before this change
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import fold as F                # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line, _fn_src)


def show(rel):
    return V.show(BASE, rel)


def disk(rel):
    return io.open(os.path.join(RELAY, *rel.split('/')), encoding='utf-8').read().replace('\r', '')


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.5): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.34.6): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def both(L, cls, what, at_base, on_disk, holds_base, holds_disk):
    """a case wanted the same at both routes (the plain reading)."""
    ok = bool(holds_base) and bool(holds_disk)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.5): %s -> (the same at both is wanted)' % at_base,
          '      AFTER  (v1.34.6): %s -> %s' % (on_disk, 'PASSES' if ok else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    """a case of the new route alone (a planted instance the old route has no reading of)."""
    L += ['  (%s) %s' % (cls, what), '      AFTER  (v1.34.6): %s -> %s' % (new, 'AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def tokens(text, act):
    for k, v in F.names(act).items():
        text = text.replace(k, v)
    return text


# ================================================================================ (phases)
class Refused(Exception):
    pass


def _phases_route(src):
    """(ACT_PHASES, act_check) executed from a commit.py text: the tuple's line and the function's source alone, Refused planted."""
    m = re.search(r'^ACT_PHASES = .*$', src, re.M)
    ns = dict(Refused=Refused)
    exec(compile(m.group(0) + NL + V._fn_src(src, 'act_check'), 'commit.py act_check', 'exec'), ns)   # noqa: S102
    return ns['ACT_PHASES'], ns['act_check']


def _takes(chk, act, phase):
    try:
        return chk(act, phase, 'the words') == '%s %s: the words' % (act, phase)
    except Refused:
        return False


def control_phases():
    L, g, n = ['### (phases): THE ONE-CALL TOOL`S ACT PHASES (b755`s amendment row 1, inside (R365)(2)(iii)`s change; data/b755_defects.txt (c))'], 0, 0
    act = A.current()['act']
    po, co = _phases_route(show('tools/standing/commit.py') or '')
    pn, cn = _phases_route(disk('tools/standing/commit.py'))
    for ph in ('component 5', 'component 6'):
        n += 1
        g += case(L, 'phases', 'an act commit of %s under the phase %r: taken, its subject "%s %s: the words"' % (act, ph, act, ph),
                  'BASE`s act_check: taken %s' % _takes(co, act, ph), 'act_check on disk: taken %s' % _takes(cn, act, ph),
                  not _takes(co, act, ph), _takes(cn, act, ph))
    n += 1
    g += guard(L, 'phases', 'a phase no component names (\'component 7\'): refused on disk, as every phase outside the list',
               'act_check on disk: taken %s' % _takes(cn, act, 'component 7'), not _takes(cn, act, 'component 7'))
    sub = [p for p in pn if p in po]
    n += 1
    g += both(L, 'phases', 'every phase of BASE`s list kept in its order (v1281`s reading: pre-root before root before record)',
              'BASE %d phases' % len(po), 'on disk %d phases ; BASE`s in order %s ; pre-root < root < record %s' % (
                  len(pn), sub == list(po), pn.index('pre-root') < pn.index('root') < pn.index('record')),
              True, sub == list(po) and pn.index('pre-root') < pn.index('root') < pn.index('record'))
    named = [ph for c in (A.current().get('components') or []) for ph in c.get('phases') or [] if ph not in ('gate', 'lock', 'seal')]
    n += 1
    g += case(L, 'phases', 'every phase data/act_current.json`s components name (%d, gate, lock and seal apart: the tool`s subject routes) taken' % len(named),
              'BASE`s act_check refuses %s' % ([ph for ph in named if not _takes(co, act, ph)] or 'none'),
              'act_check on disk refuses %s' % ([ph for ph in named if not _takes(cn, act, ph)] or 'none'),
              any(not _takes(co, act, ph) for ph in named), all(_takes(cn, act, ph) for ph in named))
    return L, g, n


# ================================================================================ (mirror)
PLANT_DIR = 'planted-shelf-q'
PLANT_ZIP = 'mirror-refresh-2099-01-01-b999.zip'
PLANT_PREV = 'mirror-refresh-2098-12-31-b998.zip'


def _plant():
    """a temporary folder holding a planted export: MANIFEST with a root line, a roster line and a row carrying a commit, one file."""
    td = tempfile.mkdtemp(prefix='v1346_')
    shelf = os.path.join(td, PLANT_DIR)
    os.makedirs(shelf)
    zp = os.path.join(shelf, PLANT_ZIP)
    with zipfile.ZipFile(zp, 'w') as z:
        z.writestr('MANIFEST.md', 'Act root: b999 %s\nROSTER planted 1\n| a.md | abc1234 | 1 |\n' % ('0' * 64))
        z.writestr('a.md', 'planted\n')
    return td, shelf, zp


def _holds(text, shelf):
    """whether a text names the planted folder: its path by either separator, or the folder's own name."""
    return any(x in text for x in (shelf, shelf.replace('\\', '/'), shelf.replace('/', '\\'), PLANT_DIR))


def _span_fn(tpl_text, act, last_export):
    """the span line route a template binds: the template's own `def span_line` where it carries one (v1.34.6), else b703's, as :198 binds it."""
    if re.search(r'^def span_line\(', tpl_text, re.M):
        src = tokens(V._fn_src(tpl_text, 'span_line'), act)
    else:
        src = V._fn_src(disk('tools/b703_record.py'), 'span_line')
    ns = dict(os=os, _last_export=last_export)
    exec(compile(src, 'span_line', 'exec'), ns)   # noqa: S102
    return ns['span_line']


def _run_mbank(tpl_text, act, zp, shelf):
    """mbank's source from a template, run over the planted export with its collaborators planted; (bank lines, json, the path the build
    control was handed, the stdout length). The two writes captured in memory; sys.modules restored after."""
    src = tokens(V._fn_src(tpl_text, 'mbank'), act)
    role = re.search(r"^MIRROR_FOLDER_ROLE = (.+)$", tpl_text, re.M)
    got = {}
    seen = {}

    def control_at_build(path, build):
        seen['path'] = path
        return dict(rows=[], ok=True)
    stubs = dict(manifest=types.SimpleNamespace(control_at_build=control_at_build),
                 b616_record=types.SimpleNamespace(nd_hits=lambda s, sets: [{}], nd_sets=lambda: None))
    prev = os.path.join(shelf, PLANT_PREV)
    ns = dict(os=os, re=re, sys=sys, NL=NL, ACT=act, T=T, PP='pp', R=types.SimpleNamespace(ZIP=zp),
              _close_step=lambda k: None, mirror_order=lambda a_, r_: '', rdn=lambda nm: 'VERDICT: CLEAN ON ALL THREE CLAUSES',
              g=lambda *a_: 'abc1234', utc=lambda: '2099-01-01T00:00:00Z',
              put_txt=lambda nm, L_: got.__setitem__('txt', list(L_)), put_json=lambda nm, j_: got.__setitem__('json', dict(j_)),
              span_line=_span_fn(tpl_text, act, lambda a_: ('b998', prev)))
    if role:
        ns['MIRROR_FOLDER_ROLE'] = eval(role.group(1))   # noqa: S307  ### the template's own string literal
    saved = dict((k, sys.modules.get(k)) for k in stubs)
    sys.modules.update(stubs)
    out = io.StringIO()
    try:
        exec(compile(src, 'mbank', 'exec'), ns)   # noqa: S102
        with contextlib.redirect_stdout(out):
            ns['mbank']()
    finally:
        for k, v in saved.items():
            if v is None:
                sys.modules.pop(k, None)
            else:
                sys.modules[k] = v
    return got.get('txt') or [], got.get('json') or {}, seen.get('path'), ns.get('MIRROR_FOLDER_ROLE')


def _closing_line(j, act):
    """closing.tpl's mirror_line (unchanged by v1.34.6) over a mirror json, its collaborators planted."""
    src = tokens(V._fn_src(disk('tools/standing/fold/closing.tpl'), 'mirror_line'), act)
    ns = dict(jl=lambda nm: j, WL=types.SimpleNamespace(DATE='2099-01-01'), state_file_sentence=lambda: 'the planted state file sentence')
    exec(compile(src, 'mirror_line', 'exec'), ns)   # noqa: S102
    return ns['mirror_line']()


def control_mirror():
    L, g, n = ['### (mirror): (R365)(2)(iii), THE MIRROR`S FOLDER BY ROLE (the amendment row 2: the closing and the mirror bank)'], 0, 0
    act = A.current()['act']
    to, tn = show('tools/standing/fold/record.tpl') or '', disk('tools/standing/fold/record.tpl')
    td, shelf, zp = _plant()
    try:
        Lo, jo, po, _ro = _run_mbank(to, act, zp, shelf)
        Ln, jn, pn, rn = _run_mbank(tn, act, zp, shelf)
        zo = [l for l in Lo if l.startswith('### THE ZIP : ')]
        zn = [l for l in Ln if l.startswith('### THE ZIP : ')]
        n += 1
        g += case(L, 'mirror', 'the mirror bank`s ZIP line over a planted export in a planted folder: the file`s name, its bytes and hashes, and no folder',
                  'BASE`s mbank: the line names the folder %s' % _holds(NL.join(zo), shelf),
                  'mbank on disk: names the folder %s ; the file by name %s ; bytes and sha256 %s ; the role %s' % (
                      _holds(NL.join(zn), shelf), bool(zn) and zn[0].startswith('### THE ZIP : %s, in ' % PLANT_ZIP),
                      bool(zn) and ' bytes ; md5 ' in zn[0] and ' ; sha256 ' in zn[0], bool(zn) and bool(rn) and rn in zn[0]),
                  _holds(NL.join(zo), shelf),
                  bool(zn) and not _holds(NL.join(zn), shelf) and zn[0].startswith('### THE ZIP : %s, in ' % PLANT_ZIP) and bool(rn) and rn in zn[0])
        n += 1
        g += case(L, 'mirror', 'the mirror bank whole (every line) and its json (every value): no line or value names the folder',
                  'BASE`s mbank: lines naming it %d ; json values naming it %s' % (
                      sum(1 for l in Lo if _holds(l, shelf)), sorted(k for k, v in jo.items() if _holds(str(v), shelf))),
                  'mbank on disk: lines naming it %d ; json values naming it %s' % (
                      sum(1 for l in Ln if _holds(l, shelf)), sorted(k for k, v in jn.items() if _holds(str(v), shelf)) or 'none'),
                  any(_holds(l, shelf) for l in Lo), bool(Ln) and not any(_holds(l, shelf) for l in Ln) and not any(_holds(str(v), shelf) for v in jn.values()))
        n += 1
        g += case(L, 'mirror', 'the json`s zip the file`s name alone, and its folder by role',
                  'BASE`s json: zip the name alone %s ; folder %s' % (jo.get('zip') == PLANT_ZIP, 'folder' in jo),
                  'json on disk: zip the name alone %s ; folder the role %s' % (jn.get('zip') == PLANT_ZIP, bool(rn) and jn.get('folder') == rn),
                  jo.get('zip') != PLANT_ZIP and 'folder' not in jo, jn.get('zip') == PLANT_ZIP and bool(rn) and jn.get('folder') == rn)
        n += 1
        g += both(L, 'mirror', 'the reads above the binding take the export`s path: the build`s MANIFEST control handed the planted path',
                  'BASE: handed it %s' % (po == zp), 'on disk: handed it %s' % (pn == zp), po == zp, pn == zp)
        so = [l for l in Lo if l.startswith('### THE SPAN: ')]
        sn = [l for l in Ln if l.startswith('### THE SPAN: ')]
        n += 1
        g += case(L, 'mirror', 'the span line, the last export planted in the same folder: its file by name, no folder',
                  'BASE (b703`s span_line, bound at :198): names the folder %s' % _holds(NL.join(so), shelf),
                  'on disk (the template`s span_line): names the folder %s ; the file by name %s ; equal to the json`s span %s' % (
                      _holds(NL.join(sn), shelf), bool(sn) and ('b998`s, %s)' % PLANT_PREV) in sn[0], bool(sn) and jn.get('span') == sn[0]),
                  _holds(NL.join(so), shelf), bool(sn) and not _holds(NL.join(sn), shelf) and ('b998`s, %s)' % PLANT_PREV) in sn[0] and jn.get('span') == sn[0])
        sp0 = _span_fn(tn, act, lambda a_: (None, None))(act)
        n += 1
        g += guard(L, 'mirror', 'the span line with no earlier mirror bank: both parts NONE, as b703`s',
                   sp0, sp0 == '### THE SPAN: every roster and ledger change of %s (the last export ### NONE`s, ### NONE)' % act)
        co, cn = _closing_line(jo, act), _closing_line(jn, act)
        n += 1
        g += case(L, 'mirror', 'the closing`s mirror line (closing.tpl, unchanged) over each bank: the file`s name, its bytes and hash, no folder',
                  'over BASE`s json: names the folder %s' % _holds(co, shelf),
                  'over the json on disk: names the folder %s ; opens with the file`s name %s ; bytes %s' % (
                      _holds(cn, shelf), cn.startswith(PLANT_ZIP + ' ; '), ' bytes ; sha256 ' in cn),
                  _holds(co, shelf), not _holds(cn, shelf) and cn.startswith(PLANT_ZIP + ' ; ') and ' bytes ; sha256 ' in cn)
    finally:
        shutil.rmtree(td, ignore_errors=True)
    n += 1
    g += guard(L, 'mirror', 'the planted folder removed after the cases', 'removed %s' % (not os.path.exists(td)), not os.path.exists(td))
    try:
        text = F.render(act, 'record')
        compile(text, '%s_record.py' % act, 'exec')
        r_ok, r_why = True, 'compiles, %d lines ; MIRROR_FOLDER_ROLE bound %d ; def span_line %d' % (
            text.count(NL), len(re.findall(r'^MIRROR_FOLDER_ROLE = ', text, re.M)), len(re.findall(r'^def span_line\(', text, re.M)))
        r_ok = r_ok and len(re.findall(r'^MIRROR_FOLDER_ROLE = ', text, re.M)) == 1 and len(re.findall(r'^def span_line\(', text, re.M)) == 1
    except (SyntaxError, F.FoldRefused) as e:
        r_ok, r_why = False, '%s: %s' % (type(e).__name__, str(e)[:120])
    n += 1
    g += guard(L, 'mirror', '%s`s record render through the template on disk' % act, r_why, r_ok)
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (show('tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.34.5', ver == 'v1.34.6')
    return L, g, n


CONTROLS = dict(phases=control_phases, mirror=control_mirror, version=control_version)
ORDER = ('phases', 'mirror', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.34.6, (R365)(2)(iii) THE MIRROR`S FOLDER BY ROLE, WITH THE AMENDMENT ROW 1`S TWO PHASES (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each change`s instances through both routes; the free memory read before each; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case through both routes, the route before read from %s' % BASE, '']
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
    out.append('### ### **v1.34.6: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1346.txt' % act), NL.join(out))
        print('written data/%s_standing_v1346.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
