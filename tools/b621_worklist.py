# -*- coding: utf-8 -*-
"""b621_worklist.py -- THE ACT'S WORK-LIST, UNDER (R231) AND THE AUTHOR'S ANSWER BEFORE THE SEAL. ### DATA AND RESOLVERS ONLY; WRITES NOTHING.

### (1) THE MONOGRAPH: every change v5.18 makes to v5.17, each an exact fragment of a v5.17 body line and its replacement, with the clause,
### the second reader's items it answers and what it cites. The ruled items: (R231)(3)(i)'s enumeration sentence; every residue sentence
### either reader read BEYOND (the author's answer before the seal, option 3: the 13 both read BEYOND, the 19 the seat read BEYOND and the
### reader AT, the one the reader read BEYOND and the seat AT -- 33 items); the sentences restating a ruled claim (the restatement clause,
### OPEN_TRAILS :12192), found by the needle survey and read by hand; one history line beneath the dated block of 2026-08-14 (the history
### clause, OPEN_TRAILS :11908), which the precedence order (:12228) sets above the ceiling and restatement clauses.
### (2) THE ROWS: the 52 sampled rows the reader graded otherwise, each with its verdict under (R231)(3)(iii); the six kernel-verified rows
### with the terminal's statement read at its pin; the cells the syntheses' next versions change.
"""
import os
import re
import subprocess

PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = chr(10)
M17 = 'day1/A_Place_to_Stand_v5_17.md'
M18 = 'day1/A_Place_to_Stand_v5_18.md'
PRE_PP = 'e6a3fbf'
M_CORR = 2241        # ### v5.17's own Correspondence heading: the body is every line above it


