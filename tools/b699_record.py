# -*- coding: utf-8 -*-
"""b699_record.py -- THE ACT'S RECORD TOOL, b699 under (R309).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b699 -- its worklist
### module K, ACT and PREV -- so that its carried routes (the helpers, the guarded landing, rowgen, answers, defects and the late routes)
### write b699's banks under b699's names; a route whose text names b698's ruling is written here afresh. (R262)(2): the one conversion of a
### backtick possessive stays b652's, imported through b698's module. Every python child is started as `python -X utf8`, no environment
### mapping passed.
### Written by the Write tool at b699 in stages: stage one, step zero's routes; Components 1-5 by the Edit tool.
### Routes: `python tools/b699_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b699_worklist as K          # noqa: E402
import b698_record as R            # noqa: E402  ### b698's routes, imported unedited

R.K, R.ACT, R.PREV, R.SP = K, 'b699', 'b698', K.SP
ACT, PREV = 'b699', 'b698'
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show

READERS = ['read_branch_row']
read_branch_row = R.read_branch_row


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank (b698's, with b699's names)."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b699_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b699_findings.json': dict(entry_line=99999, title='stand-in'),
        'b699_trail.json': dict(line=99999),
        'b699_act_root.json': dict(root='0' * 64, previous='1db80825' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


R._standins = _standins


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried)
rowgen, answers, defects = R.rowgen, R.answers, R.defects


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R309)(6); b698's form)
def branches(*a):
    """`branches before`: data/b699_branches_before.json -- b698's route, carried (every branch (R309)(6) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b699_branches.txt (.json) --
    each branch's fate read now against the tips banked before, in (R309)(6)'s words."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b699_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R309)(6): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b699_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after.']
    L += ['  %-18s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[]))
    print(NL.join(L[4:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R309)(1)
WH = ('*Appended 2026-10-21 by b699 to b698’s entry (:9684), under `(R309)`(1) -- b698 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b698_closing.txt):*')
WB = (' “b698 closed: relay f19eccc4, PLACE-papers 1a8d8d1; suite 122 of 123; root 1db808250727b615…; 4 prompts answered; 4 defects” '
      '(data/b698_closing.txt :1), the closing 14a0cb57 pushed and read back at relay main (data/b698_closing_push_out.txt :5). '
      'CORRESPONDENCE-DOMINANCE built as tools/circuit_correspondence.py, its controls passing first -- h2_sign against itself HOLDS at every '
      'binder, the planted binder caught (data/b698_correspondence_dominance.txt :77); the real reading DIFFERS at binder 1, none of the 14 rows '
      'agreeing (:76), the SIDE-lv-conservation side read as SOURCE TEXT at v0.13.0 = 8e3bc76 by the answer’s fallback since no hosted run at '
      'that tag could print residue_irreducible, the verdict qualified as source against print; W-ORD-H2-BRIDGE annotated beneath with binder 1 '
      'named as its open object (OPEN_TRAILS :15294); CLAUSE-DOMINANCE 1 of 2 by closure, DIFFERS at binder 1 by correspondence. The '
      'regularity-uses bank at 17 uses, no Lean: W1 (C¹ with absolutely integrable second derivative) 11 DISCHARGED / 6 RE-PROVED / 0 '
      'OBSTRUCTED, W2 (even C² of rapid decay without compact support) 6 / 4 / 7, W3 (finite sums of autocorrelations) 13 / 4 / 0 '
      '(data/b698_regularity_uses.txt :85), W1 and W3 together named as the wider class for the author’s word (:87). SIDE-simplicity README :9 '
      're-cut and tagged v0.1.2 naming v0.1.1 (peeled 967f747); SIMPLICITY_OF_RIEMANN_ZEROS :441 rewritten by the generator alone on the '
      'one-table roster; the partner copy’s differing lines entered beneath W-ORD-ONE-COPY (OPEN_TRAILS :15296), the generator’s stored figure 6 '
      'against the count 18 (data/b698_onecopy.txt :61). Two rules banked (data/b698_rules.txt :6, :10), row (1) binding from b699, row (2) '
      'bound at b698; the arithmetic plan’s row appended; b697’s weight line written (FINDINGS :9682). All eight scores HELD '
      '(data/b698_scores_close.json); the suite 122 of 123 before and after the push, G-NOTHING-RAN-AHEAD failing undeclared -- section (0) of '
      'the sealed face naming relay 2d19edd and 069778f in words and not by hash (data/b698_checks.txt :11, data/b698_checks_postpush.txt :11), '
      'answered by the generated corrigendum; the root 1db80825; no lean on the host; mirror-refresh-2026-10-21-b698.zip CLEAN with the root '
      'line. Four defects, all the seat’s -- (a) the stale-cell prompt quoting the stored figure 6 without a recount, (b) eight piped reads, one '
      'whole read of a 505-line file and two whole git blobs against the read rule, (c) the two face hashes left undeclared, (d) the record step '
      're-run after the root rewriting the answers bank’s timestamp line, restored by the Edit tool to the committed bytes with its write time '
      'later than the root’s (data/b698_defects.txt :6-:32). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B698_ENTRY,
         check=[('FINDINGS.md', K.B698_ENTRY, '## CLAUSE-DOMINANCE by closure and by correspondence: 1 of 2 by closure'),
                ('OPEN_TRAILS.md', K.B698_TRAIL, '### b698')], dry=dry)


# ================================================================================ COMPONENT 2: THE NAMING, (R309)(3) (b697's tie route, carried)
LICENSED_NOW = 'b690_r3_licensed.txt'      # ### reading 3's per-document rows, b648 -> b680 -> b690
KROW = re.compile(r'^  (SIDE-[\w-]+) docstrings \(read at (\w+)\)\s+(\d+) ->\s+(\d+) ->\s+(\d+)\s+\[(.*?)\]')
CUTS_SINCE = (('SIDE-rcurve', 'b691_cut.txt', 33), ('SIDE-archimedean', 'b693_cut.txt', 28),
              ('SIDE-interfaces', 'b695_cut.txt', 24), ('SIDE-simplicity', 'b697_cut.txt', 21))   # ### b697's cut added
TSUM = re.compile(r'^### ### \*\*(SIDE-[\w-]+): ROWS (\d+) ; MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+) ;')


def read_table_sum(l):
    """a per-document table's summary line (data/b647_table_<kernel>.txt): returns (kernel, rows, matches, understates, overreaches,
    unlicensed)."""
    m = TSUM.match(l or '')
    if not m:
        raise ValueError('table summary of another shape: %r' % (l,))
    return (m.group(1),) + tuple(int(x) for x in m.groups()[1:])


READERS += ['read_table_sum']


def tie(*a):
    """data/b674_rules.txt row (2) printed verbatim (:8-:11) and b652's order (data/b652_ferry.txt :19) verbatim; then every kernel row of
    reading 3's licensed table (relay data/b690_r3_licensed.txt) by line, each kernel cut since b690 replaced by its cut bank's line (b691
    SIDE-rcurve, b693 SIDE-archimedean, b695 SIDE-interfaces, b697 SIDE-simplicity); the kernels by descending count; where several stand at
    the top count, b674's rule applied in its written order, each step printed; and only then the document named. data/b699_tie.txt (.json)."""
    rl = rdn('b674_rules.txt').split(NL)[7:11]
    if not rl or not rl[0].startswith('  (2) THE TIE-BREAK BEYOND THE COUNT'):
        sys.exit('### data/b674_rules.txt :8 DOES NOT CARRY ROW (2) -- NOTHING WRITTEN')
    order = rdn('b652_ferry.txt').split(NL)[18]
    if 'the next kernel by descending count' not in order:
        sys.exit('### data/b652_ferry.txt :19 DOES NOT CARRY b652`s ORDER -- NOTHING WRITTEN')
    lt = rdn(LICENSED_NOW).split(NL)
    over = {}
    for k, bank, ln in CUTS_SINCE:
        cl = rdn(bank).split(NL)
        m = re.search(r'%s RE-CUT: THE DISTANCE BEFORE (\d+), AFTER (\d+)' % re.escape(k), cl[ln - 1] if len(cl) >= ln else '')
        if not m:
            sys.exit('### data/%s :%d DOES NOT CARRY %s`s DISTANCE -- NOTHING WRITTEN' % (bank, ln, k))
        over[k] = (int(m.group(2)), 'relay data/%s :%d (cut, THE DISTANCE BEFORE %s, AFTER %s)' % ((bank, ln) + m.groups()))
    rows = []
    for i, l in enumerate(lt, 1):
        m = KROW.match(l)
        if m:
            k, now, src = m.group(1), int(m.group(5)), 'relay data/%s :%d' % (LICENSED_NOW, i)
            if k in over:
                now, src = over[k]
            rows.append(dict(kernel=k, line=i, row=l.strip(), now=now, source=src, table=m.group(6).split(' ')[0].replace('data/', '')))
    rows.sort(key=lambda r: -r['now'])
    top = [r for r in rows if r['now'] == rows[0]['now']] if rows and rows[0]['now'] > 0 else []
    steps = []
    for r in top:
        sl = [x for x in rdn(r['table']).split(NL) if x.startswith('### ### **%s: ROWS' % r['kernel'])]
        _k, n, mt, us, ov, ul = read_table_sum(sl[0] if sl else '')
        r.update(table_rows=n, overreaches=ov, any_kind=n - mt, summary=sl[0] if sl else '')
    cand = list(top)
    if len(cand) > 1:
        mo = max(r['overreaches'] for r in cand)
        steps.append('(i) THE OVERREACHES COUNTS: %s ; the greatest %d ; standing %s' % (
            ', '.join('%s %d' % (r['kernel'], r['overreaches']) for r in cand), mo, [r['kernel'] for r in cand if r['overreaches'] == mo]))
        cand = [r for r in cand if r['overreaches'] == mo]
    if len(cand) > 1:
        ma = max(r['any_kind'] for r in cand)
        steps.append('(ii) EQUAL OVERREACHES: THE ROWS OUTSIDE LICENSED/CITED OF ANY KIND: %s ; the greatest %d ; standing %s' % (
            ', '.join('%s %d' % (r['kernel'], r['any_kind']) for r in cand), ma, [r['kernel'] for r in cand if r['any_kind'] == ma]))
        cand = [r for r in cand if r['any_kind'] == ma]
    if len(cand) > 1:
        mr = max(r['table_rows'] for r in cand)
        steps.append('(iii) EQUAL OF ANY KIND: THE LARGER TABLE: %s ; the largest %d ; standing %s' % (
            ', '.join('%s %d rows' % (r['kernel'], r['table_rows']) for r in cand), mr, [r['kernel'] for r in cand if r['table_rows'] == mr]))
        cand = [r for r in cand if r['table_rows'] == mr]
    named = cand[0] if len(cand) == 1 else None
    L = ['b699 -- COMPONENT 2, (R309)(3): THE LICENSED TABLE`S NEXT DOCUMENT, b652`S ORDER AND b674`S TIE-BREAK RULE PRINTED BEFORE IT IS NAMED (%s)' % utc(), '',
         '### b652`S ORDER, VERBATIM FROM relay data/b652_ferry.txt :19:', '    ' + order, '',
         '### b674`S TIE-BREAK RULE, VERBATIM FROM relay data/b674_rules.txt :8-:11:'] + ['  ' + l for l in rl] + [
         '', '### THE KERNEL ROWS, VERBATIM (reading 3, relay data/%s, b648 -> b680 -> b690), A KERNEL CUT SINCE b690 BY ITS CUT BANK; rows are'
         % LICENSED_NOW, '### kernels: the count now | the row | the source of the count now, in descending count:']
    L += ['  %3d | %s | %s' % (r['now'], r['row'], r['source']) for r in rows]
    L += ['', '### THE ORDER APPLIED: the top count %s ; the kernels standing at it %s ; b674`s rule %s' % (
        rows[0]['now'] if rows else '### NONE', [r['kernel'] for r in top] or 'NONE',
        'NOT REACHED (one document at the top count, no tie)' if len(top) == 1 else 'REACHED: %d documents at the top count' % len(top))]
    L += ['### the tables of the kernels at the top count, their summary lines verbatim:'] + ['    relay data/%s : %s' % (r['table'], r['summary']) for r in top]
    L += ['### b674`s rule, step by step in its written order:'] + (['    ' + s for s in steps] or ['    NOT REACHED: no step taken'])
    L += ['', '### ### **THE NEXT DOCUMENT BY b652`S ORDER AND b674`S TIE-BREAK: %s (THE TOP COUNT %d, %d DOCUMENT%s AT IT ; %s).**' % (
        named['kernel'], named['now'], len(top), '' if len(top) == 1 else 'S', 'DECIDED AT STEP %s' % ['(i)', '(ii)', '(iii)'][len(steps) - 1] if steps else 'NO TIE')
        if named else '### ### **NO DOCUMENT NAMED -- RAISED.**']
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('%s_tie.txt' % ACT, L)
    put_json('%s_tie.json' % ACT, dict(at=utc(), rule=rl, order=order, rows=rows, steps=steps, named=named['kernel'] if named else None))
    print(NL.join(L))


# ================================================================================ COMPONENT 2: THE RUNS, THE PRINTS, THE QUOTATION SEARCH (b698's routes)
STD3 = R.STD3
dispatch, runstatus, _gh, _deps = R.dispatch, R.runstatus, R._gh, R._deps
read_runner_row = R.read_runner_row
READERS += ['read_runner_row']


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <note...>`: b698's route with b699's header -- the run read by its id; the artifact listed,
    downloaded by its id into memory, its sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory
    log's low and any STOP; the axioms output banked whole, every name of the list matched to one printed line, each terminal's axioms read
    against the standard three. data/b699_runner_<kernel>_<label>.txt, data/b699_axioms_<kernel>_<label>.txt, a row of data/b699_runner_rows.json."""
    import hashlib
    import io as _io
    import zipfile
    kernel, run_id, ref, label, note = a[0], int(a[1]), a[2], a[3], ' '.join(a[4:])
    repo = 'psinary-sketch/' + kernel
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=kernel, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None)
    L = ['b699 -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (kernel, label.upper(), utc()), '',
         '### the dispatch: %s ; the ref input %s' % (note, ref),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt'))]
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        L.append('### the artifact: id %s ; %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if digest and digest == sha else '### NOTHING READ FROM IT'))
        if digest and digest == sha:
            row['artifact_sha256'] = sha
            with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    row['mem_low'] = int(low[-1]) if low else None
    row['stopped'] = any(l.startswith('STOP ') for l in mem.split(NL))
    blog = T_.get('build.log', '')
    row['build_exit'] = T_.get('build_exit.txt', '').strip() or None
    row['errors'] = [l for l in blog.split(NL) if ': error' in l or l.startswith('error:')]
    ax = T_.get('axioms.txt', '').rstrip(NL)
    row['axioms_sha256'] = hashlib.sha256(ax.encode('utf-8')).hexdigest() if ax else None
    deps = _deps(ax)
    tg = [l.strip() for l in T_.get('print_targets.txt', '').split(NL) if l.strip()]
    printed = [n for n, _d in deps]
    unmatched = [n for n in tg if n not in printed]
    outside = [(n, d) for n, d in deps if not set(d) <= set(STD3)]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d:' % (row['build_exit'], len(row['errors']))] + ['    ' + l for l in row['errors'][:40]] + [
          '### the log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-8:]] + [
          '### the print step: the list (out/print_targets.txt) %d names ; terminals printed %d ; every name printed once %s ; axiom-free %d ; '
          'sorryAx %d ; outside the standard three %d ; refused %s' % (
              len(tg), len(deps), not unmatched and len(printed) == len(set(printed)) == len(tg), sum(1 for _n, d in deps if not d),
              sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), T_.get('axioms_refused.txt', '').strip() or 'NONE'),
          '### rows are terminals: name | the axioms printed | within the standard three:']
    L += ['  %-62s %s %s' % (n, d, 'STD3' if set(d) <= set(STD3) else '### OUTSIDE') for n, d in deps]
    L += ['  %-62s ### NOT PRINTED' % n for n in unmatched]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not unmatched and not outside
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; '
          'OUTSIDE THE STANDARD THREE %d ; GATE %s.**' % (
              run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']),
              len(deps), len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), row['gate'])]
    read_runner_row(row)
    put_txt('%s_runner_%s_%s.txt' % (ACT, kernel, label), L)
    if row['artifact_sha256']:
        put_txt('%s_axioms_%s_%s.txt' % (ACT, kernel, label), ax.split(NL) if ax else ['### EMPTY'])
        put_txt('%s_buildlog_%s_%s.txt' % (ACT, kernel, label), blog.rstrip(NL).split(NL))
    j = jl('%s_runner_rows.json' % ACT) if os.path.isfile(os.path.join(D, '%s_runner_rows.json' % ACT)) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('%s_runner_rows.json' % ACT, dict(rows=rows))
    print(NL.join(L[:14] + L[-3:]))


def prints(*a):
    """`prints <kernel> <before bank> <after bank>`: b698's route with b699's header -- the 'before' terminals' printed lines compared with the
    same names' lines in the 'after' bank, line for line by name; the raw axioms banks compared byte for byte beside. data/b699_prints_<kernel>.txt."""
    kernel, bb, ab = a[0], a[1], a[2]
    b, f = rdn(bb), rdn(ab)
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bd, fd = dict(_deps(b)), dict(_deps(f))
    diff = [(n, bd[n], fd.get(n)) for n in bd if fd.get(n) != bd[n]]
    new = [n for n in fd if n not in bd]
    L = ['b699 -- THE PRINTS OF %s BEFORE AND AFTER THE RE-CUT, BY NAME AND LINE FOR LINE (%s)' % (kernel, utc()), '',
         '### before: relay data/%s (%d terminals) ; after: relay data/%s (%d terminals) ; the two banks equal line for line: %s ; rows are the '
         'terminals that differ:' % (bb, len(bd), ab, len(fd), b == f)] + (['    %s : %s | %s' % d for d in diff] or ['    NONE']) + [
        '### the names printed after and not before: %d' % len(new)] + ['    %s %s' % (n, fd[n]) for n in new]
    L += ['', '### ### **BEFORE %d TERMINALS ; EACH PRINTED AFTER %s ; DIFFERING %d ; NEW %d ; EQUAL LINE FOR LINE %s.**' % (
        len(bd), all(n in fd for n in bd), len(diff), len(new), b == f)]
    put_txt('%s_prints_%s.txt' % (ACT, kernel), L)
    print(L[-1])


# ### the quotation search, data/b690_rules.txt row (2): one distinctive substring per removed or changed line of the cut (T7Labeling.lean
# ### :19-:20 at 3a7c889), checked to stand in its own removed line before it is searched; the second shape case-insensitive and shorter
QUOTE_SETS = {'quote_substrate': (('glide reflection φ : s ↦ 1 − s̄', 'quotient is a Möbius strip'), ('glide reflection', 'is a möbius strip'))}


def quote(*a):
    """`quote <kernel dir> <base> <tip> <bank stem>`: b698's route with b699's header and needles -- every line the cut removes or changes read,
    one needle assigned to each by containment and refused where a removed line carries none or a needle stands in no removed line; each needle
    searched with git grep -n -F at the tip across the kernel's whole tracked tree, in two shapes; every hit printed with its quoting line and
    entered as a residue; the control at the base. data/b699_<stem>.txt (.json)."""
    kd, base, tip, stem = a[0], a[1], a[2], a[3]
    needles, wide = QUOTE_SETS[stem]
    d = g(kd, 'diff', '--unified=0', base, tip)
    removed = [l[1:].rstrip(chr(13)) for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    removed = [l for l in removed if l.strip()]
    rows, unassigned = [], []
    for l in removed:
        nd = [n for n in needles if n in l]
        if not nd:
            unassigned.append(l)
        rows.append(dict(line=l, needle=nd[0] if nd else None))
    unused = [n for n in needles if not any(n in r['line'] for r in rows)]
    if unassigned or unused:
        sys.exit('### A REMOVED LINE WITHOUT A NEEDLE %s OR A NEEDLE IN NO REMOVED LINE %s -- NOTHING WRITTEN' % (unassigned, unused))
    for r in rows:
        w = [n for n in wide if n.lower() in r['line'].lower()]
        r['wide'] = w[0] if w else None
    wu = [n for n in wide if not any(n.lower() in r['line'].lower() for r in rows)]
    if any(r['wide'] is None for r in rows) or wu:
        sys.exit('### THE SECOND SHAPE: A REMOVED LINE WITHOUT A NEEDLE OR A NEEDLE IN NO REMOVED LINE %s -- NOTHING WRITTEN' % wu)
    hits = []
    for r in rows:
        out = g(kd, 'grep', '-n', '-F', r['needle'], tip, '--')
        r['hits'] = [x for x in out.split(NL) if x.strip()]
        out2 = g(kd, 'grep', '-n', '-i', '-F', r['wide'], tip, '--')
        r['hits_wide'] = [x for x in out2.split(NL) if x.strip()]
        hits += [(r['wide'], h) for h in r['hits_wide']]
    L = ['b699 -- THE QUOTATION SEARCH BEFORE THE MERGE, data/b690_rules.txt row (2), OVER %s (%s)' % (os.path.basename(kd), utc()), '',
         '### the cut: git diff %s..%s ; the lines it removes or changes %d ; one needle each, checked to stand in its own removed line; each searched' % (
             base, tip, len(rows)),
         '### with git grep -n -F at the tip %s across the kernel`s whole tracked tree. Rows are removed lines: needle | hits (file:line: the quoting' % tip,
         '### line):']
    for r in rows:
        L.append('  %-44s | %d hit(s) ; case-insensitive %-26r %d hit(s) | removed: %s' % (r['needle'], len(r['hits']), r['wide'], len(r['hits_wide']),
                                                                                    r['line'].strip()[:100]))
        L += ['      %s' % h for h in r['hits_wide']]
    q = sorted(set(h.split(':', 2)[1] + ':' + h.split(':', 3)[2] for _n, h in hits))
    ctl = [(r['needle'], len([x for x in g(kd, 'grep', '-n', '-F', r['needle'], base, '--').split(NL) if x.strip()]),
            len([x for x in g(kd, 'grep', '-n', '-i', '-F', r['wide'], base, '--').split(NL) if x.strip()])) for r in rows]
    L += ['', '### THE CONTROL: each needle at the base %s, where the removed line stands (needle ; case-exact hits ; case-insensitive hits):' % base]
    L += ['  %-44s ; %d ; %d' % c for c in ctl]
    L += ['### the control %s' % ('FIRES FOR EVERY NEEDLE IN BOTH SHAPES' if all(c[1] and c[2] for c in ctl) else '### DOES NOT FIRE FOR EVERY NEEDLE')]
    L += ['', '### THE QUOTING LINES, DISTINCT (file:line): %s' % (', '.join(q) or 'NONE'),
          '### the yields: the case-exact shape %d hit(s) on %d line(s) ; the case-insensitive shape %d hit(s) on %d line(s)' % (
              sum(len(r['hits']) for r in rows), len(set(h.split(':', 3)[1] + ':' + h.split(':', 3)[2] for r in rows for h in r['hits'])),
              len(hits), len(q)),
          '', '### ### **REMOVED OR CHANGED LINES %d ; NEEDLES SEARCHED %d IN TWO SHAPES ; QUOTING LINES %d -- EACH ENTERED AS A RESIDUE.**' % (
              len(rows), len(rows), len(q))]
    put_txt('%s_%s.txt' % (ACT, stem), L)
    put_json('%s_%s.json' % (ACT, stem), dict(at=utc(), kernel=kd, base=base, tip=tip, rows=rows, hits=[list(h) for h in hits]))
    print(NL.join(L))


# ================================================================================ COMPONENTS 2-3: THE CELLS, data/b698_rules.txt ROW (1) (b698's route, generalized)
ROSTER_ALL = 'b672_roster_read.json'
_gen = R._gen


def cells(*a):
    """`cells dry <kernel> <stem>`: data/b699_roster_<stem>.json -- b672's roster with the tables whose kernels name <kernel> alone, every key
    carried -- and data/b699_correspondence_dry_<stem>.txt: the generator run dry (full) on that roster and on b672's whole roster, nothing
    written by it; every cell naming <kernel> it would change printed. `cells run <stem>` (on the author's word "run"): the generator run on
    the one-kernel roster, its diff banks under b699_correspondence_run_<stem>; the pages' git diff banked in
    data/b699_correspondence_page_diff_<stem>.txt."""
    if a and a[0] == 'run':
        stem = a[1]
        ro = '%s_roster_%s.json' % (ACT, stem)
        before = g(PP, 'rev-parse', 'HEAD').strip()
        if g(PP, 'status', '--porcelain', '--untracked-files=no').strip():
            sys.exit('### PLACE-papers HAS TRACKED CHANGES -- NOTHING RUN')
        paths = [t['path'] for t in jl(ro)['tables']]
        rc, out = _gen('run', ro, '--diff', '%s_correspondence_run_%s' % (ACT, stem))
        changed = [l for l in g(PP, 'diff', '--name-only').split(NL) if l.strip()]
        diff = g(PP, 'diff', '-U0', '--', *paths)
        L = ['%s -- THE CELLS REGENERATED BY THE GENERATOR ALONE, ON THE AUTHOR`S WORD "run", data/b698_rules.txt ROW (1) (%s)' % (ACT, utc()), '',
             '### the run: `python -X utf8 -B tools/correspondence_gen.py run data/%s --diff %s_correspondence_run_%s` (exit %d), PLACE-papers at %s ; '
             'files changed by it: %s' % (ro, ACT, stem, rc, before[:7], changed or 'NONE'), '', '### the pages` diff (git diff -U0), verbatim:']
        L += ['    ' + l for l in diff.rstrip(NL).split(NL)]
        L += ['', '### the generator`s own verdict line: ' + ([l for l in out.split(NL) if l.startswith('### ### **TABLES')] or ['### NOT READ'])[-1]]
        cl = diff.count('\n-|')
        ok = bool(changed) and set(changed) <= set(paths) and cl == diff.count('\n+|')
        L += ['', '### ### **THE CELLS REGENERATED (%s): FILES CHANGED %d ; TABLE LINES CHANGED %d ; THE ROSTER`S PAGES ALONE %s.**' % (
            stem, len(changed), cl, ok)]
        put_txt('%s_correspondence_page_diff_%s.txt' % (ACT, stem), L)
        print(NL.join(L))
        return
    kernel, stem = a[1], a[2]
    ro = '%s_roster_%s.json' % (ACT, stem)
    roster = jl(ROSTER_ALL)
    some = [t for t in roster['tables'] if kernel in (t.get('kernels') or [])]
    if some:
        sub = dict((k, v) for k, v in roster.items() if k != 'tables')
        sub['tables'] = some
        sub['b699'] = 'b672`s roster (relay data/b672_roster_read.json) with the tables naming %s alone, every key carried, under (R309)' % kernel
        put_json(ro, sub)
        rc1, o1 = _gen('dry', ro, 'full')
    else:
        ro, rc1, o1 = '(none: no table of b672`s roster names %s in its kernels; no one-kernel roster written)' % kernel, 0, ''
    rc2, o2 = _gen('dry', ROSTER_ALL, 'full')
    tables_naming = sum(1 for t in roster['tables'] if kernel in (t.get('kernels') or []))
    pick = lambda o, h: list(dict.fromkeys(l for l in o.split(NL) if l.startswith(h) and ' | ' not in l))   # noqa: E731
    diff1 = [l for l in o1.split(NL) if re.match(r'^    \S+ :\d+ \| ', l)]
    diff2 = [l for l in o2.split(NL) if re.match(r'^    \S+ :\d+ \| ', l)]
    L = ['%s -- THE CORRESPONDENCE GENERATOR RUN DRY OVER THE CELLS NAMING %s, data/b698_rules.txt ROW (1) (%s)' % (ACT, kernel, utc()), '',
         '### the runs, nothing written by either: `python -X utf8 -B tools/correspondence_gen.py dry data/%s full` (exit %d) -- b672`s roster with '
         'the %d table(s) whose kernels name %s alone (%s, every key carried) -- and the same on b672`s whole roster data/%s (exit %d), the local '
         'clones` tags read, no remote call.' % (ro, rc1, len(some), kernel, ', '.join(t['doc'] for t in some), ROSTER_ALL, rc2), '',
         '### THE DIFF ON THE ONE-KERNEL ROSTER (rows are cells changed; document :line ; column ; kernel ; old ; new), verbatim:']
    L += diff1 or ['    NONE']
    L += ['### its verdict line, verbatim:'] + (pick(o1, '### ### **TABLES') or ['    (no run: no table)'])
    L += ['', '### THE DIFF ON THE WHOLE ROSTER, verbatim:']
    L += diff2 or ['    NONE']
    L += ['### its verdict line, verbatim:'] + pick(o2, '### ### **TABLES')
    mine = list(dict.fromkeys(l for l in diff1 + diff2 if '| %s |' % kernel in l))   # ### distinct cells: the two runs print the same cell twice
    L += ['', '### ### **ROSTER TABLES NAMING %s %d ; CELLS NAMING IT THE GENERATOR WOULD CHANGE %d ; ON THE ONE-KERNEL ROSTER CELLS CHANGED %d ; ON '
              'THE WHOLE ROSTER %d ; NOTHING WRITTEN.**' % (kernel, tables_naming, len(mine), len(diff1), len(diff2))]
    put_txt('%s_correspondence_dry_%s.txt' % (ACT, stem), L)
    print(NL.join(L))


# ================================================================================ COMPONENT 2: THE CUT BANK, (R309)(3) (b697's route, carried)
CUT = dict(kernel='SIDE-substrate-cluster', table='b647_table_SIDE-substrate-cluster.txt', base='3a7c889', tip='903d79d', tag='v0.4.1',
           prior='v0.4', workflow='cebec19', targets='3a7c889', before=39558356179, after=39558461398, branch='recut-substrate-cluster-b699')
# ### the wider stems' hits, read by hand after the search (git grep -n -i at the tip, glide / s-bar / quotient / klein_trivium): each a source
# ### attribution or the cut's own successor line, none restating the retired claim
WIDE_READ = (('README.md', 21, 'the 𝕋₇ row of the README`s table naming klein_trivium.pdf as the source -- an attribution, not the claim'),
             ('SIDESubstrateCluster/Substrate.lean', 36, 'a citation of klein_trivium.pdf -- an attribution, not the claim'),
             ('SIDESubstrateCluster/T7Labeling.lean', 14, 'the header`s opening attribution "per klein_trivium.pdf", kept by the ACTION'),
             ('SIDESubstrateCluster/T7Labeling.lean', 19, 'the cut`s own successor line'),
             ('SIDESubstrateCluster/T7Labeling.lean', 23, 'the cut`s own successor line'))
PINNED = ('phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md', 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM_v0_2.md')


def _norm(t):
    return ' '.join(t.replace('--', ' ').replace('—', ' ').split())


def cut(*a):
    """data/b699_cut.txt (.json): the document named by data/b699_tie.txt; the commits on its main (the workflow and the print list alone, the
    cut on recut-substrate-cluster-b699, the merge, the tag); the before and after runs and the prints; the distance before and after by the
    b670 method -- each non-MATCHES row of its b647 table read whole; its ACTION here a RETIRE TO ERRATA with no replacement text, so the
    retired sentences as the row's STATED field carries them are searched, whitespace normalized, in the file at the base and at the merge, the
    row met where they no longer stand; the quotation search's quoting lines and the wider stems' hits each read; the generator's dry reading
    and the author's word on it; the roster-currency row for reading 4."""
    k = CUT['kernel']
    kd = 'D:/' + k
    mainc = g(kd, 'rev-parse', '--short=7', 'main').strip()
    tb = rdn(CUT['table'])
    blocks = re.findall(r'(?ms)^  (%s@\w+:(\S+):(\d+)) \| (OVERREACHES|UNDERSTATES|UNLICENSED) \|.*?\n      STATED   (.*?)$.*?\n      ACTION   (.*?)$'
                        % re.escape(k), tb)
    rows = []
    for rid, f, ln, verdict, stated, action in blocks:
        m = re.search(r'(carries the glide reflection .*? The quotient is a Möbius strip\.)', stated)
        retired = m.group(1) if m else ''
        src = _show(kd, mainc, f) or ''
        src0 = _show(kd, CUT['base'], f) or ''
        rows.append(dict(row=rid, file=f, line=int(ln), verdict=verdict, action=action.strip(), retired=retired,
                         applied=bool(retired) and _norm(retired) not in _norm(src), applied_at_base=bool(retired) and _norm(retired) not in _norm(src0),
                         stands_at_base=bool(retired) and _norm(retired) in _norm(src0)))
    if len(rows) != 1 or not rows[0]['retired'] or not rows[0]['stands_at_base']:
        sys.exit('### THE ROW OR ITS RETIRED SENTENCES ARE NOT AS READ (%d rows ; %r) -- NOTHING WRITTEN' % (len(rows), rows[0]['retired'][:60] if rows else ''))
    before = sum(1 for r in rows if not r['applied_at_base'])
    after = sum(1 for r in rows if not r['applied'])
    qv = _vl_('%s_quote_substrate.txt' % ACT)
    q = jl('%s_quote_substrate.json' % ACT)
    qlines = sorted(set((h.split(':')[1], int(h.split(':')[2])) for _n, h in q.get('hits') or []))
    wide = [l for l in g(kd, 'grep', '-n', '-i', '-e', 'glide', '-e', 's̄', '-e', 'quotient', '-e', 'klein_trivium', CUT['tip'], '--').split(NL) if l.strip()]
    wkeys = [(x.split(':')[1], int(x.split(':')[2])) for x in wide]
    if sorted(wkeys) != sorted((f, n) for f, n, _r in WIDE_READ):
        sys.exit('### THE WIDER STEMS` HITS ARE NOT THE LINES READ BY HAND %s -- NOTHING WRITTEN' % wkeys)
    tie_v = _vl_('%s_tie.txt' % ACT)
    cd = _vl_('%s_correspondence_dry_substrate.txt' % ACT)
    tag_peel = g(kd, 'rev-parse', CUT['tag'] + '^{commit}').strip()
    prior_peel = g(kd, 'rev-parse', CUT['prior'] + '^{commit}').strip()
    tag_msg = g(kd, 'tag', '-l', '--format=%(contents:subject)', CUT['tag']).strip()
    mt, tt = g(kd, 'rev-parse', mainc + '^{tree}').strip(), g(kd, 'rev-parse', CUT['tip'] + '^{tree}').strip()
    parents = g(kd, 'rev-list', '--parents', '-n', '1', mainc).split()
    pv = _vl_('%s_prints_%s.txt' % (ACT, k))
    pins = [(p, i + 1, l) for p in PINNED for i, l in enumerate((_show(PP, 'HEAD', p) or '').split(NL)) if l.startswith('| SIDE-substrate-cluster v0.4 = `06b61c3`')]
    pin_files = sorted(set(re.findall(r'`(SIDESubstrateCluster/\w+\.lean)`', ' '.join(l for _p, _i, l in pins))))
    untouched = not [f for f in pin_files if f in g(kd, 'diff', '--name-only', '06b61c3', mainc)]
    L = ['b699 -- COMPONENT 2, (R309)(3): THE RE-CUT OF %s, ITS DISTANCE, ITS RESIDUES (%s)' % (k, utc()), '',
         '### the document: %s, named by b652`s order alone, one document at the top count, b674`s rule printed and not reached (relay '
         'data/b699_tie.txt: %s)' % (k, tie_v.strip('#* ')),
         '### the commits on its main: the workflow %s alone (SIDE-simplicity`s form ff395c5, its cache step removed for a Mathlib-free kernel), the'
         % CUT['workflow'],
         '### print list %s alone (the 11 declarations of T7Labeling.lean), pushed by push_gated (relay data/b699_substrate_main_push_out.txt); the' % CUT['targets'],
         '### cut %s on %s (comments only: T7Labeling.lean :19-:20, the two sentences the ACTION retires), pushed alone by push_gated`s branch mode'
         % (CUT['tip'], CUT['branch']),
         '### named --scratch (relay data/b699_substrate_cut_push_out.txt); the merge %s by --no-ff, its parents %s, the merged tree %s the built tree'
         % (mainc, ' '.join(p[:7] for p in parents[1:]), mt[:12]),
         '### %s (%s); the tag %s peeled to %s, its message %r naming the prior tag %s = %s, the highest version tag and the one the papers cite'
         % (tt[:12], 'EQUAL' if mt == tt else '### DIFFER', CUT['tag'], tag_peel[:12], tag_msg, CUT['prior'], prior_peel[:7]),
         '### (relay data/b699_substrate_merge_push_out.txt); v0.1.0, the deposit seal, peels to the same commit as v0.4',
         '### the runs: before %d at main %s, after %d at the tip %s (relay data/b699_runner_%s_before.txt, _after.txt); the prints: %s' % (
             CUT['before'], CUT['targets'], CUT['after'], CUT['tip'], k, pv.strip('#* ')),
         '', '### THE DISTANCE BY THE b670 METHOD: each non-MATCHES row of relay data/%s; its ACTION is RETIRE TO ERRATA, with no replacement' % CUT['table'],
         '### text, so the retired sentences as the row`s STATED field carries them are searched, whitespace normalized, in the file at the base',
         '### %s and at the merge %s, the row met where they no longer stand:' % (CUT['base'], mainc)]
    L += ['  %s | %s | RETIRED SENTENCES STAND AT THE BASE %s ; AT THE MERGE %s | %s' % (r['row'], r['verdict'], r['stands_at_base'], not r['applied'],
                                                                                    r['retired']) for r in rows]
    L += ['', '### THE RESIDUES (data/b690_rules.txt row (2); relay data/b699_quote_substrate.txt, two shapes): %s' % qv.strip('#* '),
          '### the quoting lines: %s' % (', '.join('%s :%d' % x for x in qlines) or 'NONE'),
          '### the matcher widened once, the bare stems (glide, s-bar, quotient, klein_trivium) case-insensitive across the tracked tree at the tip, '
          '%d hits, each read by hand:' % len(wide)]
    L += ['  W-%d  %s :%d | %s' % (i, f, n, r) for i, (f, n, r) in enumerate(WIDE_READ, 1)]
    L += ['### none restates the retired claim: QUOTING LINES 0', '',
          '### THE CORRESPONDENCE CELLS (relay data/b699_correspondence_dry_substrate.txt, the generator run dry, data/b698_rules.txt row (1)): %s' % cd.strip('#* '),
          '### on the author`s word (data/b699_author_answers.txt), nothing written: no generator cell names the kernel. The pinned citation rows',
          '### outside the roster, read and named as read, not as residues -- each pinned at v0.4 = 06b61c3, its file %s by the cut since the pin:'
          % ('untouched' if untouched else '### TOUCHED')]
    L += ['  PIN  %s :%d | %s' % (p, i, l[:150]) for p, i, l in pins]
    L += ['', '### THE ROSTER-CURRENCY ROW FOR READING 4 (b700), on the author`s word: THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md (and its _v0_2 copy)',
          '### carries kernel citations and is not in b672`s roster, so the generator cannot see it; for b700`s census, no roster change this act.',
          '', '### ### **%s RE-CUT: THE DISTANCE BEFORE %d, AFTER %d ; TAG %s ; %s ; QUOTING LINES %d ; CELLS NAMING THE KERNEL 0, NOTHING WRITTEN ; '
          'PINNED ROWS %d STANDING.**' % (k, before, after, CUT['tag'], 'PRINTS EQUAL' if 'EQUAL LINE FOR LINE True' in pv else '### PRINTS NOT EQUAL',
                                         len(qlines), len(pins))]
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('%s_cut.txt' % ACT, L)
    put_json('%s_cut.json' % ACT, dict(at=utc(), kernel=k, rows=rows, before=before, after=after, residues=[list(x) for x in qlines], main=mainc,
                                       tip=CUT['tip'], tag=CUT['tag'], tag_peel=tag_peel, merged_tree=mt, built_tree=tt, run_before=CUT['before'],
                                       run_after=CUT['after'], pins=[[p, i] for p, i, _l in pins], wide=[list(x[:2]) for x in WIDE_READ]))
    print(NL.join(L))


# ================================================================================ COMPONENT 3: THE PARTNER COPY, (R309)(4) (b698's onecopy route, generalized)
ONECOPY_H = ('*Appended 2026-10-21 by b699 beneath `W-ORD-ONE-COPY` (:14386, its trigger re-written at :14450; b698’s reading at :15296), under '
             '`(R309)`(4) and the author’s word on the archimedean cells -- THE PATHS PARTNER COPY, THIS ACT’S READING:*')


def _table_diff(t, rev):
    import correspondence_gen as CG
    import difflib
    A = (_show(PP, rev, t['path']) or '').split(NL)
    B = (_show(PP, rev, t['partner']) or '').split(NL)
    fa, fb = CG.find_table(A, t), CG.find_table(B, t)
    if isinstance(fa, str) or isinstance(fb, str):
        sys.exit('### A TABLE NOT FOUND AT %s: %r ; %r -- NOTHING WRITTEN' % (rev, fa, fb))
    ta, tb = A[fa[0]:fa[1]], B[fb[0]:fb[1]]
    rows = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
        if tag == 'equal':
            continue
        for k in range(max(i2 - i1, j2 - j1)):
            ia, ib = (i1 + k if i1 + k < i2 else None), (j1 + k if j1 + k < j2 else None)
            rows.append(dict(op=tag, a=(fa[0] + ia + 1) if ia is not None else None, b=(fb[0] + ib + 1) if ib is not None else None,
                             ta=ta[ia] if ia is not None else '', tb=tb[ib] if ib is not None else ''))
    return fa, fb, rows


def onecopy(*a):
    """data/b699_onecopy.txt: the PATHS_TO_THE_CRITICAL_LINE table and its partner copy's, each found by the generator's own find_table with
    the roster's anchor (data/b699_roster_archimedean.json), at the commit before the generator's write and at PLACE-papers HEAD after it; the
    lines that differ, each with its line in both files, the count re-taken against the roster's stored field; the partner's SIDE-archimedean
    line read whole; and `onecopy land [dry]` -- the reading entered beneath W-ORD-ONE-COPY through the guarded landing."""
    t = jl('%s_roster_archimedean.json' % ACT)['tables'][0]
    head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    wrote = g(PP, 'log', '-1', '--format=%h', '--', t['path']).strip()
    prior = g(PP, 'rev-parse', '--short=7', wrote + '~1').strip()
    fa, fb, rows = _table_diff(t, 'HEAD')
    _fa0, _fb0, rows0 = _table_diff(t, prior)
    B = (_show(PP, 'HEAD', t['partner']) or '').split(NL)
    pl = [(i + 1, l) for i, l in enumerate(B) if '| SIDE-archimedean v' in l]
    if len(pl) != 1:
        sys.exit('### THE PARTNER DOES NOT CARRY ONE SIDE-archimedean LINE (%d) -- NOTHING WRITTEN' % len(pl))
    stored = t.get('partner_lines_differing')
    if 'land' in a:
        n = len(rows)
        body = (' the generator, run on the author’s word at b699 on a one-table roster (relay data/b699_roster_archimedean.json), wrote '
                'PATHS_TO_THE_CRITICAL_LINE_v0_7.md :285 alone -- the three SIDE-archimedean cells held since b693, kernel v0.1.0 to v0.1.1, '
                'profile, status -- and left its partner copy PATHS_TO_THE_CRITICAL_LINE.md unwritten; the partner’s :%d still carries '
                'SIDE-archimedean v0.1.0. Read line by line at PLACE-papers %s after the write, by the generator’s own table finder (relay '
                'data/b699_onecopy.txt), the two copies’ Correspondence tables differ in %d lines -- %d at %s before the write: the copy’s %s '
                'against the partner’s %s. The roster’s stored field partner_lines_differing reads %s (b672’s); the count here is re-taken, not '
                'carried. The reading is this act’s; neither copy is moved by it and the one copy of record stays the order’s question. Status '
                'OPEN.' % (pl[0][0], head, n, len(rows0), prior, ', '.join(':%s' % r['a'] for r in rows), ', '.join(':%s' % r['b'] for r in rows), stored))
        land([('OPEN_TRAILS.md', ONECOPY_H, NL + ONECOPY_H + body + NL)], '%s_onecopy_line.json' % ACT, 'onecopy', entry=14386,
             check=[('OPEN_TRAILS.md', 14386, '**`W-ORD-ONE-COPY`**'), ('OPEN_TRAILS.md', 14450, '**`W-ORD-ONE-COPY`**')], dry='dry' in a)
        return
    L = ['%s -- COMPONENT 3, (R309)(4) AND THE AUTHOR`S WORD ON "run": THE PATHS PARTNER COPY`S DIFFERING LINES, READ AT PLACE-papers HEAD %s (%s)' % (
        ACT, head, utc()), '',
         '### the tables: %s :%d-:%d and its partner %s :%d-:%d, each found by tools/correspondence_gen.py`s find_table with the roster`s anchor;'
         % (t['path'], fa[0] + 1, fa[1], t['partner'], fb[0] + 1, fb[1]),
         '### compared line by line (SequenceMatcher, autojunk off), at HEAD %s and at %s, the commit before the generator`s write %s. Rows are'
         % (head, prior, wrote),
         '### differing lines at HEAD: op | the copy`s line | the partner`s line | the two texts.', '',
         '### the partner`s SIDE-archimedean line, whole: %s :%d' % (t['partner'], pl[0][0]), '    ' + pl[0][1], '']
    for r in rows:
        L += ['  %-8s | :%-4s | :%-4s' % (r['op'], r['a'] or '-', r['b'] or '-'), '      copy:    ' + r['ta'], '      partner: ' + r['tb']]
    L += ['', '### ### **THE TWO TABLES DIFFER IN %d LINES AT HEAD, %d BEFORE THE WRITE (the roster`s stored field: %s) ; NEITHER COPY MOVED BY '
              'THIS READING.**' % (len(rows), len(rows0), stored)]
    put_txt('%s_onecopy.txt' % ACT, L)
    print(NL.join(L))


# ================================================================================ COMPONENT 3: W-ORD-H2-BRIDGE-THEOREM, (R309)(5)
BRIDGE_H = ('*Appended 2026-10-21 by b699 beneath `W-ORD-H2-BRIDGE` (:10257, annotated at :15200, its open object named at :15294), under '
            '`(R309)`(5) -- THE ORDER **`W-ORD-H2-BRIDGE-THEOREM`**, PRICED AND NOT RUN:*')
BRIDGE_B = (' the translation at binder 1 between residue_irreducible’s object and h2_sign’s, and a statement between the two faces under it, '
            'as a Lean statement to be compiled on a branch of SIDE-explicit-formula with SIDE-lv-conservation’s statement restated there '
            '(SIDE-explicit-formula’s lakefile requires no SIDE-lv-conservation). Priced in relay data/b699_bridge_plan.txt, its 14 binders each '
            'printed with the translation it needs before any statement: at binder 1 no translation object to object stands in either kernel -- '
            'no map from a test window k to a sequence lam_A -- and the two faces join at the level of their targets, through '
            'RiemannHypothesis, at lam := LiCoeff, by two theorems SIDE-explicit-formula v0.34 already compiles: h2_sign_iff_rh (Seam.lean :101) '
            'and register4_positivity_liCoeff_iff_rh (PageConverses.lean :32), the latter beside the face’s own discharge of its last binder, '
            'register4_positivity_liCoeff_imp_rh (ResidueDischarge.lean :41). The expected statement S1, h2_sign ↔ Register4_positivity '
            'LiCoeff, an equivalence of the two faces’ targets and not a translation of objects, DERIVES expected; S2, h2_sign giving the face’s '
            'third conjunct, an implication empty beyond S1; a join without RH between the faces not priced, for want of a window k_n in classK '
            'with W(k_n) = λ_n in either kernel and of the classK widening it would need. The price: one module on a branch of '
            'SIDE-explicit-formula, one dispatch at its tip; nothing compiled this act. Raised for the author’s word at b701’s ruling beside '
            'W-ORD-EPSTEIN-COUNT-LEAN and the classK widening to W1 ∪ W3. Status OPEN.')


def bridge(*a):
    p = rdn('%s_bridge_plan.txt' % ACT)
    if 'BINDERS 14 PRINTED WITH THEIR TRANSLATIONS BEFORE ANY STATEMENT' not in p or 'NOTHING COMPILED' not in p:
        sys.exit('### THE PLAN BANK DOES NOT CARRY ITS VERDICT -- NOTHING WRITTEN')
    land([('OPEN_TRAILS.md', BRIDGE_H, NL + BRIDGE_H + BRIDGE_B + NL)], '%s_bridge_line.json' % ACT, 'bridge', entry=10257,
         check=[('OPEN_TRAILS.md', 10257, '(2) **`W-ORD-H2-BRIDGE`**'), ('OPEN_TRAILS.md', K.B698_BRIDGE_LINE, 'beneath `W-ORD-H2-BRIDGE`')],
         dry='dry' in a)


# ================================================================================ THE LATE ROUTES (b698's, carried with b699's names)
import b698_worklist as K698       # noqa: E402
import edit_route as ER            # noqa: E402
import b633_record as R3           # noqa: E402
SESSION, SUBAGENTS = R.SESSION, R.SUBAGENTS
# ### the previous act's window: b698 ran in this same session (c677eaf2) -- the same-session form (b695's): b698's capture from the call that
# ### combined its post-push parts to this act's anchor
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = 'b698', K.SESSION_ID, K698.ANCHOR
R.PREV_SESSION_PATH, R.PREV_SUBAGENTS = SESSION, SUBAGENTS


def prev_capture():
    """G-EDIT-ROUTE's window over the previous act, same-session form: b698's capture AFTER ITS POST-PUSH SUITE -- every command of this session
    from the call that combined b698's post-push parts into data/b698_checks_postpush.txt to the first user line carrying (R309)'s anchor."""
    rows = ER.capture(SESSION, K698.ANCHOR, SUBAGENTS)
    first = [r['ts'] for r in rows if 'b698_checks_postpush' in r['cmd'] and '--combine' in r['cmd']]
    end = R._anchor_ts(K.ANCHOR)
    if not first or not end:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE OR THIS ACT`S ANCHOR IS NOT IN THE SESSION -- NOTHING READ')
    out = [dict(r, src='b698 %s' % r['src']) for r in rows if first[0] <= r['ts'] < end]
    for i, r in enumerate(out):
        r['n'] = 'p%d' % (i + 1)
    return out


R.prev_capture = prev_capture
capture, reads, edit_route_offences = R.capture, R.reads, R.edit_route_offences
QUOTED, REDIRECT_NULL, REDIRECT_ANY, PIPE_FILTER, PY_PRINT_READ, MOVE_OR_DELETE, SED_KIND = (
    R.QUOTED, R.REDIRECT_NULL, R.REDIRECT_ANY, R.PIPE_FILTER, R.PY_PRINT_READ, R.MOVE_OR_DELETE, R.SED_KIND)


def commands(*a):
    """b698's route with b699's names in its bank text: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's
    window (same session), the local lean reading (N1), the dispatches, the detached runs, sed, the redirects, the pipes, the one-line programs,
    the moves and deletes by shape, the outbound requests. data/b699_commands.txt (.json)."""
    rows = R.capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = edit_route_offences(rows)
    prev = prev_capture()
    phits = edit_route_offences(prev)
    sh_ = [r for r in rows if r['tool'] in ('Bash', 'PowerShell')]
    lean = [r for r in sh_ if R.local_lean(r['cmd'])]
    mv = [r for r in sh_ if MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in sh_ if re.search(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py dispatch\b(?![^\n]*\bdry\b)', QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in sh_ if (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
    seds = [r for r in sh_ if R.sed_cmd(r['cmd'])]
    nulls = [r for r in sh_ if REDIRECT_NULL.search(QUOTED.sub('""', r['cmd']))]
    redir = [r for r in sh_ if REDIRECT_ANY.search(QUOTED.sub('""', r['cmd']))]
    pipes = [r for r in sh_ if PIPE_FILTER.search(QUOTED.sub('""', r['cmd']))]
    anypipe = [r for r in sh_ if '|' in QUOTED.sub('""', r['cmd']).replace('||', '')]
    pyreads = [r for r in sh_ if PY_PRINT_READ.search(r['cmd'])]
    shapes = [(r['n'],) + R.delete_shape(r['cmd']) for r in mv if R.delete_shape(r['cmd'])[0]]
    chained = [r['n'] for r in mv if R.delete_shape(r['cmd'])[0] and R.chained_after(r['cmd'])]
    halves = dict((r['n'], len([x for x in re.split(r'&&|\|\||;|\|', QUOTED.sub('""', r['cmd'])) if x.strip()])) for r in mv)
    ob = R.outbound()
    L = ['%s -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % (ACT, utc()), '',
         '### the source: the seat`s session %s from its first user line carrying %r, with its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (b698, this same session %s, from its post-push combine to this act`s '
              'anchor): %d commands from %s, its offences printed whole (%d):' % (K.SESSION_ID[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES, ONE PER TREE STATE (relay data/b699_dispatches.json) (%d):' % len(disp)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN, BY THEIR TEXT OR THE TOOL`S run_in_background PARAMETER (%d):' % len(
        detach)] + (['  #%d %s%s' % (r['n'], '[run_in_background] ' if r.get('bg') else '', r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT ONTO /dev/null, read outside quoted strings (%d):' % len(nulls)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], r['cmd'].split(NL)[0][:200]) for r in nulls] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT OF ANY STREAM, read outside quoted strings (%d):' % len(redir)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in redir] or ['  NONE'])
    L += ['', '### THE COMMANDS PIPING INTO A SHELL FILTER (head, tail, wc, grep and the like), read outside quoted strings (%d):' % len(pipes)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in pipes] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A PIPE OF ANY KIND, read outside quoted strings (%d):' % len(anypipe)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in anypipe] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT RUN AN INTERPRETER`S ONE-LINE PROGRAM (python -c), each its first line (%d):' % len(pyreads)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:220]) for r in pyreads] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R309)(6) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
              'nothing chained after): ' + ('; '.join('#%d deletes %s, halves %d, globs %s, variables %s, chained after %s' % (
                  n, d, halves.get(n, 0), gl or 'none', vs or 'none', n in chained) for n, d, gl, vs in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git AND gh (web searches, subagent prompts and fetches), each with the author`s identifiers found '
              'in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    good = sum(1 for n, d, gl, vs in shapes if len(d) == 1 and not gl and not vs and n not in chained)
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; REDIRECTS ONTO /dev/null %d ; '
              'REDIRECTS OF ANY STREAM %d ; PIPES INTO A SHELL FILTER %d ; PIPES OF ANY KIND %d ; ONE-LINE PROGRAMS %d ; MOVE OR DELETE COMMANDS %d ; '
              'BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(nulls), len(redir), len(pipes), len(anypipe), len(pyreads), len(mv), good,
                  len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    if 'dry' in a:
        print(L[-1])
        return
    put_txt('%s_commands.txt' % ACT, [l.replace('\r', '') for l in L])
    put_json('%s_commands.json' % ACT, dict(at=utc(), anchor=K.ANCHOR, rows=rows,
                                           offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                           prev=dict(act='b698', session=K.SESSION_ID, rows=len(prev),
                                                     offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                           local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                           seds=[r['n'] for r in seds], null_redirects=[r['n'] for r in nulls], redirects=[r['n'] for r in redir],
                                           pipes=[r['n'] for r in pipes], any_pipes=[r['n'] for r in anypipe], py_programs=[r['n'] for r in pyreads],
                                           moves_deletes=[r['n'] for r in mv],
                                           delete_shapes=[dict(n=n, deletes=d, globs=gl, variables=vs, halves=halves.get(n), chained=n in chained)
                                                          for n, d, gl, vs in shapes],
                                           outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
local_lean, delete_shape, chained_after, seal_hashes, root_banks_state = R.local_lean, R.delete_shape, R.chained_after, R.seal_hashes, R.root_banks_state
read_score_row, read_head, _defect_short, _anchor_ts = R.read_score_row, R.read_head, R._defect_short, R._anchor_ts
READERS += ['read_score_row', 'read_head']


_KERNS_698 = R._kerns


def _kerns():
    return _KERNS_698() + ['SIDE-substrate-cluster']


R._kerns = _kerns


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('%s_kernels_face.json' % ACT, dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-substrate-cluster read after its merge and tag v0.4.1; no kernel written after this read)' % len(ks))


R.ROOT_EXCLUDE = re.compile(r'^b699_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                            r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                            r'commands|mirror.*|close_sentence|read_calls)\.?(txt|json|md|jsonl|)$')
root_banks, rootbanks, root, root_arm, table_final = R.root_banks, R.rootbanks, R.root, R.root_arm, R.table_final


def _standing():
    return sorted(set(R._g2_of(os.path.join(ROOT, *K.B698_FACE.split('/')))) - set(K698.ACT_ARMS))


R._standing = _standing


def standing(*a):
    """the standing arms b699 carries: b698's face's (G2) arms less b698's act arms (R264)(2); printed only."""
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


def armsecs(*a):
    st = _standing()
    rows, phases, runs = [], {}, {}
    for p in K.PARTS:
        j = jl('%s_arm_seconds_%s.json' % (ACT, p))
        phases[p] = j.get('phases') or {}
        runs[p] = j.get('run_secs')
        for nm, s in (j.get('arms') or {}).items():
            rows.append(dict(arm=nm, part=p, secs=s, standing=nm in st))
    srows = sorted([r for r in rows if r['standing']], key=lambda r: -r['secs'])
    miss = sorted(set(st) - set(r['arm'] for r in srows))
    L = ['%s -- THE STANDING ARMS` SECONDS AT HEAD, BY PART, FROM THE PRE-RUN (%s): the per-part seconds of the six parts' % (ACT, utc()), '',
         '### the source: data/%s_arm_seconds_<part>.json, written by tools/%s_checks.py at its pre-run, each arm`s seconds the sum of its' % (ACT, ACT),
         '### three readings (LIVE on the sources, NEG on a copy, POS on a mutated copy); each part`s run seconds and its phases -- the sources',
         '### built once for all its arms -- printed beside, not divided among them. standing-b2 carries no arm and is clocked by its run alone.',
         '### Rows are standing arms, slowest first:']
    L += ['  %-46s %-11s %8.3f s' % (r['arm'], r['part'], r['secs']) for r in srows]
    L += ['', '### THE PARTS` SECONDS: ' + ' | '.join('%s %s s' % (p, runs[p]) for p in K.PARTS),
          '### THE PARTS` PHASES (seconds): ' + ' | '.join('%s: %s' % (p, '; '.join('%s %.0f' % kv for kv in ph.items())) for p, ph in phases.items()),
          '### the standing arms not clocked: %s' % (miss or 'NONE'),
          '', '### ### **STANDING ARMS CLOCKED %d OF %d ; THE THREE SLOWEST %s ; THEIR SECONDS SUMMED %.1f.**' % (
              len(srows), len(st), ', '.join('%s (%s, %.2f s)' % (r['arm'], r['part'], r['secs']) for r in srows[:3]) or 'NONE',
              sum(r['secs'] for r in srows))]
    put_txt('%s_arm_seconds.txt' % ACT, L)
    put_json('%s_arm_seconds.json' % ACT, dict(at=utc(), rows=srows, phases=phases, run_secs=runs, standing=len(st), clocked=len(srows), missing=miss,
                                              slowest=[r['arm'] for r in srows[:3]]))
    print(L[-1])


# ================================================================================ THE SCORES: (N1)-(N5) OF (R309)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and commits and not the entry; the entry reads the scorer's bank. `scores`
# ### writes data/b699_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there and is read at the close.
NK, SK, SCORE_KEYS = R.NK, R.SK, R.SCORE_KEYS
N5_RELAY_DATA = ('act_roots.txt', 'b698_closing_push_out.txt', 'b675_corrigenda.txt')
N5_RELAY_TOOLS = ()
FACE = os.path.join(D, 'b699_registration_2026-10-21.txt')
FACE_REL = 'data/b699_registration_2026-10-21.txt'
R.FACE, R.FACE_REL = FACE, FACE_REL
SUB = 'D:/SIDE-substrate-cluster'
PATHS_PAGE = 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md'
_iso_epoch, _git_ct, _files_of, _ledger_adds, _amended_after, _one_git_write = (
    R._iso_epoch, R._git_ct, R._files_of, R._ledger_adds, R._amended_after, R._one_git_write)


def _s_scores():
    """the seat's (S1)-(S3), b698's readings with b699's bank names."""
    import collections
    TF, RA_ = jl('%s_table_final.json' % ACT), jl('%s_root_arm.json' % ACT)
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b699_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b699_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def _n1():
    """N1: no lean process on this host; the runner dispatched once per tree state (the re-cut's two runs, before and after)."""
    cm = jl('%s_commands.json' % ACT)
    dj = jl('%s_dispatches.json' % ACT).get('rows') or []
    trees = [r.get('tree') for r in dj]
    ok = bool(cm) and not cm.get('local_lean') and len(dj) == len(cm.get('dispatches') or []) == 2 and len(set(trees)) == len(trees) \
        and all(r.get('kernel') == 'SIDE-substrate-cluster' for r in dj)
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches %s (relay data/b699_dispatches.json: %d row(s), %s, trees '
        'distinct %s): the re-cut`s before-run at main and after-run at the cut`s tip, one per tree state (relay data/b699_commands.txt, %d '
        'commands read)' % (cm.get('local_lean') if cm else 'unread', cm.get('dispatches') if cm else 'unread', len(dj),
                            ', '.join('%s %s at %s' % (r.get('kernel'), r.get('label'), (r.get('ref') or '')[:7]) for r in dj) or '-',
                            len(set(trees)) == len(trees), len(cm.get('rows') or [])))


def _n2():
    """N2: the tie-break rule and the table rows printed from banks before the document is named; the archimedean dry run printed before any
    page write."""
    t = rdn('%s_tie.txt' % ACT).split(NL)
    ir = next((i for i, l in enumerate(t) if l.startswith('### b674`S TIE-BREAK RULE, VERBATIM')), None)
    it = next((i for i, l in enumerate(t) if l.startswith('### THE KERNEL ROWS, VERBATIM')), None)
    iname = next((i for i, l in enumerate(t) if l.startswith('### ### **THE NEXT DOCUMENT')), None)
    verb = rdn('b674_rules.txt').split(NL)[7:11]
    rule_ok = ir is not None and all(('  ' + v) in t for v in verb)
    first = ir is not None and it is not None and iname is not None and ir < it < iname
    dry = rdn('%s_correspondence_dry_archimedean.txt' % ACT)
    dry_at = _iso_epoch((re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', dry.split(NL)[0]) or [None, ''])[1])
    page_ct = _git_ct(PP, g(PP, 'log', '-1', '--format=%h', '--', PATHS_PAGE).strip())
    ok = rule_ok and first and bool(dry_at) and bool(page_ct) and dry_at < page_ct and 'NOTHING WRITTEN' in dry
    return ('HELD' if ok else 'REFUTED'), (
        'relay data/b699_tie.txt: b674`s rule verbatim (:%s), the kernel rows (:%s), the document named after both (:%s): %s, the rule equal to '
        'data/b674_rules.txt :8-:11 %s; the archimedean dry run (relay data/b699_correspondence_dry_archimedean.txt, at %s) before the page`s '
        'commit (%s): %s' % (ir + 1 if ir is not None else '-', it + 1 if it is not None else '-', iname + 1 if iname is not None else '-', first,
                             rule_ok, R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(dry_at)) if dry_at else '-',
                             R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(page_ct)) if page_ct else '-',
                             bool(dry_at) and bool(page_ct) and dry_at < page_ct))


def _n3():
    """N3: the distance after at or below the distance before; the prints before and after equal line for line; the quotation search before
    the merge with its hit count printed; no Correspondence cell written by hand."""
    cj = jl('%s_cut.json' % ACT)
    pv = R._vl('%s_prints_SIDE-substrate-cluster.txt' % ACT)
    qj = jl('%s_quote_substrate.json' % ACT)
    q_at = _iso_epoch(qj.get('at'))
    m_ct = _git_ct(SUB, cj.get('main') or 'x')
    qv = R._vl('%s_quote_substrate.txt' % ACT)
    pc = g(PP, 'log', '--format=%h', '%s..HEAD' % K.PRE_PP, '--', PATHS_PAGE).split()
    gen = rdn('%s_correspondence_page_diff_archimedean.txt' % ACT)
    hand_free = len(pc) == 1 and _files_of(PP, pc[0]) == [PATHS_PAGE] and 'THE ROSTER`S PAGES ALONE True' in gen \
        and g(PP, 'diff', '-U0', K.PRE_PP, pc[0], '--', PATHS_PAGE).count('\n+|') == 1
    ok = bool(cj) and cj.get('after') is not None and cj['after'] <= cj['before'] and 'EQUAL LINE FOR LINE True' in pv and bool(q_at) and bool(m_ct) \
        and q_at < m_ct and re.search(r'QUOTING LINES \d+', qv) is not None and hand_free
    return ('HELD' if ok else 'REFUTED'), (
        'the distance by the b670 method (relay data/b699_cut.json): before %s, after %s; the prints (relay data/b699_prints_SIDE-substrate-cluster.txt): '
        '%s; the quotation search at %s before the merge`s commit at %s: %s, its count printed (%s); the Correspondence cell written by the '
        'generator alone (PLACE-papers commits on the page since the act began %s, the page alone, one table line, relay '
        'data/b699_correspondence_page_diff_archimedean.txt): %s' % (cj.get('before'), cj.get('after'), pv.strip('#* ')[:120], qj.get('at'), m_ct,
                                                                     bool(q_at) and bool(m_ct) and q_at < m_ct,
                                                                     (re.search(r'QUOTING LINES \d+', qv) or [''])[0], pc, hand_free))


def _n4():
    """N4: the bridge plan prints each of the 14 binders with the translation it needs before any statement; nothing compiled for it."""
    p = rdn('%s_bridge_plan.txt' % ACT)
    i1, i2 = p.find('== 1. THE BINDERS'), p.find('== 2. THE EXPECTED STATEMENTS')
    blk = p[i1:i2] if 0 <= i1 < i2 else ''
    rows = re.findall(r'^  (binder \d+|conclusion) +\|', blk, re.M)
    trans = blk.count('| THE TRANSLATION:')
    dj = jl('%s_dispatches.json' % ACT).get('rows') or []
    ef = [r for r in dj if r.get('kernel') == 'SIDE-explicit-formula']
    t0 = _iso_epoch(_anchor_ts(K.ANCHOR) or '')
    ef_moved = [l for l in g(K.EF_DIR, 'log', '--format=%ct', '-5', 'main').split() if l.isdigit() and t0 and int(l) > t0]
    ok = 0 <= i1 < i2 and len(rows) == 14 and trans == 14 and not ef and not ef_moved and 'NOTHING COMPILED' in p
    return ('HELD' if ok else 'REFUTED'), (
        'relay data/b699_bridge_plan.txt: the binders` section before the statements` (%s before %s): %s; rows %d (13 binders and the conclusion), '
        'each with its translation (%d); dispatches at SIDE-explicit-formula %d; its main moved since the act began: %s' % (
            i1, i2, 0 <= i1 < i2, len(rows), trans, len(ef), ef_moved or 'NONE'))


def _n5():
    import rule_arms as RA
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    t0, moved, tags = R._kernels_moved()
    moved_beyond = [m for m in moved if m[0] != 'SIDE-substrate-cluster']
    tags_beyond = [t for t in tags if t != ('SIDE-substrate-cluster', 'v0.4.1')]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b699_', x) and x not in N5_RELAY_TOOLS]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b699_|audit_b699_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA) or x in N5_RELAY_TOOLS)]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    arms_added = sorted(set(RA.NAMES) - set(K.STANDING_ADDED) - set(R._g2_of(os.path.join(ROOT, *K.B698_FACE.split('/')))))
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock) + _amended_after(SUB, lock)) if lock else []
    ob = jl('%s_commands.json' % ACT).get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    wf = (_show(SUB, 'main', '.github/workflows/build-module.yml') or '').lower()
    wf_ident = [w for w in R.IDENT if w in wf]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    chained = [d['n'] for d in (jl('%s_commands.json' % ACT).get('delete_shapes') or []) if d.get('chained')]
    gw_ok, gw_note = _one_git_write()
    cj = jl('%s_cut.json' % ACT)
    word = [m[1] for m in moved if m[0] == 'SIDE-substrate-cluster']
    ok = k_ok and not moved_beyond and not tags_beyond and not pp_beyond and not kinds_beyond and not shared_tools and not differ \
        and not arms_added and not amended and not ident and not wf_ident and not pat and not chained and gw_ok and bool(word) and bool(cj)
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; kernel main commits '
            'since the act began beyond SIDE-substrate-cluster`s re-cut (its commits %s): %s; tags made beyond SIDE-substrate-cluster v0.4.1: %s; no '
            'standing arm added (tools/rule_arms.py`s names beyond b698`s face): %s; shared tools edited: %s; sealed tools not agreeing: %s; '
            'commits amended after the seal: %s; deletes with anything chained after: %s; one git write per message (G-RULE-ONE-GIT-WRITE`s '
            'reading: %s): %s; PLACE-papers beyond the two ledgers and the regenerated page: %s; relay files of a kind beyond the act`s banks and '
            'tools, the table, the root list, b698`s push-out bank and the corrigenda bank`s rows: %s; "patent" in the lines written: %s; outbound '
            'requests other than git and gh %d, an identifier of the author in %s; in the kernel`s workflow file %s' % (
                K.DRAFT, k_ok, word or 'NONE', moved_beyond or 'NONE', tags_beyond or 'NONE', arms_added or 'NONE', shared_tools or 'NONE',
                differ or 'NONE', amended or 'NONE', chained or 'NONE', gw_note, gw_ok, pp_beyond or 'NONE', kinds_beyond or 'NONE', pat or 'NONE',
                len(ob), [r['line'] for r in ident] or 'NONE', wf_ident or 'NONE'))


