# -*- coding: utf-8 -*-
"""test_e0_rule.py -- THE TEST OF tools/e0_rule.py's CLASS-MEMBERSHIP CLAUSE, (R180)(2)(f), written at b570.

### Both polarities on headers, and the rule's own seven-case self-test:
###   (1) the rule's self_test (b568's seven headers) still passes;
###   (2) b569's two χ headers, as Lean's source states them at v0.11 (read here from the kernel), read DERIVES;
###   (3) a class predicate on a variable the conclusion mentions is a domain condition (synthetic);
###   (4) a class predicate on a variable the conclusion does NOT mention reads as a premise (INTERFACES) -- the ruling's
###       named negative case;
###   (5) a named Prop premise beside a class binder still reads INTERFACES;
###   (6) `conclusion` reads past ( ), { }, [ ] binder groups to the ':'.
### b624, (R234)(2) and the author's two answers before b624's seal -- the statement's binders alone, `∉`, ENCODES-CONCLUSION:
###   (7) finsetSum_productLemma at v0.21, its header read by the page generator's own reader, reads DERIVES (its induction
###       hypothesis lives in the proof);
###   (8) finsetSum_insert, the step lemma, at v0.21 reads DERIVES on its non-membership binder `h : a ∉ s`;
###   (9) power_contDiff (PowerWindow.lean) at v0.21, proved by match arms with no `:=`, reads its statement's binders alone;
###   (10) a planted module, one named premise in its statement and an induction in its proof, reads INTERFACES on that
###       premise alone;
###   (11) a planted shell, the conclusion an alpha-variant binder, reads ENCODES-CONCLUSION;
###   (12) beside it a merely similar Prop as a binder does not read ENCODES-CONCLUSION.
### The planted modules are written by this test into the directory its first argument names (a fresh temporary directory
### when none is given), their absolute paths printed; they are read as text and never built.
### Usage: python tools/test_e0_rule.py [planted-directory]
"""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import e0_rule as E0   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KER = 'D:/SIDE-explicit-formula'
V011 = '19b7d1e48a40ca22618722306194404423dca224'


def header(rel, short):
    src = subprocess.run(['git', '-C', KER, 'show', '%s:%s' % (V011, rel)], capture_output=True).stdout.decode('utf-8')
    m = re.search(r'^theorem ' + re.escape(short) + r'(?![\w\'])(.*?):=', src, re.M | re.S)
    return ' '.join(m.group(1).split()) if m else None


V021 = '1d5d4dd'
NL = chr(10)
PLANTED = {
    'PlantedInterface.lean': NL.join([
        '-- b624 planted module (relay tools/test_e0_rule.py): one named premise in the statement, an induction in the proof.',
        'namespace Planted', '',
        'def NamedPremise (n : Nat) : Prop := n = n', '',
        'theorem sum_le_of_premise (hP : NamedPremise 0) (s : List Nat) : s.length ≤ s.length + 1 := by',
        '  induction s with',
        '  | nil => simp',
        '  | cons a t ih => simp', '',
        'end Planted', '']),
    'PlantedShell.lean': NL.join([
        '-- b624 planted module (relay tools/test_e0_rule.py): the conclusion as a binder, and a merely similar Prop beside it.',
        'namespace PlantedShell', '',
        'theorem shell_planted (n : Nat) (h : ∀ k : Nat, k + n = n + k) : ∀ m : Nat, m + n = n + m := h', '',
        'theorem similar_planted (n : Nat) (h : ∀ k : Nat, k + n = k + n) : ∀ m : Nat, m + n = n + m := fun m => Nat.add_comm m n', '',
        'end PlantedShell', '']),
}


def kernel_header(rel, short, CP):
    """### the declaration's header at v0.21 as the page generator reads it (chain_page.source_header)."""
    src = subprocess.run(['git', '-C', KER, 'show', '%s:%s' % (V021, rel)], capture_output=True).stdout.decode('utf-8').replace(chr(13), '')
    ls = [i + 1 for i, l in enumerate(src.split(NL)) if re.match(r'^(theorem|lemma) ' + re.escape(short) + r'(?![\w\'])', l)]
    return CP.source_header(src, short, ls[0]) if ls else None


