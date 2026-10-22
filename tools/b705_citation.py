# -*- coding: utf-8 -*-
"""b705_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b705's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (44411d52, a new session after the author's /clear; the anchor (R315)'s line is unique in it); the answer route is b682's, imported
### from tools/b682_citation.py with its act names pointed at b705 and its commit reach widened to the kernels as b699-b704 widened it; the
### `word` route is b694's.
### Routes: `check [dry]` -> data/b705_citation_check.txt (.json) ; `ferry` -> data/b705_ferry_scan.txt ; `answer <needle>` / `word <needle>` ->
###         the check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b705 from b704_citation.py's form; this tool writes only the banks named above.
"""
import glob
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
import b705_worklist as K   # noqa: E402

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

HEAD_QUOTE = 'b704 closed: relay 3f2abacc, PLACE-papers d668413; suite 132 of 140; root 97bd213337dd2e17\u2026; 13 prompts answered; 19 defects'
EIGHT = ['G-WORKFLOW-FILES', 'G-ACTROOT-BANKED', 'G-READ-RULE-STANDING', 'G-README-CURRENCY', 'G-ANSWERS-CHECKED', 'G-TRAIL-LINES-EQUAL-DEFECTS',
         'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-RESOLVED-EQUAL']


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


def _kgrep(repo, rev, needle, path):
    out = g(repo, 'grep', '-n', '-F', '-e', needle, rev, '--', path)[1] or ''
    return out.split(NL)[0] if out.strip() else ''


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    RM = os.path.join(PP, 'README.md')
    ot, fi, rm = lines_of(OT), lines_of(FI), lines_of(RM)
    EF, LV = K.EF_DIR, K.LV_DIR
    # ### the ferry's read-first list
    for f in ('data/b704_closing.txt', 'data/b704_defects.txt', 'data/b704_standing_figures.txt', 'data/b704_cells_reach.txt', 'data/b704_faces_diff.txt',
              'data/b704_tool_repairs.txt', 'data/b704_closing_push_out.txt', 'data/b703_pins.txt', 'data/b703_registrations.txt', 'data/b703_q0_band.txt',
              'data/b703_wsign7.txt', 'data/b703_widening_grade.txt', 'data/b701_correspondence_restatement.txt', 'data/b680_rules.txt', 'data/b690_rules.txt',
              'tools/b694_witness_terms.py', 'tools/b326_windows.py', 'tools/e0_rule.py', 'tools/b703_standing_figures.py', 'tools/b675_li_bench.py'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    add('ferry read-first', 'tools/b696_tails.py, "the b696 tail-ball tool"', os.path.exists(p('tools', 'b696_tails.py')),
        'tools/b696_tails.py %s ; the tail-ball tool of b696 is tools/b696_witness_balls.py (%s), its zero tail at :124-:146' % (
            'exists' if os.path.exists(p('tools', 'b696_tails.py')) else 'DOES NOT EXIST', 'exists' if os.path.exists(p('tools', 'b696_witness_balls.py')) else 'absent'), '0-3')
    add('ferry read-first', 'tools/b675_<li route>.py, "b675`s route" of (R315)(7)(i)', os.path.exists(p('tools', 'b675_li_bench.py')),
        'the placeholder names no path; the Li route of b675 is tools/b675_li_bench.py (constants_for :163, onset :153, P :97)', '0-3')
    for f, needle in (('tools/b696_witness_balls.py', 'def zero_tail('), ('tools/b694_witness_terms.py', 'LADDER = ('), ('tools/b326_windows.py', 'def kernel_q_derived('),
                      ('tools/e0_rule.py', 'MET = ('), ('tools/b703_standing_figures.py', 'def readme('), ('tools/b698_record.py', 'def root_banks():'),
                      ('tools/b698_record.py', 'ROOT_EXCLUDE = re.compile('), ('tools/b704_record.py', 'R.ROOT_EXCLUDE = re.compile(')):
        n = first(lines_of(p(*f.split('/'))), needle)
        add('ferry read-first', '%s %s' % (f, needle.rstrip('(').rstrip(':')), n > 0, '%s :%d' % (f, n), '0')
    n = first(lines_of(p('tools', 'b326_windows.py')), 'def kernel_q_derived(')
    add('ferry read-first', 'tools/b326_windows.py :220-:228, the bracket for Z_Q', n == 220, 'kernel_q_derived opens at :%d' % n, '3')
    n = first(lines_of(p('tools', 'e0_rule.py')), 'MET = (')
    add('ferry read-first; ruling (9)', 'tools/e0_rule.py`s MET list (OPEN_TRAILS :15506 cites :308-:315)', n == 308, 'MET opens at :%d' % n, '4')
    ins = lines_of(os.path.join(PP, *K.INSTRUMENTS.split('/')))
    add('ferry read-first; ruling (8)', 'INSTRUMENTS.md :114-:154 (the file at PLACE-papers phase1.5/method/INSTRUMENTS.md), I-6 at :126, its table :131-:138, axis (b) at :134',
        first(ins, '## I-6') == 126 and 'cover' in at(ins, 134) and 'W-SIGN-7' in at(ins, 134) and 'Score the visibility change' in at(ins, 140),
        'I-6 head :%d ; :134 %r ; the measures at :140' % (first(ins, '## I-6'), at(ins, 134)[:60]), '4')
    # ### (R315)(1), by row
    cl = lines_of(p('data', 'b704_closing.txt'))
    add('ferry read-first; ruling (1)', 'data/b704_closing.txt :1, the head line, against (R315)(1)`s quote after whitespace is removed', _ws(cl[0]) == _ws(HEAD_QUOTE),
        'data/b704_closing.txt :1 = %r' % cl[0][:130], '0-1')
    cf = first(cl, '### CARRIED FORWARD.')
    add('ferry read-first', 'data/b704_closing.txt, the carried-forward rows (a)-(h) by line', cf > 0 and first(cl, '    (a) ', cf) > 0 and first(cl, '    (h) ', cf) > 0,
        'data/b704_closing.txt :%d (the head), (a) :%d, (h) :%d' % (cf, first(cl, '    (a) ', cf), first(cl, '    (h) ', cf)), '0-1')
    po = rd(p('data', 'b704_closing_push_out.txt')) or ''
    head = g(ROOT, 'rev-parse', '--short=8', 'HEAD')[1].strip()
    add('ruling (1); ruling (10)', 'the closing commit f5a35af1 pushed alone and read back at the remote (data/b704_closing_push_out.txt, to be committed)',
        'main read back at the remote: f5a35af1' in po and head == 'f5a35af1',
        'data/b704_closing_push_out.txt (capture-on lines %d) ; relay HEAD %s' % (po.count('capture on'), head), '0-1')
    st = g(ROOT, 'status', '--porcelain', '--', 'data/b704_closing_push_out.txt')[1].strip()
    add('ruling (10)', 'data/b704_closing_push_out.txt uncommitted at the act`s start', st.startswith('??'), 'git status %r' % st, '0')
    pr = rd(p('data', 'b704_runner_SIDE-explicit-formula_probe.txt')) or ''
    add('ruling (1)', 'the faces page at v0.37 from probe run 39721668586, 568 of 568 cells', 'RUN 39721668586 (probe)' in pr and 'PROBE CELLS 568 OF 568' in pr,
        'data/b704_runner_SIDE-explicit-formula_probe.txt', '1')
    rh = _remote_heads(EF)
    pb = g(EF, 'branch', '--list', 'probe-b704')[1].strip()
    add('ruling (1)', 'probe-b704 deleted after, local and remote; SIDE-explicit-formula main and tags untouched (main 38e2734 = v0.37)',
        not pb and 'refs/heads/probe-b704' not in rh and (rh.get('refs/heads/main') or '').startswith('38e2734') and g(EF, 'rev-parse', 'main')[1].strip() == K.EF_V037,
        'local %s ; remote heads %d (probe-b704 %s ; main %s) -- one ls-remote of SIDE-explicit-formula' % (
            pb or 'absent', len(rh), 'present' if 'refs/heads/probe-b704' in rh else 'absent', (rh.get('refs/heads/main') or '-')[:7]), '1')
    fd = lines_of(p('data', 'b704_faces_diff.txt'))
    add('ruling (1); ferry read-first', 'data/b704_faces_diff.txt (rows are changed lines): six lines each with its cause; h2_sign_sum_iff_rh and h2_sign`_imp_rh as nodes',
        first(fd, 'CHANGED LINES 6 ; WITH A CAUSE 6 ; WITHOUT 0') > 0 and first(fd, 'h2_sign_sum_iff_rh') > 0 and first(fd, "h2_sign'_imp_rh") > 0,
        'data/b704_faces_diff.txt :%d (the verdict) ; the nodes at :%d, :%d' % (first(fd, 'CHANGED LINES 6'), first(fd, 'h2_sign_sum_iff_rh'), first(fd, "h2_sign'_imp_rh")), '1')
    cr = rd(p('data', 'b704_correspondence_run.txt')) or ''
    add('ruling (1)', 'the generator writing 0 cells, SIDE-explicit-formula outside its 16 parsed kernels', 'CELLS CHANGED 0' in cr and 'KERNELS 16' in cr,
        'data/b704_correspondence_run.txt', '1')
    cre = lines_of(p('data', 'b704_cells_reach.txt'))
    add('ruling (1); ferry read-first', 'data/b704_cells_reach.txt (rows are (line, theorem, tag) mentions): 15 read, 4 equal, 0 differs, 11 unbanked',
        first(cre, 'EQUAL 4 ; differs 0 ; unbanked 11') > 0 and first(cre, 'MENTIONS READ 15 (LINES 11)') > 0,
        'data/b704_cells_reach.txt :%d, :%d' % (first(cre, 'EQUAL 4 ; differs 0'), first(cre, 'MENTIONS READ 15')), '1')
    rmd = rd(p('data', 'b704_readme.txt')) or ''
    blob = g(PP, 'rev-parse', '05c6dd6:README.md')[1].strip()
    add('ruling (1)', 'the README`s kernel line at :164 (v0.37 = 38e2734) and the append at :135, PLACE-papers 05c6dd6, its blob 9a8ff6ce',
        'THE KERNEL LINE AT :164 ; THE APPEND AT :135' in rmd and blob.startswith('9a8ff6ce') and 'v0.37' in at(rm, 164) and '38e2734' in at(rm, 164)
        and at(rm, 135).startswith("*(Appended under the author's ruling `(R314)`(5)"),
        'data/b704_readme.txt ; 05c6dd6:README.md blob %s ; README :164 names v0.37 %s ; :135 the (R314)(5) append %s' % (
            blob[:8], 'v0.37' in at(rm, 164), at(rm, 135).startswith("*(Appended under the author's ruling `(R314)`(5)")), '1')
    gx = lines_of(p('data', 'glossary.txt'))
    add('ruling (1)', 'the glossary rows h2_sign` and h2_sign_sum at :107-:108', at(gx, 107).startswith("h2_sign'\t") and at(gx, 108).startswith('h2_sign_sum\t'),
        'data/glossary.txt :107 %r ; :108 %r' % (at(gx, 107)[:20], at(gx, 108)[:20]), '1')
    gl4 = rd(p('data', 'b704_glossary.txt')) or ''
    add('ruling (1)', 'both theorems read DERIVES under E0 and by hand (data/b704_glossary.txt)', 'BOTH DERIVES UNDER E0 AND BY HAND True' in gl4, 'data/b704_glossary.txt', '1')
    ct = rd(p('data', 'b704_cut.txt')) or ''
    add('ruling (1)', 'day1/ONE_PAGE_PROOF.md re-cut, 22 rows outside LICENSED/CITED to 2, 80 quoting lines as residues',
        'BEFORE 22, AFTER 2' in ct and 'QUOTING LINES 80 ENTERED AS RESIDUES' in ct, 'data/b704_cut.txt', '1')
    sf = lines_of(p('data', 'b704_standing_figures.txt'))
    add('ruling (1); ferry read-first', 'data/b704_standing_figures.txt (rows are the four figures): 0, 12, 131, 0 against b703`s 0, 11, 131, 0',
        first(sf, 'CORRESPONDENCE 0 ; README 12 ; PARTNERS 131 ; PINS 0 -- AGAINST b703`S 0, 11, 131, 0') > 0,
        'data/b704_standing_figures.txt :%d' % first(sf, 'CORRESPONDENCE 0 ; README 12'), '1')
    ar = json.loads(rd(p('data', 'b704_act_root.json')) or '{}')
    named = [it.split()[0] for it in ar.get('items') or [] if it.startswith('data/')]
    add('ruling (1)', 'the root 97bd2133 over 91 banks chained from 3b6de278', (ar.get('root') or '').startswith('97bd2133') and len(named) == 91 and (ar.get('previous') or '').startswith('3b6de278'),
        'data/b704_act_root.json (root %s, banks %d, prev %s)' % ((ar.get('root') or '')[:8], len(named), (ar.get('previous') or '')[:8]), '1')
    arl = act_root_line('b704')
    add('ruling (1)', 'the chain b624-b704 AGREE (data/act_roots.txt`s last line b704`s; data/b704_chain_half_b_checks.json)',
        bool(arl) and arl[-1][1].startswith('97bd2133') and 'AGREE' in (rd(p('data', 'b704_chain_half_b_checks.json')) or ''),
        'data/act_roots.txt row b704 %s ; the chain bank carries AGREE %s' % ((arl[-1][1][:8] if arl else '-'), 'AGREE' in (rd(p('data', 'b704_chain_half_b_checks.json')) or '')), '1')
    ck, cp = rd(p('data', 'b704_checks.txt')) or '', rd(p('data', 'b704_checks_postpush.txt')) or ''
    add('ruling (1)', 'suite 132 of 140 pre-push and post-push', 'ARMS RUN : 140. ### LIVE PASSING : 132.' in ck and 'ARMS RUN : 140. ### LIVE PASSING : 132.' in cp,
        'data/b704_checks.txt ; data/b704_checks_postpush.txt', '1')
    sc = json.loads(rd(p('data', 'b704_scores_close.json')) or '{}')
    add('ruling (1)', 'N1, N2, N4, N5, S1-S3 HELD, N3 REFUTED', all((sc.get(k) or [''])[0] == 'HELD' for k in ('N1', 'N2', 'N4', 'N5', 'S1', 'S2', 'S3')) and (sc.get('N3') or [''])[0] == 'REFUTED',
        'data/b704_scores_close.json: %s' % ', '.join('%s %s' % (k, (sc.get(k) or ['-'])[0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')), '1')
    add('ruling (1)', 'N3 REFUTED at README :135 on the author`s word', ':135' in (sc.get('N3') or ['', ''])[1] and 'author' in (sc.get('N3') or ['', ''])[1], 'data/b704_scores_close.json N3', '1')
    mi = lines_of(p('data', 'b704_mirror.txt'))
    mt = ' '.join(mi)
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-21-b704.zip CLEAN on all three clauses with the root line',
        'mirror-refresh-2026-10-21-b704.zip' in mt and 'CLEAN ON ALL THREE CLAUSES' in mt and 'Act root: b704 97bd2133' in mt and os.path.exists(K.MIRROR_ZIP),
        'data/b704_mirror.txt :%d (the root line) ; the zip exists %s' % (first(mi, 'THE ROOT LINE'), os.path.exists(K.MIRROR_ZIP)), '1')
    df = lines_of(p('data', 'b704_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", NL.join(df), re.M)
    add('ruling (1); ferry read-first', 'data/b704_defects.txt (rows are defects as lettered): nineteen, (a)-(s), (f), (g), (k), (n) and (q) the navigator`s',
        [x for x, _o in lt] == list('abcdefghijklmnopqrs') and [x for x, o in lt if o == 'NAVIGATOR'] == ['f', 'g', 'k', 'n', 'q'],
        'letters %s ; the navigator`s %s' % (''.join(x for x, _o in lt), [x for x, o in lt if o == 'NAVIGATOR']), '1')
    na = len(re.findall(r'^### PROMPT ', rd(p('data', 'b704_author_answers.txt')) or '', re.M))
    sq, tq = _defect_row(df, 'q')
    add('ruling (1)', '"13 prompts answered": the answers bank`s 12 rows and the root`s prompt, put in two calls under (q)', na == 12 and 'two calls' in tq,
        'data/b704_author_answers.txt PROMPT rows %d ; (q) at data/b704_defects.txt :%d names two calls %s' % (na, sq, 'two calls' in tq), '1')
    add('ruling (1)', 'b704`s entry at FINDINGS :9938, b703`s weight :9924, the corrigendum :9926, the trail OPEN_TRAILS :15552',
        at(fi, K.B704_ENTRY).startswith('## ') and 'b703' in at(fi, K.B704_WEIGHT) and at(fi, K.B704_CORRIGENDUM).startswith('## Corrigendum') and at(ot, K.B704_TRAIL).startswith('### b704'),
        'FINDINGS :%d %r ; :%d ; :%d ; OPEN_TRAILS :%d' % (K.B704_ENTRY, at(fi, K.B704_ENTRY)[:60], K.B704_WEIGHT, K.B704_CORRIGENDUM, K.B704_TRAIL), '1')
    # ### (R315)(2)
    m8 = re.search(r"LIVE FAILING : 8 \[(.*?)\]", ck)
    fails = [x.strip().strip("'") for x in (m8.group(1) if m8 else '').split(',') if x.strip()]
    add('ruling (2)', 'the eight arms failing at b704`s close, as data/b704_checks.txt lists them', sorted(fails) == sorted(EIGHT), 'data/b704_checks.txt: %s' % fails, '1')
    chk = lines_of(p('tools', 'b704_checks.py'))
    add('ruling (2) (b)', 'G-ACTROOT-BANKED`s predicate requiring a read bank among the root`s items (tools/b704_checks.py root_banked_ok; (r))',
        first(chk, 'def root_banked_ok(') > 0 and 'read_calls' in NL.join(chk[first(chk, 'def root_banked_ok(') - 1:first(chk, 'def root_banked_ok(') + 30]),
        'tools/b704_checks.py :%d ; data/b704_defects.txt (r) :%d' % (first(chk, 'def root_banked_ok('), _defect_row(df, 'r')[0]), '1')
    add('ruling (2) (c)', 'G-ANSWERS-CHECKED`s predicate allowing no check after the cut`s commit (tools/b704_checks.py answers_checked_ok; (s))',
        first(chk, 'def answers_checked_ok(') > 0 and _defect_row(df, 's')[0] > 0, 'tools/b704_checks.py :%d ; data/b704_defects.txt (s) :%d' % (first(chk, 'def answers_checked_ok('), _defect_row(df, 's')[0]), '1')
    dj = json.loads(rd(p('data', 'b704_dispatches.json')) or '{}')
    tg = ((dj.get('rows') or [{}])[0].get('target') or '').split()
    ptl = [l for l in lines_of(os.path.join(EF, 'print_targets.txt')) if l.strip()]
    add('ruling (2) (d); ruling (4)', 'G-WORKFLOW-FILES: the probe dispatched at 43 modules where print_targets.txt lists 109 (defect (p), 46 printed)',
        len(tg) == 43 and len(ptl) == 109 and 'printed 46' in _defect_row(df, 'p')[1], 'data/b704_dispatches.json target modules %d ; print_targets.txt names %d ; (p) :%d' % (len(tg), len(ptl), _defect_row(df, 'p')[0]), '1')
    rc_ = rd(p('data', 'b704_read_calls.txt')) or ''
    add('ruling (2) (e)', 'G-READ-RULE-STANDING, four reads after the word, defects (i) and (o)', 'OFFENCES 4' in rc_ and _defect_row(df, 'i')[0] > 0 and _defect_row(df, 'o')[0] > 0,
        'data/b704_read_calls.txt (OFFENCES 4) ; (i) :%d, (o) :%d' % (_defect_row(df, 'i')[0], _defect_row(df, 'o')[0]), '1')
    sr, tr = _defect_row(df, 'r')
    add('ruling (2) (f)-(h)', 'the three trail-equality arms failing because (r) was lettered after the trail landed',
        'landed before this row was lettered' in tr and all(x in tr for x in ('G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-RESOLVED-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS')),
        'data/b704_defects.txt (r) :%d' % sr, '1')
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    lastrow = max([int(m) for m in re.findall(r'^  \((\d+)\) ', NL.join(cg), re.M)] or [0])
    add('ruling (2)', 'the corrigenda bank, appended only (its last row (24), b704`s)', lastrow == 24, 'data/b675_corrigenda.txt, last row (%d) at :%d' % (lastrow, first(cg, '  (%d) ' % lastrow)), '1')
    add('ruling (2)', 'b704`s corrigendum tool to carry', os.path.exists(p('tools', 'b704_corrigendum.py')), 'tools/b704_corrigendum.py', '1')
    add('ruling (2)', 'data/b705_arm_sort.txt and data/b705_tool_repairs.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b705_arm_sort.txt')) and not os.path.exists(p('data', 'b705_tool_repairs.txt')), 'absent, as ordered', '1')
    # ### (R315)(3)
    add('ruling (3); ferry read-first', 'OPEN_TRAILS :15550, W-ORD-README-FIGURE-SCOPE, trigger b705 at carry time', 'W-ORD-README-FIGURE-SCOPE' in at(ot, K.ORDER_README) and 'Trigger: b705 at carry time' in at(ot, K.ORDER_README),
        'OPEN_TRAILS :%d' % K.ORDER_README, '1')
    sfl = lines_of(p('tools', 'b703_standing_figures.py'))
    add('ruling (3); ferry read-first', 'tools/b703_standing_figures.py readme() by line, counting every tag below the kernel`s highest', first(sfl, 'def readme(') > 0 and first(sfl, "state='CURRENT' if hi == v else ('STALE' if hi else 'UNREAD')") > 0,
        'tools/b703_standing_figures.py :%d-:%d' % (first(sfl, 'def readme('), first(sfl, 'return len(stale_lines), rows')), '1')
    rcur = lines_of(p('data', 'b702_readme_currency.txt'))
    add('ruling (3)', 'data/b702_readme_currency.txt, the README`s current-state lines registered (its (A) rows)', first(rcur, '== (A) THE CURRENCY ROWS') > 0 and first(rcur, 'the live kernel line names') > 0,
        'data/b702_readme_currency.txt :%d-:%d' % (first(rcur, '== (A) THE CURRENCY ROWS'), first(rcur, '== (B)') - 1), '1')
    add('ruling (3)', 'the dated ceiling appends ("Appended under the author`s ruling") and the deposit note`s deposited versions (:164)',
        sum(1 for l in rm if l.startswith("*(Appended under the author's ruling")) >= 9 and 'SIDE-lv-conservation v0.10.0' in at(rm, 164) and 'SIDE-kernel **v1.5**' in at(rm, 164),
        'README appends %d ; :164 names v0.10.0 and v1.5' % sum(1 for l in rm if l.startswith("*(Appended under the author's ruling")), '1')
    sfj = json.loads(rd(p('data', 'b704_standing_figures.json')) or '{}')
    add('ruling (3)', 'the README figure 12 at b704, 11 at b703 (the baseline to reset)', (sfj.get('readme') or {}).get('figure') == 12 and (json.loads(rd(p('data', 'b703_standing_figures.json')) or '{}').get('readme') or {}).get('figure') == 11,
        'data/b704_standing_figures.json readme %s ; b703 %s' % ((sfj.get('readme') or {}).get('figure'), (json.loads(rd(p('data', 'b703_standing_figures.json')) or '{}').get('readme') or {}).get('figure')), '1')
    # ### (R315)(4)
    add('ruling (4)', 'W-ORD-WORKFLOW-PROBE-STEP at :15544, trigger b706', 'W-ORD-WORKFLOW-PROBE-STEP' in at(ot, K.ORDER_PROBE_STEP) and 'Trigger: the re-cut act b706' in at(ot, K.ORDER_PROBE_STEP), 'OPEN_TRAILS :%d' % K.ORDER_PROBE_STEP, '1')
    v1, v2 = g(EF, 'rev-parse', 'v0.1^{commit}')[1].strip(), g(EF, 'rev-parse', 'v0.2^{commit}')[1].strip()
    add('ruling (4)', 'the entry tags v0.1 and v0.2 of SIDE-explicit-formula (baed4df, 5c72cad as the papers cite them)', v1.startswith('baed4df') and v2.startswith('5c72cad'), 'v0.1 peels %s ; v0.2 peels %s' % (v1[:7], v2[:7]), '1')
    add('ruling (4)', 'the eleven unbanked mentions: 9 at a tag with no print bank, 2 with no tag', first(cre, 'NO PRINT BANK AT THE TAG 9 ; NO THEOREM OR NO TAG 2') > 0, 'data/b704_cells_reach.txt :%d' % first(cre, 'NO PRINT BANK AT THE TAG 9'), '1')
    add('ruling (4)', 'data/b705_rules.txt -- TO BE WRITTEN at step zero', not os.path.exists(p('data', 'b705_rules.txt')), 'absent, as ordered', '0')
    # ### (R315)(5)
    add('ruling (5)', 'W-ORD-LV-CLOSURE-JOIN at :15452 and its opening step at :15494', 'W-ORD-LV-CLOSURE-JOIN' in at(ot, K.ORDER_LV_JOIN) and 'THE OPENING STEP READ' in at(ot, K.ORDER_LV_JOIN_READ), 'OPEN_TRAILS :%d ; :%d' % (K.ORDER_LV_JOIN, K.ORDER_LV_JOIN_READ), '2')
    pn = lines_of(p('data', 'b703_pins.txt'))
    add('ruling (5); ferry read-first', 'data/b703_pins.txt (rows are kernels at a revision): the closure join 1 DISPATCH at explicit-formula`s pin, lv`s 15 files rebuilt', first(pn, "lv's 15 files rebuilt") > 0 and 'v4.34.0-rc1' in at(pn, 53), 'data/b703_pins.txt :53-:56', '2')
    lt_ = (rd(os.path.join(EF, 'lean-toolchain')) or '').strip()
    lf = rd(os.path.join(EF, 'lakefile.toml')) or ''
    add('ruling (5)', 'SIDE-explicit-formula`s pin: Lean v4.34.0-rc1 (lean-toolchain :1), Mathlib de5ce8a9 (lakefile.toml :7)', lt_ == K.EF_LEAN and ('rev = "%s"' % K.EF_MATHLIB) in lf, 'lean-toolchain %r ; lakefile.toml rev %s' % (lt_, K.EF_MATHLIB[:8]), '2')
    v37 = g(EF, 'rev-parse', 'v0.37^{commit}')[1].strip()
    v10 = g(LV, 'rev-parse', 'v0.10.0^{commit}')[1].strip()
    add('ruling (5)', 'SIDE-explicit-formula v0.37 = 38e2734 and SIDE-lv-conservation v0.10.0 = 93c27ec', v37 == K.EF_V037 and v10 == K.LV_V0100, 'v0.37 peels %s ; v0.10.0 peels %s' % (v37[:7], v10[:7]), '2')
    lvt = (g(LV, 'show', 'v0.10.0:lean-toolchain')[1] or '').strip()
    lvl = g(LV, 'show', 'v0.10.0:lakefile.lean')[1] or ''
    add('ruling (5)', 'lv-conservation at v0.10.0: Lean v4.29.1, Mathlib 5e932f97, its lib SIDELvConservation at srcDir "." (lakefile.lean)',
        lvt == 'leanprover/lean4:v4.29.1' and '5e932f97' in lvl and 'lean_lib SIDELvConservation' in lvl, 'v0.10.0:lean-toolchain %r ; lakefile.lean requires mathlib 5e932f97 %s' % (lvt, '5e932f97' in lvl), '2')
    h2 = _kgrep(EF, 'v0.37', 'def h2_sign : Prop', 'SIDEExplicitFormula/H2Sign.lean')
    s101 = _kgrep(EF, 'v0.37', 'theorem h2_sign_iff_rh : h2_sign', 'SIDEExplicitFormula/Seam.lean')
    p32 = _kgrep(EF, 'v0.37', 'theorem register4_positivity_liCoeff_iff_rh', 'SIDEExplicitFormula/PageConverses.lean')
    lc = _kgrep(EF, 'v0.37', 'def LiCoeff (n', 'SIDEExplicitFormula/LiWeil.lean')
    add('ruling (5)', 'SIDEExplicitFormula.B321.h2_sign (H2Sign.lean :29), h2_sign_iff_rh (Seam.lean :101), PageConverses.register4_positivity_liCoeff_iff_rh (:32), LiWeil.LiCoeff (:243) at v0.37',
        ':29:' in h2 and ':101:' in s101 and ':32:' in p32 and ':243:' in lc, '%s ; %s ; %s ; %s' % (h2[:60], s101[:60], p32[:70], lc[:50]), '2')
    rp = _kgrep(LV, 'v0.10.0', 'def Register4_positivity (lam', 'SIDELvConservation/RegisterPentagon.lean')
    ns = _kgrep(LV, 'v0.10.0', 'namespace RegisterPentagon', 'SIDELvConservation/RegisterPentagon.lean')
    add('ruling (5)', 'lv-conservation`s own declaration "SIDELvConservation.Register4_positivity" -- the declaration stands in namespace SIDELvConservation.RegisterPentagon (RegisterPentagon.lean :72-:73, :152)',
        False if (':152:' in rp and ':73:' in ns) else False,
        'at v0.10.0 the name is SIDELvConservation.RegisterPentagon.Register4_positivity (RegisterPentagon.lean :152, namespace :72-:73); the ruling`s name omits RegisterPentagon', '2')
    rb = lines_of(os.path.join(EF, 'SIDEExplicitFormula', 'RegisterBridge.lean'))
    add('ruling (5)', 'b701`s restatement bridge: h2_sign_iff_rh.trans register4_positivity_liCoeff_iff_rh.symm (RegisterBridge.lean :34-:35)',
        first(rb, 'h2_sign_iff_rh.trans register4_positivity_liCoeff_iff_rh.symm', 34) == 35 and first(rb, 'theorem h2_sign_iff_register4_positivity_liCoeff') == 34,
        'RegisterBridge.lean :%d-:%d' % (first(rb, 'theorem h2_sign_iff_register4_positivity_liCoeff'), first(rb, 'h2_sign_iff_rh.trans register4_positivity_liCoeff_iff_rh.symm', 34)), '2')
    cs = rd(p('data', 'b701_correspondence_restatement.txt')) or ''
    add('ruling (5); ferry read-first', 'data/b701_correspondence_restatement.txt: the restatement HOLDS-BY-CORRESPONDENCE at every binder', 'HOLDS-BY-CORRESPONDENCE AT EVERY BINDER' in cs, 'data/b701_correspondence_restatement.txt :57', '2')
    wf = lines_of(os.path.join(EF, '.github', 'workflows', 'build-module.yml'))
    add('ruling (5)', 'SIDE-explicit-formula`s build-module.yml with its print step (:78-:96) and closure step (:98-:111)', first(wf, 'name: Axioms of the named terminals') == 78 and first(wf, 'name: Constant closure') == 98,
        '.github/workflows/build-module.yml :%d, :%d' % (first(wf, 'name: Axioms of the named terminals'), first(wf, 'name: Constant closure')), '2')
    rc0, out0, err0 = C.g('D:/', 'ls-remote', 'https://github.com/psinary-sketch/SIDE-faces-join.git') if False else (None, '', '')
    gv = subprocess.run(['gh', 'repo', 'view', 'psinary-sketch/SIDE-faces-join', '--json', 'name'], capture_output=True, text=True)
    add('ruling (5)', 'SIDE-faces-join under psinary-sketch does not yet exist (to be created), nor D:/SIDE-faces-join', gv.returncode != 0 and not os.path.exists(K.KERNEL_DIR),
        'gh repo view exit %d ; D:/SIDE-faces-join exists %s' % (gv.returncode, os.path.exists(K.KERNEL_DIR)), '2')
    cd = rd(p('data', 'b694_circuit_dominance.txt')) or ''
    add('ruling (5)', 'CLAUSE-DOMINANCE at 1 of 2 at the last circuit reading (b694)', '1 of 2' in cd or '1 OF 2' in cd, 'data/b694_circuit_dominance.txt', '2')
    add('ruling (5)', 'data/b705_join_grade.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b705_join_grade.txt')), 'absent, as ordered', '2')
    # ### (R315)(6)
    add('ruling (6)', 'W-ORD-P3-CONTOUR-SIGMA at :15504, trigger b705 step zero', 'W-ORD-P3-CONTOUR-SIGMA' in at(ot, K.ORDER_P3) and 'Trigger: b705 step zero' in at(ot, K.ORDER_P3), 'OPEN_TRAILS :%d' % K.ORDER_P3, '0')
    cpl = lines_of(p('data', 'b685_count_plan.txt'))
    add('ruling (6)', 'data/b685_count_plan.txt: N_Q over -1/2 < Re ρ < 3/2 (:9); the half path with σ₁ ≥ 3/2 (:16); the circle σ ∈ [c − r, c + r] ⊂ (−½, ∞) (:60)',
        'with −1/2 < Re ρ < 3/2' in at(cpl, 9) and 'σ₁ ≥ 3/2' in at(cpl, 16) and '(−½, ∞)' in at(cpl, 60), 'data/b685_count_plan.txt :9, :16, :60', '0')
    cnt = lines_of(p('data', 'b685_count.txt'))
    add('ruling (6)', 'data/b685_count.txt :8: c = 1.7, r = 2.05, p = c − r = −0.35, σ1 = 2.4024', 'c = 1.7, r = 2.05' in at(cnt, 8) and '2.40243902439' in at(cnt, 8), 'data/b685_count.txt :8', '0')
    p3 = lines_of(p('data', 'b685_p3.txt'))
    add('ruling (6)', 'data/b685_p3.txt :52-:53: σ ≥ 3/2 no zero (V2), σ ≤ −1/2 none by the functional equation', 'σ ≥ 3/2 no zero' in at(p3, 52) and 'σ ≤ −1/2 none by the functional equation' in at(p3, 53), 'data/b685_p3.txt :52-:53', '0')
    ec = lines_of(p('data', 'b667_epstein_counts.txt'))
    add('ruling (6)', 'data/b667_epstein_counts.txt :49-:52: the region [-0.5, 1.5] × [0.5, 150] by the half path, N(R) = 180', 'THE REGION [-0.5, 1.5]' in at(ec, 49) and 'N(R) = 180' in at(ec, 52), 'data/b667_epstein_counts.txt :49, :52', '0')
    ep = lines_of(p('data', 'b667_epstein_plan.txt'))
    add('ruling (6)', 'data/b667_epstein_plan.txt :10-:12: Λ_Q(s) = Λ_Q(1 − s) and Λ_Q(1 − conj s) = conj Λ_Q(s)', 'Λ_Q(s) = Λ_Q(1 − s)' in at(ep, 10) and 'Λ_Q(1 − conj s) = conj Λ_Q(s)' in at(ep, 12), 'data/b667_epstein_plan.txt :10, :12', '0')
    wb = lines_of(p('tools', 'b696_witness_balls.py'))
    add('ruling (6)', 'tools/b696_witness_balls.py zero_tail (:124): |δ| ≤ Y = 1 at Q0 (:130), the count on N_Q`s law (count_unit :116-:121)',
        first(wb, 'def zero_tail(') == 124 and first(wb, "Y = arb(1) if obj == 'q0' else arb(1) / 2") == 130 and first(wb, 'def count_unit(') == 116,
        'tools/b696_witness_balls.py :%d, :%d, :%d' % (first(wb, 'def zero_tail('), first(wb, "Y = arb(1) if obj == 'q0' else arb(1) / 2"), first(wb, 'def count_unit(')), '0')
    tp = lines_of(p('data', 'b696_tails_plan.txt'))
    add('ruling (6)', 'data/b696_tails_plan.txt :44-:45, :50: N_Q counts -1/2 < Re ρ < 3/2 ; |δ| < 1 in N_Q`s strip', '-1/2 < Re rho < 3/2' in at(tp, 44) and '|delta| < 1 in N_Q' in at(tp, 50), 'data/b696_tails_plan.txt :44, :50', '0')
    add('ruling (6)', 'the b687 derivation banks: 114 of 114 inequalities (data/b687_steps.txt), P3 DERIVED (data/b687_p3_status.txt :8)', '114 OF 114' in (rd(p('data', 'b687_steps.txt')) or '') and 'DERIVED' in at(lines_of(p('data', 'b687_p3_status.txt')), 8),
        'data/b687_steps.txt :122 ; data/b687_p3_status.txt :8', '0')
    a2 = lines_of(os.path.join(PP, *K.ARCHIVE2.split('/')))
    add('ruling (6)', 'OPEN_TRAILS archive-2 :2089, W-SIGN-7`s Epstein arm: off-line existence attested (Davenport–Heilbronn)', 'W-SIGN-7 closed' in at(a2, K.ARCHIVE2_WSIGN7) and 'Davenport–Heilbronn' in at(a2, K.ARCHIVE2_WSIGN7),
        '%s :%d' % (K.ARCHIVE2, K.ARCHIVE2_WSIGN7), '0')
    add('ruling (6)', 'data/b705_contour.txt -- TO BE WRITTEN at step zero', not os.path.exists(p('data', 'b705_contour.txt')), 'absent, as ordered', '0')
    # ### (R315)(7)
    rg = lines_of(p('data', 'b703_registrations.txt'))
    add('ruling (7); ferry read-first', 'data/b703_registrations.txt (rows are registrations): (ii) the detection law :21-:31, the range [0.67, 1.5] (:25), ρ₀ calibration, the controls :27-:28, the window beside it :29-:30',
        first(rg, '(ii) THE DETECTION LAW -- COMPUTED AT b705') == 21 and '[0.67, 1.5]' in at(rg, 25) and 'b675' in at(rg, 27) and 'notched Weil window' in at(rg, 29),
        'data/b703_registrations.txt :21, :25, :27, :29', '3')
    rgc = g(ROOT, 'log', '--format=%h', '--', 'data/b703_registrations.txt')[1].split()
    add('ruling (7)', 'data/b703_registrations.txt committed once (b8a36309, alone) and unchanged since', len(rgc) == 1 and rgc[0].startswith('b8a36309') and not g(ROOT, 'status', '--porcelain', '--', 'data/b703_registrations.txt')[1].strip(),
        'commits touching it %s' % rgc, '3')
    qb = lines_of(p('data', 'b703_q0_band.txt'))
    add('ruling (7); ferry read-first', 'data/b703_q0_band.txt (rows are bins): 17 off the line (:8); the lowest band zero 0.79799715717868013876 + 29.55176109862911459913 i (:18)',
        'off the line 17' in at(qb, 8) and '0.79799715717868013876 + 29.55176109862911459913 i' in at(qb, 18), 'data/b703_q0_band.txt :8, :18', '3')
    lb = lines_of(p('data', 'b675_li_bench.txt'))
    add('ruling (7)', 'b675`s figure at ρ₀: n* = 63676 (data/b675_li_bench.txt :6; data/b675_li_constants.json bench n_star)', 'n* = 63676' in at(lb, 6) and (json.loads(rd(p('data', 'b675_li_constants.json')) or '{}').get('bench') or {}).get('n_star') == 63676,
        'data/b675_li_bench.txt :6 ; data/b675_li_constants.json', '3')
    wt = lines_of(p('tools', 'b694_witness_terms.py'))
    add('ruling (7); ferry read-first', 'tools/b694_witness_terms.py: the ladder 16-192 (:51), b518`s window (:52, :107-:136), the terms P, PR, A (:9-:15)',
        "LADDER = ('16', '24', '32', '48', '64', '96', '128', '192')" in at(wt, 51) and "B518_A = '14.106736'" in at(wt, 52) and first(wt, 'class Window:') == 106,
        'tools/b694_witness_terms.py :51, :52, :106', '3')
    add('ruling (7)', 'b694`s term bank: data/b694_witness.txt and its gz beside data/b694_witness_hashes.txt; b696`s ball re-read data/b696_witness_balls.txt',
        all(os.path.exists(p('data', f)) for f in ('b694_witness.txt', 'b694_witness.json.gz', 'b694_witness_hashes.txt', 'b696_witness_balls.txt')), 'data/b694_witness.txt ; .json.gz ; _hashes.txt ; data/b696_witness_balls.txt', '3')
    add('ruling (7); ferry', 'data/b680_rules.txt (1), a binary bank beside a text hashes bank', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt :5', '3')
    # ### (R315)(8)
    add('ruling (8)', 'the three visibility measures (INSTRUMENTS.md :140): symmetry gained, measurability gained, obstruction re-presentation', 'symmetry gained' in at(ins, 140) and 'measurability gained' in at(ins, 140) and 'obstruction re-presentation' in at(ins, 140), 'INSTRUMENTS.md :140', '4')
    ws = lines_of(p('data', 'b703_wsign7.txt'))
    add('ruling (8); ferry read-first', 'data/b703_wsign7.txt (rows are the archive`s records): axis (b) a wall that narrowed (:46-:49)', first(ws, 'AXIS (b), COVER') == 46 and 'narrows' in at(ws, 49), 'data/b703_wsign7.txt :46-:49', '4')
    add('ruling (8)', 'data/b703_registrations.txt (iv) the cover axis, the ranking computed at b705 (:45-:52)', first(rg, '(iv) THE COVER AXIS AT THE CLAUSE -- COMPUTED AT b705') == 45, 'data/b703_registrations.txt :45', '4')
    add('ruling (8)', 'data/b705_registrations.txt and data/b705_i6_ranking.txt -- TO BE WRITTEN, the registration before any number', not os.path.exists(p('data', 'b705_registrations.txt')) and not os.path.exists(p('data', 'b705_i6_ranking.txt')), 'absent, as ordered', '4')
    # ### (R315)(9)
    add('ruling (9)', 'W-ORD-E0-MET-CLASSK at :15506 and its companion clause at :15548', 'W-ORD-E0-MET-CLASSK' in at(ot, K.ORDER_E0) and 'W-ORD-E0-MET-CLASSK' in at(ot, K.ORDER_E0_COMPANIONS), 'OPEN_TRAILS :%d ; :%d' % (K.ORDER_E0, K.ORDER_E0_COMPANIONS), '4')
    wg = lines_of(p('data', 'b703_widening_grade.txt'))
    wv = next((l for l in reversed(wg) if 'THEOREMS 10' in l), '')
    add('ruling (9); ferry read-first', 'data/b703_widening_grade.txt (rows are theorems): the three inclusions read PREDICATE-UNLISTED', wv.count('(E0 PREDICATE-UNLISTED)') == 3, 'data/b703_widening_grade.txt :%d' % first(wg, 'THEOREMS 10'), '4')
    for nm in ('acDeriv', "classK'", 'classKsum'):
        hit = _kgrep(EF, 'v0.36', 'def %s' % nm, 'SIDEExplicitFormula/H2SignWide.lean')
        add('ruling (9)', '%s defined in H2SignWide.lean at v0.36' % nm, bool(hit), hit[:90] or 'NOT FOUND', '4')
    # ### (R315)(10)-(13) and the ferry
    for repo, bs in K.DELETE:
        mg = (g(repo, 'branch', '--merged', 'main')[1] or '').replace('*', ' ').split()
        for b in bs:
            add('ruling (10)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in mg, 'listed by `git branch --merged main` at %s before any delete' % os.path.basename(repo) if b in mg else '### NOT LISTED', '0')
    add('ruling (11)', 'the READFIRST-CLOSURE reader', 'def readfirst(' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py :395', '0')
    add('ruling (11)', 'data/b705_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b705_readfirst.txt')), '0')
    r74 = lines_of(p('data', 'b674_rules.txt'))
    add('ruling (11)', 'b674`s measures (data/b674_rules.txt row (2)) and b704`s word at the tie (data/b704_tie.txt)', first(r74, '(2) THE TIE-BREAK BEYOND THE COUNT') > 0 and 'b674`S MEASURES READ IN THEIR WRITTEN ORDER' in (rd(p('data', 'b704_tie.txt')) or ''),
        'data/b674_rules.txt :%d ; data/b704_tie.txt' % first(r74, '(2) THE TIE-BREAK'), '0')
    add('ruling (12)', 'the draft at v5, held', K.DRAFT == '23228113', 'tools/b705_worklist.py DRAFT', '6')
    add('ruling (13)', 'W-ORD-PAPER-PARTNER-COPIES (:15446) disposition (iii) over the 17 pairs, trigger b706', 'W-ORD-PAPER-PARTNER-COPIES' in at(ot, K.ORDER_PARTNER) and '(iii), rename in place' in at(ot, K.ORDER_PARTNER) and '17 pairs' in at(ot, K.ORDER_PARTNER), 'OPEN_TRAILS :%d' % K.ORDER_PARTNER, '6')
    add('ruling (13)', 'W-ORD-CORRESPONDENCE-EF-REACH (:15546), trigger b706', 'W-ORD-CORRESPONDENCE-EF-REACH' in at(ot, K.ORDER_EF_REACH), 'OPEN_TRAILS :%d' % K.ORDER_EF_REACH, '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C5', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''), 'tools/b693_worklist.py :52', '5')
    add('ferry C5', 'the four standing arms` figures tool and b704`s baseline', os.path.exists(p('tools', 'b703_standing_figures.py')) and os.path.exists(p('data', 'b704_standing_figures.json')),
        'tools/b703_standing_figures.py ; data/b704_standing_figures.json', '5')
    add('ferry C0', 'data/b684_rules.txt row (1), a test above 450 s its own part', '(1) A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5', '0')
    add('ferry', 'data/b690_rules.txt row (2)', first(lines_of(p('data', 'b690_rules.txt')), '(2) AT A RE-CUT') == 9, 'data/b690_rules.txt :9', '0')
    add('ferry C6', 'b673`s capture names', os.path.exists(p('data', 'b704_relay_push_out.txt')), 'data/b704_relay_push_out.txt (the form carried)', '6')
    add('ferry C6', 'the b670 form of the mirror', os.path.exists(p('data', 'b704_mirror.txt')), 'data/b704_mirror.txt (the form carried)', '6')
    add('ferry C0', 'this act`s session transcript (a new session; b704 ran in %s)' % K.PREV_SESSION[:8], os.path.exists(C.SESSION), C.SESSION, '0')
    return R


def _write(L, R, miss):
    for name, data in (('b705_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b705_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b705 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b705_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b705_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b705_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b705_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b705."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.KERNEL_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b705'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b705')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b705)', 'exec'), ns)
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
        print('usage: b705_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
