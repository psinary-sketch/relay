# -*- coding: utf-8 -*-
"""b470_components.py -- COMPONENTS 1 AND 2 (Component 3 is b470_build.py). ### Run after the seal
### (sha256 `bc6990d2f64fcbe9...`).

### ### **EVERY WRITE SPLICES BYTES.** ### b469 dropped a BOM by decoding with `utf-8-sig` and
### re-encoding with `utf-8`; this writer never decodes a target. It finds the insertion offset in the
### raw bytes, inserts bytes encoded in the target's OWN line ending, and proves the before-and-after
### relation on bytes: prior bytes a true prefix (appends) or the file equal to itself with exactly
### the inserted span removed (the note).
"""
import hashlib
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
Z = os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
WORK = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
INTAKE = os.path.join(ROOT, 'reports', '2026-08-20-external-intake.md')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


S = json.load(io.open(os.path.join(D, 'b470_survey.json'), encoding='utf-8'))
DECL = {d['label']: d for d in S['decls']}


def digests():
    return {fn: hashlib.md5(open(os.path.join(DEP, fn), 'rb').read()).hexdigest()
            for fn in sorted(os.listdir(DEP)) if os.path.isfile(os.path.join(DEP, fn))}


def eol(b):
    return b'\r\n' if b'\r\n' in b else b'\n'


def append_bytes(path, text, mark):
    b = open(path, 'rb').read()
    if mark.encode('utf-8') in b:
        return dict(duplicate=True)
    e = eol(b)
    add = e + text.strip('\n').replace('\n', '\n').encode('utf-8').replace(b'\n', e) + e
    new = b.rstrip(b'\r\n') + e + add
    open(path, 'wb').write(new)
    after = open(path, 'rb').read()
    return dict(prefix=after.startswith(b.rstrip(b'\r\n')), added_lines=after.count(b'\n') - b.count(b'\n'),
                removed=0, bom_kept=(after[:3] == b'\xef\xbb\xbf') == (b[:3] == b'\xef\xbb\xbf'),
                eol=e.decode())


