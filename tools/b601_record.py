# -*- coding: utf-8 -*-
"""b601_record.py -- THE ACT'S RECORD TOOL, UNDER (R211). ### ONE SUBCOMMAND PER BANK.

### ### b601: LANE THREE, ACT TWENTY-EIGHT -- THE DOUBLING COROLLARY (THE SCHEMA'S POSITIVITY WITHOUT SIMPLICITY);
### W-ORD-KEIPER-FACE (THE TWO LEMMAS STATED AND PROVED OR CARRIED TO NAMED OBLIGATIONS).
### Subcommands write only `data/b601_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode, temp file, `os.replace`). No platform call. The template is b600_record.py (the kernel modules, their
### prints, the E0 read, the federation walk, the node list and the pages, the record lines, the scores, the record).
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
MLK = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
PRE_PP = '9473594'
PRE_RELAY = '99e42469'
PRE_KER = '1dd5cd7'
STEPZERO = '5a95a152'
TAG = 'v0.19'
BRANCH = 'doubling-keiper-b601'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/5dce8424-ec16-4701-8f42-69078426fd40/scratchpad'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/5dce8424-ec16-4701-8f42-69078426fd40.jsonl'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
KFILES = dict(doub='SIDEExplicitFormula/Doubling.lean', sdoub='SIDEExplicitFormula/SaltCheckDoubling.lean',
              keip='SIDEExplicitFormula/Keiper.lean', kbnd='SIDEExplicitFormula/KeiperBounds.lean',
              skeip='SIDEExplicitFormula/SaltCheckKeiper.lean')
KNS = dict(doub='SIDEExplicitFormula.Doubling.', sdoub='SIDEExplicitFormula.Doubling.SaltCheck.', keip='SIDEExplicitFormula.Keiper.',
           kbnd='SIDEExplicitFormula.KeiperBounds.', skeip='SIDEExplicitFormula.Keiper.SaltCheck.')
AXF = dict(doub='AxiomCheckDoubling.lean', keip='AxiomCheckKeiper.lean')
AX_KEYS = dict(doub=('doub', 'sdoub'), keip=('keip', 'kbnd', 'skeip'))
OWN = ('AxiomCheckDoubling.lean', 'AxiomCheckKeiper.lean', 'SIDEExplicitFormula/Doubling.lean', 'SIDEExplicitFormula/Keiper.lean',
       'SIDEExplicitFormula/KeiperBounds.lean', 'SIDEExplicitFormula/SaltCheckDoubling.lean', 'SIDEExplicitFormula/SaltCheckKeiper.lean')
DN, KN, BN = KNS['doub'], KNS['keip'], KNS['kbnd']
DOUB_NODES = [DN + 'DoublingCorollary', DN + 'doubling_holds', DN + 'PositivityImpliesSimplicity', DN + 'positivity_not_imp_simplicity']
KEIP_NODES = [KN + 'stieltjes', KN + 'KeiperTaylor', KN + 'KeiperTaylorIdentity', KN + 'KeiperObligations', KN + 'keiperTaylorIdentity_of',
              KN + 'keiperTaylor_zero', KN + 'liCoeff_one_keiper', BN + 'KeiperBounds', BN + 'BoundPremises', BN + 'keiperBounds_of']
NEW_NODES = KEIP_NODES + DOUB_NODES
LI_ANCHOR = 'SIDEExplicitFormula.LiCriterionBridge.li_nonneg_iff_rh | kernel | listed'
SALT_D = [KNS['sdoub'] + n for n in ('doubling_satisfiable', 'doubling_not_forced', 'positivity_with_simplicity')]
SALT_K = [KNS['skeip'] + n for n in ('keiperTaylor_zero_holds', 'split_needs_inv_s', 'split_needs_zeta', 'split_needs_gammaR',
                                     'bounds_form_satisfiable', 'bounds_form_refutable')]
STD3 = ['propext', 'Classical.choice', 'Quot.sound']
SIMP = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md'
BALPOS = 'phase1.5/spectral/BALANCE_AND_POSITIVITY_v0_9_5.md'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))
    return b


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def jl(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def flat(t):
    return ' '.join(t.split())


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) THE SEAT`S G-DOUBLED-TOY PREDICATE WAS DEFECTIVE AS SEALED, CAUGHT BEFORE ANY RUN OVER THE BANK: it looked for "= 2" on the '
    'first line of the #check of doubledToy_mult_pt, and Lean prints that statement wrapped over three lines (relay '
    'data/b601_prints_doub.txt), so the arm would have failed on a true print. The predicate corrected through the Edit tool to read '
    'the whitespace-joined #check up to the next #check and require it to be the statement exactly; the arm list unchanged.',
    '(b) THE SEAT`S N5 SCORER WAS DEFECTIVE AT ITS FIRST RUN: the trail record is this act`s only OPEN_TRAILS write and it follows the '
    'scores, so the file-set predicate, carried from b600 (whose ledger lines preceded its scores), required OPEN_TRAILS.md changed and '
    'scored REFUTED on a true file set (PLACE-papers [FINDINGS.md, the ζ page]) -- the trap b598 logged. The predicate corrected through '
    'the Edit tool to accept the pending append by name; the scores re-run whole.',
    '(c) THE SEAT`S G-E0-GATES PREDICATE WAS DEFECTIVE AT THE FIRST PRE-PUSH RUN: it required each E0 read`s branch tip to be the tag, '
    'but the components were committed in their order and the doubling files` reads were taken at their own tip 2b8abf5, before the '
    'Keiper commit 5fc0c87 = v0.19; their blobs at 2b8abf5 and at v0.19 are identical (Doubling.lean 79393f8c, SaltCheckDoubling.lean '
    'b42f1c12). The predicate corrected through the Edit tool to require each read file`s blob at its read tip to equal its blob at the '
    'tag; the suite re-run whole.',
    '(d) THE HOUSE FORM`S MARK WRAPS IN TWO KERNEL FILES, AND THE SEAT`S G-HOUSE-FORM NEEDLE COULD NOT SEE ACROSS THE WRAP: '
    'Keiper.lean and KeiperBounds.lean carry "NOT VENDORED" broken over a line end of their head comment (b600`s files carry it on one '
    'line), and the arm`s single-line needle failed on them. The files are tagged and stand; the needle corrected through the Edit tool '
    'to read the head comment whitespace-joined (the needle-wrapping lesson); the suite re-run whole.',
    '(e) THE AXIOM AUDIT AxiomCheckKeiper.lean OMITS THE #check OF TWO SALT-CHECK THEOREMS, keiperTaylor_zero_holds and '
    'bounds_form_satisfiable (both are #print-axioms-printed at the standard three, and their statements are those of '
    'keiperTaylor_zero and stieltjes_zero_coarse, whose #check is printed). G-SALT-CHECK, as sealed, reads "each #check printed" '
    'and FAILS in its letter; the file is at the tag v0.19 and is not re-tagged; the arm is not weakened. The suite stands NOT CLEAN '
    'on that arm alone, for the author.',
]


def defects():
    put_txt('b601_defects.txt', ['### b601 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
READS = [
    ('SIDE-explicit-formula v0.18 Product.lean: sum_ef, sum, ProductLemma, productLemma_holds', EFK, 'v0.18', 'SIDEExplicitFormula/Product.lean',
     [111, 142, 143, 144, 145, 146, 147, 148, 160, 161, 169, 170]),
    ('SIDE-explicit-formula v0.18 SaltCheckProduct.lean: the salt check`s two configurations and three theorems', EFK, 'v0.18',
     'SIDEExplicitFormula/SaltCheckProduct.lean', [33, 39, 47, 53, 58]),
    ('SIDE-explicit-formula v0.17 Simplicity.lean: the simplicity Prop and its configuration form', EFK, 'v0.17', 'SIDEExplicitFormula/Simplicity.lean',
     [27, 31, 34]),
    ('SIDE-explicit-formula v0.17 SaltCheckSimplicity.lean: b596`s on-line toy and its two theorems', EFK, 'v0.17',
     'SIDEExplicitFormula/SaltCheckSimplicity.lean', [33, 84, 85, 86, 92, 100, 107]),
    ('PLACE-papers OPEN_TRAILS: W-ORD-KEIPER-FACE located by name -- its row (:11704) and its re-price (:12132), whole; the generator-run '
     'line and b600`s lines', PP, PRE_PP, 'OPEN_TRAILS.md', [11704, 12132, 12288, 12352, 12354, 12356, 12358], 6000),
    ('PLACE-papers FINDINGS: the entry that priced the Keiper face (b589, :6718), its research items (:6728), its weight (:6738); b600`s entry',
     PP, PRE_PP, 'FINDINGS.md', [6718, 6728, 6738, 6950], 6000),
    ('relay the Keiper read`s bank: the re-price, the kernel`s derivative form, the price, the trigger', RELAY, 'HEAD',
     'data/b589_keiper_read.txt', [1, 169, 170, 171, 172, 173], 4000),
    ('Mathlib at the pin de5ce8a9: riemannZeta_residue_one', MLK, 'HEAD', 'Mathlib/NumberTheory/LSeries/RiemannZeta.lean', [90, 139, 242]),
    ('Mathlib at the pin: the limit to γ, ζ(1), Λ₀(1), riemannZeta₀ and riemannZeta₁', MLK, 'HEAD', 'Mathlib/NumberTheory/Harmonic/ZetaAsymp.lean',
     [342, 418, 435, 531, 532, 533, 535, 536, 539, 542, 551, 569]),
    ('Mathlib at the pin: Γℝ`s derivative at 1', MLK, 'HEAD', 'Mathlib/NumberTheory/Harmonic/GammaDeriv.lean', [205]),
    ('Mathlib at the pin: Γℝ(1)', MLK, 'HEAD', 'Mathlib/Analysis/SpecialFunctions/Gamma/Deligne.lean', [77]),
    ('Mathlib at the pin: Euler`s γ and its two bounds', MLK, 'HEAD', 'Mathlib/NumberTheory/Harmonic/EulerMascheroni.lean', [128, 167, 171]),
    ('SIDE-explicit-formula v0.18 vendored Bulka: phi, logDeriv, taylorCoeff, riemannXi', EFK, 'v0.18', 'Vendored/Bulka/Lc/LiCriterion/Basic.lean',
     [395, 409, 410, 541, 542, 1252, 1253]),
    ('SIDE-explicit-formula v0.18 LiCriterionBridge.lean: the equality lemma and the composed criterion', EFK, 'v0.18',
     'SIDEExplicitFormula/LiCriterionBridge.lean', [149, 150, 179]),
    ('PLACE-papers the ζ page at v0.18: li_identity_sym, li_coeff_eq_taylorCoeff, li_nonneg_iff_rh, arith_limit, register4 iff, the five '
     'Product nodes, the faces` multiplicity paragraph', PP, PRE_PP, PAGE, [1, 3, 20, 22, 24, 25, 28, 35, 36, 37, 38, 39, 174], 1200),
    ('relay b600`s bearing bank, whole', RELAY, 'HEAD', 'data/b600_bearing.txt', list(range(1, 13)), 3000),
    ('relay b600`s closing push-out, committed at step zero', RELAY, 'HEAD', 'data/b600_closing_push_out.txt', list(range(1, 18))),
    ('PLACE-papers the bearing candidates: SIMPLICITY v1.1.3 :82 and :180', PP, PRE_PP, SIMP, [82, 180], 4000),
    ('PLACE-papers the bearing candidates: BALANCE_AND_POSITIVITY v0.9.5 :97, :189, :195, :308', PP, PRE_PP, BALPOS, [97, 189, 195, 308], 4000),
]


def reads():
    L = ['b601 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for rr in READS:
        label, repo, rev, path, sel = rr[:5]
        width = rr[5] if len(rr) > 5 else 900
        if rev == 'HEAD' and repo == RELAY and not g(repo, 'ls-files', path).strip():
            sl = io.open(os.path.join(ROOT, path), encoding='utf-8').read().split(NL)
            at = 'working tree'
        else:
            sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
            at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, at, len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### SIDE-explicit-formula: v0.18 = %s ; main = %s ; tags %s ; the checkout`s branch %s' % (
        g(EFK, 'rev-parse', '--short=7', 'v0.18^{commit}').strip(), g(EFK, 'rev-parse', '--short=7', 'main').strip(),
        ' '.join(g(EFK, 'tag', '--sort=-creatordate').split()[:3]), g(EFK, 'branch', '--show-current').strip()),
          '### Mathlib (the kernel`s .lake/packages/mathlib) HEAD %s' % g(MLK, 'rev-parse', '--short=10', 'HEAD').strip(),
          '### chain_page.py`s hold: %s' % [l for l in io.open(os.path.join(ROOT, 'tools', 'chain_page.py'), encoding='utf-8').read().split(NL)
                                             if l.startswith('HOLD_MB')]]
    put_txt('b601_reads.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B600_ENTRY = '## REMAINDER 5: the product lemma as a salt-checked Prop at SIDE-explicit-formula v0.18'
W_HEAD = '*Appended 2026-10-02 by b601 to b600’s entry (:%d), under `(R211)`(1) -- b600 AT ITS WEIGHT:*'
R_HEAD = ('*Appended 2026-10-02 by b601 beside b600’s entry (:%d), under `(R211)`(2) -- THE READING b600 ADDS, ENTERED AS A READING AND '
          'MARKED AS THE AUTHOR’S STRIKE ITEM:*')


def weight_line():
    """### PLACE-papers FINDINGS: b600's weight and (R211)(2)'s reading, two appended lines addressed to b600's entry."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B600_ENTRY)
    if entry != 6950:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    h1, h2 = W_HEAD % entry, R_HEAD % entry
    for h in (h1, h2):
        Q.guard_absent(Q.FIND, h)
    t1 = ('\n%s SIDE-explicit-formula v0.18 = 1dd5cd7 by push_gated.sh, SIDEExplicitFormula/Product.lean: sum (the carrier the union, '
          'multiplicities added and each read on its own carrier, arithmetic sides added, targets conjoined); sum_ef, each zero side '
          'summable by its part’s count through Zeta23.WeilEF.EF_zero_sum_summable_gen; the Prop ProductLemma and productLemma_holds, '
          'DERIVES, T0, at the standard three; the salt check -- a sum with a point can be Weil-positive, and each part is load-bearing in '
          'either order, b596’s on-line toy beside b590’s off-line pair giving a sum that is not Weil-positive; the git grep over 44 '
          'kernels finding no declaration outside the act’s files concluding the Prop or its negation. The ζ page at v0.18 with five '
          'Product nodes, the χ page unchanged, page arms and the frozen control 2 of 2; the placement on the ζ page accepted, the reason '
          'the seat’s (a graded name absent from the ζ list would stop that page re-emitting). Bearing: GRH_CASCADE v0.3.6 :45 and '
          'SIMPLICITY_OF_RIEMANN_ZEROS v1.1.3 :290, relay data/b600_bearing.txt. FINDINGS :6948, :6950; OPEN_TRAILS :12352 (the '
          'amendment addressed to :12288), :12354 (the authority order), :12356 (the build clause), :12358 (the trail record). The '
          'terminal table’s housekeeping commit 32f274f9 (26 rows, no grade moved). The suite 75 of 75 before and after the push; '
          'H34a–H34c, N1–N5, S1–S5 held, N1 on the completed build. Defects (a)–(c) the seat’s as logged; the DNS retry under standing '
          'rule 14. Nothing deposited; no keystone edited.\n' % h1)
    t2 = ('\n%s Positivity is conjunctive over sums: no part’s positivity can be borrowed from another’s, and an off-line part cannot be '
          'cancelled by any on-line companion. For an abelian Dedekind zeta written as a product of Dirichlet L-functions, the lemma '
          'reads, once the factors are configurations of the schema, as Weil positivity of the product holding exactly when it holds for '
          'every factor -- a reading, carried as such until the factorisation is an instance in the kernel. And because multiplicities '
          'add, the sum of a configuration with itself doubles every multiplicity while keeping positivity unchanged: within the schema, '
          'Weil positivity does not imply simplicity. That is the faces’ silence on multiplicity (the ζ page’s last paragraph, b596) '
          'given a constructive reason at the schema level -- and it says that any route from the located clause to simplicity must use '
          'something about ζ beyond what the schema records. It is a statement about the schema and not about ζ’s zeros. *(A reading, '
          'the author’s to strike; its compiled half is b601’s doubling corollary.)*\n' % h2)
    out = []
    for h, t in ((h1, t1), (h2, t2)):
        r = Q.append_to(Q.FIND, t)
        out.append(dict(head=h, line=Q.line_of(Q.FIND, h), append=r))
    put_json('b601_weight_line.json', dict(entry=entry, lines=out))
    for o in out:
        print('  line :%s' % o['line'])


