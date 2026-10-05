# -*- coding: utf-8 -*-
"""b625_worklist.py -- THE ACT'S DATA, UNDER (R235). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b625: LANE THREE, ACT FIFTY-TWO -- THE 2/3 THEOREM VENDORED FROM Zeta23 INTO SIDE-explicit-formula AT v0.22 AND
### exceptional_mass_le_third RE-READ; THE 33 LEDGER-AGAINST-RULE NODES CLASSED UNDER THE DOMAIN-CONDITION CRITERION; THE
### ROOT'S LIST WIDENED.
### Here: the pins before the act; the upstream clone and its pin; the four cells of finsetSum_insert; the seat's class of every
### binder of the 33 nodes ((R235)(2)), each with its reason; the nodes printed for the author's ruling; the vendored set's head
### line form; the hold.
"""
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
GS = 'D:/SIDE-global-section'
UP = 'D:/relay/data/anthropic-zeta23/formal-math'   # ### the upstream clone, anthropics/formal-math (untracked in relay)
PRE_PP = '52822a5'          # ### PLACE-papers main before the act (b624's record)
PRE_RELAY = '84bae29a'      # ### relay main before the act (b624's closing)
STEPZERO = '47875922'       # ### relay: b624's closing push-out bank, committed at step zero
NSREPAIR = 'e6781b18'       # ### relay: b624's defect (b) repaired in its data module, committed alone at step zero
DATE = '2026-10-05'
V017 = ('v0.17', '5a1630b')
UP_TAG, UP_PIN = 'v1.0', '3635e74826a4c1fcece7d1cd2b6fa75e43a00510'   # ### upstream: thmB₀_mult at Zeta23/FinalMult.lean :350
UP_FILE, UP_LINE = 'Zeta23/FinalMult.lean', 350
VENDOR_COMMIT = '52d8cf9'   # ### SIDE-explicit-formula v0: 57 modules vendored from zeta23 at v1.0 = 3635e74826a4
MAX_MODULES = 20            # ### (R235)(4): "if the closure exceeds twenty modules ... the act HOLDS"

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b622_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}

E0_FILES = ('tools/e0_rule.py', 'tools/test_e0_rule.py')
ROOT_FILES = ('tools/act_root.py', 'tools/test_act_root.py')
INSERT = 'SIDEExplicitFormula.Schema.Family.finsetSum_insert'
# ### the four ledger cells grading finsetSum_insert INTERFACES ((R235)(2) names them; the table's own reader at relay 84bae29a)
INSERT_CELLS = [('FINDINGS.md', 7058), ('OPEN_TRAILS.md', 12424), ('OPEN_TRAILS.md', 12434), ('OPEN_TRAILS.md', 12438)]
E0_LINE = 12436             # ### W-ORD-E0-INDUCTION, the E0 rule's line on OPEN_TRAILS (the clause is appended addressed to it)
ACT_ROOT_OT = 12210         # ### W-ORD-ACT-ROOT
B624_ENTRY = 7512           # ### b624's FINDINGS entry

