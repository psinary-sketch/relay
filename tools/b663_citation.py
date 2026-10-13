# -*- coding: utf-8 -*-
"""b663_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b663's step zero; and the ferry
banked after it. Carried whole from tools/b662_citation.py: the helpers unchanged, the constants and the rows b663's.

### Before the ferry is banked, every path, line, bank, branch, tag, tool and named rule the ruling (R273) and the ferry cite is
### checked for existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not
### repaired silently; the print is banked as data/b663_citation_check.txt and read by the suite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R273) BEGIN'), never from a scratch copy.
### Each cite is a row: (where it is cited, what is cited, the check, the component that cites it). Figures the ruling states about prior
### banks are checked against those banks as well (a figure is a citation of a bank's content).
### Routes: `python tools/b663_citation.py check` -> data/b663_citation_check.txt (.json);
###         `python tools/b663_citation.py ferry`  -> data/b663_ferry.txt and data/b663_ferry_scan.txt (ferry_scan.py's output, captured).
### Written by the Write tool at b663; this tool writes only the four banks named above.
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
EF = 'D:/SIDE-explicit-formula'
CS = 'D:/SIDE-carrier-spec'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf.jsonl'
ANCHOR, TAIL = 'RULING (R273) BEGIN', 'FERRY END (part 1 of 1)'
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


def ferry_text():
    """the ruling and the ferry as pasted: the last user line of the session carrying the anchor, from the anchor to the ferry's end."""
    best = None
    for raw in io.open(SESSION, encoding='utf-8', errors='replace'):
        if ANCHOR not in raw:
            continue
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if o.get('type') != 'user' or o.get('isCompactSummary'):
            continue
        cs = (o.get('message') or {}).get('content')
        texts = [cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']
        for t in texts:
            i, j = t.find(ANCHOR), t.find(TAIL)
            if i >= 0 and j > i:
                best = t[i:j + len(TAIL)].replace(chr(13), '')
    if best is None:
        sys.exit('### THE RULING IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    return best


def commit_in(repo, sha):
    rc, _o = g(repo, 'cat-file', '-e', sha + '^{commit}')
    return rc == 0


def branch_listed(repo, b):
    rc, o = g(repo, 'branch', '--list', b)
    return bool(o.strip())


def rule_clause(rule, clauses):
    """a named rule's clauses in the ferry bank that carries its ruling."""
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


def mapj():
    try:
        return json.load(io.open(os.path.join(D, 'b662_detection_map_40.json'), encoding='utf-8'))['cells']
    except Exception:
        return []


def by_t(key):
    out = []
    for tt in ('14.1', '29.6', '50.0', '100.0'):
        out.append(sorted(set(c.get(key) for c in mapj() if c.get('t') == tt)))
    return out


def kgrep(rev, pat, path):
    rc, o = g(EF, 'grep', '-n', '-E', pat, rev, '--', path)
    return [l for l in o.split(NL) if l.strip()]


def jload(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    # ### the banks and files the read-first names
    for f in ('data/b662_closing.txt', 'data/b662_defects.txt', 'data/b642_epstein_rungs.txt', 'data/b662_closing_push_out.txt',
              'tools/b662_map.py', 'data/b662_detection_map_40.txt', 'data/b661_e1cfg_binding.txt', 'tools/e0_rule.py'):
        add('ferry read-first / ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-4')
    dft = rd(p('data', 'b662_defects.txt')) or ''
    letters = re.findall(r'^    \(([a-z])\) ', dft, re.M)
    add('ferry read-first', 'data/b662_defects.txt (a)-(e) and the seat`s late defect', letters == list('abcde'),
        'the bank`s lettered rows: (%s) -- %d rows, (a)-(d) the navigator`s, (e)-(h) the seat`s; "(a)-(e)" names five of eight' % (
            ')('.join(letters), len(letters)), '0')
    # ### OPEN_TRAILS :13533 and the rungs
    o33 = line(os.path.join(PP, 'OPEN_TRAILS.md'), 13533) or ''
    add('ruling (3), ferry read-first', 'OPEN_TRAILS :13533', 'W-ORD-EPSTEIN-ZQ' in o33 and 'b642_epstein_rungs' in o33, o33[:110], '2')
    rg = rd(p('data', 'b642_epstein_rungs.txt')) or ''
    add('ruling (3)', 'data/b642_epstein_rungs.txt, rows are rungs', re.findall(r'^== (R\d) ', rg, re.M) == ['R1', 'R2', 'R3', 'R4', 'R5'],
        'rungs %s ; :184 the read price "EIGHT ACTS AT THE LEAST"' % ' '.join(re.findall(r'^== (R\d) ', rg, re.M)), '2')
    add('ruling (2)', '"Mathlib carries no Epstein zeta function"', '-- Epstein, anywhere : 0 hit(s)' in rg, 'data/b642_epstein_rungs.txt :14', '2')
    # ### the Q0 banks: the form, the zero list, the off-line zero
    z = jload('b326_epstein_zeros.json')
    off = jload('b326_offline.json')
    q0b = [f for f in sorted(os.listdir(D)) if re.match(r'b54[89]_', f)]
    hold = []
    for f in q0b:
        ls = (rd(os.path.join(D, f)) or '').split(NL) if f.endswith(('.txt', '.jsonl')) else []
        hit = [i for i, l in enumerate(ls, 1) if re.search(r'29\.5517|16\.2902', l)]
        if hit:
            hold.append('%s :%d (%d line(s))' % (f, hit[0], len(hit)))
    add('ferry read-first', 'the b548/b549 bench banks for Q0 -- the certified zero list with heights, the off-line zero`s σ and t, by line',
        False, 'of %d b548/b549 banks, the text banks MENTIONING an off-line ordinate: %s; of these data/b548_interference.jsonl :1 carries '
        'HEIGHTS ONLY as its terms (146 "on" ordinates, 16 "off" ordinates; the 17th, 16.290, as its "pair"), no σ and no ball; b549 none; '
        'b548 READS the list (data/b548_reads.txt :307 "the Q0 bank: '
        '146 on-line ordinates (last 149.718008), 17 off-line zeros"; :167 b326_epstein_zeros.json); the list is b326`s: '
        'data/b326_epstein_zeros.json (zeros %d, T %s) and data/b326_offline.json (zeros %d, σ in [%s, %s], T %s)' % (
            len(q0b), hold or 'none', len(z.get('zeros', [])), z.get('T'), len(off.get('zeros', [])), off.get('sig_lo'), off.get('sig_hi'),
            off.get('T')), '2')
    add('ruling (2)', '"the discriminant −23 form ... x^2 + xy + 6y^2"', '6y^2' in (rd(p('data', 'b523_registration_2026-09-25.txt')) or ''),
        'data/b523_registration_2026-09-25.txt :62 (b325`s form header, h(-23) = 3)', '2')
    add('ruling (2)', '"its certified off-line zero as those banks record it" (one zero, certified)', False,
        'data/b326_offline.json holds %d off-line zeros with σ > 1/2 below T = %s (each by two routes, agree; mpmath at dps %s with '
        'winding counts, not ball arithmetic); data/b326_epstein_zeros.json prints registered_gate_passed = %s; the one off-line zero the '
        'kernel names is b590`s rhoE = 0.7979971571786801 + 29.551761098629115 i (Schema/Epstein.lean :32, from data/b506_c2_results.json)' % (
            len(off.get('zeros', [])), off.get('T'), off.get('dps'), z.get('registered_gate_passed')), '2-4')
    # ### the kernel at v0.28 and main
    rc, km = g(EF, 'rev-parse', '--short=7', 'main')
    rc2, tv = g(EF, 'rev-parse', '--short=7', 'v0.28^{commit}')
    add('ferry read-first', 'SIDE-explicit-formula at v0.28', rc2 == 0, 'v0.28 at %s ; main %s' % (tv.strip(), km.strip()), '2-3')
    for path, pat, what in (('SIDEExplicitFormula/Schema/Config.lean', r'^structure WeilConfig', "Config.lean's WeilConfig"),
                            ('SIDEExplicitFormula/Schema/Instances.lean', r'^def zetaWeilConfig', 'Instances.lean :25 (ζ`s instance)'),
                            ('SIDEExplicitFormula/Schema/RateIndexCfg.lean', r'^theorem zeroSide_neg_at_rate_cfg ', 'Schema/RateIndexCfg.lean'),
                            ('SIDEExplicitFormula/Schema/Converse.lean', r'^theorem zeroSide_eventually_neg_cfg', "Converse.lean's _cfg detector")):
        h = kgrep('v0.28', pat, path)
        ok = bool(h) and (what != 'Instances.lean :25 (ζ`s instance)' or ':25:' in h[0])
        add('ferry read-first', what, ok, h[0].split(':', 1)[1][:110] if h else 'no hit', '2-4')
    for tag, pat, what in (('v0.15', r'^theorem h2_sign_cfg_iff_target', 'h2_sign_cfg_iff_target, v0.15'),
                           ('v0.28', r'^theorem zeroSide_neg_at_rate_cfg ', 'zeroSide_neg_at_rate_cfg, v0.28')):
        add('ruling (2)', what, bool(kgrep(tag, pat, 'SIDEExplicitFormula')), 'present at %s' % tag, '2-4')
    add('ruling (2)', 'zeroSide_eventually_neg_cfg, v0.28', bool(kgrep('v0.15', r'^theorem zeroSide_eventually_neg_cfg', 'SIDEExplicitFormula')),
        'present at v0.28 and already at v0.15 (Converse.lean :161)', '2-4')
    # ### the instance the ruling describes as to be built
    ep = kgrep('main', r'^(def|theorem|structure) ', 'SIDEExplicitFormula/Schema/Epstein.lean')
    add('ruling (2)-(3), (5); ferry Component 3', '"THE EPSTEIN CONFIGURATION BUILT WITH ITS EXPLICIT FORMULA AS A NAMED PREMISE"', not ep,
        'SIDE-explicit-formula main carries SIDEExplicitFormula/Schema/Epstein.lean since v0.16 (c404e72, b590, (R200)(4)(b)): %s; '
        'the premises are a Prop structure over an abstract Z and rhs, the points not entered as data; OPEN_TRAILS :13436 '
        'W-ORD-PREMISE-EPSTEINPREMISES; FINDINGS :6746 -- the ruling and ferry do not name it' % ' ; '.join(
            l.split(':', 2)[2][:40] + ' :' + l.split(':')[1] for l in ep[:6]), '2-5')
    add('ferry Component 3', 'branch epstein-b663 (to be made)', not branch_listed(EF, 'epstein-b663'), 'absent, as it should be', '3')
    add('ferry Component 3', 'the workflow and print_targets.txt on EF main', g(EF, 'cat-file', '-e', 'main:.github/workflows/build-module.yml')[0] == 0
        and g(EF, 'cat-file', '-e', 'main:print_targets.txt')[0] == 0, 'both present at main', '3')
    rc, tg = g(EF, 'tag', '--list', 'v0.*')
    add('ferry Component 5', 'the tag at the next in the series', 'v0.28' in tg.split() and 'v0.29' not in tg.split(), 'last v0.28 ; next v0.29', '5')
    add('ruling (5), ferry Component 3, N3', '"the premises\' profiles printed as INTERFACES"', False,
        '#print axioms prints an axiom list, never a grade: INTERFACES is the E0 grade of tools/e0_rule.py (a theorem whose explicit '
        'binder is a named Prop); b590 printed 35 declarations at the standard three and graded INTERFACES by that rule '
        '(data/b590_e0_epstein.txt) -- read as "the E0 grade INTERFACES beside an axiom print at the standard three"?', '3')
    # ### the b662 script
    mp = rd(p('tools', 'b662_map.py')) or ''
    for nm, pat in (('J_max = D + 40', r'^J_EXTRA = 40\b'), ('Arb at 200 bits', r'^PREC = 200\b'), ('the 400-bit rung', r'^PREC_RUNG = 400\b')):
        m = re.search(pat, mp, re.M)
        add('ruling (4)', nm, m, 'tools/b662_map.py :%d' % (mp[:m.start()].count(NL) + 1) if m else 'absent', '4')
    # ### figures the ruling states about b662
    add('ruling (1)', 'j₀ = 28, 31, 44, 84 at t = 14.1, 29.6, 50, 100', by_t('j0') == [[28], [31], [44], [84]], 'the map json: %s' % by_t('j0'), '1')
    ar = rd(p('data', 'b662_additive_rerun.txt')) or ''
    add('ruling (1)', 'G-SHARED-ADDITIVE at 0 of 8', len(re.findall(r'ADDITIVE$', ar, re.M)) == 8 and 'READS 8 ; NOT ADDITIVE 0.' in ar,
        'data/b662_additive_rerun.txt: 8 reads ADDITIVE; data/b662_closing.txt :20 NOT ADDITIVE 0', '1')
    gr = rd(p('data', 'b662_sentence_grades.txt')) or ''
    add('ruling (1)', 'the "DERIVES." label removed on the cell`s VACUOUS', 'OVERREACHES DERIVES.' in gr and 'the theorem is VACUOUS' in gr,
        'data/b662_sentence_grades.txt :74-:75', '1')
    cl = rd(p('data', 'b662_closing.txt')) or ''
    for fig in ('SENTENCE ROWS 54', 'GRADED 12', 'BLOCKS TO CUT 9 IN 4 FILES'):
        add('ruling (1)', fig, fig in cl, 'data/b662_closing.txt', '1')
    ck = rd(p('data', 'b662_checks_postpush.txt')) or ''
    add('ruling (1)', 'suite 79 of 81, G-MERGES-ON-GATE and G-AXIOM-CLAIM declared',
        "LIVE PASSING : 79" in ck and "['G-MERGES-ON-GATE', 'G-AXIOM-CLAIM']" in ck, 'data/b662_checks_postpush.txt', '1')
    add('ruling (1)', 'run 38370416643, 27 profiles', '38370416643' in (rd(p('data', 'b662_runner_SIDE-carrier-spec.txt')) or ''),
        'data/b662_runner_SIDE-carrier-spec.txt', '1')
    mr = rd(p('data', 'b662_mirror.txt')) or ''
    add('ruling (1)', 'mirror-refresh-2026-10-13-b662.zip (md5 a888b7af...)', 'mirror-refresh-2026-10-13-b662.zip' in mr and 'a888b7af' in mr,
        'data/b662_mirror.txt', '1')
    for repo, sha, what in ((ROOT, '51838723', 'relay 51838723'), (PP, '16be102', 'PLACE-papers 16be102'), (CS, 'dd54a61', 'SIDE-carrier-spec dd54a61')):
        add('ruling (1)', what, commit_in(repo, sha), 'git cat-file', '1')
    rc, pv = g(CS, 'rev-parse', '--short=7', 'v0.4.2^{commit}')
    add('ruling (1)', 'tag v0.4.2', pv.strip() == 'dd54a61', 'peeled %s' % pv.strip(), '1')
    rl = act_root_line('b662')
    add('ruling (1)', 'root 769efd11...', rl and rl[0][1].startswith('769efd11'), 'data/act_roots.txt b662 line', '1')
    for n, needle in ((8507, 'b661 AT ITS WEIGHT'), (8509, '## SIDE-carrier-spec')):
        l = line(os.path.join(PP, 'FINDINGS.md'), n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in l, l[:90], '1')
    for n, needle in ((14132, 'W-ORD-E2-SEPARATION'), (14136, 'W-ORD-CITATION-CHECK ACTED'), (14138, '### b662')):
        l = line(os.path.join(PP, 'OPEN_TRAILS.md'), n) or ''
        add('ruling (1)', 'OPEN_TRAILS :%d' % n, needle in l, l[:90], '1')
    # ### branches for step zero
    for repo, nm, b in ((ROOT, 'relay', 'push-b662'), (ROOT, 'relay', 'push-b662-root'), (ROOT, 'relay', 'push-b662-root-table'),
                        (ROOT, 'relay', 'push-b662-closing'), (PP, 'PLACE-papers', 'push-b662'), (PP, 'PLACE-papers', 'push-b662-root'),
                        (CS, 'SIDE-carrier-spec', 'push-b662-workflow'), (CS, 'SIDE-carrier-spec', 'push-b662-merge'),
                        (CS, 'SIDE-carrier-spec', 'docstrings-cut-SIDE-carrier-spec')):
        add('ferry Component 0', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    # ### rules and tools
    for rule, cl_, comp in (('R265', (2, 3, 4), '7'), ('R251', (3,), '7'), ('R254', (2,), '0-7')):
        ok, how = rule_clause(rule, cl_)
        add('ruling (7); ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    for f in ('tools/push_gated.sh', 'tools/act_root.py', 'tools/additive_shared.py', 'tools/ferry_scan.py'):
        add('ferry', f, os.path.exists(p(*f.split('/'))), 'exists', '0-7')
    return R


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b663 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    for name, data in (('b663_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b663_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    text = ferry_text()
    q = os.path.join(D, 'b663_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT,
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    s = os.path.join(D, 'b663_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b663_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b663_citation.py check | ferry')
        sys.exit(2)
    fn(*sys.argv[2:])