# ================================================================================ COMPONENT 2-3: THE STATEMENTS
WO_ROW, WO_PRICE = 11704, 12132
# ### each item: (words, the text they are read in, the declaration that carries them, the declaration's printed head)
ITEMS = dict(
    doub=[
        ('sum C C has multiplicity 2·m at every point of C\'s carrier', 'ruling', 'sum_self_mult',
         r'theorem sum_self_mult \(C : WeilConfig\) \(ρ : ℂ\) \(hρ : ρ ∈ C\.carrier\) : \(sum C C\)\.mult ρ = 2 \* C\.mult ρ'),
        ('is Weil-positive exactly when C is (productLemma_holds with both parts C)', 'ruling', 'doubling_iff',
         r'theorem doubling_iff \(C : WeilConfig\) : h2_sign_cfg \(sum C C\) ↔ h2_sign_cfg C :=\n  \(productLemma_holds C C\)'),
        ('the schema\'s positivity Prop does not imply the schema\'s simplicity Prop', 'ruling', 'positivity_not_imp_simplicity',
         r'theorem positivity_not_imp_simplicity : ¬ PositivityImpliesSimplicity'),
        ('exhibited by the doubled on-line toy of b596, positive and with a point of multiplicity 2', 'ruling', 'doubledToy',
         r'def doubledToy : WeilConfig := sum \(Simplicity\.SaltCheck\.toyCfg 1 le_rfl\) \(Simplicity\.SaltCheck\.toyCfg 1 le_rfl\)'),
    ],
    keip=[
        ('the Keiper-Taylor identity', 'price', 'KeiperTaylorIdentity', r'def KeiperTaylorIdentity : Prop := KeiperTaylor ∧ StieltjesLog ∧ GammaRZetaValues'),
        ('the Stieltjes constants defined as the Taylor coefficients of riemannZeta₀ at 1', 'price', 'stieltjes',
         r'def stieltjes \(n : ℕ\) : ℂ := \(-1\) \^ n \* iteratedDeriv n riemannZeta₀ 1'),
        ('the zeroth equal to γ by the Mathlib limit above', 'price', 'stieltjes_zero_limit', r'theorem stieltjes_zero_limit :'),
        ('taylorCoeff riemannXi n equal to the finite Keiper sum in them', 'price', 'KeiperTaylor',
         r'def KeiperTaylor : Prop := ∀ n : ℕ, LiCriterion\.taylorCoeff LiCriterion\.riemannXi n = keiperSum n'),
        ('the polygamma values at 1/2', 'price', 'GammaRZetaValues', r'def GammaRZetaValues : Prop :='),
        ('log π', 'price', 'gammaRLogCoeff_zero', r'theorem gammaRLogCoeff_zero :'),
        ('power-series log', 'price', 'StieltjesLog', r'def StieltjesLog : Prop :='),
        ('the binomial transform', 'price', 'BinomialTransform', r'def BinomialTransform : Prop :='),
        ('the n = 1 check against γ', 'price', 'liCoeff_one_keiper', r'theorem liCoeff_one_keiper :'),
        ('Keiper’s definition of λ_n compiled and shown equal to `LiCoeff`', 'row', 'liCoeff_one_keiper', r'LiWeil\.LiCoeff 1 ='),
    ],
    kbnd=[
        ('computable two-sided bounds for the Stieltjes constants up to the eleventh', 'price', 'KeiperBounds',
         r'\(∀ n : ℕ, n ≤ 11 → StieltjesBoundsAt n\)'),
        ('and for the polygamma values at 1/2 (the odd zeta values among them)', 'price', 'ZetaValueBoundsAt',
         r'def ZetaValueBoundsAt \(j : ℕ\) : Prop := InInterval \(zLo j\) \(zHi j\) \(riemannZeta \(j : ℂ\)\)'),
        ('which interval arithmetic would consume to certify a finite-n sign in-kernel', 'price', 'InInterval',
         r'def InInterval \(lo hi : ℚ\) \(x : ℂ\) : Prop :='),
        ('computable bounds for the constants it consumes', 'reprice', 'BoundPremises', r'structure BoundPremises : Prop where'),
    ],
)
DECL = re.compile(r'^(theorem|def|structure|noncomputable def|abbrev) (\S+)')


