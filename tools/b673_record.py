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
    none a number any bank carries; a stand-in run writes no bank. Carried from b672_record.py :67-:77 with b673's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b673_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b673_findings.json': dict(entry_line=99999, title='stand-in'),
        'b673_trail.json': dict(line=99999),
        'b673_act_root.json': dict(root='0' * 64, previous='41f49fc1' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
        'b673_mirror.json': dict(zip='stand-in', manifest_md5='0' * 32),
    }


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


LANDINGS = ('DERIVES', 'COMPILED, PROOF OPEN', 'NOT COMPILED')


def read_landing_row(r):
    """a row of data/b673_landing.json: a declaration, its landing (one of LANDINGS) and, where open, its obstruction by file and line;
    returns (name, landing, obstruction); raises on a row of another shape. Carried from b669_record.py :196-:204 unchanged."""
    if not isinstance(r, dict) or not r.get('name') or r.get('landing') not in LANDINGS:
        raise ValueError('landing row of another shape: %r' % (r,))
    ob = r.get('obstruction')
    if r['landing'] != 'DERIVES' and not (isinstance(ob, dict) and ob.get('file') and isinstance(ob.get('line'), int)):
        raise ValueError('an open landing without its obstruction by file and line: %r' % (r.get('name'),))
    return r['name'], r['landing'], ob


RUNNER_KEYS = ('kernel', 'branch', 'ref', 'target', 'run_id', 'conclusion', 'artifact_sha256', 'mem_low', 'stopped', 'gate', 'merged', 'tag')


def read_runner_row(r):
    """a row of the runner bank (data/b673_runner_rows.json, read by the standing runner arms) -- every key of RUNNER_KEYS present; raises
    KeyError. Carried from b672_record.py :172-:186 unchanged."""
    missing = [k for k in RUNNER_KEYS if k not in r]
    if missing:
        raise KeyError('runner row without %s' % missing)
    if r['stopped']:
        outcome = 'STOPPED BENEATH THE HOLD ON THE RUNNER'
    elif r['conclusion'] != 'success':
        outcome = 'RUN %s' % (r['conclusion'] or 'NOT CONCLUDED')
    else:
        outcome = 'GATE %s' % (r['gate'] or 'UNREAD')
    return dict(kernel=r['kernel'], outcome=outcome, merged=r['merged'], low=r['mem_low'], above_hold=(r['mem_low'] is not None and r['mem_low'] >= 2560))


READERS = ['read_score_row', 'read_head', 'read_square_row', 'read_landing_row', 'read_runner_row']


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


# ================================================================================ COMPONENT 4: THE ORDER MARKED AS THE LANDING READS, AND THE ANSWER'S ITEM
PRINT_TARGETS_LINE = 14446          # ### OPEN_TRAILS: b672's W-ORD-PRINT-TARGETS line

C4_CONVERSE_HEAD = ('*Appended 2026-10-16 by b673 under `(R283)`(5)-(6), Component 4 -- **`W-ORD-LI-CONVERSE-NATIVE`** (:14334) '
                    'DISCHARGED, AS THE LANDING READS:*')
C4_CONVERSE_BODY = (' its trigger “S5 DERIVES” met. li_nonneg_cfg_imp_online DERIVES at the standard three (relay data/b673_landing.txt, '
                    '“DECLARATIONS 29 ; DERIVES 29”, run 38960681935 at 5050a46 on chi-li-b669); chi-li-b669 merged into SIDE-explicit-formula '
                    'main as e36ea31, the merged tree the built tree; tag v0.32 peeled at e36ea31 and read back at the remote. Closed with it: '
                    'V4 in both signs (powerSum_re_ge_infinitely, powerSum_re_le_neg_infinitely, Schema/PowerSum.lean), V5 (remainder_le, '
                    'Schema/LiRemainder.lean), S6 li_nonneg_chi_imp_grh_chi and S7 li_nonneg_chi_iff_grh_chi (Schema/LiConverseCfg.lean), and '
                    'the native ζ converse li_nonneg_imp_rh_native (LiConverseNative.lean), compiled beside the vendored positivity_implies_RH '
                    'and replacing nothing. The ceiling successor and the faces line drafted in the landing bank for the author’s word, '
                    'written to no keystone.')
C4_ITEM_HEAD = ('*Appended 2026-10-16 by b673 under the navigator’s answer on the C3/C4 report (4) -- an item under **`W-ORD-PRINT-TARGETS`** '
                '(:14446):*')
C4_ITEM_BODY = (' the ζ-naming walk matches an identifier by its last component, so a proof’s local binder that shares a kernel '
                'declaration’s short name is followed as a reference (relay data/b673_defects.txt (i), (i′): S5’s binder N0 read as '
                'Zeta23.N0 at 516803e). The binder renamed at b1d4342 with the matcher unchanged; the matcher’s reach into local binders is '
                'the item, not repaired in this act (relay data/b673_rules.txt row 4).')


def c4(*a):
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', C4_CONVERSE_HEAD, NL + C4_CONVERSE_HEAD + C4_CONVERSE_BODY + NL),
          ('OPEN_TRAILS.md', C4_ITEM_HEAD, NL + C4_ITEM_HEAD + C4_ITEM_BODY + NL)], 'b673_record_lines_c4.json', 'c4',
         check=[('OPEN_TRAILS.md', K.OPEN_CONVERSE, 'W-ORD-LI-CONVERSE-NATIVE'), ('OPEN_TRAILS.md', PRINT_TARGETS_LINE, '`W-ORD-PRINT-TARGETS`')],
         dry=dry)


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


