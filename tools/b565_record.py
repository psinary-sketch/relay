# -*- coding: utf-8 -*-
"""b565_record.py -- THE AUDIT OF TWO PUBLIC FORMALIZATIONS; THE SUPERSEDED GRADE IN A READABLE CELL; HOUSEKEEPING, UNDER (R175).
### `python tools/b565_record.py reads | housekeeping | supersede <stage> | audit | fieldline | conditional | findings | rows |
### trail | scores | desk | components | defects`. b564's helpers are IMPORTED, never copied. This file deletes nothing.
"""
import io, json, os, re, subprocess, sys, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b564_record as Z4  # noqa: E402
Q = Z4.Q
PP, FIND, OT, CORR, EF = Q.PP, Q.FIND, Q.OT, Q.CORR, Q.EF
NL = chr(10)
rd, g, append_to, guard_absent, poss, line_of = Q.rd, Q.g, Q.append_to, Q.guard_absent, Q.poss, Q.line_of
put_txt, put_json, jl, w_ = Q.put_txt, Q.put_json, Q.jl, Q.w_
parse_prints, STD3 = Z4.parse_prints, Q.STD3
PRIOR_RELAY = '58d73d24'
PRIOR_PP = '5c50649'
PRIOR_GS = '1135887'
V08 = '6ec71b302998'
AUD = os.path.join('D:' + os.sep, 'audit-b565')
TERM = 'li_identity_of_exchange'
# ### b565's own pre-act heads (b564's, with SIDE-explicit-formula at v0.8 and SIDE-global-section at b564's row 400)
PRE_HEADS5 = dict(Z4.PRE_HEADS, **{'SIDE-explicit-formula': '6ec71b3', 'SIDE-global-section': PRIOR_GS})
KEPT5 = dict(Z4.KEPT_TIPS, **{'grh-weil-b564': '6ec71b302998'})
ROW_AUD = '402'
Z23_OURS, Z23_ARDA = '3635e748', 'fbdc36bb'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def _lines(L, path, a, b, label, cap=400):
    ls = rd(path).split(NL)
    L.append('### %s :%d-:%d' % (label, a, b))
    L += ['    %5d | %s' % (i, ls[i - 1][:cap]) for i in range(a, min(b, len(ls)) + 1) if ls[i - 1].strip()]


def reads():
    L = ['b565 -- READING (1): THE READS, PRINTED BY PATH AND LINE', '']
    pa = os.path.join(D, 'b564_prior_art.txt')
    t = rd(pa).split(NL)
    k = [i + 1 for i, l in enumerate(t) if 'THE HITS THAT ARE FORMALIZATIONS' in l]
    L.append('### relay data/b564_prior_art.txt (sha256 %s)' % hashlib.sha256(open(pa, 'rb').read()).hexdigest()[:16])
    if k:
        L += ['    %5d | %s' % (i, t[i - 1][:300]) for i in range(k[0], len(t) + 1) if t[i - 1].strip()]
    _lines(L, FIND, 4729, 4750, 'FINDINGS.md (b536`s prior-art record and its audit form)', 300)
    _lines(L, os.path.join(EF, 'README.md'), 12, 30, 'SIDE-explicit-formula README.md (the vendoring record of Zeta23)', 300)
    _lines(L, os.path.join(EF, 'NOTICE'), 1, 12, 'SIDE-explicit-formula NOTICE')
    _lines(L, os.path.join(EF, 'lakefile.toml'), 1, 11, 'SIDE-explicit-formula lakefile.toml')
    for n in (8022, 8057, 8059):
        _lines(L, OT, n, n, 'OPEN_TRAILS.md ((R82)`s condition, (R83))', 500)
    _lines(L, FIND, 6136, 6136, 'FINDINGS.md (the field entry as b564 wrote it)', 3000)
    for r in ('395', '397'):
        cr = [l for l in rd(CORR).split(NL) if l.startswith('| %s |' % r)]
        L.append('### CORRESPONDENCE row %s : %s' % (r, cr[0][:900] if cr else 'NOT FOUND'))
    tt = os.path.join(T, 'terminal_table.py')
    _lines(L, tt, 18, 23, 'tools/terminal_table.py (the synonym map`s note)')
    _lines(L, tt, 50, 50, 'tools/terminal_table.py (GRADE_RE)')
    _lines(L, tt, 139, 163, 'tools/terminal_table.py (SUPERSEDE_RE, supersede)')
    _lines(L, tt, 219, 227, 'tools/terminal_table.py (SYNONYMS, synonym)')
    L.append('### tools/terminal_table.py searched for a tier column: %d lines carry "tier" (case-insensitive)'
             % sum(1 for l in rd(tt).split(NL) if 'tier' in l.lower()))
    fs = os.path.join(T, 'FERRY_STANDING.md')
    ls = rd(fs).split(NL)
    for i, l in enumerate(ls):
        if l.startswith('- **C18**') or l.startswith('- **A1**') or l.startswith('- **A3**') or l.startswith('## AUTHOR-RULED'):
            L.append('    FERRY_STANDING.md:%d | %s' % (i + 1, l[:300]))
    put_txt('b565_reads.txt', L)
    print('  lines %d ; NOT FOUND %d ; written: b565_reads.txt' % (len(L), sum(1 for l in L if 'NOT FOUND' in l)))


ROW_SUP = '401'


def supersede_row():
    if [l for l in rd(CORR).split(NL) if l.startswith('| %s |' % ROW_SUP)]:
        sys.exit('### ROW %s ALREADY PRESENT' % ROW_SUP)
    cells = [ROW_SUP,
             '**li_identity_of_exchange’S GRADE ON THE GRADE AXIS, AND ITS TIER** (b565, under the author’s ruling (R175)(4)): '
             'the grade axis and the tier axis are distinct. The terminal is a theorem under a named premise, and the premise, '
             'the exchange of b560, is false as stated for n ≥ 1 on b561’s reading (relay data/b561_decay_read.txt (7)); its '
             'docstring says so (marked at 61e3551). Its grade is therefore INTERFACES, and its tier T2 by the tier law’s clause. '
             'This row’s grade cell replaces row 397’s for this terminal alone; rows 395 and 397 stand unedited above. The '
             'ledger has no tier column, so the tier is written in words in the grade cell.',
             '`SIDE-explicit-formula/SIDEExplicitFormula/LiWeil.lean` -- `SIDEExplicitFormula.LiWeil.li_identity_of_exchange` '
             '(unchanged at v0.8 = 6ec71b3)',
             '[propext, Classical.choice, Quot.sound] (relay data/b560_e0.txt; the file unchanged since 61e3551)',
             'SUPERSEDES row 397: INTERFACES -- `li_identity_of_exchange`; tier T2 by the tier law’s clause; the premise false as '
             'stated for n ≥ 1, so the conditional certifies nothing about LiCoeff',
             'Written 2026-09-30 (b565) through `relay/tools/corr_row.py`; the rule is `supersede` in `relay/tools/terminal_table.py`; '
             'the synonym map maps INTERFACES-on-false-premise to INTERFACES on the grade axis (b565).']
    r = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells, capture_output=True, text=True, encoding='utf-8')
    print(r.stdout[-400:], r.stderr[-300:])
    n = [i + 1 for i, l in enumerate(rd(CORR).split(NL)) if l.startswith('| %s |' % ROW_SUP)]
    put_json('b565_suprow.json', dict(cells=cells, exit=r.returncode, line=n[0] if n else None))


def _check_block(text, name):
    """### Lean`s `#check @name` output: the line opening `name :` (Lean 4.33/4.34 print it without the `@`; an `@name :` form is
    ### read too) and its indented continuation."""
    ls = (text or '').split(NL)
    for i, l in enumerate(ls):
        if l.startswith(name + ' :') or l.startswith('@' + name + ' :'):
            out = [l]
            for m in ls[i + 1:]:
                if m.startswith(' '):
                    out.append(m)
                else:
                    break
            return out
    return []


def _print_block(text, head):
    ls = (text or '').split(NL)
    for i, l in enumerate(ls):
        if l.startswith(head):
            out = [l]
            for m in ls[i + 1:]:
                if m.startswith(' ') or m.startswith('|'):
                    out.append(m)
                else:
                    break
            return out
    return []


