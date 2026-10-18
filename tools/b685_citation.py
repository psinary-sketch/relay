# -*- coding: utf-8 -*-
"""b685_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b685's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling; the answer route is
### b682's, imported from tools/b682_citation.py with its act names pointed at b685; the rows and the banks are b685's.
### Routes: `check` -> data/b685_citation_check.txt (.json) ; `ferry` -> data/b685_ferry_scan.txt ; `answer <needle>` -> the check on one
###         answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b685 from b684_citation.py's form; this tool writes only the banks named above.
"""
import gzip
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

NL = chr(10)
PP, KE, TD = C.PP, C.KE, C.TD
C.ANCHOR, C.TAIL = 'RULING (R295) BEGIN', 'FERRY END (part 1 of 1)'
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
REPOS = C.REPOS + ('D:/SIDE-silence-principle', 'D:/SIDE-bijection', 'D:/SIDE-window', 'D:/SIDE-trivium', 'D:/SIDE-class-number-anomaly')
KTAG = 'v0.33'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def kshow(path, n=None):
    """a kernel file at the tag v0.33, whole or its line n."""
    r = subprocess.run(['git', '-C', KE, 'show', '%s:%s' % (KTAG, path)], capture_output=True)
    t = r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else ''
    return t if n is None else (t.split(NL)[n - 1] if len(t.split(NL)) >= n else '')


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    # ### the ferry's read-first list
    for f in ('data/b684_closing.txt', 'data/b684_defects.txt', 'data/b684_scores.json', 'data/b675_hypotheses.txt', 'data/b683_map_h.txt',
              'data/b679_q0_membership.txt', 'data/b667_epstein_plan.txt', 'data/b667_epstein_zeros_certified.json.gz', 'data/b667_large_banks.txt',
              'data/b681_epstein_zeros_narrowed.json.gz', 'data/b681_epstein_zeros_narrowed_hashes.txt', 'data/b673_v4v5_plan.txt',
              'tools/b671_narrow.py', 'data/b670_work_orders.txt', 'data/b684_closing_push_out.txt', 'data/b667_epstein_counts.txt',
              'data/b679_strip_plan.txt'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-4')
    # ### (R295)(1): b684 at its weight
    head = (rd(p('data', 'b684_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line at data/b684_closing.txt :1', head == ('b684 closed: relay b6df52d7, PLACE-papers a2acff6; suite 107 of 107; root '
                                                                         '4c8935f8f80c9eac\u2026; 2 prompts answered; 5 defects'), head[:110], '1')
    po = rd(p('data', 'b684_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing at relay 4b97f382 read back', 'b6df52d7..4b97f382' in po and 'read back at the remote: 4b97f382' in po,
        'data/b684_closing_push_out.txt', '0-1')
    for repo, nm, sha, needle in ((ROOT, 'relay', 'b6df52d7', 'b684 record'), (ROOT, 'relay', '4b97f382', 'b684 closing'),
                                  (PP, 'PLACE-papers', 'a2acff6', 'b684 record')):
        s = subject(repo, sha)
        add('ruling (1)', '%s %s' % (nm, sha), commit_in(repo, sha) and s.startswith(needle), s[:80], '0-1')
    for f in ('b684_checks.txt', 'b684_checks_postpush.txt'):
        add('ruling (1)', 'suite 107 of 107 (%s)' % f, 'ARMS RUN : 107. ### LIVE PASSING : 107. ### LIVE FAILING : 0 .' in (rd(p('data', f)) or ''), 'data/%s :9' % f, '1')
    add('ruling (1)', 'root 4c8935f8 in the chain', any(r[1].startswith('4c8935f8') for r in act_root_line('b684')), 'data/act_roots.txt', '1')
    add('ruling (1)', 'the split rule row "a suite PART over 450 s splits the next run"', 'A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (line(p('data', 'b684_rules.txt'), 5) or '')
        and 'data/b675_rules.txt row 2' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5, :9', '1')
    add('ruling (1)', 'a part not starting beneath the 2,560 MB hold', 'HOLD = 2560' in (rd(p('tools', 'b684_tests.py')) or ''), 'tools/b684_tests.py :42', '1')
    add('ruling (1)', 'G-RULE-SUITE-PARTS repaired at carry', 'G-RULE-SUITE-PARTS' in (rd(p('data', 'b684_tool_repairs.txt')) or ''), 'data/b684_tool_repairs.txt', '1')
    for k, tag in (('SIDE-class-number-anomaly', 'v0.2.1'), ('SIDE-window', 'v0.5.2'), ('SIDE-trivium', 'v0.1.2'), ('SIDE-silence-principle', 'v0.2.2')):
        tc = g('D:/' + k, 'rev-parse', tag + '^{commit}')[1].strip()
        add('ruling (1)', '%s tagged %s at main' % (k, tag), bool(tc) and tc == g('D:/' + k, 'rev-parse', 'main')[1].strip(), tc[:12], '1')
    cut = rd(p('data', 'b684_cut.txt')) or ''
    add('ruling (1)', 'the distance 3 to 0; R3b CARRIED (introduction :7-:12)', 'introduction :7-:12   CARRIED (R3b)' in cut
        and 'CARRIED 1 (R3b)' in cut, 'data/b684_cut.txt :72, :84', '1')
    add('ruling (1)', 'three FOUNDATIONS cells carried, not hand-written', 'CELLS CHANGED 3' in cut and 'no cell by hand' in cut, 'data/b684_cut.txt :80-:82', '1')
    sc = json.load(open(p('data', 'b684_scores.json'), encoding='utf-8'))
    add('ruling (1)', 'N4 REFUTED with the scorer`s line quoted; N1-N3, N5, S1-S3 HELD', sc['N4'][0] == 'REFUTED' and 'the sealed scorer cannot see that move and read HELD' in sc['N4'][1]
        and all(sc[k][0] == 'HELD' for k in ('N1', 'N2', 'N3', 'N5', 'S1', 'S2', 'S3')), 'data/b684_scores.json :14-:16', '1')
    dl = rd(p('data', 'b684_defects.txt')) or ''
    add('ruling (1)', 'five defects: (a), (c)-(e) the seat`s, (b) the navigator`s', re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M) == [
        ('a', 'SEAT'), ('b', 'NAVIGATOR'), ('c', 'SEAT'), ('d', 'SEAT'), ('e', 'SEAT')], 'data/b684_defects.txt :5-:29', '1')
    add('ruling (1)', 'the b684 mirror CLEAN', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-18-b684.zip')
        and 'VERDICT: CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b684_mirror_verify.txt')) or ''), 'the zip and data/b684_mirror_verify.txt :24', '0')
    for f, n, needle in (('FINDINGS', 9200, '## SIDE-class-number-anomaly re-cut'), ('OPEN_TRAILS', 14804, '### b684')):
        lt = line(FIND if f == 'FINDINGS' else OT, n) or ''
        add('ruling (1)', '%s :%d' % (f, n), needle in lt, lt[:70], '1')
    # ### (R295)(2): the object
    hy = rd(p('data', 'b675_hypotheses.txt')) or ''
    add('ruling (2)', 'P3 as data/b675_hypotheses.txt names it, quoted "HCount Z 10"', 'HCount Z 10' in hy,
        'the bank names it "HCount Z A0Q" with "def A0Q : ℝ := 10" (:61) and "(P3, A₀Q = 10)" (:67); the quoted string is not the bank`s text -- '
        'it is data/b679_q0_membership.txt :66`s (%s)' % ('HCount Z 10' in (line(p('data', 'b679_q0_membership.txt'), 66) or '')), '2')
    add('ruling (2)', 'T-COUNT at data/b675_hypotheses.txt :61', 'T-COUNT, named by (R285)(5)' in (line(p('data', 'b675_hypotheses.txt'), 61) or ''), 'data/b675_hypotheses.txt :61', '2')
    mh = rd(p('data', 'b683_map_h.txt')) or ''
    add('ruling (2); ferry', 'the hA row of data/b683_map_h.txt', re.search(r'\bhA\b', mh) is not None,
        'data/b683_map_h.txt carries rows H1-H5 and no hA row; the hA line is data/b683_map_run.txt :176 ("BY P3 (Q0Count, ...)") -- %s' % (
            'BY P3 (Q0Count' in (line(p('data', 'b683_map_run.txt'), 176) or '')), '2')
    # ### (R295)(3): the statement
    hc = kshow('SIDEExplicitFormula/RestBound.lean', 44)
    add('ruling (3); ferry', 'HCount at SIDEExplicitFormula/RestBound.lean :44 (v0.33)', hc.startswith('def HCount (Z : Zeta23.ZeroConfig) (A₀ : ℝ) : Prop :='), hc[:70], '2')
    add('ferry', 'Zeta23/Defs.lean :142 (v0.33)', 'strip : ∀ ρ ∈ carrier, 0 ≤ ρ.re ∧ ρ.re ≤ 1' in kshow('Zeta23/Defs.lean', 142), kshow('Zeta23/Defs.lean', 142).strip()[:60], '2')
    df = kshow('Zeta23/Defs.lean')
    st = df[df.index('structure ZeroConfig where'):df.index('namespace ZeroConfig')] if 'structure ZeroConfig where' in df else ''
    add('ferry', 'the configuration`s count field by line', re.search(r'^\s+\w*count\w* :', st, re.M | re.I) is not None,
        'ZeroConfig (Zeta23/Defs.lean :136-:146) carries no count field; :133-:134 "The quantitative local count ... is not part of this structure; it '
        'is a field of PaperInputs (H-RvM)" -- Zeta23/Hypotheses.lean :86 `local_count` (%s); the widened class Schema/Wide/Config.lean :49 `Wide.HCount` (%s)' % (
            'local_count : ∃ A₀' in kshow('Zeta23/Hypotheses.lean', 86), 'def HCount (Z : WideConfig)' in kshow('SIDEExplicitFormula/Schema/Wide/Config.lean', 49)), '2')
    add('ferry', 'SIDE-explicit-formula v0.33 at main 95f8dc8', g(KE, 'rev-parse', '--short', KTAG + '^{commit}')[1].strip() == '95f8dc8' == g(KE, 'rev-parse', '--short', 'main')[1].strip(),
        'git rev-parse', '2')
    add('ferry', 'Q0Count := HCount Z A0Q, A0Q := 10 (Schema/EpsteinQ0.lean :104, :108)', kshow('SIDEExplicitFormula/Schema/EpsteinQ0.lean', 104).startswith('def A0Q : ℝ := 10')
        and 'HCount Z A0Q' in kshow('SIDEExplicitFormula/Schema/EpsteinQ0.lean', 108), 'v0.33', '2')
    pl = rd(p('data', 'b667_epstein_plan.txt')) or ''
    add('ruling (3); ferry', 'Q0`s completed function and functional equation (data/b667_epstein_plan.txt :10)', 'Λ_Q(s) = (2π/√23)^{−s} Γ(s) Z_Q(s); Λ_Q(s) = Λ_Q(1 − s)'
        in (line(p('data', 'b667_epstein_plan.txt'), 10) or ''), 'section 1 :10 -- the ruling`s (√23/2π)^s is the same factor', '2')
    add('ruling (3); ferry', 'the region R and N(R) = 180', 'N(R) = 180 (ball [180.0000000 +/- 1e-12])' in (line(p('data', 'b667_epstein_counts.txt'), 52) or '')
        and 'R = [−0.5, 1.5] × [0.5, 150]' in (line(p('data', 'b667_epstein_plan.txt'), 206) or ''), 'data/b667_epstein_counts.txt :49-:52; plan section 13 :206', '2')
    add('ruling (3); (5)', 'the (3c) tail bound at σ = 3/2 (plan section 15 :247-:248)', '(3c) R\'s right edge σ = 3/2 by the uniform tail bound' in (line(p('data', 'b667_epstein_plan.txt'), 247) or '')
        and '|Z_Q(3/2 + it) − 2| < 2' in (line(p('data', 'b667_epstein_plan.txt'), 248) or ''), 'data/b667_epstein_plan.txt :247-:248', '2-3')
    add('ruling (3); (5)', 'V2: Z_Q(3/2) − 2 = [1.548...] below 2', 'below 2 : True -> V2 HOLDS' in (rd(p('data', 'b667_epstein_counts.txt')) or ''), 'data/b667_epstein_counts.txt (V2)', '2-3')
    try:
        nr = json.loads(gzip.open(p('data', 'b681_epstein_zeros_narrowed.json.gz')).read())['rows']
    except Exception:
        nr = []
    add('ruling (3)', 'b681`s 163 points', len(nr) == 163, 'data/b681_epstein_zeros_narrowed.json.gz rows %d' % len(nr), '2')
    add('ferry', 'the narrowed hashes bank', 'f6613564e9d7fcd534534d0c33e418229bf32dbc0567c951ee8750438b11eb5a' in (rd(p('data', 'b681_epstein_zeros_narrowed_hashes.txt')) or ''),
        'data/b681_epstein_zeros_narrowed_hashes.txt :3', '2')
    add('ferry', 'the certified list`s hashes bank', '5dfd6a4bfdc099298b2a0953f92faeea6e57262045cdf7ab09e24c3353b9ff05' in (rd(p('data', 'b667_large_banks.txt')) or ''),
        'data/b667_large_banks.txt :4', '2')
    add('ferry', 'K and the count`s use in V5 (data/b673_v4v5_plan.txt :79-:80)', 'finite by HCount' in (line(p('data', 'b673_v4v5_plan.txt'), 79) or ''), 'data/b673_v4v5_plan.txt :79', '2')
    add('ferry', 'tools/b671_narrow.py, the ball form', 'from flint import arb, acb, ctx' in (rd(p('tools', 'b671_narrow.py')) or ''), 'tools/b671_narrow.py :42', '3')
    wo = line(p('data', 'b670_work_orders.txt'), 275) or ''
    add('ferry', 'W-ORD-EPSTEIN-COUNT in the orders bank', 'W-ORD-EPSTEIN-COUNT' in wo and 'OPEN' in wo, 'data/b670_work_orders.txt :275', '4')
    ot = line(OT, 14678) or ''
    add('ferry', 'both routes as b680 priced them (OPEN_TRAILS :14678)', 'W-ORD-EPSTEIN-COUNT' in ot and '(i) A located explicit' in ot and '(ii) A certification by the argument principle' in ot,
        'OPEN_TRAILS :14678', '2-3')
    # ### (R295)(8): branches
    for repo, bs in (('D:/relay', ('push-b684-root', 'push-b684', 'push-b684-closing')), (PP, ('push-b684-root', 'push-b684')),
                     ('D:/SIDE-class-number-anomaly', ('push-b684-main', 'push-b684-merge', 'recut-class-number-anomaly-b684')),
                     ('D:/SIDE-window', ('push-b684r-merge', 'recut-window-b684r')), ('D:/SIDE-trivium', ('push-b684r-merge', 'recut-trivium-b684r')),
                     ('D:/SIDE-silence-principle', ('push-b684r-merge', 'recut-silence-principle-b684r'))):
        for b in bs:
            add('ruling (8)', '%s %s' % (os.path.basename(repo), b), branch_listed(repo, b), 'git branch --list', '0')
    for repo, b in (('D:/SIDE-class-number-anomaly', 'recut-class-number-anomaly-b684'), ('D:/SIDE-window', 'recut-window-b684r'),
                    ('D:/SIDE-trivium', 'recut-trivium-b684r'), ('D:/SIDE-silence-principle', 'recut-silence-principle-b684r')):
        add('ruling (8)', '%s origin/%s' % (os.path.basename(repo), b), g(repo, 'rev-parse', '--verify', '--quiet', 'refs/remotes/origin/' + b)[0] == 0,
            'the remote-tracking ref', '0')
    add('ruling (8)', 'data/b684_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b684_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    # ### (R295)(10)-(11)
    add('ruling (10)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b684_worklist.py')) or ''), 'tools/b684_worklist.py', '5')
    add('ruling (11)', 'the w = 1 split, data/b679_strip_plan.txt == 11', bool(re.search(r'^== 11\b', rd(p('data', 'b679_strip_plan.txt')) or '', re.M))
        and 'splitting D at w = 1' in (rd(p('data', 'b679_strip_plan.txt')) or ''), 'data/b679_strip_plan.txt (the split at :56-:57)', '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '1')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1, the closing a gate step', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''),
        'data/b675_rules.txt :5', '5')
    add('ferry', 'data/b680_rules.txt, binary banks beside a text hashes bank', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''),
        'data/b680_rules.txt row (1)', '4')
    for b in ('b685_readfirst.txt', 'b685_rules.txt', 'b685_p3.txt', 'b685_search.txt', 'b685_count_plan.txt', 'b685_count.txt', 'b685_count_controls.txt',
              'b685_p3_status.txt', 'b685_q0_reread.txt', 'b685_tool_repairs.txt'):
        sz = b == 'b685_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank, written after the check`s first run (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-5')
    return R


def _write(L, R, miss):
    for name, data in (('b685_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b685_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b685 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b685_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b685_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b685_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b685_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), banked == text.rstrip(NL), r.returncode))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b685."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b685'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b685')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b685)', 'exec'), ns)
    ns['answer'](needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b685_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
