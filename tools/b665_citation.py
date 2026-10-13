# -*- coding: utf-8 -*-
"""b665_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b665's step zero; and the ferry banked
after it. Carried from tools/b664_citation.py: the helpers unchanged, the constants and the rows b665's.

### Before the ferry is banked, every path, line, bank, branch, tag, tool, Mathlib name and named rule the ruling (R275) and the ferry cite is
### checked for existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not
### repaired silently; the print is banked as data/b665_citation_check.txt and read by the suite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R275) BEGIN'), never from a scratch copy.
### Each cite is a row: (where it is cited, what is cited, the check, the component that cites it). Figures the ruling states about prior
### banks are checked against those banks as well (a figure is a citation of a bank's content); a formula the ruling quotes from a bank is
### checked against the bank's own words.
### Routes: `python tools/b665_citation.py check` -> data/b665_citation_check.txt (.json);
###         `python tools/b665_citation.py ferry`  -> data/b665_ferry.txt and data/b665_ferry_scan.txt (ferry_scan.py's output, captured).
### Written by the Write tool at b665; this tool writes only the four banks named above.
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
KD = 'D:/SIDE-effects'
ML = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf.jsonl'
ANCHOR, TAIL = 'RULING (R275) BEGIN', 'FERRY END (part 1 of 1)'
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


def blob_line(repo, rev, path, n):
    rc, o = g(repo, 'show', '%s:%s' % (rev, path))
    ls = o.split(NL) if rc == 0 else []
    return ls[n - 1] if 0 < n <= len(ls) else ''


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    # ### the banks the read-first names
    for f in ('data/b664_closing.txt', 'data/b664_defects.txt', 'data/b589_three_way.txt', 'data/b589_keiper_read.txt',
              'data/b663_epstein_control.txt', 'data/b663_epstein_plan.txt', 'data/b664_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-4')
    dft = rd(p('data', 'b664_defects.txt')) or ''
    letters = re.findall(r'^    \(([a-z]|b663-late)\) ', dft, re.M)
    add('ruling (1)', '"five defects, (a) and (b) the navigator`s"', len(letters) == 5 and "(a) THE NAVIGATOR'S" in dft and "(b) THE NAVIGATOR'S" in dft,
        'data/b664_defects.txt rows: (%s) -- %d rows' % (')('.join(letters), len(letters)), '1')
    # ### b664 at its weight: figures against the closing and the repositories
    cl = rd(p('data', 'b664_closing.txt')) or ''
    add('ruling (1)', 'relay efdd9309', commit_in(ROOT, 'efdd9309'), 'git cat-file; the closing`s head prints the record commit "relay 05bf7a5b" '
        '(%s), efdd9309 is the closing`s own commit' % ('relay 05bf7a5b' in cl.split(NL)[0]), '1')
    add('ruling (1)', 'PLACE-papers b1a2bab', commit_in(PP, 'b1a2bab') and 'PLACE-papers b1a2bab' in cl, 'git cat-file; the closing`s head', '1')
    for n, needle in ((8561, 'b663'), (8563, "SIDE-effects")):
        l = line(os.path.join(PP, 'FINDINGS.md'), n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in l, l[:90], '1')
    for n, needle in ((14186, 'transform'), (14188, 'W-ORD-EPSTEIN-CERTIFY'), (14190, 'A KERNEL FILE IS READ'), (14194, '### b664')):
        l = line(os.path.join(PP, 'OPEN_TRAILS.md'), n) or ''
        add('ruling (1)', 'OPEN_TRAILS :%d (of :14186-:14194)' % n, needle.lower() in l.lower(), l[:90], '1')
    rl = act_root_line('b664')
    aj = jload('b664_act_root.json')
    nb = len((aj.get('reads') or {}).get('banks') or [])
    add('ruling (1)', 'root 1bd81723... over 46 banks', rl and rl[0][1].startswith('1bd81723') and nb == 46, 'data/act_roots.txt b664 line ; banks %d' % nb, '1')
    ck = rd(p('data', 'b664_checks_postpush.txt')) or ''
    add('ruling (1)', 'suite 82 of 83, the SIDE-cosmo row alone declared', 'LIVE PASSING : 82' in ck and "LIVE FAILING : 1 ['G-AXIOM-CLAIM']" in ck,
        'data/b664_checks_postpush.txt', '1')
    kt = rd(p('data', 'b647_table_kernels.txt')) or ''
    add('ruling (1)', 'SIDE-effects 7 at b647_table_kernels.txt :10', 'SIDE-effects' in (line(p('data', 'b647_table_kernels.txt'), 10) or ''),
        (line(p('data', 'b647_table_kernels.txt'), 10) or '')[:90], '1')
    add('ruling (1)', 'SIDE-effects main moved to 9a279ac (at b664`s read); merged 78bbcff, tag v0.1.1', commit_in(KD, '9a279ac') and commit_in(KD, '78bbcff')
        and g(KD, 'rev-parse', '--short=7', 'v0.1.1^{commit}')[1].strip() == '78bbcff', 'git cat-file ; v0.1.1 peeled', '1')
    cut = jload('b664_cut_SIDE-effects.json')
    add('ruling (1)', '2 blocks into 20 rows, 4 OVERREACHES cut in one commit', (cut.get('cut_commits') == 1), 'data/b664_cut_SIDE-effects.json cut_commits %s' % cut.get('cut_commits'), '1')
    rb = rd(p('data', 'b664_runner_SIDE-effects.txt')) or ''
    add('ruling (1)', 'run 38431820497 with 34 prints at the standard three or none', '38431820497' in rb and os.path.exists(p('data', 'b664_prints_SIDE-effects.txt')),
        'data/b664_runner_SIDE-effects.txt, data/b664_prints_SIDE-effects.txt', '1')
    for n, needle in ((28, 'Axiom-free'), (103, '0 axioms beyond ZFC')):
        l = blob_line(KD, 'main', 'README.md', n)
        add('ruling (1)', 'SIDE-effects README :%d "%s"' % (n, needle), needle in l, l[:90], '1')
    add('ruling (1)', 'the mirror at mirror-refresh-2026-10-13-b664.zip', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-13-b664.zip'), 'exists', '1')
    # ### the kernel: tags, the K-identities, the Li lemma, the window
    rc, mainv = g(EF, 'rev-parse', '--short=7', 'main')
    rc, v29 = g(EF, 'rev-parse', '--short=7', 'v0.29^{commit}')
    add('ferry read-first', 'SIDE-explicit-formula at v0.29', mainv.strip() == v29.strip() == 'd00ab16', 'main %s ; v0.29 %s' % (mainv.strip(), v29.strip()), '2-3')
    rc, first = g(EF, 'log', '--reverse', '--format=%h', '--', 'SIDEExplicitFormula/KeiperIdentities.lean')
    f0 = (first.split() or ['?'])[0]
    rc, cont = g(EF, 'tag', '--contains', f0)
    tags = sorted(cont.split(), key=lambda t: [int(x) for x in re.findall(r'\d+', t)])
    ki = [(n, grep_line(os.path.join(EF, 'SIDEExplicitFormula', 'KeiperIdentities.lean'), r'^theorem %s\b' % n)[0])
          for n in ('binomialTransform_holds', 'logDerivSplit_holds', 'stieltjesLog_holds')]
    add('ruling (2)', 'the K1-K3 identities at v0.26', tags[:1] == ['v0.26'] and all(x for _n, x in ki),
        'K1-K3 = KeiperObligations` binomial, split, stieltjesLog (relay data/b641_keiper_status.txt (K1)-(K3)); proved at KeiperIdentities.lean %s, '
        'first carried by tag %s (commit %s); K4 GammaRZetaValues OPEN' % (', '.join('%s :%s' % kv for kv in ki), tags[:1], f0), '2')
    n1, _l = grep_line(os.path.join(EF, 'SIDEExplicitFormula', 'LiCriterionBridge.lean'), r'^theorem li_coeff_eq_taylorCoeff\b')
    rc, lfirst = g(EF, 'log', '--reverse', '--format=%h', '-S', 'theorem li_coeff_eq_taylorCoeff', '--', 'SIDEExplicitFormula/LiCriterionBridge.lean')
    rc, lcont = g(EF, 'tag', '--contains', (lfirst.split() or ['?'])[0])
    ltags = sorted(lcont.split(), key=lambda t: [int(x) for x in re.findall(r'\d+', t)])
    n2, _l = grep_line(os.path.join(EF, 'SIDEExplicitFormula', 'LiWeil.lean'), r'^def LiCoeff\b')
    add('ruling (2)', 'li_coeff_eq_taylorCoeff at v0.9 and LiCoeff', n1 and n2 and ltags[:1] == ['v0.9'],
        'LiCriterionBridge.lean :%s (LiCoeff (n + 1) = (taylorCoeff riemannXi n).re), first tag %s ; LiCoeff LiWeil.lean :%s' % (n1, ltags[:1], n2), '2')
    kk = [(n, grep_line(os.path.join(EF, 'SIDEExplicitFormula', 'Keiper.lean'), r'^(theorem|def) %s\b' % n)[0])
          for n in ('stieltjes', 'keiperA', 'keiperSum', 'KeiperTaylor', 'keiperTaylorIdentity_of', 'liCoeff_one_keiper')]
    add('ruling (2)', 'the Keiper expression`s names in the kernel (b601`s Keiper.lean)', all(x for _n, x in kk),
        ', '.join('%s :%s' % kv for kv in kk) + ' -- the Stieltjes constants already a kernel definition by derivative (stieltjes n := (-1)^n riemannZeta₀^(n)(1)), not by a series', '2')
    tw = rd(p('data', 'b589_three_way.txt')) or ''
    add('ruling (2)', 'the b589 three-way bench (zero sum, arithmetic limit, Keiper, n <= 12, 36/36)', '36 comparisons, 0 misses' in tw and 'H30a HOLDS' in tw,
        'data/b589_three_way.txt (rows are n = 1..12, the three values with their floors; Keiper floor 1e-45)', '2, 4')
    kr = rd(p('data', 'b589_keiper_read.txt')) or ''
    add('ruling (2)', 'the b589 pricing: riemannZeta_residue_one and γ present at de5ce8a9, no higher Stieltjes constant by name',
        'riemannZeta_residue_one' in kr and 'THE PRICE, TWO LEMMAS OF SUBSTANCE' in kr,
        'data/b589_keiper_read.txt :%s (READ: riemannZeta_residue_one :242, tendsto_riemannZeta_sub_one_div :342) and :%s (THE PRICE, TWO LEMMAS: (1) the Keiper-Taylor '
        'identity, (2) computable two-sided bounds) -- the ruling`s "the two lemmas b589 priced" read against the bank: b589`s two priced lemmas are '
        '(1) and (2), the two Mathlib lemmas it found present are another pair' % (grep_line(p('data', 'b589_keiper_read.txt'), r'^    READ: ')[0],
                                                                                      grep_line(p('data', 'b589_keiper_read.txt'), r'THE PRICE, TWO LEMMAS')[0]), '2')
    rc, mh = g(ML, 'rev-parse', '--short=8', 'HEAD')
    m1, _l = grep_line(os.path.join(ML, 'Mathlib', 'NumberTheory', 'LSeries', 'RiemannZeta.lean'), r'^lemma riemannZeta_residue_one\b')
    m2, _l = grep_line(os.path.join(ML, 'Mathlib', 'NumberTheory', 'Harmonic', 'EulerMascheroni.lean'), r'def eulerMascheroniConstant\b')
    add('ferry read-first', 'Mathlib at de5ce8a9: riemannZeta_residue_one and the Euler-Mascheroni constant by name', mh.strip() == 'de5ce8a9' and m1 and m2,
        'HEAD %s ; RiemannZeta.lean :%s ; EulerMascheroni.lean :%s (Real.eulerMascheroniConstant)' % (mh.strip(), m1, m2), '2')
    # ### the transform bound: B1, the window, the order
    pl = rd(p('data', 'b663_epstein_plan.txt')) or ''
    add('ruling (3)', 'B1 "as b663`s bank wrote it -- the window transform bounded by 2e^{ℓ/2}/|z| by one integration by parts"',
        '2 e^{ℓ/2}/|z|' in pl or '2 e^{ℓ/2} / |z|' in pl,
        'data/b663_epstein_plan.txt :%s writes the form 2 e^{ℓ/2}/|z| with |Im z| ≤ 1/2 beside it; :%s writes B1 at strip points as offScore g0 ρ ≤ '
        '2 e^{ℓ/2} / |Im ρ|, derived at :%s from |paperFT g0 z| ≤ 2 e^{ℓ |Im z|} / |z| (:%s)' % (
            grep_line(p('data', 'b663_epstein_plan.txt'), r'2 e\^\{ℓ/2\}/\|z\|')[0],
            grep_line(p('data', 'b663_epstein_plan.txt'), r'offScore g0 ρ = ')[0], grep_line(p('data', 'b663_epstein_plan.txt'), r'^   DERIVATION')[0],
            grep_line(p('data', 'b663_epstein_plan.txt'), r'so \|paperFT g0 z\| ≤ 2 e')[0]), '2-3')
    ct = rd(p('data', 'b663_epstein_control.txt')) or ''
    add('ferry read-first', 'b663`s control: the hθ line and B1`s line', 'certified on B1 (READ), not a kernel lemma' in ct,
        'data/b663_epstein_control.txt :%s (B1), :%s (hθ at Q0)' % (grep_line(p('data', 'b663_epstein_control.txt'), r'^  B1 ')[0],
                                                                     [i for i, l in enumerate(ct.split(NL), 1) if l.startswith('  hθ ')][-1:]), '2-4')
    dl = blob_line(EF, 'main', 'SIDEExplicitFormula/Schema/Detector.lean', 33)
    db, _l = grep_line(os.path.join(EF, 'SIDEExplicitFormula', 'Schema', 'Detector.lean'), r'^def detectorBase\b')
    pv, _l = grep_line(os.path.join(EF, 'SIDEExplicitFormula', 'TwoPropertyWindow.lean'), r'^def plateau\b')
    add('ferry read-first', 'Detector.lean :33 and the detector base, its window with ℓ', 'baseWidth' in dl and db and pv,
        'Detector.lean :33 %s ; detectorBase :%s = plateau (1/2) (baseWidth ρ) ; plateau TwoPropertyWindow.lean :%s (support [-L, L], half-width L)' % (dl.strip()[:60], db, pv), '2-3')
    pw, _l = grep_line(os.path.join(EF, 'SIDEExplicitFormula', 'PowerLimit.lean'), r'hsA')
    add('ruling (3)', 'the kernel`s fourth-order bound beside (PowerLimit.lean :825)', 'hsA' in blob_line(EF, 'main', 'SIDEExplicitFormula/PowerLimit.lean', 825),
        'PowerLimit.lean :825 %s' % blob_line(EF, 'main', 'SIDEExplicitFormula/PowerLimit.lean', 825).strip()[:70], '2-3')
    l = line(os.path.join(PP, 'OPEN_TRAILS.md'), 14162) or ''
    add('ruling (3), (4)', 'OPEN_TRAILS :14162, the transform-bound order', 'W-ORD-FT-FIRST-ORDER' in l, l[:90], '2-4')
    # ### Component 3 and 5: the branch, the workflow, the tag
    add('ferry Component 3', 'branch keiper-b665 not yet made', not branch_listed(EF, 'keiper-b665'), 'git branch --list', '3')
    add('ferry Component 3', 'the workflow on SIDE-explicit-formula`s main', os.path.exists(os.path.join(EF, '.github', 'workflows', 'build-module.yml')),
        '.github/workflows/build-module.yml', '3')
    rc, tg = g(EF, 'tag', '--list', 'v0.30')
    add('ruling (4); ferry Component 5', 'tag v0.30 the next', not tg.strip(), 'absent before the act', '5')
    # ### branches for step zero
    for repo, nm, b in ((ROOT, 'relay', 'push-b664'), (ROOT, 'relay', 'push-b664-root'), (ROOT, 'relay', 'push-b664-closing'),
                        (PP, 'PLACE-papers', 'push-b664'), (PP, 'PLACE-papers', 'push-b664-root'),
                        (KD, 'SIDE-effects', 'push-b664-workflow'), (KD, 'SIDE-effects', 'push-b664-merge'),
                        (KD, 'SIDE-effects', 'docstrings-cut-SIDE-effects')):
        add('ferry Component 0', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    # ### rules and tools
    for rule, cl_, comp in (('R265', (2, 3, 4), '6'), ('R251', (3,), '7'), ('R254', (2,), '0-7'), ('R263', (4,), '3')):
        ok, how = rule_clause(rule, cl_)
        add('ruling (6); ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ruling (6)', 'b666 the next re-cut, b667 W-ORD-EPSTEIN-CERTIFY', 'b667' in (line(os.path.join(PP, 'OPEN_TRAILS.md'), 14188) or ''),
        'OPEN_TRAILS :14188', '7')
    for f in ('tools/push_gated.sh', 'tools/act_root.py', 'tools/additive_shared.py', 'tools/ferry_scan.py', 'tools/terminal_table.py'):
        add('ferry', f, os.path.exists(p(*f.split('/'))), 'exists', '0-7')
    return R


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b665 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    for name, data in (('b665_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b665_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    text = ferry_text()
    q = os.path.join(D, 'b665_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b665_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b665_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b665_citation.py check | ferry')
        sys.exit(2)
    fn(*sys.argv[2:])