def scores(*a):
    """`scores [dry]` writes data/b699_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b699_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('%s_scores_close.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('%s_scores.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))


_sv, scores_line = R._sv, R.scores_line


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
def TRAIL_HEAD():
    return ('### b699 — lane two, act one hundred and twenty-six, the re-cut act under (R309): b698 at its weight; the undeclared failure and the '
            'post-root rewrite by corrigendum; SIDE-substrate-cluster re-cut; the SIDE-archimedean cells regenerated; the bridge priced')


R.TRAIL_HEAD = TRAIL_HEAD
_calls, _rl_lines = R._calls, R._rl_lines


def _figs():
    """the figures the title and the entry carry, each read from its bank."""
    cj = jl('%s_cut.json' % ACT)
    pdiff = R._vl('%s_correspondence_page_diff_archimedean.txt' % ACT)
    oc = re.search(r'DIFFER IN (\d+) LINES AT HEAD, (\d+) BEFORE THE WRITE \(the roster`s stored field: (\d+)\)', R._vl('%s_onecopy.txt' % ACT))
    co = jl('%s_corrigendum.json' % ACT)
    pv = R._vl('%s_prints_SIDE-substrate-cluster.txt' % ACT)
    np_ = re.search(r'BEFORE (\d+) TERMINALS', pv)
    return dict(before=cj.get('before', '-'), after=cj.get('after', '-'), tag=cj.get('tag') or '-', merge=(cj.get('main') or '-')[:7],
                cells='regenerated' if 'THE ROSTER`S PAGES ALONE True' in pdiff else 'held', onecopy=oc.group(1) if oc else '-',
                stored=oc.group(3) if oc else '-', corr=co.get('entry_line') or '-', missing=[m['hash'][:8] for m in co.get('missing') or []],
                prints=np_.group(1) if np_ else '-')


def _title():
    f = _figs()
    return ('## SIDE-substrate-cluster re-cut: %s row outside LICENSED/CITED to %s, %s; the SIDE-archimedean cells at PATHS :285 %s; the bridge at '
            'binder 1 priced; b698’s undeclared failure by corrigendum' % (f['before'], f['after'], f['tag'], f['cells']))


def _finding_text():
    """the FINDINGS entry, composed before the root: its scores line from the scores bank alone (data/b686_rules.txt row (1)); the root is
    carried by the trail record."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    br = _rl_lines('%s_bridge_line.json' % ACT) + ['-']
    oc = _rl_lines('%s_onecopy_line.json' % ACT) + ['-']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'SIDE-substrate-cluster’s one row outside LICENSED/CITED, the T7Labeling.lean header’s glide reflection on the critical strip with a Möbius '
         'quotient, is retired to the errata: the map as written fixes the critical line pointwise and its quotient of the strip is a half-strip, '
         'and the strip’s construction is klein_trivium.pdf’s own statement, compiled nowhere in the kernel. The %s printed terminals are '
         'unchanged by the cut. The three SIDE-archimedean cells held since b693 are written by the generator, and the bridge at binder 1 is '
         'priced: the two faces join through RH at λ := LiCoeff by two theorems SIDE-explicit-formula already compiles, and no translation of '
         'objects stands in either kernel.' % f['prints'], '',
         '*Filed at b699 on the author’s ruling `(R309)` and the author’s words at its prompts; %d question%s put. Banks: relay `data/b699_tie.txt`, '
         '`data/b699_cut.txt`, `data/b699_quote_substrate.txt`, `data/b699_prints_SIDE-substrate-cluster.txt`, '
         '`data/b699_correspondence_dry_substrate.txt`, `data/b699_correspondence_dry_archimedean.txt`, '
         '`data/b699_correspondence_page_diff_archimedean.txt`, `data/b699_onecopy.txt`, `data/b699_bridge_plan.txt`, `data/b699_corrigendum.txt`.*' % (
             n_ans, '' if n_ans == 1 else 's'), '',
         '**The re-cut** (`(R309)`(3)): b652’s order named SIDE-substrate-cluster alone at the top count, b674’s rule printed verbatim before the '
         'naming and not reached. Its kernel had no workflow; SIDE-simplicity’s was carried with its cache step removed, the eleven declarations '
         'of T7Labeling.lean listed, built before the cut at main and after it at the branch tip, both DERIVES, the prints equal line for line. '
         'The cut retired the header’s two sentences, comments only; the quotation search before the merge found no quoting line, its matcher '
         'widened once and every hit read by hand. Merged at `%s`, tagged %s naming v0.4; the distance %s to %s by the b670 method, the retired '
         'sentences standing at the base and gone at the merge. No table of the generator’s roster names the kernel; on the author’s word '
         'nothing was written, and the paper whose pinned rows cite it at v0.4 stands as read, named for reading 4.' % (
             f['merge'], f['tag'], f['before'], f['after']), '',
         '**The archimedean cells** (`(R309)`(4), data/b698_rules.txt row (1), on the author’s word): the generator alone wrote '
         'PATHS_TO_THE_CRITICAL_LINE :285 on a one-table roster -- kernel v0.1.0 to v0.1.1, the profile printed, DERIVES UNREFRESHED to DERIVES. '
         'The partner copy was read line by line: its table differs in %s lines, re-taken against the stored %s, entered beneath W-ORD-ONE-COPY '
         '(OPEN_TRAILS :%s).' % (f['onecopy'], f['stored'], oc[0]), '',
         '**The bridge** (`(R309)`(5)): W-ORD-H2-BRIDGE-THEOREM entered beneath W-ORD-H2-BRIDGE (OPEN_TRAILS :%s), its 14 binders each printed '
         'with the translation it needs before any statement. The expected statement, h2_sign ↔ Register4_positivity LiCoeff, composes '
         'h2_sign_iff_rh and register4_positivity_liCoeff_iff_rh -- an equivalence of the two faces’ targets, not a map of objects; a join '
         'without RH between them is not priced. One dispatch; nothing compiled.' % br[0], '',
         '**The corrigendum** (`(R309)`(2)): b698’s G-NOTHING-RAN-AHEAD, failing before and after its push and undeclared, entered by its two '
         'commits, relay `%s` and `%s`; the answers bank’s bytes equal to the root’s row, the root unchanged, its write time later; the ONE-COPY '
         'figure 6 as stored and 18 as counted (FINDINGS :%s). b698 at its weight (FINDINGS :%s).' % (
             (f['missing'] + ['-', '-'])[0], (f['missing'] + ['-', '-'])[1], f['corr'], c1_[0]), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed, each raised before the component that cites '
         'it; %d answer check%s, each before its answer was acted on.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b647’s table for the kernel, b674’s tie rule, b690’s quotation rule '
         'and b698’s rule (1) against the cut and the held cells; b698’s dominance reading against the bridge’s binders. It is re-read by b700’s '
         'reading 4, which takes the roster-currency row and the two partner copies’ differing lines; and by b701’s research act on the author’s '
         'word among the bridge, the Epstein count and the classK widening. It strengthens the programme’s offering of a located clause: one '
         'more kernel header held to what it compiles, three cells brought to their prints, and the bridge’s open object priced as a statement '
         'between targets.', '',
         '**Carried to:** W-ORD-H2-BRIDGE-THEOREM (priced, one dispatch); W-ORD-ONE-COPY (the PATHS and SIMPLICITY partner copies); b700 (the '
         'roster-currency row, the regularity bank, the defects by class); `W-ORD-EPSTEIN-COUNT-LEAN`; the classK widening to W1 ∪ W3; the draft '
         'held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the prior tag read as v0.4, the highest version tag and the one the papers cite, v0.1.0 the deposit seal at the same commit; '
              '(2) the b670 distance measured for a RETIRE ACTION by its retired sentences, as the row`s STATED field carries them; (3) the cut '
              'reflowed so the unchanged line :21 stays byte for byte; (4) the quotation matcher widened once and its five hits read by hand; '
              '(5) the bridge`s binder 1 joined through RH by two compiled theorems, the direct join left unpriced; (6) the corrigendum carried '
              'from b695`s tool on the author`s answer')


