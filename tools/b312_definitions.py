# -*- coding: utf-8 -*-
"""b312_definitions.py -- THE DECIDING RUNNER: TWO DEFINITIONS, UNFOLDED AND COMPARED.

### ### **IT COMPUTES NOTHING.** ### It EXTRACTS -- from the pinned artefact's RAW page text and
### from the corpus's own emitting files -- the tokens the two definitions differ in, and compares
### them AS STRINGS. ### There is no arithmetic here and there is nothing that could produce a
### value from anybody's numbers.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E16 = os.path.join(ROOT, 'tools', 'e16')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### ### **THE SOURCE'S SIDE.** ### Four extractions, each off the RAW page text, each capturing
# ### the exponent's SIGN GROUP -- which is exactly what the flattener destroys.
# ###   `SRC-THETA`   the scaling action's own definition, its equation (61).
# ###   `SRC-IP`      the source unfolding an inner product of the remainder's own shape.
# ###   `SRC-EPS`     the source unfolding the remainder itself, in its Lemma 5.4 proof.
# ###   `SRC-QEPS`    the operator image's leading factor, its equation (99).
SRC = [
    # ### **NOTE THE ARGUMENT.** ### `SRC-THETA` is the action AT `lambda`; the other three are AT
    # ### `rho^-1`. ### Its minus is the DEFINITION'S and is not the remainder's exponent -- reading
    # ### it as one would invert the whole comparison, which is why it is reported apart.
    ('SRC-THETA', 'the scaling action AT lambda, DEFINED -- eq. (61)',
     r'pϑpλqξqpvq\s*:“\s*λ(´?)1\{2'),
    ('SRC-IP', 'the source unfolding <psi|theta(rho^-1)|xi> AT rho^-1',
     r'xψn\|ϑpρ´1qξny“\s*ρ(´?)1\{2'),
    ('SRC-EPS', 'the REMAINDER unfolded, in the Lemma 5.4 proof',
     r'ϵpρq“\s*ÿ\s*λpnq2\s*1´λpnq2\s*ˆ\s*'
     r'ρ(´?)1\{2'),
    ('SRC-QEPS', 'the operator image\'s leading factor -- eq. (99)',
     r'Cn“ρ(´?)1\{2'),
]

# ### ### **THE CORPUS'S SIDE.** ### Three extractions, each off a committed emitting file, each
# ### capturing the exponent the corpus's own code applies at the same place.
COR = [
    ('COR-EPS', os.path.join(E16, 'qeps_layer.py'), 'eps',
     r'\(\s*r\s*\*\*\s*(-?[0-9.]+)\s*\)', 'the corpus\'s remainder, its own code'),
    ('COR-QEPS', os.path.join(E16, 'qeps_layer.py'), 'Qeps',
     r'\(\s*r\s*\*\*\s*(-?[0-9.]+)\s*\)', 'the corpus\'s operator image, its own code'),
    ('COR-EPSGRID', os.path.join(E16, 'b38_act10.py'), 'per_mode_eps_grids',
     r'\(\s*r\s*\*\*\s*(-?[0-9.]+)\s*\)', 'the remainder AS THE IDENTITY CONSUMES IT'),
    ('COR-TRACE', os.path.join(E16, 'b38_act10.py'), 'trace_modes',
     r'math\.sqrt\(\s*(\w+)\s*\)', 'the TRACE side of the same identity'),
]

# ### ### **THE CORPUS'S DECLARED REASON, QUOTED FROM ITS OWN HEADER.**
COR_DECL = (os.path.join(E16, 'qeps_layer.py'),
            r'theta\(rho\^-1\) zeta_n\(u\) = rho\^\{(-?)1/2\} zeta_n\(rho u\)')


def raw_pages(pdf):
    from pypdf import PdfReader
    return [p.extract_text() or '' for p in PdfReader(pdf).pages]


def find_sign(pages, pattern):
    # ### **RETURNS (page index, captured group, the matched text).** ### The captured group for the
    # ### source's side is the SIGN CHARACTER OR THE EMPTY STRING, never a number.
    rx = re.compile(pattern)
    for i, text in enumerate(pages):
        m = rx.search(text)
        if m:
            return i, m.group(1), ' '.join(m.group(0).split())
    return None, None, None


def def_body(path, name):
    # ### **THE LINES OF ONE TOP-LEVEL `def`, UP TO THE NEXT ONE.** ### Scoped, so a value found in
    # ### a neighbouring function can never be attributed to this one -- the defect b308's site
    # ### classification had, and fixed, by exactly this means.
    lines = io.open(path, encoding='utf-8').read().splitlines()
    start = None
    for i, ln in enumerate(lines):
        if re.match(r'^def\s+%s\s*\(' % re.escape(name), ln):
            start = i
            break
    if start is None:
        return None, []
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if re.match(r'^def\s+\w+\s*\(', lines[j]):
            end = j
            break
    return start + 1, lines[start:end]


def extract_in_def(path, name, pattern):
    first, body = def_body(path, name)
    if first is None:
        return None, None, None
    rx = re.compile(pattern)
    for k, ln in enumerate(body):
        m = rx.search(ln)
        if m:
            return first + k, m.group(1), ln.strip()
    return first, None, None


def self_test():
    # ### ### **THE FIXTURES. ### EVERY ARM MUST BE ABLE TO REPORT THE OTHER ANSWER**, or it is a
    # ### control that cannot fire -- b308's finding, in its own words.
    ok = []
    # (i) the sign extractor SEES a minus when there is one, and its absence when there is not.
    pat = SRC[3][2]
    ok.append(find_sign([u'Cn“ρ´1{2'], pat)[1] == u'´')
    ok.append(find_sign([u'Cn“ρ1{2'], pat)[1] == u'')
    ok.append(find_sign([u'nothing here at all'], pat)[0] is None)
    # (ii) the def-scoped extractor does NOT reach into a neighbouring function.
    tmp = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_b312_fixture.py')
    io.open(tmp, 'w', encoding='utf-8', newline='\n').write(
        u'def alpha(r):\n    return (r ** -3.25) * 1\n\n\ndef beta(r):\n'
        u'    return (r ** 7.75) * 1\n')
    try:
        pat2 = r'\(\s*r\s*\*\*\s*(-?[0-9.]+)\s*\)'
        ok.append(extract_in_def(tmp, 'alpha', pat2)[1] == '-3.25')
        ok.append(extract_in_def(tmp, 'beta', pat2)[1] == '7.75')
        ok.append(extract_in_def(tmp, 'gamma', pat2)[1] is None)
    finally:
        os.remove(tmp)
    return all(ok), ok


def main(argv):
    if not argv:
        print('usage: python b312_definitions.py <path-to-pdf>')
        return 2
    pdf = argv[0]
    print('=' * 100)
    print('b312_definitions.py -- THE TWO DEFINITIONS, UNFOLDED AND COMPARED AS STRINGS.')
    print('=' * 100)
    good, arms = self_test()
    print('  ### THE EXTRACTORS\' OWN FIXTURES, RUN BEFORE THEY ARE TRUSTED : %s  %s'
          % (arms, 'PASS' if good else '### FAIL ###'))
    print('  ### **THE FIRST TWO ARMS ARE THE ONES THAT MATTER: THE EXTRACTOR CAN REPORT EITHER')
    print('  ### SIGN.** ### An arm that could only ever report the answer this act expects would')
    print('  ### be a control that cannot fire, which b308 named and refused.')
    if not good:
        return 2

    pages = raw_pages(pdf)
    print()
    print('  ### THE SOURCE, READ OFF THE RAW PAGE TEXT -- NOT FLATTENED, SINCE THE')
    print('  ### FLATTENER CANNOT SEE A SIGN:')
    src = {}
    for key, what, pat in SRC:
        pg, sign, txt = find_sign(pages, pat)
        src[key] = sign
        shown = ('MINUS' if sign else 'NO MINUS') if sign is not None else '### NOT FOUND'
        print('    %-10s page %-4s %-10s  %-52s' % (key, pg if pg is not None else '--', shown,
                                                    what))
        if txt:
            print('               %s' % txt)

    print()
    print('  ### THE CORPUS, READ OFF ITS OWN COMMITTED EMITTING FILES:')
    cor = {}
    for key, path, fn, pat, what in COR:
        ln, val, txt = extract_in_def(path, fn, pat)
        cor[key] = val
        print('    %-12s %-16s %-20s line %-5s value %-8s %s'
              % (key, os.path.basename(path), fn, ln, val, what))
        if txt:
            print('                 %s' % txt)

    dpath, dpat = COR_DECL
    dm = re.search(dpat, io.open(dpath, encoding='utf-8').read())
    print()
    print('  ### THE CORPUS\'S DECLARED REASON, QUOTED FROM ITS OWN HEADER:')
    print('    %s' % (dm.group(0) if dm else '### NOT FOUND'))
    print('    sign in the declaration : %s'
          % ('MINUS' if (dm and dm.group(1)) else 'NO MINUS' if dm else '--'))

    print()
    print('  ' + '-' * 96)
    print('  ### ### **THE COMPARISON.**')
    print('  ' + '-' * 96)
    print('    ### THE DEFINITION, AT ITS OWN ARGUMENT `lambda`, REPORTED APART SO IT CANNOT BE')
    print('    ### MISREAD AS THE REMAINDER\'S EXPONENT : the action carries a minus = %s,'
          % bool(src.get('SRC-THETA')))
    print('    ### WHICH AT ARGUMENT `rho^-1` IS WHAT PUTS A PLUS ON THE REMAINDER.')
    print('    the source, unfolding an inner product AT rho^-1 : sign = %s'
          % ('MINUS' if src.get('SRC-IP') else 'NO MINUS'))
    print('    the source\'s remainder      exponent sign : %s'
          % ('MINUS' if src.get('SRC-EPS') else 'NO MINUS'))
    print('    the corpus\'s remainder      exponent      : %s' % cor.get('COR-EPS'))
    print('    the corpus\'s remainder AS THE IDENTITY EATS IT : %s' % cor.get('COR-EPSGRID'))
    print('    the source\'s operator image exponent sign : %s'
          % ('MINUS' if src.get('SRC-QEPS') else 'NO MINUS'))
    print('    the corpus\'s operator image exponent      : %s' % cor.get('COR-QEPS'))
    print('    the corpus\'s TRACE side applies           : the square root of %s'
          % cor.get('COR-TRACE'))

    src_minus = bool(src.get('SRC-EPS'))
    cor_minus = str(cor.get('COR-EPS', '')).startswith('-')
    grid_minus = str(cor.get('COR-EPSGRID', '')).startswith('-')
    qsrc_minus = bool(src.get('SRC-QEPS'))
    qcor_minus = str(cor.get('COR-QEPS', '')).startswith('-')

    print()
    print('    ### REMAINDER  : source has a minus = %s ; corpus has a minus = %s  -> %s'
          % (src_minus, cor_minus,
             'AGREE' if src_minus == cor_minus else '### DISAGREE ###'))
    print('    ### THE SAME, IN THE FILE THE IDENTITY IS ASSEMBLED IN : corpus minus = %s -> %s'
          % (grid_minus, 'AGREE' if src_minus == grid_minus else '### DISAGREE ###'))
    print('    ### OPERATOR IMAGE : source minus = %s ; corpus minus = %s  -> %s'
          % (qsrc_minus, qcor_minus,
             'AGREE' if qsrc_minus == qcor_minus else '### DISAGREE ###'))
    print('    ### THE CORPUS AGAINST ITSELF : its remainder and its operator image carry')
    print('    ### opposite exponents = %s' % (cor_minus != qcor_minus))
    print('    ### THE CORPUS AGAINST ITSELF, INSIDE ONE FILE : the identity\'s remainder side and')
    print('    ### its trace side carry opposite exponents = %s'
          % (grid_minus and cor.get('COR-TRACE') is not None))
    print('=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