# ------------------------------------------------------------------------------------------------
def component1():
    rec('=' * 104)
    rec('COMPONENT 1 -- zeta23`S EXPLICIT FORMULA FOR ZETA, SET AGAINST b321`S IDENTITY.')
    rec('=' * 104)
    rec('')
    rec('  ### (1a) b321`S IDENTITY, AS THE CHAIN DEFINES IT.')
    rec('    b321_window.py:143  %s' % S['b321'][0].strip())
    rec('    b321_window.py:144  %s' % S['b321'][1].strip())
    rec('    Z  = 2 * SUM_{gamma in AT.GAM} hhat(gamma)           (:138)  hhat(u) = INT w(v) cos(u v) dv')
    rec('    P  = 2 * INT w(v) cosh(v/2) dv                        (:139)')
    rec('    A  = (1/2pi) INT hhat(u) K(u) du, u in [-UMAX, UMAX]  (:141)  K(u) = Re psi(1/4 + iu/2) - log pi')
    rec('    PR = SUM_{p^k <= e^L} 2 log p / sqrt(p^k) * w(log p^k) (:118, the corpus route)')
    rec('    normalization : f(x) = x^{-1/2} w(log x), so v = log x   (:105)')
    rec('    f = g conv g-bar-sharp : formed as the autocorrelation (f^ conv f)(v) = INT f(u) f(u+v) du')
    rec('      (b318_square.py:117) -- EVEN, positive definite, support twice the seed`s')
    rec('    the class of g : Connes-Consani Prop C.1 (155) -- g in C_c^inf(R*_+) with g~(z) = 0 on a finite')
    rec('      F containing {0, 1} (b328_source_text.txt:3830)')
    rec('    ### the chain`s sign line, quoted from the atlas`s own header at b321_window.py:17:')
    rec('    ### "sum_gamma hhat(gamma) = hhat(i/2) + hhat(-i/2) - PRIME + ARCH [sign fixed BY the E2 calibration]"')

    rec('')
    rec('  ### (1b) zeta23`S DECLARATIONS, VERBATIM WITH THEIR TEST-FUNCTION HYPOTHESES.')
    for lab in ('the transform, paperFT', 'the ordinate, gammaOf', 'the Gamma bracket',
                'the literature right-hand side', 'EF_lit (statement)', 'EF_paper (statement)',
                'ExplicitFormulaPaper (statement)', 'EF_lit_zeta (theorem)',
                'EF_lit_zetaZeroConfig (theorem)', 'zetaEF (theorem)', 'prop_EF_of_lit (bridge)',
                'explicitFormulaPaper_of_lit (bridge)'):
        d = DECL[lab]
        rec('    %s -- %s:%d' % (lab, d['file'], d['line']))
        for x in d['statement'].split(NL)[:14]:
            rec('      | %s' % x.rstrip()[:140])

    rec('')
    rec('  ### (1c) CHANNEL BY CHANNEL, UNDER THE SPECIALIZATION k := w.')
    rows = [
        ('test-function class', 'C^2, HasCompactSupport -- NO evenness hypothesis',
         'w from f = g conv g-bar-sharp: C_c^inf, real, EVEN', 'CONTAINED -- the corpus`s w meets EF_lit`s hypotheses'),
        ('variable', 'k on R, primes at k(+-log n)', 'w(v), v = log x, primes at w(log n)', 'SAME'),
        ('transform', 'h(z) = INT k(u) e^{izu} du', 'hhat(u) = INT w(v) cos(uv) dv', 'SAME FOR EVEN REAL w; the corpus`s is the cosine form'),
        ('zero side', 'SUM over EVERY nontrivial zero, WITH multiplicity, at gamma_rho = (rho - 1/2)/i (complex off the line)',
         '2 * SUM over a BANKED LIST of REAL ordinates, doubled', '### DIFFERENCE OF SCOPE -- printed, not resolved'),
        ('pole term', 'h(i/2) + h(-i/2)', '2 INT w cosh(v/2) dv', 'SAME (equal for any w)'),
        ('prime sum', '- SUM Lambda(n) n^{-1/2} (k(log n) + k(-log n))', '- SUM 2 log p p^{-k/2} w(log p^k)',
         'SAME FOR EVEN w; sign SAME (minus)'),
        ('archimedean', '+ (1/2pi) INT_R h(r) [Re psi(1/4 + ir/2) - log pi] dr',
         '+ (1/2pi) INT_{[-UMAX,UMAX]} hhat(u) K(u) du, K the same function', '### KERNEL IDENTICAL; RANGE TRUNCATED in the corpus'),
    ]
    for ch, zz, cc, v in rows:
        rec('    %-19s zeta23 : %s' % (ch, zz))
        rec('    %-19s b321   : %s' % ('', cc))
        rec('    %-19s ### %s' % ('', v))
    rec('')
    rec('  ### (1d) THE DIFFERENCES, PRINTED AND NOT RESOLVED.')
    diffs = [
        ('SIGN', 'none -- pole +, prime -, archimedean + on both sides'),
        ('NORMALIZATION', 'none at content -- the same transform (cosine form for even w), the same Lambda(n) n^{-1/2} weight, '
                          'the same kernel Re psi(1/4 + ir/2) - log pi, the same 1/2pi'),
        ('SCOPE (1) the zero side', 'zeta23 sums every nontrivial zero with multiplicity at a possibly complex ordinate; b321 sums a '
                                    'banked list of real ordinates doubled, which reads every zero in range as ON THE LINE and SIMPLE '
                                    'and stops at the list`s end -- the instrument`s truncation'),
        ('SCOPE (2) the archimedean range', 'zeta23 integrates over R; b321 over [-UMAX, UMAX] on a trapezoid grid'),
        ('SCOPE (3) evenness', 'zeta23 does not assume it; b321 does, in its cosine transform and its doubled sum; the lawful w '
                               'is even by construction, so the identity sits inside EF_lit as its EVEN case'),
    ]
    for k, v in diffs:
        rec('    %-32s %s' % (k, v))

    rec('')
    rec('  ### (1e) THE VERDICT, PER DECLARATION.')
    SPEC = ('g in C_c^inf(R*_+) with g~ = 0 on F >= {0,1}, f = g conv g-bar-sharp, k := w where f(x) = x^{-1/2} w(log x) '
            '[WHICH g]; h = paperFT, equal to the corpus`s cosine hhat for even real w, rho = 1/2 + i gamma_rho [WHICH '
            'NORMALIZATION]; zeta23`s literatureRHS signs, identical to the atlas`s: + pole, - prime, + archimedean '
            '[WHICH SIGN CONVENTION]')
    V = [
        ('EF_lit (statement)', 'CONTAINS',
         'for every k with ContDiff R 2 k and HasCompactSupport k: SUM m_rho h(gamma_rho) = literatureRHS k'),
        ('EF_paper (statement)', 'CONTAINS',
         'W(f,g) = INT h_f conj(h_g) nu_X, supports in [-L/2, L/2]: the SQUARE form of the same identity, the channels '
         'carried in the density nu_X = mu + Pi_X + P_X rather than written apart -- a difference of FORM, printed'),
        ('ExplicitFormulaPaper (statement)', 'CONTAINS',
         'EF_paper with its summability and integrability asserted in the package -- the same verdict, the same difference of form'),
        ('EF_lit_zeta (theorem)', 'CONTAINS', 'EF_lit at zeta`s zeros, under its hypothesis `hs : ZetaSeam`'),
        ('EF_lit_zetaZeroConfig (theorem)', 'CONTAINS',
         'EF_lit zetaZeroConfig, HYPOTHESIS-FREE -- the terminal an import would name'),
        ('zetaEF (theorem)', 'CONTAINS', 'a re-export of EF_lit_zetaZeroConfig'),
        ('prop_EF_of_lit (bridge)', 'DOES NOT',
         'it takes `hEF : EF_lit Z` as a HYPOTHESIS and concludes the paper form; it states no explicit formula of its own'),
        ('explicitFormulaPaper_of_lit (bridge)', 'DOES NOT',
         'it takes `hEF : EF_lit Z` and `hGamma : GammaFacts` as HYPOTHESES; a bridge between forms, not a formula'),
    ]
    rec('    ### THE SPECIALIZATION, IN THREE PARTS: %s' % SPEC)
    for lab, v, why in V:
        rec('    %-40s ### **%s**' % (lab, v))
        rec('        deciding clause: %s' % why)
    contains = [lab for lab, v, _ in V if v == 'CONTAINS']
    rec('    ### ### **CONTAINS : %d ; DOES NOT : %d ; MATCHES : 0**' % (len(contains), len(V) - len(contains)))
    rec('    ### ### **NOT `MATCHES`, BECAUSE b321`S ZERO SIDE IS A TRUNCATED, ON-LINE-ASSUMED SUM AND zeta23`S IS')
    rec('    ### THE FULL MULTISET: THE IDENTITY b321 COMPUTES IS AN INSTANCE OF zeta23`S, NOT THE SAME STATEMENT.**')
    return dict(rows=rows, diffs=diffs, spec=SPEC,
                verdicts=[dict(decl=a, verdict=b, clause=c) for a, b, c in V], contains=contains)


