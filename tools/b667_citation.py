# -*- coding: utf-8 -*-
"""b667_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b667's step zero; and the ferry banked
after it. Carried from tools/b666_citation.py: the helpers unchanged, the constants and the rows b667's.

### Before the ferry is banked, every path, line, bank, branch, tag, tool and named rule the ruling (R277) and the ferry cite is checked for
### existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not repaired silently;
### the print is banked as data/b667_citation_check.txt and read by the suite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R277) BEGIN'), never from a scratch copy.
### Each cite is a row: (where it is cited, what is cited, the check, the component that cites it). Figures the ruling states about prior
### banks are checked against those banks as well.
### Routes: `python tools/b667_citation.py check` -> data/b667_citation_check.txt (.json);
###         `python tools/b667_citation.py ferry`  -> data/b667_ferry.txt and data/b667_ferry_scan.txt (ferry_scan.py's output, captured).
### Written by the Write tool at b667; this tool writes only the four banks named above.
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
KD = 'D:/SIDE-cosmo'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf.jsonl'
ANCHOR, TAIL = 'RULING (R277) BEGIN', 'FERRY END (part 1 of 1)'
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


def jload(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def grep_line(path, pat):
    t = rd(path) or ''
    for i, l in enumerate(t.split(NL), 1):
        if re.search(pat, l):
            return i, l.strip()
    return None, None


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    # ### the banks the read-first names
    for f in ('data/b666_closing.txt', 'data/b666_defects.txt', 'data/b326_epstein_zeros.json', 'data/b326_offline.json',
              'data/b523_registration_2026-09-25.txt', 'data/b663_epstein_plan.txt', 'data/b663_epstein_control.txt', 'tools/b663_epstein_map.py',
              'data/b627_margin_inputs.txt', 'data/b666_closing_push_out.txt', 'tools/b326_zeros.py', 'tools/b326_offline.py'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-4')
    dft = rd(p('data', 'b666_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-z])\) THE ([\w']+)", dft, re.M)
    add('ruling (1)', '"four defects, all the seat`s"', len(letters) == 4 and all(w == "SEAT'S" for _l, w in letters),
        'data/b666_defects.txt rows: %s' % ', '.join('(%s) %s' % x for x in letters), '1')
    add('ruling (1)', '"(d) a sealed scorer reading an axiom-free print as outside the standard three"',
        'AN EMPTY PRINT READ AS OUTSIDE THE STANDARD THREE' in dft, 'data/b666_defects.txt (d)', '1')
    # ### b666 at its weight
    cl = rd(p('data', 'b666_closing.txt')) or ''
    add('ruling (1)', 'relay d43a72f9, PLACE-papers c143bcb', commit_in(ROOT, 'd43a72f9') and commit_in(PP, 'c143bcb') and 'PLACE-papers c143bcb' in cl,
        'git cat-file; the closing`s head prints "%s"' % cl.split(NL)[0][:100], '1')
    add('ruling (1)', 'merged alone at ca04c8c, tag v0.3.1', g(KD, 'rev-parse', '--short=7', 'v0.3.1^{commit}')[1].strip() == 'ca04c8c', 'v0.3.1 peeled', '1')
    add('ruling (1)', 'main past v0.3 untagged at c5cba30', commit_in(KD, 'c5cba30') and 'c5cba30' in cl, 'git cat-file; data/b666_closing.txt CARRIED (c)', '1')
    for rid in ('38471056772', '38470740945'):
        n_, l_ = grep_line(p('data', 'b666_closing.txt'), 'run %s success' % rid)
        add('ruling (1)', 'run %s' % rid, n_, 'data/b666_closing.txt :%s %s' % (n_, (l_ or '')[-60:]), '1')
    add('ruling (1)', '53 prints, the two banked equal, the rest at the standard three or none', 'TERMINALS 53, PRINTED 53' in cl,
        'data/b666_closing.txt :%s' % grep_line(p('data', 'b666_closing.txt'), 'TERMINALS 53, PRINTED 53')[0], '1')
    for n, needle in ((8619, 'b665 AT ITS WEIGHT'), (8621, 'SIDE-cosmo')):
        l = line(os.path.join(PP, 'FINDINGS.md'), n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in l, l[:100], '1')
    for n, needle in ((14238, 'THE TIE'), (14240, '### b666')):
        l = line(os.path.join(PP, 'OPEN_TRAILS.md'), n) or ''
        add('ruling (1)', 'OPEN_TRAILS :%d' % n, needle in l, l[:100], '1')
    rl = act_root_line('b666')
    add('ruling (1)', 'root d2c4a9d3...', rl and rl[0][1].startswith('d2c4a9d3'), 'data/act_roots.txt b666 line', '1')
    for f in ('b666_checks.txt', 'b666_checks_postpush.txt'):
        ck = rd(p('data', f)) or ''
        add('ruling (1)', 'suite 81 of 81 (%s)' % f, 'LIVE PASSING : 81. ### LIVE FAILING : 0 ' in ck, 'data/%s' % f, '1')
    add('ruling (1)', 'G-AXIOM-CLAIM at 1 before the merge and 0 after', 'G-AXIOM-CLAIM BEFORE: CONTRADICTED 1 ; AFTER: CONTRADICTED 0' in cl,
        'data/b666_closing.txt :%s' % grep_line(p('data', 'b666_closing.txt'), 'G-AXIOM-CLAIM')[0], '1')
    add('ruling (1)', 'the mirror at mirror-refresh-2026-10-13-b666.zip', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-13-b666.zip')
        and 'mirror-refresh-2026-10-13-b666.zip' in cl, 'exists; data/b666_closing.txt :%s' % grep_line(p('data', 'b666_closing.txt'), 'mirror-refresh-2026-10-13-b666')[0], '1')
    add('ruling (1)', '"14 rows, 11 graded and cut"', "{'CUT': 11, 'MATCHES': 3}" in cl, 'data/b666_closing.txt (N3): CUT 11, MATCHES 3 = 14 rows', '1')
    # ### the object: b326's banks, by key and index
    zo, zf = jload('b326_epstein_zeros.json'), jload('b326_offline.json')
    on, off = zo.get('zeros') or [], zf.get('zeros') or []
    add('ruling (2)', '146 on-line ordinates below 150', len(on) == 146 and all(z['agree'] and z['gamma_a'] == z['gamma_b'] < 150 for z in on),
        'data/b326_epstein_zeros.json key "zeros" (:%s): %d rows, index 0..%d, both routes agree, max %s' % (
            grep_line(p('data', 'b326_epstein_zeros.json'), r'^ "zeros"')[0], len(on), len(on) - 1, max(z['gamma_a'] for z in on) if on else '?'), '2-3')
    add('ruling (2)', '17 off-line zeros below 150', len(off) == 17 and zf.get('total_winding') == 17 and all(z['agree'] and z['rho_a'] == z['rho_b'] for z in off),
        'data/b326_offline.json key "zeros" (:%s): %d rows; total_winding %s (:%s); sig_lo %s sig_hi %s box %s nside %s' % (
            grep_line(p('data', 'b326_offline.json'), r'^ "zeros"')[0], len(off), zf.get('total_winding'),
            grep_line(p('data', 'b326_offline.json'), r'"total_winding"')[0], zf.get('sig_lo'), zf.get('sig_hi'), zf.get('box'), zf.get('nside')), '2-3')
    add('ruling (2)', 'banked at 119 digits, registered_gate_passed = False', zo.get('dps') == 119 and zf.get('dps') == 119 and zo.get('registered_gate_passed') is False,
        'data/b326_epstein_zeros.json :%s dps %s, :%s registered_gate_passed %s (dps_registered %s); b326_offline.json dps %s; K %s/%s' % (
            grep_line(p('data', 'b326_epstein_zeros.json'), r'"dps"')[0], zo.get('dps'), grep_line(p('data', 'b326_epstein_zeros.json'), r'registered_gate_passed')[0],
            zo.get('registered_gate_passed'), zo.get('dps_registered'), zf.get('dps'), zo.get('K'), zf.get('K')), '2')
    add('ferry read-first', 'the generating banks', 'b326_epstein_zeros.json' in (rd(p('tools', 'b326_zeros.py')) or '') and 'b326_offline.json' in (rd(p('tools', 'b326_offline.py')) or ''),
        'tools/b326_zeros.py :%s (OUT) and :%s (registered_gate_passed); tools/b326_offline.py :%s (OUT)' % (
            grep_line(p('tools', 'b326_zeros.py'), r'^OUT = ')[0], grep_line(p('tools', 'b326_zeros.py'), r'registered_gate_passed')[0],
            grep_line(p('tools', 'b326_offline.py'), r'^OUT = ')[0]), '2')
    l62 = line(p('data', 'b523_registration_2026-09-25.txt'), 62) or ''
    add('ferry read-first', 'b523 :62 (the form)', '146 on-line, 17 off-line pairs' in l62 and 'x^2 + xy + 6y^2' in l62, l62[:110], '2')
    pl = rd(p('data', 'b663_epstein_plan.txt')) or ''
    add('ferry read-first', 'the b663 plan`s count by orbit and pair', '-- 292 points' in pl and '-- 68 points' in pl and 'In all 360 points' in pl,
        'data/b663_epstein_plan.txt :%s (146 ordinates, 1/2 ± iγ, 292 points), :%s (17 orbits of four, 68 points; 360 in all)' % (
            grep_line(p('data', 'b663_epstein_plan.txt'), '-- 292 points')[0], grep_line(p('data', 'b663_epstein_plan.txt'), '-- 68 points')[0]), '2')
    ct = rd(p('data', 'b663_epstein_control.txt')) or ''
    add('ruling (2); (6)', 'the b663 control`s remaining caveat (banked, not ball-certified)', 'until W-ORD-EPSTEIN-CERTIFY (b667)' in ct,
        'data/b663_epstein_control.txt :%s (b665`s dated line)' % grep_line(p('data', 'b663_epstein_control.txt'), 'until W-ORD-EPSTEIN-CERTIFY')[0], '5')
    mp = rd(p('tools', 'b663_epstein_map.py')) or ''
    cfg = [(grep_line(p('tools', 'b663_epstein_map.py'), '^%s' % k)[0], k) for k in ('PREC = ', 'PREC_RUNG = ', 'Q0_ON, Q0_OFF = ', 'Q0_T = ', 'Q0_BASE = ', 'Q0_A0 = ')]
    add('ferry read-first', 'tools/b663_epstein_map.py configuration lines', all(n for n, _k in cfg) and 'def q0_list' in mp,
        ' ; '.join(':%s %s' % (n, k.strip(' =,')) for n, k in cfg) + ' ; q0_list :%s (the decimal literals)' % grep_line(p('tools', 'b663_epstein_map.py'), r'^def q0_list')[0], '4')
    mi = line(p('data', 'b627_margin_inputs.txt'), 7) or ''
    add('ferry read-first; ruling (3)', 'the b627 precision bank: 200 bits', 'Arb balls at 200 bits' in mi, 'data/b627_margin_inputs.txt :7 %s' % mi[:90], '3')
    add('ruling (3)', '200 bits with the 400-bit rung', 'PREC_RUNG = 400' in mp, 'tools/b663_epstein_map.py :29', '3')
    try:
        import flint
        from flint import acb, arb
        fns = [n for n in ('gamma', 'gamma_upper', 'rgamma', 'zeta', 'exp', 'integral', 'zeta_zero', 'zeta_zeros', 'zeta_nzeros', 'dirichlet_l', 'modular_theta')
               if hasattr(acb, n) or hasattr(arb, n)]
        add('ferry read-first', 'Arb`s documentation by function name (python-flint)', flint.__version__ == '0.9.0' and len(fns) == 11,
            'python-flint %s: %s present (the route`s own functions named in the plan)' % (flint.__version__, ', '.join(fns)), '2-3')
    except Exception as e:
        add('ferry read-first', 'python-flint', False, repr(e), '2-3')
    al, _ = grep_line(os.path.join(PP, 'OPEN_TRAILS.md'), r'^### `W-ORD-EPSTEIN-CERTIFY`')
    add('ruling (6)', 'W-ORD-EPSTEIN-CERTIFY on OPEN_TRAILS', al == 14158, 'OPEN_TRAILS :%s (placed :14188 by b664)' % al, '5')
    add('ruling (6)', 'the kernel`s EpsteinQ0.lean (untouched)', g(EF, 'cat-file', '-e', 'main:SIDEExplicitFormula/Schema/EpsteinQ0.lean')[0] == 0,
        'SIDE-explicit-formula main:SIDEExplicitFormula/Schema/EpsteinQ0.lean', '5')
    add('ruling (7)', 'the draft at v5, held', 'v5' in cl and '23228113' in cl, 'data/b666_closing.txt (N5): draft 23228113, v5, unsubmitted', '6')
    # ### branches for step zero
    for repo, nm, b in ((ROOT, 'relay', 'push-b666'), (ROOT, 'relay', 'push-b666-root'), (ROOT, 'relay', 'push-b666-closing'),
                        (PP, 'PLACE-papers', 'push-b666'), (PP, 'PLACE-papers', 'push-b666-root'),
                        (KD, 'SIDE-cosmo', 'push-b666-workflow'), (KD, 'SIDE-cosmo', 'push-b666-merge'), (KD, 'SIDE-cosmo', 'docstrings-cut-SIDE-cosmo')):
        add('ferry Component 0', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    # ### rules and tools
    for rule, cl_, comp in (('R265', (2, 3, 4), '7'), ('R251', (3,), '7'), ('R254', (2,), '0-5')):
        ok, how = rule_clause(rule, cl_)
        add('ruling (8); ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    for f in ('tools/push_gated.sh', 'tools/act_root.py', 'tools/additive_shared.py', 'tools/ferry_scan.py'):
        add('ferry', f, os.path.exists(p(*f.split('/'))), 'exists', '0-7')
    return R


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b667 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    for name, data in (('b667_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b667_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    text = ferry_text()
    q = os.path.join(D, 'b667_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b667_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b667_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b667_citation.py check | ferry')
        sys.exit(2)
    fn(*sys.argv[2:])
