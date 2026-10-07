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
    '### (R243)(2), b633: Alt2 and Alternates enter the named restrictions, each with the variable it restricts; and a named predicate',
    '### on the statement`s quantified variables that the rule neither lists nor has met (MET) reads PREDICATE-UNLISTED, not INTERFACES.',
    '### (R247)(3)-(4), b637, THE BINDER GRAMMAR: a binder`s name is no part of its reading. Every binder of a statement (the header`s groups,',
    '### the conclusion`s leading telescope, the antecedents of its implication, the binders of an existential in it) is classed by its',
    '### kind, its typing (a Prop or data, read from its type) and its Prop`s form (CLASSES, 26); the grade follows the classes` outcomes;',
    '### a binder that reaches no class raises BinderUnclassed and is printed as a bug, never graded.',
]

DOMAIN = r'(?:≠|<|≤|=|∈|∉|\.Even\b|IsPrimitive|\.Nonempty\b|\bNonempty\b|\.Finite\b|\bSet\.Finite\b|\bFinite\b)'

SPLITS = [
    dict(cases=(r'^\s*\w+\.Even\s*$', r'^\s*¬\s*\w+\.Even\s*$'),
         decls=('SIDEExplicitFormula.GRHWeil.gammaBracket_chi_of_even', 'SIDEExplicitFormula.GRHWeil.gammaBracket_chi_of_not_even'),
         where='SIDE-explicit-formula v0.10 = 6baed63, SIDEExplicitFormula/Chi/Statement.lean :51, :59',
         exhaustive='Classical.em (χ.Even), Lean core; beside it DirichletCharacter.even_or_odd (Mathlib de5ce8a9, '
                    'NumberTheory/DirichletCharacter/Basic.lean :538)'),
]

BINDER = re.compile(r"\(([^\W\d][\w'₀-₉✝]*) : ([^()]*(?:\((?:[^()]|\([^()]*\))*\)[^()]*)*)\)")   # ### b635, (R245)(2): two levels of nesting
# ### b637, (R247)(3): THE NAME PREFIX REMOVED. Until b637 this pattern read a parenthesised binder only when its name began with h, and
# ### grade() read hypotheses through it, so a premise named H, hyp or anything else was never read (chi_Tail's H : TailHyp; U15's
# ### nontrivialZeroInStrip). It now matches any binder name and grade() no longer reads through it: the binder grammar below reads every
# ### binder by its kind, its typing and its form. The pattern is kept, name-free, for the readers that import it.

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
CLASS_PREDS_B625 = re.compile(r'^\s*(?:[\w\']+\.)*(?:ContDiff|HasCompactSupport|IsCompact|Continuous|Integrable|Differentiable)\b.*?\s'
                              r'([^\W\d][\w\'₀-₉]*)(?:\s+(?:MeasureTheory\.)?volume)?\s*$')   # ### b635, (R245)(2): the qualified name and its default measure
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
    # ### b633, (R243)(2): the second reader's two disagreements of b632 upheld -- a restriction on a variable the statement quantifies
    # ### universally, clause (iii), which the rule had read as a premise because neither name was on this list.
    dict(head='Alt2', where='SIDE-global-section 17ce9ff, Core/LadderOrientationShadow.lean :95',
         reads='def Alt2 (c : Nat → U4) : Prop := ∀ k, c (k + 2) = mul m1 (c k) -- a condition on c alone', restricts=('c',)),
    dict(head='Alternates', where='SIDE-global-section 17ce9ff, Core/AlternationShadow.lean :33 and Core/SignTransferShadow.lean :47',
         reads='def Alternates (s : Nat → Int) : Prop := ∀ i, s (i + 1) = -s i -- a condition on s alone', restricts=('s',)),
]
# ### (R236)(3): every entry names the quantified variables it restricts (its definition's parameters, by position); an entry that
# ### cannot name one is struck. None is struck: each definition read at its pin takes its restricted objects as parameters.
# ### ### **(R243)(2), b633, AND THE AUTHOR'S ANSWER BEFORE b633'S SEAL: PREDICATE-UNLISTED.** *When a named predicate on a quantified
# ### variable is met for the first time the rule prints it as PREDICATE-UNLISTED rather than INTERFACES, so the list grows by a ruling
# ### and not by a wrong grade standing until a reader catches it.* "For the first time" is read against MET: every named premise any
# ### row of the table carried in the rule's reading at relay 8e6b63cc -- 45 from the rule-graded rows (b632's 42 heads and the 3 of
# ### the two rows graded before it) and 6 from the cell-graded rows, 51 names, by the author's two answers -- so the clause guards
# ### forward and moves no row or page cell read before it. A binder is UNLISTED when its type is a name applied to variables
# ### the statement quantifies and its conclusion mentions, the name neither a RESTRICTIONS head nor MET nor a variable the statement
# ### (or the binder's own quantifier) binds. The clause does not separate a premise structure about a fixed kernel object from a
# ### predicate restricting a quantified variable; that separation is W-ORD-BINDER-GRAMMAR's (OPEN_TRAILS :13002), and MET is the
# ### forward-only guard until it lands.
MET = ('Alt2', 'Alternates', 'AnalyticOnNhd', 'BoundPremises', 'ConservationHypothesis', 'Continuous', 'Dealigned', 'DealignedAt',
       'EpsteinPremises', 'EqOn', 'EulerFactorPremise', 'HCount', 'HasCompactSupport', 'HasDerivAt', 'IdempotentAdd', 'Integrable',
       'IsEvenFn', 'IsExpansion', 'IsOpen', 'IsRoot', 'IsSign', 'IsSignedCompletion', 'IsTrivialPoint', 'KeiperObligations', 'Monotone',
       'NotDiv', 'NymanBeurlingPremise', 'PerClassExcludes', 'PlattTrudgianHeight', 'Prime', 'Proper', 'SatisfiesCWeil', 'StepsI',
       'StepsMI', 'StrictMono', 'StructuralExhaustiveness', 'SymPairBound', 'Tendsto', 'TrivialSummandPremise', 'WindowObligations',
       'ZetaSeam', 'farSmall', 'identity', 'is_xi_zero', 'zeroSideNeg') + (
    # ### the author's second answer before b633's seal: MET from every row -- the six names cell-graded rows' rule readings carry
    'Blind', 'IsPreconnected', 'LiLimitExchange', 'VerifiedZerosTo', 'factorsDark', 'isConserved')