AUDIT = {
    'bulka': dict(url='https://github.com/nicholasbulka/li-criterion-rh-equivalence-lean',
                  terminals=['li_criterion', 'li_coefficients_eq_zero_sum', 'LiCriterion.li_criterion_rh_iff',
                             'LiCriterion.positivity_implies_RH', 'LiCriterion.li_pos_implies_rh',
                             'LiCriterion.li_equiv_from_weighted_sum_formula', 'LiCriterion.rh_equiv_mathlib',
                             'LiCriterion.biconditional_rh_li_of_hadamard_order_one', 'LiCriterion.xi_hasFiniteOrder',
                             'LiCriterion.xi_order_le_one', 'LiCriterion.summable_li_symmetrized',
                             'LiCriterion.taylorCoeff_eq_li_symmetrized'],
                  checks=['li_criterion', 'li_coefficients_eq_zero_sum', 'LiCriterion.li_criterion_rh_iff',
                          'LiCriterion.positivity_implies_RH', 'LiCriterion.li_equiv_from_weighted_sum_formula',
                          'LiCriterion.rh_equiv_mathlib'],
                  defs=['def LiChallenge.riemannXi', 'def LiChallenge.taylorCoeff', 'def LiChallenge.phi', 'def LiChallenge.logDeriv',
                        'def LiChallenge.NontrivialZero', 'def LiCriterion.riemannXi', 'def LiCriterion.NontrivialZero',
                        'def RiemannHypothesis'],
                  sorry=['b565_audit_bulka_sorry_XiOrderBridge_ReverseDirection_Fidelity_RHBridge.json',
                         'b565_audit_bulka_sorry_Solution_ChallengeDeps.json']),
    'arda': dict(url='https://github.com/DrMurphyIsIn/Arda',
                 terminals=['RvMBridge27.bl_explicit_formula', 'RvMBridge27.liValue', 'RvMBridge27.xi_logDeriv_deriv_eq',
                            'RvMBridge23.local_count_sum', 'RvMBridge24.stripDerivBound', 'RvMBridge25.bl_explicit_formula_of_two',
                            'RvMBridge25.liValue_of_two'],
                 checks=['RvMBridge27.bl_explicit_formula', 'RvMBridge27.liValue', 'RvMBridge25.bl_explicit_formula_of_two'],
                 defs=['def RvMBridge15.BombieriLagarias.liKernel', 'def RvMBridge15.BombieriLagarias.liZeroSum',
                       'def RvMBridge15.BombieriLagarias.archSide', 'def RvMBridge15.BombieriLagarias.zetaLogDerivReg',
                       'def RvMBridge15.BombieriLagarias.eta', 'def RvMBridge15.BombieriLagarias.finiteSide',
                       'def RvMBridge15.LiValue', 'def WeilExplicit.zeroMult', 'def RvMBridge22.LocalCountSum',
                       'def RvMBridge22.StripDerivBound'],
                 sorry=['b565_audit_arda_sorry_E6Bridge27.json', 'b565_audit_arda_sorry_zeta23.json']),
}


def _grade(name, check, ax, sorry_tot, repo):
    """### THE E0 GRADE OF A PRINTED TERMINAL, one clause. Only what was printed is graded."""
    if ax is None:
        return 'NOT SCORABLE', 'no print (the build did not complete, or the name did not resolve)'
    if 'sorryAx' in ax or sorry_tot.get('sorry', 0) or sorry_tot.get('axioms'):
        return 'SHELL', 'its print or closure carries sorryAx, a sorry or a declared axiom'
    if not set(ax) <= set(STD3):
        return 'SHELL', 'its print carries an axiom beyond the standard three: %s' % sorted(set(ax) - set(STD3))
    c = ' '.join(check)
    prem = re.findall(r'\((h\w*) : ([^)]{0,160})\)', c) + re.findall(r'→\s+(RvMBridge22\.\w+|Hadamard\.\w+[^→]{0,60})\s+→', c)
    named = [p for p in prem if isinstance(p, tuple) and re.match(r'(RvMBridge22|Hadamard|LiCriterion)\.', p[1].strip())] + \
            [p for p in prem if isinstance(p, str)]
    if named:
        return 'INTERFACES', 'its statement takes a named premise of the repository`s own: %s' % named[:3]
    return 'DERIVES', 'the standard three, no sorry in its closure, no named premise in its statement'


def audit():
    out, L = {}, ['b565 -- COMPONENT 3: THE AUDIT OF TWO PUBLIC FORMALIZATIONS, READ BY STATEMENT AND PRINT AT THEIR PINS, UNDER (R175)(2)', '',
                  '### A print is what Lean printed in the repository`s own environment, from a file written in D:/audit-b565 outside the',
                  '### clone; a statement is Lean`s `#check`; a definition is Lean`s `#print`. Nothing is graded from a README.', '']
    for repo, spec in AUDIT.items():
        cj = jl('b565_audit_%s_clone.json' % repo)
        info = rd(os.path.join(D, [f for f in os.listdir(D) if f.startswith('b565_audit_%s_info' % repo)][-1]))
        build = rd(os.path.join(D, 'b565_audit_%s_build.txt' % repo)) if os.path.exists(os.path.join(D, 'b565_audit_%s_build.txt' % repo)) else ''
        pr = rd(os.path.join(D, 'b565_audit_%s_prints.txt' % repo)) if os.path.exists(os.path.join(D, 'b565_audit_%s_prints.txt' % repo)) else ''
        P0 = parse_prints(pr)
        stot = {'sorry': 0, 'admit': 0, 'axioms': []}
        for sj in spec['sorry']:
            j = jl(sj)
            for k in ('sorry', 'admit'):
                stot[k] += j.get('totals', {}).get(k, 0)
            stot['axioms'] += j.get('totals', {}).get('axioms', [])
        L += ['=' * 104, '### %s -- %s' % (repo.upper(), spec['url']), '=' * 104,
              '### THE PIN: HEAD %s (cloned %s into %s)' % (cj.get('head'), cj.get('at'), cj.get('dir')),
              '### THE TOOLCHAIN AND THE MATHLIB REV (from the project`s own files):']
        L += ['    ' + l.strip() for l in info.split(NL) if 'leanprover/lean4' in l or 'package mathlib' in l or 'package Zeta23' in l
              or ('rev =' in l and 'formal-math' not in l and len(l) < 120)][:6]
        L += ['### THE BUILD (its own lake; relay data/b565_audit_%s_build.txt):' % repo]
        L += ['    ' + l for l in build.split(NL) if l.startswith('###') or 'error' in l.lower()][:30]
        L += ['### THE PRINTS, VERBATIM (relay data/b565_audit_%s_prints.txt; its header: %s)' % (repo, pr.split(NL)[0][:160] if pr else 'NO PRINT FILE')]
        rows = {}
        for n in spec['terminals']:
            ax = P0.get(n)
            raw = [l for l in pr.split(NL) if l.startswith("'%s'" % n)]
            L.append('    %s' % (raw[0][:300] if raw else '### %s -- NOT PRINTED' % n))
            rows[n] = dict(axioms=ax)
        L += ['### THE STATEMENTS (Lean`s #check):']
        for n in spec['checks']:
            blk = _check_block(pr, n)
            L += ['    ' + x for x in blk] if blk else ['    ### %s -- NO #check' % n]
            if n in rows:
                rows[n]['check'] = blk
        L += ['### THE DEFINITIONS THEY UNFOLD TO (Lean`s #print, first lines):']
        for h in spec['defs']:
            blk = _print_block(pr, h)
            L += ['    ' + x[:200] for x in blk[:6]] if blk else ['    ### %s -- NOT PRINTED' % h]
        L.append('### THE CLOSURE READ FOR sorry, admit AND axiom (lexical, comment-stripped; control: comparator/Challenge.lean reads sorry 2):'
                 ' sorry %d ; admit %d ; axioms %s' % (stot['sorry'], stot['admit'], stot['axioms'] or 'NONE'))
        L += ['### THE E0 GRADES:']
        for n in spec['terminals']:
            gname, why = _grade(n, rows[n].get('check') or [], rows[n]['axioms'], stot, repo)
            rows[n].update(grade=gname, why=why)
            L.append('    %-52s %-12s -- %s' % (n, gname, why))
        out[repo] = dict(head=cj.get('head'), rows=rows, sorry=stot, printed=len(P0))
        L.append('')
    put_txt('b565_audit_core.txt', L)
    put_json('b565_audit_core.json', out)
    print(NL.join(L))


def _w(v):
    return w_(v)


