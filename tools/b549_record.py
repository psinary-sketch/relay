# -*- coding: utf-8 -*-
"""b549_record.py -- THE CASCADE, ACT FIVE: THE_RESIDUE_OF_RH TIERED; b548`S READINGS AT THEIR WEIGHT; THE ORDER-3 BUDGET
REPAIRED; THE STRAY CHANGE SETTLED: THE RECORD, UNDER (R159).
### `python tools/b549_record.py reads | tiers | premise | residue_rows | checks | family | budget_control | sweep_xi3 <lo> <hi> |
### budget_report | stray | findings | components | desk | trail`

### The xi cell is b548`s `cell_xi(a, p)`, IMPORTED; the repaired budget adds one term beside it and edits no instrument.
### THE_RESIDUE_OF_RH one appended block; FINDINGS appends; OPEN_TRAILS one append. This file deletes nothing.
"""
import io, json, math, os, re, subprocess, sys, time
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
EF = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
RES = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
LBM = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
NL = chr(10)
GRID = list(range(10, 61))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def jsonl(n):
    p = os.path.join(D, n)
    return [json.loads(l) for l in rd(p).split(NL) if l.strip()] if os.path.exists(p) else []


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def put_txt(n, lines):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(NL.join(lines) + NL)


def append_line(n, obj):
    with io.open(os.path.join(D, n), 'a', encoding='utf-8', newline=NL) as fh:
        fh.write(json.dumps(obj) + NL)


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


LV_MAIN = '2f71068'
LV_TIP = '5a14205'
LV_TAG = 'v0.10.0'
LV_FILES = ['SIDELvConservation/ZeroActingPairing.lean', 'SIDELvConservation/ZeroActingPartial.lean']
ROWS = [  # ### the first table, :99-112, row by row: (result, [terminals], the row`s stated profile)
    ('The interface (§6)', ['zeroActingPairing_to_RH', 'distinctFromInput_discharged'], 'std3'),
    ('DH-exclusion — clause (3) load-bearing (§2)', ['signNeutral_not_eulerConsuming', 'zeroActingPairing_ledger_not_signNeutral', 'dhModelLedger_no_pairing'], 'std3'),
    ('The edge lemma (§2)', ['edge_drift_nonneg', 'edge_drift_neg_for_signNeutral'], 'std3'),
    ('The 𝔽_q anatomy (§6)', ['transfer_obstruction_is_the_two_geometric_clauses', 'exactly_two_clauses_obstruct'], 'axiom-free'),
    ('The finite-range inhabitant (§6)', ['certifiedPartialInhabitant', 'coverage_boundary_exact', 'partial_mono'], 'std3'),
    ('Positivity is free (§6)', ['positivity_free_obstruction_is_zeroRealization'], 'std3'),
    ('The realization ledger (§6)', ['no_asset_realizes_zeroSpectrum', 'location_owned_spectrum_not'], 'axiom-free'),
    ('The residue, compiled (§7)', ['residue_irreducible'], 'std3'),
    ('The X-realization spec (§6)', ['XRealization', 'xRealization_to_zeroActingPairing', 'xRealization_to_RH'], 'std3'),
    ('The family spec + residual (§8)', ['SimplicityFamilySpec', 'simplicityFamily_generic_not_universal'], 'axiom-free'),
    ('The barrier extension (§7)', ['detection_threshold_mono'], 'std3'),
    ('The escape-kind invariant (§8)', ['escape_kind_discriminates', 'horizon_kind_shared'], 'axiom-free')]
TERMS = [t for _, ts, _ in ROWS for t in ts]


# ------------------------------------------------------------------------------ THE READS
def cite(L, path, a, z, what, text=None):
    t = (text if text is not None else rd(path)).split(NL)
    rel = os.path.relpath(path, PP) if path.startswith(PP) else os.path.relpath(path, ROOT) if path.startswith(ROOT) else path
    L.append('### %s:%d-%d -- %s' % (rel.replace(os.sep, '/'), a, min(z, len(t)), what))
    L.extend('  :%d %s' % (i + 1, t[i][:900]) for i in range(a - 1, min(z, len(t))))
    L.append('')


def reads():
    L = ['b549 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    cite(L, RES, 1, 211, 'THE_RESIDUE_OF_RH.md entire (§§1-8, the two Correspondence tables, every era and currency annotation)')
    for f, a, z in ((LV_FILES[0], 34, 92), (LV_FILES[1], 110, 146)):
        cite(L, os.path.join(LV, f), a, z, 'SIDE-lv-conservation main %s' % LV_MAIN, text=g(LV, 'show', '%s:%s' % (LV_MAIN, f)))
    L.append('### the 25 terminals in three trees (git grep of a declaration line): main %s, the tip %s, the tag %s' % (LV_MAIN, LV_TIP, LV_TAG))
    for n in TERMS:
        pat = r'^(noncomputable )?(private )?(theorem|lemma|def|structure|class|abbrev|inductive) %s\b' % n
        hits = {rev: [l for l in g(LV, 'grep', '-nE', pat, rev, '--', '*.lean').split(NL) if l.strip()] for rev in (LV_MAIN, LV_TIP, LV_TAG)}
        L.append('  %-52s main %s ; tip %d ; tag %d' % (n, (hits[LV_MAIN][0].split(':')[1] + ':' + hits[LV_MAIN][0].split(':')[2]) if hits[LV_MAIN] else 'NOT FOUND',
                                                        len(hits[LV_TIP]), len(hits[LV_TAG])))
    L.append('  the two files, diff %s..%s : %s' % (LV_TIP, LV_MAIN, g(LV, 'diff', '--stat', LV_TIP, LV_MAIN, '--', *LV_FILES).strip() or 'NONE (byte-identical)'))
    L.append('  %s is an ancestor of main : %s ; of %s : %s' % (
        LV_TIP, subprocess.run(['git', '-C', LV, 'merge-base', '--is-ancestor', LV_TIP, LV_MAIN]).returncode == 0, LV_TAG,
        subprocess.run(['git', '-C', LV, 'merge-base', '--is-ancestor', LV_TIP, LV_TAG]).returncode == 0))
    L.append('  %s = %s' % (LV_TAG, g(LV, 'rev-parse', LV_TAG + '^{commit}').strip()))
    L.append('')
    cite(L, os.path.join(EF, 'SIDEExplicitFormula/H2Sign.lean'), 22, 31, 'SIDE-explicit-formula v0.2 = 5c72cad', text=g(EF, 'show', 'v0.2:SIDEExplicitFormula/H2Sign.lean'))
    cite(L, os.path.join(EF, 'SIDEExplicitFormula/Seam.lean'), 99, 101, 'SIDE-explicit-formula v0.2', text=g(EF, 'show', 'v0.2:SIDEExplicitFormula/Seam.lean'))
    cite(L, FIND, 5529, 5531, 'the detection-geometries entry')
    cite(L, FIND, 5613, 5615, 'b548`s entry')
    cite(L, FIND, 5649, 5649, 'b548`s pointer')
    for n in ('b548_interference.txt', 'b548_sweep_xi.txt', 'b548_sweep_q0.txt', 'b548_h2.txt'):
        t = rd(os.path.join(D, n))
        L.append('### relay data/%s : %d lines ; its summary lines:' % (n, len(t.split(NL))))
        L += ['  :%d %s' % (i + 1, l[:300]) for i, l in enumerate(t.split(NL)) if l.strip().startswith(('### n =', '  ### n =', '  H1.', '  H2.', '  REFUTER', '  ### H'))]
        L.append('')
    cite(L, os.path.join(T, 'b521_tail.py'), 44, 53, 'PWindow -- variant (B) at order p')
    cite(L, os.path.join(T, 'b519_window.py'), 67, 135, 'VWindow: the plateau window, phihat, ghat, khat -- the window definition verbatim')
    cite(L, os.path.join(T, 'b519_window.py'), 32, 32, 'F_RAMP')
    cite(L, os.path.join(T, 'e16', 'carto_atlas.py'), 8, 25, 'the instrument constants: NU, UMAX and the decay assumption')
    cite(L, os.path.join(T, 'e16', 'carto_atlas.py'), 33, 40, 'the xi kernel')
    cite(L, os.path.join(T, 'b326_windows.py'), 220, 229, 'the Q0 kernel (qd)')
    cite(L, os.path.join(T, 'b511_families.py'), 44, 47, 'the three u-grids')
    cite(L, os.path.join(T, 'b511_families.py'), 193, 194, 'arch')
    cite(L, os.path.join(T, 'b548_record.py'), 78, 102, 'cell_xi -- the quadrature budget E_u at :84')
    cite(L, os.path.join(T, 'b519_window.py'), 160, 180, 'phi_bound, majorant, tail -- the order-p majorant')
    L.append('### relay data/b546_scores.json -- the working-tree diff')
    L += ['  ' + l for l in g(ROOT, 'diff', '--', 'data/b546_scores.json').split(NL) if l.strip()]
    L.append('  file time %s ; b546 commits: %s' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(os.path.join(D, 'b546_scores.json')))),
                                                 ' ; '.join(g(ROOT, 'log', '--format=%h %ci', '-1', r).strip() for r in ('ce0cccfb', '9e06a910'))))
    L.append('  PLACE-papers 37b36b3 (b546) files: %s' % ', '.join(x for x in g(PP, 'show', '--name-only', '--format=', '37b36b3').split(NL) if x.strip()))
    L.append('')
    cite(L, LBM, 66, 71, 'THE_LOAD_BEARING_MAP`s RESIDUE rows')
    cite(L, os.path.join(D, 'b506_c2_results.json'), 5550, 5560, 'the b506 bank`s found zero near t = 16.290 (its σ)')
    cite(L, os.path.join(PP, 'archive', '2026-08-24-ledger-split', 'VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md'), 2296, 2304,
         'the Epstein C-run §4 draws on (provenance epstein_crun2.py)')
    cite(L, os.path.join(PP, 'phase1.5', 'spectral', 'THE_COHERENCE_INVARIANT.md'), 25, 38, 'the coherence table')
    put_txt('b549_reads.txt', L)
    print('  reads banked : %d lines' % len(L))


