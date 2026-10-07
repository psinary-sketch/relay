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
### b625, (R235)(2) -- the domain-condition criterion, one case per clause, each with both polarities:
###   (13) clause (i): an instance binder whose class is not Fact is a domain condition, a Fact instance a premise;
###   (14) clause (ii): non-emptiness and finiteness conditions on a set the statement names are domain conditions, a named
###       premise beside them still reads INTERFACES;
###   (15) clause (iii): continuity and the support inclusion restricting the function the statement quantifies are domain
###       conditions; at v0.21 B321.paperFT_polyOp reads DERIVES on its support binder; a Prop about a fixed object behind a
###       bounded quantifier's range (register3_of_one_lt_re`s `∀ C ∈ sevenClasses, C Phi`) is a premise.
###   (9) power_contDiff now reads DERIVES on hg and hs -- its support binder a domain condition under clause (iii).
### b626, (R236)(2) and the author's answer before b626's seal -- the seam antecedent and the data binder:
###   (16) h2_sign_imp_rh_of_seam at v0.21 reads INTERFACES on the seam rh_strip_imp_rh its arrow carries;
###   (17) paperFT_growth and paperFT_growth_at at v0.21 read DERIVES, their data binder h : ℝ → ℂ not entering;
###   (18) a planted P → Q with P a domain condition reads DERIVES, and a plain implication between open statements keeps DERIVES,
###       where a seam antecedent reads INTERFACES;
###   (19) a planted theorem whose data binder is named h reads its Prop binders alone.
### b633, (R243)(2) and the author's two answers before b633's seal -- the two named restrictions and PREDICATE-UNLISTED:
###   (19) re-pointed: its planted NamedPremise on the quantified h is a predicate the rule neither lists nor has met, and reads
###       PREDICATE-UNLISTED (the case's expectation was the old reading itself; listed for the author's strike);
###   (20) Alt2 restricting the quantified c reads DERIVES;
###   (21) Alternates restricting the quantified s reads DERIVES;
###   (22) a planted unlisted predicate on a quantified variable reads PREDICATE-UNLISTED, the same name on a fixed object still
###       INTERFACES, and a met name (LiLimitExchange) on a quantified variable still INTERFACES.
### b635, (R245)(2) -- the textual rule's three repairs, a case each:
###   (23) a conclusion written as a type_of% term reads DEFERRED (the elaborated type is the statement), a plain conclusion beside it not;
###   (24) a hypothesis binder nested two parentheses deep is read (ZerosBound's hfAnalytic form, a premise on AnalyticOnNhd), and one
###       nested one deep still is;
###   (25) a class-membership binder under its qualified name with its default measure reads as a domain condition
###       (MeasureTheory.Integrable h MeasureTheory.volume), as the bare name does.
### b637, (R247)(3)-(4) -- the binder grammar, names removed from the reading:
###   (26) the rule's class table equals the classification banked before the rule was rewritten (relay data/b637_binder_classes.json);
###   (27) the planted module b637 banked, rebuilt here from the bank's declarations, has the bank's sha256;
###   (28)-(53) one case per class: the planted declaration's binder reaches the class the bank fixed, and the declaration reads the grade
###        the bank fixed, before the rule read it;
###   (54) the five-name test: one hypothesis planted under the names h, H, hyp, x and ξ reads one outcome;
###   (55) the no-class control: a binder whose type is a bare name no lexicon lists reaches no class and raises, printed as a bug, no grade.
### Each new case is guarded: a rule without the grammar fails the case, it does not stop the test.
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


CLASSES_BANK = os.path.join(ROOT, 'data', 'b637_binder_classes.json')


def planted_module(J):
    """### b637's planted module, rebuilt from the bank's declarations in the form the act's record tool wrote it."""
    body = ['-- b637 planted module (relay tools/b637_record.py classes, (R247)(4)(i)): one declaration per binder class, the five-name test and',
            '-- the no-class control. Read by the rule as text, never built. Each declaration`s expected class and grade is fixed in relay',
            '-- data/b637_binder_classes.json before the rule reads it.', 'namespace PlantedB637', '']
    for p in J['planted']:
        tag = 'FIVE' if p['test'] == 'five-name' else ('NONE' if p['test'] == 'no-class control' else p['cls'])
        body += ['-- %s : binder %s ; the grade the rule must read: %s' % (tag, p['binder'] or '[inst]', p['grade']), p['text'], '']
    return NL.join(body + ['end PlantedB637', ''])


def _read_planted(src, p):
    """### one planted declaration read by the rule: RETURN (class of the binder under test or None, grade or 'NO CLASS' or 'RAISED x')."""
    m = re.search(r'^theorem ' + re.escape(p['decl']) + r'(?![\w\'])(.*?):=', src, re.M | re.S)
    head = ' '.join(m.group(1).split()) if m else ''
    try:
        bs = E0.binders_of(head)
        b = [x for x in bs if x['name'] == p['binder'] or (p['binder'] == '' and x['kind'] == 'instance')]
        gc = b[0]['cls'] if b else None
    except Exception as e:
        gc = 'RAISED %s' % type(e).__name__
    try:
        gr = E0.grade(head, 'theorem')[0]
    except Exception as e:
        gr = 'NO CLASS' if type(e).__name__ == 'BinderUnclassed' else 'RAISED %s' % type(e).__name__
    return gc, gr


