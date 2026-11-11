# -*- coding: utf-8 -*-
"""b753_kernels.py -- (R363)(5)(i): THE KERNELS RECONCILED, data/b753_kernels.txt.

One row for every repository of data/repo_visibility.txt and every SIDE-* directory on D:, each remote read once by one `git ls-remote
--heads --tags` (one remote read per row; a read that fails prints FAILED with its exit code and error text and is not read again by this
run -- the seat's one retry, by the `retry` route, is an event). Per row: its visibility; whether it stands on D:; whether the pins roster
names it (tools/b303_pins.py's roster, read live, beside data/b752_pins_closing.txt's rows), the root's repository list (tools/act_root.py),
the face's kernels (data/b752_kernels_face.json) and the census's kernel table (the census at v0.8.3, its section 1A, first column); its
local HEAD beside its remote main; its latest tag by version order; its branches and tags counted; and a last column naming every list the
row is absent from. A bank of this act and no ledger: nothing fetched, nothing written to any repository but this bank and its JSON; from a
PRIVATE repository names, counts and hashes alone.

  python -X utf8 -u tools/b753_kernels.py control          the controls alone, no remote read
  python -X utf8 -u tools/b753_kernels.py run              the controls printed, then the reads, then the bank (refuses unless this file is
                                                           committed and unchanged, and under the memory and disk holds)
  python -X utf8 -u tools/b753_kernels.py retry <name>     one repository read again (the seat's one retry, an event), the bank recomposed
  python -X utf8 -u tools/b753_kernels.py compose          the bank recomposed from the JSON, no remote read
"""
import glob
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT = 'b753'
BANK = os.path.join(RELAY, 'data', '%s_kernels.txt' % ACT)
JSN = os.path.join(RELAY, 'data', '%s_kernels.json' % ACT)
CENSUS = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'
FACE = os.path.join(RELAY, 'data', 'b752_kernels_face.json')
PINS_BANK = os.path.join(RELAY, 'data', 'b752_pins_closing.txt')
LISTS = ('pins', 'root', 'face', 'census')
VERSION = re.compile(r'^v(\d+(?:\.\d+)*)$')
# ### the navigator's read of 2026-11-11 ((R363)(5)(i)), a figure to reproduce or differ; and the heads the record holds entering the read
NAV = dict(public_side=42, ef_branches=31, ef_tags=40)
KNOWN = (('relay', '0e855242', 'the remote main after b752`s closing push, nothing pushed since (data/b753_stepzero.txt)'),
         ('PLACE-papers', '4db2fc1c', 'the remote main after b752`s record push'),
         ('SIDE-explicit-formula', '8fbab45d', 'main as (R363)(5)(iii) names it'))


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a, **kw):
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='Never')
    args = ['git'] + (['-C', repo] if repo else []) + list(a)
    try:
        r = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace', env=env, timeout=kw.get('timeout', 60))
    except subprocess.TimeoutExpired:
        return '', 124, 'timed out after %d s' % kw.get('timeout', 60)
    return r.stdout, r.returncode, (r.stderr or '').strip()


def vkey(tag):
    m = VERSION.match(tag)
    return tuple(int(x) for x in m.group(1).split('.')) if m else None


def latest(tags):
    """the latest tag by version order among the tags of the form v<n>(.<n>)*; None where none has the form."""
    v = [t for t in tags if vkey(t)]
    return max(v, key=vkey) if v else None


def parse(text):
    """an ls-remote listing -> dict(heads {name: sha}, tags {name: commit sha, the peeled one where the tag is annotated})."""
    heads, tags, peel = {}, {}, {}
    for l in text.split('\n'):
        if '\t' not in l:
            continue
        sha, ref = [x.strip() for x in l.split('\t', 1)]
        if ref.startswith('refs/heads/'):
            heads[ref[len('refs/heads/'):]] = sha
        elif ref.startswith('refs/tags/'):
            n = ref[len('refs/tags/'):]
            if n.endswith('^{}'):
                peel[n[:-3]] = sha
            else:
                tags[n] = sha
    tags.update(peel)
    return dict(heads=heads, tags=tags)


def visibility():
    import b303_pins as P
    return P.visibility()


def path_of(name):
    return {'relay': RELAY.replace('\\', '/'), 'PLACE-papers': 'D:/MY-DOwnloads/PLACE-papers'}.get(name, 'D:/' + name)