NAMED_PRED = re.compile(r"^(?:([^\W\d][\w'.₀-₉]*)((?:\s+[^\W\d][\w'₀-₉]*)+)|([^\W\d][\w'₀-₉]*)\.([^\W\d][\w'₀-₉]*))\s*$")


def unlisted_case(t, head):
    """### (R243)(2): the name of a predicate the binder type applies to the statement's own quantified variables alone, when the rule
    ### neither lists it, nor has met it, nor reads it as a variable bound by the statement or by the binder's own quantifier; else None."""
    return _named_on_quantified(t, head, met=False)


def met_case(t, head):
    """### b637, (R247)(3): the name of such a predicate when MET holds it (the forward guard of OPEN_TRAILS :13221); else None."""
    return _named_on_quantified(t, head, met=True)


def _named_on_quantified(t, head, met):
    """### the predicate's short name when the binder type applies it to quantified variables alone, it is no bound variable and no
    ### RESTRICTIONS head, and MET holds it (met=True) or does not (met=False); else None."""
    s = (t or '').strip()
    qbound = set()
    for _ in range(6):
        s = re.sub(r'^¬\s*', '', s)
        m = re.match(r'^∀\s+([^,]*?)\s∈\s[^,]*,\s*', s) or re.match(r'^∀\s+([^,]*?),\s*', s)
        if not m:
            break
        qbound |= set(re.findall(IDENT, m.group(1).split(':')[0]))
        s = s[m.end():]
    m = NAMED_PRED.match(s)
    if not m:
        return None
    if m.group(1):
        name, args = m.group(1), m.group(2).split()
    else:
        name, args = m.group(4), [m.group(3)]
    short = name.split('.')[-1]
    if '.' not in name and (name in bound_vars(head) or name in qbound):
        return None
    if short in [r['head'] for r in RESTRICTIONS] or ((short in MET) != met):
        return None
    return short if args and all(quantified(a, head) for a in args) else None
STRUCK_RESTRICTIONS = [r['head'] for r in RESTRICTIONS if not r.get('restricts')]
RESTRICTIONS = [r for r in RESTRICTIONS if r.get('restricts')]


def bound_vars(head):
    """### the variables a header's binder groups ( ), { }, ⦃ ⦄ bind before its conclusion (instance groups bind none read here)."""
    s = conclusion_start(head)
    pre = head[:s - 1] if s else head
    out = set()
    for m in re.finditer(r'[({⦃]\s*([^:(){}⦃⦄\[\]]+?)\s*:', pre):
        out |= set(re.findall(IDENT, m.group(1)))
    return out | set(n for _k, n, _t in telescope(conclusion(head))[0])   # ### b637: the conclusion's telescope binds too


def quantified(v, head):
    """### (iii)'s variable: one the statement binds and its conclusion mentions -- b570's reading of "the class the statement is
    ### about" kept, so a restriction on a bound variable the conclusion never mentions stays a premise ((R180)(2)(f)'s case).
    ### b637: a variable the conclusion's telescope binds is quantified when the body after the telescope mentions it."""
    pat = r'(?<![\w.\'])' + re.escape(v) + r'(?![\w\'₀-₉])'
    tel, body = telescope(conclusion(head))
    if v in set(n for _k, n, _t in tel):
        return re.search(pat, body) is not None
    return v in bound_vars(head) and re.search(pat, conclusion(head)) is not None


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


