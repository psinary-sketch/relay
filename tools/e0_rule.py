# -*- coding: utf-8 -*-
"""e0_rule.py -- THE E0 READ'S GRADING RULE, SHARED. ### Written at b568 under the author's ruling (R178)(2)(iii).

### ### **WHAT THIS IS.** Until b568 no shared E0 instrument existed: each act's record tool printed the rule at the head of
### its E0 bank and carried its own copy of the domain pattern (b566_record.py; b567_record.py :408-:439). The rule is
### now one module, imported by every reader that grades by it (b568_record.py's E0 read, tools/chain_page.py). It
### grades; it confers nothing on a ledger, and a grade it returns is a reading of a statement's binders.

### ### **THE RULE (b566's, with b567's reading and (R178)(2)(iii)'s rule):**
###   (1) A theorem is INTERFACES when an explicit hypothesis binder of its statement is a named Prop of a vendored or
###       kernel module (a premise passed through); DERIVES when its only binders are domain conditions.
###   (2) A domain condition is a binder whose type is an order or (in)equality relation, a membership, or a predicate
###       on the object's own data (DOMAIN below).
###   (3) (R178)(2)(iii), THE AUTHOR'S RULE: *a hypothesis that is one case of an exhaustive split on the object's own
###       data is a domain condition, not a premise, when both cases are present as declarations and the
###       exhaustiveness is itself compiled.* Each split the rule has been applied to is entered in SPLITS with its two
###       case declarations and the compiled exhaustiveness, by name and pin.
### ### **ITS INSTANCE (the occasion):** SIDE-explicit-formula v0.10 = 6baed63, SIDEExplicitFormula/Chi/Statement.lean --
### `gammaBracket_chi_of_even` (:51, binder `he : χ.Even`) and `gammaBracket_chi_of_not_even` (:59, binder
### `he : ¬ χ.Even`); the split is χ.Even / ¬ χ.Even, exhaustive by `Classical.em` (Lean core); beside it Mathlib's
### `DirichletCharacter.even_or_odd : ψ.Even ∨ ψ.Odd` (Mathlib/NumberTheory/DirichletCharacter/Basic.lean :538 at
### de5ce8a9; `Even` is `ψ (-1) = 1` at :536, `Odd` is `ψ (-1) = -1` at :533) and `not_even_and_odd` (:542). Both
### grade DERIVES (b567's E0 read, relay data/b567_e0_chi.txt), now under the rule and not a seat's reading.
"""
import re

RULE_TEXT = [
    '### THE E0 RULE (relay tools/e0_rule.py, shared from b568): a theorem is INTERFACES when an explicit hypothesis binder',
    '### of its statement is a named Prop of a vendored or kernel module (a premise passed through); DERIVES when its only',
    '### binders are domain conditions. A domain condition is an order or (in)equality relation, a membership, or a',
    '### predicate on the object`s own data. (R178)(2)(iii): a hypothesis that is one case of an exhaustive split on the',
    '### object`s own data is a domain condition, not a premise, when both cases are present as declarations and the',
    '### exhaustiveness is itself compiled (SPLITS, with its instance gammaBracket_chi_of_even / _of_not_even).',
]

DOMAIN = r'(?:≠|<|≤|=|∈|\.Even\b|IsPrimitive)'

SPLITS = [
    dict(cases=(r'^\s*\w+\.Even\s*$', r'^\s*¬\s*\w+\.Even\s*$'),
         decls=('SIDEExplicitFormula.GRHWeil.gammaBracket_chi_of_even', 'SIDEExplicitFormula.GRHWeil.gammaBracket_chi_of_not_even'),
         where='SIDE-explicit-formula v0.10 = 6baed63, SIDEExplicitFormula/Chi/Statement.lean :51, :59',
         exhaustive='Classical.em (χ.Even), Lean core; beside it DirichletCharacter.even_or_odd (Mathlib de5ce8a9, '
                    'NumberTheory/DirichletCharacter/Basic.lean :538)'),
]

BINDER = re.compile(r'\((h\w*) : ([^()]*(?:\([^()]*\)[^()]*)*)\)')


def split_case(t):
    """### the SPLITS entry whose case pattern the binder type matches, or None."""
    for s in SPLITS:
        if any(re.match(c, t) for c in s['cases']):
            return s
    return None


def grade(head, kind):
    """### RETURN `(grade, why, binders)` for a declaration header (the text between the name and `:=`).
    ### kind 'def' grades DEF. A binder is a premise unless DOMAIN matches its type or it is a SPLITS case."""
    if kind == 'def':
        return 'DEF', '', []
    binders = BINDER.findall(head)
    prem = [(b, t) for b, t in binders if not re.search(DOMAIN, t) and not split_case(t)]
    if prem:
        return 'INTERFACES', ', '.join('%s : %s' % bt for bt in prem), binders
    if binders:
        return 'DERIVES', 'domain conditions only: ' + ', '.join('%s : %s' % bt for bt in binders), binders
    return 'DERIVES', 'no hypothesis binder', binders


def self_test():
    """### both polarities, on synthetic headers written here."""
    cases = [
        ('(n : ℕ) : LiCoeff (n + 1) = x', 'theorem', 'DERIVES'),
        ('(hX : LiLimitExchange n) (c : ℕ → ℝ) : P', 'theorem', 'INTERFACES'),
        ('{χ : DirichletCharacter ℂ N} (he : χ.Even) (r : ℝ) : P', 'theorem', 'DERIVES'),
        ('{χ : DirichletCharacter ℂ N} (he : ¬ χ.Even) (r : ℝ) : P', 'theorem', 'DERIVES'),
        ('(hχ : χ ≠ 1) : P', 'theorem', 'DERIVES'),
        ('(h : Register4_positivity lam) : P', 'theorem', 'INTERFACES'),
        (': Prop', 'def', 'DEF'),
    ]
    return all(grade(h, k)[0] == want for h, k, want in cases)


if __name__ == '__main__':
    ok = self_test()
    print('\n'.join(RULE_TEXT))
    print('### self-test (seven headers, both polarities): %s' % ('PASS' if ok else 'FAIL'))
    raise SystemExit(0 if ok else 1)
