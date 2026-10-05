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
    '### (R234)(2), b624: the grade is read from the statement`s binders alone -- a hypothesis the proof introduces (by induction,',
    '### by cases, by a match arm, by intro inside the proof term) is no binder of the statement (statement_only cuts a header where',
    '### a proof begins inside it); a non-membership (∉) is a domain condition as a membership is; a theorem one of whose explicit',
    '### hypothesis binders has the conclusion itself as its type, its bound variables abstracted, reads ENCODES-CONCLUSION.',
    '### (R235)(2), b625, THE DOMAIN-CONDITION CRITERION: a binder is a domain condition, and does not enter the grade, when it is',
    '### (i) an instance binder whose class is not Fact; (ii) a membership, non-membership, non-emptiness or finiteness condition on',
    '### an object the statement names; (iii) a restriction on a variable the same statement quantifies universally (support,',
    '### parity, smoothness, continuity, integrability; a real`s positivity; a natural`s bound). A binder is a premise when it asserts',
    '### a Prop about a fixed object the kernel names and does not derive (a structure of premises, an EF_lit_* hypothesis, a Fact',
    '### instance, a Summable or HasSum of the kernel`s own series). Read here: a Fact instance a premise (INSTANCE); non-emptiness',
    '### and finiteness in DOMAIN; continuity, integrability and the support inclusion beside CLASS_PREDS, on a variable the',
    '### statement binds and its conclusion mentions; the named restrictions the seat read at their pins (RESTRICTIONS) on such',
    '### variables alone; a',
    '### bounded quantifier`s range (∀ x ∈ S,) no condition on a named object, its body read in its place (strip_range).',
    '### (R236)(2), b626: (i) SEAM ANTECEDENTS -- a Prop that is the antecedent of a top-level implication in the conclusion is',
    '### read as a binder when it is itself a named implication between open statements, a SEAMS entry (seam_antecedents), the',
    '### author`s answer before b626`s seal narrowing the ruled reading of every antecedent; a plain A -> B keeps DERIVES;',
    '### (ii) DATA BINDERS -- a binder whose type is not a Prop (a function, a real, a natural, a character) is an object of the',
    '### statement and not a hypothesis whatever its name (data_binder). (R236)(3): each named restriction names the quantified',
    '### variable it restricts; an entry that cannot is struck.',
]

DOMAIN = r'(?:≠|<|≤|=|∈|∉|\.Even\b|IsPrimitive|\.Nonempty\b|\bNonempty\b|\.Finite\b|\bSet\.Finite\b|\bFinite\b)'

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


# ### ### **(R234)(2), b624: THE STATEMENT'S BINDERS ALONE, NON-MEMBERSHIP, AND THE CONCLUSION AS A BINDER.**
# ### *A hypothesis the proof introduces -- by induction, by cases, by a match arm, by intro inside the proof term -- is not a
# ### binder of the statement and does not enter the grade; the grade is read from the statement's binders alone.* Read here
# ### as: a header handed in without `:=` (a proof by match arms, `| 0 => ... | j + 1 => ...`) is cut where its first arm
# ### begins (statement_only), so neither the arms nor any text a reader carried past them is read. Its instance (the occasion):
# ### SIDE-explicit-formula v0.21 = 1d5d4dd, PowerWindow.lean :139 `power_contDiff`, whose header the page generator read on
# ### through its arms into the next theorem's binders (hev, hg, hs). An induction hypothesis (`ih` in finsetSum_productLemma,
# ### Schema/Family.lean :136) lives after `:=` and never reached the rule. *A non-membership is a domain condition as a
# ### membership is* (the author's answer before b624's seal): `∉` joins DOMAIN; its instance `finsetSum_insert` (Family.lean
# ### :130, `h : a ∉ s`). *A theorem one of whose explicit hypothesis binders has the conclusion itself as its type reads
# ### ENCODES-CONCLUSION* (the author's answer): equality is syntactic after the bound variables of each side are abstracted
# ### (alpha), so an alpha-variant is caught and a merely similar Prop is not.
def statement_only(head):
    """### the header cut where a proof begins inside it: the first match arm `|` at bracket depth 0 after the conclusion
    ### starts; a header with no such arm is returned whole."""
    s = conclusion_start(head)
    if s is None:
        return head
    depth = 0
    for i in range(s, len(head)):
        ch = head[i]
        if ch in '([{⦃⟨':
            depth += 1
        elif ch in ')]}⦄⟩':
            depth -= 1
        elif ch == '|' and depth == 0 and head[i - 1:i] in (' ', '\n') and head[i + 1:i + 2] == ' ':
            return head[:i]
    return head


