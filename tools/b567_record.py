# -*- coding: utf-8 -*-
"""b567_record.py -- GRH-WEIL ACT THREE; THE CEILING AMENDED; THE ADDENDUM FORMS; THE FORWARD MOVE; THE RESIDUE PREMISE,
UNDER (R177). ### THE RECORD TOOL.
### `python tools/b567_record.py reads | weight | ceiling | field | census | deprecations | bulka | zb | ...`. b566's, b565's
### and b564's helpers are IMPORTED, never copied. This file deletes nothing and moves nothing: the .lake moves and the clone's
### deletion are the seat's own commands on verified absolute paths, after `bulka` has re-verified the vendored bodies.
"""
import io, json, os, re, subprocess, sys, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b566_record as R6  # noqa: E402
import b564_record as Z4  # noqa: E402
Q = R6.Q
PP, FIND, OT, CORR, EF = Q.PP, Q.FIND, Q.OT, Q.CORR, Q.EF
README, REGISTRY = Z4.README, Z4.REGISTRY
RESIDUE = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
NL = chr(10)
rd, g, append_to, guard_absent, poss, line_of = Q.rd, Q.g, Q.append_to, Q.guard_absent, Q.poss, Q.line_of
put_txt, put_json, jl = Q.put_txt, Q.put_json, Q.jl
STD3 = Q.STD3
KER = 'D:/SIDE-explicit-formula'
FWD = 'D:/b566-forward'
LV = 'D:/SIDE-lv-conservation'
PRIOR_RELAY = 'ce360e88'      # ### b566's table housekeeping -- relay's tip before this act
PRIOR_PP = '5ce2895'          # ### b566's PLACE-papers commit
PRIOR_GS = '5440757'          # ### SIDE-global-section before this act
V09 = 'e5a5a83'
BULKA = R6.BULKA
PIN = R6.PIN
MATHLIB = os.path.join(FWD, '.lake', 'packages', 'mathlib')
WEIGHT7_H = '*Appended 2026-10-01 by b567 to the field entry (:5575) and b566’s composition line (:6192), under `(R177)`(1)'
FIELD7_H = '*Appended 2026-10-01 by b567 to the field entry (:5575), under `(R177)`(2)'
CEIL7_H = '*Appended 2026-10-01 by b567 to b564’s record of the ceiling entry (:6144), under `(R177)`(2)'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def _lines(L, path, a, b, label, cap=400):
    R6._lines(L, path, a, b, label, cap)


def _find(L, path, needle, label, cap=300, ctx=0):
    return R6._find(L, path, needle, label, cap, ctx)


def _git_lines(L, repo, rev, rel, needles, label, cap=260):
    """### a file AT A REV, each needle's first line printed with its number."""
    txt = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, rel)], capture_output=True).stdout.decode('utf-8', 'replace')
    ls = txt.replace(chr(13), '').split(NL)
    L.append('### %s -- %s at %s (%s)' % (label, rel, rev, repo))
    for nd in needles:
        hit = [i + 1 for i, l in enumerate(ls) if nd in l]
        L.append('    %-58s %s' % (nd[:58], (':%d | %s' % (hit[0], ls[hit[0] - 1].strip()[:cap])) if hit else '### NOT FOUND'))