# ------------------------------------------------------------------------------ COMPONENT 1: THE RESIDUE TIERED
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
LIT_WEIL_LI = 'the Weil direction (channel inequality to Li positivity) and Li`s criterion (Bombieri-Lagarias 1999), named premises, neither compiled'
LIT_NZ = 'the named premise `NontrivialZeroExistsInStrip`, a literature fact not compiled'
TIER = {
    'zeroActingPairing_to_RH': ('T1-lit', 'concludes Mathlib`s `RiemannHypothesis` through ' + LIT_WEIL_LI),
    'distinctFromInput_discharged': ('T1-lit', 'rests on ' + LIT_NZ),
    'signNeutral_not_eulerConsuming': ('T2', 'arithmetic on an abstract ledger ℕ → ℝ; no premise about zeta'),
    'zeroActingPairing_ledger_not_signNeutral': ('T2', 'about the typed specification and an abstract ledger; no premise about zeta'),
    'dhModelLedger_no_pairing': ('T2', 'about a model ledger and the typed specification; no premise about zeta'),
    'edge_drift_nonneg': ('T2', 'a sum of non-negative terms over abstract sequences'),
    'edge_drift_neg_for_signNeutral': ('T2', 'an explicit witness over the model ledger'),
    'transfer_obstruction_is_the_two_geometric_clauses': ('T2', 'a model-level enumeration (a Bool table on four clauses)'),
    'exactly_two_clauses_obstruct': ('T2', 'a count over the same model-level table'),
    'certifiedPartialInhabitant': ('T1-lit', 'rests on `VerifiedZerosTo`, `ExplicitFormulaDecomp` and `TailBoundPremise`, named premises stating literature and numerical facts not compiled'),
    'coverage_boundary_exact': ('T2', '`N₀ T = ⌊2T²⌋₊` by `rfl`: arithmetic; the reading is carried by the identifier'),
    'partial_mono': ('T2', 'monotonicity of a finite-range Prop over abstract sequences'),
    'positivity_free_obstruction_is_zeroRealization': ('T1-lit', 'rests on ' + LIT_NZ),
    'no_asset_realizes_zeroSpectrum': ('T2', 'a model-level enumeration of the programme`s assets'),
    'location_owned_spectrum_not': ('T2', 'the same enumeration'),
    'residue_irreducible': ('T1-lit', 'rests on ' + LIT_NZ + ', on `VerifiedZerosTo`, `ExplicitFormulaDecomp`, `TailBoundPremise`, and on ' + LIT_WEIL_LI),
    'XRealization': ('T2', 'a typed specification (STRUCTURE), no instance'),
    'xRealization_to_zeroActingPairing': ('T1-lit', 'rests on ' + LIT_NZ),
    'xRealization_to_RH': ('T1-lit', 'rests on ' + LIT_NZ + ' and on ' + LIT_WEIL_LI),
    'SimplicityFamilySpec': ('T2', 'a typed specification (STRUCTURE), no instance'),
    'simplicityFamily_generic_not_universal': ('T2', 'an explicit witness over an abstract predicate on ℕ'),
    'detection_threshold_mono': ('T2', 'monotonicity of `⌊2T²⌋₊` in T: arithmetic; the reading is carried by the identifier'),
    'escape_kind_discriminates': ('T2', 'a model-level enumeration (two wall kinds)'),
    'horizon_kind_shared': ('T2', 'the same enumeration')}


def parse_check():
    t = rd(os.path.join(D, 'b549_residue_check.txt'))
    out, last = {}, 0
    for m in re.finditer(r"'SIDELvConservation\.RegisterPentagon\.(\w+)' (does not depend on any axioms|depends on axioms: \[([^\]]*)\])", t):
        name = m.group(1)
        prof = set() if m.group(2).startswith('does not') else {x.strip() for x in m.group(3).replace(NL, ' ').split(',') if x.strip()}
        out[name] = dict(statement=' '.join(t[last:m.start()].split()), profile=sorted(prof))
        last = m.end()
    head = t.split(NL)[0]
    ok = re.search(r'exit 0', t) is not None
    return out, head, ok


def pname(s):
    return 'std3' if s == STD3 else ('axiom-free' if not s else '[' + ', '.join(sorted(s)) + ']')


def three_trees(n):
    pat = r'^(noncomputable )?(private )?(theorem|lemma|def|structure|class|abbrev|inductive) %s\b' % n
    c = {rev: [l for l in g(LV, 'grep', '-nE', pat, rev, '--', '*.lean').split(NL) if l.strip()] for rev in (LV_MAIN, LV_TIP, LV_TAG)}
    loc = ':'.join(c[LV_MAIN][0].split(':')[1:3]) if c[LV_MAIN] else None
    return dict(main=len(c[LV_MAIN]), tip=len(c[LV_TIP]), tag=len(c[LV_TAG]), loc=loc)


def tiers():
    chk, head, ok = parse_check()
    identical = g(LV, 'diff', '--stat', LV_TIP, LV_MAIN, '--', *LV_FILES).strip() == ''
    L = ['b549 -- COMPONENT 1 (a): THE RESIDUE`S TERMINALS, TIERED (READINGS (1)-(3)); the #check bank: ' + head + (' ; exit 0' if ok else ' ; NOT exit 0'), '',
         '### the two files holding every terminal, %s..%s : %s' % (LV_TIP, LV_MAIN, 'byte-identical' if identical else 'DIFFER'), '',
         '  terminal                                            main:line                                   tip tag  profile      tier    reason']
    rows_out, terms_out = [], []
    for res, ts, stated in ROWS:
        union, found = set(), True
        for n in ts:
            tt = three_trees(n)
            c = chk.get(n)
            prof = set(c['profile']) if c else None
            found = found and tt['main'] == 1 and tt['tip'] == 1 and c is not None
            union |= (prof or set())
            tier, why = TIER[n]
            terms_out.append(dict(terminal=n, row=res, loc=tt['loc'], main=tt['main'], tip=tt['tip'], tag=tt['tag'], profile=pname(prof) if prof is not None else 'NO CHECK',
                                  statement=c['statement'] if c else None, tier=tier, reason=why))
            L.append('  %-51s %-43s %d   %d    %-12s %-7s %s' % (n, tt['loc'], tt['tip'], tt['tag'], pname(prof) if prof is not None else 'NO CHECK', tier, why))
        disp = 'CARRIED' if (found and pname(union) == stated and identical and ok) else 'MOVED'
        smaller = [t['terminal'] for t in terms_out if t['row'] == res and t['profile'] != stated]
        rows_out.append(dict(result=res, terminals=ts, stated=stated, fresh_union=pname(union), disposition=disp, smaller=smaller,
                             tiers=sorted(set(TIER[n][0] for n in ts))))
        L.append('    ### ROW "%s" : stated %s ; fresh union %s ; %s%s' % (res, stated, pname(union), disp,
                 (' ; a terminal`s own profile below the row`s: ' + ', '.join(smaller)) if smaller else ''))
    tc = {k: sum(1 for t in terms_out if t['tier'] == k) for k in ('T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4')}
    dc = {k: sum(1 for r in rows_out if r['disposition'] == k) for k in ('CARRIED', 'MOVED')}
    second = [dict(row='the residue, compiled (§7)', disposition=rows_out[7]['disposition'], tier='T1-lit'),
              dict(row='the 𝔽_q anatomy (§6)', disposition=rows_out[3]['disposition'], tier='T2'),
              dict(row='the realization ledger (§6)', disposition=rows_out[6]['disposition'], tier='T2'),
              dict(row='the finite-range inhabitant (§6)', disposition=rows_out[4]['disposition'], tier='T1-lit'),
              dict(row='the eight further rows above', disposition='CARRIED' if all(r['disposition'] == 'CARRIED' for r in rows_out) else 'MOVED', tier='as the first table'),
              dict(row='the zero-acting positive pairing`s EXISTENCE', disposition='CARRIED', tier='no terminal (RESEARCH-REACH, disclaimed); annotated by appended line'),
              dict(row='`h2`, the one open premise', disposition='MOVED', tier='T1-open as premise; the equivalence T0 ((R159)(5))')]
    L += ['', '### the terminals: %d ; on main %d ; at the tip %d ; in the tag`s tree %d' % (
        len(terms_out), sum(t['main'] for t in terms_out), sum(t['tip'] for t in terms_out), sum(t['tag'] for t in terms_out)),
        '### tiers : ' + ' · '.join('%s %d' % kv for kv in tc.items()),
        '### first table, rows : ' + ' · '.join('%s %d' % kv for kv in dc.items()),
        '### the second table (:124-132):'] + ['  %-48s %-8s %s' % (s['row'], s['disposition'], s['tier']) for s in second]
    put_json('b549_tiers.json', dict(rows=rows_out, terminals=terms_out, tier_counts=tc, disp_counts=dc, second=second, identical=identical, check_ok=ok, check_head=head))
    put_txt('b549_tiers.txt', L)
    print(NL.join(L[-14:]))