def binder_grammar(want, pdir):
    """### b637's cases (26)-(55), each guarded."""
    import hashlib
    import io
    import json
    try:
        J = json.load(io.open(CLASSES_BANK, encoding='utf-8'))
    except Exception as e:
        want('(26) the classification bank read (%s)' % type(e).__name__, False)
        return
    try:
        table = [list(c) for c in E0.CLASSES]
    except Exception:
        table = None
    want('(26) the rule`s class table equals the bank`s classification (%d classes)' % len(J['classes']),
         table == [[c['id'], c['kind'], c['typing'], c['form'], c['outcome']] for c in J['classes']])
    text = planted_module(J)
    b = text.encode('utf-8')
    p = os.path.abspath(os.path.join(pdir, 'B637Planted.lean'))
    open(p, 'w', encoding='utf-8', newline=NL).write(text)
    print('  planted: %s (%d bytes)' % (p, len(b)))
    want('(27) the planted module rebuilt from the bank has the bank`s sha256 (%s)' % hashlib.sha256(b).hexdigest()[:16],
         hashlib.sha256(b).hexdigest() == J['planted_sha256'])
    n = 28
    for q in [x for x in J['planted'] if x['test'] == 'class']:
        gc, gr = _read_planted(text, q)
        want('(%d) %s: binder %s reaches %s, the declaration reads %s (read %s, %s)' % (n, q['decl'], q['binder'] or '[inst]', q['cls'], q['grade'], gc, gr),
             gc == q['cls'] and gr == q['grade'])
        n += 1
    five = [(q['binder'],) + _read_planted(text, q) for q in J['planted'] if q['test'] == 'five-name']
    want('(%d) the five-name test: %s read %s' % (n, [x[0] for x in five], sorted(set((x[1], x[2]) for x in five))),
         len(five) == 5 and len(set((x[1], x[2]) for x in five)) == 1 and five[0][2] == 'INTERFACES')
    n += 1
    ctl = [q for q in J['planted'] if q['test'] == 'no-class control']
    gc, gr = _read_planted(text, ctl[0]) if ctl else ('?', '?')
    want('(%d) the no-class control: binder %s reaches %s, the declaration reads %s (a bug, no grade)' % (n, ctl[0]['binder'] if ctl else '?', gc, gr),
         bool(ctl) and gc is None and gr == 'NO CLASS')


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-104s %s' % (label, 'PASS' if cond else '### FAIL'))

    want('(1) the rule`s own self-test (b568`s seven headers, b624`s four, b625`s four and b626`s three)', E0.self_test())
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
                                                     ('SIDEExplicitFormula/PowerWindow.lean', 'power_contDiff', 'DERIVES', ['hg', 'hs'])), 7):
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
    a13 = E0.grade('(N : ℕ) [NeZero N] [Fintype ι] (x : ι) : P N x', 'theorem')
    b13 = E0.grade('(p : ℕ) [NeZero p] [hp : Fact p.Prime] : P p', 'theorem')
    want('(13) clause (i): instances not of Fact read %s; a Fact instance reads %s on %s' % (a13[0], b13[0], b13[1]),
         a13[0] == 'DERIVES' and b13[0] == 'INTERFACES' and b13[1] == 'hp : Fact p.Prime')
    a14 = E0.grade('{s : Set ℂ} (hn : s.Nonempty) (hf : s.Finite) : P s', 'theorem')
    b14 = E0.grade('{s : Set ℂ} (hn : s.Nonempty) (hf : s.Finite) (hP : EpsteinPremises s) : P s', 'theorem')
    want('(14) clause (ii): non-emptiness and finiteness read %s; beside a named premise %s on %s' % (a14[0], b14[0], b14[1]),
         a14[0] == 'DERIVES' and b14[0] == 'INTERFACES' and b14[1] == 'hP : EpsteinPremises s')
    a15 = E0.grade('{g : ℝ → ℝ} {L : ℝ} (hc : Continuous g) (hs : Function.support g ⊆ Set.Icc (-L) L) : Q g', 'theorem')
    hk = kernel_header('SIDEExplicitFormula/PowerWindow.lean', 'paperFT_polyOp', CP)
    k15 = E0.grade(hk or '', 'theorem')
    b15 = E0.grade('(h1 : ∀ C ∈ sevenClasses, C Phi) : ∀ s : ℂ, 1 < s.re → R s', 'theorem')
    want('(15) clause (iii): restrictions on the quantified function read %s; paperFT_polyOp at v0.21 %s; behind a range %s' % (
         a15[0], k15[0], b15[0]), a15[0] == 'DERIVES' and hk is not None and k15[0] == 'DERIVES' and b15[0] == 'INTERFACES')
    h16 = kernel_header('SIDEExplicitFormula/PowerLimit.lean', 'h2_sign_imp_rh_of_seam', CP)
    g16 = E0.grade(h16 or '', 'theorem')
    want('(16) h2_sign_imp_rh_of_seam at v0.21 reads INTERFACES on its seam (read %s; %s)' % (g16[0], g16[1]),
         h16 is not None and g16[0] == 'INTERFACES' and g16[1] == '→ : rh_strip_imp_rh')
    g17 = []
    for short in ('paperFT_growth', 'paperFT_growth_at'):
        h17 = kernel_header('SIDEExplicitFormula/GrowthBound.lean', short, CP)
        g = E0.grade(h17 or '', 'theorem')
        g17.append((short, h17 is not None, g[0], [b for b, _t in g[2]]))
    want('(17) paperFT_growth and paperFT_growth_at at v0.21 read DERIVES without h (read %s)' % [(x[0], x[2], x[3]) for x in g17],
         all(x[1] and x[2] == 'DERIVES' and 'h' not in x[3] for x in g17) and len(g17) == 2)
    a18 = E0.grade('(n : ℕ) : 1 ≤ n → Q n', 'theorem')
    b18 = E0.grade(': RiemannHypothesis → h2_sign', 'theorem')
    c18 = E0.grade('(x : ℝ) : rh_strip_imp_rh → Q x', 'theorem')
    want('(18) a domain antecedent reads %s; a plain implication between open statements %s; a seam antecedent %s' % (a18[0], b18[0], c18[0]),
         a18[0] == 'DERIVES' and b18[0] == 'DERIVES' and c18[0] == 'INTERFACES')
    a19 = E0.grade('(h : ℝ → ℝ) (hc : Continuous h) : Q h', 'theorem')
    b19 = E0.grade('(h : ℝ → ℝ) (hP : NamedPremise h) : Q h', 'theorem')
    want('(19) a data binder named h does not enter (read %s, binders %s); beside a named premise %s on %s' % (
         a19[0], [b for b, _t in a19[2]], b19[0], b19[1]),
         a19[0] == 'DERIVES' and [b for b, _t in a19[2]] == ['hc'] and b19[0] == 'PREDICATE-UNLISTED' and b19[1] == 'hP : NamedPremise h')
    g20 = E0.grade('{c : Nat → U4} (h : Alt2 c) : c 4 = c 0', 'theorem')
    want('(20) Alt2 restricting the quantified c reads DERIVES (read %s; %s)' % (g20[0], g20[1]), g20[0] == 'DERIVES')
    g21 = E0.grade('{s : Nat → Int} (h : Alternates s) : s 2 = s 0', 'theorem')
    want('(21) Alternates restricting the quantified s reads DERIVES (read %s; %s)' % (g21[0], g21[1]), g21[0] == 'DERIVES')
    a22 = E0.grade('{f : ℕ → ℕ} (hU : PlantedUnmet f) : Q f', 'theorem')
    b22 = E0.grade('(hU : PlantedUnmet 0) (n : ℕ) : Q n', 'theorem')
    c22 = E0.grade('{n : ℕ} (hX : LiLimitExchange n) : Q n', 'theorem')
    want('(22) a planted unlisted predicate reads %s on %s; on a fixed object %s; a met name %s' % (a22[0], a22[1], b22[0], c22[0]),
         a22[0] == 'PREDICATE-UNLISTED' and a22[1] == 'hU : PlantedUnmet f' and b22[0] == 'INTERFACES' and c22[0] == 'INTERFACES')
    a23 = E0.grade('(χ : DirichletCharacter ℂ N) (hχ : χ.IsPrimitive) : type_of% (@Zeta23.Tail.norm_uvec_le (chiZeroConfig χ hχ))', 'theorem')
    b23 = E0.grade('(n : ℕ) : n + 0 = n', 'theorem')
    want('(23) a type_of%% conclusion reads %s; a plain conclusion %s' % (a23[0], b23[0]), a23[0] == 'DEFERRED' and b23[0] == 'DERIVES')
    a24 = E0.grade('{f : ℂ → ℂ} (hfAnalytic : AnalyticOnNhd ℂ f (Metric.closedBall (0 : ℂ) 1)) : f 0 = 1', 'theorem')
    b24 = E0.grade('{f : ℂ → ℂ} (hfAnalytic : AnalyticOnNhd ℂ f (Metric.closedBall 0 1)) : f 0 = 1', 'theorem')
    want('(24) a binder nested two deep read %s on %s; one deep %s' % (a24[0], a24[1], b24[0]),
         a24[0] == 'INTERFACES' and a24[1].startswith('hfAnalytic : AnalyticOnNhd') and b24[0] == 'INTERFACES')
    a25 = E0.grade('(h : ℝ → ℂ) (L : ℝ) (hi : MeasureTheory.Integrable h MeasureTheory.volume) : Q h', 'theorem')
    b25 = E0.grade('(h : ℝ → ℂ) (L : ℝ) (hi : Integrable h) : Q h', 'theorem')
    want('(25) the qualified class name with its default measure reads %s; the bare name %s' % (a25[0], b25[0]),
         a25[0] == 'DERIVES' and b25[0] == 'DERIVES')
    binder_grammar(want, pdir)
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
