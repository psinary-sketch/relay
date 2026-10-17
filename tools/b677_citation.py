# -*- coding: utf-8 -*-
"""b677_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b677's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it. Carried from
tools/b676_citation.py by the Write tool: the helpers unchanged (both apostrophes, SESSIONS_AFTER, the after-root redirect of (R282)(2)
row 1: once data/act_roots.txt carries b677's root, an answer's print goes to data/b677_defects.txt and to no root-named bank; each answer
cut from BEGIN to END around its needle); the constants and the rows b677's.

### Before the ferry is banked, every path, line, bank, branch, tag, declaration and named rule the ruling (R287) and the ferry cite is
### checked for existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not
### repaired silently; the print is banked as data/b677_citation_check.txt and read by the suite. A bank the ruling orders written is
### printed TO BE WRITTEN, not a cite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R287) BEGIN'), never from a scratch copy.
### Routes: `python tools/b677_citation.py check` -> data/b677_citation_check.txt (.json);
###         `python tools/b677_citation.py ferry`  -> data/b677_ferry.txt and data/b677_ferry_scan.txt (ferry_scan.py's output, captured);
###         `python tools/b677_citation.py answer <needle>` -> the latest session answer carrying <needle>, its cites checked, the print APPENDED
###         to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b677; this tool writes only the banks named above.
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
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KE = 'D:/SIDE-explicit-formula'
TD = 'D:/SIDE-trivium'
KREV = 'e36ea31'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/df03c73f-520a-4848-85dc-8fada095f008.jsonl'
SESSIONS_AFTER = ()
ANCHOR, TAIL = 'RULING (R287) BEGIN', 'FERRY END (part 1 of 1)'
REPOS = (ROOT, PP, KE, TD, 'D:/SIDE-window')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout.replace(chr(13), '')


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else None


def line(p, n):
    t = rd(p)
    ls = t.split(NL) if t is not None else []
    return ls[n - 1] if 0 < n <= len(ls) else None


def _user_texts(results=True):
    """the session's user texts; with results, the results of the seat's own prompts alone (b670 defect (e))."""
    ask = set()
    for raw in (r for s in (SESSION,) + SESSIONS_AFTER for r in io.open(s, encoding='utf-8', errors='replace')):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if o.get('isCompactSummary'):
            continue
        cs = (o.get('message') or {}).get('content')
        for c in (cs if isinstance(cs, list) else []):
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                ask.add(c.get('id'))
        if o.get('type') == 'user':
            for t in ([cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']):
                yield t
            for c in (cs if isinstance(cs, list) else []) if results else []:
                if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask:
                    t = c.get('content')
                    yield ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')


def ferry_text():
    """the ruling and the ferry as pasted: the last user line of the session carrying the anchor, from the anchor to the ferry's end."""
    best = None
    for t in _user_texts(results=False):
        i, j = t.find(ANCHOR), t.find(TAIL)
        if i >= 0 and j > i:
            best = t[i:j + len(TAIL)].replace(chr(13), '')
    if best is None:
        sys.exit('### THE RULING IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    return best


def commit_in(repo, sha):
    rc, _o = g(repo, 'cat-file', '-e', sha + '^{commit}')
    return rc == 0


def subject(repo, sha):
    return g(repo, 'log', '-1', '--format=%s', sha)[1].strip()


def branch_listed(repo, b):
    rc, o = g(repo, 'branch', '--list', b)
    return bool(o.strip())


def rule_clause(rule, clauses):
    for f in sorted(os.listdir(D)):
        if f.endswith('_ferry.txt'):
            t = rd(os.path.join(D, f))
            if t and ('RULING (%s) BEGIN' % rule) in t:
                body = t[t.index('RULING (%s) BEGIN' % rule):]
                return all(('(%d)' % c) in body for c in clauses), 'data/%s' % f
    return False, 'no ferry bank carries RULING (%s)' % rule


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    ls = [l.split() for l in t.split(NL) if l.strip()]
    return [l for l in ls if l[0] == act]


def grep_lines(path, pat, flags=0):
    t = rd(path) or ''
    return [(i, l.strip()) for i, l in enumerate(t.split(NL), 1) if re.search(pat, l, flags)]


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    # ### the ferry's read-first list
    for f in ('data/b676_closing.txt', 'data/b676_defects.txt', 'data/b676_q0_lines.txt', 'data/b676_strip_uses.txt', 'data/b670_work_orders.txt',
              'data/b667_epstein_plan.txt', 'data/b667_h4_reading.txt', 'tools/b667_epstein_map_balls.py', 'data/b671_tie_diagnostic.txt',
              'data/b675_li_plan.txt', 'data/b675_li_bench.txt', 'data/b675_li_controls.txt', 'data/b675_rules.txt',
              'data/b676_closing_push_out.txt'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-4')
    add('ferry read-first', 'data/b671_epstein_zeros_narrowed.json (rows are points with balls)', os.path.exists(p('data', 'b671_epstein_zeros_narrowed.json')),
        'absent under that name; the bank stands gzipped under its own name as data/b671_epstein_zeros_narrowed.json.gz (%s), its hashes in '
        'data/b671_epstein_zeros_narrowed_hashes.txt (%s), as OPEN_TRAILS :14396 cites it -- RAISED' % (
            os.path.exists(p('data', 'b671_epstein_zeros_narrowed.json.gz')), os.path.exists(p('data', 'b671_epstein_zeros_narrowed_hashes.txt'))), '0-3')
    # ### (R287)(1): b676 at its weight
    cl = rd(p('data', 'b676_closing.txt')) or ''
    head = cl.split(NL)[0]
    quoted = ('b676 closed: relay afb4bd59, PLACE-papers 9abb234, SIDE-trivium 135be2e v0.1.1; suite 84 of 84; root d3271717321e8d5e\u2026; '
              '2 prompts answered; 9 defects')
    add('ruling (1)', 'the head line quoted at data/b676_closing.txt :1', head == quoted, 'character for character: %s' % (head == quoted), '1')
    for repo, nm, sha, needle in ((ROOT, 'relay', 'afb4bd59', 'b676 record'), (ROOT, 'relay', 'e41e165f', 'b676 closing'),
                                  (PP, 'PLACE-papers', '9abb234', 'b676 record')):
        s = subject(repo, sha)
        add('ruling (1)', '%s %s, its subject opening "%s"' % (nm, sha, needle), commit_in(repo, sha) and s.startswith(needle), s[:80], '1')
    po = line(p('data', 'b676_closing_push_out.txt'), 4) or ''
    add('ruling (1)', 'the closing pushed at relay e41e165f', 'afb4bd59..e41e165f' in po, 'data/b676_closing_push_out.txt :4', '1')
    for sha, what in (('dd587f9', 'the workflow on main'), ('7074154', 'the 22-name print list on main'), ('db315fe', 'the cut'),
                      ('135be2e', 'the merge')):
        add('ruling (1)', 'SIDE-trivium %s, %s' % (sha, what), commit_in(TD, sha), subject(TD, sha)[:80], '1')
    add('ruling (1)', 'SIDE-trivium tag v0.1.1 at 135be2e', g(TD, 'rev-parse', 'v0.1.1^{commit}')[1].startswith('135be2e'), 'rev-parse', '1')
    nine = grep_lines(p('data', 'b676_closing.txt'), r'9 commits past v0\.1')
    add('ruling (1)', 'the before print bank at main, 9 commits past v0.1', nine, 'data/b676_closing.txt :%s' % (nine[0][0] if nine else None), '1')
    m17 = grep_lines(p('data', 'b676_cut.txt'), r"marker at :17")
    add('ruling (1)', 'the residue beside SIDE-window`s marker at :17', m17, 'data/b676_cut.txt :%s' % (m17[0][0] if m17 else None), '1')
    q0 = grep_lines(p('data', 'b676_q0_lines.txt'), r'HITS 136 ; CONSISTENT 100 ; TO RE-CUT 36 \(ON 35 LINES: FINDINGS 25, OPEN_TRAILS 11')
    add('ruling (1)', 'the Q0 lines: 136 hits, 100 CONSISTENT, 36 on 35 lines (25, 11)', q0, 'data/b676_q0_lines.txt :%s' % (q0[0][0] if q0 else None), '1')
    ql = line(OT, 14556) or ''
    add('ruling (1)', 'W-ORD-Q0-CLASS-LINES at OPEN_TRAILS :14556', 'W-ORD-Q0-CLASS-LINES' in ql, ql[:80], '1')
    wo = grep_lines(p('data', 'b670_work_orders.txt'), r'^  W-ORD-Q0-CLASS-LINES .* OPEN ')
    add('ruling (1)', 'W-ORD-Q0-CLASS-LINES OPEN in the orders bank', wo, 'data/b670_work_orders.txt :%s' % (wo[0][0] if wo else None), '1')
    su = grep_lines(p('data', 'b676_strip_uses.txt'), r'USES 22 \(V5 12, THE COMPOSITION 10\).*LiConverseCfg\.lean :231')
    add('ruling (1)', 'the strip`s uses 22; LiConverseCfg.lean :231', su, 'data/b676_strip_uses.txt :%s' % (su[0][0] if su else None), '1')
    l231 = g(KE, 'show', '%s:SIDEExplicitFormula/Schema/LiConverseCfg.lean' % KREV)[1].split(NL)
    add('ruling (1)', 'LiConverseCfg.lean :231 at %s' % KREV, len(l231) >= 231 and 'div_pos hst.1' in l231[230], (l231[230].strip() if len(l231) >= 231 else '')[:80], '1')
    c6 = grep_lines(p('data', 'b676_checks.txt'), r'the standing arms .* 68 ; carried here 68')
    add('ruling (1)', '68 standing arms at b676', c6, 'data/b676_checks.txt :%s' % (c6[0][0] if c6 else None), '1')
    for f, n, needle in (('FINDINGS.md', 8913, '## SIDE-trivium docstrings re-cut'), ('OPEN_TRAILS.md', 14560, '### b676')):
        l = line(os.path.join(PP, f), n) or ''
        add('ruling (1)', '%s :%d' % (f, n), needle in l, l[:90], '1')
    ar = act_root_line('b676')
    rj = json.loads(rd(p('data', 'b676_act_root.json')) or '{}')
    nb = len((rj.get('reads') or {}).get('banks') or [])
    add('ruling (1)', 'the root d3271717 over 48 banks', ar and ar[0][1].startswith('d3271717') and nb == 48, 'data/act_roots.txt (b676 row); '
        'data/b676_act_root.json banks %d' % nb, '1')
    dl = rd(p('data', 'b676_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M)
    add('ruling (1)', 'nine defects (a)-(i)', [x for x, _o in letters] == list('abcdefghi'), 'data/b676_defects.txt: %s' % ''.join(x for x, _o in letters), '1')
    add('ruling (1)', 'defects (f) and (i) of b676 (the redirect writes)', re.search(r'^    \(f\) .*REDIRECT', dl, re.M) and re.search(r'^    \(i\) ', dl, re.M),
        'data/b676_defects.txt (f) :26, (i) :40', '0')
    for fn, case in (('test_chain_page.py', '(9)'), ('test_chain_page_b638.py', '(4)')):
        add('ruling (1)', 'the failing test %s %s' % (fn, case), os.path.exists(p('tools', fn)), 'tools/%s; failing at b676 (data/b676_tests_stepzero.txt :61)' % fn, '0')
    o9 = line(OT, 13838) or ''
    add('ruling (1)', 'an order carrying test_chain_page.py (9)', 'W-ORD-TESTS-WITH-THE-LISTS-IN-FORCE' in o9 and 'test_chain_page.py (9)' in o9,
        'OPEN_TRAILS :13838 (b650), ACTED at data/b670_work_orders.txt :151', '0')
    # ### the wide shape (the file and an order on one line) hits :13583 alone, hand-read: b643's defects line, its (e) naming the file and its
    # ### one order W-ORD-WATCHDOG-STOP unrelated; the tightened shape asks the order within 200 characters of the file name, one clause
    wide = [i for i, l in enumerate((rd(OT) or '').split(NL), 1) if 'test_chain_page_b638' in l and 'W-ORD-' in l]
    ob = [i for i, l in enumerate((rd(OT) or '').split(NL), 1) if re.search(r'W-ORD-[A-Z0-9-]+[^;]{0,200}test_chain_page_b638|test_chain_page_b638[^;]{0,200}W-ORD-', l)]
    add('ruling (1)', 'no order carries test_chain_page_b638.py (4)-(7) -- an order TO BE ENTERED with a trigger, as the ruling provides', not ob,
        'the wide shape (file and order on one line) %s, hand-read: :13583 b643`s defects, its order W-ORD-WATCHDOG-STOP unrelated; the tightened '
        'shape (one clause) %s' % (wide or 'NONE', ob or 'NONE'), '0')
    # ### (R287)(2): the object
    add('ruling (2)', 'tools/b667_epstein_map_balls.py, the map', os.path.exists(p('tools', 'b667_epstein_map_balls.py')), 'exists', '2')
    dg = grep_lines(p('data', 'b671_tie_diagnostic.txt'), r'Q0 AT qE0 at 200 bits : CONTROLS 41 ; PASS 18 ; FAIL 23 .* INSTRUMENT 23, OBJECT 0')
    add('ruling (2)', 'hQtie 18 of 41; 23 INSTRUMENT, 0 OBJECT', dg, 'data/b671_tie_diagnostic.txt :%s' % (dg[0][0] if dg else None), '2')
    h3 = grep_lines(p('data', 'b671_landing.txt'), r'H3 REFUTED|\(H3\)[^;]*REFUTED')
    add('ruling (2)', 'H3 REFUTED at b671', h3 or 'H3 REFUTED' in (line(OT, 14396) or ''), 'OPEN_TRAILS :14396 ("H1, H2 and H4 HELD, H3 REFUTED")', '2')
    add('ruling (2)', 'the radius doubling to j ~ 53, then 5-100x per j', 'five to a hundred times per j' in (line(OT, 14396) or ''),
        'OPEN_TRAILS :14396', '2')
    tr = line(OT, 14404) or ''
    add('ruling (2)', 'W-ORD-MAP-ANGLE-FORM, trigger "before the next narrowing act"', 'W-ORD-MAP-ANGLE-FORM' in (line(OT, 14398) or '') and
        'before the next narrowing act' in tr, 'OPEN_TRAILS :14398, :14404', '2')
    eb = grep_lines(p('data', 'b675_li_bench.txt'), r'exp\(n·log z\)')
    add('ruling (2)', 'b675`s powers as exp(n·log z)', eb, 'data/b675_li_bench.txt :%s' % (eb[0][0] if eb else None), '2')
    hb = grep_lines(p('data', 'b675_li_controls.txt'), r'^   358865 ')
    add('ruling (2)', 'the angle form to n beyond 3·10⁵ with the radius printed', hb, 'data/b675_li_controls.txt :%s (H6, n = 358865, every row its '
        'ball; C2′ itself to 63876, :644)' % (hb[0][0] if hb else None), '2')
    c2 = grep_lines(p('data', 'b675_li_controls.txt'), r'C2′: NEG 0')
    add('ruling (2)', 'C2′ NEG 0', c2, 'data/b675_li_controls.txt :%s' % (c2[-1][0] if c2 else None), '2')
    bp = grep_lines(p('data', 'b675_li_plan.txt'), r'b671_epstein_zeros_narrowed\.json\.gz')
    add('ruling (2)', '"over the same balls"', bp, 'data/b675_li_plan.txt :%s (the narrowed balls)' % (bp[0][0] if bp else None), '2')
    # ### (R287)(3): the plan's sources
    tie = [line(p('tools', 'b667_epstein_map_balls.py'), n) or '' for n in (331, 356)]
    add('ruling (3)', 'the map`s tie test at tools/b667_epstein_map_balls.py :331-:356', 'controls of hQtie' in tie[0] and "ok('hQtie'" in tie[1],
        ':331 %s | :356 %s' % (tie[0].strip()[:50], tie[1].strip()[:40]), '2')
    secs = grep_lines(p('data', 'b667_epstein_plan.txt'), r'^== 1[1-6]\. ')
    add('ruling (3), ferry', 'data/b667_epstein_plan.txt sections 11-16 as "the map`s quantities and hypotheses"', False,
        'the sections stand (%s) but carry the evaluation route`s amendments -- the author`s word, the Bessel obstructions, T4 -- not the map: '
        'the map`s one row is section 8 :124-:125 (H4), its quantities in tools/b667_epstein_map_balls.py itself -- RAISED' % (
            ', '.join(':%d' % n for n, _l in secs)), '2')
    h3b = line(p('data', 'b667_epstein_plan.txt'), 123) or ''
    h4b = line(p('data', 'b667_epstein_plan.txt'), 124) or ''
    add('ruling (3)-(4)', '"H3 as the b667 plan states it" -- the map`s H3', False,
        'the b667 plan`s H3 (section 8 :123) is the region count, "%s"; the map`s H3 that b671 read REFUTED is data/b671_narrow_plan.txt '
        ':102 -- RAISED' % h3b.strip()[:40], '2-4')
    add('ruling (3)-(4)', '"H4 as the b667 plan states it"', 'b667_epstein_map_balls.py' in h4b, 'data/b667_epstein_plan.txt section 8 :124-:125', '2-4')
    n102 = line(p('data', 'b671_narrow_plan.txt'), 102) or ''
    add('ruling (3)-(4)', 'the map`s H3 at b671', n102.strip().startswith('H3 the map on the narrowed list'), 'data/b671_narrow_plan.txt :102', '2-4')
    cons = ''.join(line(p('data', 'b667_h4_reading.txt'), n) or '' for n in range(9, 15))
    add('ruling (3), (4) H5', 'the consumer at data/b667_h4_reading.txt :9-:14 and its estimate near 1e-18 at :13-:14', 'tie check' in cons and '1e-18' in cons,
        'the tie check, each control`s residual ball at 0 below 2^-20; the input width near 1e-18', '2')
    add('ruling (3)', 'the j range 24 to 64', 'D = 24, J_max = 64' in (line(p('data', 'b667_h4_reading.txt'), 4) or ''), 'data/b667_h4_reading.txt :4', '2')
    wa = grep_lines(p('data', 'b670_work_orders.txt'), r'W-ORD-MAP-ANGLE-FORM')
    add('ferry read-first', 'W-ORD-MAP-ANGLE-FORM by row in data/b670_work_orders.txt', wa,
        'the orders bank was written at b670, before b671 entered the order; no row carries it (%s); the order stands at OPEN_TRAILS :14398 -- '
        'RAISED' % (wa or 'NONE'), '0, 4')
    wb = grep_lines(p('data', 'b670_work_orders.txt'), r'^  W-ORD-EPSTEIN-BALL-WIDTH ')
    add('ferry read-first', 'W-ORD-EPSTEIN-BALL-WIDTH by row', wb, 'data/b670_work_orders.txt :%s' % ', :'.join(str(n) for n, _l in wb), '0, 4')
    # ### (R287)(6): branches
    for repo, nm, bs in (('D:/relay', 'relay', ('push-b676', 'push-b676-root', 'push-b676-closing')),
                         (PP, 'PLACE-papers', ('push-b676', 'push-b676-root')),
                         (TD, 'SIDE-trivium', ('push-b676-main', 'push-b676-merge', 'recut-trivium-b676'))):
        for b in bs:
            add('ruling (6)', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    rt = g(TD, 'branch', '-r', '--list', 'origin/recut-trivium-b676')[1].strip()
    add('ruling (6)', 'SIDE-trivium origin/recut-trivium-b676 (the remote-tracking ref)', rt, rt or 'absent', '0')
    add('ruling (6)', 'data/b676_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b676_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    # ### (R287)(7)-(9) and the banks the ruling orders written
    rl = rd(p('data', 'b675_rules.txt')) or ''
    add('ruling (7)', 'data/b675_rules.txt row 2', '(2) A PRE-RUN\'S LONG PHASE SPLITS THE NEXT ONE' in rl, 'data/b675_rules.txt :9', '5')
    add('ruling (7); ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in rl, 'data/b675_rules.txt :5', '5')
    for b in ('b677_readfirst.txt', 'b677_map_plan.txt', 'b677_map.txt', 'b677_map_h.txt', 'b677_tolerance.txt', 'b677_rules.txt',
              'b677_tool_repairs.txt'):
        sz = b == 'b677_readfirst.txt'
        add('ruling (3)-(8); ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank, written by this act after the check`s first run (exists %s)' % os.path.exists(p('data', b))) if sz
            else 'absent, as ordered', '0-5')
    add('ferry C3', 'tools/b677_epstein_map_angle.py -- TO BE WRITTEN', not os.path.exists(p('tools', 'b677_epstein_map_angle.py')), 'absent, as ordered', '3')
    add('ruling (9)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b676_worklist.py')) or ''), 'tools/b676_worklist.py :25', '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '4')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    return R


def _write(L, R, miss):
    for name, data in (('b677_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b677_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b677 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    _write(L, R, miss)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    text = ferry_text()
    q = os.path.join(D, 'b677_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b677_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b677_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


def after_root():
    """(R282)(2) row 1: the exclusion list read before the write -- True once data/act_roots.txt carries b677's root."""
    return bool(act_root_line('b677'))


def answer(needle, *a):
    """(R278)(4): the latest session text carrying `needle` (a navigator answer or note) -- its relay paths, ledger lines and commits checked
    at HEAD, the print appended to the citation bank, or after the root to the defects bank, with the answer named."""
    best = None
    for t in _user_texts():
        u = t.replace('’', "'")
        if needle in t and ("NAVIGATOR'S ANSWER" in u or "NAVIGATOR'S NOTE" in u or "AUTHOR'S" in u or 'The user answered' in u):
            best = t
    if best is None:
        sys.exit('### NO ANSWER CARRYING %r IN THE SESSION -- NOTHING WRITTEN' % needle)
    # ### one result can carry several answers (b675 defect (j), b676 defect (b)): the answer is cut from the last BEGIN before the needle
    # ### to the first END after it
    k = best.find(needle)
    b0, e0 = best.rfind('BEGIN', 0, k), best.find('END', k)
    if b0 >= 0 and e0 > k:
        best = best[b0:e0 + 3]
    rows_ = []
    for pth in sorted(set(re.findall(r'\b((?:data|tools)/[\w./-]+\.[a-z]{2,4})\b', best))):
        ex = os.path.exists(os.path.join(ROOT, *pth.split('/')))
        if not ex and re.match(r'^(data|tools)/b677_', pth):
            rows_.append(('path, this act`s bank or tool the answer orders written -- TO BE WRITTEN, not a cite', pth, True))
        elif not ex and 'bNNN' in pth:
            rows_.append(('path, a placeholder of a form for later acts -- not a cite', pth, True))
        else:
            rows_.append(('path', pth, ex))
    for m in re.finditer(r'\b(FINDINGS|OPEN_TRAILS)\b((?:[^:\n]{0,20}:\d{3,5})+(?:(?:,|;| and|,? or)\s*:\d{3,5})*)', best):
        for n in sorted(set(re.findall(r':(\d{3,5})', m.group(2)))):
            rows_.append(('line', '%s :%s' % (m.group(1), n), line(os.path.join(PP, m.group(1) + '.md'), int(n)) is not None))
    for h in sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', best))):
        if re.search(r'[a-f]', h) and re.search(r'\d', h):
            rows_.append(('commit', h, any(commit_in(r_, h) for r_ in REPOS)))
    miss = [r for r in rows_ if not r[2]]
    q = os.path.join(D, 'b677_defects.txt' if after_root() else 'b677_citation_check.txt')
    old = (rd(q) or '').rstrip(NL)
    L = ['', '### (R278)(4) THE MID-ACT CHECK (%s): the answer carrying %r, %d characters; its cites checked at HEAD before the seat '
         'acts on it%s:' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), needle, len(best),
                            ' (after the root: printed to the defects bank, (R282)(2) row 1)' if after_root() else '')]
    L += ['  %-4s | %s | %s' % ('OK' if ok else 'MISS', k, w) for k, w, ok in rows_] or ['  (no path, ledger line or commit named)']
    L += ['### ### **ANSWER CITES CHECKED %d ; OK %d ; MISSES %d%s.**%s' % (len(rows_), len(rows_) - len(miss), len(miss),
                                                                         (' -- RAISED: ' + ', '.join(w for _k, w, _o in miss)) if miss else '',
                                                                         ' -- VACUOUS: no cite to check.' if not rows_ else '')]
    open(q + '.tmp', 'wb').write((old + NL + NL.join(L) + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    print(NL.join(L))


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b677_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
