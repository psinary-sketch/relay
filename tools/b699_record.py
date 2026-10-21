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
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show

READERS = ['read_branch_row']
read_branch_row = R.read_branch_row


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


def _vl_(name):
    return ([x for x in rdn(name).split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, c1=c1, tie=tie, dispatch=dispatch, runstatus=runstatus,
              runner=runner, prints=prints, quote=quote, cells=cells, cut=cut, onecopy=onecopy, bridge=bridge)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b699_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
