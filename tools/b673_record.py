# -*- coding: utf-8 -*-
"""b673_record.py -- THE ACT'S RECORD TOOL, b673 under (R283).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b673's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b672_record.py (the helpers, the guarded landing, the readers, the answers route); new here: Component 1's
### weight line, read from (R283)(1) in the ferry bank verbatim with the order range the navigator's answer on the PROSE-PINS line gives; the
### later routes are added at their components. No kernel byte is written by any route.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b673_record.py <route> [dry]`.
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
sys.path.insert(0, T)
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b673_worklist as K          # noqa: E402

SP = K.SP
STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(path) else ''


def rdn(name):
    return rd(os.path.join(D, name))


def put_json(name, obj):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank."""
    return {}


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return _standins().get(name, {}) if STANDIN else {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b673's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b673_scanfile_%s.md' % tag)
    R3._write(p, allt.encode('utf-8'))
    sc = R3._scan(p)
    clean = R3._clean(sc)
    ticks = odd_lines(allt)
    unread = [x for x in ('### NOT', 'None', ' ? ', '`?`') if x in allt]
    outside = [n for n in R41.OAI_NEEDLES if n in allt]
    stems = [s for s in ('gap', 'blind') if re.search(r'\b' + s, allt, re.I)]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks by line: %s ; unread figures: %s ; outside names: %s ; '
          'stems: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', outside or 'NONE',
                         stems or 'NONE'))
    if not clean:
        print(sc[-1500:])
    fired = bool(any(nd.values()) or not clean or ticks or unread or outside or stems)
    return [tuple(c) for c in cells], fired


def land(items, bank, tag, entry=None, check=(), expect_cells=(), dry=True):
    for f, ln, needle in check:
        L = rd(FIND if f == 'FINDINGS.md' else OT).split(NL)
        if needle not in L[ln - 1]:
            sys.exit('### %s :%d DOES NOT CARRY %r -- NOTHING WRITTEN' % (f, ln, needle))
    items = [(f, h, conv(t)) for f, h, t in items]
    cells, fired = screens(items, tag, dry)
    if dry:
        for f, h, t in items:
            print('----', f, NL + t)
        return
    if cells != [tuple(x) for x in expect_cells] or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    n = {'FINDINGS.md': len(rd(FIND).split(NL)), 'OPEN_TRAILS.md': len(rd(OT).split(NL))}
    want = {}
    for f, h, t in items:
        want[h] = n[f] + 1 if rd(FIND if f == 'FINDINGS.md' else OT).endswith(NL) else n[f] + 2
        n[f] += len(t.strip(NL).split(NL)) + 1
    for f, h, _t in items:
        guard_absent(FIND if f == 'FINDINGS.md' else OT, h)
    out = []
    for f, h, t in items:
        path = FIND if f == 'FINDINGS.md' else OT
        r = append_to(path, t)
        got = line_of(path, h)
        out.append(dict(file=f, head=h, line=got, append=r))
        if got != want[h]:
            put_json(bank, dict(entry=entry, lines=out, at=utc(), stopped=True))
            sys.exit('### %s LANDED AT :%s, NOT :%d -- STOPPED' % (h[:60], got, want[h]))
    put_json(bank, dict(entry=entry, lines=out, at=utc()))
    print('  ' + ' ; '.join('%s :%s' % (x['file'], x['line']) for x in out))