QUANT = re.compile(r'(∀|∃!|∃|fun|λ)\s')
IDENT = r"[^\W\d][\w'₀-₉]*"


def alpha(t):
    """### the text with each variable bound by ∀, ∃, ∃!, fun or λ renamed in binding order (_b0, _b1, ...) from its binder on,
    ### and its whitespace collapsed: two Props that differ only in the names of their bound variables read the same."""
    t = ' '.join(t.split())
    k, pos = 0, 0
    while True:
        m = QUANT.search(t, pos)
        if not m:
            break
        j, depth = m.end(), 0
        while j < len(t):
            ch = t[j]
            if ch in '([{⦃⟨':
                depth += 1
            elif ch in ')]}⦄⟩':
                depth -= 1
            elif depth == 0 and (ch == ',' or t.startswith('=>', j)):
                break
            j += 1
        seg = t[m.end():j]
        grp = re.findall(r'[(\[{⦃]\s*([^:()\[\]{}⦃⦄]*?)\s*:', seg)
        if grp:
            names = [n for g in grp for n in re.findall(IDENT, g)]
        else:
            left = re.split(r'\s*(?::|∈|∉|>|<|≥|≤|≠)\s*', seg, maxsplit=1)[0]
            names = re.findall(IDENT, left)
        for n in names:
            t = t[:m.start()] + re.sub(r'(?<![\w.\'])' + re.escape(n) + r'(?![\w\'₀-₉])', '_b%d' % k, t[m.start():])
            k += 1
        pos = m.end()
    t = re.sub(r'([(\[{⦃])\s+', r'\1', t)
    return re.sub(r'\s+([)\]}⦄])', r'\1', t).strip()