def show(rev, path, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    ls = (t or '').replace(chr(13), '').split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


# ================================================================================ CITATIONS, WRITTEN ONCE
RH60 = ('RH-60 (the sieve v0.5 :124: each class’s exclusion compiles as a statement about a real σ alone, the Euler product entering none; '
        'the step from the classes to ξ’s zeros is the located clause)')
F7210 = 'FINDINGS :7210 (as compiled, the seven-class exclusion is a family of σ-conditions and its joint step is RH restated)'
NONE_P = ('none_produce (SIDE-kernel v1.5 = 0e5233f, Bridge/TheBridgeComplete.lean :198) over produces_offline (:157), its C₂ case '
          'σ ≠ 1/2 ∧ -σ = -(1 - σ) (:159)')
H2S = 'h2_sign_iff_rh (SIDE-explicit-formula v0.2 = 5c72cad, ζ page node 8)'
OT12072 = 'OPEN_TRAILS :12072 (the author’s reading: the place count closed by Ostrowski, the exhaustiveness at ξ the open clause h2)'
T2 = 'conservation_of_spectra (SIDE-kernel v1.5 = 0e5233f, Kernel/ProductFormula_Rat.lean :72: ∀ (s : Int), (1 : Rat) ^ s = 1), T2'
BAL = 'balance_theorem (SIDE-kernel v1.5 = 0e5233f, Kernel/Voice1.lean :22: for a prime p, p ^ (−s) = p ^ (−(1 − s)) ↔ s = 1/2)'
README = 'README :106-:111'
FOLD = 'the Fold Criterion of §4.5 (v5.17 :314): the absence of folds is RH-equivalent'

# ================================================================================ (1) THE MONOGRAPH
# ### (id, v5.17 line, old fragment, new fragment, clause, the second reader's items, why)
_C = 'the ceiling clause (OPEN_TRAILS :11906)'
_C3I = 'the ceiling clause under (R231)(3)(i)'
_CA = 'the ceiling clause under (R231)(3)(iv) and the author’s answer before the seal'
_R = 'the restatement clause (OPEN_TRAILS :12192)'
CHANGES = [
    # ### (R231)(3)(i) -- the enumeration sentence, and the reader's other objects on its line (X004)
    ('C01', 1218, 'The reduction examines seven mechanism classes and finds that none produces off-line zeros.',
     "The reduction examines seven mechanism classes and finds that each class's exclusion, as compiled, is a condition on a real σ alone, while "
     "the step from the classes to ξ's zeros is the located clause, open (RH-60, the sieve v0.5 :124, and FINDINGS :7210).",
     _C3I, ['S045', 'X004'], 'states unconditionally that no mechanism produces off-line zeros; as compiled the seven exclusions are σ-conditions '
     'and the step to ξ’s zeros is the located clause (the reader’s verdict upheld, (R231)(3)(i))', [RH60, F7210, NONE_P]),
    ('C02', 1218, "The balance theorem (C₂ (Euler/multiplicative) — the Euler product's identification of σ = 1/2) identifies the critical line.",
     "The balance theorem (C₂ (Euler/multiplicative) — compiled for a prime p as p^(−s) = p^(−(1−s)) if and only if s = 1/2, a condition on a "
     "real s in which the Euler product does not enter) identifies the critical line.",
     _CA, ['X004'], 'C₂ glossed as the Euler product’s identification of σ = 1/2; the compiled balance is a condition on a real exponent', [BAL, RH60]),
    ('C03', 1218, 'The exhaustive catalogue certifies that no class produces an alternative location.',
     'The catalogue, were it exhaustive at ξ — the open clause h2 — would certify that no class produces an alternative location.',
     _CA, ['X004'], 'the catalogue’s exhaustiveness at ξ, the open clause h2, read as settled', [OT12072, H2S]),
    ('C04', 1960, '| Verified (systematic enumeration) |',
     "| Per-class exclusions compiled as conditions on a real σ (none_produce); the step to ξ's zeros the located clause, open (RH-60) |",
     _CA, ['X036'], 'the row’s status “Verified” for no class producing off-line zeros reads past none_produce, a statement about a real σ; '
     'the title cell is a name and carries (collision CL1)', [NONE_P, RH60]),
    ('C05', 318, 'real-valued, perpendicular, monotone, convex, and unfoldable.',
     'real-valued, perpendicular, monotone, convex, and unfoldable at the 25,000 sample points checked — the absence of folds everywhere being '
     'RH-equivalent and open.', _CA, ['X159'], 'ξ said unfoldable, where the absence of folds is RH-equivalent', [FOLD]),
    ('C06', 452, 'Part I establishes *where* the zeros must be.',
     'Part I identifies *where* the zeros must be if the open clause h2 holds: the line σ = 1/2.',
     _CA, ['X051'], 'Part I said to establish where the zeros must be; it identifies the line, the placement the open clause', [H2S]),
    ('C07', 767, 'because they establish the seal that makes a finite catalogue sufficient:',
     'because they argue for the seal that would make a finite catalogue sufficient, its exhaustiveness at ξ being the open clause h2:',
     _CA, ['X073'], 'two chapters said to establish the seal that makes the catalogue sufficient; the seal is argued, the sufficiency at ξ is h2',
     [OT12072, T2]),
    ('C08', 1019, 'a path identifies where the zeros are, a closure establishes why they cannot be elsewhere.',
     "a path identifies the line, a closure argues why the zeros would not be elsewhere, its step to ξ's zeros the located clause.",
     _CA, ['X130'], 'a closure said to establish why the zeros cannot be elsewhere', [RH60]),
    ('C09', 1115, 'The following five results establish this conversion.',
     "The following five results argue for this conversion; at ξ's zeros it is the located clause, open (RH-60).",
     _CA, ['X136'], 'five results said to establish the conversion from generic to actual', [RH60]),
    ('C10', 1129, 'The five CLOSURES each independently establish that codimension-2 coincidences cannot occur — they seal the exits.',
     "The five CLOSURES each independently argue that codimension-2 coincidences cannot occur — at ξ's zeros that step is the located clause, "
     "open (RH-60).", _CA, ['X163'], 'the five closures said each to establish that codimension-2 coincidences cannot occur', [RH60]),
    ('C11', 1131, 'The codimension question is resolved not by one argument but by five independent results, each using different mathematics:',
     "The codimension question is addressed not by one argument but by five independent results, each using different mathematics, its step "
     "to ξ's zeros the located clause, open:", _CA, ['X100'], 'the codimension question said resolved by five results', [RH60]),
    ('C12', 1097, 'The changed variable is the Euler product — mechanism class C₂ (Euler/multiplicative) in the catalogue.',
     "The changed variable is the Euler product — read as mechanism class C₂ (Euler/multiplicative) in the catalogue, though C₂'s compiled "
     "exclusion is a condition on a real σ in which the product does not enter (RH-60).",
     _CA, ['X158'], 'the Euler product said to be mechanism class C₂', [RH60, NONE_P]),
    ('C13', 1097, 'Keep it and zeros stay (confirmed computationally for 10¹³+ zeros of ζ).',
     'Keep it and the zeros computed stay on the line (10¹³+ zeros of ζ), that every zero does being the located clause, open.',
     _CA, ['X158'], 'with the Euler product the zeros said to stay, beyond the finite computation', [H2S]),
    ('C14', 1099, 'The Euler product (C₂) provides the confinement — the multiplicative balance that holds zeros at σ = 1/2.',
     "The Euler product (C₂) is read as the confinement — the multiplicative balance read as holding zeros at σ = 1/2, though C₂'s compiled "
     "exclusion is a condition on a real σ alone and the confinement of ξ's zeros is the located clause (RH-60).",
     _CA, ['X091'], 'the Euler product (C₂) said to provide the confinement that holds zeros at σ = 1/2', [RH60]),
    ('C15', 1099, 'Remove C₂ and the confinement fails.', 'Remove the Euler product and the confinement fails.',
     _CA, ['X091'], 'removing C₂ read as removing the Euler product; the experiment removes the product', [RH60]),
    ('C16', 1198, 'then removing C₂ (the Euler product) alone should not', 'then removing the Euler product (read as C₂) alone should not',
     _CA, ['X148'], 'removing C₂ read as removing the Euler product', [RH60]),
    ('C17', 1198, 'But removing C₂ always produces off-line zeros', 'But removing the Euler product always produces off-line zeros',
     _CA, ['X148'], 'removing C₂ read as removing the Euler product', [RH60]),
    ('C18', 1198, 'This means the Euler product is the entire confinement mechanism.',
     'This is read as the Euler product being the whole of the confinement; that it confines every zero of ξ is the located clause, open (RH-60).',
     _CA, ['X148'], 'the Euler product said to be the entire confinement mechanism, implying the catalogue complete and RH', [RH60, H2S]),
    ('C19', 1198, '— is confirmed by the experiment.',
     "— is supported by the experiment as evidence, the catalogue's exhaustiveness at ξ being the open clause h2.",
     _CA, ['X148'], 'that no eighth class contributes said confirmed by the experiment; the exhaustiveness at ξ is h2', [OT12072]),
    ('C20', 931, 'With both constraints, the two close from opposite sides: transversality from σ = 1/2 (C₃, functional equation) meets the '
     'zero-free region from σ = 1 (C₂, Euler product).',
     'With both constraints, the two act from opposite sides — transversality from σ = 1/2 (C₃, functional equation) and the zero-free region '
     'from σ = 1 (C₂, Euler product) — and that they close across the strip is the located clause, open (RH-60).',
     _CA, ['X153'], 'the two constraints said to close from opposite sides, implying no off-line zeros', [RH60, H2S]),
    ('C21', 68, 'Part I establishes the structural significance of σ = 1/2.', 'Part I argues the structural significance of σ = 1/2.',
     _CA, ['X054'], 'a reading guide says an argument Part establishes σ = 1/2’s significance', []),
    ('C22', 417, 'and established for ξ in Part III;', 'and argued for ξ in Part III;',
     _CA, ['X034'], 'the I+D+S conditions said established for ξ in an argument Part', []),
    ('C23', 421, 'Symmetry — established for ξ in Chapter 13)', 'Symmetry — argued for ξ in Chapter 13)',
     _CA, ['X042'], 'the I+D+S conditions said established for ξ in Chapter 13', []),
    ('C24', 462, 'Part I established that σ = 1/2 is structurally distinguished', 'Part I argued that σ = 1/2 is structurally distinguished',
     _CA, ['X131'], 'Part I said to have established σ = 1/2 distinguished', []),
    ('C25', 535, 'Conservation of Spectra (argued within ZFC — Chapter 13) establishes that this binding constraint is spectrally silent.',
     'Conservation of Spectra (argued within ZFC — Chapter 13, its Lean terminal stating `∀ s : ℤ, (1 : ℚ) ^ s = 1`, T2) argues that this '
     'binding constraint is spectrally silent.',
     _CA, ['X119'], 'an argued chapter said to establish spectral silence; the compiled terminal states (1 : ℚ)^s = 1', [T2]),
    ('C26', 848, '(C₂ (Euler/multiplicative)).',
     '(C₂ (Euler/multiplicative), whose compiled exclusion is a condition on a real σ in which the Euler product does not enter, RH-60).',
     _CA, ['X062'], 'unique factorization and the Euler product assigned to C₂', [RH60, NONE_P]),
    ('C27', 890, '| Balance at σ = 1/2; unique factorization |',
     '| Balance at σ = 1/2, compiled as a condition on a real σ in which the Euler product does not enter (RH-60); unique factorization |',
     _CA, ['X010'], 'the table gives C₂’s source as the multiplicative structure (Euler product)', [RH60, NONE_P]),
    ('C28', 905, 'It produces no off-line zeros because the balance explicitly fails at σ ≠ 1/2.',
     "Its exclusion is that the balance fails at σ ≠ 1/2, a condition on a real σ in which the Euler product does not enter; the step from it to "
     "ξ's zeros is the located clause (RH-60).",
     _CA, ['X157'], 'C₂ named as the Euler product’s balance; the compiled condition carries no product', [BAL, NONE_P, RH60]),
    ('C29', 945, 'The Epstein zeta functions (functional equation without Euler product) separate the transformation-stage classes.',
     "The Epstein zeta functions (functional equation without Euler product) separate the transformation-stage classes as the classes are read; "
     "as compiled, each class's exclusion is a condition on a real σ that holds beside the Epstein configuration too (RH-60).",
     _CA, ['X017'], 'the Euler product read as the class Epstein lacks, separating the classes', [RH60]),
    ('C30', 985, '| Relates prime sums to zero sums via Euler product + Hadamard |',
     "| Relates prime sums to zero sums via Euler product + Hadamard; the prime side enters here, at the explicit formula, not at C₂'s compiled "
     "exclusion (RH-60) |", _CA, ['X104'], 'the explicit formula’s row: prime sums via the Euler product, set under C₂', [RH60, F7210]),
    ('C31', 1168, 'The Euler product identifies σ = 1/2 and fails elsewhere.',
     'The balance condition read from the Euler product identifies σ = 1/2 and fails elsewhere, a condition on a real σ in which the product '
     'does not enter (RH-60).', _CA, ['X031'], 'the enumeration’s step (7): the Euler product said to identify σ = 1/2', [BAL, RH60]),
    ('C32', 1214, "and applies it through results ranging from 1737 (Euler product) to 1950 (Tate's thesis).",
     "and applies it through results ranging from 1737 (Euler product) to 1950 (Tate's thesis), its class exclusions compiled as conditions on "
     "a real σ in which the Euler product does not enter (RH-60).",
     _CA, ['X070'], 'the reduction’s enumeration said to apply results from the Euler product on', [RH60, F7210]),
    ('C33', 1276, 'The four SIDE conditions are verified for each L(s, χ) in §20.1, with the independence transfer demonstrated explicitly for '
     'χ mod 5 in §20.2.',
     'The four SIDE conditions are argued for each L(s, χ) in §20.1, with the independence transfer worked explicitly for χ mod 5 alone in §20.2.',
     _CA, ['X084'], 'the SIDE conditions said verified for each L(s, χ), the transfer shown for χ mod 5 alone', []),
    ('C34', 1392, '- **C₂ (Euler product):**',
     '- **C₂ (Euler balance, compiled as a condition on a real σ in which the product does not enter, RH-60):**',
     _CA, ['X049'], 'C₂ named as the Euler product', [RH60, BAL]),
    ('C35', 1491, 'The Euler product provides the balance but does not cancel the derivative.',
     "C₂'s balance, compiled as a condition on a real σ in which the Euler product does not enter (RH-60), fixes σ = 1/2 but does not cancel "
     "the derivative.", _CA, ['X133'], 'the per-class answer: the Euler product said to provide the balance', [RH60, BAL]),
    ('C36', 1884, 'Epstein functions have C₃ (functional equation) but lack C₂ (Euler product), demonstrating that the transformation-stage '
     'classes are independent.',
     "Epstein functions have the functional equation but lack the Euler product, read as separating C₃ from C₂, though C₂'s compiled exclusion "
     "is a condition on a real σ that holds beside them too (RH-60).",
     _CA, ['X118', 'X028'], 'the Epstein experiment read as demonstrating class independence, Epstein said to lack C₂ (Euler product)', [RH60]),
    ('C37', 1884, 'Polynomials and Hadamard products demonstrate that the output-stage classes are independent.',
     'Polynomials and Hadamard products are offered as separating the output-stage classes.',
     _CA, ['X099'], 'polynomials and Hadamard products read as demonstrating output-stage independence', []),
    ('C38', 1888, 'The multiplicative monoid (ℤ \\ {0}, ×) with unique factorization produces C₂ (the Euler product).',
     "The multiplicative monoid (ℤ \\ {0}, ×) with unique factorization produces the Euler product, read as C₂, whose compiled exclusion is a "
     "condition on a real σ in which the product does not enter (RH-60).",
     _CA, ['X075'], 'the multiplicative monoid said to produce C₂ (the Euler product)', [RH60, NONE_P]),
    # ### the restatement clause: unmarked sentences restating a ruled claim, the rest unchanged
    ('P01', 37, 'Seven mechanism classes, each checked, none producing zeros off the critical line.',
     "Seven mechanism classes, each checked, each exclusion compiled as a condition on a real σ, the step to ξ's zeros the located clause (RH-60).",
     _R, ['C01'], 'restates (R231)(3)(i)’s claim: none producing zeros off the line, unconditionally', [RH60, F7210]),
    ('P02', 117, 'each class still identifies σ = 1/2 and none produces offline zeros.',
     "each class still identifies σ = 1/2 and none produces offline zeros by its compiled exclusion, a condition on a real σ, the step to ξ's "
     "zeros being the located clause (RH-60).", _R, ['C01'], 'restates (R231)(3)(i)’s claim', [RH60]),
    ('P03', 314, 'The curves do not fold — verified across 25,000 sample points spanning the first 10,000 zeros with zero exceptions.',
     'The curves do not fold at the points checked — 25,000 sample points spanning the first 10,000 zeros, with zero exceptions — and that none '
     'folds anywhere is RH-equivalent and open.', _R, ['C05'], 'restates the unfoldable claim of C05 beyond the finite check', [FOLD]),
    ('P04', 462, 'Part II develops the method for proving that no other point shares this distinction: no zeros of ξ exist off the critical line.',
     'Part II develops the method by which the reduction argues that no other point shares this distinction: that no zeros of ξ lie off the '
     'critical line is the located clause, open.', _R, ['C06'], 'restates C06’s claim, where the zeros must be, as the method’s result', [H2S]),
    ('P05', 553, 'Therefore the catalogue is complete.',
     "Therefore the catalogue's place count is closed; its exhaustiveness at ξ is the open clause h2 (§27.3).",
     _R, ['C03'], 'restates C03’s claim, the exhaustive catalogue, at ξ', [OT12072]),
    ('P06', 795, 'This is the seal that makes the seven-class enumeration (Chapter 15) sufficient.',
     'This is the seal argued to make the seven-class enumeration (Chapter 15) sufficient, its exhaustiveness at ξ the open clause h2 (§27.3).',
     _R, ['C07'], 'restates C07’s claim, the seal that makes the catalogue sufficient', [OT12072, T2]),
    ('P07', 795, 'it is a count of *all* mechanisms, sealed by the spectral inertness of the only interface.',
     'it is argued to be a count of *all* mechanisms, sealed by the spectral inertness of the only interface, its exhaustiveness at ξ the open '
     'clause h2.', _R, ['C07'], 'restates C07’s claim', [OT12072]),
    ('P08', 929, 'None produces a codimension-2 coincidence at σ ≠ 1/2.',
     'None produces a codimension-2 coincidence at σ ≠ 1/2 by its compiled exclusion, a condition on a real σ; that ξ has none there is the '
     'located clause (RH-60).', _R, ['C01'], 'restates (R231)(3)(i)’s claim', [RH60, NONE_P]),
    ('P09', 1113, 'Seven mechanism classes, none producing the codimension-2 coincidence Re = Im = 0 at σ ≠ 1/2.',
     'Seven mechanism classes, none producing the codimension-2 coincidence Re = Im = 0 at σ ≠ 1/2 by its compiled exclusion, a condition on a '
     'real σ; that ξ has none there is the located clause (RH-60).', _R, ['C01'], 'restates (R231)(3)(i)’s claim', [RH60]),
    ('P10', 1133, 'The seven-class catalogue is complete.',
     "The seven-class catalogue's place count is complete; its exhaustiveness at ξ is the open clause h2 (§27.3).",
     _R, ['C03'], 'restates C03’s claim at ξ', [OT12072]),
    ('P11', 1133, 'The search space is closed by a classification theorem.', 'The place count is closed by a classification theorem.',
     _R, ['C03'], 'restates C03’s claim: the search space, the catalogue at ξ', [OT12072]),
    ('P12', 1135, 'Systems with it do not (computationally).',
     'Systems with it show none in the computations (10¹³+ zeros of ζ), that none has any being the located clause, open.',
     _R, ['C13'], 'restates C13’s claim beyond the finite computation', [H2S]),
    ('P13', 1139, '— and none exists.', '— and none is found among the seven classes, that none exists at ξ being the located clause, open (RH-60).',
     _R, ['C01'], 'restates (R231)(3)(i)’s claim', [RH60]),
    ('P14', 1141, 'and no mechanism class provides one.',
     "and no mechanism class provides one by its compiled exclusion, a condition on a real σ, that step at ξ's zeros being the located clause "
     "(RH-60).", _R, ['C01'], 'restates (R231)(3)(i)’s claim', [RH60]),
    ('P15', 1143, '— off-line zeros do not occur —', '— that off-line zeros do not occur, which at ξ is the located clause, open —',
     _R, ['C10', 'C11'], 'restates C10’s and C11’s claim, the closures’ conclusion', [RH60, H2S]),
    ('P16', 1168, 'None of the seven couples Re(ξ) to Im(ξ) at any single off-line point.',
     'None of the seven couples Re(ξ) to Im(ξ) at any single off-line point by its compiled exclusion, a condition on a real σ; that ξ has no '
     'off-line zero is the located clause (RH-60).', _R, ['C01'], 'restates (R231)(3)(i)’s claim', [RH60, NONE_P]),
    ('P17', 1184, '(system sealed)              (catalogue exhaustive)', '(seal argued)                (exhaustive at ξ: h2, open)',
     _R, ['C07', 'C03'], 'the diagram’s labels restate C07’s and C03’s claims', [OT12072]),
    ('P18', 1187, '(C₁–C₇: none produces off-line zeros)', '(C₁–C₇: each a condition on a real σ)',
     _R, ['C01'], 'the diagram’s label restates (R231)(3)(i)’s claim', [RH60, NONE_P]),
    ('P19', 1191, 'Riemann Hypothesis', 'Riemann Hypothesis, under h2 (open)',
     _R, ['C01'], 'the diagram reaches RH from the classes with no clause named; the step is the located clause', [H2S, RH60]),
    ('P20', 1276, 'none produces off-line zeros for the same structural reasons as for ξ.',
     "each class's exclusion a condition on a real σ, as for ξ (RH-60).", _R, ['C01'], 'restates (R231)(3)(i)’s claim for each L(s, χ)', [RH60]),
    ('P21', 1785, 'This seals the system: no external force exists.',
     'This is argued to seal the system, no external force existing; its Lean terminal states only `∀ s : ℤ, (1 : ℚ) ^ s = 1` (T2).',
     _R, ['C07', 'C25'], 'restates C07’s and C25’s claim, the seal', [T2]),
    ('P22', 1914, 'Seven mechanism classes, each examined, none producing zeros off the critical line.',
     "Seven mechanism classes, each examined, each exclusion compiled as a condition on a real σ, the step to ξ's zeros the located clause (RH-60).",
     _R, ['C01', 'C04'], 'restates (R231)(3)(i)’s claim', [RH60]),
    ('P23', 1914, 'Conservation of Spectra proving the system is closed.', 'Conservation of Spectra arguing the system is closed.',
     _R, ['C07', 'C25'], 'restates C07’s and C25’s claim', [T2]),
    ('P24', 1914, 'The exhaustive catalogue certifying that no structural consequence was missed.',
     'The catalogue, its exhaustiveness at ξ the open clause h2, read as missing no structural consequence.',
     _R, ['C03'], 'restates C03’s claim', [OT12072]),
    ('P25', 724, 'Chapters 13 and 14 seal the system, proving that the one interface',
     'Chapters 13 and 14 argue for the seal of the system, that the one interface',
     _R, ['C07', 'C25'], 'restates C07’s and C25’s claim, the seal established', [T2]),
    ('P26', 724, 'because it is what makes a finite catalogue sufficient:',
     'because it is argued to make a finite catalogue sufficient, the exhaustiveness at ξ remaining the open clause h2:',
     _R, ['C07'], 'restates C07’s claim', [OT12072]),
    ('P27', 724, 'and checks each: none couples the two conditions off the line.',
     "and checks each: none couples the two conditions off the line by its compiled exclusion, a condition on a real σ, the step at ξ's zeros "
     "the located clause (RH-60).", _R, ['C01'], 'restates (R231)(3)(i)’s claim', [RH60]),
    ('P28', 1125, 'and no mechanism class provides coupling).',
     "and no mechanism class provides coupling by its compiled exclusion, a condition on a real σ, the step at ξ's zeros the located clause).",
     _R, ['C01'], 'restates (R231)(3)(i)’s claim', [RH60]),
    ('P29', 1413, 'seven classes, none producing off-line zeros, exhaustive by Ostrowski.',
     'seven classes, each exclusion a condition on a real σ, their place count closed by Ostrowski and their exhaustiveness at ξ the premise.',
     _R, ['C01', 'C03'], 'restates (R231)(3)(i)’s claim and C03’s, the catalogue exhaustive by Ostrowski', [RH60, OT12072]),
    ('P30', 1845, 'follows from the same fold exclusion (§22.5–§22.6), with the 25,000-point record confirming it.',
     'would follow from the same fold exclusion (§22.5–§22.6), itself the open direction, the 25,000-point record consistent with it.',
     _R, ['C05'], 'restates C05’s claim: R-curves said not to fold, beyond the finite record', [FOLD]),
]
# ### the survey's hits on lines no change touches, each read by hand and carried, with its reason (the dated block's hits go to the
# ### history line; the rewritten lines are the changes above)
SURVEY_KEPT = {
    130: 'a count of the reduction’s parts, the open premise named', 167: 'states what RH asserts, not that it holds',
    207: 'names the paths and the closures as objects', 344: 'the n₄ = 0 count’s reading, argued in Chapter 13',
    358: 'the identification redundancy among the classes: each identifies the line, none placing the zeros',
    436: 'the derivative-level joint step named as the open geometric clause', 438: 'the method’s general principle (Part II), not a claim at ξ',
    493: 'the method’s template, stated generally', 549: 'the method’s condition E stated generally (Part II)',
    564: 'the method’s template across the table', 635: 'the method stated conditionally (“if ... provably complete”)',
    637: 'the Mechanism Theorem’s general statement', 653: 'the syllogism’s step, general', 675: 'the method’s test case (CH)',
    793: 'the product formula’s reading, argued in Chapter 13', 833: 'the Silence Principle’s chain, general',
    837: 'the distributive interface’s reading', 855: 'a count closed at the places', 861: 'the n₄ = 0 stage contributes no class, a count',
    919: 'the modular surface’s completeness, a classical fact', 951: 'Ostrowski’s classification, a theorem of the literature',
    997: 'what an eighth class would require, the place count', 1105: 'a chapter title (the name-and-title exception)',
    1127: 'a section title (the name-and-title exception)', 1137: 'the paths’ coverage of the classes, not a placement',
    1194: 'names the seal', 1313: 'the derivative-level joint step named as the open geometric clause',
    1394: 'a per-class statement at the derivative level, the joint step named open at :1399',
    1399: 'the joint step named as the open geometric clause', 1463: 'the paths’ coverage of the classes',
    1597: 'the compiled conjunction read as it states: none_produce is the algebraic signature',
    1613: 'the compiled implication from the premise, conditional', 1695: 'the kernel’s axiom audit, a closure of the audit',
    1771: 'a version note naming Closure 5', 1799: 'the premise section’s preface', 1801: 'the five registers, each at its stated depth',
    1807: 'the literature’s results (Voros), cited', 1820: 'h1 at the witness, compiled', 1849: 'other domains’ completeness, flagged '
    'for independent scrutiny', 1916: 'the method’s template, the exhaustiveness at ξ named open', 2063: 'the glossary’s Mechanism Theorem',
    2077: 'the glossary’s Silence Principle', 2100: 'the valence dichotomy, a finite fact', 2189: 'a version-history entry',
}
# ### the history clause: one line beneath the dated block's paragraph (v5.17 :2231-:2239), inserted after the blank line :2240
HISTORY_AFTER = 2240
HISTORY = ('*v5.18, 2026-10-04, a history line under the paragraph above, the dated block of 2026-08-14 carried as its record, under `(R231)`(3)(iv) '
           "and the restatement clause: the five closures of §18.3 argue that codimension-2 coincidences cannot occur off the critical line, and "
           "the catalogue's place count is closed by Ostrowski while its exhaustiveness at ξ is the open clause h2 (§27.3); each class's exclusion "
           "compiles as a condition on a real σ alone, and the step from the classes to ξ's zeros is the located clause, open (RH-60, the sieve "
           "v0.5 :124, and FINDINGS :7210) -- in its Weil form h2_sign, equivalent to RH (h2_sign_iff_rh); the seals are argued, and the argument "
           "reduces RH to its located clause without settling it (README :106-:111).*")
HISTORY_ITEMS = ['X102']
HISTORY_COVERS = [(2232, 'the paragraph’s seven-classes sentence: “Four classical theorems certify the decomposition is exhaustive” and '
                         '“none produces the codimension-2 coincidence”, restating C03 and (R231)(3)(i)'),
                  (2234, 'the five-closures sentence, X102, the reader’s BEYOND (R231)(3)(iv)'),
                  (2238, 'the layers sentence: “the seals that close it” and “only one answer exists”, restating C07 and C03')]
HISTORY_CITES = [RH60, F7210, H2S, README]

# ### every ruled residue item and its change(s): the author's answer's 33
ITEMS_BOTH = ['X153', 'X158', 'X091', 'X148', 'X004', 'X159', 'X051', 'X073', 'X130', 'X136', 'X163', 'X100', 'X036']
ITEMS_READER = ['X102']
ITEMS_SEAT = ['X054', 'X034', 'X042', 'X131', 'X119', 'X062', 'X010', 'X157', 'X017', 'X104', 'X031', 'X070', 'X084', 'X049', 'X133',
              'X118', 'X028', 'X099', 'X075']

# ### the precedence order's collisions (OPEN_TRAILS :12228), each resolved by the seat and listed in the back matter
COLLISIONS = [
    ('CL1', 1960, 'the name-and-title exception and the ceiling clause on one table row (X036)', 'the title cell “Seven mechanism classes, none '
     'producing off-line zeros” is the row’s name and carries; the status cell takes the ceiling (C04)'),
    ('CL2', 2234, 'the history clause and the ceiling clause (X102, a sentence of the dated block of 2026-08-14)', 'the history clause governs: '
     'the sentence carries as a dated record and the history line beneath the paragraph states what the compiled facts say'),
    ('CL3', 2232, 'the history clause and the restatement clause (:2232 and :2238 in the same dated block)', 'the history clause governs: both '
     'carry, the one history line beneath the paragraph naming them'),
    ('CL4', 1218, '(R231)(3)(i) and the residue item X004 on one line', 'one rewrite of the enumeration sentence answers both (C01); the '
     'line’s other two sentences X004 names take the ceiling by the author’s answer (C02, C03)'),
    ('CL5', 1884, 'the seed’s item X028 and the addendum’s X118 name one sentence', 'one rewrite answers both (C36); the line’s second sentence, '
     'X099, takes its own (C37)'),
    ('CL6', 0, 'a ruled item and a restating sentence on one line (:462, :1097, :1099, :1133, :1168, :1198, :1218, :1276)', 'each sentence takes '
     'its own clause, the rest of the line unchanged'),
]

# ### the needle survey behind the restatement clause: every body hit, the restated claim, and the fate
SURVEY_NEEDLES = [
    ('none-produces', r'none produc|none of the seven|no class produc|no mechanism class produc'),
    ('closures', r'closure|seal the exit|cannot be elsewhere|codimension question'),
    ('established', r'established for ξ|establishe[sd]? (that|where|the)'),
    ('seal', r'the seal|system is closed|is closed\b|spectrally silent'),
    ('certifies', r'catalogue certif|certif(y|ies|ying) that no|no structural consequence'),
    ('where-the-zeros', r'zeros must|must lie|where the zeros'),
    ('folds', r'unfoldable|no folds|fold-free|do not fold'),
    ('no-mechanism', r'no mechanism|none exists|(cannot|can not|do not|does not) occur|only one answer|seals? (the|that)|is complete\b'),
]


def resolve_changes(M=None):
    """### every change's old fragment occurs exactly once on its v5.17 line; returns (M, bad)."""
    M = M or lines_of(show(PRE_PP, M17))
    bad = []
    for cid, n, old, new, *_r in CHANGES:
        if not (0 < n < M_CORR) or M[n - 1].count(old) != 1:
            bad.append((cid, n, M[n - 1].count(old) if 0 < n <= len(M) else None))
    if M[HISTORY_AFTER - 1] != '' or M[HISTORY_AFTER] != '' and not M[HISTORY_AFTER].startswith('## Correspondence'):
        bad.append(('H1', HISTORY_AFTER, 'not a blank line before the Correspondence heading'))
    if not M[M_CORR - 1].startswith('## Correspondence *(added 2026-08-12'):
        bad.append(('CORR', M_CORR, M[M_CORR - 1][:40]))
    return M, bad


# ================================================================================ (2) THE ROWS
GRADES = ('kernel-verified', 'theorem-supported', 'computationally-verified', 'argument-supported', 'synthesis-suggested', 'statement-grade')
SYN = {
    'P12': 'phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md',
    '15E': 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md',
    '2B': 'phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md',
    '2D': 'phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS_v0_2.md',
    '2F': 'phase2/empirical/ZERO_SIMPLICITY_AND_THE_FORMATION_TRANSFER_TO_ELLIPTIC_CURVES.md',
    '2G': 'phase2/physics-speculative/THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md',
}
NEXT = {'P12': (SYN['P12'][:-3] + '_v0_2.md', 'v0.2', 'v0.1'), '15E': (SYN['15E'][:-3] + '_v0_2.md', 'v0.2', 'v0.1'),
        '2B': (SYN['2B'][:-3] + '_v0_2.md', 'v0.2', 'v0.1'), '2D': (SYN['2D'].replace('_v0_2.md', '_v0_3.md'), 'v0.3', 'v0.2'),
        '2F': (SYN['2F'][:-3] + '_v0_2.md', 'v0.2', 'v0.1'), '2G': (SYN['2G'][:-3] + '_v0_2.md', 'v0.2', 'v0.1')}

# ### the six kernel-verified rows: (paper, its pin, the lines printed beside the cited one -- (start, end, cited|omitted)),
# ### and the terminal statements read at their pins -- (repo, rev, path, start, end)
KV = {
    'R060': dict(paper=('phase1.5/proofs/MECHANISM_EXCLUSION.md', 'f374bba', [(145, 145, 'cited'), (408, 408, 'naming the terminal at its pin')]),
                 terms=[('D:/SIDE-kernel', 'b1407b2', 'Kernel/SpectralCannonFull.lean', 58, 59)],
                 verdict='stands', reason='the statement at the pin is the paper’s line: the real part of the derivative of completedRiemannZeta₀ '
                 '(the paper’s Λ₀) vanishes at every point of the critical line, so the derivative is purely imaginary there'),
    'R066': dict(paper=('phase1.5/proofs/INTEGRATED_PROOF.md', 'f374bba', [(97, 98, 'cited')]),
                 terms=[('D:/SIDE-kernel', 'b1407b2', 'Kernel/Voice1.lean', 22, 24)],
                 verdict='stands', reason='the statement is the balance for a prime p and a real exponent: p^(−s) = p^(−(1−s)) if and only if '
                 's = 1/2, the claim; the terminal is the one EA :538 and :542, papers of the same cluster, name at v1.2, as the row states'),
    'R089': dict(paper=('phase1.5/proofs/IDS_TO_RH.md', 'f374bba', [(300, 300, 'omitted by the packet: the file named'), (302, 302, 'cited')]),
                 terms=[('D:/SIDE-kernel', 'b1407b2', 'Kernel/Integration.lean', 201, 202), ('D:/SIDE-kernel', 'b1407b2', 'Kernel/Integration.lean', 210, 212)],
                 verdict='stands', reason='IR :300 names `Integration.lean` as “the assembled conditional” and :302 its pin; the theorem there '
                 'states the conditional StructuralExhaustiveness → RiemannHypothesis the claim names, with StructuralExhaustiveness defined '
                 'as ∀ σ, is_xi_zero σ → σ = 1/2; that the paper argues for the antecedent is the paper’s own sentence at :302'),
    'R108': dict(paper=('phase1.5/proofs/THE_EXCLUSION_ARCHITECTURE.md', 'f374bba', [(540, 540, 'omitted by the packet: the file named'), (542, 542, 'cited')]),
                 terms=[('D:/SIDE-kernel', 'b1407b2', 'Kernel/Integration.lean', 201, 202), ('D:/SIDE-kernel', 'b1407b2', 'Kernel/Integration.lean', 210, 212)],
                 verdict='stands', reason='EA :540 names `Integration.lean` as “the assembled conditional” and :542 its pin; the statement is the '
                 'conditional the claim names, as at R089'),
    'R074': dict(paper=('phase2/physics/YANG_MILLS_MONOGRAPH.md', 'e7b444e', [(405, 405, 'cited')]),
                 terms=[('D:/SIDE-effects', 'c66f3c5', 'SIDEEffects/Structural.lean', 43, 47), ('D:/SIDE-effects', 'c66f3c5', 'SIDEEffects/Structural.lean', 49, 49),
                        ('D:/SIDE-effects', 'c66f3c5', 'SIDEEffects/Structural.lean', 56, 56), ('D:/SIDE-effects', 'a27415d', 'SIDEEffects/Structural.lean', 73, 74)],
                 verdict='stands', reason='at c66f3c5 `gapped` is defined True on each of four sectors and `mass_gap : ¬Massless` follows from '
                 '`all_gapped`, the placeholder YM cites; at a27415d the file records it retired (:73-:74) -- the claim, a statement of what '
                 'YM cites, is carried by the two pins; the row’s cell placed the retirement line under c66f3c5, a fact the next version '
                 'corrects (F01)'),
    'R118': dict(paper=('phase2/physics/MATTER_AS_ARITHMETIC.md', 'e7b444e', [(180, 182, 'omitted by the packet: the annotation’s head'),
                                                                             (183, 183, 'cited'), (184, 186, 'omitted by the packet: the annotation’s tail')]),
                 terms=[('D:/SIDE-cosmo', 'c5cba30', 'SIDECosmo/FormationPhaseSpace.lean', 22, 22), ('D:/SIDE-cosmo', 'c5cba30', 'SIDECosmo/FormationPhaseSpace.lean', 53, 53),
                        ('D:/SIDE-cosmo', 'c5cba30', 'SIDECosmo/FormationPhaseSpace.lean', 59, 60)],
                 verdict='stands', reason='xi is defined as the tuple ⟨2, 3, 2, 0⟩ and `xi_total` and `xi_visible` decide 81 and 4 from it -- '
                 'counts derived from a tuple carried by definition, the annotation’s reading at :180-:186, of which the packet held one line'),
}

# ### the 46 others: (verdict, the omitted cited line the seat names, the reason). 'moves' takes the reader's grade; 'stands' keeps the
# ### seat's on the omitted line; 'unchanged' where the seat's grade is the lower one (the grading rule's order, reading R-7).
OTHERS = {
    'R012': ('moves', 'TF :363-:369, :391', 'the omitted lines mark steps one to four done, a line each, and call the Mechanism Theorem the '
             'load-bearing axiom; they state the architecture and read no pattern across results'),
    'R042': ('moves', 'TR :67', 'TR :67 names Serre (1977) for the free product of the cyclic groups of orders 2 and 3, not for the fixed points '
             'the claim states; no theorem of the literature is named for them'),
    'R044': ('stands', 'TF :239', 'TF :239 names Størmer’s theorem (1897) for the list the cited line gives'),
    'R050': ('stands', 'TS :100', 'TS :100 is the proposition’s argument: −σ log n = −(1−σ) log n gives σ = 1/2'),
    'R058': ('moves', '', 'no line beyond :34 is cited; the line argues the exponent through Poisson summation and the Gaussian transform and '
             'names no theorem of the literature for it'),
    'R073': ('stands', 'TS :549-:554', 'TS :550 is the formula and :554 its argument by Cauchy–Riemann'),
    'R094': ('moves', '', 'no line is cited for the backing; the line states a change of variable'),
    'R023': ('stands', 'IS :157', 'IS :157 names Størmer (1897) and Lehmer (1964) for the list'),
    'R032': ('stands', 'IS :37', 'IS :37 is the proposition’s argument'),
    'R037': ('stands', 'IS :307-:323', 'IS :307-:323 is the theorem’s argument through the three independent Legendre symbols'),
    'R041': ('stands', 'IS :87-:89', 'IS :87 argues the emptiness and :89 the turn to the centred coordinate'),
    'R062': ('stands', 'SE :81-:86', 'SE :81-:86 are the four steps the abstract names'),
    'R088': ('unchanged', '', 'the seat’s argument-supported is below the reader’s computationally-verified in the grading rule’s order'),
    'R095': ('stands', 'CG :116-:121', 'the table the cited line introduces aligns McLuhan’s temperature with κ, the network and Bloom’s level '
             'across four media: a pattern read across results'),
    'R104': ('unchanged', '', 'the seat’s argument-supported is below the reader’s theorem-supported'),
    'R105': ('unchanged', '', 'the seat’s statement-grade is the lowest grade'),
    'R008': ('unchanged', '', 'the seat’s statement-grade is the lowest grade'),
    'R043': ('unchanged', '', 'the seat’s statement-grade is the lowest grade'),
    'R048': ('moves', '', 'no line beyond :75 is cited; the paper states the coefficients and the arithmetic is the claim bank’s'),
    'R053': ('moves', '', 'no line beyond :383 is cited; the paper states the sum, the arithmetic and the twinning not reported as computed'),
    'R055': ('unchanged', '', 'the seat’s statement-grade is the lowest grade'),
    'R067': ('stands', 'CS :155-:156', 'CS :156 cites the models of Corazza and colleagues (2025) reproducing both plateaux, the claim’s second half'),
    'R070': ('unchanged', '', 'the seat’s statement-grade is the lowest grade'),
    'R071': ('stands', 'YM :252-:261', 'YM :255 reports the lattice string tension near 0.19 GeV² and :261 the deconfinement temperature near 155 MeV'),
    'R077': ('moves', '', 'no line beyond :157 is cited; the paper states the formula, the recomputation is the claim bank’s'),
    'R099': ('unchanged', '', 'the seat’s statement-grade is the lowest grade'),
    'R102': ('unchanged', '', 'the seat’s argument-supported is below the reader’s theorem-supported'),
    'R006': ('stands', 'BT :202-:206', 'BT :202-:206 trace each of the four terms to its class with a gloss: the formula read against the catalogue'),
    'R034': ('unchanged', '', 'the seat’s statement-grade is the lowest grade'),
    'R036': ('unchanged', '', 'the seat’s statement-grade is the lowest grade'),
    'R052': ('unchanged', '', 'the seat’s statement-grade is the lowest grade'),
    'R022': ('moves', '', 'no line beyond :90 is cited; the paper states the figures, the ratio recomputed in the claim bank'),
    'R030': ('moves', '', 'no line beyond :83 is cited; the paper states the arithmetic, the recomputation is the claim bank’s'),
    'R051': ('unchanged', '', 'the seat’s statement-grade is the lowest grade'),
    'R061': ('moves', '', 'no line beyond :145 is cited; the paper states the distances, the recomputation is the claim bank’s'),
    'R076': ('moves', '', 'no line beyond :216 is cited; the paper states the difference, the recomputation is the claim bank’s'),
    'R082': ('moves', '', 'no line beyond :22 is cited; the paper states Planck’s value and the distance, the recomputation is the claim bank’s'),
    'R110': ('moves', 'TH :108-:118', 'TH :108-:118 is the per-domain table of counts, which states the counts; the sum to 14 is the claim '
             'bank’s, and no computation is reported for it'),
    'R001': ('stands', 'IR :127-:135', 'IR :127-:131 assign each structure’s productions a type and :135 draws the exclusion from them: the type '
             'analysis the backing names'),
    'R010': ('moves', '', 'the backing cites :210 alone, the line the packet held; it states the structural-reading status'),
    'R021': ('stands', 'IR :30-:42', 'IR :30-:42 argue that coupling would contradict the independence'),
    'R024': ('stands', 'EA :400-:410', 'EA :401-:410 decompose the exhaustiveness claim into four sub-claims and argue its weakest link'),
    'R056': ('unchanged', '', 'the seat’s synthesis-suggested is below the reader’s theorem-supported'),
    'R068': ('unchanged', '', 'the seat’s argument-supported is below the reader’s theorem-supported'),
    'R103': ('moves', 'EA :132', 'EA :132 marks the step standard and uncontroversial and names no theorem of the literature; the line combines '
             'the functional equation with Schwarz reflection, an argument'),
    'R113': ('stands', 'ME :265', 'ME :265 gives the reason: three of the five paths take the involution as their definition, so the machinery '
             'is shared'),
}

# ### the cells the next versions change: (row id, synthesis key, claim id, old grade, new grade, old backing, new backing)
REGRADES = [
    ('R012', '15E', 'TF-08', 'synthesis-suggested', 'statement-grade', 'its steps marked done at :363-:369, its weight on the Mechanism Theorem (:391)',
     'stated: its steps marked done at :363-:369 and its weight on the Mechanism Theorem (:391), no pattern read across results'),
    ('R042', '15E', 'TR-04', 'theorem-supported', 'statement-grade',
     'the modular group’s fixed points, classical (Serre, named at :67); the identification with σ = 1/2 is the paper’s',
     'stated: Serre is named at :67 for the free product of the cyclic groups of orders 2 and 3, not for the fixed points; the identification '
     'with σ = 1/2 is the paper’s'),
    ('R058', '15E', 'TR-03', 'theorem-supported', 'argument-supported', 'Poisson summation and the Gaussian transform, classical, at :34',
     'argued at :34 through Poisson summation and the Gaussian transform, no theorem of the literature named for it'),
    ('R094', '15E', 'TR-01', 'theorem-supported', 'statement-grade', 'the functional equation, classical',
     'stated at :26, a change of variable, no theorem of the literature named'),
    ('R048', '2D', 'PO-09', 'computationally-verified', 'statement-grade', 'the arithmetic recomputed in the claim bank',
     'stated at :75; the arithmetic recomputed in the claim bank, the paper reporting no computation'),
    ('R053', '2D', 'UF-08', 'computationally-verified', 'statement-grade', 'arithmetic; the twinning a reading',
     'stated at :383; arithmetic the paper does not report computing, the twinning a reading'),
    ('R077', '2D', 'UF-05', 'computationally-verified', 'statement-grade', 'recomputed in the claim bank',
     'stated at :157; recomputed in the claim bank, the paper reporting no computation'),
    ('R022', '2G', 'LC-08', 'computationally-verified', 'statement-grade', 'the ratio recomputed in the claim bank',
     'stated at :90; the ratio recomputed in the claim bank, the paper reporting no computation'),
    ('R030', '2G', 'DM-05', 'computationally-verified', 'statement-grade', 'recomputed in the claim bank',
     'stated at :83; recomputed in the claim bank, the paper reporting no computation'),
    ('R061', '2G', 'FD-10', 'computationally-verified', 'statement-grade', 'recomputed in the claim bank',
     'stated at :145; recomputed in the claim bank, the paper reporting no computation'),
    ('R076', '2G', 'TH-10', 'computationally-verified', 'statement-grade', 'recomputed in the claim bank',
     'stated at :216; recomputed in the claim bank, the paper reporting no computation'),
    ('R082', '2G', 'FD-03', 'computationally-verified', 'statement-grade', 'recomputed in the claim bank (0.126σ)',
     'stated at :22; recomputed in the claim bank (0.126σ), the paper reporting no computation'),
    ('R110', '2G', 'TH-03', 'computationally-verified', 'statement-grade', 'the per-domain counts (:108-:118) sum to 14 (the claim bank)',
     'stated at :20; the per-domain counts (:108-:118) sum to 14 in the claim bank, the paper stating counts and reporting no computation'),
    ('R010', 'P12', 'EA-09', 'argument-supported', 'statement-grade', 'the paper’s own [ESTABLISHED] and its words at :210',
     'stated at :210 with the paper’s own [ESTABLISHED], no argument in the line'),
    ('R103', 'P12', 'EA-05', 'theorem-supported', 'argument-supported', 'the functional equation and the reflection principle, standard (:132)',
     'argued at :130 from the functional equation and Schwarz reflection; :132 marks it standard and names no theorem of the literature'),
]
# ### the fact clause, on a row the act re-read at its pin
FACTS = [
    ('F01', '2D', 'YM-20', 'SIDEEffects/Structural.lean the placeholder recorded as retired (:73)',
     'SIDEEffects/Structural.lean at a27415d (= commit a27415d1aa0c, on the remote main ef4cff7) the placeholder recorded as retired (:73)',
     'the retirement line :73 is the file’s at a27415d, where :73-:74 record the placeholder retired; at c66f3c5 the line :73 is the doc '
     'comment of `sectors_complete`'),
]


def row_cells(line):
    c = line.strip().strip('|').split(' | ')
    return [x.strip() for x in c]


def resolve_rows(texts):
    """### texts: {key: synthesis lines at HEAD}. Every regraded row's grade and backing cells, and every fact's fragment, as the work-list
    ### states them; returns a list of what fails."""
    bad = []
    for rid, key, cid, og, ng, ob, nb in REGRADES:
        hit = [l for l in texts[key] if l.startswith('| %s |' % cid)]
        if len(hit) != 1:
            bad.append((rid, cid, 'rows %d' % len(hit)))
            continue
        c = row_cells(hit[0])
        if len(c) != 6 or c[3] != og or c[4] != ob:
            bad.append((rid, cid, c[3:5]))
    for fid, key, cid, old, new, why in FACTS:
        hit = [l for l in texts[key] if l.startswith('| %s |' % cid)]
        if len(hit) != 1 or hit[0].count(old) != 1:
            bad.append((fid, cid, 'fragment'))
    return bad
