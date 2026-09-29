# -*- coding: utf-8 -*-
"""b564_scan.py -- THE SCANS OF b564, UNDER (R174): `priorart` (READING (3) (i)-(ii)), `powersum` (READING (4) (V4)),
`generic` (READING (6)(b): the generic modules' ζ-specific constants and their ZeroConfig-taking declarations).
### Every query is a regex printed with its file count and its hit lines. This file reads and writes relay data/b564_* only;
### it deletes nothing.
"""
import io, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
EF = os.path.join('D:' + os.sep, 'SIDE-explicit-formula')
ML = os.path.join(EF, '.lake', 'packages', 'mathlib')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def files(root, sub):
    out = []
    for dp, dn, fn in os.walk(os.path.join(root, sub)):
        for f in fn:
            if f.endswith('.lean'):
                out.append(os.path.join(dp, f))
    return sorted(out)


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')


def search(label, root, sub, queries, cap=60):
    fs = files(root, sub)
    texts = {f: rd(f) for f in fs}
    L = ['### %s -- %d .lean files under %s, case-insensitive' % (label, len(fs), os.path.join(root, sub))]
    res = {}
    for name, rx in queries:
        pat = re.compile(rx, re.I)
        hits = []
        for f, t in texts.items():
            for i, l in enumerate(t.split(NL)):
                if pat.search(l):
                    hits.append((os.path.relpath(f, root).replace(os.sep, '/'), i + 1, l.strip()[:220]))
        nf = len(set(h[0] for h in hits))
        L.append('  query %-34s regex %-60s files %4d  lines %5d' % (name, rx, nf, len(hits)))
        L += ['      %s:%d: %s' % h for h in hits[:cap]]
        if len(hits) > cap:
            L.append('      ... %d more lines, their files: %s' % (len(hits) - cap, sorted(set(h[0] for h in hits[cap:]))))
        res[name] = dict(regex=rx, files=nf, lines=len(hits), hits=hits)
    return L, res


PRIOR = [
    ('Keiper', r'Keiper'),
    ('Bombieri', r'Bombieri'),
    ('Lagarias', r'Lagarias'),
    ('liCoeff', r'liCoeff|li_coeff|LiCoeff'),
    ("Li's criterion", r"Li['’]s criterion"),
    ('Li criterion', r'\bLi criterion'),
    ('Li coefficient', r'\bLi coefficient'),
    ('Li (whole word, case-sensitive read by hand)', r'(?-i:\bLi\b)'),
    ('(1 - 1/ρ)^n : 1 - 1 / ρ', r'1\s*-\s*1\s*/\s*[ρrs]\b\s*\)\s*\^'),
    ('(1 - 1/ρ)^n : 1 - ρ⁻¹', r'1\s*-\s*[ρrs]\s*⁻¹\s*\)\s*\^'),
    ('(1 - 1/ρ)^n : (ρ - 1) / ρ', r'\(\s*[ρrs]\s*-\s*1\s*\)\s*/\s*[ρrs]\b\s*\)\s*\^'),
    ('WIDENED: (1 - 1/x)^ or (1 - x⁻¹)^, any name', r'\(\s*1\s*-\s*(?:1\s*/\s*[^\s()]+|[^\s()]+\s*⁻¹)\s*\)\s*\^'),
]

POWER = [
    ('Turán', r'Tur[aá]n'),
    ('powerSum', r'powerSum|power_sum'),
    ('power sum', r'power[- ]sums?\b'),
    ('sum of powers', r'sums? of (?:the )?(?:n-?th )?powers'),
    ('Dirichlet approximation', r'Dirichlet[’\']?s? approximation|exists_int_int_abs_mul_sub_le|dirichlet_approx'),
    ('Kronecker', r'Kronecker'),
]


