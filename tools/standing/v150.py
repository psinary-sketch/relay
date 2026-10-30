# -*- coding: utf-8 -*-
"""standing/v150.py -- THE ROUTES AND CONTROLS OF v1.5.0 ((R335)(2)(ii), (iii) and (v)), in v140.py's form: each instance replayed through
the route as it stood at HEAD before the repair (the blob read from git, or the literal the template carried) and through the repaired
route; AS WANTED where the old route fails the instance and the new passes it. Written at b725 by the Write tool.

  python -X utf8 tools/standing/v150.py copy
        (R335)(2)(iii): writes tools/standing/routes/b644_record.py -- tools/b644_record.py byte for byte beneath a header, except its line
        :1088, where the author's name (read in memory from the monograph's byline, as the address scan reads it; never printed) is
        replaced by the account login (read from `gh api user` at run time). Refuses unless the line carries the name exactly once and no
        other line carries the name, the previous user.name or the previous address.
  python -X utf8 tools/standing/v150.py control [short|needle|legacy|cites ...] [--bank]
        runs the named controls (all where none is named); --bank writes data/<act>_standing_v150.txt with every control run and the
        exception file's remainder with its price, nothing else.
"""
import hashlib
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
for p_ in (S, T):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import allow as AL              # noqa: E402

BASE = 'HEAD'   # ### the routes before the repair: v1.5.0's files are uncommitted when the controls run, so HEAD carries v1.4.0's
TMP = tempfile.mkdtemp(prefix='v150_')
SRC = os.path.join(T, 'b644_record.py')
COPY = os.path.join(S, 'routes', 'b644_record.py')
LINE = 1088
HEADER = (
    '# -*- coding: utf-8 -*-',
    '# ### standing/routes/b644_record.py -- (R335)(2)(iii), tools/standing/ v1.5.0, b725: tools/b644_record.py copied under its standing',
    '# ### name, byte for byte beneath this header, EXCEPT ITS SOURCE LINE :%d (this file`s :%d): the author`s name in that line`s needle is' % (LINE, LINE + 7),
    '# ### REPLACED BY THE ACCOUNT LOGIN, so the copy writes no occurrence (R332)(9)(i) bars. The needle is patch_plan`s author-line reader',
    '# ### (b644`s route, run at b644): read through this copy it finds a companion`s author line only where that line starts with the login.',
    '# ### Served by tools/standing/fold.py`s RouteLoader with __file__ at tools/b644_record.py; legacy.py names b644_record no more.',
    '# ### Source: tools/b644_record.py blob %s; the control: tools/standing/v150.py control legacy.',
)


def _git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob(rel, rev=None, repo=RELAY):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev or BASE, rel)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def old_module(rel, name):
    """the module at BASE, loaded from a temporary copy under its own name (the live module untouched)"""
    p = os.path.join(TMP, name + '.py')
    with open(p, 'wb') as f:
        f.write(blob(rel))
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.4.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.5.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def targets():
    """the three identifiers, held in memory only: the byline's name, the previous user.name, the previous address."""
    import b725_address_scan as SC
    return (('name', SC.author_name()), ('username', SC.previous_username()), ('address', SC.previous_address())), SC.count


def login():
    r = subprocess.run(['gh', 'api', 'user', '--jq', '.login'], capture_output=True, text=True, encoding='utf-8', errors='replace')
    s = r.stdout.strip()
    if r.returncode != 0 or not re.fullmatch(r'[A-Za-z0-9-]{2,39}', s):
        sys.exit('### THE ACCOUNT LOGIN NOT READ -- NOTHING WRITTEN')
    return s


