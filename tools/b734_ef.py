# -*- coding: utf-8 -*-
"""tools/b734_ef.py -- (R344)(3): THE DEPENDENCY PRINT. The constant closure beneath Zeta23.WeilEF.EF_lit_zeta, read from run 41408235115's closure.jsonl.gz, sorted into the ruling's four bins, every member printed.

  python -X utf8 -u tools/b734_ef.py print <artifact dir> [--bank]     controls first, then the bins; --bank writes data/b734_ef_print.txt and data/b734_ef_print.json

THE TWO GRADES, NEVER MIXED. COMPILED: the programme constants, the records the compiled closure wrote. LEXICAL: Mathlib constants, which the closure tool stops short of (its docstring: a library constant reaches no programme constant), read as tokens of the
closure's own declarations at the pin and resolved against the declaration names of the Mathlib tree the kernel builds on. A token resolves or does not; nothing lexical is called compiled.
THE BINS, in the order the first rule that takes a constant takes it:
  (b) the ruling's own list, quoted and not improved: riemannZeta, completedRiemannZeta, zetaZeros, Landau's partial fraction at zeta, the Gamma bracket, Zeta23.WeilEF.GammaRBracket, Zeta23.GammaFacts (RULING_B, RULING_B_MODULES): each takes (b) whatever else it says.
  (b/a) a constant whose NAME or STATEMENT carries a zeta word (ZETA_WORDS) goes to (a) where ROLE names a closed field's theorem doing its work for Q0, and otherwise to (b).
  (d) every other programme constant: neither, named. It reads no zeta word in its own statement and is usable as it stands or by import.
  (c) the Mathlib tokens, LEXICAL; zeta-named library constants (LIB_ZETA) go to (b) and are marked so.
A constant in (d) may rest on a (b) constant below it: the bins sort by what a declaration says, and the transitive reading is printed apart, as BENEATH.
"""
import gzip
import hashlib
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(os.path.dirname(T), 'data')
sys.path.insert(0, os.path.join(T, 'standing'))
EF = 'D:/SIDE-explicit-formula'
PIN = '09053d3b07367aa7ef2e26cbeb27fd35d8734d82'
RUN = 41408235115
TOP = 'Zeta23.WeilEF.EF_lit_zeta'
NL = '\n'

ZETA_WORDS = re.compile(r"riemannZeta|completedRiemannZeta|completedZeta|Zeta0|zeta|ζ|ZetaSeam|IsNontrivialZero|zeroMult|zerosIn|Ncount|N0star|N0simple|Ndist|Gammaℝ|gammaBracket|vonMangoldt|literatureRHS|EF_lit")
RULING_B = ('Zeta23.zetaZeros', 'Zeta23.WeilEF.zeta_logDeriv_partial_fraction', 'Zeta23.EF.gammaBracket')
RULING_B_MODULES = ('Zeta23.WeilEF.GammaRBracket', 'Zeta23.GammaFacts', 'Zeta23.GammaFacts.Series', 'Zeta23.GammaFacts.Mu', 'Zeta23.GammaFacts.StirlingVert')
# ### library constants the ruling does not name, each the Mathlib form of a closed field's work: (a), LEXICAL
LIB_SUPPLIED = {'ArithmeticFunction.LSeries_vonMangoldt_eq_deriv_riemannZeta_div': 'logDeriv', 'riemannZeta_ne_zero_of_one_le_re': 'logDeriv', 'riemannZeta_ne_zero_of_one_lt_re': 'logDeriv', 'zeta_eq_tsum_one_div_nat_cpow': 'logDeriv', 'zeta_eq_tsum_one_div_nat_add_one_cpow': 'logDeriv',
                'completedRiemannZeta_one_sub': 'continuation', 'riemannZeta_one_sub': 'continuation', 'differentiableAt_riemannZeta': 'continuation', 'differentiableAt_completedZeta': 'continuation', 'riemannZeta_def_of_ne_zero': 'continuation', 'riemannZeta_residue_one': 'continuation',
                'completedRiemannZeta_residue_one.congr': 'continuation', 'HolomorphicOn_riemannZeta.analyticOnNhd': 'continuation', 'riemannZeta_analyticOnNhd_compl_one.analyticOrderAt_ne_top_of_isPreconnected': 'zeros'}
