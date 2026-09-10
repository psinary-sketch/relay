# -*- coding: utf-8 -*-
"""b404_extract.py -- THE SURVEY THE FACE IS WRITTEN FROM. ### **A READ, AND NOTHING ELSE.**

### ### **THE INSTRUMENT LANE IS PARKED, SO NOTHING IS BUILT.** ### Addition Two asks for two
### terminals *read at their pins with axiom profiles printed*. ### One repository ships a printed
### profile and one does not, and ### **THAT ASYMMETRY IS REPORTED AS A LIMIT ON THIS ACT'S REACH
### ### RATHER THAN WORKED AROUND.** ### Where a profile cannot be read, the answer is what the
### source text discloses about itself -- an import line is not a measurement, and this file says so.

### ### **AND THE ONE THING THIS SURVEY MUST NOT DO IS WIDEN A SCOPED CLAIM**, which is the very
### defect it goes looking for. ### Every claim it quotes is quoted with the sentence that scopes it.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import b305_source as S5        # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SE = os.path.join('D:', os.sep, 'SIDE-effects')
SG = os.path.join('D:', os.sep, 'SIDE-global-section')
FL = os.path.join(PP, 'FACES_LEDGER.md')
CONS = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
SERM = os.path.join(SE, 'README.md')
M1 = os.path.join(SE, 'SIDEEffects', 'Phase15', 'Module1.lean')
FS = os.path.join(SG, 'Core', 'FiniteSideSeal.lean')
AP = os.path.join(SG, 'AXIOM_PRINTS.txt')

CC_SHA = 'b8e0b54ade8535cf3ca633d1ef325bfc5c793b407da577a83d111726935b58e0'
CC_BYTES = 1213504
LG_SHA = '86f3d3c49f5a889f121bb1f04f67694cb9066dc8360f6988165788679594a4a7'
LG_BYTES = 423379
SEARCH_ROOTS = [os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects'),
                os.path.join('C:', os.sep, 'Users', 'ECHOCH~1', 'AppData', 'Local', 'Temp',
                             'claude')]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
READS = []
SRCREADS = []
FIG = {}


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=240):
    return ' '.join(s.split())[:n]


def q(path, hint, label, n=340):
    try:
        i, ln = AF.find(path, hint)
        v = 'ANCHORED'
    except Exception as e:
        i, ln, v = 0, '', ('AMBIGUOUS' if 'AMBIGUOUS' in str(e).upper() else 'ABSENT')
    READS.append(dict(path=os.path.basename(path), label=flat(label, 160), line=i, verdict=v,
                      text=flat(ln, 1200)))
    rec('    %s  ### `%s:%s`' % (label, os.path.basename(path), i or '--'))
    rec('      > %s' % flat(ln, n) if v == 'ANCHORED' else '      ### **%s**' % v)
    return i, ln


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as fh:
        for b in iter(lambda: fh.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def acquire(want_sha, want_bytes):
    hits, scanned = [], 0
    for r in SEARCH_ROOTS:
        for dp, _dn, fn in os.walk(r):
            for f in fn:
                p = os.path.join(dp, f)
                try:
                    if os.path.getsize(p) != want_bytes:
                        continue
                except OSError:
                    continue
                scanned += 1
                try:
                    if sha256_file(p) == want_sha:
                        hits.append(p)
                except OSError:
                    continue
    return hits, scanned


def survey0():
    bar('=')
    rec('  ### (0) THE SOURCES, VERIFIED BEFORE ANY QUOTATION.')
    bar('=')
    out = {}
    for key, sha, nby in (('CC', CC_SHA, CC_BYTES), ('LG', LG_SHA, LG_BYTES)):
        hits, scanned = acquire(sha, nby)
        rec('  ### **%s** : %d bytes ; %d examined by digest ; %d byte-identical copies'
            % (key, nby, scanned, len(hits)))
        if hits:
            rec('      ### **VERIFIED** -- recomputed `%s`' % sha256_file(hits[0])[:32])
            out[key] = hits[0]
        else:
            rec('      ### **HALT** -- no copy matches the pin.')
            out[key] = None
    FIG['sources'] = {k: bool(v) for k, v in out.items()}
    rec()
    return out


def pdf_pages(p):
    from pypdf import PdfReader
    return [S5.flatten(pg.extract_text() or '') for pg in PdfReader(p).pages]


def qsrc(pages, needle, label, after=420):
    nn = S5.flatten(needle)
    found = [(i, t[t.find(nn):t.find(nn) + after]) for i, t in enumerate(pages, 1) if nn in t]
    SRCREADS.append(dict(label=flat(label, 160), needle=nn[:80],
                         pages=[i for i, _ in found]))
    rec('    %s' % label)
    if found:
        rec('      ### page index `%d` -- %d hit(s)' % (found[0][0], len(found)))
        rec('      > %s' % found[0][1][:after])
    else:
        rec('      ### **NOT LOCATED.**')
    rec()
    return found


# ==================================================================================================
def survey1(src):
    bar('=')
    rec('  ### (1) COMPONENT 1 -- THE FIFTH SITE: WHAT EACH CONSTANT IS ALLOWED TO DEPEND ON.')
    bar('=')
    if src.get('LG'):
        pages = pdf_pages(src['LG'])
        qsrc(pages, 'in which the implied constant',
             '### **THEOREM 6.1`S CONSTANT -- THE FINITE PLACES**')
        qsrc(pages, 'and the implied constant in the o notation is absolute',
             '### **THEOREM 5.1`S CONSTANT -- THE ARCHIMEDEAN PLACE**')
    rec('  ### **AND THE RECORD`S OWN READING OF THE PAIR, WHICH THIS ACT DOES NOT RE-IMPORT.**')
    q(os.path.join(D, 'b358_closing.txt'), 'NO UNCONDITIONAL BOUND AT ALL',
      '### `b358` on the asymmetry between the two channels')
    q(os.path.join(D, 'b401_the_absent_element_searched.txt'),
      'ADDITION ONE : ### UNIFORM -- AND VACUOUSLY',
      '### `b401`s verdict, which found the fifth site and did not enter it')
    rec()


def survey2():
    bar('=')
    rec('  ### (2) COMPONENT 2 -- IS THIS A ONE-L-FUNCTION CORPUS? ### **THE QUESTION THE ORDER`S')
    rec('  ### ADDED CLAUSE TURNS ON, AND IT IS ANSWERED FROM THE LEDGER AND NOT FROM ASSUMPTION.**')
    bar('=')
    q(FL, 'a positive Li ledger with RH false',
      '### row `F7` -- **A SECOND L-FUNCTION, AND IT IS ALREADY IN THE RECORD**', 700)
    q(os.path.join(D, 'b325_the_negative_control.txt'),
      'THE ARCHIMEDEAN DISTRIBUTION DOES NOT TRANSFER',
      '### and `b325` on whether anything carried across to it')
    q(os.path.join(D, 'b326_the_reach.txt'), 'do not: Theorem 1 and Theorem 4.7 are stated for',
      '### and `b326` naming exactly which hypothesis fails across the two')
    rec()


def survey3():
    bar('=')
    rec('  ### (3) COMPONENT 3 -- THE ROW`S OWN LAW, READ AT CONTENT.')
    bar('=')
    q(FL, 'U1 -- the uniformity obstruction', '### row `U1`, whole', 1400)
    txt = io.open(FL, encoding='utf-8', errors='replace').read()
    row = [x for x in txt.split(chr(10)) if x.startswith('| U1 |')]
    marks = re.findall(r'\*\*\((i+v?|iv|v|vi)\)', row[0]) if row else []
    rec('      instances the row now carries : %d %s' % (len(marks), marks))
    FIG['u1_instances'] = len(marks)
    rec()


def survey4():
    bar('=')
    rec('  ### (4) ADDITION ONE -- THE CONSPIRACY KEYSTONE`S BOUNDARY PARAGRAPH.')
    bar('=')
    q(CONS, 'The boundary is a local-to-global interchange',
      '### ### **THE BOUNDARY PARAGRAPH, WHOLE**', 1200)
    q(CONS, 'the density lower bound is the whole of the remaining weight',
      '### the residue named for twin primes (M3)', 380)
    q(CONS, 'the representation lower bound is the whole of the remaining weight',
      '### the residue named for Goldbach (M4)', 380)
    q(CONS, 'the sieve density bound is the whole of the remaining weight',
      '### the residue named for Sophie Germain (M5)', 380)
    q(CONS, 'This interchange is exactly what the D↔E unification names',
      '### and the unification the paper names for it', 460)
    rec()


def survey5():
    bar('=')
    rec('  ### (5) ADDITION TWO -- THE TWO TERMINALS, AT CONTENT AND AT THEIR PINS.')
    bar('=')
    rec('  --- **(5a) THE CONSPIRACY PAPER`S COMPILED HALF.** ---')
    q(M1, 'theorem crt_exhaustiveness', '### the terminal statement', 400)
    q(M1, 'theorem no_type_d_conspiracies', '### and the exclusion it licenses', 300)
    q(M1, 'moduli := {L}',
      '### ### **AND THE MODULAR COUPLING IT PRODUCES HAS A SINGLETON MODULI SET**', 300)
    q(M1, 'import Mathlib', '### ### **AND THE MODULE IMPORTS MATHLIB**', 200)
    q(M1, 'classical decidability for the residue filter',
      '### which the module`s own header discloses', 340)
    rec()
    rec('  --- **(5b) WHAT THE PAPER SAYS ABOUT IT, AND WHAT THE REPOSITORY SAYS.** ---')
    q(CONS, '`SIDE-effects` (`c66f3c5`; vanilla Lean 4, no Mathlib). The additive-multiplicative',
      '### ### **THE PAPER`S CLAIM**', 460)
    q(SERM, 'Axiom-free; core',
      '### the README`s claim -- **AND THE SENTENCE IT BELONGS TO**', 420)
    q(SERM, '### `SIDEEffects/Phase15/Module1.lean` — genuine Type-D exclusion',
      '### and what the README says of THIS module, in its own entry', 300)
    q(SERM, 'no-conspiracy result. Genuine content, 0 sorry',
      '### ### **THE README`S GRADE FOR MODULE1: `0 sorry`, AND NOT `0 axioms`**', 300)
    rec()
    rec('  --- **(5c) AT THE PAPER`S OWN CITED REF, `c66f3c5`.** ---')
    r = subprocess.run(['git', '-C', SE, 'show', 'c66f3c5:SIDEEffects/Phase15/Module1.lean'],
                       capture_output=True)
    at_ref = r.stdout.decode('utf-8', 'replace')
    imports = [ln for ln in at_ref.split(chr(10)) if ln.startswith('import ')]
    rec('      the ref resolves in this clone : %s' % bool(at_ref))
    for ln in imports:
        rec('      > %s' % ln)
    mathlib_at_ref = any('Mathlib' in ln for ln in imports)
    rec('      ### ### **MATHLIB IMPORTED AT THE CITED REF : %s**' % mathlib_at_ref)
    FIG['mathlib_at_cited_ref'] = mathlib_at_ref
    FIG['imports_at_cited_ref'] = imports
    rec()
    rec('  --- **(5d) THE FINITE-SIDE SEAL, AND THE ONE PROFILE THAT CAN BE READ.** ---')
    q(FS, 'theorem finite_side_silence', '### the terminal statement', 420)
    q(FS, 'Component 4 -- EXHAUSTIVENESS (`finite_side_silence`): one theorem whose',
      '### and what its own module says it is', 420)
    q(AP, "'B329.finite_side_silence' does not depend on any axioms",
      '### ### **ITS PRINTED PROFILE LINE, READ AND NOT RUN**', 200)
    rec()
    rec('  --- **(5e) AND THE PROFILE THAT CANNOT BE READ, WHICH IS A LIMIT AND NOT A GAP.** ---')
    prof = []
    for dp, _dn, fn in os.walk(SE):
        if '.git' in dp or 'build' in dp or '.lake' in dp:
            continue
        for f in fn:
            if 'AXIOM' in f.upper() or 'PRINT' in f.upper():
                prof.append(os.path.relpath(os.path.join(dp, f), SE))
    rec('      printed-profile files in `SIDE-effects` : %s' % (prof or '### **NONE**'))
    src_has = 0
    for dp, _dn, fn in os.walk(SE):
        if '.git' in dp or 'build' in dp or '.lake' in dp:
            continue
        for f in fn:
            if f.endswith('.lean'):
                try:
                    if '#print axioms' in io.open(os.path.join(dp, f), encoding='utf-8',
                                                  errors='replace').read():
                        src_has += 1
                except OSError:
                    pass
    rec('      `.lean` files carrying a `#print axioms` line : %d' % src_has)
    FIG['se_profile_files'] = prof
    FIG['se_axiomcheck_files'] = src_has
    rec('      ### ### **SO THE AXIOM PROFILE OF `no_type_d_conspiracies` CANNOT BE READ FROM THIS')
    rec('      ### ### REPOSITORY AT ALL, AND THE LANE IS PARKED SO IT IS NOT BUILT.** ### What')
    rec('      ### can be read is what the module DISCLOSES: an import line and a classical')
    rec('      ### decidability. ### **AN IMPORT LINE IS NOT A MEASUREMENT AND IS NOT REPORTED AS')
    rec('      ### ### ONE.**')
    rec()
    for lbl, repo in (('SIDE-effects', SE), ('SIDE-global-section', SG)):
        h = subprocess.run(['git', '-C', repo, 'rev-parse', 'HEAD'], capture_output=True,
                           text=True).stdout.strip()
        rec('      %-22s HEAD : %s' % (lbl, h))
        FIG['head_' + lbl.replace('-', '_')] = h
    rec()


def main():
    bar('=')
    rec('b404 -- THE FIFTH SITE, THE SIXTH CANDIDATE, AND THE ROW`S LAW. ### THE EXTRACT.')
    rec('### **A SURVEY. ### NO KERNEL IS BUILT AND NO INSTRUMENT IS RUN.**')
    bar('=')
    rec()
    src = survey0()
    survey1(src)
    survey2()
    survey3()
    survey4()
    survey5()
    bar('=')
    rec('  ### THE SURVEY, COUNTED.')
    bar('=')
    anc = sum(1 for r in READS if r['verdict'] == 'ANCHORED')
    loc = sum(1 for s in SRCREADS if s['pages'])
    rec('    reads : %d ; ANCHORED %d ; AMBIGUOUS %d ; ABSENT %d'
        % (len(READS), anc, sum(1 for r in READS if r['verdict'] == 'AMBIGUOUS'),
           sum(1 for r in READS if r['verdict'] == 'ABSENT')))
    rec('    source fragments : %d ; LOCATED %d' % (len(SRCREADS), loc))
    FIG['reads'] = len(READS)
    FIG['anchored'] = anc
    FIG['srcreads'] = len(SRCREADS)
    FIG['srclocated'] = loc
    bar('=')
    p = run_clock.write(D, 'b404_extract_notes', L)
    io.open(os.path.join(D, 'b404_extract.json'), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(dict(reads=READS, srcreads=SRCREADS, fig=FIG),
                                              indent=1, ensure_ascii=False) + chr(10))
    print('  written: %s' % os.path.basename(p))
    print('  written: b404_extract.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
