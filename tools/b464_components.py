# -*- coding: utf-8 -*-
"""b464_components.py -- THE EIGHT UNFOLDED, AND THE FORMULA'S PARAMETERS AGAINST THE SIX SITES.

### ### **EVERY RULE IS ON THE LOCKED FACE.** ### **NO ITEM'S GRADE IS A TOOL'S VERDICT:** each is
### the seat's reading, said to be one, with the terminal's statement printed beside it so a later
### reader can disagree without re-doing the search.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
NL = chr(10)
L = []

sys.path.insert(0, T)
from b464_extract import the_eight, search_terminals, statement_of   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


# ### PER ITEM: the subject tokens, the one-line claim, the grade, its reason, and -- where the rule's
# ### tie-break picked a worse hit than the record holds -- the CONTENT-NEAREST named beside it.
ITEMS = [
    (['kernel', 'redundancy', 'necessity', 'lean'],
     'that the kernel`s redundancy to the manuscript proof is itself machine-checked',
     'NOT THE CLAIM',
     'the structure bundles four premises -- `symmetry`, `independence`, `catalogue`, `no_mechanism` '
     '-- and states nothing about redundancy, necessity, or the relation of kernel to manuscript.',
     None, 'the search found nothing nearer: no declared name in the roster carries redundancy or necessity'),
    (['mechanism', 'theorem', 'zfc', 'ids', 'condition'],
     'that the Mechanism Theorem of Chapter 10 is carried in machine-checked forms',
     'INTERFACES',
     'it concludes `kappa P f a0 = 0` FROM the named premise `(h_no_mechanism : forall a, P (f a) = '
     'P (f a0))`; the premise is the no-mechanism hypothesis itself, and the theorem is read at HEAD '
     'in SIDE-interfaces, not at a deposited pin -- weaker, under (R8).',
     None, ''),
    (['witness', 'mellin', 'phi', 'coupling', 'trace', 'spectral'],
     'that the fixed witness Phi is the heat trace of a self-adjoint spectrum, machine-checked',
     'NOT THE CLAIM',
     'it states an equivalence between a zero of `completedRiemannZeta` and a zero of `mellin Phi`, '
     'under `(hs : 1 < s.re)`; it says nothing of a heat trace, nothing of self-adjointness, and '
     'nothing of a spectrum. ### **AND ITS OWN HYPOTHESIS CONFINES IT TO `Re s > 1`**, printed as '
     'the terminal`s own wording and not read further by this act.',
     None, 'the search found nothing nearer: no declared name in the roster carries `heat` or `selfadjoint` with Phi'),
    (['channel', 'decomposition', 'lambda', 'li', 'coeff'],
     'that the channel decomposition lambda = lambda_A + lambda_Z reconstructs a published line exactly',
     'NOT THE CLAIM',
     'it is an inductive type with two constructors, `product_formula` and `distributive_law`; it '
     'enumerates coupling channels and states no decomposition of any lambda.',
     ('SIDE-lv-conservation', 'R4_channelDecomposition'),
     'THE RULE`S TIE-BREAK IS ALPHABETICAL AND CONTENT-BLIND: a second hit at the same score and the '
     'same pin is nearer in content, and it is named and read beside the rule`s own nearest'),
    (['conservation', 'premise', 'tate', 'product', 'dark'],
     'that the s-darkness of the product formula is certified and localized at a single compiled goal state',
     'SHELL',
     'the terminal the rule reaches is `theorem conservation_s_dark : True := trivial` -- a '
     'proposition that is `True`, proved by `trivial`. ### **THE VOCABULARY`S OWN WORD FOR THIS IS '
     '`SHELL`**, and it sits in `legacy/`.',
     ('SIDE-kernel', 's_darkness_from_product'),
     'AND THE SAME TIE-BREAK DEFECT, WITH THE OPPOSITE SIGN: a second hit at the same score and pin is '
     'SUBSTANTIVE, and it is named and read beside the shell'),
    (['path', 'critical', 'line', 'growth', 'negative', 'compiled'],
     'that two paths to the critical line are compiled negatives',
     'NOT THE CLAIM',
     'it states that the imaginary part of `completedRiemannZeta0` at `1/2 + it` vanishes; it is not '
     'a negative, not about growth forms, and not about a per-class-to-combination passage. It also '
     'sits in `legacy/`.',
     None, 'the search found nothing nearer: no declared name carries a compiled negative of a growth form'),
    (['conservation', 'premise', 'register', 'seal'],
     'that the inter-class conservation premise is certified and everything surrounding it is machine-checked',
     'NOT THE CLAIM',
     'it is a `def` introducing a `Prop` -- it STATES the register, and a definition certifies '
     'nothing. ### The sentence`s claim about the SURROUNDINGS is a different claim, and this act '
     'names no terminal for it.',
     None, ''),
    (['seal', 'conservation', 'premise', 'catalogue', 'inert'],
     'that the seal is the proof of RH`s one certified premise and the catalogue surrounding it is machine-checked',
     'NOT THE CLAIM',
     'it is a `def` introducing a `Prop`; it states the hypothesis and certifies nothing. ### Same '
     'shape as the item above, in a different deposited file.',
     None, ''),
]


def component1():
    rec('=' * 110)
    rec('### COMPONENT 1 -- THE EIGHT MACHINE-CHECKED SENTENCES, UNFOLDED.')
    rec('=' * 110)
    eight, idx, per = the_eight()
    rec('  re-derived population : %d ; b462`s banked count : %s ; ### **AGREE : %s**'
        % (len(eight),
           json.loads(read(os.path.join(D, 'b462_census.json')))['machine_checked_no_terminal'],
           len(eight) == json.loads(read(os.path.join(D, 'b462_census.json')))['machine_checked_no_terminal']))
    rec('')
    out, grades = [], {}
    for k, (e, spec) in enumerate(zip(eight, ITEMS), 1):
        toks, claim, grade, reason, alt, note = spec
        hits = search_terminals(toks, idx)
        sc, _pr, kernel, how, full, short = hits[0]
        path, stmt, ref = statement_of(kernel, full)
        rec('-' * 110)
        rec('### ITEM %d -- %s:%d   [%s]' % (k, e['surface'], e['line'], e['bin']))
        rec('-' * 110)
        rec('  QUOTED: %s' % e['text'][:400])
        rec('  CLAIMS AS MACHINE-CHECKED: %s' % claim)
        rec('  NEAREST TERMINAL BY THE RULE : %s  @ %-8s in %s  (%s, score %d of %d hits)'
            % (full, ref, kernel, how, sc, len(hits)))
        rec('    its STATEMENT, read from the source at that ref -- NOT its docstring:')
        for l in (stmt or '(not located)').split(NL)[:8]:
            rec('      | %s' % l[:132])
        rec('  ### ### **GRADE : %s** -- the seat`s reading, and said to be one.' % grade)
        rec('    reason, in the terminal`s own words: %s' % reason)
        if note:
            rec('    ### **%s.**' % note)
        if alt:
            akernel, aname = alt
            apath, astmt, aref = statement_of(akernel, aname)
            rec('    ### THE CONTENT-NEAREST, NAMED BESIDE THE RULE`S OWN NEAREST:')
            rec('      %s @ %s in %s : %s' % (aname, aref, akernel, apath))
            for l in (astmt or '(not located)').split(NL)[:7]:
                rec('      | %s' % l[:132])
        grades[grade] = grades.get(grade, 0) + 1
        out.append(dict(n=k, surface=e['surface'], line=e['line'], bin=e['bin'], text=e['text'],
                        claim=claim, terminal=full, kernel=kernel, ref=ref, how=how, path=path,
                        statement=stmt, grade=grade, reason=reason,
                        alt=(alt[1] if alt else None), note=note))
    rec('')
    rec('  ### ### **THE EIGHT, BY GRADE : %s.**'
        % ' ; '.join('%s %d' % (g, grades[g]) for g in sorted(grades)))
    ntc = [o for o in out if o['grade'] == 'NOT THE CLAIM']
    rec('  ### ### **`NOT THE CLAIM` : %d. ### NONE IS b455`S C2 OR C6** -- those are the record`s'
        % len(ntc))
    rec('  ### description paragraph and the kernel README line; all eight sit in DEPOSITED FILES.')
    rec('  ### ### **SO EACH IS A DEPOSIT-LEVEL MATTER UNDER (R66) THAT `E-2026-09-14-1` DOES NOT COVER:**')
    for o in ntc:
        rec('      %s:%d -- NAMED AND ROUTED, NOT REPAIRED' % (o['surface'], o['line']))
    rec('  ### ### **NO ERRATUM IS DRAFTED IN THIS ACT, NO LIVE SURFACE IS NARROWED, NO WAVE OPENS.**')
    rec('  ### ### **AND WHAT A `NOT THE CLAIM` HERE IS NOT:** it is not a finding that the sentence is')
    rec('  ### false, nor that no terminal could carry it, nor that the deposit is wrong. ### It is a')
    rec('  ### finding that ### **THIS SEARCH, BY THIS RULE, FOUND NO TERMINAL STATING IT.**')
    rec('  ### ### **AND THE RULE HAS A NAMED WEAKNESS, PRINTED RATHER THAN LEFT:** its tie-break is')
    rec('  ### ALPHABETICAL, so among equal-scoring hits at the same pin it picks by name. ### At item 5')
    rec('  ### that reached a `SHELL` while a SUBSTANTIVE terminal sat beside it; at item 4 it reached an')
    rec('  ### inductive while a decomposition theorem sat beside it. ### **BOTH ARE NAMED AND READ.**')
    json.dump(dict(items=out, by_grade=grades, not_the_claim=len(ntc)),
              io.open(os.path.join(D, 'b464_grades.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return out, grades


# ====================================================================================================
PARAMS = [
    ('f', 'the test function',
     'f P C8 c pR* `q  --  reading: f in C_c^infty(R*_+), from (147)`s own preamble', 'PARAMETER'),
    ('the class of f', 'a condition on f',
     'C8 c pR* `q  --  reading: compactly supported and smooth on the positive reals', 'CONDITION OF f'),
    ('the support of f', 'a condition on f',
     'the c in C8 c  --  reading: COMPACT SUPPORT; its width is a datum of that support', 'CONDITION OF f'),
    ('f7', 'derived from f, not independent',
     'f7pxq :=x^-1 fpx^-1q', 'DERIVED FROM f'),
    ('rho', 'the summation variable on the left',
     'the sum on the left hand side is over all complex zeros rho of the Riemann zeta function',
     'PARAMETER'),
    ('v', 'the summation variable on the right',
     'where v runs over all places tR, 2, 3, 5,... u of Q', 'PARAMETER'),
    ('m', 'the summation variable inside W_p',
     'Wppfq = p logpq sum_{m=1}^{infty} ( fppmq + f7ppmq )  --  (149)', 'PARAMETER'),
    ('p', 'the finite places',
     'for v = p  --  the primes, as the finite places of Q', 'PARAMETER'),
    ('the L-function', 'FIXED, not a parameter',
     'all complex zeros rho of the Riemann zeta function  --  ZETA AND NO OTHER', 'FIXED, NOT A PARAMETER'),
]

SITES = [
    ('(i)', 'class', 'A COORDINATE OF ONE',
     'the source names `C8 c pR* `q` as the condition on its named parameter f; the class of the test '
     'function is a condition of a named parameter, which is the order`s own gloss'),
    ('(ii)', 'height', 'OF NO PARAMETER',
     'the left sum runs over ALL complex zeros rho with no height, cutoff or ordinate anywhere in the '
     'statement; the height is the corpus instrument`s truncation of that sum -- `AT.GAM`, the first '
     'ten thousand banked ordinates -- and not a datum of the formula'),
    ('(iii)', 'width', 'A COORDINATE OF ONE',
     'the compact support of f is a condition the source states; its width is a datum of that support'),
    ('(iv)', 'width', 'A COORDINATE OF ONE',
     'the same condition of the same named parameter; (iii) and (iv) share this index, which row U1 '
     'already says of itself'),
    ('(v)', 'representation', 'OF NO PARAMETER',
     'the statement is about the Riemann zeta function and no other; it carries no L-function, no '
     'representation, no conductor and no `pi`. ### The index comes from Lagarias Theorem 6.1, a '
     'DIFFERENT pinned source, and against CC`s (148) it is of no parameter'),
    ('(vi)', 'modulus', 'OF NO PARAMETER',
     'the right sum runs over PLACES and, inside `W_p`, over prime powers `p^m`; a modulus of '
     'congruence is neither, and no datum of f, of rho or of v is a modulus'),
]


def component2():
    rec('')
    rec('=' * 110)
    rec('### COMPONENT 2 -- THE EXPLICIT FORMULA`S PARAMETERS, AT THE SOURCE THE RECORD IMPORTS.')
    rec('=' * 110)
    src = read(os.path.join(D, 'b328_source_text.txt'))
    rec('  SOURCE : Connes-Consani, arXiv:2006.13771v1, pinned sha256 b8e0b54ade8535cf...')
    rec('  THE STATEMENT READ : ### **(148)**, the Riemann-Weil explicit formula, with (147) the Mellin')
    rec('  transform, (149) the prime term and (150) the archimedean distribution.')
    rec('  ### **AND THE RECORD PINS ANOTHER:** Lagarias `math/0404394v4` (b358), for the Li side.')
    rec('  ### **THE CHAIN IMPORTS CC`s (148) FOR `Z = P - PR + A`, AND THAT IS THE ONE READ.**')
    rec('')
    rec('  ### THE STATEMENT AS THE BANKED TEXT LAYER RENDERS IT -- ### **GARBLED, AND SAID TO BE:**')
    i = src.find('Then, with f7pxq')
    for l in src[i:i + 620].split(NL):
        rec('      | %s' % l[:120])
    rec('  ### **LIGATURE SUBSTITUTIONS, NAMED:** `p...q` for parentheses, `ÿ` for a summation sign,')
    rec('  ### `ż` for an integral, `˜f` for f-tilde. ### **THE READING IS STATED BESIDE THE RAW TEXT')
    rec('  ### AND THE RAW TEXT IS NOT SILENTLY CLEANED** -- b305`s caveat, carried.')
    rec('  ### THE READING: ### **sum_rho f~(rho) = int_0^inf f + int_0^inf f7 - sum_v W_v(f)**')
    rec('')
    rec('  ### ### **EVERYTHING THE STATEMENT QUANTIFIES OVER OR TAKES AS DATA, PRINTED BEFORE ANY SITE')
    rec('  ### ### IS PLACED:**')
    rec('  %-20s %-26s %s' % ('name', 'kind', 'the source`s own words'))
    rec('  ' + '-' * 106)
    for name, kind, words, sort in PARAMS:
        rec('  %-20s %-26s %s' % (name, sort, words[:60]))
    rec('')
    rec('-' * 110)
    rec('### THE SIX SITE INDICES AGAINST THAT LIST.')
    rec('-' * 110)
    tally = {}
    for site, index, verdict, why in SITES:
        tally[verdict] = tally.get(verdict, 0) + 1
        rec('  %-6s %-16s ### **%s**' % (site, index, verdict))
        rec('         %s' % why)
    rec('')
    rec('  ### ### **%s.**' % ' ; '.join('%s %d' % (k, tally[k]) for k in sorted(tally)))
    rec('  ### ### **AND THE VERDICT `OF NO PARAMETER` IS SCOPED TO CC`s (148) AND NOTHING WIDER.**')
    rec('  ### A site whose index this statement does not carry may be carried by a different source')
    rec('  ### the record also pins -- Lagarias for the Li side, where the representation IS a parameter.')
    rec('  ### **ONE SOURCE`S SILENCE IS NOT THE RECORD`S.**')
    rec('')
    rec('-' * 110)
    rec('### THE REVERSE: PARAMETERS WITH NO SITE AGAINST THEM.')
    rec('-' * 110)
    # ### **THE FIRST FORM MATCHED SUBSTRINGS AND VISITED TWO PARAMETERS THAT NO SITE TOUCHES:**
    # ### `m` matched inside `modulus` and `p` inside `representation`. ### **A2's OWN SPECIES -- the
    # ### substring where the thing was meant** -- committed in the reverse check of an act that
    # ### carries A2 on its face. ### Both yields printed; the visited set is now built from the
    # ### PLACEMENT ITSELF, which is the only thing that can visit a parameter.
    visited = set()
    for _site, _index, verdict, _why in SITES:
        if verdict == 'A COORDINATE OF ONE':
            visited |= {'f', 'the class of f', 'the support of f'}
        elif verdict == 'A PARAMETER':
            visited.add(_index)
    rec('  ### the visited set, built from the placement and not by substring : %s'
        % (', '.join(sorted(visited)) or 'none'))
    unvisited = []
    for name, kind, words, sort in PARAMS:
        if sort == 'DERIVED FROM f':
            continue
        if name not in visited:
            unvisited.append((name, sort, words))
    for name, sort, words in unvisited:
        rec('  ### **UNVISITED : %-14s** [%s]' % (name, sort))
        rec('      %s' % words[:110])
    rec('  ### ### **UNVISITED PARAMETERS : %d.**' % len(unvisited))
    rec('  ### ### **EACH IS ROUTED TO THE AUTHOR WITH ROW U1`S REOPENING CONDITION BESIDE IT:**')
    rec('  ### *"A SITE WHOSE ENTRY PRODUCES A STATEMENT ABOUT THE OBJECT -- about `xi`, about the')
    rec('  ### Epstein object, or about any zero -- RATHER THAN A STATEMENT ABOUT THE RECORD."*')
    rec('  ### ### **NO SITE IS ENTERED. ### ROW U1 IS FROZEN AT SIX AND IS NOT WRITTEN. ### NO BRIDGE')
    rec('  ### ### IS TYPED BETWEEN ANY PARAMETER AND ANY SITE.**')
    rec('  ### **AND THE ZEROS ARE AMONG THE UNVISITED**, which is worth one sentence and no more: the')
    rec('  ### sum on the left of (148) runs over every complex zero of zeta, and no site index of row')
    rec('  ### U1 is the zeros. ### **THAT IS AN OBSERVATION ABOUT THE ROW, NOT ABOUT THE ZEROS.**')
    rec('=' * 110)
    json.dump(dict(params=[dict(name=n, kind=k, words=w, sort=s) for n, k, w, s in PARAMS],
                   sites=[dict(site=s, index=i, verdict=v, why=w) for s, i, v, w in SITES],
                   tally=tally, unvisited=[u[0] for u in unvisited]),
              io.open(os.path.join(D, 'b464_params.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return tally, unvisited


if __name__ == '__main__':
    out, grades = component1()
    tally, unvisited = component2()
    io.open(os.path.join(D, 'b464_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(by_grade=grades, site_tally=tally, unvisited=len(unvisited)),
              io.open(os.path.join(D, 'b464_placement.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: b464_components.txt, b464_grades.json, b464_params.json, b464_placement.json')