# ================================================================================ THE READERS, ONE PER ROW SHAPE A ROUTE READS ((R263)(3))
def read_score_row(k, v):
    """a scores row: key N1..N5, H1..H6 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text)."""
    if not re.match(r'^(N[1-5]|H[1-6]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


SQUARE_KEYS = ('kind', 'idx', 're', 'im', 'h', 'count')


def read_square_row(r):
    """a row of b671's narrowed list: kind ON or OFF, its index, its centre (re, im as decimal strings), its half-width h and its count 1;
    returns (kind, idx); raises on a row of another shape or a count not 1. Carried from b671_record.py :174-:182 unchanged."""
    if not isinstance(r, dict) or any(k not in r for k in SQUARE_KEYS) or r['kind'] not in ('ON', 'OFF') or r['count'] != 1:
        raise ValueError('square row of another shape or count: %r' % ((r.get('kind'), r.get('idx'), r.get('count')) if isinstance(r, dict) else r,))
    float(r['re'])
    float(r['im'])
    float(r['h'])
    return r['kind'], r['idx']


READERS = ['read_score_row', 'read_head', 'read_square_row']


# ================================================================================ COMPONENT 1: b672 AT ITS WEIGHT, (R283)(1)
def _ruling():
    t = rdn('b673_ferry.txt')
    i, j = t.find('RULING (R283) BEGIN'), t.find('RULING (R283) END')
    if i < 0 or j < i:
        sys.exit('### THE FERRY BANK CARRIES NO (R283) -- NOTHING WRITTEN')
    return t[i:j]


def _clause(n):
    r = _ruling()
    m = re.search(r'\n\(%d\) (.*?)(?=\n\(%d\) |\Z)' % (n, n + 1), r, re.S)
    if not m:
        sys.exit('### (R283)(%d) NOT FOUND IN THE FERRY BANK -- NOTHING WRITTEN' % n)
    return ' '.join(m.group(1).split())


RANGE_RULED = 'entered at OPEN_TRAILS :14440–:14450, the nine kernels without a print bank as runner items'
RANGE_READ = 'entered at OPEN_TRAILS :14442–:14452, the nine kernels without a print bank as runner items at :14440'

WH = ('*Appended 2026-10-16 by b673 to b672’s entry (:8791), under `(R283)`(1) -- b672 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b672_closing.txt), ITS TWO H2 FIGURES CARRIED:*')


def _weight():
    c = _clause(1)
    pre = 'b672 AT ITS WEIGHT, as data/b672_closing.txt prints and the seat cites at step zero: '
    if not c.startswith(pre) or c.count(RANGE_RULED) != 1:
        sys.exit('### (R283)(1) IS NOT IN THE FORM READ AT STEP ZERO -- NOTHING WRITTEN')
    body = c[len(pre):].replace(RANGE_RULED, RANGE_READ)
    return ('\n' + WH + ' ' + body + ' The five orders`’ lines as OPEN_TRAILS carries them, by the navigator’s answer on the PROSE-PINS line '
            '(relay data/b673_defects.txt (c)).\n').replace('orders`’', 'orders’')


def c1(*a):
    dry = 'dry' in a
    for n, needle in ((14440, 'THE KERNELS WITH NO RELAY PRINT BANK'), (14442, '`W-ORD-TABLE-SHAPE`'), (14452, '`W-ORD-PROSE-PINS`')):
        if needle not in rd(OT).split(NL)[n - 1]:
            sys.exit('### OPEN_TRAILS :%d DOES NOT CARRY %s -- NOTHING WRITTEN' % (n, needle))
    land([('FINDINGS.md', WH, _weight())], 'b673_record_lines.json', 'c1', entry=K.B672_ENTRY,
         check=[('FINDINGS.md', K.B672_ENTRY, '## The Correspondence generator'), ('OPEN_TRAILS.md', K.B672_TRAIL, '### b672')], dry=dry)


# ================================================================================ COMPONENT 2: THE PLAN, (R283)(3), IN THE b663 FORM WITH THE CONSUMERS SECTION
MATHLIB_CO = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
DECL = r'^(@\[[^]]*\] *)?(protected |private |nonrec )*(theorem|lemma) ([A-Za-z_.]*\.)?%s\b'
# ### every fact the steps consume, searched at the pin: (the step, the name, the shapes tried in order -- the first shape `theorem <name> `
# ### with the space, the second any declaration form by the bare word, the third the multiplicative source of a to_additive name)
# ### the fourth element: the path of the hit the step uses -- every other hit a namesake, counted and not used (b645's lesson: grep namesakes)
SEARCHES = [
    ('V4 (i), the partial sums over a window', 'geom_sum_eq', ['geom_sum_eq'], 'Algebra/Field/GeomSum.lean'),
    ('V4 (i), the partial sums over a window', 'geom_sum_Ico', ['geom_sum_Ico'], 'Algebra/Field/GeomSum.lean'),
    ('V4 (ii), |s_n|^2 expanded', 'RCLike.mul_conj (Complex)', ['mul_conj'], 'Analysis/RCLike/Basic.lean'),
    ('V4 (ii), |s_n|^2 expanded', 'Complex.normSq_eq_norm_sq', ['normSq_eq_norm_sq'], 'Analysis/Complex/Norm.lean'),
    ('V4 (ii)-(ii`), the double sums', 'Finset.sum_mul_sum', ['sum_mul_sum'], 'Algebra/BigOperators/Ring/Finset.lean'),
    ('V4 (ii`), the real part of a sum', 'Complex.re_sum', ['re_sum'], 'Data/Complex/BigOperators.lean'),
    ('V4 (ii`), conj of a power', 'map_pow (starRingEnd is a ring hom)', ['map_pow'], 'Algebra/Group/Hom/Defs.lean'),
    ('V5, |w^n| and |z^n|', 'norm_pow', ['norm_pow'], 'Analysis/Normed/Ring/Basic.lean'),
    ('V5, the binomial tail', 'Nat.sum_range_choose', ['sum_range_choose'], 'Data/Nat/Choose/Sum.lean'),
    ('V5, the binomial tail', 'add_pow (the binomial theorem, CommSemiring)', ['add_pow'], 'Data/Nat/Choose/Sum.lean'),
    ('V5, the summable tail', 'Summable.of_norm_bounded', ['of_norm_bounded'], 'Analysis/Normed/Group/InfiniteSum.lean'),
    ('S5, the dominant modulus', 'Finset.exists_max_image', ['exists_max_image'], 'Data/Finset/Max.lean'),
    ('S5, the split of the tsum at the dominant set', 'Summable.sum_add_tsum_compl (to_additive)', ['sum_add_tsum_compl', 'prod_mul_tprod_compl'],
     'Topology/Algebra/InfiniteSum/Group.lean'),
    ('S5, the split of the tsum at the dominant set', 'Summable.tsum_union_disjoint (to_additive)', ['tsum_union_disjoint', 'tprod_union_disjoint'],
     'Topology/Algebra/InfiniteSum/Basic.lean'),
    ('S5, n^2 (s/r)^n tends to 0', 'tendsto_pow_const_mul_const_pow_of_abs_lt_one', ['tendsto_pow_const_mul_const_pow_of_abs_lt_one'],
     'Analysis/SpecificLimits/Normed.lean'),
    ('S5, r^n unbounded', 'tendsto_pow_atTop_atTop_of_one_lt', ['tendsto_pow_atTop_atTop_of_one_lt'], 'Analysis/SpecificLimits/Basic.lean'),
    ('V4 (iii), the squeeze`s Bernoulli step', 'one_add_mul_le_pow', ['one_add_mul_le_pow'], 'Algebra/Order/Ring/Pow.lean'),
]


def _mgrep(pat):
    r = subprocess.run(['git', '-C', MATHLIB_CO, 'grep', '-n', '-E', pat, 'HEAD', '--', 'Mathlib/*.lean', 'Mathlib/**/*.lean'], capture_output=True,
                       text=True, encoding='utf-8', errors='replace')
    return [l[len('HEAD:'):] for l in r.stdout.split(NL) if l.strip()]


def _search(shapes, use):
    """each shape tried in turn; the hits of every shape kept; the hit the step uses is the one in `use`'s file, the rest namesakes."""
    tried, hits = [], []
    for s in shapes:
        for kind, pat in (('`theorem %s `' % s, r'^theorem %s ' % re.escape(s)), ('any declaration form, the bare word %s' % s, DECL % re.escape(s))):
            h = _mgrep(pat)
            tried.append((kind, len(h)))
            hits += [x for x in h if x not in hits]
        if any(use in x for x in hits):
            break
    chosen = next((x for x in hits if use in x), None)
    return tried, chosen, len([x for x in hits if x != chosen])


def plan(*a):
    dry = 'dry' in a
    mrev = g(MATHLIB_CO, 'rev-parse', 'HEAD').strip()
    if mrev != K.MATHLIB:
        sys.exit('### THE MATHLIB CHECKOUT IS AT %s, NOT THE PIN %s -- NOTHING WRITTEN' % (mrev[:12], K.MATHLIB[:12]))
    kt = g(K.KE, 'rev-parse', '--short=7', K.OPEN_BRANCH).strip()
    res = []
    for step, name, shapes, use in SEARCHES:
        tried, first, nsake = _search(shapes, use)
        res.append(dict(step=step, name=name, tried=tried, first=first, namesakes=nsake, use=use))
    cj = jl('b673_v4_control.json')
    L = ['b673 -- COMPONENT 2, (R283)(3): THE PLAN -- V4 AND V5 WITH THEIR SIGNS AND CONSTANTS, THE COMPOSITION, IN THE b663 FORM WITH THE '
         'CONSUMERS SECTION (%s)' % utc(), '',
         '### rows are statements, steps and priced facts. The kernel: SIDE-explicit-formula at %s = %s; Mathlib at %s (the kernel`s lake-manifest pin; '
         'the package checkout .lake/packages/mathlib read by git grep at HEAD = the pin). No Lean is written before the author`s word on this plan.' % (
             K.OPEN_BRANCH, kt, mrev[:8]), '',
         '== 0. THE SIGN S5 CONSUMES, PRINTED FROM THE BRANCH (N2: before V4 is written)',
         '  S5 (Schema/LiConverseCfg.lean :145-:146): (∀ n, 0 ≤ liCoeffCfg Z n) → ∀ ρ ∈ Z.carrier, ρ.re = 1/2, under B321.HCount and B321.HStrip.',
         '  liCoeffCfg Z n = (1/2) Σ` ρ, m_ρ Re (pairTerm n ρ) (Schema/LiCfg.lean :28-:29); pairTerm n ρ = 2 Re (liTerm n ρ) (LiWeil.lean :71,',
         '  pairTerm_eq); liTerm n ρ = 1 - (1 - ρ⁻¹) ^ n (LiWeil.lean :60). So liCoeffCfg Z n = Σ` ρ, m_ρ (1 - Re z_ρ ^ n), z_ρ = 1 - 1/ρ.',
         '  On the dominant set D (the points with the largest ‖z_ρ‖ = r_max > 1), z_ρ = r_max w_ρ, ‖w_ρ‖ = 1, and the dominant part is',
         '  Σ_D m_ρ - r_max ^ n Re s_n, s_n = Σ_D m_ρ w_ρ ^ n. A NEGATIVE COEFFICIENT NEEDS Re s_n LARGE AND POSITIVE:',
         '  ### S5 CONSUMES V4 IN THE SIGN Re s_n ≥ +c FOR INFINITELY MANY n.',
         '  The branch`s V4 (LiConverseCfg.lean :125-:128, powerSum_re_le_neg_infinitely) states the OTHER sign alone, Re s_n ≤ -c, with',
         '  c = Σ m^2 / (8 Σ m). The ruling`s V4 states both signs with c = Σ m^2 / (4 Σ m); this plan states both, the sign S5 consumes first.', '',
         '== 1. THE SEARCHES, PRINTED (`git grep -n -E <pattern> HEAD -- Mathlib/` at the pin; each name tried in its shapes, the yield of each, the first hit)']
    for x in res:
        L.append('  %-46s %-50s %s' % (x['step'], x['name'], ' ; '.join('%s yield %d' % t for t in x['tried'])))
        L.append('      %s' % (('THE ONE THE STEP USES: %s ; namesakes not used %d' % (x['first'][:140], x['namesakes'])) if x['first']
                                else '### ABSENT IN EVERY SHAPE TRIED AT %s (namesakes found %d)' % (x['use'], x['namesakes'])))
    absent = [x['name'] for x in res if not x['first']]
    L += ['  the branch`s own facts the steps consume: norm_geom_sum_le (:102), norm_sum_powerSum_le (:112), exists_dominant_point (:49),',
          '  dominant_finite (:68) -- DERIVES on the branch (relay data/b669_chi_li_landing.txt :12-:15); liCoeffCfg_summable (Schema/LiCfg.lean :36);',
          '  WeilEF.zero_sum_inv_sq_gen (the vendored Σ m / (1 + ‖γ‖^2) summable under HCount, read by liCoeffCfg_summable); Z.finite_window.', '',
          '== 2. (V4) THE POWER-SUM LEMMA, STATED IN BOTH SIGNS ((R283)(3), H1)',
          '  For a finite set s, w : ι → ℂ injective on s, ‖w i‖ = 1, w i ≠ 1, m i ≥ 1, B = Σ m_i, c = Σ m_i^2 / (4 B):',
          '  (V4+) powerSum_re_ge_infinitely : ∀ N, ∃ n ≥ N, c ≤ (Σ_i m_i w_i ^ n).re          -- THE SIGN S5 CONSUMES',
          '  (V4-) powerSum_re_le_neg_infinitely : ∀ N, ∃ n ≥ N, (Σ_i m_i w_i ^ n).re ≤ -c     -- the branch`s name, re-stated at c = Σ m^2/(4B)',
          '  the proof, finite (no limit taken): over a window [N, N + M),',
          '  (i)   |Σ_{n ∈ [N, N+M)} s_n| ≤ A, A = 2 Σ_i m_i (2/‖w_i - 1‖), uniform in N and M (geom_sum_Ico; norm_sum_powerSum_le`s form) -- the',
          '        mean of s_n tends to 0;',
          '  (ii)  Σ_window |s_n|^2 = M Σ m_i^2 + Σ_{i≠j} m_i m_j Σ_window (w_i conj w_j)^n, each w_i conj w_j ≠ 1 of modulus 1 (injectivity), so',
          '        Σ_window |s_n|^2 ≥ M Σ m_i^2 - A2 -- the mean of |s_n|^2 tends to Σ m_i^2;',
          '  (ii`) Σ_window Re(s_n^2) = Σ_{w_i w_j = 1} m_i m_j M + Re Σ_{w_i w_j ≠ 1} m_i m_j Σ_window (w_i w_j)^n ≥ -A3, the first sum ≥ 0 --',
          '        ### A STEP THE RULING`S THREE STEPS DO NOT NAME: the squeeze runs on the real part, and (Re s)^2 = (|s|^2 + Re s^2)/2, so the',
          '        ### mean of (Re s_n)^2 at or above Σ m_i^2 / 2 needs the mean of s_n^2 bounded below as well as the mean of |s_n|^2;',
          '  (iii) the squeeze: x_n = Re s_n, |x_n| ≤ B; if x_n < c for every n of the window, Σ x^2 ≤ c Σ x⁺ + B Σ x⁻ and Σ x⁻ = Σ x⁺ - Σ x, so',
          '        M Σ m^2 / 2 - A4 ≤ Σ x^2 ≤ (c + B) c M + B A; with c = Σ m^2/(4B): (c + B) c = Σ m^2/4 + Σ m^2 ^2/(16 B^2) < Σ m^2 / 2 (as',
          '        Σ m^2 < 4 B^2), so M large refutes it; the sign -c by x ↦ -x. c = Σ m^2/(4B) is the constant the squeeze gives at this B.',
          '  the constant at Q0 (relay data/b673_v4_control.txt): the dominant pair %s; c = 1/4; n = 1..%s: at or above c %s (the least n %s), at or '
          'below -c %s (the least n %s), strictly inside %s, none straddling; (C2) the mean %s, as planted %s.' % (
              ('idx %s`s reflection and its conjugate, certified dominant %s' % (cj.get('dominant_idx'), cj.get('dominant_separated'))) if cj else '### NOT RUN',
              cj.get('N'), cj.get('up'), cj.get('first_up'), cj.get('down'), cj.get('first_down'), cj.get('neither'), cj.get('c2_mean'),
              (abs((cj.get('c2_mean') or 0) - 1) < 0.01) if cj else '?'), '',
          '== 3. (V5) THE REMAINDER, IN THE FORM THE COMPOSITION CONSUMES ((R283)(3), H2)',
          '  the composition needs an UPPER bound on every point off D: λ_n ≤ (dominant part) + (the rest). The ruling`s V5 gives LOWER bounds',
          '  (each pair at or above -(r^(n/2) - r^(-n/2))^2, the on-line points at or above 0), which bound λ_n from below and do not refute',
          '  0 ≤ λ_n. The branch`s V5 (LiConverseCfg.lean :135-:138, remainder_le) is the two-sided bound the composition consumes:',
          '  (V5) remainder_le : 1 < s → ∃ C, ∀ n, |Σ` over {ρ ∈ Z | ‖1 - ρ⁻¹‖ < s} of m_ρ Re (liTerm n ρ)| ≤ C (n + 1)^2 s^n   -- KEPT AS STATED',
          '  the proof: split at R0 = max(1, 1/(s - 1)). (a) the points with ‖ρ‖ < R0 are finitely many (the strip and finite_window), each',
          '  |Re liTerm n ρ| ≤ 1 + ‖z_ρ‖^n ≤ 1 + s^n; (b) for ‖ρ‖ ≥ R0, u = 1/ρ, ‖u‖ ≤ s - 1 and 1 - (1 - u)^n = n u - Σ_{k≥2} C(n,k)(-u)^k, so',
          '  |Re liTerm n ρ - n Re u| ≤ C(n,2) ‖u‖^2 (1 + ‖u‖)^(n-2) ≤ n^2 s^n / ‖ρ‖^2 (sum_range_choose, add_pow), and |Re u| ≤ 1/‖ρ‖^2;',
          '  so the sum over (b) is at most (n + n^2 s^n) K`, K` = Σ_{‖ρ‖≥R0} m_ρ / ‖ρ‖^2, finite by HCount (WeilEF.zero_sum_inv_sq_gen);',
          '  C = 2 #(a) + 2 K`. The ruling`s K = Σ m_ρ (log r_ρ)^2 is replaced by K`, the sum HCount gives directly. The one new fact of',
          '  substance: the binomial tail bound |(1 - u)^n - 1 + n u| ≤ C(n,2) ‖u‖^2 (1 + ‖u‖)^(n-2), proved by induction on n or from add_pow.', '',
          '== 4. THE COMPOSITION (S5, H3)',
          '  Under HCount and HStrip, suppose a point ρ0 off the line. (V2) exists_dominant_point: some ρ` with r0 := ‖1 - ρ`⁻¹‖ > 1. (V3)',
          '  dominant_finite at r = (1 + r0)/2: the points with ‖z‖ ≥ r are finitely many; r_max their largest ‖z‖ (Finset.exists_max_image),',
          '  D = {‖z‖ = r_max}, finite, nonempty; s strictly between r_max and the largest ‖z‖ < r_max among them (or r if none), so every point',
          '  off D has ‖z‖ < s. On D, w_ρ = z_ρ / r_max: injective (z = 1 - 1/ρ is), unimodular, ≠ 1 (z_ρ = r_max > 1 real puts ρ = 1/(1 - r_max)',
          '  < 0, outside the strip), m_ρ ≥ 1. Split liCoeffCfg at D (Summable.sum_add_tsum_compl, liCoeffCfg_summable; pairTerm_re turns the',
          '  half of twice the real part into the real part): along (V4+)`s n, λ_n ≤ Σ_D m_ρ - c r_max^n + C (n + 1)^2 s^n, negative for n',
          '  large ((n + 1)^2 (s / r_max)^n → 0 by tendsto_pow_const_mul_const_pow_of_abs_lt_one; r_max^n → ∞) -- against 0 ≤ λ_n. So every',
          '  point is on the line: S5. ### THE COMPOSITION LINE, RE-WRITTEN BY THE NAVIGATOR`S ANSWER ON V5: λ_n ≤ Σ_D m - c·r_max^n +',
          '  C (n + 1)^2 s^n with s < r_max (the ruling`s "+ n^2·r_1^n·K" read through V5`s consumed form; relay data/b673_defects.txt (h)).', '',
          '== 5. S6, S7 AND THE NATIVE ζ CONVERSE ((R283)(5), H4, H5)',
          '  S6 li_nonneg_chi_imp_grh_chi (LiConverseCfg.lean :159-:165): as written, resting on S5 at chiZeroConfig with chiZeroConfig_local_count.',
          '  S7 li_nonneg_chi_iff_grh_chi : (∀ n, 0 ≤ liCoeffCfg (chiZeroConfig χ hχ h1) n) ↔ GRH_chi χ := ⟨S6, grh_chi_imp_li_nonneg_chi⟩',
          '     (Chi/LiForward.lean :28, DERIVES at b669).',
          '  the native ζ converse li_nonneg_imp_rh_native : (∀ n, 0 ≤ LiWeil.LiCoeff n) → RiemannHypothesis -- S5 at zetaZeroConfig (LiCoeff n =',
          '     liCoeffCfg zetaZeroConfig n by rfl, Schema/LiCfg.lean :32), HCount from Zeta23.RvM.zetaZeroConfig_local_count (Zeta23/RvM/LocalCount.lean',
          '     :310), HStrip from IsNontrivialZero`s strict strip (Zeta23/Statement.lean :105-:108), concluded through rh_equiv_mathlib.mpr',
          '     (Vendored/Bulka/Lc/LiCriterion/RHBridge.lean :43) as li_nonneg_iff_rh does (LiCriterionBridge.lean :179-:183); compiled beside the',
          '     vendored converse, replacing nothing.',
          '  ### THE TWO STATEMENTS SIDE BY SIDE (H5):',
          '     vendored  positivity_implies_RH (ReverseDirection.lean :413): (∀ n, 0 ≤ (taylorCoeff riemannXi n).re) →',
          '               (∀ s, riemannZeta s = 0 → (0 < s.re ∧ s.re < 1) → s.re = 1/2)',
          '     native    li_nonneg_imp_rh_native: (∀ n, 0 ≤ LiWeil.LiCoeff n) → RiemannHypothesis',
          '     the conclusions equal through rh_equiv_mathlib (RiemannHypothesis ↔ the strip form); the hypotheses differ in form -- Bulka`s',
          '     Taylor coefficient of ξ against the kernel`s sum over the zeros -- and li_nonneg_iff_rh already joins them at ζ (b669).', '',
          '== 6. THE ζ-NAMING WALK (N4): b669`s text walk (tools/b669_record.py :559-:621, carried), from li_nonneg_cfg_imp_online on the branch',
          '  after the attempt; S5 is generic over Z, so the walk is expected to read 0 ζ objects; its control from rh_imp_li_nonneg reads ζ.', '',
          '== 7. THE CONSUMERS SECTION ((R278)(3), standing): each bank the act writes, its consumers, each consumer`s input tolerance',
          '  data/b673_v4v5_plan.txt -> the attempt`s Lean (the statements of == 2-5 verbatim) and the one prompt; tolerance: the signs and the',
          '    constants exactly as printed, no reading by the seat.',
          '  data/b673_v4_control.txt -> H6 and == 2`s constant at Q0; tolerance: certified ball readings alone (a row straddling ±c counted NEITHER).',
          '  data/b673_runner_<kernel>.txt (Component 3) -> the gate reading per terminal and data/b673_landing.txt; tolerance: the artifact`s sha256',
          '    equal to the platform`s digest before any reading; prints at the standard three or none.',
          '  data/b673_landing.txt -> Component 4`s merges (DERIVES alone), the ceiling successor`s draft and the faces node text (written to no',
          '    keystone), OPEN_TRAILS for W-ORD-LI-CONVERSE-NATIVE; tolerance: one landing point per declaration.',
          '  data/b673_zeta_walk.txt -> N4 and H3; tolerance: a short-name over-reach counts, never an under-reach.', '',
          '== 8. THE HYPOTHESES AS THE RUN READS THEM ((R283)(5))',
          '  H1 (V4+) and (V4-) DERIVES, (V4+) in the sign S5 consumes; H2 (V5) DERIVES on the configuration with C from HCount; H3 S5 DERIVES, the',
          '  walk at 0 ζ objects; H4 S6 and S7 DERIVES at χ; H5 li_nonneg_imp_rh_native DERIVES at the standard three, the two statements printed',
          '  side by side; H6 the control prints the least n for each sign and C2 reads as planted (relay data/b673_v4_control.txt).', '',
          '== 9. THE ORDER AND THE HOST: no lean or lake on this host; the Lean written on chi-li-b669 by the Write tool after the author`s word;',
          '  print_targets.txt on the branch; one dispatch at main with the branch tip as the ref, read by its run id, the artifact by sha256.', '',
          '== 10. WHAT STOPS THE ACT AT THIS PLAN: the author`s word on (3), raised as one prompt with == 0, == 2 (ii`) and == 3.', '',
          '### ### **SEARCHES %d ; FOUND %d ; ABSENT %d%s ; THE SIGN S5 CONSUMES +c ; V4 IN BOTH SIGNS AT c = Σ m^2/(4 Σ m) ; V5 IN THE BRANCH`S '
          'TWO-SIDED FORM ; NO LEAN WRITTEN.**' % (len(res), len(res) - len(absent), len(absent), (' (' + ', '.join(absent) + ')') if absent else '')]
    print(NL.join(L[16:17 + 2 * len(res)]))
    print(L[-1])
    if dry:
        return
    put_txt('b673_v4v5_plan.txt', L)
    put_json('b673_v4v5_plan.json', dict(at=utc(), kernel=K.KERNEL, branch=K.OPEN_BRANCH, rev=kt, mathlib=mrev, searches=res,
                                         sign_consumed='+c', c='sum m^2 / (4 sum m)'))


# ================================================================================ THE AUTHOR'S ANSWERS (b672's route, carried by the Write tool)
def _session_rows():
    """the seat's session from K.ANCHOR, then each continuation (K.SESSIONS_AFTER, b646's form) from its own anchor; a continuation whose
    anchor is not a user line stops the route."""
    for sid, anc in ((K.SESSION_ID, K.ANCHOR),) + K.SESSIONS_AFTER:
        start = None
        for i, raw in enumerate(io.open('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, encoding='utf-8', errors='replace'), 1):
            try:
                o = json.loads(raw)
            except ValueError:
                continue
            if start is None and anc in raw.replace('’', "'") and o.get('type') == 'user' and not o.get('isCompactSummary'):
                start = i
            if start is not None:
                yield i, o, start, sid
        if start is None and sid != K.SESSION_ID:
            sys.exit('### THE ANCHOR %r IS NOT A USER LINE OF SESSION %s -- NOTHING WRITTEN' % (anc, sid))


def answers(*a):
    """data/b673_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; every word of the author
    delivered between BEGIN and END after the ruling (pastes unwrapped from the host's wrapper), and the author's plain messages, verbatim."""
    calls, results, words, plain_, start = [], {}, [], [], None
    for i, o, st, sid in _session_rows():
        start = st if sid == K.SESSION_ID else start
        ln = i if sid == K.SESSION_ID else '%s:%d' % (sid[:8], i)
        m = o.get('message') or {}
        cs = m.get('content')
        att = o.get('attachment') or {}
        texts = []
        if att.get('type') == 'queued_command' and isinstance(att.get('prompt'), str):
            texts = [att['prompt']]
        elif o.get('type') == 'user' and not o.get('isCompactSummary'):
            texts = [cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']
            for t in texts:
                if t and not t.lstrip().startswith(('<', 'BEGIN', 'RULING')) and len(t) < 400 and i > st:
                    plain_.append((ln, t.strip()))
        texts = [re.sub(r'(?s)^\s*<pasted_content[^>]*>\s*(.*?)\s*</pasted_content[^>]*>\s*$', r'\1', t or '') for t in texts]
        ask = set(x[1] for x in calls)
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((ln, c['id'], c['input'], o.get('timestamp')))
                ask.add(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask:
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')
                results[c.get('tool_use_id')] = (ln, t, o.get('timestamp'))
                texts.append(t)
        for t in texts:
            for mm in re.finditer(r'(?s)(?:\A\s*|=")BEGIN\s*(.*?)\s*END(?=\s*\Z|")', t or ''):
                if K.ANCHOR not in mm.group(1) and 'RULING (' not in mm.group(1)[:20]:
                    words.append((ln, mm.group(1)))
    if start is None:
        sys.exit('### THE ANCHOR IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    L, n = [], 0
    for i, cid, inp, ts in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %s, %s)' % (cid, K.SESSION_ID, i, ts))
        for k, q in enumerate(inp.get('questions', []), 1):
            n += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT', None))
        L += ['RESULT (transcript line %s, %s): %s' % (r[0], r[2], r[1]), '']
    W, seen = [], set()
    for i, w in words:
        if w in seen:
            continue
        seen.add(w)
        W += ['### THE AUTHOR`S WORD (transcript line %s), BEGIN to END, verbatim:' % i] + w.replace('\r', '').split(NL) + ['']
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b673 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d)%s.' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start,
                ''.join('; the continuation %s from its first user line carrying %r' % (s[:8], a) for s, a in K.SESSIONS_AFTER)), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b673_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b673_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


ROUTES = {'c1': c1, 'answers': answers, 'plan': plan}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b673_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
