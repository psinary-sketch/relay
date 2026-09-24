# -*- coding: utf-8 -*-
"""b513_table.py -- COMPONENTS 1-3: THE CHAIN'S STATEMENT-READS AND THE CONVERSE PRICED. ### `python tools/b513_table.py`

### Component 1: `rh_imp_h2_sign` printed from its declaration line to its `:=`; the proof's length in lines by READING (4).
### Component 2: the three links, each statement read from the kernel's own text, its model statement beside it, and
### the grade the order confers. ### Component 3: the converse `h2_sign_imp_rh` as the module states it, its docstring,
### and READING (6)'s six needs -- each FOUND by a DECLARATION in the kernel's tree or its Mathlib, or ABSENT with its
### needles and their yields printed. ### **ABSENT IS COMPUTED FROM DECLARATION YIELDS, NEVER TYPED.**
### ### b512's search functions are IMPORTED from `b512_table.py`, not copied.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b512_table as B  # noqa: E402

D = os.path.join(ROOT, 'data')
KER, ML = B.KER, B.ML
MODF = 'SIDEExplicitFormula/RHChain.lean'
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def decl(name):
    """### the declaration from its line to its FIRST `:=`, and whole to the next blank line, from the kernel's own text."""
    for f, t in B.KT.items():
        m = re.search(r'^(?:def|theorem) %s\b' % re.escape(name), t, re.M)
        if m and f.startswith('SIDEExplicitFormula/'):
            j = t.index(':=', m.start())
            k = t.find(NL + NL, m.start())
            return dict(file=f, head=t[m.start():j + 2], whole=t[m.start():k if k >= 0 else len(t)].rstrip(),
                        line=t[:m.start()].count(NL) + 1)
    return None


def docstring_of(name):
    t = B.KT.get(MODF, '')
    m = re.search(r'/--((?:(?!-/).)*?)-/\s*\n(?:def|theorem) %s\b' % re.escape(name), t, re.S)
    return m.group(1).strip() if m else ''