def _headers(text):
    ls = text.split(NL)
    out = []
    for i, l in enumerate(ls):
        m = DECL.match(l)
        if not m:
            continue
        h = [l]
        j = i
        while not re.search(r':=|\bwhere\b', ls[j]) and j + 1 < len(ls):
            j += 1
            h.append(ls[j])
        out.append(dict(kind=m.group(1), name=m.group(2), line=i + 1, head=NL.join(h)))
    return out


def _sources_of_words():
    ot = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8').read().split(NL)
    price = [l for l in rd('b589_keiper_read.txt').split(NL) if l.startswith('    THE PRICE, TWO LEMMAS OF SUBSTANCE')]
    ferry = rd('b601_ferry.txt')
    r3 = ferry[ferry.index('(3) THE DOUBLING COROLLARY'):ferry.index('(4) W-ORD-KEIPER-FACE')]
    return dict(row=ot[WO_ROW - 1], reprice=ot[WO_PRICE - 1], price=price[0] if price else '', ruling=r3)


def statements(key, suffix=''):
    """### the statements of one kernel file as written in the working tree of the branch, printed before its build; for `doub`,
    ### `keip` and `kbnd`, the statement each is held to (the ruling's (3), or the work-order's row, re-price and price bank) beside the
    ### declarations that carry it, item by item (H35c's first half)."""
    rel = KFILES[key]
    b = open(os.path.join(EFK, rel), 'rb').read()
    t = b.decode('utf-8')
    hs = _headers(t)
    L = ['b601 -- THE STATEMENTS OF %s, PRINTED %s' % (rel, 'BEFORE THE BUILD' if not suffix else 'AGAIN AFTER THE FILE CHANGED (the first print kept beside)'), '']
    if suffix:
        first = {d['name']: d['head'] for d in jl('b601_statements_%s.json' % key)['decls']}
        now = {d['name']: d['head'] for d in hs}
        L += ['### against the first print: headers unchanged %s ; changed %s ; added %s ; gone %s' % (
            sorted(n for n in now if first.get(n) == now[n]), sorted(n for n in now if n in first and first[n] != now[n]),
            sorted(set(now) - set(first)), sorted(set(first) - set(now))), '']
    L += ['### written at (UTC) %s ; the branch %s (checked out: %s) ; the file`s sha256 %s ; its bytes %d' % (
        utc(), BRANCH, g(EFK, 'branch', '--show-current').strip(), sha(b), len(b)), '']
    items = []
    if key in ITEMS:
        W = _sources_of_words()
        if key == 'doub':
            L += ['### THE STATEMENT, (R211)(3) AS BANKED IN data/b601_ferry.txt (whitespace joined):', '    ' + flat(W['ruling']), '']
        else:
            L += ['### THE WORK-ORDER, LOCATED BY NAME: its row, OPEN_TRAILS :%d, WHOLE:' % WO_ROW, '    ' + W['row'],
                  '### its re-price, OPEN_TRAILS :%d, WHOLE:' % WO_PRICE, '    ' + W['reprice'],
                  '### the price it cites (relay data/b589_keiper_read.txt), WHOLE:', '    ' + W['price'], '']
        L.append('### THE STATEMENT, ITEM BY ITEM, BESIDE THE DECLARATION THAT CARRIES IT:')
        for words, src, name, rx in ITEMS[key]:
            inwo = flat(words) in flat(W[src])
            found = re.search(rx, t) is not None
            items.append(dict(words=words, source=src, decl=name, in_statement=inwo, declared=found))
            L.append('    %-84s [%s] -> %-30s in its statement %s ; declared as printed %s' % ('“%s”' % words, src, name, inwo, found))
        L.append('### ### **%s**' % ('EVERY ITEM OF THE STATEMENT CARRIED BY A DECLARATION' if all(i['in_statement'] and i['declared'] for i in items)
                                     else '### AN ITEM NOT CARRIED'))
        L.append('')
    for h in hs:
        L.append('### :%d %s %s' % (h['line'], h['kind'], h['name']))
        L += ['    ' + x for x in h['head'].split(NL)]
    put_txt('b601_statements_%s%s.txt' % (key, suffix), L)
    put_json('b601_statements_%s%s.json' % (key, suffix), dict(file=rel, sha256=sha(b), at=utc(), decls=hs, items=items))


def build_bank(key, logpath):
    """### the watchdog's build log copied into relay data/b601_build_<key>.txt with a head line."""
    src = io.open(logpath, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    hdr = ('### b601 -- THE BUILD OF %s ON %s, ONE MODULE PER CALL, A DETACHED PROCESS WATCHED FROM THE FOREGROUND (OPEN_TRAILS :12356), '
           'THE WATCHDOG`S LOG (lean resident cap 3500 MB, free floor 900 MB; the seat starts no call below the 2560 MB hold), copied from '
           'the seat`s scratchpad' % (key, BRANCH))
    put_txt('b601_build_%s.txt' % key, [hdr, ''] + src.rstrip(NL).split(NL))


def prints(key, logpath):
    """### the Lean output of one axiom-check run (the watchdog's log, its `  | ` lines), banked as data/b601_prints_<key>.txt / .json."""
    import b569_record as R9
    src = io.open(logpath, encoding='utf-8').read().replace(chr(13), '')
    out = [l[4:] for l in src.split(NL) if l.startswith('  | ')]
    ex = [l for l in src.split(NL) if l.startswith('### EXIT')]
    txt = NL.join(out)
    ax = R9.prints_axioms(txt)
    L = ['b601 -- THE PRINTS: `lake env lean %s` at SIDE-explicit-formula %s (checked out: %s, HEAD %s), the watchdog`s run' % (
        AXF[key], BRANCH, g(EFK, 'branch', '--show-current').strip(), g(EFK, 'rev-parse', '--short=7', 'HEAD').strip()),
         '### %s' % (ex[-1] if ex else '### NO EXIT LINE'), ''] + out
    put_txt('b601_prints_%s.txt' % key, L)
    put_json('b601_prints_%s.json' % key, dict(axioms=ax, sorry=[n for n, a in ax.items() if 'sorryAx' in a],
                                               std3=all(set(a) <= set(STD3) for a in ax.values()), exit=ex[-1] if ex else None,
                                               errors=sum(1 for l in out if ': error' in l or l.startswith('error')), text=txt))
    print('  prints', len(ax), 'std3', all(set(a) <= set(STD3) for a in ax.values()))


def e0(key):
    """### every declaration of one kernel file graded by the shared E0 rule (tools/e0_rule.py) at the branch tip, with its print."""
    import b569_record as R9
    import e0_rule as E0
    st = jl('b601_statements_%s_final.json' % key) if os.path.exists(os.path.join(D, 'b601_statements_%s_final.json' % key)) \
        else jl('b601_statements_%s.json' % key)
    axk = 'doub' if key in AX_KEYS['doub'] else 'keip'
    P0 = jl('b601_prints_%s.json' % axk)['axioms']
    tip = g(EFK, 'rev-parse', BRANCH).strip()
    src = g(EFK, 'show', '%s:%s' % (tip, st['file']))
    rows = {}
    L = ['b601 -- THE E0 READ OF %s AT THE BRANCH TIP %s (%s)' % (st['file'], tip[:7], BRANCH)] + E0.RULE_TEXT + [
        '### the file at the tip is the one printed: %s' % (sha(src) == st['sha256']), '']
    for d in st['decls']:
        n = KNS[key] + d['name']
        kind = 'theorem' if d['kind'] == 'theorem' else 'def'
        head, _ln = R9.header_of(src, d['name'])
        gr, why, _b = E0.grade(head or '', kind)
        ax = P0.get(n)
        rows[n] = dict(grade=gr if kind == 'theorem' else 'DEF', why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3), head=head, kind=kind)
        L.append('    %-34s %-10s %s  -- %s' % (d['name'], rows[n]['grade'], 'std3' if rows[n]['std3'] else ax, (why or '')[:140]))
    gate = all(r['std3'] for r in rows.values()) and all(r['head'] is not None or r['kind'] == 'def' for r in rows.values())
    L.append('### ### **THE GATE: %s** -- declarations %d, theorems %d (DERIVES %d, INTERFACES %d)' % (
        'PASS' if gate else 'FAIL', len(rows), sum(1 for r in rows.values() if r['kind'] == 'theorem'),
        sum(1 for r in rows.values() if r['grade'] == 'DERIVES'), sum(1 for r in rows.values() if r['grade'] == 'INTERFACES')))
    put_txt('b601_e0_%s.txt' % key, L)
    put_json('b601_e0_%s.json' % key, dict(rows=rows, gate=gate, tip=tip, file=st['file'], same_file=sha(src) == st['sha256']))