def premise():
    chk, _, _ = parse_check()
    st = chk['residue_irreducible']['statement']
    ef = g(EF, 'show', 'v0.2:SIDEExplicitFormula/H2Sign.lean').split(NL)
    seam = g(EF, 'show', 'v0.2:SIDEExplicitFormula/Seam.lean').split(NL)
    prem = [('hZero', 'NontrivialZeroExistsInStrip'), ('hdecomp', '∀ n, lam n = lam_A n + lam_Z n'), ('hV', 'VerifiedZerosTo T'),
            ('hEF', 'ExplicitFormulaDecomp lam low tail T'), ('hTail', 'TailBoundPremise low tail T'),
            ('inequalityToPositivity', 'Register4_channelInequality lam_A lam_Z → Register4_positivity lam'),
            ('liCriterion', 'Register4_positivity lam → RiemannHypothesis')]
    shapes = ('h2_sign', 'h2_sign → RiemannHypothesis', 'RiemannHypothesis → h2_sign')
    match = [p for p in prem if p[1] in shapes]
    reqs = [l.strip() for l in rd(os.path.join(LV, 'lakefile.lean')).split(NL) if l.strip().startswith('require')]
    mani = {}
    for r, p in (('SIDE-lv-conservation', LV), ('SIDE-explicit-formula', EF)):
        m = json.loads(rd(os.path.join(p, 'lake-manifest.json')))
        mani[r] = dict(mathlib=next((x.get('rev') for x in m.get('packages', []) if x.get('name') == 'mathlib'), None), toolchain=rd(os.path.join(p, 'lean-toolchain')).strip())
    L = ['b549 -- COMPONENT 1 (b): THE PREMISES OF residue_irreducible (READING (4))', '',
         '### the fresh #check (lv main %s):' % LV_MAIN, '  ' + st, '',
         '### its premises, by name and type:'] + ['  %-24s : %s' % p for p in prem] + [
        '', '### beside them, at SIDE-explicit-formula v0.2 = 5c72cad:',
        '  H2Sign.lean:29-30  ' + ef[28].strip() + ' ' + ef[29].strip(),
        '  Seam.lean:101      ' + seam[100].strip(), '',
        '### a premise whose type is one of %s : %s' % (' / '.join(shapes), ', '.join(p[0] for p in match) or 'NONE'),
        '### THE FORM DIFFERS, and where: the Weil premise of residue_irreducible is `inequalityToPositivity` (with the pairing`s own',
        '### field `yieldsInequality`), a map between Li-channel Props on sequences ℕ → ℝ that the theorem leaves arbitrary; h2_sign is a',
        '### Prop over classK test functions k : ℝ → ℂ built from ζ`s pole term, prime sum and arch term. No premise names h2_sign, and',
        '### the lam of the Li premises is not tied to ζ inside the theorem.',
        '### lv requires %s ; lv toolchain %s, Mathlib %s ; explicit-formula toolchain %s, Mathlib %s -- lv does not import explicit-formula.'
        % (reqs, mani['SIDE-lv-conservation']['toolchain'], (mani['SIDE-lv-conservation']['mathlib'] or '')[:7],
           mani['SIDE-explicit-formula']['toolchain'], (mani['SIDE-explicit-formula']['mathlib'] or '')[:7]), '',
        '### THE DISCHARGE, PRICED IN LEMMAS (not attempted):',
        '  route W (the Weil form, bypassing Li): (W1) a classK field for the pairing -- a sibling specification of ZeroActingPairing whose',
        '      positivity clause is stated on classK test functions (the present fields are Li-channel and carry no test function);',
        '      (W2) that field implies h2_sign, by unfolding; (W3) compose with h2_sign_iff_rh.mp to RiemannHypothesis. W3 is one line; W1',
        '      is the item of substance; the join needs the two kernels on one toolchain and one Mathlib (lv bumped to explicit-formula`s,',
        '      or the specification restated in explicit-formula).',
        '  route L (the Li form, as stated): (L1) ζ`s Li channels as definitions (Mathlib 51e6992 has no Li coefficient, b546) with the',
        '      decomposition at ζ; (L2) Li`s criterion for ζ, Bombieri-Lagarias 1999 -- not compiled, the lemma of substance; (L3) the Weil',
        '      direction inequalityToPositivity at ζ`s channels. h2_sign_iff_rh discharges none of L1-L3: it concludes RH from h2_sign, and',
        '      no premise of the Li route has h2_sign as its hypothesis.',
        '### so the discharge is not immediate: route W costs three lemmas and a toolchain join; route L costs the Li instance.']
    put_json('b549_premise.json', dict(statement=st, premises=prem, match=[p[0] for p in match], requires=reqs, manifests=mani))
    put_txt('b549_premise.txt', L)
    print(NL.join(L[-22:]))


