# -*- coding: utf-8 -*-
"""b711_independence.py -- (R321)(3): THE INDEPENDENCE SUPPLEMENT, W-ORD-READING5-INDEPENDENCE (OPEN_TRAILS :15806), at step zero.

### `blobs`: each named terminal's kernel and tag resolved (`git rev-parse <tag>^{commit}`), its file located AT THE TAG by `git grep -l -w`
### (the worklist's file printed beside), the file's blob at the tag written to the scratchpad (this tool's own scratch writes) for the
### Read tool, and the declaration's line in the blob printed -- no source line printed. `write`: data/b711_independence.txt (.json) from the
### blobs: each terminal's statement cut from its blob (the declaration line to the line that opens the proof, `:=` at the line's end or
### ` := by`), its grade from the statement (GRADES below, the seat's reading after the Read tool read each blob at the line) and from
### EXCLUSION_ENGINE's table where it grades it (the row's line and grade cell); the principle's row restated (data/b710_reading5.txt
### :34-:52); T3'' read as Independence's control object; and the search query that missed them at b710 printed beside
### (data/b710_r5_search.txt :70 and :586-:598). Written by the Write tool at b711. Writes only the scratch blobs and the two banks.
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b711_worklist as K   # noqa: E402

NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
PP = K.PP
BLOBS = os.path.join(K.SP, 'b711_indep')
DECL = r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*(theorem|lemma|def|structure|class|abbrev|instance)\s+%s\b'


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def rd(p):
    return open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def _membrane(p):
    """(R321)(2)(ii), standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path), refusing a
    bank the root names once this act's root is appended; the scratch blobs pass."""
    import act_membrane as MEM
    import b711_record as REC
    MEM.guard_path('b711', p, REC.R.ROOT_EXCLUDE)


def short(name):
    return name.split('.')[-1]


def blob_path(kernel, tag, f):
    return os.path.join(BLOBS, '%s__%s__%s' % (kernel, tag, f.replace('/', '__')))


def locate(kernel, tag, name):
    """the tag's commit and every *.lean file at the tag naming `name` as a word: (commit, [files])."""
    repo = 'D:/' + kernel
    rc, c = git(repo, 'rev-parse', '--verify', '--quiet', tag + '^{commit}')
    if rc:
        return None, []
    rc, out = git(repo, 'grep', '-l', '-w', short(name), tag, '--', '*.lean')
    return c.strip(), [l.split(':', 1)[1] for l in out.split(NL) if l.strip()]


def decl_lines(text, name):
    pat = re.compile(DECL % re.escape(short(name)))
    return [i for i, l in enumerate(text.split(NL), 1) if pat.match(l)]


