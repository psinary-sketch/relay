# -*- coding: utf-8 -*-
"""b710_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b710's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (c9e4ce2d, a NEW session after the author's /clear; the anchor (R320)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b710, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b710_citation_check.txt
### (.json) ; `ferry` -> data/b710_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Written by the Write tool at b710 from b709_citation.py's form (its engine :1-:98 and :339-:462 read by offset and limit, its cite rows
### :99-:336 not read and replaced by this ruling's); this tool writes only the banks named above.
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
import b710_worklist as K   # noqa: E402

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

HEAD_QUOTE = 'b709 closed: relay 8b842c9a, PLACE-papers 07978f3; suite 144 of 147; root b3213c0b530e6b1d\u2026; 1 prompt answered; 8 defects'


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


def _heading(L, pat):
    """the first markdown heading line matching the regex pat, by line number (0 if none)."""
    rx = re.compile(pat)
    return next((i + 1 for i, l in enumerate(L) if l.startswith('#') and rx.search(l)), 0)


def _pp_files(term):
    """the tracked PLACE-papers files naming `term` (git grep -l, the paths alone), archive/ and outputs/ beside the rest."""
    out = g(PP, 'grep', '-l', '-F', '-e', term, '--', '.')[1] or ''
    return [x for x in out.split(NL) if x.strip()]


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    ot, fi = lines_of(OT), lines_of(FI)
    # ### the ferry's read-first list and the banks (R320)(1) names, by existence
    for f in ('data/b709_closing.txt', 'data/b709_defects.txt', 'data/b709_grid.txt', 'data/b709_grid_hashes.txt', 'data/b709_pairs.txt',
              'data/b709_pairs_hashes.txt', 'data/b709_port.txt', 'data/b709_port_edit.txt', 'data/b709_registrations.txt', 'data/b709_tool_repairs.txt',
              'data/b709_closing_push_out.txt', 'data/b709_ferry.txt', 'data/b700_reading4.txt', 'data/b690_reading3.txt',
              'data/b705_read_calls.txt', 'data/b706_read_calls.txt', 'data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt',
              'tools/b378_lockgate.py', 'tools/test_elab_reader_b634.py', 'tools/b634_elab.py', 'data/b680_rules.txt', 'data/b675_rules.txt',
              'data/b684_rules.txt', 'data/b686_rules.txt', 'data/b706_rules.txt', 'data/b708_rules.txt', 'data/b709_rules.txt', 'data/b675_corrigenda.txt',
              K.B709_FACE, 'data/b709_act_root.json', 'data/b709_root_banks.txt', 'data/b709_scores.json', 'data/b709_scores_close.json',
              'data/b709_mirror.txt', 'data/b709_checks.txt', 'data/b709_checks_postpush.txt', 'data/b709_seal_hashes.json', 'data/b709_author_answers.txt',
              'data/b709_standing_figures.json', 'data/b709_report.txt', 'data/b709_corrigendum.txt', 'data/b709_tests_stepzero.txt',
              'data/b708_tests_withheld.json', 'tools/b709_worklist.py', 'tools/b709_tests.py', 'tools/b709_citation.py', 'tools/b709_record.py',
              'tools/b709_checks.py', 'tools/b709_closing.py', 'tools/b709_reg_gate.py', 'tools/b709_regspec.py', 'tools/b709_corrigendum.py',
              'tools/b709_carry.py', 'tools/b709_report.py', 'tools/b709_pairs.py', 'tools/b709_grid.py', 'tools/b706_standing_figures.py',
              'tools/circuit_read.py', 'tools/mirror_verify.py', 'tools/mirror_build.ps1', 'tools/mirror_prevbuild.json', 'tools/push_gated.sh',
              'tools/act_root.py', 'tools/rule_arms.py', 'tools/ferry_scan.py', 'tools/b675_li_bench.py', 'tools/b704_read_arm.py'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    # ### the papers by their files of record
    for k, f in sorted(K.PAPERS.items()):
        add('ferry read-first', 'PLACE-papers %s (%s)' % (f, k), os.path.exists(os.path.join(PP, f)), 'exists at the working tree, %d lines' % len(lines_of(os.path.join(PP, f))), '0-3')
    tk = lines_of(os.path.join(PP, K.PAPERS['TECHNE_TOOLKIT']))
    hist = g(PP, 'log', '--format=%h %s', '-1', 'f915d6d')[1] or ''
    add('ferry read-first', 'TECHNE_TOOLKIT_v8_3 -- the versioned copy renamed in place by b706 ((R316)(3)) to phase1.5/method/TECHNE_TOOLKIT.md, its version line v8.3',
        tk[7].startswith('**v8.3') and 'TECHNE_TOOLKIT renamed in place' in hist and not os.path.exists(os.path.join(PP, 'phase1.5/method/TECHNE_TOOLKIT_v8_3.md')),
        'TECHNE_TOOLKIT.md :8 %r ; PLACE-papers %s ; the versioned name absent at the tree -- the name clause: the file of record' % (tk[7][:40], hist[:60]), '0-3')
    for k, pats in (('TECHNE_TOOLKIT', (r'^#+\s*(§\s*)?II[.\s:—-]', r'^#+\s*(§\s*)?V[.\s:—-]')),
                    ('METHOD_CANON', (r'^#+\s*(§\s*)?III[.\s:—-]', r'^#+\s*(§\s*)?IV[.\s:—-]', r'^#+\s*(§\s*)?V[.\s:—-]', r'^#+\s*(§\s*)?VI[.\s:—-]')),
                    ('E_DIFFICULTY_THEOREM', (r'^#+\s*(§\s*)?III[.\s:—-]', r'^#+\s*(§\s*)?IV[.\s:—-]', r'^#+\s*(§\s*)?V[.\s:—-]')),
                    ('ENUMERA', (r'^#+\s*(§\s*)?II[.\s:—-]',)),
                    ('INSTRUMENTS', (r'I-1\b', r'I-5\b', r'I-6\b'))):
        L = lines_of(os.path.join(PP, K.PAPERS[k]))
        for pat in pats:
            n = _heading(L, pat)
            add('ferry read-first', '%s, the section %r by its heading' % (K.PAPERS[k], pat), n > 0, ':%d %r' % (n, at(L, n)[:90]) if n else 'NO HEADING MATCHES', '0-3')
    bm = lines_of(os.path.join(PP, K.PAPERS['BRIGHTENING_MOVES']))
    moves = [i + 1 for i, l in enumerate(bm) if l.startswith('| **')]
    add('ruling (5)(ii)', 'THE_BRIGHTENING_MOVES: the six moves', len(moves) == 6, 'the table rows :%s' % ', :'.join(str(x) for x in moves), '3')
    ins = lines_of(os.path.join(PP, K.PAPERS['INSTRUMENTS']))
    i6 = _heading(ins, r'I-6\b')
    add('ruling (5)(ii)', 'INSTRUMENTS I-6: the six perspective axes (b705`s reading :131-:138, data/b705_i6_ranking.txt :3)', i6 > 0 and 'the six axes :131-:138' in (rd(p('data', 'b705_i6_ranking.txt')) or ''),
        'INSTRUMENTS.md I-6 heading :%d ; data/b705_i6_ranking.txt :3' % i6, '3')
    # ### (R320)(1), by row
    cl = lines_of(p('data', 'b709_closing.txt'))
    add('ruling (1)', 'data/b709_closing.txt :1, the head line, against (R320)(1)`s quote after whitespace is removed', _ws(cl[0]) == _ws(HEAD_QUOTE),
        'data/b709_closing.txt :1 = %r' % cl[0][:130], '0-1')
    cf = first(cl, '### CARRIED FORWARD.')
    add('ferry read-first', 'data/b709_closing.txt, the carried-forward rows (a)-(h) by line', cf > 0 and first(cl, '    (a) ', cf) > 0 and first(cl, '    (h) ', cf) > 0,
        'data/b709_closing.txt :%d (the head), (a) :%d, (h) :%d' % (cf, first(cl, '    (a) ', cf), first(cl, '    (h) ', cf)), '0-1')
    po = lines_of(p('data', 'b709_closing_push_out.txt'))
    add('ruling (1); ruling (7)', 'the closing commit relay 42dd8768 pushed in main mode and read back (data/b709_closing_push_out.txt, to be committed)',
        'push-b709-closing' in at(po, 2) and '42dd87685308f3e71bceba9ee8185229f192e7b5' in at(po, 5), 'data/b709_closing_push_out.txt :2, :5', '0-1')
    st = g(ROOT, 'status', '--porcelain', '--', 'data/b709_closing_push_out.txt')[1] or ''
    add('ruling (7); ferry C0', 'data/b709_closing_push_out.txt uncommitted at the act`s start', st.startswith('??'), 'git status %r' % st.strip(), '0')
    rp = rd(p('data', 'b709_report.txt')) or ''
    gr = rd(p('data', 'b709_grid.txt')) or ''
    add('ruling (1)', 'the band zero`s onset at the rung log 32381, a = 10.3853, lambda_min -3.53e-5, Lambda_Q vanishing there, between the entering rungs log 32213 and log 32423',
        all(x in rp for x in ('rung log 32381', 'a = 10.38532711', 'lambda_min -3.5300862e-5', 'Lambda_Q(32381) = 0', 'log 32213', 'log 32423')), 'data/b709_report.txt :16', '1')
    add('ruling (1)', 'rho_0`s onset at the midpoint between log 929 and log 937, a = 6.8384, lambda_min -0.00372',
        all(x in rp for x in ('midpoint between log 929 and log 937', 'a = 6.838396011', 'lambda_min -0.0037191321')), 'data/b709_report.txt :16', '1')
    add('ruling (1)', 'the zeta form positive at all 4443 points with its tail balls beside lambda_min (392 + 4051)',
        '4051 of 4051 and 392 of 392' in rp and 392 + 4051 == 4443, 'data/b709_report.txt :17', '1')
    gl = gr.split(NL)
    c1 = [l for l in gl[10:44] if l.startswith('  rho0 a') or l.startswith('  band a')]
    add('ruling (1)', 'the coarse endpoints reproducing b707`s 32 rows exactly', len(c1) == 32 and all(l.rstrip().endswith('AS WANTED') for l in c1) and 'C1 AS WANTED True' in gr,
        'data/b709_grid.txt :12-:43, rows %d, every one AS WANTED; :44' % len(c1), '1')
    add('ruling (1)', 'the registered hypothesis and falsifier printed vacuous as worded per family', 'each vacuous as worded' in rp, 'data/b709_report.txt :16', '1')
    pl = lines_of(p('data', 'b709_pairs.txt'))
    bands = [l for l in pl if l.startswith('  band [')]
    add('ruling (1)', 'the certified list of Q0`s zeros extended from 150 to 325 in 17 closed bands (231 new on-line zeros, 29 new off-line pairs)',
        len(bands) == 17 and all(l.rstrip().endswith('COMPLETE') for l in bands) and 'new on-line zeros 231 ; new off-line pairs 29' in at(pl, 36),
        'data/b709_pairs.txt :19-:35 (17 bands COMPLETE), :36', '1')
    rows12 = [l for l in pl if re.match(r'^\s+\d+ \| \[', l)]
    rat = []
    for l in rows12:
        m = re.search(r'n\*/predicted \[([0-9.]+)', l)
        h = re.search(r'\+ \[([0-9.]+) i', l)
        if m and h:
            rat.append((int(l.split('|')[0]), float(h.group(1)), float(m.group(1))))
    inside = [x for x in rat if 0.67 <= x[2] <= 1.5]
    add('ruling (1)', 'ten of twelve pairs within [0.67, 1.5] with ratios 1.23 to 1.34; pairs 11 and 15 beyond reach at 325 (needing 405.4 and 442.3)',
        len(rows12) == 12 and len(inside) == 10 and round(min(x[2] for x in rat), 2) == 1.23 and round(max(x[2] for x in rat), 2) == 1.34
        and 'T0` needed > 405.4' in at(pl, 52) and 'T0` needed > 442.3' in at(pl, 56),
        'data/b709_pairs.txt :46-:57 -- computed %d, within %d, least %.4f, greatest %.4f ; :52, :56' % (len(rat), len(inside), min(x[2] for x in rat), max(x[2] for x in rat)), '1')
    srt = sorted(rat, key=lambda x: x[1])
    inv = [(b[0], a[0]) for a, b in zip(srt, srt[1:]) if b[2] < a[2]]
    add('ruling (1); ruling (2)(ii)', 'the ratios "rising with height" -- read step by step in the order of height',
        not inv, 'data/b709_pairs.txt :46-:57 in order of height: %s ; the pairs whose ratio is BELOW the next-lower pair`s: %s -- the rise a trend over the ten, not a rise at every step '
        '(b709`s own words, FINDINGS :10200 "rising with height", carried into the ruling); entered by the fact clause in the weight line beside the quotation, the trend and the four steps printed'
        % (', '.join('%d %.4f' % (x[0], x[2]) for x in srt), ', '.join('pair %d below pair %d' % x for x in inv) or 'NONE'), '1')
    add('ruling (1)', 'W-ORD-Q0-ZEROS-443 at OPEN_TRAILS :15764', 'W-ORD-Q0-ZEROS-443' in at(ot, 15764), 'OPEN_TRAILS :15764 %r' % at(ot, 15764)[:80], '1')
    pt = rd(p('data', 'b709_port.txt')) or ''
    pe = rd(p('data', 'b709_port_edit.txt')) or ''
    add('ruling (1)', 'the port at port-b707 = 92af8a34, one edit at C7OrderBounds.lean :277, one dispatch, 11 of 12 modules, DirichletC7Order.lean :212:55 next, nothing merged or tagged',
        '92af8a344f1161e5f91df448f270bd3dea304429' in pt and 'MODULES BUILT 11 OF 12' in pt and 'DirichletC7Order.lean:212:55' in pt and 'HUNKS 1' in pe,
        'data/b709_port.txt :4, :19, :21, :53 ; data/b709_port_edit.txt HUNKS 1', '1')
    add('ruling (1)', 'the axis (e) representation coordinates registered for b711', '(e) REPRESENTATION COORDINATES' in (rd(p('data', 'b709_registrations.txt')) or ''),
        'data/b709_registrations.txt :10, :60', '1')
    lgd = g(ROOT, 'diff', 'HEAD', '--', 'data/b378_lockgate.json')[1] or ''
    add('ruling (1)', 'b378`s lock-gate bank overwritten by a call without its argument and restored byte-equal, shown so before the root',
        'EQUAL True -- the bank stands at its committed bytes' in rp and not lgd.strip(), 'data/b709_report.txt :4-:7 ; `git diff HEAD -- data/b378_lockgate.json` now %d bytes' % len(lgd), '1')
    add('ruling (1)', 'the entry at FINDINGS :10198, the trail at OPEN_TRAILS :15766', at(fi, 10198).startswith('## The sign-onset radius') and at(ot, 15766).startswith('### b709'),
        'FINDINGS :10198 %r ; OPEN_TRAILS :15766 %r' % (at(fi, 10198)[:50], at(ot, 15766)[:50]), '1')
    ar = _jl('b709_act_root.json')
    rb = lines_of(p('data', 'b709_root_banks.txt'))
    row = act_root_line('b709')
    add('ruling (1)', 'the root b3213c0b over 96 banks chained from a840da57', bool(row) and row[0][1].startswith('b3213c0b') and 'BANKS 96' in ' '.join(rb) and 'a840da57' in json.dumps(ar),
        'data/act_roots.txt row b709 %s ; data/b709_root_banks.txt BANKS 96 ; data/b709_act_root.json prev a840da57' % (row[0][1][:16] if row else 'NONE'), '1')
    cpp = rd(p('data', 'b709_checks_postpush.txt')) or ''
    add('ruling (1)', 'the chain b624-b709 AGREE (G-ACTROOT-VERIFY passing post-push); suite 144 of 147',
        'G-ACTROOT-VERIFY' not in (re.search(r'LIVE FAILING : 3 (\[.*?\])', cpp) or re.search('', '')).group(0) and 'LIVE PASSING : 144' in cpp and 'ARMS RUN : 147' in cpp,
        'data/b709_checks_postpush.txt %r' % ((re.search(r'LIVE FAILING : 3 (\[.*?\])', cpp) or re.search('', '')).group(0)), '1')
    mr = rd(p('data', 'b709_mirror.txt')) or ''
    add('ruling (1)', 'the mirror CLEAN over 70 files', 'CLEAN' in mr and '70' in mr and os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-23-b709.zip'),
        'data/b709_mirror.txt ; the zip exists %s' % os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-23-b709.zip'), '1')
    sc, scc = _jl('b709_scores.json'), _jl('b709_scores_close.json')
    sv = lambda J, k: (J.get(k) or {}).get('verdict') if isinstance(J.get(k), dict) else J.get(k)   # noqa: E731
    flat = json.dumps(sc) + json.dumps(scc)
    add('ruling (1)', 'N1 and N3 REFUTED as worded, N2 and N4 HELD, N5 REFUTED at the record and HELD at the close, S1-S3 HELD (data/b709_scores.json, data/b709_scores_close.json)',
        'REFUTED' in flat and 'HELD' in flat, 'data/b709_scores.json keys %s ; data/b709_scores_close.json keys %s ; the closing :81 %r' % (
            sorted(sc)[:8], sorted(scc)[:8], at(cl, 81).strip()[:110]), '1')
    dl = lines_of(p('data', 'b709_defects.txt'))
    lets = [m.group(1) for l in dl for m in [re.match(r'^    \(([a-z])\) (THE [A-Z]+)', l)] if m]
    owners = [re.match(r'^    \([a-z]\) (THE [A-Z`\']+)', l).group(1) for l in dl if re.match(r'^    \([a-z]\) THE ', l)]
    add('ruling (1)', 'eight defects (a)-(h), all the seat`s', ''.join(lets) == 'abcdefgh' and all(o.startswith("THE SEAT") for o in owners),
        'data/b709_defects.txt letters %s ; owners %s' % (''.join(lets), sorted(set(owners))), '1')
    add('ruling (1); ruling (9)', '"nothing deposited": the draft at v5, held', K.DRAFT == '23228113', 'tools/b710_worklist.py DRAFT', '6')
    # ### (R320)(2): the navigator's readings, entered beside the entry in its words for the strike
    add('ruling (2)(i)', 'the rung hypothesis vacuous at the onset scale: the grid`s rungs per family (data/b708_registrations.txt :24, :26: rho_0 197 rungs to n = 1024, the band 2026 rungs to n = 36864)',
        'rungs 197' in gr, 'data/b709_grid.txt :46 ; a reading in the navigator`s words, entered beside the entry for the strike', '1')
    add('ruling (2)(ii)', 'the refined law`s form: n* solves r n* = log(M(n*)/A); b675`s onset (tools/b675_li_bench.py :153-:160, :188-:189: the least n with 2 - (1/4) R^n + C (n + 1)^2 s^n below 0)',
        'Cc * (n + 1) ** 2 * (ls * n).exp()' in (rd(p('tools', 'b675_li_bench.py')) or ''), 'tools/b675_li_bench.py :157 ; a reading in the navigator`s words', '1, 0 (6)(i)')
    add('ruling (2)(iii)', 'the zeta control positive at 4443 points beyond its certified tails, entered as the strongest control reading in the Q0 series', '4051 of 4051 and 392 of 392' in rp,
        'data/b709_report.txt :17 ; a reading in the navigator`s words, entered as such', '1')
    # ### (R320)(3): the needles, the test, the lock gate, the corrigendum
    ck = lines_of(p('tools', 'b709_checks.py'))
    ru, ax = first(ck, 'def report_unsealed_ok'), first(ck, 'def axis_registered_ok')
    add('ruling (3)', 'G-REPORT-UNSEALED`s source (tools/b709_checks.py report_unsealed_ok) and its key RATIO', ru > 0 and any('RATIO' in at(ck, n) for n in range(ru, ru + 25)),
        'tools/b709_checks.py :%d (def report_unsealed_ok)' % ru, '1')
    add('ruling (3)', 'G-AXIS-REGISTERED`s source (tools/b709_checks.py axis_registered_ok), its needle the ranking`s row as one string', ax > 0,
        'tools/b709_checks.py :%d (def axis_registered_ok) ; data/b709_registrations.txt :12-:13 the quotation wrapped' % ax, '1')
    s_c, t_c = _defect_row(dl, 'c')
    add('ruling (3)', 'the test that ran lean on this host, named by file and line from data/b709_defects.txt: tools/test_elab_reader_b634.py, its calls at :34 and :65',
        'tools/test_elab_reader_b634.py' in t_c and ':34 and :65' in t_c and 'EL.call(' in at(lines_of(p('tools', 'test_elab_reader_b634.py')), 34)
        and 'EL.call(' in at(lines_of(p('tools', 'test_elab_reader_b634.py')), 65), 'data/b709_defects.txt (c) :%d-:44 ; tools/test_elab_reader_b634.py :34, :65' % s_c, '0-1')
    lg = lines_of(p('tools', 'b378_lockgate.py'))
    add('ruling (3)', 'the lock gate`s argument: tools/b378_lockgate.py main reads its act with b378 as the default', "act = argv[0] if argv else 'b378'" in at(lg, 148),
        'tools/b378_lockgate.py :148 %r ; its writes :187-:190, :217-:224' % at(lg, 148).strip(), '1')
    add('ruling (3)', 'b709`s two post-seal needles, the corrigendum`s items (data/b709_defects.txt, the unlettered event)', first(dl, 'TWO ARMS FAILING AFTER THE SEAL') > 0,
        'data/b709_defects.txt :%d-:129' % first(dl, 'TWO ARMS FAILING AFTER THE SEAL'), '1')
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    last = [l for l in cg if re.match(r'^\s*\((\d+)\)', l)]
    add('ruling (3)', 'the corrigenda bank, appended only (its last row (29), b709`s)', bool(last) and re.match(r'^\s*\(29\)', last[-1]) is not None,
        'data/b675_corrigenda.txt, last row %r' % (last[-1][:40] if last else ''), '1')
    add('ruling (3)', 'the corrigendum tool to carry (b678`s form, tools/b709_corrigendum.py)', os.path.exists(p('tools', 'b709_corrigendum.py')) and os.path.exists(p('tools', 'b678_corrigendum.py')),
        'tools/b709_corrigendum.py ; tools/b678_corrigendum.py', '1')
    # ### (R320)(4): the standing clauses
    add('ruling (4)', 'W-ORD-STANDING-CLAUSES-BANK at OPEN_TRAILS :15450, trigger b710', 'W-ORD-STANDING-CLAUSES-BANK' in at(ot, 15450) and 'b710' in at(ot, 15450),
        'OPEN_TRAILS :15450 ; its readers: tools/ferry_scan.py, G-RECEIPT-IN-FULL, the citation tool', '2')
    fb = lines_of(p('data', 'b709_ferry.txt'))
    add('ruling (4)', '(R319)`s ferry as banked at b709: the standing procedural paragraph and Components 5 and 6',
        at(fb, 49).startswith('Foreground runs under the 600 s limit') and at(fb, 43).startswith('COMPONENT 5 - THE SEAL AND THE SUITE') and at(fb, 45).startswith('COMPONENT 6 - THE RECORD AND THE MIRROR'),
        'data/b709_ferry.txt :43 (Component 5), :45 (Component 6), :49 (the procedural paragraph) of %d lines' % len(fb), '2')
    fs = lines_of(p('tools', 'ferry_scan.py'))
    add('ruling (4)', 'the ferry scan`s standing-clauses citation (tools/ferry_scan.py :697-:703, OPEN_TRAILS :15450`s price)', len(fs) >= 703,
        'tools/ferry_scan.py %d lines ; :697 %r' % (len(fs), at(fs, 697).strip()[:70]), '2')
    add('ruling (4)', 'G-RECEIPT-IN-FULL over the banked ferry (tools/b709_checks.py)', first(ck, 'G-RECEIPT-IN-FULL') > 0, 'tools/b709_checks.py :%d' % first(ck, 'G-RECEIPT-IN-FULL'), '2')
    add('ruling (4)', 'data/standing_clauses_v1.txt -- TO BE WRITTEN at Component 2', not os.path.exists(p('data', 'standing_clauses_v1.txt')), 'absent, as ordered', '2')
    # ### (R320)(5): reading 5's objects, located in the corpus by name
    for term in ('conservation strength', 'formation measure', 'formation distance', 'Universal Darkness', 'Ostrowski', 'dichotomy', 'licen'):
        fl = _pp_files(term)
        add('ruling (5)(i)', 'the measure %r named in the corpus' % term, len(fl) > 0, 'PLACE-papers files naming it %d, the first %s' % (len(fl), fl[:3]), '3')
    for princ in ('Symmetry', 'Independence', 'Determination', 'Exhaustiveness'):
        fl = _pp_files(princ)
        add('ruling (5)(i)', 'the principle %r named in the corpus' % princ, len(fl) > 0, 'PLACE-papers files naming it %d' % len(fl), '3')
    add('ruling (5)(i)', 'Q0 the control for the Euler product (data/b703_q0_band.txt; data/b705_i6_ranking.txt)', os.path.exists(p('data', 'b703_q0_band.txt')), 'data/b703_q0_band.txt', '3')
    add('ruling (5)(iii)', 'readings 3 and 4 (data/b690_reading3.txt, data/b700_reading4.txt) and the defects banks since b700', os.path.exists(p('data', 'b690_reading3.txt')) and os.path.exists(p('data', 'b700_reading4.txt'))
        and all(os.path.exists(p('data', 'b%d_defects.txt' % a)) for a in range(700, 710)), 'data/b700_defects.txt .. data/b709_defects.txt', '3')
    add('ruling (5)(iii)', 'the closure reader`s banks per act (data/b7NN_readfirst_closure.txt, _diff.txt, b700-b709)', all(os.path.exists(p('data', 'b%d_readfirst_diff.txt' % a)) for a in range(700, 710)),
        'data/b700_readfirst_diff.txt .. data/b709_readfirst_diff.txt', '3')
    add('ruling (5)(iv)', 'the read banks of b705-b709', all(os.path.exists(p(*f.split('/'))) for f in K.READ_BANKS), ' ; '.join(K.READ_BANKS), '3')
    add('ruling (5)', 'data/b710_reading5.txt -- TO BE WRITTEN at Component 3', not os.path.exists(p('data', 'b710_reading5.txt')), 'absent, as ordered', '3')
    # ### (R320)(6): the registrations
    lb = rd(p('tools', 'b675_li_bench.py')) or ''
    add('ruling (6)(i)', '"M the main term of the configuration`s Li coefficient and A the off-line pair`s amplitude, both as b709`s route computes them" -- the route`s terms by line',
        False, 'the route (tools/b675_li_bench.py :153-:160 onset, :188-:189 C and the call onset(arb(2), R, arb(1) / 4, Cc, s); tools/b709_pairs.py constants_for709 line for line): n* is the least n '
        'with 2 - (1/4) R^n + C (n + 1)^2 s^n < 0 -- the competitor of the pair`s term is the REMAINDER BOUND C (n + 1)^2 s^n (C from the rest set`s K), not a main term of the Li coefficient; the '
        'pair`s coefficient is the constant 1/4 for every pair, not a pair-dependent amplitude; and the rate is log(R/s), s = (1 + 3R)/4, about r/4 for R near 1, not r. The ruling`s form is the route`s '
        'equation read to first order in R - 1: r n* = 4 log(4C) + 8 log(n* + 1). ENTERED BY THE FACT CLAUSE IN THE REGISTRATION: the route`s own equation registered by line, the ruling`s form its '
        'first-order reading, the fitted constants the offset and the coefficient of log n* over the ten computed pairs (%s)' % ('onset(arb(2), R, arb(1) / 4, Cc, s)' in lb), '0 (6)(i)')
    add('ruling (6)(i)', 'the ten computed pairs` r(rho) and n* banked (data/b709_pairs.txt :46-:57), pairs 11 and 15`s r(rho) beside', len(rat) == 10 and 'r(rho) [1.216894664e-5' in at(pl, 52) and 'r(rho) [1.022443029e-5' in at(pl, 56),
        'data/b709_pairs.txt :46-:57', '0 (6)(i)')
    add('ruling (6)(i)', 'the list below pairs 11 and 15`s heights ("before the list reaches their heights": 325 < 405.4, 442.3)', 'THE LIST COMPLETE TO T0` = 325' in at(pl, 36), 'data/b709_pairs.txt :36', '0 (6)(i)')
    add('ruling (6)(ii)', 'b709`s onset eigenvalues for the unoperated control (data/b709_report.txt :16)', 'lambda_min -3.5300862e-5' in rp and 'lambda_min -0.0037191321' in rp, 'data/b709_report.txt :16', '0 (6)(ii)')
    add('ruling (6)(iii)', 'e^{10.39} against the band`s onset a = 10.3853 (the coefficients through n = e^{10.39}, about 32532, reach past 32381)', 2.718281828459045 ** 10.39 > 32381,
        'e^10.39 = %.1f' % (2.718281828459045 ** 10.39), '0 (6)(iii)')
    add('ruling (6)', 'data/b710_registrations.txt -- TO BE WRITTEN at step zero, committed alone before any number', not os.path.exists(p('data', 'b710_registrations.txt')), 'absent, as ordered', '0')
    # ### (R320)(7): the branches
    merged = g(ROOT, 'branch', '--merged', 'main')[1] or ''
    mpp = g(PP, 'branch', '--merged', 'main')[1] or ''
    for repo, names, lst in (('relay', ('push-b709', 'push-b709-root', 'push-b709-root2', 'push-b709-closing'), merged), ('PLACE-papers', ('push-b709', 'push-b709-root'), mpp)):
        for b in names:
            add('ruling (7)', '%s %s (local, listed --merged)' % (repo, b), b in [x.strip(' *') for x in lst.split(NL)], 'listed by `git branch --merged main` at %s before any delete' % repo, '0')
    lh = _remote_heads(K.LV_DIR)
    loc = (g(K.LV_DIR, 'rev-parse', 'port-b707')[1] or '').strip()
    add('ruling (7)', 'port-b707 at b709`s one commit 92af8a34 locally and at the remote, NOT deleted (one ls-remote of SIDE-lv-conservation)', loc == K.PORT_TIP and lh.get('refs/heads/port-b707') == K.PORT_TIP,
        'local %s ; remote %s' % (loc[:8], (lh.get('refs/heads/port-b707') or '')[:8]), '0')
    add('ruling (7)', 'the 2,560 MB hold', K.HOLD == 2560, 'tools/b710_worklist.py HOLD', '0')
    # ### (R320)(8)-(10)
    add('ruling (8)', 'the READFIRST-CLOSURE reader', os.path.exists(p('tools', 'circuit_read.py')), 'tools/circuit_read.py (readfirst)', '0')
    add('ruling (8)', 'data/b710_rules.txt and data/b711_rules.txt by form (the (W) list admits them)', not os.path.exists(p('data', 'b711_rules.txt')), 'b711`s absent; admitted by form', '5')
    add('ruling (8)', 'tools/mirror_prevbuild.json, the mirror builder`s state file, named in (W)', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'tools/mirror_prevbuild.json', '5')
    add('ruling (10)', 'the port`s next line DirichletC7Order.lean :212:55 (data/b709_port.txt :21)', 'DirichletC7Order.lean:212:55' in at(lines_of(p('data', 'b709_port.txt')), 21), 'data/b709_port.txt :21', '6')
    add('ruling (10)', 'W-ORD-LV-FORWARD-PORT at OPEN_TRAILS :15686 and W-ORD-LV-CLOSURE-JOIN at :15452', 'W-ORD-LV-FORWARD-PORT' in at(ot, 15686) and 'W-ORD-LV-CLOSURE-JOIN' in at(ot, 15452),
        'OPEN_TRAILS :15686, :15452', '6')
    # ### the ferry's standing references
    add('ferry', '(R278)(4)', os.path.exists(p('data', 'b668_ferry.txt')), 'data/b668_ferry.txt', '6')
    add('ferry', '(R251)(3)', os.path.exists(p('data', 'b641_ferry.txt')), 'data/b641_ferry.txt', '6')
    add('ferry', '(R254)(2)', os.path.exists(p('data', 'b644_ferry.txt')), 'data/b644_ferry.txt', '5')
    add('ferry C5', 'data/b675_rules.txt row 1', '(1)' in (rd(p('data', 'b675_rules.txt')) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry C5', 'the score order b686 fixed', os.path.exists(p('data', 'b686_rules.txt')), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C5', 'the chain halves as b693 drew them, b710 added to the second', K.CHAIN_HALVES[1] == ('b659', 'b710'), 'tools/b710_worklist.py CHAIN_HALVES', '5')
    add('ferry C5', 'the four standing arms` figures tool and b709`s baselines', os.path.exists(p('tools', 'b706_standing_figures.py')) and os.path.exists(p('data', 'b709_standing_figures.json')),
        'tools/b706_standing_figures.py ; data/b709_standing_figures.json', '5')
    add('ferry C0', 'data/b684_rules.txt row (1), a test file over 450 s its own part', os.path.exists(p('data', 'b684_rules.txt')), 'data/b684_rules.txt :5', '0')
    add('ferry C5', 'data/b706_rules.txt row (1): ROOT_EXCLUDE, the root route dry READY before the seal', 'a face whose dry READY reads False is not locked' in (rd(p('data', 'b706_rules.txt')) or ''), 'data/b706_rules.txt :6-:15', '5')
    add('ferry C5', 'data/b709_rules.txt row (1), the carry read by diff', 'THE CARRY IS READ BY DIFF' in (rd(p('data', 'b709_rules.txt')) or ''), 'data/b709_rules.txt :6', '5')
    add('ferry C6', 'b673`s capture names', os.path.exists(p('data', 'b709_relay_push_out.txt')), 'data/b709_relay_push_out.txt (the form carried)', '6')
    add('ferry C6', 'the b670 form of the mirror', os.path.exists(p('data', 'b709_mirror.txt')), 'data/b709_mirror.txt (the form carried)', '6')
    add('ferry C6', 'the unsealed report tool`s form (tools/b709_report.py, written after the root`s word; data/b709_report.txt)', os.path.exists(p('tools', 'b709_report.py')) and not os.path.exists(p('tools', 'b710_report.py')),
        'tools/b709_report.py ; tools/b710_report.py TO BE WRITTEN after the root`s word', '6')
    add('ferry C0', 'this act`s session transcript (a new session) and b709`s', os.path.exists(C.SESSION) and os.path.exists('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.PREV_SESSION), C.SESSION, '0')
    return R


def _write(L, R, miss):
    for name, data in (('b710_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b710_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b710 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b710_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b710_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b710_ferry_scan.txt')
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b710_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


# ### b706's repair of the answer checker (b705 defect (n)), carried: a token that a bank's row names as a sha256 -- the root list, a hashes
# ### bank's row, a bank line carrying "sha256" -- or that a kernel's lakefile or manifest pins as a rev, is not a commit.
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
    """(R278)(4): b682's route, imported, with its act names pointed at b710, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b710'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b710')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b710)', 'exec'), ns)
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
        print('usage: b710_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
