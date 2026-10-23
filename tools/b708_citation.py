# -*- coding: utf-8 -*-
"""b708_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b708's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (0be08567, a NEW session: b707 ran in aa198636; the anchor (R318)'s line is unique in it); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b708 and its commit reach widened to the kernels, with b706's repair carried
### (a bare eight-hex token that a bank's row or a kernel's lakefile names as a sha256 or a rev is not read as a commit); the `word` route is
### b694's. Routes: `check [dry]` -> data/b708_citation_check.txt (.json) ; `ferry` -> data/b708_ferry_scan.txt ; `answer <needle>` /
### `word <needle>` -> the check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b708 from b707_citation.py's form; this tool writes only the banks named above.
"""
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b677_citation as C   # noqa: E402  ### the helpers, imported unchanged
import b708_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID


def continuation_sessions():
    """the act's continuation sessions (K.SESSIONS_AFTER, b671's form) as transcript paths, read by b677's helpers after the seat's session."""
    return tuple('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid for sid, _anc in K.SESSIONS_AFTER)


C.SESSIONS_AFTER = continuation_sessions()
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = K.ANCHOR, K.TAIL
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HEAD_QUOTE = 'b707 closed: relay 2507e99c, PLACE-papers 95dc6f6; suite 129 of 137; root 6fe154f9820e7d9e\u2026; 3 prompts answered; 9 defects'
RULING_NAV_AT_STEPZERO = 4       # ### (R318)(1): "nine defects (a)-(i), four the navigator`s at step zero" -- read against the bank`s owners
ONSET_ROW = re.compile(r'^  (band|rho0) \| (\S+)\s+\| a (\S+) \+- (\S+) \| .*?\| lambda (\S+) \+- (\S+), (\S+) \+- (\S+) \| ([A-Z ]+?BEYOND ITS BOUND)', re.M)


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def lines_of(path):
    return (rd(path) or '').split(NL)


def first(L, needle, start=1):
    return next((i + 1 for i, l in enumerate(L) if i + 1 >= start and needle in l), 0)


def at(L, n):
    return L[n - 1] if n and len(L) >= n else ''


def _ws(s):
    return ''.join((s or '').split())


def _remote_heads(repo):
    out = g(repo, 'ls-remote', '--heads', 'origin')[1] or ''
    return dict((l.split('\t', 1)[1].strip(), l.split('\t', 1)[0]) for l in out.split(NL) if '\t' in l)


def _defect_row(L, letter):
    """the text of a lettered defect row, from its letter to the next letter's row."""
    s = first(L, '    (%s) ' % letter)
    if not s:
        return 0, ''
    e = next((i for i in range(s, len(L)) if re.match(r'^    \([a-z]\) ', L[i]) or L[i].startswith('###')), len(L))
    return s, ' '.join(x.strip() for x in L[s - 1:e])


def _jl(name):
    try:
        return json.loads(rd(os.path.join(D, name)) or '{}')
    except Exception:
        return {}


def _onset_rows(text):
    out = {}
    for m in ONSET_ROW.finditer(text):
        out[(m.group(1), m.group(2))] = dict(a=m.group(3), lmin=m.group(5), reading=m.group(9).strip())
    return out


def _near(x, s, places):
    try:
        return round(float(x), places) == round(float(s), places)
    except Exception:
        return False


def _tree(repo, ref):
    return [x for x in (g(repo, 'ls-tree', '-r', '--name-only', ref)[1] or '').split(NL) if x.strip()]


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    ot, fi = lines_of(OT), lines_of(FI)
    EF, LV = K.EF_DIR, K.LV_DIR
    # ### the ferry's read-first list, by existence
    for f in ('data/b707_closing.txt', 'data/b707_defects.txt', 'data/b707_onset.txt', 'data/b707_onset_hashes.txt', 'data/b707_onset_controls.txt',
              'data/b707_port.txt', 'data/b707_registrations.txt', 'data/b705_registrations.txt', 'data/b707_tool_repairs.txt',
              'data/b707_closing_push_out.txt', 'tools/mirror_prevbuild.json', K.B707_FACE, 'data/b704_probe.txt', 'data/b704_probe.json',
              K.B704_PROBE_OUT, K.NODES_B704, 'data/b706_cells_reread.txt', 'data/b704_cells_reach.txt', 'data/b670_licensed_table.txt',
              'data/%s' % K.CUT_TABLE, 'data/b646_table_Silence_of_Foundations.txt', 'data/b646_table_Third_Identity_Element.txt', 'data/b704_tie.txt',
              'data/b702_tie.txt', 'data/b704_cut.txt', 'data/b704_cut.json', 'data/b704_quote.txt', 'data/b674_rules.txt', 'data/b705_rules.txt',
              'data/b690_rules.txt', 'data/b680_rules.txt', 'data/b675_rules.txt', 'data/b684_rules.txt', 'data/b686_rules.txt', 'data/b692_rules.txt',
              'data/b694_rules.txt', 'data/b698_rules.txt', 'data/b706_rules.txt', 'data/b675_corrigenda.txt', 'data/b652_ferry.txt', 'data/b706_ferry.txt',
              'data/b707_standing_figures.json', 'data/b707_report.txt', 'data/b707_report_root.txt', 'data/b707_act_root.json', 'data/b707_root_banks.txt',
              'data/b707_scores_close.json', 'data/b707_mirror.txt', 'data/b707_mirror_verify.txt', 'data/b707_checks.txt', 'data/b707_checks_postpush.txt',
              'data/b707_seal_hashes.json', 'data/b707_author_answers.txt', 'data/b707_port_files.txt', 'data/b707_buildlog_SIDE-lv-conservation_port.txt',
              'data/b706_partners.json', 'data/b706_print_files_prints-b706-v0.1.txt', 'data/b706_prints_v0.1.txt', 'data/b705_i6_ranking.txt',
              'tools/b707_report.py', 'tools/b707_report_root.py', 'tools/b707_record.py', 'tools/b707_checks.py', 'tools/b707_citation.py',
              'tools/b707_closing.py', 'tools/b707_reg_gate.py', 'tools/b707_regspec.py', 'tools/b707_corrigendum.py', 'tools/b707_worklist.py',
              'tools/b707_tests.py', 'tools/b706_standing_figures.py', 'tools/b706_record.py', 'tools/b704_record.py', 'tools/chain_page.py',
              'tools/circuit_read.py', 'tools/mirror_verify.py', 'tools/mirror_build.ps1', 'tools/push_gated.sh', 'tools/act_root.py', 'tools/rule_arms.py'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    # ### (R318)(1), by row
    cl = lines_of(p('data', 'b707_closing.txt'))
    add('ruling (1)', 'data/b707_closing.txt :1, the head line, against (R318)(1)`s quote after whitespace is removed', _ws(cl[0]) == _ws(HEAD_QUOTE),
        'data/b707_closing.txt :1 = %r' % cl[0][:130], '0-1')
    cf = first(cl, '### CARRIED FORWARD.')
    add('ferry read-first', 'data/b707_closing.txt, the carried-forward rows (a)-(h) by line', cf > 0 and first(cl, '    (a) ', cf) > 0 and first(cl, '    (h) ', cf) > 0,
        'data/b707_closing.txt :%d (the head), (a) :%d, (h) :%d' % (cf, first(cl, '    (a) ', cf), first(cl, '    (h) ', cf)), '0-1')
    po = rd(p('data', 'b707_closing_push_out.txt')) or ''
    head = g(ROOT, 'rev-parse', '--short=8', 'HEAD')[1].strip()
    add('ruling (1); ruling (8)', 'the closing commit relay b5898a61 pushed in main mode and read back (data/b707_closing_push_out.txt, to be committed)',
        'main read back at the remote: b5898a61' in po and 'branch push-b707-closing' in po and head == K.PRE_RELAY,
        'data/b707_closing_push_out.txt :2 (branch push-b707-closing), :5 (read back) ; relay HEAD %s' % head, '0-1')
    st = g(ROOT, 'status', '--porcelain', '--', 'data/b707_closing_push_out.txt')[1].strip()
    add('ruling (8); ferry C0', 'data/b707_closing_push_out.txt uncommitted at the act`s start', st.startswith('??'), 'git status %r' % st, '0')
    on = rd(p('data', 'b707_onset.txt')) or ''
    onl = on.split(NL)
    q0 = _onset_rows(on)
    b192, b128 = q0.get(('band', '192'), {}), q0.get(('band', '128'), {})
    r32, rl2 = q0.get(('rho0', '32'), {}), q0.get(('rho0', 'log2'), {})
    add('ruling (1); ferry read-first', 'data/b707_onset.txt (rows are rungs): the band zero`s family negative at a* = 2 log 192, lambda_min -0.180 there and +0.882 at 128',
        first(onl, 'band | negative at [\'192\'] ; undecided at NO RUNG ; a* = 192') > 0 and _near(b192.get('lmin'), -0.180, 3) and _near(b128.get('lmin'), 0.882, 3)
        and b192.get('reading') == 'NEGATIVE DIRECTION BEYOND ITS BOUND' and b128.get('reading') == 'POSITIVE DEFINITE BEYOND ITS BOUND',
        'data/b707_onset.txt :%d (a* = 192) ; :%d (192: lambda %s) ; :%d (128: lambda %s)' % (
            first(onl, 'band | negative at [\'192\']'), first(onl, '  band | 192 '), b192.get('lmin'), first(onl, '  band | 128 '), b128.get('lmin')), '1')
    add('ruling (1)', 'rho_0`s family negative at a* = 2 log 32 with lambda_min -0.140 there and +3.72 at log 2',
        first(onl, 'rho0 | negative at [\'32\'') > 0 and 'a* = 32' in at(onl, first(onl, 'rho0 | negative at [\'32\'')) and _near(r32.get('lmin'), -0.140, 3) and _near(rl2.get('lmin'), 3.72, 2),
        'data/b707_onset.txt :%d (a* = 32) ; :%d (32: lambda %s) ; :%d (log2: lambda %s)' % (
            first(onl, 'rho0 | negative at [\'32\''), first(onl, '  rho0 | 32 '), r32.get('lmin'), first(onl, '  rho0 | log2 '), rl2.get('lmin')), '1')
    ctl = rd(p('data', 'b707_onset_controls.txt')) or ''
    ctll = ctl.split(NL)
    z = _onset_rows(ctl)
    zb, zr = z.get(('band', '192'), {}), z.get(('rho0', '32'), {})
    add('ruling (1); ferry read-first', 'the zeta control positive definite at every rung with lambda_min 1.9e-7 and 2.1e-7 at those radii (data/b707_onset_controls.txt, rows are rungs)',
        first(ctll, 'C1 (ZETA) POSITIVE DEFINITE AT EVERY RUNG OF BOTH FREQUENCIES') > 0 and _near(float(zb.get('lmin') or 0) * 1e7, 1.9, 1) and _near(float(zr.get('lmin') or 0) * 1e7, 2.1, 1),
        'data/b707_onset_controls.txt :%d (C1) ; :%d (band 192: lambda %s) ; :%d (rho0 32: lambda %s)' % (
            first(ctll, 'C1 (ZETA) POSITIVE DEFINITE AT EVERY RUNG'), first(ctll, '  band | 192 '), zb.get('lmin'), first(ctll, '  rho0 | 32 '), zr.get('lmin')), '1')
    add('ruling (1)', '"the falsifier HELD": the onset bank`s own words for the falsifier and the hypothesis',
        first(onl, 'THE FALSIFIER (a positive form at every a computed, both frequencies): HELD') > 0,
        'data/b707_onset.txt :%d reads "THE FALSIFIER ... NOT FIRED" and :%d "THE REGISTRATION`S HYPOTHESIS ... HELD" -- the falsifier is NOT FIRED, the hypothesis HELD (the closing`s report line (1) the same)' % (
            first(onl, 'THE FALSIFIER (a positive form'), first(onl, 'THE REGISTRATION`S HYPOTHESIS')), '1')
    pt = lines_of(p('data', 'b707_port.txt'))
    add('ruling (1); ruling (7); ferry read-first', 'data/b707_port.txt naming the modules built and C7OrderBounds.lean :277 and :380 as the next failing lines',
        first(pt, 'error: SIDELvConservation/C7OrderBounds.lean:277:55: Application type mismatch') == 11 and first(pt, 'error: SIDELvConservation/C7OrderBounds.lean:380:8: (kernel) unknown constant') == 14
        and first(pt, 'modules built 6 of 12:') == 16 and first(pt, 'the modules remaining (not built by this run): 6') == 18,
        'data/b707_port.txt :11 (:277:55, Application type mismatch), :14 (:380:8, unknown constant), :16 (built 6 of 12), :18 (remaining 6)', '1-4')
    pf = lines_of(p('data', 'b707_port_files.txt'))
    add('ruling (1)', 'five files on the branch, one dispatch (data/b707_port_files.txt; data/b707_dispatches.json), nothing merged, the deposit untouched',
        first(pf, 'FIVE FILES ON port-b707') > 0 and len(_jl('b707_dispatches.json').get('rows') or []) == 1 and g(LV, 'rev-parse', 'main')[1].strip() == K.LV_MAIN
        and g(LV, 'rev-parse', 'v0.10.0^{commit}')[1].strip() == K.LV_V0100 and g(LV, 'rev-parse', K.PORT_BRANCH)[1].strip() == K.PORT_COMMIT,
        'data/b707_port_files.txt :%d ; dispatch rows %d ; lv main %s, v0.10.0 %s, port-b707 %s' % (
            first(pf, 'FIVE FILES ON port-b707'), len(_jl('b707_dispatches.json').get('rows') or []), K.LV_MAIN[:7], K.LV_V0100[:7], K.PORT_COMMIT[:7]), '1')
    tr = lines_of(p('data', 'b707_tool_repairs.txt'))
    add('ruling (1); ferry read-first', 'the three readers of the renames written and controlled (data/b707_tool_repairs.txt rows (1)-(3): the roster at 70 entries, four re-pointed, thirteen struck; the table excluding archive/; the split arm`s family reading)',
        first(tr, '  (1) tools/mirror_roster.json') > 0 and 'four rows' in at(tr, first(tr, '  (1) tools/mirror_roster.json')) and 'thirteen duplicate rows removed, 70 entries' in at(tr, first(tr, '  (1) tools/mirror_roster.json'))
        and first(tr, '  (2) tools/terminal_table.py') > 0 and first(tr, '  (3) tools/rule_arms.py') > 0 and first(tr, 'REPAIRS 6 ; SHARED FILES EDITED 3') > 0,
        'data/b707_tool_repairs.txt :%d, :%d, :%d ; the verdict :%d' % (first(tr, '  (1) tools/mirror_roster.json'), first(tr, '  (2) tools/terminal_table.py'), first(tr, '  (3) tools/rule_arms.py'), first(tr, 'REPAIRS 6 ;')), '1')
    mi = lines_of(p('data', 'b707_mirror.txt'))
    add('ruling (1)', 'the mirror CLEAN on all three clauses over 70 files (data/b707_mirror.txt)', first(mi, 'THE VERIFICATION : CLEAN ON ALL THREE CLAUSES') > 0 and first(mi, 'files 70') > 0 and os.path.exists(K.MIRROR_ZIP),
        'data/b707_mirror.txt :%d (CLEAN), :%d (files 70) ; the zip exists %s' % (first(mi, 'THE VERIFICATION : CLEAN ON ALL THREE CLAUSES'), first(mi, 'files 70'), os.path.exists(K.MIRROR_ZIP)), '1')
    rg7 = lines_of(p('data', 'b707_registrations.txt'))
    add('ruling (1); ruling (11); ferry read-first', 'the higher pairs` route registered in data/b707_registrations.txt (rows are registrations), committed alone at relay 6e8ece87',
        first(rg7, '  (i) THE HIGHER PAIRS\' ROUTE -- COMPUTED AT b709') == 10 and [x for x in g(ROOT, 'diff-tree', '--no-commit-id', '--name-only', '-r', '6e8ece87')[1].split(NL) if x.strip()] == ['data/b707_registrations.txt'],
        'data/b707_registrations.txt :10 ; relay 6e8ece87 carries that file alone', '1')
    add('ruling (1)', 'the entry at FINDINGS :10106, the trail at OPEN_TRAILS :15688', at(fi, K.B707_ENTRY).startswith('## The sign-onset radius at the Epstein zeta') and at(ot, K.B707_TRAIL) == K.B707_TRAIL_HEAD,
        'FINDINGS :%d %r ; OPEN_TRAILS :%d %r' % (K.B707_ENTRY, at(fi, K.B707_ENTRY)[:50], K.B707_TRAIL, at(ot, K.B707_TRAIL)[:60]), '1')
    ar = _jl('b707_act_root.json')
    rb = lines_of(p('data', 'b707_root_banks.txt'))
    add('ruling (1)', 'the root 6fe154f9 over 83 banks chained from aa8a696b (data/b707_act_root.json; data/b707_root_banks.txt; data/act_roots.txt`s b707 row)',
        (ar.get('root') or '').startswith('6fe154f9') and (ar.get('previous') or '').startswith('aa8a696b') and bool(act_root_line('b707')) and first(rb, 'BANKS 83 ;') > 0,
        'data/b707_act_root.json (root %s, prev %s) ; data/b707_root_banks.txt :%d ; data/act_roots.txt row b707 %s' % ((ar.get('root') or '')[:8], (ar.get('previous') or '')[:8], first(rb, 'BANKS 83 ;'), bool(act_root_line('b707'))), '1')
    ck, cp = rd(p('data', 'b707_checks.txt')) or '', rd(p('data', 'b707_checks_postpush.txt')) or ''
    add('ruling (1)', 'the chain b624-b707 AGREE (G-ACTROOT-VERIFY passing pre-push and post-push)', 'G-ACTROOT-VERIFY' in ck and 'G-ACTROOT-VERIFY' not in re.search(r'LIVE FAILING : \d+ \[(.*?)\]', cp).group(1) if re.search(r'LIVE FAILING : \d+ \[(.*?)\]', cp) else False,
        'data/b707_checks_postpush.txt LIVE FAILING names no G-ACTROOT-VERIFY', '1')
    add('ruling (1)', 'suite 133 of 137 pre-push and 129 of 137 post-push', 'ARMS RUN : 137. ### LIVE PASSING : 133.' in ck and 'ARMS RUN : 137. ### LIVE PASSING : 129.' in cp,
        'data/b707_checks.txt ; data/b707_checks_postpush.txt', '1')
    sr, sc = _jl('b707_scores.json'), _jl('b707_scores_close.json')
    add('ruling (1)', 'N1-N5 and S3 HELD at the lock, N5 REFUTED at the close on tools/mirror_prevbuild.json alone (data/b707_scores.json, data/b707_scores_close.json)',
        all((sr.get(k) or [''])[0] == 'HELD' for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S3')) and (sc.get('N5') or [''])[0] == 'REFUTED' and 'mirror_prevbuild.json' in (sc.get('N5') or ['', ''])[1]
        and all((sc.get(k) or [''])[0] == 'HELD' for k in ('S1', 'S2')),
        'data/b707_scores.json: %s ; data/b707_scores_close.json: N5 %s, S1 %s, S2 %s' % (', '.join('%s %s' % (k, (sr.get(k) or ['-'])[0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S3')),
                                                                                     (sc.get('N5') or ['-'])[0], (sc.get('S1') or ['-'])[0], (sc.get('S2') or ['-'])[0]), '1')
    df = lines_of(p('data', 'b707_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", NL.join(df), re.M)
    nav = [x for x, o in lt if o == 'NAVIGATOR']
    add('ruling (1); ferry read-first', 'data/b707_defects.txt (rows are defects as lettered): nine, (a)-(i), (i) the seat`s', [x for x, _o in lt] == list('abcdefghi') and dict(lt).get('i') == 'SEAT',
        'letters %s ; (i) THE %s`S' % (''.join(x for x, _o in lt), dict(lt).get('i')), '1')
    add('ruling (1)', '"four the navigator`s at step zero": the bank`s owners', len(nav) == RULING_NAV_AT_STEPZERO,
        'the navigator`s by the bank: %s -- FIVE, every one at step zero ((c), (d), (e) by the fact clause; (f), (g) raised in one prompt before Components 1 and 3)' % nav, '1')
    add('ruling (1)', '"nothing deposited": the draft at v5, held', K.DRAFT == '23228113', 'tools/b708_worklist.py DRAFT', '6')
    # ### (R318)(2)
    cfiles = [x for x in g(ROOT, 'diff-tree', '--no-commit-id', '--name-only', '-r', K.PRE_RELAY)[1].split(NL) if x.strip()]
    add('ruling (2); ferry read-first', 'tools/mirror_prevbuild.json the mirror builder`s state file, written at every build and committed with the closing (relay b5898a61)',
        'tools/mirror_prevbuild.json' in cfiles and 'mirror_build.ps1' not in cfiles and first(lines_of(p('tools', 'mirror_prevbuild.json')), '"lastChanged":  "2026-10-22-b707"') == 2,
        'relay b5898a61 carries tools/mirror_prevbuild.json ; its :2 lastChanged 2026-10-22-b707', '1')
    s_i, t_i = _defect_row(df, 'i')
    add('ruling (2)', 'b707`s post-seal item (i) for the corrigendum (data/b707_defects.txt (i): the write list omits the mirror builder`s pointer file)',
        s_i > 0 and 'WRITE LIST OMITS THE MIRROR BUILDER' in t_i and 'lettered after the trail' in t_i.lower() or ('lettered before the act part' in t_i),
        'data/b707_defects.txt (i) :%d' % s_i, '1')
    cgb = lines_of(p('data', 'b675_corrigenda.txt'))
    lastrow = max([int(m) for m in re.findall(r'^  \((\d+)\) ', NL.join(cgb), re.M)] or [0])
    add('ruling (2)', 'the corrigenda bank, appended only (its last row (27), b707`s)', lastrow == 27, 'data/b675_corrigenda.txt, last row (%d) at :%d' % (lastrow, first(cgb, '  (%d) ' % lastrow)), '1')
    add('ruling (2)', 'b707`s corrigendum tool to carry (b678`s form)', os.path.exists(p('tools', 'b707_corrigendum.py')) and os.path.exists(p('tools', 'b678_corrigendum.py')), 'tools/b707_corrigendum.py ; tools/b678_corrigendum.py', '1')
    add('ruling (2); ruling (9)', 'data/b708_rules.txt row (1) -- TO BE WRITTEN at step zero (the report tool outside the sealed list until the root`s word)', not os.path.exists(p('data', 'b708_rules.txt')), 'absent, as ordered', '0')
    add('ruling (2)', 'the report tool outside this act`s sealed list (tools/b708_worklist.py SEALED)', 'b708_report.py' not in K.SEALED and 'b707_report.py' in __import__('b707_worklist').SEALED,
        'b708 SEALED %d tools, the report tool not among them ; b707 sealed its report tool (the event in data/b707_defects.txt)' % len(K.SEALED), '5')
    rg = lines_of(p('data', 'b705_registrations.txt'))
    add('ruling (2)', 'the onsets at the coarse grid`s own points, a = 2 log N at the widths 32 and 192 b694 and b705 used (data/b705_registrations.txt :19-:21; the ladder :39-:40)',
        'a window of width w has h supported' in at(rg, 19) and 'w = 32: a = 2 log 32' in at(rg, 20) and "ladder's radii 2 log w, w = 32 ... 192" in at(rg, 40),
        'data/b705_registrations.txt :19-:21, :39-:40', '1')
    add('ruling (2)', 'no grid point between the coarse points where the sign turns (the ladder log 2, 32, 48, 64, 96, 128, 192: the band`s turn between 128 and 192, rho_0`s between log 2 and 32)',
        b128.get('reading') == 'POSITIVE DEFINITE BEYOND ITS BOUND' and b192.get('reading') == 'NEGATIVE DIRECTION BEYOND ITS BOUND' and rl2.get('reading') == 'POSITIVE DEFINITE BEYOND ITS BOUND' and r32.get('reading') == 'NEGATIVE DIRECTION BEYOND ITS BOUND',
        'data/b707_onset.txt :12-:25 (the fourteen rows)', '1')
    add('ruling (2)', 'the zeta control`s margin of order 1e-7 beside its certified tail bound (b696`s arch_tail, tools/b696_witness_balls.py :90)',
        first(lines_of(p('tools', 'b696_witness_balls.py')), 'def arch_tail(') == 90 and first(ctll, 'arch_tail :90') > 0, 'tools/b696_witness_balls.py :90 ; data/b707_onset_controls.txt :4', '1')
    # ### (R318)(3)
    i3 = first(rg, '  (iii) THE SIGN-ONSET RADIUS AT Q0')
    add('ruling (3); ferry read-first', 'data/b705_registrations.txt (iii) by line: the parameter, the empty prime side, the source, the quantity, the hypothesis, the falsifier, the controls',
        i3 == 15 and first(rg, 'THE PARAMETER: a > 0') == 17 and first(rg, 'THE EMPTY PRIME SIDE') == 22 and first(rg, 'THE QUANTITY: for each support radius a on a ladder') == 39
        and first(rg, 'HYPOTHESIS: a* exists on the ladder') == 44 and first(rg, 'FALSIFIER: a positive form at every a computed') == 47 and first(rg, 'CONTROLS: (C1) the zeta form') == 48,
        'data/b705_registrations.txt (iii) :%d ; :17 ; :22 ; :26 ; :39 ; :44 ; :47 ; :48' % i3, '0')
    rlog = g(ROOT, 'log', '--format=%h', '--', 'data/b705_registrations.txt')[1].split()
    add('ruling (3)', 'the registration (iii) unchanged from its b705 commit (d139cfcf), the one commit touching it', rlog == ['d139cfcf'], 'commits touching data/b705_registrations.txt %s' % rlog, '0')
    add('ruling (3)', 'the coarse endpoints per family: the band zero`s greatest positive radius 2 log 128 (a 9.704) and least negative 2 log 192 (a 10.515); rho_0`s log 2 (a 0.693) and 2 log 32 (a 6.931)',
        _near(b128.get('a'), 9.704, 3) and _near(b192.get('a'), 10.515, 3) and _near(rl2.get('a'), 0.693, 3) and _near(r32.get('a'), 6.931, 3),
        'data/b707_onset.txt :17-:18 (band 128, 192), :19-:20 (rho0 log2, 32)', '0')
    add('ruling (3)', 'the rungs log p^k in each interval, counted by the controls bank`s rung structure (data/b707_onset_controls.txt :15-:21: Q0 terms new at 32 = 270 in (log 2, 2 log 32]; new at 192 = 4127 in (2 log 128, 2 log 192])',
        'Q0 terms 270 (first [4, 6, 8, 9, 12, 16] ; new at this rung 270)' in at(ctll, 16) and 'new at this rung 4127' in at(ctll, 21),
        'data/b707_onset_controls.txt :16, :21', '0')
    add('ruling (3)', 'data/b708_registrations.txt -- TO BE WRITTEN at step zero, committed alone before any computation', not os.path.exists(p('data', 'b708_registrations.txt')), 'absent, as ordered', '0')
    # ### (R318)(4)
    add('ruling (4); ferry read-first', 'W-ORD-WORKFLOW-PROBE-STEP discharged at OPEN_TRAILS :15638 with the trigger for the chain`s next probe, b708',
        'W-ORD-WORKFLOW-PROBE-STEP' in at(ot, K.ORDER_WORKFLOW_PROBE_DISCHARGED) and 'The trigger for the chain’s next probe, b708' in at(ot, K.ORDER_WORKFLOW_PROBE_DISCHARGED) and 'W-ORD-WORKFLOW-PROBE-STEP' in at(ot, K.ORDER_WORKFLOW_PROBE),
        'OPEN_TRAILS :%d (entered), :%d (discharged, the trigger b708)' % (K.ORDER_WORKFLOW_PROBE, K.ORDER_WORKFLOW_PROBE_DISCHARGED), '2')
    wf = lines_of(os.path.join(EF, *K.WORKFLOW.split('/')))
    efm = g(EF, 'rev-parse', 'main')[1].strip()
    add('ruling (4); ferry read-first', 'SIDE-explicit-formula`s build-module.yml at main, the probe step by line (:101 the step, :105 the root ChainProbe.lean test, :140 the separate artifact)',
        efm == K.EF_MAIN and first(wf, "- name: Chain probe of the ref's root ChainProbe.lean") == 101 and first(wf, 'if [ ! -f ChainProbe.lean ]; then') == 105 and first(wf, "- name: Upload the chain probe's artifact, separate from the run's") == 140,
        'main %s ; build-module.yml :101, :105, :140' % efm[:8], '2')
    ef37 = g(EF, 'rev-parse', 'v0.37^{commit}')[1].strip()
    dstat = [x for x in g(EF, 'diff', '--name-only', 'v0.37', 'main')[1].split(NL) if x.strip()]
    add('ruling (4)', '"a branch probe-b708 cut from SIDE-explicit-formula`s main at its current tag": main stands AT the tag v0.37', efm == ef37,
        'main %s ; v0.37 peeled %s ; main is ONE COMMIT PAST v0.37 (badaccc, the workflow`s probe step, b706): the diff v0.37..main %s -- the modules` tree v0.37`s, the probe step at main alone, so the branch is cut from main and probes the tree at the tag' % (
            efm[:8], ef37[:8], dstat), '2')
    tree37 = _tree(EF, 'v0.37')
    treem = _tree(EF, 'main')
    add('ferry read-first', 'a listing of SIDE-explicit-formula`s tree at its current tag v0.37, printed (git ls-tree -r): ChainProbe.lean absent, CircuitClosure.lean and print_targets.txt present, the workflow present',
        bool(tree37) and K.PROBE_FILE not in tree37 and 'CircuitClosure.lean' in tree37 and 'print_targets.txt' in tree37 and K.WORKFLOW in tree37 and K.PROBE_FILE not in treem,
        'the tree at v0.37: %d files (main %d) ; ChainProbe.lean absent at both ; CircuitClosure.lean, print_targets.txt and the workflow present' % (len(tree37), len(treem)), '0-2')
    rh = _remote_heads(EF)
    add('ruling (4); ruling (5)', 'the branches probe-b708 and prints-b708-v0.17 absent before the act, locally and at the remote (one ls-remote of SIDE-explicit-formula)',
        not branch_listed(EF, K.PROBE_BRANCH) and not branch_listed(EF, K.PRINTS_BRANCH) and ('refs/heads/%s' % K.PROBE_BRANCH) not in rh and ('refs/heads/%s' % K.PRINTS_BRANCH) not in rh,
        'local %s, %s ; remote %s, %s' % ('present' if branch_listed(EF, K.PROBE_BRANCH) else 'absent', 'present' if branch_listed(EF, K.PRINTS_BRANCH) else 'absent',
                                          'present' if ('refs/heads/%s' % K.PROBE_BRANCH) in rh else 'absent', 'present' if ('refs/heads/%s' % K.PRINTS_BRANCH) in rh else 'absent'), '2')
    r5 = lines_of(p('data', 'b705_rules.txt'))
    pt37 = [l for l in (g(EF, 'show', 'v0.37:print_targets.txt')[1] or '').split(NL) if l.strip()]
    add('ruling (4); ferry read-first', 'data/b705_rules.txt row (1): the probe route`s target is print_targets.txt whole -- 109 names at v0.37',
        first(r5, '(1) THE PROBE ROUTE\'S TARGET IS print_targets.txt WHOLE') == 6 and len(pt37) == 109 and '109 names at' in at(r5, 7),
        'data/b705_rules.txt :6-:10 ; print_targets.txt at v0.37 %d names' % len(pt37), '2')
    pb = lines_of(p('data', 'b704_probe.txt'))
    add('ruling (4); ferry read-first', 'data/b704_probe.txt: the generator`s text (sha256 8c18df42..., 568 cells, 43 target modules) and data/b704_probe_out_zeta.txt the probe bank (run 39721668586)',
        first(pb, 'sha256 8c18df4244c5f25a03ba2bf26ea1346ab318192014f70a46366835c69c5bf364') == 7 and first(pb, 'the lake target (the probe`s module imports at the pin, 43)') == 8 and 'CELLS 568' in at(pb, 10)
        and os.path.exists(p('data', 'b704_probe_out_zeta.txt')) and (_jl('b704_dispatches.json').get('rows') or [{}])[0].get('run_id') == 39721668586,
        'data/b704_probe.txt :7, :8, :10 ; data/b704_probe_out_zeta.txt %d lines ; data/b704_dispatches.json run 39721668586' % len(lines_of(p('data', 'b704_probe_out_zeta.txt'))), '2')
    pg = lines_of(os.path.join(PP, K.FACES_PAGE))
    add('ruling (4)', 'the faces page generated from the list data/b704_nodes_zeta.txt at v0.37 = 38e2734 (its :3)', 'data/b704_nodes_zeta.txt' in at(pg, 3) and 'v0.37 = `38e2734`' in at(pg, 3),
        '%s :3' % K.FACES_PAGE, '2')
    # ### (R318)(5)
    add('ruling (5); ferry read-first', 'W-ORD-ENTRY-TAG-PRINTS`s remainder at OPEN_TRAILS :15684: the two unbanked mentions, SIMPLICITY :442 at v0.17 (one dispatch) and FACES_LEDGER :20 (no tag, no dispatch)',
        'THE REMAINDER ENTERED, THE TWO UNBANKED MENTIONS' in at(ot, K.ORDER_TAG_REMAINDER) and 'priced at one dispatch at b708' in at(ot, K.ORDER_TAG_REMAINDER) and 'nothing to print, no dispatch priced' in at(ot, K.ORDER_TAG_REMAINDER),
        'OPEN_TRAILS :%d' % K.ORDER_TAG_REMAINDER, '2')
    cr = lines_of(p('data', 'b706_cells_reread.txt'))
    add('ruling (5); ferry read-first', 'data/b706`s reach bank, the two unbanked rows by line (data/b706_cells_reread.txt :16 SIMPLICITY :442, :37 FACES_LEDGER :20)',
        'SIMPLICITY_OF_RIEMANN_ZEROS.md :442' in at(cr, 16) and 'unbanked' in at(cr, 16) and 'FACES_LEDGER.md :20' in at(cr, 37) and 'unbanked' in at(cr, 37),
        'data/b706_cells_reread.txt :16, :37', '2')
    s442 = at(lines_of(os.path.join(PP, 'phase1.5', 'simplicity', 'SIMPLICITY_OF_RIEMANN_ZEROS.md')), 442)
    f20 = at(lines_of(os.path.join(PP, 'FACES_LEDGER.md')), 20)
    m442 = re.search(r'SIDE-explicit-formula (v\d+(?:\.\d+)*) = `([0-9a-f]{7,40})`', s442)
    add('ruling (5)', 'SIMPLICITY_OF_RIEMANN_ZEROS :442 names SIDE-explicit-formula v0.17 = 5a1630b by `simplicity_iff` (the first mention`s tag)',
        bool(m442) and m442.group(1) == 'v0.17' and K.EF_V017.startswith(m442.group(2)) and '`simplicity_iff`' in s442, 'SIMPLICITY :442 names %s' % (('%s = %s' % (m442.group(1), m442.group(2))) if m442 else 'NO tag'), '2')
    add('ruling (5)', '"the tag each cites ... a scratch branch cut at each tag ... one dispatch each" (and N1`s three dispatches): FACES_LEDGER :20 names a tag beside the kernel',
        'SIDE-explicit-formula' in f20 and bool(re.search(r'v\d+(?:\.\d+)* = `[0-9a-f]{7,40}`', f20)),
        'FACES_LEDGER :20 (the F1 row) names NO kernel and NO tag (b707`s (e), OPEN_TRAILS :15684: nothing to print, no dispatch priced) -- one tag cited, one scratch branch, one dispatch for the prints; the act`s dispatches two, not three', '2')
    add('ruling (5)', 'v0.17 peeled 5a1630b at SIDE-explicit-formula, its tree without the workflow and without print_targets.txt (b706`s form supplies both)',
        g(EF, 'rev-parse', 'v0.17^{commit}')[1].strip() == K.EF_V017 and K.WORKFLOW not in _tree(EF, 'v0.17') and 'print_targets.txt' not in _tree(EF, 'v0.17') and 'SIDEExplicitFormula/Simplicity.lean' in _tree(EF, 'v0.17'),
        'v0.17 = %s ; its tree %d files, Simplicity.lean present, the workflow and print_targets.txt absent' % (K.EF_V017[:8], len(_tree(EF, 'v0.17'))), '2')
    add('ruling (5)', '(R316)(7)`s form (data/b706_ferry.txt; tools/b706_record.py printprobe, printsbank, cellsreach; data/b706_print_files_prints-b706-v0.1.txt)',
        rule_clause('R316', (7,))[0] and 'def printprobe(' in (rd(p('tools', 'b706_record.py')) or '') and 'def printsbank(' in (rd(p('tools', 'b706_record.py')) or '') and os.path.exists(p('data', 'b706_print_files_prints-b706-v0.1.txt')),
        rule_clause('R316', (7,))[1] + ' ; tools/b706_record.py :1453, :1580, :1616', '2')
    add('ruling (5)', 'b704`s probe bank holds simplicity_iff at v0.37 for the "equal"/"differs" reading', first(lines_of(p('data', 'b704_probe_out_zeta.txt')), '@@BEGIN SIDEExplicitFormula.Simplicity.simplicity_iff') > 0,
        'data/b704_probe_out_zeta.txt :%d' % first(lines_of(p('data', 'b704_probe_out_zeta.txt')), '@@BEGIN SIDEExplicitFormula.Simplicity.simplicity_iff'), '2')
    # ### (R318)(6)
    lt_ = lines_of(p('data', 'b670_licensed_table.txt'))
    add('ruling (6); ferry read-first', 'data/b670_licensed_table.txt (the licensed table, reading 1; the agenda rows :90-:122)', first(lt_, 'THE LICENSED TABLE') == 1 and first(lt_, '### B. PER AGENDA DOCUMENT') == 89,
        'data/b670_licensed_table.txt :1, :89', '0-3')
    f52 = lines_of(p('data', 'b652_ferry.txt'))
    add('ruling (6)', 'b652`s order (data/b652_ferry.txt :19): the next kernel by descending count, then the companions', 'then the companions' in at(f52, 19), 'data/b652_ferry.txt :19', '0-3')
    r74 = lines_of(p('data', 'b674_rules.txt'))
    add('ruling (6); ferry read-first', 'b674`s rule (data/b674_rules.txt :8-:11, row (2) the tie-break beyond the count)', first(r74, '(2) THE TIE-BREAK BEYOND THE COUNT') == 8, 'data/b674_rules.txt :8-:11', '0-3')
    add('ruling (6); ferry read-first', 'data/b705_rules.txt row (2): the tie-break`s silence closed, b674`s measures in their written order (:11-:14)', first(r5, '(2) THE TIE-BREAK\'S SILENCE CLOSED') == 11, 'data/b705_rules.txt :11-:14', '0-3')
    r90 = lines_of(p('data', 'b690_rules.txt'))
    add('ruling (6); ferry read-first', 'data/b690_rules.txt row (2): the quotation search with git grep before the merge, every hit a residue (:9-:12)', first(r90, '(2) AT A RE-CUT, EACH LINE THE CUT REMOVES OR CHANGES') == 9, 'data/b690_rules.txt :9-:12', '3')
    t04 = lines_of(p('data', 'b704_tie.txt'))
    c04 = _jl('b704_cut.json')
    add('ruling (6)', 'the agenda as b704`s tie bank read it (data/b704_tie.txt :14-:46) with b704`s cut entered from its bank (ONE_PAGE_PROOF 22 -> %s): the companions by count' % c04.get('after'),
        first(t04, 'day1/Spectral_Inertness.md (v2.3.1)') == 17 and first(t04, 'day1/ONE_PAGE_PROOF.md (v1.0.1)') == 21 and c04.get('before') == 22 and c04.get('after') == 2 and c04.get('document') == 'day1/ONE_PAGE_PROOF.md',
        'data/b704_tie.txt :17 (Spectral_Inertness 22), :21 (ONE_PAGE_PROOF 22) ; data/b704_cut.json before 22 after 2', '0-3')
    tb = lines_of(p('data', K.CUT_TABLE))
    dm = re.search(r'PLACE-papers (\S+) at (\w+), (\d+) lines, sha256 ([0-9a-f]{64})', NL.join(tb[:4]))
    head_sha = hashlib.sha256((C.g(PP, 'show', 'HEAD:%s' % K.CUT_DOC)[1] or '').encode('utf-8')).hexdigest() if dm else ''
    add('ruling (6); ferry read-first', 'the per-document table of the companion at the top count, data/%s (rows are claims): its summary line and the document unmoved since its read' % K.CUT_TABLE,
        bool(dm) and dm.group(1) == K.CUT_DOC and first(tb, 'Spectral_Inertness: CLAIMS 116 ; SKIPPED LINES 58 ; MATCHES 92 ; UNDERSTATES 2 ; OVERREACHES 14 ; UNLICENSED 8') == 254 and head_sha == (dm.group(4) if dm else ''),
        'data/%s :3 (%s at %s, sha256 %s), :254 (the summary) ; the document at PLACE-papers HEAD sha256 %s ; %s' % (
            K.CUT_TABLE, dm.group(1) if dm else '?', dm.group(2) if dm else '?', (dm.group(4) if dm else '')[:16], head_sha[:16], 'UNMOVED' if dm and head_sha == dm.group(4) else '### MOVED'), '0-3')
    add('ruling (6)', 'the tables read at the renamed paths (the roster`s 20 tables at the unversioned names, data/b706_partners.json; b707`s rowgen roster re-pointed)',
        len(_jl('b706_partners.json').get('rows') or []) == 17 and os.path.exists(p('data', 'b707_rowgen_stepzero.txt')) and 'RE-POINTED 8' in (rd(p('data', 'b707_rowgen_stepzero.txt')) or ''),
        'data/b706_partners.json 17 rows ; data/b707_rowgen_stepzero.txt RE-POINTED 8', '0')
    add('ruling (6); ferry read-first', 'W-ORD-KEYSTONE-HEADS at OPEN_TRAILS :15454 (held: the cut writes rows, not the paper`s opening)', 'W-ORD-KEYSTONE-HEADS' in at(ot, K.ORDER_KEYSTONE) and 'ENTERED' in at(ot, K.ORDER_KEYSTONE),
        'OPEN_TRAILS :%d' % K.ORDER_KEYSTONE, '3')
    add('ruling (6)', 'the b670 method`s form for a companion`s cut (data/b704_cut.txt :130; tools/b704_record.py cutbank :976, quote :938)',
        'THE DISTANCE BY THE b670 METHOD: BEFORE 22, AFTER 2' in at(lines_of(p('data', 'b704_cut.txt')), 130) and 'def cutbank(' in (rd(p('tools', 'b704_record.py')) or '') and 'def quote(' in (rd(p('tools', 'b704_record.py')) or ''),
        'data/b704_cut.txt :130 ; tools/b704_record.py cutbank :976, quote :938', '3')
    add('ruling (6)', 'data/b708_cut.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b708_cut.txt')), 'absent, as ordered', '3')
    # ### (R318)(7)
    rhl = _remote_heads(LV)
    add('ruling (7); ruling (8)', 'port-b707 at its one commit 69e239d locally and at the remote, kept (one ls-remote of SIDE-lv-conservation)',
        branch_listed(LV, K.PORT_BRANCH) and rhl.get('refs/heads/%s' % K.PORT_BRANCH) == K.PORT_COMMIT and g(LV, 'rev-parse', K.PORT_BRANCH)[1].strip() == K.PORT_COMMIT,
        'local %s ; remote %s' % (g(LV, 'rev-parse', K.PORT_BRANCH)[1].strip()[:8], (rhl.get('refs/heads/%s' % K.PORT_BRANCH) or 'absent')[:8]), '4')
    add('ruling (7)', 'the two failures` kinds readable from data/b707_port.txt: :277:55 an application type mismatch (a changed signature, :35-:42), :380:8 an unknown constant (a renamed Mathlib declaration, :14)',
        'Application type mismatch' in at(pt, 11) and 'WeakFEPair.hasMellin (hurwitzEvenFEPair 0).toStrongFEPair w' in at(pt, 42) and "unknown constant 'SIDELvConservation.exists_norm_completedRiemannZeta₀_le_exp_half'" in at(pt, 14),
        'data/b707_port.txt :11, :35-:42 (the mismatch: the hypothesis `k < re s` expected where the argument `w` was given), :14 (the constant moved)', '4')
    # ### (R318)(8)-(10) and the ferry
    for repo, bs in K.DELETE:
        mg = (g(repo, 'branch', '--merged', 'main')[1] or '').replace('*', ' ').split()
        for b in bs:
            add('ruling (8)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in mg, 'listed by `git branch --merged main` at %s before any delete' % os.path.basename(repo) if b in mg else '### NOT LISTED', '0')
    add('ruling (8)', 'the 2,560 MB hold', K.HOLD == 2560, 'tools/b708_worklist.py HOLD', '0')
    add('ruling (9)', 'the READFIRST-CLOSURE reader', 'def readfirst(' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py :%d' % first(lines_of(p('tools', 'circuit_read.py')), 'def readfirst('), '0')
    add('ruling (9)', 'data/b708_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b708_readfirst.txt')), '0')
    add('ruling (9)', 'data/b709_rules.txt by form (the (W) list admits it; none written)', not os.path.exists(p('data', 'b709_rules.txt')), 'absent; admitted by form', '5')
    add('ruling (10)', 'the draft at v5, held', K.DRAFT == '23228113', 'tools/b708_worklist.py DRAFT', '6')
    add('ruling (11)', 'W-ORD-STANDING-CLAUSES-BANK at OPEN_TRAILS :15450, trigger b710', 'W-ORD-STANDING-CLAUSES-BANK' in at(ot, K.ORDER_STANDING_CLAUSES) and 'Trigger: the reading act b710' in at(ot, K.ORDER_STANDING_CLAUSES), 'OPEN_TRAILS :%d' % K.ORDER_STANDING_CLAUSES, '6')
    i6 = lines_of(p('data', 'b705_i6_ranking.txt'))
    add('ruling (11)', 'the next axis of data/b705_i6_ranking.txt (:58, (e) representation coordinates, for b709)', first(i6, '2. (e) representation coordinates') == 58, 'data/b705_i6_ranking.txt :58', '6')
    add('ruling (11)', 'readings 3 and 4 (data/b690_r3_residues.txt, data/b700_r4_licensed.txt) for b710`s readfirst flip', os.path.exists(p('data', 'b690_r3_residues.txt')) and os.path.exists(p('data', 'b700_r4_licensed.txt')),
        'data/b690_r3_residues.txt ; data/b700_r4_licensed.txt', '6')
    add('ruling (11)', 'the port`s next dispatch at b709, W-ORD-LV-FORWARD-PORT at OPEN_TRAILS :15686 (trigger the next ruling that names it)', 'W-ORD-LV-FORWARD-PORT' in at(ot, K.ORDER_LV_PORT) and 'Trigger: the next ruling that names it (b709 the research act)' in at(ot, K.ORDER_LV_PORT),
        'OPEN_TRAILS :%d' % K.ORDER_LV_PORT, '4-6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C5', 'the chain halves as b693 drew them, b708 added to the second', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or '') and K.CHAIN_HALVES == (('b624', 'b658'), ('b659', 'b708')),
        'tools/b693_worklist.py :52 ; tools/b708_worklist.py CHAIN_HALVES', '5')
    add('ferry C5', 'the four standing arms` figures tool and b707`s baselines', os.path.exists(p('tools', 'b706_standing_figures.py')) and os.path.exists(p('data', 'b707_standing_figures.json')),
        'tools/b706_standing_figures.py (b707 read it unedited) ; data/b707_standing_figures.json', '5')
    add('ferry; ruling (2)', 'data/b680_rules.txt (1), a binary bank beside a text hashes bank', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt :5', '2')
    add('ferry C0', 'data/b684_rules.txt row (1), a test file over 450 s its own part', '(1) A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5', '0')
    add('ferry C5', 'data/b706_rules.txt row (1): ROOT_EXCLUDE carried and extended, the root route dry READY before the seal', 'a face whose dry READY reads False is not locked' in (rd(p('data', 'b706_rules.txt')) or ''), 'data/b706_rules.txt :6-:15', '5')
    add('ferry C6', 'b673`s capture names', os.path.exists(p('data', 'b707_relay_push_out.txt')), 'data/b707_relay_push_out.txt (the form carried)', '6')
    add('ferry C6', 'the b670 form of the mirror', os.path.exists(p('data', 'b707_mirror.txt')), 'data/b707_mirror.txt (the form carried)', '6')
    add('ferry C6', 'the unsealed report tool`s form (tools/b707_report_root.py, written after the root`s word; data/b707_report_root.txt)', os.path.exists(p('tools', 'b707_report_root.py')) and os.path.exists(p('data', 'b707_report_root.txt')) and not os.path.exists(p('tools', 'b708_report.py')),
        'tools/b707_report_root.py ; data/b707_report_root.txt ; tools/b708_report.py TO BE WRITTEN after the root`s word', '6')
    add('ferry C0', 'this act`s session transcript (a new session; b707 ran in aa198636)', os.path.exists(C.SESSION) and os.path.exists('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.PREV_SESSION), C.SESSION, '0')
    return R


def _write(L, R, miss):
    for name, data in (('b708_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b708_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b708 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR OR ENTERED BY THE FACT CLAUSE BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    if 'dry' in a:
        print(NL.join(L))
        return
    _write(L, R, miss)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    """the ferry is banked by the Write tool (data/b708_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b708_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b708_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b708_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


# ### b706's repair of the answer checker (b705 defect (n)), carried: b682's route reads every bare eight-hex token as a commit. A token that a
# ### bank's row names as a sha256 -- the root list, a hashes bank's row, a bank line carrying "sha256" -- or that a kernel's lakefile or
# ### manifest pins as a rev, is a root prefix, a file hash or a pin, not a commit, and is checked against that row instead.
_HEX8 = re.compile(r'(?<![0-9a-f])([0-9a-f]{8})(?![0-9a-f])')


def _sha_rows():
    out = {}
    for q in [os.path.join(D, 'act_roots.txt')] + sorted(glob.glob(os.path.join(D, '*.txt')), reverse=True):   # ### the later act's row named first
        t = rd(q) or ''
        if 'sha256' not in t and not q.endswith('act_roots.txt') and not q.endswith('_hashes.txt'):
            continue
        for i, l in enumerate(t.split(NL), 1):
            if 'sha256' in l or q.endswith('act_roots.txt') or q.endswith('_hashes.txt'):
                for m in re.finditer(r'(?<![0-9a-f])([0-9a-f]{64})(?![0-9a-f])', l):
                    out.setdefault(m.group(1)[:8], ('data/' + os.path.basename(q), i))
    for kd in sorted(d_ for d_ in os.listdir('D:/') if d_.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d_, '.git'))):
        for f in ('lakefile.toml', 'lakefile.lean', 'lake-manifest.json'):
            t = rd(os.path.join('D:/', kd, f)) or ''
            for i, l in enumerate(t.split(NL), 1):
                for m in re.finditer(r'(?:rev\s*=\s*"|"rev"\s*:\s*"|@\s*"|rev\s+")([0-9a-f]{40})"', l):
                    out.setdefault(m.group(1)[:8], ('%s/%s' % (kd, f), i))
    return out


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b708, and b706's repair carried: before b682's body runs, every eight-hex
    token of the answer that a bank's row names as a sha256 is checked against that row and printed, and masked from b682's commit reading."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b708'))
    shas = _sha_rows()
    base = P.C._user_texts

    def masked(*k, **kw):
        out = []
        for t in base(*k, **kw):
            if t and needle in t:
                for m in _HEX8.finditer(t):
                    h8 = m.group(1)
                    if h8 in shas:
                        print('  ### SHA256 PREFIX %s... NAMED BY %s :%d -- a root or file hash by its bank`s row, not a commit; OK, masked from the commit reading' % (h8, shas[h8][0], shas[h8][1]))
                        t = t.replace(h8, 'SHA-' + h8[:4] + '-' + h8[4:])
            out.append(t)
        return out

    P.C._user_texts = masked
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b708')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b708)', 'exec'), ns)
    ns['answer'](needle)


def word(needle, *a):
    """(R278)(4) on an author's word delivered as a bare BEGIN ... END paste: b694's route."""
    import b682_citation as P
    base = C._user_texts

    def marked(*k, **kw):
        return [("THE AUTHOR'S WORD " + t) if (t or '').lstrip().startswith(('BEGIN', '<pasted_content')) and 'END' in (t or '') else t
                for t in base(*k, **kw)]

    C._user_texts = marked
    P.C._user_texts = marked
    answer(needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer, 'word': word}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b708_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