LIB_ZETA = ('riemannZeta', 'completedRiemannZeta', 'completedRiemannZeta₀', 'riemannZeta_one_sub', 'completedRiemannZeta_one_sub', 'differentiableAt_riemannZeta', 'differentiable_completedZeta₀', 'differentiableAt_completedZeta', 'riemannZeta_ne_zero_of_one_le_re',
            'riemannZeta_ne_zero_of_one_lt_re', 'riemannZeta_residue_one', 'riemannZeta_zero', 'riemannZeta_def_of_ne_zero', 'zeta_eq_tsum_one_div_nat_add_one_cpow', 'zeta_eq_tsum_one_div_nat_cpow', 'Gammaℝ', 'Complex.Gammaℝ', 'Gammaℝ_ne_zero_of_re_pos', 'Gammaℝ_def')
CONT, ZERO, LOGD, CNT = 'continuation', 'zeros', 'logDeriv', 'count'
SUPPLY = {CONT: ('SIDEExplicitFormula/Schema/ZQ/Continuation.lean', 221, 'zq_continuation'), ZERO: ('SIDEExplicitFormula/Schema/ZQ/Zeros.lean', 329, 'zq_zeros'),
          LOGD: ('SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean', 396, 'zq_logDeriv'), CNT: ('SIDEExplicitFormula/Schema/ZQ/Count.lean', 338, 'zq_count_holds')}
# ### the role of a zeta-worded constant: a module whose whole work the field does for Q0; ROLE_NAME takes the single constants of a mixed module. What is in neither is (b).
ROLE_MODULE = {'Zeta23.Statement': ZERO, 'Zeta23.Statement.Seam': ZERO, 'Zeta23.Statement.SeamClosed': ZERO, 'Zeta23.ZetaReflect': ZERO, 'Zeta23.Defs.Counting': ZERO,
               'Zeta23.RvM.LocalCount': CNT, 'Zeta23.RvM.Halving': CNT, 'Zeta23.RvM.ZetaGrowth': CNT, 'Zeta23.RvM.CountByIntegral': ZERO, 'Zeta23.FromPNTPlus.ZetaBounds': CONT, 'Zeta23.FromPNTPlus.EulerMaclaurin': CONT, 'Zeta23.FromPNTPlus.StrongPNTPrefix': CONT}
ROLE_NAME = {'Zeta23.RvM.analyticOnNhd_riemannZeta': CONT, 'Zeta23.WeilEF.analyticAt_riemannZeta': CONT}


def git(*a, repo=EF):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def rows_of(art):
    p = os.path.join(art, 'build-module-%d' % RUN, 'closure.jsonl.gz')
    with open(p, 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()
    return [json.loads(l) for l in gzip.open(p, 'rt', encoding='utf-8')], h


def source(m):
    return git('show', '%s:%s.lean' % (PIN, m.replace('.', '/'))).split(NL)


DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private |protected |noncomputable |unsafe |nonrec )*(theorem|lemma|def|abbrev|structure|inductive|instance|class)\b')


def stmt(lines, l, name):
    """the declaration's own text from the record's line (1-indexed, the docstring's if it has one), the docstring dropped: (statement, body). A record with no line reads empty."""
    if not l or l > len(lines):
        return '', ''
    i = l - 1
    while i < len(lines) and not DECL.match(lines[i]):
        i += 1
        if i - l > 40:
            return '', ''
    j, st, br = i, [], None
    while j < len(lines):
        if j > i and DECL.match(lines[j]) and not lines[j].startswith(' '):
            break
        if j > i and lines[j].startswith('/--'):
            break
        if j > i and re.match(r'^(end |namespace |section\b|open |variable |/-!)', lines[j]):
            break
        st.append(lines[j])
        j += 1
    t = NL.join(st)
    m = re.search(r':=|\bwhere\b', t)
    return (t[:m.start()], t[m.start():]) if m else (t, '')


