# -*- coding: utf-8 -*-
"""b566_record.py -- THE CONVERSE VENDORED, UNDER (R176). ### THE RECORD TOOL.
### `python tools/b566_record.py reads | weight | ceiling | arda | trials | route | eq | prints | findings | rows | trail |
### scores | desk | components`. b565's and b564's helpers are IMPORTED, never copied. This file deletes nothing: Arda's clone
### is deleted by the seat's own command on its verified absolute path, after `arda` has re-verified the banks' hashes.
"""
import io, json, os, re, subprocess, sys, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b565_record as Z5  # noqa: E402
import b564_record as Z4  # noqa: E402
Q = Z5.Q
PP, FIND, OT, CORR, EF = Q.PP, Q.FIND, Q.OT, Q.CORR, Q.EF
README, REGISTRY = Z4.README, Z4.REGISTRY
NL = chr(10)
rd, g, append_to, guard_absent, poss, line_of = Q.rd, Q.g, Q.append_to, Q.guard_absent, Q.poss, Q.line_of
put_txt, put_json, jl, w_ = Q.put_txt, Q.put_json, Q.jl, Q.w_
STD3 = Q.STD3
PRIOR_RELAY = 'dbddf5ce'
PRIOR_PP = 'b6539b2'
PRIOR_GS = 'b9b0005'
V08 = '6ec71b302998'
BULKA = 'D:/audit-b565/bulka'
ARDA = 'D:/audit-b565/arda'
PIN = '35df682f3b709ffe5fbcfdd452dfa964bd622b87'
BULKA_URL = 'https://github.com/nicholasbulka/li-criterion-rh-equivalence-lean'
BR_A, BR_B = 'vendor-bulka-backport-b566', 'vendor-bulka-forward-b566'
WEIGHT6_H = '*Appended 2026-09-30 by b566 to the field entry (:5575), b564’s line (:6136) and b565’s (:6168), under `(R176)`(1)'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def _lines(L, path, a, b, label, cap=400):
    Z5._lines(L, path, a, b, label, cap)


def _find(L, path, needle, label, cap=300, ctx=0):
    ls = rd(path).split(NL)
    hit = [i + 1 for i, l in enumerate(ls) if needle in l]
    if not hit:
        L.append('### %s -- NOT FOUND: %s' % (label, needle))
        return None
    n = hit[0]
    L.append('### %s -- %s :%d' % (label, os.path.relpath(path, 'D:/').replace(os.sep, '/'), n))
    L += ['    %5d | %s' % (i, ls[i - 1][:cap]) for i in range(n, min(n + ctx, len(ls)) + 1)]
    return n