def scores():
    au = jl('b565_audit.json')
    sa, sn = jl('b565_supersede_after.json'), jl('b565_supersede_noop.json')
    b, a = au['bulka'], au['arda']
    conv = b['rows'].get('LiCriterion.positivity_implies_RH', {})
    h17a = None if conv.get('grade') == 'NOT SCORABLE' else (not b['converse_genuine'])
    h17b = None if a['rows'].get('RvMBridge27.bl_explicit_formula', {}).get('grade') == 'NOT SCORABLE' else (not a['bl_genuine'])
    only = sa['changed'] == ['SIDE-explicit-formula|SIDEExplicitFormula.LiWeil.%s SHELL -> INTERFACES' % TERM]
    cells = sa['term'].get('regenerated', {}).get('cells', [])
    row = [l for l in rd(CORR).split(NL) if l.startswith('| %s |' % ROW_SUP)]
    n5 = only and len(cells) == 1 and cells[0]['grade'] == 'INTERFACES' and bool(row) and 'tier T2' in row[0]
    # ### (N6) against b565's OWN pre-act heads (PRE_HEADS5): every kernel main unchanged, SIDE-global-section the ledger alone,
    # ### the kept branches at their tips local and remote, the deposit directory clean.
    mains = {kk: sorted(x for x in g(os.path.join(Q.DD, kk), 'diff', '--name-only', h, 'main').split(NL) if x.strip())
             for kk, h in PRE_HEADS5.items()}
    rem = {l.split('\t')[1].strip(): l.split('\t')[0] for l in g(EF, 'ls-remote', 'origin').split(NL) if '\t' in l}
    kept = all(g(EF, 'rev-parse', br).strip().startswith(t[:12]) and rem.get('refs/heads/' + br, '').startswith(t[:12])
               for br, t in KEPT5.items())
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    n6 = (all(not v for kk, v in mains.items() if kk != 'SIDE-global-section')
          and set(mains['SIDE-global-section']) <= {'CORRESPONDENCE.md'} and g(EF, 'rev-parse', 'main').strip().startswith(V08)
          and kept and dep)
    s = dict(h17a=h17a, h17b=h17b, n1=h17a, n2=h17b, n3=au.get('n3'), n4=au['bulka']['build_exit'] == 0 and au['arda']['build_exit'] == 0,
             n5=n5, n6=n6, s1=(h17a is False), s2=au.get('s2'), s3=(sn['changed'] == [] and only and len(sa['conflict_regenerated']) == len(sa['conflict_committed'])))
    L = ['b565 -- THE SCORES, READ OFF THE BANKS', ''] + ['    %-4s %s' % (x.upper(), _w(s[x])) for x in ('h17a', 'h17b', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')]
    L += ['### (N5) read on the row`s own cell (the table has no tier column): the table grade %s ; the row`s cell carries "tier T2" %s'
          % (cells[0]['grade'] if cells else None, bool(row) and 'tier T2' in row[0])]
    put_txt('b565_scores.txt', L)
    put_json('b565_scores.json', s)
    print(NL.join(L))


def housekeeping():
    L = ['b565 -- COMPONENT 1: HOUSEKEEPING, UNDER (R175)(5)', '']
    for sha_ in ('80346ab6', '9de84b16'):
        L.append('### relay %s : %s' % (sha_, g(ROOT, 'log', '-1', '--format=%s', sha_).strip()[:200]))
        L += ['    file: ' + x for x in g(ROOT, 'show', '--name-only', '--format=', sha_).split(NL) if x.strip()]
    L.append('### the process listing (step zero): relay data/b565_procs_stepzero.txt --')
    L += ['    ' + l for l in rd(os.path.join(D, 'b565_procs_stepzero.txt')).split(NL) if l.strip()]
    fs = rd(os.path.join(T, 'FERRY_STANDING.md')).split(NL)
    a4 = [(i + 1, l) for i, l in enumerate(fs) if l.startswith('- **A4**')]
    L.append('### tools/FERRY_STANDING.md clause A4 at :%s -- %s' % (a4[0][0] if a4 else None, a4[0][1][:260] if a4 else 'ABSENT'))
    L.append('### the VERSION line: %s' % next((l for l in fs if l.startswith('VERSION:')), 'ABSENT'))
    L.append('### the capture`s test (relay data/b565_capture_test.txt):')
    L += ['    ' + l for l in rd(os.path.join(D, 'b565_capture_test.txt')).split(NL) if l.startswith(('###', '    ('))]
    sr = rd(os.path.join(T, 'SUITE_README.md')).split(NL)
    L.append('### tools/SUITE_README.md (new, %d lines): %s' % (len(sr), [l for l in sr if 'placeholder' in l][:1]))
    put_txt('b565_housekeeping.txt', L)
    print(NL.join(L[-12:]))


# ================================================================================ COMPONENT 3: THE READINGS, THE GRADES, THE COMPARISONS
# ### Each reading is the seat's, of what Lean printed; its NEEDLES are strings that must stand verbatim in the banked Lean output
# ### (prints + reads), and the yield is printed per terminal. A print outside the standard three, a sorryAx or a closure sorry
# ### overrides any reading to SHELL (`_grade`, unchanged). INTERFACES = a premise in the statement itself (named, with where it
# ### is discharged if it is); ENCODES = a parameter zero set or a local RH Prop -- none is printed here.
XI_UNFOLD = 'fun s => 1 / 2 * s * (s - 1) * completedRiemannZeta₀ s + 1 / 2'
NTZ = '{ ρ // riemannZeta ρ = 0 ∧ 0 < ρ.re ∧ ρ.re < 1 }'
MRH = 'WHERE RiemannHypothesis : declared in module Mathlib.NumberTheory.LSeries.RiemannZeta'
MZ = 'WHERE riemannZeta : declared in module Mathlib.NumberTheory.LSeries.RiemannZeta'
STRIP = 'riemannZeta s = 0 → 0 < s.re ∧ s.re < 1 → s.re = 1 / 2'
ZS_COEF = ('none in the statement: the coefficient is the n-th Taylor coefficient at 0 of the log-derivative of ξ(1/(1 − z)), ξ '
           'unfolding to 1/2 · s(s − 1) · completedRiemannZeta₀ s + 1/2 over Mathlib`s completedRiemannZeta₀')
RH_M = 'Mathlib`s RiemannHypothesis (declared in Mathlib.NumberTheory.LSeries.RiemannZeta)'
RH_STRIP = ('the strip form ∀ s, riemannZeta s = 0 → 0 < Re s < 1 → Re s = 1/2, stated inline over Mathlib`s riemannZeta -- not a '
            'local Prop; LiCriterion.rh_equiv_mathlib proves it equivalent to Mathlib`s RiemannHypothesis')
ZS_NTZ = ('Mathlib`s riemannZeta zeros in the open strip, under the repository`s own name %s := ' + NTZ +
          ', each weighted by Mathlib`s analyticOrderNatAt of its ξ')
ZS_WX = ('Mathlib`s riemannZeta zeros in the open strip with |Im ρ| ≤ T, weighted by WeilExplicit.zeroMult ρ := (MeromorphicOn.divisor '
         'riemannZeta {s | 0 < Re s < 1} ρ).toNat, the repository`s own name (E6Bridge4) for the divisor of Mathlib`s riemannZeta')
READINGS = {
    'li_criterion': dict(zero_set=ZS_COEF, rh=RH_M, grade='DERIVES',
                         why='the standard three and no premise; its body is LiCriterion.li_criterion_rh_iff',
                         needles=['li_criterion : RiemannHypothesis ↔ ∀ (n : ℕ), 0 ≤ (LiChallenge.taylorCoeff LiChallenge.riemannXi n).re',
                                  'LiCriterion.li_criterion_rh_iff', MRH, XI_UNFOLD, 'WHERE completedRiemannZeta₀ : declared in module Mathlib.']),
    'li_coefficients_eq_zero_sum': dict(zero_set=ZS_NTZ % 'LiChallenge.NontrivialZero (ChallengeDeps)', rh='none in the statement',
                                        grade='DERIVES', why='the standard three and no premise',
                                        needles=['li_coefficients_eq_zero_sum : ∀ (n : ℕ),', NTZ,
                                                 'WHERE LiChallenge.NontrivialZero : declared in module ChallengeDeps',
                                                 'WHERE analyticOrderNatAt : declared in module Mathlib.']),
    'LiCriterion.li_criterion_rh_iff': dict(zero_set=ZS_COEF, rh=RH_M, grade='DERIVES',
                                            why='the standard three and no premise; its body applies biconditional_rh_li_of_hadamard_order_one '
                                                'to xi_hasFiniteOrder and xi_order_le_one, each printed at the standard three',
                                            needles=['LiCriterion.li_criterion_rh_iff : RiemannHypothesis ↔',
                                                     'LiCriterion.biconditional_rh_li_of_hadamard_order_one LiCriterion.xi_hasFiniteOrder LiCriterion.xi_order_le_one']),
    'LiCriterion.positivity_implies_RH': dict(zero_set='Mathlib`s riemannZeta zeros in the open strip, quantified in the conclusion',
                                              rh=RH_STRIP, grade='DERIVES',
                                              why='the standard three; its one premise is the positivity the direction converts, not an assumption about ζ',
                                              needles=['LiCriterion.positivity_implies_RH : (∀ (n : ℕ), 0 ≤ (LiCriterion.taylorCoeff LiCriterion.riemannXi n).re) →',
                                                       STRIP, MZ]),
    'LiCriterion.li_pos_implies_rh': dict(zero_set='Mathlib`s riemannZeta zeros in the open strip, quantified in the conclusion',
                                          rh=RH_STRIP, grade='DERIVES',
                                          why='the standard three; its one premise is the positivity the direction converts',
                                          needles=['LiCriterion.li_pos_implies_rh : (∀ (n : ℕ), 0 ≤ (LiCriterion.taylorCoeff LiCriterion.riemannXi n).re) →']),
    'LiCriterion.li_equiv_from_weighted_sum_formula': dict(
        zero_set=ZS_NTZ % 'LiCriterion.NontrivialZero (Lc.LiCriterion.Basic)', rh=RH_STRIP, grade='INTERFACES',
        premise='the summability of m(ρ)/‖ρ‖² and the weighted zero-sum formula for the coefficient, both premises in its statement',
        why='its statement takes the summability of m(ρ)/‖ρ‖² and the weighted zero-sum formula as premises',
        needles=['LiCriterion.li_equiv_from_weighted_sum_formula : (Summable fun ρ =>', 'WHERE LiCriterion.NontrivialZero : declared in module Lc.LiCriterion.Basic']),
    'LiCriterion.rh_equiv_mathlib': dict(zero_set='Mathlib`s riemannZeta zeros in the open strip, quantified', rh=RH_M + '; ' + RH_STRIP,
                                         grade='DERIVES', why='the standard three and no premise',
                                         needles=['LiCriterion.rh_equiv_mathlib : RiemannHypothesis ↔ ∀ (s : ℂ), ' + STRIP]),
    'LiCriterion.biconditional_rh_li_of_hadamard_order_one': dict(
        zero_set=ZS_COEF, rh=RH_M, grade='INTERFACES',
        premise='Hadamard.hasFiniteOrder ξ and Hadamard.order ξ ≤ 1, the repository`s own Props, discharged for its ξ by '
                'xi_hasFiniteOrder and xi_order_le_one in li_criterion_rh_iff',
        why='its statement takes the repository`s own Hadamard.hasFiniteOrder ξ and Hadamard.order ξ ≤ 1 as premises, discharged in li_criterion_rh_iff',
        needles=['Hadamard.hasFiniteOrder LiCriterion.riemannXi →', 'Hadamard.order LiCriterion.riemannXi ≤ 1 →']),
    'LiCriterion.xi_hasFiniteOrder': dict(zero_set='none in the statement', rh='none in the statement', grade='DERIVES',
                                          why='the standard three and no premise',
                                          needles=['LiCriterion.xi_hasFiniteOrder : Hadamard.hasFiniteOrder LiCriterion.riemannXi']),
    'LiCriterion.xi_order_le_one': dict(zero_set='none in the statement', rh='none in the statement', grade='DERIVES',
                                        why='the standard three and no premise',
                                        needles=['LiCriterion.xi_order_le_one : Hadamard.order LiCriterion.riemannXi ≤ 1']),
    'LiCriterion.summable_li_symmetrized': dict(zero_set=ZS_NTZ % 'LiCriterion.NontrivialZero (Lc.LiCriterion.Basic)',
                                                rh='none in the statement', grade='DERIVES', why='the standard three and no premise',
                                                needles=['LiCriterion.summable_li_symmetrized : ∀ (n : ℕ),']),
    'LiCriterion.taylorCoeff_eq_li_symmetrized': dict(zero_set=ZS_NTZ % 'LiCriterion.NontrivialZero (Lc.LiCriterion.Basic)',
                                                      rh='none in the statement', grade='DERIVES', why='the standard three and no premise',
                                                      needles=['LiCriterion.taylorCoeff_eq_li_symmetrized : ∀ (n : ℕ),']),
    'RvMBridge27.bl_explicit_formula': dict(zero_set=ZS_WX, rh='none in the statement', grade='DERIVES',
                                            why='the standard three and no premise beyond 0 < n; its body is bl_explicit_formula_of_two '
                                                'applied to local_count_sum and stripDerivBound, each printed at the standard three',
                                            needles=['RvMBridge27.bl_explicit_formula : ∀ (n : ℕ),',
                                                     'RvMBridge25.bl_explicit_formula_of_two RvMBridge23.local_count_sum RvMBridge24.stripDerivBound',
                                                     'fun ρ => ((MeromorphicOn.divisor riemannZeta {s | 0 < s.re ∧ s.re < 1}) ρ).toNat',
                                                     'WHERE WeilExplicit.zeroMult : declared in module E6Bridge4', MZ]),
    'RvMBridge27.liValue': dict(zero_set='Mathlib`s riemannZeta zeros: RvMBridge15.liLimit n := the tsum over ρ : ℂ of WeilExplicit.zeroMult ρ · '
                                         'Re(1 − (1 − 1/ρ)^n), the unwindowed sum of real parts, zeroMult the divisor of Mathlib`s riemannZeta',
                                rh='none in the statement',
                                grade='DERIVES', why='the standard three and no premise beyond 0 < n; its body is liValue_of_two applied to '
                                                     'local_count_sum and stripDerivBound',
                                needles=['RvMBridge27.liValue : ∀ (n : ℕ), 0 < n → RvMBridge15.LiValue n',
                                         'RvMBridge25.liValue_of_two RvMBridge23.local_count_sum RvMBridge24.stripDerivBound',
                                         "fun n => ∑' (ρ : ℂ), RvMBridge15.liPaired n ρ",
                                         'fun n ρ => ↑(WeilExplicit.zeroMult ρ) * ↑(RvMBridge15.BombieriLagarias.liKernel n ρ).re']),
    'RvMBridge27.xi_logDeriv_deriv_eq': dict(zero_set='Mathlib`s riemannZeta zeros: it proves the repository`s XiLogDerivDerivEq, off Zeta23`s '
                                                      'IsNontrivialZero (riemannZeta ρ = 0 ∧ 0 < Re ρ < 1), (log ξ)′′ = − the tsum over ρ : ℂ of '
                                                      'zeroMult ρ/(s − ρ)², ξ the repository`s s(s − 1)/2 · completedRiemannZeta₀ s + 1/2',
                                             rh='none in the statement', grade='DERIVES',
                                             why='the standard three and no premise; it proves the repository`s XiLogDerivDerivEq outright',
                                             needles=['RvMBridge27.xi_logDeriv_deriv_eq : RvMBridge18.XiLogDerivDerivEq',
                                                      "deriv (logDeriv RvMBridge18.xi) s = -∑' (ρ : ℂ), ↑(WeilExplicit.zeroMult ρ) / (s - ρ) ^ 2",
                                                      'fun s => s * (s - 1) / 2 * completedRiemannZeta₀ s + 1 / 2',
                                                      'fun ρ => riemannZeta ρ = 0 ∧ 0 < ρ.re ∧ ρ.re < 1']),
    'RvMBridge23.local_count_sum': dict(zero_set='Mathlib`s riemannZeta zeros, through RvMBridge22.lcTerm (printed)', rh='none in the statement',
                                        grade='DERIVES', why='the standard three and no premise; it proves the repository`s LocalCountSum outright',
                                        needles=['RvMBridge23.local_count_sum : RvMBridge22.LocalCountSum',
                                                 'WHERE RvMBridge23.local_count_sum : declared in module E6Bridge23']),
    'RvMBridge24.stripDerivBound': dict(zero_set='Mathlib`s riemannZeta zeros, through Zeta23.IsNontrivialZero and RvMBridge22.window (printed)',
                                        rh='none in the statement', grade='DERIVES',
                                        why='the standard three and no premise; it proves the repository`s StripDerivBound outright',
                                        needles=['RvMBridge24.stripDerivBound : RvMBridge22.StripDerivBound',
                                                 'WHERE RvMBridge24.stripDerivBound : declared in module E6Bridge24']),
    'RvMBridge25.bl_explicit_formula_of_two': dict(zero_set=ZS_WX, rh='none in the statement', grade='INTERFACES',
                                                   premise='RvMBridge22.LocalCountSum and RvMBridge22.StripDerivBound, the repository`s own Props, '
                                                           'discharged by local_count_sum and stripDerivBound in bl_explicit_formula',
                                                   why='its statement takes the repository`s LocalCountSum and StripDerivBound as premises, '
                                                       'discharged by name in bl_explicit_formula',
                                                   needles=['RvMBridge25.bl_explicit_formula_of_two : RvMBridge22.LocalCountSum →',
                                                            'RvMBridge22.StripDerivBound →']),
    'RvMBridge25.liValue_of_two': dict(zero_set='Mathlib`s riemannZeta zeros through RvMBridge15.liLimit (printed; as liValue)', rh='none in the statement', grade='INTERFACES',
                                       premise='RvMBridge22.LocalCountSum and RvMBridge22.StripDerivBound, discharged by name in liValue',
                                       why='its statement takes the repository`s LocalCountSum and StripDerivBound as premises, discharged by name in liValue',
                                       needles=['RvMBridge25.liValue_of_two : RvMBridge22.LocalCountSum →']),
}

COMPARE = dict(
    bulka_vs_fwd=dict(
        word='SAME',
        word_line='the same object as rh_imp_li_nonneg -- Li`s coefficients nonnegative from Mathlib`s RiemannHypothesis over Mathlib`s zeros -- '
                  'up to the index (their n is Li`s n + 1) and the coefficient`s definition; neither is a parameterized configuration.',
        text='Bulka’s forward direction (li_criterion_rh_iff’s left-to-right) and the programme’s `rh_imp_li_nonneg` are the same object up '
             'to the index and the coefficient’s definition: both conclude, from Mathlib’s `RiemannHypothesis`, that Li’s coefficients over '
             'Mathlib’s `riemannZeta` zeros are nonnegative -- ours for `LiCoeff n`, the absolutely convergent zero sum ½ Σ m(ρ) Re pairTerm n '
             'ρ over Zeta23’s configuration (multiplicity the analytic order of ζ), theirs for Re of the Taylor coefficient of (log '
             'ξ(1/(1 − z)))′, which is λ_(n+1) and which `taylorCoeff_eq_li_symmetrized` identifies with the symmetric zero sum weighted by '
             'the analytic order of ξ. In Lean neither statement implies the other until the equality lemma LiCoeff (n + 1) = Re '
             '(taylorCoeff riemannXi n) is compiled; neither is weaker. Their repository also compiles the converse, which ours does not.'),
    arda_vs_sym=dict(
        word='DIFFERENT',
        word_line='bl_explicit_formula states the height-window limit over Mathlib`s zeros with the repository`s own multiplicity (the divisor, '
                  'E6Bridge4) and closed forms; li_identity_sym is the δ → 0⁺ limit of EF_lit`s literature side at the symmetric family -- '
                  'a different limit and an evaluated arithmetic side.',
        text='Arda’s `bl_explicit_formula` and the programme’s `li_identity_sym` are different objects with one zero side: Arda’s states that '
             'the height-window sums Σ over |Im ρ| ≤ T of m(ρ)(1 − (1 − 1/ρ)^n) tend, as T → ∞, to closed forms evaluated at the '
             'archimedean place (γ, log π, log 2, the values ζ(j)) and at the finite place (the coefficients η_j of −ζ′/ζ − 1/(s − 1) '
             'at 1); ours states that `LiCoeff n` -- the absolutely convergent sum, so no window is needed -- is the δ → 0⁺ limit of the '
             'explicit formula’s literature right-hand side (pole terms, the prime sum, the Γ-integral) at the symmetric smoothed family. '
             'A different limit and an unevaluated arithmetic side: neither implies the other as stated. Nearer to ours is Arda’s '
             '`liValue`, whose `liLimit n` is the unwindowed Σ over ρ : ℂ of m(ρ) Re(1 − (1 − 1/ρ)^n) -- our `LiCoeff n`’s zero side '
             'up to the multiplicity’s definition (the divisor of ζ there, the analytic order of ζ here) -- set equal to the same '
             'closed forms: with the multiplicity lemma, it and `li_identity_sym` together would give `LiCoeff n` its evaluated closed '
             'form. Both rest on Zeta23 -- ours vendored at v1.0 = `3635e748`, theirs a dependency at '
             '`fbdc36bb`; over the 57 modules we vendor, 50 are byte-identical at the two pins and 7 (LinAlg) differ in a header-comment '
             'sentence alone, the code identical with comments stripped.'))

EQUALITY_PRICE = ('four lemmas, one of substance -- (E1) the carrier: Zeta23’s IsNontrivialZero ρ is riemannZeta ρ = 0 ∧ 0 < Re ρ < 1, '
                  'LiCriterion.NontrivialZero’s own predicate, so the index types agree by unfolding; (E2) THE LEMMA OF SUBSTANCE, the '
                  'multiplicity: (analyticOrderAt riemannZeta ρ).toNat = analyticOrderNatAt riemannXi ρ on the strip, ξ = ½ s(s − 1) '
                  'Λ(s) with the factor beside ζ analytic and nonzero there; (E3) the term: the reflection ρ ↦ 1 − ρ carries (1 − 1/ρ)^(n+1) '
                  'to (1 − 1/ρ)^(−(n+1)), so their symmetric sum is our paired sum at n + 1, reindexed by the kernel’s zeta_mult_reflect; '
                  '(E4) Re of a summable tsum is the tsum of Re (Complex.re_tsum, their summable_li_symmetrized, our pair_summable). Beside '
                  'the lemmas, a toolchain divergence: the repository pins Lean v4.34.0-rc1 and Mathlib de5ce8a9, the kernel v4.33.0-rc2 and '
                  '51e6992e, so the vendored copy compiles at the kernel’s rev or the kernel moves -- priced at the vendoring, not here')


def _needle_text(repo):
    return NL.join(rd(os.path.join(D, n)) for n in ('b565_audit_%s_prints.txt' % repo, 'b565_audit_%s_reads.txt' % repo,
                                                    'b565_audit_%s_reads2.txt' % repo) if os.path.exists(os.path.join(D, n)))


def _build_count(repo):
    t = rd(os.path.join(D, 'b565_audit_%s_build.txt' % repo))
    good = set(re.findall(r'^--- \+(\S+) rc=0 ', t, re.M))
    bad = re.findall(r'^--- \+(\S+) rc=(?!0 )', t, re.M)
    return len(good), bad


def auditbank():
    core = jl('b565_audit_core.json')
    zp = json.loads(rd(os.path.join(D, 'b565_zeta23_pins.json')))
    out = dict(comparisons=COMPARE, equality_price=EQUALITY_PRICE)
    L = ['b565 -- COMPONENT 3: THE AUDIT, UNDER (R175)(2) -- THE READINGS, THE GRADES, THE COMPARISONS', '',
         '### The prints, the builds and the closures: relay data/b565_audit_core.txt. The statements and the declaring modules:',
         '### data/b565_audit_<repo>_prints.txt, _reads.txt, _reads2.txt (Lean`s own output, from files written in D:/audit-b565).', '']
    n_std, n_all = 0, 0
    for repo, spec in AUDIT.items():
        cj = jl('b565_audit_%s_clone.json' % repo)
        ct = rd(os.path.join(D, 'b565_audit_%s_clone.txt' % repo))
        hd = re.search(r'HEAD`s commit: \S+ (\S+)', ct)
        txt = _needle_text(repo)
        nb, bad = _build_count(repo)
        rows = {}
        L += ['=' * 104, '### %s -- %s at %s' % (repo.upper(), spec['url'], cj.get('head')), '=' * 104,
              '### THE BUILD: %d modules, one lake call each, every rc 0: %s ; failing calls: %s' % (nb, not bad, bad or 'NONE')]
        for n in spec['terminals']:
            rdg = READINGS[n]
            c = core[repo]['rows'].get(n, {})
            ax = c.get('axioms')
            got = [x for x in rdg['needles'] if x in txt]
            st = _check_block(txt, n)
            grade, why = rdg['grade'], rdg['why']
            if ax is None:
                grade, why = 'NOT SCORABLE', 'no print'
            elif not set(ax) <= set(STD3) or core[repo]['sorry']['sorry'] or core[repo]['sorry']['axioms']:
                grade, why = 'SHELL', 'its print or closure carries sorryAx, a sorry or a declared axiom'
            n_all += 1
            n_std += bool(ax) and set(ax) <= set(STD3)
            rows[n] = dict(axioms=ax, statement=st, zero_set=rdg['zero_set'], rh=rdg['rh'], grade=grade, why=why,
                           premise=rdg.get('premise'), needles_total=len(rdg['needles']), needles_found=len(got),
                           needles_missing=[x for x in rdg['needles'] if x not in txt])
            L += ['', '### %s' % n, '    PRINT     : %s' % ax,
                  '    STATEMENT : ' + (NL + '                ').join(st or ['### NOT FOUND']),
                  '    ZERO SET  : %s' % rdg['zero_set'], '    RH        : %s' % rdg['rh'],
                  '    E0 GRADE  : %s -- %s' % (grade, why),
                  '    NEEDLES   : %d of %d found verbatim in the banked Lean output%s'
                  % (len(got), len(rdg['needles']), '' if len(got) == len(rdg['needles']) else ' ; MISSING %s' % rows[n]['needles_missing'])]
        sk = core[repo]['sorry']
        out[repo] = dict(url=spec['url'], head=cj.get('head'), head_date=hd.group(1)[:10] if hd else None, build_modules=nb,
                         build_exit=0 if (nb and not bad) else 1, rows=rows, sorry=sk,
                         closure_modules=len(jl('b565_audit_bulka_sorry_XiOrderBridge_ReverseDirection_Fidelity_RHBridge.json').get('closure', {}))
                         if repo == 'bulka' else len(jl('b565_audit_arda_sorry_E6Bridge27.json').get('closure', {})),
                         zeta23_modules=len(jl('b565_audit_arda_sorry_zeta23.json').get('closure', {})) if repo == 'arda' else None)
    b, a = out['bulka'], out['arda']
    conv = [b['rows'][x] for x in ('LiCriterion.positivity_implies_RH', 'li_criterion', 'LiCriterion.li_criterion_rh_iff')]
    b['converse_genuine'] = all(r['grade'] == 'DERIVES' and r['needles_found'] == r['needles_total'] for r in conv)
    blr = a['rows']['RvMBridge27.bl_explicit_formula']
    a['bl_genuine'] = blr['grade'] == 'DERIVES' and blr['needles_found'] == blr['needles_total']
    out['n3'] = COMPARE['bulka_vs_fwd']['word'] in ('SAME', 'WEAKER') and b['converse_genuine']
    out['s2'] = COMPARE['arda_vs_sym']['word'] == 'DIFFERENT' and a['bl_genuine'] and 'E6Bridge4' in blr['zero_set']
    out['std3_count'], out['terminal_count'] = n_std, n_all
    diffs = [r for r in zp if r['v10'] != r['fbdc']]
    out['zeta23'] = dict(vendored=len(zp), identical=len(zp) - len(diffs), comment_only=sum(1 for r in diffs if r.get('code_identical_comments_stripped')),
                         code_differs=[r['file'] for r in diffs if not r.get('code_identical_comments_stripped')],
                         ours_is_v10=sum(1 for r in zp if r.get('body_is_v10_suffix')))
    out['h17a_reason'] = ('the Bulka converse as compiled -- li_criterion`s right-to-left, through li_criterion_rh_iff and positivity_implies_RH -- '
                          'prints [propext, Classical.choice, Quot.sound], concludes Mathlib`s RiemannHypothesis (declared in '
                          'Mathlib.NumberTheory.LSeries.RiemannZeta), its zeros Mathlib`s riemannZeta zeros under the repository`s own name for '
                          'the strip set, its closure sorry 0 and axiom declarations 0: no clause of H17a is printed.'
                          if b['converse_genuine'] else 'a clause of H17a is printed (see the grades).')
    out['h17b_reason'] = ('bl_explicit_formula prints the standard three with no premise beyond 0 < n, its zero set the divisor of Mathlib`s '
                          'riemannZeta, its two analytic premises discharged by name (local_count_sum, stripDerivBound), its closure (15 '
                          'modules and 59 of Zeta23) sorry 0 and axiom declarations 0: DERIVES over Mathlib`s zeros.'
                          if a['bl_genuine'] else 'bl_explicit_formula is not DERIVES over Mathlib`s zeros (see the grades).')
    out['summary'] = dict(
        bulka='`li_criterion` (the comparator`s statement of record, at `%s`) states Mathlib’s `RiemannHypothesis` ↔ ∀ n, 0 ≤ Re of the '
              'n-th Taylor coefficient at 0 of the log-derivative of ξ(1/(1 − z)), ξ = ½ s(s − 1) completedRiemannZeta₀ s + ½; its body '
              'is the library’s `li_criterion_rh_iff`, which applies `biconditional_rh_li_of_hadamard_order_one` to `xi_hasFiniteOrder` '
              'and `xi_order_le_one`; `taylorCoeff_eq_li_symmetrized` identifies the coefficient with the symmetric sum over Mathlib’s '
              'zeros in the strip weighted by the analytic order of ξ. %d terminals audited: %s. Every print the standard three; the '
              'closure (%d library modules and the comparator) sorry 0, axiom declarations 0 (the control, Challenge.lean, reads sorry 2).'
              % (b['head'][:8], len(b['rows']), ', '.join('%s %s' % (n.split('.')[-1], r['grade']) for n, r in b['rows'].items()),
                 b['closure_modules']),
        arda='`RvMBridge27.bl_explicit_formula` (its node RH_bl_explicit_formula, at `%s`) states, for n ≥ 1, the height-window limit of '
             'Σ m(ρ)(1 − (1 − 1/ρ)^n) as the archimedean closed form plus the finite side; m is the repository’s own name for the '
             'divisor of Mathlib’s `riemannZeta` on the strip; its body is `bl_explicit_formula_of_two` applied to `local_count_sum` '
             'and `stripDerivBound`, which prove the repository’s LocalCountSum and StripDerivBound outright. %d terminals audited: %s. '
             'Every print the standard three; the closure (%d modules and %d of Zeta23 at `fbdc36bb`) sorry 0, axiom declarations 0 '
             '(the control, Zeta23’s Challenge.lean, reads sorry 17; two `axiom` lines inside a docstring’s example, first read as '
             'declarations, were a nested-comment defect of the scanner, repaired and re-run).'
             % (a['head'][:8], len(a['rows']), ', '.join('%s %s' % (n.split('.')[-1], r['grade']) for n, r in a['rows'].items()),
                a['closure_modules'], a['zeta23_modules']),
        scores_line=('The Bulka converse is genuine at its pin -- the standard three over Mathlib’s RiemannHypothesis and zeros, no sorry; '
                     'Arda’s formula DERIVES over Mathlib’s zeros, its premises discharged by name.'))
    L += ['', '=' * 104, '### THE COMPARISON: BULKA`S FORWARD DIRECTION AGAINST rh_imp_li_nonneg -- %s' % COMPARE['bulka_vs_fwd']['word'],
          '=' * 104, '    ' + poss(COMPARE['bulka_vs_fwd']['text']), '',
          '=' * 104, '### THE COMPARISON: ARDA`S bl_explicit_formula AGAINST li_identity_sym -- %s' % COMPARE['arda_vs_sym']['word'],
          '=' * 104, '    ' + poss(COMPARE['arda_vs_sym']['text']), '',
          '### THE ZETA23 PINS (relay data/b565_zeta23_pins.json): ours v1.0 = %s (vendored, every body the v1.0 file: %d of %d), Arda`s %s.'
          % (Z23_OURS, out['zeta23']['ours_is_v10'], out['zeta23']['vendored'], Z23_ARDA),
          '    over the %d modules we vendor: %d byte-identical ; %d differing in a header comment alone ; code differing: %s'
          % (out['zeta23']['vendored'], out['zeta23']['identical'], out['zeta23']['comment_only'], out['zeta23']['code_differs'] or 'NONE'),
          '    => no consumed statement differs; no pin-refresh work-order.', '',
          '### THE EQUALITY LEMMA, PRICED (the vendoring`s first act, should the author`s word be to vendor): ' + EQUALITY_PRICE, '',
          '### H17a: %s -- %s' % (w_(not b['converse_genuine']), out['h17a_reason']),
          '### H17b: %s -- %s' % (w_(not a['bl_genuine']), out['h17b_reason']),
          '### (N3) from the comparison: %s ; (S2) from the comparison: %s' % (w_(out['n3']), w_(out['s2'])), '',
          '### No sentence here claims priority. Nothing here is a statement about RH or any zero beyond the compiled statements` own words.']
    put_txt('b565_audit.txt', L)
    put_json('b565_audit.json', out)
    miss = [(r, n, t['needles_missing']) for r in AUDIT for n, t in out[r]['rows'].items() if t['needles_missing']]
    print(NL.join(L[-12:]))
    print('### NEEDLES MISSING: %s' % (miss or 'NONE'))


# ================================================================================ COMPONENT 4: THE RECORD
BULKA_URL, ARDA_URL = AUDIT['bulka']['url'], AUDIT['arda']['url']
FIELD5_H = '*Appended 2026-09-30 by b565 to the field entry'
WO5 = ('*Appended 2026-09-30 by b565, under the author’s ruling `(R175)`(3), to the LI-WEIL-BRIDGE work-order (:3548; b563’s line '
       'at :11590) -- THE CONDITIONAL, (R82)’S FORM, BOTH BRANCHES:*')
FH5 = ('## The audit: two public formalizations of Li’s criterion and the Bombieri–Lagarias formula, read by statement and print '
       'at their pins')
HEADING5 = ('### b565 — the audit under (R175): two public formalizations of Li’s criterion and the Bombieri–Lagarias formula '
            'built and read at their pins; the superseded grade in a readable cell; housekeeping')


def _au():
    return jl('b565_audit.json')


def fieldline():
    guard_absent(FIND, FIELD5_H)
    a = _au()
    b, r = a['bulka'], a['arda']
    t = (FIELD5_H + ' (:5575) and b564’s line (:6136), under `(R175)`(2) -- THE TWO PUBLIC FORMALIZATIONS, BUILT AND READ AT '
         'THEIR PINS (relay `data/b565_audit.txt`):* (a) ' + BULKA_URL + ' at `' + b['head'][:8] + '` (its HEAD committed ' +
         b['head_date'] + '), cloned and built 2026-09-30 with its own toolchain (Lean v4.34.0-rc1, Mathlib `de5ce8a9`), %d modules '
         'one per call, every exit 0: `li_criterion` states Mathlib’s `RiemannHypothesis` ↔ ∀ n, 0 ≤ Re of the n-th Taylor '
         'coefficient at 0 of the log-derivative of ξ(1/(1 − z)), ξ built from Mathlib’s `completedRiemannZeta₀`; '
         '`li_coefficients_eq_zero_sum` identifies that coefficient with ½ Σ, over Mathlib’s `riemannZeta` zeros in the open '
         'strip weighted by the analytic order of ξ, of (1 − (1 − 1/ρ)^(−(n+1))) + (1 − (1 − 1/ρ)^(n+1)) -- λ_(n+1) in Li’s '
         'indexing; the converse `LiCriterion.positivity_implies_RH` concludes Re ρ = 1/2 for every zero of `riemannZeta` in the '
         'strip. Every audited terminal prints [propext, Classical.choice, Quot.sound], and the closure (%d library modules and '
         'the comparator) reads no sorry and no axiom declaration. (b) ' + ARDA_URL + ' at `' + r['head'][:8] + '` (its HEAD '
         'committed ' + r['head_date'] + '), project `telperion/examples/rvm_bridge/lean`, built 2026-09-30 with Lean '
         'v4.33.0-rc2, Mathlib `51e6992e` and Zeta23 at formal-math `fbdc36bb`, %d modules one per call, every exit 0: '
         '`RvMBridge27.bl_explicit_formula` states, for n ≥ 1, that the height-window sums Σ over 0 < Re ρ < 1, |Im ρ| ≤ T of '
         'm(ρ)(1 − (1 − 1/ρ)^n), m the divisor of Mathlib’s `riemannZeta` on the strip, tend as T → ∞ to the archimedean closed '
         'form plus the finite side in the coefficients of −ζ′/ζ − 1/(s − 1) at 1; it prints the standard three, its two '
         'analytic premises discharged by name (`RvMBridge23.local_count_sum`, `RvMBridge24.stripDerivBound`), and its closure '
         '(%d modules of its own and %d of Zeta23) reads no sorry and no axiom declaration. Each is recorded in its own terms; '
         'neither is vendored at this act. No sentence here claims priority.')
    t = t % (b['build_modules'], b['closure_modules'], r['build_modules'], r['closure_modules'], r['zeta23_modules'])
    res = append_to(FIND, NL + t + NL)
    n = line_of(FIND, FIELD5_H)
    print('### the field line at FINDINGS :%s ; %s' % (n, json.dumps(res)))
    put_json('b565_fieldline.json', dict(line=n, text=poss(t), res=res))


def conditional():
    guard_absent(OT, WO5)
    a = _au()
    s = jl('b565_scores.json')
    eq = a['equality_price']
    t = (WO5 + ' the audit reads H17a %s (relay `data/b565_audit.txt`; the Bulka converse at `%s` prints the standard three over '
         'Mathlib’s `RiemannHypothesis` and `riemannZeta`’s zeros, no sorry in its closure). **(i) IF THE AUTHOR’S WORD AT b565’S '
         'CLOSING IS TO VENDOR:** the repository vendored at `%s` as a dependency of SIDE-explicit-formula in the manner Zeta23 '
         'was -- its NOTICE and licence carried, its terminals cited by fully qualified name; the vendoring’s first act the '
         'equality lemma, priced here in lemmas: %s; the converse re-graded T0-vendored; the ceiling sentence amended to name the '
         'vendored source; (V1)-(V4) closed as superseded by the vendoring, the price left on record. **(ii) IF H17a HOLDS, OR '
         'THE AUTHOR’S WORD IS NOT TO VENDOR:** the field entry carries the audit’s findings beside the URLs (FINDINGS :%s), the '
         'converse stays T1-lit, and (V1)-(V4) stand. In either branch no priority is claimed and each repository is recorded in its own terms. **The Zeta23 '
         'pins:** Arda’s Zeta23 at `fbdc36bb` against ours at v1.0 = `3635e748`, over the %d modules we vendor: %d byte-identical, '
         '%d differing in a header-comment sentence alone (the LinAlg files, the code identical with comments stripped), so no '
         'consumed statement differs and no pin-refresh work-order is filed (relay `data/b565_zeta23_pins.json`). Nothing is '
         'vendored at this act.'
         % (w_(s.get('h17a')), a['bulka']['head'][:8], a['bulka']['head'][:8], eq, jl('b565_fieldline.json').get('line'),
            a['zeta23']['vendored'], a['zeta23']['identical'], a['zeta23']['comment_only']))
    o = append_to(OT, NL + t + NL)
    o['line'] = line_of(OT, WO5)
    put_json('b565_conditional.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes, prefix %(prefix)s)' % o)


def findings():
    guard_absent(FIND, FH5)
    a, s = _au(), jl('b565_scores.json')
    fa, cj = jl('b565_fieldline.json'), jl('b565_conditional.json')
    b, r, c = a['bulka'], a['arda'], a['comparisons']
    t = ['', FH5, '',
         '*Filed at b565 on the author’s ruling `(R175)`(2). Banks: relay `data/b565_audit.txt` (with `.json`), '
         '`data/b565_audit_bulka_build.txt`, `data/b565_audit_bulka_prints.txt`, `data/b565_audit_bulka_reads.txt`, '
         '`data/b565_audit_arda_build.txt`, `data/b565_audit_arda_prints.txt`, `data/b565_audit_arda_reads.txt`, the sorry banks '
         '`data/b565_audit_*_sorry_*.txt` and `data/b565_zeta23_pins.json`. Nothing of either repository enters the corpus; the '
         'clones stay under D:/audit-b565 until the author’s word. Nothing about the zeros of ζ is claimed beyond the compiled '
         'statements’ own words.*', '',
         '**What was done.** Each repository was cloned at its HEAD (%s, `%s`; %s, `%s`), built with its own toolchain one module '
         'per call in import order (%d and %d modules, every exit 0; the cache fetched by the project’s own `lake exe cache get`), '
         'and read by `#print axioms`, `#check` and `#print` from files written outside the clones and elaborated in each '
         'project’s environment; every constant a zero set or an RH unfolds to was read to its declaring module; the transitive '
         'closures were read for sorry, admit and axiom declarations with positive controls firing.'
         % (BULKA_URL, b['head'][:8], ARDA_URL, r['head'][:8], b['build_modules'], r['build_modules']), '',
         '**Li’s criterion (Bulka).** %s' % a['summary']['bulka'], '',
         '**The Bombieri–Lagarias formula (Arda).** %s' % a['summary']['arda'], '',
         '**Against the programme’s own terminals.** %s %s' % (c['bulka_vs_fwd']['text'], c['arda_vs_sym']['text']), '',
         '**The scores.** H17a %s; H17b %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s; the seat’s (S1) %s, (S2) %s, (S3) %s.'
         % tuple(w_(s.get(x)) for x in ('h17a', 'h17b', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')), '',
         '**Entered beside it.** The field line at FINDINGS :%s; the `(R175)`(3) conditional at the LI-WEIL-BRIDGE work-order '
         '(OPEN_TRAILS :%s), both branches, the vendoring’s first act priced; the superseding row 401 (li_identity_of_exchange '
         'INTERFACES, tier T2 in words) and the audit’s row %s.' % (fa.get('line'), cj.get('line'), ROW_AUD), '',
         '**Next.** b566 is GRH-Weil act three, fixed by `(R175)`(6): the frontier’s obstacle, the representation of LFunction χ on '
         '0 < Re s for non-principal χ, by Abel summation (H18a-H18c). The act after it is the converse’s (V4) or the vendoring '
         'per `(R175)`(3), on the author’s word at this closing.', '',
         '*Nothing deposits; nothing at Zenodo written; no kernel file written; no sentence here claims priority; nothing here is a '
         'statement about RH or any zero beyond the compiled statements’ own words.*', '']
    o = append_to(FIND, NL.join(t))
    o['heading_line'] = line_of(FIND, FH5)
    put_json('b565_findings.json', o)
    print('  FINDINGS.md:%s (the entry)' % o['heading_line'])


def rows():
    if [l for l in rd(CORR).split(NL) if l.startswith('| %s |' % ROW_AUD)]:
        sys.exit('### ROW %s ALREADY PRESENT' % ROW_AUD)
    a = _au()
    b, r = a['bulka'], a['arda']
    act = [ROW_AUD,
           '**THE AUDIT: TWO PUBLIC FORMALIZATIONS OF LI’S CRITERION AND THE BOMBIERI–LAGARIAS FORMULA, BUILT AND READ AT THEIR '
           'PINS** (b565, under (R175)(2)). Not the programme’s own terminals and not vendored: ' + BULKA_URL + ' at %s (Lean '
           'v4.34.0-rc1, Mathlib de5ce8a9, %d modules built) states Li’s criterion both ways over Mathlib’s RiemannHypothesis and '
           'riemannZeta’s zeros; ' % (b['head'][:8], b['build_modules']) + ARDA_URL + ' at %s (Lean v4.33.0-rc2, Mathlib '
           '51e6992e, Zeta23 fbdc36bb, %d modules built) states the Bombieri–Lagarias explicit formula over Mathlib’s zeros with '
           'its own multiplicity and closed forms. Recorded in each repository’s own terms; no priority claimed.'
           % (r['head'][:8], r['build_modules']),
           ('`D:/audit-b565/bulka` @%s : `li_criterion`, `LiCriterion.positivity_implies_RH`, `LiCriterion.li_criterion_rh_iff` ; '
            '`D:/audit-b565/arda` @%s : `RvMBridge27.bl_explicit_formula`, `RvMBridge27.liValue`' % (b['head'][:8], r['head'][:8])),
           '%d of %d audited terminals: [propext, Classical.choice, Quot.sound], no sorryAx; closures sorry 0, axiom declarations 0 '
           '(relay data/b565_audit.txt)' % (a['std3_count'], a['terminal_count']),
           ' ; '.join('`%s` %s' % (n, t['grade']) for n, t in list(b['rows'].items())[:3] + list(r['rows'].items())[:2]),
           'READ, NOT VENDORED: the clones under D:/audit-b565 outside the corpus, kept until the author’s word; the (R175)(3) '
           'conditional at the LI-WEIL-BRIDGE work-order; nothing deposits; nothing at Zenodo written.']
    r2 = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + act, capture_output=True, text=True, encoding='utf-8')
    print(r2.stdout[-300:], r2.stderr[-300:])
    put_json('b565_rows.json', dict(act=act, exit_act=r2.returncode, sup=ROW_SUP))


def trail():
    guard_absent(OT, HEADING5)
    s, a = jl('b565_scores.json'), _au()
    f, fa, cj = jl('b565_findings.json'), jl('b565_fieldline.json'), jl('b565_conditional.json')
    sr, sa = jl('b565_suprow.json'), jl('b565_supersede_after.json')
    t = ['', HEADING5, '',
         '**(R175) ratified.** (1) b564 at its weight. (2) The audit of the two public formalizations at their pins. (3) The '
         'conditional, (R82)’s form. (4) The superseded grade in a cell the table reads. (5) Housekeeping: the push output '
         'committed, the step-zero process listing standing, the push capture, the write-list glob rule. (6) GRH-WEIL act three '
         'fixed for b566. (7) The act after b566 on the author’s word.', '',
         '**Entered:** FINDINGS.md:%s (the field line), :%s (the entry); OPEN_TRAILS.md:%s (the (R175)(3) conditional at the '
         'LI-WEIL-BRIDGE work-order); SIDE-global-section CORRESPONDENCE.md rows %s (the superseding grade, line %s) and %s (the '
         'audit); relay tools/FERRY_STANDING.md clause A4; relay tools/push_gated.sh (the capture), tools/terminal_table.py (the '
         'synonym entry), tools/SUITE_README.md (new).'
         % (fa.get('line'), f.get('heading_line'), cj.get('line'), ROW_SUP, sr.get('line'), ROW_AUD), '',
         '**H17a %s · H17b %s.** %s' % (w_(s.get('h17a')), w_(s.get('h17b')), a['summary']['scores_line']), '',
         '**The table:** li_identity_of_exchange reads row 401’s cell, INTERFACES, its tier T2 in words; CONFLICT %d → %d; no other '
         'grade moved.' % (len(sa.get('conflict_committed', [])), len(sa.get('conflict_regenerated', []))), '',
         '**Next:** b566, GRH-WEIL act three, as `(R175)`(6) fixes it (H18a-H18c); the author’s word on (R175)(3) at this closing.', '',
         '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s.'
         % tuple(w_(s.get(x)) for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
         '**No kernel file written; no tag made; nothing vendored.** Nothing deposits; nothing at Zenodo written; no existing '
         'statement changed; no Zeta23 file edited or added; no monograph byte changed; ERRATA untouched; the ceiling sentence '
         'untouched; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about '
         'RH or any zero beyond the compiled statements’ own words.', '']
    o = append_to(OT, NL.join(t))
    o['line'] = line_of(OT, HEADING5)
    put_json('b565_trail.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


def desk():
    s, a = jl('b565_scores.json'), _au()
    c = a['comparisons']
    L = ['=' * 104, 'b565 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### (R175)`S TWO.', '-' * 104,
         '  **(H17a)** ### **%s.** -- %s' % (w_(s['h17a']), a['h17a_reason']),
         '  **(H17b)** ### **%s.** -- %s' % (w_(s['h17b']), a['h17b_reason']), '',
         '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- H17a %s: no declared axiom, no sorry, no parameter zero set, no local RH is printed.' % (w_(s['n1']), w_(s['h17a'])),
         '  **(N2)** ### **%s.** -- H17b %s: bl_explicit_formula DERIVES over Mathlib`s zeros.' % (w_(s['n2']), w_(s['h17b'])),
         '  **(N3)** ### **%s.** -- %s' % (w_(s['n3']), c['bulka_vs_fwd']['word_line']),
         '  **(N4)** ### **%s.** -- Bulka %d modules and Arda %d modules, every one-module call exit 0 (the build logs).'
         % (w_(s['n4']), a['bulka']['build_modules'], a['arda']['build_modules']),
         '  **(N5)** ### **%s.** -- the regenerated table grade INTERFACES; row 401`s own cell carries tier T2 in words; the synonym '
         'entry alone moved no grade.' % w_(s['n5']),
         '  **(N6)** ### **%s.** -- every kernel main at its pre-act head (SIDE-explicit-formula v0.8 = 6ec71b3), SIDE-global-section'
         ' the ledger rows alone, the kept branches at their tips; nothing deposits; nothing at Zenodo.' % w_(s['n6']), '',
         '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the Bulka converse at the standard three over Mathlib`s RiemannHypothesis and riemannZeta`s zeros,'
         ' no sorry in its closure.' % w_(s['s1']),
         '  **(S2)** ### **%s.** -- %s' % (w_(s['s2']), c['arda_vs_sym']['word_line']),
         '  **(S3)** ### **%s.** -- after the row li_identity_of_exchange reads INTERFACES from row 401 alone; CONFLICT unmoved; the '
         'synonym entry alone moved no grade.' % w_(s['s3']), '',
         '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % (sum(1 for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6') if s[x]), sum(1 for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6') if s[x] is False),
            sum(1 for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6') if s[x] is None),
            sum(1 for x in ('s1', 's2', 's3') if s[x]), sum(1 for x in ('s1', 's2', 's3') if not s[x])),
         '### ### **(R175) : H17a %s ; H17b %s.**' % (w_(s['h17a']), w_(s['h17b'])), '']
    L += rd(os.path.join(D, 'b565_defects.txt')).rstrip().split(NL)
    put_txt('b565_desk_notes.txt', L)
    print(NL.join(L[:30]))


def components():
    L = ['=' * 132, 'b565 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b565_reads.txt', 'b565_housekeeping.txt', 'b565_capture_test.txt', 'b565_synonym_unit.txt', 'b565_supersede_noop.txt',
              'b565_supersede_after.txt', 'b565_supersede_tableline.txt', 'b565_audit.txt', 'b565_audit_core.txt',
              'b565_branches.txt', 'b565_scores.txt'):
        L.append('### relay data/%s' % n)
        L.extend('  ' + x for x in rd(os.path.join(D, n)).rstrip().split(NL))
        L.append('')
    for n, key in (('b565_suprow.json', 'line'), ('b565_fieldline.json', 'line'), ('b565_conditional.json', 'line'),
                   ('b565_findings.json', 'heading_line'), ('b565_rows.json', 'exit_act'), ('b565_trail.json', 'line')):
        L.append('### relay data/%s -- %s %s' % (n, key, jl(n).get(key)))
    put_txt('b565_components.txt', L)
    print('  written: b565_components.txt (%d lines)' % len(L))


def main(argv):
    cmd = argv[0] if argv else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_') or cmd == 'main':
        sys.exit('usage: b565_record.py <component>')
    return fn(*argv[1:])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