# ### THE FEDERATION WALK. LOOSE: a theorem header naming one of the act's Props or the Stieltjes constants. STRICT: a conclusion
# ### that IS one of the act's Props or the corollary's non-implication, or the negation of one.
FED_PAT = r'DoublingCorollary|PositivityImpliesSimplicity|KeiperTaylor|KeiperBounds|KeiperObligations|BoundPremises|[Ss]tieltjes'
PROPS = r'(DoublingCorollary|KeiperTaylor|KeiperTaylorIdentity|KeiperBounds)'
QUAL = r'(SIDEExplicitFormula\.)?((Doubling|Keiper|KeiperBounds)\.)?'
STRICT_POS = re.compile(r'^\s*(' + QUAL + PROPS + r'|¬\s*\(?\s*' + QUAL + r'PositivityImpliesSimplicity\s*\)?)\s*$')
STRICT_NEG = re.compile(r'^\s*(¬\s*\(?\s*' + QUAL + PROPS + r'\s*\)?|' + QUAL + r'PositivityImpliesSimplicity)\s*$')
LOOSE = re.compile(r'(DoublingCorollary|PositivityImpliesSimplicity|Keiper|[Ss]tieltjes)')


def _strict_controls():
    """### each strict shape on a conclusion it must read and one it must not; RETURNS the results (all True to pass)."""
    return dict(pos_reads=bool(STRICT_POS.search(' ¬ PositivityImpliesSimplicity')) and bool(STRICT_POS.search(' Keiper.KeiperTaylor')),
                pos_refuses=not STRICT_POS.search(' h2_sign_cfg C ↔ C.target'),
                neg_reads=bool(STRICT_NEG.search(' ¬ KeiperBounds')) and bool(STRICT_NEG.search(' PositivityImpliesSimplicity')),
                neg_refuses=not STRICT_NEG.search(' ¬ h2_sign_cfg C'))


def _decl_heads(text):
    out = []
    for m in re.finditer(r'^[ \t]*(?:@\[[^\]]*\][ \t]*)?(?:(?:private|protected|nonrec)[ \t]+)*(theorem|lemma)[ \t]+(\S+)(.*?):=', text, re.M | re.S):
        out.append((text[:m.start()].count(NL) + 1, m.group(2), ' '.join((m.group(2) + m.group(3)).split())))
    return out


def fed_walk(head_of_ker=None):
    """### every kernel's HEAD by git grep (the explicit-formula kernel at `head_of_ker` when given, the act's branch tip), every
    ### theorem/lemma header naming the act's Props or the Stieltjes constants, its conclusion classified. RETURNS (rows, kernels, files)."""
    kernels = sorted(d for d in os.listdir('D:/') if d.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d, '.git')))
    rows, files = [], 0
    for k in kernels:
        rep = 'D:/' + k
        rev = head_of_ker if (k == 'SIDE-explicit-formula' and head_of_ker) else 'HEAD'
        out = g(rep, 'grep', '-l', '-I', '-E', FED_PAT, rev, '--', '*.lean')
        for f in [x.split(':', 1)[1] for x in out.split(NL) if x.strip()]:
            files += 1
            t = g(rep, 'show', '%s:%s' % (rev, f))
            for ln, name, head in _decl_heads(t):
                if not re.search(FED_PAT, head):
                    continue
                depth, cut = 0, -1
                for i, ch in enumerate(head):
                    if ch in '([{⟨':
                        depth += 1
                    elif ch in ')]}⟩':
                        depth -= 1
                    elif ch == ':' and depth == 0 and head[i:i + 2] != ':=':
                        cut = i
                concl = head[cut + 1:] if cut >= 0 else head
                own = k == 'SIDE-explicit-formula' and f in OWN
                if own:
                    cls = 'OWN'
                elif STRICT_NEG.search(concl):
                    cls = 'NEGATES'
                elif STRICT_POS.search(concl):
                    cls = 'CONCLUDES'
                elif LOOSE.search(concl):
                    cls = 'READ'
                else:
                    cls = 'OTHER'
                rows.append(dict(kernel=k, file=f, line=ln, name=name, cls=cls, conclusion=concl[:300], reading=HAND.get((f, name)) if cls == 'READ' else None))
    return rows, kernels, files


HAND = {}


def grep_bank():
    """### the federation searched by git grep at every kernel's HEAD (the explicit-formula kernel at the act's branch tip) for a
    ### declaration concluding one of the act's Props or its negation; the strict shapes exercised; the act's own files marked OWN."""
    tip = g(EFK, 'rev-parse', BRANCH).strip()
    rows, kernels, files = fed_walk(tip or None)
    bad = [r for r in rows if r['cls'] in ('CONCLUDES', 'NEGATES') or (r['cls'] == 'READ' and not r['reading'])]
    ctl = _strict_controls()
    L = ['b601 -- THE FEDERATION SEARCHED FOR A DECLARATION CONCLUDING THE DOUBLING COROLLARY, THE KEIPER PROPS OR THEIR NEGATIONS (UTC %s)' % utc(), '',
         '### git grep -l -E "%s" at HEAD of every kernel (%d; SIDE-explicit-formula at %s, the branch tip %s), %d files; every theorem/lemma '
         'header naming one, its conclusion (the header after its last top-level colon) classified: CONCLUDES / NEGATES by the strict shapes, '
         'READ by the loose one, OTHER, OWN (this act`s files)' % (FED_PAT, len(kernels), BRANCH, tip[:7], files)]
    for r in rows:
        if r['cls'] != 'OTHER':
            L.append('    %-9s %s %s:%d %s -- %s' % (r['cls'], r['kernel'], r['file'], r['line'], r['name'], r['conclusion'][:180]))
            if r['cls'] == 'READ':
                L.append('              ### the seat`s hand reading: %s' % (r['reading'] or '### NONE -- COUNTED'))
    L += ['### OTHER rows (named the pattern, conclusion not one of the Props) %d: %s' % (sum(r['cls'] == 'OTHER' for r in rows),
                                                                                        ', '.join('%s:%s' % (r['file'].split('/')[-1], r['name']) for r in rows if r['cls'] == 'OTHER')[:3000]),
          '### headers %d ; CONCLUDES %d ; NEGATES %d ; READ %d (hand-read %d) ; OTHER %d ; OWN %d' % (
              len(rows), sum(r['cls'] == 'CONCLUDES' for r in rows), sum(r['cls'] == 'NEGATES' for r in rows), sum(r['cls'] == 'READ' for r in rows),
              sum(r['cls'] == 'READ' and bool(r['reading']) for r in rows), sum(r['cls'] == 'OTHER' for r in rows), sum(r['cls'] == 'OWN' for r in rows)),
          '### the strict shapes, each exercised: %s' % ctl,
          '', '### ### **OUTSIDE THIS ACT`S OWN FILES, DECLARATIONS CONCLUDING ONE OF THE PROPS OR ITS NEGATION : %d**' % len(bad)]
    put_txt('b601_grep.txt', L)
    put_json('b601_grep.json', dict(rows=rows, kernels=kernels, files=files, bad=bad, controls=ctl, tip=tip))
    print('  headers', len(rows), 'bad', len(bad), 'own', sum(r['cls'] == 'OWN' for r in rows), ctl)


# ================================================================================ THE NODE LIST AND THE PAGES
NODE_HEAD = ['# b601 -- THE ζ NODE LIST AT v0.19, (R211)(4)-(5): b600`s list (relay data/b600_nodes_zeta.txt, every record line unchanged,',
             '# its backmatter record kept), the pin moved to v0.19; ten declarations of the Keiper face placed beside the Li ladder, directly',
             '# after li_nonneg_iff_rh (H35e), and four of the doubling corollary appended after the Product nodes. Every cell is elaborated by',
             '# the generator`s probe at the pin, never typed here.', '#']
KEIP_ADD = [KN + 'stieltjes | kernel | added: (R211)(4), the Stieltjes constants as the Taylor coefficients of Mathlib`s riemannZeta₀ at 1',
            KN + 'KeiperTaylor | kernel | added: (R211)(4), Bulka`s Taylor coefficient of ξ as the Keiper sum, a Prop',
            KN + 'KeiperTaylorIdentity | kernel | added: (R211)(4), the work-order`s lemma (1), the identity in the Stieltjes constants, the polygamma values at 1/2 and log π',
            KN + 'KeiperObligations | kernel | added: (R211)(4), lemma (1)`s four named obligations',
            KN + 'keiperTaylorIdentity_of | kernel | added: (R211)(4), lemma (1) at INTERFACES on its obligations',
            KN + 'keiperTaylor_zero | kernel | added: (R211)(4), lemma (1) at n = 0, proved',
            KN + 'liCoeff_one_keiper | kernel | added: (R211)(4), Keiper`s λ_1 = 1 + γ/2 − ½ log 4π, the n = 1 check against γ',
            BN + 'KeiperBounds | kernel | added: (R211)(4), the work-order`s lemma (2), the bound table as a Prop',
            BN + 'BoundPremises | kernel | added: (R211)(4), lemma (2)`s named premises (γ to the table`s width, γ_1..γ_11, ζ(2)..ζ(12))',
            BN + 'keiperBounds_of | kernel | added: (R211)(4), lemma (2) at INTERFACES on its premises']