# ================================================================================ copy
def copy():
    raw = open(SRC, 'rb').read()
    lines = raw.split(b'\n')
    tg, count = targets()
    name = tg[0][1]
    hits = [(i + 1, k) for i, ln in enumerate(lines) for k, v in tg if count(ln.decode('utf-8'), v)]
    ln = lines[LINE - 1].decode('utf-8')
    if sorted(set(i for i, _k in hits)) != [LINE] or ln.count(name) != 1:
        sys.exit('### THE SOURCE IS NOT AS READ AT b724 (the identifiers on :%d alone, the name once, exact case) -- NOTHING WRITTEN' % LINE)
    lg = login()
    eol = b'\r\n' if raw.count(b'\r\n') * 2 > raw.count(b'\n') else b'\n'
    sha = _git(RELAY, 'rev-parse', 'HEAD:tools/b644_record.py').strip()
    head = [(h % sha if '%s' in h else h).encode('utf-8') + (b'\r' if eol == b'\r\n' else b'') for h in HEADER]
    new = list(lines)
    new[LINE - 1] = ln.replace(name, lg, 1).encode('utf-8')
    out = b'\n'.join(head + new)
    os.makedirs(os.path.dirname(COPY), exist_ok=True)
    with open(COPY + '.tmp', 'wb') as f:
        f.write(out)
    os.replace(COPY + '.tmp', COPY)
    print('written tools/standing/routes/b644_record.py ; %d bytes ; sha256 %s ; header %d lines ; source line :%d is the copy`s :%d ; '
          'line endings %s ; the source blob %s' % (len(out), hashlib.sha256(out).hexdigest()[:16], len(head), LINE, LINE + len(head),
                                                     'CR LF' if eol == b'\r\n' else 'LF', sha[:12]))


# ================================================================================ (short) A SHORT NAME READ AFTER ITS FULL ONE
def control_short():
    """b725's step-zero deletes (data/b725_stepzero.txt, tools/b725_worklist.py DELETE): the ruling names them as "push-b724-preroot,
    -record and -closing"; v1.4.0 read the first name alone (b724 wrote its own regex to expand them). Both rulings read: b724's and b725's."""
    L = ['### (short) THE SHORT NAMES -- tools/standing/allow.py deletes_read; instances: each act`s DELETE (its worklist) against its own ferry']
    AL0 = old_module('tools/standing/allow.py', 'allow_v140')
    g = n = 0
    for act, prev in (('b724', 'b723'), ('b725', 'b724')):
        dels = [('D:/relay', 'push-%s-%s' % (prev, w)) for w in ('closing', 'preroot', 'record')] + \
               [('D:/MY-DOwnloads/PLACE-papers', 'push-%s-%s' % (prev, w)) for w in ('preroot', 'record')]
        fe = A.rd('%s_ferry.txt' % act)
        r0, r1 = AL0.deletes_read(dels, fe), AL.deletes_read(dels, fe)
        n += 1
        g += case(L, 'short', '%s`s five deletes against data/%s_ferry.txt' % (act, act),
                  'outside %d of 5 (%s) ; names read %s' % (len(r0['outside']), ', '.join(b for _r, b in r0['outside']) or 'none', ', '.join(r0['allowed'])),
                  'outside %d of 5 ; names read %s' % (len(r1['outside']), ', '.join(r1['allowed'])), not r0['ok'], r1['ok'])
    return L, g, n


