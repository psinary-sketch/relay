# -*- coding: utf-8 -*-
"""b675_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b675's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it. Carried from
tools/b674_citation.py by the Write tool: the helpers unchanged (both apostrophes, SESSIONS_AFTER, the after-root redirect of (R282)(2)
row 1: once data/act_roots.txt carries b675's root, an answer's print goes to data/b675_defects.txt and to no root-named bank); the
constants and the rows b675's.

### Before the ferry is banked, every path, line, bank, branch, tag, declaration and named rule the ruling (R285) and the ferry cite is
### checked for existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not
### repaired silently; the print is banked as data/b675_citation_check.txt and read by the suite. A bank the ruling orders written is
### printed TO BE WRITTEN, not a cite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R285) BEGIN'), never from a scratch copy.
### Routes: `python tools/b675_citation.py check` -> data/b675_citation_check.txt (.json);
###         `python tools/b675_citation.py ferry`  -> data/b675_ferry.txt and data/b675_ferry_scan.txt (ferry_scan.py's output, captured);
###         `python tools/b675_citation.py answer <needle>` -> the latest session answer carrying <needle>, its cites checked, the print APPENDED
###         to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b675; this tool writes only the banks named above.
"""
import gzip
import hashlib
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
KREV = 'e36ea31'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/51ceaa11-0301-4ed4-9e1c-71b70f1e78ca.jsonl'
SESSIONS_AFTER = ()
ANCHOR, TAIL = 'RULING (R285) BEGIN', 'FERRY END (part 1 of 1)'
REPOS = (ROOT, PP, KE, 'D:/SIDE-window', 'D:/SIDE-trivium')
MIRROR = 'D:/MY-DOwnloads/mirror-refresh-2026-10-17-b674.zip'
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