DOUB_ADD = [DN + 'DoublingCorollary | kernel | added: (R211)(3), the doubling corollary as a Prop',
            DN + 'doubling_holds | kernel | added: (R211)(3), the doubling corollary proved by productLemma_holds',
            DN + 'PositivityImpliesSimplicity | kernel | added: (R211)(3), the schema`s positivity implying its simplicity, a Prop',
            DN + 'positivity_not_imp_simplicity | kernel | added: (R211)(3), the named corollary, exhibited by the doubled toy']


def node_list():
    """### data/b601_nodes_zeta.txt: b600's ζ list, the pin moved to v0.19, the Keiper nodes directly after li_nonneg_iff_rh's record and
    ### the doubling nodes after the last Product node (the backmatter record stays the list's last line)."""
    z = rd('b600_nodes_zeta.txt').rstrip(NL).split(NL)
    if z.count('# pin: v0.18') != 1 or not z[-1].startswith('# backmatter: ') or z.count(LI_ANCHOR) != 1:
        sys.exit('### b600`s ζ list does not carry its pin once, its backmatter record last, or the Li anchor once -- NOTHING WRITTEN')
    body = [('# pin: v0.19' if l == '# pin: v0.18' else l) for l in z[:-1]]
    i = body.index(LI_ANCHOR) + 1
    body = body[:i] + KEIP_ADD + body[i:]
    put_txt('b601_nodes_zeta.txt', NODE_HEAD + body + DOUB_ADD + [z[-1]])


NODES = {'zeta': 'b601_nodes_zeta.txt', 'chi': 'b596_nodes_chi.txt'}
PROBE = {'zeta': 'b601_probe_out.txt', 'chi': 'b596_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}


def free_mb():
    try:
        out = subprocess.run(['powershell', '-NoProfile', '-Command', '(Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory'],
                             capture_output=True, text=True).stdout
        return int(out.strip()) // 1024
    except Exception:
        return -1


def cr0(b):
    return (b or b'').replace(b'\r\n', b'\n')


def page(k):
    """### after the tag: ONE page per call in the foreground. `zeta`: a full run at v0.19 from data/b601_nodes_zeta.txt (free memory read
    ### before the call against the hold; the probe banked as data/b601_probe_out.txt and .lean.txt); `chi`: re-emitted from b596's v0.17
    ### list and banked probe. Writes the page only when it changed, and data/b601_page_<k>.json."""
    import shutil
    import difflib
    import chain_page as C
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b601_%s' % k)
    fm = free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, C.HOLD_MB))
    if 0 <= fm < C.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    frm = None if k == 'zeta' else os.path.join(D, PROBE[k])
    rc, pg, meta, log = C.build(os.path.join(D, NODES[k]), pdir, frm)
    secs = int(time.time() - t0)
    for l in log:
        print('  %s: %s' % (k, l))
    if rc:
        put_json('b601_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    if frm is None:
        shutil.copyfile(os.path.join(pdir, 'chain_page_probe_out.txt'), os.path.join(D, PROBE[k]))
        shutil.copyfile(os.path.join(pdir, 'chain_page_probe.lean'), os.path.join(D, PROBE[k].replace('_out.txt', '.lean.txt')))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    new = [dict(name=n, grade=meta['cells'][n].get('grade'), tier=meta['cells'][n].get('tier'), premises=meta['cells'][n].get('premises'),
                axioms=meta['cells'][n].get('axioms'), entry=meta['cells'][n].get('entry'), module=meta['cells'][n].get('module'))
           for n in NEW_NODES if n in (meta.get('cells') or {})]
    lines = b.decode('utf-8').split(NL)
    rows = {n: [l for l in lines if ('`%s`' % n) in l or (' %s ' % n) in l][:2] for n in NEW_NODES}
    li = [i for i, l in enumerate(lines) if l.split(' — ')[0].endswith('`SIDEExplicitFormula.LiCriterionBridge.li_nonneg_iff_rh`')]
    nb = lines[li[0] + 1] if li and li[0] + 1 < len(lines) else ''
    J = dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, at=utc(),
             free_mb_before=fm, seconds=secs, new=new, rows=rows, li_row=lines[li[0]] if li else None, li_neighbour=nb,
             pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), log=log)
    put_json('b601_page_%s.json' % k, J)
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))
    for x in new:
        print('    NEW NODE %s -- %s ; tier %s ; premises %s ; axioms %s ; entry %s' % (x['name'], x['grade'], x['tier'], x['premises'], x['axioms'], x['entry']))
    print('  the Li ladder`s neighbour row: %s' % nb[:200])
    for x in dl[:80]:
        print('    ' + x[:240])


