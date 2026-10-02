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
    '### (R180)(2)(f): a binder restricting a variable to the class the statement is about (ContDiff, HasCompactSupport or',
    '### IsCompact of a variable the conclusion mentions) is a domain condition; on a variable the conclusion does not',
    '### mention it is a premise (CLASS_PREDS, class_case).',
    '### (R201)(3), b591: a binder inside an existential in a theorem`s conclusion is part of the conclusion and not a premise',
    '### (exist_spans: from an ∃ in the conclusion to its top-level comma); every binder before the conclusion is read as before.',
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

# ### ### **(R180)(2)(f), b570: THE CLASS-MEMBERSHIP CLAUSE.** *A binder that restricts a variable to the class the
# ### statement is about -- the test-function class EF_lit quantifies over (smoothness, compact support, IsCompact of the
# ### support) -- is a domain condition and not a premise.* Read here as: the binder's type is one of CLASS_PREDS applied
# ### to a variable `v` (its last token), and `v` occurs in the statement's CONCLUSION (the text after the binder list):
# ### the statement is about that variable's class. A class predicate on a variable the conclusion does not mention is a
# ### premise, as before. ### Its instance (the occasion): SIDE-explicit-formula v0.11 = 19b7d1e, Chi/LocalCount.lean
# ### `LFunction_zeros_finite_of_isCompact` (hK : IsCompact K) and Chi/ZeroSummability.lean `EF_zero_sum_summable_chi`
# ### (hk : ContDiff ℝ 2 k) (hkc : HasCompactSupport k) -- b569's defect (f).
CLASS_PREDS = re.compile(r'^\s*(?:ContDiff|HasCompactSupport|IsCompact)\b.*?([A-Za-z_][\w\']*)\s*$')


def conclusion(head):
    """### the text after the leading binder groups ( ), { }, [ ], ⦃ ⦄ of a header, from its ':' on; '' when none."""
    pairs = {'(': ')', '{': '}', '[': ']', '⦃': '⦄'}
    i, n = 0, len(head)
    while True:
        while i < n and head[i].isspace():
            i += 1
        if i < n and head[i] in pairs:
            depth, j = 0, i
            while j < n:
                if head[j] in pairs:
                    depth += 1
                elif head[j] in pairs.values():
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            i = j + 1
            continue
        break
    rest = head[i:].lstrip()
    return rest[1:] if rest.startswith(':') else ''


# ### ### **(R201)(3), b591: THE EXISTENTIAL-BINDER CLAUSE.** *A binder inside an existential in a theorem's conclusion is
# ### part of the conclusion and not a premise.* Read here as: a hypothesis binder whose text lies within an existential's
# ### binder list in the header's conclusion -- from an `∃` to its top-level comma -- is not read as a premise; every binder
# ### before the conclusion is read as before. ### Its instance (the occasion): SIDE-explicit-formula v0.16 = c404e72,
# ### Schema/SaltCheckEpstein.lean `membership_load_bearing : ∃ (Z : …) (rhs : …) (hP : EpsteinPremises Z rhs), …`, which
# ### the rule read INTERFACES on `hP` at b590 (relay data/b590_e0_salt.txt :27); its outer-binder neighbour
# ### `epstein_not_h2_sign_cfg (hP : EpsteinPremises Z rhs) (hE : rhoE ∈ Z.carrier)` stays INTERFACES.
def conclusion_start(head):
    """### the index in `head` where its conclusion begins (just after the ':'), or None when the header has none."""
    pairs = {'(': ')', '{': '}', '[': ']', '⦃': '⦄'}
    i, n = 0, len(head)
    while True:
        while i < n and head[i].isspace():
            i += 1
        if i < n and head[i] in pairs:
            depth, j = 0, i
            while j < n:
                if head[j] in pairs:
                    depth += 1
                elif head[j] in pairs.values():
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            i = j + 1
            continue
        break
    return i + 1 if head[i:i + 1] == ':' else None


def exist_spans(head):
    """### the [start, end) spans of every existential binder list in the conclusion: an `∃` to its top-level comma."""
    s = conclusion_start(head)
    if s is None:
        return []
    opens, closes = '([{⦃⟨', ')]}⦄⟩'
    out = []
    for p in range(s, len(head)):
        if head[p] != '∃':
            continue
        depth, q = 0, p + 1
        while q < len(head):
            ch = head[q]
            if ch in opens:
                depth += 1
            elif ch in closes:
                depth -= 1
                if depth < 0:
                    break
            elif ch == ',' and depth == 0:
                break
            q += 1
        out.append((p, q))
    return out


def class_case(t, head):
    """### True when the binder type `t` is a CLASS_PREDS predicate on a variable the header's conclusion mentions."""
    m = CLASS_PREDS.match(t)
    if not m:
        return False
    return re.search(r'(?<![\w.\'])' + re.escape(m.group(1)) + r'(?![\w\'])', conclusion(head)) is not None


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
    spans = exist_spans(head)
    binders = [m.groups() for m in BINDER.finditer(head) if not any(a <= m.start() < b for a, b in spans)]
    prem = [(b, t) for b, t in binders if not re.search(DOMAIN, t) and not split_case(t) and not class_case(t, head)]
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