def yields(pattern):
    kh = sorted(f for f, t in B.KT.items() if re.search(pattern, t, re.M))
    r = subprocess.run(['git', '-C', ML, 'grep', '-l', '-E', pattern, '--', 'Mathlib'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    mh = [l for l in r.stdout.split(NL) if l.strip()]
    return dict(needle=pattern, kernel_files=len(kh), mathlib_files=len(mh), kernel=kh[:3], mathlib=mh[:3])


DECL = r'^\s*(@\[[^]]*\]\s*)?(noncomputable\s+)?(private\s+|protected\s+)?(theorem|lemma|def|structure|class|instance|abbrev)\s+\S*'


def need(key, what, decl_needles, text_needles):
    """### FOUND iff some DECLARATION needle yields a file in either tree; the text needles are printed for reading only."""
    d = [yields(DECL + n) for n in decl_needles]
    t = [yields(n) for n in text_needles]
    files = [f for y in d for f in (y['kernel'] + y['mathlib'])]
    return dict(key=key, what=what, found=bool(files), files=files[:3], decl=d, text=t)


def main():
    B1 = decl('rh_imp_h2_sign')
    lines = B1['whole'].split(NL) if B1 else []
    C1 = dict(name='rh_imp_h2_sign', statement=B1['head'] if B1 else None, file=B1['file'] if B1 else None,
              proof_lines=len(lines), first_line=B1['line'] if B1 else None)
    links = [('rh_imp_h2_sign', 'RH -> h2_sign', 'rh_imp_h2'),
             ('h2_sign_imp_cell', 'h2_sign -> the cell form, on an admissible family', 'h2_imp_cell (b512: compiled, no Prop)'),
             ('rh_imp_cell_form', 'RH -> the cell form, on an admissible family', 'rh_imp_cell')]
    C2 = []
    for n, model, prop in links:
        d = decl(n)
        C2.append(dict(name=n, model=model, b512_prop=prop, statement=d['head'] if d else None,
                       file=d['file'] if d else None, grade='DERIVES' if d else 'NOT FOUND',
                       body=(d['whole'][d['whole'].index(':=') + 2:].strip() if d else None)))
    conv = decl('h2_sign_imp_rh')
    NEEDS = [
        need('a', 'a C^2 compactly supported bump', [r'ContDiffBump\b'], []),
        need('b', 'the Weil form h * h~ that puts it in classK', [r'weilTest\b'], []),
        need('c', 'an off-line zero from the negation of RiemannHypothesis', [r'RiemannHypothesis\b'], []),
        need('d', 'a growth bound for paperFT of a compactly supported function at a complex argument (Paley-Wiener type)',
             [r'(PaleyWiener|paleyWiener|paley_wiener)'],
             # ### the matcher WIDENED before the ceiling was banked: a second shape, the growth bound by its other names
             [r'Paley', r'Wiener', r'(exponential type|[Ee]xponentialType)', r'(HasCompactSupport.*fourierIntegral|fourierIntegral.*HasCompactSupport)']),
        need('e', 'a bound on the remaining zeros` terms: the local zero count', [r'zetaZeroConfig_local_count\b'], []),
        need('f', 'THE DECISIVE LEMMA: the off-line pair`s term negative and dominating the rest, so zeroSide k < 0',
             [r'(weil_criterion|weilCriterion|WeilCriterion|weil_positivity|weilPositivity|WeilPositivity|zeroSide_neg|zeroSide_lt|zeroSide_nonpos)'],
             [r'Weil.*criterion', r'zeroSide', r'off-line|offLine|off_line']),
    ]
    res = dict(C1=C1, C2=C2, converse=dict(statement=conv['head'] if conv else None, docstring=docstring_of('h2_sign_imp_rh')),
               needs=NEEDS, absent=[n['key'] for n in NEEDS if not n['found']])
    L = ['=' * 104, 'b513 -- RH -> h2_sign COMPILED: THE STATEMENT-READS, THE CHAIN, THE CONVERSE PRICED.', '=' * 104,
         '### COMPONENT 1 -- THE THEOREM, FROM ITS DECLARATION LINE TO ITS `:=` <%s, line %s>:' % (C1['file'], C1['first_line'])]
    L += ['    ' + x for x in (C1['statement'] or 'NOT FOUND').split(NL)]
    L += ['    ### THE PROOF`S LENGTH, READING (4): %d lines (declaration line to the last line of its tactic block).' % C1['proof_lines'],
          '', '### COMPONENT 2 -- THE THREE-LINK CHAIN, EACH OF ITS MODEL STATEMENT:']
    for r in C2:
        L.append('  %-18s model: %-52s grade by the order: %s' % (r['name'], r['model'], r['grade']))
        L += ['       ' + x for x in (r['statement'] or 'NOT FOUND').split(NL)] + ['       <%s> ; b512`s Prop: %s' % (r['file'], r['b512_prop'])]
    L.append('    ### the composite`s proof term: %s' % C2[2]['body'])
    L += ['', '### COMPONENT 3 -- THE CONVERSE, STATED AND NOT ATTEMPTED:']
    L += ['    ' + x for x in (res['converse']['statement'] or 'NOT FOUND').split(NL)]
    L += ['    docstring: ' + ' '.join(res['converse']['docstring'].split())]
    L += ['    ### WHAT A WITNESS NEEDS (READING (6)); FOUND = a declaration in the kernel`s tree or its Mathlib:']
    for n in NEEDS:
        L.append('  (%s) %-100s %s' % (n['key'], n['what'][:100], ('FOUND ' + ', '.join(n['files'])) if n['found'] else 'ABSENT'))
        for y in n['decl']:
            L.append('        declaration needle %s : kernel %d / Mathlib %d files' % (y['needle'][len(DECL):], y['kernel_files'], y['mathlib_files']))
        for y in n['text']:
            L.append('        text needle        %s : kernel %d / Mathlib %d files %s' % (y['needle'], y['kernel_files'], y['mathlib_files'],
                                                                                         (y['kernel'] + y['mathlib'])[:3]))
    L += ['    ### ABSENT : %s' % (res['absent'] or 'NONE'),
          '    ### A FOUND NAME IS AN INGREDIENT, NOT THE CONSTRUCTION: the converse is priced here, not attempted.',
          '=' * 104]
    io.open(os.path.join(D, 'b513_table.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b513_table.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1, ensure_ascii=False) + NL)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main())