def _trail_text():
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    br = _rl_lines('%s_bridge_line.json' % ACT) + ['-']
    oc = _rl_lines('%s_onecopy_line.json' % ACT) + ['-']
    f = _figs()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R309) ratified.** (1) b698 at its weight. (2) The corrigendum. (3) The re-cut. (4) The archimedean cells. (5) The bridge priced. '
             '(6) The branches. (7) The readfirst bank. (8) The draft held at v5. (9) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b698`s weight), :%s (the corrigendum), :%s (the entry); OPEN_TRAILS :%s (beneath W-ORD-ONE-COPY), :%s '
             '(W-ORD-H2-BRIDGE-THEOREM); this record.' % (c1_[0], f['corr'], fj.get('entry_line'), oc[0], br[0]), '',
             '**Act root:** b699 `%s` (previous `%s`, b698`s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s (relay data/b699_author_answers.txt); none after the root.' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The re-cut:** SIDE-substrate-cluster, %s to %s, %s at `%s`; the prints equal; no quoting line (relay data/b699_cut.txt).' % (
                 f['before'], f['after'], f['tag'], f['merge']), '',
             '**The cells:** PATHS_TO_THE_CRITICAL_LINE :285 %s by the generator alone; the partner copy`s %s differing lines read, %s stored (relay '
             'data/b699_correspondence_page_diff_archimedean.txt, data/b699_onecopy.txt).' % (f['cells'], f['onecopy'], f['stored']), '',
             '**The bridge:** W-ORD-H2-BRIDGE-THEOREM priced at one dispatch, nothing compiled (relay data/b699_bridge_plan.txt).', '',
             '**The kernels:** SIDE-substrate-cluster alone written -- its workflow and print list, the cut, its merge and tag v0.4.1; the runner '
             'dispatched once per tree state, before and after; no lean or lake on this host.', '',
             '**The corrigendum:** b698`s face, G-NOTHING-RAN-AHEAD by its two commits, the answers bank`s rewrite and the ONE-COPY figure (FINDINGS '
             ':%s; relay data/b675_corrigenda.txt rows (11)-(13)).' % f['corr'], '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b699_closing.txt).', '',
             '**The open orders:** `W-ORD-H2-BRIDGE-THEOREM` (priced, :%s); `W-ORD-ONE-COPY`; `W-ORD-B518-FLOAT` (the reading act b700); '
             '`W-ORD-EPSTEIN-COUNT-LEAN` and the classK widening (b701, on the author`s word).' % br[0], '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b699_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