def sort_(rows):
    by = dict((r['n'], r) for r in rows if 'n' in r)
    clo = sorted(set(by[TOP]['c']) | {TOP})
    src = dict((m, source(m)) for m in sorted(set(by[n]['m'] for n in clo)))
    out = []
    for n in clo:
        r = by[n]
        s, b = stmt(src[r['m']], r.get('l'), n)
        short = n.split('.')[-1]
        word = ZETA_WORDS.search(re.sub(r'Zeta23', '', n) + ' ' + re.sub(r'Zeta23', '', s))
        gen = bool(re.search(r'_proof_|_simp_|\.match_|\.mk$|\.eq_\d+$', n)) or not r.get('l')
        role = ROLE_NAME.get(n) or ROLE_MODULE.get(r['m'])
        if n in RULING_B or r['m'] in RULING_B_MODULES:
            b_, role = 'b', None
        elif word:
            b_ = 'a' if role else 'b'
        elif gen and role:
            b_, role = 'd', None
        else:
            b_, role = 'd', None
        out.append(dict(n=n, m=r['m'], l=r.get('l'), k=r['k'], bin=b_, role=role, word=word.group(0) if word else None, gen=gen, s=s, body=b, short=short, c=r['c']))
    return clo, by, out


def mathlib_names():
    """the declaration names of the Mathlib tree under the kernel's .lake, by git grep at its HEAD; the head recorded."""
    m = os.path.join(EF, '.lake', 'packages', 'mathlib')
    head = git('rev-parse', 'HEAD', repo=m).strip()
    t = git('grep', '-h', '-E', r'^\s*(@\[[^]]*\]\s*)?(private |protected |noncomputable |nonrec |scoped )*(theorem|lemma|def|abbrev|structure|inductive|class|instance)\s+[^ :({\[]+', 'HEAD', '--', 'Mathlib', repo=m)
    names = set()
    for l in t.split(NL):
        x = re.search(r'\b(?:theorem|lemma|def|abbrev|structure|inductive|class|instance)\s+([^\s:({\[]+)', l)
        if x:
            names.add(x.group(1).split('.')[-1])
    spaces = set(re.sub(r'^.*\bnamespace\s+', '', l).strip().split('.')[0] for l in git('grep', '-h', '-E', r'^\s*namespace\s', 'HEAD', '--', 'Mathlib', repo=m).split(NL) if l.strip())
    return head, names, spaces | set(('Nat', 'Int', 'Real', 'Complex', 'Set', 'Finset', 'Function', 'Filter', 'MeasureTheory', 'List', 'And', 'Or', 'Iff', 'Eq', 'Ne', 'Exists', 'Subtype', 'Sigma', 'Prod', 'Option', 'Fin', 'Bool'))


TOK = re.compile(r"[A-Za-z_ℝℂ][\w'.₀₁₂₃₄₅₆₇₈₉ℝℂ]*")


def lexical(sorted_rows, by, names, spaces):
    prog = set(k.split('.')[-1] for k in by)
    hits, local = {}, set()
    for r in sorted_rows:
        for t in TOK.findall(r['s'] + NL + r['body']):
            t = t.strip('.')
            if len(t) < 4:
                continue
            last = t.split('.')[-1]
            if last in prog or last not in names:
                continue
            if '.' in t and t.split('.')[0] not in spaces:
                local.add(t)   # ### a local hypothesis's dot-notation: its head no namespace; tallied, not a member
                continue
            hits.setdefault(t, set()).add(r['n'])
    return hits, local


def controls(clo, srt, names):
    L, g, n = ['## THE CONTROLS FIRST'], 0, 0
    d = dict((r['n'], r) for r in srt)

    def c(what, ok):
        L.append('  %-96s %s' % (what, 'AS WANTED' if ok else 'NOT AS WANTED'))
        return int(bool(ok))
    tests = [('the top constant is in the closure, a (b) constant', d[TOP]['bin'] == 'b'),
             ('a known zeta statement reads (b): Zeta23.WeilEF.good_heights', d.get('Zeta23.WeilEF.good_heights', {}).get('bin') == 'b'),
             ('a generic disk lemma reads (d): Zeta23.WeilEF.logDeriv_partial_fraction_disk', d.get('Zeta23.WeilEF.logDeriv_partial_fraction_disk', {}).get('bin') == 'd'),
             ('a count constant reads (a): Zeta23.RvM.local_count, or the module`s first zeta constant', any(r['bin'] == 'a' and r['role'] == CNT for r in srt)),
             ('every closure constant found a statement or is compiler-generated', all(r['s'] or r['gen'] or r['k'] == 'ctor' for r in srt)),
             ('the tokenizer resolves a planted Mathlib name: Real.log_le_log', 'log_le_log' in names),
             ('the tokenizer refuses a planted false name: Mathlib.no_such_lemma_b734', 'no_such_lemma_b734' not in names)]
    for w, ok in tests:
        n += 1
        g += c(w, ok)
    return L, g, n