# ### ### **(R235)(2), b625: THE DOMAIN-CONDITION CRITERION.** *A binder of a statement is a domain condition, and does not enter
# ### the grade, when it is (i) an instance binder whose class is not Fact; (ii) a membership, non-membership, non-emptiness or
# ### finiteness condition on an object the statement names; (iii) a restriction on a variable the same statement quantifies
# ### universally -- the restriction being part of the quantifier's domain and not a premise about the analytic object. A binder
# ### is a premise when it asserts a Prop about a fixed object the kernel names and does not derive.* Read here as:
# ###   (i) instance binders were never read as hypotheses; a `[Fact P]` instance is now read, and read as a premise (INSTANCE);
# ###   (ii) non-emptiness and finiteness join DOMAIN beside membership and non-membership;
# ###   (iii) continuity and integrability join the class predicates, the support inclusion `Function.support v ⊆ ...` is read
# ###        as one, on a variable the statement binds and its conclusion mentions (quantified: b570's reading kept, so a class
# ###        predicate on a variable the conclusion never mentions stays a premise, (R180)(2)(f)'s named case); a named
# ###        restriction the seat read at its pin as a condition on its arguments' own data (RESTRICTIONS, each with its
# ###        definition's file and line) is a domain condition when every argument is such a variable;
# ###   a bounded quantifier's range is no condition on an object the statement names: a binder `∀ x ∈ S, P x` is read by its
# ###   body (strip_range), so `∀ C ∈ sevenClasses, C Phi` -- a Prop about the fixed Phi -- reads as a premise.
# ### Its occasion: the 33 page nodes whose ledger grade differed from the rule's read at b624 (relay data/b624_e0_nodes.txt),
# ### classed binder by binder at b625 (relay data/b625_e0_classes.txt).
INSTANCE = re.compile(r'\[(?:\s*(\w+)\s*:)?\s*(Fact\b[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*)\]')
CLASS_PREDS_B625 = re.compile(r'^\s*(?:ContDiff|HasCompactSupport|IsCompact|Continuous|Integrable|Differentiable)\b.*?\s([^\W\d][\w\'₀-₉]*)\s*$')
SUPPORT = re.compile(r'^\s*(?:Function\.support|tsupport)\s+([^\W\d][\w\'₀-₉]*)\s*⊆')
RESTRICTIONS = [
    dict(head='admissible', where='SIDE-explicit-formula v0.20 = 914c413, SIDEExplicitFormula/Registers.lean :38',
         reads='∀ a ∈ W, classK (F a) ∧ poleTerm (F a) = 0 -- a condition on F and W alone', restricts=('F', 'W')),
    dict(head='HStrip', where='SIDE-explicit-formula v0.20 = 914c413, SIDEExplicitFormula/RestBound.lean :40',
         reads='∀ ρ ∈ Z.carrier, 0 < ρ.re ∧ ρ.re < 1 -- a condition on Z`s own carrier', restricts=('Z',)),
    dict(head='HCount', where='SIDE-explicit-formula v0.20 = 914c413, SIDEExplicitFormula/RestBound.lean :44',
         reads='1 ≤ A₀ ∧ ∀ t, Z.N t (t + 1) ≤ A₀ * log (|t| + 3) -- a condition on Z and A₀ alone', restricts=('Z', 'A₀')),
    dict(head='is_universal', where='SIDE-explicit-formula v0.20 = 914c413, SIDEExplicitFormula/RegisterDepth.lean :38',
         reads='∀ c₁ c₂, I.action c₁ = I.action c₂ -- a condition on I`s own action', restricts=('I',)),
    dict(head='IsNontrivialZeroChi', where='SIDE-explicit-formula v0.21 = 1d5d4dd, SIDEExplicitFormula/Chi/ZeroConfig.lean :48',
         reads='LFunction χ ρ = 0 ∧ 0 < ρ.re ∧ ρ.re < 1 -- the membership of ρ in the nontrivial zeros of L(s, χ)', restricts=('χ', 'ρ')),
]
# ### (R236)(3): every entry names the quantified variables it restricts (its definition's parameters, by position); an entry that
# ### cannot name one is struck. None is struck: each definition read at its pin takes its restricted objects as parameters.
STRUCK_RESTRICTIONS = [r['head'] for r in RESTRICTIONS if not r.get('restricts')]
RESTRICTIONS = [r for r in RESTRICTIONS if r.get('restricts')]


def bound_vars(head):
    """### the variables a header's binder groups ( ), { }, ⦃ ⦄ bind before its conclusion (instance groups bind none read here)."""
    s = conclusion_start(head)
    pre = head[:s - 1] if s else head
    out = set()
    for m in re.finditer(r'[({⦃]\s*([^:(){}⦃⦄\[\]]+?)\s*:', pre):
        out |= set(re.findall(IDENT, m.group(1)))
    return out


def quantified(v, head):
    """### (iii)'s variable: one the statement binds and its conclusion mentions -- b570's reading of "the class the statement is
    ### about" kept, so a restriction on a bound variable the conclusion never mentions stays a premise ((R180)(2)(f)'s case)."""
    return v in bound_vars(head) and re.search(r'(?<![\w.\'])' + re.escape(v) + r'(?![\w\'₀-₉])', conclusion(head)) is not None


def strip_range(t):
    """### a bounded quantifier's range is no condition on a named object: `∀ x ∈ S, P` read as `P` (repeatedly)."""
    while True:
        m = re.match(r'^\s*∀\s+[^,]*?\s∈\s[^,]*,\s*', t)
        if not m:
            return t
        t = t[m.end():]


def restriction_case(t, head):
    """### the RESTRICTIONS entry whose head the binder type applies to the statement's own quantified variables alone, or None."""
    t = t.strip()
    for r in RESTRICTIONS:
        m = re.match(r'^(?:' + re.escape(r['head']) + r'((?:\s+[^\W\d][\w\'₀-₉]*)+)|([^\W\d][\w\'₀-₉]*)\.' + re.escape(r['head']) + r')\s*$', t)
        if m:
            args = m.group(1).split() if m.group(1) else [m.group(2)]
            if args and all(quantified(a, head) for a in args):
                return r
    return None