def page_arms(tag):
    """### both page arms at PLACE-papers HEAD from this act's ζ list and probe and b596's χ list and probe, and the frozen control.
    ### Writes data/b601_page_arms_<tag>.txt."""
    import g_chain_page as GCP
    import test_chain_page_b596 as T
    L = ['b601 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b601_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = T.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            T.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (T.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b601_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ THE BEARING
BEARING = [
    ('corollary', SIMP, 82, 'which the schema’s fields, its target and Weil positivity do not force',
     'The sentence cites allSimple_not_forced (v0.17): one configuration of the schema, target held and Weil-positive on classK, with '
     'a point of multiplicity two, built for the purpose. The doubling corollary gives that silence a constructive reason inside the '
     'schema: for every configuration C, the sum of C with itself doubles every multiplicity on the carrier and is Weil-positive '
     'exactly when C is (`doubling_holds`, SIDE-explicit-formula v0.19), so every Weil-positive configuration with a point yields one '
     'with a multiple point, and the schema’s positivity Prop does not imply its simplicity Prop (`positivity_not_imp_simplicity`, '
     'exhibited by `doubledToy`, b596’s on-line toy doubled). What does not move: the sentence’s simplicity stays open as its own '
     'statement; the corollary is about the schema’s form, and a route from Weil positivity to the simplicity of ζ’s zeros has to use '
     'something about ζ the schema does not record.'),
    ('corollary', SIMP, 180, 'a configuration whose fields, target and Weil positivity all hold has a point of multiplicity two',
     'The sentence’s compiled half says the explicit formula weighs zeros by multiplicity and that the schema admits a Weil-positive '
     'configuration with a point of multiplicity two. The corollary turns the single toy into an operation on the whole schema: the sum '
     'of any configuration with itself satisfies every field (the summed explicit formula `sum_ef` and the counts added, v0.18), '
     'doubles each multiplicity, and leaves the criterion where it was (`doubling_iff`, v0.19). The derivative-level mismatch the '
     'sentence’s first half describes is not among the schema’s fields; the corollary shows the fields admit doubling at every '
     'configuration, not at one.'),
    ('keiper', BALPOS, 195, 'that identification is analysis, done outside the kernel',
     'The sentence says the kernel’s Li map certifies the algebra of the split λ_n = λ_A(n) + λ_Z(n) and not that the streams are the '
     'Taylor coefficients of the archimedean and pole+Euler channels. The Keiper face defines those coefficients in the kernel on '
     'Mathlib’s objects at the pin -- `zetaLogCoeff`, the Taylor coefficients at 1 of the logarithmic derivative of riemannZeta₁ = '
     '(s − 1) ζ(s), and `gammaRLogCoeff`, those of Γℝ -- and states the identification as the Prop `KeiperTaylor` (Bulka’s taylorCoeff '
     'riemannXi n, which is LiCoeff (n + 1) by `li_coeff_eq_taylorCoeff`, as the binomial transform of 1/s, the ζ channel and the Γℝ '
     'channel), at INTERFACES on four named obligations (`keiperTaylorIdentity_of`, v0.19). It is proved at n = 0 '
     '(`keiperTaylor_zero`), each channel’s first coefficient compiled: γ for the ζ channel, −(γ + log 4π)/2 for Γℝ. For n ≥ 1 the '
     'identification stays outside the kernel, now as named obligations rather than as unstated analysis.'),
    ('keiper', BALPOS, 308, '**0.0230957089661**',
     'The row’s three numbers at n = 1 -- λ_A(1) = −0.554119955935, λ_Z(1) = 0.577215664902, the margin λ_1 = 0.0230957089661 -- are '
     'measurements. At n = 1 the kernel now holds the margin as an identity, LiCoeff 1 = 1 + γ/2 − ½ log 4π (`liCoeff_one_keiper`, '
     'T0, v0.19), and the split at k = 0 into 1, γ and −(γ + log 4π)/2 (`logDerivSplit_zero`): the row’s λ_Z(1) is γ and its λ_A(1) '
     'is 1 − (γ + log 4π)/2, their sum the compiled value. The sign of λ_1 is not certified in the kernel: Mathlib’s interval (1/2, '
     '2/3) for γ leaves 1 + γ/2 − ½ log 4π in an interval about zero, so the bench’s tight γ enters as the named premise '
     '`BoundPremises.gamma_tight`.'),
]


def bearing():
    """### the keystone sentences each component bears on, each printed from its current version at PLACE-papers HEAD by path and line,
    ### the reading beside it; data/b601_bearing.txt / .json."""
    L = ['b601 -- COMPONENT 4: THE BEARING -- THE KEYSTONE SENTENCES THE DOUBLING COROLLARY AND THE KEIPER FACE CHANGE THE READING OF, EACH '
         'PRINTED BY PATH AND LINE FROM ITS CURRENT VERSION AT PLACE-papers %s, THE READING BESIDE IT (UTC %s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc()),
         '### the search: the keystones` current versions grepped for simple/simplicity beside positivity or Weil, multiplicity, Keiper, Stieltjes, '
         'λ_1 and its value, the channels λ_A / λ_Z -- the residue hand-read.', '']
    rows = []
    for comp, path, ln, needle, reading in BEARING:
        line = g(PP, 'show', 'HEAD:' + path).split(NL)[ln - 1]
        ok = needle in line
        rows.append(dict(component=comp, path=path, line=ln, needle=needle, found=ok, sentence=line, reading=reading))
        L += ['### [%s] %s :%d%s' % (comp, path, ln, '' if ok else '   ### THE NEEDLE IS NOT ON THE CITED LINE'),
              '    THE SENTENCE: ' + line, '    THE READING: ' + reading, '']
    L.append('### ### **SENTENCES PRINTED AS BEARING : %d (the corollary %d, the Keiper face %d) ; ON THEIR CITED LINES : %d**' % (
        len(rows), sum(r['component'] == 'corollary' for r in rows), sum(r['component'] == 'keiper' for r in rows), sum(r['found'] for r in rows)))
    put_txt('b601_bearing.txt', L)
    put_json('b601_bearing.json', dict(rows=rows, at=utc()))


# ================================================================================ THE PROMPTS, BANKED VERBATIM
def answers():
    """### every AskUserQuestion of this session, with question, options, recommended mark and the answer, read from the session
    ### transcript (b595's method); data/b601_author_answers.txt."""
    calls, results = [], {}
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
        try:
            o = json.loads(raw)
        except Exception:
            continue
        m = o.get('message') or {}
        for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
            if c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((i, c['id'], c['input']))
            if c.get('type') == 'tool_result':
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t
                results[c.get('tool_use_id')] = (i, t)
    L = ['### b601 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat (2026-10-02/03), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % sum(len(c[2].get('questions', [])) for c in calls), '']
    k = 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session 5dce8424-ec16-4701-8f42-69078426fd40, transcript line %d)' % (cid, i))
        for q in inp.get('questions', []):
            k += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'), op.get('description')))
        ri, rt = results.get(cid, (None, '### NO RESULT FOUND'))
        L += ['RESULT (transcript line %s): %s' % (ri, rt), '']
    if not calls:
        L.append('### NONE: no prompt was put to the author in this act.')
    put_txt('b601_author_answers.txt', L)


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
SCORE_KEYS = ('H35a', 'H35b', 'H35c', 'H35d', 'H35e', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
THE_PROPS = {'KeiperTaylorIdentity': KN + 'KeiperTaylorIdentity', 'KeiperBounds': BN + 'KeiperBounds'}


def _closed_lemmas(E):
    """### a work-order lemma CLOSES when a theorem of this act concludes its Prop with no premise binder and DERIVES at the standard
    ### three; RETURNS {Prop: [theorem names]}."""
    out = {}
    for prop in THE_PROPS:
        out[prop] = [n for e in E.values() for n, r in (e.get('rows') or {}).items()
                     if r['kind'] == 'theorem' and r['grade'] == 'DERIVES' and r['std3']
                     and re.search(r':\s*' + prop + r'\s*:=', ' '.join((r.get('head') or '').split()))]
    return out


def scores():
    E = {k: jl('b601_e0_%s.json' % k) for k in KFILES}
    PR = {k: jl('b601_prints_%s.json' % k) for k in AXF}
    ST = {k: jl('b601_statements_%s.json' % k) for k in ITEMS}
    gp, br = jl('b601_grep.json'), jl('b601_bearing.json')
    Z, X = jl('b601_page_zeta.json'), jl('b601_page_chi.json')
    rows = {n: r for e in E.values() for n, r in (e.get('rows') or {}).items()}
    g_ = lambda n: rows.get(n, {})
    all_std3 = all(e.get('gate') for e in E.values()) and all(not p.get('sorry') and p.get('std3') is True and p.get('errors') == 0 for p in PR.values())
    items_ok = {k: bool(ST[k].get('items')) and all(i['in_statement'] and i['declared'] for i in ST[k]['items']) for k in ITEMS}
    salt_d = all(g_(n).get('std3') and g_(n).get('grade') == 'DERIVES' for n in SALT_D)
    salt_k = all(g_(n).get('std3') and g_(n).get('grade') == 'DERIVES' for n in SALT_K)
    doub_closed = g_(DN + 'doubling_holds').get('grade') == 'DERIVES' and g_(DN + 'positivity_not_imp_simplicity').get('grade') == 'DERIVES' \
        and E['doub'].get('gate') is True
    doub_src = g(EFK, 'show', '%s:%s' % (TAG, KFILES['doub'])) or g(EFK, 'show', '%s:%s' % (BRANCH, KFILES['doub']))
    direct = bool(re.search(r'theorem doubling_iff[^\n]*\n\s*\(productLemma_holds C C\)', doub_src))
    toy = [DN + 'doubledToy_h2_sign_cfg', DN + 'doubledToy_not_allSimple', DN + 'doubledToy_mult_pt']
    toy_ok = all(g_(n).get('std3') and g_(n).get('grade') == 'DERIVES' for n in toy) and all(('%s :' % n) in (PR['doub'].get('text') or '') for n in toy)
    closed = _closed_lemmas(E)
    any_closed = any(closed.values())
    prem = g_(BN + 'keiperBounds_of').get('grade') == 'INTERFACES' and 'higher_stieltjes' in g(EFK, 'show', '%s:%s' % (BRANCH, KFILES['kbnd']))
    zn = {x['name']: x for x in Z.get('new', [])}
    nb = Z.get('li_neighbour') or ''
    li_row = bool(Z.get('li_row')) and any(('`%s`' % n) in nb for n in KEIP_NODES)
    zrows = sum(1 for d in Z.get('diff', []) if d.startswith('+') and not d.startswith('+++'))
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
                                                                               'SIDE-structural-error-correction', 'SIDE-cosmo', 'SIDE-silence-principle')}
    tagc = g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip()
    kern_ok = kern['SIDE-explicit-formula'] == tagc and {k: v for k, v in kern.items() if k != 'SIDE-explicit-formula'} == {
        'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-structural-error-correction': '6a4f482', 'SIDE-cosmo': 'c5cba30',
        'SIDE-silence-principle': '667c254'}
    kfiles = sorted(x for x in g(EFK, 'diff', '--name-only', PRE_KER, TAG).split(NL) if x.strip())
    kmerges = [x for x in g(EFK, 'rev-list', '--merges', '%s..%s' % (PRE_KER, TAG)).split(NL) if x.strip()]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md'] + [p['page'] for p in (Z, X) if p.get('changed')])
    # ### the trail record is this act's only OPEN_TRAILS write and it follows the scores: its pending append is accepted by name (b598)
    pp_ok = pp_ch in (want_pp, sorted(set(want_pp) - {'OPEN_TRAILS.md'}))
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b601_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b600_closing_push_out.txt'))
    bear = [r for r in br.get('rows', []) if r['found']]
    lam1 = g_(KN + 'liCoeff_one_keiper')
    S = dict(
        H35a=('HOLDS' if doub_closed and salt_d else 'REFUTED',
              'Doubling.lean`s gate %s (every declaration at the standard three) ; doubling_holds %s, positivity_not_imp_simplicity %s ; the '
              'salt-check`s three theorems DERIVES at the standard three %s' % (E['doub'].get('gate'), g_(DN + 'doubling_holds').get('grade'),
                                                                                g_(DN + 'positivity_not_imp_simplicity').get('grade'), salt_d)),
        H35b=('HOLDS' if toy_ok else 'REFUTED',
              'doubledToy_h2_sign_cfg, doubledToy_not_allSimple, doubledToy_mult_pt each DERIVES at the standard three and #check-printed from '
              'the kernel (data/b601_prints_doub.txt) %s' % toy_ok),
        H35c=('HOLDS' if items_ok['keip'] and items_ok['kbnd'] and salt_k else 'REFUTED',
              'lemma (1)`s statement item by item carried %s, lemma (2)`s %s (data/b601_statements_keip.txt, _kbnd.txt) ; the salt-check`s six '
              'theorems DERIVES at the standard three %s' % (items_ok['keip'], items_ok['kbnd'], salt_k)),
        H35d=('HOLDS' if any_closed else 'REFUTED',
              'a theorem concluding a work-order lemma`s Prop with no premise, DERIVES at the standard three: KeiperTaylorIdentity %s, '
              'KeiperBounds %s ; each carried at INTERFACES (keiperTaylorIdentity_of %s on four obligations, keiperBounds_of %s on three '
              'premises) ; closed beside them: keiperTaylor_zero %s, liCoeff_one_keiper %s, stieltjes_zero_coarse %s' % (
                  closed['KeiperTaylorIdentity'] or 'NONE', closed['KeiperBounds'] or 'NONE', g_(KN + 'keiperTaylorIdentity_of').get('grade'),
                  g_(BN + 'keiperBounds_of').get('grade'), g_(KN + 'keiperTaylor_zero').get('grade'), lam1.get('grade'),
                  g_(BN + 'stieltjes_zero_coarse').get('grade'))),
        H35e=('HOLDS' if li_row else 'REFUTED',
              'the ζ page`s row after li_nonneg_iff_rh names a Keiper node %s: %s' % (li_row, nb[:160])),
        N1=('HELD' if doub_closed and direct else 'REFUTED',
            'the corollary in one module (Doubling.lean) at the standard three %s ; doubling_iff`s proof the term (productLemma_holds C C) %s' % (doub_closed, direct)),
        N2=('HELD' if toy_ok else 'REFUTED', 'the doubled toy printed positive, its point of multiplicity 2, failing the simplicity Prop: %s' % toy_ok),
        N3=('HELD' if any_closed and prem else 'REFUTED',
            'a Keiper lemma closed at the standard three: %s ; every Stieltjes constant beyond γ a named premise (BoundPremises.higher_stieltjes, '
            'keiperBounds_of INTERFACES) %s' % (any_closed, prem)),
        N4=('HELD' if zrows >= 3 and Z.get('changed') is True and X.get('changed') is False else 'REFUTED',
            'the ζ page re-emitted at %s gains %d rows (diff + lines), changed %s ; the χ page changed %s' % (TAG, zrows, Z.get('changed'), X.get('changed'))),
        N5=('HELD' if kern_ok and not kmerges and kfiles == sorted(OWN) and pp_ok and relay_beyond == [] else 'REFUTED',
            'nothing deposits; SIDE-explicit-formula main at the tag %s, the other mains unmoved %s; the kernel`s files %s..%s %s, merges %d; '
            'PLACE-papers %s; relay files beyond the act`s own banks and tools and the table: %s' % (
                tagc, kern_ok, PRE_KER, TAG, kfiles, len(kmerges), pp_ch, relay_beyond)),
        S1=('HELD' if all_std3 else 'REFUTED',
            'every declaration of the five modules (%s) at the standard three, no sorryAx, no error: %s' % (
                ', '.join('%s %d' % (k, len(E[k].get('rows') or {})) for k in KFILES), all_std3)),
        S2=('HELD' if salt_d and salt_k else 'REFUTED',
            'the salt-checks` nine theorems, each DERIVES at the standard three: %s' % [(n.split('.')[-1], g_(n).get('grade')) for n in SALT_D + SALT_K]),
        S3=('HELD' if lam1.get('grade') == 'DERIVES' and lam1.get('std3') else 'REFUTED',
            'liCoeff_one_keiper (λ_1 = 1 + γ/2 − ½ log 4π) %s at the standard three %s' % (lam1.get('grade'), lam1.get('std3'))),
        S4=('HELD' if gp.get('bad') == [] and all(gp.get('controls', {}).values()) and any(r['cls'] == 'OWN' for r in gp.get('rows', [])) else 'REFUTED',
            'no declaration outside the act`s files concluding one of the Props or its negation ; the strict shapes exercised %s ; the act`s own '
            'declarations found by the same walk %s' % (gp.get('controls'), any(r['cls'] == 'OWN' for r in gp.get('rows', [])))),
        S5=('HELD' if [(r['path'], r['line']) for r in bear] == [(SIMP, 82), (SIMP, 180), (BALPOS, 195), (BALPOS, 308)] else 'REFUTED',
            'the bearing sentences: %s' % [(r['path'].split('/')[-1], r['line']) for r in bear]),
    )
    put_json('b601_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-6s %s -- %s' % (k, S[k][0], S[k][1][:220]))


