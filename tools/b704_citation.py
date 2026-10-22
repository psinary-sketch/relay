# -*- coding: utf-8 -*-
"""b704_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b704's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (fb68aaef, a new session after the author's /clear; the anchor (R314)'s line is unique in it); the answer route is b682's, imported
### from tools/b682_citation.py with its act names pointed at b704 and its commit reach widened to the kernels as b699-b703 widened it; the
### `word` route is b694's.
### Routes: `check [dry]` -> data/b704_citation_check.txt (.json) ; `ferry` -> data/b704_ferry_scan.txt ; `answer <needle>` / `word <needle>` ->
###         the check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b704 from b703_citation.py's form; this tool writes only the banks named above.
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
import b704_worklist as K   # noqa: E402

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

HEAD_QUOTE = 'b703 closed: relay 3ee79ba0, PLACE-papers 1532695; suite 138 of 138; root 3b6de278d4eb0467\u2026; 4 prompts answered; 12 defects'
MEMORY_STATE = 'C:/Users/echo chamber/.claude/projects/D--/memory/project_state_cp4_cp5_b559_b576.md'


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


def _defect_row(L, letter):
    """the text of a lettered defect row, from its letter to the next letter's row."""
    s = first(L, '    (%s) ' % letter)
    if not s:
        return 0, ''
    e = next((i for i in range(s, len(L)) if re.match(r'^    \([a-z]\) ', L[i]) or L[i].startswith('###')), len(L))
    return s, ' '.join(x.strip() for x in L[s - 1:e])


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    RM = os.path.join(PP, 'README.md')
    ot, fi, rm = lines_of(OT), lines_of(FI), lines_of(RM)
    EF = K.EF_DIR
    # ### the ferry's read-first list
    for f in ('data/b703_closing.txt', 'data/b703_defects.txt', 'data/b703_widening_grade.txt', 'data/b703_epstein_grade.txt', 'data/b703_q0_band.txt',
              'data/b703_pins.txt', 'data/b703_tool_repairs.txt', 'data/b703_closing_push_out.txt', 'data/b701_glossary_rows.txt', 'data/b702_nodes_zeta.txt',
              'data/b703_commands.txt', 'data/b670_licensed_table.txt', 'data/b674_rules.txt', 'data/b690_rules.txt', 'data/b698_rules.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    add('ferry read-first', 'PLACE-papers README.md', os.path.exists(RM), 'exists at the working tree (%d lines)' % len([x for x in rm if x is not None]), '0')
    cl = lines_of(p('data', 'b703_closing.txt'))
    add('ferry read-first; ruling (1)', 'data/b703_closing.txt :1, the head line, against (R314)(1)`s quote after whitespace is removed', _ws(cl[0]) == _ws(HEAD_QUOTE),
        'data/b703_closing.txt :1 = %r' % cl[0][:130], '0-1')
    cf = first(cl, '### CARRIED FORWARD.')
    add('ferry read-first', 'data/b703_closing.txt, the carried-forward rows (a)-(h) by line', cf > 0 and first(cl, '    (a) ', cf) > 0 and first(cl, '    (h) ', cf) > 0,
        'data/b703_closing.txt :%d (the head), (a) :%d, (h) :%d' % (cf, first(cl, '    (a) ', cf), first(cl, '    (h) ', cf)), '0-1')
    po = rd(p('data', 'b703_closing_push_out.txt')) or ''
    head = g(ROOT, 'rev-parse', '--short=8', 'HEAD')[1].strip()
    add('ruling (1); ruling (8)', 'the closing commit 295e53f0 pushed alone and read back at the remote (data/b703_closing_push_out.txt, to be committed)',
        'main read back at the remote: 295e53f0' in po and head == '295e53f0',
        'data/b703_closing_push_out.txt (capture-on lines %d) ; relay HEAD %s' % (po.count('capture on'), head), '0-1')
    st = g(ROOT, 'status', '--porcelain', '--', 'data/b703_closing_push_out.txt')[1].strip()
    add('ruling (8)', 'data/b703_closing_push_out.txt uncommitted at the act`s start', st.startswith('??'), 'git status %r' % st, '0')
    # ### (R314)(1), by row
    df = lines_of(p('data', 'b703_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", NL.join(df), re.M)
    add('ruling (1)', 'data/b703_defects.txt (rows are defects as lettered): twelve, (a)-(l), (d) and (e) the navigator`s', [x for x, _o in lt] == list('abcdefghijkl')
        and [x for x, o in lt if o == 'NAVIGATOR'] == ['d', 'e'], 'letters %s ; the navigator`s %s' % (''.join(x for x, _o in lt), [x for x, o in lt if o == 'NAVIGATOR']), '1')
    v36 = g(EF, 'rev-parse', 'v0.36^{commit}')[1].strip()
    v37 = g(EF, 'rev-parse', 'v0.37^{commit}')[1].strip()
    add('ruling (1)', 'SIDE-explicit-formula v0.36 = dfadc8c and v0.37 = 38e2734', v36 == K.EF_V036 and v37 == K.EF_V037, 'v0.36 peels %s ; v0.37 peels %s' % (v36[:7], v37[:7]), '1')
    tm = g(EF, 'tag', '-l', '--format=%(contents)', 'v0.37')[1] or ''
    add('ruling (1)', 'v0.37 naming v0.36 (the tag`s message)', 'v0.36' in tm, 'v0.37`s message %r' % ' '.join(tm.split())[:120], '1')
    wg = lines_of(p('data', 'b703_widening_grade.txt'))
    wv = at(wg, len([x for x in wg if x is not None]) - 1) if wg else ''
    wv = next((l for l in reversed(wg) if 'THEOREMS 10' in l), '')
    names = ('acDeriv_of_contDiff_two GRADE DERIVES', "classK_subset_classK' GRADE DERIVES", 'classK_subset_classKsum GRADE DERIVES',
             "classKsum_subset_classK' GRADE DERIVES", "h2_sign'_imp_h2_sign GRADE DERIVES", "h2_sign'_imp_rh GRADE DERIVES", 'rh_imp_h2_sign_sum GRADE DERIVES',
             'h2_sign_sum_imp_h2_sign GRADE DERIVES', 'h2_sign_sum_iff_rh GRADE DERIVES', 'paperFT_finset_sum GRADE INTERFACES')
    add('ruling (1); ferry read-first', 'data/b703_widening_grade.txt (ten rows): nine DERIVES and paperFT_finset_sum INTERFACES, each at the standard three, every salt-check PASS',
        all(n in wv for n in names) and wv.count('SALT PASS PROFILE STD3') == 10, 'data/b703_widening_grade.txt :%d (the verdict; SALT PASS PROFILE STD3 x%d)' % (first(wg, 'THEOREMS 10'), wv.count('SALT PASS PROFILE STD3')), '1')
    add('ruling (1)', 'paperFT_finset_sum INTERFACES on its hypotheses hf and hs', first(wg, 'THE HAND GRADE INTERFACES -- INTERFACES on hf and hs') > 0,
        'data/b703_widening_grade.txt :%d' % first(wg, 'THE HAND GRADE INTERFACES -- INTERFACES on hf and hs'), '1')
    add('ruling (1)', 'the inclusions` E0 reading PREDICATE-UNLISTED (three), entered as W-ORD-E0-MET-CLASSK', wv.count('(E0 PREDICATE-UNLISTED)') == 3 and 'W-ORD-E0-MET-CLASSK' in at(ot, K.ORDER_E0),
        'the verdict`s PREDICATE-UNLISTED x%d ; OPEN_TRAILS :%d' % (wv.count('(E0 PREDICATE-UNLISTED)'), K.ORDER_E0), '1')
    eg = rd(p('data', 'b703_epstein_grade.txt')) or ''
    add('ruling (1); ferry read-first', 'the Epstein module Schema/EpsteinZQ.lean, its four premises over Wide.WideConfig (data/b703_epstein_grade.txt)',
        all(x in eg for x in ('ZQContinuation', 'ZQZeros', 'ZQExplicitFormula', 'ZQPremises', 'WideConfig', 'EpsteinZQ.lean')),
        'the four premise names, WideConfig and the module named in the bank', '1')
    r2 = rd(p('data', 'b703_runner_SIDE-explicit-formula_run2.txt')) or ''
    add('ruling (1)', 'run 39703864050 DERIVES at 109 of 109', '39703864050' in r2 and 'TERMINALS PRINTED 109 OF 109' in r2 and 'GATE DERIVES' in r2,
        'data/b703_runner_SIDE-explicit-formula_run2.txt', '1')
    qb = lines_of(p('data', 'b703_q0_band.txt'))
    qv = ' '.join(qb)
    add('ruling (1); ferry read-first', 'data/b703_q0_band.txt (rows are bins): 163 rows, 17 off, 146 on; bins 0, 5, 10, 2; 15 in (1/2, 7/8]; the lowest 0.79799715717868013876 + 29.55176109862911459913 i; the control',
        all(x in qv for x in ('rows 163 ; off the line 17 ; on the line 146', '(1/2, 0.6]     0', '(0.6, 0.75]    5', '(0.75, 7/8]   10', '(7/8, 1)       2',
                              '15 in the band, the lowest-height 0.79799715717868013876 + 29.55176109862911459913 i', 'the row count 163 against the stated 163: True')),
        'data/b703_q0_band.txt :8, :12-:15, :18-:19', '1')
    pn = rd(p('data', 'b703_pins.txt')) or ''
    add('ruling (1); ferry read-first', 'data/b703_pins.txt: the closure join one dispatch at v4.34.0-rc1 / de5ce8a9, lv`s 15 files; the interval vendoring one dispatch, 86 files, 44 days, waiting on BINDER-PROVENANCE',
        all(x in pn for x in ('v4.34.0-rc1', 'de5ce8a9', "lv's 15 files rebuilt", '86 files back 44 days, 1 DISPATCH, waiting on BINDER-PROVENANCE')), 'data/b703_pins.txt :53-:56', '1')
    ar = json.loads(rd(p('data', 'b703_act_root.json')) or '{}')
    named = [it.split()[0] for it in ar.get('items') or [] if it.startswith('data/')]
    add('ruling (1)', 'the root 3b6de278 over 83 banks chained from 56312178', (ar.get('root') or '').startswith('3b6de278') and len(named) == 83 and (ar.get('prev') or ar.get('previous') or '').startswith('56312178'),
        'data/b703_act_root.json (root %s, banks %d, prev %s)' % ((ar.get('root') or '')[:8], len(named), (ar.get('prev') or ar.get('previous') or '')[:8]), '1')
    ck, cp = rd(p('data', 'b703_checks.txt')) or '', rd(p('data', 'b703_checks_postpush.txt')) or ''
    add('ruling (1)', 'suite 138 of 138 pre-push and post-push, no failure carried', 'ARMS RUN : 138. ### LIVE PASSING : 138.' in ck and 'ARMS RUN : 138. ### LIVE PASSING : 138.' in cp,
        'data/b703_checks.txt ; data/b703_checks_postpush.txt', '1')
    sc = rd(p('data', 'b703_scores_close.json')) or ''
    add('ruling (1)', 'all eight scores HELD', sc.count('"HELD"') >= 8, 'data/b703_scores_close.json (HELD %d)' % sc.count('"HELD"'), '1')
    add('ruling (1)', 'the sealed tools` hashes equal at the close, 11 of 11', first(cl, '### AGREE 11 of 11') > 0, 'data/b703_closing.txt :%d' % first(cl, '### AGREE 11 of 11'), '1')
    mi = lines_of(p('data', 'b703_mirror.txt'))
    mt = ' '.join(mi)
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-21-b703.zip, sha256 5263fb6f, CLEAN on all three clauses, its span line reading b702 as the last export',
        'mirror-refresh-2026-10-21-b703.zip' in mt and 'sha256 5263fb6f' in mt and 'CLEAN ON ALL THREE CLAUSES' in mt and first(mi, '### THE SPAN:') > 0 and 'b702' in at(mi, first(mi, '### THE SPAN:')),
        'data/b703_mirror.txt :%d (the span)' % first(mi, '### THE SPAN:'), '1')
    add('ruling (1)', 'the scratch clone D:\\relay\\scratch\\interval-b703 deleted', not os.path.exists('D:/relay/scratch/interval-b703'), 'absent', '1')
    add('ruling (1)', 'b703`s entry at FINDINGS :9888, b702`s weight :9872, the corrigendum :9874, the trail OPEN_TRAILS :15508', at(fi, K.B703_ENTRY).startswith('## ') and 'b702' in at(fi, K.B703_WEIGHT)
        and at(ot, K.B703_TRAIL).startswith('### b703'), 'FINDINGS :%d %r ; OPEN_TRAILS :%d' % (K.B703_ENTRY, at(fi, K.B703_ENTRY)[:80], K.B703_TRAIL), '1')
    # ### (R314)(2)
    ml = lines_of(MEMORY_STATE)
    add('ruling (2) (m)', 'the project-state memory file (514 lines when b703 read it whole)', os.path.exists(MEMORY_STATE), '%s : %d lines now (the file has been edited since; b703`s read was at 514)' % (
        os.path.basename(MEMORY_STATE), len(ml)), '1')
    sk, tk = _defect_row(df, 'k')
    add('ruling (2) (k)', 'b703 (k): thirteen calls', 'thirteen calls' in tk, 'data/b703_defects.txt :%d' % sk, '1')
    sl, tl = _defect_row(df, 'l')
    add('ruling (2) (l)', 'b703 (l): "one after the seal" -- the read (l) letters, made after the seal', sl > 0 and 'before the lock' not in tl,
        'data/b703_defects.txt :%d: the read at transcript line 10815 %s; the row lettered after the seal' % (sl, 'BEFORE THE LOCK' if 'before the lock' in tl else 'after the seal'), '1')
    word = _find_in(sorted(glob.glob(p('data', 'b68[3-9]_*.txt'))) + sorted(glob.glob(p('data', 'b69[0-9]_*.txt'))), 'arms for the traceable ones')
    add('ruling (2)', 'the author`s word of 2026-10-18, "arms for the traceable ones, the seat sorts them", in a bank', word[1] > 0, 'data: %s :%d' % word, '1')
    add('ruling (2)', 'b683`s sort rule (TRACEABLE / PROSE)', os.path.exists(p('data', 'b683_arms_sort.txt')), 'data/b683_arms_sort.txt', '1')
    add('ruling (2)', 'the act`s command bank (b703`s by path) and b703`s read bank', os.path.exists(p('data', 'b703_commands.txt')) and os.path.exists(p('data', 'b703_read_calls.txt')),
        'data/b703_commands.txt ; data/b703_read_calls.txt', '1')
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    lastrow = max([int(m) for m in re.findall(r'^  \((\d+)\) ', NL.join(cg), re.M)] or [0])
    add('ruling (2)', 'the corrigenda bank, appended only', lastrow > 0, 'data/b675_corrigenda.txt, last row (%d) at :%d' % (lastrow, first(cg, '  (%d) ' % lastrow)), '1')
    add('ruling (2)', 'b703`s corrigendum tool to carry', os.path.exists(p('tools', 'b703_corrigendum.py')), 'tools/b703_corrigendum.py', '1')
    add('ruling (2)', 'data/b704_defects.txt and data/b704_tool_repairs.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b704_defects.txt')) and not os.path.exists(p('data', 'b704_tool_repairs.txt')), 'absent, as ordered', '1')
    # ### (R314)(3)
    fo = at(ot, K.ORDER_FACES)
    add('ruling (3); ferry read-first', 'OPEN_TRAILS :15444, W-ORD-FACES-PROBE-CURRENT (its text: "re-probed at v0.35"; the ruling: at v0.37)', 'W-ORD-FACES-PROBE-CURRENT' in fo,
        'OPEN_TRAILS :%d ; names v0.35 %s' % (K.ORDER_FACES, 're-probed at v0.35' in fo), '2')
    fp = lines_of(os.path.join(PP, K.FACES_PAGE))
    fh = first(fp, '82550e4')
    add('ruling (3)', 'the faces page`s header naming v0.26 = 82550e4', fh > 0 and 'v0.26' in at(fp, fh), '%s :%d %r' % (K.FACES_PAGE, fh, at(fp, fh)[:110]), '2')
    nz = lines_of(p('data', 'b702_nodes_zeta.txt'))
    add('ruling (3)', 'data/b702_nodes_zeta.txt, its pin line', first(nz, '# pin: v0.26') > 0, 'data/b702_nodes_zeta.txt :%d' % first(nz, '# pin: v0.26'), '2')
    add('ruling (3)', 'tools/chain_page.py, the generator', os.path.exists(p('tools', 'chain_page.py')), 'tools/chain_page.py', '2')
    for nm in K.NODES_NEW:
        gr = g(EF, 'grep', '-n', '-e', 'theorem %s ' % nm, 'v0.36', '--', '*.lean')[1] or ''
        add('ruling (3)', '%s at v0.36 (git grep bounded to the kernel`s source)' % nm, bool(gr.strip()), (gr.split(NL)[0] if gr.strip() else 'NOT FOUND')[:120], '2')
    c1 = first(ot, 'W-ORD-EXPLICIT-FORMULA-C1')
    add('ruling (3)', 'W-ORD-EXPLICIT-FORMULA-C1 at its line', c1 > 0, 'OPEN_TRAILS :%d' % c1, '2')
    add('ruling (3)', 'data/b704_nodes_zeta.txt and data/b704_faces_diff.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b704_nodes_zeta.txt')) and not os.path.exists(p('data', 'b704_faces_diff.txt')),
        'absent, as ordered', '2')
    # ### (R314)(4)
    r98, r90 = lines_of(p('data', 'b698_rules.txt')), lines_of(p('data', 'b690_rules.txt'))
    add('ruling (4); ferry read-first', 'data/b698_rules.txt row (1), a tag move regenerates the cells', first(r98, "(1) A KERNEL'S TAG MOVE REGENERATES THE CORRESPONDENCE CELLS") > 0,
        'data/b698_rules.txt :%d' % first(r98, "(1) A KERNEL'S TAG MOVE"), '3')
    add('ruling (4)', 'the print banks of b703`s two runs', os.path.exists(p('data', 'b703_axioms_SIDE-explicit-formula_run1r.txt')) and os.path.exists(p('data', 'b703_axioms_SIDE-explicit-formula_run2.txt')),
        'data/b703_axioms_SIDE-explicit-formula_run1r.txt ; _run2.txt', '3')
    cgn = rd(p('tools', 'correspondence_gen.py')) or ''
    add('ruling (4)', 'tools/correspondence_gen.py, the carried-at reading b691 repaired', 'carried' in cgn.lower(), 'tools/correspondence_gen.py (carried-at reading present %s)' % ('carried' in cgn.lower()), '3')
    add('ruling (4)', 'the roster bank the generator reads', os.path.exists(p('data', 'b672_roster_read.json')), 'data/b672_roster_read.json', '3')
    # ### (R314)(5)
    kl = at(rm, K.README_KERNEL_LINE)
    kloc = first(rm, 'SIDE-explicit-formula **v0.35** (`d4e046a`)')
    add('ruling (5); ferry read-first', 'README.md :160, "SIDE-explicit-formula v0.35 (d4e046a)"', 'v0.35' in kl and 'd4e046a' in kl,
        'README.md :160 %r ; the kernel line stands at :%d' % (kl[:60], kloc), '3')
    ap = first(rm, "`(R312)`(5)")
    add('ruling (5); ferry read-first', 'the b702 append by line', ap > 0 and 'b702' in at(rm, ap), 'README.md :%d' % ap, '3')
    # ### (R314)(6)
    gl = lines_of(p('data', 'b701_glossary_rows.txt'))
    add('ruling (6)', 'data/b701_glossary_rows.txt: the companion rows h2_sign` (H2SignWide.lean :38-:39) and h2_sign_sum (:48-:49) named', first(gl, "h2_sign'") > 0 and first(gl, 'h2_sign_sum') > 0,
        'data/b701_glossary_rows.txt :%d' % first(gl, 'h2_sign_sum'), '3')
    gx = lines_of(p('data', 'glossary.txt'))
    add('ruling (6)', 'the glossary carries classK` (b703) and not yet h2_sign` or h2_sign_sum', first(gx, "classK'\t") > 0 and not first(gx, "h2_sign'\t") and not first(gx, 'h2_sign_sum\t'),
        'data/glossary.txt classK` :%d' % first(gx, "classK'\t"), '3')
    hw = g(EF, 'show', 'v0.36:SIDEExplicitFormula/H2SignWide.lean')[1].split(NL)
    add('ruling (6)', 'h2_sign` and h2_sign_sum defined in H2SignWide.lean at v0.36', any(l.startswith("def h2_sign'") for l in hw) and any(l.startswith('def h2_sign_sum') for l in hw),
        'h2_sign` :%d ; h2_sign_sum :%d' % (next((i + 1 for i, l in enumerate(hw) if l.startswith("def h2_sign'")), 0), next((i + 1 for i, l in enumerate(hw) if l.startswith('def h2_sign_sum')), 0)), '3')
    e0 = at(ot, K.ORDER_E0)
    add('ruling (6)', 'W-ORD-E0-MET-CLASSK names the companion rows (its text: "at b705 ... once that grade is settled"; the ruling: raised at b704)', 'h2_sign’ and h2_sign_sum' in e0,
        'OPEN_TRAILS :%d ; names b705 %s' % (K.ORDER_E0, 'at b705' in e0), '3')
    # ### (R314)(7)
    r74 = lines_of(p('data', 'b674_rules.txt'))
    add('ruling (7); ferry read-first', 'data/b674_rules.txt row (2), the tie-break', first(r74, '(2) THE TIE-BREAK BEYOND THE COUNT') > 0, 'data/b674_rules.txt :%d' % first(r74, '(2) THE TIE-BREAK'), '4')
    f52 = lines_of(p('data', 'b652_ferry.txt'))
    add('ruling (7)', 'b652`s order (data/b652_ferry.txt :19)', 'the next kernel by descending count under the same rules, then the companions' in at(f52, 19), 'data/b652_ferry.txt :19', '4')
    add('ruling (7)', 'the per-document tables and the agenda`s latest reading', os.path.exists(p('data', 'b700_r4_licensed.txt')) and os.path.exists(p('data', 'b648_recut_order.txt'))
        and len(glob.glob(p('data', 'b646_table_*.txt'))) >= 7, 'data/b700_r4_licensed.txt ; data/b648_recut_order.txt ; data/b646_table_*.txt %d' % len(glob.glob(p('data', 'b646_table_*.txt'))), '4')
    add('ruling (7); ferry read-first', 'data/b690_rules.txt row (2), the quotation search', first(r90, '(2) AT A RE-CUT') > 0, 'data/b690_rules.txt :%d' % first(r90, '(2) AT A RE-CUT'), '4')
    ra = rd(p('tools', 'rule_arms.py')) or ''
    add('ruling (7)', 'the quote arm G-RULE-RECUT-QUOTE branched by kind (b703)', "'G-RULE-RECUT-QUOTE'" in ra and 'paper' in ra, 'tools/rule_arms.py :%d' % first(ra.split(NL), "'G-RULE-RECUT-QUOTE'"), '4')
    add('ruling (7)', 'W-ORD-KEYSTONE-HEADS (:15454) and its trigger moved (:15496)', 'W-ORD-KEYSTONE-HEADS' in at(ot, K.ORDER_KEYSTONE) and 'THE TRIGGER MOVED' in at(ot, K.ORDER_KEYSTONE_MOVED),
        'OPEN_TRAILS :%d ; :%d' % (K.ORDER_KEYSTONE, K.ORDER_KEYSTONE_MOVED), '4')
    add('ruling (7)', 'data/b704_cut.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b704_cut.txt')), 'absent, as ordered', '4')
    # ### (R314)(8)
    for repo, bs in K.DELETE:
        mg = (g(repo, 'branch', '--merged', 'main')[1] or '').replace('*', ' ').split()
        for b in bs:
            add('ruling (8)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in mg, 'listed by `git branch --merged main` at %s before any delete' % os.path.basename(repo) if b in mg else '### NOT LISTED', '0')
    mg = (g(EF, 'branch', '--merged', 'main')[1] or '').replace('*', ' ').split()
    rh = _remote_heads(EF)
    for b in K.KERNEL_BRANCHES_PROMPT:
        add('ruling (8)', 'SIDE-explicit-formula %s, local and remote, merged (raised before any delete)' % b, b in mg and ('refs/heads/' + b) in rh,
            'local merged %s ; remote %s (one ls-remote of SIDE-explicit-formula)' % (b in mg, (rh.get('refs/heads/' + b) or '-')[:7]), '0')
    # ### (R314)(9)-(11) and the ferry
    add('ruling (9)', 'the READFIRST-CLOSURE reader', 'readfirst' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py', '0')
    add('ruling (9)', 'data/b704_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b704_readfirst.txt')), '0')
    add('ruling (10)', 'the draft at v5, held', K.DRAFT == '23228113', 'tools/b704_worklist.py DRAFT', '6')
    p3 = first(ot, 'W-ORD-P3-CONTOUR-SIGMA`**')
    add('ruling (11)', 'W-ORD-P3-CONTOUR-SIGMA at its line', p3 > 0, 'OPEN_TRAILS :%d' % p3, '6')
    rg = rd(p('data', 'b703_registrations.txt')) or ''
    add('ruling (11)', 'the detection law of (R313)(6)(ii) registered (data/b703_registrations.txt)', '(ii)' in rg, 'data/b703_registrations.txt', '6')
    pc = first(ot, 'W-ORD-PAPER-PARTNER-COPIES`**')
    add('ruling (11)', 'W-ORD-PAPER-PARTNER-COPIES at its line', pc > 0, 'OPEN_TRAILS :%d' % pc, '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C5', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''), 'tools/b693_worklist.py :52', '5')
    add('ferry C5', 'the four standing arms` figures tool and b703`s baseline', os.path.exists(p('tools', 'b703_standing_figures.py')) and os.path.exists(p('data', 'b703_standing_figures.json')),
        'tools/b703_standing_figures.py ; data/b703_standing_figures.json', '5')
    add('ferry C0', 'data/b684_rules.txt row (1), a test above 450 s its own part', '(1) A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5', '0')
    add('ferry C6', 'b673`s capture names', os.path.exists(p('data', 'b703_relay_push_out.txt')), 'data/b703_relay_push_out.txt (the form carried)', '6')
    add('ferry C6', 'the b670 form of the mirror', os.path.exists(p('data', 'b703_mirror.txt')), 'data/b703_mirror.txt (the form carried)', '6')
    add('ferry C0', 'this act`s session transcript (a new session; b703 ran in %s)' % K.PREV_SESSION[:8], os.path.exists(C.SESSION), C.SESSION, '0')
    return R


def _write(L, R, miss):
    for name, data in (('b704_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b704_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b704 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b704_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b704_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b704_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b704_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b704."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, 'D:/SIDE-lv-conservation', 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects') if r not in P.REPOS)
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b704'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b704')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b704)', 'exec'), ns)
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
        print('usage: b704_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