def restricts_bound(t, head):
    """### (iii): a smoothness, continuity, integrability, compact-support or support restriction on a quantified variable."""
    m = CLASS_PREDS_B625.match(t) or SUPPORT.match(t)
    return bool(m) and quantified(m.group(1), head)


def domain_case(t, head):
    """### the binder type read as a domain condition: DOMAIN on its body (a bounded quantifier's range stripped), a SPLITS case, a
    ### class predicate on a variable the conclusion mentions, (iii)'s restriction on a variable the statement binds, or a named
    ### restriction on the statement's own variables."""
    return bool(re.search(DOMAIN, strip_range(t)) or split_case(t) or class_case(t, head) or restricts_bound(t, head)
                or restriction_case(t, head))


# ### ### **(R236)(2), b626: SEAM ANTECEDENTS AND DATA BINDERS.** *(i) A Prop that is the antecedent of a top-level implication
# ### in a statement's conclusion is read as the rule reads a binder -- the curried and the bound forms of one hypothesis take one
# ### grade* -- as the author narrowed it before b626's seal, for an antecedent that is a seam (SEAMS below). Read here as: the
# ### conclusion, unless it opens with a quantifier, a lambda or a negation, or its top-level connective is ↔, is split at its
# ### depth-0 arrows before any depth-0 quantifier; every part but the last is an antecedent (arrow_antecedents), read as a binder
# ### named `→` when it is a SEAMS entry (seam_antecedents). Its instance: h2_sign_imp_rh_of_seam `: rh_strip_imp_rh →
# ### h2_sign_imp_rh`, INTERFACES on the seam its arrow carries, as its cells grade it. *(ii) A binder whose type is not a Prop --
# ### a function, a real, a natural, a character -- is an object of the statement and not a hypothesis whatever its name.* Read
# ### here as: a binder whose type is a number type, Prop or Type, an arrow chain of those, or a Dirichlet character is not read
# ### (data_binder). Its instance: paperFT_growth and paperFT_growth_at, `h : ℝ → ℂ`, read by the rule's name pattern until b626.
DATA_ATOM = r'(?:ℝ|ℂ|ℕ|ℤ|ℚ|ℕ∞|ℝ≥0|ℝ≥0∞|Prop|Type\*?|Type u|Sort\*?)'
DATA_TYPE = re.compile(r'^\s*(?:' + DATA_ATOM + r'(?:\s*→\s*' + DATA_ATOM + r')*|DirichletCharacter\b.*)\s*$')


def data_binder(t):
    """### (R236)(2)(ii): True when the binder's type is no Prop -- a number type, Prop or Type, an arrow chain of those, a character."""
    return DATA_TYPE.match(t) is not None


# ### (R236)(2)(i) AS NARROWED BY THE AUTHOR'S ANSWER BEFORE b626's SEAL: *a plain A → B between open statements is the kernel's
# ### result and keeps DERIVES; an antecedent that is itself a named implication between open statements -- a seam, the kernel's
# ### own "_of_seam" marker -- is a premise.* THE PRINCIPLE, beside the entries so that the next seam is added by it and not by a
# ### name match: an entry is a Prop the kernel names whose definition, read at its pin, is an implication between open statements
# ### and which no theorem of the kernel derives. The measurement that narrowed it: the clause as first worded moved 14 plain
# ### implications DERIVES -> INTERFACES over the 193 page nodes, measured before the seal (relay data/b626_author_answers.txt).
SEAMS = [
    dict(name='rh_strip_imp_rh', where='SIDE-explicit-formula v0.20 = 914c413, SIDEExplicitFormula/PowerWindow.lean :495',
         reads='def rh_strip_imp_rh : Prop := rh_strip → RiemannHypothesis -- a named implication between open statements, a premise'),
]


def seam_antecedents(concl):
    """### (R236)(2)(i), narrowed: the conclusion's top-level antecedents that are SEAMS entries by name."""
    names = set(s['name'] for s in SEAMS)
    return [a for a in arrow_antecedents(concl) if a.strip() in names]