desk = R.desk


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('%s_scores.json' % ACT, '%s_findings.json' % ACT, '%s_trail.json' % ACT, '%s_act_root.json' % ACT))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R309).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b699_citation_check.txt), step zero (data/b699_ferry.txt, data/b699_readfirst.txt, '
         'data/b699_stepzero.txt, data/b699_tests_stepzero.txt, data/b699_rowgen_stepzero.txt, data/b699_branches.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b698`s weight FINDINGS :%s ; the corrigendum FINDINGS :%s (data/b699_corrigendum.txt) ; the corrigenda bank`s rows' % (
             c1_[0], f['corr']),
         '### COMPONENT 2 : the re-cut of SIDE-substrate-cluster (data/b699_tie.txt, data/b699_cut.txt, data/b699_quote_substrate.txt, '
         'data/b699_prints_SIDE-substrate-cluster.txt, data/b699_correspondence_dry_substrate.txt) ; N2 %s ; N3 %s' % (S['N2'][0], S['N3'][0]),
         '### COMPONENT 3 : the archimedean cells (data/b699_correspondence_dry_archimedean.txt, data/b699_correspondence_page_diff_archimedean.txt, '
         'data/b699_onecopy.txt) and the bridge (data/b699_bridge_plan.txt) ; N4 %s' % S['N4'][0],
         '### COMPONENT 4 : the carry-time reading (data/b699_tool_repairs.txt), the dry-run steps (data/b699_reg_gate.txt), the seal '
         '(data/b699_seal_hashes.json), the suite in six parts, the per-part seconds (data/b699_arm_seconds.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 5 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('%s_components.txt' % ACT, L)
    print(NL.join(L[2:]))


def findings(*a):
    t, e = _finding_text()
    e = R.conv(e)
    dry = 'dry' in a
    cells_, fired = R.screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells_)
        return
    if not os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = R._land_one(FIND, t, e, '%s_findings.json' % ACT, dict(title=t))
    j = jl('%s_findings.json' % ACT)
    j['entry_line'] = ln
    put_json('%s_findings.json' % ACT, j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = R.conv(_trail_text())
    dry = 'dry' in a
    cells_, fired = R.screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells_)
        return
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = R._land_one(OT, TRAIL_HEAD(), e, '%s_trail.json' % ACT, {})
    print('  OPEN_TRAILS record :%s' % ln)


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them, converted by conv and run
    through the screens their landing runs, the needles the face names read in each; DRY-RUN STEP : CLEAN only when both screens are quiet and
    every needle is found. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = R.conv(text)
        print('  %s (the screens):' % which)
        cells_, fired = R.screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = R._face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells_ and not fired and nd and not miss
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells_ or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