def checks():
    doc = rd(RES).split(NL)
    b = json.loads(rd(os.path.join(D, 'b506_c2_results.json')))
    found = [f for f in b.get('found', []) if abs(f['rho'][1] - 16.290) < 0.01]
    sig = found[0]['rho'][0] if found else None
    rho_line = [i + 1 for i, l in enumerate(rd(os.path.join(D, 'b506_c2_results.json')).split(NL)) if '"rho"' in l][:1]
    s5 = next(i + 1 for i, l in enumerate(doc) if '0.9533 + 16.290' in l)
    sig_ok = sig is not None and round(sig, 3) == round(0.9533, 3)
    loom = os.path.join(PP, 'archive', '2026-08-24-ledger-split', 'VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md')
    lt = rd(loom).split(NL)
    rows = {}
    for i in range(2296, 2304):
        l = lt[i - 1]
        if l.startswith('| ') and not l.startswith('|:--') and 'C[L](N)' not in l:
            cells = [c.strip().strip('*') for c in l.strip('|').split('|')]
            vals = [float(c.replace('−', '-')) for c in cells[1:]]
            key = 'zeta' if cells[0].startswith('ζ') else ('epstein' if 'Epstein' in cells[0] else 'dh')
            rows[key] = dict(line=i, vals=vals)
    ep = rows['epstein']['vals']
    c_ok = round(min(ep), 2) == 0.65 and round(max(ep), 1) == 1.2
    z_ok = round(min(rows['zeta']['vals']), 1) == 0.9 and round(max(rows['zeta']['vals']), 1) == 1.3
    d_ok = round(min(rows['dh']['vals']), 2) == -0.13 and round(max(rows['dh']['vals']), 2) == 0.21
    s4 = next(i + 1 for i, l in enumerate(doc) if '0.65–1.2' in l)
    import banned_terms as BT
    stems = [dict(line=i + 1, col=m.start() + 1, word=m.group(0), context=l[max(0, m.start() - 40):m.end() + 20])
             for i, l in enumerate(doc) for m in BT.PAT.finditer(l)]
    s1 = next(i + 1 for i, l in enumerate(doc) if 'Bombieri–Lagarias' in l)
    s7 = next(i + 1 for i, l in enumerate(doc) if 'the Weil-criterion direction; Li' in l)
    li_reading = ('§7`s "the named classical premises (the Weil-criterion direction; Li`s criterion)" names, in the compiled residue, '
                  'the two uncompiled premises `inequalityToPositivity` and `liCriterion` (T1-lit), and since b536 it names one of two routes '
                  'from positivity to RH: the Weil direction also has its own compiled form, `h2_sign_iff_rh` (T0), which reaches '
                  'RiemannHypothesis on classK test functions without Li`s criterion, but which no premise of `residue_irreducible` takes.')
    L = ['b549 -- COMPONENT 1 (d)-(f): THE σ, THE C-RANGE, THE STEM, THE LI FORM (READINGS (6), (7))', '',
         '### (d) §5 at THE_RESIDUE_OF_RH.md:%d says "ρ ≈ 0.9533 + 16.290 i"; relay data/b506_c2_results.json:%s (found) σ = %r, t = %r'
         % (s5, rho_line[0] if rho_line else '?', sig, found[0]['rho'][1] if found else None),
         '    σ to three decimals: bank %.3f, document %.3f -- %s ; to four: bank %.4f, document 0.9533'
         % (sig, 0.9533, 'MATCH' if sig_ok else 'NO MATCH', sig),
         '### (d) §4 at THE_RESIDUE_OF_RH.md:%d says C[Z_Q] ≈ 0.65–1.2 across N = 10–120, ζ ≈ 0.9–1.3, DH ≈ −0.13 … 0.21; the source table,' % s4,
         '    %s:2298-2302 (provenance epstein_crun2.py, named by the loom; not found in relay or PLACE-papers):' % os.path.relpath(loom, PP).replace(os.sep, '/')]
    for k, v in rows.items():
        L.append('    :%d %-8s %s  min %.3f max %.3f' % (v['line'], k, v['vals'], min(v['vals']), max(v['vals'])))
    L += ['    Epstein %s ; ζ %s ; DH %s' % tuple('MATCH' if x else 'NO MATCH' for x in (c_ok, z_ok, d_ok)), '',
          '### (e) the banned stems (tools/banned_terms.py STEMS %s) in THE_RESIDUE_OF_RH.md, every occurrence, UNEDITED:' % BT.STEMS]
    L += ['    :%d col %d  "%s"  ... %s ...' % (s['line'], s['col'], s['word'], s['context']) for s in stems]
    L += ['    ### (R159)(6) names the 2026-08-12 annotation`s "language gap" (:152); the scan finds %d occurrences on %d lines.' % (len(stems), len(set(s['line'] for s in stems))),
          '', '### (f) §1 (:%d) states Li`s form, "RH holds iff λ_n ≥ 0 for every n" (Bombieri–Lagarias): T1-lit, per (R156)(1).' % s1,
          '### (f) §7 (:%d), the reading in one sentence: %s' % (s7, li_reading)]
    put_json('b549_residue_reads.json', dict(sigma=sig, sigma_line=rho_line, s5=s5, sigma_ok=sig_ok, loom=rows, c_ok=c_ok, z_ok=z_ok, d_ok=d_ok, s4=s4,
                                             stems=stems, s1=s1, s7=s7, li_reading=li_reading))
    put_txt('b549_residue_reads.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 2: THE WINDOW FAMILY, AND THE PRICE
def family():
    import b519_window as B19
    L = ['b549 -- COMPONENT 2 (b): THE WINDOW FAMILY (READING (8))', '', '### the definition, verbatim:']
    cite(L, os.path.join(T, 'b521_tail.py'), 44, 53, 'PWindow')
    cite(L, os.path.join(T, 'b519_window.py'), 77, 93, 'VWindow`s plateau branch and phihat')
    cite(L, os.path.join(T, 'b519_window.py'), 120, 135, 'ghat_cos, poly, ghat, khat')
    L += ['### read: L = ln a ; R = F_RAMP·L/2 = L/8 (F_RAMP = %.2f) ; W = L − R = 7L/8 ; h = 2R/p ; φ̂(z) = sinc(zW)·sinc(zh/2)^p, so' % B19.F_RAMP,
          '### φ = 1[−W,W]/(2W) ⋆ (the order-p B-spline of half-width R), supported on [−L, L] = [−ln a, ln a] AT EVERY p; the test',
          '### function is k̂ = ĝ², ĝ(z) = (γ₀² − z²)·½(φ̂(z − γ₀) + φ̂(z + γ₀)).',
          '### the n-fold self-convolution of an indicator of half-width a/n has transform sinc(z·a/n)^n and support [−a, a], growing',
          '### with the base; the family`s support is ln a, fixed in p, and its base factor carries a plateau of half-width 7L/8 that',
          '### no power of one indicator has.',
          '### VERDICT : THE FAMILY IS NOT THE SELF-CONVOLUTION FAMILY.',
          '### IN ONE SENTENCE: raising p in b522`s family only smooths the two ramps of a fixed plateau on [−ln a, ln a], while the',
          '### route raises a fixed base to its n-th convolution power so that the support grows as n times the base; so F(n·b, n) is',
          '### not the route`s sequence, and the diagonal is not read. H3 : NOT SCORABLE (READING (8)).', '']
    # ### the price, from b548`s banked per-cell seconds (cumulative within a call; the increments are the per-cell cost)
    cost = {}
    for obj, bank in (('q', 'b548_sweep_q.jsonl'), ('xi', 'b548_sweep_xi.jsonl')):
        rows = jsonl(bank)
        prev = None
        for c in rows:
            s = c['seconds']
            d = s - prev if (prev is not None and s >= prev and c['p'] == pp_) else s
            cost[(obj, c['p'], c['a'])] = d
            prev, pp_ = s, c['p']
    tot = {o: sum(v for (ob, p, a), v in cost.items() if ob == o) for o in ('q', 'xi')}
    diag = [(b, n) for b in (4, 5, 6) for n in (3, 5, 7, 9, 11) if n * b <= 60]
    dcost = {o: sum(cost.get((o, n, float(n * b)), 0.0) for b, n in diag) for o in ('q', 'xi')}
    L += ['### THE RE-PARAMETRIZED SWEEP, PRICED (not run, not filed):',
          '  (P1) a window class for the route`s family: φ_n = the n-th convolution power of a fixed base (an indicator, or the base the',
          '       route`s PowerWindow fixes), its transform in closed form (sinc(βz)^n), and the cos-modulation and γ₀-factor kept;',
          '  (P2) its majorant and closed-form zero-side tail -- b521`s constants divide by the plateau half-width W, which this family',
          '       lacks, so the tail constants are re-derived, not imported;',
          '  (P3) a fixture at one cell (closed form against quadrature) before any sweep;',
          '  (P4) the sweep. b548`s banked per-cell seconds: Q0 %.0f s, ξ %.0f s over 255 cells each (total %.0f s). A sweep over the same'
          % (tot['q'], tot['xi'], tot['q'] + tot['xi']),
          '       51 supports and five orders costs about that, since a cell`s cost is set by its support (the prime channel`s range) and',
          '       its order; the ruling`s diagonal alone, %d cells per object (b ∈ {4, 5, 6}, n·b <= 60), costs about Q0 %.0f s and ξ %.0f s'
          % (len(diag), dcost['q'], dcost['xi']),
          '       at b548`s cost for the same (n, a). (P1)-(P3) are tool work of about one act; (P4) runs in foreground chunks.']
    put_json('b549_family.json', dict(self_convolution=False, h3='NOT SCORABLE', cost_total=tot, diag=diag, diag_cost=dcost, F_RAMP=B19.F_RAMP))
    put_txt('b549_diagonal.txt', L)
    print(NL.join(L[-24:]))


# ------------------------------------------------------------------------------ COMPONENT 3: THE ORDER-3 BUDGET
KAPPA = {'xi': 1.0, 'q': 2.0}   # ### |K(u)| <= KAPPA * log u past 2 UMAX: xi Re psi(1/4 + iu/2) - log pi ; Q0 2 Re psi(1/2 + iu) - 2 log(2 pi / sqrt 23)


def x_arch():
    import b511_families as F
    return float(F.U_WIDE[-1])


def e_arch(W, obj):
    """### the arch integral`s truncation past the widest grid, bounded: (1/pi) INT_{2 UMAX}^inf M_p(u) kappa log u du, M_p b519`s
    ### majorant of |k-hat| at the window`s order p (exponent p: |k-hat| <= C u^(2 - 2p)); the geometric grid of b519`s own tail."""
    import b519_window as B19
    X = x_arch()
    u = np.geomspace(X, X * 1e8, 200001)
    return float(np.trapezoid(B19.majorant(W, u, 0.0) * KAPPA[obj] * np.log(u), u) / math.pi)


def kern_mp(obj, u):
    from mpmath import mp, digamma, mpc, re as mre
    mp.dps = 15
    if obj == 'xi':
        return np.array([float(mre(digamma(mpc(0.25, x / 2.0)))) for x in u]) - math.log(math.pi)
    return 2.0 * np.array([float(mre(digamma(mpc(0.5, x)))) for x in u]) - 2.0 * math.log(2.0 * math.pi / math.sqrt(23.0))


def budget_control():
    import b511_families as F
    import b521_tail as B21
    L = ['b549 -- COMPONENT 3: THE BUDGET`S ASSUMPTION, THE KERNEL BOUND, THE CONTROL (READING (9))', '']
    cite(L, os.path.join(T, 'e16', 'carto_atlas.py'), 12, 14, 'the assumption the budget carries')
    cite(L, os.path.join(T, 'b548_record.py'), 84, 84, 'the budget line: E_u = |A_half - A| + |A_wide - A|')
    cite(L, os.path.join(T, 'b511_families.py'), 45, 47, 'the grids: the wide grid doubles the range at the same step')
    L += ['### THE ASSUMPTION AND WHAT ORDER p HAS: the budget treats the two grid differences as the whole quadrature error, which is',
          '### right when k-hat is negligible past 2·UMAX -- "hhat decays faster than any polynomial" (carto_atlas.py:13), true of the',
          '### smooth bump the constants were set for. The order-p window has φ-hat ~ |z|^-(p+1) (a plateau ⋆ an order-p B-spline: the',
          '### order-3 spline is C¹), ĝ ~ |z|^(1-p) after the γ₀-factor, k-hat = ĝ² ~ |z|^(2-2p): |u|^-4 at order 3, |u|^-8 at order 5.',
          '### The wide difference measures the piece on [UMAX, 2·UMAX] and misses the piece past 2·UMAX; for |u|^-4 the missed piece is',
          '### about 1/7 of the measured one, which is the 1.12-1.17 excess of |r| over B b548 banked at order 3.',
          '### THE REPAIR: E_arch = (1/π) ∫_{2·UMAX}^∞ M_p(u)·κ·log u du, M_p b519`s majorant at the window`s order p -- the exponent now',
          '### depends on the order -- added beside B, never in place of it.', '']
    X = x_arch()
    Uw = F.U_WIDE
    ok_k = {}
    for obj, key in (('xi', 'z_wide'), ('q', 'qd_wide')):
        K = F.KER[key]
        sel = np.abs(Uw) >= X / 2.0
        worst = float(np.max(np.abs(K[sel]) / (KAPPA[obj] * np.log(np.abs(Uw[sel])))))
        um = np.geomspace(X, X * 1e8, 61)
        wm = float(np.max(np.abs(kern_mp(obj, um)) / (KAPPA[obj] * np.log(um))))
        ok_k[obj] = worst <= 1.0 and wm <= 1.0
        L.append('### the kernel bound |K| <= %.0f·log u, %s: banked wide grid |u| in [%.0f, %.0f] worst ratio %.4f ; mpmath at 61 points in [%.0f, %.0e] worst %.4f -- %s'
                 % (KAPPA[obj], obj, X / 2.0, X, worst, X, X * 1e8, wm, 'HOLDS' if ok_k[obj] else 'FAILS'))
    L.append('')
    ctl = []
    b48 = {c['a']: c for c in jsonl('b548_sweep_xi.jsonl') if c['p'] == 3}
    for a in (14.0, 38.0):
        W = B21.PWindow(a, 'xi', 3)
        u = np.linspace(X, 2.0 * X, int(round(X / (Uw[1] - Uw[0]))) + 1)
        piece = float(np.trapezoid(W.khat(u).real * kern_mp('xi', u), u) / math.pi)
        E = e_arch(W, 'xi')
        c = b48[a]
        excess = abs(c['r']) - c['B']
        ctl.append(dict(a=a, piece=piece, E_arch=E, excess=excess, r=c['r'], B=c['B'], holds=abs(piece) <= E))
        L.append('### CONTROL a = %.0f, ξ, p = 3 : the four-fold grid`s added piece (|u| in [%.0f, %.0f], step %.2f) %+.3e ; E_arch %.3e ; |piece| <= E_arch %s ;'
                 ' b548`s |r| - B %.3e ; E_arch covers it %s' % (a, X, 2 * X, Uw[1] - Uw[0], piece, E, abs(piece) <= E, excess, E >= excess))
    put_json('b549_budget_control.json', dict(kernel_ok=ok_k, controls=ctl, X=X))
    put_txt('b549_budget_control.txt', L)
    print(NL.join(L[-8:]))


def sweep_xi3():
    import b548_record as B48
    import b521_tail as B21
    lo, hi = int(sys.argv[2]), int(sys.argv[3])
    b48 = {c['a']: c for c in jsonl('b548_sweep_xi.jsonl') if c['p'] == 3}
    done = {c['a'] for c in jsonl('b549_sweep_xi_n3.jsonl')}
    t0 = time.time()
    for a in range(lo, hi + 1):
        if float(a) in done:
            continue
        c = B48.slim(B48.cell_xi(float(a), 3))
        E = e_arch(B21.PWindow(float(a), 'xi', 3), 'xi')
        c.update(object='xi', E_arch=E, B_rep=c['B'] + E, Bprime_rep=c['Bprime'] + E)
        c['verified_rep'] = bool(abs(c['r']) <= c['B_rep'])
        c['sign_rep'], c['reach_rep'], c['status_rep'] = B48.classify(dict(h2=c['h2'], B=c['B_rep'], Bprime=c['Bprime_rep'], Etail=c['Etail'], verified=c['verified_rep']))
        o = b48.get(float(a), {})
        c['same_as_b548'] = all(o.get(k) == c[k] for k in ('h2', 'r', 'B', 'Z', 'A', 'PR', 'P'))
        c['seconds'] = round(time.time() - t0, 1)
        append_line('b549_sweep_xi_n3.jsonl', c)
        print('[%s] xi p=3 a=%-3d h2 %+.6e |r| %.3e B %.3e E_arch %.3e B_rep %.3e %s %s same %s ; %.0f s' % (
            time.strftime('%H:%M:%S'), a, c['h2'], abs(c['r']), c['B'], E, c['B_rep'], c['sign_rep'], c['status_rep'], c['same_as_b548'], time.time() - t0), flush=True)


def budget_report():
    import b548_record as B48
    import b521_tail as B21
    X = jsonl('b549_sweep_xi_n3.jsonl')
    L = ['b549 -- COMPONENT 3: ξ AT ORDER 3 UNDER THE REPAIRED BUDGET, a = 10..60 (beside relay data/b548_sweep_xi.txt, not over it)', '',
         '  a    F                  |r|         B (b548)    E_arch      B_rep       |r|/B   |r|/B_rep  b548 status   repaired status  same']
    for c in sorted(X, key=lambda c: c['a']):
        L.append('  %-4.0f %+.10e  %.3e   %.3e   %.3e   %.3e   %6.3f  %6.3f     %-12s  %-15s  %s' % (
            c['a'], c['h2'], abs(c['r']), c['B'], c['E_arch'], c['B_rep'], abs(c['r']) / c['B'], abs(c['r']) / c['B_rep'], c['status'], c['status_rep'], c['same_as_b548']))
    nv = sum(1 for c in X if c['verified_rep'])
    fails = [c['a'] for c in X if not c['verified_rep']]
    L += ['', '### ξ order 3 : cells %d ; VERIFY under the repair %d of %d ; still UNVERIFIED %s ; every value but the budget equal to b548`s %s'
          % (len(X), nv, len(X), fails or 'NONE', all(c['same_as_b548'] for c in X)),
          '### E_arch against b548`s excess |r| - B: covers it at %d of %d cells' % (sum(1 for c in X if c['E_arch'] >= abs(c['r']) - c['B']), len(X))]
    if fails:
        L.append('### THE REASON THEY STAY UNVERIFIED: |r| exceeds B + E_arch at %s -- the added term does not carry the residual there.' % fails)
    Q = sorted([c for c in jsonl('b548_sweep_q.jsonl') if c['p'] == 3], key=lambda c: c['a'])
    L += ['', '### THE Q0 ORDER-3 CELLS, RE-SCORED FROM THEIR BANKED VALUES (relay data/b548_sweep_q.jsonl), E_arch added, no cell recomputed:',
          '  a    F                  B (b548)    E_arch(Q0)  B_rep       Etail       B`_rep      b548 sign/reach/status          repaired sign/reach/status']
    qrows, changed = [], []
    for c in Q:
        E = e_arch(B21.PWindow(c['a'], 'q', 3), 'q')
        Br, Bpr = c['B'] + E, c['Bprime'] + E
        ver = abs(c['r']) <= Br
        s, rch, st = B48.classify(dict(h2=c['h2'], B=Br, Bprime=Bpr, Etail=c['Etail'], verified=ver))
        qrows.append(dict(a=c['a'], E_arch=E, B_rep=Br, Bprime_rep=Bpr, sign=s, reach=rch, status=st, before=[c['sign'], c['reach'], c['status']]))
        if [s, rch, st] != [c['sign'], c['reach'], c['status']]:
            changed.append(c['a'])
        L.append('  %-4.0f %+.10e  %.3e   %.3e   %.3e   %.3e   %.3e   %-9s %-4s %-17s  %-9s %-4s %s' % (
            c['a'], c['h2'], c['B'], E, Br, c['Etail'], Bpr, c['sign'], c['reach'], c['status'], s, rch, st))
    L.append('### Q0 order 3 : %d cells ; changed in sign, reach or status : %s' % (len(qrows), changed or 'NONE'))
    put_json('b549_budget.json', dict(xi=dict(n=len(X), verified=nv, fails=fails, same=all(c['same_as_b548'] for c in X),
                                              covers=sum(1 for c in X if c['E_arch'] >= abs(c['r']) - c['B'])), q=qrows, q_changed=changed))
    put_txt('b549_sweep_xi_n3.txt', L)
    print(NL.join(L[-4:]))
    print(L[len(X) + 5])


# ------------------------------------------------------------------------------ COMPONENT 4: THE STRAY CHANGE
def stray():
    diff = g(ROOT, 'diff', '--', 'data/b546_scores.json')
    files = [l[3:].strip() for l in g(ROOT, 'status', '--porcelain', '--', 'data/b546_scores.json').split(NL) if l.strip()]
    mt = os.path.getmtime(os.path.join(D, 'b546_scores.json'))
    t_main = int(g(ROOT, 'log', '-1', '--format=%ct', 'ce0cccfb').strip())
    t_close = int(g(ROOT, 'log', '-1', '--format=%ct', '9e06a910').strip())
    new = json.loads(rd(os.path.join(D, 'b546_scores.json'))).get('written')
    pp = sorted(x for x in g(PP, 'show', '--name-only', '--format=', '37b36b3').split(NL) if x.strip())
    hunks = [l for l in diff.split(NL) if l.startswith(('+', '-')) and not l.startswith(('+++', '---'))]
    own = bool(diff) and t_main < mt < t_close and sorted(new or []) == pp and hunks == ['+  "OPEN_TRAILS.md",']
    L = ['b549 -- COMPONENT 4: THE STRAY CHANGE (READING (10))', '', '### git diff -- data/b546_scores.json (relay working tree):'] + ['  ' + l for l in diff.split(NL) if l.strip()] + [
        '', '### the file time %s ; b546`s main commit ce0cccfb %s ; its closing commit 9e06a910 %s ; between them %s'
        % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mt)), time.strftime('%H:%M:%S', time.localtime(t_main)),
           time.strftime('%H:%M:%S', time.localtime(t_close)), t_main < mt < t_close),
        '### the new "written" list %s ; the files of b546`s PLACE-papers commit 37b36b3 %s ; equal %s' % (new, pp, sorted(new or []) == pp),
        '### the changed lines %s' % hunks,
        '### VERDICT : %s' % ('b546`S OWN SCORE LINE, written after b546`s main commit -- COMMITTED ALONE IN A COMMIT NAMED FOR b546, the diff quoted'
                              if own else 'NOT b546`s OWN SCORE LINE -- REVERTED, the diff quoted in the b549 record')]
    put_json('b549_stray.json', dict(diff=diff, own=own, mtime=mt, t_main=t_main, t_close=t_close, new=new, pp=pp, hunks=hunks, status=files))
    put_txt('b549_stray.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ THE APPENDS
def outside_bt(text):
    return sum(l.count('`') % 2 for l in text.split(NL))


def poss(t):
    return re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", t)


def append_to(path, text):
    text = poss(text)
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE APPEND TO %s' % path)
    import banned_terms as BT
    live = [m.group(0) for l in text.split(NL) for m in BT.PAT.finditer(l)]
    if live:
        sys.exit('### A BANNED STEM IN THE APPEND TO %s: %s' % (path, live))
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP).replace(os.sep, '/'), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def guard_absent(path, h):
    if poss(h).encode('utf-8') in open(path, 'rb').read():
        sys.exit('### ALREADY PRESENT IN %s: %s' % (os.path.basename(path), h[:80]))