def priorart():
    L = ['b564 -- READING (3) (i)-(ii): THE PRIOR-ART SEARCHES IN THE CHECKOUTS, b536`S FORM', '']
    L1, r1 = search('(i) the Mathlib checkout at 51e6992e', ML, 'Mathlib', PRIOR)
    L2, r2 = search('(ii) Zeta23 at v0.7 (the working tree of SIDE-explicit-formula, branch cut at 1e4a007)', EF, 'Zeta23', PRIOR)
    L += L1 + [''] + L2
    io.open(os.path.join(D, 'b564_priorart_grep.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(mathlib=r1, zeta23=r2), io.open(os.path.join(D, 'b564_priorart_grep.json'), 'w', encoding='utf-8', newline=NL),
              ensure_ascii=False, indent=1)
    for l in L:
        if l.startswith(('###', '  query')):
            print(l)


def powersum():
    L = ['b564 -- READING (4) (V4): THE POWER-SUM SEARCH IN THE MATHLIB CHECKOUT AT 51e6992e', '']
    L1, r1 = search('the Mathlib checkout', ML, 'Mathlib', POWER, cap=80)
    L += L1
    io.open(os.path.join(D, 'b564_powersum_grep.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(r1, io.open(os.path.join(D, 'b564_powersum_grep.json'), 'w', encoding='utf-8', newline=NL), ensure_ascii=False, indent=1)
    for l in L:
        if l.startswith(('###', '  query')):
            print(l)


def control():
    """### THE POSITIVE CONTROL: the same queries over the kernel's own tree, which holds LiCoeff and the power (LiWeil.lean);
    ### a query that finds nothing there cannot report an absence anywhere."""
    L = ['b564 -- READING (3): THE POSITIVE CONTROL -- THE PRIOR-ART AND POWER-SUM REGEXES OVER THE KERNEL`S OWN TREE AT v0.7', '']
    L1, r1 = search('CONTROL: SIDEExplicitFormula/ (the programme`s tree)', EF, 'SIDEExplicitFormula', PRIOR, cap=4)
    L += L1
    io.open(os.path.join(D, 'b564_priorart_control.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))


ZCONST = [
    ('riemannZeta (any ζ object by name)', r'\b(?:riemannZeta\w*|completedRiemannZeta\w*|zetaZeroConfig|zetaSeam|ZetaSeam|IsNontrivialZero|zeroMult|zerosIn|Ncount)\b'),
    ('the pole terms: PiX, "pole", h(±i/2)', r'\bPiX\b|\bpole\b|I\s*/\s*2\b|\(1\s*/\s*2\s*:\s*ℂ\)\s*[+-]\s*I|i\s*/\s*2'),
    ('ζ`s Γ bracket: mu, gammaBracket, digamma at 1/4', r'\bmu\b|\bgammaBracket\b|digamma\s*\(\s*1\s*/\s*4'),
    ('log π with no log N', r'Real\.log\s+(?:Real\.)?π|Real\.log\s+Real\.pi|\blog\s+π'),
    ('the prime sum with no character: PX, nuX, Λ n', r'\bPX\b|\bnuX\b|\bΛ\s+n\b|vonMangoldt'),
    ('literatureRHS (ζ`s explicit-formula right-hand side)', r'\bliteratureRHS\b'),
]


def strip_comments(t):
    t = re.sub(r'/-.*?-/', '', t, flags=re.S)
    return NL.join(l.split('--')[0] for l in t.split(NL))


def generic():
    """### READING (6)(b), the scan's second clause: the generic modules' comment-stripped code read for riemannZeta and the
    ### ζ-specific constants the face fixes; every hit line printed for the hand-read."""
    dg = json.loads(io.open(os.path.join(D, 'b564_dag.json'), encoding='utf-8').read())
    L = ['b564 -- READING (6)(b): THE GENERIC MODULES READ FOR riemannZeta AND THE ζ-SPECIFIC CONSTANTS (COMMENTS STRIPPED)',
         '### the modules: the %d the DAG bank classes GENERIC (relay data/b564_dag.json)' % len(dg['generic']), '']
    res = {}
    for m in dg['generic']:
        p = os.path.join(EF, *m.split('.')) + '.lean'
        code = strip_comments(rd(p)).split(NL)
        hits = {}
        for name, rx in ZCONST:
            pat = re.compile(rx)
            hs = [(i + 1, l.strip()[:200]) for i, l in enumerate(code) if pat.search(l)]
            if hs:
                hits[name] = hs
        res[m] = hits
        if hits:
            L.append('### %s -- %d marker(s)' % (m, len(hits)))
            for name, hs in hits.items():
                L.append('    %s : %d line(s)' % (name, len(hs)))
                L += ['        :%d  %s' % h for h in hs[:12]]
                if len(hs) > 12:
                    L.append('        ... %d more' % (len(hs) - 12))
    clean = [m for m in dg['generic'] if not res[m]]
    L += ['', '### modules with NO marker: %d -- %s' % (len(clean), ', '.join(clean))]
    io.open(os.path.join(D, 'b564_generic_scan.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(res, io.open(os.path.join(D, 'b564_generic_scan.json'), 'w', encoding='utf-8', newline=NL), ensure_ascii=False, indent=1)
    print(NL.join(l for l in L if l.startswith(('###', '    '))))


HELD = [
    ('LFunction on the strip by its series', r'LFunction_eq_LSeries|LFunction_eq_tsum|LFunction_eq_sum|LFunction_eq_integral'),
    ('L-series as the summatory integral', r'LSeries_eq_mul_integral'),
    ('convergence off absolute convergence', r'abscissaOfConv\b|LSeries_converges|LSeriesConverges|conditionally'),
    ('bounded partial sums of a character', r'(?:DirichletCharacter|MulChar)\.\w*(?:sum_range|sum_Icc|partial|norm_sum|sum_le|bounded)\w*'),
    ('Dirichlet test for series', r'cauchySeq_series_mul_of_tendsto_zero_of_bounded|Monotone\.cauchySeq_series_mul|Antitone\.cauchySeq_series_mul'),
    ('growth of LFunction in vertical strips', r'LFunction\w*(?:isBigO|IsBigO|bound|Bound|growth)'),
]


def heldsearch():
    """### READING (6)(c): the Mathlib search for the fact the held declaration needs -- the representation of `LFunction χ`
    ### on `0 < re s` by its partial sums, and its ingredients. Each query with its count and every hit line."""
    L = ['b564 -- READING (6)(c): THE MATHLIB SEARCH FOR THE HELD FACT (the checkout at 51e6992e, case-sensitive)', '']
    L1, r1 = search('the Mathlib checkout', ML, 'Mathlib', [(n, '(?-i:' + rx + ')') for n, rx in HELD], cap=40)
    L += L1
    io.open(os.path.join(D, 'b564_held_search.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(r1, io.open(os.path.join(D, 'b564_held_search.json'), 'w', encoding='utf-8', newline=NL), ensure_ascii=False, indent=1)
    print(NL.join(L))


def main(argv):
    cmd = argv[0] if argv else ''
    if cmd == 'heldsearch':
        return heldsearch()
    if cmd == 'generic':
        return generic()
    if cmd == 'control':
        return control()
    if cmd == 'priorart':
        return priorart()
    if cmd == 'powersum':
        return powersum()
    sys.exit('usage: b564_scan.py priorart | powersum | generic')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