def _n_obligations():
    return 4 + 3


def _title():
    S = jl('b601_scores.json')
    lemmas = 'proved at the standard three' if S['H35d'][0] == 'HOLDS' else 'carried to %d named obligations' % _n_obligations()
    return ('## The doubling corollary: Weil positivity of the schema without simplicity, at v0.19; the Keiper face’s two lemmas %s, the '
            'Li ladder’s arithmetic end at the page' % lemmas)


TRAIL_HEAD = ('### b601 — lane three, act twenty-eight under (R211): the doubling corollary -- the schema’s positivity without simplicity; '
              'W-ORD-KEIPER-FACE -- the two lemmas stated and carried to named obligations')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


FINDINGS_BODY = [
    '**The doubling corollary** (`(R211)`(3)). SIDE-explicit-formula v0.19 = `{TAGC}` (merged fast-forward and tagged by push_gated.sh '
    'after read-back; the branch doubling-keiper-b601 kept): `SIDEExplicitFormula/Doubling.lean` -- the sum of a configuration of the '
    'schema with itself has multiplicity 2·m at every point of its carrier and is Weil-positive on classK exactly when the configuration '
    'is, by `productLemma_holds` with both parts, joined as `DoublingCorollary` and proved, `doubling_holds`; and the named corollary '
    '`positivity_not_imp_simplicity`: the schema’s positivity Prop does not imply its simplicity Prop, exhibited by the sum of b596’s '
    'one-point toy on the line with itself, printed from the kernel Weil-positive, its point of multiplicity 2, failing the simplicity '
    'Prop. The salt-check `SaltCheckDoubling.lean`: a doubled sum Weil-positive, a doubled sum not (b590’s off-line toy), and a '
    'configuration Weil-positive with every point simple, so the non-implication is not an exclusion. All at the standard three, no '
    'sorryAx (relay data/b601_prints_doub.txt).', '',
    '**The Keiper face** (`(R211)`(4), by the work-order at OPEN_TRAILS :11704, re-priced at :12132). Lemma (1), '
    '`SIDEExplicitFormula/Keiper.lean`: the Stieltjes constants defined as the Taylor coefficients at 1 of Mathlib’s riemannZeta₀, the '
    'zeroth γ (riemannZeta₀_one, with tendsto_riemannZeta_sub_one_div read beside it), the residue riemannZeta_residue_one read at '
    'riemannZeta₁ 1; `KeiperTaylor`, Bulka’s Taylor coefficient of ξ as the binomial transform of the Taylor coefficients at 1 of 1/s, '
    'of (s − 1) ζ(s)’s and of Γℝ’s logarithmic derivatives, and `KeiperTaylorIdentity`, that identity with the power-series logarithm '
    'in the Stieltjes constants and the polygamma values at 1/2 as zeta values -- carried to `KeiperObligations` (the binomial '
    'transform, the split at 1, the power-series logarithm, the polygamma values), `keiperTaylorIdentity_of`. Proved beside it: the '
    'identity at n = 0 (`keiperTaylor_zero`), three of the obligations at their first index, and Keiper’s λ_1 = 1 + γ/2 − ½ log 4π '
    '(`liCoeff_one_keiper`), from Mathlib’s completedRiemannZeta₀_one, Complex.hasDerivAt_Gammaℝ_one and deriv_riemannZeta₁_one. Lemma '
    '(2), `SIDEExplicitFormula/KeiperBounds.lean`: the bench’s outward-rounded table for γ_0..γ_11 and ζ(2)..ζ(12) and `KeiperBounds`, '
    'carried to `BoundPremises` (γ to the table’s width, γ_1..γ_11, the zeta values), `keiperBounds_of`; every Stieltjes constant '
    'beyond γ a named premise, none assumed; proved beside it: γ_0 in Mathlib’s interval (1/2, 2/3). The salt-check '
    '`SaltCheckKeiper.lean`: each of the three summands of Keiper’s coefficient load-bearing at k = 0, the bound form satisfiable and '
    'refutable. Neither lemma closes without its premises (H35d refuted in its letter; the detector finds a closed row when one is '
    'planted). All at the standard three, no sorryAx (relay data/b601_prints_keip.txt). The federation walk finds no declaration '
    'outside this act’s files concluding any of its Props or a negation ({HEADERS} headers, all the act’s own).', '',
    '**The pages.** The ζ page re-emitted at v0.19 (PLACE-papers {ZCOMMIT}): the Keiper face’s ten declarations directly after '
    '`li_nonneg_iff_rh` -- the Li ladder’s arithmetic end at the page, `keiperTaylorIdentity_of` and `keiperBounds_of` with their '
    'premise structures printed, `keiperTaylor_zero` and `liCoeff_one_keiper` at T0; the doubling corollary’s four after the Product '
    'nodes, `doubling_holds` and `positivity_not_imp_simplicity` at T0. The χ page unchanged; page arms and the frozen control 2 of 2.', '',
    '**Its bearing** (relay data/b601_bearing.txt). For the corollary: SIMPLICITY_OF_RIEMANN_ZEROS v1.1.3 :82 and :180, whose “do not '
    'force” and single toy of multiplicity two become an operation on every configuration -- doubling keeps the criterion and doubles '
    'the multiplicities -- so a route from Weil positivity to the simplicity of ζ’s zeros has to use something the schema does not '
    'record; the sentences’ simplicity stays open. For the Keiper face: BALANCE_AND_POSITIVITY v0.9.5 :195, whose channel streams’ '
    'identification “is analysis, done outside the kernel”, now stated in the kernel on Mathlib’s objects with its obligations named '
    'and its first coefficient proved; and :308, the n = 1 row, whose margin is now the compiled identity λ_1 = 1 + γ/2 − ½ log 4π, '
    'λ_Z(1) = γ and λ_A(1) = 1 − (γ + log 4π)/2 -- its sign not certified in the kernel, since Mathlib’s interval for γ leaves λ_1 in '
    'an interval about zero.', '',
    '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the corollary re-reads b600’s product lemma (FINDINGS :6950, v0.18) at the '
    'diagonal and b596’s simplicity face (:6856, v0.17), turning its one toy into an operation; it is the compiled half of the reading '
    'at :{W2}. The Keiper face re-reads b566’s equality lemma (`li_coeff_eq_taylorCoeff`, v0.9) and b589’s three-way bench and Keiper '
    'read (:6718, :6728, :6738), which it meets at the price -- two lemmas, the constants beyond γ outside Mathlib -- and '
    'BALANCE_AND_POSITIVITY’s channel split; it is re-read by any act that certifies a finite-n sign in the kernel, which now has its '
    'premises named. It strengthens the programme’s offerings of the schema and its instances (the schema’s silence on multiplicity a '
    'theorem of the schema) and of the pages (the Li ladder’s arithmetic end at the page, its premises printed).', '',
    '**The record lines.** b600’s weight at FINDINGS :{W1}; `(R211)`(2)’s reading at :{W2}, entered as a reading and marked as the '
    'author’s strike item.', '',
]