def names():
    """the rows: every repository of the visibility map, then every SIDE-* directory on D: the map does not name."""
    vis = visibility()
    extra = sorted(os.path.basename(p) for p in glob.glob('D:/SIDE-*') if os.path.isdir(p) and os.path.basename(p) not in vis)
    return sorted(vis, key=lambda n: (n not in ('relay', 'PLACE-papers'), n)) + extra, vis


def census_table():
    """the first column of the census's kernel table: section 1A of the census at v0.8.3, read at PLACE-papers HEAD."""
    t, code, err = git(path_of('PLACE-papers'), 'show', 'HEAD:%s' % CENSUS)
    if code:
        raise SystemExit('### THE CENSUS NOT READ: exit %d %s' % (code, err[:200]))
    out, on = [], False
    for l in t.split('\n'):
        if l.startswith('## '):
            on = l.startswith('## §1A')
            continue
        if on and l.startswith('|'):
            c = l.split('|')[1].strip().strip('`*').strip()
            if c in ('relay', 'PLACE-papers') or re.fullmatch(r'SIDE-[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*', c):
                out.append(c)
    return out


def lists():
    """{list: set of names}, each read from its own source; and the notes the reading found."""
    import act_root as AR
    import b303_pins as P
    ros, _src = P.roster()
    bank = re.findall(r'(?m)^--- (\S+)\s+\(', io.open(PINS_BANK, encoding='utf-8').read())
    live = [n for n, _p, _s in ros]
    face = json.load(io.open(FACE, encoding='utf-8'))
    L = dict(pins=set(live), root=set(AR.repositories()), face=set(face['kernels']), census=set(census_table()))
    notes = ['the pins roster read live (tools/b303_pins.py roster(), the texts on PLACE-papers main): %d ; data/b752_pins_closing.txt`s rows: %d ; %s' % (
        len(live), len(bank), 'THE SAME NAMES' if set(live) == set(bank) else '### DIFFERING: live alone %s ; the bank alone %s' % (
            sorted(set(live) - set(bank)), sorted(set(bank) - set(live)))),
        'the root`s repository list (tools/act_root.py repositories(), HEAD): %d ; its census reader reads %s' % (len(L['root']), AR.CENSUS),
        'the face`s kernels (data/b752_kernels_face.json, banked %s): %d' % (face.get('at'), len(L['face'])),
        'the census`s kernel table (%s section 1A, first column, PLACE-papers HEAD): %d' % (CENSUS, len(L['census']))]
    return L, notes, face


def absent_from(name, L):
    return [k for k in LISTS if name not in L[k]]


def url_for(name):
    """for a repository with no clone on D:, the relay's own origin with its last segment replaced; no URL is typed here."""
    u = git(RELAY, 'remote', 'get-url', 'origin')[0].strip()
    return re.sub(r'/relay(\.git)?$', '/%s.git' % name, u)


def read_one(name):
    """one repository: its local reads and one remote read."""
    p = path_of(name)
    row = dict(name=name, at=stamp(), on_d=os.path.isdir(os.path.join(p, '.git')), dir_no_git=os.path.isdir(p) and not os.path.isdir(os.path.join(p, '.git')))
    if row['on_d']:
        row['head'] = git(p, 'rev-parse', 'HEAD')[0].strip()
        row['branch'] = git(p, 'rev-parse', '--abbrev-ref', 'HEAD')[0].strip()
        out, code, err = git(p, 'ls-remote', '--heads', '--tags', 'origin', timeout=120)
    else:
        out, code, err = git(None, 'ls-remote', '--heads', '--tags', url_for(name), timeout=120)
    row['code'], row['err'] = code, err[:240]
    if code:
        return row
    r = parse(out)
    row['heads'], row['tags'] = r['heads'], r['tags']
    main = r['heads'].get('main') or r['heads'].get('master')
    row['main'], row['main_name'] = main, ('main' if 'main' in r['heads'] else 'master' if 'master' in r['heads'] else None)
    if row['on_d'] and main:
        if row['head'] == main:
            row['rel'] = 'EQUAL'
        elif git(p, 'cat-file', '-e', main + '^{commit}')[1]:
            row['rel'] = 'THE REMOTE MAIN NOT IN THE CLONE'
        else:
            a = git(p, 'rev-list', '--count', '%s..HEAD' % main)[0].strip()
            b = git(p, 'rev-list', '--count', 'HEAD..%s' % main)[0].strip()
            row['rel'] = 'CLONE %s AHEAD, %s BEHIND' % (a, b)
    return row