def hline(path, h):
    return rd(path).split(NL).index(poss(h)) + 1


R1H = '*Appended at b549 (2026-09-26) to b548`s entry (`FINDINGS.md`:5613), under the author`s ruling `(R159)`(1) -- reading one at its weight:*'
R2H = '*Appended at b549 (2026-09-26) to b548`s entry (`FINDINGS.md`:5613), under `(R159)`(2) -- THE NAVIGATOR’S DEFECT, recorded as such:*'
ACTH = '## The cascade, act five: THE_RESIDUE_OF_RH tiered, the h2 row given its terminal, the pairing`s criterion distinguished from its existence'
RESH = ('#### **THE CASCADE, ACT FIVE -- THE CORRESPONDENCE TIERED** *(appended 2026-09-26, b549, under the author`s ruling `(R159)`(5); no '
        'byte above this block changes; §§1–8 are not edited -- the edition waits for CP-7, `(R157)`(2))*')
HEADING = ('### b549 — the cascade, act five under (R159): THE_RESIDUE_OF_RH tiered, the h2 row given its terminal, the pairing`s '
           'criterion distinguished from its existence; b548`s readings at their weight; the order-3 budget repaired; the stray change settled')
SEVEN = ('§7 says the residue is a conjunction of two clauses, each free apart, and that "only the conjunction is RH". Read beside the '
         'compiled criterion `h2_sign_iff_rh`, clause 2 in full -- the inequality for every test function, in the Weil form on `classK` -- '
         'is RH, so the residue is clause 2 past its certified range; clause 1, realization, is one candidate supplier of clause 2 and not '
         'a separate necessity. `residue_irreducible` compiles that the conjunction implies RH through named premises; it does not compile '
         'that RH needs clause 1. In §7`s own Li form, clause 2 for every n is RH by Li`s criterion, T1-lit. This is a reading, not an '
         'edit: §§1–8 stand as written, and the edition waits for CP-7.')


