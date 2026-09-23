# -*- coding: utf-8 -*-
"""b482_components.py -- COMPONENTS 1, 2 AND 3. ### Run after the seal (`8ce9439063b28a4e...`).
### ### **NO LEAN IS RUN, NOTHING IS IMPORTED, NO GRADE IS CONFERRED.** ### The kernel lane is open
### to READ STATEMENTS AT A PIN and closes at the act's end.
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


# ### ### **THE PLACEMENT, DECLARED AS DATA AND NOT WRITTEN AS PROSE.** ### Each cell carries its
# ### verdict AND, where the verdict is not `APART`, ### **THE DECIDING CLAUSE, QUOTED FROM BOTH
# ### SIDES** -- so that a reader can check the verdict against the two texts it rests on.
SHARE_XIP = ("both quantify over `xiDeriv` / `deriv completedRiemannZeta₀` -- "
             "THE SAME FUNCTION -- and both speak of the critical line")
PLACEMENT = {
    'xiPrime_zeros_in_open_critical_strip': {
        'A': ('TOUCHES',
              "corpus: *“At every simple zero ρ on the critical line, ξ'(ρ) is "
              "purely imaginary”* ; declaration: `∀ ρ : ℂ, "
              "XiPrime.xiDeriv ρ = 0 → 0 < ρ.re ∧ ρ.re < 1`. "
              "### **THE SHARED TERM IS `ξ'`; THE QUANTIFIED SET IS NOT.** The clause ranges "
              "over ZEROS OF `ξ`, the declaration over ZEROS OF `ξ'`."),
        'B': ('TOUCHES',
              "corpus: `(deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0` for ALL `t` ; "
              "declaration: every zero of `ξ'` has `0 < re < 1`. "
              "### **ONE FIXES A VALUE OF `ξ'` ON THE LINE, THE OTHER LOCATES ITS ZEROS IN THE "
              "STRIP.** Same function, different predicate; neither implies the other."),
        'C1': ('APART', None), 'C2': ('APART', None)},
    'xiPrime_over_xi_re_pos': {
        'A': ('APART', None), 'B': ('APART', None),
        'C1': ('APART', None), 'C2': ('APART', None)},
    'xiPrime_simple_zeros_on_critical_line': {
        'A': ('TOUCHES', SHARE_XIP), 'B': ('TOUCHES', SHARE_XIP),
        'C1': ('APART', None), 'C2': ('APART', None)},
    'xiPrime_simple_zeros_on_critical_line_cumulative': {
        'A': ('TOUCHES', SHARE_XIP), 'B': ('TOUCHES', SHARE_XIP),
        'C1': ('APART', None), 'C2': ('APART', None)},
    'xiPrime_simple_zeros_on_critical_line_quartic': {
        'A': ('TOUCHES', SHARE_XIP), 'B': ('TOUCHES', SHARE_XIP),
        'C1': ('APART', None), 'C2': ('APART', None)},
    'xiPrime_simple_zeros_on_critical_line_quartic_cumulative': {
        'A': ('TOUCHES', SHARE_XIP), 'B': ('TOUCHES', SHARE_XIP),
        'C1': ('APART', None), 'C2': ('APART', None)},
}
KEYS = [('A', 'the geometric clause'), ('B', 'spectral_cannon'),
        ('C1', 'transversal_generic_empty'), ('C2', 'codim_margin')]


def main():
    SV = json.loads(read(os.path.join(D, 'b482_survey.json')))
    six = SV['six']
    comp = SV['comparator']
    corpus = {c['key'] if c['key'] != 'C' else c['name']: c for c in SV['corpus']}
    byname = {c['name']: c for c in SV['corpus']}

    rec('=' * 108)
    rec('COMPONENT 1 -- THE SIX STATEMENTS, AT THE PIN `%s`.' % SV['pin'][:7])
    rec('=' * 108)
    for d in six:
        rec('')
        rec('  ### `%s`   (`Challenge/XiPrime.lean:%d`)' % (d['name'], d['line']))
        for s in d['stmt'].split(NL):
            rec('      %s' % s)
    rec('')
    rec('  ### ### **EVERY ONE OF THE SIX IS CLOSED BY `sorry` -- %d IN THE FILE.** ### They are'
        % SV['sorries'])
    rec('  ### ### **CHALLENGE STATEMENTS, NOT THEOREMS HELD.** ### Nothing below says otherwise.')
    rec('')
    rec('  ### THE COMPARATOR, `comparator-xiprime.json`:')
    rec('    challenge module : %s ; solution module : %s'
        % (comp['challenge_module'], comp['solution_module']))
    rec('    `theorem_names` (%d) : the SAME SET as the file`s theorems.' % len(comp['theorem_names']))
    rec('    `definition_names` : ### **EMPTY** -- the eight `def`s are NOT under comparison.')
    rec('    ### ### **PERMITTED AXIOMS : %s.**' % ', '.join(comp['permitted_axioms']))
    rec('    ### Those are the three Lean`s own `#print axioms` calls standard; ### **THEY ARE NOT A')
    rec('    ### LICENCE FOR AN EXTRA HYPOTHESIS**, and the corpus`s own `(R-)`statement-form rule')
    rec('    ### applies to them exactly as it does to a corpus terminal.')

    rec('')
    rec('=' * 108)
    rec('COMPONENT 2 -- THE CORPUS`S OWN STATEMENTS. ### **STATEMENTS, NOT DOCSTRINGS.**')
    rec('=' * 108)
    for key, label in KEYS:
        c = byname.get(label) or corpus.get(key)
        if c is None:
            continue
        rec('')
        rec('  ### (%s) ### **%s** ### -- `%s`' % (key, c['name'], c['addr']))
        for s in c['text'].split(NL):
            rec('      %s' % s[:140])
    rec('')
    rec('  ### the tags these are read at : ### **the deposited copy** ### for (A);')
    rec('  ### ### **SIDE-kernel `v1.5`** ### for (B); ### **SIDE-simplicity `v0.1.0`, its latest')
    rec('  ### tag** ### for (C1) and (C2).')
    rec('  ### ### **AND (C1) AND (C2) QUANTIFY OVER `ℤ` AND NOTHING ELSE.** ### Neither mentions')
    rec('  ### `ξ`, `ζ`, a zero, or a complex number; `curveDim` and `numSources` are integer')
    rec('  ### constants and both are closed by `omega`. ### **THE MATHEMATICS THEY ARE NAMED FOR')
    rec('  ### LIVES IN THEIR DOCSTRINGS**, which the order excludes. ### This is a fact about what')
    rec('  ### the statements SAY and ### **IS NOT A JUDGEMENT ON THE REPOSITORY.**')

    rec('')
    rec('=' * 108)
    rec('COMPONENT 3 -- THE PLACEMENT. ### ONE VERDICT PER DECLARATION PER CORPUS STATEMENT.')
    rec('=' * 108)
    rec('')
    rec('  %-52s %-10s %-10s %-10s %s' % ('declaration', '(A)', '(B)', '(C1)', '(C2)'))
    rec('  ' + '-' * 100)
    counts = {}
    for d in six:
        row = PLACEMENT[d['name']]
        rec('  %-52s %-10s %-10s %-10s %s'
            % (d['name'][:52], row['A'][0], row['B'][0], row['C1'][0], row['C2'][0]))
        for k in ('A', 'B', 'C1', 'C2'):
            counts[row[k][0]] = counts.get(row[k][0], 0) + 1
    rec('')
    rec('  ### ### **CELLS : %d. ### `SAME OBJECT` : %d. ### `TOUCHES` : %d. ### `APART` : %d.**'
        % (sum(counts.values()), counts.get('SAME OBJECT', 0), counts.get('TOUCHES', 0),
           counts.get('APART', 0)))
    rec('')
    rec('  ### THE DECIDING CLAUSE FOR EVERY NON-`APART` CELL:')
    seen = set()
    for d in six:
        row = PLACEMENT[d['name']]
        for k in ('A', 'B', 'C1', 'C2'):
            v, why = row[k]
            if v == 'APART':
                continue
            rec('')
            rec('    ### `%s`  ×  (%s) : ### **%s**' % (d['name'], k, v))
            if why in seen:
                rec('        (the deciding clause is the one printed above for this pair of kinds)')
                continue
            seen.add(why)
            for chunk in [why[i:i + 116] for i in range(0, len(why), 116)]:
                rec('        %s' % chunk)
    rec('')
    rec('  ### ### **AND EVERY `APART` CELL AGAINST (C1) AND (C2) HAS ONE REASON:** ### those two')
    rec('  ### statements contain no complex number, no `ξ`, and no zero -- ### **THERE IS NO SHARED')
    rec('  ### OBJECT TO BE THE SAME AS OR TO TOUCH.**')
    rec('  ### ### **AND `xiPrime_over_xi_re_pos` IS `APART` FROM (A) AND (B) FOR A DIFFERENT')
    rec('  ### REASON:** it quantifies over the half-plane `1 ≤ s.re`, and (A) and (B) both')
    rec('  ### speak of the CRITICAL LINE `re = 1/2`. ### **THE REGIONS ARE DISJOINT**, so the')
    rec('  ### statements cannot bear on one another at all.')

    rec('')
    rec('  ### (3b) THE TWO REVERSE READS.')
    rec('  ' + '-' * 100)
    rec('    ### ### **(i) WHAT THE SIX STATE THAT THE CORPUS DOES NOT.**')
    rec('      - ### **A POSITIVE PROPORTION, WITH A NUMBER.** ### `0.85838` and `0.92919`, and')
    rec('        `0.86864` and `0.93432` in the quartic window. ### **THE CORPUS STATES NO')
    rec('        PROPORTION OF THE ZEROS OF `ξ\'` ANYWHERE**, in any tag read here.')
    rec('      - ### **THE LOCATION OF EVERY ZERO OF `ξ\'`.** ### `0 < ρ.re ∧ ρ.re < 1` for every')
    rec('        zero of `ξ\'`. ### The corpus`s clause (A) speaks of `ξ\'` only AT ZEROS OF `ξ`.')
    rec('      - ### **A HALF-PLANE POSITIVITY FOR `ξ\'/ξ`.** ### `0 < (ξ\'(s)/ξ(s)).re` for')
    rec('        `1 ≤ s.re`. ### Nothing in the three corpus sources mentions that quotient.')
    rec('      - ### **AND A COUNTING APPARATUS**: `Ncount`, `Ndist`, `N0simple` with multiplicity')
    rec('        in the denominator. ### **THE CORPUS HAS NO SUCH APPARATUS FOR `ξ\'`.**')
    rec('')
    rec('    ### ### **(ii) WHAT THE CORPUS STATES THAT THE SIX DO NOT.**')
    rec('      - ### **A POINTWISE VALUE OF `ξ\'` AT EVERY POINT OF THE CRITICAL LINE.** ###')
    rec('        `spectral_cannon` gives `(deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0` for ALL')
    rec('        `t : ℝ` -- ### **NOT ONLY AT ZEROS** -- and ### **IT IS PROVED, NOT POSED.**')
    rec('        ### None of the six states any value of `ξ\'` at any point.')
    rec('      - ### **THE CODIMENSION DICHOTOMY FOR THE ZEROS OF `ξ`** (clause (A)`s setting): a')
    rec('        zero on the line is a codimension-1 condition, off it codimension-2. ### The six')
    rec('        say nothing about `ξ`\'s own zeros.')
    rec('      - ### **AND AN INTEGER MARGIN**: (C1) and (C2). ### The six state no integer fact.')
    rec('')
    rec('    ### ### **THE ASYMMETRY WORTH NAMING:** the corpus`s one PROVED statement about `ξ\'`')
    rec('    ### is ### **STRONGER POINTWISE** ### than anything the six assert about `ξ\'`\'s value')
    rec('    ### -- it holds at every `t`, not only at zeros -- while the six assert ### **A')
    rec('    ### QUANTITATIVE COUNT THE CORPUS NEVER ATTEMPTS.** ### **NEITHER SIDE SUBSUMES THE')
    rec('    ### OTHER, AND NO CELL IS `SAME OBJECT`.**')
    rec('  ### ### **NO GRADE IS CONFERRED ON ANY CORPUS OBJECT BY THIS PLACEMENT.**')

    io.open(os.path.join(D, 'b482_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(placement={k: {kk: vv[0] for kk, vv in v.items()} for k, v in PLACEMENT.items()},
                   counts=counts, cells=sum(counts.values())),
              io.open(os.path.join(D, 'b482_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
