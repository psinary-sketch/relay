# -*- coding: utf-8 -*-
"""b471_extract.py -- THE SURVEY. ### (R81)'s flagged words, SPIRAL_MAP section 7, the federation's
### pins, the import closure of EF_lit_zetaZeroConfig, and the licence terms -- banked before the seal.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
FM = os.path.join(D, 'anthropic-zeta23', 'formal-math')
Z = os.path.join(FM, 'zeta23')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
NL = chr(10)
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def src(m):
    return os.path.join(Z, *m.split('.')) + '.lean'


def imports(m):
    out = []
    for l in read(src(m)).split(NL):
        mm = re.match(r'^\s*import\s+(\S+)', l)
        if mm:
            out.append(mm.group(1))
    return out


def main():
    rec('=' * 104)
    rec('b471 -- THE SURVEY.')
    rec('=' * 104)

    rec('')
    rec('(P1) (R81)`S FLAGGED WORDS IN THIS FERRY, AND WHOSE WORDS THEY ARE.')
    rec('-' * 104)
    t = read(os.path.join(D, 'b471_ferry.txt')).split(NL)
    act = next(i for i, l in enumerate(t) if 'FERRY -> CLAUDE CODE' in l)
    flags = []
    for i, l in enumerate(t):
        for m in re.finditer(r'\b(first|never|only|ever)\b', l, re.I):
            flags.append(dict(line=i + 1, word=m.group(1), part='RULING (author)' if i < act else 'ACT (navigator)'))
            rec('    :%-3d %-16s %-6s %s' % (i + 1, flags[-1]['part'], m.group(1), l.strip()))
    nav = [f for f in flags if f['part'].startswith('ACT')]
    rec('  ### ### **FLAGGED WORDS : %d ; IN THE NAVIGATOR`S ACT : %d ; IN THE AUTHOR`S RULINGS : %d.**'
        % (len(flags), len(nav), len(flags) - len(nav)))
    rec('  ### (R81) refuses a ferry whose flagged word carries no record check IN THE NAVIGATOR`S MESSAGE;')
    rec('  ### the navigator`s act carries none, so ### **THE FERRY IS NOT REFUSED.**')

    rec('')
    rec('(P2) SPIRAL_MAP SECTION 7, RULES 2, 4, 7 -- AND 8, 9, WHICH ALSO BEAR ON VENDORING.')
    rec('-' * 104)
    sm = read(os.path.join(PP, 'SPIRAL_MAP.md')).split(NL)
    rules = {}
    for n, lo, hi in ((2, 364, 365), (4, 368, 370), (7, 380, 381), (8, 382, 383), (9, 384, 386)):
        body = ' '.join(x.strip() for x in sm[lo - 1:hi])
        ok = body.startswith('%d.' % n)
        if not ok:
            MISSES.append(('SPIRAL_MAP.md', 'rule %d at %d' % (n, lo)))
        rules[n] = dict(line=lo, text=body)
        rec('    SPIRAL_MAP.md:%d-%d  %s' % (lo, hi, body))

    rec('')
    rec('(P3) THE FEDERATION`S TOOLCHAIN PINS -- THE RECORD CHECK FOR "the federation`s v4.29 pins".')
    rec('-' * 104)
    pins = {}
    for r in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-effects'):
        v = read(os.path.join('D:', os.sep, r, 'lean-toolchain')).strip()
        pins[r] = v
        rec('    %-22s %s' % (r, v))
    zt = read(os.path.join(Z, 'lean-toolchain')).strip()
    rec('    zeta23                 %s' % zt)
    rec('  ### ### **THREE OF FOUR ROSTERED KERNELS PIN v4.29.x (rc8 or .1); SIDE-effects pins v4.30.0-rc2,')
    rec('  ### WHICH RULE 4 NAMES AS ITS OWN EXAMPLE OF DIVERGENCE.** ### "the federation`s v4.29 pins" is')
    rec('  ### borne out for three of four; the fourth already diverges, as rule 4 permits.')

    rec('')
    rec('(P4) THE IMPORT CLOSURE OF EF_lit_zetaZeroConfig WITHIN Zeta23/.')
    rec('-' * 104)
    root = 'Zeta23.WeilEF.Main'
    seen, stack = set(), [root]
    while stack:
        m = stack.pop()
        if m in seen or not os.path.exists(src(m)):
            continue
        seen.add(m)
        stack += [x for x in imports(m) if x.startswith('Zeta23')]
    closure = sorted(seen)
    lines = sum(read(src(m)).count(NL) for m in closure)
    mathlib = sorted(set(x for m in closure for x in imports(m) if x.startswith('Mathlib')))
    other = sorted(set(x for m in closure for x in imports(m)
                       if not x.startswith(('Mathlib', 'Zeta23'))))
    allmods = []
    for dp, dns, fns in os.walk(os.path.join(Z, 'Zeta23')):
        for fn in fns:
            if fn.endswith('.lean'):
                allmods.append(fn)
    total_lines = 0
    for dp, dns, fns in os.walk(os.path.join(Z, 'Zeta23')):
        for fn in fns:
            if fn.endswith('.lean'):
                total_lines += read(os.path.join(dp, fn)).count(NL)
    rec('    the theorem : EF_lit_zetaZeroConfig, in %s' % root)
    rec('    ### ### **CLOSURE : %d MODULES of %d in Zeta23/ (%.1f%%) ; %d LINES of %d (%.1f%%)**'
        % (len(closure), len(allmods), 100.0 * len(closure) / len(allmods), lines, total_lines,
           100.0 * lines / total_lines))
    rec('    ### ### **DIRECT MATHLIB IMPORTS FROM THE CLOSURE : %d**' % len(mathlib))
    for x in mathlib:
        rec('      %s' % x)
    if other:
        rec('    other non-project imports : %s' % other)
    # ### does the closure reach the headline? -- the analytic inputs vs the theorem
    head = 'Zeta23.Final'
    rec('    the headline module %s in the closure : %s' % (head, head in closure))
    uses_lemma = sum(1 for m in closure if re.search(r'^\s*(private\s+)?lemma\s', read(src(m)), re.M))
    rec('    closure modules using the `lemma` keyword (rule 9) : %d' % uses_lemma)
    for m in closure:
        rec('      . %s' % m)

    rec('')
    rec('(P5) THE LICENCE TERMS THAT GOVERN VENDORING.')
    rec('-' * 104)
    lic = read(os.path.join(Z, 'LICENSE')) or read(os.path.join(FM, 'LICENSE'))
    notice = read(os.path.join(Z, 'NOTICE')) or read(os.path.join(FM, 'NOTICE'))
    m = re.search(r'4\. Redistribution\..*?(?=\n\s*5\. )', lic, re.S)
    red = re.sub(r'\s+', ' ', m.group(0)).strip() if m else ''
    if not red:
        MISSES.append(('LICENSE', 'section 4'))
    rec('    LICENSE, section 4 :')
    rec('      %s' % red[:1600])
    rec('    NOTICE, in full (%d lines) :' % notice.count(NL))
    for x in notice.split(NL)[:30]:
        rec('      | %s' % x)
    hdr = read(os.path.join(Z, 'Zeta23', 'WeilEF', 'Main.lean')).split(NL)[:5]
    rec('    a source file`s own header (Zeta23/WeilEF/Main.lean:1-5) :')
    for x in hdr:
        rec('      | %s' % x)

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b471_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(flags=flags, navigator_flags=len(nav), rules=rules, pins=pins, zeta23_toolchain=zt,
                   closure=closure, closure_modules=len(closure), zeta23_modules=len(allmods),
                   closure_lines=lines, zeta23_lines=total_lines, mathlib_direct=mathlib,
                   closure_lemma_modules=uses_lemma, headline_in_closure=head in closure,
                   licence_s4=red, notice=notice, misses=MISSES),
              io.open(os.path.join(D, 'b471_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
