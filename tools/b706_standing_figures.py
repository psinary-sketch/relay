# -*- coding: utf-8 -*-
"""b706_standing_figures.py -- THE FOUR STANDING ARMS' FIGURES AT b706, READ FROM THIS ACT'S ROSTER AFTER THE RENAMES OF (R316)(3).

### tools/b705_standing_figures.py (sealed at b705) and tools/b703_standing_figures.py (sealed at b703) are IMPORTED and unedited: readme() is
### b705's repaired one, pins() b703's, each re-exported here. THE CARRY-TIME REPAIR (relay data/b706_tool_repairs.txt row (7)): b703's
### correspondence() and partners() take their roster from b672's bank (data/b672_roster_read.json), whose `path` is the VERSIONED copy for nine
### tables and whose `partner` is the unversioned copy of each pair -- after (R316)(3) every versioned copy stands at the unversioned name and
### every unversioned copy in archive/2026-10-22-b706-partner-copies/, so b703's readers would find nine tables missing and seventeen partners
### gone. Here:
###   correspondence()  b703's reading, its body carried line for line, over THIS ACT'S roster (data/b706_roster_read.json: the 20 tables at the
###                     unversioned names, written by the record tool's roster706 route before the generator's dry run, each found by its anchor);
###   partners()        one copy per table after the disposition: a row per roster table reading ONE COPY, no partner, differing 0; the figure 0
###                     -- the order's unit (lines differing between the two copies of one paper) has no two copies to count from b706 on; a
###                     table that still names a partner (none in this act's roster) is read as b703 read it.
### No sealed module's constant is rebound. No figure is a verdict; every reader prints its rows. Written by the Write tool at b706; it writes
### nothing.
"""
import difflib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b703_standing_figures as SF3   # noqa: E402  ### sealed at b703, imported unedited
import b705_standing_figures as SF5   # noqa: E402  ### sealed at b705, imported unedited
import correspondence_gen as CG       # noqa: E402  ### the generator's readers (its parser extended at this act under (R316)(6))

PP, NL = SF3.PP, SF3.NL
ROSTER = 'b706_roster_read.json'
readme, pins, highest_local, faces_kernels, deposited, decl_at = SF5.readme, SF3.pins, SF3.highest_local, SF3.faces_kernels, SF5.deposited, SF3.decl_at
_read = SF3._read


def _roster():
    """this act's roster: data/b706_roster_read.json's tables (the 20 at the unversioned names)."""
    try:
        return json.load(io.open(os.path.join(D, ROSTER), encoding='utf-8')).get('tables') or []
    except Exception:
        return []


def correspondence():
    """per paper: the rows current, behind, at a moved tag with a changed statement, unread; the figure the changed-statement rows (b703's
    reading over this act's roster)."""
    papers = []
    for t in _roster():
        path = os.path.join(PP, *t['path'].split('/'))
        lines = _read(path).split(NL)
        r = CG.find_table(lines, t)
        row = dict(paper=t['doc'], path=t['path'], current=0, behind=0, changed=0, unread=0, changed_rows=[], reason=None)
        if not isinstance(r, tuple):
            row['reason'] = r
            papers.append(row)
            continue
        j, e = r
        cols = CG.columns(lines[j])
        if cols['kernel'] is None or cols['terminal'] is None:
            row['reason'] = 'NOT IN THE GENERATOR`S SHAPE'
            papers.append(row)
            continue
        prev_k = None
        for i in range(j + 1, e):
            l = lines[i]
            if CG.SEP_ROW.match(l):
                continue
            sp = CG.spans(l)
            if len(sp) <= max(cols['kernel'], cols['terminal']):
                row['unread'] += 1
                continue
            kc, tc = CG.cell(l, sp[cols['kernel']]), CG.cell(l, sp[cols['terminal']])
            cl = CG.parse_kernel_cell(kc)
            k = (cl[0][0] if cl else None) or prev_k
            prev_k = k or prev_k
            ver = next((x for _s, _e, kind, x in (cl[0][1] if cl else []) if kind == 'ver'), None)
            m = CG.IDENT.search(tc)
            if not k or not ver or not m:
                row['unread'] += 1
                continue
            cur = highest_local(k)
            if cur is None:
                row['unread'] += 1
                continue
            if ver == cur:
                row['current'] += 1
                continue
            row['behind'] += 1
            short = m.group(1).split('.')[-1]
            d0, d1 = decl_at(k, ver, short), decl_at(k, cur, short)
            if d0 and d1 and d0 != d1:
                row['changed'] += 1
                row['changed_rows'].append(':%d %s %s -> %s %s' % (i + 1, k, ver, cur, short))
        papers.append(row)
    return sum(p['changed'] for p in papers), papers


def partners():
    """per roster table after (R316)(3): ONE COPY at the unversioned name, no partner, differing 0; a table still naming a partner (none in this
    act's roster) read as b703's partners() reads a pair. The figure the total."""
    out = []
    for t in _roster():
        a, b = t.get('path'), t.get('partner')
        if not b or b == a:
            out.append(dict(paper=t['doc'], path=a, partner=None, differing=0, reason='ONE COPY (the pair renamed in place at b706, (R316)(3))'))
            continue
        x = _read(os.path.join(PP, *a.split('/'))).split(NL)
        y = _read(os.path.join(PP, *b.split('/'))).split(NL)
        rx, ry = CG.find_table(x, t), CG.find_table(y, t)
        if not isinstance(rx, tuple) or not isinstance(ry, tuple):
            out.append(dict(paper=t['doc'], path=a, partner=b, differing=None, reason='%s ; %s' % (rx if not isinstance(rx, tuple) else 'found',
                                                                                                  ry if not isinstance(ry, tuple) else 'found')))
            continue
        tx, ty = x[rx[0]:rx[1]], y[ry[0]:ry[1]]
        n = sum(max(i2 - i1, j2 - j1) for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, tx, ty, autojunk=False).get_opcodes() if tag != 'equal')
        out.append(dict(paper=t['doc'], path=a, partner=b, differing=n, reason=None))
    return sum(r['differing'] or 0 for r in out), out


def all_figures(baseline=None, remote=None, readme_text=None):
    c, cr = correspondence()
    r, rr = readme(remote, readme_text)
    p, pr = partners()
    s, sr = pins(baseline)
    return dict(correspondence=dict(figure=c, papers=cr), readme=dict(figure=r, rows=rr), partners=dict(figure=p, rows=pr),
                pins=dict(figure=s, rows=sr['rows'], federation=sr['federation'], faces=sr['faces'], moved=sr['moved']))