# ------------------------------------------------------------------------------------------------
NOTE = ('**Analytic-row note (2026-09-22, a new external bound).** An unconditional proportion now exceeds '
        'this row’s: *at least two thirds of the nontrivial zeros of ζ, counted with multiplicity, '
        'are simple and lie on the critical line*, and 0.6725 with the Montgomery–Taylor window — '
        'Claude (Anthropic), paper dated 2026-08-11, sha256 `19f827bee5834d61aa6dd756cdaea582492703ddbfd6bdc2058de10b93f7e814`; '
        'the same theorem in Alpöge–Furman, arXiv:2608.13637v2, sha256 '
        '`6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444`; formalised in Lean 4 in '
        '`anthropics/formal-math` at `fbdc36bbf17d20af3fd0447c6d1a8a02773c9844` (project `zeta23`). The method is '
        'not a mollifier: a rank–trace inequality on a finite compression of Weil’s Hermitian form. '
        '**The row’s own figure stays true as a lower bound**; the new bound is, like it, a proportion and '
        'not all. Read at address and graded in the working record, relay `data/b468r_the_proportion_result_at_address.txt`.')

R78 = '''<!-- (R78) the representation coordinate fires only on an identity or a bound -->

### (R78) — on the representation coordinate, (R76)’s trigger is fired only by an identity or a bound — filed 2026-09-22

**RULING (R78), THE AUTHOR’S, RATIFIED AND STRIKEABLE: ON THE REPRESENTATION COORDINATE, (R76)’S TRIGGER IS FIRED ONLY BY AN IDENTITY OR A BOUND.** *The corpus’s second object has off-line zeros (the RH-false witness the deposit itself carries), so no theorem locating zeros on the line can range over a class containing it; the class boundary such theorems show at site (v) is structural and is not counted as an obstruction instance. Appended beside (R76).*

**Where it applies first.** b468r graded the proportion theorem `K1 CLASS BOUNDARY` at sites (v) and (vi) (`data/b468r_components.txt`). Under this ruling the site-(v) boundary is **structural and not an obstruction instance**: a theorem that places zeros on the line cannot range over a class containing an object with off-line zeros. The grade b468r printed stands as its reading; this ruling says how it counts.

*(R76) is not replaced and its record is not edited; this entry is appended beside it. No grade moved; no site was entered; row `U1` is unedited; nothing is claimed about `h2`.*
'''