def reads():
    """### READING (1): every read printed by path and line, at its pin."""
    L = ['b567 -- READING (1): THE READS, CITED BY PATH AND LINE', '']
    _git_lines(L, KER, V09, 'SIDEExplicitFormula/LiCriterionBridge.lean',
               ['theorem li_coeff_eq_taylorCoeff', 'theorem li_nonneg_iff_rh', 'theorem arith_limit_nonneg_iff_rh',
                'theorem analyticOrderAt_xi_eq_zeta'], 'the composed criterion (the ferry names LiWeil.lean; they are here)')
    _git_lines(L, KER, V09, 'SIDEExplicitFormula/LiWeil.lean', ['def liTerm', 'def LiCoeff', 'theorem rh_imp_li_nonneg'], 'LiWeil.lean')
    _git_lines(L, KER, V09, 'NOTICE', ['Bulka', 'Apache', '35df682f'], 'the kernel`s NOTICE (Bulka`s repository has none)')
    _git_lines(L, KER, V09, 'Vendored/Bulka/LICENSE', ['Apache License', 'Version 2.0, January 2004'], 'the carried LICENSE')
    _git_lines(L, KER, V09, 'SIDEExplicitFormula/GRHWeil.lean',
               ['def parity', 'def GRH_chi ', 'def primeSum_chi', 'def gammaBracket_chi', 'def archTerm_chi', 'def h2_sign_chi'],
               'GRHWeil.lean')
    _git_lines(L, KER, V09, 'SIDEExplicitFormula/Chi/ZeroConfig.lean', ['def chiZeroConfig', 'def IsNontrivialZeroChi'],
               'Chi/ZeroConfig.lean')
    _git_lines(L, KER, V09, 'SIDEExplicitFormula/Chi/ZetaBounds.lean',
               ['WHERE THIS FILE STOPS', 'theorem norm_charPartialSum_le', 'def charPartialSum', 'def LFunction0'],
               'Chi/ZetaBounds.lean, the held point')
    _git_lines(L, KER, V09, 'Zeta23/FromPNTPlus/ZetaBounds.lean',
               ['lemma ZetaBnd_aux1b', 'lemma HasDerivAtZeta0', 'lemma Zeta0EqZeta', 'lemma DerivZeta0EqDerivZeta',
                'theorem analyticAt_riemannZeta', 'noncomputable def riemannZeta0'], 'Zeta23`s ZetaBounds')
    _git_lines(L, KER, V09, 'Zeta23/ExplicitFormula.lean', ['def gammaBracket', 'def literatureRHS', 'def EF_lit'], 'Zeta23`s EF_lit')
    _git_lines(L, KER, V09, 'Zeta23/Defs.lean', ['def paperFT', 'def gammaOf', 'structure ZeroConfig'], 'Zeta23`s Defs')
    mr = subprocess.run(['git', '-C', MATHLIB, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    L.append('### Mathlib checkout %s at %s' % (MATHLIB, mr))
    for rel, nds in (('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean',
                      ['noncomputable def LFunction (χ', 'lemma LFunction_eq_LSeries', 'theorem completedLFunction_one_sub']),
                     ('Mathlib/Analysis/Analytic/Uniqueness.lean', ['theorem eqOn_of_preconnected_of_eventuallyEq']),
                     ('Mathlib/NumberTheory/AbelSummation.lean', ['theorem _root_.sum_mul_eq_sub_sub_integral_mul ',
                                                                   'theorem _root_.sum_mul_eq_sub_sub_integral_mul\'']),
                     ('Mathlib/NumberTheory/LSeries/SumCoeff.lean', ['theorem LSeries_eq_mul_integral ']),
                     ('Mathlib/Analysis/MellinTransform.lean', ['def mellin ', 'theorem mellin_hasDerivAt_of_isBigO_rpow',
                                                                 'theorem mellin_differentiableAt_of_isBigO_rpow '])):
        _git_lines(L, MATHLIB, 'HEAD', rel, nds, 'Mathlib')
    _git_lines(L, LV, '2f71068', 'SIDELvConservation/RegisterPentagon.lean', ['def Register4_positivity', 'theorem R4_positivity_to_RH'],
               'lv (the residue`s premises)')
    _git_lines(L, LV, '2f71068', 'SIDELvConservation/ZeroActingPartial.lean', ['theorem residue_irreducible'], 'lv')
    _git_lines(L, LV, '2f71068', 'SIDELvConservation/ZeroActingPairing.lean', ['theorem zeroActingPairing_to_RH'], 'lv')
    _find(L, os.path.join(D, 'b549_premise.txt'), 'inequalityToPositivity   :', 'b549`s premise list')
    _find(L, OT, 'THE RESIDUE CHAIN, PRICED AFTER THE COMPOSITION', 'OPEN_TRAILS, the residue price', cap=200)
    _find(L, OT, 'THE CONDITIONAL, (R82)’S FORM, BOTH BRANCHES', 'OPEN_TRAILS, the conditional', cap=200)
    _find(L, RESIDUE, '## Correspondence', 'THE_RESIDUE_OF_RH, Correspondence')
    _find(L, RESIDUE, 'THE CASCADE, ACT FIVE -- THE CORRESPONDENCE TIERED', 'THE_RESIDUE_OF_RH, the tier block', cap=160)
    for path, n in ((README, 115), (README, 117), (README, 119), (REGISTRY, 950), (REGISTRY, 952), (REGISTRY, 954),
                    (FIND, 6144), (FIND, 6190), (FIND, 6192)):
        _lines(L, path, n, n, os.path.basename(path), cap=220)
    _find(L, os.path.join(D, 'b551_toolchains.txt'), 'DISTINCT MATHLIB REVS', 'the toolchain census (b551)')
    _find(L, os.path.join(T, 'b566_checks.py'), "('G-LICENCE-PRINTED'", 'the suite`s licence arm (b566)')
    _find(L, os.path.join(T, 'b566_checks.py'), "('G-WRITELIST-KINDS'", 'the suite`s write-list arm (b566)')
    for n in ('b566_trial_b_build.txt', 'b566_reprint_summary.txt', 'b566_step1_license.txt'):
        p = os.path.join(D, n)
        L.append('### relay data/%s : %d lines, sha256 %s' % (n, len(rd(p).split(NL)), hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]))
    L.append('### relay data/b566_closing_push_out.txt committed alone at the act`s start: %s' %
             g(ROOT, 'log', '--format=%h %s', '-1', '--', 'data/b566_closing_push_out.txt')[:120])
    put_txt('b567_reads.txt', L)
    print(NL.join(L))


def weight():
    """### (R177)(1): Li's criterion at its weight, one line after b566's composition line, in b561's and b566's form."""
    guard_absent(FIND, WEIGHT7_H)
    t = (WEIGHT7_H + ' -- LI’S CRITERION COMPILED AS AN EQUIVALENCE, AT ITS WEIGHT:* SIDE-explicit-formula v0.9 = `e5a5a83`: '
         '`li_nonneg_iff_rh : (∀ n, 0 ≤ LiCoeff n) ↔ RiemannHypothesis`, from the kernel’s `rh_imp_li_nonneg` and Bulka’s vendored '
         '`positivity_implies_RH` joined by `li_coeff_eq_taylorCoeff` (`LiCoeff (n+1) = (taylorCoeff riemannXi n).re`); '
         '`arith_limit_nonneg_iff_rh` through `li_identity_sym`. Fifteen new declarations and the twelve they rest on print the '
         'standard three; `RiemannHypothesis` and `riemannZeta` are Mathlib’s, read from their declaring module. **The equality '
         'lemma is itself a finding:** the zero-sum definition of λ_n (the paired sum over Mathlib’s zeros) and the '
         'Taylor-coefficient definition (Li’s original, through log ξ) coincide in the kernel -- the Li–Bombieri–Lagarias '
         'identity compiled, its one substantive step the multiplicity of ζ against ξ on the strip (`analyticOrderAt_xi_eq_zeta`). '
         'The compiled picture of the single located clause has three faces, each equivalent to Mathlib’s RH and so to each other: '
         'Weil positivity on classK (`h2_sign`, through `h2_sign_iff_rh`), Li positivity (∀ n, 0 ≤ LiCoeff n, through '
         '`li_nonneg_iff_rh`), and arithmetic-limit positivity (through `arith_limit_nonneg_iff_rh`). h2 is open; nothing about '
         'ζ’s zeros is proved; the three faces are three statements of the one obligation.')
    res = append_to(FIND, NL + t + NL)
    n = line_of(FIND, WEIGHT7_H)
    put_json('b567_weight.json', dict(line=n, text=poss(t), res=res))
    L = ['b567 -- COMPONENT 1 (a): LI`S CRITERION AT ITS WEIGHT, (R177)(1)', '', '### FINDINGS.md :%s -- %s' % (n, json.dumps(res)),
         '    ' + rd(FIND).split(NL)[n - 1]]
    put_txt('b567_weight.txt', L)
    print(NL.join(L))


def author_sentence():
    """### (R177)(2)'s sentence, READ from the banked ferry between its quotation marks, whitespace-joined -- not retyped."""
    f = ' '.join(rd(os.path.join(D, 'b567_ferry.txt')).split())
    m = re.search(r'amended in the author.s words at README, REGISTRY and the \(R146\)\(2\) entry: "([^"]+)"', f)
    return m.group(1) if m else None


def ceiling():
    s = author_sentence()
    if not s:
        sys.exit('### THE AUTHOR`S SENTENCE WAS NOT FOUND IN THE BANKED FERRY')
    para = ("*(Appended under the author's ruling `(R177)`(2), 2026-10-01, b567, beside the `(R146)`(2) sentence, b564's "
            "`(R174)`(1) sentence and b566's `(R176)`(2) sentence above, which stay: Li's criterion compiled as an equivalence, "
            "SIDE-explicit-formula v0.9 = `e5a5a83`.)* Supportable, the author's sentence: *" + s + "* Not supportable, "
            "unchanged: *RH proved*; *h2_sign proved*; *λ_n ≥ 0 proved*.")
    out = {}
    for path, n in ((README, 119), (REGISTRY, 954)):
        l0 = rd(path).split(NL)[n - 1]
        if '(R176)' not in l0:
            sys.exit('### %s :%d IS NOT b566`S (R176)(2) LINE' % (os.path.basename(path), n))
        guard_absent(path, para[:90])
        out[os.path.basename(path)] = Z4._insert_after(path, n, para) if n < len(rd(path).rstrip(NL).split(NL)) else \
            dict(append_to(path, NL + para + NL), after_line=n, new_line=n + 2)
    # ### the FINDINGS record prints it, as b564's record (:6144) printed the (R174)(1) sentence
    guard_absent(FIND, CEIL7_H)
    rec = (CEIL7_H + ' -- THE CEILING ENTRY AMENDED:* the author’s sentence inserted beside the `(R146)`(2) entry at README.md '
           ':%d and REGISTRY.md :%d (the `(R146)`(2) lines at :115 and :950, b564’s and b566’s beside them, standing unedited): *%s* '
           'Not supportable, unchanged: *RH proved*; *h2_sign proved*; *λ_n ≥ 0 proved*.'
           % (out['README.md']['new_line'], out['REGISTRY.md']['new_line'], s))
    res = append_to(FIND, NL + rec + NL)
    fl = line_of(FIND, CEIL7_H)
    L = ['b567 -- COMPONENT 1 (b): THE CEILING SENTENCE, (R177)(2), BESIDE b566`S LINE IN b536`S FORM', '',
         '### the author`s sentence, read from the banked ferry: ' + s, '### the paragraph: ' + para, '']
    for k, v in out.items():
        L.append('### %s : %s' % (k, json.dumps(v)))
        L.append('    the line now at :%d : %s' % (v['new_line'], rd(os.path.join(PP, k)).split(NL)[v['new_line'] - 1]))
    L.append('### FINDINGS.md :%d -- %s' % (fl, json.dumps(res)))
    put_txt('b567_ceiling.txt', L)
    put_json('b567_ceiling.json', dict(sentence=s, para=para, files=out, findings_line=fl))
    print(NL.join(L))


def field():
    """### (R177)(2): the field entry's sentence, the author's words."""
    guard_absent(FIND, FIELD7_H)
    t = (FIELD7_H + ' -- ONE KERNEL, ONE PIN:* three groups’ compiled pieces -- Zeta23’s explicit formula, Bulka’s converse, the '
         'programme’s criterion, forward half, limit formula and χ-instance -- now compose in one kernel at one pin '
         '(SIDE-explicit-formula v0.9 = `e5a5a83`, Lean v4.34.0-rc1, Mathlib `de5ce8a9`); no priority is claimed.')
    res = append_to(FIND, NL + t + NL)
    n = line_of(FIND, FIELD7_H)
    put_json('b567_field.json', dict(line=n, text=poss(t), res=res))
    L = ['b567 -- COMPONENT 1 (c): THE FIELD ENTRY`S LINE, (R177)(2)', '', '### FINDINGS.md :%s -- %s' % (n, json.dumps(res)),
         '    ' + rd(FIND).split(NL)[n - 1]]
    put_txt('b567_field.txt', L)
    print(NL.join(L))


CENSUS7_H = '### APPENDED 2026-10-01 BY b567 UNDER (R177)(4) -- THE FORWARD MOVE:'


def _mathlib_rev(repo):
    """### the mathlib rev of a repository's lake-manifest.json AT HEAD (the committed file), or None."""
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:lake-manifest.json'], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        return None
    m = json.loads(r.stdout.decode('utf-8', 'replace'))
    for pk in m.get('packages', []):
        if pk.get('name') == 'mathlib':
            return pk.get('rev')
    return None


def census():
    """### (R177)(4): the census gains one line -- SIDE-explicit-formula at the new rev, the distinct-rev count recomputed from
    ### each non-VANILLA repository's lake-manifest.json at HEAD (b551's rule; SIDE-global-section its README's declared rev)."""
    bank = os.path.join(D, 'b551_toolchains.txt')
    txt = rd(bank)
    if CENSUS7_H in txt:
        sys.exit('### THE b567 LINE IS ALREADY IN THE CENSUS')
    rows = [l for l in txt.split(NL) if ' | ' in l and not l.startswith('repository |')]
    L = ['b567 -- COMPONENT 2 (a): THE TOOLCHAIN CENSUS, RECOMPUTED AT HEAD, (R177)(4)', '',
         '### b551`s rows %d; each non-VANILLA row`s mathlib rev re-read from lake-manifest.json AT HEAD' % len(rows), '']
    revs = {}
    for l in rows:
        cells = [c.strip() for c in l.split('|')]
        name, b551_rev = cells[0], cells[2]
        if b551_rev == 'VANILLA':
            continue
        if name.startswith('TECHNE-Core'):
            repo = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
        else:
            repo = os.path.join('D:', os.sep, name)
        if name == 'SIDE-global-section':
            rl = rd(os.path.join(repo, 'README.md')).split(NL)
            li = [i for i, x in enumerate(rl, 1) if 'cecd0c4d56' in x]
            now = 'cecd0c4d56' if li else None
            src = 'README.md:%s (declared, no manifest)' % (li[0] if li else 'NOT FOUND')
        else:
            now = _mathlib_rev(repo)
            src = 'HEAD:lake-manifest.json'
        tc = subprocess.run(['git', '-C', repo, 'show', 'HEAD:lean-toolchain'], capture_output=True, text=True).stdout.strip()
        short = (now or 'NONE')[:10]
        moved = not (now or '').startswith(b551_rev.split(';')[0].split()[-1][:10]) if name != 'SIDE-global-section' else False
        revs.setdefault(short, []).append(name)
        L.append('  %-34s b551 %-44s now %-12s %-28s %s%s' % (name, b551_rev[:44], short, tc, src, '  ### MOVED' if moved else ''))
    L.append('')
    L.append('### ### **DISTINCT MATHLIB REVS AMONG NON-VANILLA REPOSITORIES, RECOMPUTED : %d** (b551: 7)' % len(revs))
    for k, v in revs.items():
        L.append('    %s : %s' % (k, ', '.join(v)))
    ef = _mathlib_rev(KER)
    ef_tc = subprocess.run(['git', '-C', KER, 'show', 'HEAD:lean-toolchain'], capture_output=True, text=True).stdout.strip()
    line = (CENSUS7_H + ' SIDE-explicit-formula | %s | %s | v0.9 = e5a5a83 (was v4.33.0-rc2 / 51e6992efd06 at b551) ; '
            'DISTINCT MATHLIB REVS AMONG NON-VANILLA REPOSITORIES, RECOMPUTED AT HEAD : %d (b551: 7) -- %s'
            % (ef_tc, (ef or 'NONE')[:12], len(revs), '; '.join('%s %s' % (k, '/'.join(v)) for k, v in revs.items())))
    raw = open(bank, 'rb').read()
    if not raw.endswith(b'\n') or b'\r' in raw:
        sys.exit('### THE CENSUS BANK DOES NOT END IN A BARE LF: REFUSING')
    open(bank, 'ab').write(line.encode('utf-8') + b'\n')
    after = open(bank, 'rb').read()
    L.append('')
    L.append('### the line appended to data/b551_toolchains.txt (prefix kept %s, +%d bytes):' % (after.startswith(raw), len(after) - len(raw)))
    L.append('    ' + line)
    put_txt('b567_census_revs.txt', L)
    put_json('b567_census_revs.json', dict(revs=revs, count=len(revs), b551=7, line=line, prefix=after.startswith(raw)))
    print(NL.join(L))


DEP_RE = re.compile(r'^warning: (\S+?\.lean):(\d+):(\d+): (.*deprecated.*)$', re.I)
DEP_NAME = re.compile(r'^`([^`]+)` has been deprecated(?:[:,.]\s*(?:[Uu]se|[Pp]refer using) `([^`]+)` instead)?')   # ### widened: push_neg's `Prefer using`


def deprecations():
    """### (R177)(4): trial (b)'s deprecation warnings counted by class (the deprecated name), the top ten printed; each class
    ### read for a named replacement ("Use `Y` instead": a rename) or none (read by hand, never guessed)."""
    log = rd(os.path.join(D, 'b566_trial_b_build.txt')).replace(chr(13), '').split(NL)
    hits = [m for m in (DEP_RE.match(l) for l in log) if m]
    other = [l for l in log if 'deprecat' in l.lower() and not DEP_RE.match(l)]
    raw = {}
    sites = {}
    repl = {}
    unparsed = []
    for m in hits:
        f, ln, col, msg = m.groups()
        n = DEP_NAME.match(msg)
        if not n:
            unparsed.append(msg)
            key = '(unparsed) ' + msg[:60]
        else:
            key = n.group(1)
            repl.setdefault(key, set()).add(n.group(2) or '(NONE NAMED)')
        raw[key] = raw.get(key, 0) + 1
        sites.setdefault(key, set()).add((f, ln, col))
    order = sorted(raw, key=lambda k: (-raw[k], k))
    files = sorted(set(m.group(1) for m in hits))
    tree = {}
    for f in files:
        top = f.split('/')[0]
        tree[top] = tree.get(top, 0) + 1
    L = ['b567 -- COMPONENT 2 (c): W-ORD-DEPRECATIONS -- TRIAL (b)`S DEPRECATION WARNINGS, COUNTED BY CLASS, (R177)(4)', '',
         '### the log: relay data/b566_trial_b_build.txt (sha256 %s), %d lines' %
         (hashlib.sha256(open(os.path.join(D, 'b566_trial_b_build.txt'), 'rb').read()).hexdigest()[:16], len(log)),
         '### deprecation warning lines (`warning: <file>:<l>:<c>: ... deprecated ...`) : %d' % len(hits),
         '### distinct sites (file, line, column) : %d ; the log repeats a module`s warnings when a later call replays it' %
         len(set((m.group(1), m.group(2), m.group(3)) for m in hits)),
         '### lines naming deprecation in any other shape : %d %s' % (len(other), [x[:100] for x in other[:3]]),
         '### classes (the deprecated name) : %d ; lines whose message is not of the `X` has been deprecated form : %d' % (len(raw), len(unparsed)),
         '### files carrying a warning : %d, by tree: %s' % (len(files), json.dumps(tree)), '',
         '### ### **THE TOP TEN CLASSES BY COUNT** (lines ; distinct sites ; the replacement the warning names):']
    for k in order[:10]:
        L.append('    %-44s %5d ; %4d sites ; -> %s' % (k, raw[k], len(sites[k]), ', '.join(sorted(repl.get(k, {'?'})))))
    L.append('')
    L.append('### every class (lines ; sites ; replacement):')
    for k in order:
        L.append('    %-44s %5d ; %4d ; -> %s' % (k, raw[k], len(sites[k]), ', '.join(sorted(repl.get(k, {'?'})))))
    noname = [k for k in order if '(NONE NAMED)' in repl.get(k, set())]
    L.append('')
    L.append('### classes whose warning names NO replacement : %d %s' % (len(noname), noname))
    put_txt('b567_deprecations.txt', L)
    put_json('b567_deprecations.json', dict(lines=len(hits), classes=len(raw), top=[(k, raw[k], len(sites[k]), sorted(repl.get(k, [])))
                                                                                    for k in order[:10]],
                                            all=[(k, raw[k], len(sites[k]), sorted(repl.get(k, []))) for k in order],
                                            noname=noname, files=len(files), tree=tree, other=len(other)))
    print(NL.join(L[:22]))


STALE7_H = '*Appended 2026-10-01 by b567, under the author’s ruling `(R177)`(4), to the toolchain item (:11232)'
DEPR7_H = '### `W-ORD-DEPRECATIONS` — filed 2026-10-01, b567, under the author’s ruling (R177)(4)'


def trails2():
    """### (R177)(4): toolchain-trial-b551 marked STALE on the trails; W-ORD-DEPRECATIONS filed with the classes counted."""
    guard_absent(OT, STALE7_H)
    guard_absent(OT, DEPR7_H)
    tip = g(LV, 'rev-parse', '--short', 'toolchain-trial-b551').strip()
    n0 = line_of(OT, '**The toolchain item, priced by trial, not merged.**')
    if n0 != 11232:
        sys.exit('### THE TOOLCHAIN ITEM IS NOT AT :11232 (read :%s)' % n0)
    stale = (STALE7_H + ' -- `toolchain-trial-b551` STALE:* SIDE-explicit-formula has moved to Lean `v4.34.0-rc1` and Mathlib '
             '`de5ce8a9` (v0.9 = `e5a5a83`, b566), so the branch `toolchain-trial-b551` (SIDE-lv-conservation forwarded to '
             '`v4.33.0-rc2` / `51e6992e`, tip `%s`) prices a move to a rev no kernel now holds (relay `data/b567_census_revs.txt`). '
             'It is marked STALE; its price is to be re-measured against `de5ce8a9` when the lv item next rises. The branch is kept, '
             'unedited.' % tip)
    dj = jl('b567_deprecations.json')
    top = dj['top']
    cls = '; '.join('`%s` → `%s` %d lines, %d sites' % (k, ', '.join(r), n, s) for k, n, s, r in top)
    wo = (DEPR7_H + NL + NL + '| # | ID | kind | the item | price | trigger |' + NL + '|:--|:--|:--|:--|:--|:--|' + NL +
          '| **1** | `W-ORD-DEPRECATIONS` | **KERNEL** | SIDE-explicit-formula at Lean `v4.34.0-rc1` / Mathlib `de5ce8a9` builds '
          'clean with %d deprecation warning lines (trial (b), relay `data/b566_trial_b_build.txt`), %d distinct sites in %d files '
          '(%s), %d classes, every one naming its replacement (relay `data/b567_deprecations.txt`). The top ten by count: %s. '
          'No class is a semantic change by its own warning: each names a renamed lemma or tactic. | replace each deprecated name '
          'by the one its warning names, file by file (Zeta23 files are vendored: a vendored body is not edited, so their sites '
          'wait for the source`s own move or a vendoring refresh), each module rebuilt one per call, every print re-read | '
          '**the next Mathlib move of SIDE-explicit-formula** |' % (dj['lines'], sum(x[2] for x in dj['all']), dj['files'],
                                                                     ', '.join('%s %d' % kv for kv in dj['tree'].items()),
                                                                     dj['classes'], cls) + NL + NL +
          '*Filed, not started. No kernel byte changes for it at b567.*')
    r1 = append_to(OT, NL + stale + NL)
    r2 = append_to(OT, NL + wo + NL)
    L = ['b567 -- COMPONENT 2 (b)-(c): THE STALE MARK AND W-ORD-DEPRECATIONS ON THE TRAILS, (R177)(4)', '',
         '### OPEN_TRAILS.md :%s -- %s' % (line_of(OT, STALE7_H), json.dumps(r1)), '    ' + poss(stale), '',
         '### OPEN_TRAILS.md :%s -- %s' % (line_of(OT, DEPR7_H), json.dumps(r2))]
    L += ['    ' + x for x in poss(wo).split(NL)]
    put_txt('b567_trails2.txt', L)
    put_json('b567_trails2.json', dict(stale_line=line_of(OT, STALE7_H), wo_line=line_of(OT, DEPR7_H), tip=tip))
    print(NL.join(L))


def bulka():
    """### (R177)(4): the vendored copy verified against the clone's git blobs by digest BEFORE the clone is deleted -- every
    ### vendored body on the kernel's main (header cut at its closing line) against the blob at 35df682f, the LICENSE blob
    ### against the carried copy. The seat deletes the clone only if this exits 0."""
    import b566_checks as C
    S = dict(vdig=jl('b566_vendor_digests.json'))
    rows = C.vendored(S)
    head = g(BULKA, 'rev-parse', 'HEAD').strip()
    lic_c = subprocess.run(['git', '-C', BULKA, 'cat-file', 'blob', PIN + ':LICENSE'], capture_output=True).stdout
    lic_m = subprocess.run(['git', '-C', KER, 'cat-file', 'blob', 'main:Vendored/Bulka/LICENSE'], capture_output=True).stdout
    L = ['b567 -- COMPONENT 2 (e): BULKA`S CLONE -- THE VENDORED COPY VERIFIED AGAINST ITS GIT BLOBS BY DIGEST, (R177)(4)', '',
         '### the clone %s at HEAD %s (the pin %s) ; the kernel`s main %s' % (BULKA, head, PIN, g(KER, 'rev-parse', '--short', 'main').strip()), '']
    agree = 0
    for r in rows:
        ok = bool(r['clone']) and r['body'] == r['clone'] == r['recorded'] == r['bank'] and r['hdr_ok']
        agree += ok
        L.append('  %-74s body %s clone %s hdr %s %s' % (r['path'], r['body'][:12], (r['clone'] or 'ABSENT')[:12],
                                                          r['recorded'] == r['body'], 'AGREE' if ok else '### DIFFER ###'))
    lok = bool(lic_c) and lic_c == lic_m
    L.append('  %-74s clone %s main %s %s' % ('Vendored/Bulka/LICENSE (blob against blob)', hashlib.sha256(lic_c).hexdigest()[:12],
                                               hashlib.sha256(lic_m).hexdigest()[:12], 'AGREE' if lok else '### DIFFER ###'))
    v = (head == PIN and rows and agree == len(rows) and lok)
    L.append('')
    L.append('### ### **VENDORED BODIES %d ; AGREEING %d ; LICENSE %s : %s**' % (len(rows), agree, 'AGREE' if lok else 'DIFFER',
                                                                                 'VERIFIED -- THE CLONE MAY BE DELETED' if v else 'NOT VERIFIED -- KEEP THE CLONE'))
    put_txt('b567_bulka_verify.txt', L)
    put_json('b567_bulka_verify.json', dict(rows=rows, agree=agree, total=len(rows), licence=lok, head=head, verified=bool(v)))
    print(NL.join(L[-3:]))
    return 0 if v else 1


def prints_axioms7(text):
    """### b566's reader WIDENED: a name may END IN A PRIME, which Lean prints as `'X'' depends ...`; b566's `'([^']+)'` could
    ### not read it (b567, Component 4: LFunction0' and sum_mul_eq_sub_sub_integral_mul' were unread by it). The list may wrap."""
    out = {}
    for m in re.finditer(r"^'(.+?)' depends on axioms: \[([^\]]*)\]", text, re.M | re.S):
        out[m.group(1)] = [x.strip() for x in m.group(2).replace(NL, ' ').split(',') if x.strip()]
    for m in re.finditer(r"^'(.+?)' does not depend on any axioms", text, re.M):
        out[m.group(1)] = []
    return out


E0SETS = {
    'residue': dict(prints='b567_residue_prints.txt', decls='b567_decls_residue.json', rev='main',   # ### read at main after the merge: the file is byte-identical to the printed tip
                   
                    record=[('SIDEExplicitFormula/ResidueDischarge.lean',
                             ['SIDEExplicitFormula.ResidueDischarge.register4_positivity_liCoeff_imp_rh',
                              'SIDEExplicitFormula.ResidueDischarge.liCoeff_zero'])]),
    'chi': dict(prints='b567_chi_prints.txt', decls='b567_decls_chi.json', rev='main',
                record=[('SIDEExplicitFormula/Chi/ZetaBoundsStrip.lean',
                         ['SIDEExplicitFormula.GRHWeil.LFunction_eq_mul_integral', 'SIDEExplicitFormula.GRHWeil.hasDerivAt_LFunction0',
                          'SIDEExplicitFormula.GRHWeil.LFunction0_eq_LFunction', 'SIDEExplicitFormula.GRHWeil.norm_integral_tail_le']),
                        ('SIDEExplicitFormula/Chi/Statement.lean', ['SIDEExplicitFormula.GRHWeil.gammaBracket_chi_of_even'])]),
}
DOMAIN = r'(?:≠|<|≤|=|∈|\.Even\b|IsPrimitive)'


def e0(which):
    """### READING (6): every declaration of the set graded from its prints of record and its own statement at the branch's
    ### tip; definitions salt-checked; rowgen's source-side record of the terminals of record (IMPORTED through Q.rowgen_record).
    ### b566's rule, with ONE reading added and printed: a parity predicate of the character is a domain condition."""
    c = E0SETS[which]
    pr = rd(os.path.join(D, c['prints']))
    P0 = prints_axioms7(pr)
    dj = jl(c['decls'])
    decls, consumed = dj['decls'], dj['consumed']
    tip = g(EF, 'rev-parse', c['rev']).strip()
    L = ['b567 -- READING (6): THE E0 READ (%s) -- EVERY DECLARATION GRADED, THE SALT-CHECK, THE ROWGEN RECORD' % which, '',
         '### the prints of record: relay data/%s ; the statements at %s (%s).' % (c['prints'], tip[:7], c['rev']),
         '### THE RULE (b566`s): a theorem is INTERFACES when an explicit hypothesis binder of its statement is a named Prop of a',
         '### vendored or kernel module (a premise passed through); DERIVES when its only binders are domain conditions. ### b567`s',
         '### ONE ADDED READING, declared: a parity predicate of the character (`χ.Even`, `¬ χ.Even`) is a domain condition, as',
         '### `χ ≠ 1` is. ### The prints reader is b566`s widened to names ending in a prime.', '']
    rows = {}
    srcs = {}
    for d in decls:
        n = d['name']
        if d['file'] not in srcs:
            srcs[d['file']] = Q.at(tip, d['file'])
        src = srcs[d['file']]
        ax = P0.get(n)
        m = re.search(r'^(?:theorem|def) ' + re.escape(n.split('.')[-1]) + r'(?![\w\'])(.*?):=', src, re.M | re.S)
        head = ' '.join(m.group(1).split()) if m else ''
        binders = re.findall(r'\((h\w*) : ([^()]*(?:\([^()]*\)[^()]*)*)\)', head)
        prem = [(b, t) for b, t in binders if not re.search(DOMAIN, t)]
        if d['kind'] == 'def':
            gr, why = 'DEF', ''
        else:
            gr = 'INTERFACES' if prem else 'DERIVES'
            why = ', '.join('%s : %s' % bt for bt in prem) or ('domain conditions only: ' + ', '.join('%s : %s' % bt for bt in binders)
                                                               if binders else 'no hypothesis binder')
        rows[n] = dict(grade=gr, why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3), head=head, file=d['file'])
        L.append('    %-40s %-10s %s  -- %s' % (n.split('.')[-1], 'DEFINITION' if gr == 'DEF' else gr,
                                                 'std3' if rows[n]['std3'] else ax, why[:150]))
    L.append('')
    L.append('### THE CONSUMED TERMINALS, their prints:')
    cons = {n: P0.get(n) for n in consumed}
    for n, ax in cons.items():
        L.append('    %-56s %s' % (n, 'std3' if ax is not None and set(ax) <= set(STD3) else ax))
    L.append('')
    L.append('### THE SALT-CHECK -- Lean`s #print of each definition (no sorry):')
    salt = {}
    for d in decls:
        if d['kind'] != 'def':
            continue
        j = pr.find('def %s ' % d['name'])
        if j < 0:
            j = pr.find('def %s' % d['name'])
        blk = pr[j:j + 900].split(NL + 'def ')[0] if j >= 0 else ''
        salt[d['name']] = bool(blk) and 'sorry' not in blk
        L += ['    ' + x for x in blk.strip().split(NL)[:2]] if blk else ['    ### %s NOT PRINTED' % d['name']]
    salt_ok = all(salt.values()) and bool(salt)
    L.append('### ### **THE SALT-CHECK: %s** (%d definitions)' % (salt_ok, len(salt)))
    recs_all = []
    ctl = (True,)
    for rel, names in c['record']:
        recs, ctl = Q.rowgen_record(names, rel, tip, pr)
        recs_all += recs
    L.append('')
    L.append('### THE ROWGEN RECORD (rowgen.py`s extract_doc_body and definition_encoded IMPORTED, at %s):' % tip[:7])
    for r in recs_all:
        L.append('    %-30s defenc %-5s %s | check %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], bool(r['check'])))
    L.append('    control: definition_encoded on `def b560_ctl_stub : Prop := True` -> %s (must be True)' % (ctl,))
    thms = [n for n, r in rows.items() if r['grade'] != 'DEF']
    cnt = {k: sum(1 for n in thms if rows[n]['grade'] == k) for k in ('DERIVES', 'INTERFACES')}
    allstd = all(r['std3'] for r in rows.values())
    consstd = all(a is not None and set(a) <= set(STD3) for a in cons.values())
    gate = (allstd and consstd and salt_ok and ctl[0] and not any(r['defenc'] for r in recs_all) and all(r['check'] for r in recs_all)
            and len(P0) >= len(rows) + len(cons))
    L.append('### ### **THE GATE: EVERY PRINT THE STANDARD THREE %s ; THEOREMS %d (DERIVES %d, INTERFACES %d) ; DEFINITIONS %d ; '
             'CONSUMED %d AT THE STANDARD THREE %s ; THE SALT-CHECK %s => MERGE %s**'
             % (allstd, len(thms), cnt['DERIVES'], cnt['INTERFACES'], len(rows) - len(thms), len(cons), consstd, salt_ok, gate))
    put_txt('b567_e0_%s.txt' % which, L)
    put_json('b567_e0_%s.json' % which, dict(rows=rows, consumed=cons, gate=gate, salt=salt_ok, rowgen=recs_all, rowgen_control=ctl[0],
                                             tip=tip, counts=cnt))
    print(NL.join(L))
    return 0 if gate else 1


ZB_ANALOGUE = {
    'analyticAt_riemannZeta': 'analyticAt_LFunction (Chi/ZetaBounds.lean, b564)',
    'riemannZeta0': 'LFunction0 (Chi/ZetaBounds.lean, b564)',
    'HasDerivAtZeta0': 'hasDerivAt_LFunction0 (Chi/ZetaBoundsStrip.lean, b567)',
    'Zeta0EqZeta': 'LFunction0_eq_LFunction (Chi/ZetaBoundsStrip.lean, b567)',
    'DerivZeta0EqDerivZeta': 'deriv_LFunction0_eq (Chi/ZetaBoundsStrip.lean, b567)',
    'ZetaBnd_aux1b': 'norm_integral_tail_le (Chi/ZetaBoundsStrip.lean, b567)',
}


def zb():
    """### READING (5): which declarations of Zeta23's ZetaBounds.lean a LATER Zeta23 module consumes -- every declaration name
    ### of the file (its own `theorem|lemma|def` lines) searched as a whole word in every other Zeta23 file at v0.9 (git show,
    ### not the working tree); and, for each consumed name and the HasDerivAt pair (R177)(6) names, its χ-analogue by name."""
    rel = 'Zeta23/FromPNTPlus/ZetaBounds.lean'
    src = Q.at(V09, rel)
    names = sorted(set(m.group(2).split('.')[-1] for m in re.finditer(r'^(theorem|lemma|noncomputable def|def) ([^\s({:\[]+)', src, re.M)))
    files = [f for f in g(KER, 'ls-tree', '-r', '--name-only', V09, 'Zeta23').split(NL) if f.endswith('.lean') and f != rel]
    use = {}
    for f in files:
        t = Q.at(V09, f)
        for n in names:
            if re.search(r'(?<![\w.])' + re.escape(n) + r'(?![\w\'])', t):
                use.setdefault(n, []).append(f)
    L = ['b567 -- READING (5): ZETABOUNDS` CONSUMERS -- WHICH OF ITS DECLARATIONS A LATER ZETA23 MODULE READS, AND THE χ-ANALOGUES', '',
         '### %s at v0.9 (%s): %d declaration names ; searched in %d other Zeta23 files, each read at v0.9' % (rel, V09, len(names), len(files)),
         '### CONTROL: the matcher finds `riemannZeta0` in ZetaBounds.lean itself: %s' %
         bool(re.search(r'(?<![\w.])riemannZeta0(?![\w\'])', src)), '']
    for n in sorted(use):
        L.append('    %-34s consumed by %s' % (n, ', '.join(sorted(use[n]))))
    L.append('')
    L.append('### ### **CONSUMED BY A LATER MODULE : %d of %d -- %s**' % (len(use), len(names), ', '.join(sorted(use))))
    L.append('')
    L.append('### THE χ-ANALOGUES, BY NAME (the consumed set and the HasDerivAt pair (R177)(6) names):')
    need = sorted(set(use) | {'HasDerivAtZeta0', 'DerivZeta0EqDerivZeta'})
    have = {}
    tip = g(KER, 'rev-parse', 'main').strip()
    kfiles = {'Chi/ZetaBounds.lean': Q.at(tip, 'SIDEExplicitFormula/Chi/ZetaBounds.lean'),
              'Chi/ZetaBoundsStrip.lean': Q.at(tip, 'SIDEExplicitFormula/Chi/ZetaBoundsStrip.lean')}
    for n in need:
        a = ZB_ANALOGUE.get(n)
        an = a.split(' ')[0] if a else None
        found = bool(an) and any(re.search(r'^(theorem|def) ' + re.escape(an) + r'(?![\w\'])', t, re.M) for t in kfiles.values())
        have[n] = found
        L.append('    %-26s -> %-58s %s' % (n, a or '### NONE', 'PRESENT at main %s' % tip[:7] if found else '### ABSENT'))
    rest = [n for n in names if n not in use]
    L.append('')
    L.append('### NOT CONSUMED BY ANY LATER ZETA23 MODULE (listed, not attempted): %d -- %s' % (len(rest), ', '.join(rest)))
    put_txt('b567_zb_consumers.txt', L)
    put_json('b567_zb_consumers.json', dict(consumed={k: sorted(v) for k, v in use.items()}, analogues=have, total=len(names),
                                            not_consumed=rest, complete=all(have.values())))
    print(NL.join(L[:22]))
    return 0 if all(have.values()) else 1


# ================================================================================ COMPONENTS 3-5: THE RECORD
RES7_H = '*Appended 2026-10-01 by b567, under the author’s ruling `(R177)`(5), to the tier block at :215'
S7_H = '*Appended 2026-10-01 by b567 to b549’s reading of §7 (:5665), under `(R177)`(5)'
FH7 = ('## GRH-Weil, act three: the representation of L(s, χ) on the strip, ZetaBounds’ analogue completed, the explicit '
       'formula for χ stated; the residue chain’s premise discharged; Li’s criterion as three compiled faces')
HEADING7 = ('### b567 — GRH-Weil act three under (R177): the representation of L(s, χ) on the strip, ZetaBounds’ analogue, '
            'EF_lit_chi stated; the residue premise discharged; the ceiling amended; the addendum forms; v0.10')
ROW_ACT7, ROW_T7 = '407', ('408', '409', '410', '411', '412')
TERMS7 = [('SIDEExplicitFormula.ResidueDischarge.', 'register4_positivity_liCoeff_imp_rh', 'SIDEExplicitFormula/ResidueDischarge.lean', 'residue'),
          ('SIDEExplicitFormula.GRHWeil.', 'LFunction_eq_mul_integral', 'SIDEExplicitFormula/Chi/ZetaBoundsStrip.lean', 'chi'),
          ('SIDEExplicitFormula.GRHWeil.', 'hasDerivAt_LFunction0', 'SIDEExplicitFormula/Chi/ZetaBoundsStrip.lean', 'chi'),
          ('SIDEExplicitFormula.GRHWeil.', 'LFunction0_eq_LFunction', 'SIDEExplicitFormula/Chi/ZetaBoundsStrip.lean', 'chi'),
          ('SIDEExplicitFormula.GRHWeil.', 'norm_integral_tail_le', 'SIDEExplicitFormula/Chi/ZetaBoundsStrip.lean', 'chi')]


def kstate7():
    ls = {}
    for l in g(EF, 'ls-remote', 'origin').split(NL):
        if l.strip():
            sha, ref = l.split()
            ls[ref] = sha
    return dict(main=ls.get('refs/heads/main', ''), v010obj=ls.get('refs/tags/v0.10', ''), v010=ls.get('refs/tags/v0.10^{}', ''),
                res=ls.get('refs/heads/residue-discharge-b567', ''), grh=ls.get('refs/heads/grh-weil-b567', ''),
                kept={b: ls.get('refs/heads/' + b, '') for b in ('detection-region-b559', 'grh-weil-b562', 'grh-weil-b564',
                                                                 'li-weil-b561', 'li-weil-b563', 'vendor-bulka-backport-b566',
                                                                 'vendor-bulka-forward-b566')},
                local_main=g(EF, 'rev-parse', 'main').strip())


def residue_line():
    """### (R177)(5): ONE line appended to THE_RESIDUE_OF_RH.md pointing at the discharge by name and pin."""
    guard_absent(RESIDUE, RES7_H)
    k = kstate7()
    t = (RES7_H + ' -- THE LI-CHANNEL PREMISE DISCHARGED:* the row “The residue, compiled (§7)” names `residue_irreducible`, '
         'whose λ carries two premises; at λ := `LiCoeff` the second, `liCriterion : Register4_positivity lam → RiemannHypothesis`, '
         'is now the theorem `SIDEExplicitFormula.ResidueDischarge.register4_positivity_liCoeff_imp_rh` (SIDE-explicit-formula '
         'v0.10 = `%s`, `ResidueDischarge.lean`; [propext, Classical.choice, Quot.sound]; relay `data/b567_residue_prints.txt`), with '
         '`Register4_positivity` restated there from `RegisterPentagon.lean` :152 at `2f71068` (the kernels share no toolchain). The '
         'first premise, `inequalityToPositivity`, is NOT discharged; `residue_irreducible` keeps its INTERFACES grade in lv '
         '(`v0.11.0` = `2f71068`). No byte above this line changes.' % k['main'][:7])
    res = append_to(RESIDUE, NL + t + NL)
    n = line_of(RESIDUE, RES7_H)
    put_json('b567_residue_line.json', dict(line=n, text=poss(t), res=res))
    print('THE_RESIDUE_OF_RH.md :%s %s' % (n, json.dumps(res)))


def s7():
    """### (R177)(5): the §7 reading, a reading and not an edit, at FINDINGS beside b549's."""
    guard_absent(FIND, S7_H)
    if '**§7, read in the light of the compiled criterion.**' not in rd(FIND).split(NL)[5664]:
        sys.exit('### FINDINGS :5665 IS NOT b549`S §7 READING')
    t = (S7_H + ' -- §7 READ AGAINST THE COMPILED FACTS (a reading, not an edit of THE_RESIDUE_OF_RH.md):* §7 calls the residue a '
         'conjunction of two clauses -- zero-realization, and the inequality past the threshold -- and says “only the conjunction is '
         'RH”. Read against what is now compiled, the **“inequality” clause in full is RH**, by three compiled faces, each '
         'equivalent to Mathlib’s `RiemannHypothesis`: Weil positivity on classK (`h2_sign_iff_rh`), Li positivity '
         '(`li_nonneg_iff_rh`; in lv’s own vocabulary, `register4_positivity_liCoeff_imp_rh` for the direction the residue theorem '
         'consumes), and arithmetic-limit positivity (`arith_limit_nonneg_iff_rh`). The **“realization” clause** -- a self-adjoint '
         'operator whose spectrum realizes the zeros -- **is a candidate supplier of that positivity and not a separate '
         'necessity**: no compiled statement makes RH require it, and `residue_irreducible`’s remaining premise, '
         '`inequalityToPositivity`, is the map from such a supplier’s output to the positivity. The disclaimer stands: nothing about '
         'ζ’s zeros is proved, and §§1–8 are not edited.')
    res = append_to(FIND, NL + t + NL)
    n = line_of(FIND, S7_H)
    put_json('b567_s7.json', dict(line=n, text=poss(t), res=res))
    print('FINDINGS.md :%s %s' % (n, json.dumps(res)))


def scores():
    """### every hypothesis and expectation, scored on its bank; each verdict carries the bank line it reads."""
    rv = jl('b567_census_revs.json')
    dj = jl('b567_deprecations.json')
    e3, e4 = jl('b567_e0_residue.json'), jl('b567_e0_chi.json')
    zbj = jl('b567_zb_consumers.json')
    k = kstate7()
    rr = rd(os.path.join(D, 'b567_b566_rerun_after.txt'))
    lic_ok = re.search(r'G-LICENCE-PRINTED\s+PASS\s+PASS\s+FAIL\s+OK', rr) is not None
    wl_ok = re.search(r'G-WRITELIST-KINDS\s+PASS\s+PASS\s+FAIL\s+OK', rr) is not None
    tw, tl = rd(os.path.join(D, 'b567_test_writelist.txt')), rd(os.path.join(D, 'b567_test_licence.txt'))
    mut = ('15 of 15 cases as wanted -- PASS' in tw and '13 of 13 cases as wanted -- PASS' in tl
           and 'ARM MUTATION: a stray CHANGELOG.md no clause names, beside the addendum -> FAIL got False want False OK' in tw)
    res_decls = e3['rows']
    chi = e4['rows']
    ab = 'SIDEExplicitFormula.GRHWeil.'
    h18a = all(chi.get(ab + n, {}).get('std3') for n in ('LFunction_eq_mul_integral', 'LFunction_eq_mul_integral_of_one_lt_re',
                                                         'differentiableOn_abelRep'))
    h18b = zbj['complete'] and all(chi.get(ab + n, {}).get('std3') for n in ('hasDerivAt_LFunction0', 'LFunction0_eq_LFunction',
                                                                              'deriv_LFunction0_eq', 'norm_integral_tail_le'))
    stmt = Q.at(k['main'], 'SIDEExplicitFormula/Chi/Statement.lean')
    h18c = ('def EF_lit_chi' in stmt and chi.get(ab + 'EF_lit_chi', {}).get('std3') and chi.get(ab + 'gammaBracket_chi_of_even', {}).get('std3')
            and 'theorem EF_lit_chi' not in stmt)
    top = dj['top'][0]
    rename = top[3] and top[3][0] not in ('(NONE NAMED)',) and top[0].split('.')[-1].replace('setOf', 'ofPred') == top[3][0].split('.')[-1]
    kd = [x for x in g(EF, 'diff', '--name-status', 'e5a5a83', k['main'], '--').split(NL) if x.strip()]
    edited_lean = [x for x in kd if x.startswith('M') and x.endswith('.lean')]
    prior = jl('b566_scores.json').get('kstate', {}).get('remote', {})
    kept_same = all(v and v == prior.get('refs/heads/' + br) for br, v in k['kept'].items())   # ### against b566's recorded remote heads
    b566_kept = jl('b566_scores.json').get('kstate', {})
    s = dict(
        h18a=('HELD' if h18a else 'REFUTED') + ' -- LFunction_eq_mul_integral (Chi/ZetaBoundsStrip.lean) prints the standard three: '
             'L(s, χ) = s ∫_(1,∞) S_χ(t) t^(−s−1) dt on 0 < re s, from LFunction_eq_LSeries and LSeries_eq_mul_integral on re s > 1 and '
             'AnalyticOnNhd.eqOn_of_preconnected_of_eventuallyEq on the convex half-plane (data/b567_e0_chi.txt).',
        h18b=('HELD' if h18b else 'REFUTED') + ' -- ON THE FACE`S DECLARED READING of "completes": the %d ZetaBounds names a later Zeta23 '
             'module consumes (%s) and the HasDerivAt pair each have a χ-analogue at the standard three (data/b567_zb_consumers.txt); '
             'the %d names no later module consumes (the strip bounds, the zero-free region) are listed and not attempted. The frontier '
             'moves to Statement.' % (len(zbj['consumed']), ', '.join(sorted(zbj['consumed'])), len(zbj['not_consumed'])),
        h18c=('HELD' if h18c else 'REFUTED') + ' -- Chi/Statement.lean states literatureRHS_chi (archTerm_chi − primeSum_chi) and '
             'EF_lit_chi as definitions, the archimedean bracket by parity printed (gammaBracket_chi_of_even, _of_not_even); EF_lit_chi '
             'is not proved: HELD at its proof.',
        n1=('HELD' if (lic_ok and wl_ok and mut) else 'REFUTED') + ' -- b566`s re-run after the two commits reads G-LICENCE-PRINTED and '
           'G-WRITELIST-KINDS PASS with NEG PASS and POS FAIL (data/b567_b566_rerun_after.txt); the tests` mutations still fail (a '
           'stray no clause names; a working-copy digest) (data/b567_test_writelist.txt 15/15, data/b567_test_licence.txt 13/13). The '
           're-run`s count is 72 of 74, not 74: G-NUMBER-UNCLAIMED and G-PEEK-DECLARED fail because b567 exists (data/b567_b566_rerun_reading.txt).',
        n2='REFUTED -- its first limb: the distinct-rev count is %d, b551`s %d (data/b567_census_revs.txt): 51e6992e was SIDE-explicit-formula`s '
           'alone, so the move traded one rev for another. Its second limb holds: the top class `%s` (%d lines, %d sites) names `%s`, a '
           'renamed lemma (data/b567_deprecations.txt).' % (rv['count'], rv['b551'], top[0], top[1], top[2], ', '.join(top[3]))
           if rv['count'] == rv['b551'] else ('HELD' if rename else 'REFUTED') + ' -- count %d.' % rv['count'],
        n3=('HELD' if len(res_decls) == 3 and all(r['std3'] for r in res_decls.values()) else 'REFUTED') +
           ' -- ResidueDischarge.lean: Register4_positivity (definition), liCoeff_zero, register4_positivity_liCoeff_imp_rh, each '
           '[propext, Classical.choice, Quot.sound] (data/b567_residue_prints.txt).',
        n4=('HELD' if h18a else 'REFUTED') + ' -- H18a HELD at de5ce8a9; the analytic input is Mathlib`s (LSeries_eq_mul_integral, '
           'mellin_differentiableAt_of_isBigO_rpow, the identity theorem); no differentiation under the integral is written in the kernel.',
        n5=('HELD' if h18b else 'REFUTED') + ' -- H18b HELD on the declared reading; the frontier moves to Statement.',
        n6=('HELD' if (h18c and k['v010'] == k['main'] and k['v010']) else 'REFUTED') +
           ' -- EF_lit_chi stated, the bracket by parity named, HELD at its proof; v0.10 = %s (tag object %s) read back at the remote, '
           'carrying Component 3 and all of Component 4.' % (k['v010'][:7], k['v010obj'][:7]),
        n7=('HELD' if (not edited_lean and kept_same) else 'REFUTED') + ' -- no existing .lean file of the kernel modified (v0.9 -> v0.10: %s); '
           'the prior banks changed only by the lines (R177) orders (b566_step1_license.txt, b551_toolchains.txt), the addendum bank new; '
           'nothing at Zenodo; nothing deposits; the kept branches at their remote heads.' % ', '.join(kd),
        s1=('HELD' if rv['count'] == rv['b551'] else 'REFUTED') + ' -- the count stays %d.' % rv['count'],
        s2=('HELD' if (h18a and all(r['std3'] for r in chi.values()) and all(r['std3'] for r in res_decls.values())) else 'REFUTED') +
           ' -- (C3) is differentiableOn_abelRep through mellin_differentiableAt_of_isBigO_rpow; (C5) through mellin_hasDerivAt_of_isBigO_rpow; '
           'every new declaration of Components 3 and 4 prints the standard three.',
        s3=('HELD' if (h18b and h18c) else 'REFUTED') + ' -- (C1)-(C8) built (module exit 0); EF_lit_chi stated over GRHWeil.lean`s '
           'primeSum_chi and archTerm_chi, unchanged.',
        kstate=k, edited_lean=edited_lean, b566_kept=bool(b566_kept))
    put_json('b567_scores.json', s)
    for x in ('h18a', 'h18b', 'h18c', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3'):
        print('  %-5s %s' % (x, s[x][:170]))


def findings():
    guard_absent(FIND, FH7)
    s = jl('b567_scores.json')
    k = s['kstate']
    wj, cj, fj, sj = jl('b567_weight.json'), jl('b567_ceiling.json'), jl('b567_field.json'), jl('b567_s7.json')
    t2 = jl('b567_trails2.json')
    rv, dj = jl('b567_census_revs.json'), jl('b567_deprecations.json')
    t = ['', FH7, '',
         '*Filed at b567 on the author’s ruling `(R177)`. Banks: relay `data/b567_residue_statement.txt`, `data/b567_residue_build.txt`, '
         '`data/b567_residue_prints.txt`, `data/b567_chi_build.txt`, `data/b567_chi_prints.txt`, `data/b567_e0_residue.txt`, '
         '`data/b567_e0_chi.txt`, `data/b567_zb_consumers.txt`, `data/b567_census_revs.txt`, `data/b567_deprecations.txt`, '
         '`data/b567_bulka_verify.txt`, `data/b567_b566_rerun_reading.txt`. Nothing about the zeros of ζ or of any L(s, χ) is '
         'claimed beyond the compiled statements’ own words.*', '',
         '**The representation of L(s, χ) on the strip.** For a Dirichlet character χ ≠ 1, `LFunction_eq_mul_integral`: L(s, χ) = '
         's ∫_(1,∞) S_χ(t) t^(−s−1) dt on 0 < re s, S_χ the bounded partial sums. On re s > 1 it is Mathlib’s `LSeries_eq_mul_integral` '
         '(SumCoeff.lean :137) with the partial sums O(1); the right side is s · mellin S_χ (−s), analytic on 0 < re s by Mathlib’s '
         '`mellin_differentiableAt_of_isBigO_rpow` (S_χ = O(1) at ∞ and 0 near 0); the identity theorem on the convex half-plane '
         'carries the equality to the strip. The held point of b564 is crossed with no differentiation under the integral written here.', '',
         '**ZetaBounds’ analogue completed, on the act’s reading.** Of Zeta23’s ZetaBounds.lean, four names are consumed by a later Zeta23 '
         'module (`analyticAt_riemannZeta`, `riemannZeta0`, `Zeta0EqZeta`, `ZetaBnd_aux1b`); each has its χ-analogue, with the '
         'HasDerivAt pair: `hasDerivAt_LFunction0` (the derivative `LFunction0\'` explicit, the tail by Mathlib’s Mellin derivative), '
         '`LFunction0_eq_LFunction` (Abel summation on [1, M] by Mathlib’s `sum_mul_eq_sub_sub_integral_mul\'`), `deriv_LFunction0_eq`, '
         '`norm_integral_tail_le` ((N + 1) M^(−σ)/σ where ζ’s has M^(−σ)/σ). The remaining 146 names (the strip bounds, the zero-free '
         'region) feed no consumer of the explicit formula and are listed, not attempted. Every one of the 29 declarations prints the '
         'standard three; 24 theorems grade DERIVES -- two of them (`gammaBracket_chi_of_even`, `_of_not_even`) on the act’s declared '
         'reading that a parity predicate is a domain condition.', '',
         '**The explicit formula for χ, stated.** `EF_lit_chi`: for every k ∈ C_c²(ℝ), the zero sum over the nontrivial zeros of '
         '`LFunction χ` (`chiZeroConfig`) is absolutely summable and equals `literatureRHS_chi χ k` = `archTerm_chi χ k − primeSum_chi '
         'χ k` -- the Γ term by χ’s parity (log(N/π) + Re ψ(1/4 + a/2 + ir/2)), the prime term with χ(n) at log n and conj χ(n) at '
         '−log n, no pole term. STATED and HELD at its proof: the next ζ-specific input is the growth of L in vertical strips '
         '(RvM/ZetaGrowth’s analogue), whose own ZetaBounds inputs are now compiled.', '',
         '**The residue chain’s premise, discharged.** `register4_positivity_liCoeff_imp_rh : Register4_positivity LiCoeff → '
         'RiemannHypothesis`, with `Register4_positivity` restated from lv’s RegisterPentagon.lean :152 at `2f71068` and '
         '`liCoeff_zero`; the three print the standard three. That is residue_irreducible’s `liCriterion` at λ := LiCoeff; its '
         '`inequalityToPositivity` is not discharged, and lv’s theorem keeps its INTERFACES grade. THE_RESIDUE_OF_RH.md gains one '
         'appended line; the §7 reading is entered at FINDINGS :%s.' % sj.get('line'), '',
         '**Li’s criterion as three compiled faces.** At its weight (FINDINGS :%s): Weil positivity on classK, Li positivity and '
         'arithmetic-limit positivity, each equivalent to Mathlib’s RH and so to each other; the ceiling sentence of `(R177)`(2) '
         'beside the (R146)(2) entry at README :%s and REGISTRY :%s, recorded at FINDINGS :%s; the field entry’s line at FINDINGS :%s.'
         % (wj.get('line'), cj['files']['README.md']['new_line'], cj['files']['REGISTRY.md']['new_line'], cj.get('findings_line'),
            fj.get('line')), '',
         '**The forward move, entered.** The toolchain census gains a line: SIDE-explicit-formula at v4.34.0-rc1 / de5ce8a9, the '
         'distinct-rev count recomputed at %d (b551: %d); `toolchain-trial-b551` marked STALE (OPEN_TRAILS :%s); W-ORD-DEPRECATIONS '
         'filed (OPEN_TRAILS :%s): %d deprecation lines, %d classes, every one naming its replacement. The main checkout runs on the '
         'forward worktree’s build tree; Bulka’s clone was deleted after its 33 vendored bodies and the LICENSE agreed by blob digest. '
         'b566’s two record defects are settled by the two addendum forms, each committed alone with its test.'
         % (rv['count'], rv['b551'], t2.get('stale_line'), t2.get('wo_line'), dj['lines'], dj['classes']), '',
         '**v0.10 = `%s`** (tag object `%s`), pushed after main read back; residue-discharge-b567 and grh-weil-b567 pushed by name '
         'and kept.' % (k['v010'][:7], k['v010obj'][:7]), '',
         '**The scores.** H18a %s; H18b %s; H18c %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s, (N7) %s; the seat’s (S1) %s, '
         '(S2) %s, (S3) %s.' % tuple(s[x].split(' --')[0] for x in ('h18a', 'h18b', 'h18c', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7',
                                                                    's1', 's2', 's3')), '',
         '**Next.** The act after this one opens lane three for the ζ-leg alongside GRH-Weil, as `(R177)`(7) gives it: CP-4, the page '
         'without narrative, the ceiling as its last derived line; the author rules on the closing.', '',
         '*Nothing deposits; nothing at Zenodo written; no existing statement of any kernel changed; no sentence here claims priority; '
         'nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    o = append_to(FIND, NL.join(t))
    o['heading_line'] = line_of(FIND, FH7)
    put_json('b567_findings.json', o)
    print('  FINDINGS.md:%s (the entry)' % o['heading_line'])


def rows():
    for r in (ROW_ACT7,) + ROW_T7:
        if [l for l in rd(CORR).split(NL) if l.startswith('| %s |' % r)]:
            sys.exit('### ROW %s ALREADY PRESENT' % r)
    s = jl('b567_scores.json')
    k = s['kstate']
    recs = jl('b567_e0_residue.json')['rowgen'] + jl('b567_e0_chi.json')['rowgen']
    chk = {r['name'].split('.')[-1]: ' '.join(r['check'].split()) for r in recs}
    pin = 'v0.10 = %s' % k['main'][:7]
    act = [ROW_ACT7,
           '**GRH-WEIL ACT THREE AND THE RESIDUE PREMISE** (b567, under (R177)(5)-(6)). SIDE-explicit-formula %s: for χ ≠ 1, '
           'L(s, χ) = s ∫_(1,∞) S_χ(t) t^(−s−1) dt on 0 < re s (Abel summation, Mathlib’s Mellin differentiability, the identity '
           'theorem); the χ-analogues of the ZetaBounds declarations a later Zeta23 module consumes, with the HasDerivAt pair; '
           'EF_lit_chi, the explicit formula for χ, stated and held at its proof; residue_irreducible’s liCriterion premise at '
           'λ := LiCoeff discharged (inequalityToPositivity not). Nothing here proves RH or GRH.' % pin,
           '`SIDE-explicit-formula/SIDEExplicitFormula/ResidueDischarge.lean`, `Chi/ZetaBoundsStrip.lean`, `Chi/Statement.lean` (%s) : ' % pin
           + ', '.join('`%s%s`' % (ns, n) for ns, n, _, _ in TERMS7) + ', `SIDEExplicitFormula.GRHWeil.EF_lit_chi` (definition)',
           '32 of 32 declarations and 9 of 9 consumed terminals: [propext, Classical.choice, Quot.sound], no sorryAx (relay '
           'data/b567_residue_prints.txt, data/b567_chi_prints.txt, data/b567_e0_residue.txt, data/b567_e0_chi.txt)',
           ' ; '.join('`%s` DERIVES' % n for _, n, _, _ in TERMS7),
           'LANDED on main by fast-forward, v0.10 pushed after main read back (tools/push_gated.sh); residue-discharge-b567 and '
           'grh-weil-b567 pushed by name and kept; EF_lit_chi held at its proof; nothing deposits; nothing at Zenodo written.']
    out = []
    r2 = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + act, capture_output=True, text=True, encoding='utf-8')
    out.append(dict(row=ROW_ACT7, exit=r2.returncode, tail=(r2.stdout + r2.stderr)[-300:]))
    for rn, (ns, n, rel, which) in zip(ROW_T7, TERMS7):
        prf = 'data/b567_residue_prints.txt' if which == 'residue' else 'data/b567_chi_prints.txt'
        cells = [rn, '**%s** (b567, under (R177)(%s)), SIDE-explicit-formula %s: `%s`.' % (n, '5' if which == 'residue' else '6', pin,
                                                                                           chk.get(n, '')),
                 '`SIDE-explicit-formula/%s` (%s) : `%s%s`' % (rel, pin, ns, n),
                 "'%s%s' depends on axioms: [propext, Classical.choice, Quot.sound] (relay %s)" % (ns, n, prf),
                 '`%s` DERIVES' % n,
                 'LANDED at %s; Mathlib`s LFunction, LSeries and Mellin transform%s; no premise.'
                 % (pin, '; Mathlib`s RiemannHypothesis' if which == 'residue' else '')]
        r3 = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells, capture_output=True, text=True, encoding='utf-8')
        out.append(dict(row=rn, exit=r3.returncode, tail=(r3.stdout + r3.stderr)[-300:]))
    put_json('b567_rows.json', dict(rows=out, act=act))
    print(json.dumps(out, ensure_ascii=False, indent=1)[:1500])


def rowgen_diff():
    sys.path.insert(0, os.path.join(T, 'rowgen'))
    import rowgen as RG
    recs = jl('b567_e0_residue.json').get('rowgen', []) + jl('b567_e0_chi.json').get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = "'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or [])) if isinstance(r.get('axioms'), list) else (r.get('axioms') or '')
    L = ['b567 -- READING (6): THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE MERGED RECORDS AGAINST CORRESPONDENCE ROWS %s-%s' % (ROW_ACT7, ROW_T7[-1]), '']
    for rn in (ROW_ACT7,) + ROW_T7:
        rowtxt = [l for l in rd(CORR).split(NL) if l.startswith('| %s |' % rn)]
        out = RG.diff(recs, NL.join(rowtxt))
        L.append('### row %s found: %s ; records %d' % (rn, bool(rowtxt), len(recs)))
        L += ['    ' + str(x) for x in out]
    put_txt('b567_rowgen.txt', L)
    print(NL.join(L))


def trail():
    guard_absent(OT, HEADING7)
    s = jl('b567_scores.json')
    k = s['kstate']
    f, wj, cj, fj, sj, t2, rl = (jl(x) for x in ('b567_findings.json', 'b567_weight.json', 'b567_ceiling.json', 'b567_field.json',
                                                 'b567_s7.json', 'b567_trails2.json', 'b567_residue_line.json'))
    rv, dj = jl('b567_census_revs.json'), jl('b567_deprecations.json')
    w = lambda x: s[x].split(' --')[0]
    t = ['', HEADING7, '',
         '**(R177) ratified.** (1) Li’s criterion compiled as an equivalence, entered at its weight. (2) The ceiling amended in the '
         'author’s words. (3) b566’s two record defects settled by addendum forms, the face not edited. (4) The forward move’s '
         'consequences entered. (5) The residue chain’s premise discharged. (6) GRH-Weil act three as (R175)(6) fixed it. (7) The act '
         'after this one opens lane three for the ζ-leg.', '',
         '**Entered:** FINDINGS.md:%s (the weight), :%s (the ceiling record), :%s (the field line), :%s (the §7 reading), :%s (the '
         'entry); README.md:%s and REGISTRY.md:%s (the ceiling sentence of (R177)(2)); OPEN_TRAILS.md:%s (toolchain-trial-b551 STALE) '
         'and :%s (W-ORD-DEPRECATIONS filed); THE_RESIDUE_OF_RH.md:%s (the discharge line); SIDE-global-section CORRESPONDENCE.md rows '
         '%s-%s; SIDE-explicit-formula main = **v0.10** = `%s` (tag object `%s`), residue-discharge-b567 (`%s`) and grh-weil-b567 '
         '(`%s`) pushed by name and kept; relay `data/b551_toolchains.txt` and `data/b566_step1_license.txt` one line each, '
         '`data/b566_writelist_addendum.txt` new.'
         % (wj.get('line'), cj.get('findings_line'), fj.get('line'), sj.get('line'), f.get('heading_line'),
            cj['files']['README.md']['new_line'], cj['files']['REGISTRY.md']['new_line'], t2.get('stale_line'), t2.get('wo_line'),
            rl.get('line'), ROW_ACT7, ROW_T7[-1], k['v010'][:7], k['v010obj'][:7], k['res'][:7], k['grh'][:7]), '',
         '**Component 1:** the addendum forms -- (g) relay `0e50bd19`, (h) relay `90373807`, each with its test; b566’s suite re-run '
         'on b566’s push: the two arms clear, the count 72 of 74 for two arms b567’s existence fails (G-NUMBER-UNCLAIMED, '
         'G-PEEK-DECLARED). **Component 2:** distinct revs %d (b551 %d); %d deprecation lines in %d classes, the top `Set.mem_setOf_eq` '
         '→ `Set.mem_ofPred_eq`; the checkout’s build tree moved in from the forward worktree (the old one aside at '
         '`D:/b567-lake-51e6992e`); Bulka’s clone deleted after 33 of 33 bodies and the LICENSE agreed. **Component 3:** '
         'register4_positivity_liCoeff_imp_rh at the standard three. **Component 4:** LFunction_eq_mul_integral (H18a %s); the '
         'ZetaBounds analogue (H18b %s); EF_lit_chi stated, held (H18c %s).'
         % (rv['count'], rv['b551'], dj['lines'], dj['classes'], w('h18a'), w('h18b'), w('h18c')), '',
         '**Next:** the act after b567 opens lane three for the ζ-leg (CP-4: the page without narrative, the ceiling as its last '
         'derived line) alongside GRH-Weil, as `(R177)`(7) gives it; the author rules on the closing.', '',
         '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s · (N7) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s.'
         % tuple(w(x) for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
         '**Two fast-forwards onto `main`, one tag pushed after main read back, no `sorry` on any `main`.** Nothing deposits; nothing '
         'at Zenodo written; no existing statement changed; no existing `.lean` declaration edited; no Zeta23 or vendored file edited '
         'or added; no monograph byte changed; ERRATA untouched; the ceiling gains one sentence as ruled; row U1 unedited; `h2` where '
         'the deposit left it; the four lists stay OPEN; nothing here is a statement about RH, GRH or any zero beyond the compiled '
         'statements’ own words.', '']
    o = append_to(OT, NL.join(t))
    o['line'] = line_of(OT, HEADING7)
    put_json('b567_trail.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


def desk():
    s = jl('b567_scores.json')
    L = ['=' * 104, 'b567 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H18a-H18c ((R175)(6), carried by (R177)(6)).', '-' * 104]
    L += ['  **(%s)** ### **%s.** -- %s' % (x.upper(), s[x].split(' --')[0], s[x].split(' -- ', 1)[-1]) for x in ('h18a', 'h18b', 'h18c')]
    L += ['', '### THE NAVIGATOR`S SEVEN.', '-' * 104]
    L += ['  **(%s)** ### **%s.** -- %s' % (x.upper(), s[x].split(' --')[0], s[x].split(' -- ', 1)[-1]) for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7')]
    L += ['', '### THE SEAT`S THREE.', '-' * 104]
    L += ['  **(%s)** ### **%s.** -- %s' % (x.upper(), s[x].split(' --')[0], s[x].split(' -- ', 1)[-1]) for x in ('s1', 's2', 's3')]
    nav = [s[x].split(' --')[0] for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7')]
    seat = [s[x].split(' --')[0] for x in ('s1', 's2', 's3')]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE 0.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; '
          'REFUTED %d.**' % (nav.count('HELD'), nav.count('REFUTED'), seat.count('HELD'), seat.count('REFUTED')),
          '### ### **H18 : H18a %s ; H18b %s ; H18c %s.**' % tuple(s[x].split(' --')[0] for x in ('h18a', 'h18b', 'h18c')), '']
    L += [rd(os.path.join(D, 'b567_defects.txt'))]
    put_txt('b567_desk_notes.txt', L)
    print(NL.join(L[:30]))


def components():
    L = ['=' * 132, 'b567 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b567_reads.txt', 'b567_weight.txt', 'b567_ceiling.txt', 'b567_field.txt', 'b567_test_writelist.txt', 'b567_test_licence.txt',
              'b567_b566_rerun_reading.txt', 'b567_census_revs.txt', 'b567_trails2.txt', 'b567_cache.txt', 'b567_cache_nobuild.txt',
              'b567_bulka_verify.txt', 'b567_bulka_delete.txt', 'b567_residue_statement.txt', 'b567_residue_prints.txt',
              'b567_e0_residue.txt', 'b567_zb_consumers.txt', 'b567_e0_chi.txt', 'b567_rowgen.txt', 'b567_branches.txt',
              'b567_kernel_push_out.txt'):
        L.append('### relay data/%s' % n)
        L.extend('  ' + x for x in rd(os.path.join(D, n)).rstrip().split(NL))
        L.append('')
    L.append('### relay data/b567_deprecations.txt -- the classes (first 24 lines):')
    L.extend('  ' + x for x in rd(os.path.join(D, 'b567_deprecations.txt')).rstrip().split(NL)[:24])
    L.append('### relay data/b567_chi_build.txt -- the attempts and the module builds, their headline lines:')
    L.extend('  ' + x for x in rd(os.path.join(D, 'b567_chi_build.txt')).split(NL) if x.startswith('=== ') or x.startswith('--- ') or ': error' in x)
    for n, key in (('b567_weight.json', 'line'), ('b567_field.json', 'line'), ('b567_s7.json', 'line'), ('b567_residue_line.json', 'line'),
                   ('b567_findings.json', 'heading_line'), ('b567_trail.json', 'line')):
        L.append('### relay data/%s -- %s %s' % (n, key, jl(n).get(key)))
    L.append('### relay data/b567_rows.json -- rows %s' % ', '.join('%s exit %s' % (r['row'], r['exit']) for r in jl('b567_rows.json')['rows']))
    put_txt('b567_components.txt', L)
    print('  written: b567_components.txt (%d lines)' % len(L))


def main(argv):
    cmd = argv[0] if argv else ''
    fn = globals().get(cmd)
    if not cmd or not callable(fn) or cmd.startswith('_') or cmd == 'main':
        print(__doc__)
        return 2
    r = fn(*argv[1:])
    return r if isinstance(r, int) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
