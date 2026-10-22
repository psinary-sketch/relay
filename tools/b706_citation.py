# -*- coding: utf-8 -*-
"""b706_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b706's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (44411d52, the same session b705 ran in; the anchor (R316)'s line is unique in it); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b706 and its commit reach widened to the kernels as b699-b705 widened it, AND with
### (R316)(2)'s repair: a bare eight-hex token that a bank's row names as a sha256 (a root or a file hash) is not read as a commit -- the
### repair is in `answer` below, a wrapper over b682's route, diffed in data/b706_tool_repairs.txt; the `word` route is b694's.
### Routes: `check [dry]` -> data/b706_citation_check.txt (.json) ; `ferry` -> data/b706_ferry_scan.txt ; `answer <needle>` / `word <needle>` ->
###         the check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b706 from b705_citation.py's form; this tool writes only the banks named above.
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
import b706_worklist as K   # noqa: E402

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

HEAD_QUOTE = 'b705 closed: relay 9f5871da, PLACE-papers c4c4273; suite 128 of 138; root 8454a2bb2428eba3\u2026; 5 prompts answered; 15 defects'
SIX = ['G-WRITELIST-KINDS', 'G-ANSWERS-CHECKED', 'G-ENTRY-TITLE-FORM', 'G-TRAIL-LINES-EQUAL-DEFECTS', 'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-RESOLVED-EQUAL']
FOUR = ['G-READ-RULE-STANDING', 'G-WORKFLOW-FILES', 'G-RUNNER-READ', 'G-RUNNER-GATE']


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
    ot, fi = lines_of(OT), lines_of(FI)
    EF, LV, FJ = K.EF_DIR, K.LV_DIR, K.KERNEL_DIR
    # ### the ferry's read-first list, by existence
    for f in ('data/b705_closing.txt', 'data/b705_defects.txt', 'data/b705_join_grade.txt', 'data/b705_art_SIDE-faces-join_join_cache_log.txt',
              'data/b705_tool_repairs.txt', 'data/b705_closing_push_out.txt', 'data/b706_rules.txt', 'data/b700_reading4.txt', 'data/b672_roster_read.json',
              'data/b704_cells_reach.txt', 'data/b684_rules.txt', 'data/b680_rules.txt', 'data/b690_rules.txt', 'data/b675_rules.txt', 'data/b686_rules.txt',
              'tools/correspondence_gen.py', 'tools/b705_record.py', 'tools/b705_checks.py', 'tools/b705_citation.py', 'tools/circuit_read.py',
              'tools/b705_corrigendum.py', 'tools/b705_standing_figures.py', 'tools/b705_closing.py', 'tools/b705_reg_gate.py', 'tools/b705_regspec.py',
              'data/b704_nodes_zeta.txt', 'data/b704_probe_out_zeta.txt', 'data/b704_runner_SIDE-explicit-formula_probe.txt', 'data/b705_standing_figures.json'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    # ### (R316)(1), by row
    cl = lines_of(p('data', 'b705_closing.txt'))
    add('ruling (1)', 'data/b705_closing.txt :1, the head line, against (R316)(1)`s quote after whitespace is removed', _ws(cl[0]) == _ws(HEAD_QUOTE),
        'data/b705_closing.txt :1 = %r' % cl[0][:130], '0-1')
    cf = first(cl, '### CARRIED FORWARD.')
    add('ferry read-first', 'data/b705_closing.txt, the carried-forward rows (a)-(h) by line', cf > 0 and first(cl, '    (a) ', cf) > 0 and first(cl, '    (h) ', cf) > 0,
        'data/b705_closing.txt :%d (the head), (a) :%d, (h) :%d' % (cf, first(cl, '    (a) ', cf), first(cl, '    (h) ', cf)), '0-1')
    po = rd(p('data', 'b705_closing_push_out.txt')) or ''
    head = g(ROOT, 'rev-parse', '--short=8', 'HEAD')[1].strip()
    add('ruling (1); ruling (9)', 'the closing pushed alone and read back at relay main f9a60e40 (data/b705_closing_push_out.txt, to be committed)',
        'main read back at the remote: f9a60e40' in po and head == K.PRE_RELAY,
        'data/b705_closing_push_out.txt (capture-on lines %d) ; relay HEAD %s' % (po.count('capture on'), head), '0-1')
    st = g(ROOT, 'status', '--porcelain', '--', 'data/b705_closing_push_out.txt')[1].strip()
    add('ruling (9); ferry C0', 'data/b705_closing_push_out.txt uncommitted at the act`s start', st.startswith('??'), 'git status %r' % st, '0')
    co = lines_of(p('data', 'b705_contour.txt'))
    add('ruling (1)', 'data/b705_contour.txt: the contour and the tail bound each enclosing every zero of Λ_Q, the Q0 figures standing',
        first(co, 'EACH ENCLOSE EVERY ZERO') > 0 and first(co, 'THE Q0 FIGURES STAND') > 0, 'data/b705_contour.txt :%d' % first(co, 'EACH ENCLOSE EVERY ZERO'), '1')
    wb = lines_of(p('tools', 'b696_witness_balls.py'))
    add('ruling (1)', 'tools/b696_witness_balls.py :124-:146, the tail-ball tool`s zero tail', first(wb, 'def zero_tail(') == 124, 'zero_tail opens at :%d' % first(wb, 'def zero_tail('), '1')
    de = lines_of(p('data', 'b705_detection.txt'))
    add('ruling (1)', 'the detection law over the five pairs b675`s route reaches, within [0.67, 1.5], HELD, twelve beyond reach (data/b705_detection.txt)',
        first(de, 'PAIRS 17 ; COMPUTED 5, WITHIN [0.67, 1.5] 5, OUTSIDE 0 ; BEYOND REACH 12 ; THE FALSIFIER HELD') > 0,
        'data/b705_detection.txt :%d' % first(de, 'PAIRS 17 ; COMPUTED 5'), '1')
    add('ruling (1)', '"the twelve higher pairs entered as beyond the route`s modulus rule with the bound and not estimated"', first(de, 'beyond reach') > 0 and ('modulus' in NL.join(de) or 'MODULUS' in NL.join(de)),
        'data/b705_detection.txt: "beyond reach" at :%d ; the modulus rule named %s' % (first(de, 'beyond reach'), 'modulus' in NL.join(de).lower()), '1')
    wi = lines_of(p('data', 'b705_window.txt'))
    add('ruling (1)', 'the notched window at 0.79799715717868013876 + 29.55176109862911459913 i nonnegative at widths 32 to 128 and negative at 192, HELD (data/b705_window.txt)',
        first(wi, "NEGATIVE AT ['192']") > 0 and first(wi, 'THE HYPOTHESIS HELD') > 0 and first(wi, K.__dict__.get('BAND_ZERO', ('0.79799715717868013876',))[0]) > 0 or (
            first(wi, "NEGATIVE AT ['192']") > 0 and first(wi, '0.79799715717868013876') > 0),
        'data/b705_window.txt :%d (the sign line) ; the zero named at :%d' % (first(wi, "NEGATIVE AT ['192']"), first(wi, '0.79799715717868013876')), '1')
    i6 = lines_of(p('data', 'b705_i6_ranking.txt'))
    add('ruling (1)', 'data/b705_i6_ranking.txt with the support radius at its head', first(i6, 'THE TOP (d`) THE SUPPORT RADIUS') > 0, 'data/b705_i6_ranking.txt :%d' % first(i6, 'THE TOP (d`) THE SUPPORT RADIUS'), '1')
    rg = lines_of(p('data', 'b705_registrations.txt'))
    add('ruling (1); ruling (12)', 'data/b705_registrations.txt (iii) the sign-onset radius, committed alone before any number (d139cfcf)',
        first(rg, '(iii)') > 0 and 'sign-onset' in NL.join(rg).lower() and len(g(ROOT, 'log', '--format=%h', '--', 'data/b705_registrations.txt')[1].split()) == 1,
        'data/b705_registrations.txt (iii) :%d ; commits touching it %s' % (first(rg, '(iii)'), g(ROOT, 'log', '--format=%h', '--', 'data/b705_registrations.txt')[1].split()), '1')
    add('ruling (1)', 'the Connes–Consani range read by page from the fetched source (data/b705_source_cc_2006_13771.txt)', os.path.exists(p('data', 'b705_source_cc_2006_13771.txt')), 'data/b705_source_cc_2006_13771.txt', '1')
    e0 = rd(p('data', 'b705_e0_met.txt')) or ''
    add('ruling (1)', 'E0`s RESTRICTIONS given four heads, the three inclusions DERIVES, every other header unchanged (data/b705_e0_met.txt)',
        'CHANGED BY THE EXTENSION 3' in e0 and 'EVERY OTHER NAME UNCHANGED True' in e0, 'data/b705_e0_met.txt', '1')
    jg = lines_of(p('data', 'b705_join_grade.txt'))
    add('ruling (1); ferry read-first', 'data/b705_join_grade.txt: the join HELD at its one run, the gate NOT DERIVES', first(jg, 'THE JOIN HELD') > 0 and first(jg, 'THE GATE NOT DERIVES') > 0,
        'data/b705_join_grade.txt :%d' % first(jg, 'THE JOIN HELD'), '1-3')
    cg_ = lines_of(p('data', 'b705_art_SIDE-faces-join_join_cache_log.txt'))
    add('ruling (1); ferry read-first', 'the join run`s artifact bank for (j): data/b705_art_SIDE-faces-join_join_cache_log.txt, "failed to fetch cache"',
        first(cg_, 'failed to fetch cache') > 0, 'data/b705_art_SIDE-faces-join_join_cache_log.txt :%d' % first(cg_, 'failed to fetch cache'), '1-3')
    tip = g(FJ, 'rev-parse', 'main')[1].strip()
    add('ruling (1); ruling (4)', 'SIDE-faces-join created at 732c1b49, its main there still', tip == K.JOIN_TIP_B705, 'SIDE-faces-join main %s' % tip[:8], '3')
    ar = json.loads(rd(p('data', 'b705_act_root.json')) or '{}')
    add('ruling (1)', 'the root 8454a2bb chained from 97bd2133', (ar.get('root') or '').startswith('8454a2bb') and (ar.get('previous') or '').startswith('97bd2133'),
        'data/b705_act_root.json (root %s, prev %s, banks %d)' % ((ar.get('root') or '')[:8], (ar.get('previous') or '')[:8], len([it for it in ar.get('items') or [] if it.startswith('data/')])), '1')
    ck, cp = rd(p('data', 'b705_checks.txt')) or '', rd(p('data', 'b705_checks_postpush.txt')) or ''
    add('ruling (1)', 'suite 131 of 138 pre-push and 128 of 138 post-push', 'ARMS RUN : 138. ### LIVE PASSING : 131.' in ck and 'ARMS RUN : 138. ### LIVE PASSING : 128.' in cp,
        'data/b705_checks.txt ; data/b705_checks_postpush.txt', '1')
    m10 = re.search(r"LIVE FAILING : 10 \[(.*?)\]", cp)
    fails = [x.strip().strip("'") for x in (m10.group(1) if m10 else '').split(',') if x.strip()]
    add('ruling (1); ruling (2)', 'four failures declared on the face, six after the seal, as the post-push bank lists them', sorted(fails) == sorted(SIX + FOUR) and "failing beyond them %s" % SIX in cp,
        'data/b705_checks_postpush.txt :12 LIVE FAILING %d ; beyond the face %s' % (len(fails), SIX), '1')
    sc = json.loads(rd(p('data', 'b705_scores_close.json')) or '{}')
    sr = json.loads(rd(p('data', 'b705_scores.json')) or '{}')
    add('ruling (1)', 'N1-N4 and S1-S3 HELD, N5 HELD at the record and REFUTED at the close on data/b706_rules.txt',
        all((sc.get(k) or [''])[0] == 'HELD' for k in ('N1', 'N2', 'N3', 'N4', 'S1', 'S2', 'S3')) and (sr.get('N5') or [''])[0] == 'HELD'
        and (sc.get('N5') or [''])[0] == 'REFUTED' and 'b706_rules' in (sc.get('N5') or ['', ''])[1],
        'data/b705_scores.json N5 %s ; data/b705_scores_close.json: %s' % ((sr.get('N5') or ['-'])[0], ', '.join('%s %s' % (k, (sc.get(k) or ['-'])[0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3'))), '1')
    df = lines_of(p('data', 'b705_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", NL.join(df), re.M)
    add('ruling (1); ferry read-first', 'data/b705_defects.txt (rows are defects as lettered): fifteen, (a)-(o), four the navigator`s ((g), (h), (i), (k))',
        [x for x, _o in lt] == list('abcdefghijklmno') and [x for x, o in lt if o == 'NAVIGATOR'] == ['g', 'h', 'i', 'k'],
        'letters %s ; the navigator`s %s' % (''.join(x for x, _o in lt), [x for x, o in lt if o == 'NAVIGATOR']), '1')
    sl, tl = _defect_row(df, 'l')
    add('ruling (1)', 'the three excluded files moved to the session scratchpad with sha256 equal before and after ((l))', 'scratchpad' in tl and 'equal' in tl, 'data/b705_defects.txt (l) :%d' % sl, '1')
    mi = lines_of(p('data', 'b705_mirror.txt'))
    mt = ' '.join(mi)
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-22-b705.zip CLEAN with the root line', 'mirror-refresh-2026-10-22-b705.zip' in mt and 'CLEAN ON ALL THREE CLAUSES' in mt and 'Act root: b705 8454a2bb' in mt and os.path.exists(K.MIRROR_ZIP),
        'data/b705_mirror.txt :%d (the root line) ; the zip exists %s' % (first(mi, 'THE ROOT LINE'), os.path.exists(K.MIRROR_ZIP)), '1')
    na = len(re.findall(r'^### PROMPT ', rd(p('data', 'b705_author_answers.txt')) or '', re.M))
    add('ruling (1)', '"5 prompts answered": the answers bank`s 4 rows and the root`s prompt, put in two calls under (m)', na == 4 and 'second' in _defect_row(df, 'm')[1].lower(),
        'data/b705_author_answers.txt PROMPT rows %d ; (m) at data/b705_defects.txt :%d' % (na, _defect_row(df, 'm')[0]), '1')
    add('ruling (1)', 'b705`s entry at FINDINGS :9990, b704`s weight :9974, the corrigendum :9976, the trail OPEN_TRAILS :15592',
        at(fi, K.B705_ENTRY).startswith('## ') and 'b704' in at(fi, K.B705_WEIGHT) and at(fi, K.B705_CORRIGENDUM).startswith('## Corrigendum') and at(ot, K.B705_TRAIL).startswith('### b705'),
        'FINDINGS :%d %r ; :%d ; :%d ; OPEN_TRAILS :%d' % (K.B705_ENTRY, at(fi, K.B705_ENTRY)[:60], K.B705_WEIGHT, K.B705_CORRIGENDUM, K.B705_TRAIL), '1')
    add('ruling (1)', '"nothing deposited": the draft at v5, held', K.DRAFT == '23228113', 'tools/b706_worklist.py DRAFT', '6')
    # ### (R316)(2)
    chk = lines_of(p('tools', 'b705_checks.py'))
    ra = lines_of(p('tools', 'rule_arms.py'))
    wl = [i for i, l in enumerate(chk, 1) if 'G-WRITELIST-KINDS' in l]
    add('ruling (2); ferry read-first', 'G-WRITELIST-KINDS`s arm source by path and line (tools/b705_checks.py, a standing-c arm over the face`s (W) list)', len(wl) >= 2,
        'tools/b705_checks.py names it at %s (C_ARMS :144; the arm`s row and its predicate at the later lines)' % wl, '1')
    for arm, fn, src in (('G-ANSWERS-CHECKED', 'def _answers_checked(', 'b705_checks.py'), ('G-ENTRY-TITLE-FORM', 'def entry_title_ok(', 'b705_checks.py')):
        L_ = chk if src == 'b705_checks.py' else ra
        n = first(L_, fn)
        where = first(L_, "'%s'" % arm)
        add('ruling (2); ferry read-first', '%s`s arm source by path and line (%s %s)' % (arm, src, fn.rstrip('(')), n > 0 and where > 0, 'tools/%s :%d (the predicate) ; the arm named at :%d' % (src, n, where), '1')
    add('ruling (2)', 'G-WRITELIST-KINDS failing on data/b706_rules.txt alone, "the navigator`s", entered as an event (the defects bank`s EVENTS)',
        first(df, 'G-WRITELIST-KINDS fails after the seal, pre-push and post-push, on relay/data/b706_rules.txt alone') > 0, 'data/b705_defects.txt :%d' % first(df, 'G-WRITELIST-KINDS fails after the seal'), '1')
    sn, tn = _defect_row(df, 'n')
    add('ruling (2)', '(n): the checker reading a sha256 prefix as a commit', 'sha256' in tn.lower() and 'commit' in tn.lower(), 'data/b705_defects.txt (n) :%d' % sn, '1')
    so, to = _defect_row(df, 'o')
    add('ruling (2)', '(o): the needle`s lower-case "the" against the entry`s "The"', 'lower case' in to.lower() and 'entry_title_ok' in to, 'data/b705_defects.txt (o) :%d' % so, '1')
    add('ruling (2)', 'the three trail-equality arms failing from (o)`s lettering after the trail landed, no repair', 'trail having landed first' in to and 'three trail-equality arms' in to, 'data/b705_defects.txt (o) :%d' % so, '1')
    ok2, how2 = rule_clause('R315', (2,))
    add('ruling (2)', '(R315)(2), the sequence rule: no defect lettered after the trail`s dry run without that dry run re-read', ok2, how2, '1')
    rec = lines_of(p('tools', 'b705_record.py'))
    add('ruling (2); ferry read-first', 'tools/b705_record.py ROOT_EXCLUDE by line (:57-:59)', first(rec, 'R.ROOT_EXCLUDE = re.compile(') == 57, 'tools/b705_record.py :%d' % first(rec, 'R.ROOT_EXCLUDE = re.compile('), '1')
    r6 = lines_of(p('data', 'b706_rules.txt'))
    add('ruling (2); ferry read-first', 'data/b706_rules.txt row (1): ROOT_EXCLUDE carried and extended, a dry rootbanks READY before the seal, a face with READY False not locked',
        first(r6, "(1) THE ROOT ROUTE'S EXCLUSION LIST, CARRIED AND EXTENDED AT CARRY TIME, WITH A DRY RUN BEFORE THE SEAL") == 6 and first(r6, 'a face whose dry READY reads False is not locked') > 0,
        'data/b706_rules.txt :6-:15', '1')
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    lastrow = max([int(m) for m in re.findall(r'^  \((\d+)\) ', NL.join(cg), re.M)] or [0])
    add('ruling (2)', 'the corrigenda bank, appended only (its last row (25), b705`s)', lastrow == 25, 'data/b675_corrigenda.txt, last row (%d) at :%d' % (lastrow, first(cg, '  (%d) ' % lastrow)), '1')
    add('ruling (2)', 'b705`s corrigendum tool to carry', os.path.exists(p('tools', 'b705_corrigendum.py')), 'tools/b705_corrigendum.py', '1')
    b2 = lines_of(p('data', 'b705_checks_postpush_standing-b2.txt'))
    add('ruling (2)', 'the standing-b2 part "577 s post-push" (the part bank`s own run line; the summed bank rounds it to 576)', first(b2, '### the run took 577 s') == 25 and 'standing-b2 : ARMS 0 ; 576 s' in (rd(p('data', 'b705_checks_postpush.txt')) or ''),
        'data/b705_checks_postpush_standing-b2.txt :25 "the run took 577 s" (the chain phase 507 s at :5-:6) ; data/b705_checks_postpush.txt :7 prints 576 s', '1')
    add('ruling (2); ferry C0', 'data/b684_rules.txt row (1), a part over 450 s splits the next run', '(1) A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5', '0')
    add('ruling (2)', 'data/b706_arm_sort.txt and data/b706_tool_repairs.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b706_arm_sort.txt')) and not os.path.exists(p('data', 'b706_tool_repairs.txt')), 'absent, as ordered', '1')
    # ### (R316)(3)
    add('ruling (3); ferry read-first', 'W-ORD-PAPER-PARTNER-COPIES (:15446) disposition (iii) over the 17 pairs, trigger b706, the 102 standing reader hits',
        'W-ORD-PAPER-PARTNER-COPIES' in at(ot, K.ORDER_PARTNER) and '(iii), rename in place' in at(ot, K.ORDER_PARTNER) and '17 pairs' in at(ot, K.ORDER_PARTNER) and '102 standing reader hits' in at(ot, K.ORDER_PARTNER)
        and 'Trigger: the re-cut act b706' in at(ot, K.ORDER_PARTNER), 'OPEN_TRAILS :%d' % K.ORDER_PARTNER, '2')
    r4 = lines_of(p('data', 'b700_reading4.txt'))
    add('ruling (3); ferry read-first', 'data/b700_reading4.txt (rows are readings; row (18)`s unit lines differing): 17 pairs ; 131 lines ; a regenerated cell 123, a hand edit 8 (:66-:76)',
        first(r4, '17 pairs ; 131 lines differing') == 67 and 'a regenerated cell 123, a hand edit 8' in at(r4, 70), 'data/b700_reading4.txt :66-:76 (row (18): the pairs by name :67-:70, the causes :70, the sort by hand :72-:76)', '2')
    rr = json.loads(rd(p('data', 'b672_roster_read.json')) or '{}')
    add('ruling (3); ferry read-first', 'data/b672_roster_read.json, the generator`s roster (its tables with their partners)', bool(rr), 'data/b672_roster_read.json keys %s' % list(rr)[:6], '2')
    sf = lines_of(p('data', 'b705_standing_figures.txt'))
    add('ruling (3)', 'G-PARTNER-COPIES at 131 at b705 (the baseline the renames move)', first(sf, 'PARTNERS 131') > 0, 'data/b705_standing_figures.txt :%d' % first(sf, 'PARTNERS 131'), '2')
    rgm = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (3)', 'PLACE-papers REGISTRY.md, the rows keeping the version as the tag', len(rgm) > 10 and any('|' in l for l in rgm), 'PLACE-papers REGISTRY.md (%d lines)' % len(rgm), '2')
    add('ruling (3)', 'PLACE-papers archive/ exists for the retired copies', os.path.isdir(os.path.join(PP, 'archive')), 'PLACE-papers archive/', '2')
    add('ruling (3)', 'data/b706_partners.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b706_partners.txt')), 'absent, as ordered', '2')
    # ### (R316)(4)
    lf = (g(FJ, 'show', '%s:lakefile.toml' % K.JOIN_TIP_B705)[1] or '').split(NL)
    add('ruling (4); ferry read-first', 'SIDE-faces-join`s lakefile at 732c1b49 by line: mathlib at de5ce8a9 (:11-:14), SIDEExplicitFormula (:16-:19), sideLvConservation last (:21-:24)',
        first(lf, 'name = "mathlib"') == 12 and first(lf, 'rev = "%s"' % K.EF_MATHLIB) == 14 and first(lf, 'name = "SIDEExplicitFormula"') == 17 and first(lf, 'name = "sideLvConservation"') == 22,
        '732c1b49:lakefile.toml mathlib :%d, rev :%d, SIDEExplicitFormula :%d, sideLvConservation :%d' % (first(lf, 'name = "mathlib"'), first(lf, 'rev = "%s"' % K.EF_MATHLIB), first(lf, 'name = "SIDEExplicitFormula"'), first(lf, 'name = "sideLvConservation"')), '3')
    tree = (g(FJ, 'ls-tree', '--name-only', K.JOIN_TIP_B705)[1] or '').split()
    add('ferry read-first', 'SIDE-faces-join`s lake-manifest.json at 732c1b49 "by line"', 'lake-manifest.json' in tree,
        'the tree at 732c1b49: %s -- NO lake-manifest.json (the root had none; that absence is (j)`s cause, Lake resolving from the last require`s manifest)' % ' '.join(tree), '3')
    add('ruling (4)', 'the ruling`s order "explicit-formula`s require ahead of lv-conservation`s, Mathlib explicitly before both" against 732c1b49`s order (mathlib, SIDEExplicitFormula, sideLvConservation)',
        first(lf, 'name = "mathlib"') < first(lf, 'name = "SIDEExplicitFormula"') < first(lf, 'name = "sideLvConservation"'),
        'at 732c1b49 the order is already mathlib, SIDEExplicitFormula, sideLvConservation -- the ruling`s ordering is the lakefile`s; the manifest is what (j) lacked (Lake`s hint: require mathlib LAST, or a manifest at the root)', '3')
    sj, tj = _defect_row(df, 'j')
    add('ruling (4)', '(j): Lake resolving from the last require`s manifest, Lake`s own hint (require mathlib last, or a manifest at the root)', 'require mathlib last' in tj and 'manifest at the root' in tj, 'data/b705_defects.txt (j) :%d' % sj, '3')
    ok5, how5 = rule_clause('R315', (5,))
    add('ruling (4)', '(R315)(5), the join`s specification (the grade as it specified it)', ok5, how5, '3')
    rhj = _remote_heads(FJ)
    tags = (g(FJ, 'tag', '--list')[1] or '').split()
    add('ruling (4)', 'SIDE-faces-join: no tag yet (v0.1.0 to be made on DERIVES), main at the remote 732c1b49', not tags and (rhj.get('refs/heads/main') or '').startswith('732c1b49'),
        'tags %s ; remote main %s -- one ls-remote of SIDE-faces-join' % (tags or 'NONE', (rhj.get('refs/heads/main') or '-')[:8]), '3')
    add('ruling (4)', 'data/b706_join_grade.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b706_join_grade.txt')), 'absent, as ordered', '3')
    # ### (R316)(5)
    add('ruling (5); ferry read-first', 'W-ORD-WORKFLOW-PROBE-STEP at :15544, trigger b706, "a root ChainProbe.lean when the ref carries one"',
        'W-ORD-WORKFLOW-PROBE-STEP' in at(ot, K.ORDER_PROBE_STEP) and 'Trigger: the re-cut act b706' in at(ot, K.ORDER_PROBE_STEP) and 'ChainProbe.lean' in at(ot, K.ORDER_PROBE_STEP), 'OPEN_TRAILS :%d' % K.ORDER_PROBE_STEP, '3')
    wf = lines_of(os.path.join(EF, '.github', 'workflows', 'build-module.yml'))
    add('ruling (5); ferry read-first', 'SIDE-explicit-formula`s build-module.yml at main by line: the print step (:78) and the closure step (:98)',
        first(wf, 'name: Axioms of the named terminals') == 78 and first(wf, 'name: Constant closure') == 98,
        '.github/workflows/build-module.yml :%d, :%d (%d lines)' % (first(wf, 'name: Axioms of the named terminals'), first(wf, 'name: Constant closure'), len(wf)), '3')
    rh = _remote_heads(EF)
    add('ruling (5)', 'SIDE-explicit-formula main at v0.37 = 38e2734, local and remote', g(EF, 'rev-parse', 'main')[1].strip() == K.EF_V037 and (rh.get('refs/heads/main') or '').startswith('38e2734'),
        'main %s ; remote %s -- one ls-remote of SIDE-explicit-formula' % (g(EF, 'rev-parse', 'main')[1].strip()[:7], (rh.get('refs/heads/main') or '-')[:7]), '3')
    add('ruling (5)', 'probe-b704`s form: the probe run as the root CircuitClosure.lean of a scratch branch (OPEN_TRAILS :15542)', 'root CircuitClosure.lean of the scratch branch probe-b704' in at(ot, 15542), 'OPEN_TRAILS :15542', '3-4')
    # ### (R316)(6)
    add('ruling (6); ferry read-first', 'W-ORD-CORRESPONDENCE-EF-REACH at :15546, trigger b706, the 11 table lines, the reach printed beside the figure',
        'W-ORD-CORRESPONDENCE-EF-REACH' in at(ot, K.ORDER_EF_REACH) and '11 roster table lines' in at(ot, K.ORDER_EF_REACH) and 'Trigger: the re-cut act b706' in at(ot, K.ORDER_EF_REACH), 'OPEN_TRAILS :%d' % K.ORDER_EF_REACH, '3')
    cgl = lines_of(p('tools', 'correspondence_gen.py'))
    add('ruling (6); ferry read-first', 'tools/correspondence_gen.py`s parser by line: parse_kernel_cell (:153), kernels_of (:636), regen_lines (:281), regen_bytes (:473)',
        first(cgl, 'def parse_kernel_cell(') == 153 and first(cgl, 'def kernels_of(') == 636 and first(cgl, 'def regen_bytes(') == 473,
        'tools/correspondence_gen.py parse_kernel_cell :%d ; kernels_of :%d ; regen_lines :%d ; regen_bytes :%d' % (first(cgl, 'def parse_kernel_cell('), first(cgl, 'def kernels_of('), first(cgl, 'def regen_lines('), first(cgl, 'def regen_bytes(')), '3')
    cre = lines_of(p('data', 'b704_cells_reach.txt'))
    add('ruling (6); ruling (7); ferry read-first', 'data/b704_cells_reach.txt (rows are (line, theorem, tag) mentions): 11 table lines, 15 mentions, 4 equal, 0 differs, 11 unbanked',
        first(cre, 'EQUAL 4 ; differs 0 ; unbanked 11') > 0 and first(cre, 'MENTIONS READ 15 (LINES 11)') > 0 and first(cre, '(11 table lines naming the kernel)') > 0,
        'data/b704_cells_reach.txt :3 (the 11 lines), :%d (the raised mentions), :%d' % (first(cre, '### THE RAISED MENTIONS'), first(cre, 'EQUAL 4 ; differs 0')), '3-4')
    cr = rd(p('data', 'b704_correspondence_run.txt')) or ''
    add('ruling (6)', 'the generator`s 16 parsed kernels at b704 (so 17 with SIDE-explicit-formula)', 'KERNELS 16' in cr, 'data/b704_correspondence_run.txt', '3')
    add('ruling (6)', 'G-CORRESPONDENCE-CURRENCY at 0 at b705 (data/b705_standing_figures.txt)', first(sf, 'CORRESPONDENCE 0') > 0, 'data/b705_standing_figures.txt :%d' % first(sf, 'CORRESPONDENCE 0'), '3')
    # ### (R316)(7)
    add('ruling (7); ferry read-first', 'W-ORD-ENTRY-TAG-PRINTS at :15590, trigger b706, the form (a scratch branch at each tag carrying the workflow and a print list)',
        'W-ORD-ENTRY-TAG-PRINTS' in at(ot, K.ORDER_TAG_PRINTS) and 'Trigger: b706' in at(ot, K.ORDER_TAG_PRINTS) and 'a scratch branch cut at the tag carrying the workflow and a print list' in at(ot, K.ORDER_TAG_PRINTS),
        'OPEN_TRAILS :%d' % K.ORDER_TAG_PRINTS, '4')
    v1, v2 = g(EF, 'rev-list', '-n', '1', 'v0.1')[1].strip(), g(EF, 'rev-list', '-n', '1', 'v0.2')[1].strip()
    add('ruling (7)', 'v0.1 = baed4df and v0.2 = 5c72cad of SIDE-explicit-formula, local; at the remote', v1 == K.EF_V01 and v2 == K.EF_V02 and any(k.endswith('v0.1') for k in g(EF, 'ls-remote', '--tags', 'origin')[1].split()) ,
        'v0.1 %s ; v0.2 %s ; the remote tags read once' % (v1[:7], v2[:7]), '4')
    for tg in ('v0.1', 'v0.2'):
        tr = (g(EF, 'ls-tree', '--name-only', '-r', tg)[1] or '').split()
        add('ruling (7)', 'at %s neither print_targets.txt nor the workflow (both entered at b658), so the branch carries them' % tg, 'print_targets.txt' not in tr and '.github/workflows/build-module.yml' not in tr,
            '%s tree: %d files ; print_targets.txt %s ; the workflow %s' % (tg, len(tr), 'print_targets.txt' in tr, '.github/workflows/build-module.yml' in tr), '4')
    for tg, nm in ((('v0.1', 'theorem ch_iff_rh :'), ('v0.2', 'theorem h2_sign_iff_rh :'))):
        hit = _kgrep(EF, tg, nm, '.')
        add('ruling (7)', '%s at %s, the mentioned theorem' % (nm, tg), bool(hit), hit[:100] or 'NOT FOUND', '4')
    for _tg, b in K.PRINT_BRANCHES:
        add('ruling (7)', 'the scratch branch %s absent before the act, local and remote' % b, not g(EF, 'branch', '--list', b)[1].strip() and ('refs/heads/%s' % b) not in rh, 'local %s ; remote %s' % (g(EF, 'branch', '--list', b)[1].strip() or 'absent', 'present' if ('refs/heads/%s' % b) in rh else 'absent'), '4')
    add('ruling (7)', 'data/b706_prints_v0.1.txt and data/b706_prints_v0.2.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b706_prints_v0.1.txt')) and not os.path.exists(p('data', 'b706_prints_v0.2.txt')), 'absent, as ordered', '4')
    # ### (R316)(8)
    nz = lines_of(p('data', 'b704_nodes_zeta.txt'))
    add('ruling (8)', 'the node list`s form, data/b704_nodes_zeta.txt, with the lv-conservation row', len(nz) > 5 and first(nz, 'lv-conservation') > 0, 'data/b704_nodes_zeta.txt (%d lines; lv-conservation at :%d)' % (len(nz), first(nz, 'lv-conservation')), '4')
    add('ruling (8)', 'the faces page`s generator (tools/chain_page.py --from-output) and the page', os.path.exists(p('tools', 'chain_page.py')) and os.path.exists(os.path.join(PP, K.FACES_PAGE)), 'tools/chain_page.py ; PLACE-papers %s' % K.FACES_PAGE, '4')
    add('ruling (8)', 'data/b706_nodes_zeta.txt -- TO BE WRITTEN where (4) tags', not os.path.exists(p('data', 'b706_nodes_zeta.txt')), 'absent, as ordered', '4')
    # ### (R316)(9)-(12) and the ferry
    for repo, bs in K.DELETE:
        mg = (g(repo, 'branch', '--merged', 'main')[1] or '').replace('*', ' ').split()
        for b in bs:
            add('ruling (9)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in mg, 'listed by `git branch --merged main` at %s before any delete' % os.path.basename(repo) if b in mg else '### NOT LISTED', '0')
    add('ruling (9)', 'the 2,560 MB hold', K.HOLD == 2560, 'tools/b706_worklist.py HOLD', '0')
    add('ruling (10)', 'the READFIRST-CLOSURE reader', 'def readfirst(' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py :%d' % first(lines_of(p('tools', 'circuit_read.py')), 'def readfirst('), '0')
    add('ruling (10)', 'data/b706_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b706_readfirst.txt')), '0')
    add('ruling (11)', 'the draft at v5, held', K.DRAFT == '23228113', 'tools/b706_worklist.py DRAFT', '6')
    add('ruling (12)', 'data/b705_registrations.txt (iii) for b707, "committed alone before the ranking"', first(rg, 'COMMITTED ALONE') > 0 or first(rg, '(iii)') > 0, 'data/b705_registrations.txt :%d' % first(rg, '(iii)'), '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C5', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''), 'tools/b693_worklist.py :52', '5')
    add('ferry C5', 'the four standing arms` figures tool and b705`s baseline', os.path.exists(p('tools', 'b705_standing_figures.py')) and os.path.exists(p('data', 'b705_standing_figures.json')),
        'tools/b705_standing_figures.py ; data/b705_standing_figures.json', '5')
    add('ferry', 'data/b680_rules.txt (1), a binary bank beside a text hashes bank', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt :5', '5')
    add('ferry', 'data/b690_rules.txt row (2)', first(lines_of(p('data', 'b690_rules.txt')), '(2) AT A RE-CUT') == 9, 'data/b690_rules.txt :9', '2')
    add('ferry C6', 'b673`s capture names', os.path.exists(p('data', 'b705_relay_push_out.txt')), 'data/b705_relay_push_out.txt (the form carried)', '6')
    add('ferry C6', 'the b670 form of the mirror', os.path.exists(p('data', 'b705_mirror.txt')), 'data/b705_mirror.txt (the form carried)', '6')
    add('ferry C0', 'this act`s session transcript (the same session b705 ran in)', os.path.exists(C.SESSION), C.SESSION, '0')
    return R


def _write(L, R, miss):
    for name, data in (('b706_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b706_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b706 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b706_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b706_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b706_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b706_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


# ### (R316)(2), THE REPAIR OF THE ANSWER CHECKER (b705 defect (n)): b682's route reads every bare eight-hex token as a commit. A token that a
# ### bank's row names as a sha256 -- the root list (data/act_roots.txt, a 64-hex root per act), a hashes bank's row, or a bank line carrying
# ### "sha256" beside the token -- is a root prefix or a file hash, not a commit, and is checked against that bank's row instead.
_HEX8 = re.compile(r'(?<![0-9a-f])([0-9a-f]{8})(?![0-9a-f])')


def _sha_rows():
    """every 64-hex sha256 any bank's row names, mapped by its first eight characters to (bank, line)."""
    out = {}
    for q in [os.path.join(D, 'act_roots.txt')] + sorted(glob.glob(os.path.join(D, '*.txt')), reverse=True):   # ### the later act's row named first
        t = rd(q) or ''
        if 'sha256' not in t and not q.endswith('act_roots.txt') and not q.endswith('_hashes.txt'):
            continue
        for i, l in enumerate(t.split(NL), 1):
            if 'sha256' in l or q.endswith('act_roots.txt') or q.endswith('_hashes.txt'):
                for m in re.finditer(r'(?<![0-9a-f])([0-9a-f]{64})(?![0-9a-f])', l):
                    out.setdefault(m.group(1)[:8], ('data/' + os.path.basename(q), i))
    return out


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b706, and the repair above: before b682's body runs, every eight-hex
    token of the answer that a bank's row names as a sha256 is checked against that row and printed, and masked from b682's commit reading."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.KERNEL_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b706'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b706')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b706)', 'exec'), ns)
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
        print('usage: b706_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