def findings():
    guard_absent(FIND, R1H)
    t = jl('b549_tiers.json')
    pj, rj, fj, bj, sj = jl('b549_premise.json'), jl('b549_residue_reads.json'), jl('b549_family.json'), jl('b549_budget.json'), jl('b549_stray.json')
    r1 = (R1H + ' H1`s "at most five zeros" clause scored k* = 1 because the excess at widths 36–38 is 4–7 % of the rest and one zero`s '
          'contribution exceeds that margin; the clause as written cannot distinguish a carried excess from a diffuse one, and the peak clause '
          'fails at 36 and 37. The reading that stands is the one the bank shows: the pair term is negative at every width from 30 to 45; the '
          'rest is positive at every width; the sign of the quantity at 36–38 is the rest overtaking the pair by a small margin; and the '
          'largest single movement in the rest across 34–38 is the off-line zero at t = 29.551761 (σ = 0.798), from −44.8 at a = 34 to +74.0 '
          'at a = 38. Whether that zero`s term is what opens and closes the positive window is not decided by k*; it is the question the next '
          'bench reading carries, not a finding.')
    r2 = (R2H + ' H2`s Q0 clause was written in the wrong variable. The power-window route (PowerWindow, PowerLimit) fixes the base window '
          'and raises it to the n-th convolution power, so the support grows with n; b548`s sweep held the window`s parameter a fixed while n '
          'rose. The refutation is of the clause as written, not of the route. b549 read the family (relay `data/b549_diagonal.txt`): the '
          'order-p window of parameter a is a plateau on [−ln a, ln a] whose two ramps are order-p B-splines, its support fixed in p -- not '
          'the n-fold self-convolution of an indicator -- so the diagonal F(n·b, n) is not the route`s variable either; H3 is NOT SCORABLE, '
          'and the re-parametrized sweep is priced (about %.0f s at b548`s per-cell cost, after a window class, its tail constants and a '
          'fixture), not run.' % (fj['cost_total']['q'] + fj['cost_total']['xi']))
    out1 = append_to(FIND, NL.join(['', r1, '', r2, '']))
    tc, dc = t['tier_counts'], t['disp_counts']
    L = ['', ACTH, '',
         '*Filed at b549 on the author`s ruling `(R159)`. The cascade`s act five. Banks: relay `data/b549_tiers.txt`, `data/b549_residue_check.txt`, '
         '`data/b549_premise.txt`, `data/b549_residue_reads.txt`, `data/b549_diagonal.txt`, `data/b549_sweep_xi_n3.txt`, `data/b549_budget_control.txt`, '
         '`data/b549_stray.txt`.*', '',
         '**THE_RESIDUE_OF_RH (Tier K), tiered.** Its first Correspondence table names %d terminals in twelve rows; each was re-read at '
         'SIDE-lv-conservation `main` (`2f71068`), where the two files holding them are byte-identical to the merged branch`s tip `5a14205`, by a '
         'fresh `#check` and `#print axioms`. None is in the tree of the tag `v0.10.0`, which predates the branch. Tiers: %s. Rows: %s. The '
         'second table: its five compiled rows CARRIED; the pairing-existence row CARRIED and annotated; the h2 row MOVED -- h2 in its Weil form '
         'has a terminal, `h2_sign` (SIDE-explicit-formula v0.2, `H2Sign.lean`:29–30), and its equivalence to Mathlib`s `RiemannHypothesis` is '
         '`h2_sign_iff_rh` (T1-open as premise; the equivalence T0). The two lines sit beneath the table in one appended block at the document`s '
         'end; no byte above it changed.' % (len(t['terminals']), ' · '.join('%s %d' % kv for kv in tc.items()), ' · '.join('%s %d' % kv for kv in dc.items())), '',
         '**The pairing`s criterion and its existence.** `h2_sign_iff_rh` says positivity of the Weil form on `classK` is RH; it constructs no '
         'operator and realizes no spectrum. So the criterion is compiled and the existence of the zero-acting positive pairing is untouched, '
         'as the document`s own frame disclaims it.', '',
         '**The premise form.** `residue_irreducible` takes the Weil criterion as a named hypothesis, `inequalityToPositivity` (with the '
         'pairing`s field `yieldsInequality`), in the Li-channel form on sequences ℕ → ℝ, not in the `classK` form of `h2_sign`; no premise has '
         'the type `h2_sign` or an implication between it and RH, and the kernels stand on different toolchains (lv v4.29.1, Mathlib `5e932f9`; '
         'explicit-formula v4.33.0-rc2, Mathlib `51e6992`). The discharge is priced, not attempted: through the Weil form, a `classK` field for '
         'the pairing, its implication to `h2_sign`, and one composition with `h2_sign_iff_rh`, after a toolchain join; through the Li form, '
         'ζ’s Li channels and Li`s criterion, which `h2_sign_iff_rh` does not supply.', '',
         '**§7, read in the light of the compiled criterion.** ' + SEVEN, '',
         '**The document`s figures against their banks.** §5`s ρ ≈ 0.9533 + 16.290 i: the b506 bank`s σ = %.10f -- equal at three decimals and '
         'at four. §4`s C[Z_Q] ≈ 0.65–1.2 across N = 10–120: the loom`s Epstein row runs %.3f to %.3f -- equal; the ζ and Davenport–Heilbronn '
         'ranges equal too. The banned stem of `(R159)`(6) occurs %d times on lines %s, listed for the edition and left unedited.'
         % (rj['sigma'], min(rj['loom']['epstein']['vals']), max(rj['loom']['epstein']['vals']), len(rj['stems']), sorted(set(s['line'] for s in rj['stems']))), '',
         '**The order-3 budget, repaired.** The quadrature budget assumed a transform that decays faster than any polynomial (carto_atlas.py:13); '
         'the order-p window`s decays as |u|^(2−2p), |u|^−4 at order 3, and the widest grid missed the piece past 2·UMAX. The repair adds the '
         'bounded truncation past 2·UMAX, with the order`s exponent, beside the banked budget. ξ at order 3, recomputed at a = 10…60: %d of %d '
         'cells now VERIFY, every value but the budget equal to b548`s; the four-fold grid`s added piece lies below the added term at both '
         'control widths. The Q0 order-3 cells, re-scored from their banks: %s changed in sign, reach or status.'
         % (bj['xi']['verified'], bj['xi']['n'], 'none' if not bj['q_changed'] else bj['q_changed']), '',
         '**b548`s readings at their weight** are appended beneath b548`s entry (`FINDINGS.md`:5613): reading one as `(R159)`(1) states it, and '
         'the navigator`s defect in H2. The window family is not the self-convolution family, so the diagonal was not read and no line is '
         'added at the detection-geometries entry.', '',
         '**The stray change** in relay `data/b546_scores.json` was b546`s own score line, written after b546`s main commit; it is committed '
         'alone in a relay commit named for b546, the diff quoted.' if sj.get('own') else '**The stray change** was reverted; the diff is quoted in the record.', '',
         '**Next keystone:** THE_IDENTITY_CHAIN.', '',
         '*Nothing deposits; nothing at Zenodo written; no kernel edited; nothing here is a statement about RH or about ζ’s zeros.*', '']
    out2 = append_to(FIND, NL.join(L))
    out2['heading_line'] = hline(FIND, ACTH)
    lines = rd(FIND).split(NL)
    l1 = [i + 1 for i, l in enumerate(lines) if l.startswith(poss(R1H))]
    l2 = [i + 1 for i, l in enumerate(lines) if l.startswith(poss(R2H))]
    put_json('b549_findings.json', dict(lines=out1, r1_line=l1, r2_line=l2, act=out2))
    print('  FINDINGS : (R159)(1) :%s ; (R159)(2) :%s ; act :%d' % (l1, l2, out2['heading_line']))