def findings():
    Q = _Q()
    S, wl = jl('b601_scores.json'), jl('b601_weight_line.json')
    Z, gp = jl('b601_page_zeta.json'), jl('b601_grep.json')
    title = _title()
    Q.guard_absent(Q.FIND, title[:90])
    tagc = g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip()
    zcommit = _pp_commit('b601 (R211)(5): ' + PAGE)
    body = [x.replace('{TAGC}', tagc).replace('{ZCOMMIT}', zcommit).replace('{HEADERS}', str(len(gp.get('rows') or [])))
            .replace('{W1}', str(wl['lines'][0]['line'])).replace('{W2}', str(wl['lines'][1]['line'])) for x in FINDINGS_BODY]
    e = ['', title, '',
         '*Filed at b601 on the author’s ruling `(R211)`. Banks: relay `data/b601_statements_doub.txt`, `data/b601_statements_keip.txt`, '
         '`data/b601_statements_kbnd.txt`, `data/b601_build_*.txt`, `data/b601_prints_doub.txt`, `data/b601_prints_keip.txt`, '
         '`data/b601_e0_*.txt`, `data/b601_grep.txt`, `data/b601_page_zeta.json`, `data/b601_page_arms_c2.txt`, `data/b601_bearing.txt`, '
         '`data/b601_reads.txt`. Nothing deposits.*', ''] + body + [
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R211)`(6): b602, (E3)’s compiled window of the bench’s family at DETECTION-REGION (OPEN_TRAILS :12170), the '
         'research sequence’s fourth item. The author rules on the closing.', '',
         '*Nothing deposits; no keystone edited; README and REGISTRY unwritten; nothing here is a statement about RH, GRH or any zero beyond '
         'the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b601_findings.json', dict(entry_line=Q.line_of(Q.FIND, title[:90]), title=title, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, title[:90]))


TRAIL_BODY = [
    '**Entered:** FINDINGS.md:{W1} (b600’s weight), :{W2} (`(R211)`(2)’s reading, the author’s strike item), :{ENTRY} (the entry, with '
    'its mutual-light line); this record; SIDE-explicit-formula v0.19 = `{TAGC}` (Doubling.lean, SaltCheckDoubling.lean, Keiper.lean, '
    'KeiperBounds.lean, SaltCheckKeiper.lean, AxiomCheckDoubling.lean, AxiomCheckKeiper.lean; the branch doubling-keiper-b601 kept); '
    'the ζ page re-emitted at v0.19.', '',
    '**The obligations, named where the proofs stop** (the work-order’s two lemmas carried, not closed): lemma (1) at '
    '`keiperTaylorIdentity_of` on `KeiperObligations` -- (O1) the binomial transform, (O2) the logarithmic-derivative split at 1, (O3) '
    'the power-series logarithm, (O4) the polygamma values at 1/2, (O1)-(O3) proved at their first index; lemma (2) at '
    '`keiperBounds_of` on `BoundPremises` -- γ to the table’s width, γ_1..γ_11, ζ(2)..ζ(12). Each is a priced item for a later act; '
    'none is started.', '',
    '**Resolved by the seat, for the author’s strike:** the price bank’s riemannZeta₀ read as Mathlib’s declaration of that name at the '
    'pin (ZetaAsymp.lean :532) and consumed, with riemannZeta₁ and their lemmas, rather than re-made; the corollary in a sibling module, '
    'so Product.lean stays byte for byte at v0.18; the Keiper nodes placed directly after `li_nonneg_iff_rh` on the ζ page (H35e’s '
    'neighbours), renumbering the rows after it, and the doubling nodes after the Product nodes; the `(R211)`(2) reading appended after '
    'the weight line and addressed to :6950, the ledgers append-only; the bound table read from the bench at 60 digits and rounded '
    'outward at 10⁻³⁰, data until a premise or a proof meets it.', '',
    '**Defects (a)-(b), the seat’s** (relay data/b601_defects.txt): a suite predicate reading a wrapped #check on one line, corrected '
    'before any run over the bank; the N5 scorer requiring OPEN_TRAILS before the trail record, corrected and re-run.', '',
]


def trail():
    Q = _Q()
    S, fj, wl = jl('b601_scores.json'), jl('b601_findings.json'), jl('b601_weight_line.json')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    tagc = g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip()
    body = [x.replace('{TAGC}', tagc).replace('{W1}', str(wl['lines'][0]['line'])).replace('{W2}', str(wl['lines'][1]['line']))
            .replace('{ENTRY}', str(fj['entry_line'])) for x in TRAIL_BODY]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R211) ratified.** (1) b600 at its weight. (2) The reading b600 adds, for the record and the author’s strike. (3) The '
             'doubling corollary. (4) W-ORD-KEIPER-FACE, the two lemmas. (5) The tag v0.19 and the pages. (6) The act after: b602.', ''] + body + [
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R211)`(6), b602, (E3)’s compiled window of the bench’s family at DETECTION-REGION (OPEN_TRAILS :12170), the '
             'research sequence’s fourth item; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no keystone edited; FACES_LEDGER untouched; row U1 unedited; `h2` where the '
             'deposit left it; the four lists stay OPEN.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b601_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b601_trail.json')['line'])


DEF_HEAD = '*Appended 2026-10-02 by b601 to its own record (:%d), after the pre-push suite -- THE DEFECTS LINE CORRECTED:*'


def trail_defects():
    """### PLACE-papers OPEN_TRAILS: one dated line appended at the end, addressed to this act's record, carrying the defects the
    ### pre-push suite found after the record was written (the record's 'Defects (a)-(b)' left as written, the ledgers append-only)."""
    Q = _Q()
    tl = jl('b601_trail.json')['line']
    if Q.line_of(Q.OT, TRAIL_HEAD) != tl:
        sys.exit('### THE RECORD MOVED -- NOTHING WRITTEN')
    h = DEF_HEAD % tl
    Q.guard_absent(Q.OT, h)
    t = ('\n%s the record’s “Defects (a)-(b)” was written before the suite’s first pre-push run, which found three more, the seat’s '
         '(relay data/b601_defects.txt): (c) the E0 arm required each read’s tip to be the tag, while the doubling reads were taken at '
         '2b8abf5 with the files’ blobs identical at v0.19 -- the predicate corrected; (d) Keiper.lean and KeiperBounds.lean wrap the '
         'house form’s “NOT VENDORED” over a line end -- the arm’s needle corrected to read across it, the files standing at the tag; '
         '(e) AxiomCheckKeiper.lean omits the #check of two salt-check theorems, keiperTaylor_zero_holds and bounds_form_satisfiable '
         '(both printed at the standard three by #print axioms, their statements those of keiperTaylor_zero and stieltjes_zero_coarse), '
         'so G-SALT-CHECK fails in its letter and the suite reads 80 of 81, for the author. The tag is not moved.\n' % h)
    r = Q.append_to(Q.OT, t)
    put_json('b601_trail_defects.json', dict(head=h, line=Q.line_of(Q.OT, h), addressed=tl, append=r))
    print('  defects line :%s' % Q.line_of(Q.OT, h))


def desk():
    S = jl('b601_scores.json')
    HK = ('H35a', 'H35b', 'H35c', 'H35d', 'H35e')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b601 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H35a-H35e, (R211)(3)-(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HK]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H35 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HK), sum(S[k][0] == 'REFUTED' for k in HK),
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b601_defects.txt').rstrip(NL).split(NL)
    put_txt('b601_desk_notes.txt', L)


def components():
    S, fj, tj, wl = jl('b601_scores.json'), jl('b601_findings.json'), jl('b601_trail.json'), jl('b601_weight_line.json')
    Z, X = jl('b601_page_zeta.json'), jl('b601_page_chi.json')
    tagc = g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip()
    L = ['b601 -- THE COMPONENTS, BANKED UNDER (R211).', '',
         '### COMPONENT 0 : the process listing (two tail orphans stopped by PID) ; b600`s closing push-out relay %s ; push-b600* branches '
         'deleted by name (data/b601_branches.txt) ; the kept branches untouched ; the work-order printed whole (data/b601_reads.txt, '
         'data/b601_statements_keip.txt) ; the suite run at HEAD before the face (data/b601_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b600`s weight FINDINGS :%d ; (R211)(2)`s reading :%d, marked as the author`s strike item' % (wl['lines'][0]['line'], wl['lines'][1]['line']),
         '### COMPONENT 2 : the doubling corollary, Doubling.lean and SaltCheckDoubling.lean ; H35a %s, H35b %s' % (S['H35a'][0], S['H35b'][0]),
         '### COMPONENT 3 : the Keiper face, Keiper.lean, KeiperBounds.lean, SaltCheckKeiper.lean ; H35c %s, H35d %s, H35e %s' % (
             S['H35c'][0], S['H35d'][0], S['H35e'][0]),
         '### COMPONENT 4 : SIDE-explicit-formula %s = %s on %s merged ; the ζ page changed %s, the χ page changed %s ; the bearing '
         'data/b601_bearing.txt' % (TAG, tagc, BRANCH, Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b602, (E3)`s window at DETECTION-REGION ; N1 %s, '
         'N2 %s, N3 %s, N4 %s, N5 %s' % (fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b601_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b601_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
