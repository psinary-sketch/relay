# -*- coding: utf-8 -*-
"""b557_record.py -- THE CASCADE, ACT ELEVEN, BATCH TWO: THE EIGHT METHOD KEYSTONES TIERED AND CP-1 CLOSED; THE no_type_d
TIER SETTLED; THE STALE OLEAN REBUILT; THE ANCHOR LIST'S SCOPE RESTATED: THE RECORD, UNDER (R167).
### `python tools/b557_record.py reads | supersede | cost | prints | replace | anchor | census | rows | tiers | w6 | blocks |
### stems | roster | findings | components | desk | trail`
### The probes` and the build`s launches, the worktree, the junction, the copies, the commits, pushes and branch commands are the
### seat`s. This file deletes nothing and copies nothing: `replace` prints the plan the seat executes.
"""
import glob, hashlib, io, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b551_record as P  # noqa: E402
DD = 'D:' + os.sep
PP, LV, TRIAL = P.PP, P.LV, P.TRIAL
KER = os.path.join(DD, 'SIDE-kernel')
EFF = os.path.join(DD, 'SIDE-effects')
WT = os.path.join(DD, 'wt-b557-lv')
FIND, OT = P.FIND, P.OT
MAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
GRHR = 'phase1.5/spectral/GRH_CASCADE.md'
CENR = 'phase2/method/THE_KEYSTONE_CENSUS.md'
NL = chr(10)
rd, g, cite, append_to, guard_absent, line_of, poss, outside_bt = P.rd, P.g, P.cite, P.append_to, P.guard_absent, P.line_of, P.poss, P.outside_bt
PRIOR_RELAY = 'f1c2e65f'   # ### b556`s closing -- relay`s tip before this act (no housekeeping commit at b556)
PRIOR_PP = 'f54a255'       # ### b556`s PLACE-papers commit
DOCS = {'FOUND': 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'TECHNE': 'phase1.5/method/TECHNE_TOOLKIT.md',
        'SILENCE': 'phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md', 'LICENSE': 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md',
        'INVAR': 'phase1.5/method/INVARIANCE_BARRIERS.md', 'REPARAM': 'phase2/method/REPARAMETERIZATION_BARRIERS_v0_1.md',
        'EDIFF': 'phase2/method/E_DIFFICULTY_THEOREM.md', 'ENUMERA': 'phase1.5/method/ENUMERA.md'}