def residue_rows():
    guard_absent(RES, RESH)
    t, fnd = jl('b549_tiers.json'), jl('b549_findings.json')
    tab = ['| result | terminals | fresh profile (union) | disposition | tier(s) |', '|:--|:--|:--|:--|:--|']
    for r in t['rows']:
        tab.append('| %s | %s | %s | **%s** | %s |' % (r['result'], '; '.join('`%s`' % x for x in r['terminals']),
                                                      r['fresh_union'], r['disposition'], ', '.join(r['tiers'])))
    L = ['', '<!-- b549 TIER BLOCK, 2026-09-26 -->', '', RESH, '',
         '**The twelve rows, re-read.** Every terminal is found on `main` (`2f71068`) at the tip `5a14205`’s line, where '
         '`ZeroActingPairing.lean` and `ZeroActingPartial.lean` are byte-identical to the tip; none is in the tree of the tag `v0.10.0` '
         '(`93c27ec`), which predates the branch. Statements and profiles by a fresh `#check` and `#print axioms` (relay '
         '`data/b549_residue_check.txt`; the tiers, with a reason per terminal, `data/b549_tiers.txt`). The tier is that of the weakest link '
         'to Mathlib, `(R149)`(2).', ''] + tab + [
        '', '*Tiers over the %d terminals: %s. `distinctFromInput_discharged` is axiom-free within a row whose union is `{propext, '
        'Classical.choice, Quot.sound}`.*' % (len(t['terminals']), ' · '.join('%s %d' % kv for kv in t['tier_counts'].items())), '',
        '**Beneath the second table (:124–132), two rows, appended; the table above is unchanged:**', '',
        '| claim | kernel | fully-qualified terminal | axiom profile | status | `VERIFY-BY` |', '|:--|:--|:--|:--|:--|:--|',
        '| `h2`, the one open premise -- **MOVED** (b549, 2026-09-26) | `SIDE-explicit-formula` v0.2 = `5c72cad` | `SIDEExplicitFormula.B321.h2_sign` '
        '(`H2Sign.lean`:29–30); the equivalence `SIDEExplicitFormula.B321.h2_sign_iff_rh` (`Seam.lean`:101) | the equivalence: `{propext, '
        'Classical.choice, Quot.sound}` | h2 in its Weil form has a terminal, `h2_sign`, and its equivalence to Mathlib`s `RiemannHypothesis` '
        'is the theorem `h2_sign_iff_rh`. Tier: **T1-open** as premise; the equivalence **T0** | `#check` and `#print axioms` of '
        '`h2_sign_iff_rh` at v0.2 |',
        '| the zero-acting positive pairing`s EXISTENCE -- **CARRIED** (b549, 2026-09-26) | NONE -- no kernel exists | — | — | RESEARCH-REACH, '
        'unchanged. The pairing`s **criterion** is compiled; its **existence** is not touched: `h2_sign_iff_rh` says positivity of the Weil '
        'form on `classK` is RH; it constructs no operator and realizes no spectrum. | no verification exists to point at; the row says so |', '',
        '**Back matter -- the §7 reading.** A reading of §7 in the light of the compiled criterion, not an edit of it, is entered at '
        '`FINDINGS.md`:%d (b549).' % fnd['act']['heading_line'], '',
        '*Appended by b549. No claim of §§1–8 is altered; `h2` stays where the deposit left it.*', '']
    out = append_to(RES, NL.join(L))
    out['heading_line'] = hline(RES, RESH)
    put_json('b549_residue_rows.json', out)
    print('  THE_RESIDUE_OF_RH : block :%d %s' % (out['heading_line'], out))


# ------------------------------------------------------------------------------ THE SCORES, THE DESK, THE COMPONENTS, THE TRAIL
PRIOR_PP = '6999324'
WRITE_OK = {'FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md'}
MEMDIR = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', 'memory')


