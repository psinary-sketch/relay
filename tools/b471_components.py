# -*- coding: utf-8 -*-
"""b471_components.py -- COMPONENT 1's launch record and COMPONENT 2's price. ### Run after the seal
### (sha256 `cb5e868ad1ac6dd6...`) and after the detached launch. ### **THE BUILD LOG IS NOT OPENED.**
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
FM = os.path.join(D, 'anthropic-zeta23', 'formal-math')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def git(*a):
    return subprocess.run(['git', '-C', FM] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


S = json.load(io.open(os.path.join(D, 'b471_survey.json'), encoding='utf-8'))
LA = json.load(io.open(os.path.join(D, 'b471_launch.json'), encoding='utf-8-sig'))


def main():
    rec('=' * 104)
    rec('COMPONENT 1 -- THE DETACHED RUN, AS LAUNCHED. ### THE LOG IS NOT READ BY THIS ACT.')
    rec('=' * 104)
    rec('    pid          : %s   (relay/data/b471_zeta23_build.pid)' % LA['pid'])
    rec('    started      : %s' % LA['started_utc'])
    rec('    launcher     : %s -- via Start-Process, hidden, detached' % LA['launcher'])
    rec('    log          : %s' % LA['log'])
    rec('    LEAN_NUM_THREADS : %s' % LA['lean_num_threads'])
    rec('    steps        : lake build Solution ; scripts\\PrintAxioms.lean as shipped ; the named file')
    rec('                   (EF_lit_zetaZeroConfig, EF_lit, EF_lit_zeta), text banked as b471_named_axioms.txt')
    rec('    at launch    : the process was alive after 5 s and the log file existed -- a read of the process')
    rec('                   table and of the file`s EXISTENCE, not of its contents')

    rec('')
    rec('=' * 104)
    rec('COMPONENT 2 -- THE PRICE OF VENDORING, READ AND NOT PAID.')
    rec('=' * 104)
    rec('')
    rec('  ### (2a) THE RULES, AT THEIR LINES.')
    for n in (2, 4, 7, 8, 9):
        r = S['rules'][str(n)]
        rec('    SPIRAL_MAP.md:%d  %s' % (r['line'], r['text']))
    rec('    ### rules 2 and 7 are the order`s; 4 is the order`s claim, checked; 8 and 9 the order did not name.')

    rec('')
    rec('  ### (2b) THE IMPORT CLOSURE OF EF_lit_zetaZeroConfig WITHIN Zeta23/.')
    rec('    ### ### **MODULES : %d of %d (%.1f%%) ; LINES : %d of %d (%.1f%%)**'
        % (S['closure_modules'], S['zeta23_modules'], 100.0 * S['closure_modules'] / S['zeta23_modules'],
           S['closure_lines'], S['zeta23_lines'], 100.0 * S['closure_lines'] / S['zeta23_lines']))
    rec('    ### ### **DIRECT MATHLIB IMPORTS : %d**' % len(S['mathlib_direct']))
    for x in S['mathlib_direct']:
        rec('      %s' % x)
    pnt = [m for m in S['closure'] if 'FromPNTPlus' in m]
    rec('    the headline module Zeta23.Final in the closure : %s' % S['headline_in_closure'])
    rec('    closure modules derived from PrimeNumberTheoremAnd (Zeta23/FromPNTPlus) : %d' % len(pnt))
    rec('    closure modules using the `lemma` keyword : %d' % S['closure_lemma_modules'])

    rec('')
    rec('  ### (2c) THE LICENCE TERMS.')
    rec('    LICENSE, section 4 : %s' % S['licence_s4'])
    rec('    NOTICE, in full :')
    for x in S['notice'].split(NL):
        rec('      | %s' % x)

    rec('')
    rec('  ### (2d) THE THREE THINGS A RULING ON W-ORD-GW-IMPORT WOULD FIX.')
    tag = git('tag')
    rec('    (i) THE PIN. `fbdc36bbf17d20af3fd0447c6d1a8a02773c9844` (2026-09-05, untagged, the tree b468r and')
    rec('        b470 read) or the repository`s only tag `%s` = `%s` (2026-08-10). ### At `v1.0` the' % (tag, git('rev-list', '-n', '1', tag)[:8]))
    rec('        repository root IS the project (no `zeta23/` directory); `EF_lit_zetaZeroConfig` is there at')
    rec('        `Zeta23/WeilEF/Main.lean:270`, the toolchain and Mathlib pin are the same, and the `EF_lit`')
    rec('        statement is IDENTICAL; ### %s commits after the tag touch `zeta23/`, so the PROOFS may differ.'
        % git('rev-list', '--count', 'v1.0..HEAD', '--', 'zeta23'))
    rec('    (ii) THE ATTRIBUTION HEADER. Rule 7: *"Each vendored namespace carries the source kernel name and')
    rec('        version in a comment header."* ### And licence section 4 adds its own: a copy of the licence')
    rec('        (a), notices on modified files (b), retained attribution notices (c), and the NOTICE text (d).')
    rec('        ### **TWO LAYERS: %d of the closure`s modules are PrimeNumberTheoremAnd-derived and carry their' % len(pnt))
    rec('        upstream notices, which the NOTICE says must travel with them.**')
    rec('    (iii) THE TOOLCHAIN. zeta23 pins `%s` and Mathlib `51e6992e`; the federation pins' % S['zeta23_toolchain'])
    rec('        SIDE-kernel `%s` (Mathlib `e960b841`), SIDE-lv-conservation `%s`, SIDE-global-section `%s`,'
        % (S['pins']['SIDE-kernel'], S['pins']['SIDE-lv-conservation'], S['pins']['SIDE-global-section']))
    rec('        SIDE-effects `%s`. ### Rule 4 permits the divergence -- *"Each kernel pins its own toolchain;' % S['pins']['SIDE-effects'])
    rec('        divergence is expected"* -- ### **BUT ONLY PER KERNEL: a vendored copy cannot build inside a')
    rec('        kernel pinned to v4.29 with Mathlib e960b84, so it would have to be its own kernel.**')
    rec('')
    rec('  ### (2e) WHAT THE ORDER`S LIST OMITS, READ FROM THE SAME SECTION.')
    rec('    rule 2 -- *"No Lake cross-dependencies"* -- forbids depending on formal-math by Lake; so the copy is')
    rec('      the only route, and it is what (2b) prices.')
    rec('    rule 8 -- *"`@[default_target]` + `globs := #[.submodules ...]` in every lakefile"* -- zeta23 builds')
    rec('      from `lakefile.toml`; a federation kernel holding it would need the lakefile form rule 8 names.')
    rec('    rule 9 -- *"No `lemma` keyword ... always `theorem`"* -- %d of the %d closure modules use `lemma`;'
        % (S['closure_lemma_modules'], S['closure_modules']))
    rec('      a copy obeying rule 9 would be MODIFIED, which licence section 4(b) then requires be marked.')
    rec('    ### ### **NO FILE IS COPIED. NOTHING IS IMPORTED. THE RULING IS THE AUTHOR`S.**')

    price = dict(closure_modules=S['closure_modules'], zeta23_modules=S['zeta23_modules'],
                 closure_lines=S['closure_lines'], zeta23_lines=S['zeta23_lines'],
                 mathlib_direct=len(S['mathlib_direct']), pnt_derived=len(pnt),
                 lemma_modules=S['closure_lemma_modules'], headline_in_closure=S['headline_in_closure'],
                 tag=tag, pin_head='fbdc36bbf17d20af3fd0447c6d1a8a02773c9844')
    io.open(os.path.join(D, 'b471_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(price, io.open(os.path.join(D, 'b471_price.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main())
