# -*- coding: utf-8 -*-
"""standing/amend.py -- v1.17.0, (R347)(2)(i), b736 events (1): THE FACE THAT DID NOT FOLLOW THE AMENDMENT.

The author's word at a prompt that widens or narrows a ruling clause is an amendment row, banked in data/<act>_amendments.json; the face's (W)
row and N5's text are regenerated from the ruling plus its amendment rows before the lock, the regeneration printed. b736's word amending
(R346)(4) widened the writes to the PLACE-papers file each passed item names; the worklist carried three doors from 02:07Z, the face's (W) row,
composed from the ruling's clauses alone (standing.faceform.clause_writes), did not, and N5 read REFUTED on it.

  data/<act>_amendments.json = {"rows": [{"at": utc, "clause": "(R346)(4)", "words": the author's words verbatim, "widens": [paths], "narrows": [paths]}]}
  writes(ruling, rows) -> [paths]           the ruling's clause-ordered files, each amendment's widened paths added and its narrowed paths removed
  missing(ruling, rows, face) -> [paths]    the files writes() names that the face's (W) list does not cover (faceform.w_missing's reading)
  w_row(ruling, rows, face) -> str or None  the regenerated (W) row naming them; None where the face covers every one
  n5_clause(ruling, rows, face) -> str      N5's write clause regenerated: the files beyond the face's (W) list the amended ruling orders, or none
  regenerate(act, ruling, face) -> lines    the printed regeneration: the rows read, the files, the (W) row, N5's clause
Pure in its arguments but regenerate, which reads the act's bank; nothing written.
v1.34.0, (R364)(3)(xvi): THE ITEM'S ROUTE, `amend.py pass ...` (below): a passed item's writes beyond the (W) list banked as an amendment row
before the write, the (W) bank regenerated and act_current's shared_edits written in the same step; the only writer here, and only with --write.
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import faceform as FF   # noqa: E402

RELAY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def bank_path(act, relay=RELAY):
    return os.path.join(relay, 'data', '%s_amendments.json' % act)


def rows_of(act, relay=RELAY):
    p = bank_path(act, relay)
    if not os.path.exists(p):
        return []
    with io.open(p, encoding='utf-8') as f:
        return list(json.load(f).get('rows') or [])


def writes(ruling, rows):
    out = set(FF.clause_writes(ruling))
    for r in rows or ():
        out |= set(r.get('widens') or ())
    for r in rows or ():
        out -= set(r.get('narrows') or ())
    return sorted(out)


def _split(p):
    """(repository, path): a path written `PLACE-papers/...` or `SIDE-x/...` is that repository's, a bare path the relay's."""
    for pre in ('relay/', 'PLACE-papers/'):
        if p.startswith(pre):
            return pre[:-1], p[len(pre):]
    m = re.match(r'(SIDE-[\w-]+)/(.*)$', p)
    return (m.group(1), m.group(2)) if m else ('relay', p)


def _covered(p, face):
    """the face's (W) list read as the scorer reads it: tools/act_close.py w_patterns and w_allows, a backticked path carrying its repository.
    b736's row named the three doors bare (`phase2/method/...`), a form w_patterns does not read, and N5 counted them beyond the list."""
    sys.path.insert(0, os.path.join(RELAY, 'tools'))
    import act_close as AC
    repo, rel = _split(p)
    return AC.w_allows(rel, AC.w_patterns(face or ''), repo)


def missing(ruling, rows, face):
    return [p for p in writes(ruling, rows) if not _covered(p, face)]


def w_row(ruling, rows, face):
    miss = missing(ruling, rows, face)
    if not miss:
        return None
    shown = ' '.join('`%s/%s`' % _split(p) for p in miss)
    return '### | the ruling`s clauses and its amendment rows, read by the composer (v1.17.0) | %s |' % shown


def n5_clause(ruling, rows, face):
    miss = missing(ruling, rows, face)
    return ('no file written beyond the (W) list regenerated from the ruling and its %d amendment row%s' % (len(rows or ()), '' if len(rows or ()) == 1 else 's')
            + ('' if not miss else ' ; THE FACE LACKS %s' % ', '.join(miss)))