gatebanks = R.gatebanks
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
mbuild, mroot, mverify = R.mbuild, R.mroot, R.mverify


def mbank(*a):
    import zipfile
    import hashlib as _hl
    import b616_record as R6
    z = zipfile.ZipFile(R.ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    commits = sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', NL.join(l for l in ls if '|' in l))))
    zb = open(R.ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('%s_mirror_verify.txt' % ACT)
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['%s -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % (ACT, utc()),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (R.ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b699 (the last export b698`s, D:/MY-DOwnloads/mirror-refresh-2026-10-21-b698.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=R.ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


# ================================================================================ THE CARRY-TIME READING (the ferry's Component 4)
REPAIR_ROWS = [      # ### (text, carried tool, carried function, this act's tool)
    ('(1) tools/b699_record.py prev_capture, carried from tools/b698_record.py prev_capture (sealed at b698) -- ANSWERS the session: b698 ran in '
     'this act`s own session (c677eaf2), so the previous act`s window is the same-session form (b695`s): b698`s capture from the call that '
     'combined its post-push parts to this act`s anchor, not to the session`s end.', 'b698_record.py', 'prev_capture', 'b699_record.py'),
    ('(2) tools/b699_citation.py answer, carried from tools/b698_citation.py answer -- ANSWERS this act`s kernels: b698`s widening of b682`s '
     'REPOS carried and extended to SIDE-archimedean, SIDE-simplicity and SIDE-substrate-cluster; b682`s tool unedited.', 'b698_citation.py',
     'answer', 'b699_citation.py'),
    ('(3) tools/b699_record.py cells, carried from tools/b698_record.py cells -- ANSWERS (R309)(3)-(4): one route for any kernel`s cells, a roster '
     'of the tables naming it; where no table names it the dry reading banked as a result (NONE) and not refused; the cells counted distinct, '
     'the two runs printing the same cell twice (caught in the archimedean dry run`s first print, 6 against 3, and re-run before any write).',
     'b698_record.py', 'cells', 'b699_record.py'),
    ('(4) tools/b699_record.py cut, carried from tools/b697_record.py cut -- ANSWERS the row`s ACTION, RETIRE TO ERRATA with no replacement text: '
     'the b670 distance read by the retired sentences as the row`s STATED field carries them, standing at the base and gone at the merge.',
     'b697_record.py', 'cut', 'b699_record.py'),
    ('(5) tools/b699_corrigendum.py compose, carried from tools/b695_corrigendum.py compose on the author`s answer to citation miss 2 -- ANSWERS '
     '(R309)(2): b698`s failure G-NOTHING-RAN-AHEAD read as the arm reads it, recomputed from the logs; the answers bank`s bytes against the '
     'root`s row; the ONE-COPY figure.', 'b695_corrigendum.py', 'compose', 'b699_corrigendum.py'),
]


def repairs(*a):
    """data/b699_tool_repairs.txt: the carry-time repairs, each with the defect or order it answers, its diff written by this route (difflib
    over the carried function's source at relay HEAD against this act's). No shared tool is edited by this act."""
    import difflib
    L = ['%s -- THE CARRY-TIME READING: THE REPAIRS (%s)' % (ACT, utc()), '',
         '### rows are repairs with the defect or order they answer: the tool and its part ; what it answers ; the form. Each diff beneath its',
         '### row, written by this route (difflib over the function`s source, relay HEAD`s carried tool against this act`s).', '']
    n = 0
    for text, src_tool, fn, new_tool in REPAIR_ROWS:
        old = R._fn_src(_show(ROOT, 'HEAD', 'tools/' + src_tool) or '', fn).split(NL)
        new = R._fn_src(rd(os.path.join(T, new_tool)), fn).split(NL)
        d = list(difflib.unified_diff(old, new, 'tools/%s %s (sealed)' % (src_tool, fn), 'tools/%s %s (this act)' % (new_tool, fn), lineterm=''))
        n += len(d)
        L += ['  ' + text, ''] + ['      ' + x for x in d] + ['']
    L += ['### ### **REPAIRS %d ; NO SHARED TOOL EDITED ; DIFF LINES %d ; NO FROZEN BANK EDITED.**' % (len(REPAIR_ROWS), n)]
    if 'dry' not in a:
        put_txt('%s_tool_repairs.txt' % ACT, L)
    print(L[-1])


def _vl_(name):
    return ([x for x in rdn(name).split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, c1=c1, tie=tie, dispatch=dispatch, runstatus=runstatus,
              runner=runner, prints=prints, quote=quote, cells=cells, cut=cut, onecopy=onecopy, bridge=bridge, commands=commands, reads=reads,
              kernels=kernels, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final, standing=standing, armsecs=armsecs,
              scores=scores, desk=desk, components=components, findings=findings, trail=trail, drycheck=drycheck, gatebanks=gatebanks,
              mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank, repairs=repairs)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b699_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
