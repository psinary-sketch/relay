# -*- coding: utf-8 -*-
"""b558_record.py -- CP-1b, THE IMPLICATION PASS: EVERY CITER OF EVERY MOVED TERMINAL READ FOR MEANING; THE EDITION
WORK-LISTS BANKED; THREE SETTLEMENTS; THE SEAT'S MEMORY AND THE MIRROR REFRESHED: THE RECORD, UNDER (R168).
### `python tools/b558_record.py reads | union | citers | extract | readings | settle | maprow | table | credits | editions |
### findings | components | desk | trail`
### The tag, its push and read-back, the commits, pushes, branch commands, the memory rewrite and the mirror build are the
### seat`s. This file deletes nothing.
"""
import io, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b551_record as P  # noqa: E402
DD = 'D:' + os.sep
PP = P.PP
FIND, OT = P.FIND, P.OT
MAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SPIRAL = P.SPIRAL
SP = os.path.join(DD, 'SIDE-silence-principle')
NL = chr(10)
rd, g, append_to, guard_absent, poss, outside_bt = P.rd, P.g, P.append_to, P.guard_absent, P.poss, P.outside_bt
PRIOR_RELAY = 'a922e617'   # ### b557`s closing -- relay`s tip before this act (no housekeeping commit at b557)
PRIOR_PP = 'f8b4a31'       # ### b557`s PLACE-papers commit
B537_PP = 'b7e0c52'        # ### the last PLACE-papers commit before b538: the window b538-b557 is B537_PP..PRIOR_PP
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ------------------------------------------------------------------------------ THE ROSTER (b557`s, by heading)
# ### the sentences of MONO are the monograph`s own (`day1/A_Place_to_Stand.md`); its tier block lives in FINDINGS (:4835).
ROSTER = [('PATHS', 'PATHS_TO_THE_CRITICAL_LINE', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md'),
          ('SIMP', 'SIMPLICITY_OF_RIEMANN_ZEROS', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md'),
          ('SURR', 'THE_UNCONDITIONAL_SURROUND', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md'),
          ('GRH', 'GRH_CASCADE', 'phase1.5/spectral/GRH_CASCADE.md'),
          ('RCURVE', 'R_CURVE_CRITERION', 'phase1.5/rcurve/R_CURVE_CRITERION.md'),
          ('INDEX', 'INDEX_ARITY_AT_THE_CRITICAL_LINE', 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md'),
          ('RESIDUE', 'THE_RESIDUE_OF_RH', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md'),
          ('AMC', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY', 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md'),
          ('FOUND', 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME', 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md'),
          ('TECHNE', 'TECHNE_TOOLKIT', 'phase1.5/method/TECHNE_TOOLKIT.md'),
          ('SILENCE', 'SILENCE_STAGES_DEALIGNMENT', 'phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md'),
          ('LIC', 'EXHAUSTIVENESS_LICENSE', 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md'),
          ('INVAR', 'INVARIANCE_BARRIERS', 'phase1.5/method/INVARIANCE_BARRIERS.md'),
          ('REPARAM', 'REPARAMETERIZATION_BARRIERS_v0_1', 'phase2/method/REPARAMETERIZATION_BARRIERS_v0_1.md'),
          ('EDIFF', 'E_DIFFICULTY_THEOREM', 'phase2/method/E_DIFFICULTY_THEOREM.md'),
          ('ENUMERA', 'ENUMERA', 'phase1.5/method/ENUMERA.md'),
          ('MONO', 'A_Place_to_Stand', 'day1/A_Place_to_Stand.md'),
          ('BALPOS', 'BALANCE_AND_POSITIVITY', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'),
          ('FACES', 'FACES_OF_H2_AT_FINITE_INSTANCE', 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md'),
          ('LEDGER', 'FACES_LEDGER', 'FACES_LEDGER.md'),
          ('IDC', 'THE_IDENTITY_CHAIN', 'phase2/method/THE_IDENTITY_CHAIN.md'),
          ('CENSUS', 'THE_KEYSTONE_CENSUS', 'phase2/method/THE_KEYSTONE_CENSUS.md')]
KEY = {k: (t, p) for k, t, p in ROSTER}


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


# ### `--dry` (the extraction before the seal): every bank goes to the scratch directory named by B558_SCRATCH, not to data/.
DRY = '--dry' in sys.argv
OUTD = os.environ.get('B558_SCRATCH', D) if DRY else D


def put_json(n, obj):
    open(os.path.join(OUTD, n), 'wb').write((json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def put_txt(n, lines):
    open(os.path.join(OUTD, n), 'wb').write((NL.join(lines) + NL).encode('utf-8'))


def ppath(rel):
    return os.path.join(PP, *rel.split('/'))


def at(rev, rel):
    return subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (rev, rel)], capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '')


def ident(n):
    return r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])'


# ------------------------------------------------------------------------------ COMPONENT 2: THE UNION
# ### S1 -- every tier-block row whose disposition cell is MOVED (the 22 blocks at PRIOR_PP, each block from its heading to the
# ### next heading of its level). S2 -- every line ADDED in PLACE-papers between B537_PP and PRIOR_PP (acts b538-b557) whose FORM
# ### is a supersession or correction line: it opens with `SUPERSEDES`, `*Correction`, `**Rectification`, `- rectification:`,
# ### `**A correction`, or carries `A CORRECTION` in its opening italic -- and the register census table`s rows (FINDINGS
# ### :4795-:4799 at PRIOR_PP, b538`s grading, the set the ruling names). A terminal is a backticked name in such a line that
# ### the cascade has tiered or graded: it stands in a tier block`s terminal cell, the census table, or the map`s anchor or
# ### ranked tables. S3 -- the ruling`s own settlements, (R168)(2)(a) and (b).
BLOCKLINES = {'PATHS': 544, 'SIMP': 496, 'SURR': 211, 'GRH': 437, 'RCURVE': 477, 'INDEX': 647, 'RESIDUE': 215, 'AMC': 482,
              'FOUND': 663, 'TECHNE': 569, 'SILENCE': 267, 'LIC': 140, 'INVAR': 718, 'REPARAM': 266, 'EDIFF': 236, 'ENUMERA': 1058,
              'MONO': 4835, 'BALPOS': 668, 'FACES': 190, 'LEDGER': 490, 'IDC': 3170, 'CENSUS': 243}
S2FORM = re.compile(r'^(SUPERSEDES\b|\*Correction\b|\*\*Rectification\b|\*\*A correction\b)|^\*Appended[^*]*A CORRECTION')
# ### a `- rectification:` line (b545) replaces a SENTENCE of its document and quotes whatever terminals that sentence
# ### names; it is not a terminal`s own correction line, so it is printed with its yield and not counted.
RECTF = re.compile(r'^\s*- rectification:')
BT = re.compile(r'`([^`\s]+)`')
NOTNAME = re.compile(r'(\.lean|\.md|\.txt|\.json)$|^[0-9a-f]{7,40}$|^v\d|^Mathlib\.|^\(|:|/|^\d|-')
# ### THE RULING`S NAMED LIST, (R168)(3), as its entries: an entry is in the union when any of its names is. "ch_iff_rh with
# ### ConservationHypothesis" and "h2_sign and h2_sign_iff_rh" are one entry each, as the ruling writes them; "lvh2 false at
# ### re <= 1" is `lv_h2_false_on_strip`, the census`s name (FINDINGS :4799); "the five paired_* lemmas" are GRH_CASCADE :445`s
# ### six `paired_*` names (the row carries six), one entry with grh_structural_exhaustiveness_proved.
RULED = [('not_register1',), ('register5_output_holds',), ('ch_iff_rh', 'ConservationHypothesis'), ('h2_sign', 'h2_sign_iff_rh'),
         ('lv_h2_false_on_strip',), ('conservation_of_spectra',), ('perpendicular_gradients',), ('T2b_mellin_exhaustion',),
         ('h1_complete_at_Phi',), ('T3doubleprime_general_commutation_fails',), ('no_type_d_conspiracies', 'crt_exhaustiveness'),
         ('partialPositivity_finiteRange',),
         ('grh_structural_exhaustiveness_proved', 'paired_reflection_axis_invariant_iff', 'paired_conjugation_real_axis_agree_iff',
          'paired_cr_minimal_codim_axis_iff', 'paired_modular_S_fixed_iff', 'paired_spectral_offset_zero_iff',
          'paired_topological_no_sigma_preference'),
         ('silence_universal',), ('e_difficulty', 'sieve_ceiling'), ('residue_irreducible',), ('mellin_Phi_eq_zero_of_re_le_one',)]


# ### S2b -- THE TIER MOVES IN THE CASCADE`S OWN PER-TERMINAL BANKS: every terminal the banks b539-b557 tier more than once, with
# ### two different tiers (b540`s and b541`s banks tier rows and chapters, not terminals, and are not read here).
def tier_history():
    H = {}

    def add(n, act, tier, src):
        for t in re.split(r',\s*', tier or ''):
            if t.strip():
                H.setdefault(short(n), []).append((act, t.strip(), src))
    d = jl('b539_tiers.json')
    for r in d['ranked'] + d['extra']:
        add(r['terminal'], 'b539', r['tier'], 'THE_LOAD_BEARING_MAP (b539)')
    for r in jl('b545_tiers.json')['rows']:
        for t in r.get('terminals', []):
            add(t['terminal'], 'b545', t['tier'], 'BALPOS :%s' % t['line'])
    for t in jl('b549_tiers.json')['terminals']:
        add(t['terminal'], 'b549', t.get('tier'), 'RESIDUE')
    for t in jl('b550_tiers.json')['rows']:
        add(t['terminal'], 'b550', t.get('tier'), 'IDC')
    for f, act, doc in (('b554_simp_tiers.json', 'b554', 'SIMP'), ('b555_tiers.json', 'b555', 'GRH')):
        for t in jl(f)['terms']:
            add(t['name'], act, t.get('tier'), '%s :%s' % (doc, t['row']))
    for f, act in (('b556_tiers.json', 'b556'), ('b557_tiers.json', 'b557')):
        for k, v in jl(f).items():
            if isinstance(v, dict) and 'terms' in v:
                for t in v['terms']:
                    add(t['name'], act, t.get('tier'), '%s :%s' % (k, t['row']))
    return H


def blocks_at(rev):
    out = {}
    for k, _, rel in ROSTER:
        src = 'FINDINGS.md' if k == 'MONO' else rel
        L = at(rev, src).split(NL)
        i = BLOCKLINES[k] - 1
        lvl = len(re.match(r'^#+', L[i]).group(0))
        j = i + 1
        while j < len(L) and not re.match(r'^#{1,%d} ' % lvl, L[j]):
            j += 1
        out[k] = (src, i + 1, [(n + 1, L[n]) for n in range(i, j)])
    return out


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def vocabulary(bl):
    v = set()
    for k, (src, a, rows) in bl.items():
        for n, l in rows:
            if l.startswith('|') and not l.startswith('|:'):
                for c in cells(l)[1:4]:
                    v.update(x for x in BT.findall(c) if not NOTNAME.search(x))
    F = at(PRIOR_PP, 'FINDINGS.md').split(NL)
    for l in F[4793:4799]:
        v.update(x for x in BT.findall(l) if not NOTNAME.search(x))
    M = at(PRIOR_PP, 'phase1.5/method/THE_LOAD_BEARING_MAP.md').split(NL)
    for l in M:
        if l.startswith('|') and not l.startswith('|:'):
            v.update(x for x in BT.findall(cells(l)[0] if not cells(l)[0].startswith('**') else cells(l)[1]) if not NOTNAME.search(x))
            if len(cells(l)) > 1:
                v.update(x for x in BT.findall(cells(l)[1]) if not NOTNAME.search(x))
    return v


def short(n):
    return n.split('.')[-1]


def added_lines():
    raw = subprocess.run(['git', '-C', PP, 'diff', '--unified=0', B537_PP, PRIOR_PP, '--', '.', ':!*.json'], capture_output=True).stdout.decode('utf-8', 'replace')
    out, f = [], None
    for l in raw.replace(chr(13), '').split(NL):
        if l.startswith('+++ '):
            f = l[6:]
        elif l.startswith('+') and not l.startswith('+++'):
            out.append((f, l[1:]))
    return out


def blame_commit(rel, n):
    r = subprocess.run(['git', '-C', PP, 'blame', '-L', '%d,%d' % (n, n), '--porcelain', PRIOR_PP, '--', rel], capture_output=True).stdout.decode('utf-8', 'replace')
    return r.split(' ')[0][:7] if r else None


def act_of(c):
    s = g(PP, 'log', '-1', '--format=%s', c)
    m = re.match(r'(b\d{3})', s)
    return m.group(1) if m else c


# ### the kernel and pin of each union terminal, as the banks print them (the source named beside each); nothing here decides
# ### membership.
META = {'riemann_hypothesis': ('SIDE-kernel', 'v1.7 = 2957e7d (b556 k1); v1.2-v1.5 carried', 'b556_tiers.json INDEX :369'),
        'h2_sign': ('SIDE-explicit-formula', 'v0.2 = 5c72cad', 'THE_RESIDUE_OF_RH :240 (b549)'),
        'h2_sign_iff_rh': ('SIDE-explicit-formula', 'v0.2 = 5c72cad', 'FINDINGS :4797 (b538)'),
        'no_type_d_conspiracies': ('SIDE-effects', 'a27415d (clean) / c66f3c5 (sorryAx)', 'b556_tiers.json AMC :446'),
        'crt_exhaustiveness': ('SIDE-effects', 'a27415d', 'b555_tiers.json :388'),
        'silence_principle': ('SIDE-silence-principle', 'v0.1.0', 'b557_tiers.json FOUND :628'),
        'silence_universal': ('SIDE-kernel (SilenceTheorem) / SIDE-silence-principle (Universal)', 'v1.2 / HEAD 667c254', 'b557_tiers.json FOUND :625, :628'),
        'sieve_ceiling': ('SIDE-kernel', 'v1.1 -> v1.4 (SCAFFOLDING) -> v1.7', 'b557_tiers.json EDIFF :162'),
        'e_difficulty': ('SIDE-kernel', 'v1.1 -> v1.4 (repaired) -> v1.7', 'b557_tiers.json EDIFF :164'),
        'T3doubleprime_general_commutation_fails': ('SIDE-lv-conservation', 'c8e3d31 -> v0.10.0', 'b545 BALPOS :344; b554 SIMP :448'),
        'register5_output_holds': ('SIDE-explicit-formula', '81ae175', 'FINDINGS :4798 (b538)'),
        'h1_complete_at_Phi': ('SIDE-lv-conservation', 'v0.6.0 = c80bdc2 (cited at SIDE-kernel v1.5 by FACES :180)', 'FACES :205 (b547)'),
        'not_register1': ('SIDE-explicit-formula', '81ae175', 'FINDINGS :4794 (b538)'),
        'ch_iff_rh': ('SIDE-explicit-formula', '81ae175 (identical at v0.2)', 'FINDINGS :4795 (b538)'),
        'register3_of_one_lt_re': ('SIDE-explicit-formula', '81ae175', 'FINDINGS :4796 (b538)'),
        'mellin_Phi_eq_zero_of_re_le_one': ('SIDE-explicit-formula', '81ae175', 'FINDINGS :4799 (b538)'),
        'lv_h2_false_on_strip': ('SIDE-explicit-formula', '81ae175', 'FINDINGS :4799 (b538)'),
        'partialPositivity_finiteRange': ('SIDE-lv-conservation', 'v0.8.0 = 6efa9e5', 'b539 map; b545 BALPOS :345'),
        'conservation_of_spectra': ('SIDE-kernel', 'v1.2 = b1407b2 (v1.7 the same)', 'b557_tiers.json FOUND :634')}
# ### what moved, per terminal, in one clause each, from the line that moved it (cited).
MOVE = {'riemann_hypothesis': ('T2', 'T2', 'called "the reduction" by INDEX :369 and INVARIANCE :499; its premise is RH restated; the compiled reduction of RH is h2_sign_iff_rh (b556, b557)'),
        'h2_sign': ('-', 'T1-open (premise)', 'h2 gains its terminal in the Weil form, h2_sign (THE_RESIDUE_OF_RH :240, b549)'),
        'h2_sign_iff_rh': ('-', 'T0 (the RH-anchor`s head)', 'h2_sign <-> RiemannHypothesis compiled (the census R4, FINDINGS :4797, b538)'),
        'no_type_d_conspiracies': ('T0', 'T2', 'programme-type (StructuralCoupling), GRH_CASCADE :467 (b557); sorryAx at c66f3c5, ADDITIVE_MULTIPLICATIVE :507 (b556)'),
        'crt_exhaustiveness': ('T0', 'T2', 'programme-type (its modular lift), GRH_CASCADE :467 (b557)'),
        'silence_principle': ('T2', 'T2', 'row :628 MOVED with silence_universal, which is absent at the row`s pin v0.1.0 (FOUNDATIONS :672, b557)'),
        'silence_universal': ('T2', 'T2-INTERFACES', 'T2-INTERFACES by the programme-premise clause (FINDINGS :5812, b555); Universal.silence_universal absent at v0.1.0 (FOUNDATIONS :672, b557); its universal register false as stated (not_register1)'),
        'sieve_ceiling': ('T2', 'T2-SHELL', 'SCAFFOLDING by docstring from v1.4; named as the ceiling without that note (E_DIFFICULTY :242, b557)'),
        'e_difficulty': ('T2', 'T2', 'its statement differs at the tag v1.7 from the bullet`s v1.1 (E_DIFFICULTY :244, b557)'),
        'T3doubleprime_general_commutation_fails': ('T2', 'T0', 'a compiled negative (SIMPLICITY :448, b554); BALANCE_AND_POSITIVITY :678 superseded (b555)'),
        'register5_output_holds': ('-', 'T0 (a theorem)', 'R5-output holds outright; the disclaimed face is a theorem (FINDINGS :4798, :4831, b538, b541); OPEN_TRAILS :11042 superseded (b554)'),
        'h1_complete_at_Phi': ('T0', 'T0', 'its pin cell rectified: SIDE-lv-conservation`s, not SIDE-kernel`s (FACES :205, b547); certifies nothing about the zeros (the map :138)'),
        'not_register1': ('-', 'T0', 'R1 as stated is false (FINDINGS :4794, b538)'),
        'ch_iff_rh': ('-', 'T0', 'ConservationHypothesis <-> RiemannHypothesis: Route 3 is RH restated (FINDINGS :4795, b531-b538)'),
        'register3_of_one_lt_re': ('-', 'partial (INTERFACES on lv`s h1)', 'R3 UNDECIDED on the strip; only re s > 1 compiled (FINDINGS :4796, b538)'),
        'mellin_Phi_eq_zero_of_re_le_one': ('-', 'T0', 'lv`s h2 is false at every s with re s <= 1 (FINDINGS :4799, b538)'),
        'lv_h2_false_on_strip': ('-', 'T0', 'lv`s h2 false on the strip (FINDINGS :4799, b538)'),
        'partialPositivity_finiteRange': ('T4', 'T1-lit', 'T1 split: its premises are uncompiled literature (THE_LOAD_BEARING_MAP :144, b540)'),
        'conservation_of_spectra': ('DERIVES (the map`s grade)', 'T2', 'states forall s : Z, (1 : Q) ^ s = 1, a STIPULATION (THE_LOAD_BEARING_MAP :105, b539; (R168)(2)(b))')}


def union():
    bl = blocks_at(PRIOR_PP)
    voc = vocabulary(bl)
    L = ['b558 -- COMPONENT 2: THE INPUT LIST -- THE UNION, COMPUTED BEFORE ANY READING', '',
         '### S1: tier-block rows with disposition MOVED (22 blocks at PLACE-papers %s)' % PRIOR_PP]
    s1, nonterm = {}, []
    for k, (src, a, rows) in bl.items():
        for n, l in rows:
            if l.startswith('|') and re.search(r'\*\*MOVED\b|MOVED \(|-- \*\*MOVED\*\*', l):
                cs = cells(l)
                names = [x for c in cs[1:4] for x in BT.findall(c) if not NOTNAME.search(x) and x in voc]
                act = act_of(blame_commit(src, n))
                if not names:
                    nonterm.append((k, src, n, cs[0][:90], act))
                for x in names:
                    s1.setdefault(short(x), []).append(dict(doc=k, src=src, line=n, row=cs[0][:60], act=act))
                L.append('    %-7s %s:%d  (%s)  %s  -> %s' % (k, src, n, act, cs[0][:60], ', '.join(names) or 'NO TERMINAL'))
    L += ['### S1 rows naming no terminal (printed, not in the union): %d' % len(nonterm)] + ['    %s %s:%d %s (%s)' % x for x in nonterm]
    s2, forms, rect, recty = {}, 0, 0, set()
    for f, l in added_lines():
        if RECTF.search(l):
            rect += 1
            recty.update(short(x) for x in BT.findall(l) if not NOTNAME.search(x) and x in voc)
            continue
        if not S2FORM.search(l):
            continue
        forms += 1
        m = re.match(r'^SUPERSEDES [^`]*? for ((?:`[^`]+`(?:,? (?:and )?)?)+)', l)
        names = BT.findall(m.group(1)) if m else BT.findall(l)
        for x in names:
            if not NOTNAME.search(x) and x in voc:
                s2.setdefault(short(x), set()).add((f, l[:90]))
    F = at(PRIOR_PP, 'FINDINGS.md').split(NL)
    for n in range(4794, 4800):
        cs = cells(F[n - 1])
        for x in BT.findall(cs[4]):
            if not NOTNAME.search(x):
                s2.setdefault(short(x), set()).add(('FINDINGS.md:%d (the census, b538)' % n, cs[0]))
    L += ['', '### S2: supersession/correction-form lines added b538-b557: %d lines, and the census rows FINDINGS :4794-:4799; '
          'terminals named in them that the cascade tiered or graded: %d' % (forms, len(s2))]
    for x in sorted(s2):
        L.append('    %-44s %s' % (x, ' ; '.join(sorted(set(a for a, b in s2[x])))[:150]))
    L.append('### NOT COUNTED: %d `- rectification:` lines (sentence replacements, b545); the terminals they quote: %d -- %s' % (rect, len(recty), ', '.join(sorted(recty))))
    H = tier_history()
    s2b = {n: h for n, h in H.items() if len(set(t for a, t, s in h)) > 1}
    L += ['', '### S2b: tier moves in the cascade`s per-terminal banks (b539, b545, b549, b550, b554-b557): %d terminals banked, %d tiered twice with two tiers' % (len(H), len(s2b))]
    for n, h in sorted(s2b.items()):
        L.append('    %-44s %s' % (n, ' -> '.join('%s %s (%s)' % x for x in h)))
    s3 = {'silence_universal': '(R168)(2)(a)', 'conservation_of_spectra': '(R168)(2)(b)'}
    L += ['', '### S3: the ruling`s settlements: %s' % ', '.join('%s %s' % kv for kv in s3.items())]
    U = sorted(set(s1) | set(s2) | set(s2b) | set(s3), key=str.lower)
    over = [e for e in RULED if not any(x in U for x in e)]
    named = {x for e in RULED for x in e}
    add = [x for x in U if x not in named]
    L += ['', '### ### **THE UNION: %d terminals.** (terminal -- sources -- kernel -- pin -- tier before -> after -- the act and line that moved it)' % len(U)]
    rows = []
    for x in U:
        src = ' + '.join(s for s, S in (('S1', s1), ('S2', s2), ('S2b', s2b), ('S3', s3)) if x in S)
        k, pin, where = META.get(x, ('?', '?', '?'))
        b, a, why = MOVE.get(x, ('?', '?', '?'))
        acts = sorted(set([r['act'] for r in s1.get(x, [])] + [h[0] for h in s2b.get(x, [])][1:] +
                          re.findall(r'b5\d\d', why)))
        rows.append(dict(terminal=x, sources=src, kernel=k, pin=pin, before=b, after=a, moved_by=', '.join(acts), why=why, meta_source=where))
        L.append('    %-40s %-11s %s @ %s ; %s -> %s ; %s -- %s' % (x, src, k, pin, b, a, ', '.join(acts), why))
    L += ['', '### THE NAVIGATOR`S OVER-COUNT (a ruling entry none of whose names is in the union; printed and dropped): %d' % len(over)]
    L += ['    ' + ' / '.join(e) for e in over]
    L += ['### THE ADDITIONS (in the union, named by no ruling entry): %d -- %s' % (len(add), ', '.join(add) or 'none')]
    miss = [x for x in U if x not in META or x not in MOVE]
    L += ['### union terminals with no kernel/pin or move line in this file: %d %s' % (len(miss), miss)]
    put_json('b558_union.json', dict(s1=s1, s2={k: sorted(v) for k, v in s2.items()}, s2b=s2b, s3=s3, union=U, rows=rows,
                                     over=[list(e) for e in over], add=add, nonterm=nonterm, s2_lines=forms, rect_lines=rect,
                                     rect_terms=sorted(recty), banked_terminals=len(H)))
    put_txt('b558_moved_terminals.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 3: THE CITERS
# ### the search patterns: each union terminal by its name (a whole identifier, namespace-free); ALIASES only as the ferry and the
# ### ruling give them -- the ferry`s four ("h2", "Route 3", "Conservation of Spectra", "the reduction"), each put on the terminal
# ### it names, and the ruling`s pairing name `ConservationHypothesis` (R168)(3) on ch_iff_rh. No other alias.
# ### b599, under (R209)(2)(i), the author`s: "Silence Principle" on silence_principle -- the corpus`s own named object, its home
# ### the document that states it, PLACE-papers `phase1.5/structural/SILENCE_FORMAL.md` :43 ("Theorem (Silence Principle)",
# ### REGISTRY 1.5d-2), so that later censuses reach the sentences that name it.
ALIAS = {'h2_sign': [('h2', r'(?<![A-Za-z0-9_])h2(?![A-Za-z0-9_])'), ('the reduction', r'\b[Tt]he reduction\b')],
         'ch_iff_rh': [('ConservationHypothesis', ident('ConservationHypothesis')), ('Route 3', r'\bRoute 3\b')],
         'conservation_of_spectra': [('Conservation of Spectra', r'Conservation of Spectra')],
         'silence_principle': [('Silence Principle', r'Silence Principle')]}
SILENCE_HOME = ('phase1.5/structural/SILENCE_FORMAL.md', 43)
# ### the map`s rows carrying a citing-keystones cell: (A) at :22-:35; the union terminals with such a row.
MAPROW = re.compile(r'^\| (?:\*\*)?(?:\d+|—)(?:\*\*)? \| `([^`]+)`')


def pats(t):
    return [(t, ident(t))] + ALIAS.get(t, [])


def map_rows():
    out = {}
    for i, l in enumerate(rd(MAP).split(NL)[:40]):
        m = MAPROW.match(l)
        if m:
            cs = cells(l)
            out[short(m.group(1))] = dict(line=i + 1, citing=cs[4])
    return out


def blame_file(rel):
    r = subprocess.run(['git', '-C', PP, 'blame', '--line-porcelain', PRIOR_PP, '--', rel], capture_output=True).stdout.decode('utf-8', 'replace')
    out, cur, meta = [], None, {}
    for l in r.split(NL):
        m = re.match(r'^([0-9a-f]{40}) \d+ \d+', l)
        if m:
            cur = m.group(1)[:7]
        elif l.startswith('author-time '):
            meta[cur] = int(l.split()[1])
        elif l.startswith(chr(9)):
            out.append(cur)
    return out, meta


SPLIT = re.compile(r'(?<=[.;!?])\s+(?=[A-Z*_(\"`“§])')


def segments(line):
    s = line.strip()
    if s.startswith('|') or s.startswith('#') or not s:
        return [s]
    return [x for x in SPLIT.split(s) if x.strip()]


def extract():
    U = jl('b558_union.json') if not DRY else json.loads(rd(os.path.join(OUTD, 'b558_union.json')))
    terms = U['union']
    window = set(x[:7] for x in g(PP, 'rev-list', '%s..%s' % (B537_PP, PRIOR_PP)).split())
    acts = {c: act_of(c) for c in window}
    mr = map_rows()
    rows, L = [], ['b558 -- COMPONENT 3: THE CITERS -- EVERY SENTENCE OF THE ROSTER NAMING A UNION TERMINAL OR ITS ALIAS', '',
                   '### the roster: b557`s 22 documents; MONO read in `day1/A_Place_to_Stand.md` (its tier map is in FINDINGS :4835)',
                   '### a line whose last change is a commit of b538-b557 (%s..%s) is the CASCADE`S OWN line; every other line is the '
                   'DOCUMENT`S OWN' % (B537_PP, PRIOR_PP), '']
    import datetime
    for k, title, rel in ROSTER:
        txt = at(PRIOR_PP, rel).split(NL)
        bl, meta = blame_file(rel)
        fence = False
        for i, l in enumerate(txt):
            if l.strip().startswith('```'):
                fence = not fence
                continue
            for s in segments(l):
                for t in terms:
                    hit = [a for a, p in pats(t) if re.search(p, s)]
                    if not hit:
                        continue
                    c = bl[i] if i < len(bl) else None
                    rows.append(dict(id='%s:%d:%d' % (k, i + 1, len(rows)), terminal=t, doc=k, path=rel, line=i + 1, sentence=s,
                                     by=hit, alias=[a for a in hit if a != t], own='CASCADE' if c in window else 'DOCUMENT', commit=c,
                                     act=acts.get(c, ''), date=datetime.datetime.utcfromtimestamp(meta.get(c, 0)).strftime('%Y-%m-%d'),
                                     kind='code' if fence else ('table' if s.startswith('|') else ('heading' if s.startswith('#') else 'prose'))))
    per = {}
    for r in rows:
        per.setdefault(r['terminal'], {}).setdefault(r['doc'], [0, 0])[0 if r['own'] == 'DOCUMENT' else 1] += 1
    L.append('### the map`s rows with a citing-keystones cell, for the union: %s' % (', '.join('%s (:%d, %s)' % (t, mr[t]['line'], mr[t]['citing']) for t in terms if t in mr)))
    L.append('### union terminals with NO such row: %d -- %s' % (len([t for t in terms if t not in mr]), ', '.join(t for t in terms if t not in mr)))
    L.append('')
    for t in terms:
        d = per.get(t, {})
        docs_own = sorted(x for x in d if d[x][0])
        L.append('    %-40s map: %-40s roster documents citing (document`s own lines): %2d %s ; sentences own %d, cascade %d%s' % (
            t, (mr[t]['citing'][:40] if t in mr else 'NO ROW'), len(docs_own), '·'.join(docs_own), sum(v[0] for v in d.values()),
            sum(v[1] for v in d.values()), ('; by alias %s' % ', '.join(a for a, _ in ALIAS[t])) if t in ALIAS else ''))
    own = [r for r in rows if r['own'] == 'DOCUMENT']
    L += ['', '### ### **CITING SENTENCES: %d rows (terminal x sentence); the document`s own %d, the cascade`s own %d; distinct sentences %d.**' % (
        len(rows), len(own), len(rows) - len(own), len(set((r['doc'], r['line'], r['sentence']) for r in rows)))]
    put_json('b558_citers.json', dict(rows=rows, maprows=mr, terms=terms, alias={k: [a for a, _ in v] for k, v in ALIAS.items()}))
    put_txt('b558_citers.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 1: THE SETTLEMENTS
FOUND = ppath('phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md')
L628 = '*Appended 2026-09-29 by b558, under the author`s ruling `(R168)`(2)(a), to the row at :628 (its tier-block row at :672):*'
LSP = '*Appended 2026-09-29 by b558, under the author`s ruling `(R168)`(2)(a), to the Foundations row at :268:*'
LC = '*Appended 2026-09-29 by b558, under the author`s ruling `(R168)`(2)(c), to b557`s record at :11452:*'
LD = '*Appended 2026-09-29 by b558, under the author`s ruling `(R168)`(2)(d), to b557`s record at :11452:*'


def tagread():
    t = rd(os.path.join(D, 'b558_tag_lsremote.txt')).split(NL)
    obj = [l.split()[0] for l in t if l.endswith('refs/tags/v0.2.0')]
    peel = [l.split()[0] for l in t if l.endswith('refs/tags/v0.2.0^{}')]
    loc = [l for l in t if l.startswith('local tag object')]
    lo, lp = (loc[0].split()[3], loc[0].split()[5]) if loc else (None, None)
    return dict(remote_obj=obj[0] if obj else None, remote_peeled=peel[0] if peel else None, local_obj=lo, local_peeled=lp,
                equal=bool(peel and lp and peel[0] == lp), n6=bool(peel and peel[0].startswith('667c254')))


def line_at_end(path, head):
    ls = [i + 1 for i, l in enumerate(rd(path).split(NL)) if l.startswith(poss(head))]
    return ls[-1] if ls else None


def settle():
    tr = tagread()
    if not tr['equal'] or not tr['n6']:
        sys.exit('### THE TAG READ-BACK DOES NOT MATCH: %s' % tr)
    t1 = (L628 + ' `SIDESilencePrinciple.Universal.silence_universal` is declared at SIDE-silence-principle `v0.2.0` (annotated, '
          'tag object `%s`), peeled `%s`; the peeled SHA read back from the remote equals the local. The row`s pin `v0.1.0` '
          'predates the terminal it names and is kept as written.' % (tr['remote_obj'][:7], tr['remote_peeled'][:7]))
    t2 = (LSP + ' SIDE-silence-principle pinned **`v0.2.0`** = `%s` (annotated, tag object `%s`; the peeled SHA read back '
          'from the remote), the pin at which `Universal.silence_universal` is declared (`FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md`:628). '
          'No byte above this line changes.' % (tr['remote_peeled'][:7], tr['remote_obj'][:7]))
    t3 = (LC + ' the no_type_d supersession line at `GRH_CASCADE.md`:467 sits outside the terminal table`s inputs and moves '
          'nothing in it; it stands as the document-level record, and no table action follows: the table carries neither '
          '`no_type_d_conspiracies` nor `crt_exhaustiveness` (relay `data/terminal_table.md`, 0 lines naming either).')
    t4 = (LD + ' the SieveCeiling pin the ferry gave (SIDE-effects `a27415d`) was the navigator`s; the file is SIDE-kernel`s '
          '(`Kernel/Cascade/SieveCeiling.lean`), as b557 read it; the gate named W-6 stands as b557 printed it -- no `sorry`, '
          '`True` or `fun _ => True` at v1.4 or v1.7, the two base terminals SCAFFOLDING by docstring (relay `data/b557_w6.txt`).')
    tt = rd(os.path.join(ROOT, 'data', 'terminal_table.md'))
    n_tt = len([l for l in tt.split(NL) if 'no_type_d' in l or 'crt_exhaustiveness' in l])
    if n_tt:
        sys.exit('### THE TERMINAL TABLE NAMES A no_type_d TERMINAL: %d lines' % n_tt)
    out = []
    for path, head, text in ((FOUND, L628, t1), (SPIRAL, LSP, t2), (OT, LC, t3), (OT, LD, t4)):
        guard_absent(path, head)
        out.append(append_to(path, NL + text + NL))
        out[-1]['line'] = line_at_end(path, head)
    L = ['b558 -- COMPONENT 1: THE SETTLEMENTS, (R168)(2)', '',
         '### (a) the tag: SIDE-silence-principle v0.2.0 -- local tag object %s, peeled %s ; remote (ls-remote) tag object %s, peeled %s'
         % (tr['local_obj'], tr['local_peeled'], tr['remote_obj'], tr['remote_peeled']),
         '### ### **PEELED SHA, REMOTE == LOCAL: %s ; == 667c254: %s**' % (tr['equal'], tr['n6'])]
    for o, text in zip(out, (t1, t2, t3, t4)):
        L += ['', '### %s:%d (%d bytes appended, prefix kept %s)' % (o['file'], o['line'], o['added'], o['prefix']), poss(text)]
    L += ['', '### (b) conservation_of_spectra T2 enters the union as S3 (`data/b558_moved_terminals.txt`).',
          '### the terminal table`s lines naming no_type_d_conspiracies or crt_exhaustiveness: %d' % n_tt]
    put_json('b558_settle.json', dict(tag=tr, appends=out, table_lines=n_tt))
    put_txt('b558_settle.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 4: THE READINGS
VERDICTS = ('STANDS', 'MOVED-IN-MEANING', 'CREDIT')
TITLES = {k: t for k, t, p in ROSTER}
PATHS_ = {k: p for k, t, p in ROSTER}


def load_verdicts():
    import glob
    V = {}
    for f in sorted(glob.glob(os.path.join(D, 'b558_verdicts_*.tsv'))):
        mac = {}
        for l in rd(f).split(NL):
            if not l.strip() or l.startswith('#'):
                continue
            if l.startswith('@'):
                k, v = l.split(chr(9), 1)
                mac[k] = v
                continue
            i, v, r = l.split(chr(9), 2)
            V[i] = (v, mac.get(r, r), os.path.basename(f))
    return V


def readings():
    C = jl('b558_citers.json')
    V = load_verdicts()
    out, bad = [], []
    for r in C['rows']:
        if r['own'] == 'CASCADE':
            v, rdg = 'STANDS', 'the cascade`s own line (%s, `%s`), written at or after the move; STANDS by the declared default.' % (r['act'], r['commit'])
            src = 'DEFAULT'
        else:
            if r['id'] not in V:
                bad.append(r['id'])
                continue
            v, rdg, src = V[r['id']]
        if v not in VERDICTS:
            bad.append(r['id'])
        out.append(dict(r, verdict=v, reading=rdg, source=src))
    if bad:
        sys.exit('### ROWS WITHOUT ONE VERDICT: %d %s' % (len(bad), bad[:10]))
    per_t, per_d = {}, {}
    for r in out:
        per_t.setdefault(r['terminal'], {x: 0 for x in VERDICTS})[r['verdict']] += 1
        per_d.setdefault(r['doc'], {x: 0 for x in VERDICTS})[r['verdict']] += 1
    own = [r for r in out if r['own'] == 'DOCUMENT']
    cnt = lambda rs: {x: sum(1 for r in rs if r['verdict'] == x) for x in VERDICTS}
    L = ['b558 -- COMPONENT 4: THE READINGS -- EVERY CITING SENTENCE x TERMINAL, ONE VERDICT (STANDS / MOVED-IN-MEANING / CREDIT)', '',
         '### the rows: %d ; the documents’ own %d, read by the seat (relay `data/b558_verdicts_<terminal>.tsv`) ; the cascade`s own %d, STANDS '
         'by the declared default' % (len(out), len(own), len(out) - len(own)),
         '### over all rows: %s ; over the documents’ own: %s' % (cnt(out), cnt(own)), '',
         '### PER TERMINAL (all rows ; the documents’ own)']
    for t in C['terms']:
        rs = [r for r in out if r['terminal'] == t]
        L.append('    %-40s %s ; own %s' % (t, cnt(rs), cnt([r for r in rs if r['own'] == 'DOCUMENT'])))
    L += ['', '### PER DOCUMENT (all rows ; the documents’ own)']
    for k, t, p in ROSTER:
        rs = [r for r in out if r['doc'] == k]
        L.append('    %-8s %-40s %s ; own %s' % (k, t, cnt(rs), cnt([r for r in rs if r['own'] == 'DOCUMENT'])))
    L += ['', '### THE TABLE -- terminal | document | line | verdict | the sentence, quoted | the reading', '']
    for r in out:
        L.append('%s | %s | :%d | %s | "%s" | %s' % (r['terminal'], TITLES[r['doc']], r['line'], r['verdict'], r['sentence'], r['reading']))
    put_json('b558_cp1b.json', dict(rows=out, per_terminal=per_t, per_document=per_d, counts_all=cnt(out), counts_own=cnt(own)))
    put_txt('b558_cp1b.txt', L)
    print(NL.join(L[:60]))


# ------------------------------------------------------------------------------ COMPONENT 3 (the map`s rows) AND 4 (the map`s section)
MAPROWH = ('### The terminals CP-1b reads that (A) does not rank -- rows appended 2026-09-29 by b558 under the author`s ruling (R168)(3) '
           '(the ranked list (A) and every byte above are unedited)')
MAPSECH = ('### CP-1b, the implication pass -- the moved terminals’ citers read for meaning, appended 2026-09-29 by b558 under the author`s '
           'ruling (R168)(3) (no byte above changes)')


def clean_quote(s, n=220):
    import banned_terms as BT
    if BT.PAT.search(s):
        return None
    q = s.replace('`', '').replace('|', '/').replace('*', '')
    return q if len(q) <= n else q[:n].rstrip() + ' [...]'


def maprow():
    C, U = jl('b558_citers.json'), jl('b558_union.json')
    mr = C['maprows']
    rows = [x for x in U['rows'] if x['terminal'] not in mr]
    own = [r for r in C['rows'] if r['own'] == 'DOCUMENT']
    L = ['', MAPROWH, '',
         '*One row per union terminal of CP-1b (relay `data/b558_moved_terminals.txt`) for which (A) above has no row. The citing documents are '
         'found by a search of the roster (b557`s, `data/b557_roster.txt`) for the terminal`s name as a whole identifier and for the aliases the '
         'ferry and the ruling give -- "h2" and "the reduction" on `h2_sign`, "Route 3" and `ConservationHypothesis` on `ch_iff_rh` -- counting '
         'lines each document holds as its own (a line last changed by b538-b557 is the cascade`s own and is not counted here). The search, '
         'its patterns and every hit: relay `data/b558_citers.txt`, `data/b558_citers.json`.*', '',
         '| terminal | kernel | pin | tier (before -> after) | citing roster documents (the documents’ own lines) | searched by |',
         '|:--|:--|:--|:--|:--|:--|']
    for x in rows:
        t = x['terminal']
        docs = sorted(set(r['doc'] for r in own if r['terminal'] == t))
        L.append('| `%s` | %s | %s | %s -> %s | %s -- **%d** | %s |' % (
            t, x['kernel'], x['pin'], x['before'], x['after'], ' · '.join(docs) or 'none (named only in the cascade`s own lines)', len(docs),
            'name' + (', ' + ', '.join('"%s"' % a for a in C['alias'].get(t, [])) if t in C['alias'] else '')))
    L += ['', '*Appended by b558. The ranked list (A) is unedited; these rows sit beside it.*', '']
    guard_absent(MAP, MAPROWH)
    o = append_to(MAP, NL.join(L))
    o['line'] = line_at_end(MAP, MAPROWH)
    o['rows'] = [x['terminal'] for x in rows]
    put_json('b558_maprow.json', o)
    print(NL.join(rd(MAP).split(NL)[o['line'] - 1:o['line'] + len(L)]))


def mapsection():
    T_ = jl('b558_cp1b.json')
    rows = T_['rows']
    L = ['', MAPSECH, '',
         '*The full table -- terminal, document, line, the sentence quoted, the verdict and a one-sentence reading, for every citing sentence '
         'of every union terminal on the roster -- is relay `data/b558_cp1b.txt` (%d rows). This section carries its counts and every '
         'MOVED-IN-MEANING and CREDIT row; a quotation here drops its backticks and asterisks and is cut at 220 characters (verbatim in the '
         'bank); a sentence carrying a stem the record`s voice does not use is cited by its line and not quoted.*' % len(rows), '',
         '**Counts.** All rows: %s. The documents’ own: %s. The cascade`s own lines read STANDS by the declared default.' % (
             ' · '.join('%s %d' % kv for kv in T_['counts_all'].items()), ' · '.join('%s %d' % kv for kv in T_['counts_own'].items())), '',
         '| terminal | STANDS | MOVED-IN-MEANING | CREDIT |', '|:--|--:|--:|--:|']
    for t, c in T_['per_terminal'].items():
        L.append('| `%s` | %d | %d | %d |' % (t, c['STANDS'], c['MOVED-IN-MEANING'], c['CREDIT']))
    L += ['', '| document | STANDS | MOVED-IN-MEANING | CREDIT |', '|:--|--:|--:|--:|']
    for k, t, p in ROSTER:
        c = T_['per_document'].get(k, {x: 0 for x in VERDICTS})
        L.append('| %s | %d | %d | %d |' % (t, c['STANDS'], c['MOVED-IN-MEANING'], c['CREDIT']))
    for v in ('CREDIT', 'MOVED-IN-MEANING'):
        L += ['', '**%s** rows:' % v, '']
        for r in rows:
            if r['verdict'] != v:
                continue
            q = clean_quote(r['sentence'])
            L.append('- `%s` -- %s:%d -- %s -- %s' % (r['terminal'], TITLES[r['doc']], r['line'],
                                                    ('*"%s"*' % q) if q is not None else '(not quoted: a stem the record`s voice does not use; verbatim in the bank)',
                                                    r['reading']))
    L += ['', '*Appended by b558. No keystone body is edited; the work-lists are relay `data/b558_editions/`. Nothing deposits.*', '']
    guard_absent(MAP, MAPSECH)
    o = append_to(MAP, NL.join(L))
    o['line'] = line_at_end(MAP, MAPSECH)
    put_json('b558_mapsection.json', o)
    print('### THE_LOAD_BEARING_MAP.md:%d (%d bytes appended, prefix kept %s)' % (o['line'], o['added'], o['prefix']))


# ------------------------------------------------------------------------------ COMPONENT 4: THE CREDITS, IN THE FORM OF FINDINGS :5563
MOVER = {'conservation_of_spectra': ('b539', 'THE_LOAD_BEARING_MAP.md:105 (2026-09-25)', 'the terminal states `forall s : Z, (1 : Q) ^ s = 1`, '
                                     'its conservation reading carried by the namespace, T2 -- the tier b539 set and (R168)(2)(b) settles'),
         'h2_sign': ('b536/b549', 'SIDE-explicit-formula v0.2 = `5c72cad` (b536, 2026-09-25); THE_RESIDUE_OF_RH :240 (b549)',
                     '`h2_sign_iff_rh : h2_sign <-> RiemannHypothesis`, h2 in its Weil form equivalent to RH through a theorem of real content'),
         'ch_iff_rh': ('b531-b532', 'SIDE-explicit-formula `H2Bridge.lean` (b532, 2026-09-25); the census R2 (FINDINGS :4795)',
                       '`ch_iff_rh : conservationHypothesis <-> RiemannHypothesis`, Route 3`s premise RH restated'),
         'T3doubleprime_general_commutation_fails': ('b554/b555', 'SIMPLICITY_OF_RIEMANN_ZEROS :448 (b554); BALANCE_AND_POSITIVITY :678 superseded (b555)',
                                                     'T0 -- a compiled negative about Mathlib`s Mellin transform, against b545`s T2 "logic over abstract couplings"')}
ENTERED = {'BALPOS:274:566'}


def credits():
    T_ = jl('b558_cp1b.json')
    cr = [r for r in T_['rows'] if r['verdict'] == 'CREDIT' and r['id'] not in ENTERED]
    import datetime
    out = []
    for r in cr:
        act, where, what = MOVER[r['terminal']]
        h = '## %s :%d, %s, read against %s: an earlier reading of `%s` held against a later drift' % (TITLES[r['doc']], r['line'], r['date'], act, r['terminal'])
        guard_absent(FIND, h)
        q = clean_quote(r['sentence'], 2000)
        L = ['', h, '',
             '*Filed at b558 on the author`s ruling `(R168)`(3), CP-1b. The document is `%s`; the credit promotes nothing in it and edits no byte of it.*' % PATHS_[r['doc']], '',
             '**The reading, at `%s`:%d (its line last changed %s, commit `%s`):**' % (os.path.basename(PATHS_[r['doc']]), r['line'], r['date'], r['commit']), '',
             '> %s' % (q if q is not None else '(the sentence carries a stem the record`s voice does not use; verbatim in relay `data/b558_cp1b.txt`)'), '',
             '**What the later act showed.** %s, at %s.' % (what[0].upper() + what[1:], where), '',
             '**The relation.** %s' % r['reading'][0].upper() + r['reading'][1:], '',
             '*Nothing deposits; nothing here is a statement about RH.*', '']
        o = append_to(FIND, NL.join(L))
        o['line'] = line_at_end(FIND, h)
        o['id'] = r['id']
        out.append(o)
        print('### FINDINGS.md:%d -- the credit for %s' % (o['line'], r['id']))
    put_json('b558_credits.json', dict(entered=out, already=sorted(ENTERED)))


# ------------------------------------------------------------------------------ COMPONENT 5: THE EDITION WORK-LISTS
def informing(r):
    if r['doc'] == 'GRH':
        return 'W-ORD-GRH-WEIL (the chi-side of the Weil arc; OPEN_TRAILS :11373)'
    if r['terminal'] == 'partialPositivity_finiteRange':
        return 'W-ORD-LI-WEIL-BRIDGE (the Li form made T0; OPEN_TRAILS :11203)'
    if r['terminal'] in ('h2_sign', 'h1_complete_at_Phi'):
        return 'W-ORD-DETECTION-REGION (positivity of h2_sign on bounded windows against an explicit zero-free region; OPEN_TRAILS :11151)'
    return 'none named on the critical path'


POINTER = '*Appended 2026-09-29 by b558, under the author`s ruling `(R168)`(4) -- BACK MATTER, THE EDITION WORK-LIST:*'


def editions():
    T_ = jl('b558_cp1b.json')
    ed = os.path.join(D, 'b558_editions')
    os.makedirs(ed, exist_ok=True)
    out = {}
    for k, t, p in ROSTER:
        rs = [r for r in T_['rows'] if r['doc'] == k and r['verdict'] == 'MOVED-IN-MEANING']
        if not rs:
            continue
        fn = os.path.join(ed, t + '.txt')
        L = ['b558 -- THE EDITION WORK-LIST OF %s (%s) -- AN INPUT TO CP-7`S EDITION, NOT AN EDITION' % (t, p), '',
             '### every sentence of the document read MOVED-IN-MEANING by CP-1b (relay `data/b558_cp1b.txt`), in line order: the line, the '
             'terminal, the sentence quoted, what the compiled fact supports, and the informing work-order where the critical path names one '
             '(OPEN_TRAILS :11407). By (R166)(2), no edition is written before its informing work-orders land or are ruled out of scope for it.', '']
        for r in sorted(rs, key=lambda x: (x['line'], x['terminal'])):
            L += [':%d -- `%s`' % (r['line'], r['terminal']), '    the sentence: "%s"' % r['sentence'],
                  '    what the compiled fact supports: %s' % r['reading'], '    informing work-order: %s' % informing(r), '']
        L.append('### %d sentence-rows (%d distinct lines).' % (len(rs), len(set(r['line'] for r in rs))))
        open(fn, 'wb').write((NL.join(L) + NL).encode('utf-8'))
        target = FIND if k == 'MONO' else ppath(p)
        text = (POINTER + ' %s -- %d sentence-rows read MOVED-IN-MEANING by CP-1b, each with what the compiled fact supports and its informing '
                'work-order, are listed in relay `data/b558_editions/%s.txt`, an input to CP-7`s edition and not an edition%s. No byte above '
                'this line changes.' % (('A_Place_to_Stand`s tier map (`FINDINGS.md`:4835)' if k == 'MONO' else 'This document`s'), len(rs), t,
                                        '; the monograph is not edited' if k == 'MONO' else ''))
        guard_absent(target, POINTER + ' ' + (('A_Place_to_Stand`s') if k == 'MONO' else 'This document`s'))
        o = append_to(target, NL + text + NL)
        o['line'] = line_at_end(target, POINTER)
        out[k] = dict(file='data/b558_editions/%s.txt' % t, rows=len(rs), lines=len(set(r['line'] for r in rs)), pointer=o)
        print('    %-8s %-40s %3d sentence-rows  -> %s:%d' % (k, t, len(rs), o['file'], o['line']))
    none = [k for k, t, p in ROSTER if k not in out]
    print('### documents with no MOVED-IN-MEANING sentence (no work-list): %s' % none)
    put_json('b558_editions.json', dict(lists=out, none=none))


MAPFIX = ('*Appended 2026-09-29 by b558, correcting its own CREDIT row for PATHS_TO_THE_CRITICAL_LINE:240 at :%d in the same act:*')


def mapfix():
    sec = jl('b558_mapsection.json')['line']
    ls = rd(MAP).split(NL)
    row = [i + 1 for i, l in enumerate(ls) if i + 1 > sec and l.startswith('- `ch_iff_rh` -- PATHS_TO_THE_CRITICAL_LINE:240 -- ')]
    if len(row) != 1:
        sys.exit('### THE ROW IS NOT FOUND ONCE: %s' % row)
    h = MAPFIX % row[0]
    text = (h + ' the flag that row cites at FINDINGS :396 is FINDINGS :396 as of 2026-07-17 (written 2026-05-24, commit `3de3c15`); since '
            'b143 it stands at `archive/2026-08-24-ledger-split/FINDINGS-archive-1-entries-through-2026-08-20c.md`:19, and today`s FINDINGS '
            ':396 carries other text. The row above is kept as written; relay `data/b558_cp1b.txt` carries the reading with this provenance.')
    guard_absent(MAP, h)
    o = append_to(MAP, NL + text + NL)
    o['line'] = line_at_end(MAP, h)
    o['row'] = row[0]
    put_json('b558_mapfix.json', o)
    print('### THE_LOAD_BEARING_MAP.md:%d (the row at :%d)' % (o['line'], row[0]))


# ------------------------------------------------------------------------------ READING (1): THE READS, CITED
def reads():
    L = ['b558 -- READING (1): THE READS, CITED BY PATH AND LINE (made before the seal; the face`s (C))', '']
    for k, t, p in ROSTER:
        src = 'FINDINGS.md' if k == 'MONO' else p
        L.append('    the tier block of %-40s %s:%d' % (t, src, BLOCKLINES[k]))
    F = at(PRIOR_PP, 'FINDINGS.md').split(NL)
    for n, what in ((4787, 'the register census'), (5812, 'the tier law`s programme-premise clause'), (5868, 'the tier law`s anchor-scope clause'),
                    (5461, 'the credit BALPOS B.6(4)'), (5527, 'its correction'), (5563, 'the credit FACES §2')):
        L.append('    FINDINGS.md:%-5d %s -- %s' % (n, what, F[n - 1][:110]))
    L.append('    FINDINGS b538-b557 lines carrying a supersession or correction: :4953, :5492, :5527, :5681, :5703, :5713, :5754, :5766, :5842, :5892, :5896')
    M = at(PRIOR_PP, 'phase1.5/method/THE_LOAD_BEARING_MAP.md').split(NL)
    L.append('    THE_LOAD_BEARING_MAP.md entire: %d lines at %s; (A) at :22-:35 (its citing-keystones cell); the appendix from :81; no writer tool' % (len(M), PRIOR_PP))
    L.append('    SIDE-silence-principle: HEAD %s ; tags before this act: v0.1.0 = 5337e1a (peeled 90e540f)' % g(SP, 'rev-parse', '--short', 'HEAD').strip())
    S_ = at(PRIOR_PP, 'SPIRAL_MAP.md').split(NL)
    L.append('    SPIRAL_MAP.md:268 (the Foundations row, live table) -- %s' % S_[267][-160:])
    L.append('    FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md:628 -- %s' % at(PRIOR_PP, 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md').split(NL)[627][:160])
    mem = os.path.join(P.MEMDIR, 'MEMORY.md')
    ml = rd(mem).split(NL)
    L.append('    the seat`s memory file: %s -- %d lines, %d index entries' % (mem, len(ml), sum(1 for l in ml if l.startswith('- ['))))
    L.append('    the mirror-export tool: %s (takes only -DateTag); verify: tools/mirror_verify.py (run from PLACE-papers)' % os.path.join(T, 'mirror_build.ps1'))
    import glob, hashlib, zipfile, datetime
    zs = sorted(glob.glob(os.path.join(DD, 'MY-DOwnloads', 'mirror-refresh-*.zip')), key=os.path.getmtime)
    if zs:
        with zipfile.ZipFile(zs[-1]) as zf:
            mb = zf.read('MANIFEST.md')
        L.append('    the last mirror: %s (written %s) -- MANIFEST.md md5 %s (%d bytes)' % (
            os.path.basename(zs[-1]), datetime.datetime.fromtimestamp(os.path.getmtime(zs[-1])).strftime('%Y-%m-%d %H:%M'), hashlib.md5(mb).hexdigest(), len(mb)))
    put_txt('b558_reads.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 7: THE ENTRY
FH = '## CP-1b, the implication pass: the moved terminals, their citers, the readings and credits; the edition work-lists banked; the refresh'
HEADING = ('### b558 — CP-1b, the implication pass under (R168): the moved terminals, their citers, the readings and credits; the edition '
           'work-lists banked; three settlements; the refresh')


def findings():
    guard_absent(FIND, FH)
    U, T_, st, cr, ed, mp, mr = (jl('b558_union.json'), jl('b558_cp1b.json'), jl('b558_settle.json'), jl('b558_credits.json'), jl('b558_editions.json'),
                                 jl('b558_mapsection.json'), jl('b558_maprow.json'))
    ca, co = T_['counts_all'], T_['counts_own']
    L = ['', FH, '',
         '*Filed at b558 on the author`s ruling `(R168)`. Lane one`s last act: CP-1b. Banks: relay `data/b558_moved_terminals.txt`, '
         '`data/b558_citers.txt`, `data/b558_cp1b.txt`, `data/b558_verdicts_<terminal>.tsv`, `data/b558_editions/`.*', '',
         '**The settlements.** SIDE-silence-principle tagged `v0.2.0` at `667c254` (annotated, tag object `%s`), the peeled SHA read back from the '
         'remote equal to the local; the line at `FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md`:%d; the pin at `SPIRAL_MAP.md`:%d; b557`s record gains '
         'the no_type_d line and the SieveCeiling line at `OPEN_TRAILS.md`:%d and :%d.' % (
             st['tag']['remote_obj'][:7], st['appends'][0]['line'], st['appends'][1]['line'], st['appends'][2]['line'], st['appends'][3]['line']), '',
         '**The moved terminals.** The union of the tier blocks’ MOVED rows, the supersession and correction lines of b538-b557 with the census '
         'rows, the tier moves in the cascade`s per-terminal banks, and the ruling`s two settlements: **%d terminals**. The ruling`s named list '
         'read as its entries: %d over-counted and dropped (%s); %d additions (%s).' % (
             len(U['union']), len(U['over']), '; '.join(' / '.join(e) if len(e) < 3 else e[0] + ' with the paired_* lemmas' for e in U['over']),
             len(U['add']), ', '.join(U['add'])), '',
         '**The citers.** %d rows (terminal x sentence) over the roster; %d are the documents’ own lines, %d the cascade`s. (A) had rows for %d '
         'of the terminals; the other %d gained rows at `THE_LOAD_BEARING_MAP.md`:%d, `h2_sign` among them, its citers by name and alias %d '
         'roster documents.' % (len(T_['rows']), sum(co.values()), sum(ca.values()) - sum(co.values()), len(U['union']) - len(mr['rows']),
                                len(mr['rows']), mr['line'],
                                len(set(r['doc'] for r in T_['rows'] if r['terminal'] == 'h2_sign' and r['own'] != 'CASCADE'))), '',
         '**The readings.** The documents’ own rows: STANDS %d · MOVED-IN-MEANING %d · CREDIT %d; every cascade row STANDS by the declared '
         'default. The table at `THE_LOAD_BEARING_MAP.md`:%d (counts per terminal and per document; every MOVED-IN-MEANING and CREDIT row).' % (
             co['STANDS'], co['MOVED-IN-MEANING'], co['CREDIT'], mp['line']), '',
         '**The credits.** %d entered above this entry (%s), in the form of `FINDINGS.md`:5563; BALANCE_AND_POSITIVITY :274`s clause is the '
         'credit already at :5461 as corrected at :5527, not entered again.' % (len(cr['entered']), ', '.join(':%d' % o['line'] for o in cr['entered'])), '',
         '**The edition work-lists.** %d documents, each with its list in relay `data/b558_editions/` and one pointer line at its end '
         '(A_Place_to_Stand`s in this file, beside its tier map; the monograph is not edited): %s. No MOVED-IN-MEANING sentence, no list: %s. '
         'The lists are inputs to CP-7`s editions and are not editions.' % (
             len(ed['lists']), ', '.join('%s %d' % (TITLES[k], v['rows']) for k, v in ed['lists'].items()), ', '.join(TITLES[k] for k in ed['none'])), '',
         '**The refresh.** After this act`s last push: the seat`s memory rewritten from the ledgers, and the mirror export built by date with the '
         'act suffix; the closing record names both as owed after its own push, and their figures (the memory file`s headings and line counts, the MANIFEST md5 and last-commit) are the closing paste`s.', '',
         '**Next:** W-ORD-DETECTION-REGION, lane two`s first act, with its hypotheses fixed in `(R169)`.', '',
         '*Nothing deposits; nothing at Zenodo written; no `.lean` file edited; no keystone body edited; nothing here is a statement about RH or any zero.*', '']
    o = append_to(FIND, NL.join(L))
    o['line'] = line_at_end(FIND, FH)
    put_json('b558_findings.json', o)
    print(NL.join(rd(FIND).split(NL)[o['line'] - 1:]))


# ------------------------------------------------------------------------------ THE SCORES, THE DESK, THE RECORD
PRE_HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': 'a91d941',
             'SIDE-effects': 'ef4cff7', 'SIDE-silence-principle': '667c254', 'SIDE-compression': 'e9a5a36', 'SIDE-structural-error-correction': '6a4f482',
             'SIDE-cosmo': 'c5cba30'}
COMPILED = re.compile(r'[Cc]ompiled|COMPILED|Lean-verified|verified in Lean|formally verified|machine-verified|DERIVES|provides Conservation|via `ProductFormula')
STIP = re.compile(r'STIPULATION|\(1 : ℚ\) \^ s')


def w_(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def mains():
    return {k: sorted(x for x in g(os.path.join(DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip()) for k, h in PRE_HEADS.items()}


def scores():
    U, T_, C, st, ed, cr = jl('b558_union.json'), jl('b558_cp1b.json'), jl('b558_citers.json'), jl('b558_settle.json'), jl('b558_editions.json'), jl('b558_credits.json')
    rows = T_.get('rows', [])
    own = [r for r in rows if r['own'] == 'DOCUMENT']
    cos = [r for r in own if r['terminal'] == 'conservation_of_spectra']
    cos_docs = sorted(set(r['doc'] for r in cos))
    compiled = [r for r in cos if COMPILED.search(r['sentence']) and not STIP.search(r['sentence'])]
    h2docs = sorted(set(r['doc'] for r in own if r['terminal'] == 'h2_sign'))
    h2alias_docs = sorted(set(r['doc'] for r in own if r['terminal'] == 'h2_sign' and r['alias']))
    credits_beyond = [r['id'] for r in rows if r['verdict'] == 'CREDIT' and r['id'] != 'BALPOS:274:566' and not (r['doc'] == 'FACES' and r['line'] == 39)]
    idc1 = [r['id'] for r in rows if r['doc'] == 'IDC' and r['line'] in (37, 38)]
    moved_docs = sorted(set(v['doc'] for x in U.get('s1', {}).values() for v in x) | set(n[0] for n in U.get('nonterm', [])))
    lists = set(ed.get('lists', {}))
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b558_') and needle in rd(os.path.join(T, x))]
    tk = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(tk) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b558_') and os.path.isfile(os.path.join(d0, f))) if tk else None
    m = mains()
    lean = [(k, f) for k, v in m.items() for f in v if f.endswith('.lean')]
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    trial = dict(head=g(P.TRIAL, 'rev-parse', 'HEAD').strip(), status=g(P.TRIAL, 'status', '--porcelain', '--untracked-files=no').strip())
    sp_head = g(SP, 'rev-parse', 'HEAD').strip()
    h2a = [r for r in own if r['terminal'] == 'h2_sign' and 'h2' in r['by']]
    h2a_m = sum(1 for r in h2a if r['verdict'] == 'MOVED-IN-MEANING')
    return dict(
        n1=len(cos_docs) >= 3 and bool(compiled) and all(r['verdict'] == 'MOVED-IN-MEANING' for r in compiled),
        n1_docs=cos_docs, n1_compiled=[(r['id'], r['verdict']) for r in compiled],
        n2=('h2_sign' not in C.get('maprows', {})) and ('h2_sign' in jl('b558_maprow.json').get('rows', [])) and len(h2alias_docs) > 10,
        n2_docs=h2docs, n2_alias_docs=h2alias_docs,
        n3=bool(credits_beyond), n3_credits=credits_beyond, n3_idc1=idc1,
        n4=all(d in lists for d in moved_docs) and 'ENUMERA' not in lists, n4_moved_docs=moved_docs, n4_missing=[d for d in moved_docs if d not in lists],
        n4_enumera='ENUMERA' in lists,
        n5=bool(U.get('add')), n5_add=U.get('add'),
        n6=bool(st.get('tag', {}).get('n6')) and st['tag'].get('equal'), n6_tag=st.get('tag'),
        n7=not lean and not zen and tok == 0 and dep and trial['head'].startswith('f22ff35') and trial['status'] == '' and sp_head.startswith('667c254'),
        mains=m, zen=zen, token=tok, deposit_clean=dep, trial=trial, sp_head=sp_head,
        s1=T_.get('counts_own', {}).get('MOVED-IN-MEANING', 0) > T_.get('counts_own', {}).get('CREDIT', 0),
        s2=bool(h2a) and h2a_m * 2 < len(h2a), s2_counts=(h2a_m, len(h2a)),
        s3=sum(1 for r in own if r['doc'] == 'ENUMERA' and r['verdict'] == 'MOVED-IN-MEANING') >= 1)


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7'), ('s1', 's2', 's3')
    L = ['=' * 104, 'b558 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SEVEN.', '-' * 104,
         '  **(N1)** ### **%s.** -- conservation_of_spectra`s citing documents (their own lines): %d %s ; the sentences calling it compiled for the '
         'theorem (a compile word, no printed stipulation), with their verdicts: %s.' % (w_(sc['n1']), len(sc['n1_docs']), sc['n1_docs'], sc['n1_compiled']),
         '  **(N2)** ### **%s.** -- (A) had no h2_sign row at the start and the map gained one; citing documents %d, by alias %d: %s.' % (
             w_(sc['n2']), len(sc['n2_docs']), len(sc['n2_alias_docs']), sc['n2_alias_docs']),
         '  **(N3)** ### **%s.** -- CREDIT rows beyond BALPOS B.6(4) and FACES §2: %s ; IDENTITY_CHAIN §1`s sentence ("A ZERO-SORRY FILE OVER FREE '
         'PARAMETERS CONSTRAINS NOTHING", THE_IDENTITY_CHAIN.md:37-38) is a citer of no union terminal -- rows at :37-:38: %s -- file E`s '
         'terminal was tiered once (T2 ENCODES, b550) and moved in no bank, so the navigator`s example lies outside the union.' % (
             w_(sc['n3']), sc['n3_credits'], sc['n3_idc1'] or 'NONE'),
         '  **(N4)** ### **%s.** -- roster documents with a MOVED row in their tier block: %s ; without a work-list: %s ; ENUMERA has a work-list: %s '
         '(its h2 closure lines read MOVED-IN-MEANING).' % (w_(sc['n4']), sc['n4_moved_docs'], sc['n4_missing'] or 'NONE', sc['n4_enumera']),
         '  **(N5)** ### **%s.** -- the additions: %s.' % (w_(sc['n5']), sc['n5_add']),
         '  **(N6)** ### **%s.** -- v0.2.0 peeled (remote) %s ; local %s.' % (w_(sc['n6']), (sc['n6_tag'] or {}).get('remote_peeled'), (sc['n6_tag'] or {}).get('local_peeled')),
         '  **(N7)** ### **%s.** -- (before the commit) mains changed %s ; tools naming the platform %s ; token %s ; deposit clean %s ; trial %s ; '
         'SIDE-silence-principle HEAD %s. ### The mirror`s time against the last push: OWED to the refresh after the last push (the closing paste).' % (
             w_(sc['n7']), {k: v for k, v in sc['mains'].items() if v} or 'NONE', sc['zen'] or 'NONE', sc['token'], sc['deposit_clean'], sc['trial'], sc['sp_head'][:7]),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the documents’ own: %s.' % (w_(sc['s1']), jl('b558_cp1b.json').get('counts_own')),
         '  **(S2)** ### **%s.** -- rows found by the alias "h2": MOVED-IN-MEANING %d of %d.' % (w_(sc['s2']), sc['s2_counts'][0], sc['s2_counts'][1]),
         '  **(S3)** ### **%s.** -- ENUMERA.' % w_(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in N].count(None),
            [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b558_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b558_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b558_desk_notes.txt', L)
    put_json('b558_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b558 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b558_reads.txt', 'b558_settle.txt', 'b558_moved_terminals.txt', 'b558_citers.txt'):
        if os.path.exists(os.path.join(D, n)):
            L += ['### relay data/%s' % n] + ['  ' + l for l in rd(os.path.join(D, n)).rstrip(NL).split(NL)] + ['']
    L += ['### relay data/b558_cp1b.txt (its head; the table follows it there)'] + ['  ' + l for l in rd(os.path.join(D, 'b558_cp1b.txt')).split(NL)[:52]] + ['']
    for n in ('b558_maprow.json', 'b558_mapsection.json', 'b558_mapfix.json', 'b558_credits.json', 'b558_editions.json', 'b558_findings.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)[:3000]))
    L += ['### THE TAG READ-BACK : data/b558_tag_lsremote.txt', '=' * 132]
    put_txt('b558_components.txt', L)
    print(NL.join(L[:6]))


def trail():
    sc = scores()
    U, T_, st, cr, ed, fj, mr, mp = (jl('b558_union.json'), jl('b558_cp1b.json'), jl('b558_settle.json'), jl('b558_credits.json'), jl('b558_editions.json'),
                                     jl('b558_findings.json'), jl('b558_maprow.json'), jl('b558_mapsection.json'))
    co = T_['counts_own']
    body = ['', HEADING, '',
            '**(R168) ratified.** (1) CP-1 closed as b557 declared it. (2) The settlements: (a) SIDE-silence-principle tagged v0.2.0 at 667c254; '
            '(b) conservation_of_spectra T2, its "Compiled" citers CP-1b`s; (c) the no_type_d line moves nothing in the terminal table; (d) the '
            'SieveCeiling pin a27415d the navigator`s. (3) CP-1b run. (4) The edition work-lists banked, not written. (5) The refresh at close. '
            '(6) The act after is W-ORD-DETECTION-REGION.', '',
            '**Entered:** FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md:%d (the tag line); SPIRAL_MAP.md:%d (the pin); OPEN_TRAILS.md:%d and :%d (the (c) '
            'and (d) lines to b557`s record); THE_LOAD_BEARING_MAP.md:%d (the rows), :%d (the CP-1b section) and :%d (its same-act line); '
            'FINDINGS.md %s (the credits) and :%d (the entry); the pointer lines at %s.' % (
                st['appends'][0]['line'], st['appends'][1]['line'], st['appends'][2]['line'], st['appends'][3]['line'], mr['line'], mp['line'],
                jl('b558_mapfix.json')['line'], ', '.join(':%d' % o['line'] for o in cr['entered']), fj['line'],
                '; '.join('%s:%d' % (v['pointer']['file'], v['pointer']['line']) for v in ed['lists'].values())), '',
            '**The union:** %d terminals; over-counted %d; additions %s. **The citers:** %d rows, the documents’ own %d. **The readings, the '
            'documents’ own:** STANDS %d · MOVED-IN-MEANING %d · CREDIT %d. **The work-lists:** %d documents.' % (
                len(U['union']), len(U['over']), ', '.join(U['add']), len(T_['rows']), sum(co.values()), co['STANDS'], co['MOVED-IN-MEANING'],
                co['CREDIT'], len(ed['lists'])), '',
            '**Next:** W-ORD-DETECTION-REGION, under (R169).', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s · (N7) %s before the commit, its mirror clause owed to the closing.** '
            'The seat`s own: (S1) %s, (S2) %s, (S3) %s.' % tuple(w_(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
            '**No kernel lane opened at this act; one tag written (SIDE-silence-principle v0.2.0), no build, no elaboration.** Nothing deposits; '
            'nothing at Zenodo written; no `.lean` file edited; no monograph byte changed; no keystone body edited; ERRATA untouched; the ceiling '
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
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(poss(HEADING)),
               line=line_at_end(OT, HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading, at :%(line)s' % out)
    put_json('b558_trail_notes.json', out)


if __name__ == '__main__':
    fn = {'reads': reads, 'union': union, 'extract': extract, 'settle': settle, 'readings': readings, 'maprow': maprow, 'table': mapsection,
          'credits': credits, 'editions': editions, 'mapfix': mapfix, 'findings': findings, 'components': components, 'desk': desk, 'trail': trail}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