def regenerate(act, ruling, face, rows=None, relay=RELAY):
    rows = rows_of(act, relay) if rows is None else rows
    L = ['### THE (W) REGENERATION ((R347)(2)(i)): the ruling`s clauses plus %d amendment row%s, data/%s_amendments.json' % (len(rows), '' if len(rows) == 1 else 's', act)]
    for r in rows:
        L.append('  %s %s widens %s narrows %s' % (r.get('at'), r.get('clause'), r.get('widens') or 'none', r.get('narrows') or 'none'))
    L.append('  the files ordered: %d ; the face lacks: %s' % (len(writes(ruling, rows)), missing(ruling, rows, face) or 'none'))
    L.append('  the (W) row: %s' % (w_row(ruling, rows, face) or 'none owed, the face covers every file'))
    L.append('  N5: %s' % n5_clause(ruling, rows, face))
    return L


# ### v1.34.0, (R364)(3)(xvi), b753 (v'): A PASSED ITEM'S WRITE BEYOND THE (W) LIST. b753's [M1] passed and its draft wrote
# ### tools/mirror_roster_added.json beside the roster (R363)(9) named (relay 0db31ce3); the (W) bank did not cover it, the hook (which reads
# ### tracked paths) let the new file through, no amendment row was banked until the face's composition, and data/act_current.json's
# ### shared_edits was not written with it, so the act part's probe failed G-ACT-CURRENT. The item's route: run before the write, it reads the
# ### paths the passed draft writes against the (W) bank, banks one amendment row widening to those the list does not cover, regenerates the
# ### bank, and writes act_current's shared_edits line as standing.act.shared_edits will read it after the pass's commit -- all before the
# ### write, in the step the commit closes. It refuses where a path beyond the list already stands written (the write before its row).
#
#   python -X utf8 -u tools/standing/amend.py pass <item> <word_at> <word_cite> <path> [<path> ...] [--write]
#     <item> e.g. [M1]; <word_at> the author's word's UTC time; <word_cite> the bank and line holding it; a <path> as the (W) table writes it
#     (relay/..., PLACE-papers/..., SIDE-x/..., a bare path the relay's). Dry without --write: the plan printed, nothing written.
SHARED_LINE = re.compile(r'^ "shared_edits": \[[^\n]*\](,?)$', re.M)
PP = 'D:/MY-DOwnloads/PLACE-papers'


def beyond(paths, pats):
    """the passed item's paths the (W) patterns do not cover, each as repository/path."""
    import wlist as WL
    out = []
    for p in paths:
        repo, rel = _split(p)
        if not WL.allows(repo, rel, pats):
            out.append('%s/%s' % (repo, rel))
    return out


def pass_row(ruling, item, word_at, word_cite, widen, at):
    """the amendment row the item's route banks: no words of its own (the author's word stands at word_cite), widening to `widen`."""
    return dict(at=at, clause='(%s)(5)%s passed on the author`s word (%s, %s): the item`s writes beyond the (W) list, banked by the item`s route '
                              'before the write ((R364)(3)(xvi))' % (ruling, item, word_at, word_cite),
                session=None, transcript_line=None, words='', word_at=word_at, word_cite=word_cite, widens=list(widen), narrows=[],
                by='tools/standing/amend.py pass')


def shared_after(act, committed, paths):
    """data/act_current.json's shared_edits after the pass's commit: the committed list (standing.act.shared_edits over the act's commits) with
    the pass's own relay paths under tools/ outside the act's own files, the act modules and the standing tools."""
    out = set(committed or ())
    for p in paths:
        repo, rel = _split(p)
        if repo == 'relay' and rel.startswith('tools/') and not rel.startswith(('tools/%s_' % act, 'tools/acts/', 'tools/standing/')):
            out.add(rel)
    return sorted(out)


def written(p, relay=RELAY, pp=PP):
    """True where a path already stands written: tracked and differing from HEAD, or untracked and present; None where its repository is
    not one this route reads (a kernel)."""
    import subprocess
    repo, rel = _split(p)
    top = {'relay': relay, 'PLACE-papers': pp}.get(repo)
    if top is None:
        return None
    g = lambda *a: subprocess.run(['git', '-C', top] + list(a), capture_output=True, text=True)   # noqa: E731
    if g('ls-files', '--error-unmatch', '--', rel).returncode == 0:
        return g('diff', '--quiet', 'HEAD', '--', rel).returncode != 0
    return os.path.exists(os.path.join(top, *rel.split('/')))


def plan(act, ruling, item, word_at, word_cite, paths, pats, committed, at, landed=written):
    """the route's plan, pure but for `landed`: dict(beyond, landed, row or None, shared, refused)."""
    bey = beyond(paths, pats)
    lan = [p for p in bey if landed(p)]
    return dict(beyond=bey, landed=lan, row=pass_row(ruling, item, word_at, word_cite, bey, at) if bey else None,
                shared=shared_after(act, committed, paths), refused=bool(lan))


