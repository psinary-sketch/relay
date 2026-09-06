# -*- coding: utf-8 -*-
"""b333_filings.py -- TWO APPEND-ONLY FILINGS IN PLACE-papers, GENERATED FROM THE ACT'S OWN RECORDS.

### ### (1) `FACES_LEDGER.md` -- an UPDATE block through the writer's `append_block` (b327_faces_row.py), naming
### row `S1` and the constituent K5 ONLY: its grade lifted from DEFINED-ONLY (b315) to DERIVES-ON-IMPORTS
### (this act's derivation, the imports named); MEASURED-ON-FAMILIES NOT conferred, the sealed bar not met;
### the re-run ranking beside it. ### Row S1 itself is never rewritten.
### ### (2) `FINDINGS.md` -- an addendum appended AFTER the `clause-stated` section (the last section), the
### section byte-identical; the derivation tool's verdict AS PRINTED first, its diagnosis, the chain, the
### third route's like-for-like table, the re-rank.
### ### Every verdict, value and ranking is read from `b333_derive.json`, `b333_diagnose.json` and
### `b333_rerank.json`; nothing is typed from memory of a run. ### Two paths, two run files, numbered on a
### repeat writing run.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
FINDINGS = os.path.join(PP, 'FINDINGS.md')
MARK_F = '<!-- b333 addendum: the archimedean term derived -->'
MARK_L = '<!-- b333 update -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def load(n):
    return json.load(io.open(os.path.join(D, n), encoding='utf-8'))


def texts():
    r = load('b333_derive.json')
    g = load('b333_diagnose.json')
    k = load('b333_rerank.json')
    rk = ', '.join('%d. %s (%s)' % (i, key, gr) for i, (_o, key, _n, gr, _re) in enumerate(k['ranking'], 1))
    soft = ' and '.join(k['softest'])
    k5 = '; '.join('%s (%s)' % (gr, o) for gr, o, _f in k['k5_grades'])
    tab = '; '.join('a = %s: A_3 %+.6f, atlas %+.6f, digamma-on-bump %+.6f, (38)-on-bump %+.6f'
                    % (a, c['A3'], c['atlas_arch'], c['dig_on_bump'], c['w38_on_bump']) for a, c in g['cells'].items())
    tabB = '; '.join('a = %s: (150) %+.6f, A_dig %+.6f, W_38 %+.6f' % (a, c['A150_on_b320_f'], c['A_dig_b320'], c['W38_b320']) for a, c in g['cells'].items())
    verdict = r['verdict']
    faces = [
        '', MARK_L, '',
        '## UPDATE — filed 2026-09-06 (b333): row S1, constituent K5 only',
        '',
        '*Rows above are never rewritten; an update names the row and the constituent it bears on. Written through the writer\'s `append_block`.*',
        '',
        '| row / constituent | what b333 did | the grade table\'s change, and the re-run ranking |',
        '|:--|:--|:--|',
        '| **S1**, constituent **K5** (the archimedean distribution) | THE CLASSICAL TERM DERIVED under the import bar: the source\'s Appendix B read link by link — (150) the principal value at the identity, (151) the Gamma factor with its power of π and its logarithmic derivative against the transform, (152)–(153) the digamma kernel, and the source\'s own `W_∞ = −W_R` — with two elementary identities named (Fourier inversion at zero; the Gamma factor\'s logarithmic derivative, checked numerically for ζ and for the Epstein factor of b326, which is where the factor-of-two hazard lives). **THE DERIVATION TOOL\'S VERDICT, AS PRINTED: %s** — diagnosed (relay `tools/b333_diagnose.py`): this act\'s sealed bar paired the third route on the atlas\'s bump with b320\'s table, and b320 computed that table for its own function, `autocorrelation(mean_zero_variant(a))`; **the record\'s archimedean numbers are not touched** — the third route ((150) on the real side by `mpmath.quad`, no corpus code) agrees with the atlas\'s own banked channel for the bump at all thirteen cells (worst %.3e) and with b320\'s two routes applied to the bump (worst %.3e against the digamma route, %.3e against the (38) route), and (150) on b320\'s own function agrees with b320\'s table (worst %.3e / %.3e). The sealed bar, as sealed, is NOT MET and is not rewritten. | K5\'s grades: %s. MEASURED-ON-FAMILIES is NOT conferred (the sealed bar not met; the diagnostic\'s reading is a reading). THE RANKING RE-RUN under b332\'s sealed rule, nothing adjusted: %s. **THE NEW SOFTEST: %s.** The navigator\'s expectation for the new softest was not stated in the order; this seat\'s (K5 and K6 tied) was %s; the ranking is identical with or without the un-conferred grade (%s). The aim-map is named as next, its target the new softest; neither it nor this act is the discharge. K8, the quantifiers, stays unowned. |'
        % (verdict, g['A_worst']['atlas'], g['A_worst']['dig'], g['A_worst']['w38'], g['B_worst']['dig'], g['B_worst']['w38'],
           k5, rk, soft, k['seat_expectation'], k['ranking_with_families_identical']),
        '',
        '*No grade conferred beyond the derivation\'s own; the measurement\'s grade is not conferred. Nothing about the clause moves. Filed by b333 (relay `data/b333_the_archimedean_term_derived.txt`).*',
    ]
    addendum = [
        '', MARK_F, '',
        '### Addendum to `clause-stated` — filed 2026-09-06 (b333): the archimedean term derived',
        '',
        '*The section above is not edited. This addendum lifts one constituent\'s provenance and re-runs the sealed ranking; it moves nothing about the clause.*',
        '',
        '**The derivation tool\'s verdict, as printed, first: %s.** Diagnosed (relay `tools/b333_diagnose.py`, `data/b333_diagnose_run.txt`): the act\'s sealed bar paired the third route, run on the atlas\'s bump, with the two columns of b320\'s table, and b320 computed that table for its own test function — `autocorrelation(mean_zero_variant(a))`, built in `tools/b320_corroborate.py` before either of its routes runs. **The record\'s archimedean numbers are not touched.** The third route agrees with the corpus\'s own banked channel for the bump (`arch` in `data/carto_atlas.jsonl`) at all thirteen cells, worst %.3e; with b320\'s digamma route applied to the bump, worst %.3e; with b320\'s (38) route applied to the bump, worst %.3e. The source\'s (150) evaluated on b320\'s own function agrees with b320\'s table, worst %.3e against the digamma column and %.3e against the (38) column. The sealed bar, as sealed, is NOT MET and is not rewritten; it is a defect on this act\'s sealed face, declared in the bank.'
        % (verdict, g['A_worst']['atlas'], g['A_worst']['dig'], g['A_worst']['w38'], g['B_worst']['dig'], g['B_worst']['w38']),
        '',
        '**The classical term, from the pinned source\'s Appendix B** (Connes–Consani, arXiv:2006.13771v1, `sha256 b8e0b54a…`, re-hashed before a word was read): (150) `W_R(f) := (log 4π + γ) f(1) + ∫_1^∞ (f(x) + f♯(x) − 2f(1)/x) dx/(x − x⁻¹)` — the principal value at the identity handled by the subtracted term; (151) `W_R(f) = (log π) f(1) − (1/2πi) ∫_{1/2+iw} Re(Γ′/Γ(w/2)) f̃(w) dw` — the Gamma factor with its power of π and its logarithmic derivative against the transform; (152)–(153) `W_∞(f) = ∫_{w=1/2+iτ} h₊(τ) f̃(w) dτ/2π`, `h₊(τ) = −log π + Re λ(1/4 + iτ/2)`, `λ = Γ′/Γ`, with the source\'s own `W_∞ = −W_R`.',
        '',
        '**The chain to the corpus\'s digamma integral, and its own verdict: DERIVES-ON-IMPORT.** Under the corpus\'s conventions — `f(x) = x^{−1/2} w(log x)`, so `f̃(1/2 + iτ) = f̂(τ)` (b318\'s `f-hat`, the atlas\'s `hhat`); `f(1) = w(0)`; `f♯ = f` for even `w` — and the one elementary identity `w(0) = (1/2π)∫ f̂`, the source\'s `h₊` **is** the atlas\'s kernel `Re ψ(1/4 + iu/2) − log π` and the source\'s (152) **is** the atlas\'s `A = (1/2π)∫ ĥ·kernel`: **the corpus\'s `A(f)` is the source\'s `W_∞(f) = −W_R(f)`**, entering (148) as `pole + W_∞ − PRIME`, which is the orientation the calibration fixed (b315). The factor-of-two hazard b326 found is one identity: `h₊` is twice the real part of the logarithmic derivative of `π^{−s/2}Γ(s/2)` at `s = 1/2 + iτ`; the same rule on the Epstein factor `(√23/2π)^s Γ(s)` gives b326\'s `2 Re ψ(1/2 + iτ) − 2 log(2π/√23)`, and b325 had carried the half without the two. Every link is a quotation located in the extract file or an identity checked numerically to 1e-30.',
        '',
        '**The third route, like for like.** (150) on the real side with `mpmath.quad` on the bump re-implemented from its definition, sharing no code with the atlas, with b320\'s (38) route or with the digamma route, at the thirteen arc cells, against the corpus\'s three routes on the same function: %s. **Four routes on the bump now agree at every arc cell; that certifies the routes agree, not the size of the term.** And (150) on b320\'s function against b320\'s table: %s.' % (tab, tabB),
        '',
        '**The re-rank, under the sealed rule with nothing adjusted.** K5\'s grades are now %s; MEASURED-ON-FAMILIES is not conferred (the sealed bar not met). Ranking, softest first: %s. **The new softest: %s.** The ranking is identical with or without the un-conferred grade (%s). The navigator\'s expectation for the new softest was not stated in the order; this seat\'s (K5 and K6 tied) was %s. **The aim-map is named as next, its target the new softest constituent; neither it nor this act is the discharge.** K8, the quantifiers, stays unowned.' % (k5, rk, soft, k['ranking_with_families_identical'], k['seat_expectation']),
        '',
        '### **h2 UNCHANGED. NOTHING PROMOTED. NOTHING DEPOSITS.**',
    ]
    return faces, addendum, r, g, k


def main():
    fails = []
    rec('=' * 100)
    rec('b333 -- THE FILINGS. ### THE LEDGER UPDATE THROUGH THE WRITER; THE FINDINGS ADDENDUM.')
    rec('=' * 100)
    faces, addendum, r, g, k = texts()
    rec('  verdict read from the derivation record : %s' % r['verdict'])
    rec('  diagnostic worst, the bump : atlas %.3e digamma %.3e (38) %.3e ; b320\'s function : %.3e / %.3e ; both inside the reading bar : %s / %s'
        % (g['A_worst']['atlas'], g['A_worst']['dig'], g['A_worst']['w38'], g['B_worst']['dig'], g['B_worst']['w38'], g['A_ok'], g['B_ok']))
    rec('  re-rank record : softest %s ; seat %s ; K5 grades %s' % (k['softest'], k['seat_expectation'], [x[0] for x in k['k5_grades']]))
    st, det = W.append_block(MARK_L, faces)
    rec('  FACES_LEDGER.md   %-16s %s' % (st, det))
    if st not in ('WRITTEN', 'DUPLICATE'):
        fails.append('FACES_LEDGER')
    before = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FINDINGS.md'], capture_output=True).stdout.decode('utf-8', 'replace')
    if MARK_F in before:
        rec('  FINDINGS.md       ALREADY FILED, nothing written (idempotent); mark once : %s' % (before.count(MARK_F) == 1))
    else:
        new = before.rstrip(chr(10)) + chr(10) + chr(10).join(addendum) + chr(10)
        open(FINDINGS + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(FINDINGS + '.tmp', FINDINGS)
        after = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
        pw = after.startswith(before.rstrip(chr(10)))
        pb = after.replace(chr(13) + chr(10), chr(10)).startswith(blob.replace(chr(13) + chr(10), chr(10)).rstrip(chr(10)))
        rec('  FINDINGS.md       WRITTEN +%d lines ; working TRUE PREFIX %s ; blob TRUE PREFIX %s ; mark once %s' % (len(after.splitlines()) - len(before.splitlines()), pw, pb, after.count(MARK_F) == 1))
        if not (pw and pb):
            fails.append('FINDINGS')
    st2 = subprocess.run(['git', '-C', PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2'], capture_output=True, text=True).stdout.strip()
    rec('  git status over outputs/DEPOSITED-v1.1.2 : %r ; THE DEPOSIT IS BYTE-UNCHANGED : %s' % (st2, not st2))
    if st2:
        fails.append('DEPOSIT')
    rec('  ### FILING CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    wrote = any('WRITTEN' in x for x in LINES)
    base = 'b333_filings_run' if wrote else 'b333_filings_rerun'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    sys.exit(code)