TITLE = {k: os.path.basename(v)[:-3] for k, v in DOCS.items()}
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def dp(k):
    return os.path.join(PP, *DOCS[k].split('/'))


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    open(os.path.join(D, n), 'wb').write((json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def put_txt(n, lines):
    open(os.path.join(D, n), 'wb').write((NL.join(lines) + NL).encode('utf-8'))


def lines_with(path, pat, text=None):
    return [i + 1 for i, l in enumerate((text if text is not None else rd(path)).split(NL)) if re.search(pat, l)]


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout.decode('utf-8-sig', 'replace').replace(chr(13), '')


def newest(path):
    best = 0.0
    for dp_, _, fs in os.walk(path):
        for f in fs:
            try:
                best = max(best, os.path.getmtime(os.path.join(dp_, f)))
            except OSError:
                pass
    return best


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


# ------------------------------------------------------------------------------ READING (3): THE REBUILD`S COST
def banked_seconds():
    out = {}
    for f in sorted(glob.glob(os.path.join(D, 'b5[5-9][0-9]_probes.jsonl'))):
        for l in rd(f).split(NL):
            if l.strip():
                r = json.loads(l)
                if r.get('repo') == 'SIDE-lv-conservation' and r.get('exit') == 0 and not r.get('inlined'):
                    out.setdefault(r['path'], []).append((os.path.basename(f)[:4], r['pin'], r['seconds']))
    return out


def cost():
    mods = sorted(f for f in g(LV, 'ls-tree', '-r', '--name-only', '2f71068').split(NL) if f.startswith('SIDELvConservation/') and f.endswith('.lean'))
    bs = banked_seconds()
    L = ['b557 -- READING (3): THE REBUILD`S COST, PRINTED BEFORE THE BUILD -- SIDE-lv-conservation v0.11.0 = 2f71068', '',
         '### the library`s modules: %d (lakefile globs `.submodules SIDELvConservation`)' % len(mods)]
    tot, none = 0.0, []
    for m in mods:
        v = bs.get(m, [])
        if v:
            tot += max(x[2] for x in v)
        else:
            none.append(m)
        L.append('    %-52s %s' % (m, ' ; '.join('%s@%s %.0f s' % x for x in v) or 'NO BANKED TIME'))
    L += ['', '### the banked times summed (the largest per module): %.0f s over %d modules ; modules with no banked time: %d' % (tot, len(mods) - len(none), len(none)),
          '### a probe`s time includes loading its imports` oleans, so the sum is an upper bound for the banked modules; the rest are unpriced',
          '### ### **OVER 600 S: THE BUILD RUNS IN THE BACKGROUND, WATCHED FROM THE FOREGROUND.**']
    pk = os.path.join(LV, '.lake', 'packages')
    out = dict(modules=mods, banked=bs, sum=tot, unpriced=none, packages_newest_before=newest(os.path.join(pk, 'mathlib', '.lake', 'build')))
    L.append('### the shared packages` Mathlib build, newest file time before: %.0f' % out['packages_newest_before'])
    put_json('b557_cost.json', out)
    put_txt('b557_cost.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (1): THE READS
KERNELS_CITED = {
    'FOUND': 'SIDE-kernel v1.2 (b1407b2; audit ce5d7bd), v1.4 (f374174); SIDE-silence-principle v0.1.0; SIDE-compression v0.2.0 (e9a5a36)',
    'TECHNE': 'SIDE-kernel (no pin for Xi.7; v1.4 for Xi.17; 0e5233f for V3B); SIDE-lv-conservation v0.9.0 (e3d08b6); SIDE-substrate-cluster 2e76426 (a module); a private repository`s module (not tiered)',
    'SILENCE': 'SIDE-structural-error-correction v0.2.1 (6a4f482); SIDE-cosmo c5cba30',
    'LICENSE': 'SIDE-effects `ExhaustivenessLicense` (no commit named; merged from w-ladder-skeleton, tip a0dc376 on main)',
    'INVAR': 'SIDE-kernel v1.7 (2957e7d)',
    'REPARAM': 'SIDE-kernel 5e668b4 (drafted against v1.7)',
    'EDIFF': 'SIDE-kernel v1.1 (e0a8ba0), with the v1.4 update note',
    'ENUMERA': 'none named'}


def reads():
    L = ['b557 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    for k, v in DOCS.items():
        t = rd(dp(k))
        L += ['### %s at `%s`: %d lines, read whole ; kernels cited: %s' % (TITLE[k], v, len(t.split(NL)), KERNELS_CITED[k])]
        ls = lines_with(None, r'^#+ .*Correspondence|^## VII\. Kernel correspondence', t)
        if ls:
            cite(L, dp(k), ls[0], min(ls[0] + 28, len(t.split(NL))), '%s -- its correspondence section' % TITLE[k])
    cite(L, os.path.join(D, 'b556_defects.txt'), 1, 60, 'relay data/b556_defects.txt -- defect (b) and the rest')
    for pid in ('m4', 'm4c'):
        L += ['### relay data/b556_probe_%s.txt, tail:' % pid] + ['  ' + l for l in rd(os.path.join(D, 'b556_probe_%s.txt' % pid)).rstrip(NL).split(NL)[-6:]]
    cite(L, FIND, 4805, 4811, 'FINDINGS.md:4805 -- the tier law (b539)')
    cite(L, FIND, 4819, 4823, 'FINDINGS.md:4819 -- the tier law corrected (b540)')
    cite(L, FIND, 5812, 5812, 'FINDINGS.md:5812 -- the programme-premise clause (b555)')
    cite(L, MAP, 134, 146, 'THE_LOAD_BEARING_MAP.md -- the RH-anchor list and T1 split')
    grh = os.path.join(PP, *GRHR.split('/'))
    cite(L, grh, 450, 450, 'GRH_CASCADE.md:450 -- b555`s line grading the SIDE-effects pair T0')
    cite(L, grh, 455, 455, 'GRH_CASCADE.md:455 -- b555`s second such line')
    cite(L, CENSUS, 40, 57, 'THE_KEYSTONE_CENSUS.md -- §1`s pin table')
    cite(L, CENSUS, 119, 119, 'THE_KEYSTONE_CENSUS.md -- R_CURVE_CRITERION`s pin sentence')
    cite(L, CENSUS, 243, 283, 'THE_KEYSTONE_CENSUS.md -- the v0.2 section')
    mp = rd(MAP)
    ab = {'FOUND': 'FOUND', 'LICENSE': 'LIC', 'INVAR': 'INVARIANCE|SIEVE', 'EDIFF': 'E_DIFF|E-Difficulty', 'TECHNE': 'TECHNE', 'SILENCE': 'SILENCE_STAGES',
          'REPARAM': 'REPARAM', 'ENUMERA': 'ENUMERA'}
    L += ['### THE_LOAD_BEARING_MAP lines naming each document: %s' % {k: lines_with(None, r'\b(%s)\b' % v, mp) for k, v in ab.items()}]
    put_txt('b557_reads.txt', L)
    print('  reads banked : %d lines' % len(L))


# ------------------------------------------------------------------------------ READING (2): THE no_type_d SETTLEMENT
SUPL = ('SUPERSEDES GRH_CASCADE :450 and :455 for `no_type_d_conspiracies` and `crt_exhaustiveness`: T2 -- appended 2026-09-28 by b557 under '
        'the author`s ruling `(R167)`(1): both quantify over the programme`s own structures (`StructuralCoupling` and its modular lift), so '
        'they are programme-type and T2 whatever their profile; b555`s T0 at :450 and :455 is kept as written; the row`s own grade stands.')


def supersede():
    import terminal_table as TT
    grh = os.path.join(PP, *GRHR.split('/'))
    guard_absent(grh, SUPL[:60])
    assert not TT.GRADE_RE.search(SUPL), 'a grade word'
    assert not TT.SUPERSEDE_RE.search(SUPL) and not TT.TRAIL_SUP_RE.search(SUPL), 'a table form'
    t = rd(grh).split(NL)
    assert 'no_type_d_conspiracies' in t[449] and '| T0 |' in t[449] and 'no_type_d_conspiracies' in t[454] and '| T0 |' in t[454]
    o = append_to(grh, NL.join(['', SUPL, '']))
    o['line'] = line_of(grh, SUPL[:60])
    put_json('b557_supersede.json', o)
    print(rd(grh).split(NL)[o['line'] - 1]); print(o)


def table_lines():
    t = rd(os.path.join(D, 'terminal_table.md'))
    return [l for l in t.split(NL) if 'no_type_d_conspiracies' in l or 'crt_exhaustiveness' in l]


# ------------------------------------------------------------------------------ READING (4): THE ANCHOR SCOPE LINE
ANH = '*Appended at b557 (2026-09-28) to the tier law (`FINDINGS.md`:4805, :4819, :5812), under `(R167)`(3) -- THE SCOPE OF THE RH-ANCHOR LIST:*'


def anchor():
    guard_absent(FIND, ANH)
    s = (ANH + ' the RH-anchor list (THE_LOAD_BEARING_MAP.md:134) is the T0 subset bearing on zero location: on it, the conclusion names a '
         'zero of ζ or Mathlib`s `RiemannHypothesis`, and the statement has no premise. A terminal concluding `RiemannHypothesis` under a '
         'premise -- `ConservationBridge.riemann_hypothesis` on `ConservationHypothesis`, `R4_positivity_to_RH` on its positivity premise -- '
         'is T1-open or T2 by its premise`s kind and is not on the list, as b556 found. b556`s (N5) wording was the navigator`s.')
    o = append_to(FIND, NL.join(['', s, '']))
    o['line'] = line_of(FIND, ANH)
    put_json('b557_anchor.json', o)
    print(poss(s)); print(o)


# ------------------------------------------------------------------------------ READING (5): THE CENSUS LINE
CEL = '*Appended 2026-09-28 by b557, under the author`s ruling `(R167)`(4), to the v0.2 section (:243) and §2`s table (:119):*'
V01 = '0d4a6fe'


def census():
    guard_absent(CENSUS, CEL)
    rc = blob(PP, V01 + ':phase1.5/rcurve/R_CURVE_CRITERION.md')
    rc_now = blob(PP, PRIOR_PP + ':phase1.5/rcurve/R_CURVE_CRITERION.md')
    pins = sorted(set(re.findall(r'`([0-9a-f]{7,12})`', rc)))
    bd = [i + 1 for i, l in enumerate(rc.split(NL)) if 'bd2ae1a' in l]
    ln119 = rd(CENSUS).split(NL)[118]
    assert 'bd2ae1a' in ln119 and 'R_CURVE_CRITERION' in ln119
    res = dict(v01=V01, pins=pins, pin_count=len(pins), bd2_lines=bd, bd2_now=[i + 1 for i, l in enumerate(rc_now.split(NL)) if 'bd2ae1a' in l],
               lines=len(rc.split(NL)))
    s = (CEL + ' the sentence at :119 says R_CURVE_CRITERION has "five cited pins, one of which (`bd2ae1a`)" is absent from '
         'SIDE-lv-conservation. Read at the census v0.1 commit `%s`, R_CURVE_CRITERION.md cites %d commit-shaped pins in backticks (%s) and '
         '`bd2ae1a` on %s of its lines; at b556`s commit it cites `bd2ae1a` on %s. The pin the sentence attributes to that document is not in '
         'it; `bd2ae1a` is the PLACE-papers sitting commit of E-2026-09-27-1, cited by PATHS_TO_THE_CRITICAL_LINE. The navigator carried the '
         'sentence into b556`s ferry. No other action.' % (V01, len(pins), ', '.join('`%s`' % p for p in pins), len(bd) or 'none', len(res['bd2_now']) or 'none'))
    o = append_to(CENSUS, NL.join(['', s, '']))
    o['line'] = line_of(CENSUS, CEL)
    res['append'] = o
    put_json('b557_census.json', res)
    print(poss(s)); print(o)


# ------------------------------------------------------------------------------ READING (3): THE PRINTS AND THE REPLACEMENT
PR_RE = re.compile(r"'([A-Za-z_][A-Za-z0-9_.₀']*)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)")


def parse_prints(text):
    return {m.group(1): ' '.join(m.group(2).split()) for m in PR_RE.finditer(text)}


def bank_profiles():
    """### every profile the relay probe banks carry for SIDE-lv-conservation names, with its source; and the transcript`s."""
    bank = {}
    for f in sorted(glob.glob(os.path.join(D, 'b5[5-9][0-9]_probes.jsonl'))):
        for l in rd(f).split(NL):
            if l.strip():
                r = json.loads(l)
                if r.get('repo') == 'SIDE-lv-conservation' and r.get('exit') == 0:
                    for n, p in (r.get('profiles') or {}).items():
                        if p:
                            bank.setdefault(n, set()).add((' '.join(p.split()), '%s %s@%s' % (os.path.basename(f)[:4], r['id'], r['pin'])))
    return bank


def prints():
    scr = os.environ['B557_SCR']
    log = rd(os.path.join(scr, 'b557_build.log'))
    root = rd(os.path.join(D, 'b557_prints_root.txt'))
    got = {}
    got.update(parse_prints(log))
    got.update(parse_prints(root))
    bank = bank_profiles()
    rows, agree, disagree, unbanked = [], 0, [], []
    for n, p in sorted(got.items()):
        cands = [k for k in bank if k == n or k.endswith('.' + n) or n.endswith('.' + k)]
        if not cands:
            unbanked.append(n)
            rows.append('    %-70s %-60s NO BANKED PROFILE' % (n, p))
            continue
        bp = sorted({x for k in cands for x in bank[k]})
        ok = all(x[0] == p for x in bp)
        agree += ok
        if not ok:
            disagree.append((n, p, bp))
        rows.append('    %-70s %-60s %s against %s' % (n, p, 'AGREES' if ok else 'DISAGREES', ['%s (%s)' % x for x in bp]))
    ex = re.findall(r'(?m)^exit (\d+)', log)
    errs = len(re.findall(r'(?m)error:', log))
    L = ['b557 -- READING (3): THE REBUILD`S PRINTS AT v0.11.0 = 2f71068, COMPARED WITH THE BANK', '',
         '### the build: exit %s ; error lines %d ; its start and end %s' % (ex[-1] if ex else 'NONE', errs, rd(os.path.join(D, 'b557_build_start.txt')).split()),
         '### prints parsed: %d (build log %d, root AxiomCheck files %d)' % (len(got), len(parse_prints(log)), len(parse_prints(root))),
         '### with a banked profile: %d -- AGREE %d, DISAGREE %d ; with none: %d' % (len(got) - len(unbanked), agree, len(disagree), len(unbanked)), ''] + rows
    out = dict(build_exit=int(ex[-1]) if ex else None, errors=errs, prints=got, agree=agree, disagree=disagree, unbanked=unbanked,
               verdict=bool(ex) and ex[-1] == '0' and errs == 0 and not disagree and agree > 0)
    L += ['', '### ### **VERDICT: %s**' % ('THE PRINTS AGREE WITH THE BANK -- THE REPLACEMENT MAY PROCEED' if out['verdict'] else 'NOT AGREED -- NOTHING IS REPLACED')]
    put_json('b557_prints.json', out)
    put_txt('b557_prints.txt', L)
    print(NL.join(L[:6] + L[-2:]))


def replace():
    pj = jl('b557_prints.json')
    src = os.path.join(WT, '.lake', 'build', 'lib', 'lean', 'SIDELvConservation')
    dst = os.path.join(LV, '.lake', 'build', 'lib', 'lean', 'SIDELvConservation')
    plan = []
    for f in sorted(os.listdir(src)):
        a, b = os.path.join(src, f), os.path.join(dst, f)
        if os.path.isfile(a) and (not os.path.exists(b) or sha(a) != sha(b)):
            plan.append(dict(file=f, rebuilt=sha(a), working=sha(b) if os.path.exists(b) else None))
    L = ['b557 -- READING (3): THE REPLACEMENT PLAN (the seat copies; this tool copies nothing)', '',
         '### the prints` verdict: %s' % pj.get('verdict'), '### artefacts differing between the rebuild and the working checkout: %d' % len(plan)]
    L += ['    %-42s rebuilt %s working %s' % (p['file'], p['rebuilt'][:16], (p['working'] or 'ABSENT')[:16]) for p in plan]
    put_json('b557_replace_plan.json', dict(verdict=pj.get('verdict'), plan=plan, src=src, dst=dst))
    put_txt('b557_replace_plan.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (6): THE ROWS
EL = 'SIDEEffects.ExhaustivenessLicense.'
DEA = 'DeAlignment.'
PPS = 'SIDELvConservation.PartialPositivity.partialPositivity_finiteRange'
ROWMAP = {
    'FOUND': {625: [('SilenceTheorem.silence_universal', 'k7', 'k7t')], 626: [('SIDESilencePrinciple.product_formula_silent', 's1', None)],
              627: [('SIDESilencePrinciple.distributive_law_silent', 's1', None)],
              628: [('SIDESilencePrinciple.silence_principle', 's1', None), ('SIDESilencePrinciple.Universal.silence_universal', 's1', None)],
              629: [('ECondition.type_I_has_ostrowski', 'k6', 'k6t')],
              630: [('sieve_ceiling', 'c1', 'c1t'), ('SieveCeilingSemantic.sieve_ceiling_semantic', 'c2', 'c2t')],
              631: [('proof_dichotomy', 'c1', 'c1t')], 632: [('bright_access_required', 'c1', 'c1t')],
              633: [('e_difficulty', 'c1', 'c1t'), ('e_difficulty_xi', 'c1', 'c1t')], 634: [('ProductFormula.conservation_of_spectra', 'k3', 'k3t')],
              635: [('ostrowski_exhaustive', 'k8', 'k8t')], 636: [('neg_eq_neg_one_sub_iff', 'k9', 'k9t')],
              637: [('Compression.compression', 'cp', None), ('Compression.compression_infinite_objects', 'cp', None)], 638: [], 639: []},
    'TECHNE': {507: [('SIDEKernel.formation', 'kc', None)], 508: [], 509: [('e_difficulty', 'c1', 'c1t')], 510: [],
               511: [('techne_kernel_voice3b.offLine_of_codim_two', 'vb', 'vbt')], 512: [], 513: [(PPS, 'lp', 'lpt')], 514: [],
               515: [('SIDELvConservation.h1_complete_at_Phi', 'lh', 'lht'), (PPS, 'lp', 'lpt')], 516: []},
    'SILENCE': {202: [(DEA + 'no_domain_covers_line', 'se', None)], 203: [(DEA + 'single_domain_fault_not_logical', 'se', None)],
                204: [(DEA + 'dealigned_of_lines_injective', 'se', None)], 205: [(DEA + 'fano_dealignment_decidable_example', 'se', None)],
                206: [(DEA + 'fano_collapsed_line_rejected', 'se', None)], 207: [(DEA + 'fano_two_design', 'se', None)],
                208: [('steane_parameters', 'co', None)], 209: [('knill_laflamme_t1', 'co', None)], 210: [], 211: []},
    'LICENSE': {105: [(EL + 'Grade', 'el', None)], 106: [(EL + 'Grade.le_refl', 'el', None), (EL + 'Grade.le_trans', 'el', None)],
                107: [(EL + 'theorem_is_top', 'el', None), (EL + 'none_is_bottom', 'el', None), (EL + 'ladder_strict', 'el', None)],
                108: [(EL + x, 'el', None) for x in ('RH_grade', 'Hodge_grade', 'T7_grade', 'classNumberDiagonal_grade')],
                109: [(EL + 'instances_ordered', 'el', None)], 110: [(EL + 'RH_typeI_of_top', 'el', None)]},
    'INVAR': {499: [('ConservationBridge.riemann_hypothesis', 'k1', None)], 500: [('SieveCeilingSemantic.sieve_ceiling_semantic', 'c2t', None)],
              501: [('proof_dichotomy', 'c1t', None)], 502: [('sieve_ceiling', 'c1t', None)], 503: [('bright_access_required', 'c1t', None)],
              504: [('e_difficulty', 'c1t', None)], 505: [('SieveCeilingWitness.dh_witness', 'dw', None)],
              506: [('InvarianceBarrier.invariance_barrier', 'ib', None)], 507: [('InvarianceBarrier.derivability_barrier', 'ib', None)],
              508: [], 509: [], 510: [], 511: [], 512: []},
    'REPARAM': {223: [('InvarianceBarrier.invariance_barrier', 'rp', 'rpt')], 224: [('InvarianceBarrier.derivability_barrier', 'rp', 'rpt')],
                225: [], 226: [], 227: [], 228: [], 229: [], 230: [], 231: []},
    'EDIFF': {162: [('sieve_ceiling', 'e11', 'e11t')], 163: [('proof_dichotomy', 'e11', 'e11t')], 164: [('e_difficulty', 'e11', 'e11t')],
              165: [('e_difficulty_xi', 'e11', 'e11t')]},
    'ENUMERA': {},
}
NOTERM = {('TECHNE', 508): 'a private repository`s objects (a module and a definition), not tiered here',
          ('TECHNE', 512): 'a module at SIDE-substrate-cluster 2e76426, not a terminal', ('TECHNE', 514): 'a module (`SteaneLabeling`) at SIDE-substrate-cluster 2e76426, not a terminal',
          ('TECHNE', 510): 'METHOD (manuscript-resident)', ('TECHNE', 516): 'METHOD (manuscript-resident)'}
HEADS = {'FOUND': '| Claim | Kernel | Theorem', 'TECHNE': '| Entry | Grade | Anchor', 'SILENCE': '| Claim | Kernel | Theorem', 'LICENSE': '| Claim | Kernel | Theorem',
         'INVAR': '| Claim (as stated here) |', 'REPARAM': '| Claim | Kernel | Theorem'}


def short(n):
    return n.split('.')[-1]


def rows():
    out = {}
    for k in DOCS:
        src = blob(PP, PRIOR_PP + ':' + DOCS[k]).split(NL)
        rs = []
        if k == 'EDIFF':
            for ln in sorted(ROWMAP[k]):
                l = src[ln - 1]
                n = ROWMAP[k][ln][0][0]
                assert l.startswith('- `%s`' % n), (k, ln)
                rs.append(dict(line=ln, claim=l[2:].replace('`', ''), kernel='SIDE-kernel v1.1 (`Kernel/Cascade/SieveCeiling.lean`; §VII)', terminal_cell=l,
                               profile_cell='', status=l, names=[n], probes=[(ROWMAP[k][ln][0][1], ROWMAP[k][ln][0][2])]))
        elif k in HEADS:
            hi = [i for i, l in enumerate(src) if l.startswith(HEADS[k])][0]
            for i in range(hi + 2, len(src)):
                l = src[i]
                if not l.startswith('|'):
                    break
                c = [x.strip() for x in l.strip().strip('|').split('|')]
                if len(c) == 3:
                    claim, kernel, tcell, pcell, status = c[0], c[2], c[2], c[2], c[1]
                else:
                    claim, kernel, tcell, pcell, status = c[0], c[1], c[2], c[3], c[4]
                names = ROWMAP[k].get(i + 1)
                assert names is not None, (k, i + 1, 'a row the map lacks')
                for n, _, _ in names:
                    assert short(n) in (tcell + pcell), (k, i + 1, n)
                rs.append(dict(line=i + 1, claim=claim, kernel=kernel, terminal_cell=tcell, profile_cell=pcell, status=status[:700],
                               names=[n for n, _, _ in names], probes=[(p, t) for _, p, t in names], note=NOTERM.get((k, i + 1))))
            assert sorted(r['line'] for r in rs) == sorted(ROWMAP[k]), (k, 'map and table disagree')
        out[k] = rs
        print('  %-8s rows %2d ; naming a terminal %2d ; readings %2d' % (k, len(rs), sum(1 for r in rs if r['names']), sum(len(r['names']) for r in rs)))
    put_json('b557_rows.json', out)


# ------------------------------------------------------------------------------ THE TIERS
STD3 = 'depends on axioms: [propext, Classical.choice, Quot.sound]'
PQ = 'depends on axioms: [propext, Quot.sound]'
PX = 'depends on axioms: [propext]'
NONE_AX = 'does not depend on any axioms'
NA = 'T0, not RH-anchor: '
ORDER = ['T0', 'T1-open', 'T1-lit', 'T2', 'T2-SHELL', 'T2-INTERFACES', 'T3', 'T4']
REPAIR = ('the repair note (2026-08-08): `e_difficulty` repaired at SIDE-kernel v1.4 (reads its system); `sieve_ceiling` and '
          '`bright_access_required` relabelled SCAFFOLDING; `sieve_ceiling_semantic` the contentful ceiling')
SCAF = 'T2-SHELL: abstract-Proof bookkeeping over the file`s own `Proof`; its docstring at v1.4 and v1.7 labels it SCAFFOLDING'
# ### name -> (tier, reason, subject for (N1) or None)
TERMS = {
    'SilenceTheorem.silence_universal': ('T2-INTERFACES', 'INTERFACES on `I.is_universal`, a programme structure`s property the manuscript asserts ((R165)(3); b555)', None),
    'SIDESilencePrinciple.product_formula_silent': ('T2', '`decide` over the in-kernel Boolean model (`isSilent I := I.kappa_x100 == 0` on hand-defined instances); the row grades it ENCODES-CONCLUSION', None),
    'SIDESilencePrinciple.distributive_law_silent': ('T2', 'as `product_formula_silent`', None),
    'SIDESilencePrinciple.silence_principle': ('T2', 'a Bool chain over the file`s `Interface` -- the decidable shadow (the file`s own later relabel)', None),
    'SIDESilencePrinciple.Universal.silence_universal': ('T2-INTERFACES', 'ABSENT at v0.1.0; at HEAD `667c254` (untagged) a type-generic universality premise over the file`s interfaces', None),
    'ECondition.type_I_has_ostrowski': ('T2', 'modus tollens over an abstract `Domain` whose `[Fintype Domain]` is never used -- logic alone (b539, b555)', None),
    'sieve_ceiling': ('T2-SHELL', SCAF, None),
    'bright_access_required': ('T2-SHELL', SCAF, None),
    'SieveCeilingSemantic.sieve_ceiling_semantic': ('T2', 'a general schema over an arbitrary carrier and indistinguishability relation -- the contentful ceiling, logic whose readings are carried by names', None),
    'proof_dichotomy': ('T2', 'excluded middle over the file`s `StepAccess` lists', None),
    'e_difficulty': ('T2', 'over the file`s `DeterminedSystem`, `SysProof` and `DomainOstrowski` -- programme-type; at v1.4 it reads its system (the repair)', None),
    'e_difficulty_xi': ('T2', 'the smoke test at the file`s own `xi_system`', None),
    'ProductFormula.conservation_of_spectra': ('T2', '`∀ s : ℤ, 1 ^ s = 1` -- the unit norm raised to any power; the Conservation-of-Spectra reading (the product formula is s-dark) is carried by the name, not the statement', None),
    'ostrowski_exhaustive': ('T0', NA + 'Mathlib`s Ostrowski theorem restated (b555)', 'ℚ`s places'),
    'neg_eq_neg_one_sub_iff': ('T0', NA + 'in a field of characteristic 0, −s = −(1 − s) ↔ s = 1/2 (b555)', 'an arbitrary field of characteristic 0'),
    'Compression.compression': ('T2', 'a schema over the file`s `Catalogue` -- content enters at instantiation (the row`s words)', None),
    'Compression.compression_infinite_objects': ('T2', 'as `compression`, at `Catalogue Nat N`', None),
    'ConservationBridge.riemann_hypothesis': ('T2', 'INTERFACES on `ConservationHypothesis`, RH restated (`ch_iff_rh`; E-2026-09-25-1): ENCODES-CONCLUSION', None),
    'SieveCeilingWitness.dh_witness': ('T2', 'over the file`s `Config` with the stipulated Davenport–Heilbronn datum (b556)', None),
    'InvarianceBarrier.invariance_barrier': ('T2', 'a general schema over an abstract carrier, agreement relation and property -- logic (b556)', None),
    'InvarianceBarrier.derivability_barrier': ('T2', 'the soundness corollary, same schema (b556)', None),
    'steane_parameters': ('T2', 'over the file`s check map `H` and the formation record -- programme objects', None),
    'knill_laflamme_t1': ('T2', 'over the file`s check map `H` -- programme objects', None),
    'SIDEKernel.formation': ('T2', '`2 + 3 + 2 + 0 = 7` by `decide` -- a numeral identity whose reading (the formation count) is carried by the name', None),
    'techne_kernel_voice3b.offLine_of_codim_two': ('T2', 'over the file`s codimension definitions -- the identifier-over-claim repair`s terminal', None),
    PPS: ('T1-lit', 'INTERFACES on Bombieri–Lagarias` decomposition and Voros` tail bound, literature theorems not compiled (b540, b554)', None),
    'SIDELvConservation.h1_complete_at_Phi': ('T0', NA + 'the eight coupling facts of lv`s theta-kernel `Phi`, built from Mathlib`s `evenKernel` (b539, b554)', 'ζ`s theta kernel Φ'),
    EL + 'RH_typeI_of_top': ('T2-INTERFACES', 'INTERFACES on the named premise `EDifficultyTop`, the programme`s own bridge, never proved in the module', None),
}
for x in ('Grade', 'Grade.le_refl', 'Grade.le_trans', 'theorem_is_top', 'none_is_bottom', 'ladder_strict', 'RH_grade', 'Hodge_grade', 'T7_grade',
          'classNumberDiagonal_grade', 'instances_ordered'):
    TERMS[EL + x] = ('T2', 'over the file`s four-constructor `Grade` and its rank function -- programme-type, computed by `rfl`/`decide`', None)
for x in ('no_domain_covers_line', 'single_domain_fault_not_logical', 'dealigned_of_lines_injective', 'fano_dealignment_decidable_example',
          'fano_collapsed_line_rejected', 'fano_two_design'):
    TERMS[DEA + x] = ('T2', 'over the file`s `Line` structure and a domain map, or its Fano line table by `decide` -- programme-type', None)
EARLIER = {'SilenceTheorem.silence_universal': ('T2-INTERFACES', 'b555'), 'ECondition.type_I_has_ostrowski': ('T2', 'b555'), 'ostrowski_exhaustive': ('T0', 'b555'),
           'neg_eq_neg_one_sub_iff': ('T0', 'b555'), 'ConservationBridge.riemann_hypothesis': ('T2', 'b539-b541, b556'), 'SieveCeilingWitness.dh_witness': ('T2', 'b556'),
           'InvarianceBarrier.derivability_barrier': ('T2', 'b556'), PPS: ('T1-lit', 'b540, b554, b556'), 'SIDELvConservation.h1_complete_at_Phi': ('T0', 'b554, b556')}


def probes():
    out = {}
    p = os.path.join(D, 'b557_probes.jsonl')
    for l in (rd(p).split(NL) if os.path.exists(p) else []):
        if l.strip():
            r = json.loads(l)
            out[r['id']] = r
    return out


def ptext(pid):
    p = os.path.join(D, 'b557_probe_%s.txt' % pid)
    return rd(p) if os.path.exists(p) else ''


def check_text(pid, name, pr):
    r = pr.get(pid, {})
    if r.get('identical_to'):
        return check_text(r['identical_to'], name, pr)
    t = ptext(pid)
    i = t.find('@' + name + ' :')
    if i < 0:
        i = t.find(name + ' :')
    if i < 0 or t[max(0, i - 1):i] not in ('', '\n', '@'):
        j = t.find('\n' + name + ' :')
        if j < 0:
            return None
        i = j + 1
    rest = t[i:]
    stop = [m.start() for m in re.finditer(r"(?m)^(@?[A-Za-z_][A-Za-z0-9_.₀]* : |'[A-Za-z_]|real |<stdin>|inductive |def |structure )", rest)][1:2]
    return ' '.join(rest[:stop[0] if stop else 1500].split())


def fresh_profile(pid, name, pr):
    r = pr.get(pid, {})
    if r.get('identical_to'):
        return fresh_profile(r['identical_to'], name, pr)
    return (r.get('profiles') or {}).get(name)


def found_at(pid, name, pr):
    r = pr.get(pid, {})
    if r.get('identical_to'):
        return found_at(r['identical_to'], name, pr)
    return r.get('exit') == 0 and bool(check_text(pid, name, pr))


def row_profile(cell, name, k, line):
    c = cell.replace('`', '')
    if (k, line) == ('FOUND', 628):
        return PX if short(name) == 'silence_principle' else NONE_AX
    if (k, line) == ('FOUND', 633) or (k, line) == ('INVAR', 504) or (k, line) == ('TECHNE', 509):
        return PQ if short(name) == 'e_difficulty' else None
    if '{propext, Classical.choice, Quot.sound}' in c or 'standard three' in c:
        return STD3
    if '{propext, Quot.sound}' in c:
        return PQ
    if '[propext]' in c:
        return PX
    if 'axiom-free' in c:
        return NONE_AX
    return None


def tiers():
    rs = jl('b557_rows.json')
    pr = probes()
    ei = jl('b544_ei.json').get('marks', {})
    need = sorted({x for k in rs for r in rs[k] for (p, t) in r['probes'] for x in (p, t) if x and x not in pr})
    if need:
        sys.exit('### PROBES NOT YET BANKED: %s' % need)
    out, L = {}, ['b557 -- READING (6): THE CORRESPONDENCE ROWS OF THE SECOND BATCH, RE-READ AT PIN', '', '### the probes (relay data/b557_probe_<id>.txt):']
    for pid, p in sorted(pr.items()):
        L.append('    %-5s %-34s %-8s %-48s %s' % (pid, p['repo'], p['pin'], p['path'], 'IDENTICAL to %s' % p['identical_to'] if p.get('identical_to') else
                                                     'mode %s exit %s %.1f s errors %s imports %s' % (p['mode'], p['exit'], p['seconds'], p['errors'], p['closure'] or 'NONE')))
    for k in DOCS:
        terms, rows_out = [], []
        for r in rs[k]:
            tl, ok, why = [], True, []
            for n, (pid, tid) in zip(r['names'], r['probes']):
                tier, reason, subj = TERMS[n]
                fnd = found_at(pid, n, pr)
                prof = fresh_profile(pid, n, pr)
                want = row_profile(r['profile_cell'], n, k, r['line'])
                st = check_text(pid, n, pr)
                tag = None
                if tid:
                    tst = check_text(tid, n, pr)
                    tag = dict(probe=tid, pin=pr[tid]['pin'], identical=bool(pr[tid].get('identical_to')), found=found_at(tid, n, pr),
                               same_statement=(tst == st) if (tst and st) else False, statement=tst if tst != st else None, profile=fresh_profile(tid, n, pr))
                moved = [x for x, b in (('not found at its pin', not fnd),
                                        ('fresh profile %s against the row`s %s' % (prof, want), fnd and want is not None and prof != want),
                                        ('statement differs at the tag %s' % (tag or {}).get('pin'), bool(tag) and fnd and not tag['same_statement'])) if b]
                note = REPAIR if short(n) in ('e_difficulty', 'sieve_ceiling', 'sieve_ceiling_semantic', 'bright_access_required') else None
                terms.append(dict(row=r['line'], name=n, probe=pid, pin=pr[pid]['pin'], found=fnd, statement=st, profile=prof, row_profile=want, tier=tier,
                                  reason=reason, subject=subj, tag=tag, earlier=EARLIER.get(n), moved=moved, repair=note,
                                  ei=ei.get('%s|%s' % (pr[pid]['repo'], n), 'not indexed')))
                tl.append(tier)
                ok = ok and not moved
                if moved:
                    why.append('%s: %s' % (short(n), '; '.join(moved)))
            ruling = 'ConservationBridge.riemann_hypothesis' in r['names'] and 'the reduction' in (r['claim'] + r['status'])
            if ruling:
                why.append('(R167)(5): the row calls the terminal "the reduction"; its premise is RH restated (E-2026-09-25-1); the programme`s compiled reduction of RH is `h2_sign_iff_rh`')
            ediff = k == 'EDIFF' and 'sieve_ceiling' in r['names'] and not re.search(r'SCAFFOLD|SHELL|work-order', r['claim'])
            if ediff:
                why.append('READING (7): the bullet names `sieve_ceiling` as the ceiling without SCAFFOLDING, SHELL or work-order on the bullet')
            rt = max(tl, key=ORDER.index) if tl else 'T4'
            rows_out.append(dict(line=r['line'], claim=r['claim'], names=r['names'], tiers=tl, tier=rt, disp='CARRIED' if (ok and not ruling and not ediff) else 'MOVED',
                                 why=why, kernel=r['kernel'], note=r.get('note')))
        tc = {x: sum(1 for t in terms if t['tier'] == x) for x in ORDER}
        rc = {x: sum(1 for r in rows_out if r['tier'] == x) for x in ORDER}
        dc = {x: sum(1 for r in rows_out if r['disp'] == x) for x in ('CARRIED', 'MOVED')}
        out[k] = dict(rows=rows_out, terms=terms, term_tiers=tc, row_tiers=rc, disp=dc)
        L += ['', '=' * 100, '### %s (%s at PLACE-papers %s): %d rows; %d terminal readings' % (TITLE[k], DOCS[k], PRIOR_PP, len(rows_out), len(terms)), '=' * 100]
        for t in terms:
            L += ['', '### :%d %s [%s at %s via %s]' % (t['row'], t['name'], 'FOUND' if t['found'] else 'NOT FOUND', t['pin'], t['probe']),
                  '    statement : %s' % (t['statement'] or 'NONE')[:900], '    profile   : %s   (the row prints: %s)' % (t['profile'], t['row_profile']),
                  '    at the tag: %s' % (t['tag'] or 'no tag beyond the pin'), '    tier      : %s -- %s' % (t['tier'], t['reason']),
                  '    earlier   : %s ; E/I (b544): %s%s' % (t['earlier'] or 'none banked', t['ei'], ' ; ' + t['repair'] if t['repair'] else ''),
                  '    disposition: %s' % ('CARRIED' if not t['moved'] else 'MOVED -- ' + '; '.join(t['moved']))]
        L += ['', '### ROWS:'] + ['    :%d %-8s %-14s %s%s' % (r['line'], r['disp'], r['tier'], r['claim'][:64], ('  -- ' + ' | '.join(r['why'])) if r['why'] else
                                                                 ('  -- ' + r['note'] if r['note'] else '')) for r in rows_out]
        L += ['### TIERS OVER THE %d READINGS: %s' % (len(terms), ' · '.join('%s %d' % (x, tc[x]) for x in ORDER)),
              '### ROW TIERS: %s' % ' · '.join('%s %d' % (x, rc[x]) for x in ORDER), '### DISPOSITIONS: CARRIED %d · MOVED %d' % (dc['CARRIED'], dc['MOVED'])]
    t0 = sorted({(t['name'], t['subject']) for k in DOCS for t in out[k]['terms'] if t['tier'] == 'T0'})
    out['t0'] = t0
    L += ['', '### T0 TERMINALS ACROSS THE BATCH (distinct): %d -- %s' % (len(t0), t0)]
    put_json('b557_tiers.json', out)
    put_txt('b557_tiers.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (8): THE W-6 GATE, FROM THE KERNEL
W6FILES = ['Kernel/Cascade/SieveCeiling.lean', 'Kernel/Cascade/SieveCeilingSemantic.lean', 'Kernel/Cascade/SieveCeilingWitness.lean']


def classify_decls(src):
    out = []
    lines = src.split(NL)
    for i, l in enumerate(lines):
        m = re.match(r'^(theorem|lemma|def|abbrev|structure|inductive)\s+(\S+)', l)
        if not m:
            continue
        j = i + 1
        while j < len(lines) and not re.match(r'^(theorem|lemma|def|abbrev|structure|inductive|/--|end |namespace )', lines[j]):
            j += 1
        body = NL.join(lines[i:j])
        doc = NL.join(lines[max(0, i - 8):i])
        kind = ('sorry' if re.search(r'\bsorry\b', body) else 'fun _ => True' if 'fun _ => True' in body else
                'True body' if re.search(r':=\s*True\b|:\s*Prop\s*:=\s*True', body) else
                'SCAFFOLDING (docstring)' if 'SCAFFOLDING' in doc and '/--' in doc else 'contentful')
        out.append(dict(line=i + 1, kind=m.group(1), name=m.group(2), grade=kind))
    return out


def w6():
    res, L = {}, ['b557 -- READING (8): THE GATE NAMED W-6, READ FROM THE KERNEL (SIDE-kernel)', '']
    for t in ('v1.2', 'v1.4', 'v1.7'):
        for f in W6FILES:
            src = blob(KER, '%s:%s' % (t, f))
            if not src.strip():
                L.append('### %s %s: ABSENT' % (t, f))
                continue
            ds = classify_decls(src)
            res['%s:%s' % (t, f)] = ds
            L.append('### %s %s: %d declarations -- %s' % (t, f, len(ds), {k: sum(1 for d in ds if d['grade'] == k) for k in sorted({d['grade'] for d in ds})}))
            L += ['    :%-4d %-10s %-34s %s' % (d['line'], d['kind'], d['name'], d['grade']) for d in ds if d['grade'] != 'contentful' or d['kind'] == 'theorem']
    eff = g(EFF, 'ls-tree', '-r', '--name-only', 'a27415d')
    effhit = [x for x in eff.split(NL) if 'SieveCeiling' in x]
    L += ['', '### the ferry`s pin for this read, SIDE-effects `a27415d`: files named like SieveCeiling -- %s' % (effhit or 'NONE; the file lives in SIDE-kernel `Kernel/Cascade/`')]
    put_json('b557_w6.json', dict(files=res, effects_a27415d=effhit))
    put_txt('b557_w6.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (9): THE BLOCKS
BH = ('#### THE CASCADE, ACT ELEVEN -- THE CORRESPONDENCE TIERED *(appended 2026-09-29, b557, under the author`s ruling `(R167)`(5); no byte '
      'above this block changes; the body is not edited)*')


def cleanclaim(c):
    import banned_terms as BTM
    c = re.sub(r'\$[^$]*\$', '…', c).replace('|', '/').replace('**', '').replace('###', '').replace('`', '')
    c = re.sub(r'\s*\S*' + BTM.PAT.pattern + r'\S*', '', c, flags=re.I)
    return ' '.join(c.split())


def table(s):
    L = ['| row | claim (abridged) | terminal(s) | fresh profile(s) | disposition | tier(s) |', '|:--|:--|:--|:--|:--|:--|']
    for r in s['rows']:
        ts = [t for t in s['terms'] if t['row'] == r['line']]
        prof = sorted(set((t['profile'] or 'NOT FOUND').replace('depends on axioms: ', '').replace('does not depend on any axioms', 'axiom-free') for t in ts))
        L.append('| :%d | %s | %s | %s | **%s** | %s |' % (r['line'], cleanclaim(r['claim'])[:90], ', '.join('`%s`' % short(t['name']) for t in ts) or 'NONE',
                                                          '; '.join(prof) or '—', r['disp'], ', '.join(sorted(set(r['tiers']), key=ORDER.index)) or 'T4'))
    L += ['', '*Tiers over the %d terminal readings: %s. Rows by their weakest link: %s. Dispositions: CARRIED %d · MOVED %d.*' % (
        len(s['terms']), ' · '.join('%s %d' % (k, s['term_tiers'][k]) for k in ORDER), ' · '.join('%s %d' % (k, s['row_tiers'][k]) for k in ORDER),
        s['disp']['CARRIED'], s['disp']['MOVED'])]
    return L


def moved_lines(s):
    return ['*Row :%d MOVED:* %s' % (r['line'], '; '.join(r['why'])) for r in s['rows'] if r['disp'] == 'MOVED']


def tag_counts(t):
    return {x: len(re.findall(r'\[' + re.escape(x) + r'[\]\s—-]', t)) for x in ('PROVED', 'FORCED', 'ESTABLISHED', 'VALIDATED', 'SUPPORTED', 'TESTABLE', 'INTERPRETIVE', 'POETIC')}


def blocks():
    ts, w = jl('b557_tiers.json'), jl('b557_w6.json')
    pr = probes()
    out = {}
    for k in DOCS:
        if poss(BH).encode('utf-8') in open(dp(k), 'rb').read():
            out[k] = dict(present_before=True, line=line_of(dp(k), BH))
            continue
        L = ['', '<!-- b557 THE CASCADE, ACT ELEVEN, 2026-09-29 -->', '', BH, '']
        if k == 'ENUMERA':
            t = blob(PP, PRIOR_PP + ':' + DOCS[k])
            L += ['**No Correspondence table naming terminals.** This document names no kernel terminal and no pin (searched for `SIDE-` repository '
                  'names, qualified terminal names and `#print axioms`: none). Its "§IV. The Correspondences" are conceptual pairings, not kernel '
                  'rows. Every claim it makes is therefore, in the tier law`s terms, a claim with no terminal: T4. Its own epistemic tags, counted '
                  'as it prints them: %s. The RH closure is carried under `h2` by its own 2026-07-19 note; nothing here moves it.' % tag_counts(t), '']
        else:
            s = ts[k]
            L += ['**The rows, re-read at pin.** %d rows, %d naming a terminal. Each terminal`s file at the row`s pin was elaborated fresh with '
                  '`#check` and `#print axioms` appended, narrow imports (the file`s own header) (relay `data/b557_probe_<id>.txt`; statements, '
                  'profiles, tiers and reasons in `data/b557_tiers.txt`); at the current tag where one exists beyond the pin, the file compared '
                  'and, if different, elaborated there. The tier is the weakest link; T2-SHELL marks scaffolding or a shell; a row with no '
                  'terminal is T4.' % (len(s['rows']), sum(1 for r in s['rows'] if r['names'])), ''] + table(s) + ['']
            L += moved_lines(s)
            notes = ['*Row :%d:* %s.' % (r['line'], r['note']) for r in s['rows'] if r.get('note')]
            L += notes
            rep = sorted({t['row'] for t in s['terms'] if t['repair']})
            if rep:
                L += ['', '**The repair note, carried on rows %s:** %s.' % (', '.join(':%d' % x for x in rep), REPAIR)]
            if k == 'FOUND':
                sh = pr.get('s1h', {})
                L += ['', '**`SIDESilencePrinciple.Universal.silence_universal`** is absent at the row`s pin v0.1.0; it is declared at HEAD `667c254` '
                      '(untagged; profile there `%s`), so the row`s pin predates the terminal it names.' % ((sh.get('profiles') or {}).get('SIDESilencePrinciple.Universal.silence_universal')),
                      '', '**The W-6 gate, read from the kernel (§VI):** in SIDE-kernel `Kernel/Cascade/SieveCeiling.lean` at v1.4 and v1.7 no declaration '
                      'is `sorry`, `True` or `fun _ => True`; the base `sieve_ceiling` and `bright_access_required` carry SCAFFOLDING docstrings; '
                      'the contentful ceiling is `SieveCeilingSemantic.sieve_ceiling_semantic`. The ferry`s pin for this read, SIDE-effects `a27415d`, '
                      'carries no SieveCeiling file (relay `data/b557_w6.txt`).']
            if k == 'EDIFF':
                L += ['', '**§VII`s bullets, read with the section`s own update paragraph (:175, W-6 DISCHARGED at v1.4):** the bullets cite the v1.1 '
                      'skeleton; the paragraph names `sieve_ceiling_semantic` as the contentful ceiling, but no bullet carries SCAFFOLDING, SHELL or '
                      'work-order.']
            if k == 'TECHNE':
                L += ['', '*The anchor `formation_count` in row :507 names a declaration made twice at the root of two SIDE-kernel files; it is read '
                      'through `SIDEKernel.formation`, the declaration both restate.*']
        L += ['', '*Appended by b557. No claim of the document is altered; `h2` stays where the deposit left it.*', '']
        out[k] = append_to(dp(k), NL.join(L))
        out[k]['line'] = line_of(dp(k), BH)
    put_json('b557_blocks.json', out)
    for k in DOCS:
        print(k, out[k])


# ------------------------------------------------------------------------------ READING (10): THE STEMS
def stems():
    import banned_terms as BTM
    res, L = {}, ['b557 -- READING (10): THE BANNED-STEM COUNT OVER THE SECOND-BATCH DOCUMENTS (before this act`s appends); no edit', '']
    for k in DOCS:
        src = blob(PP, PRIOR_PP + ':' + DOCS[k]).split(NL)
        hits = []
        for i, l in enumerate(src, 1):
            for m in BTM.PAT.finditer(l):
                hits.append(dict(line=i, stem=[x for x in BTM.STEMS if m.group(0).lower().startswith(x)][0], word=m.group(0),
                                 cls=BTM.classify(l, m.start(), dp(k)) or 'LIVE USE', text=l[max(0, m.start() - 60):m.end() + 60]))
        per = {x: sum(1 for h in hits if h['stem'] == x) for x in BTM.STEMS}
        live = {x: sum(1 for h in hits if h['stem'] == x and h['cls'] == 'LIVE USE') for x in BTM.STEMS}
        res[k] = dict(per=per, live=live, hits=hits)
        L += ['### %s: per stem %s ; live uses %s' % (TITLE[k], per, live)] + ['    :%-4d %-6s %-12s %-40s ...%s...' % (
            h['line'], h['stem'], h['word'], h['cls'][:40], h['text']) for h in hits] + ['']
    put_json('b557_stems.json', res)
    put_txt('b557_stems.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (11): CP-1 CLOSE
ROSTER = [('PATHS_TO_THE_CRITICAL_LINE', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md', r'^## The tiers of \(R149\)-\(R150\)'),
          ('SIMPLICITY_OF_RIEMANN_ZEROS', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', r'^#### THE CASCADE, ACT EIGHT'),
          ('THE_UNCONDITIONAL_SURROUND', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md', r'^### Correspondence, tiered under \(R149\)'),
          ('GRH_CASCADE', GRHR, r'^#### THE CASCADE, ACT NINE'),
          ('R_CURVE_CRITERION', 'phase1.5/rcurve/R_CURVE_CRITERION.md', r'^#### THE CASCADE, ACT TEN'),
          ('INDEX_ARITY_AT_THE_CRITICAL_LINE', 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md', r'^#### THE CASCADE, ACT TEN'),
          ('THE_RESIDUE_OF_RH', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md', r'^#### \*\*THE CASCADE, ACT FIVE'),
          ('ADDITIVE_MULTIPLICATIVE_CONSPIRACY', 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md', r'^#### THE CASCADE, ACT TEN')] + [
          (TITLE[k], DOCS[k], r'^#### THE CASCADE, ACT ELEVEN') for k in DOCS] + [
          ('A_Place_to_Stand (MONO, CONCORDANCE-CARRIED; its tier map in FINDINGS)', 'FINDINGS.md', r'^## A Place To Stand read against the RH-anchor: the sentence census and the chapter tier map, act one'),
          ('BALANCE_AND_POSITIVITY', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md', r'^### Appendix B\.5, tiered under'),
          ('FACES_OF_H2_AT_FINITE_INSTANCE', 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md', r"^### The Correspondence paragraph's terminals, tiered"),
          ('FACES_LEDGER', 'FACES_LEDGER.md', r'^## UPDATE .*\(b547\): the rows R1-R5, F1-F7 and L1 tiered'),
          ('THE_IDENTITY_CHAIN', 'phase2/method/THE_IDENTITY_CHAIN.md', r'^#### \*\*THE CASCADE, ACT SIX'),
          ('THE_KEYSTONE_CENSUS', CENR, r'^# THE KEYSTONE CENSUS v0\.2')]


def roster():
    out, L = [], ['b557 -- READING (11): CP-1`S ROSTER, EACH DOCUMENT`S TIER-BLOCK LINE', '']
    for name, rel, pat in ROSTER:
        p = os.path.join(PP, *rel.split('/'))
        if not os.path.exists(p):
            hits = [x for x in g(PP, 'ls-files').split(NL) if x.endswith('/' + os.path.basename(rel))]
            p = os.path.join(PP, *hits[0].split('/')) if hits else p
            rel = hits[0] if hits else rel
        ls = lines_with(p, pat) if os.path.exists(p) else []
        out.append(dict(document=name, path=rel, line=ls[0] if ls else None))
        L.append('    %-72s %-60s %s' % (name, rel, (':%d' % ls[0]) if ls else 'MISSING'))
    miss = [o['document'] for o in out if not o['line']]
    L += ['', '### ### **CP-1 %s** -- %d documents on the roster, %d with a tier block%s' % ('CLOSED' if not miss else 'NOT CLOSED', len(out), len(out) - len(miss),
                                                                                         '' if not miss else '; missing: %s' % miss)]
    put_json('b557_roster.json', dict(roster=out, missing=miss, closed=not miss))
    put_txt('b557_roster.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (12): THE ENTRY
FH = '## The cascade, act eleven: the eight method keystones tiered; CP-1 closed; the no_type_d tier settled; the stale olean rebuilt'
HEADING = ('### b557 — the cascade, act eleven under (R167): the eight method keystones tiered; CP-1 closed; the no_type_d tier settled; the '
           'stale olean rebuilt; the anchor list`s scope restated')


def findings():
    guard_absent(FIND, FH)
    ts, bl, ro, pj, sp, an, ce, st = (jl('b557_tiers.json'), jl('b557_blocks.json'), jl('b557_roster.json'), jl('b557_prints.json'), jl('b557_supersede.json'),
                                      jl('b557_anchor.json'), jl('b557_census.json'), jl('b557_stems.json'))
    m4r = probes().get('m4r', {})
    L = ['', FH, '', '*Filed at b557 on the author`s ruling `(R167)`. The cascade`s act eleven, CP-1`s batch two. Banks: relay `data/b557_tiers.txt`, '
         '`data/b557_prints.txt`, `data/b557_w6.txt`, `data/b557_roster.txt`, `data/b557_stems.txt`, `data/b557_probes.jsonl`.*', '']
    for k in DOCS:
        s = ts.get(k, {})
        if not s.get('rows'):
            L += ['**%s** (block at `%s`:%d): no Correspondence table naming terminals; its claims T4.' % (TITLE[k], DOCS[k], bl[k]['line']), '']
            continue
        L += ['**%s** (block at `%s`:%d): %d rows; tiers over %d readings %s; CARRIED %d · MOVED %d%s; banned stems %d.' % (
            TITLE[k], DOCS[k], bl[k]['line'], len(s['rows']), len(s['terms']), ' · '.join('%s %d' % (x, s['term_tiers'][x]) for x in ORDER if s['term_tiers'][x]),
            s['disp']['CARRIED'], s['disp']['MOVED'], (' (' + ', '.join(':%d' % r['line'] for r in s['rows'] if r['disp'] == 'MOVED') + ')') if s['disp']['MOVED'] else '',
            sum(st[k]['per'].values())), '']
    L += ['**The T0 terminals across the batch:** %s.' % ('; '.join('`%s` (%s)' % (short(n), sj) for n, sj in ts['t0']) or 'none'), '',
          '**The no_type_d tier settled:** the superseding line at `GRH_CASCADE.md`:%d (T2 by `(R167)`(1); b555`s T0 kept as written).' % sp['line'], '',
          '**The stale olean rebuilt:** SIDE-lv-conservation v0.11.0 built in a worktree (exit %s, 8273 jobs); %d prints with a banked profile agree, '
          '%d disagree; the working checkout`s artefacts replaced; probe m4 re-run as m4r: exit %s, errors %s.' % (
              pj.get('build_exit'), pj.get('agree'), len(pj.get('disagree', [])), m4r.get('exit'), m4r.get('errors')), '',
          '**The anchor list`s scope** restated at `FINDINGS.md`:%d; **the census line** at `THE_KEYSTONE_CENSUS.md`:%d, corrected in the same act '
          'at :%d.' % (an['line'], ce['append']['line'], ce['correction']['line']), '',
          '**CP-1 %s:** %d documents on the roster, each with its tier-block line (relay `data/b557_roster.txt`)%s.' % (
              'CLOSED' if ro['closed'] else 'NOT CLOSED', len(ro['roster']), '' if ro['closed'] else '; missing %s' % ro['missing']), '',
          '**Next:** b558, CP-1b -- the implication pass.', '',
          '*Nothing deposits; nothing at Zenodo written; no `.lean` file edited; nothing here is a statement about RH or any zero.*', '']
    o = append_to(FIND, NL.join(L))
    o['line'] = line_of(FIND, FH)
    put_json('b557_findings.json', o)
    print(NL.join(rd(FIND).split(NL)[o['line'] - 1:]))


# ------------------------------------------------------------------------------ THE SCORES, THE DESK, THE RECORD
WRITE_OK = {'FINDINGS.md', 'OPEN_TRAILS.md', GRHR, CENR} | set(DOCS.values())
MEMDIR = P.MEMDIR
PRE_HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': 'a91d941',
             'SIDE-effects': 'ef4cff7', 'SIDE-silence-principle': '667c254', 'SIDE-compression': 'e9a5a36', 'SIDE-structural-error-correction': '6a4f482',
             'SIDE-cosmo': 'c5cba30'}


def w_(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def mains():
    return {k: sorted(x for x in g(os.path.join(DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip()) for k, h in PRE_HEADS.items()}


def scores():
    ts, pj, ro = jl('b557_tiers.json'), jl('b557_prints.json'), jl('b557_roster.json')
    pr = probes()
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b557_') and needle in rd(os.path.join(T, x))]
    tk = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(tk) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b557_')) if tk else None
    m = mains()
    lean = [(k, f) for k, v in m.items() for f in v if f.endswith('.lean')]
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    trial = dict(head=g(TRIAL, 'rev-parse', 'HEAD').strip(), status=g(TRIAL, 'status', '--porcelain', '--untracked-files=no').strip())
    terms = [t for k in DOCS for t in ts.get(k, {}).get('terms', [])]
    t0 = ts.get('t0', [])
    shells = [(t['row'], t['name']) for t in terms if short(t['name']) in ('grh_exclusion', 'no_ls_zero')]
    fun_true = [(k, r['line']) for k in DOCS for r in ts.get(k, {}).get('rows', []) for n in r['names']
                if short(n) in ('grh_exclusion', 'no_ls_zero', 'no_conspiracy_twins', 'no_conspiracy_goldbach', 'no_conspiracy_sg')]
    ed = ts.get('EDIFF', {}).get('rows', [])
    m4r = pr.get('m4r', {})
    return dict(
        n1=bool(ts) and len(t0) <= 5 and all(sj and 'ζ' not in sj for _, sj in t0),
        n2=bool(fun_true), n2_hits=fun_true,
        n3=bool(ed) and all(r['disp'] == 'CARRIED' for r in ed) and any('sieve_ceiling_semantic' in r['names'] for r in ed),
        n4=bool(pj.get('verdict')) and m4r.get('exit') == 0 and m4r.get('errors') == 0,
        n5=bool(ro.get('closed')),
        n6=not lean and not zen and tok == 0 and dep and trial['head'].startswith('f22ff35') and trial['status'] == '',
        t0=t0, mains=m, zen=zen, token=tok, deposit_clean=dep, trial=trial, m4r=dict(exit=m4r.get('exit'), errors=m4r.get('errors')),
        s1=any(r['disp'] == 'MOVED' and 'SIDESilencePrinciple.Universal.silence_universal' in r['names'] for r in ts.get('FOUND', {}).get('rows', [])),
        s2=not shells,
        s3=any(r['disp'] == 'MOVED' and 'sieve_ceiling' in r['names'] for r in ed))


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6'), ('s1', 's2', 's3')
    ts = jl('b557_tiers.json')
    L = ['=' * 104, 'b557 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- T0 terminals (distinct): %d -- %s.' % (w_(sc['n1']), len(sc['t0']), sc['t0']),
         '  **(N2)** ### **%s.** -- rows naming a `fun _ => True` shell of SIDE-effects: %s ; the SieveCeiling terminals the rows name carry no `True` '
         'body at v1.4 or v1.7 (relay data/b557_w6.txt): their shell grade is SCAFFOLDING by docstring, not `fun _ => True`.' % (w_(sc['n2']), sc['n2_hits'] or 'NONE'),
         '  **(N3)** ### **%s.** -- E_DIFFICULTY rows: %s.' % (w_(sc['n3']), [(r['line'], r['disp'], r['names']) for r in ts.get('EDIFF', {}).get('rows', [])]),
         '  **(N4)** ### **%s.** -- prints verdict %s ; m4r %s.' % (w_(sc['n4']), jl('b557_prints.json').get('verdict'), sc['m4r']),
         '  **(N5)** ### **%s.** -- the roster: %s.' % (w_(sc['n5']), 'CLOSED' if sc['n5'] else jl('b557_roster.json').get('missing')),
         '  **(N6)** ### **%s.** -- mains changed %s ; token %s ; deposit clean %s ; trial %s.' % (
             w_(sc['n6']), {k: v for k, v in sc['mains'].items() if v} or 'NONE', sc['token'], sc['deposit_clean'], sc['trial']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- FOUNDATIONS :628.' % w_(sc['s1']), '  **(S2)** ### **%s.** -- no row names the SIDE-effects shells.' % w_(sc['s2']),
         '  **(S3)** ### **%s.** -- E_DIFFICULTY :162.' % w_(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in N].count(None),
            [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b557_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b557_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b557_desk_notes.txt', L)
    put_json('b557_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b557 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b557_cost.txt', 'b557_prints.txt', 'b557_replace_plan.txt', 'b557_tiers.txt', 'b557_w6.txt', 'b557_stems.txt', 'b557_roster.txt'):
        if os.path.exists(os.path.join(D, n)):
            L += ['### relay data/%s' % n] + ['  ' + l for l in rd(os.path.join(D, n)).rstrip(NL).split(NL)] + ['']
    for n in ('b557_supersede.json', 'b557_anchor.json', 'b557_census.json', 'b557_replace_done.json', 'b557_blocks.json', 'b557_findings.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)[:3000]))
    L += ['### THE PROBES : relay data/b557_probe_<id>.txt and data/b557_probes.jsonl', '### THE WORKTREE : data/b557_worktree.txt', '=' * 132]
    put_txt('b557_components.txt', L)
    print(NL.join(L[:6]))


def trail():
    sc = scores()
    ts, bl, sp, an, ce, ro, fj = (jl('b557_tiers.json'), jl('b557_blocks.json'), jl('b557_supersede.json'), jl('b557_anchor.json'), jl('b557_census.json'),
                                  jl('b557_roster.json'), jl('b557_findings.json'))
    body = ['', HEADING, '',
            '**(R167) ratified.** (1) no_type_d_conspiracies and crt_exhaustiveness T2, b555`s line superseded. (2) The stale olean rebuilt at its tag '
            'in a worktree and replaced on agreement. (3) The RH-anchor list`s scope restated. (4) The census`s bd2ae1a sentence checked and recorded. '
            '(5) Batch two tiered. (6) CP-1 closed if every roster document carries a tier block.', '',
            '**Entered:** GRH_CASCADE.md:%d (the superseding line); FINDINGS.md:%d (the anchor scope) and :%d (the entry); THE_KEYSTONE_CENSUS.md:%d '
            'and :%d (the census line and its correction); %s.' % (sp['line'], an['line'], fj['line'], ce['append']['line'], ce['correction']['line'],
                                                                   '; '.join('%s.md:%d (the tier block)' % (TITLE[k], bl[k]['line']) for k in DOCS)), '']
    for k in DOCS:
        s = ts.get(k, {})
        if s.get('rows'):
            body.append('**%s:** tiers %s; CARRIED %d · MOVED %d.' % (TITLE[k], ' · '.join('%s %d' % (x, s['term_tiers'][x]) for x in ORDER if s['term_tiers'][x]),
                                                                    s['disp']['CARRIED'], s['disp']['MOVED']))
        else:
            body.append('**%s:** no terminal named; T4.' % TITLE[k])
    body += ['', '**CP-1:** %s.' % ('CLOSED -- every roster document carries a tier block' if ro['closed'] else 'NOT CLOSED; missing %s' % ro['missing']), '',
             '**Next:** b558, CP-1b.', '',
             '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
             % tuple(w_(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
             '**No kernel lane opened at this act; one build ran in a worktree, removed after; the kernel reads were fresh elaborations at pin.** '
             'Nothing deposits; nothing at Zenodo written; no `.lean` file edited; no monograph byte changed; ERRATA untouched; the ceiling '
             'unchanged; row U1 unedited; no work-order started; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a '
             'statement about RH or any zero.', '']
    text = poss(NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    import banned_terms as BT
    if [m.group(0) for m in BT.PAT.finditer(text)]:
        sys.exit('### A BANNED STEM IN THE TRAIL')
    before = open(OT, 'rb').read()
    if poss(HEADING).encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(poss(HEADING)))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b557_trail_notes.json', out)


if __name__ == '__main__':
    fn = {k: globals()[k] for k in list(globals()) if k in ('reads', 'supersede', 'cost', 'prints', 'replace', 'anchor', 'census', 'rows', 'tiers',
                                                               'w6', 'blocks', 'stems', 'roster', 'findings', 'components', 'desk', 'trail')}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