def blobs(*a):
    os.makedirs(BLOBS, exist_ok=True)
    rows = []
    for kernel, tag, f, name in K.INDEPENDENCE_TERMINALS:
        if ' ' in name:
            c, files = locate(kernel, tag, 'x')[0], [f]
        else:
            c, files = locate(kernel, tag, name)
        if not c:
            print('  %-22s %-8s ### THE TAG IS NOT THERE' % (kernel, tag))
            continue
        use = f if f in files or ' ' in name else (files[0] if files else f)
        if ' ' not in name:   # ### the file at the tag that DECLARES the name, where the listed file only names it (interface_split)
            decl_in = [x for x in files if decl_lines(git('D:/' + kernel, 'show', '%s:%s' % (tag, x))[1], name)]
            use = f if f in decl_in else (decl_in[0] if decl_in else use)
        rc, body = git('D:/' + kernel, 'show', '%s:%s' % (tag, use))
        if rc:
            print('  %-22s %-8s %s ### NOT AT THE TAG' % (kernel, tag, use))
            continue
        p = blob_path(kernel, tag, use)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(body.encode('utf-8'))
        os.replace(p + '.tmp', p)
        dl = decl_lines(body, name) if ' ' not in name else []
        rows.append(dict(kernel=kernel, tag=tag, commit=c, name=name, file=use, listed=f, located=files, lines=body.count(NL), decl=dl, blob=p))
        print('  %-22s %-8s %s %-46s %-46s lines %4d ; decl %s ; files naming it %d%s' % (
            kernel, tag, c[:8], name[:46], use[:46], body.count(NL), dl or '-', len(files), '' if use == f else ' ### LOCATED, NOT THE LISTED ' + f))
    with open(os.path.join(BLOBS, 'index.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(rows, indent=1))
    print('### ### **TERMINALS %d ; BLOBS WRITTEN %d UNDER %s.**' % (len(K.INDEPENDENCE_TERMINALS), len(rows), BLOBS))


# ### THE ROWS: (kernel, tag, file, declaration, the hypotheses named (salt-check (c)), the grade read from the statement (EXCLUSION_ENGINE's
# ### vocabulary, :185-:206), EXCLUSION_ENGINE's row line or None, the form in which it bears on Independence or None). The grades are the
# ### seat's reading after the Read tool read each blob at its line (b711 step zero); the EE grade is read from the table's row, not written here.
FACT = 'FACTORIZATION'
SEP = 'SEPARATION'
COMM = 'COMMUTATION'
HYP = 'AS A HYPOTHESIS'
COUNT = 'AS A HAND-SET COUNT'
ROWS = (
    ('SIDE-bijection', 'v0.2.1', 'SIDEBijection/Theorem.lean', 'identity_formation_bijection', 'S : IDSSystem, whose fields distinctness (:124) and noOrphans (:127) are assumed',
     'SHELL at the schema -- screen (b) fires: the conclusion is the conjunction of the two assumed fields (its docstring: "hypothesis-assumed"), the shape of determination_collapse (EE :194); DERIVES (thin) at the concrete instance sideIDS_bijection :237, the fields proved there for the identity on Fin',
     None, HYP),
    ('SIDE-bijection', 'v0.2.1', 'SIDEBijection/Theorem.lean', 'statement_b_distinctness', 'S : IDSSystem ; stage -- the proof is the field S.distinctness stage',
     'SHELL -- screen (b) fires: the paper`s Independence Lemma (IDENTITY_FORMATION_BIJECTION.md :65, Lemma 3.1 :67-:71) compiles as the structure FIELD distinctness (:122-:124, assumed per stage), and this theorem restates the field',
     None, HYP),
    ('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/T3_StepNineBridge.lean', 'T3prime_shared_witness', 'h1 : every coupling of the family satisfied by T1`s Phi (the shared witness, Determination`s supply) ; h2 : mellin Phi (s / 2) ≠ 0',
     'DERIVES (thin) -- existential introduction ⟨Phi, h1, h2⟩; the shared witness is the hypothesis h1, named as such in its docstring',
     None, COMM),
    ('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/T3_StepNineBridge.lean', 'T3doubleprime_general_commutation_fails', 'none',
     'DERIVES -- a countermodel at s = 3: two couplings Φ = f₁ and Φ = f₂ (f₁, f₂ agreeing on Ioi 0, differing at t = -1), each excluding at s through completedRiemannZeta 3 ≠ 0, no Φ satisfying both',
     None, COMM),
    ('SIDE-explicit-formula', 'v0.18', 'SIDEExplicitFormula/Product.lean', 'productLemma_holds', 'none beyond the two configurations (WeilConfig, whose fields carry ef, count, target_iff)',
     'DERIVES -- ProductLemma unfolds (:160-:161) to "∀ C₁ C₂ : WeilConfig, h2_sign_cfg (sum C₁ C₂) ↔ h2_sign_cfg C₁ ∧ h2_sign_cfg C₂"; an equivalence between open statements; its substance the summed explicit formula sum_ef :111 (each zero side summable by its count); the target of the sum is DEFINED as the conjunction (:147), so the factorization is h2_sign_cfg_iff_target read three times (:170)',
     None, FACT),
    ('SIDE-explicit-formula', 'v0.21', 'SIDEExplicitFormula/Schema/Family.lean', 'family_theorem', 'q : ℕ with NeZero q',
     'DERIVES -- an equivalence between open statements (Weil positivity of the family`s summed configuration ↔ GRH_chi at every non-trivial character`s primitive inducer); the Dedekind reading`s two premises named and NOT DISCHARGED (:255-:272)',
     None, FACT),
    ('SIDE-explicit-formula', 'v0.15', 'SIDEExplicitFormula/Schema/Converse.lean', 'h2_sign_cfg_iff_target', 'C : WeilConfig',
     'DERIVES -- its docstring: "An equivalence between open statements; it proves neither"',
     None, FACT),
    ('SIDE-explicit-formula', 'v0.36', 'SIDEExplicitFormula/H2SignWide.lean', 'h2_sign_sum_iff_rh', 'none',
     'DERIVES -- an equivalence between open statements (its head :15: "Nothing here proves RH or h2_sign"); the converse half reads each zero term as the finite sum of |ĥ_i(γ)|² over the summands (:129-:136)',
     None, FACT),
    ('SIDE-li-map', 'v0.1.1', 'LiLinearMap.lean', 'lam_add', 'η η` : Nat → Int ; n : Nat',
     'DERIVES (thin) -- linearity of the Li map over integer-valued streams; the archimedean / pole+Euler split, with real coefficients, is "not an instance compiled here" (its docstring :51-:54)',
     None, FACT),
    ('SIDE-interfaces', 'v0.2.1', 'Interfaces/Kappa.lean', 'kappa_zero_of_no_mechanism', 'h_no_mechanism : ∀ a, P (f a) = P (f a0)',
     'DERIVES -- κ computed as the max of a Fintype response set, zero under no response',
     190, SEP),
    ('SIDE-interfaces', 'v0.2.1', 'Interfaces/ConnectionRequiresStructure.lean', 'parametric_mechanism_theorem', 'h_no_mechanism : ∀ a, P (f a) = P (f a0)',
     'DERIVES -- the statement of kappa_zero_of_no_mechanism, its proof that theorem applied (:46): one result under two names',
     190, SEP),
    ('SIDE-interfaces', 'v0.2.1', 'Interfaces/ConservationProfile.lean', 'interface_split', 'h_nontrivial : ¬ IsAllStructural P',
     'DERIVES -- Finset.card_lt_card on the structural filter; the source-fidelity form with f : A → B reserved for a later kernel (its docstring :104-:106)',
     191, SEP),
    ('SIDE-kernel', 'v1.8', 'Kernel/SilenceTheorem.lean', 'silence_universal', 'h_univ : I.is_universal',
     'DERIVES -- constant action, every factoring measurement constant; the essential field unused; its instances over Unit (:104-:136)',
     189, SEP),
    ('SIDE-kernel', 'v1.8', 'Kernel/Voice3b.lean', 'offLine_of_codim_two', 'h_codim2 : zero_codimension sigma = 2',
     'DERIVES (thin) -- codimension arithmetic; its docstring: "it does NOT use Determination"',
     193, None),
    ('SIDE-simplicity', 'v0.1.2', 'SIDESimplicity/Codimension.lean', 'transversal_generic_empty', 'hcurve : curveDim = 1 ; hcodim : 2 ≤ obstrCodim (integers)',
     'DERIVES (thin) -- integer arithmetic by omega; the analytic Thom transversality delegated (the file head :15-:17)',
     None, COUNT),
    ('SIDE-simplicity', 'v0.1.2', 'SIDESimplicity/Codimension.lean', 'codim_exceeds_curve', 'none -- over the constants numSources := 5 and curveDim := 1 set in the file (:46-:47)',
     'DERIVES (thin) -- 1 < 5 over hand-set constants; the "five independent mechanism-class sources" are the constant numSources (:40-:46)',
     None, COUNT),
    ('SIDE-simplicity', 'v0.1.2', 'SIDESimplicity/Codimension.lean', 'codim_margin', 'h0 : 0 ≤ lost ; h3 : lost ≤ 3',
     'DERIVES (thin) -- 1 < 5 - lost over the hand-set constants',
     None, COUNT),
    ('SIDE-simplicity', 'v0.1.2', 'SIDESimplicity/Codimension.lean', 'margin_fails_at_threshold', 'none',
     'DERIVES (thin) -- ¬ (1 < 1)',
     None, COUNT),
    ('SIDE-simplicity', 'v0.1.2', 'SIDESimplicity/Codimension.lean', 'no_tuning', 'none -- freeParameters := 0 set in the file (:69)',
     'ENCODES-CONCLUSION -- a constant set to the wanted value, proved equal by rfl (the shape of EE :205); its comment: "the kernel records the load-bearing premise", the premise it names "the Independence step" (:61-:67)',
     None, COUNT),
)
SEARCH = 'b710_r5_search.txt'
SEARCH_PAPERS_LINE, SEARCH_KERNELS_LINE, SEARCH_KERNELS_END = 70, 586, 598
CONTROL_POS = 'structure IndependentConstraints (X : Type u) where'   # ### data/b710_r5_search.txt :596, the pattern's own hit (SIDE-kernel Layer1.lean :17)


def cut_statement(text, line):
    """the declaration from its line to the proof's opening `:=`, the `:=` and what follows it dropped; a field's line alone where no `:=` comes
    before the next declaration."""
    L = text.split(NL)
    out = []
    for l in L[line - 1:line + 30]:
        if ':=' in l:
            out.append(l[:l.index(':=')].rstrip())
            break
        out.append(l.rstrip())
    return NL.join(out)


def ee_row(line):
    L = rd(os.path.join(PP, K.EXCLUSION_ENGINE)).split(NL)
    row = L[line - 1]
    cells = [c.strip() for c in row.strip().strip('|').split('|')]
    return row, cells


def write(*a):
    idx = dict(((r['kernel'], r['tag'], r['file']), r) for r in json.loads(rd(os.path.join(BLOBS, 'index.json')) or '[]'))
    out, bad = [], []
    for kernel, tag, f, name, hyps, grade, ee, bear in ROWS:
        b = idx.get((kernel, tag, f))
        text = rd(b['blob']) if b else ''
        dl = decl_lines(text, name)
        if not b or len(dl) != 1:
            bad.append('%s %s %s %s: blob %s, declarations %s' % (kernel, tag, f, name, bool(b), dl))
            continue
        st = cut_statement(text, dl[0])
        eecell = None
        if ee:
            row, cells = ee_row(ee)
            named = short(name) in row
            eecell = dict(line=ee, grade=cells[2] if len(cells) > 2 else '', names_it=named, terminal=cells[0] if cells else '')
            if not named:
                bad.append('%s: EXCLUSION_ENGINE :%d does not name it' % (name, ee))
        out.append(dict(kernel=kernel, tag=tag, commit=b['commit'], file=f, line=dl[0], name=name, statement=st, hypotheses=hyps, grade=grade, ee=eecell, bears=bear))
    # ### T3'' as the control object: its statement carries the bodies of PerClassExcludes (:53) and CombinationsExclude (:58) unfolded
    t3 = idx.get(('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/T3_StepNineBridge.lean'))
    t3text = rd(t3['blob']) if t3 else ''
    T3L = t3text.split(NL)
    per_body = T3L[52].strip() if len(T3L) > 57 else ''
    comb_body = T3L[57].strip() if len(T3L) > 57 else ''
    t3dd = next((r for r in out if r['name'] == 'T3doubleprime_general_commutation_fails'), None)
    flat = ' '.join((t3dd or {}).get('statement', '').split())
    per_in = bool(per_body) and ' '.join(per_body.split()) in flat
    comb_in = bool(comb_body) and ' '.join(comb_body.split()) in flat
    sorry_t3 = [i for i, l in enumerate(T3L, 1) if l.strip().startswith('sorry')]
    # ### the search that missed them: b710's kernel pattern read from its bank, run on each declaration's first line; its own hit the positive control
    S = rd(os.path.join(D, SEARCH)).split(NL)
    kl = S[SEARCH_KERNELS_LINE - 1]
    m = re.search(r"the pattern '(.*)':\s*$", kl)
    kpat = m.group(1) if m else ''
    krx = re.compile(kpat) if kpat else None
    pos = bool(krx and krx.search(CONTROL_POS))
    for r in out:
        first = r['statement'].split(NL)[0].strip()
        r['b710_pattern_hit'] = bool(krx and krx.search(first))
    ppat = S[SEARCH_PAPERS_LINE - 1]
    bears = [r for r in out if r['bears']]
    forms = {}
    for r in bears:
        forms.setdefault(r['bears'], []).append(r['name'])
    L = ['b711 -- STEP ZERO, (R321)(3): THE INDEPENDENCE SUPPLEMENT, W-ORD-READING5-INDEPENDENCE (PLACE-papers OPEN_TRAILS.md :15806) -- EACH NAMED TERMINAL READ AT ITS KERNEL AND TAG (%s)' % utc(), '',
         '### rows are terminal declarations: the kernel at its tag (the tag`s commit) | the file :line AT THE TAG | the statement, cut from the blob at the',
         '### tag to the proof`s `:=` | the hypotheses named (salt-check (c), EXCLUSION_ENGINE.md :181) | the grade read from the statement, in EXCLUSION_ENGINE`s',
         '### vocabulary (its table :185-:206) | the table`s own row and grade where it grades the terminal | the form in which it bears on Independence.',
         '### Each blob written to the scratchpad by tools/b711_independence.py `blobs` (git show <tag>:<file>) and read through the Read tool at its',
         '### line; the grades are the seat`s reading of each statement, no lean run and no #print axioms profile taken on this host (salt-check (d)',
         '### stands at each kernel`s own transcript). The author named fifteen items ((R321)(3)); they expand to %d declarations: the bijection`s' % len(out),
         '### Independence lemma to its field and restatement, the codimension terminals of SIDE-simplicity to its five theorems. EXCLUSION_ENGINE`s',
         '### grades were read at its own pins (:183: SIDE-kernel v1.2, SIDE-interfaces v0.2); the statements here are at the tags the author named.', '']
    for r in out:
        L.append('  %s %s (%s) %s :%d -- %s' % (r['kernel'], r['tag'], r['commit'][:8], r['file'], r['line'], r['name']))
        L += ['      ' + l for l in r['statement'].split(NL)]
        L.append('      HYPOTHESES: %s' % r['hypotheses'])
        L.append('      GRADE (the statement): %s' % r['grade'])
        if r['ee']:
            L.append('      GRADE (EXCLUSION_ENGINE.md :%d, the row naming it %s): %s' % (r['ee']['line'], r['ee']['names_it'], r['ee']['grade']))
        else:
            L.append('      GRADE (EXCLUSION_ENGINE.md): not graded in its table')
        L.append('      BEARS ON INDEPENDENCE: %s' % (r['bears'] or 'NO -- codimension arithmetic, outside the principle'))
        L.append('')
    L += ['### THE CONTROL OBJECT: T3″ (SIDE-lv-conservation v0.10.0 T3_StepNineBridge.lean :%d)' % (t3dd or {}).get('line', 0),
          '  its hypothesis carries PerClassExcludes`s body (:53 "%s") unfolded: %s' % (per_body, per_in),
          '  its conclusion carries CombinationsExclude`s body (:58 "%s") unfolded: %s' % (comb_body, comb_in),
          '  READING: %s' % ('the statement bears it -- per-class exclusion holding (each of C₁, C₂ excludes at s = 3) and the joint conclusion failing (no Φ satisfies both) '
                             'without a shared witness; T3′ (:121) the same conclusion with the shared witness as its hypothesis h1. Independence`s control object at the compiled level: '
                             'the principle`s step from per-class to joint is not free, and T3″ is the compiled proof that it is not' if per_in and comb_in else '### THE STATEMENT DOES NOT CARRY BOTH BODIES'),
          '  beside it, at the tag: the unrestricted bridge T3_perClass_to_combinations (:92) closed by `sorry` at line(s) %s -- the deposit`s own pinned stop (its docstring :106-:108); on main' % (sorry_t3 or 'NONE'),
          '  (d38f3e8c) restated at b648 under (R258)(2) as a `def ... : Prop` whose docstring names T3″ as its refutation and T3′ as its shared-witness form (main`s file :77-:91 read',
          '  through the Read tool; the quarantine map sorry-quarantine-SIDE-lv-conservation README.md :9). Known, not a finding of this act.', '',
          '### THE SEARCH THAT MISSED THEM AT b710 (relay data/b710_r5_search.txt):',
          '  the papers` pattern, :%d: %s' % (SEARCH_PAPERS_LINE, ppat.strip()),
          '  the kernels` pattern, :%d: %s' % (SEARCH_KERNELS_LINE, kpat or '### NOT READ'),
          '  its yield :%d-:%d: 11 declarations in 6 kernels, none of the terminals above' % (SEARCH_KERNELS_LINE, SEARCH_KERNELS_END),
          '  POSITIVE CONTROL: the pattern on its own hit "%s" (:596): %s' % (CONTROL_POS, pos),
          '  the pattern on each terminal`s declaration line: hits %d of %d -- %s' % (
              sum(1 for r in out if r['b710_pattern_hit']), len(out), ', '.join(r['name'] for r in out if r['b710_pattern_hit']) or 'NONE'),
          '  WHY IT MISSED: the pattern reads the declaration`s NAME (independen, euler product, crt, coprime filter); the terminals bear on the principle',
          '  by their statements (a joint criterion as the conjunction of per-component ones, no response under no mechanism, the per-class to joint',
          '  step) and none carries the word in its name. A reach by name cannot test a principle stated by content (relay memory: reach is not argument).', '',
          '### THE PRINCIPLE`S ROW, RESTATED (relay data/b710_reading5.txt (I) :34-:52, its COMPILED cell :39-:44 "DEFINITIONS ALONE"):',
          '  (I) INDEPENDENCE',
          '      STATED: as reading 5 :35-:38 has it, unchanged.',
          '      COMPILED: NOT DEFINITIONS ALONE. Read at their tags, %d of the %d declarations above bear on the principle, in five forms:' % (len(bears), len(out))]
    for fm, desc in ((FACT, 'a joint criterion as the conjunction or the sum of per-component ones (DERIVES; equivalences between open statements, or linearity over integer streams)'),
                     (SEP, 'a channel with no mechanism carries no response (DERIVES, EXCLUSION_ENGINE :189-:191)'),
                     (COMM, 'the per-class to joint step: DERIVES under a shared witness (T3′), REFUTED unrestricted (T3″, the control object)'),
                     (HYP, 'the paper`s Independence Lemma (Lemma 3.1, distinct identities) compiled as an assumed field and its restatement (SHELL by screen (b))'),
                     (COUNT, 'Independence as five hand-set sources and a recorded premise (DERIVES (thin) over constants; no_tuning ENCODES-CONCLUSION)')):
        L.append('          %s (%d): %s -- %s' % (fm, len(forms.get(fm, [])), ', '.join(forms.get(fm, [])), desc))
    L += ['          not bearing (%d): %s' % (len(out) - len(bears), ', '.join(r['name'] for r in out if not r['bears'])),
          '      THE SCOPE: the forms compiled are the principle`s consequences at named objects, each with its premise named; among the declarations',
          '          read here none takes the principle as the corpus states it (E_DIFFICULTY_THEOREM.md :71, the mechanism classes "connected only through',
          '          essential interfaces") as a hypothesis or a conclusion. The SIDE-meta and SIDE-kernel definitions reading 5 located stand beside them.',
          '      MEASURED and CONTROL: as reading 5 :45-:52 has them, unchanged; at the compiled level T3″ added as the control object.', '']
    if bad:
        L += ['### NOT READ: ' + b_ for b_ in bad] + ['']
    ok = not bad and per_in and comb_in and pos and not any(r['b710_pattern_hit'] for r in out)
    L.append('### ### **DECLARATIONS READ %d AT THEIR TAGS (THE AUTHOR`S %d ITEMS) ; BEARING ON INDEPENDENCE %d ; GRADED BY EXCLUSION_ENGINE %d ; T3″ THE CONTROL OBJECT %s ; '
             'THE b710 PATTERN HITS %d OF %d, ITS OWN HIT %s ; NOT READ %d.**' % (
                 len(out), len(K.INDEPENDENCE_TERMINALS), len(bears), sum(1 for r in out if r['ee']), per_in and comb_in,
                 sum(1 for r in out if r['b710_pattern_hit']), len(out), pos, len(bad)))
    if 'dry' in a:
        print(NL.join(L[-40:]))
        return
    for name_, data in (('b711_independence.txt', NL.join(L) + NL),
                        ('b711_independence.json', json.dumps(dict(at=utc(), rows=out, control=dict(per_in=per_in, comb_in=comb_in, sorry_lines=sorry_t3),
                                                                   search=dict(pattern=kpat, positive=pos), bears=len(bears), ok=ok), indent=1, ensure_ascii=False) + NL)):
        p = os.path.join(D, name_)
        _membrane(p)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(data.encode('utf-8'))
        os.replace(p + '.tmp', p)
    print(L[-1])


def blob(kernel, ref, path, *a):
    """`blob <kernel> <ref> <path>`: one file's blob at a ref written to the scratchpad for the Read tool; its line count and the blob's path printed."""
    os.makedirs(BLOBS, exist_ok=True)
    rc, c = git('D:/' + kernel, 'rev-parse', '--verify', '--quiet', ref + '^{commit}')
    rc2, body = git('D:/' + kernel, 'show', '%s:%s' % (ref, path))
    if rc or rc2:
        sys.exit('### %s %s:%s NOT READ (rev-parse %d, show %d)' % (kernel, ref, path, rc, rc2))
    p = blob_path(kernel, ref.replace('/', '_'), path)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(body.encode('utf-8'))
    os.replace(p + '.tmp', p)
    print('  %s %s (%s) %s lines %d -> %s' % (kernel, ref, c.strip()[:8], path, body.count(NL), p))


if __name__ == '__main__':
    fn = {'blobs': blobs, 'blob': blob, 'write': write}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b711_independence.py blobs | blob <kernel> <ref> <path> | write [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
