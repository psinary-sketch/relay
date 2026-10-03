# -*- coding: utf-8 -*-
"""b607_worklist.py -- CP-8 ACT TWO'S WORK-LIST AS DATA, UNDER (R217)(4). ### NO WRITE.

### The scope (R216)(2) fixes and (R217)(4) reads: chapters 21 and 22, §24.4 and §27.3 of the monograph's v5.14
### (PLACE-papers day1/A_Place_to_Stand_v5_14.md at 2988bfa). Each change is a sentence of v5.14 copied from its blob (the old
### wording, which must occur once on its line) with the seat's new wording, the clause that reaches it, and what it cites;
### each carry is a sentence of the scope holding a ceiling hit, with its reason. The resolver (`resolve`) reads the blob at the
### pin and checks every old wording; nothing here writes.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
PP = 'D:/MY-DOwnloads/PLACE-papers'
CUR = 'day1/A_Place_to_Stand_v5_14.md'          # ### the current version this act reads (v5.14), unedited
ORIG = 'day1/A_Place_to_Stand.md'               # ### v5.13, unedited
ED = 'day1/A_Place_to_Stand_v5_15.md'
PRE_PP = '2988bfa'
SIEVE = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md'
NL = chr(10)

SCOPE = [(1316, 1418, 'chapters 21-22'), (1490, 1505, '§24.4'), (1788, 1820, '§27.3')]


def show(rev, path, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    ls = t.split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


def in_scope(n):
    return any(a <= n <= b for a, b, _t in SCOPE)


def scope_of(n):
    return next((t for a, b, t in SCOPE if a <= n <= b), None)


# ================================================================================ THE PINS THE CHANGES CITE, AS THE PAGES PRINT THEM
PINS = {
    'simplicity_iff': ('SIDEExplicitFormula.Simplicity.simplicity_iff', 'v0.17 = 5a1630b', 'ζ page node 41 (:45)'),
    'positivity_not_imp_simplicity': ('SIDEExplicitFormula.Doubling.positivity_not_imp_simplicity', 'v0.19 = 5fc0c87', 'ζ page node 52 (:56)'),
    'SimpleProportion': ('SIDEExplicitFormula.Simplicity.SimpleProportion', 'v0.17 = 5a1630b', 'ζ page node 42 (:46)'),
    'exceptional_mass_le_third': ('SIDEExplicitFormula.Simplicity.exceptional_mass_le_third', 'v0.17 = 5a1630b', 'ζ page node 43 (:47)'),
    'ch_iff_rh': ('SIDEExplicitFormula.B321.ch_iff_rh', 'v0.1 = baed4df', 'ζ page node 7 (:11)'),
    'h2_sign_iff_rh': ('SIDEExplicitFormula.B321.h2_sign_iff_rh', 'v0.2 = 5c72cad', 'ζ page node 8 (:12)'),
}
WALK = 'relay data/b596_h29b.txt :133 (headers 117 ; CONCLUDES 0 ; NEGATES 0)'
UPSTREAM = 'relay data/b596_lemmas.txt :140-:146 (thmB₀_mult, Zeta23/FinalMult.lean :350, anthropics/formal-math at 3635e748)'
SIMP_CITE = ('simplicity_iff (v0.17, ζ page node 41); positivity_not_imp_simplicity (v0.19, ζ page node 52); the b596 walk, ' + WALK)

# ================================================================================ THE CHANGES
# ### (id, v5.14 line, kind, clause, old wording (a sentence of the line, copied), new wording, cites, reason)
# ### kind: join (a sentence or a title letting simplicity carry RH), ceiling, restatement, ruled (the ruling's own reading),
# ### table (the convergence table's sieve column).
CHANGES = [
    ('J01', 1316, 'join', 'the ceiling clause (OPEN_TRAILS :11906)',
     '# Chapter 21: The Simplicity Reduction',
     '# Chapter 21: The Simplicity Reduction, an Open Direction',
     SIMP_CITE, 'the chapter`s title names the reduction of RH to simplicity, an edge no compiled statement carries; the object it names is an open direction'),
    ('L01', 1328, 'ruled', '(R217)(4): Conrey`s 40.77% read by §24.4`s analytic-row note',
     '- **Theoretical:** Conrey (1989) proved at least 40.77% of zeros are simple.',
     '- **Theoretical:** Conrey (1989) proved at least 40.77% of zeros are simple — a proportion, read with §24.4’s analytic-row note, '
     'where the unconditional two thirds stands in the kernel as the named premise SimpleProportion (SIDE-explicit-formula v0.17), not a '
     'compiled fact.',
     'SimpleProportion (v0.17, ζ page node 42); ' + UPSTREAM, 'the ruling reads Conrey`s figure by the analytic-row note; the published "proved" is Conrey`s theorem and carries'),
    ('J02', 1337, 'join', 'the ceiling clause, with (R217)(4)`s citations',
     'The direction argued here is the reverse: from simplicity toward RH, an edge no compiled statement carries (simplicity is a separate '
     'located clause, simplicity_iff, SIDE-explicit-formula v0.17).',
     'The direction argued here is the reverse: from simplicity toward RH, the programme’s reading of an open direction — an edge no compiled '
     'statement carries (simplicity is the second located clause, simplicity_iff, SIDE-explicit-formula v0.17; within the schema positivity '
     'does not imply it, positivity_not_imp_simplicity, v0.19; the b596 walk read 117 federation headers and found none concluding or '
     'negating it, relay data/b596_h29b.txt :133).',
     SIMP_CITE, '"the direction ... is the reverse" takes the ceiling as the programme`s reading of an open direction (R217)(4); simplicity named the second located clause'),
    ('J03', 1337, 'join', 'the ceiling clause',
     'The structural reason it works is the perpendicular crossing theorem, which converts information about zero multiplicity into '
     'information about the geometry of level curves near the critical line.',
     'The structural reason the programme pursues it is the perpendicular crossing theorem, which converts information about zero '
     'multiplicity into information about the geometry of level curves near the critical line.',
     SIMP_CITE, '"it works" says the open direction carries; the object is the direction the programme pursues'),
    ('J04', 1341, 'join', 'the ceiling clause',
     '# Chapter 22: The Proof from Simplicity',
     '# Chapter 22: The Argument from Simplicity, an Open Direction',
     SIMP_CITE, 'the title names a proof of RH from simplicity; the object the chapter carries is an argument along an open direction'),
    ('J05', 1380, 'join', 'the ceiling clause',
     '## 22.5 The Main Theorem',
     '## 22.5 The Main Conditional, an Open Direction',
     SIMP_CITE, 'the heading titles simplicity -> RH a theorem; no compiled statement carries it'),
    ('J06', 1382, 'join', 'the ceiling clause, with (R217)(4)`s citations',
     '**Theorem.** If all nontrivial zeros of ζ are simple, then the Riemann Hypothesis holds.',
     '**The conditional, the programme’s reading of an open direction.** If all nontrivial zeros of ζ are simple, then the Riemann '
     'Hypothesis holds — an edge no compiled statement carries: simplicity is the second located clause (simplicity_iff, '
     'SIDE-explicit-formula v0.17), within the schema positivity does not imply it (positivity_not_imp_simplicity, v0.19), and the b596 '
     'walk found 0 of 117 federation headers concluding or negating it (relay data/b596_h29b.txt :133).',
     SIMP_CITE, 'the join itself, stated as a theorem: simplicity carrying RH'),
    ('J07', 1384, 'join', 'the ceiling clause',
     '*Proof.* Suppose all nontrivial zeros are simple.',
     '*Argument, under the open direction.* Suppose all nontrivial zeros are simple.',
     SIMP_CITE, 'the argument for the join, labelled a proof; its joint step is the geometric clause, open (§22.5, §24.4)'),
    ('J08', 1398, 'join', 'the ceiling clause',
     'By the fold criterion (§22.4), the absence of folds implies the absence of off-line zeros.',
     'By the fold criterion (§22.4), in the programme’s reading of an open direction, the absence of folds implies the absence of off-line '
     'zeros.',
     SIMP_CITE, 'the chain`s last link toward RH, read in the open direction'),
    ('J09', 1400, 'join', 'the ceiling clause',
     'The proof chain: simplicity → transversal crossing → nonzero departure speed → no fold → no off-line zero.',
     'The conditional chain, the programme’s reading of an open direction: simplicity → transversal crossing → nonzero departure speed → no '
     'fold → no off-line zero.',
     SIMP_CITE, '"the proof chain" from simplicity to no off-line zero; the object is a conditional chain along an open direction'),
    ('J10', 1400, 'join', 'the ceiling clause',
     'Each link is proved — the chain is the conditional, and its antecedent (simplicity) is the geometric clause (§24.4).',
     'Each link is argued in §22.1–§22.5, the perpendicular crossing compiled for completedRiemannZeta₀ alone (spectral_cannon, §25.8) and '
     'the joint step of §22.5 open — the chain is the conditional, and its antecedent (simplicity) is the geometric clause (§24.4), the '
     'second located clause (simplicity_iff, v0.17).',
     SIMP_CITE + '; spectral_cannon, §25.8`s concordance (Route 2, SIDE-kernel)', '"each link is proved" while the joint step is open (§22.5, :1396)'),
    ('J11', 1406, 'join', 'the ceiling clause',
     '## 22.7 The Two Proofs',
     '## 22.7 The Two Strategies',
     SIMP_CITE, 'the heading names Parts III and IV proofs of RH; the section`s own words name them strategies (:1400)'),
    ('J12', 1408, 'join', '(R217)(4)`s citations on act one`s U08 rewrite',
     'Part IV argues RH from simplicity: perpendicular crossing, monotonicity, fold exclusion — an edge no compiled statement carries '
     '(simplicity_iff).',
     'Part IV argues RH from simplicity: perpendicular crossing, monotonicity, fold exclusion — an edge no compiled statement carries '
     '(simplicity_iff, v0.17, the second located clause; positivity_not_imp_simplicity, v0.19; the b596 walk, 0 of 117).',
     SIMP_CITE, 'act one`s ceiling rewrite (U08) carries the join without (R217)(4)`s citations'),
    ('J13', 1408, 'join', 'the ceiling clause',
     'The two proofs use overlapping but distinct mathematics.',
     'The two strategies use overlapping but distinct mathematics.',
     SIMP_CITE, '"the two proofs" names Part IV`s argument from simplicity a proof of RH'),
    ('J14', 1408, 'join', 'the ceiling clause',
     'Their convergence on the same conclusion is the structural hallmark of a determined system.',
     'Their convergence on the same conclusion, each conditional on its own open clause, is the structural hallmark of a determined system.',
     SIMP_CITE + '; h2_sign_iff_rh (v0.2, ζ page node 8)', 'the convergence of the two strategies read as reaching RH; each is conditional on its own open clause'),
    # ### §24.4 -- the convergence table's sieve column (THE_FINDINGS_AS_THEY_STAND v0.3 at 2988bfa, by row and line)
    ('T00', 1492, 'table', '(R217)(4): the table takes one new column naming each row`s sieve verdict and the test',
     '| Tradition | Method | Span | Grade toward simplicity |',
     '| Tradition | Method | Span | Grade toward simplicity | Sieve verdict at v0.3 (test; row) |',
     SIEVE, 'the column`s head'),
    ('T01', 1493, 'table', '(R217)(4)', '|:---|:---|:---|:---|', '|:---|:---|:---|:---|:---|', SIEVE, 'the column`s alignment cell'),
    ('T02', 1494, 'table', '(R217)(4)',
     '| Analytic number theory | Mollifiers, mean values (Conrey) | 1942–present | ≥ 40.77% simple — a **proportion**, not all |',
     '| Analytic number theory | Mollifiers, mean values (Conrey) | 1942–present | ≥ 40.77% simple — a **proportion**, not all | DARK, test 1 — '
     'RH-16 (v0.3 :79), the 0.6725 ceiling: a proportion over the zeros, not each zero |',
     SIEVE + ' :79 (RH-16, DARK, test 1); the bench :594', 'the row`s register is the sieve`s 0.6725 ceiling, its one row RH-16'),
    ('T03', 1495, 'table', '(R217)(4)',
     '| Random matrix theory | GUE statistics, universality | 1973–present | 100% simple — **statistical, conditional on GUE** |',
     '| Random matrix theory | GUE statistics, universality | 1973–present | 100% simple — **statistical, conditional on GUE** | DARK, test 1 — '
     'no row; the bench’s super-repulsion fit (v0.3 :593): a spacing statistic carries no real part |',
     SIEVE + ' :593 (the bench) and :37 (the dark registers)', 'the sieve rows no GUE conclusion; its register stands in the bench, darkened by test 1'),
    ('T04', 1496, 'table', '(R217)(4)',
     '| Computation | Zero tables (Odlyzko, LMFDB) | 1986–present | 10¹³⁺ zeros simple — a **finite range** |',
     '| Computation | Zero tables (Odlyzko, LMFDB) | 1986–present | 10¹³⁺ zeros simple — a **finite range** | no row at v0.3 — the sieve '
     'carries no row and no register for a finite range of zeros found simple |',
     SIEVE + ' (no row; the registers :36-:38)', 'no sieve row; no verdict is supplied by the seat'),
    ('T05', 1497, 'table', '(R217)(4)',
     '| RH-false witnesses | Davenport–Heilbronn / Epstein off-line zeros | 2026 | every located off-line zero simple, incl. the new t≈176.70 '
     '(‖D′‖=1.207, doubly-sourced) — **evidence for genericity** |',
     '| RH-false witnesses | Davenport–Heilbronn / Epstein off-line zeros | 2026 | every located off-line zero simple, incl. the new t≈176.70 '
     '(‖D′‖=1.207, doubly-sourced) — **evidence for genericity** | NOT A ROUTE — FD-01 (v0.3 :277) and FD-02 (v0.3 :278), the Epstein witnesses: test '
     '2’s own instrument, not a route; the bench (v0.3 :595) |',
     SIEVE + ' :277 (FD-01), :278 (FD-02), :595 (the bench)', 'the row`s register is the sieve`s Epstein witnesses, two rows, both NOT A ROUTE'),
    ('T06', 1498, 'table', '(R217)(4)',
     '| Mechanism enumeration | I+D+S, seven classes | 2026 | per-class reductions compile (C₁ derives, std3); **joint step open** = the '
     'geometric clause |',
     '| Mechanism enumeration | I+D+S, seven classes | 2026 | per-class reductions compile (C₁ derives, std3); **joint step open** = the '
     'geometric clause | no row at v0.3 — the sieve carries no row for the per-class reductions; their joint step is the geometric clause, '
     'carried openly |',
     SIEVE + ' (no row)', 'no sieve row; no verdict is supplied by the seat'),
    ('T08', 1504, 'ceiling', 'the ceiling clause',
     '**Part III\'s proof of RH does not depend on this clause** — its premise is the arithmetic clause alone (§27.3); the geometric clause '
     'belongs to Part IV\'s independent strategy, which carries it.',
     '**Part III\'s reduction of RH does not depend on this clause** — its premise is the arithmetic clause alone (§27.3); the geometric '
     'clause belongs to Part IV\'s independent strategy, which carries it.',
     'h2_sign_iff_rh (v0.2, ζ page node 8); README :106', '"Part III`s proof of RH": the object Part III carries is the reduction'),
    # ### §27.3
    ('S01', 1790, 'ceiling', 'the ceiling clause',
     'This section does that for the present proof.',
     'This section does that for the present reduction.',
     'README :106 (the supportable sentence: RH reduced to a single located clause)', '"the present proof" names the monograph`s argument a proof of RH'),
    ('S02', 1792, 'restatement', 'the restatement clause (OPEN_TRAILS :12192), under E-2026-09-25-6`s reading (E6-04)',
     'The premise has appeared in this monograph and its deposits under several names, in several vocabularies, without a section stating '
     'that they are the same thing.',
     'The premise has appeared in this monograph and its deposits under several names, in several vocabularies, without a section stating '
     'how they stand to one another.',
     'ERRATA :714-:716 (E6-04: the registers stand at four depths, b538, not one premise)', 'restates "one premise in five registers", which E6-04 corrected'),
    ('S03', 1798, 'restatement', 'the restatement clause, under E6-04`s reading',
     'A reader who discharges any one of them discharges all five.',
     'A reader who discharges the second or the fourth discharges the other, both being RH (ch_iff_rh, h2_sign_iff_rh); the first, false as '
     'stated, the third, undecided, and the fifth, whose compiled face holds, are not discharged with them.',
     'ch_iff_rh (v0.1, ζ page node 7); h2_sign_iff_rh (v0.2, ζ page node 8); not_register1 and register5_output_holds (RegisterDepth.lean :60, '
     ':297 at 81ae175 and v0.21, not page nodes); relay data/b538_census.json',
     'restates "one premise in five registers" beside the depths E6-04 wrote: four depths, not one premise'),
    ('S04', 1819, 'ceiling', 'the ceiling clause',
     'This section is that discipline applied to the proof\'s own foundation — and it was produced by the discipline\'s hardest instrument, '
     'the compiler, aimed by the programme at itself.',
     'This section is that discipline applied to the reduction\'s own foundation — and it was produced by the discipline\'s hardest '
     'instrument, the compiler, aimed by the programme at itself.',
     'README :106', '"the proof`s own foundation" names the monograph`s argument a proof of RH'),
]

# ### the history line the history clause places beneath the dated analytic-row note (v5.14 :1500), carrying (R217)(4)`s reading
HIST = {
    1500: ('*v5.15, 2026-10-03, a history line under the analytic-row note of 2026-09-22 above: in the programme’s kernel the two thirds '
           'is the named premise `SimpleProportion` (SIDE-explicit-formula v0.17), not a compiled fact; its theorem stands upstream as '
           '`thmB₀_mult` at `anthropics/formal-math` Zeta23/FinalMult.lean :350 (relay `data/b596_lemmas.txt` :140-:146), and under the '
           'premise `exceptional_mass_le_third` (v0.17) bounds the exceptional mass of a dyadic window by a third plus ε — Conrey’s 40.77% '
           'in the row above and at §21.1 is a proportion read with this note.*'),
}
HIST_CITE = {1500: 'SimpleProportion and exceptional_mass_le_third (v0.17, ζ page nodes 42, 43); ' + UPSTREAM}

# ================================================================================ THE CARRIED SENTENCES OF THE SCOPE WITH A CEILING HIT
# ### (v5.14 line, a fragment of the sentence, the reason it carries)
CARRIES = [
    (1328, 'Conrey (1989) proved', 'a published theorem`s "proved" (Conrey 1989), within the ceiling; the line takes L01`s ruled reading'),
    (1330, 'simplicity is proved for generic curves', 'a published theorem over function fields, within the ceiling'),
    (1335, 'Gallagher and Mueller (1978) proved', 'a published theorem, within the ceiling (a literature report, not a join of the programme`s argument)'),
    (1335, 'Turnage-Butterbaugh (2025) proved', 'a published theorem, within the ceiling'),
    (1502, 'none, alone or together, proves it', 'negated: the sentence says no line proves simplicity'),
    (1504, 'not a proof of it', 'negated: the five lines are evidence, not a proof; the geometric clause STANDS (R217)(4)'),
    (1790, 'Every extended proof carries assumptions', 'a general statement about proofs, naming no object of this monograph'),
    (1794, 'removing it from the proof of `silence_universal`', 'a Lean proof term of a compiled theorem, within the ceiling'),
    (1794, 'Weil\'s 1948 proof runs through', 'Weil`s published proof over function fields, within the ceiling'),
    (1794, 'and the proof closes', 'Weil`s proof over function fields closing, within the ceiling'),
    (1794, 'The season proved positivity is free', 'v5.13`s sentence on the season`s finding (the final compression), naming no RH proof; within the ceiling'),
    (1794, 'is positive and proved', 'the built object`s pairing, a compiled fact of SIDE-global-section; within the ceiling'),
    (1800, 'Li (1997) proved', 'a published theorem (Li 1997), within the ceiling'),
    (1800, 'Oesterlé (unpublished) proved', 'a published result, within the ceiling'),
    (1800, 'Voros (2004–06) proved', 'a published theorem, within the ceiling'),
    (1800, 'against a proved theorem', 'Voros`s published asymptotic, within the ceiling'),
    (1804, 'a theorem awaiting proof', 'a general statement of the axiom journey, within the ceiling'),
    (1813, 'this proof-shape over function fields', 'the function-field proof shape, within the ceiling'),
    (1815, 'nonnegativity proved', 'a compiled fact of SIDE-lv-conservation v0.8.0, within the ceiling'),
    (1815, 'is now itself **proved**', 'a compiled fact of SIDE-lv-conservation v0.10.0 (lowFinset), within the ceiling'),
    (1815, '(v0.9.0) proves that', 'a compiled theorem of SIDE-lv-conservation v0.9.0, within the ceiling'),
    (1819, 'A proof that knows exactly what it assumes', 'a general maxim naming its own limit ("short of the discharge itself"); within the ceiling'),
]

# ### sentences of the scope the ruling names as standing, carried unchanged
STANDS = [
    (1346, 'the perpendicular-crossing theorem STANDS with its pin (R217)(4): its compiled form is spectral_cannon, §25.8 (v5.14 :1669), SIDE-kernel'),
    (1350, 'the perpendicular-crossing sentence (act one`s E5-05), carried: spectral_cannon at §25.8'),
    (1396, 'the geometric clause carried openly (act one`s text), STANDS'),
    (1504, 'the geometric clause`s canonical statement (act one`s E5-06) and "an open premise carried openly", STANDS (R217)(4)'),
    (1817, '"convergent, not independent", carried (R217)(4)'),
]

# ### join-shaped sentences of the scope that carry, each with its reason (reading R-4)
NOT_JOINS = [
    (1335, 'The standard literature goes: PCC → simplicity + RH.', 'a literature report of PCC`s consequences, not a join of the programme`s argument'),
    (1335, 'Montgomery (1973) introduced PCC and showed, assuming RH, that it implies at least two-thirds of zeros are simple.',
     'a published conditional (Montgomery 1973), not a join of the programme`s argument'),
    (1337, 'This direction is new.', 'a statement of the direction`s novelty; it joins nothing; the open reading is J02`s'),
]

# ### the χ-side scan (reading R-9): sentences of the scope that speak of χ, GRH, a Dirichlet character, an L-function or a family
CHI_RE = re.compile(r'χ|GRH|Dirichlet|L-function|\bfamil')

# ### the restatements outside the scope, priced for act three
OUTSIDE = [
    (1304, 'the conditional (simplicity → RH) is proved', 'Part IV`s preamble'),
    (1306, 'We establish it here.', 'Part IV`s preamble'),
    (1308, '**Theorem (ZFC).** If all nontrivial zeros of ξ are simple, then the Riemann Hypothesis holds.', 'Part IV`s preamble'),
    (1310, 'The proof uses the perpendicular crossing theorem', 'Part IV`s preamble'),
    (1464, 'converge on the same conclusion: all zeros of ξ are simple', 'Chapter 24`s opening'),
]

# ================================================================================ THE §24.4 TABLE AGAINST THE SIEVE
TABLE = [
    ('Analytic number theory', ['RH-16'], 'DARK', '1', 'the 0.6725 ceiling'),
    ('Random matrix theory', [], 'DARK', '1', 'the super-repulsion fit (the bench :593)'),
    ('Computation', [], None, None, 'none'),
    ('RH-false witnesses', ['FD-01', 'FD-02'], 'NOT A ROUTE', '—', 'the Epstein witnesses'),
    ('Mechanism enumeration', [], None, None, 'none'),
]
SIEVE_CITE_LINE = 594        # ### the sieve`s own citation into §24.4 (the bench`s 0.6725 ceiling: "A_Place_to_Stand §24.4’s analytic-row note, :1499")


def resolve():
    """### every change`s old wording once on its v5.14 line; every carry`s fragment on its line; returns (rows, problems)."""
    M = lines_of(show(PRE_PP, CUR))
    rows, bad = [], []
    for c in CHANGES:
        cid, n, kind, clause, old, new, cites, why = c
        k = M[n - 1].count(old)
        rows.append(dict(id=cid, line=n, kind=kind, clause=clause, old=old, new=new, cites=cites, why=why, count=k, scope=scope_of(n)))
        if k != 1 or not in_scope(n):
            bad.append((cid, n, k))
    for n, frag, why in CARRIES:
        if frag not in M[n - 1]:
            bad.append(('carry', n, frag))
    for n, frag, why in NOT_JOINS:
        if frag not in M[n - 1]:
            bad.append(('notjoin', n, frag))
    return M, rows, bad


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    M, rows, bad = resolve()
    for r in rows:
        print('%s :%d %s x%d' % (r['id'], r['line'], r['kind'], r['count']))
    print('problems:', bad or 'NONE')