def arrow_antecedents(concl):
    """### (R236)(2)(i): the antecedents of the conclusion's top-level implication chain, [] when it opens with a quantifier,
    ### a lambda or a negation or carries no depth-0 arrow."""
    c = (concl or '').strip()
    if not c or re.match(r'^(∀|∃|fun\b|λ|¬)', c):
        return []
    parts, depth, last = [], 0, 0
    for i, ch in enumerate(c):
        if ch in '([{⦃⟨':
            depth += 1
        elif ch in ')]}⦄⟩':
            depth -= 1
        elif depth == 0 and ch == '↔':
            return []          # ### ↔ binds looser than →: the top-level connective is the equivalence, no implication
        elif depth == 0 and (ch in '∀∃λ' or c.startswith('fun ', i)):
            break              # ### a quantifier's body runs to the end: its arrows are not the conclusion's
        elif ch == '→' and depth == 0:
            parts.append(c[last:i].strip())
            last = i + 1
    return [p for p in parts if p]


def grade(head, kind):
    """### RETURN `(grade, why, binders)` for a declaration header (the text between the name and `:=`).
    ### kind 'def' grades DEF. A binder is a premise unless it is a domain condition (domain_case); a Fact instance is a premise;
    ### a data binder is no hypothesis; a seam antecedent of the conclusion is read as a binder."""
    if kind == 'def':
        return 'DEF', '', []
    head = statement_only(head)
    spans = exist_spans(head)
    binders = [m.groups() for m in BINDER.finditer(head) if not any(a <= m.start() < b for a, b in spans)]
    binders = [(b, t) for b, t in binders if not data_binder(t)]
    binders = binders + [('→', a) for a in seam_antecedents(conclusion(head))]
    cs = conclusion_start(head)
    facts = [((m.group(1) or '[inst]'), m.group(2).strip()) for m in INSTANCE.finditer(head) if cs is None or m.start() < cs]
    concl = alpha(conclusion(head))
    enc = [(b, t) for b, t in binders if concl and alpha(t) == concl]
    if enc:
        return 'ENCODES-CONCLUSION', 'the conclusion is the binder ' + ', '.join('%s : %s' % bt for bt in enc), binders
    prem = [(b, t) for b, t in binders if not domain_case(t, head)] + facts
    binders = binders + facts
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
        ('{a : ι} {s : Finset ι} (h : a ∉ s) : P a s', 'theorem', 'DERIVES'),
        ('(n : ℕ) (h : ∀ k : ℕ, k + n = n + k) : ∀ m : ℕ, m + n = n + m', 'theorem', 'ENCODES-CONCLUSION'),
        ('(n : ℕ) (h : ∀ k : ℕ, k + n = k + n) : ∀ m : ℕ, m + n = n + m', 'theorem', 'DERIVES'),
        ('(n : ℕ) : ∀ j, R n j\n  | 0 => f\n  | j + 1 => g (hX : Q j)', 'theorem', 'DERIVES'),
        ('(p : ℕ) [NeZero p] [Fact p.Prime] : P p', 'theorem', 'INTERFACES'),
        ('{s : Set ℂ} (hn : s.Nonempty) (hf : s.Finite) : P s', 'theorem', 'DERIVES'),
        ('{g : ℝ → ℝ} {L : ℝ} (hc : Continuous g) (hs : Function.support g ⊆ Set.Icc (-L) L) : Q g', 'theorem', 'DERIVES'),
        ('(h1 : ∀ C ∈ sevenClasses, C Phi) : ∀ s : ℂ, 1 < s.re → R s', 'theorem', 'INTERFACES'),
        (': rh_strip_imp_rh → h2_sign_imp_rh', 'theorem', 'INTERFACES'),
        (': RiemannHypothesis → h2_sign', 'theorem', 'DERIVES'),
        ('(h : ℝ → ℂ) (hc : Continuous h) : Q h', 'theorem', 'DERIVES'),
    ]
    return all(grade(h, k)[0] == want for h, k, want in cases)


if __name__ == '__main__':
    ok = self_test()
    print('\n'.join(RULE_TEXT))
    print('### self-test (eighteen headers, both polarities): %s' % ('PASS' if ok else 'FAIL'))
    raise SystemExit(0 if ok else 1)