def kline(path, n):
    """a kernel file's line n at KREV, read by git show (the kernel is not built or checked out here)."""
    rc, o = g(KE, 'show', '%s:%s' % (KREV, path))
    ls = o.split(NL) if rc == 0 else []
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
    for f in ('data/b674_closing.txt', 'data/b674_defects.txt', 'data/b674_cut.txt', 'data/b674_rules.txt', 'data/b673_v4v5_plan.txt',
              'data/b673_v4_control.txt', 'data/b673_landing.txt', 'data/b671_narrow_plan.txt', 'data/b667_epstein_plan.txt',
              'tools/b671_narrow.py', 'data/b671_tie_diagnostic.txt', 'data/b674_closing_push_out.txt'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-6')
    zj = p('data', 'b671_epstein_zeros_narrowed.json')
    hb = rd(p('data', 'b671_epstein_zeros_narrowed_hashes.txt')) or ''
    add('ruling (4); ferry read-first', 'data/b671_epstein_zeros_narrowed.json', os.path.exists(zj),
        'absent as a file: the bank is committed as data/b671_epstein_zeros_narrowed.json.gz (exists %s), the JSON inside it named by '
        'data/b671_epstein_zeros_narrowed_hashes.txt :2 (sha256 cd3a8ea1..., carried %s); read through the .gz with the inner sha256 '
        'printed -- RAISED' % (os.path.exists(zj + '.gz'), 'cd3a8ea1dcc7660c' in hb), '2-4')
    # ### (R285)(1): b674 at its weight
    cl = rd(p('data', 'b674_closing.txt')) or ''
    head = cl.split(NL)[0]
    quoted = ('b674 closed: relay 7d432c88, PLACE-papers 4cb90e0, SIDE-window e5b737a v0.5.1; suite 84 of 84; root 34e0e30f0034da57'
              '\u2026; 6 prompts answered; 14 defects')
    add('ruling (1)', 'the head line quoted at data/b674_closing.txt :1', head == quoted, 'character for character: %s' % (head == quoted), '1')
    for repo, nm, sha, needle in ((ROOT, 'relay', '92e003e7', 'b674 record'), (ROOT, 'relay', '27992411', 'b674 closing'),
                                  (ROOT, 'relay', '7d432c88', 'b674 seal'), (PP, 'PLACE-papers', '6b95ac8', 'b674 record'),
                                  (PP, 'PLACE-papers', '4cb90e0', 'b674 Component 2')):
        s = subject(repo, sha)
        add('ruling (1), corrigenda', '%s %s, its subject opening "%s"' % (nm, sha, needle), commit_in(repo, sha) and s.startswith(needle),
            s[:80], '0-1')
    for pat, what in ((r'ROWS 6 ; MATCHES AFTER 5 ; CUT IN PART 1 ; THE DISTANCE BEFORE 5, AFTER 1 \(OF ANY KIND 6, 1\)', 'the re-cut 6 to 1, by b670`s method 5 to 1'),
                      (r'before 38988546013 at 3dab5f4 DERIVES ; after 38988610526 at 22bf840 DERIVES', 'both runner builds DERIVES'),
                      (r'THE SUCCESSOR BYTE-EQUAL AT ITS THREE SITES True', 'the successor byte-equal'),
                      (r'### AGREE 8 of 8', 'the sealed tools agree')):
        h = grep_lines(p('data', 'b674_closing.txt'), pat)
        add('ruling (1)', what, h, 'data/b674_closing.txt :%s' % (h[0][0] if h else None), '1')
    h = grep_lines(p('data', 'b674_cut.txt'), r'the marker at :17')
    add('ruling (1)', 'the Sawtooth header`s marker at :17 left', h, 'data/b674_cut.txt :%s' % (h[0][0] if h else None), '1')
    add('ruling (1)', 'SIDE-window e5b737a, tag v0.5.1 peeled e5b737a', g('D:/SIDE-window', 'rev-parse', 'v0.5.1^{commit}')[1].startswith('e5b737a'),
        'rev-parse v0.5.1^{commit}', '1')
    for f, n, needle in (('README.md', 127, '(R284)`(3)'), ('REGISTRY.md', 962, '(R284)`(3)'), ('FINDINGS.md', 8849, '(R284)`(3)'),
                         ('FINDINGS.md', 8851, '## SIDE-window docstrings re-cut'), ('OPEN_TRAILS.md', 14508, '### b674')):
        l = line(os.path.join(PP, f), n) or ''
        add('ruling (1)', '%s :%d' % (f, n), needle in l, l[:90], '1')
    ar = act_root_line('b674')
    n_items = len([i for i in (json.loads(rd(p('data', 'b674_act_root.json')) or '{}').get('items') or []) if i.startswith('data/')])
    add('ruling (1)', 'root 34e0e30f... chained from 4f86a025... over 45 banks', ar and ar[0][1].startswith('34e0e30f')
        and ar[0][2].startswith('4f86a025') and n_items == 45, 'data/act_roots.txt b674 ; data/b674_act_root.json`s data items %d' % n_items, '1')
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-17-b674.zip CLEAN with the root line', os.path.exists(MIRROR)
        and 'Act root: b674 34e0e30f' in (rd(p('data', 'b674_mirror.txt')) or ''), MIRROR, '1')
    dl = rd(p('data', 'b674_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-m]'?)\) THE ([A-Z']+?)'S", dl, re.M)
    nav = [x for x, o in letters if o == 'NAVIGATOR']
    add('ruling (1)', 'fourteen defects (a)-(m) and (e`), "(a)-(d) the navigator`s"', len(letters) == 14 and nav == list('abcd'),
        'data/b674_defects.txt: %d lettered rows; the navigator`s %s -- (e`) is the navigator`s as well (:32, "THE NAVIGATOR`S: A ROW TO '
        'DISCHARGE THAT THE ITEM DOES NOT CARRY") -- RAISED' % (len(letters), nav), '1')
    # ### (R285)(2): defect (m)'s three readings, (l)'s names
    add('ruling (2)', 'defect (m): the lightweight tag, the prints line, the citation line', all(k in dl for k in (
        'lightweight tag', 'PRINTS BEFORE[^*]*', 'the citation line')), 'data/b674_defects.txt (m), :82-:90', '5')
    add('ruling (2)', 'defect (l): the capture names', "(l) THE SEAT'S: THE PUSH CAPTURES NAMED" in dl, 'data/b674_defects.txt (l), :73', '5')
    add('ruling (2)', 'tools/b674_closing.py, the sealed copy the repairs diff against', os.path.exists(p('tools', 'b674_closing.py')), 'exists', '5')
    # ### (R285)(3): branches
    for repo, nm, bs in (('D:/relay', 'relay', ('push-b674', 'push-b674-root', 'push-b674-closing')),
                         (PP, 'PLACE-papers', ('push-b674', 'push-b674-root')),
                         ('D:/SIDE-window', 'SIDE-window', ('push-b674-workflow', 'push-b674-merge', 'recut-window-b674'))):
        for b in bs:
            add('ruling (3)', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (3)', 'SIDE-window origin/recut-window-b674', g('D:/SIDE-window', 'rev-parse', '--verify', '-q', 'origin/recut-window-b674')[0] == 0,
        'the remote-tracking ref (the remote read at deletion)', '0')
    tip = g(KE, 'rev-parse', 'origin/chi-li-b669')[1].strip()
    add('ruling (3)', 'SIDE-explicit-formula origin/chi-li-b669 tip 5050a46, an ancestor of main e36ea31', tip.startswith('5050a46')
        and g(KE, 'merge-base', '--is-ancestor', tip or 'x', KREV)[0] == 0, 'tip %s ; merge-base --is-ancestor' % tip[:12], '0')
    # ### (R285)(4)-(6): the kernel's statements at v0.32 and the object
    add('ruling (4)', 'SIDE-explicit-formula v0.32 at e36ea31', g(KE, 'rev-parse', 'v0.32^{commit}')[1].startswith('e36ea31'), 'rev-parse', '2-4')
    for path, n, needle in (('SIDEExplicitFormula/RestBound.lean', 40, 'def HStrip'), ('SIDEExplicitFormula/RestBound.lean', 44, 'def HCount'),
                            ('SIDEExplicitFormula/Schema/LiRemainder.lean', 175, 'theorem remainder_le'),
                            ('SIDEExplicitFormula/Schema/LiRemainder.lean', 110, 'theorem summable_rest'),
                            ('SIDEExplicitFormula/Schema/LiRemainder.lean', 125, 'theorem rest_term_le'),
                            ('SIDEExplicitFormula/Schema/LiConverseCfg.lean', 157, 'theorem li_nonneg_cfg_imp_online'),
                            ('SIDEExplicitFormula/Schema/LiConverseCfg.lean', 192, 's1 < s ∧ s < R'),
                            ('SIDEExplicitFormula/Schema/LiConverseCfg.lean', 259, 'powerSum_re_ge_infinitely'),
                            ('SIDEExplicitFormula/Schema/EpsteinQ0.lean', 104, 'def A0Q : ℝ := 10'),
                            ('SIDEExplicitFormula/Schema/EpsteinQ0.lean', 108, 'def Q0Count')):
        l = kline(path, n) or ''
        add('ruling (4)-(6); ferry read-first', '%s :%d at %s' % (path, n, KREV), needle in l, l.strip()[:90], '2-3')
    for f in ('Schema/PowerSum.lean', 'Schema/LiCfg.lean'):
        add('ferry read-first', 'SIDEExplicitFormula/%s at %s' % (f, KREV), g(KE, 'cat-file', '-e', '%s:SIDEExplicitFormula/%s' % (KREV, f))[0] == 0,
            'git cat-file', '3')
    zz = {}
    try:
        zz = json.load(gzip.open(zj + '.gz', 'rt', encoding='utf-8'))
    except (OSError, ValueError):
        pass
    kinds = [r_.get('kind') for r_ in zz.get('rows') or []]
    add('ruling (4)', '163 points narrowed to half-width 1e-24, 146 on the line and 17 off it', str(zz.get('w')) == '1e-24' and kinds.count('ON') == 146
        and kinds.count('OFF') == 17, 'the .gz`s rows: ON %d, OFF %d, w %s' % (kinds.count('ON'), kinds.count('OFF'), zz.get('w')), '2')
    pl = rd(p('data', 'b673_v4v5_plan.txt')) or ''
    add('ruling (4)', 'the composition along V4`s subsequence, c = Σm²/(4Σm)', 'C (n + 1)^2 s^n' in pl and 'along (V4+)`s n' in pl,
        'data/b673_v4v5_plan.txt :75, :89', '3')
    vc = rd(p('data', 'b673_v4_control.txt')) or ''
    add('ruling (6)(i)', 'the control of b673 read 1/4', 'c = Σ m^2 / (4 Σ m) = 1/4' in vc, 'data/b673_v4_control.txt :24', '3')
    # ### (R285)(5): the count law
    ep = rd(p('data', 'b667_epstein_plan.txt')) or ''
    add('ruling (5)', 'a count law for Z_Q pinned in data/b667_epstein_plan.txt', False,
        'the plan pins none (its counts are the region and square counts of sections 1, 4, 11; %d lines read); the kernel carries one as a '
        'PREMISE: (P3) Q0Count := HCount Z A0Q, A0Q = 10 (Schema/EpsteinQ0.lean :104-:108, "stated, not proved; open", its reason relay '
        'data/b663_a0_list.txt) -- by the ruling`s clause named T-COUNT and carried as an ASSUMPTION; RAISED with Component 2' % len(ep.split(NL)), '2')
    # ### (R285)(6): the plan's constants against the Lean proof
    l182 = kline('SIDEExplicitFormula/Schema/LiRemainder.lean', 180) or ''
    add('ruling (6)(ii)', '"K` = Σ_{‖ρ‖≥R0} m/‖ρ‖²" as the proof`s constant', False,
        'the proof fixes C = 2(2 + 2(1 + s)²)·Σ over {‖1 - ρ⁻¹‖ < s} of m/(1 + |γ|²) (Schema/LiRemainder.lean :180-:181: "%s"), and its '
        'header (:12) reads "The plan`s split at ‖ρ‖ = R0 is not needed"; the plan computes the proof`s C (partial sum plus tail under '
        'T-COUNT) and prints K` beside it as the ruling names it -- RAISED' % l182.strip()[:60], '3')
    add('ruling (6)(ii)', '"s chosen as the proof chooses it"', 's1 < s ∧ s < R' in (kline('SIDEExplicitFormula/Schema/LiConverseCfg.lean', 192) or ''),
        'Schema/LiConverseCfg.lean :192 s = (s1 + R)/2, s1 from r = (1 + ‖1 - ρ`⁻¹‖)/2 (:165-:166), ρ` the orbit member of an off-line '
        'point the by_contra names (:162-:164): the proof fixes s once that point is fixed; the plan fixes it at the dominant point', '3')
    td = rd(p('data', 'b671_tie_diagnostic.txt')) or ''
    add('ruling (6)(iii)', 'data/b671_tie_diagnostic.txt as "b671`s blow-up" by repeated multiplication', re.search(r'(?i)squar', td),
        'the diagnostic`s rows print the tie separation`s radius growing with j and name no squaring; the reason, squaring the ball in '
        'place of amplifying the angle, is stated at data/b671_scanfile_landing.md :6 and OPEN_TRAILS :14396 -- RAISED', '3')
    # ### (R285)(7): H3 against the theorem's scope
    add('ruling (7) H3', '"P_n + U_n < 0 at every n in [n*, n* + 200]" as the bound`s prediction', False,
        'the composition bounds λ_n only at the n of V4`s subsequence, where Re Σ_D m wⁿ ≥ c (Schema/LiConverseCfg.lean :259, '
        'powerSum_re_ge_infinitely; data/b673_v4v5_plan.txt :89 "along (V4+)`s n"); at Q0, D = {qE0`s reflection, its conjugate}, '
        'Re Σ_D wⁿ = 2cos(nθ), and data/b673_v4_control.txt :4032 certifies Re ≤ -c at 1839 of n = 1..4000 -- the bound predicts '
        'nothing there -- RAISED with Component 3', '3-4')
    # ### (R285)(9)-(11)
    for b in ('b675_readfirst.txt', 'b675_corrigenda.txt', 'b675_hypotheses.txt', 'b675_li_plan.txt', 'b675_li_bench.txt',
              'b675_li_controls.txt', 'b675_tool_repairs.txt', 'b675_rules.txt'):
        sz = b in ('b675_readfirst.txt', 'b675_corrigenda.txt')
        add('ruling (5)-(9); ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank, written by this act after the check`s first run (exists %s)' % os.path.exists(p('data', b))) if sz
            else 'absent, as ordered', '0-5')
    add('ruling (10)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b674_worklist.py')) or ''), 'tools/b674_worklist.py :24', '6')
    rl = rd(p('data', 'b674_rules.txt')) or ''
    add('ruling (11)', 'the tie-break rule of data/b674_rules.txt', '(2) THE TIE-BREAK BEYOND THE COUNT' in rl, 'data/b674_rules.txt row (2)', '6')
    l119 = line(p('data', 'b670_licensed_table.txt'), 119) or ''
    add('ruling (11)', 'SIDE-trivium at 5, the carried candidate', 'SIDE-trivium docstrings' in l119 and re.search(r'\b5 ->\s+5\b', l119),
        'data/b670_licensed_table.txt :119', '6')
    for rule, cl_, comp in (('R278', (4,), '0-6'), ('R251', (3,), '6'), ('R254', (2,), '0-6')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    return R


def _write(L, R, miss):
    for name, data in (('b675_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b675_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b675 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
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
    q = os.path.join(D, 'b675_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b675_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b675_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


def after_root():
    """(R282)(2) row 1: the exclusion list read before the write -- True once data/act_roots.txt carries b675's root."""
    return bool(act_root_line('b675'))


def answer(needle, *a):
    """(R278)(4): the latest session text carrying `needle` (a navigator answer or note) -- its relay paths, ledger lines and commits checked
    at HEAD, the print appended to the citation bank, or after the root to the defects bank, with the answer named."""
    best = None
    for t in _user_texts():
        u = t.replace('’', "'")
        if needle in t and ("NAVIGATOR'S ANSWER" in u or "NAVIGATOR'S NOTE" in u or "AUTHOR'S" in u):
            best = t
    if best is None:
        sys.exit('### NO ANSWER CARRYING %r IN THE SESSION -- NOTHING WRITTEN' % needle)
    rows_ = []
    for pth in sorted(set(re.findall(r'\b((?:data|tools)/[\w./-]+\.[a-z]{2,4})\b', best))):
        ex = os.path.exists(os.path.join(ROOT, *pth.split('/')))
        if not ex and re.match(r'^(data|tools)/b675_', pth):
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
    q = os.path.join(D, 'b675_defects.txt' if after_root() else 'b675_citation_check.txt')
    old = (rd(q) or '').rstrip(NL)
    L = ['', '### (R278)(4) THE MID-ACT CHECK (%s): the navigator`s answer carrying %r, %d characters; its cites checked at HEAD before the seat '
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
        print('usage: b675_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