# ### ### **(R247)(3)-(4), b637: THE BINDER GRAMMAR -- THE RULE AS A TOTAL FUNCTION OVER A FINITE CLASSIFICATION, NAMES REMOVED.**
# ### *A binder's name is no part of its reading: the criterion is a function of the binder's kind (explicit, implicit, instance,
# ### strict-implicit), its type (a Prop or data), the Prop's form (a structure of premises about a fixed object; a named predicate
# ### restricting a variable the same statement quantifies; a membership, non-membership, finiteness or non-emptiness condition; a seam
# ### antecedent; the conclusion itself) and the MET list -- and of nothing the author typed as a name.* Read here as follows.
# ###   THE BINDERS OF A STATEMENT are Lean's: the header's binder groups ( ), { }, ⦃ ⦄, [ ] (BinderInfo.default, .implicit,
# ###   .strictImplicit, .instImplicit -- Lean/Expr.lean :71-:79 at the toolchain v4.34.0-rc1); then the conclusion's leading telescope
# ###   `∀ (x : T) {y : U}, …` / `∀ x y : T, …` / `∀ x ∈ S, …`, as the elaborated type carries those binders in its header (a bounded
# ###   binder ends the telescope, its condition an anonymous antecedent); then the top-level antecedents of the body's implication chain
# ###   (kind `antecedent`); the binder groups of an existential in the conclusion are listed (kind `existential`) and are part of it.
# ###   THE TYPING of a binder of the four Lean kinds is read from its type alone (typing): a Prop when the type is a negation, an
# ###   existential, a bounded universal, a relation at depth 0 (= ≠ < ≤ > ≥ ∈ ∉ ⊆ ⊂ ∣ ↔ ∧ ∨), an implication into a Prop, a universal over
# ###   a Prop body, a variable of a predicate type applied, a property field of an object (PROP_FIELDS), or a name the lexicon reads as a
# ###   Prop (LEXICON: each kernel head with its declaration's file and line, each Mathlib head with its file and line at de5ce8a9; MET,
# ###   the RESTRICTIONS heads and the SEAMS names are Props by their entries); data when it is a number or sort atom, a product, a
# ###   function type into data, a type variable or a set of the statement used as a type, an untyped variable, a data field, or a name
# ###   the lexicon reads as a type former; an application of a name no lexicon lists to arguments is read as a named predicate, a Prop,
# ###   and is so marked. A type none of these reaches has no typing: the binder reaches no class and is printed as a bug, not graded.
# ###   THE FORM of a Prop binder is the criterion's, read in this order, the first that holds: the conclusion itself (alpha); a
# ###   membership, non-membership, non-emptiness, finiteness, order or (in)equality condition or a listed property, or a compiled split's
# ###   case (DOMAIN, SPLITS; criterion (ii)); a restriction on a variable the statement quantifies (class predicates, support, RESTRICTIONS;
# ###   criterion (iii)); a named predicate on quantified variables neither listed nor met (PREDICATE-UNLISTED, MET); one MET holds (its own
# ###   class, a premise under the forward guard of OPEN_TRAILS :13221 until a name is ruled a restriction); any other Prop -- a
# ###   structure of premises or a named Prop about a fixed object -- a premise. An antecedent is a seam when SEAMS names it, else part of
# ###   the conclusion; an instance binder is a premise when its class is Fact, else a domain condition (criterion (i)).
# ### THE CLASSES, kind × typing × form, each with its outcome (CLASSES below; relay data/b637_binder_classes.txt prints the table with one
# ### planted declaration per class). The grade follows the outcomes: a binder whose outcome is `conclusion` by the form "the conclusion
# ### itself" -- ENCODES-CONCLUSION; else an `unlisted` -- PREDICATE-UNLISTED; else a `premise` or `seam` -- INTERFACES; else DERIVES.
BINDER_KINDS = ('explicit', 'implicit', 'strict-implicit', 'instance', 'antecedent', 'existential')
OUTCOMES = ('domain condition', 'premise', 'data', 'seam', 'conclusion', 'unlisted')
FORMS = (('itself', 'the conclusion itself', 'conclusion'),
         ('domain', 'a membership, non-membership, non-emptiness, finiteness, order or (in)equality condition, a listed property or a '
                    'compiled split`s case (criterion (ii); DOMAIN, SPLITS)', 'domain condition'),
         ('restriction', 'a restriction on a variable the statement quantifies -- a class predicate, a support inclusion or a named '
                         'restriction (criterion (iii); RESTRICTIONS)', 'domain condition'),
         ('unlisted', 'a named predicate on quantified variables, neither listed nor met (PREDICATE-UNLISTED; MET)', 'unlisted'),
         ('met', 'a named predicate on quantified variables that MET holds -- the forward guard (OPEN_TRAILS :13221), a premise until '
                 'the author rules the name a restriction', 'premise'),
         ('premise', 'any other Prop: a structure of premises or a named Prop about a fixed object', 'premise'))
NF = len(FORMS)
CLASSES = ([('B01', 'explicit', 'data', '—', 'data'), ('B02', 'implicit', 'data', '—', 'data'), ('B03', 'strict-implicit', 'data', '—', 'data'),
            ('B04', 'instance', 'a class', 'Fact', 'premise'), ('B05', 'instance', 'a class', 'any class but Fact (criterion (i))', 'domain condition')]
           + [('B%02d' % (6 + NF * i + j), k, 'Prop', f[1], f[2]) for i, k in enumerate(('explicit', 'implicit', 'strict-implicit'))
              for j, f in enumerate(FORMS)]
           + [('B%02d' % (6 + 3 * NF), 'antecedent', 'Prop', 'a seam (SEAMS)', 'seam'),
              ('B%02d' % (7 + 3 * NF), 'antecedent', 'Prop', 'any other antecedent: a plain implication between open statements, a domain '
                                                               'antecedent', 'conclusion'),
              ('B%02d' % (8 + 3 * NF), 'existential', 'any', 'a binder of an existential in the conclusion', 'conclusion')])
_FORM_INDEX = dict((f[0], j) for j, f in enumerate(FORMS))
_KIND_INDEX = {'explicit': 0, 'implicit': 1, 'strict-implicit': 2}