# ### ### (R235)(2), THE SEAT'S CLASS OF EVERY BINDER OF THE 33 NODES, read at the pins through the generator (relay
# ### data/b625_e0_classes.txt prints each binder with its type). Classes: '(i)' an instance binder whose class is not Fact;
# ### '(ii)' a membership, non-membership, non-emptiness or finiteness condition on an object the statement names; '(iii)' a
# ### restriction on a variable the same statement quantifies universally; 'premise' a Prop about a fixed object the kernel
# ### names and does not derive; 'NONE' a binder no clause reaches (the node printed for the author's ruling).
# ### Keyed by the binder's type with its whitespace collapsed; the reason is the seat's.
R_SUPPORT = 'the support of the test function the statement quantifies'
R_SMOOTH = 'the smoothness of the test function the statement quantifies'
R_COMPACT = 'the compact support of the test function the statement quantifies'
R_CONT = 'the continuity of the test function the statement quantifies'
R_INTEG = 'the integrability of the test function the statement quantifies'
R_PARITY = 'the parity of the test function the statement quantifies'
R_NONNEG = 'the non-negativity of the test function the statement quantifies'
R_POS = 'a real`s positivity, the real quantified by the statement'
CLASS = {
    'ContDiff ℝ 4 g': ('(iii)', R_SMOOTH), 'ContDiff ℝ 4 φ': ('(iii)', R_SMOOTH), 'ContDiff ℝ n g': ('(iii)', R_SMOOTH),
    'ContDiff ℝ (2 * a.length) g': ('(iii)', R_SMOOTH), 'ContDiff ℝ a.length g': ('(iii)', R_SMOOTH),
    'Function.support g ⊆ Set.Icc (-L) L': ('(iii)', R_SUPPORT), 'Function.support g0 ⊆ Set.Icc (-L) L': ('(iii)', R_SUPPORT),
    'Function.support φ ⊆ Set.Icc (-L) L': ('(iii)', R_SUPPORT), 'Function.support h ⊆ Set.Icc (-L) L': ('(iii)', R_SUPPORT),
    'HasCompactSupport φ': ('(iii)', R_COMPACT), 'HasCompactSupport g': ('(iii)', R_COMPACT),
    'Continuous φ': ('(iii)', R_CONT), 'Continuous g': ('(iii)', R_CONT),
    'Integrable h': ('(iii)', R_INTEG),
    '∀ x, g0 (-x) = g0 x': ('(iii)', R_PARITY), '∀ x, φ (-x) = φ x': ('(iii)', R_PARITY), '∀ x, g (-x) = g x': ('(iii)', R_PARITY),
    '∀ x, 0 ≤ φ x': ('(iii)', R_NONNEG),
    '0 < ∫ u, φ u': ('(iii)', 'the positivity of the integral of the test function the statement quantifies'),
    '0 ≤ L': ('(iii)', R_POS), '0 < c': ('(iii)', R_POS), '0 < δ': ('(iii)', R_POS),
    'δ < 2 * γ₀': ('(iii)', 'a bound between two reals the statement quantifies'),
    'ρ₁ ∈ Z.carrier': ('(ii)', 'a membership in the carrier of the configuration the statement names'),
    'ρ₁.re ≠ 1 / 2': ('(iii)', 'a restriction on the point ρ₁ the statement quantifies'),
    '0 < offScore g ρ₁': ('(iii)', 'a positivity restriction on the point ρ₁ the statement quantifies'),
    'admissible F W': ('(iii)', 'the window family F and width set W the statement quantifies restricted to classK with the pole '
                                'term annihilated (Registers.lean :38, a def on F and W alone)'),
    'HStrip Z': ('(iii)', 'the configuration Z the statement quantifies restricted to the open strip (RestBound.lean :40, a def on Z`s '
                          'own carrier)'),
    'HCount Z A₀': ('(iii)', 'the configuration Z and the real A₀ the statement quantifies restricted by the local count '
                             '(RestBound.lean :44, a def on Z and A₀ alone)'),
    'I.is_universal': ('(iii)', 'the interface I the statement quantifies restricted to universal interfaces (RegisterDepth.lean :38, '
                                'a def on I`s own action)'),
    'χ.IsPrimitive': ('(iii)', 'the character χ the statement quantifies restricted to primitive characters'),
    'χ ≠ 1': ('(iii)', 'the character χ the statement quantifies restricted to the non-trivial ones'),
    'IsNontrivialZeroChi χ ρ': ('(ii)', 'a membership of ρ in the nontrivial zeros of L(s, χ) (Chi/ZeroConfig.lean :48)'),
    '∀ C ∈ sevenClasses, C Phi': ('premise', 'a Prop about the fixed objects Phi and sevenClasses the kernel names and does not '
                                             'derive (RegisterDepth.lean :81, :230); the membership is the quantifier`s range, not a '
                                             'condition on an object the statement names'),
    'a ∉ s': ('(ii)', 'a non-membership of a in the Finset s the statement names'),
    'ℝ → ℂ': ('NONE', 'not a Prop: the function the statement quantifies, read as a hypothesis binder by the rule`s name '
                     'pattern (h...); no clause of (R235)(2) speaks to a binder that is no condition'),
}
# ### a node no binder decides: its ledger cells grade it on a named Prop in its conclusion`s arrow, which the clause (binders)
# ### does not reach
NO_BINDER = {
    'SIDEExplicitFormula.B321.h2_sign_imp_rh_of_seam': 'no binder; its INTERFACES cells (FINDINGS :4648, CORRESPONDENCE :458) read '
                                                       'the named Prop rh_strip_imp_rh in the antecedent of the conclusion`s arrow, '
                                                       'which the clause, a reading of binders, does not reach',
}


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l


def norm(t):
    return ' '.join((t or '').split())
