# -*- coding: utf-8 -*-
"""b703_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b703's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (e5bcf1d0, the session b701 and b702 ran in; the anchor (R313)'s line is unique in it); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b703 and its commit reach widened to the kernels as b699-b702 widened it; the `word`
### route is b694's.
### Routes: `check [dry]` -> data/b703_citation_check.txt (.json) ; `ferry` -> data/b703_ferry_scan.txt ; `answer <needle>` / `word <needle>` ->
###         the check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b703 from b702_citation.py's form; this tool writes only the banks named above.
"""
import glob
import gzip   # noqa: F401  ### not used: the compressed bank is read by its named reader alone
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
import b703_worklist as K   # noqa: E402

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

HEAD_QUOTE = 'b702 closed: relay ca46b729, PLACE-papers 79266e3; suite 126 of 127; root 5631217833cd6085\u2026; 7 prompts answered; 9 defects'


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


def _find_in(paths, needle):
    """the first (path, line) carrying the needle among the named files, read by this tool."""
    for q in paths:
        n = first(lines_of(q), needle)
        if n:
            return os.path.relpath(q, ROOT).replace(os.sep, '/'), n
    return '', 0


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    ot, fi = lines_of(OT), lines_of(FI)
    EF = K.EF_DIR
    # ### the ferry's read-first list
    for f in ('data/b702_closing.txt', 'data/b702_defects.txt', 'data/b702_tool_repairs.txt', 'data/b702_closing_push_out.txt', 'data/b701_obstruction.txt',
              'data/b701_widening_plan.txt', 'data/b701_epstein_plan.txt', 'data/b698_regularity_uses.txt', 'data/b702_circuit_spec.txt',
              'data/b681_epstein_zeros_narrowed_hashes.txt', 'data/b681_findings.json', 'data/b698_rules.txt', 'data/b690_rules.txt',
              'data/b681_epstein_zeros_narrowed.json.gz', 'data/b675_corrigenda.txt', 'tools/rule_arms.py', 'tools/circuit_read.py'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    for f in (K.OT_ARCHIVE2, K.LOOM_ARCHIVE, K.INSTRUMENTS, 'REGISTRY.md', 'README.md'):
        add('ferry read-first', 'PLACE-papers %s' % f, os.path.exists(os.path.join(PP, f)), 'exists at the working tree', '0')
    cl = lines_of(p('data', 'b702_closing.txt'))
    add('ferry read-first; ruling (1)', 'data/b702_closing.txt :1, the head line, against (R313)(1)`s quote after whitespace is removed', _ws(cl[0]) == _ws(HEAD_QUOTE),
        'data/b702_closing.txt :1 = %r' % cl[0][:130], '0-1')
    cf = first(cl, '### CARRIED FORWARD.')
    add('ferry read-first', 'data/b702_closing.txt, the carried-forward rows (a)-(h) by line', cf > 0 and first(cl, '    (a) ', cf) > 0 and first(cl, '    (h) ', cf) > 0,
        'data/b702_closing.txt :%d (the head), (a) :%d, (h) :%d' % (cf, first(cl, '    (a) ', cf), first(cl, '    (h) ', cf)), '0-1')
    po = rd(p('data', 'b702_closing_push_out.txt')) or ''
    add('ruling (1); ruling (9)', 'the closing commit 8773acc9 pushed and read back equal at the remote (data/b702_closing_push_out.txt, to be committed)',
        'main read back at the remote: 8773acc9' in po and g(ROOT, 'rev-parse', '--short=8', 'HEAD')[1].strip() == '8773acc9',
        'data/b702_closing_push_out.txt (capture-on lines %d) ; relay HEAD %s' % (po.count('capture on'), g(ROOT, 'rev-parse', '--short=8', 'HEAD')[1].strip()), '0-1')
    df = lines_of(p('data', 'b702_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", NL.join(df), re.M)
    add('ferry read-first; ruling (1)', 'data/b702_defects.txt (rows are defects as lettered): nine, (a)-(i), (d) and (e) the navigator`s', [x for x, _o in lt] == list('abcdefghi')
        and [x for x, o in lt if o == 'NAVIGATOR'] == ['d', 'e'], 'letters %s ; the navigator`s %s' % (''.join(x for x, _o in lt), [x for x, o in lt if o == 'NAVIGATOR']), '0-1')
    tr = lines_of(p('data', 'b702_tool_repairs.txt'))
    add('ferry read-first', 'data/b702_tool_repairs.txt (rows are repairs): four', first(tr, 'REPAIRS 4') > 0, 'data/b702_tool_repairs.txt :%d (the count line)' % first(tr, 'REPAIRS 4'), '0-1')
    cut = json.loads(rd(p('data', 'b702_cut.json')) or '{}')
    ct = lines_of(p('data', 'b702_cut.txt'))
    add('ruling (1)', 'the cut at PLACE-papers a1d5d59, distance 24 to 2 by the b670 method, the cells :282 and :283 held, 46 quoting lines, record lines :7 and :272 named stale',
        commit_in(PP, 'a1d5d59') and cut.get('before') == 24 and cut.get('after') == 2 and first(ct, 'QUOTING LINES 46') > 0 and first(ct, ':282') > 0 and first(ct, ':283') > 0,
        'data/b702_cut.json before %r after %r held %r ; data/b702_cut.txt :%d (the quoting lines), :%d (:282), :%d (:283)' % (
            cut.get('before'), cut.get('after'), cut.get('held'), first(ct, 'QUOTING LINES 46'), first(ct, ':282'), first(ct, ':283')), '1')
    fc = (g(PP, 'show', '--stat', '--format=%s', '65a8367')[1] or '')
    add('ruling (1)', 'the faces page regenerated at three lines (65a8367), the third :191`s Placement row', commit_in(PP, '65a8367') and K.FACES_PAGE in fc,
        'PLACE-papers 65a8367 %r' % fc.split(NL)[0][:110], '1')
    rb = lines_of(p('data', 'b702_readme_readback.txt'))
    add('ruling (1)', 'the README`s sharpened ceiling append (d5f8a03), its blob c72e8edb read back at the remote and equal', commit_in(PP, 'd5f8a03') and first(rb, 'c72e8edb, EQUAL') > 0,
        'data/b702_readme_readback.txt :%d' % first(rb, 'c72e8edb, EQUAL'), '1')
    for n in K.ORDERS_B702:
        add('ruling (1); ferry read-first', 'OPEN_TRAILS :%d (b702`s orders, :15444-:15456)' % n, 'b702' in at(ot, n), 'OPEN_TRAILS :%d %r' % (n, at(ot, n)[:110]), '0-1')
    ar = json.loads(rd(p('data', 'b702_act_root.json')) or '{}')
    named = [it.split()[0] for it in ar.get('items') or [] if it.startswith('data/')]
    add('ruling (1)', 'the root 56312178 over 77 banks chained from 663799f0', (ar.get('root') or '').startswith('56312178') and len(named) == 77 and (ar.get('prev') or ar.get('previous') or '').startswith('663799f0'),
        'data/b702_act_root.json (root %s, banks %d, prev %s)' % ((ar.get('root') or '')[:8], len(named), (ar.get('prev') or ar.get('previous') or '')[:8]), '1')
    ck, cp = rd(p('data', 'b702_checks.txt')) or '', rd(p('data', 'b702_checks_postpush.txt')) or ''
    add('ruling (1)', 'suite 126 of 127 pre-push and post-push, G-RULE-RECUT-QUOTE carried', 'ARMS RUN : 127. ### LIVE PASSING : 126.' in ck and 'ARMS RUN : 127. ### LIVE PASSING : 126.' in cp
        and "['G-RULE-RECUT-QUOTE']" in ck and "['G-RULE-RECUT-QUOTE']" in cp, 'data/b702_checks.txt ; data/b702_checks_postpush.txt', '1')
    face = rd(p(*K.B702_FACE.split('/'))) or ''
    add('ruling (1)', 'G-RULE-RECUT-QUOTE declared on the face', 'G-RULE-RECUT-QUOTE' in face, K.B702_FACE, '1')
    sc = rd(p('data', 'b702_scores_close.json')) or ''
    add('ruling (1)', 'all eight scores held', sc.count('"HELD"') >= 8, 'data/b702_scores_close.json (HELD %d)' % sc.count('"HELD"'), '1')
    mi = lines_of(p('data', 'b702_mirror.txt'))
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-21-b702.zip, sha256 b4ded385, CLEAN on all three clauses over 83 files, built after 79266e3', first(mi, 'sha256 b4ded385') > 0
        and first(mi, 'CLEAN ON ALL THREE CLAUSES') > 0 and first(mi, 'ROSTER: 83 files') > 0 and first(mi, 'PLACE-papers HEAD AT THE BUILD : 79266e3') > 0, 'data/b702_mirror.txt :%d' % first(mi, 'sha256 b4ded385'), '1')
    add('ruling (1)', 'b702`s entry at FINDINGS :9840, b701`s weight :9824, the corrigendum :9826, the trail OPEN_TRAILS :15458', at(fi, K.B702_ENTRY).startswith('## ') and 'b701' in at(fi, K.B702_WEIGHT)
        and at(ot, K.B702_TRAIL).startswith('### b702'), 'FINDINGS :%d %r ; OPEN_TRAILS :%d' % (K.B702_ENTRY, at(fi, K.B702_ENTRY)[:80], K.B702_TRAIL), '1')
    # ### (R313)(2)
    sp_ = first(mi, '### THE SPAN:')
    add('ruling (2) (j)', 'the mirror bank`s span line names b697`s export', 'b697' in at(mi, sp_), 'data/b702_mirror.txt :%d %r' % (sp_, at(mi, sp_)[:120]), '1')
    m98 = lines_of(p('tools', 'b698_record.py'))
    s98 = first(m98, '### THE SPAN:')
    mloc = _find_in(sorted(glob.glob(p('tools', 'b6*_record.py'))), '### THE SPAN:')
    b702r = rd(p('tools', 'b702_record.py')) or ''
    add('ruling (2) (j); ferry read-first', 'the mirror tool`s span line, carried as wording from b698`s tool (b702_record imports b698_record)', s98 > 0 and 'b697' in at(m98, s98) and 'import b698_record as R' in b702r,
        'tools/b698_record.py :%d %r ; the earliest record tool carrying the line %s :%d' % (s98, at(m98, s98).strip()[:90], mloc[0], mloc[1]), '1')
    add('ruling (2) (k)', 'the closing push`s opening call stopping at exit 128, both calls in data/b702_closing_push_out.txt', po.count('capture on') == 2 and 'cannot change' in po,
        'data/b702_closing_push_out.txt: capture-on lines %d ; the git error of the first call in the capture %s' % (po.count('capture on'), 'cannot change' in po), '1')
    ra = lines_of(p('tools', 'rule_arms.py'))
    qa = first(ra, "'G-RULE-RECUT-QUOTE'")
    add('ruling (2); ferry read-first', 'the quote arm G-RULE-RECUT-QUOTE by path and line', qa > 0, 'tools/rule_arms.py :%d' % qa, '1')
    add('ruling (2)', 'b697`s kernel cut bank and b702`s paper cut bank for the arm`s control', bool(glob.glob(p('data', 'b697_quote_*.json'))) and os.path.exists(p('data', 'b702_cut.json')),
        'data/%s ; data/b702_cut.json' % ', '.join(os.path.basename(x) for x in glob.glob(p('data', 'b697_quote_*.json'))), '1')
    add('ruling (2)', 'b676`s quote form (data/b676_cut.txt) and the b670 form (data/b670_rules.txt)', os.path.exists(p('data', 'b676_cut.txt')) and os.path.exists(p('data', 'b670_rules.txt')), 'exist', '1')
    add('ruling (2)', 'data/b703_defects.txt and data/b703_tool_repairs.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b703_defects.txt')) and not os.path.exists(p('data', 'b703_tool_repairs.txt')), 'absent, as ordered', '1')
    nl_ = lines_of(p('data', 'b681_narrow.txt'))
    add('ruling (2)', 'data/b681_narrow.txt :5-:40, rows of the narrowing bank (OFF 0-16, ON 0-18)', at(nl_, 5).startswith('  OFF 0') and at(nl_, 40).startswith('  ON  18'), 'data/b681_narrow.txt :5, :40', '1')
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    lastrow = max([int(m) for m in re.findall(r'^  \((\d+)\) ', NL.join(cg), re.M)] or [0])
    add('ruling (2)', 'the corrigenda bank, appended only', lastrow > 0, 'data/b675_corrigenda.txt, last row (%d) at :%d' % (lastrow, first(cg, '  (%d) ' % lastrow)), '1')
    add('ruling (2)', 'b702`s corrigendum tool to carry', os.path.exists(p('tools', 'b702_corrigendum.py')), 'tools/b702_corrigendum.py', '1')
    # ### (R313)(3)
    add('ruling (3)', 'OPEN_TRAILS :15410, W-ORD-CLASSK-WIDENING-HELD', 'W-ORD-CLASSK-WIDENING-HELD' in at(ot, K.ORDER_HELD), 'OPEN_TRAILS :%d' % K.ORDER_HELD, '2')
    ob = lines_of(p('data', 'b701_obstruction.txt'))
    add('ruling (3); ferry read-first', 'data/b701_obstruction.txt: the error at H2SignWide.lean :59, le_rfl, the repair one_ne_zero', first(ob, 'H2SignWide.lean:59') > 0 and first(ob, 'le_rfl') > 0 and first(ob, 'one_ne_zero') > 0,
        'data/b701_obstruction.txt :%d (the error), :%d (le_rfl), :%d (the repair)' % (first(ob, 'H2SignWide.lean:59'), first(ob, 'le_rfl'), first(ob, 'one_ne_zero')), '2')
    wt = g(EF, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.WIDEN_BRANCH)[1].strip()
    rh = _remote_heads(EF)
    add('ruling (3)', 'widening-b701 at 8a4ab68, local and remote', wt == K.WIDEN_TIP and rh.get('refs/heads/widening-b701') == K.WIDEN_TIP,
        'local %s ; remote %s (one ls-remote of SIDE-explicit-formula)' % (wt[:7], (rh.get('refs/heads/widening-b701') or '-')[:7]), '2')
    hw = (g(EF, 'ls-tree', '-r', '--name-only', K.WIDEN_TIP)[1] or '').split(NL)
    hwp = next((x for x in hw if x.endswith('H2SignWide.lean')), '')
    h59 = ((g(EF, 'show', '%s:%s' % (K.WIDEN_TIP, hwp))[1] or '').split(NL) + [''] * 60)[58] if hwp else ''
    add('ruling (3)', 'H2SignWide.lean :59 at 8a4ab68 carries ContDiff.differentiable le_rfl (dot notation, hf.deriv`.differentiable, at column 42)', "hf.deriv'.differentiable le_rfl" in h59
        and h59.find('le_rfl') == 42, '%s :59 %r ; the first le_rfl at 0-based column %d (Lean`s :59:42 counts from 0)' % (hwp, h59.strip()[:100], h59.find('le_rfl')), '2')
    v35 = g(EF, 'rev-parse', 'v0.35^{commit}')[1].strip()
    v36 = g(EF, 'rev-parse', '--verify', '--quiet', 'refs/tags/v0.36')[1].strip()
    add('ruling (3)', 'v0.35 the current tag, v0.36 not yet made', v35 == K.EF_V035 and not v36, 'v0.35 peels %s ; v0.36 %s' % (v35[:7], v36[:7] or 'ABSENT'), '2')
    r98, r90 = lines_of(p('data', 'b698_rules.txt')), lines_of(p('data', 'b690_rules.txt'))
    add('ruling (3); ferry read-first', 'data/b698_rules.txt row (1), a tag move regenerates the cells', first(r98, "(1) A KERNEL'S TAG MOVE REGENERATES THE CORRESPONDENCE CELLS") > 0, 'data/b698_rules.txt :%d' % first(r98, "(1) A KERNEL'S TAG MOVE"), '2')
    add('ferry read-first', 'data/b690_rules.txt row (2), the quotation search', first(r90, '(2) AT A RE-CUT') > 0, 'data/b690_rules.txt :%d' % first(r90, '(2) AT A RE-CUT'), '0')
    gl = lines_of(p('data', 'b701_glossary_rows.txt'))
    add('ruling (3)', 'the glossary`s classK` row held at b702 (data/b701_glossary_rows.txt)', first(gl, 'classK') > 0, 'data/b701_glossary_rows.txt :%d' % first(gl, 'classK'), '2')
    add('ruling (3)', 'data/b703_widening_grade.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b703_widening_grade.txt')), 'absent, as ordered', '2')
    # ### (R313)(4)
    ep = lines_of(p('data', 'b701_epstein_plan.txt'))
    add('ruling (4); ferry read-first', 'data/b701_epstein_plan.txt: the opening step, its kernel and branch named', first(ep, 'THE OPENING STEP 1 DISPATCH') > 0,
        'data/b701_epstein_plan.txt :%d (the price) ; the kernel/branch lines %s' % (first(ep, 'THE OPENING STEP 1 DISPATCH'), [i + 1 for i, l in enumerate(ep) if 'branch' in l.lower()][:6]), '2')
    add('ruling (4)', 'data/b703_epstein_grade.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b703_epstein_grade.txt')), 'absent, as ordered', '2')
    # ### (R313)(5)
    add('ruling (5)', 'SIDE-explicit-formula lean-toolchain and lake-manifest.json at its current tag v0.35', bool(g(EF, 'cat-file', '-e', 'v0.35:lean-toolchain')[0] == 0) and g(EF, 'cat-file', '-e', 'v0.35:lake-manifest.json')[0] == 0,
        'v0.35:lean-toolchain, v0.35:lake-manifest.json', '3')
    lvc = g(K.LV_DIR, 'rev-parse', '--short=7', 'v0.10.0^{commit}')[1].strip()
    add('ruling (5)', 'SIDE-lv-conservation v0.10.0 = 93c27ec, the deposit', lvc == K.LV_V0100 and g(K.LV_DIR, 'cat-file', '-e', 'v0.10.0:lean-toolchain')[0] == 0, 'v0.10.0 peels %s' % lvc, '3')
    add('ruling (5)', 'D:\\relay\\scratch\\interval-b703 -- TO BE CLONED in its own message', not os.path.exists(K.INTERVAL_SCRATCH), 'absent, as ordered', '3')
    add('ruling (5)', 'BINDER-PROVENANCE named in data/b702_circuit_spec.txt (twelve rows)', 'BINDER-PROVENANCE' in (rd(p('data', 'b702_circuit_spec.txt')) or '') and 'ROWS 12' in (rd(p('data', 'b702_circuit_spec.txt')) or ''),
        'data/b702_circuit_spec.txt :%d' % first(lines_of(p('data', 'b702_circuit_spec.txt')), 'BINDER-PROVENANCE'), '0-3')
    jo = first(ot, 'W-ORD-LV-CLOSURE-JOIN')
    add('ruling (5)', 'W-ORD-LV-CLOSURE-JOIN at its line', jo > 0, 'OPEN_TRAILS :%d' % jo, '3')
    # ### (R313)(6)
    hb = lines_of(p(*K.Q0_HASHES.split('/')))
    add('ruling (6)(i); ferry read-first', 'data/b681_epstein_zeros_narrowed_hashes.txt :2-:3, the json and the .gz sha256', at(hb, 2).startswith('data/b681_epstein_zeros_narrowed.json (inside the .gz) sha256')
        and at(hb, 3).startswith('data/b681_epstein_zeros_narrowed.json.gz sha256'), 'data/b681_epstein_zeros_narrowed_hashes.txt :2, :3', '3')
    fj = json.loads(rd(p('data', 'b681_findings.json')) or '{}')
    add('ruling (6)(i); ferry read-first', 'data/b681_findings.json :2, the stated 163', 'The 163 certified zeros of Q0' in (fj.get('title') or ''), 'data/b681_findings.json :2', '3')
    rloc = _find_in(sorted(glob.glob(p('data', 'b67[0-9]_*.txt'))) + sorted(glob.glob(p('data', 'b68[01]_*.txt'))), K.RHO0_RE)
    add('ruling (6)(i)', 'ρ₀ at Re 0.95326047479466068625 in a text bank (the control`s digits)', rloc[1] > 0, 'data: %s :%d' % rloc, '3')
    add('ruling (6)(i)', 'tools/b703_q0_zeros_read.py, data/b703_q0_band.txt, data/b703_registrations.txt -- TO BE WRITTEN', not any(os.path.exists(p(*x.split('/'))) for x in (
        'tools/b703_q0_zeros_read.py', 'data/b703_q0_band.txt', 'data/b703_registrations.txt')), 'absent, as ordered', '0-3')
    bl = g(EF, 'grep', '-n', 'blTerm_nonneg_of_onLine', 'v0.35', '--', '*.lean')[1] or ''
    add('ruling (6)(ii)', 'blTerm_nonneg_of_onLine (git grep bounded to the kernel`s source at v0.35)', bool(bl.strip()), (bl.split(NL)[0] if bl.strip() else 'NOT FOUND in SIDE-explicit-formula at v0.35')[:120], '0')
    b675 = sorted(glob.glob(p('data', 'b675_*.txt')))
    add('ruling (6)(ii)', 'b675`s route and figure (its banks)', bool(b675), 'data/b675_*.txt %d banks' % len(b675), '0')
    b518 = sorted(glob.glob(p('data', 'b518_*')))
    add('ruling (6)(ii)', 'b518`s notched Weil window (its banks)', bool(b518), 'data/b518_* %d banks' % len(b518), '0')
    ins = lines_of(os.path.join(PP, K.INSTRUMENTS))
    i5 = first(ins, '## I-5')
    add('ruling (6)(iii); ferry read-first', 'INSTRUMENTS I-5 and its record form (a)-(d) by line', i5 > 0 and first(ins, '- **(a) Trigger', i5) > 0 and first(ins, '- **(d) VERDICT', i5) > 0,
        'INSTRUMENTS.md :%d (I-5), :%d (a), :%d (d)' % (i5, first(ins, '- **(a) Trigger', i5), first(ins, '- **(d) VERDICT', i5)), '0')
    add('ferry read-first; ruling (6)(iv)', 'INSTRUMENTS.md :114-:154 (I-6 at :126, axis (b) at :134 naming W-SIGN-7)', at(ins, 126).startswith('## I-6') and 'W-SIGN-7' in at(ins, 134), 'INSTRUMENTS.md :126, :134', '0')
    nb = g(EF, 'grep', '-n', '-e', 'rh_iff_nb', '-e', 'NymanBeurlingPremise', 'v0.24', '--', '*.lean')[1] or ''
    add('ruling (6)(iii)', 'rh_iff_nb (v0.24) and NymanBeurlingPremise (git grep bounded to the kernel`s source at v0.24)', 'rh_iff_nb' in nb and 'NymanBeurlingPremise' in nb,
        ('%d lines ; first %r' % (len([x for x in nb.split(NL) if x.strip()]), nb.split(NL)[0][:100])) if nb.strip() else 'NOT FOUND in SIDE-explicit-formula at v0.24', '0')
    a2 = lines_of(os.path.join(PP, K.OT_ARCHIVE2))
    add('ruling (6)(iv); ferry read-first', 'OPEN_TRAILS-archive-2 :2087-:2093 (W-MINE-QUADRATIC :2087, W-SIGN-7 :2089, W-FAMILY :2091, W-SUBSTRATE :2093)', at(a2, 2087).startswith('**W-MINE-QUADRATIC closed')
        and at(a2, 2089).startswith('**W-SIGN-7 closed (2026-07-27).**') and at(a2, 2091).startswith('**W-FAMILY closed') and at(a2, 2093).startswith('**W-SUBSTRATE'), 'archive-2 :2087-:2093', '0')
    lo = lines_of(os.path.join(PP, K.LOOM_ARCHIVE))
    add('ruling (6)(iv); ferry read-first', 'the loom archive :2671-:2825 (W-SIGN-7 at :2671)', 'W-SIGN-7' in at(lo, 2671) and 'W-SIGN-7' in at(lo, 2825), 'loom archive :2671 %r ; :2825 carries W-SIGN-7 %s' % (at(lo, 2671)[:70], 'W-SIGN-7' in at(lo, 2825)), '0')
    add('ruling (6)(iv)', 'data/b703_wsign7.txt -- TO BE WRITTEN at step zero', not os.path.exists(p('data', 'b703_wsign7.txt')), 'absent, as ordered', '0')
    # ### (R313)(7)-(8)
    sa = first(ot, 'W-ORD-STANDING-ARMS-B703')
    add('ruling (7)', 'W-ORD-STANDING-ARMS-B703 at its line', sa > 0, 'OPEN_TRAILS :%d' % sa, '4')
    add('ruling (7)', 'data/b672_one_copy.txt (rows are the 25 documents with their copies), the partner copies', os.path.exists(p('data', 'b672_one_copy.txt')), 'data/b672_one_copy.txt', '4')
    kh = first(ot, 'W-ORD-KEYSTONE-HEADS')
    add('ruling (8)', 'W-ORD-KEYSTONE-HEADS at its line, its trigger "the re-cut act b704"', kh > 0 and 'the re-cut act b704' in at(ot, kh), 'OPEN_TRAILS :%d' % kh, '4')
    add('ruling (8)', 'data/b703_rules.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b703_rules.txt')), 'absent, as ordered', '4')
    # ### (R313)(9)
    for repo, bs in K.DELETE:
        mg = (g(repo, 'branch', '--merged', 'main')[1] or '').replace('*', ' ').split()
        for b in bs:
            add('ruling (9)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in mg, 'listed by `git branch --merged main` at %s before any delete' % os.path.basename(repo) if b in mg else '### NOT LISTED', '0')
    # ### (R313)(10)-(12) and the ferry
    add('ruling (10)', 'the READFIRST-CLOSURE reader', 'readfirst' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py', '0')
    add('ruling (11)', 'the draft at v5, held', K.DRAFT == '23228113', 'tools/b703_worklist.py DRAFT', '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C5', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''), 'tools/b693_worklist.py :52', '5')
    add('ferry C0', 'data/b684_rules.txt row (1), a test above 450 s its own part', '(1) A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5', '0')
    add('ferry C6', 'b673`s capture names', os.path.exists(p('data', 'b702_relay_push_out.txt')), 'data/b702_relay_push_out.txt (the form carried)', '6')
    add('ferry C6', 'the b670 form of the mirror', os.path.exists(p('data', 'b702_mirror.txt')), 'data/b702_mirror.txt (the form carried)', '6')
    add('ruling; ferry', 'data/b703_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b703_readfirst.txt')), '0')
    return R


def _write(L, R, miss):
    for name, data in (('b703_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b703_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b703 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    if 'dry' in a:
        print(NL.join(L))
        return
    _write(L, R, miss)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    """the ferry is banked by the Write tool (data/b703_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b703_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b703_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b703_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b703."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, 'D:/SIDE-lv-conservation', 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects') if r not in P.REPOS)
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b703'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b703')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b703)', 'exec'), ns)
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
        print('usage: b703_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