def class_id(kind, typing_, form=None):
    """### the class of a binder by its kind, its typing and its form; None for no class."""
    if kind == 'instance':
        return 'B04' if form == 'fact' else 'B05'
    if kind == 'antecedent':
        return 'B%02d' % ((6 if form == 'seam' else 7) + 3 * NF)
    if kind == 'existential':
        return 'B%02d' % (8 + 3 * NF)
    if kind not in _KIND_INDEX or typing_ not in ('data', 'prop'):
        return None
    if typing_ == 'data':
        return 'B%02d' % (1 + _KIND_INDEX[kind])
    return 'B%02d' % (6 + NF * _KIND_INDEX[kind] + _FORM_INDEX[form]) if form in _FORM_INDEX else None


OUTCOME_OF = dict((c[0], c[4]) for c in CLASSES)


class BinderUnclassed(Exception):
    """### a binder that reaches no class: a bug of the grammar, printed as such and never a grade."""


_OPEN, _CLOSE = '([{⦃⟨', ')]}⦄⟩'
_GKIND = {'(': 'explicit', '{': 'implicit', '⦃': 'strict-implicit', '[': 'instance'}
NAME = r"[^\W\d][\w'₀-₉✝]*"


def _close(s, i):
    """### the index of the bracket closing the one opened at s[i]."""
    depth, j = 0, i
    while j < len(s):
        if s[j] in _OPEN:
            depth += 1
        elif s[j] in _CLOSE:
            depth -= 1
            if depth == 0:
                return j
        j += 1
    return len(s) - 1


def _group(kind, inner):
    """### one binder group's binders: [(kind, name, type)]; an instance group binds its optional name; an untyped group binds names."""
    if kind == 'instance':
        m = re.match(r'^\s*(' + NAME + r')\s*:\s*(.*)$', inner, re.S)
        return [(kind, m.group(1) if m else '', ' '.join((m.group(2) if m else inner).split()))]
    depth, cut = 0, None
    for i, ch in enumerate(inner):
        if ch in _OPEN:
            depth += 1
        elif ch in _CLOSE:
            depth -= 1
        elif ch == ':' and depth == 0:
            cut = i
            break
    names = (inner[:cut] if cut is not None else inner).split()
    t = ' '.join(inner[cut + 1:].split()) if cut is not None else ''
    return [(kind, n, t) for n in names]


def header_groups(head):
    """### the header's leading binder groups, each binder (kind, name, type), in order."""
    out, i, n = [], 0, len(head)
    while True:
        while i < n and head[i].isspace():
            i += 1
        if i < n and head[i] in _GKIND:
            j = _close(head, i)
            out += _group(_GKIND[head[i]], head[i + 1:j])
            i = j + 1
            continue
        return out


def _top_comma(s):
    depth = 0
    for i, ch in enumerate(s):
        if ch in _OPEN:
            depth += 1
        elif ch in _CLOSE:
            depth -= 1
        elif ch == ',' and depth == 0:
            return i
    return None


def telescope(concl):
    """### the conclusion's leading universal telescope: RETURN (binders [(kind, name, type)], body). A bounded binder (∀ x ∈ S,) is read
    ### and ends the telescope; its condition stays in the body as an anonymous antecedent, as the elaborated type carries it."""
    out, s = [], (concl or '').strip()
    while s.startswith('∀'):
        rest = s[1:].lstrip()
        if rest[:1] in _GKIND:
            gs, i = [], 0
            while i < len(rest) and rest[i] in _GKIND:
                j = _close(rest, i)
                gs += _group(_GKIND[rest[i]], rest[i + 1:j])
                i = j + 1
                while i < len(rest) and rest[i].isspace():
                    i += 1
            if rest[i:i + 1] == ',':
                out += gs
                s = rest[i + 1:].strip()
                continue
            break
        c = _top_comma(rest)
        if c is None:
            break
        seg = rest[:c].strip()
        mb = re.match(r'^((?:' + NAME + r'\s*)+?)\s*(∈|∉|>|<|≥|≤|≠|⊆)\s*(.+)$', seg)
        if mb:
            out += [('explicit', n, '') for n in mb.group(1).split()]
            s = '%s %s %s → %s' % (mb.group(1).split()[-1], mb.group(2), mb.group(3), rest[c + 1:].strip())
            break
        m = re.match(r'^((?:' + NAME + r'\s*)+?)\s*(?::\s*(.+))?$', seg)
        if m:
            out += [('explicit', n, ' '.join((m.group(2) or '').split())) for n in m.group(1).split()]
            s = rest[c + 1:].strip()
            continue
        mixed, i, ok = [], 0, True        # ### names and groups mixed: ∀ j (w : ℂ), …
        while i < len(seg):
            if seg[i].isspace():
                i += 1
            elif seg[i] in _GKIND:
                j = _close(seg, i)
                mixed += _group(_GKIND[seg[i]], seg[i + 1:j])
                i = j + 1
            else:
                mm = re.match(NAME, seg[i:])
                if not mm:
                    ok = False
                    break
                mixed.append(('explicit', mm.group(0), ''))
                i += mm.end()
        if not ok or not mixed:
            break
        out += mixed
        s = rest[c + 1:].strip()
    return out, s


# ### THE TYPING'S LISTS. Number and sort atoms are data; a product or a function type into data is data. PROP_FIELDS are the property
# ### fields read on an object (χ.IsPrimitive, s.Nonempty, I.is_universal); DATA_FIELDS the fields that are objects (Z.carrier, ρ.re).
SORT_ATOMS = re.compile(r"^(?:ℝ|ℂ|ℕ|ℤ|ℚ|ℕ∞|ℝ≥0|ℝ≥0∞|EReal|ENNReal|NNReal|Nat|Int|Real|Complex|Rat|Bool|Prop|Unit|Type\*?|Type\s+[\w'₀-₉]+|Sort\*?|"
                        r"Sort\s+[\w'₀-₉]+|ℚ_\[\w+\]|ℤ_\[\w+\])$")