def controls():
    """(ok, lines): printed before any figure."""
    L, ok = [], True

    def case(what, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        L.append('  %s: %r %s' % (what, got, 'AS WANTED' if good else '### NOT AS WANTED, wanted %r' % (want,)))
    fx = ('1111111111111111111111111111111111111111\trefs/heads/main\n2222222222222222222222222222222222222222\trefs/heads/side\n'
          '3333333333333333333333333333333333333333\trefs/tags/v0.9\n4444444444444444444444444444444444444444\trefs/tags/v0.10\n'
          '5555555555555555555555555555555555555555\trefs/tags/v0.10^{}\n6666666666666666666666666666666666666666\trefs/tags/v0.2.1\n'
          '7777777777777777777777777777777777777777\trefs/tags/a-name-with-no-version\n')
    r = parse(fx)
    case('(parser) a planted listing, two heads and four tags, one annotated: (branches, tags, latest, its commit, main)',
         (len(r['heads']), len(r['tags']), latest(r['tags']), r['tags']['v0.10'][:4], r['heads']['main'][:4]), (2, 4, 'v0.10', '5555', '1111'))
    case('(parser) an error text and an empty answer are no listing', (parse('fatal: repository not found'), parse('')),
         (dict(heads={}, tags={}), dict(heads={}, tags={})))
    case('(version order) v0.9, v0.10, v0.19.1, v0.34.1, v0.38, v0.4', latest(['v0.9', 'v0.10', 'v0.19.1', 'v0.34.1', 'v0.38', 'v0.4']), 'v0.38')
    case('(version order) v1.5 beside v1.10, and a name of no version form alone', (latest(['v1.5', 'v1.10']), latest(['release'])), ('v1.10', None))
    import remoteread
    try:
        remoteread.g(RELAY, 'ls-remote', 'no-such-remote-b753', 'refs/heads/main')
        failed = 'NO FAILURE'
    except remoteread.RemoteReadFailed as e:
        failed = str(e)[:10]
    case('(a failed read) the kept reader against a remote name that does not resolve (no network)', failed, '### FAILED')
    out, code, _err = git(RELAY, 'ls-remote', '--heads', '--tags', 'no-such-remote-b753')
    case('(a failed read) this tool`s own reader on the same: (output, exit code non-zero)', (out, bool(code)), ('', True))
    vis = visibility()
    case('(the map) data/repo_visibility.txt: (rows, PRIVATE, PUBLIC), its own closing line 52 ; 8 ; 44',
         (len(vis), sum(1 for v in vis.values() if v == 'PRIVATE'), sum(1 for v in vis.values() if v == 'PUBLIC')), (52, 8, 44))
    LL, notes, _face = lists()
    case('(the lists) each reader reaches a known member: relay in pins, SIDE-kernel in root, SIDE-explicit-formula in face, SIDE-archimedean in census',
         ('relay' in LL['pins'], 'SIDE-kernel' in LL['root'], 'SIDE-explicit-formula' in LL['face'], 'SIDE-archimedean' in LL['census']), (True, True, True, True))
    case('(the lists) a planted name no list holds reads absent from each', absent_from('SIDE-planted-b753', LL), list(LISTS))
    case('(the lists) SIDE-explicit-formula, held by all four, reads absent from none', absent_from('SIDE-explicit-formula', LL), [])
    case('(no clone) the URL for a repository with no clone is the relay`s origin with its last segment replaced',
         url_for('X-planted').endswith('/X-planted.git') and '/relay' not in url_for('X-planted'), True)
    L.append('  ### THE CONTROLS: %d ; %s' % (len(L), 'ALL AS WANTED' if ok else '### NOT ALL AS WANTED'))
    return ok, L, notes


def sh(x):
    return (x or '')[:8] or '-'


def compose(state):
    rows, vis = state['rows'], visibility()
    LL, notes, face = lists()
    ok, CL, _n = controls()
    order = state['order']
    L = ['%s -- (R363)(5)(i): THE KERNELS RECONCILED -- every repository of data/repo_visibility.txt and every SIDE-* directory on D:, each remote read '
         'once by ls-remote (%s)' % (ACT, state['at'][:10]), '',
         '### Written by tools/%s_kernels.py at relay %s (the generator committed before its run), the reads %s to %s. A bank of this act and no ledger;'
         % (ACT, state['generator'], state['at'], state['end']),
         '### nothing fetched, no repository changed. One `git ls-remote --heads --tags` per row; a read that fails prints FAILED and is not read again by',
         '### the run. From a PRIVATE repository: its name, as the map names it, counts and hashes alone.', '',
         '## THE CONTROLS, printed before any figure'] + CL + ['', '## THE LISTS READ'] + ['  ' + n for n in notes] + ['']
    L += ['## THE ROWS: repository | visibility | on D: | local HEAD (its branch) | remote main | the two compared | latest tag by version order = its commit | '
          'branches ; tags at the remote | absent from']
    fails, answered, cnt = [], 0, dict((k, 0) for k in LISTS)
    for n in order:
        r = rows[n]
        v = vis.get(n, '### NOT IN THE MAP')
        ab = absent_from(n, LL)
        for k in ab:
            cnt[k] += 1
        where = 'on D:' if r['on_d'] else ('### A DIRECTORY, NO REPOSITORY' if r.get('dir_no_git') else 'NO CLONE ON D:')
        local = '%s (%s)' % (sh(r.get('head')), r.get('branch')) if r['on_d'] else '-'
        if r['code']:
            fails.append(n)
            L.append('  %s | %s | %s | %s | ### FAILED exit %d: %s%s | - | - | - | %s' % (
                n, v, where, local, r['code'], r['err'], ' (read again: %s)' % r['retry'] if r.get('retry') else '', ', '.join(ab) or 'none'))
            continue
        answered += 1
        lt = latest(r['tags'])
        L.append('  %s | %s | %s | %s | %s%s | %s | %s | %d ; %d | %s%s' % (
            n, v, where, local, sh(r.get('main')), '' if r.get('main_name') == 'main' else ' (%s)' % (r.get('main_name') or '### NO main'),
            r.get('rel', '-'), ('%s = %s' % (lt, sh(r['tags'][lt]))) if lt else ('no tag' if not r['tags'] else 'no tag of the version form'),
            len(r['heads']), len(r['tags']), ', '.join(ab) or 'none', ' (read again once, an event: %s)' % r['retry'] if r.get('retry') else ''))
    pub_side = [n for n in order if n.startswith('SIDE-') and vis.get(n) == 'PUBLIC']
    pub_ans = [n for n in pub_side if not rows[n]['code']]
    ef = rows.get('SIDE-explicit-formula', {})
    L += ['', '## THE FIGURES TO REPRODUCE OR DIFFER',
          '  the navigator`s read of 2026-11-11, the 42 public SIDE repositories, every one answered: here PUBLIC SIDE-* %d, answered %d: %s' % (
              len(pub_side), len(pub_ans), 'REPRODUCED' if (len(pub_side), len(pub_ans)) == (NAV['public_side'], NAV['public_side']) else '### DIFFERS'),
          '  SIDE-explicit-formula at 31 branches and 40 tags: here %s ; %s: %s (the face`s bank of %s: %d branches, %d tags)' % (
              len(ef.get('heads', {})), len(ef.get('tags', {})),
              'REPRODUCED' if (len(ef.get('heads', {})), len(ef.get('tags', {}))) == (NAV['ef_branches'], NAV['ef_tags']) else '### DIFFERS',
              face.get('at'), len(face['kernels']['SIDE-explicit-formula'][2]), len(face['kernels']['SIDE-explicit-formula'][1]))]
    for n, h, why in KNOWN:
        got = sh(rows.get(n, {}).get('main'))
        L.append('  %s remote main %s, the record`s %s (%s): %s' % (n, got, h, why, 'EQUAL' if got == h else '### DIFFERS'))
    uneq = [n for n in order if rows[n].get('rel') not in (None, 'EQUAL')]
    L += ['', '## READ BESIDE THE ROWS',
          '  local HEAD not the remote main: %d%s' % (len(uneq), (' -- ' + ' ; '.join('%s %s' % (n, rows[n]['rel']) for n in uneq)) if uneq else ''),
          '  a clone standing on a branch other than main: %s' % (', '.join('%s (%s)' % (n, rows[n]['branch']) for n in order
                                                                 if rows[n]['on_d'] and rows[n].get('branch') not in ('main', rows[n].get('main_name'))) or 'none'),
          '  rows absent from a list, by list: %s' % ' ; '.join('%s %d' % (k, cnt[k]) for k in LISTS),
          '  rows absent from no list: %d ; from every list: %d (%s)' % (
              sum(1 for n in order if not absent_from(n, LL)), sum(1 for n in order if len(absent_from(n, LL)) == 4),
              ', '.join(n for n in order if len(absent_from(n, LL)) == 4) or 'none'),
          '  names a list holds and no row carries: %s' % (', '.join('%s (%s)' % (x, k) for k in LISTS for x in sorted(LL[k]) if x not in rows) or 'none'),
          '']
    u = sum(1 for n in order if absent_from(n, LL))
    L.append('### ### **THE KERNELS RECONCILED: %d REPOSITORIES ; ANSWERED %d ; FAILED %d%s ; ON D: %d ; ABSENT FROM A LIST %d ; LOCAL HEAD NOT THE REMOTE MAIN %d ; '
             'CONTROLS %s.**' % (len(order), answered, len(fails), (' (%s)' % ', '.join(fails)) if fails else '', sum(1 for n in order if rows[n]['on_d']), u,
                                 len(uneq), 'ALL AS WANTED' if ok else '### NOT ALL AS WANTED'))
    return L


def bank(state):
    tmp = JSN + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(state, indent=1, sort_keys=True, ensure_ascii=False) + '\n')
    os.replace(tmp, JSN)
    L = compose(state)
    tmp = BANK + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(L) + '\n')
    os.replace(tmp, BANK)
    return L


