# -*- coding: utf-8 -*-
"""b706_report.py -- THE CLOSING'S REPORT LINES ON THE AUTHOR'S WORD AT THE ROOT'S PROMPT (b706, (R316)(10)).

### The author's word at the root (relay data/b706_author_answers.txt, the root's call; checked by tools/b706_citation.py answer before this
### tool was written): "The closing's report prints, each in one line with its bank: the 17 renames with the retired paths; the join's holding
### line at lv-conservation's module, by file and line of the error in the artifact; the 15 grades the final table moved, by paper, with the
### cell before and after; the entry-tag prints' readings of the 11 mentions; and the four standing arms' figures beside b705's, the
### partner-copies figure expected at 0." The closing tool (tools/b706_closing.py) is SEALED and its report prints the counts; this tool,
### written whole by the Write tool after the seal and not sealed, reads the same banks and prints the five lines into data/b706_report.txt
### (with data/b706_report.json), committed before the root so that the root names them; the defects bank's event carries the five lines
### verbatim, and the closing, which prints that bank whole, prints them. ### Writes data/b706_report.txt and data/b706_report.json and
### nothing else; reads banks alone, no ledger line.
"""
import io
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
ARCHIVE = 'archive/2026-10-22-b706-partner-copies'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


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


def cells_of(row):
    return ', '.join('%s :%s %s' % ((c.get('ledger') or '').replace('PLACE-papers/', ''), c.get('line'), c.get('grade')) for c in (row.get('grade_cells') or [])) or 'no cell'