MORPHISMS = ('→+*', '→+', '→*', '→ₗ', '→L', '→ₐ', '→ᵃ', '→ᵇ', '≃ₗᵢ', '≃ₗ', '≃+', '≃*', '≃L', '≃')   # ### bundled maps and equivalences: data
TYPE_VAR = re.compile(r"^(?:[A-Z]|[α-ωΑ-Ω𝕜])[₀-₉'0-9]?$")   # ### a one-letter type name the statement binds nowhere: a section or auto-bound variable
RELS = ('=', '≠', '<', '≤', '>', '≥', '∈', '∉', '⊆', '⊂', '⊇', '⊃', '∣', '↔', '∧', '∨', '≡', '=ᶠ', '≤ᶠ', '≍')
ML_ = 'Mathlib de5ce8a9 Mathlib/'
PROP_FIELDS = {'IsPrimitive': ML_ + 'NumberTheory/DirichletCharacter/Basic.lean :292', 'Even': ML_ + 'NumberTheory/DirichletCharacter/Basic.lean :536',
               'Odd': ML_ + 'NumberTheory/DirichletCharacter/Basic.lean :533', 'Prime': ML_ + 'Data/Nat/Prime/Defs.lean :42',
               'Nonempty': ML_ + 'Data/Set/Defs.lean :280', 'Finite': ML_ + 'Data/Finite/Defs.lean :185',
               'IsHermitian': ML_ + 'LinearAlgebra/Matrix/Hermitian.lean :44',
               'is_universal': 'SIDE-explicit-formula SIDEExplicitFormula/RegisterDepth.lean :38',
               'Valid': 'SIDE-explicit-formula Zeta23/Defs.lean :209',
               'Proper': 'SIDE-structural-error-correction SIDEStructuralErrorCorrection/DeAlignment.lean :39',
               'isConserved': 'SIDE-kernel Kernel/Cascade/SieveCeiling.lean :86', 'factorsDark': 'SIDE-kernel Kernel/Cascade/SieveCeiling.lean :111'}
DATA_FIELDS = {'carrier': 'SIDE-explicit-formula Zeta23/Defs.lean :136 (ZeroConfig`s carrier)', 're': 'Lean core Complex.re', 'im': 'Lean core Complex.im',
               'H': 'SIDE-global-section Interfaces/GlobalSection.lean :26 (GlobalSectionData`s H : Type)'}