# ================================================================================ (needle) THE PLANT'S NEEDLE FROM THE ACT'S OWN FERRY
def control_needle():
    """b724 event (9): G-DELETES-ONE-BRANCH's plant replaced a hand-kept sentence its ferry did not carry, so the plant changed nothing
    and the seal refused. The old plant (the template's literal at HEAD, :1621) and the new (allow.plant_kept) on the b723, b724 and b725
    ferries; and a ferry with no such clause (b725's with its delete clause cut out) read None by the new."""
    L = ['### (needle) THE PLANT`S NEEDLE -- checks.tpl :1621, G-DELETES-ONE-BRANCH; instances: the b723, b724 and b725 ferries, and one with no clause']
    tpl = blob('tools/standing/fold/checks.tpl').decode('utf-8')
    m = re.search(r"S\['ferry'\]\.replace\('([^']*)', '([^']*)'\)", tpl)
    L.append('  the old plant read at %s: %s' % (BASE, 'FOUND' if m else '### NOT FOUND'))
    g = n = 0
    for act, prev in (('b723', 'b722'), ('b724', 'b723'), ('b725', 'b724')):
        must = sorted('push-%s-%s' % (prev, w) for w in ('closing', 'preroot', 'record'))
        fe = A.rd('%s_ferry.txt' % act)
        old_needle = m.group(1).replace('⟪PREV⟫', prev) if m else '\x00'
        old_changed = old_needle in fe
        planted = AL.plant_kept(fe, must)
        before = AL.deletes_read([('D:/relay', b) for b in must], fe)['ok']
        after = AL.deletes_read([('D:/relay', b) for b in must], planted)['ok'] if planted else None
        c = AL.delete_clause(fe, must)
        n += 1
        g += case(L, 'needle', '%s`s ferry, the branches %s' % (act, ', '.join(must)), 'the plant changes the ferry %s' % old_changed,
                  'clause found %s (%d chars) ; the deletes allowed before the plant %s, after it %s' % (bool(c), len(c), before, after),
                  not old_changed, bool(c) and before and after is False)
    fe = re.sub(r'\s+', ' ', A.rd('b725_ferry.txt'))
    c = AL.delete_clause(fe, sorted('push-b724-%s' % w for w in ('closing', 'preroot', 'record')))
    cut = fe.replace(c, '') if c else fe
    p = AL.plant_kept(cut, sorted('push-b724-%s' % w for w in ('closing', 'preroot', 'record')))
    n += 1
    ok = bool(c) and p is None
    L += ['  (needle) a ferry with no such clause: b725`s with its delete clause (%d chars) cut out' % len(c),
          '      AFTER  (v1.5.0): plant_kept -> %s -> %s' % ('None' if p is None else 'a ferry', 'PASSES (the plant reads nothing to plant)' if p is None else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    g += ok
    return L, g, n


# ================================================================================ (legacy) THE LEGACY COPY
def control_legacy():
    """(R335)(2)(iii): the copy equal to its source except at :1088; no identifier in the copy; at :1088 the login in the name's place;
    served by fold.py's finder (its __file__ the original's, __route__ the copy); legacy.py at HEAD names b644_record, now not."""
    L = ['### (legacy) THE LEGACY COPY -- tools/standing/routes/b644_record.py against tools/b644_record.py; fold.py`s RouteLoader; legacy.py']
    g = n = 0
    if not os.path.isfile(COPY):
        return L + ['  ### THE COPY IS NOT WRITTEN -- NOT AS WANTED'], 0, 1
    src = open(SRC, 'rb').read().split(b'\n')
    cp = open(COPY, 'rb').read().split(b'\n')
    h = len(HEADER)
    body = cp[h:]
    diff = [i + 1 for i in range(max(len(src), len(body))) if (src[i] if i < len(src) else None) != (body[i] if i < len(body) else None)]
    tg, count = targets()
    lg = login()
    in_copy = dict((k, count(b'\n'.join(cp).decode('utf-8'), v)) for k, v in tg)
    at = body[LINE - 1].decode('utf-8') if len(body) >= LINE else ''
    at_ok = count(at, lg) == 1 and all(count(at, v) == 0 for _k, v in tg)
    same_shape = at.replace(lg, '') == src[LINE - 1].decode('utf-8').replace(tg[0][1], '')
    n += 1
    g += case(L, 'legacy', 'the copy against its source, line by line beneath its %d-line header' % h,
              'no copy at %s (the route served from tools/b644_record.py, the name in code)' % BASE,
              'lines %d against %d ; differing lines %s ; at :%d the login once and no identifier %s, the rest of the line equal %s ; in the whole copy '
              'name %d, username %d, address %d' % (len(body), len(src), diff, LINE, at_ok, same_shape, in_copy['name'], in_copy['username'], in_copy['address']),
              blob('tools/standing/routes/b644_record.py') is None,
              diff == [LINE] and len(body) == len(src) and at_ok and same_shape and not any(in_copy.values()))
    L0 = old_module('tools/standing/legacy.py', 'legacy_v140')
    import legacy as L1
    import fold as F
    F.install()
    sys.modules.pop('b644_record', None)
    try:
        mod = importlib.import_module('b644_record')
        served = (getattr(mod, '__route__', None) == COPY, os.path.normcase(mod.__file__) == os.path.normcase(SRC), callable(getattr(mod, 'patch_plan', None)))
        err = ''
    except Exception as e:  # noqa: BLE001
        served, err = (False, False, False), '%s: %s' % (type(e).__name__, e)
    n += 1
    g += case(L, 'legacy', 'import b644_record through fold.py`s finder',
              'legacy.py names b644_record %s (%d names)' % ('b644_record' in L0.NAMES, len(L0.NAMES)),
              'legacy.py names it %s (%d names) ; served from the copy %s, __file__ the original`s %s, patch_plan defined %s%s' % (
                  'b644_record' in L1.NAMES, len(L1.NAMES), served[0], served[1], served[2], (' ; RAISED ' + err) if err else ''),
              'b644_record' in L0.NAMES, 'b644_record' not in L1.NAMES and all(served))
    L += ['  THE EXCEPTION FILE`S REMAINDER (tools/standing/legacy.py NAMES, %d; not emptied): %s' % (len(L1.NAMES), ' '.join(L1.NAMES)),
          '  ITS PRICE: about 1.5-2 h (data/b724_legacy.txt :33, the flatten of the predecessors that carry no identifier: each copied under its',
          '  standing name into tools/standing/routes/ and served by the RouteLoader, its control the copy`s equality); carried, not run at b725.']
    return L, g, n


# ================================================================================ (cites) THE MIRROR BANK'S CITATIONS
def control_cites():
    """b724 event (18): data/b724_mirror.txt cites (R334)(5) for the roster and (R334)(2)(iii) for the MANIFEST control. The bank read by
    cites.check against the table: the two caught, (W)'s citation read from b724's ferry and not flagged where it stands."""
    import cites as CI
    L = ['### (cites) THE MIRROR BANK`S CITATIONS -- tools/standing/cites.py; instance data/b724_mirror.txt (event (18))']
    t = A.rd('b724_mirror.txt')
    got = CI.check(t, 'b724')
    tpl = blob('tools/standing/fold/record.tpl').decode('utf-8')
    old_tok = tpl.count("MAIN AT THE BUILD ((⟪RUL⟫)(5)") + tpl.count("'### (⟪RUL⟫)(2)(iii)`S MANIFEST CONTROL")
    new_tpl = open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    new_tok = new_tpl.count("MAIN AT THE BUILD ((⟪RUL⟫)(5)") + new_tpl.count("'### (⟪RUL⟫)(2)(iii)`S MANIFEST CONTROL")
    keys = sorted(k for k, _c, _w in got)
    L += ['  caught: %s' % ('; '.join('%s cited %s, the table %s' % r for r in got) or 'none'),
          '  the table: roster %s, manifest %s ; (W) read from the b724 ferry %s, from the b725 ferry %s' % (
              CI.cite('mirror.roster'), CI.cite('mirror.manifest'), CI.cite('mirror.prevbuild', 'b724'), CI.cite('mirror.prevbuild', 'b725'))]
    # ### the predicate, b725 14:08:48Z: its first run wanted the caught keys EXACTLY the two event (18) names, and read NOT AS WANTED on
    # ### three -- the third, (W)'s "(R334)(10)", hand-read against data/b724_ferry.txt: the clause naming tools/mirror_prevbuild.json is
    # ### item (8) at :23, so (10) was wrong too and event (18) named two of the bank's three. The order's control is "the b724 bank's two
    # ### wrong citations caught": the two among those caught; every other catch printed as a finding with its ferry reading.
    third = [r for r in got if r[0] not in ('mirror.manifest', 'mirror.roster')]
    L += ['  FIRST RUN (14:08:48Z): the predicate wanted exactly the two, caught three -> NOT AS WANTED; the predicate now the two among those caught',
          '  A FINDING BEYOND EVENT (18): %s' % ('; '.join('%s cited %s in data/b724_mirror.txt, the ferry`s own item %s (data/b724_ferry.txt, '
                                                         'its top-level head before the clause carrying mirror_prevbuild)' % (k, c, w) for k, c, w in third) or 'none')]
    ok = case(L, 'cites', 'record.tpl`s mbank citations; the b724 bank checked',
              'the two citations rendered from the ruling token, %d template sites' % old_tok,
              'ruling-token sites %d ; the bank`s wrong citations caught %d (%s)' % (new_tok, len(got), ', '.join(keys)),
              old_tok == 2, new_tok == 0 and 'mirror.manifest' in keys and 'mirror.roster' in keys)
    return L, int(ok), 1


CONTROLS = dict(short=control_short, needle=control_needle, legacy=control_legacy, cites=control_cites)
ORDER = ('short', 'needle', 'legacy', 'cites')


def main(argv):
    if argv and argv[0] == 'copy':
        return copy()
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.5.0, (R335)(2)(ii), (iii) AND (v): THE SHORT NAMES, THE PLANT`S NEEDLE, THE LEGACY COPY, '
           'THE MIRROR CITATIONS (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
           '### the routes before the repair read at %s (%s); each case its instance through both' % (BASE, _git(RELAY, 'rev-parse', '--short=8', BASE).strip()), '']
    tg = tn = 0
    try:
        for k in names:
            try:
                L, g, n = CONTROLS[k]()
            except Exception as e:  # noqa: BLE001
                L, g, n = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
            out += L + ['']
            tg, tn = tg + g, tn + n
    finally:
        shutil.rmtree(TMP, ignore_errors=True)
    out.append('### ### **v1.5.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (
        ', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v150.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v150.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