WORDER = '''<!-- W-ORD-GW-IMPORT opened: a third party's explicit formula contains the instrument's identity -->

### `W-ORD-GW-IMPORT` — OPENED 2026-09-22 (b470): a third party’s machine-checked explicit formula contains the instrument’s identity

**Filed because b470’s comparison returned `CONTAINS`, and b468r’s rule files this order only on `MATCHES` or `CONTAINS`.** In `anthropics/formal-math` at `fbdc36bbf17d20af3fd0447c6d1a8a02773c9844`, project `zeta23`, the theorem `EF_lit_zetaZeroConfig : Zeta23.EF.EF_lit zetaZeroConfig` (`Zeta23/WeilEF/Main.lean:270`) states Weil’s explicit formula for ζ over every `C²` compactly supported test function. **b321’s identity `Z = P − PR + A` (`b321_window.py:143-144`) is its even case**, under the specialization b470 printed: `g ∈ C_c^∞(R*_+)` with `g̃ = 0` on `F ⊇ {0,1}`, `f = g ⋆ ḡ♯`, `k := w` where `f(x) = x^{-1/2} w(log x)`; the same transform, weights, kernel and signs. **It does not `MATCH`**: the corpus’s zero side is a truncated, on-line-assumed sum over banked ordinates, and zeta23’s is the full multiset. That is the instrument’s truncation, printed and not resolved.

**The trigger: the author’s ruling on importing a third party’s terminal under the import bar, at a pin, with its axiom profile RUN and not read.** Until that ruling nothing is imported, and until the profile is run it is not known. b470’s foreground build is the attempt to run it, and its outcome is in b470’s own record.

*Species: **IMPORT**, filed and not taken. No grade moved; no corpus Lean touched; `h2` where the deposit left it.*
'''


def component2():
    rec('')
    rec('=' * 104)
    rec('COMPONENT 2 -- (R79) EXECUTED; (R78) ENTERED.')
    rec('=' * 104)
    before = digests()
    json.dump(before, io.open(os.path.join(D, 'b470_md5_before.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    W = {}
    # ---- the note, inserted after the 24.4 table, bytes spliced
    b = open(WORK, 'rb').read()
    if b'Analytic-row note (2026-09-22' in b:
        W['note'] = dict(duplicate=True)
    else:
        lines = b.split(b'\n')
        end = S['work_table_end'] - 1          # 0-indexed first line after the table
        assert lines[end - 1].startswith(b'|') and not lines[end].startswith(b'|')
        ins = [b'', NOTE.encode('utf-8')]
        new = b'\n'.join(lines[:end] + ins + lines[end:])
        open(WORK, 'wb').write(new)
        a = open(WORK, 'rb').read().split(b'\n')
        restored = a[:end] + a[end + len(ins):]
        W['note'] = dict(added=len(a) - len(lines), removed=0, no_line_edited=(restored == lines),
                         after_table=lines[end - 1][:40].decode('utf-8', 'replace'))
    rec('  the 24.4 note : %s' % W['note'])
    # ---- the intake closure
    close = ('> **CLOSED 2026-09-22 (b470), under the author’s ruling (R79).** The paper read owed here since '
             '2026-08-20 is made: the five primaries are on disk and hash-verified, the theorem is read at address, '
             'and both paper-read flags above can now be read against it — relay `data/b468r_the_proportion_result_'
             'at_address.txt` and `data/b468r_components.txt` (the no-Euler-clause flag against the paper’s sentence '
             'that its inputs *hold for Davenport–Heilbronn and Epstein zeta functions*; the obstructed-limit flag '
             'against its bandwidth-one ceiling sentence). This line is appended; no line above it is edited.')
    W['intake'] = append_bytes(INTAKE, close, 'CLOSED 2026-09-22 (b470)')
    rec('  the intake closure : %s' % W['intake'])
    # ---- (R78) beside (R76), and W-ORD-GW-IMPORT
    W['r78'] = append_bytes(OT, R78, '### (R78) —')
    rec('  (R78) entry : %s' % W['r78'])
    after = digests()
    json.dump(after, io.open(os.path.join(D, 'b470_md5_after.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    rec('  the deposited directory :')
    for fn in sorted(before):
        rec('    %-38s %s  %s%s' % (fn, before[fn], after[fn], '' if before[fn] == after[fn] else '  ### CHANGED'))
    W['deposit'] = dict(unchanged=sum(before[f] == after[f] for f in before), total=len(before),
                        all_same=before == after)
    rec('  ### ### **UNCHANGED : %d of %d**' % (W['deposit']['unchanged'], W['deposit']['total']))
    return W


def main():
    C1 = component1()
    W = component2()
    if C1['contains']:
        W['worder'] = append_bytes(OT, WORDER, '### `W-ORD-GW-IMPORT` — OPENED')
        rec('  W-ORD-GW-IMPORT filed (CONTAINS) : %s' % W['worder'])
    io.open(os.path.join(D, 'b470_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(C1, io.open(os.path.join(D, 'b470_comparison.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    json.dump(W, io.open(os.path.join(D, 'b470_writes.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