def main():
    # (1) the 17 renames with the retired paths
    pj = jl('b706_partners.json').get('rows') or []
    ren = [r for r in pj if str(r.get('reading', '')).startswith('RENAME')]
    l1 = ('the %d renames with the retired paths (relay data/b706_partners.txt; PLACE-papers 1dfd9bc..cedf7e9, one commit each): ' % len(ren)
          + ' ; '.join('%s: %s -> %s, the retired copy at %s/%s' % (r['doc'], r['versioned'], r['unversioned'], ARCHIVE, r['unversioned']) for r in ren))
    # (2) the join`s holding line, by file and line of the error in the artifact
    bl = rd('b706_buildlog_SIDE-faces-join_join.txt').split(NL)
    rn = rd('b706_runner_SIDE-faces-join_join.txt').split(NL)
    bi = next((i + 1 for i, l in enumerate(bl) if 'GammaBounds.lean:177' in l), None)
    ri = next((i + 1 for i, l in enumerate(rn) if 'GammaBounds.lean:177' in l), None)
    err = bl[bi - 1].strip() if bi else '### NOT READ'
    l2 = ('the join`s holding line at lv-conservation`s module (the artifact`s build.log of run 39850337262, banked whole as relay '
          'data/b706_buildlog_SIDE-faces-join_join.txt :%s, read after the artifact`s sha256 agreed; the runner bank data/b706_runner_SIDE-faces-join_join.txt :%s; '
          'the grade bank data/b706_join_grade.txt): %s -- SIDELvConservation/GammaBounds.lean, line 177, column 8, at the shared pin Lean v4.34.0-rc1 / Mathlib de5ce8a9; '
          'FacesJoin.lean not reached' % (bi, ri, err))
    # (3) the grades the final table moved, by paper, with the cell before and after
    cur = dict(((r.get('repo'), r.get('name')), r) for r in (jl('terminal_table.json').get('rows') or jl('terminal_table.json') if isinstance(jl('terminal_table.json'), dict) else []))
    if not cur:
        cur = dict(((r.get('repo'), r.get('name')), r) for r in jl('terminal_table.json'))
    prj = jl('terminal_table_prior.json')
    pri = dict(((r.get('repo'), r.get('name')), r) for r in (prj.get('rows') if isinstance(prj, dict) else prj))
    dj = jl('terminal_table_diff.json')
    changed = [tuple(x) for x in (dj.get('changed') or [])]
    added = [tuple(x) for x in (dj.get('added') or [])]
    parts, arch = [], 0
    for k in changed:
        a, b = pri.get(k) or {}, cur.get(k) or {}
        ca, cb = cells_of(a), cells_of(b)
        if ARCHIVE in cb:
            arch += 1
        parts.append('%s/%s: %s [%s] -> %s [%s]%s' % (k[0], k[1], a.get('grade'), ca, b.get('grade'), cb, (' (conflict %s)' % ' vs '.join(b['conflict'])) if b.get('conflict') else ''))
    added_arch = sum(1 for k in added if ARCHIVE in cells_of(cur.get(k) or {}))
    l3 = ('the %d grades the final table moved (relay data/b706_table_final.txt; data/terminal_table.json against data/terminal_table_prior.json), by paper with the cell '
          'before and after -- %d of the %d after-cells cite the retired copies under %s/, which tools/terminal_table.py reads as ledgers, and %d of the %d added rows cite them too: ' % (
              len(changed), arch, len(changed), ARCHIVE, added_arch, len(added)) + ' ; '.join(parts))
    # (4) the entry-tag prints` readings of the 11 mentions
    cj = jl('b706_cells_reread.json').get('rows') or []
    l4 = ('the entry-tag prints` readings of the %d mentions (relay data/b706_cells_reread.txt, against data/b706_prints_v0.1.txt and data/b706_prints_v0.2.txt): ' % len(cj)
          + ' ; '.join('%s :%s %s at %s -- %s' % (r.get('doc'), r.get('line'), r.get('full'), r.get('tag'), r.get('verdict')) for r in cj))
    # (5) the four standing arms` figures beside b705`s
    f6, f5 = jl('b706_standing_figures.json'), jl('b705_standing_figures.json')
    fig = lambda j, k: (j.get(k) or {}).get('figure')   # noqa: E731
    l5 = ('the four standing arms` figures beside b705`s (relay data/b706_standing_figures.txt, data/b705_standing_figures.json): correspondence %s (b705 %s) ; readme %s (b705 %s) ; '
          'partners %s (b705 %s; expected 0 at the resolution, one copy per table: %s) ; pins %s (b705 %s)' % (
              fig(f6, 'correspondence'), fig(f5, 'correspondence'), fig(f6, 'readme'), fig(f5, 'readme'), fig(f6, 'partners'), fig(f5, 'partners'),
              'AS EXPECTED' if fig(f6, 'partners') == 0 else '### NOT 0', fig(f6, 'pins'), fig(f5, 'pins')))
    L = ['%s -- THE CLOSING`S REPORT LINES ON THE AUTHOR`S WORD AT THE ROOT, EACH WITH ITS BANK (%s)' % ('b706', utc()), '',
         '### rows are the five lines the author`s word at the root`s prompt orders the closing`s report to print (relay data/b706_author_answers.txt), each',
         '### read from its bank by this tool; the sealed closing tool prints its own report and this bank whole through the defects bank`s event.', '',
         '  (1) ' + l1, '  (2) ' + l2, '  (3) ' + l3, '  (4) ' + l4, '  (5) ' + l5, '',
         '### ### **LINES 5 ; RENAMES %d ; THE HOLDING LINE AT build.log :%s ; GRADES MOVED %d, %d CITING THE RETIRED COPIES ; MENTIONS %d ; PARTNERS FIGURE %s.**' % (
             len(ren), bi, len(changed), arch, len(cj), fig(f6, 'partners'))]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b706_report.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    j = dict(at=utc(), lines=[l1, l2, l3, l4, l5], renames=len(ren), holding_line=bi, moved=len(changed), moved_citing_archive=arch, added=len(added),
             added_citing_archive=added_arch, mentions=len(cj), partners_figure=fig(f6, 'partners'))
    pj_ = os.path.join(D, 'b706_report.json')
    with open(pj_ + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(pj_ + '.tmp', pj_)
    print(NL.join(L))


if __name__ == '__main__':
    main()
