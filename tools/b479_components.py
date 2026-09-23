# -*- coding: utf-8 -*-
"""b479_components.py -- COMPONENTS 1, 2 AND 3. ### Run after the seal (`8186f852c9bc6e9c...`).
### ### **NOTHING IS COMPILED, NO GRADE MOVES, NO BRIDGE IS TYPED.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


# ### ### **THE VERDICTS, AND THE WORDS EACH RESTS ON.** ### `clause` is quoted from the fact's own
# ### STATEMENT: for a TOUCH it is the constraining clause; for an APART it is the words that show
# ### the fact constrains something else.
VERDICTS = {
    'C1': ('APART', 'C1_realness',
           "∀ t : ℝ, (Φ t).im = 0",
           "the quantifier runs over `t : ℝ` and the predicate fixes an IMAGINARY PART of "
           "`Φ` itself. ### **NO TRANSFORM IS NAMED**, so the statement constrains the "
           "integrand on the real ray and reaches the form only through a derivation it does "
           "not carry."),
    'C2': ('TOUCHES THE FORM', 'C2_halfplane_nonvanishing',
           "∀ s : ℂ, 1 < s.re → mellin Φ (s / 2) ≠ 0",
           "### **THE CONSTRAINING CLAUSE IS `mellin Φ (s / 2) ≠ 0` ON THE FAMILY "
           "`1 < s.re`.** ### That is the transform `W`'s channels are read off, constrained on a "
           "half-plane the statement's own quantifier names -- and non-vanishing there is exactly "
           "what lets the prime channel be summed."),
    'C3': ('APART', 'C3_theta_transformation',
           "∀ t : ℝ, 0 < t → Φ (1 / t) = Real.sqrt t * Φ t + "
           "(Real.sqrt t - 1) / 2",
           "an identity for `Φ` on the positive reals. ### **IT NEVER MENTIONS THE MELLIN "
           "TRANSFORM.** ### The functional equation is what `C3` YIELDS through a derivation; "
           "### **IT IS NOT WHAT `C3` SAYS**, and the order asks for the statement."),
    'C4': ('APART', 'C4_modularity',
           "∃ F : ℂ → ℂ, ... F (2 + τ) = F τ ... "
           "F (-1 / τ) = (-I * τ) ^ (1/2) * F τ",
           "every clause quantifies over `τ` in the UPPER HALF-PLANE and constrains `F`, a "
           "function of `τ`. ### **NO TRANSFORM AND NO TEST FUNCTION APPEARS.** ### The "
           "file's own docstring says the spectral mathematics is *“the manuscript leg, cited "
           "there, not re-formalized here”*."),
    'C5': ('APART', 'C5_input',
           "∃ μ : ℤ → ℝ, (∀ n, 0 ≤ μ n) ∧ ∀ t, "
           "0 < t → HasSum (fun n => exp (-π * μ n * t)) (2 * Φ t + 1)",
           "a heat trace on `0 < t` with a non-negative spectrum. ### **NO TRANSFORM IS NAMED.** "
           "### The half that WOULD reach the form is `C5_output`, which places the spectrum on "
           "`ρ.re = 1/2` -- and it is ### **DISCLAIMED, DELIBERATELY OUTSIDE "
           "`sevenClasses`, AND CLAIMED BY NO THEOREM IN THE FILE.** ### It is NOT counted here."),
    'C6': ('APART', 'C6_holomorphic_extension',
           "∃ F : ℂ → ℂ, (∀ z, 0 < z.re → DifferentiableAt ℂ F z) "
           "∧ ∀ t, 0 < t → F t = Φ t",
           "an extension of `Φ` itself to the right half-plane. ### **IT CONSTRAINS THE "
           "INTEGRAND, NOT ITS TRANSFORM**, and names no family of test functions."),
    'C7': ('TOUCHES THE FORM', 'C7_entirety + C7_order',
           "∃ G, Differentiable ℂ G ∧ (∀ s, 1 < s.re → G s = "
           "mellin Φ (s / 2) + 1 / s + 1 / (1 - s)) ∧ ∃ A C, ∀ s, "
           "‖G s‖ ≤ C * exp (A * (‖s‖ * log (‖s‖ + 2)))",
           "### **THE CONSTRAINING CLAUSE IS `G s = mellin Φ (s / 2) + 1 / s + 1 / (1 - s)` "
           "ON `1 < s.re`, TOGETHER WITH THE GROWTH BOUND ON ALL OF `ℂ`.** ### It names the "
           "transform, completes it to an entire `G`, and bounds `G`'s order -- which is what "
           "gives the zero side of the form its shape at all. ### **THE ROW IS CARRIED BY "
           "`C7_order`**, since entirety alone does not give the bound, as the file's own "
           "docstring says."),
}
ORDER = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']
LABEL = {'C1': 'Schwarz reflection / realness', 'C2': 'Euler / multiplicative',
         'C3': 'functional equation / theta', 'C4': 'modular / PSL2(Z)',
         'C5': 'spectral', 'C6': 'Cauchy-Riemann / analyticity', 'C7': 'Hadamard'}


def main():
    SV = json.loads(read(os.path.join(D, 'b479_survey.json')))
    byname = {f['name']: f for f in SV['facts']}

    rec('=' * 108)
    rec('COMPONENT 1 -- THE SEVEN CLASSES, BY TERMINAL NAME AND STATEMENT, AT lv v0.10.0 = 93c27ec.')
    rec('=' * 108)
    rec('    ### ### **STATEMENTS, NOT DOCSTRINGS.** ### Read as TEXT by `git show`; nothing built.')
    rec('    ### `h1_complete_at_Phi` has ### **%d CONJUNCTS FOR SEVEN CLASSES** -- `C7` gives two.'
        % SV['conjuncts'])
    for cid in ORDER:
        rec('')
        rec('  ### **%s -- %s**' % (cid, LABEL[cid]))
        for f in SV['facts']:
            if f['cid'] != cid:
                continue
            rec('    coupling  `%s`  (`CouplingsAtPhi.lean:%d`)' % (f['name'], f['line']))
            for x in f['stmt'].split(NL):
                rec('        %s' % x)
            if f['discharge']:
                rec('    discharge `%s_at_Phi`  (`:%d`)' % (f['name'], f['dline']))
                rec('        %s' % f['discharge'].split(NL)[0])
            rec('    ### the statement names the Mellin transform : ### **%s**' % f['mentions_mellin'])

    rec('')
    rec('=' * 108)
    rec('COMPONENT 2 -- THE SEVEN-ROW TABLE.')
    rec('=' * 108)
    rec('    ### THE CRITERION, AS THE SEALED FACE FIXED IT BEFORE ANY VERDICT:')
    rec('    ### ### **A FACT TOUCHES THE FORM WHEN ITS STATEMENT CONSTRAINS THE OBJECT `W` IS')
    rec('    ### BUILT FROM -- THE MELLIN TRANSFORM OF `Φ` -- ON A FAMILY ITS OWN QUANTIFIER NAMES.**')
    rec('')
    rec('    %-5s %-30s %s' % ('class', 'label', 'verdict'))
    rec('    ' + '-' * 76)
    touch = []
    for cid in ORDER:
        v = VERDICTS[cid][0]
        rec('    %-5s %-30s ### **%s**' % (cid, LABEL[cid], v))
        if v.startswith('TOUCHES'):
            touch.append(cid)
    rec('')
    rec('    ### ### **TOUCHES THE FORM : %d -- %s. ### APART : %d.**'
        % (len(touch), ', '.join(touch), len(ORDER) - len(touch)))
    rec('')
    for cid in ORDER:
        v, name, clause, why = VERDICTS[cid]
        rec('  ### **%s -- %s** ### (`%s`)' % (cid, v, name))
        rec('      the statement, in brief : %s' % clause)
        head = ('THE CONSTRAINING CLAUSE, QUOTED' if v.startswith('TOUCHES')
                else 'WHY APART, IN THE FACT`S OWN WORDS')
        rec('      ### %s:' % head)
        for chunk in [why[i:i + 108] for i in range(0, len(why), 108)]:
            rec('        %s' % chunk)
        rec('')

    rec('=' * 108)
    rec('COMPONENT 3 -- THE SENTENCE THE TABLE SUPPORTS, AND NO WIDER.')
    rec('=' * 108)
    rec('')
    rec('  ### ### **WHICH CLASSES` EXCLUSIONS REACH THE FORM.**')
    rec('    ### ### **TWO OF THE SEVEN: `C2` AND `C7`.** ### Their statements are the only two that')
    rec('    ### name `mellin Φ (s / 2)` and constrain it on a family their own quantifiers give --')
    rec('    ### `C2` by non-vanishing on `1 < re s`, `C7` by completing it to an entire `G` and')
    rec('    ### bounding that `G`\'s order on all of `ℂ`.')
    rec('    ### ### **THE OTHER FIVE CONSTRAIN `Φ` AND NOT ITS TRANSFORM.** ### That is a statement')
    rec('    ### about what they SAY. ### **IT IS NOT A CLAIM THAT THEY ARE IRRELEVANT TO THE FORM**')
    rec('    ### -- `C3` yields the functional equation and `C1` the reflection symmetry, by')
    rec('    ### derivations the record holds elsewhere. ### **THOSE DERIVATIONS ARE NOT IN THESE')
    rec('    ### STATEMENTS, AND THIS ACT SCORES STATEMENTS.**')
    rec('')
    rec('  ### ### **AND ONE OF THE TWO IS HALF OPEN.** ### `C7_order` carries its row, and the')
    rec('    ### file\'s own docstring marks it ### **OPEN** ### -- *"Formalising C₇-order is')
    rec('    ### therefore a Γ-asymptotics project, not a corollary of what exists."* ### So of the')
    rec('    ### two classes whose statements reach the form, ### **ONE REACHES IT THROUGH A')
    rec('    ### CONJUNCT THE REPOSITORY HAS NOT DISCHARGED.**')
    rec('')
    rec('  ### ### **WHAT EXHAUSTIVENESS WOULD SAY, IF THOSE CLASSES ALONE CARRIED IT.**')
    rec('    ### ### **THE CONDITIONAL IS NOT DISCHARGED AND NOTHING BELOW IS ASSERTED OF THE')
    rec('    ### RECORD.** ### The stem `inerti` was searched in `FINDINGS.md` and `REGISTRY.md` and')
    rec('    ### ### **THE VOCABULARY IS NOT AT AN ADDRESS IN EITHER**, so the sentence is written')
    rec('    ### in the vocabulary the order names WITHOUT claiming the record carries it:')
    rec('')
    rec('      ### *IF the exclusions that reach Weil`s form were carried by `C2` and `C7` alone,')
    rec('      ### then exhaustiveness over the seven classes would not be the operative claim:')
    rec('      ### the operative claim would be that the form is inert to the other five --- that')
    rec('      ### `C1`, `C3`, `C4`, `C5` and `C6` constrain the integrand in ways that leave `W`')
    rec('      ### unmoved on every family of test functions. ### And that inertia is NOT what the')
    rec('      ### seven-class argument asserts: it asserts that the five SUPPLY constraints, not')
    rec('      ### that they leave the form free.*')
    rec('')
    rec('    ### ### **SO THE TABLE SUPPORTS A NARROWER SENTENCE THAN THE SEVEN-CLASS ARGUMENT')
    rec('    ### NEEDS, AND THE DIFFERENCE IS WHERE THE DERIVATIONS LIVE.** ### The five classes`')
    rec('    ### route to the form runs through steps their Lean statements do not contain.')
    rec('    ### ### **THAT IS A MEASUREMENT OF THE FORMALISATION`S REACH, NOT OF THE ARGUMENT`S')
    rec('    ### TRUTH**, and this act makes no claim about the latter.')
    rec('')
    rec('  ### ### **AND `h2` IS QUOTED AND NOT DISCHARGED.** ### `h1_complete_at_Phi`\'s own')
    rec('    ### docstring: *"`h2` (nonvanishing of the Mellin transform at the operative point)')
    rec('    ### remains the outstanding obligation."* ### **h2 IS WHERE THE DEPOSIT LEFT IT.**')

    io.open(os.path.join(D, 'b479_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(verdicts={c: VERDICTS[c][0] for c in ORDER}, touch=touch,
                   apart=[c for c in ORDER if c not in touch], conjuncts=SV['conjuncts']),
              io.open(os.path.join(D, 'b479_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