# ================================================================================ COMPONENT 3: THE ζ-NAMING WALK ON THE BRANCH (b669's, carried)
ZETA_ID = re.compile(r'\b(?:riemannZeta\w*|completedRiemannZeta\w*|\w*riemannZeta\w*|zeta_\w+|\w+_riemannZeta\w*)\b')   # ### b564_record.py :454
DECL_RE = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(?:noncomputable\s+)?(theorem|def|abbrev|structure|instance|lemma)\s+([^\s(:{\[]+)', re.M)


def _strip_comments(t):
    t = re.sub(r'/-[\s\S]*?-/', ' ', t)
    return NL.join(l.split('--', 1)[0] for l in t.split(NL))


def _decl_index(rev):
    """every declaration of the kernel's source trees (SIDEExplicitFormula/, Zeta23/) at `rev`: short name -> [(file, line, code)], the code
    the comment-stripped text from its head to the next declaration's head. Carried from b669_record.py :569-:580 unchanged."""
    import collections
    idx = collections.defaultdict(list)
    files = [f for f in g(K.KD, 'ls-tree', '-r', '--name-only', rev, '--', 'SIDEExplicitFormula', 'Zeta23').split(NL) if f.endswith('.lean')]
    for f in files:
        t = (_show(K.KD, rev, f) or '')
        heads = [(m.start(), m.group(2)) for m in DECL_RE.finditer(t)]
        for i, (pos, name) in enumerate(heads):
            end = heads[i + 1][0] if i + 1 < len(heads) else len(t)
            idx[name.split('.')[-1]].append((f, t[:pos].count(NL) + 1, _strip_comments(t[pos:end])))
    return idx


def _walk_from(idx, root):
    seen, queue, order = {root}, [root], []
    while queue:
        n = queue.pop(0)
        for f, ln, code in idx.get(n, []):
            order.append((n, f, ln, sorted(set(ZETA_ID.findall(code)))))
            for tok in set(re.findall(r"[A-Za-z_][A-Za-z0-9_'.₀-₉]*", code)):
                s = tok.split('.')[-1]
                if s in idx and s not in seen:
                    seen.add(s)
                    queue.append(s)
    return order


def walk(*a):
    """(R283)(5), H3 and N4: S5's proof walked through the kernel's source at the branch tip -- from li_nonneg_cfg_imp_online, every
    identifier of a reached declaration's comment-stripped code that names a kernel declaration (by its last component; an over-reach, never
    an under-reach) followed transitively; each reached declaration read by b564's ζ pattern. The control: the same walk from
    LiWeil.rh_imp_li_nonneg (ζ's forward half), which must reach a ζ-naming declaration. data/b673_zeta_walk.txt (.json)."""
    rev = a[0] if a else K.OPEN_BRANCH
    idx = _decl_index(rev)
    root = 'li_nonneg_cfg_imp_online'
    order = _walk_from(idx, root)
    ctl = _walk_from(idx, 'rh_imp_li_nonneg')
    ctl_z = [x for x in ctl if x[3]]
    zn = [x for x in order if x[3]]
    L = ['b673 -- COMPONENT 3: THE ζ-NAMING WALK OF THE GENERIC CONVERSE S5, ON THE BRANCH (%s)' % utc(), '',
         '### rows are declarations, in the order the walk reaches them: from %s at %s (%s), every identifier of a reached declaration`s '
         'comment-stripped code that is a kernel declaration`s name (SIDEExplicitFormula/, Zeta23/; matched by its last component, so a '
         'shared short name over-reaches and never under-reaches) followed; each reached declaration read by b564`s ζ pattern %r.' % (
             root, rev, g(K.KD, 'rev-parse', '--short=7', rev).strip(), ZETA_ID.pattern), '']
    L += ['  %-48s %s:%d %s' % (n, f, ln, ('ζ-NAMING ' + ', '.join(z[:4])) if z else '') for n, f, ln, z in order]
    L += ['', '### THE CONTROL: the same walk from LiWeil.rh_imp_li_nonneg (ζ`s forward half) reaches %d declarations, ζ-naming %d -- %s; the '
          'matcher fires where ζ is consumed.' % (len(ctl), len(ctl_z), ', '.join('%s %s:%d %s' % (n, f, ln, z[:2]) for n, f, ln, z in ctl_z[:4]) or '### NONE')]
    L += ['', '### ### **DECLARATIONS REACHED %d ; ζ-NAMING %d%s ; THE CONTROL %d.**' % (
        len(order), len(zn), (' -- ' + ', '.join(sorted(set(x[0] for x in zn)))) if zn else '', len(ctl_z))]
    put_txt('b673_zeta_walk.txt', L)
    put_json('b673_zeta_walk.json', dict(at=utc(), rev=rev, root=root, reached=len(order), zeta=[dict(name=n, file=f, line=ln, ids=z) for n, f, ln, z in zn],
                                         order=[[n, f, ln] for n, f, ln, _z in order], control_reached=len(ctl), control_zeta=len(ctl_z)))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE RUNNER (b669's, carried; no banked prints for
# ================================================================================ the act's new names, so every print is read at the standard three)
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
ERR_RE = re.compile(r'^(?:error: )?(\S+\.lean):(\d+):(\d+): error: (.*)$', re.M)


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def runner(*a):
    """`runner <run id> <ref> <workflow commit> [<branch>]`: the run read by its id; the artifact listed, downloaded by its id into memory, its
    sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP; every
    print of print_targets.txt at the ref read at the standard three or none, sorryAx named. Banked as data/b673_runner_<kernel>_run<id>.txt
    and a row of data/b673_runner_rows.json (rows keyed by run id; an earlier run's row kept). Carried from b669_record.py :635-:733."""
    import hashlib
    import zipfile
    import b569_record as R9
    run_id, ref, wfc = int(a[0]), a[1], a[2]
    branch = a[3] if len(a) > 3 else K.OPEN_BRANCH
    kern = K.KERNEL
    repo = 'psinary-sketch/' + kern
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    pt = [l.strip() for l in (_show(K.KD, ref, 'print_targets.txt') or '').split(NL) if l.strip()]
    row = dict(kernel=kern, branch=branch, ref=ref, target=None, run_id=run_id, conclusion=run.get('conclusion'),
               artifact_sha256=None, mem_low=None, stopped=False, gate=None, merged=None, tag=None)
    L = ['b673 -- COMPONENT 3, (R283)(5): THE HOSTED RUNNER FOR %s, READ BY ITS RUN ID (%s)' % (kern, utc()), '',
         '### the workflow on main: %s (build-module.yml, b658`s form; the print step imports each module of the target)' % wfc,
         '### print_targets.txt at the ref: %d names' % len(pt),
         '### the dispatch: at main, the ref input %s (the tip of %s)' % (ref, branch),
         '### the run: id %s ; %s ; %s %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('workflowName'), run.get('event'), run.get('status'), run.get('conclusion'), run.get('headSha'),
             run.get('headBranch'), run.get('createdAt'), run.get('updatedAt'))]
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        row['artifact_sha256'] = sha
        L.append('### the artifact: id %s ; name %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if digest and digest == sha else ('### DIFFER' if digest else 'no digest to compare -- NOTHING READ FROM IT')))
        if not digest or digest != sha:
            row['artifact_sha256'] = None
        else:
            with zipfile.ZipFile(io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    row['mem_low'] = int(low[-1]) if low else None
    stops = [l for l in mem.split(NL) if l.startswith('STOP ')]
    row['stopped'] = bool(stops)
    blog = T_.get('build.log', '')
    bexit = T_.get('build_exit.txt', '').strip()
    errs = [(m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)) for m in ERR_RE.finditer(blog)]
    P = dict((k_, sorted(v_)) for k_, v_ in R9.prints_axioms(T_.get('axioms.txt', '')).items())
    axerr = [l for l in T_.get('axioms.txt', '').split(NL) if ': error' in l]
    gate_rows = []
    for n in pt:
        ax = P.get(n)
        if ax is None:
            gate_rows.append((n, ax, '### NOT PRINTED'))
        elif 'sorryAx' in ax:
            gate_rows.append((n, ax, 'SORRYAX'))
        else:
            gate_rows.append((n, ax, 'STANDARD THREE OR NONE' if set(ax) <= STD3 else '### OUTSIDE THE STANDARD THREE'))
    good = [r for r in gate_rows if r[2] == 'STANDARD THREE OR NONE']
    ok = (run.get('conclusion') == 'success' and row['artifact_sha256'] and bexit == '0' and not errs and not stops and row['mem_low'] is not None
          and row['mem_low'] >= K.HOLD and len(pt) > 0 and len(good) == len(pt) and not axerr)
    row['gate'] = 'DERIVES' if ok else ('STOPPED BENEATH THE HOLD' if stops else 'NOT DERIVES')
    row['errors'] = [list(e) for e in errs]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: samples %d ; LOW %s MB ; the hold %d ; STOP lines %s' % (
              len([l for l in mem.split(NL) if 'avail_mb=' in l]), row['mem_low'], K.HOLD, stops or 'NONE'),
          '### the build: exit %s ; error lines %d ; the log`s last lines:' % (bexit or '### UNREAD', len(errs))] + \
        ['    ' + l for l in blog.rstrip(NL).split(NL)[-8:]] + ['    %s:%d:%d: %s' % e for e in errs[:60]] + [
          '### the print step: error lines %d%s ; names refused %s' % (len(axerr), (' -- ' + ' | '.join(axerr[:4])) if axerr else '',
                                                                       T_.get('axioms_refused.txt', '').strip() or 'NONE'),
          '### THE GATE READING PER TERMINAL (no banked print for the act`s new names: each read at the standard three or none, sorryAx named):'] + \
        ['  %-58s %-44s %s' % (n, ax if ax is not None else '### NOT PRINTED', v) for n, ax, v in gate_rows] + [
          '', '### ### **RUN %s ; CONCLUSION %s ; ARTIFACT SHA256 %s ; MEMORY LOW %s MB (HOLD %d) ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS %d, PRINTED %d, '
          'AT THE STANDARD THREE OR NONE %d, SORRYAX %d ; GATE %s.**' % (
              run_id, run.get('conclusion'), (row['artifact_sha256'] or '### NONE')[:16], row['mem_low'], K.HOLD, bexit or '### UNREAD', len(errs),
              len(pt), sum(1 for r in gate_rows if r[1] is not None), len(good), sum(1 for r in gate_rows if r[2] == 'SORRYAX'), row['gate'])]
    tag = 'run%d' % run_id
    put_txt('b673_runner_%s_%s.txt' % (kern, tag), L)
    if row['artifact_sha256']:
        put_txt('b673_axioms_%s.txt' % tag, T_.get('axioms.txt', '').rstrip(NL).split(NL))
        put_txt('b673_build_log_%s.txt' % tag, blog.rstrip(NL).split(NL))
    j = jl('b673_runner_rows.json') if os.path.isfile(os.path.join(D, 'b673_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if r.get('run_id') != run_id] + [row]
    gr = dict(j.get('gate_rows') or {})
    gr[str(run_id)] = [list(r) for r in gate_rows]
    put_json('b673_runner_rows.json', dict(rows=rows, gate_rows=gr, workflow_commit=wfc))
    print(L[-1])
    for e in errs[:60]:
        print('  ERROR %s:%d:%d: %s' % e)


# ================================================================================ COMPONENT 3: THE LANDING, ONE ROW PER DECLARATION (b669's, carried)
def _sorry_lines(rev, f):
    t = _show(K.KD, rev, f) or ''
    return [i for i, l in enumerate(t.split(NL), 1) if re.search(r'(?<![A-Za-z_])sorry(?![A-Za-z_])', l.split('--', 1)[0])]


def landing(*a):
    """`landing <run id> <ref>`: each print target of the run's ref landed on its own reading -- DERIVES (printed, at the standard three or
    none, the build clean), COMPILED, PROOF OPEN (printed with sorryAx; the obstruction the declaration's own `sorry` by file and line,
    else the first `sorry` of a declaration its code names), NOT COMPILED (not printed; the first error line). Each row read back through
    read_landing_row. data/b673_landing.txt (.json). Carried from b669_record.py :741-:786 with b673's names."""
    import collections
    run_id, ref = a[0], a[1]
    j = jl('b673_runner_rows.json')
    rr = [r for r in j.get('rows') or [] if str(r.get('run_id')) == run_id][0]
    gate_rows = j['gate_rows'][run_id]
    idx = _decl_index(ref)
    errs = rr.get('errors') or []
    rows = []
    for n, ax, v in gate_rows:
        short = n.split('.')[-1]
        loc = [(f, ln, code) for f, ln, code in idx.get(short, []) if f.startswith('SIDEExplicitFormula/')]
        if not loc and n.startswith('LiCriterion.'):
            loc = [('Vendored/Bulka (vendored, not walked)', 0, '')]
        f, ln, code = loc[0] if loc else ('?', 0, '')
        if v == 'STANDARD THREE OR NONE' and rr.get('artifact_sha256') and not errs and rr.get('gate') == 'DERIVES':
            rows.append(dict(name=n, landing='DERIVES', axioms=ax, file=f, line=ln, obstruction=None))
        elif v == 'SORRYAX':
            own = [x for x in _sorry_lines(ref, f) if ln <= x < ln + code.count(NL) + 1]
            ob = dict(file=f, line=own[0], why='its own sorry') if own else dict(file=f, line=ln, why='sorryAx printed; no own sorry line')
            rows.append(dict(name=n, landing='COMPILED, PROOF OPEN', axioms=ax, file=f, line=ln, obstruction=ob))
        else:
            e0 = errs[0] if errs else [f, ln, 0, v]
            rows.append(dict(name=n, landing='NOT COMPILED', axioms=ax, file=f, line=ln, obstruction=dict(file=e0[0], line=int(e0[1]), why=str(e0[3])[:200])))
    for r in rows:
        read_landing_row(r)
    c = collections.Counter(r['landing'] for r in rows)
    L = ['b673 -- COMPONENT 3, (R283)(5): EACH DECLARATION LANDED ON ITS OWN READING (%s)' % utc(), '',
         '### rows are declarations: the name, its landing, its file and line at %s (%s), its printed axioms, and where open the obstruction by '
         'file and line. The run: %s (relay data/b673_runner_%s_run%s.txt); the earlier runs of the attempt, each at its own tip, in '
         'data/b673_runner_rows.json and data/b673_defects.txt (l).' % (ref[:8], K.OPEN_BRANCH, run_id, K.KERNEL, run_id), '']
    for r in rows:
        L.append('  %-62s %-22s %s:%s  %s' % (r['name'], r['landing'], r['file'], r['line'], r['axioms']))
        if r['obstruction']:
            L.append('  %-62s %-22s OBSTRUCTION %s:%s (%s)' % ('', '', r['obstruction']['file'], r['obstruction']['line'], r['obstruction']['why']))
    L += ['', '### ### **DECLARATIONS %d ; %s.**' % (len(rows), ' ; '.join('%s %d' % kv for kv in sorted(c.items())))]
    files = sorted(set(r['file'] for r in rows if r['file'].startswith('SIDEExplicitFormula/')))
    put_txt('b673_landing.txt', L)
    put_json('b673_landing.json', dict(at=utc(), run_id=int(run_id), ref=ref, rows=rows, file_list=files))
    print(NL.join(L[3:]))


# ================================================================================ COMPONENT 3: H5, THE TWO ζ CONVERSES SIDE BY SIDE
H5_DECLS = (('native', 'SIDEExplicitFormula/LiConverseNative.lean', 'theorem li_nonneg_imp_rh_native',
             'SIDEExplicitFormula.LiConverseNative.li_nonneg_imp_rh_native'),
            ('vendored', 'Vendored/Bulka/Lc/LiCriterion/ReverseDirection.lean', 'theorem positivity_implies_RH',
             'LiCriterion.positivity_implies_RH'))


def _statement(rev, f, head):
    """a declaration's statement as its source carries it at `rev`: from its head to the `:=` that opens the proof, whitespace joined."""
    t = _show(K.KD, rev, f) or ''
    i = t.find(head)
    if i < 0:
        return None, None
    j = t.find(':=', i)
    return t[:i].count(NL) + 1, ' '.join(t[i:j].split())


def h5(*a):
    """`h5 <rev> <run id>`: (R283)(5) H5 and the navigator's answer on the C3/C4 report (5)(b) -- li_nonneg_imp_rh_native and the vendored
    positivity_implies_RH printed side by side, each statement from its source at `rev`, each axiom line from the run's print bank
    (data/b673_axioms_run<id>.txt); the hypothesis and conclusion forms compared as text, and the native conclusion read through
    rh_equiv_mathlib's statement (RHBridge.lean) at the same rev. data/b673_h5.txt (.json)."""
    import b569_record as R9
    rev, run_id = a[0], a[1]
    P = R9.prints_axioms(rdn('b673_axioms_run%s.txt' % run_id))
    rows = []
    for tag, f, head, full in H5_DECLS:
        ln, st = _statement(rev, f, head)
        body = st[len(head):].strip() if st else ''
        body = body[1:].strip() if body.startswith(':') else body
        hyp, _arrow, concl = body.partition(' → ')
        rows.append(dict(tag=tag, name=full, file=f, line=ln, statement=st, hypothesis=hyp.strip(), conclusion=concl.strip(), axioms=P.get(full)))
    brl, br = _statement(rev, 'Vendored/Bulka/Lc/LiCriterion/RHBridge.lean', 'theorem rh_equiv_mathlib')
    nat, ven = rows
    same_hyp = nat['hypothesis'] == ven['hypothesis']
    same_concl = nat['conclusion'] == ven['conclusion']
    bridge = bool(br) and 'RiemannHypothesis ↔' in br and ven['conclusion'] in br
    _sp = lambda x: re.sub(r'\s+', '', x or '')
    bridge_sp = bool(br) and 'RiemannHypothesis↔' in _sp(br) and _sp(ven['conclusion']) in _sp(br)
    L = ['b673 -- COMPONENT 3, (R283)(5) H5: THE NATIVE AND THE VENDORED ζ CONVERSE, SIDE BY SIDE (%s)' % utc(), '',
         '### rows are the two declarations: each statement from its source at %s (%s), its axioms from relay data/b673_axioms_run%s.txt; then '
         'the hypothesis and conclusion forms compared as text, the comparison the text`s and not a proof of equality.' % (
             rev[:8], g(K.KD, 'rev-parse', '--short=7', rev).strip(), run_id), '']
    for r in rows:
        L += ['  %-9s %s  (%s:%s)' % (r['tag'], r['name'], r['file'], r['line']),
              '            statement   %s' % r['statement'],
              '            hypothesis  %s' % r['hypothesis'],
              '            conclusion  %s' % r['conclusion'],
              '            axioms      %s' % r['axioms'], '']
    L += ['  the bridge  LiCriterion.rh_equiv_mathlib  (Vendored/Bulka/Lc/LiCriterion/RHBridge.lean:%s)' % brl,
          '            statement   %s' % br, '',
          '### THE HYPOTHESES AS TEXT: %s -- the native premise is the kernel`s LiWeil.LiCoeff n, a sum over the zero configuration; the vendored '
          'premise is the real part of the Taylor coefficient of Bulka`s riemannXi; li_nonneg_iff_rh (LiCriterionBridge.lean :179) joins them at ζ '
          'through li_coeff_eq_taylorCoeff.' % ('EQUAL' if same_hyp else 'DIFFERENT'),
          '### THE CONCLUSIONS AS TEXT: %s; the native conclusion RiemannHypothesis and the vendored strip form are the two sides of '
          'rh_equiv_mathlib, whose statement carries the vendored conclusion character for character: %s; with whitespace removed from both '
          '(the vendored `1/2` against the bridge`s `1 / 2`): %s.' % ('EQUAL' if same_concl else 'DIFFERENT', bridge, bridge_sp),
          '', '### ### **H5: li_nonneg_imp_rh_native AXIOMS %s ; positivity_implies_RH AXIOMS %s ; HYPOTHESES %s AS TEXT ; CONCLUSIONS %s AS TEXT, '
          'JOINED BY rh_equiv_mathlib: CHARACTER FOR CHARACTER %s, WHITESPACE REMOVED %s.**' % (
              nat['axioms'], ven['axioms'], 'EQUAL' if same_hyp else 'DIFFERENT', 'EQUAL' if same_concl else 'DIFFERENT', bridge, bridge_sp)]
    put_txt('b673_h5.txt', L)
    put_json('b673_h5.json', dict(at=utc(), rev=rev, run_id=int(run_id), rows=rows, bridge=dict(line=brl, statement=br, carries_vendored=bridge,
                                                                                                carries_vendored_whitespace_removed=bridge_sp),
                                  hypotheses_equal=same_hyp, conclusions_equal=same_concl))
    print(NL.join(L[3:]))


# ================================================================================ COMPONENT 4: THE MERGE ON THE RUNNER ROW (b669's `merged`, carried)
def merged(*a):
    """`merged <run id> <merge sha> <tag>`: the merge of the DERIVES run's tree recorded on its runner row -- the tag's peeled SHA read
    locally, the merged tree against the built tree, the run's gate DERIVES; nothing written unless all three hold."""
    run_id, sha, tag = a[0], a[1], a[2]
    j = jl('b673_runner_rows.json')
    rows = [r for r in j.get('rows') or [] if str(r.get('run_id')) == run_id]
    if len(rows) != 1 or rows[0].get('gate') != 'DERIVES':
        sys.exit('### RUN %s IS NOT ONE DERIVES ROW -- NOTHING WRITTEN' % run_id)
    built = rows[0]['ref']
    peeled = g(K.KD, 'rev-parse', '%s^{commit}' % tag).strip()
    tree_eq = g(K.KD, 'rev-parse', sha + '^{tree}').strip() == g(K.KD, 'rev-parse', built + '^{tree}').strip()
    if peeled != sha or not tree_eq:
        sys.exit('### THE TAG PEELS TO %s, THE TREES EQUAL %s -- NOTHING WRITTEN' % (peeled[:12], tree_eq))
    rows[0]['merged'], rows[0]['tag'] = sha, tag
    put_json('b673_runner_rows.json', j)
    print('  run %s : merged %s ; tag %s peeled %s ; the merged tree the built tree %s' % (run_id, sha[:12], tag, peeled[:12], tree_eq))


# ================================================================================ (R283)(5): THE HYPOTHESES, EACH READ OFF ITS BANK'S PRINTED LINE
def _landing_of(name):
    rows = dict((r['name'].split('.')[-1], r) for r in jl('b673_landing.json').get('rows') or [])
    r = rows.get(name)
    return read_landing_row(r)[1] if r else '### NOT IN THE LANDING BANK'


def _hyp():
    wt, h5t, ct = rdn('b673_zeta_walk.txt'), rdn('b673_h5.txt'), rdn('b673_v4_control.txt')
    wj, cj = jl('b673_zeta_walk.json'), jl('b673_v4_control.json')
    v4, v5, s5 = _landing_of('powerSum_re_ge_infinitely'), _landing_of('remainder_le'), _landing_of('li_nonneg_cfg_imp_online')
    s6, s7, nat = _landing_of('li_nonneg_chi_imp_grh_chi'), _landing_of('li_nonneg_chi_iff_grh_chi'), _landing_of('li_nonneg_imp_rh_native')
    walk0 = '### ### **DECLARATIONS REACHED' in wt and ' ; ζ-NAMING 0 ; ' in wt and (wj.get('control_zeta') or 0) >= 1 and wj.get('rev') == K.TIP
    h5m = re.search(r'\*\*H5: (.*?)\.\*\*', h5t)
    std3 = "AXIOMS ['propext', 'Classical.choice', 'Quot.sound'] ; positivity_implies_RH AXIOMS ['propext', 'Classical.choice', 'Quot.sound']" in h5t
    joined = 'WHITESPACE REMOVED True' in h5t
    textual = 'CONCLUSIONS EQUAL AS TEXT' in h5t
    ctl = (cj.get('first_up') is not None and cj.get('first_down') is not None and abs((cj.get('c2_mean') or 0) - 1) < 0.01
           and abs(cj.get('control_mean') or 9) < 0.01 and 'AS PLANTED: True' in ct)
    return {
        'H1': ['HELD' if v4 == 'DERIVES' else 'REFUTED', 'powerSum_re_ge_infinitely, V4 in the sign S5 consumes (c ≤ Re s_n infinitely often, '
               'c = Σ m^2 / (4 Σ m)), lands %s at the standard three (relay data/b673_landing.txt, run 38960681935)' % v4],
        'H2': ['HELD' if v5 == 'DERIVES' else 'REFUTED', 'remainder_le, V5 on the configuration under B321.HCount and B321.HStrip, its constant '
               'from the local count through WeilEF.zero_sum_inv_sq_gen (summable_rest, rest_term_le), lands %s (relay data/b673_landing.txt)' % v5],
        'H3': ['HELD' if s5 == 'DERIVES' and walk0 else 'REFUTED', 'li_nonneg_cfg_imp_online lands %s; the ζ-naming walk at %s reads ζ-naming 0, '
               'its control %s (relay data/b673_zeta_walk.txt); the walk at 516803e read 2 through the local binder N0 (relay '
               'data/b673_defects.txt (i), (i′))' % (s5, K.TIP[:7], wj.get('control_zeta'))],
        'H4': ['HELD' if s6 == s7 == 'DERIVES' else 'REFUTED', 'li_nonneg_chi_imp_grh_chi lands %s and li_nonneg_chi_iff_grh_chi lands %s at χ '
               '(relay data/b673_landing.txt)' % (s6, s7)],
        'H5': [('HELD THROUGH rh_equiv_mathlib; REFUTED AS TEXT' if nat == 'DERIVES' and std3 and joined and not textual else
                ('HELD' if nat == 'DERIVES' and std3 and textual else 'REFUTED')),
               'li_nonneg_imp_rh_native lands %s at the standard three beside the vendored positivity_implies_RH, the two statements printed side '
               'by side (relay data/b673_h5.txt: %s); its conclusion RiemannHypothesis and the vendored strip form are the two sides of '
               'rh_equiv_mathlib, not the same text' % (nat, h5m.group(1) if h5m else '### UNREAD')],
        'H6': ['HELD' if ctl else 'REFUTED', 'the control at Q0 (relay data/b673_v4_control.txt): the least n at or above c = 1/4 is %s, at or '
               'below -c %s; (C2) planted, its mean %.5f, tending to 1, the control`s own mean %.5f, tending to 0' % (
                   cj.get('first_up'), cj.get('first_down'), cj.get('c2_mean') or 0, cj.get('control_mean') or 0)],
    }


def hypotheses(*a):
    H = _hyp()
    for k in H:
        read_score_row(k, H[k])
    L = ['b673 -- (R283)(5): THE HYPOTHESES, EACH READ OFF ITS BANK`S PRINTED LINE (%s)' % utc(), ''] + [
        '  (%s) %s -- %s' % (k, v[0], v[1]) for k, v in sorted(H.items())] + [
        '', '### ### **H1 %s ; H2 %s ; H3 %s ; H4 %s ; H5 %s ; H6 %s.**' % tuple(H[k][0] for k in ('H1', 'H2', 'H3', 'H4', 'H5', 'H6'))]
    print(NL.join(L[2:]))
    if 'dry' in a:
        return
    put_txt('b673_hypotheses.txt', L)
    put_json('b673_hypotheses.json', H)


# ================================================================================ THE LATE ROUTES (b672's, carried by the Edit tool; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for sid, anc in K.SESSIONS_AFTER:
        more = ER.capture('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, anc,
                          'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % sid)
        if not more:
            sys.exit('### THE CONTINUATION SESSION %s READ NO COMMAND (the anchor %r not found as a user line) -- NOTHING WRITTEN' % (sid, anc))
        rows += [dict(r, src=r['src'] + ' ' + sid[:8]) for r in more]
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


MOVE_OR_DELETE = re.compile(r'\bgit\s+(-C\s+\S+\s+)?(mv|rm)\b|\bgit\s+(-C\s+\S+\s+)?branch\s+-[dD]\b|(^|[;&|]\s*|\s)rm\s+-|Remove' + r'-Item|\bos\.remove\b')


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    mv = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    L = ['b673 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1) AND THE MOVES AND DELETES (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; MOVE OR DELETE COMMANDS %d.**' % (
        len(rows), len(hits), len(lean), len(mv))]
    put_txt('b673_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b673_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], moves_deletes=[r['n'] for r in mv]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r in mv:
        print('  MOVE OR DELETE #%d: %s' % (r['n'], r['cmd'].split(NL)[0][:200]))


def kernels(*a):
    import b641_record as R41
    put_json('b673_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


DEFECT_ROW = re.compile(r'^    \(([a-z])\) ')


def _defect_short():
    out = []
    L = rdn('b673_defects.txt').split(NL)
    for i, l in enumerate(L):
        if DEFECT_ROW.match(l):
            j = i + 1
            while j < len(L) and L[j].startswith('    ') and not DEFECT_ROW.match(L[j]) and not L[j].startswith('    ###') \
                    and not L[j].startswith('    (i′)'):
                j += 1
            m = re.match(r'^\(([a-z])\) (.*?)\.(?= |$)', ' '.join(x.strip() for x in L[i:j]))
            if m:
                out.append(m.group(0)[:-1])
    return out


def defects(*a):
    t = rdn('b673_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b673_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b673_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b673_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b673_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands|'
                          r'mirror.*)\.(txt|json|md)$')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b673_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)]
                  + list(K.SHARED_APPENDED))


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if not b_.endswith('.gz') and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b673_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b673'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b673_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith('.gz')][0]
    with tempfile.TemporaryDirectory(prefix='b673_ra_') as tmp:
        cp = os.path.join(tmp, os.path.basename(bank_))
        b_ = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b_[0] ^= 0x01
        open(cp, 'wb').write(bytes(b_))
        items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    late = []
    for it in J['items']:
        p = it.split()
        if p[0].startswith('data/'):
            fp = os.path.join(ROOT, *p[0].split('/'))
            if not os.path.exists(fp) or AR.sha256_file(fp) != p[1]:
                late.append('%s changed' % p[0])
            elif os.path.getmtime(fp) > J.get('at_epoch', 0) + AR.ORDER_SLACK:
                late.append('%s written after the root' % p[0])
    L = ['b673 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b673_root_arm.txt', L)
    put_json('b673_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    before = _rows_state(json.loads(_show(RELAY, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b673 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b673_table_final.txt', L)
    put_json('b673_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b673_registration_2026-10-16.txt'
FACE = os.path.join(D, 'b673_registration_2026-10-16.txt')


def gatebanks(*a):
    """the gate's steps between the face and the lock (b665's order), each tool's output banked by this route, never by a shell redirect."""
    import gate_hash as G
    env = dict(os.environ, PYTHONIOENCODING='utf-8')

    def runb(args, out):
        r = subprocess.run([sys.executable] + args, capture_output=True, cwd=ROOT, env=env)
        b_ = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            open(p + '.tmp', 'wb').write(b_)
            os.replace(p + '.tmp', p)
        return r.returncode, b_.decode('utf-8', 'replace')
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b673_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b673_regspec.py')], 'b673_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b673_satisfiable.json', '--emit', 'b673'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b673_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b673_census_stepzero.txt'), ('b327_faces_census.py', 'b673_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b673_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b673'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b673_reg_gate.txt', 'data/b673_reg_termscan.txt', 'data/b673_regspec_run.txt', 'data/audit_b673_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES, (N1)-(N5) OF THE FERRY AND THE SEAT'S (S1)-(S3)
# ### carried from b672_record.py :1079-:1227 by the Edit tool, every predicate re-written against (R283)'s expectations and this act's banks
import collections                 # noqa: E402
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b672_closing_push_out.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
PRIOR_MAIN = '115abfe'               # ### SIDE-explicit-formula main before the act (b669's merge, v0.31)
BRANCH_FILES = ('SIDEExplicitFormula/LiConverseNative.lean', 'SIDEExplicitFormula/Schema/LiConverseCfg.lean',
                'SIDEExplicitFormula/Schema/LiRemainder.lean', 'SIDEExplicitFormula/Schema/PowerSum.lean', 'print_targets.txt')


def TRAIL_HEAD():
    return ('### b673 — lane two, act one hundred, the research act under (R283): V4 and V5 on the configuration; the generic Li converse, '
            'the χ converse and the χ-Li equivalence composed; the native ζ converse beside the vendored one; v0.32')


def _calls():
    return jl('b673_author_answers.json').get('calls') or []


def _ledger_adds():
    out = []
    for f in N5_PP:
        old = _show(PP, K.PRE_PP, f) or ''
        now = rd(os.path.join(PP, f))
        out.append(now[len(old):] if now.startswith(old) else now)
    return NL.join(out)


def _first_commit(repo, path, pre):
    """the first commit since the act began that touches `path`: (epoch, short hash), or None."""
    l = [x for x in g(repo, 'log', '--reverse', '--format=%ct %h', pre + '..HEAD', '--', path).split(NL) if x.strip()]
    return (int(l[0].split()[0]), l[0].split()[1]) if l else None


def _kernel_ct(rev):
    t = g(K.KD, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t else None


def _kernel_main_moves():
    """the commits SIDE-explicit-formula's main gained since the act began, by first parent: (short hash, parents)."""
    return [(l.split()[0], l.split()[1:]) for l in g(K.KD, 'log', '--first-parent', '--format=%h %p', PRIOR_MAIN + '..main').split(NL) if l.strip()]


def _n1():
    cm = jl('b673_commands.json')
    ok = bool(cm) and not cm.get('local_lean')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b673_commands.txt); every build on the hosted runner, four '
        'runs each at its own tip (relay data/b673_runner_rows.json)' % (cm.get('local_lean') if cm else '### UNREAD'))


def _n2():
    kt = _kernel_ct(K.FIRST_KERNEL_COMMIT)
    pc = _first_commit(RELAY, 'data/b673_v4v5_plan.txt', K.PRE_RELAY)
    cc = _first_commit(RELAY, 'data/b673_v4_control.txt', K.PRE_RELAY)
    plan = rdn('b673_v4v5_plan.txt')
    sign = '### S5 CONSUMES V4 IN THE SIGN Re s_n ≥ +c FOR INFINITELY MANY n.' in plan
    traced = all(x in plan for x in ('== 2. (V4)', '== 3. (V5)', '== 4. THE COMPOSITION', '(i)', '(ii)', '(ii`)', '(iii)'))
    cj = jl('b673_v4_control.json')
    least = cj.get('first_up') is not None and cj.get('first_down') is not None
    order = bool(kt and pc and cc and pc[0] < kt and cc[0] < kt)
    ok = sign and traced and least and order
    return ('HELD' if ok else 'REFUTED'), (
        'the plan prints the sign S5 consumes, Re s_n ≥ +c, %s, its terms traced through V4`s four steps, V5 and the composition %s (relay '
        'data/b673_v4v5_plan.txt, committed %s); the control`s least n for each sign printed, %s and %s (relay data/b673_v4_control.txt, '
        'committed %s); both before the first Lean commit SIDE-explicit-formula %s, %s' % (
            sign, traced, pc[1] if pc else '### NONE', cj.get('first_up'), cj.get('first_down'), cc[1] if cc else '### NONE',
            K.FIRST_KERNEL_COMMIT, order))


def _n3():
    lj = jl('b673_landing.json')
    rows = lj.get('rows') or []
    try:
        lands = [read_landing_row(r)[1] for r in rows]
    except Exception:
        lands = []
    one = len(rows) == len(set(r['name'] for r in rows)) == K.LANDED and len(lands) == len(rows)
    sorry = [f for f in BRANCH_FILES if f.endswith('.lean') and re.search(r'(?<![A-Za-z_])sorry(?![A-Za-z_])',
                                                                             NL.join(l.split('--', 1)[0] for l in (_show(K.KD, 'main', f) or '').split(NL)))]
    open_ = [r['name'] for r in rows if r['landing'] != 'DERIVES']
    ok = one and not sorry and not open_
    return ('HELD (the split clause VACUOUS: no declaration open, no split)' if ok else 'REFUTED'), (
        'declarations %d, each with one landing point (relay data/b673_landing.txt): %s; `sorry` in code in the act`s files on main %s; '
        'open declarations %s, so no branch was split and none is left open on main' % (
            len(rows), dict(collections.Counter(lands)), sorry or 'NONE', open_ or 'NONE'))


def _n4():
    H = jl('b673_hypotheses.json')
    walk_ok = (H.get('H3') or ['?'])[0] == 'HELD'
    h5t = rdn('b673_h5.txt')
    side = 'vendored  LiCriterion.positivity_implies_RH' in h5t and 'native    SIDEExplicitFormula.LiConverseNative.li_nonneg_imp_rh_native' in h5t \
        and '            conclusion  RiemannHypothesis' in h5t
    ok = walk_ok and side
    return ('HELD' if ok else 'REFUTED'), (
        'S5 lands DERIVES and the walk reads 0 ζ objects in its closure at %s (H3 %s; relay data/b673_zeta_walk.txt), the 516803e reading of 2 '
        'through a local binder entered (relay data/b673_defects.txt (i′)); the native converse`s conclusion printed beside the vendored one %s '
        '(relay data/b673_h5.txt)' % (K.TIP[:7], (H.get('H3') or ['?'])[0], side))


def _n5():
    face = jl('b673_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    moves = _kernel_main_moves()
    main_ok = len(moves) == 1 and moves[0][0] == K.MERGE[:7] and sorted(moves[0][1]) == sorted([PRIOR_MAIN, K.TIP[:7]])
    kfiles = sorted(x for x in g(K.KD, 'diff', '--name-only', PRIOR_MAIN, 'main').split(NL) if x.strip())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b673_|audit_b673_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b673_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    rr = [x for x in ('README.md', 'REGISTRY.md') if x in pp_ch]
    ok = others_ok and main_ok and kfiles == sorted(BRANCH_FILES) and not pp_beyond and not kinds_beyond and not differ and not new_arms and not pat and not rr
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); SIDE-explicit-formula`s main moved by %s alone (the merge '
            'of Component 4, parents %s) %s, its files beyond the branch`s %s; every kernel as the face read it after the merge %s; README and '
            'REGISTRY written %s; standing arms added: %s (the act`s arms over its own banks %d); sealed tools not agreeing %s; PLACE-papers '
            'beyond the ledgers: %s; relay files of a kind beyond the banks, the act`s tools, the table, the root list and b672`s push-out bank: '
            '%s; "patent" in the ledger lines: %s; outbound requests: the seat`s git reads and pushes and the gh workflow, run and artifact '
            'calls to the author`s own repositories at github.com, no search made, so no identifier of the author placed in a request' % (
                K.DRAFT, [m[0] for m in moves], [m[1] for m in moves], main_ok, [x for x in kfiles if x not in BRANCH_FILES] or 'NONE', others_ok,
                rr or 'NONE', new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE', pat or 'NONE'))


def scores(*a):
    TF, RA = jl('b673_table_final.json'), jl('b673_root_arm.json')
    _r, _n, sh = seal_hashes()
    S = {
        'N1': _n1(), 'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))
    if 'dry' in a:
        return
    put_json('b673_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _title():
    cj = jl('b673_v4_control.json')
    land = dict((r['name'].split('.')[-1], r['landing']) for r in jl('b673_landing.json').get('rows') or [])
    return ('## V4 %s and V5 %s on the configuration; the generic Li converse %s; the χ-Li equivalence %s; the native ζ converse %s; the V4 '
            'constant at Q0 read at n = %s; v0.32' % (land.get('powerSum_re_ge_infinitely', 'OPEN'), land.get('remainder_le', 'OPEN'),
                                                     land.get('li_nonneg_cfg_imp_online', 'OPEN'), land.get('li_nonneg_chi_iff_grh_chi', 'OPEN'),
                                                     land.get('li_nonneg_imp_rh_native', 'OPEN'), cj.get('first_up')))


def _finding_text():
    S, J, H = jl('b673_scores.json'), jl('b673_act_root.json'), jl('b673_hypotheses.json')
    cj = jl('b673_v4_control.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b673_author_answers.txt'), re.M))
    c1 = _rl_lines('b673_record_lines.json') + ['?']
    c4 = _rl_lines('b673_record_lines_c4.json') + ['?'] * 2
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    mids = re.findall(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    hv = ', '.join('%s %s' % (k, (H.get(k) or ['?'])[0]) for k in ('H1', 'H2', 'H3', 'H4', 'H5', 'H6'))
    lj = jl('b673_landing.json')
    nd = len(lj.get('rows') or [])
    e = ['', _title(), '',
         'Li’s criterion now has a kernel-native converse over any zero configuration under its local count and the open strip, and so at '
         'primitive χ ≠ 1 an equivalence (li_nonneg_chi_iff_grh_chi) and at ζ a second converse beside the vendored one (li_nonneg_imp_rh_native, '
         'a stated implication from Li nonnegativity to RiemannHypothesis); %d declarations DERIVE at the standard three, merged as v0.32. '
         'Nothing here proves RH or GRH.' % nd, '',
         '*Filed at b673 on the author’s ruling `(R283)` and the navigator’s answers (%d questions in %d calls, and the pasted answers). Banks: '
         'relay `data/b673_v4v5_plan.txt`, `data/b673_v4_control.txt`, `data/b673_runner_rows.json`, `data/b673_landing.txt`, '
         '`data/b673_zeta_walk.txt`, `data/b673_h5.txt`, `data/b673_hypotheses.txt`, `data/b673_act_root.txt`.*' % (n_ans, len(_calls())), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed and each raised and answered; the mid-act '
         'checks of `(R278)`(4), %d prints, the last %s of %s OK. b672 at its weight (FINDINGS :%s).' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', len(mids), mids[-1][1] if mids else '?',
             mids[-1][0] if mids else '?', c1[0]), '',
         '**The plan and the control** (`(R283)`(3), (4)): the sign S5 consumes printed first, Re s_n ≥ +c, the branch’s V4 stating the other; '
         'V4 in both signs at c = Σ m² / (4 Σ m) with a fourth step, the mean of s_n² bounded below, and V5 kept two-sided as the composition '
         'consumes it (defects (g), (h), the navigator’s). The control at Q0 before any Lean: c = 1/4, the least n at or above c %s and at or '
         'below −c %s over n ≤ %s, the planted mean %.4f.' % (cj.get('first_up'), cj.get('first_down'), cj.get('N'), cj.get('c2_mean') or 0), '',
         '**The attempt** (`(R283)`(5)): on chi-li-b669, V4 (Schema/PowerSum.lean), V5 (Schema/LiRemainder.lean), S5 with its split at the '
         'dominant set, S6, S7 (Schema/LiConverseCfg.lean) and the native ζ converse (LiConverseNative.lean), by the Write tool; four runs on '
         'the hosted runner, one per tree state (relay data/b673_rules.txt row 1), the first three failing at their tips and repaired, the '
         'fourth DERIVES at 5050a46: %d terminals at the standard three, sorryAx 0. The ζ-naming walk on S5 reads 0 at the tip; at 516803e '
         'it read 2, reached through a local binder named as a kernel declaration (defects (i), (i′)).' % nd, '',
         '**The merge** (Component 4): chi-li-b669 merged as e36ea31, the merged tree the built tree, tag v0.32 read back; '
         '`W-ORD-LI-CONVERSE-NATIVE` DISCHARGED (OPEN_TRAILS :%s); the walk’s reach into local binders an item under `W-ORD-PRINT-TARGETS` '
         '(:%s).' % (c4[0], c4[1]), '',
         '**H5:** the native statement `(∀ n, 0 ≤ LiCoeff n) → RiemannHypothesis` and the vendored `(∀ n, 0 ≤ (taylorCoeff riemannXi n).re) → '
         '(the strip form)` printed side by side; their hypotheses differ as text, their conclusions are the two sides of rh_equiv_mathlib. '
         'The hypotheses: %s.' % hv, '',
         '**The root.** b673 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b669’s converse plan and the vendored converse, and closes the '
         'route b669 left open at V4 and V5; it is re-read by the regeneration of the faces page, where the drafted line on unequal converses '
         'waits for the author’s word, and by the claim ceiling’s next sentence, drafted in the landing bank. It strengthens the programme’s '
         'offering of compiled faces of the one open clause: the Li face is now an equivalence at primitive χ and has two converses at ζ, each '
         'printed with its axioms.', '',
         '**Carried to:** the ceiling successor and the faces line for the author’s word (relay data/b673_landing.txt); the walk’s binder reach '
         'under `W-ORD-PRINT-TARGETS`; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero: the native converse is an implication whose premise is not proved.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) “one dispatch” read as one dispatch per tree state, confirmed by the navigator’s answer on the C3/C4 report (relay '
              'data/b673_rules.txt row 1); (2) V4 stated in both signs at c = Σ m² / (4 Σ m) and V5 kept two-sided, by the answer on the plan; '
              '(3) H5 scored at the conclusion through rh_equiv_mathlib and printed as text beside it')


def _trail_text():
    S, J = jl('b673_scores.json'), jl('b673_act_root.json')
    fj = jl('b673_findings.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b673_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b673_record_lines.json')
    c4 = _rl_lines('b673_record_lines_c4.json')
    lj = jl('b673_landing.json')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R283) ratified.** (1) b672 at its weight. (2) V4 and V5 on chi-li-b669. (3) The plan. (4) The control at Q0. (5) The attempt. '
             '(6) The landing. (7) The read-first bank. (8) The draft held at v5. (9) The act after.', '',
             '**Entered:** FINDINGS.md:%s (b672’s weight), :%s (the entry); OPEN_TRAILS.md:%s (W-ORD-LI-CONVERSE-NATIVE discharged, the '
             'W-ORD-PRINT-TARGETS item); this record.' % (c1[0] if c1 else '?', fj.get('entry_line'), ', :'.join(str(x) for x in c4)), '',
             '**Act root:** b673 `%s` (previous `%s`, b672’s; relay data/act_roots.txt), computed after the last bank it names, every one of them '
             'LF.' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d calls (relay data/b673_author_answers.txt), the one prompt of `(R283)`(3) raised before '
             'any Lean, and the navigator’s pasted answers; none after the root.' % (n_ans, len(_calls())), '',
             '**The converse and its runs:** %d declarations DERIVE (relay data/b673_landing.txt), run 38960681935 at 5050a46 after three runs '
             'repaired at their tips; merged at e36ea31, v0.32; the walk on S5 at 0.' % len(lj.get('rows') or []), '',
             '**The open orders:** `W-ORD-LI-CONVERSE-NATIVE` discharged; `W-ORD-PRINT-TARGETS` with the walk’s binder item; `W-ORD-ONE-COPY`; '
             '`W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; `W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; the ledger split at the b680 reading act.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b673_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b673_scores.json')
    L = ['=' * 104, 'b673 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b673_hypotheses.txt').rstrip(NL).split(NL) + [''] + rdn('b673_defects.txt').rstrip(NL).split(NL)
    put_txt('b673_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b673_scores.json', 'b673_findings.json', 'b673_trail.json', 'b673_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b673_record_lines.json') + ['?']
    c4 = _rl_lines('b673_record_lines_c4.json') + ['?'] * 2
    H = jl('b673_hypotheses.json')
    lj = jl('b673_landing.json')
    L = ['b673 -- THE COMPONENTS, BANKED UNDER (R283).', '',
         '### COMPONENT 0 : the citation check (data/b673_citation_check.txt), step zero (data/b673_ferry.txt, data/b673_readfirst.txt, '
         'data/b673_stepzero.txt, data/b673_tests_stepzero.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b672`s weight FINDINGS :%s' % c1[0],
         '### COMPONENT 2 : the plan (data/b673_v4v5_plan.txt) and the control (data/b673_v4_control.txt) ; the one prompt answered ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the attempt on chi-li-b669, four runs (data/b673_runner_rows.json), the landing %d DERIVES (data/b673_landing.txt), the '
         'walk (data/b673_zeta_walk.txt), H5 (data/b673_h5.txt) ; H %s ; N3 %s ; N4 %s' % (
             len(lj.get('rows') or []), ' '.join('%s %s' % (k, (H.get(k) or ['?'])[0]) for k in sorted(H)), S['N3'][0], S['N4'][0]),
         '### COMPONENT 4 : the merge e36ea31, v0.32 (data/b673_merge_push_out.txt) ; OPEN_TRAILS :%s, :%s' % (c4[0], c4[1]),
         '### COMPONENT 5 : the dry-run step (data/b673_reg_gate.txt), the seal (data/b673_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b673_components.txt', L)
    print(NL.join(L[2:]))


def _land_one(path, head, e, bank, extra):
    if odd_lines(e):
        sys.exit('### ODD BACKTICKS -- NOTHING WRITTEN: %s' % odd_lines(e)[:3])
    guard_absent(path, head)
    r = append_to(path, e)
    ln = read_head(path, head)
    put_json(bank, dict(extra, line=ln, head=head, append=r))
    return ln


def findings(*a):
    t, e = _finding_text()
    e = conv(e)
    dry = 'dry' in a
    cells, fired = screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells)
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b673_findings.json', dict(title=t))
    j = jl('b673_findings.json')
    j['entry_line'] = ln
    put_json('b673_findings.json', j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = conv(_trail_text())
    dry = 'dry' in a
    cells, fired = screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells)
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b673_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written -- converted by conv and run through the screens their landing runs, the needles the face names read in
    each; prints DRY-RUN STEP : CLEAN and exits 0 only when both screens are quiet and every needle is found. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = conv(text)
        print('  %s (the screens):' % which)
        cells, fired = screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = _face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells and not fired and nd and not miss
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


# ================================================================================ THE MIRROR, AT THE CLOSE (the b655 form; b672's routes, carried)
import hashlib as _hl   # noqa: E402

MIRROR_TAG = '2026-10-16-b673'
ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % MIRROR_TAG
STAGE = os.path.join(os.environ.get('TEMP', SP), 'mirror-build-%s' % MIRROR_TAG)


def mbuild(*a):
    if os.path.exists(ZIP) or os.path.exists(STAGE):
        sys.exit('### THE ZIP OR ITS STAGE EXISTS -- NOT STARTED')
    loc, rem = g(PP, 'rev-parse', 'HEAD').strip(), (g(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    if loc != rem:
        sys.exit('### PLACE-papers HEAD %s IS NOT THE REMOTE MAIN %s -- NOT STARTED' % (loc[:12], rem[:12]))
    t0 = time.time()
    r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(ROOT, 'tools', 'mirror_build.ps1'), '-DateTag',
                        MIRROR_TAG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_json('b673_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b673':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b673`s -- NOTHING WRITTEN' % last[0])
    line = 'Act root: %s %s' % (last[0], last[1])
    man_p = os.path.join(STAGE, 'MANIFEST.md')
    raw = open(man_p, 'rb').read()
    if b'Act root: ' in raw:
        sys.exit('### THE ROOT LINE IS IN THE STAGED MANIFEST ALREADY -- REFUSING TO WRITE IT TWICE')
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    sep = '\r\n' if '\r\n' in text else '\n'
    out = text.rstrip('\r\n') + sep + sep + line + sep
    before = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('b673_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b673_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
    print(r.stdout[-600:])


def mbank(*a):
    import zipfile
    import b616_record as R6
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    commits = sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', NL.join(l for l in ls if '|' in l))))
    zb = open(ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b673_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b673 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE MOVES: none this act; the roster`s files as before',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b673_mirror.txt', L)
    put_json('b673_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


ROUTES = {'c1': c1, 'answers': answers, 'plan': plan, 'walk': walk, 'runner': runner, 'landing': landing, 'h5': h5, 'c4': c4,
          'merged': merged, 'hypotheses': hypotheses, 'commands': commands, 'kernels': kernels, 'defects': defects, 'root': root,
          'root_arm': root_arm, 'table_final': table_final, 'gatebanks': gatebanks, 'scores': scores, 'desk': desk, 'components': components,
          'findings': findings, 'trail': trail, 'drycheck': drycheck, 'mbuild': mbuild, 'mroot': mroot, 'mverify': mverify, 'mbank': mbank}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b673_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
