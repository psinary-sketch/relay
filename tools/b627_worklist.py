# -*- coding: utf-8 -*-
"""b627_worklist.py -- THE ACT'S DATA, UNDER (R237). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b627: LANE THREE, ACT FIFTY-FOUR -- THE POSITIVITY MARGIN AT HEIGHT: THE v0.20 WINDOW EVALUATED FROM THE PRIME SIDE AT THE
### LOWEST ZEROS TO CERTIFIED PRECISION; THE SEAM EQUIVALENCE RULED; THE BOUNDED SHAPE ENTERED; THE CLOSING FORM AMENDED.
### Here: the pins before the act; ch_iff_h2_sign_of_seam and its DERIVES cells ((R237)(2)); the generator's files and the nodes the
### BOUNDED word moves ((R237)(3)); the next act's terminals and their pins ((R237)(4), (6)); the bench's parameters as the author
### answered before the seal, each with the kernel line it comes from ((R237)(5)).
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
GS = 'D:/SIDE-global-section'
FM = 'D:/relay/data/anthropic-zeta23/formal-math'   # ### the upstream clone b625 read (untracked in relay), read here by git show
PRE_PP = 'a43e1ba'          # ### PLACE-papers main before the act (b626's record)
PRE_RELAY = '746ab804'      # ### relay main before the act (b626's closing)
PRE_GS = 'dbacb9f'          # ### SIDE-global-section main before the act
PRE_KER = 'e939c92'         # ### SIDE-explicit-formula main before the act = v0.22, untouched by this act
STEPZERO = '152039e5'       # ### relay: b626's closing push-out bank, committed at step zero
DATE = '2026-10-05'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b626_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
PROBE = {'zeta': 'b626_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}

# ### (R237)(2): the seam equivalence, ruled INTERFACES on rh_strip_imp_rh; its two DERIVES cells, read from the table at PRE_RELAY
CHIFF = 'SIDEExplicitFormula.B321.ch_iff_h2_sign_of_seam'
CHIFF_TRAIL = 10884                       # ### OPEN_TRAILS :10884, its DERIVES cell there
CHIFF_CORR = [(383, CHIFF)]               # ### CORRESPONDENCE row 383 (line 456, b534), its DERIVES cell there
CHIFF_STMT = ('PowerLimit.lean', 1240)    # ### at v0.22: theorem ch_iff_h2_sign_of_seam : rh_strip_imp_rh → (conservationHypothesis ↔ h2_sign)

# ### (R237)(3): the BOUNDED word in the quantifier column
GEN_FILES = ('tools/chain_page.py', 'tools/test_chain_page_b596.py')
RUNG_NODES = ['SIDEExplicitFormula.PlattRung.rh_upto', 'SIDEExplicitFormula.PlattRung.forall_rh_upto_iff_rh',
              'SIDEExplicitFormula.PlattRung.plattTrudgianT', 'SIDEExplicitFormula.PlattRung.PlattTrudgianHeight',
              'SIDEExplicitFormula.PlattRung.rh_upto_platt']
BOUNDED_WANT = ['SIDEExplicitFormula.PlattRung.PlattTrudgianHeight', 'SIDEExplicitFormula.PlattRung.rh_upto',
                'SIDEExplicitFormula.PlattRung.rh_upto_platt']     # ### measured before the seal: the three, UNIVERSAL -> BOUNDED
GEN_CONTROL_FAILING = ['(10)', '(11)']

# ### (R237)(4) and (6): the next act's terminals, each at its pin -- route (b) of W-ORD-VENDOR-FINALMULT (OPEN_TRAILS :12970) or
# ### W-ORD-NYMAN-BEURLING-FACE (:12893), which names no kernel terminal yet
NEXT_ROUTES = [
    ('route (b) of W-ORD-VENDOR-FINALMULT (OPEN_TRAILS :12970)', [
        ('Zeta23.thmB₀_mult', FM, '3635e748', 'Zeta23/FinalMult.lean', 350),
        ('SIDEExplicitFormula.Simplicity.SimpleProportion', KER, 'v0.22', 'SIDEExplicitFormula/Simplicity.lean', 40),
        ('SIDEExplicitFormula.Simplicity.exceptional_mass_le_third', KER, 'v0.22', 'SIDEExplicitFormula/Simplicity.lean', 45)]),
    ('W-ORD-NYMAN-BEURLING-FACE (OPEN_TRAILS :12893)', [])]

# ### (R237)(5) as the author answered before the seal: the bench
BENCH_SCRIPT = 'tools/b627_margin.py'
W, H_NUM, H_DEN, P = 4, 1, 3, 6          # ### W = 4, h = 1/3, p = 6 (the classK floor of WindowInClassK, PlateauRamp.lean :156-:158)
L_SUPPORT = 5                            # ### L = W + p·h/2
NMAX = 22026                             # ### the prime sum over n ≤ e^10: k_t is supported in [-2L, 2L] = [-10, 10]
PREC = 200                               # ### bits, python-flint Arb balls throughout
DELTA = 1200                             # ### the archimedean integral cut at t + DELTA, the closed-form tail beyond it added to the radius
N_ORD = 100
ZERO_URL = 'https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros2'
KPIN = 'v0.20'
KERNEL_LINES = [('SIDEExplicitFormula/Schema/PlateauRamp.lean', (45, 48, 51, 55, 56, 57, 151, 152, 153, 156, 157, 158)),
                ('SIDEExplicitFormula/B321Identity.lean', (24, 25, 26, 29, 30, 33, 34, 37, 38, 44, 45, 46)),
                ('Zeta23/ExplicitFormula.lean', (64, 68, 80)),
                ('Zeta23/Defs.lean', (60,)),
                ('SIDEExplicitFormula/H2Sign.lean', (24, 25, 26))]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