def planted_grade(path, short, CP):
    src = open(path, encoding='utf-8').read()
    ls = [i + 1 for i, l in enumerate(src.split(NL)) if re.match(r'^theorem ' + re.escape(short) + r'(?![\w\'])', l)]
    h = CP.source_header(src, short, ls[0]) if ls else None
    return E0.grade(h or '', 'theorem')[:2] if h else ('UNREAD', '')


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-104s %s' % (label, 'PASS' if cond else '### FAIL'))

    want('(1) the rule`s own self-test (b568`s seven headers and b624`s four)', E0.self_test())
    for rel, short in (('SIDEExplicitFormula/Chi/LocalCount.lean', 'LFunction_zeros_finite_of_isCompact'),
                       ('SIDEExplicitFormula/Chi/ZeroSummability.lean', 'EF_zero_sum_summable_chi')):
        h = header(rel, short)
        g = E0.grade(h or '', 'theorem')
        want('(2) %s at v0.11 reads DERIVES (read %s; %s)' % (short, g[0], g[1][:60]), h is not None and g[0] == 'DERIVES')
    g3 = E0.grade('{k : ℝ → ℂ} (hk : ContDiff ℝ 2 k) (hkc : HasCompactSupport k) : Summable (fun n => k n)', 'theorem')
    want('(3) a class binder on a variable the conclusion mentions: DERIVES (read %s)' % g3[0], g3[0] == 'DERIVES')
    g4 = E0.grade('{f k : ℝ → ℂ} (hf : ContDiff ℝ 2 f) : Summable (fun n => k n)', 'theorem')
    want('(4) a class binder on a variable the conclusion does NOT mention: INTERFACES (read %s)' % g4[0], g4[0] == 'INTERFACES')
    g5 = E0.grade('{k : ℝ → ℂ} (hk : ContDiff ℝ 2 k) (hX : LiLimitExchange n) : P k', 'theorem')
    want('(5) a named premise beside a class binder: INTERFACES (read %s)' % g5[0], g5[0] == 'INTERFACES')
    c6 = E0.conclusion('{N : ℕ} [NeZero N] (h1 : χ ≠ 1) {K : Set ℂ} (hK : IsCompact K) : (K ∩ s).Finite')
    want('(6) conclusion reads past the binder groups (read %r)' % c6, c6.strip() == '(K ∩ s).Finite')
    import chain_page as CP
    for i, (rel, short, wantg, wantb) in enumerate((('SIDEExplicitFormula/Schema/Family.lean', 'finsetSum_productLemma', 'DERIVES', []),
                                                     ('SIDEExplicitFormula/Schema/Family.lean', 'finsetSum_insert', 'DERIVES', ['h']),
                                                     ('SIDEExplicitFormula/PowerWindow.lean', 'power_contDiff', 'INTERFACES', ['hg', 'hs'])), 7):
        h = kernel_header(rel, short, CP)
        g = E0.grade(h or '', 'theorem')
        want('(%d) %s at v0.21 reads %s on binders %s (read %s; binders %s)' % (i, short, wantg, wantb, g[0], [b for b, _t in g[2]]),
             h is not None and g[0] == wantg and [b for b, _t in g[2]] == wantb)
    pdir = sys.argv[1] if len(sys.argv) > 1 else tempfile.mkdtemp()
    os.makedirs(pdir, exist_ok=True)
    for fn, text in PLANTED.items():
        p = os.path.abspath(os.path.join(pdir, fn))
        open(p, 'w', encoding='utf-8', newline=NL).write(text)
        print('  planted: %s (%d bytes)' % (p, len(text.encode('utf-8'))))
    gi = planted_grade(os.path.join(pdir, 'PlantedInterface.lean'), 'sum_le_of_premise', CP)
    want('(10) the planted interface, an induction in its proof, reads INTERFACES on its one premise (read %s; %s)' % (gi[0], gi[1]),
         gi[0] == 'INTERFACES' and gi[1] == 'hP : NamedPremise 0')
    gs_ = planted_grade(os.path.join(pdir, 'PlantedShell.lean'), 'shell_planted', CP)
    want('(11) the planted shell, the conclusion an alpha-variant binder, reads ENCODES-CONCLUSION (read %s; %s)' % (gs_[0], gs_[1][:60]),
         gs_[0] == 'ENCODES-CONCLUSION')
    gn = planted_grade(os.path.join(pdir, 'PlantedShell.lean'), 'similar_planted', CP)
    want('(12) a merely similar Prop as a binder does not read ENCODES-CONCLUSION (read %s)' % gn[0], gn[0] != 'ENCODES-CONCLUSION')
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