# ### THE LEXICON: every head the binder types of the two kernels and of the table's rows apply, read at its declaration (sort 'prop' -- its
# ### type is Prop; 'data' -- a Type former; 'pred-type' -- a Type whose terms are predicates), with the declaration's repository, file and line.
LEXICON = {
    'AddSubgroup': ('data', ML_ + 'Algebra/Group/Subgroup/Defs.lean :301'),
    'Aggregation': ('data', 'SIDE-global-section Core/AggregationCircularityShadow.lean :112'),
    'AnalyticOn': ('prop', ML_ + 'Analysis/Analytic/Basic.lean :123'),
    'BlockInputs': ('prop', 'SIDE-explicit-formula Zeta23/Assembly/Inputs.lean :58'),
    'Carrier': ('data', 'SIDE-global-section Interfaces/RestrictedTensorLayer1.lean :82'),
    'CarrierSpec': ('data', 'SIDE-carrier-spec SIDECarrierSpec/Spec.lean :53'),
    'ConfigurationSpace': ('data', 'SIDE-explicit-formula SIDEExplicitFormula/RegisterDepth.lean :27'),
    'ContDiff': ('prop', ML_ + 'Analysis/Calculus/ContDiff/Defs.lean :1068'),
    'ContDiffBump': ('data', ML_ + 'Analysis/Calculus/BumpFunction/Basic.lean :70'),
    'Coupling': ('pred-type', 'SIDE-explicit-formula SIDEExplicitFormula/RegisterDepth.lean :180'),
    'Descent': ('data', 'SIDE-carrier-spec SIDECarrierSpec/Level.lean :53'),
    'DeterminedSystem': ('data', 'SIDE-kernel Kernel/Cascade/SieveCeiling.lean :80'),
    'DirichletCharacter': ('data', ML_ + 'NumberTheory/DirichletCharacter/Basic.lean :40'),
    'EF_lit': ('prop', 'SIDE-explicit-formula Zeta23/ExplicitFormula.lean :97'),
    'ExhaustiveCatalogue': ('data', 'SIDE-effects SIDEEffects/Phase15/SIDEFramework.lean :36'),
    'ExplicitFormulaDecomp': ('prop', 'SIDE-lv-conservation SIDELvConservation/PartialPositivity.lean :88'),
    'Fin': ('data', 'Lean v4.34.0-rc1 src/lean/Init/Prelude.lean :2315'),
    'Finset': ('data', ML_ + 'Data/Finset/Defs.lean :75'),
    'GammaFacts': ('prop', 'SIDE-explicit-formula Zeta23/Hypotheses.lean :141'),
    'GlobalSectionData': ('data', 'SIDE-global-section Interfaces/GlobalSection.lean :25'),
    'GR': ('data', 'SIDE-global-section Core/GroupRingGlue.lean :41'),
    'IDSSystem': ('data', 'SIDE-bijection SIDEBijection/Theorem.lean :109'),
    'InTail': ('prop', 'SIDE-explicit-formula Zeta23/Tail/Basic.lean :52'),
    'IntegrableOn': ('prop', ML_ + 'MeasureTheory/Integral/IntegrableOn.lean :92'),
    'Interface': ('data', 'SIDE-explicit-formula SIDEExplicitFormula/RegisterDepth.lean :33'),
    'IsCompact': ('prop', ML_ + 'Topology/Defs/Filter.lean :276'),
    'Line': ('data', 'SIDE-structural-error-correction SIDEStructuralErrorCorrection/DeAlignment.lean :32'),
    'List': ('data', 'Lean v4.34.0-rc1 src/lean/Init/Prelude.lean :2969'),
    'LocalCount': ('prop', 'SIDE-explicit-formula Zeta23/Tail/Basic.lean :82'),
    'LocallyIntegrableOn': ('prop', ML_ + 'MeasureTheory/Function/LocallyIntegrable.lean :50'),
    'LSeriesSummable': ('prop', ML_ + 'NumberTheory/LSeries/Basic.lean :178'),
    'Measure': ('data', ML_ + 'MeasureTheory/Measure/MeasureSpaceDef.lean :77'),
    'MechanismClass': ('data', 'SIDE-kernel Bridge/TheBridgeComplete.lean :20'),
    'NoneProduces': ('prop', 'SIDE-effects SIDEEffects/Phase15/SIDEFramework.lean :41'),
    'NontrivialZero': ('data', 'SIDE-explicit-formula Vendored/Bulka/Lc/LiCriterion/Basic.lean :116'),
    'NontrivialZeroExistsInStrip': ('prop', 'SIDE-lv-conservation SIDELvConservation/RegisterPentagon.lean :312'),
    'PaperInputs': ('prop', 'SIDE-explicit-formula Zeta23/Hypotheses.lean :163'),
    'Params': ('data', 'SIDE-explicit-formula Zeta23/Defs.lean :202'),
    'Polynomial': ('data', ML_ + 'Algebra/Polynomial/Basic.lean :74'),
    'Proof': ('data', 'SIDE-kernel Kernel/Cascade/SieveCeiling.lean :108'),
    'PWSetup': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/PowerLimit.lean :245'),
    'Register4_positivity': ('prop', 'SIDE-lv-conservation SIDELvConservation/RegisterPentagon.lean :152'),
    'Register5_output_HilbertPolya': ('prop', 'SIDE-lv-conservation SIDELvConservation/RegisterPentagon.lean :189'),
    'RiemannHypothesis': ('prop', ML_ + 'NumberTheory/LSeries/RiemannZeta.lean :185'),
    'RiemannVonMangoldt': ('prop', 'SIDE-explicit-formula Zeta23/Hypotheses.lean :83'),
    'SelfDualFE': ('prop', 'SIDE-lv-conservation SIDELvConservation/FieldLayer.lean :56'),
    'Set': ('data', ML_ + 'Data/Set/Defs.lean :51 (a type of sets; its terms are not applied as predicates here)'),
    'SimpleProportion': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/Simplicity.lean :40'),
    'Submodule': ('data', ML_ + 'Algebra/Module/Submodule/Defs.lean :41'),
    'TailBoundPremise': ('prop', 'SIDE-lv-conservation SIDELvConservation/PartialPositivity.lean :131'),
    'TailHyp': ('prop', 'SIDE-explicit-formula Zeta23/Tail.lean :288'),
    'TailInputs': ('prop', 'SIDE-explicit-formula Zeta23/Assembly/Inputs.lean :73'),
    'TypeIIParams': ('data', 'SIDE-lv-conservation SIDELvConservation/Genus5.lean :46'),
    'WeilConfig': ('data', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/Config.lean :24'),
    'ZeroActingPairing': ('prop', 'SIDE-lv-conservation SIDELvConservation/ZeroActingPairing.lean :41'),
    'ZeroConfig': ('data', 'SIDE-explicit-formula Zeta23/Defs.lean :136'),
}
MATHLIB_PROP = {}     # ### folded into LEXICON
MATHLIB_DATA = {}


def _strip_parens(s):
    s = s.strip()
    while s.startswith('(') and _close(s, 0) == len(s) - 1:
        s = s[1:-1].strip()
    return s


def _depth0(s, toks):
    """### the depth-0 tokens of `toks` occurring in s (outside every bracket and outside `|…|`)."""
    depth, bar, out, i = 0, False, [], 0
    while i < len(s):
        ch = s[i]
        if ch in _OPEN:
            depth += 1
        elif ch in _CLOSE:
            depth -= 1
        elif ch == '|':
            bar = not bar
        elif depth == 0 and not bar:
            for t in toks:
                if s.startswith(t, i):
                    out.append(t)
                    break
        i += 1
    return out


def _split0(s, tok):
    depth, last, parts = 0, 0, []
    for i, ch in enumerate(s):
        if ch in _OPEN:
            depth += 1
        elif ch in _CLOSE:
            depth -= 1
        elif depth == 0 and s.startswith(tok, i):
            parts.append(s[last:i])
            last = i + len(tok)
    return parts + [s[last:]]


def _lex(name):
    """### the lexicon's reading of a head name (its last component tried after the whole): (sort, where) or None."""
    for n in (name, name.split('.')[-1]):
        if n in LEXICON:
            return LEXICON[n]
        if n in MATHLIB_PROP:
            return 'prop', MATHLIB_PROP[n]
        if n in MATHLIB_DATA:
            return 'data', MATHLIB_DATA[n]
    short = name.split('.')[-1]
    if short in MET or short in [r['head'] for r in RESTRICTIONS] or short in [s['name'] for s in SEAMS]:
        return 'prop', 'a name of MET, RESTRICTIONS or SEAMS'
    return None


def typing(t, ctx=None, depth=0):
    """### RETURN (typing, how): typing 'prop', 'data' or None (no typing -- a bug); `ctx` maps the statement's bound names to their types."""
    ctx = ctx or {}
    s = _strip_parens(' '.join((t or '').split()))
    if not s:
        return 'data', 'an untyped variable (its type inferred: an object)'
    if depth > 12:
        return None, 'nesting beyond the reader'
    s = re.sub(r'^@', '', s)
    if re.match(r'^(¬|Not\b)', s):
        return 'prop', 'a negation'
    if re.match(r'^∃', s):
        return 'prop', 'an existential'
    if re.match(r'^(∀ᶠ|∃ᶠ)', s):
        return 'prop', 'a filter quantifier'
    if s.startswith('↑') and not _depth0(s, RELS):
        s = _strip_parens(re.sub(r'^↑\s*', '', s))
    if s.startswith('∀'):
        bs, body = telescope(s)
        if not bs:
            return None, 'a universal the reader cannot open'
        if re.match(r'^\S+ (∈|∉|>|<|≥|≤|≠|⊆) ', body) and '→' in body:
            return 'prop', 'a bounded universal'
        c2 = dict(ctx, **dict((n, ty) for _k, n, ty in bs))
        ty_, how = typing(body, c2, depth + 1)
        return ty_, 'a universal over %s' % how
    if re.match(r'^(fun|λ)\b', s):
        return None, 'a lambda as a type'
    if _depth0(s, RELS):
        return 'prop', 'a relation at depth 0 (%s)' % _depth0(s, RELS)[0]
    if _depth0(s, MORPHISMS):
        return 'data', 'a bundled map or equivalence (%s)' % _depth0(s, MORPHISMS)[0]
    pf = re.match(r"^(\(.*\))\.(" + NAME + r")(\s.*)?$", s)
    if pf and _close(s, 0) == len(pf.group(1)) - 1:     # ### a field of a parenthesised object: (tieSet Z g0 M).Nonempty
        f_ = pf.group(2)
        if f_ in PROP_FIELDS:
            return 'prop', 'a property field of an object (%s)' % f_
        if f_ in DATA_FIELDS:
            return 'data', 'an object field (%s)' % f_
        return None, 'a field %s the lists do not read' % f_
    parts = _split0(s, '→')
    if len(parts) > 1:
        ty_, how = typing(parts[-1], ctx, depth + 1)
        return ty_, ('an implication into a Prop' if ty_ == 'prop' else 'a function type into %s' % how)
    if len(_split0(s, '×')) > 1:
        return 'data', 'a product type'
    s = re.sub(r'^↑\s*', '', s)
    if SORT_ATOMS.match(s):
        return 'data', 'a number or sort atom'
    m = re.match(r"^(" + NAME + r"(?:\." + NAME + r")*)(.*)$", s)
    if not m:
        return None, 'no head the reader names'
    head, args = m.group(1), m.group(2).strip()
    base = head.split('.')[0]
    if head in ctx or (base in ctx and '.' in head):
        if head in ctx:
            vt = ' '.join((ctx[head] or '').split())
            if not vt:
                return None, 'a variable of no ascribed type applied'
            if re.search(r'(^|→\s*)Prop$', vt):
                return 'prop', 'a variable of a predicate type' + (' applied' if args else '')
            if SORT_ATOMS.match(vt) and re.match(r'^(Type|Sort)', vt):
                return 'data', 'a term of a type variable'
            if re.match(r'^(Set|Finset)\b', vt):
                return 'data', 'a set of the statement used as a type'
            vh = re.match(r'^(' + NAME + r'(?:\.' + NAME + r')*)', vt)
            lx = _lex(vh.group(1)) if vh else None
            if lx and lx[0] == 'pred-type':
                return ('prop', 'a variable of a predicate type applied') if args else ('data', 'a predicate as an object')
            if not args and typing(vt, ctx, depth + 1)[0] == 'data':
                return 'data', 'an object the statement binds, used as a type (its elements)'
            return None, 'a variable of type %s used as a type' % vt[:40]
        field = head.split('.')[-1]
        if field in PROP_FIELDS:
            return 'prop', 'a property field of an object (%s)' % field
        if field in DATA_FIELDS:
            return 'data', 'an object field (%s)' % field
        return None, 'a field %s the lists do not read' % field
    lx = _lex(head)
    if lx:
        if lx[0] == 'pred-type':
            return 'data', 'a predicate type (%s)' % lx[1]
        return lx[0], 'the lexicon: %s (%s)' % (head.split('.')[-1], lx[1])
    if '.' in head and head.split('.')[-1] in PROP_FIELDS:
        return 'prop', 'a property field (%s)' % head.split('.')[-1]
    if '.' in head and head.split('.')[-1] in DATA_FIELDS:
        return 'data', 'an object field (%s)' % head.split('.')[-1]
    if not args and TYPE_VAR.match(head):
        return 'data', 'a one-letter type the statement binds nowhere: a section or auto-bound type variable'
    if args:
        return 'prop', 'UNLEXED: an application of a name no lexicon lists, read as a named predicate'
    return None, 'a bare name no lexicon lists (%s)' % head


def _ctx(bs):
    return dict((n, t) for _k, n, t in bs if n)


def form_of(t, head):
    """### the form of a Prop binder's type, the first that holds, in FORMS' order."""
    c = conclusion(head)
    if c and alpha(t) == alpha(c):
        return 'itself'
    if re.search(DOMAIN, strip_range(t)) or split_case(t):
        return 'domain'
    if class_case(t, head) or restricts_bound(t, head) or restriction_case(t, head):
        return 'restriction'
    if unlisted_case(t, head):
        return 'unlisted'
    if met_case(t, head):
        return 'met'
    return 'premise'


def binders_of(head):
    """### EVERY binder of a statement's header (the text after the name, to `:=`), each classed: RETURN a list of dicts kind, name,
    ### type, typing, how, form, cls, outcome; `cls` None for a binder that reaches no class."""
    head = statement_only(head)
    hg = header_groups(head)
    concl = conclusion(head)
    tel, body = telescope(concl)
    ctx = _ctx(hg + tel)
    out = []
    for k, n, t in hg + tel:
        if k == 'instance':
            f = 'fact' if re.match(r'^\s*Fact\b', t) else 'class'
            out.append(dict(kind=k, name=n, type=t, typing='a class', how='an instance binder', form=f, cls=class_id(k, None, f)))
            continue
        ty_, how = typing(t, ctx)
        f = form_of(t, head) if ty_ == 'prop' else None
        out.append(dict(kind=k, name=n, type=t, typing=ty_, how=how, form=f, cls=class_id(k, ty_, f) if ty_ else None))
    for a in arrow_antecedents(body):
        f = 'seam' if a.strip() in [s['name'] for s in SEAMS] else 'plain'
        out.append(dict(kind='antecedent', name='→', type=a, typing='prop', how='an antecedent of the conclusion', form=f, cls=class_id('antecedent', 'prop', f)))
    for a, b in exist_spans(head):
        seg = head[a + 1:b]
        i = 0
        while i < len(seg):
            while i < len(seg) and seg[i].isspace():
                i += 1
            if i < len(seg) and seg[i] in _GKIND:
                j = _close(seg, i)
                for k, n, t in _group(_GKIND[seg[i]], seg[i + 1:j]):
                    out.append(dict(kind='existential', name=n, type=t, typing='any', how='inside an existential', form=None,
                                    cls=class_id('existential', 'any')))
                i = j + 1
                continue
            break
    for d in out:
        d['outcome'] = OUTCOME_OF.get(d['cls']) if d['cls'] else None
    return out


def grade(head, kind):
    """### RETURN `(grade, why, binders)` for a declaration header (the text between the name and `:=`); kind 'def' grades DEF.
    ### (R247): every binder is classed by binders_of; a binder that reaches no class raises BinderUnclassed. `binders` are the
    ### hypotheses read -- the Prop binders of the four Lean kinds, the seams, the Fact instances -- as (name, type)."""
    if kind == 'def':
        return 'DEF', '', []
    head = statement_only(head)
    if re.match(r'^\s*type_of%', conclusion(head) or ''):   # ### b635, (R245)(2): the statement is the elaborated type
        return 'DEFERRED', 'the conclusion is a type_of% term; the elaborated type is the statement', []
    bs = binders_of(head)
    bad = [b for b in bs if not b['cls']]
    if bad:
        raise BinderUnclassed('; '.join('%s %s : %s (%s)' % (b['kind'], b['name'], b['type'], b['how']) for b in bad))
    hyp = [b for b in bs if (b['typing'] == 'prop' and b['kind'] in _KIND_INDEX) or b['outcome'] == 'seam']
    facts = [b for b in bs if b['cls'] == 'B04']
    nm = lambda b: b['name'] if b['kind'] != 'instance' else (b['name'] or '[inst]')   # noqa: E731
    pairs = lambda xs: ', '.join('%s : %s' % (nm(b), b['type']) for b in xs)   # noqa: E731
    read = [(nm(b), b['type']) for b in hyp + facts]
    enc = [b for b in hyp if b['form'] == 'itself']
    if enc:
        return 'ENCODES-CONCLUSION', 'the conclusion is the binder ' + pairs(enc), read
    unl = [b for b in hyp if b['outcome'] == 'unlisted']
    if unl:          # ### (R243)(2): a predicate met for the first time is printed, not graded INTERFACES
        return 'PREDICATE-UNLISTED', pairs(unl), read
    prem = [b for b in hyp if b['outcome'] in ('premise', 'seam')] + facts
    if prem:
        return 'INTERFACES', pairs(prem), read
    if read:
        return 'DERIVES', 'domain conditions only: ' + pairs(hyp + facts), read
    return 'DERIVES', 'no hypothesis binder', read


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
        ('(H : NontrivialZeroExistsInStrip) : True', 'theorem', 'INTERFACES'),      # ### b637: a premise named otherwise than h…
        ('(x : ℕ) (y : ℝ) : x = x', 'theorem', 'DERIVES'),                          # ### b637: data binders, no hypothesis
    ]
    return all(grade(h, k)[0] == want for h, k, want in cases)


if __name__ == '__main__':
    ok = self_test()
    print('\n'.join(RULE_TEXT))
    print('### self-test (twenty headers, both polarities): %s' % ('PASS' if ok else 'FAIL'))
    raise SystemExit(0 if ok else 1)