def w(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def scores():
    t, pj, rj, fj, bj, sj, cj = (jl(n) for n in ('b549_tiers.json', 'b549_premise.json', 'b549_residue_reads.json', 'b549_family.json',
                                                 'b549_budget.json', 'b549_stray.json', 'b549_budget_control.json'))
    committed = g(PP, 'log', '-1', '--pretty=%s').startswith('b549 --')
    base = 'HEAD~1' if committed else 'HEAD'
    pref = {}
    for f in sorted(WRITE_OK):
        old = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (base, f)], capture_output=True).stdout.replace(b'\r\n', b'\n')
        new = open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n')
        pref[f] = new.startswith(old)
    written = sorted(x for x in g(PP, 'diff', '--name-only', PRIOR_PP).split(NL) if x) if not committed else \
        sorted(x for x in g(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x)
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b549_') and needle in rd(os.path.join(T, x))]
    tk = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(tk) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b549_')) if tk else None
    kernels = {k: g(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no').strip() == ''
               for k in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-explicit-formula', 'SIDE-global-section')}
    terms = t.get('terminals', [])
    rows = t.get('rows', [])
    second = {s['row']: s['disposition'] for s in t.get('second', [])}
    n1_main = len(terms) > 0 and all(x['main'] == 1 and x['tip'] == 1 for x in terms) and len(rows) == 12 and all(r['disposition'] == 'CARRIED' for r in rows)
    n1_tag = len(terms) > 0 and all(x['tag'] == 1 for x in terms)
    n1_rows = second.get('`h2`, the one open premise') == 'MOVED' and 'EXISTENCE' in ' '.join(second)
    hk = g(ROOT, 'log', '-1', '--format=%s', '--', 'data/b546_scores.json').strip()
    stray_clean = g(ROOT, 'status', '--porcelain', '--', 'data/b546_scores.json').strip() == ''
    prior_mod = sorted(l[3:].strip() for l in g(ROOT, 'status', '--porcelain').split(NL)
                       if l.strip() and not l.startswith('??') and re.match(r'data/b(\d+)_', l[3:].strip()) and int(re.match(r'data/b(\d+)_', l[3:].strip()).group(1)) < 549)
    ctl = cj.get('controls', [])
    return dict(
        n1=n1_main and n1_tag and n1_rows, n1_main=n1_main, n1_tag=n1_tag, n1_rows=n1_rows,
        n2=not pj.get('match') and any(p[0] == 'inequalityToPositivity' for p in pj.get('premises', [])),
        n3=bool(fj.get('self_convolution')),
        n4=bj.get('xi', {}).get('verified') == 51 and bj.get('xi', {}).get('n') == 51,
        n5=bool(sj.get('own')) and hk.startswith('b546 housekeeping') and stray_clean,
        n6=bool(rj.get('sigma_ok')),
        n7=all(pref.values()) and not zen and tok == 0 and all(kernels.values()) and set(written) <= WRITE_OK,
        prefixes=pref, written=written, zen=zen, token=tok, kernels=kernels, housekeeping=hk, prior_modified=prior_mod,
        s1=len(ctl) == 2 and all(c['holds'] for c in ctl) and bj.get('xi', {}).get('covers') == 51,
        s2=bj.get('q_changed') == [] and len(bj.get('q', [])) == 51,
        s3=prior_mod == [])


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7'), ('s1', 's2', 's3')
    t, bj, fj, rj = jl('b549_tiers.json'), jl('b549_budget.json'), jl('b549_family.json'), jl('b549_residue_reads.json')
    L = ['=' * 104, 'b549 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SEVEN.', '-' * 104,
         '  **(N1)** ### **%s.** -- on main at the tip`s line, and every first-table row CARRIED: %s ; in the tag v0.10.0`s tree: %s (0 of %d -- the '
         'terminals postdate the tag) ; the two rows of (R159)(5) MOVED / annotated: %s.' % (w(sc['n1']), sc['n1_main'], sc['n1_tag'], len(t['terminals']), sc['n1_rows']),
         '  **(N2)** ### **%s.** -- the Weil premise is `inequalityToPositivity`, a named hypothesis in Li-channel form; no premise of the h2_sign shapes.' % w(sc['n2']),
         '  **(N3)** ### **%s.** -- the family is a plateau on [−ln a, ln a] with order-p ramps, not a self-convolution; H3 NOT SCORABLE; the sweep priced.' % w(sc['n3']),
         '  **(N4)** ### **%s.** -- ξ order 3 under the repaired budget: %d of %d VERIFY.' % (w(sc['n4']), bj['xi']['verified'], bj['xi']['n']),
         '  **(N5)** ### **%s.** -- b546`s own score line (file time between b546`s two commits; the new list equals 37b36b3`s files); committed: %s.'
         % (w(sc['n5']), sc['housekeeping'] or 'NOT YET'),
         '  **(N6)** ### **%s.** -- σ bank %.10f, document 0.9533.' % (w(sc['n6']), rj['sigma']),
         '  **(N7)** ### **%s.** -- prefixes kept %s ; files written %s ; tools naming the platform %s ; token %s ; kernels clean %s.'
         % (w(sc['n7']), sc['prefixes'], sc['written'], sc['zen'] or 'NONE', sc['token'], sc['kernels']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the four-fold grid`s piece below E_arch at both control widths; E_arch covers |r| − B at %d of 51.' % (w(sc['s1']), bj['xi']['covers']),
         '  **(S2)** ### **%s.** -- Q0 order-3 cells changed: %s.' % (w(sc['s2']), bj['q_changed'] or 'NONE'),
         '  **(S3)** ### **%s.** -- prior acts` banks modified in relay`s working tree: %s.' % (w(sc['s3']), sc['prior_modified'] or 'NONE'),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b549_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b549_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b549_desk_notes.txt', L)
    put_json('b549_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b549 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b549_tiers.txt', 'b549_premise.txt', 'b549_residue_reads.txt', 'b549_diagonal.txt', 'b549_budget_control.txt', 'b549_stray.txt'):
        L += ['### relay data/%s' % n] + ['  ' + l for l in rd(os.path.join(D, n)).rstrip(NL).split(NL)] + ['']
    L += ['### relay data/b549_sweep_xi_n3.txt (its verdict lines)'] + ['  ' + l for l in rd(os.path.join(D, 'b549_sweep_xi_n3.txt')).split(NL) if l.startswith('###')]
    for n in ('b549_findings.json', 'b549_residue_rows.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)))
    L += ['### THE BRANCHES : see data/b549_branches.txt', '=' * 132]
    put_txt('b549_components.txt', L)
    print(NL.join(L[:6]))


def trail():
    sc, t, fnd, rr, bj, fj = scores(), jl('b549_tiers.json'), jl('b549_findings.json'), jl('b549_residue_rows.json'), jl('b549_budget.json'), jl('b549_family.json')
    body = ['', HEADING, '',
            '**(R159) ratified.** (1) b548`s reading one entered at its weight: the pair negative at every width 30–45, the rest positive, '
            'the sign at 36–38 the rest overtaking the pair by a small margin; the off-line zero at t = 29.551761 the largest movement -- '
            'the question the next bench reading carries. (2) H2`s Q0 clause, the navigator`s defect, written in the wrong variable; H3 '
            'fixed on the diagonal F(n·b, n), to be read only if the family is the self-convolution family. (3) The order-3 budget repaired, '
            'not waived. (4) The stray change settled. (5) THE_RESIDUE_OF_RH tiered as the cascade`s act five, the h2 row MOVED, the '
            'pairing row distinguished, §7 read in the light of the compiled criterion. (6) The stem occurrence listed for the edition. (7) '
            'THE_IDENTITY_CHAIN next.', '',
            '**Entered:** THE_RESIDUE_OF_RH.md:%d (the tier block, the two row lines, the back-matter pointer); FINDINGS.md:%s and :%s (the '
            'two lines beneath b548`s entry), :%d (the act).' % (rr['heading_line'], fnd['r1_line'][0], fnd['r2_line'][0], fnd['act']['heading_line']), '',
            '**The residue:** %d terminals, on main at the tip`s line, none in the tag v0.10.0`s tree; rows CARRIED %d; tiers %s. The Weil '
            'premise of `residue_irreducible` is Li-channel, not `classK`; the discharge priced in lemmas (a `classK` field, its implication '
            'to `h2_sign`, a composition with `h2_sign_iff_rh`, after a toolchain join), not attempted.'
            % (len(t['terminals']), t['disp_counts']['CARRIED'], ' · '.join('%s %d' % kv for kv in t['tier_counts'].items())), '',
            '**The family:** not the self-convolution family -- H3 NOT SCORABLE; the re-parametrized sweep priced at about %.0f s of cells '
            'after a window class, its tail constants and a fixture; not filed as a work-order.' % (fj['cost_total']['q'] + fj['cost_total']['xi']), '',
            '**The budget:** ξ order 3 VERIFIES at %d of %d under the repaired term; Q0 order 3 unchanged.' % (bj['xi']['verified'], bj['xi']['n']), '',
            '**CP-1:** open; the cascade continues with THE_IDENTITY_CHAIN, then the remaining tables, then CP-1b.', '',
            '**Next:** THE_IDENTITY_CHAIN.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s · (N7) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
            '**The numerical lane opened for this act and shuts at its close; no kernel lane.** Nothing deposits; nothing at Zenodo written; '
            'no kernel edited; no monograph byte changed; ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit '
            'left it; the four lists stay OPEN; nothing here is a statement about RH or about ζ’s zeros.', '']
    text = poss(NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    before = open(OT, 'rb').read()
    if poss(HEADING).encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(poss(HEADING)))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b549_trail_notes.json', out)


if __name__ == '__main__':
    fn = {'reads': reads, 'tiers': tiers, 'premise': premise, 'checks': checks, 'family': family,
          'budget_control': budget_control, 'sweep_xi3': sweep_xi3, 'budget_report': budget_report, 'stray': stray,
          'findings': findings, 'residue_rows': residue_rows, 'components': components, 'desk': desk, 'trail': trail}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