def slim(row, vis):
    """what the JSON keeps: every ref of a PUBLIC SIDE-* repository and the relay; from any other, the main, the counts and the version tags."""
    if row.get('code') or (row['name'].startswith('SIDE-') and vis.get(row['name']) == 'PUBLIC') or row['name'] == 'relay':
        return row
    keep = dict(row)
    keep['heads'] = dict((('b%04d' % i) if k not in ('main', 'master') else k, '') for i, k in enumerate(sorted(row['heads'])))
    keep['tags'] = dict((k if vkey(k) else 't%05d' % i, v if vkey(k) else '') for i, (k, v) in enumerate(sorted(row['tags'].items())))
    return keep


def committed():
    rel = 'tools/%s_kernels.py' % ACT
    tracked = git(RELAY, 'ls-files', '--error-unmatch', rel)[1] == 0
    dirty = git(RELAY, 'status', '--porcelain', '--', rel)[0].strip()
    return tracked and not dirty, git(RELAY, 'rev-parse', '--short=8', 'HEAD')[0].strip()


def main(argv):
    if argv[:1] == ['control']:
        ok, L, notes = controls()
        print('\n'.join(L + ['  ' + n for n in notes]))
        return 0 if ok else 1
    if argv[:1] == ['compose']:
        print('\n'.join(bank(json.load(io.open(JSN, encoding='utf-8')))))
        return 0
    if argv[:1] == ['retry'] and len(argv) == 2:
        state = json.load(io.open(JSN, encoding='utf-8'))
        if argv[1] not in state['rows'] or not state['rows'][argv[1]]['code'] or state['rows'][argv[1]].get('retry'):
            raise SystemExit('### REFUSED: %s is no failed row, or was read again already (one retry)' % argv[1])
        first = state['rows'][argv[1]]
        row = slim(read_one(argv[1]), visibility())
        row['retry'] = 'the first read at %s FAILED exit %d (%s); read again at %s' % (first['at'], first['code'], first['err'][:120], row['at'])
        state['rows'][argv[1]] = row
        state['end'] = stamp()
        print('\n'.join(bank(state)[-14:]))
        return 0
    if argv[:1] != ['run']:
        raise SystemExit(__doc__)
    done, head = committed()
    if not done:
        raise SystemExit('### REFUSED: tools/%s_kernels.py is not committed or differs from its commit; the generator commits before its run ((R363)(5))' % ACT)
    import hold
    if hold.refuses('the kernels read ((R363)(5)(i))'):
        return 3
    ok, CL, notes = controls()
    print('## THE CONTROLS, printed before any figure')
    print('\n'.join(CL))
    if not ok:
        raise SystemExit('### THE CONTROLS NOT ALL AS WANTED: NOTHING READ')
    order, vis = names()
    state = dict(at=stamp(), generator=head, order=order, rows={})
    for n in order:
        row = read_one(n)
        state['rows'][n] = slim(row, vis)
        print('  read %s %s: %s' % (row['at'], n, ('### FAILED exit %d: %s' % (row['code'], row['err'])) if row['code'] else
                                    'main %s ; %d branches ; %d tags' % (sh(row.get('main')), len(row['heads']), len(row['tags']))))
    state['end'] = stamp()
    L = bank(state)
    print('\n'.join(L[L.index('## THE LISTS READ'):]))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