def _pass_main(argv):
    import time
    import act as A_
    import wlist as WL
    write = '--write' in argv
    a = [x for x in argv if x != '--write']
    if len(a) < 4:
        sys.exit('usage: amend.py pass <item> <word_at> <word_cite> <path> [<path> ...] [--write]')
    item, word_at, word_cite, paths = a[0], a[1], a[2], a[3:]
    cur = WL._cur()
    act, ruling = cur['act'], cur.get('ruling') or ''
    pats, src, _s = WL.patterns(act)
    committed = A_.shared_edits(act, cur['pre_relay'])
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    P = plan(act, ruling, item, word_at, word_cite, paths, pats, committed, at)
    print('### THE ITEM`S ROUTE ((R364)(3)(xvi)): %s %s, the author`s word %s (%s) ; %s' % (act, item, word_at, word_cite, 'WRITE' if write else 'DRY, nothing written'))
    print('  the paths %d: %s' % (len(paths), ' '.join(paths)))
    print('  the (W) list (%s, %d patterns) covers all but: %s' % (src, len(pats), ', '.join(P['beyond']) or 'none'))
    print('  shared_edits: as it stands %s ; the committed list %s ; after the pass %s' % (cur.get('shared_edits'), committed, P['shared']))
    if P['refused']:
        print('  REFUSED: written before its row: %s -- the write stands before its amendment row; enter it as a defect, nothing written' % ', '.join(P['landed']))
        sys.exit(2)
    if not write:
        print('  the plan: %s ; act_current`s shared_edits %s' % ('a row widening to %s' % P['beyond'] if P['row'] else 'no row owed',
                                                               'unchanged' if P['shared'] == cur.get('shared_edits') else 'written'))
        return
    if P['row']:
        bp = bank_path(act)
        j = json.load(io.open(bp, encoding='utf-8')) if os.path.exists(bp) else {'rows': []}
        j['rows'].append(P['row'])
        with open(bp + '.tmp', 'wb') as f:
            f.write((json.dumps(j, indent=1, ensure_ascii=False) + '\n').encode('utf-8'))
        os.replace(bp + '.tmp', bp)
        print('  BANKED the amendment row %d of data/%s_amendments.json, widening %s' % (len(j['rows']), act, P['row']['widens']))
        for l in WL.regenerate(act, write=True):
            print('  ' + l)
        pats2, _src2, _s2 = WL.patterns(act)
        print('  covered after: %s' % ('every path' if not beyond(paths, pats2) else 'NOT %s' % beyond(paths, pats2)))
    if P['shared'] != cur.get('shared_edits'):
        write_shared(P['shared'])
    print('  then the write, and its commit with the bank, the (W) bank and act_current through the one-call tool')


def write_shared(shared, relay=RELAY):
    """data/act_current.json's one shared_edits line replaced by `shared`, every other byte as it stands."""
    cp = os.path.join(relay, 'data', 'act_current.json')
    t = io.open(cp, encoding='utf-8', newline='').read()
    new, k = SHARED_LINE.subn(lambda m: ' "shared_edits": %s%s' % (json.dumps(shared, ensure_ascii=False), m.group(1)), t)
    if k != 1:
        sys.exit('  REFUSED: data/act_current.json carries %d shared_edits lines, not one; nothing written to it' % k)
    with open(cp + '.tmp', 'wb') as f:
        f.write(new.encode('utf-8'))
    os.replace(cp + '.tmp', cp)
    print('  WRITTEN data/act_current.json shared_edits %s' % shared)


def _shared_main(argv):
    """`amend.py shared [--write]`: act_current's shared_edits against standing.act.shared_edits over the act's commits (a shared file committed
    by a route other than a pass, a carried file among them); with --write the field written to the committed list."""
    import act as A_
    import wlist as WL
    cur = WL._cur()
    committed = A_.shared_edits(cur['act'], cur['pre_relay'])
    same = sorted(cur.get('shared_edits') or []) == committed
    print('### THE SHARED EDITS ((R364)(3)(xvi)): %s act_current %s ; the committed list %s ; %s' % (cur['act'], cur.get('shared_edits'), committed,
                                                                                                   'EQUAL' if same else 'DIFFER'))
    if not same and '--write' in argv:
        write_shared(committed)


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if sys.argv[1:2] == ['pass']:
        _pass_main(sys.argv[2:])
    elif sys.argv[1:2] == ['shared']:
        _shared_main(sys.argv[2:])
    else:
        sys.exit(__doc__)