def reads():
    L = ['b566 -- READING (1): THE READS, PRINTED BY PATH AND LINE', '']
    a = jl('b565_audit.json')
    b = a['bulka']
    L.append('### relay data/b565_audit.json -- Bulka: url %s head %s (%s), build_modules %s, build_exit %s; terminals: %s'
             % (b['url'], b['head'], b['head_date'], b['build_modules'], b['build_exit'], ', '.join(b['rows'])))
    L.append('### relay data/b565_audit.json -- h17a_reason: ' + a['h17a_reason'])
    L.append('### relay data/b565_audit.json -- equality_price: ' + a['equality_price'])
    for n in ('b565_audit_bulka_build.txt', 'b565_audit_bulka_prints.txt', 'b565_audit_bulka_reads.txt', 'b565_audit_bulka_info.txt'):
        p = os.path.join(D, n)
        L.append('### relay data/%s (sha256 %s, %d lines)' % (n, hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16],
                                                         len(rd(p).split(NL))))
    _find(L, os.path.join(D, 'b565_audit_bulka_prints.txt'), 'positivity_implies_RH', 'the converse`s print, b565', 300, 3)
    L.append('### the converse`s fully qualified name and module: LiCriterion.positivity_implies_RH, '
             'Lc/LiCriterion/ReverseDirection.lean')
    _find(L, os.path.join(BULKA, 'Lc/LiCriterion/ReverseDirection.lean'), 'theorem positivity_implies_RH', 'Bulka', 300, 3)
    _find(L, os.path.join(BULKA, 'Lc/LiCriterion/Fidelity.lean'), 'theorem taylorCoeff_eq_li_symmetrized', 'Bulka', 300, 6)
    _find(L, os.path.join(BULKA, 'Lc/LiCriterion/Fidelity.lean'), 'theorem summable_li_symmetrized', 'Bulka', 300, 5)
    _find(L, os.path.join(BULKA, 'Lc/LiCriterion/Fidelity.lean'), 'lemma analyticOrderNatAt_riemannXi_one_sub', 'Bulka', 300, 1)
    _find(L, os.path.join(BULKA, 'Lc/LiCriterion/RHBridge.lean'), 'theorem rh_equiv_mathlib', 'Bulka', 300, 2)
    _find(L, os.path.join(BULKA, 'Lc/XiZeros.lean'), 'noncomputable def riemannXi', 'Bulka', 300, 1)
    _find(L, os.path.join(BULKA, 'Lc/XiZeros.lean'), 'lemma xi_eq_half_s_sm1_Lambda', 'Bulka', 300, 1)
    _find(L, os.path.join(BULKA, 'Lc/LiCriterion/Basic.lean'), 'noncomputable def NontrivialZero', 'Bulka', 300, 1)
    _find(L, os.path.join(BULKA, 'Lc/LiCriterion/Basic.lean'), 'noncomputable def riemannXi', 'Bulka', 300, 1)
    _find(L, os.path.join(BULKA, 'Lc/LiCriterion/Basic.lean'), 'noncomputable def taylorCoeff', 'Bulka', 300, 1)
    _find(L, os.path.join(BULKA, 'Lc/LiCriterion/Basic.lean'), 'noncomputable def pairedZeroEquiv', 'Bulka', 300, 1)
    L.append('### Bulka`s LICENSE at 35df682f: relay data/b566_step1_license.txt (printed whole); lean-toolchain '
             + rd(os.path.join(BULKA, 'lean-toolchain')).strip())
    _find(L, os.path.join(BULKA, 'lakefile.lean'), '"de5ce8a9', 'Bulka lakefile.lean (Mathlib rev)', 200, 0)
    _find(L, os.path.join(BULKA, 'lakefile.lean'), 'maxSynthPendingDepth', 'Bulka lakefile.lean (the options)', 200, 0)
    # the Zeta23 vendoring record
    for n in (8022, 8059):
        _lines(L, OT, n, n, 'OPEN_TRAILS.md ((R82)/(R83), the Zeta23 vendoring record)', 500)
    k = subprocess.run(['git', '-C', EF, 'show', V08 + ':README.md'], capture_output=True, text=True, encoding='utf-8').stdout.split(NL)
    L.append('### SIDE-explicit-formula README.md at v0.8 :1-:30')
    L += ['    %5d | %s' % (i + 1, k[i][:300]) for i in range(0, 30) if k[i].strip()]
    for f in ('NOTICE', 'lakefile.toml', 'lean-toolchain'):
        k = subprocess.run(['git', '-C', EF, 'show', V08 + ':' + f], capture_output=True, text=True, encoding='utf-8').stdout.split(NL)
        L.append('### SIDE-explicit-formula %s at v0.8' % f)
        L += ['    %5d | %s' % (i + 1, x[:300]) for i, x in enumerate(k) if x.strip()]
    k = subprocess.run(['git', '-C', EF, 'show', V08 + ':lake-manifest.json'], capture_output=True, text=True, encoding='utf-8').stdout.split(NL)
    L.append('### SIDE-explicit-formula lake-manifest.json at v0.8, its rev and name lines')
    L += ['    %5d | %s' % (i + 1, x.strip()) for i, x in enumerate(k) if '"rev"' in x or '"name"' in x]
    _lines(L, os.path.join(EF, 'Zeta23/Defs.lean'), 1, 16, 'a vendored file`s header (Zeta23/Defs.lean)')
    _lines(L, os.path.join(PP, 'SPIRAL_MAP.md'), 479, 495, 'SPIRAL_MAP.md (the rule 9 waiver for vendored namespaces)', 300)
    # the kernel's objects
    lw = os.path.join(EF, 'SIDEExplicitFormula/LiWeil.lean')
    for nd, c in (('def liTerm', 0), ('def LiCoeff', 1), ('theorem LiCoeff_eq', 1), ('theorem liTerm_re_summable', 1),
                  ('theorem rh_imp_li_nonneg', 0)):
        _find(L, lw, nd, 'LiWeil.lean', 300, c)
    _find(L, os.path.join(EF, 'SIDEExplicitFormula/LiWeilSym.lean'), 'theorem li_identity_sym', 'LiWeilSym.lean', 300, 1)
    _find(L, os.path.join(EF, 'Zeta23/Statement.lean'), 'def IsNontrivialZero', 'Zeta23', 300, 0)
    _find(L, os.path.join(EF, 'Zeta23/Statement.lean'), 'def zeroMult', 'Zeta23', 300, 0)
    _find(L, os.path.join(EF, 'Zeta23/Statement/SeamClosed.lean'), 'def zetaZeroConfig', 'Zeta23', 300, 0)
    _find(L, os.path.join(EF, 'Zeta23/ZetaReflect.lean'), 'theorem zeta_mult_reflect', 'Zeta23', 300, 0)
    # Mathlib at both pins
    for tag, M in (('51e6992e (the kernel`s)', os.path.join(EF, '.lake/packages/mathlib')),
                   ('de5ce8a9 (Bulka`s)', os.path.join(BULKA, '.lake/packages/mathlib'))):
        head = subprocess.run(['git', '-C', M, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
        L.append('### MATHLIB AT %s -- checkout HEAD %s' % (tag, head))
        rz = os.path.join(M, 'Mathlib/NumberTheory/LSeries/RiemannZeta.lean')
        for nd in ('def completedRiemannZeta₀', 'def completedRiemannZeta ', 'lemma completedRiemannZeta_eq',
                   'theorem differentiable_completedZeta₀', 'def riemannZeta', 'theorem differentiableAt_riemannZeta',
                   'lemma riemannZeta_def_of_ne_zero', 'def RiemannHypothesis'):
            _find(L, rz, nd, 'Mathlib', 200, 0)
        _find(L, os.path.join(M, 'Mathlib/Analysis/SpecialFunctions/Gamma/Deligne.lean'), 'lemma Gammaℝ_ne_zero_of_re_pos', 'Mathlib', 200, 0)
        _find(L, os.path.join(M, 'Mathlib/Analysis/SpecialFunctions/Gamma/Deligne.lean'), 'lemma differentiable_Gammaℝ_inv', 'Mathlib', 200, 0)
        ao = os.path.join(M, 'Mathlib/Analysis/Analytic/Order.lean')
        for nd in ('theorem analyticOrderAt_mul ', 'lemma analyticOrderAt_congr', 'protected lemma AnalyticAt.analyticOrderAt_eq_zero'):
            _find(L, ao, nd, 'Mathlib', 200, 0)
    # the ledgers
    _lines(L, FIND, 6144, 6144, 'FINDINGS.md (b564`s record of the ceiling sentence)', 600)
    _lines(L, FIND, 6168, 6168, 'FINDINGS.md (b565`s field line)', 3000)
    _lines(L, FIND, 6170, 6172, 'FINDINGS.md (b565`s entry)', 600)
    _lines(L, README, 115, 117, 'README.md (the ceiling: (R146)(2) and b564`s sentence)', 600)
    _lines(L, REGISTRY, 950, 952, 'REGISTRY.md (the ceiling: (R146)(2) and b564`s sentence)', 600)
    _lines(L, OT, 11609, 11609, 'OPEN_TRAILS.md (the converse`s price, b564)', 3000)
    _lines(L, OT, 11630, 11630, 'OPEN_TRAILS.md (the (R175)(3) conditional, b565)', 4000)
    c = subprocess.run(['git', '-C', ROOT, 'log', '-1', '--format=%h %s', '--', 'data/b565_closing_push_out.txt'],
                       capture_output=True, text=True, encoding='utf-8').stdout.strip()
    L.append('### relay data/b565_closing_push_out.txt -- committed alone at this act`s start: ' + c[:200])
    put_txt('b566_reads.txt', L)
    print('  lines %d ; NOT FOUND %d ; written: b566_reads.txt' % (len(L), sum(1 for l in L if 'NOT FOUND' in l)))


def weight():
    """### (R176)(1): the audit at its weight, one line after b565's entry, in b561's and b565's form."""
    guard_absent(FIND, WEIGHT6_H)
    a = jl('b565_audit.json')
    z = a['zeta23']
    t = (WEIGHT6_H + ' -- THE AUDIT AT ITS WEIGHT:* both public formalizations are genuine at their pins. Both repositories build '
         'clean at their pins with one lean process per module (Bulka %d, Arda %d); all %d audited terminals print '
         '[propext, Classical.choice, Quot.sound]; every closure reads 0 sorry and 0 axiom declarations, Zeta23’s modules at '
         '`fbdc36bb` included. H17a refuted: Bulka’s converse (positivity → RH) is over Mathlib’s `RiemannHypothesis` and '
         'Mathlib’s `riemannZeta`, confirmed by their declaring module, its zero set Mathlib’s under the repository’s own name '
         'for the strip set. H17b refuted: Arda’s `bl_explicit_formula` DERIVES over the divisor of Mathlib’s `riemannZeta`, '
         'its two premises discharged by name. Bulka’s forward direction is the same object as `rh_imp_li_nonneg` up to an '
         'index shift (their n is Li’s n + 1) and the coefficient’s definition; Arda’s `bl_explicit_formula` is a different '
         'object from `li_identity_sym` (a different limit, a closed-form arithmetic side), and Arda’s `liValue` is the nearer '
         'one. The programme’s %d vendored Zeta23 modules are identical in code to `fbdc36bb` (%d byte-identical, %d differing in '
         'a header comment alone); no pin refresh is needed. Each is stated in its own terms; no priority is claimed.'
         % (a['bulka']['build_modules'], a['arda']['build_modules'], a['terminal_count'], z['vendored'], z['identical'],
            z['comment_only']))
    res = append_to(FIND, NL + t + NL)
    n = line_of(FIND, WEIGHT6_H)
    put_json('b566_weight.json', dict(line=n, text=poss(t), res=res))
    L = ['b566 -- COMPONENT 1 (i): THE AUDIT AT ITS WEIGHT, (R176)(1)', '', '### FINDINGS.md :%s -- %s' % (n, json.dumps(res)),
         '    ' + rd(FIND).split(NL)[n - 1]]
    put_txt('b566_weight.txt', L)
    print(NL.join(L))


def author_sentence():
    """### (R176)(2)`s sentence, READ from the banked ferry between its quotation marks, whitespace-joined -- not retyped."""
    f = ' '.join(rd(os.path.join(D, 'b566_ferry.txt')).split())
    m = re.search(r'amended in the author.s words: "([^"]+)"', f)
    return m.group(1) if m else None


def ceiling():
    s = author_sentence()
    if not s:
        sys.exit('### THE AUTHOR`S SENTENCE WAS NOT FOUND IN THE BANKED FERRY')
    para = ("*(Appended under the author's ruling `(R176)`(2), 2026-09-30, b566, beside the `(R146)`(2) sentence and b564's "
            "`(R174)`(1) sentence above, which stay: the audit of b565 entered at its weight.)* Supportable, the author's "
            "sentence: *" + s + "* Not supportable, unchanged: *RH proved*; *h2_sign proved*.")
    out = {}
    for path, n in ((README, 117), (REGISTRY, 952)):
        l0 = rd(path).split(NL)[n - 1]
        if '(R174)' not in l0:
            sys.exit('### %s :%d IS NOT b564`S (R174)(1) LINE' % (os.path.basename(path), n))
        guard_absent(path, para[:90])
        out[os.path.basename(path)] = Z4._insert_after(path, n, para) if n < len(rd(path).rstrip(NL).split(NL)) else \
            dict(append_to(path, NL + para + NL), after_line=n, new_line=n + 2)
    L = ['b566 -- COMPONENT 1 (ii): THE CEILING SENTENCE, (R176)(2), BESIDE b564`S LINE IN b536`S FORM', '',
         '### the author`s sentence, read from the banked ferry: ' + s, '### the paragraph: ' + para, '']
    for k, v in out.items():
        L.append('### %s : %s' % (k, json.dumps(v)))
        L.append('    the line now at :%d : %s' % (v['new_line'], rd(os.path.join(PP, k)).split(NL)[v['new_line'] - 1]))
    put_txt('b566_ceiling.txt', L)
    put_json('b566_ceiling.json', dict(sentence=s, para=para, files=out))
    print(NL.join(L))


def arda():
    """### (R176)(5): Arda`s banks re-hashed against the relay blobs at b565`s close, BEFORE the seat deletes the clone."""
    names = sorted(n for n in os.listdir(D) if n.startswith('b565_audit_arda_'))
    L = ['b566 -- COMPONENT 1 (iii): ARDA`S BANKS RE-HASHED BEFORE THE CLONE IS DELETED, (R176)(5)', '',
         '### against the relay blobs at b565`s close (%s); %d banks' % (PRIOR_RELAY, len(names))]
    agree = 0
    rows = []
    for n in names:
        disk = hashlib.sha256(open(os.path.join(D, n), 'rb').read()).hexdigest()
        b = subprocess.run(['git', '-C', ROOT, 'show', '%s:data/%s' % (PRIOR_RELAY, n)], capture_output=True).stdout
        blob = hashlib.sha256(b).hexdigest() if b else None
        ok = (blob is not None and disk == blob)
        agree += ok
        rows.append(dict(bank=n, disk=disk, blob=blob, agree=ok))
        L.append('  %-58s disk %s blob %s %s' % (n, disk[:16], (blob or 'ABSENT')[:16], 'AGREE' if ok else '### DIFFER ###'))
    head = subprocess.run(['git', '-C', ARDA, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    L.append('### the clone at %s: HEAD %s (the audit`s pin %s)' % (ARDA, head or 'ABSENT', jl('b565_audit.json')['arda']['head']))
    L.append('### ### **BANKS %d ; AGREEING %d : %s**' % (len(names), agree, 'RE-VERIFIED' if agree == len(names) and names else 'NOT RE-VERIFIED'))
    put_txt('b566_arda_rehash.txt', L)
    put_json('b566_arda_rehash.json', dict(banks=rows, agree=agree, total=len(names), clone_head=head))
    print(NL.join(L))
    return 0 if agree == len(names) and names else 1


TRIAL_RE = re.compile(r'^--- \+(\S+) rc=(\S+) secs=([\d,]+)', re.M)
ERR_RE = re.compile(r'^error: (\S+?\.lean):(\d+):(\d+): (.*)$', re.M)


def _trial(log, modules, blocked):
    """### per module: its LAST call`s rc and the Lean errors printed in that call`s block (file:line:col lines only)."""
    t = rd(os.path.join(D, log))
    blocks = re.split(r'(?m)^(?==== \S+ \+)', t)
    per = {}
    for b in blocks:
        m = re.match(r'=== (\S+) \+(\S+) ', b)
        if not m:
            continue
        mod = m.group(2)
        r = TRIAL_RE.search(b)
        errs = [dict(file=e.group(1), line=int(e.group(2)), col=int(e.group(3)), msg=e.group(4)) for e in ERR_RE.finditer(b)]
        if r:
            per[mod] = dict(rc=r.group(2), secs=int(r.group(3).replace(',', '')), errors=errs, started=m.group(1))
        else:
            per.setdefault(mod, dict(rc='NO RESULT LINE', secs=None, errors=errs, started=m.group(1)))
    rows = []
    for mod in modules:
        if mod in per:
            rows.append(dict(module=mod, **per[mod]))
        else:
            rows.append(dict(module=mod, rc='BLOCKED' if mod in blocked else 'NOT CALLED', secs=None, errors=[],
                             upstream=blocked.get(mod)))
    return rows


def _imports_of(k, m):
    """### a module`s imports within its own tree, read from the trial branch`s committed file (COMPUTED, not typed)."""
    if k == 'a':
        rev, base = BR_A, 'Vendored/Bulka/'
    else:
        rev, base = BR_B, ''
    t = subprocess.run(['git', '-C', EF, 'show', '%s:%s%s.lean' % (rev, base, m.replace('.', '/'))], capture_output=True).stdout
    return re.findall(r'^import\s+(\S+)', t.decode('utf-8', 'replace'), re.M)


def _blocked(k, mods, failed):
    """### a module is BLOCKED when it was not called and its import closure within the list reaches a failed module."""
    ms = set(mods)
    memo = {}

    def up(m, seen=()):
        if m in memo:
            return memo[m]
        hit = None
        for i in _imports_of(k, m):
            if i in failed:
                hit = i
                break
            if i in ms and i not in seen:
                h = up(i, seen + (m,))
                if h:
                    hit = h
                    break
        memo[m] = hit
        return hit
    return {m: up(m) for m in mods if m not in failed and up(m)}


def trials():
    import itertools
    S = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/14ee47b5-97c5-4229-babc-8972b52dc38a/scratchpad'
    out = {}
    L = ['b566 -- COMPONENT 2: THE TWO TRIALS, PER MODULE (R176)(3) STEP ONE', '']
    spec = [('a', 'b566_trial_a_build.txt', os.path.join(D, 'b566_vendor_list.txt'), 'BACKPORT: the vendored set at the kernel`s pins '
             'v4.33.0-rc2 / 51e6992e, branch ' + BR_A),
            ('b', 'b566_trial_b_build.txt', os.path.join(D, 'b566_trial_b_modules.txt'), 'FORWARD: the kernel`s own library at Bulka`s '
             'pins v4.34.0-rc1 / de5ce8a9, branch ' + BR_B + ', worktree D:/b566-forward')]
    for k, log, lst, title in spec:
        if not os.path.exists(os.path.join(D, log)):
            L.append('### TRIAL (%s) -- %s : NO LOG BANKED' % (k, title))
            continue
        mods = [x.strip() for x in rd(lst).split(NL) if x.strip()]
        rows0 = _trial(log, mods, {})
        failed = {r['module'] for r in rows0 if r['rc'] not in ('0', 'NOT CALLED', 'BLOCKED')}
        bl = _blocked(k, mods, failed)
        rows = _trial(log, mods, bl)
        called = [r for r in rows if r['rc'] not in ('BLOCKED', 'NOT CALLED')]
        ok = [r for r in called if r['rc'] == '0']
        bad = [r for r in called if r['rc'] != '0']
        nerr = sum(len(r['errors']) for r in rows)
        clean = (len(ok) == len(mods))
        L.append('### TRIAL (%s) -- %s' % (k, title))
        L.append('    modules %d ; called %d ; exit 0 %d ; exit non-zero %d ; blocked %d ; not called %d ; LEAN ERRORS %d'
                 % (len(mods), len(called), len(ok), len(bad), sum(r['rc'] == 'BLOCKED' for r in rows),
                    sum(r['rc'] == 'NOT CALLED' for r in rows), nerr))
        for r in rows:
            L.append('    %-52s rc %-8s secs %-6s errors %d%s' % (r['module'], r['rc'], r['secs'] if r['secs'] is not None else '-',
                     len(r['errors']), ('   (upstream: %s)' % r.get('upstream')) if r.get('upstream') else ''))
            for e in r['errors']:
                L.append('        error %s:%d:%d %s' % (e['file'], e['line'], e['col'], e['msg'][:160]))
        L.append('    ### ### **TRIAL (%s) : %s**' % (k, 'CLEAN -- EVERY MODULE EXIT 0, NO SOURCE EDIT' if clean else
                                                   'NOT CLEAN -- %d LEAN ERRORS IN %d MODULES, %d BLOCKED' % (
                                                       nerr, len(bad), sum(r['rc'] == 'BLOCKED' for r in rows))))
        L.append('')
        out[k] = dict(modules=len(mods), called=len(called), ok=len(ok), bad=[r['module'] for r in bad], errors=nerr, clean=clean,
                      rows=rows)
    put_txt('b566_trials.txt', L)
    put_json('b566_trials.json', out)
    print(NL.join(L))


def route():
    """### (R176)(3): the route is the trial that builds clean with no source edit; if both do, the backport (the face`s reading);
    ### if neither, the cheaper by Lean error count is priced and the act is HELD at step one with both prices."""
    tj = jl('b566_trials.json')
    a, b = tj.get('a'), tj.get('b')
    L = ['b566 -- COMPONENT 2: THE ROUTE, (R176)(3) STEP ONE', '']
    for k, t in (('a', a), ('b', b)):
        if not t:
            L.append('### TRIAL (%s): NO BANK -- the route cannot be named' % k)
    if not (a and b):
        put_txt('b566_route.txt', L)
        return 1
    for k, t in (('a', a), ('b', b)):
        L.append('### TRIAL (%s): modules %d, exit 0 %d, non-zero %s, LEAN ERRORS %d, clean %s'
                 % (k, t['modules'], t['ok'], t['bad'], t['errors'], t['clean']))
    if a['clean'] and b['clean']:
        word, held = 'ROUTE (a), THE BACKPORT -- both trials clean; the backport moves no pin of the kernel (the face`s reading)', False
    elif a['clean']:
        word, held = 'ROUTE (a), THE BACKPORT -- the only clean trial', False
    elif b['clean']:
        word, held = 'ROUTE (b), THE FORWARD MOVE -- the only clean trial', False
    else:
        cheaper = 'a' if a['errors'] <= b['errors'] else 'b'
        word, held = ('HELD AT STEP ONE -- BOTH TRIALS NEED SOURCE EDITS; the cheaper by Lean error count is (%s) (%d against %d)'
                      % (cheaper, min(a['errors'], b['errors']), max(a['errors'], b['errors']))), True
    L.append('')
    L.append('### ### **%s**' % word)
    put_txt('b566_route.txt', L)
    put_json('b566_route.json', dict(word=word, held=held, a_errors=a['errors'], b_errors=b['errors'], a_clean=a['clean'],
                                     b_clean=b['clean']))
    print(NL.join(L))
    return 0


def prints_axioms(text):
    """### `'<name>' depends on axioms: [...]` read with the list allowed to wrap across lines (Lean wraps a long one), and
    ### `'<name>' does not depend on any axioms` read as []. b560_record.parse_prints reads the one-line form only."""
    out = {}
    for m in re.finditer(r"^'([^']+)' depends on axioms: \[([^\]]*)\]", text, re.M):
        out[m.group(1)] = [x.strip() for x in m.group(2).replace(NL, ' ').split(',') if x.strip()]
    for m in re.finditer(r"^'([^']+)' does not depend on any axioms", text, re.M):
        out[m.group(1)] = []
    return out


NSB = 'SIDEExplicitFormula.LiCriterionBridge.'
OF_RECORD = ['li_coeff_eq_taylorCoeff', 'li_nonneg_iff_rh', 'arith_limit_nonneg_iff_rh']


def e0():
    """### READING (5): every declaration of LiCriterionBridge.lean graded from the prints of record (data/b566_prints.txt) and
    ### its own statement at the route branch`s tip; definitions salt-checked; rowgen`s source-side record of the terminals of
    ### record (rowgen.py`s extract_doc_body and definition_encoded IMPORTED through b560_record.rowgen_record)."""
    pr = rd(os.path.join(D, 'b566_prints.txt'))
    P0 = prints_axioms(pr)
    decls = jl('b566_decls.json')['decls']
    consumed = jl('b566_decls.json')['consumed']
    tip = g(EF, 'rev-parse', BR_B).strip()
    src = Q.at(tip, 'SIDEExplicitFormula/LiCriterionBridge.lean')
    L = ['b566 -- READING (5): THE E0 READ -- EVERY DECLARATION OF SIDEExplicitFormula/LiCriterionBridge.lean GRADED, THE SALT-CHECK,'
         ' THE ROWGEN RECORD', '',
         '### the prints of record: relay data/b566_prints.txt (lake env lean AxiomCheckLiCriterion.lean at %s, branch %s).' % (tip[:7], BR_B),
         '### THE RULE: a theorem is INTERFACES when an explicit hypothesis binder of its statement is a named Prop of a vendored or',
         '### kernel module (a premise passed through); DERIVES when its only binders are domain conditions (a nonzero point, a real',
         '### part, an index) -- read from the statement`s own text up to `:=`, printed here. Definitions are ungraded and salt-checked.', '']
    rows = {}
    for d in decls:
        n = d['name']
        ax = P0.get(n)
        m = re.search(r'^(?:theorem|def) ' + re.escape(n.split('.')[-1]) + r'\b(.*?):=', src, re.M | re.S)
        head = ' '.join(m.group(1).split()) if m else ''
        binders = re.findall(r'\((h\w*) : ([^()]*(?:\([^()]*\)[^()]*)*)\)', head)
        prem = [(b, t) for b, t in binders if not re.search(r'(?:≠|<|≤|=|∈)', t)]
        if d['kind'] == 'def':
            gr, why = 'DEF', ''
        else:
            gr = 'INTERFACES' if prem else 'DERIVES'
            why = ', '.join('%s : %s' % bt for bt in prem) or ('domain conditions only: ' + ', '.join(b for b, _ in binders) if binders else 'no hypothesis binder')
        rows[n] = dict(grade=gr, why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3), head=head)
        L.append('    %-34s %-10s %s  -- %s' % (n.split('.')[-1], 'DEFINITION' if gr == 'DEF' else gr, 'std3' if rows[n]['std3'] else ax, why))
    L.append('')
    L.append('### THE CONSUMED TERMINALS (vendored and kernel), their prints:')
    cons = {n: P0.get(n) for n in consumed}
    for n, ax in cons.items():
        L.append('    %-52s %s' % (n, 'std3' if ax is not None and set(ax) <= set(STD3) else ax))
    L.append('')
    L.append('### THE SALT-CHECK -- Lean`s #print of each definition (no sorry):')
    salt = {}
    for d in decls:
        if d['kind'] != 'def':
            continue
        j = pr.find('def %s' % d['name'])
        blk = pr[j:j + 600].split(NL + 'def ')[0] if j >= 0 else ''
        salt[d['name']] = bool(blk) and 'sorry' not in blk
        L += ['    ' + x for x in blk.strip().split(NL)[:3]] if blk else ['    ### %s NOT PRINTED' % d['name']]
    salt_ok = all(salt.values()) and bool(salt)
    L.append('### ### **THE SALT-CHECK: %s** (%d definitions)' % (salt_ok, len(salt)))
    recs, ctl = Q.rowgen_record([NSB + x for x in OF_RECORD], 'SIDEExplicitFormula/LiCriterionBridge.lean', tip, pr)
    L.append('')
    L.append('### THE ROWGEN RECORD (rowgen.py`s extract_doc_body and definition_encoded IMPORTED, at %s):' % tip[:7])
    for r in recs:
        L.append('    %-30s defenc %-5s %s | check %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], bool(r['check'])))
        L.append('        check: %s' % ' '.join(r['check'].split())[:300])
    L.append('    control: definition_encoded on `def b560_ctl_stub : Prop := True` -> %s (must be True)' % (ctl,))
    thms = [n for n, r in rows.items() if r['grade'] != 'DEF']
    cnt = {k: sum(1 for n in thms if rows[n]['grade'] == k) for k in ('DERIVES', 'INTERFACES')}
    gate = (all(r['std3'] for r in rows.values()) and all(a is not None and set(a) <= set(STD3) for a in cons.values()) and salt_ok
            and ctl[0] and not any(r['defenc'] for r in recs) and all(r['check'] for r in recs) and len(P0) >= len(rows) + len(cons))
    L.append('### ### **THE GATE: EVERY PRINT THE STANDARD THREE %s ; THEOREMS %d (DERIVES %d, INTERFACES %d) ; DEFINITIONS %d ; '
             'CONSUMED %d AT THE STANDARD THREE %s ; THE SALT-CHECK %s => MERGE %s**'
             % (all(r['std3'] for r in rows.values()), len(thms), cnt['DERIVES'], cnt['INTERFACES'], len(rows) - len(thms), len(cons),
                all(a is not None and set(a) <= set(STD3) for a in cons.values()), salt_ok, gate))
    put_txt('b566_e0.txt', L)
    put_json('b566_e0.json', dict(rows=rows, consumed=cons, gate=gate, salt=salt_ok, rowgen=recs, rowgen_control=ctl[0], tip=tip, counts=cnt))
    print(NL.join(L))


# ================================================================================ COMPONENT 5: THE RECORD
V09 = 'e5a5a8347af1'
COMP6_H = '*Appended 2026-10-01 by b566 to the field entry (:5575) and the weight line above it, under `(R176)`(3)'
WO6 = '*Appended 2026-10-01 by b566, under the author’s ruling `(R176)`(6), to the LI-WEIL-BRIDGE work-order (:3548; b565’s conditional at :11630)'
FH6 = ('## The converse vendored: Bulka’s positivity → RH at 35df682f composed with the programme’s Li coefficients through the '
       'equality lemma; Li’s criterion as a compiled equivalence')
HEADING6 = ('### b566 — the converse vendored under (R176): the licence, the toolchain trial both ways, the equality lemma, the '
            'composed criterion; v0.9')
ROW_ACT6, ROW_T = '403', ('404', '405', '406')
TERMS6 = ['li_nonneg_iff_rh', 'arith_limit_nonneg_iff_rh', 'li_coeff_eq_taylorCoeff']


def _e0():
    return jl('b566_e0.json')


def kstate6():
    ls = {}
    for l in g(EF, 'ls-remote', 'origin').split(NL):
        if '\t' in l:
            h, r = l.split('\t')
            ls[r.strip()] = h.strip()
    ns = [x for x in g(EF, 'diff', '--name-status', V08, 'main').split(NL) if x.strip()]
    lean_changed = [x for x in ns if x.endswith('.lean') and not x.startswith('A')]
    kept = {b: g(EF, 'rev-parse', b).strip() for b in Z5.KEPT5}
    mains = {}
    for k, h in Z5.PRE_HEADS5.items():
        mains[k] = sorted(x for x in g(os.path.join(Q.DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip())
    return dict(main=g(EF, 'rev-parse', 'main').strip(), remote=ls, v09=g(EF, 'rev-parse', 'v0.9^{}').strip(),
                v09obj=g(EF, 'rev-parse', 'v0.9').strip(), v09type=g(EF, 'cat-file', '-t', 'v0.9').strip(),
                fwd=g(EF, 'rev-parse', BR_B).strip(), back=g(EF, 'rev-parse', BR_A).strip(), kept=kept,
                ns_count=len(ns), lean_changed=lean_changed, mains=mains,
                ff=subprocess.run(['git', '-C', EF, 'merge-base', '--is-ancestor', V08, 'main']).returncode == 0)


def scores():
    k = kstate6()
    tj, rj, e = jl('b566_trials.json'), jl('b566_route.json'), _e0()
    lic = rd(os.path.join(D, 'b566_step1_license.txt'))
    clo = rd(os.path.join(D, 'b566_step1_closure.txt'))
    m = re.search(r'ITS CLOSURE: (\d+) MODULES\*\* \(import order\)', clo)
    n_conv = int(m.group(1)) if m else None
    rows = e['rows']
    std = lambda n: rows.get(NSB + n, {}).get('std3') and rows.get(NSB + n, {}).get('grade') == 'DERIVES'
    h19a = ('Apache License' in lic and 'Version 2.0, January 2004' in lic and '4. Redistribution.' in lic
            and 'You may reproduce and distribute copies' in lic)
    h19b = bool(tj['a']['clean'] or tj['b']['clean'])
    e2 = rows.get(NSB + 'analyticOrderAt_xi_eq_zeta', {})
    h19c = bool(e2.get('std3')) and e2.get('grade') == 'DERIVES'
    h19d = bool(std('li_nonneg_iff_rh'))
    v09 = (k['v09'] == k['main'] == k['fwd'] and k['remote'].get('refs/tags/v0.9^{}') == k['v09']
           and k['remote'].get('refs/heads/main') == k['main'])
    others = {kk: v for kk, v in k['mains'].items() if kk not in ('SIDE-explicit-formula', 'SIDE-global-section')}
    n6 = (k['lean_changed'] == [] and k['ff'] and all(not v for v in others.values())
          and set(k['mains'].get('SIDE-global-section', [])) <= {'CORRESPONDENCE.md'}
          and all(k['kept'][b].startswith(t[:12]) for b, t in Z5.KEPT5.items()))
    # (S3): the face`s first clause names the Mathlib facts READING (4) lists; the module`s (E2) proof uses others too.
    listed = ('riemannZeta_def_of_ne_zero', 'Gammaℝ_ne_zero_of_re_pos', 'analyticOrderAt_mul', 'analyticOrderAt_congr')
    src = Q.at(k['fwd'], 'SIDEExplicitFormula/LiCriterionBridge.lean')
    blk = src[src.find('theorem analyticOrderAt_xi_eq_zeta'):src.find('/-- Bulka`s multiplicity') if '/-- Bulka`s multiplicity' in src else src.find('def xiMult')]
    used = sorted(set(re.findall(r'\b(differentiableAt_completedZeta|differentiable_Gammaℝ_inv|DifferentiableOn\.analyticAt|'
                                 r'analyticOrderAt_eq_zero|riemannZeta_def_of_ne_zero|Gammaℝ_ne_zero_of_re_pos|analyticOrderAt_mul|'
                                 r'analyticOrderAt_congr|analyticAt|isOpen_ne|isOpen_lt)\b', blk)))
    beyond = [u for u in used if u not in listed]
    s3 = (not beyond) and all(std(t) for t in TERMS6)
    s = dict(h19a=h19a, h19b=h19b, h19c=h19c, h19d=h19d, n1=h19a, n2=bool(tj['a']['clean']), n3=(n_conv is not None and n_conv <= 12),
             n4=h19c, n5=all(std(t) for t in TERMS6[:2]) and v09, n6=n6 and v09,
             s1=bool(tj['a']['clean']), s2=not tj['b']['clean'], s3=s3, v09=v09, n_conv=n_conv, s3_beyond=beyond, kstate=k)
    L = ['b566 -- THE SCORES, READ OFF THE BANKS', '']
    for key in ('h19a', 'h19b', 'h19c', 'h19d', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3', 'v09'):
        L.append('    %-5s %s' % (key.upper(), w_(s[key])))
    L.append('    the converse`s closure count (b566_step1_closure.txt): %s' % n_conv)
    L.append('    (S3)`s first clause: the (E2) proof`s Mathlib names beyond READING (4)`s list: %s' % (beyond or 'NONE'))
    L.append('    kernel: main %s v0.9 obj %s (%s) peeled %s ; remote main %s ; route branch %s ; backport branch %s ; ff from v0.8 %s ;'
             ' changed paths %d ; existing .lean changed %s' % (k['main'][:7], k['v09obj'][:7], k['v09type'], k['v09'][:7],
                                                                k['remote'].get('refs/heads/main', '')[:7], k['fwd'][:7], k['back'][:7],
                                                                k['ff'], k['ns_count'], k['lean_changed'] or 'NONE'))
    put_txt('b566_scores.txt', L)
    put_json('b566_scores.json', s)
    print(NL.join(L))


def complete_line():
    """### the field entry`s line that the composition landed (the ferry`s Component 5)."""
    guard_absent(FIND, COMP6_H)
    e, k = _e0(), kstate6()
    t = (COMP6_H + ' -- THE COMPOSITION LANDED:* SIDE-explicit-formula v0.9 = `' + k['v09'][:7] + '` (tag object `' + k['v09obj'][:7]
         + '`) carries `li_nonneg_iff_rh : (∀ n, 0 ≤ LiCoeff n) ↔ RiemannHypothesis` and `arith_limit_nonneg_iff_rh` (RH as the '
         'nonnegativity of the δ → 0⁺ limits of EF_lit’s literature side at the symmetric family), each printing [propext, '
         'Classical.choice, Quot.sound], over Mathlib’s `riemannZeta` zeros and Mathlib’s `RiemannHypothesis`; the converse is '
         'Bulka’s `LiCriterion.positivity_implies_RH`, vendored byte-identical at `35df682f` (33 modules, Apache 2.0), consumed by '
         'name through `li_coeff_eq_taylorCoeff : LiCoeff (n + 1) = Re(taylorCoeff riemannXi n)`. The kernel moved to Lean '
         'v4.34.0-rc1 and Mathlib `de5ce8a9` to do it, after the trial both ways (relay `data/b566_trials.txt`). No priority is '
         'claimed; the work composed is the vendored repository’s and the programme’s, each named.')
    res = append_to(FIND, NL + t + NL)
    n = line_of(FIND, COMP6_H)
    put_json('b566_complete_line.json', dict(line=n, text=poss(t), res=res))
    print('### FINDINGS :%s -- %s' % (n, json.dumps(res)))


def price():
    """### (R176)(6): the residue chain`s Li-channel premise priced at the work-order, not attempted."""
    guard_absent(OT, WO6)
    t = (WO6 + ' -- THE RESIDUE CHAIN, PRICED AFTER THE COMPOSITION, NOT ATTEMPTED:* the residue theorem '
         '`zeroActingPairing_to_RH` (SIDE-lv-conservation `2f71068`, SIDELvConservation/ZeroActingPairing.lean :66-:75, Lean '
         'v4.29.1) takes two premises for its λ: `inequalityToPositivity : Register4_channelInequality lam_A lam_Z → '
         'Register4_positivity lam` and `liCriterion : Register4_positivity lam → RiemannHypothesis`, with `Register4_positivity '
         'lam := ∀ n, 1 ≤ n → 0 ≤ lam n` (RegisterPentagon.lean :152). At λ := `LiCoeff` the Li-channel premise `liCriterion` is '
         'now DISCHARGEABLE in SIDE-explicit-formula at v0.9, priced at three declarations: (L1) `Register4_positivity` restated '
         'there with its source cited by pin (the kernels share no toolchain, so it is restated, not imported); (L2) `LiCoeff 0 = '
         '0`, since `liTerm 0 ρ = 1 − 1`; (L3) `Register4_positivity LiCoeff → RiemannHypothesis`, from (L2) and '
         '`li_nonneg_iff_rh`. The other premise, `inequalityToPositivity`, stays as b561’s consumer read (:11542) priced it: it '
         'consumes `LiCoeff n = λ_A(n) + λ_Z(n)` with the channels named, i.e. `li_identity_sym`’s limit split into its '
         'pole-and-Γ part and its prime part, each part’s δ → 0⁺ limit shown to exist -- two limit lemmas over '
         '`EF.literatureRHS`’s summands at the symmetric family, the last item of the bridge. Not attempted at this act.')
    o = append_to(OT, NL + t + NL)
    o['line'] = line_of(OT, WO6)
    put_json('b566_price.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes, prefix %(prefix)s)' % o)


def findings():
    guard_absent(FIND, FH6)
    s, e, tj = jl('b566_scores.json'), _e0(), jl('b566_trials.json')
    wj, cl, pj = jl('b566_weight.json'), jl('b566_complete_line.json'), jl('b566_price.json')
    cj = jl('b566_ceiling.json')
    k = s['kstate']
    t = ['', FH6, '',
         '*Filed at b566 on the author’s ruling `(R176)`(3). Banks: relay `data/b566_step1_license.txt`, `data/b566_step1_closure.txt`, '
         '`data/b566_step1_distance.txt`, `data/b566_vendor_digests.json`, `data/b566_trials.txt` (with `.json`), '
         '`data/b566_trial_a_build.txt`, `data/b566_trial_b_build.txt`, `data/b566_route.txt`, `data/b566_eq_statement.txt`, '
         '`data/b566_prints.txt`, `data/b566_provenance.txt`, `data/b566_e0.txt`, `data/b566_reprint_summary.txt`. Nothing about '
         'the zeros of ζ is claimed beyond the compiled statements’ own words.*', '',
         '**Step one -- the licence and the toolchain trial.** Bulka’s licence at `35df682f` is the Apache License 2.0 (Copyright '
         '2026 Nicholas Bulka; section 4 permits redistribution with the licence, notices kept and changes marked); the repository '
         'carries no NOTICE file. The converse `LiCriterion.positivity_implies_RH` (Lc/LiCriterion/ReverseDirection.lean :397) has '
         'a closure of %s modules in the tree; the equality lemma consumes `taylorCoeff_eq_li_symmetrized` (Fidelity.lean :124), whose '
         'closure of 33 contains it, so the vendored set is the 33. The Mathlib distance is 129 commits (51e6992e an ancestor of '
         'de5ce8a9, 2026-08-03 to 2026-08-11, 1156 files). Trial (a), the backport at v4.33.0-rc2 / 51e6992e: %d of 33 modules '
         'called, %d exit 0, `Hadamard.General.Factorization` exits 1 on three unknown identifiers (`ite_eq_right` twice, '
         '`ite_eq_left` once -- core lemmas that enter Lean at v4.34.0-rc1, Init/Core.lean :1179, :1188), five modules blocked '
         'downstream of it; the converse’s own closure builds clean there. Trial (b), the forward move to v4.34.0-rc1 / de5ce8a9: '
         'the kernel’s %d modules (57 of Zeta23, 22 of the programme) all exit 0 with no source edit -- with 2749 warning lines, '
         '2044 of them deprecations the move introduces, and no error. **The route is (b)**, the only clean trial; the vendored '
         'set built on it (33 of 33 exit 0), and every existing `AxiomCheck*.lean` of the kernel re-elaborated there: 469 prints '
         'at the standard three or less, none moved of the 131 an earlier bank carries.'
         % (s.get('n_conv'), tj['a']['called'], tj['a']['ok'], tj['b']['modules']), '',
         '**Step two -- the equality lemma.** `li_coeff_eq_taylorCoeff : LiCoeff (n + 1) = (LiCriterion.taylorCoeff '
         'LiCriterion.riemannXi n).re`, its statement banked before the build. (E1) `carrierEquiv`: Zeta23’s `IsNontrivialZero` and '
         'Bulka’s `NontrivialZero` print the same predicate. (E2) `analyticOrderAt_xi_eq_zeta`: on 0 < Re ρ, ρ ≠ 1, the order of ξ '
         'is the order of ζ, since near ρ ξ = (½ s(s − 1))·Λ and ζ = Γℝ⁻¹·Λ with both cofactors analytic and nonzero there '
         '(`riemannZeta_def_of_ne_zero`, `Gammaℝ_ne_zero_of_re_pos`, `differentiableAt_completedZeta`, `differentiable_Gammaℝ_inv`, '
         '`analyticOrderAt_mul`, `analyticOrderAt_congr`); no Γ fact was missing at the pin. (E3) `neg_term_eq`: the reflected half '
         'of Bulka’s summand is `liTerm (n + 1)` at the paired zero. (E4) the real part of the summable symmetrized sum is the sum '
         'of real parts, split into the direct and the reflected sums, equal by the pairing and the multiplicity’s invariance.', '',
         '**Step three -- the composition.** `li_nonneg_iff_rh : (∀ n, 0 ≤ LiCoeff n) ↔ RiemannHypothesis` -- `←` the kernel’s '
         '`rh_imp_li_nonneg`, `→` Bulka’s `positivity_implies_RH` through the equality lemma and `rh_equiv_mathlib` -- and '
         '`arith_limit_nonneg_iff_rh`, the same through `li_identity_sym`. Every declaration of the module (12 theorems, 3 '
         'definitions) and the 12 terminals it consumes print [propext, Classical.choice, Quot.sound]; `RiemannHypothesis` and '
         '`riemannZeta` are declared in `Mathlib.NumberTheory.LSeries.RiemannZeta`; the 12 theorems grade DERIVES. main moved by '
         'fast-forward and **v0.9 = `%s`** (tag object `%s`) was pushed after main read back; both trial branches are pushed by '
         'name and kept.' % (k['v09'][:7], k['v09obj'][:7]), '',
         '**The scores.** H19a %s; H19b %s; H19c %s; H19d %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s; the seat’s (S1) %s, '
         '(S2) %s, (S3) %s.' % tuple(w_(s.get(x)) for x in ('h19a', 'h19b', 'h19c', 'h19d', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1',
                                                            's2', 's3')), '',
         '**Entered beside it.** The audit at its weight (FINDINGS :%s); the ceiling sentence of `(R176)`(2) beside README :117 and '
         'REGISTRY :952 (now :%s and :%s); the composition’s line (FINDINGS :%s); the residue chain priced at the LI-WEIL-BRIDGE '
         'work-order (OPEN_TRAILS :%s); correspondence rows %s-%s. **The ceiling’s second amendment** -- “Li’s criterion is compiled '
         'over Mathlib’s zeros in the programme’s kernel, its converse vendored from Bulka at 35df682f” -- is the author’s to write at '
         'the closing, as `(R176)`(3) orders; it is not written here.'
         % (wj.get('line'), cj['files']['README.md']['new_line'], cj['files']['REGISTRY.md']['new_line'], cl.get('line'),
            pj.get('line'), ROW_ACT6, ROW_T[-1]), '',
         '**Next.** b567 is GRH-Weil act three, as `(R175)`(6) fixed it and `(R176)`(7) carries it: LFunction χ on 0 < Re s by Abel '
         'summation, H18a-H18c unchanged.', '',
         '*Nothing deposits; nothing at Zenodo written; no existing statement of any kernel changed; no sentence here claims priority; '
         'nothing here is a statement about RH or any zero beyond the compiled statements’ own words.*', '']
    o = append_to(FIND, NL.join(t))
    o['heading_line'] = line_of(FIND, FH6)
    put_json('b566_findings.json', o)
    print('  FINDINGS.md:%s (the entry)' % o['heading_line'])


def rows():
    for r in (ROW_ACT6,) + ROW_T:
        if [l for l in rd(CORR).split(NL) if l.startswith('| %s |' % r)]:
            sys.exit('### ROW %s ALREADY PRESENT' % r)
    s, e = jl('b566_scores.json'), _e0()
    k = s['kstate']
    chk = {r['name'].split('.')[-1]: ' '.join(r['check'].split()) for r in e['rowgen']}
    pin = 'v0.9 = %s' % k['v09'][:7]
    rel = '`SIDE-explicit-formula/SIDEExplicitFormula/LiCriterionBridge.lean` (%s)' % pin
    act = [ROW_ACT6,
           '**THE CONVERSE VENDORED AND LI’S CRITERION COMPOSED** (b566, under (R176)(3)). SIDE-explicit-formula %s: the converse '
           'of Li’s criterion vendored from github.com/nicholasbulka/li-criterion-rh-equivalence-lean at 35df682f (33 modules, '
           'Apache 2.0, bodies byte-identical) and consumed by name; the kernel moved to Lean v4.34.0-rc1 and Mathlib de5ce8a9 after '
           'the trial both ways; the equality lemma identifies LiCoeff (n + 1) with the real part of the vendored Taylor '
           'coefficient over Mathlib’s zeros; li_nonneg_iff_rh and arith_limit_nonneg_iff_rh composed. Nothing here proves RH.' % pin,
           rel + ' : ' + ', '.join('`%s%s`' % (NSB, n) for n in TERMS6 + ['analyticOrderAt_xi_eq_zeta']),
           '15 of 15 declarations and 12 of 12 consumed terminals: [propext, Classical.choice, Quot.sound], no sorryAx (relay '
           'data/b566_prints.txt, data/b566_e0.txt)',
           ' ; '.join('`%s` DERIVES' % n for n in TERMS6 + ['analyticOrderAt_xi_eq_zeta']),
           'LANDED on main by fast-forward, v0.9 pushed after main read back; the trial branches vendor-bulka-backport-b566 and '
           'vendor-bulka-forward-b566 pushed by name and kept; nothing deposits; nothing at Zenodo written.']
    out = []
    r2 = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + act, capture_output=True, text=True, encoding='utf-8')
    out.append(dict(row=ROW_ACT6, exit=r2.returncode, tail=(r2.stdout + r2.stderr)[-300:]))
    for rn, n in zip(ROW_T, TERMS6):
        cells = [rn, '**%s** (b566, under (R176)(3)), SIDE-explicit-formula %s: `%s`.' % (n, pin, chk.get(n, '')),
                 rel + ' : `%s%s`' % (NSB, n),
                 "'%s%s' depends on axioms: [propext, Classical.choice, Quot.sound] (relay data/b566_prints.txt)" % (NSB, n),
                 '`%s` DERIVES' % n,
                 'LANDED at %s; Mathlib`s RiemannHypothesis and riemannZeta (declared in Mathlib.NumberTheory.LSeries.RiemannZeta); '
                 'no premise.' % pin]
        r3 = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells, capture_output=True, text=True, encoding='utf-8')
        out.append(dict(row=rn, exit=r3.returncode, tail=(r3.stdout + r3.stderr)[-300:]))
    put_json('b566_rows.json', dict(rows=out, act=act))
    print(json.dumps(out, ensure_ascii=False, indent=1)[:1500])


def rowgen_diff():
    sys.path.insert(0, os.path.join(T, 'rowgen'))
    import rowgen as RG
    recs = _e0().get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = "'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or [])) if isinstance(r.get('axioms'), list) else (r.get('axioms') or '')
    L = ['b566 -- READING (5): THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE MERGED RECORDS AGAINST CORRESPONDENCE ROWS %s-%s' % (ROW_ACT6, ROW_T[-1]), '']
    for rn in (ROW_ACT6,) + ROW_T:
        rowtxt = [l for l in rd(CORR).split(NL) if l.startswith('| %s |' % rn)]
        out = RG.diff(recs, NL.join(rowtxt))
        L.append('### row %s found: %s ; records %d' % (rn, bool(rowtxt), len(recs)))
        L += ['    ' + str(x) for x in out]
    put_txt('b566_rowgen.txt', L)
    print(NL.join(L))



def trail():
    guard_absent(OT, HEADING6)
    s = jl('b566_scores.json')
    k = s['kstate']
    f, wj, cl, pj, cj = (jl(x) for x in ('b566_findings.json', 'b566_weight.json', 'b566_complete_line.json', 'b566_price.json',
                                         'b566_ceiling.json'))
    t = ['', HEADING6, '',
         '**(R176) ratified.** (1) The audit at its weight. (2) The ceiling sentence amended in the author’s words. (3) Branch (i) '
         'of (R175)(3): the converse vendored -- the licence and the toolchain trial, the equality lemma, the composed criterion. '
         '(4) H19a-H19d fixed. (5) Arda’s clone deleted after its banks re-verified; Bulka’s kept. (6) The residue chain priced, '
         'not attempted. (7) b567 is GRH-Weil act three.', '',
         '**Entered:** FINDINGS.md:%s (the weight line), :%s (the composition’s line), :%s (the entry); README.md:%s and '
         'REGISTRY.md:%s (the ceiling sentence of (R176)(2)); OPEN_TRAILS.md:%s (the residue chain priced at the LI-WEIL-BRIDGE '
         'work-order); SIDE-global-section CORRESPONDENCE.md rows %s-%s; SIDE-explicit-formula main = **v0.9** = `%s` (tag object '
         '`%s`), the trial branches vendor-bulka-backport-b566 (`%s`) and vendor-bulka-forward-b566 (`%s`) pushed by name and kept.'
         % (wj.get('line'), cl.get('line'), f.get('heading_line'), cj['files']['README.md']['new_line'],
            cj['files']['REGISTRY.md']['new_line'], pj.get('line'), ROW_ACT6, ROW_T[-1], k['v09'][:7], k['v09obj'][:7],
            k['back'][:7], k['fwd'][:7]), '',
         '**Step one:** the licence Apache 2.0 (H19a %s); the converse’s closure %s modules, the vendored set 33 (Fidelity’s); the '
         'distance 129 commits; trial (a) 3 errors in one module, 5 blocked; trial (b) 79 of 79 clean (H19b %s); **the route (b), '
         'the forward move to Lean v4.34.0-rc1 / Mathlib de5ce8a9.** **Step two:** li_coeff_eq_taylorCoeff (H19c %s). **Step three:** '
         'li_nonneg_iff_rh and arith_limit_nonneg_iff_rh at the standard three, DERIVES (H19d %s).'
         % (w_(s['h19a']), s.get('n_conv'), w_(s['h19b']), w_(s['h19c']), w_(s['h19d'])), '',
         '**The ceiling’s second amendment** is the author’s word at the closing, as (R176)(3) orders; not written here.', '',
         '**Next:** b567, GRH-WEIL act three, as `(R175)`(6) fixes it (H18a-H18c).', '',
         '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s.'
         % tuple(w_(s.get(x)) for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
         '**One fast-forward onto `main`, one tag pushed after main read back, no `sorry` on any `main`.** Nothing deposits; nothing '
         'at Zenodo written; no existing statement changed; no existing `.lean` file edited; no Zeta23 file edited or added; no '
         'vendored body edited; no monograph byte changed; ERRATA untouched; the ceiling gains one sentence as ruled; row U1 '
         'unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH or any zero '
         'beyond the compiled statements’ own words.', '']
    o = append_to(OT, NL.join(t))
    o['line'] = line_of(OT, HEADING6)
    put_json('b566_trail.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


def desk():
    s, tj = jl('b566_scores.json'), jl('b566_trials.json')
    L = ['=' * 104, 'b566 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### (R176)`S FOUR.', '-' * 104,
         '  **(H19a)** ### **%s.** -- Bulka`s LICENSE at 35df682f is the Apache License 2.0, whose section 4 permits redistribution '
         'with the licence given, notices kept and changes marked (data/b566_step1_license.txt).' % w_(s['h19a']),
         '  **(H19b)** ### **%s.** -- trial (b), the forward move, built the kernel`s %d modules clean with no source edit; trial (a) '
         'did not (data/b566_trials.txt).' % (w_(s['h19b']), tj['b']['modules']),
         '  **(H19c)** ### **%s.** -- analyticOrderAt_xi_eq_zeta compiles from Mathlib`s completedRiemannZeta and its relation to '
         'riemannZeta on the strip (riemannZeta_def_of_ne_zero, differentiableAt_completedZeta) with Gammaℝ_ne_zero_of_re_pos and '
         'differentiable_Gammaℝ_inv; no Gamma fact was missing at the pin; std3, DERIVES (data/b566_e0.txt).' % w_(s['h19c']),
         '  **(H19d)** ### **%s.** -- li_nonneg_iff_rh prints [propext, Classical.choice, Quot.sound], no sorryAx and no premise '
         '(data/b566_prints.txt).' % w_(s['h19d']), '',
         '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- H19a %s.' % (w_(s['n1']), w_(s['h19a'])),
         '  **(N2)** ### **%s.** -- the backport did not build clean: Hadamard.General.Factorization exits 1 on ite_eq_right and '
         'ite_eq_left (core lemmas from v4.34.0-rc1), five modules blocked; the forward trial was needed and is the route.' % w_(s['n2']),
         '  **(N3)** ### **%s.** -- the converse`s closure within Bulka`s tree is %s modules (the vendored set, Fidelity`s closure, '
         'is 33).' % (w_(s['n3']), s.get('n_conv')),
         '  **(N4)** ### **%s.** -- H19c %s from completedRiemannZeta facts at the pin.' % (w_(s['n4']), w_(s['h19c'])),
         '  **(N5)** ### **%s.** -- li_nonneg_iff_rh and arith_limit_nonneg_iff_rh print the standard three and grade DERIVES; v0.9 '
         'tagged and read back.' % w_(s['n5']),
         '  **(N6)** ### **%s.** -- no existing .lean file of any kernel changed (SIDE-explicit-formula v0.8 -> v0.9: additions and '
         'config only), every other kernel main at its pre-act head, SIDE-global-section the ledger rows alone, the kept branches '
         'at their tips; nothing deposits; nothing at Zenodo.' % w_(s['n6']), '',
         '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the backport did not build clean (3 errors in one module).' % w_(s['s1']),
         '  **(S2)** ### **%s.** -- the forward trial built every kernel module with no source edit (79 of 79 exit 0).' % w_(s['s2']),
         '  **(S3)** ### **%s.** -- its first clause fails: the (E2) proof uses Mathlib names beyond READING (4)`s list: %s. Its '
         'second clause holds: the equality lemma and both composed theorems print the standard three.' % (w_(s['s3']), ', '.join(s['s3_beyond'])), '',
         '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % (sum(1 for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6') if s[x]), sum(1 for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6') if s[x] is False),
            sum(1 for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6') if s[x] is None),
            sum(1 for x in ('s1', 's2', 's3') if s[x]), sum(1 for x in ('s1', 's2', 's3') if not s[x])),
         '### ### **(R176) : H19a %s ; H19b %s ; H19c %s ; H19d %s.**' % (w_(s['h19a']), w_(s['h19b']), w_(s['h19c']), w_(s['h19d'])), '']
    L += rd(os.path.join(D, 'b566_defects.txt')).rstrip().split(NL)
    put_txt('b566_desk_notes.txt', L)
    print(NL.join(L[:40]))


def components():
    L = ['=' * 132, 'b566 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b566_reads.txt', 'b566_weight.txt', 'b566_ceiling.txt', 'b566_arda_rehash.txt', 'b566_arda_delete.txt',
              'b566_step1_closure.txt', 'b566_step1_distance.txt', 'b566_trials.txt', 'b566_trial_b_setup.txt', 'b566_route.txt',
              'b566_eq_statement.txt', 'b566_prints.txt', 'b566_provenance.txt', 'b566_e0.txt', 'b566_reprint_summary.txt',
              'b566_rowgen.txt', 'b566_branches.txt', 'b566_scores.txt'):
        L.append('### relay data/%s' % n)
        L.extend('  ' + x for x in rd(os.path.join(D, n)).rstrip().split(NL))
        L.append('')
    L.append('### relay data/b566_step1_license.txt -- the licence printed whole (%d lines), not repeated here' % len(rd(os.path.join(D, 'b566_step1_license.txt')).split(NL)))
    L.append('### relay data/b566_kernel_push_out.txt -- the kernel push, its capture:')
    L.extend('  ' + x for x in rd(os.path.join(D, 'b566_kernel_push_out.txt')).rstrip().split(NL))
    for n, key in (('b566_weight.json', 'line'), ('b566_complete_line.json', 'line'), ('b566_price.json', 'line'),
                   ('b566_findings.json', 'heading_line'), ('b566_trail.json', 'line')):
        L.append('### relay data/%s -- %s %s' % (n, key, jl(n).get(key)))
    L.append('### relay data/b566_rows.json -- rows %s' % ', '.join('%s exit %s' % (r['row'], r['exit']) for r in jl('b566_rows.json')['rows']))
    put_txt('b566_components.txt', L)
    print('  written: b566_components.txt (%d lines)' % len(L))


def main(argv):
    cmd = argv[0] if argv else ''
    fn = dict(reads=reads, weight=weight, ceiling=ceiling, arda=arda, trials=trials, route=route, e0=e0, scores=scores, complete_line=complete_line, price=price, findings=findings, rows=rows, rowgen_diff=rowgen_diff, trail=trail, desk=desk, components=components).get(cmd)
    if not fn:
        print(__doc__)
        return 2
    r = fn()
    return r or 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
