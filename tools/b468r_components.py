# -*- coding: utf-8 -*-
"""b468r_components.py -- THE TWO COMPONENTS, RUN AFTER THE SEAL (sha256 `bc9142a3c35321c3...`).

### Component 1 reads the two papers at their lines. ### Component 2 reads the Lean at `fbdc36bb` and
### whatever the Lean run left in `b468r_lean_run.txt` / `b468r_print_axioms.txt` -- and ### **IF THE
### RUN DID NOT COMPLETE, `#print axioms` IS REPORTED `NOT RUN` WITH THE STOPPING STEP**, never filled
### from the third party's audit.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
TX = os.path.join(D, 'b468r_text')
Z = os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
CP = os.path.join(TX, 'claude_paper_2026-08-11.txt')
AF = os.path.join(TX, 'alpoge_furman_2608.13637.txt')
ARCH = os.path.join(PP, 'archive', '2026-08-24-ledger-split',
                    'FINDINGS-archive-1-entries-through-2026-08-20c.md')
NL = chr(10)
L = []

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


def at(p, needle):
    for i, l in enumerate(read(p).split(NL)):
        if needle in l:
            return i + 1, re.sub(r'\s+', ' ', l).strip()
    return None, None


def quote(label, p, needle, extra=0, show=260):
    n, t = at(p, needle)
    if n is None:
        rec('    %-34s ### NOT FOUND' % label)
        return None
    ls = read(p).split(NL)
    body = re.sub(r'\s+', ' ', ' '.join(ls[n - 1:n + extra])).strip()
    rec('    %-34s %s:%d' % (label, os.path.basename(p), n))
    rec('      "%s"' % body[:show])
    return dict(file=os.path.basename(p), line=n, text=body)


S = json.load(io.open(os.path.join(D, 'b468r_survey.json'), encoding='utf-8'))


def component1():
    rec('=' * 104)
    rec('COMPONENT 1 -- THE STATEMENT.')
    rec('=' * 104)
    Q = {}
    rec('')
    rec('  ### (1a) THE MAIN THEOREM, BOTH PAPERS, AS EXTRACTED.')
    Q['A_claude'] = quote('Theorem A, Claude paper', CP, 'Theorem A. As T', extra=4)
    Q['A_arxiv'] = quote('Theorem A, arXiv 2608.13637v2', AF, 'Theorem A. As T', extra=4)
    Q['B_claude'] = quote('Theorem B, Claude paper', CP, 'Theorem B. Theorem A holds verbatim', extra=1)
    Q['B_arxiv'] = quote('Theorem B, arXiv 2608.13637v2', AF, 'Theorem B. Theorem A holds verbatim', extra=1)
    rec('    ### ### **DO THEY AGREE? THEOREM A : %s ; THEOREM B : %s**' % (S['thmA_agree'], S['thmB_agree']))
    rec('    ### the survey`s first comparison said Theorem A DISAGREES; that was a page break, printed there.')
    rec('    ### ### **AND WHAT DIFFERS IS THE ATTRIBUTION, NOT THE THEOREM:**')
    quote('the Claude paper`s byline', CP, 'CLAUDE', show=60)
    Q['arxiv_auth'] = quote('the arXiv authorship', AF, 'discovered and written by Claude', show=160)
    rec('')
    rec('  ### (1b) UNCONDITIONAL, AND WHAT IT COUNTS, IN ITS OWN WORDS.')
    Q['uncond'] = quote('unconditional', CP, 'We prove unconditionally that at least two thirds')
    Q['counts'] = quote('what it counts', CP, 'counted with multiplicity, are simple and lie on the critical line')
    rec('    ### ### **IT COUNTS SIMPLE ZEROS ON THE LINE, AGAINST ALL ZEROS COUNTED WITH MULTIPLICITY:**')
    rec('    ### `N0s(T,2T) >= (2/3 - o(1)) N(T,2T)`, and with the Montgomery-Taylor window `0.67250...`.')
    rec('')
    rec('  ### (1c) WHERE THE CONSTANTS COME FROM, IN THE PAPERS` WORDS.')
    Q['const'] = quote('2/3, 5/6, 0.6725', CP, 'constants  3  ,  6  ,  0.6725  are  those', extra=2)
    Q['cmt_opt'] = quote('the window constant is optimal', CP, 'this is optimal [CCLM17', show=200)
    Q['chain'] = quote('the chain that yields 2/3', CP, '(1.2) N0s + o(N )  rank P1', extra=2)
    Q['inputs_an'] = quote('the three cited analytic inputs', CP, 'The analytic inputs are those of Aryan')
    Q['inputs_ar'] = quote('the arithmetic inputs', CP, 'The arithmetic inputs are Weil', extra=4)
    Q['not_used'] = quote('what is not used', CP, 'No mollifier, zero-density estimate')
    rec('    ### ### **2/3 AND 5/6 ARE MONTGOMERY`S AND CONREY-GHOSH-GONEK`S CONSTANTS UNDER RH, AND 0.6725 IS')
    rec('    ### MONTGOMERY-TAYLOR`S; THE PAPER GETS THEM UNCONDITIONALLY FROM `2 - R(window)`, R(indicator)')
    rec('    ### = 4/3 AND R(Montgomery-Taylor) = 1/c_MT** -- the chain (1.2), quoted above.')
    rec('')
    rec('  ### (1d) THE SUPPORT CONDITION AND THE WINDOW.')
    Q['window'] = quote('the window class', CP, 'Fix  an   even  window', extra=0)
    Q['windows26'] = quote('the two windows, (2.6)', CP, '(2.6)', extra=0)
    Q['L'] = quote('L = log(T/2pi)', CP, 'With L := l = log(T /2) and', extra=1)
    Q['supp'] = quote('the test function`s support', CP, 'supp          =    [-  L  ,  L  ]', extra=2)
    Q['bw1'] = quote('bandwidth one', CP, 'information beyond Fourier support 1')
    rec('    ### ### **THE SUPPORT GROWS WITH T: `supp phi = [-L/2, L/2]`, `L = log(T/2pi)` -- FOURIER SUPPORT')
    rec('    ### `[-1, 1]` IN THE SCALED VARIABLE. THE WINDOW IS `Psi in C^2([-1/2, 1/2])`, EVEN, POSITIVE.**')

    # ------------------------------------------------------------------ (a)
    rec('')
    rec('  ### (1e) READ (a) -- THE IMPORT BAR, ALONG BOTH (R76) COORDINATES.')
    rec('  ' + '-' * 100)
    rec('    THE REPRESENTATION COORDINATE.')
    rec('      the class : zeta (Theorem A) and L(s, chi) for any fixed primitive Dirichlet chi (Theorem B).')
    rec('      the corpus`s FIRST object, zeta : ### **INSIDE THE CLASS** -- Theorem A is about zeta itself.')
    rec('      the corpus`s SECOND object, Epstein Z_Q (row F7, no Euler product) : ### **OUTSIDE** --')
    rec('        not zeta and not a Dirichlet L-function. ### Deciding sentence, Theorem B above.')
    rec('    THE TEST-FUNCTION COORDINATE.')
    rec('      ### **THE THEOREM QUANTIFIES OVER NO CLASS OF TEST FUNCTIONS AT ALL.** ### Its test family is')
    rec('      internal to the proof -- modulated copies of a fixed window, at a support `L` that grows')
    rec('      with `T` -- and the conclusion is a count of zeros. ### Deciding sentences, (1d) above.')
    rec('      The corpus`s test functions sit at FIXED widths; the paper states nothing uniform over them.')
    rec('    ### ### **VERDICT (a): `K1 CLASS BOUNDARY` ON THE SECOND OBJECT ONLY. ON THE FIRST OBJECT THE CLASS')
    rec('    ### CONTAINS IT, WHICH IS NOT A BOUNDARY; ON THE TEST-FUNCTION COORDINATE THERE IS NO CLASS TO')
    rec('    ### GRADE -- `NONE`.**')
    rec('    ### ### **AND THE SENTENCE THE PAPER PUTS CLOSEST TO THE SECOND OBJECT IS ABOUT ITS INPUTS, NOT ITS')
    rec('    ### THEOREM:**')
    Q['epstein'] = quote('the inputs and Epstein', CP, 'insensitive to o(N ) off-line zeros', extra=2)
    rec('    ### *"The inputs are ... insensitive to o(N) off-line zeros and hold for Davenport-Heilbronn and')
    rec('    ### Epstein zeta functions"* -- the INPUTS hold for Epstein; the THEOREM is not stated for it.')

    # ------------------------------------------------------------------ (b)
    rec('')
    rec('  ### (1f) READ (b) -- ROW U1, SITE BY SITE, UNDER (R76).')
    rec('  ' + '-' * 100)
    sites = [
        ('(i)', 'class', 'NONE',
         'no statement uniform in the test function; the class of the test family is the proof`s, not the theorem`s'),
        ('(ii)', 'height', 'UNIFORM IN T -- DOES NOT FIRE',
         'the theorem holds for all T >= T0(eps), at the T-dependent support L = log(T/2pi); it is a PROPORTION '
         '(2/3 of zeros), not a statement about each zero; and under (R76) the height is the instrument`s '
         'truncation, which no source fires'),
        ('(iii)', 'width', 'NONE', 'no statement uniform in the test function`s support at fixed width'),
        ('(iv)', 'width', 'NONE', 'the same index, the same absence'),
        ('(v)', 'representation', 'K1 CLASS BOUNDARY',
         'the Dirichlet extension`s class is primitive Dirichlet L-functions (and zeta); Epstein Z_Q has no Euler '
         'product and is in neither; at the paper`s support the second object is outside the class'),
        ('(vi)', 'modulus', 'K1 CLASS BOUNDARY, AND PER-MODULUS',
         'the same class, so the second object is outside it; and within the class the statement is for ANY FIXED '
         'chi -- in the Lean, T0 is chosen after chi -- so it holds at every modulus and not uniformly across '
         'moduli, which is site (vi)`s own shape'),
    ]
    for s, idx, v, why in sites:
        rec('    %-6s %-15s ### **%s**' % (s, idx, v))
        for c in re.findall(r'.{1,92}(?:\s|$)', why):
            rec('        %s' % c.strip())
    Q['fixed_chi'] = quote('Theorem B, fixed chi', CP, 'for any fixed primitive', show=160)
    rec('    ### ### **(R61)/(R76)`S TRIGGER DOES NOT FIRE:** not uniform in the test function over a class')
    rec('    ### containing the corpus`s test functions; not uniform in the representation over a class')
    rec('    ### containing the second object; and the uniformity it does have is in `T`, which (R76) says')
    rec('    ### no source fires.')

    # ------------------------------------------------------------------ (c)
    rec('')
    rec('  ### (1g) READ (c) -- THE CENSUS. ### **DRAFTS, NOT APPLIED; AUTHORING ROUTED.**')
    rec('  ' + '-' * 100)
    n244, cell = at(os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md'),
                    '| Analytic number theory | Mollifiers, mean values |')
    rec('    section 24.4, deposited, :%s' % n244)
    rec('      %s' % cell)
    rec('    ### b466 found that cell counts SIMPLICITY and the banked headline counted THE LINE. ### **THE PAPER')
    rec('    ### NOW SETTLES IT: IT COUNTS SIMPLE ZEROS ON THE LINE, SO IT DOES BEAR ON THAT CELL.**')
    rec('    ### DRAFT 1 -- an era-annotation candidate for section 24.4, NOT APPLIED:')
    rec('      | Analytic number theory | Weil-form rank-trace inequality, non-mollifier (Claude / Anthropic;')
    rec('      |   Alpoge-Furman, arXiv 2608.13637v2) | 2026 | >= 2/3 simple and on the line, unconditional')
    rec('      |   (0.6725 with the Montgomery-Taylor window) |')
    rec('      ### a new row beside the existing one, since the existing row is a tradition`s record and not')
    rec('      ### this method`s; which of row or column is authoring, and is routed.')
    rec('    ### DRAFT 2 -- the intake item owed since 2026-08-20, NOT APPLIED:')
    rec('      the intake held two paper-read flags open: *"no-Euler-clause SUPPORTED (paper-read flag')
    rec('      open); obstructed-limit PARTIAL (paper-read flag open)"* (`2026-08-20-external-intake.md:32`).')
    rec('      candidate: *no-Euler-clause* -- read against the paper`s sentence that its inputs *"hold for')
    rec('      Davenport-Heilbronn and Epstein zeta functions"* (%s:%s); *obstructed-limit* -- read against'
        % (Q['epstein']['file'] if Q['epstein'] else '?', Q['epstein']['line'] if Q['epstein'] else '?'))
    rec('      its ceiling sentence below. ### **THE DRAFT NAMES WHERE EACH FLAG CAN NOW BE READ; IT DOES NOT')
    rec('      CLOSE EITHER FLAG**, which is the intake`s owner`s call.')
    rec('')
    rec('  ### THE PAPER`S OWN CEILING SENTENCE, AND THE CORPUS`S RESIDUE SENTENCE. ### NOTHING BETWEEN THEM.')
    ceil = quote('the paper`s ceiling sentence', CP, 'The    bandwidth-one          ceiling.', extra=2, show=400)
    res = quote('the corpus`s residue sentence', ARCH, '**The chiasmus', show=900)
    rec('    ### the residue sentence`s index line is live at `FINDINGS.md:60`.')
    Q['ceiling'], Q['residue'] = ceil, res
    return Q, sites


def component2():
    rec('')
    rec('=' * 104)
    rec('COMPONENT 2 -- THE LEAN, READ NOT TRUSTED. ### THE KERNEL LANE IS OPEN FOR THIS COMPONENT.')
    rec('=' * 104)
    rec('    clone HEAD : %s ; project zeta23 ; toolchain leanprover/lean4:v4.33.0-rc2' % S['head'])
    rec('    ### **MATHLIB PIN : %s**' % S['mathlib'])
    rec('')
    rec('  ### (2a) THE TRUSTED STATEMENT FILES -- EVERY DECLARATION CARRYING `sorry` OR BEING AN AXIOM.')
    for d_ in S['trusted']:
        rec('    %s:%d  %s %s  hyps: %s' % (d_['file'], d_['line'], d_['kind'], d_['name'],
                                          [h for h, _ in d_['hypotheses']] or 'none'))
    rec('    ### ### **%d DECLARATIONS, EVERY ONE A THEOREM WITH `sorry` AS ITS PROOF; AXIOMS : %d.**'
        % (len(S['trusted']), S['trusted_axioms']))
    rec('    ### The file says why, at its own line 26: *"The `sorry`s below are deliberate (this is the')
    rec('    ### challenge side)"*. ### **THEY ARE THE COMPARATOR`S TARGET STATEMENTS, NOT INPUTS TAKEN ON TRUST:**')
    rec('    ### Solution must prove exactly these types. ### The ONLY hypotheses any carries are')
    rec('    ### %s -- `1 < q` and primitivity of chi on the Dirichlet statements -- ### **AND NEITHER IS AN'
        % S['trusted_hyps'])
    rec('    ### ANALYTIC INPUT.**')
    rec('    ### the full statements are banked verbatim in `b468r_survey.json` under `trusted`.')
    rec('')
    rec('  ### (2b) WHERE THE ANALYTIC INPUTS WENT -- THE UNTRUSTED LIBRARY, READ.')
    rec('    `Zeta23/Hypotheses.lean` names the paper`s inputs as fields of `PaperInputs` (explicit formula,')
    rec('    Riemann-von Mangoldt, Chebyshev-Mertens, Montgomery-Vaughan, Gamma facts), and')
    rec('    `Zeta23/Final.lean` DISCHARGES THEM FOR ZETA: `theorem paperInputs_zeta : PaperInputs')
    rec('    zetaZeroConfig := PaperInputs.of_EF zetaEF`, with `zetaEF` proved from Mathlib`s functional')
    rec('    equation. ### Axiom declarations anywhere in the project, comments stripped : %d.'
        % len(S.get('axiom_declarations', [])))
    rec('')
    rec('  ### (2c) `#print axioms`, RUN -- OR NOT, WITH THE REASON.')
    run = read(os.path.join(D, 'b468r_lean_run.txt'))
    pa = read(os.path.join(D, 'b468r_print_axioms.txt'))
    complete = '### RUN COMPLETE' in run
    stopped = re.findall(r'### RUN STOPPED AT: (.*)', run)
    lines_pa = [l for l in pa.split(NL) if 'depends on axioms' in l or 'does not depend' in l]
    std = '[propext, Classical.choice, Quot.sound]'
    if complete and lines_pa:
        rec('    ### ### **RUN. %d LINES PRINTED:**' % len(lines_pa))
        for l in lines_pa:
            rec('      %s' % l.strip())
        clean = all(std in l for l in lines_pa)
        rec('    ### ### **EVERY LINE READS EXACTLY THE THREE STANDARD AXIOMS : %s**' % clean)
        head = [l for l in lines_pa if "'two_thirds_simple_on_critical_line'" in l]
        rec('    ### the paper`s Theorem A(i) -- simple on the line -- is Lean`s `two_thirds_simple_on_critical_line`:')
        rec('      %s' % (head[0].strip() if head else '### NOT PRINTED'))
        status = 'RUN'
    else:
        clean = None
        status = 'NOT RUN'
        rec('    ### ### **`#print axioms` : NOT RUN.** ### stopped at : %s' % (stopped or ['(the run did not finish)']))
        crashed = sorted(set(re.findall(r'Building (\S+)', ' '.join(l for l in run.split(NL) if '✖' in l))))
        rec('    ### ### **HOW IT STOPPED, READ FROM THE COMPLETE LOG:** the harness reported the background task')
        rec('    ### stopped for low system memory; the build itself carried on and ended `error: build failed`,')
        rec('    ### with %d module builds crashing on Windows status 3221225794 (0xC0000142, a process that could'
            % len(crashed))
        rec('    ### not initialise); the script then stopped at that step by its own rule, before `#print axioms`.')
        rec('    ### crashed : %s' % ' '.join(crashed))
        tail = [l for l in run.split(NL) if l.strip()][-8:]
        for l in tail:
            rec('      | %s' % l[:150])
        rec('    ### The third party`s audit prints three-axiom lines for its statements, and it is quoted')
        rec('    ### ONLY AS ITS CLAIM: the survey found `AUDIT.md` names %d statements not in this tree.'
            % len(S['audit_absent']))
    rec('')
    rec('  ### (2d) THE GRADE, IN THE CORPUS`S VOCABULARY.')
    if status == 'RUN' and clean:
        grade = 'DERIVES'
        rec('    ### ### **`DERIVES`.** ### The trusted files carry no analytic input, and the untrusted proofs')
        rec('    ### close them on the three standard axioms, as run here.')
    elif status == 'RUN':
        grade = 'NOT CLEAN'
        rec('    ### ### **NOT GRADED `DERIVES`: SOME LINE PRINTS AN AXIOM BEYOND THE STANDARD THREE.**')
    else:
        grade = 'DERIVES, CONDITIONAL ON AN UNRUN #print axioms'
        rec('    ### ### **`DERIVES` BY THE ORDER`S RULE ON THE TRUSTED FILES -- AND CONDITIONAL, SAID IN THE SAME')
        rec('    ### BREATH, ON A `#print axioms` THIS ACT DID NOT RUN.** ### Nothing stronger is claimed.')
    rec('')
    rec('  ### (2e) THE ONE COMPARISON.')
    rec('    the deposit`s pending input, lv v0.10.0 at 93c27ec, second conjunct of ExplicitFormulaDecomp:')
    rec('      %s' % S['lv_conjunct'])
    n, t = at(os.path.join(Z, 'Zeta23', 'Hypotheses.lean'), 'def ExplicitFormulaPaper (Z : ZeroConfig) : Prop :=')
    rec('    zeta23`s explicit formula, `Zeta23/Hypotheses.lean:%s`, proved for zeta via `zetaEF`:' % n)
    for l in read(os.path.join(Z, 'Zeta23', 'Hypotheses.lean')).split(NL)[n - 1:n + 6]:
        rec('      %s' % l.rstrip())
    rec('    ### ### **VERDICT : `DOES NOT`.** ### zeta23`s explicit formula is Weil`s Hermitian form for test')
    rec('    ### functions `C^2` with `tsupport` in `[-L/2, L/2]`, summed over ALL zeros. ### The deposit`s')
    rec('    ### conjunct is a Li-coefficient splitting at a height `T`, whose test functions `1 - (1 - 1/s)^n`')
    rec('    ### have no compact support -- b400 recorded the Li family outside every compactly supported')
    rec('    ### class -- so no specialization of zeta23`s statement reaches it; and no Li-shaped declaration')
    rec('    ### exists in the library (%d hits). ### **`W-ORD-GW-IMPORT` IS NOT FILED. NOTHING IS IMPORTED.**'
        % S['li_hits'])
    return dict(status=status, clean=clean, grade=grade, lines=lines_pa, stopped=stopped,
                comparison='DOES NOT', worder=False)


def main():
    Q, sites = component1()
    C2 = component2()
    rec('')
    rec('=' * 104)
    rec('THE EXPECTATIONS, SCORED.')
    rec('=' * 104)
    sc = {}
    sc['N1'] = dict(navigator='the two statements agree and the theorem counts simple zeros on the line, unconditionally',
                    verdict='HELD' if S['thmA_agree'] and S['thmB_agree'] else 'REFUTED',
                    note='both theorems agree; N0s -- simple on the line; "We prove unconditionally"'
                         + ('' if C2['status'] == 'RUN' and C2['clean'] else
                            '; the Lean check of "unconditionally" is %s' % C2['status']))
    sc['N2'] = dict(navigator="K1 at every site; the support restriction excludes the corpus's objects; (R61)'s trigger does not fire",
                    verdict='REFUTED ON ITS FIRST CLAUSE, HELD ON ITS LAST',
                    note='K1 at sites (v) and (vi) only; NONE at (i), (iii), (iv) where no uniform statement exists; '
                         'at (ii) uniform in T, which (R76) says fires nothing; zeta, the first object, is INSIDE the '
                         'class -- and the trigger does not fire')
    sc['N3'] = dict(navigator='the trusted statement files carry the pair-correlation input as a hypothesis, so INTERFACES; comparison DOES NOT',
                    verdict='REFUTED ON THE FIRST TWO CLAUSES, HELD ON THE THIRD',
                    note='the trusted files carry no analytic hypothesis (only 1 < q and primitivity); the grade is %s; '
                         'the comparison is DOES NOT' % C2['grade'])
    sc['seat'] = dict(N1='HELD on all three clauses, as the face said',
                      N2='as the face predicted: first clause REFUTED, last HELD, K1 at (v) -- and at (vi), which the face did not name',
                      N3='as the face predicted: first two REFUTED, DOES NOT HELD; the grade %s' % C2['grade'])
    for k in ('N1', 'N2', 'N3'):
        rec('  (%s) %s' % (k, sc[k]['navigator']))
        rec('       ### ### **%s**' % sc[k]['verdict'])
        rec('       %s' % sc[k]['note'])
    rec('  ### THE SEAT`S OWN, FROM THE FACE:')
    for k in ('N1', 'N2', 'N3'):
        rec('    (%s) %s' % (k, sc['seat'][k]))
    rec('')
    rec('  ### ### **NO BRIDGE TYPED. NO SITE ENTERED. ROW U1 UNEDITED. NO DRAFT APPLIED. NOTHING IMPORTED.')
    rec('  ### ### NO LEAN OF THE CORPUS TOUCHED. `h2` WHERE THE DEPOSIT LEFT IT.**')
    io.open(os.path.join(D, 'b468r_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(quotes=Q, sites=[dict(site=a, index=b, verdict=c, why=d) for a, b, c, d in sites]),
              io.open(os.path.join(D, 'b468r_readings.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    json.dump(C2, io.open(os.path.join(D, 'b468r_lean.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    json.dump(sc, io.open(os.path.join(D, 'b468r_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