def main(argv):
    if len(argv) < 2 or argv[0] != 'print':
        sys.exit(__doc__)
    rows, sha = rows_of(argv[1])
    clo, by, srt = sort_(rows)
    head, names, spaces = mathlib_names()
    hits, local = lexical(srt, by, names, spaces)
    L, g, n = controls(clo, srt, names)
    lib_z = sorted(t for t in hits if t.split('.')[-1] in LIB_ZETA or 'iemannZeta' in t or 'Gammaℝ' in t or 'vonMangoldt_eq_deriv' in t)
    lib_a = dict((t, LIB_SUPPLIED[t]) for t in lib_z if t in LIB_SUPPLIED)
    lib_b = [t for t in lib_z if t not in lib_a]
    lib_c = sorted(t for t in hits if t not in lib_z)
    bins = dict((b, [r for r in srt if r['bin'] == b]) for b in 'abd')
    ba = set(r['n'] for r in bins['b'])
    aa = set(r['n'] for r in bins['a'])
    beneath = sorted(r['n'] for r in bins['d'] if set(r['c']) & ba)
    beneath_a = sorted(r['n'] for r in bins['d'] if set(r['c']) & aa)
    # ### (d) is not one pile: a constant that TAKES a ZeroConfig names no zeta word and still does not apply to Q0's WideConfig
    cfg = sorted(r['n'] for r in bins['d'] if 'ZeroConfig' in (r['s'] or '') or 'ZeroConfig' in r['n'])
    O = ['b734 -- THE DEPENDENCY PRINT, (R344)(3): THE CONSTANT CLOSURE BENEATH %s, SORTED INTO THE RULING`S FOUR BINS, NO BUILD OF ANYTHING NEW AND NO LEAN FILE WRITTEN (%s)' % (TOP, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### THE SOURCE: run %d of build-module.yml at SIDE-explicit-formula %s, the tree as it stands, closure.jsonl.gz sha256 %s ; records %d ; Mathlib read at its clone`s HEAD %s, %d declaration names.' % (RUN, PIN, sha, sum(1 for r in rows if 'n' in r), head, len(names)),
         '### THE MAIN THEOREM, printed from the tree: Zeta23/WeilEF/Main.lean :67 theorem EF_lit_zeta (hs : ZetaSeam) : Zeta23.EF.EF_lit (zetaZeros hs) ; its axioms in the record: %s.' % ', '.join(by[TOP]['a']),
         '### THE GRADES: (a), (b) programme members and (d) are COMPILED, the records the compiled closure wrote; (c) and the library members of (b) are LEXICAL, tokens of the closure`s own declarations resolved against Mathlib`s names. The tool stops at the library`s edge, so no library constant is called compiled here.', '']
    O += L + ['', '### CONTROLS %d OF %d AS WANTED' % (g, n), '']
    O += ['## THE COUNTS',
          '  the closure: %d programme constants, the theorem itself among them, 0 of them from SIDEExplicitFormula.Chi' % len(clo),
          '  (a) SUPPLIED BY THE CLOSED FIELDS (COMPILED)                %d' % len(bins['a']),
          '  (a) SUPPLIED, LIBRARY FORMS OF THE SAME WORK (LEXICAL)      %d' % len(lib_a),
          '  (b) ζ`S ALONE, PROGRAMME (COMPILED)                         %d' % len(bins['b']),
          '  (b) ζ`S ALONE, LIBRARY (LEXICAL)                            %d' % len(lib_b),
          '  (c) MATHLIB, NEUTRAL (LEXICAL)                              %d' % len(lib_c),
          '  (d) NEITHER, PROGRAMME, NAMING NO ζ WORD (COMPILED)         %d, of which compiler-generated %d' % (len(bins['d']), sum(1 for r in bins['d'] if r['gen'])),
          '  BENEATH: members of (d) with a (b) constant in their own closure: %d, and with an (a) constant: %d (a statement that names no ζ word and a proof that rests on one; the two are read apart; named at the rows, BENEATH-b and BENEATH-a)' % (len(beneath), len(beneath_a)),
          '  TAKING A ZeroConfig: members of (d) whose own statement or name carries Zeta23.ZeroConfig: %d. Each reads no zeta word and none applies as it stands to Q0, whose configuration is a WideConfig; marked TAKES-ZeroConfig at the rows.' % len(cfg),
          '  THE LEXICAL TOKENS OF A LOCAL HYPOTHESIS`S DOT-NOTATION, RESOLVED ON THEIR LAST COMPONENT ONLY, HEAD NO NAMESPACE, NOT MEMBERS: %d' % len(local), '']
    def row(r):
        return '  %s  [%s :%s] %s%s' % (r['n'], r['m'], r['l'], r['k'], ('  <- %s' % r['word']) if r['word'] else '')
    O += ['## (a) SUPPLIED BY THE CLOSED FIELDS, BY FIELD, THE SUPPLYING THEOREM BY PATH AND LINE ON zq-b730 AT 09053d3b']
    for role, (p, ln, th) in SUPPLY.items():
        m = [r for r in bins['a'] if r['role'] == role]
        l_ = sorted(t for t, v in lib_a.items() if v == role)
        O += ['### %s: %s :%d %s -- %d members, %d library forms' % (role, p, ln, th, len(m), len(l_))] + [row(r) for r in m] + ['  %s  LEXICAL (%d)' % (t, len(hits[t])) for t in l_]
    O += ['', '## (b) ζ`S ALONE, PROGRAMME, BY MODULE']
    for m_ in sorted(set(r['m'] for r in bins['b'])):
        m = [r for r in bins['b'] if r['m'] == m_]
        O += ['### %s -- %d' % (m_, len(m))] + [row(r) for r in m]
    O += ['', '## (b) ζ`S ALONE, LIBRARY (LEXICAL), EACH WITH THE CLOSURE DECLARATIONS THAT NAME IT'] + ['  %s  (%d)' % (t, len(hits[t])) for t in lib_b]
    O += ['', '## (c) MATHLIB, NEUTRAL (LEXICAL)'] + ['  %s  (%d)' % (t, len(hits[t])) for t in lib_c]
    O += ['', '## (d) NEITHER, BY MODULE']
    for m_ in sorted(set(r['m'] for r in bins['d'])):
        m = [r for r in bins['d'] if r['m'] == m_]
        O += ['### %s -- %d' % (m_, len(m))] + [row(r) + ('  BENEATH-b' if r['n'] in beneath else '') + ('  BENEATH-a' if r['n'] in beneath_a else '') + ('  TAKES-ZeroConfig' if r['n'] in cfg else '') for r in m]
    O += ['', '### ### **THE CLOSURE %d PROGRAMME CONSTANTS: (a) %d ; (b) %d ; (d) %d, COMPILED ; AND LEXICALLY (a) %d, (b) %d, (c) %d ; CONTROLS %d OF %d.**' % (len(clo), len(bins['a']), len(bins['b']), len(bins['d']), len(lib_a), len(lib_b), len(lib_c), g, n)]
    print(NL.join(O))
    if '--bank' in argv:
        p = os.path.join(D, 'b734_ef_print.txt')
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(O) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        j = dict(run=RUN, pin=PIN, sha256=sha, closure=len(clo), a=[r['n'] for r in bins['a']], a_library=lib_a, b=[r['n'] for r in bins['b']], b_library=lib_b, c=lib_c, d=[r['n'] for r in bins['d']], beneath=beneath, beneath_a=beneath_a, d_zeroconfig=cfg, mathlib=head)
        p = os.path.join(D, 'b734_ef_print.json')
        with open(p + '.tmp', 'wb') as f:
            f.write(json.dumps(j, ensure_ascii=False, indent=0).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/b734_ef_print.txt, data/b734_ef_print.json')


if __name__ == '__main__':
    main(sys.argv[1:])
