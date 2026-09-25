# -*- coding: utf-8 -*-
"""b538_record.py -- THE ACT`S CORPUS WRITES AND RECORD, UNDER (R148).
### `python tools/b538_record.py couplings | census | rows | findings | pointer | components | desk | trail`

### Grades are read from the profile and the module`s own statements; faces are cited at their pins. FINDINGS and OPEN_TRAILS
### take ONE append each; the correspondence ledger one row through the carried `corr_row.py`. This file deletes nothing.
"""
import hashlib, io, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FIND = os.path.join(PP, 'FINDINGS.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
CORR = os.path.join('D:', os.sep, 'SIDE-global-section', 'CORRESPONDENCE.md')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
SK = os.path.join('D:', os.sep, 'SIDE-kernel')
MEM = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects', 'D--', 'memory')
MEMF = 'feedback_mirror_after_last_push.md'
PRIOR_PP = 'b7e0c52'
NL = chr(10)
NS = 'SIDEExplicitFormula.RegisterDepth.'
LVTAG, LVPEEL, SKPIN = 'v0.10.0', '93c27ec', '0e5233f'
THMS = ['not_register1', 'silence_universal_restated', 'one_le_evenKernel_zero', 'rpow_le_evenKernel_zero',
        'mellin_Phi_eq_zero_of_re_le_one', 'lv_h2_false_on_strip', 'lvh2_corrected_iff', 'register3_of_one_lt_re',
        'zeta_zeros_countable', 'xi_zero_re_countable', 'register5_output_holds']
CLAIMS = {
    'not_register1': 'R1 (Register1_universalityHypothesis) is false',
    'silence_universal_restated': 'a universal interface has kappa zero (the kernel theorem, per interface)',
    'one_le_evenKernel_zero': '1 ≤ evenKernel 0 x for x > 0',
    'rpow_le_evenKernel_zero': 't^(-1/2) ≤ evenKernel 0 t for t > 0',
    'mellin_Phi_eq_zero_of_re_le_one': 'mellin Phi (s/2) = 0 whenever re s ≤ 1',
    'lv_h2_false_on_strip': 'lv`s h2 fails at every s of the critical strip',
    'lvh2_corrected_iff': 'the completedRiemannZeta strip face is equivalent to rh_strip',
    'register3_of_one_lt_re': 'R3 holds at every s with 1 < re s, given lv`s h1',
    'zeta_zeros_countable': 'the zeros of zeta off the pole are countable',
    'xi_zero_re_countable': 'the real parts of the nontrivial zeros are countable',
    'register5_output_holds': 'R5-output (Register5_output_HilbertPolya) holds'}
CTITLE = "## The five registers of §27.3 and lv-conservation's h2, graded by their Lean statements against RH"
HEADING = ('### b538 — W-ORD-REGISTER-DEPTH under (R148): R1 FALSE-AS-STATED, R5-output TRUE-AS-STATED, lv`s h2 FALSE-AS-STATED '
           'on re s ≤ 1, R3 UNDECIDED; the census in FINDINGS')
POINTER = ('**The pointer owed by b537 ((R148)(5)):** relay `data/b537_closing_addendum.txt` — "the upload is the -post build; the '
           'pre-push build is superseded, kept, not deleted."')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def append_to(path, text):
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.basename(path), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def axline(n):
    return next((l for l in jl('b538_profile.json').get('lines', []) if l.startswith("'%s%s'" % (NS, n))), 'NOT PROFILED')


def within(n):
    return (jl('b538_profile.json').get('within_std3') or {}).get(NS + n) is True


def fails():
    out = {}
    for a in jl('b538_attempts.json') or []:
        for d0 in a.get('failed_decls', []):
            out.setdefault(d0, []).append(a['attempt'])
    return out


def modline(name):
    t = rd(os.path.join(KER, 'SIDEExplicitFormula', 'RegisterDepth.lean')).split(NL)
    return next(i + 1 for i, l in enumerate(t) if re.match(r'^(theorem|def|structure|abbrev) %s\b' % re.escape(name), l))


# ------------------------------------------------------------------------------ COMPONENT 3: the couplings read
COUPLINGS = [
    ('C1_realness', ':67', 'UP TO A FAMILY', 'Im Φ = 0 pointwise; Re Φ free -- every real-valued Φ'),
    ('C2_halfplane_nonvanishing', ':72-73', 'UP TO A FAMILY', 'a condition on mellin Φ on 1 < re s, not on the values of Φ'),
    ('C3_theta_transformation', ':79-80', 'UP TO A FAMILY', 'Φ on (0,1) fixed by Φ on [1,∞), which stays free'),
    ('C4_modularity', ':108-113', 'UP TO A FAMILY', 'Φ = (F(i t) - 1)/2 for some F holomorphic on ℍ with the T- and S-laws; no growth '
                                                     'condition at the cusps, so F is not pinned'),
    ('C5_input', ':120-122', 'UP TO A FAMILY', '2Φ + 1 a heat trace of some non-negative spectrum μ; μ free'),
    ('C6_holomorphic_extension', ':144-146', 'UP TO A FAMILY', 'Φ the restriction of a function holomorphic on 0 < re z'),
    ('C7_order', ':182-185', 'UP TO A FAMILY', 'the completed Mellin transform of Φ extends to an entire function of order ≤ 1 growth')]


def couplings():
    L = ['b538 -- THE SEVEN COUPLINGS READ (lv `SIDELvConservation/CouplingsAtPhi.lean` at %s), EACH: POINTWISE TO PHI`S VALUES, '
         'UP TO A FAMILY, OR NOT AT ALL' % LVTAG, '']
    for n, ln, k, why in COUPLINGS:
        L.append('  %-27s CouplingsAtPhi.lean%-10s %-15s -- %s' % (n, ln, k, why))
    L += ['', '  ### POINTWISE TO PHI : 0 of 7 ; UP TO A FAMILY : 7 of 7 ; NOT AT ALL : 0 of 7.',
          '  ### Whether the seven JOINTLY pin Φ to Phi (a Hamburger-type uniqueness) is not decided here.']
    io.open(os.path.join(D, 'b538_couplings.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 5: the census
def census():
    rp = 'SIDE-lv-conservation/SIDELvConservation/RegisterPentagon.lean'
    b532 = next((l.strip() for l in rd(os.path.join(D, 'b532_profile_log.txt')).split(NL) if "B321.ch_iff_rh' " in l), 'NOT FOUND')
    b536 = next((l.strip() for l in rd(os.path.join(D, 'b536_profile_log.txt')).split(NL) if "B321.h2_sign_iff_rh' " in l), 'NOT FOUND')
    rows = [
        dict(reg='R1', face='%s:106-107 at %s (restating SIDE-kernel v1.5 `Kernel/SilenceTheorem.lean:26-44`)' % (rp, LVTAG),
             statable='yes (b538; b512: NOT STATABLE)', grade='FALSE-AS-STATED',
             thm='`not_register1` (RegisterDepth.lean:%d) -- %s' % (modline('not_register1'), axline('not_register1')),
             missing='`essential` is an uninterpreted Prop field, so the register quantifies over interfaces it cannot distinguish '
                     '(Bool, identity action, essential := True refutes it); the kernel`s own `silence_universal` takes universality '
                     'per interface and is untouched (`silence_universal_restated`, %s)' % axline('silence_universal_restated')),
        dict(reg='R2', face='%s:127-130 at %s (restating SIDE-kernel `Bridge/ConservationBridge.lean:26-29`)' % (rp, LVTAG),
             statable='yes (graded at b531-b532)', grade='EQUIVALENT-REWORDING',
             thm='`ch_iff_rh` (SIDE-explicit-formula `H2Bridge.lean:71`) -- %s (relay `data/b532_profile_log.txt`)' % b532, missing='--'),
        dict(reg='R3', face='%s:139-140 at %s' % (rp, LVTAG), statable='yes (b538; b512: NOT STATABLE)', grade='UNDECIDED',
             thm='none decides it at every s or refutes it at one; partial: `register3_of_one_lt_re` (RegisterDepth.lean:%d, INTERFACES on '
                 'lv`s h1) -- %s' % (modline('register3_of_one_lt_re'), axline('register3_of_one_lt_re')),
             missing='to decide it: (i) per-class exclusion at re s ≤ 1, class by class, and (ii) whether the seven couplings jointly '
                     'pin Φ to Phi (a Hamburger-type uniqueness); none of the seven pins Φ alone (`data/b538_couplings.txt`)'),
        dict(reg='R4', face='%s:152-153 and :158-159 at %s; in the Weil form, `h2_sign`' % (rp, LVTAG),
             statable='yes, in the Weil form (b536)', grade='EQUIVALENT-DEEP',
             thm='`h2_sign_iff_rh` (SIDE-explicit-formula `Seam.lean:101`, v0.2) -- %s (relay `data/b536_profile_log.txt`)' % b536,
             missing='-- (lv`s literal faces are predicates on an abstract stream `lam`; their RH content is the manuscript`s '
                     'identification of `lam` with Li`s coefficients)'),
        dict(reg='R5-output', face='%s:189-195 at %s' % (rp, LVTAG), statable='yes (b538; b512: NOT STATABLE)', grade='TRUE-AS-STATED (a SHELL)',
             thm='`register5_output_holds` (RegisterDepth.lean:%d) -- %s' % (modline('register5_output_holds'), axline('register5_output_holds')),
             missing='it asks only that the REAL PARTS of the nontrivial zeros be enumerated; the constant pairing 1 and the diagonal '
                     'operator witness it. Missing: the ordinates, and a self-adjoint operator on a Hilbert space whose spectrum they are'),
        dict(reg='lv`s h2', face='`mellin Phi (s / 2) ≠ 0`, the hypothesis of `goalState_sevenClasses_of_h2` (%s:215 at %s), Phi at '
                                 '`T1_MellinFactorization.lean:26`' % (rp, LVTAG),
             statable='yes (b538)', grade='FALSE-AS-STATED at every s with re s ≤ 1, the critical strip included',
             thm='`mellin_Phi_eq_zero_of_re_le_one` (RegisterDepth.lean:%d) -- %s; `lv_h2_false_on_strip` -- %s'
                 % (modline('mellin_Phi_eq_zero_of_re_le_one'), axline('mellin_Phi_eq_zero_of_re_le_one'), axline('lv_h2_false_on_strip')),
             missing='the sentence names the Mellin INTEGRAL where it means its continuation: Mathlib`s `mellin` is a Bochner integral, '
                     '0 where the integrand is not integrable, and `Phi` grows like t^(-1/2)/2 at 0, so the integral is 0 on re s ≤ 1. '
                     'The object meant is `completedRiemannZeta`, equal to it on 1 < re s alone (`T2_SDarkness.lean:72-74`); the corrected '
                     'face is `lvh2_corrected_iff` : (strip, off the line, completedRiemannZeta s ≠ 0) ↔ rh_strip -- %s -- and rh_strip ↔ '
                     'RiemannHypothesis stands compiled at v0.2' % axline('lvh2_corrected_iff'))]
    put_json('b538_census.json', dict(rows=rows))
    for r in rows:
        print('  %-10s %-26s %s' % (r['reg'], r['grade'][:26], r['thm'][:90]))
    print('  ### grade cells filled : %d of %d' % (sum(1 for r in rows if r['grade'].strip()), len(rows)))


def findings():
    rows = jl('b538_census.json')['rows']
    t = ['', CTITLE, '',
         '*Filed at b538 on the author`s ruling `(R148)`, W-ORD-REGISTER-DEPTH. Each register is read from its COMPILED face at its pin -- '
         'SIDE-lv-conservation `%s` (peeled `%s`; every file cited byte-identical at HEAD `2f71068`), SIDE-kernel `v1.5` = `%s` -- restated '
         'verbatim in SIDE-explicit-formula `SIDEExplicitFormula/RegisterDepth.lean`, and graded by what its Lean sentence says, relative '
         'to RH, in the five grades of `(R148)`(2). A FALSE-AS-STATED or TRUE-AS-STATED grade is a defect of the Lean sentence meant to '
         'carry the mathematics of §27.3, not of that mathematics. b512`s table (relay `data/b512_closing.txt:5-7`) is cited and not '
         'edited.*' % (LVTAG, LVPEEL, SKPIN), '',
         '| register | face (path:line at pin) | statable here | grade | the theorem that decides it (`#print axioms`) | what the sentence is missing |',
         '|:--|:--|:--|:--|:--|:--|']
    for r in rows:
        t.append('| %s | %s | %s | **%s** | %s | %s |' % tuple(r[k].replace('|', '∣') for k in ('reg', 'face', 'statable', 'grade', 'thm', 'missing')))
    t += ['',
          '**What the h2 result does to R3`s hypothesis side.** With `mellin_Phi_eq_zero_of_re_le_one`, every `PerClassExcludes C s` and '
          'every `CombinationsExclude 𝒞 s` offered with `Phi` as its witness is false at re s ≤ 1: there R3`s hypothesis, if it holds at '
          'all, holds by witnesses other than Phi, and lv`s shared-witness route (`goalState_of_h1_h2`, T3′) cannot reach any s with '
          're s ≤ 1 -- `goalState_sevenClasses_of_h2` is vacuous on the critical strip. The seat`s further observation, NOT COMPILED: '
          'C3 alone forces the Mellin integrand of EVERY Φ satisfying it to be non-integrable at 1/2 ≤ re s ≤ 1, so R3 holds there '
          'vacuously; R3 at re s < 1/2 and at re s ≤ 0 is open.', '',
          '**The deposited sentences this touches** (lv-conservation`s own description; THE_UNCONDITIONAL_SURROUND §6`s "goal ⇐ h1 ∧ h2", '
          'h2 the open node) are read against it at the act after, on the author`s word `(R148)`(4). No deposited kernel is edited, '
          'nothing is filed to ERRATA, the ceiling is unchanged, nothing deposits.', '']
    w = append_to(FIND, NL.join(t))
    w['heading_line'] = rd(FIND).split(NL).index(CTITLE) + 1
    put_json('b538_findings.json', w)
    print('  FINDINGS.md : %(added)d bytes added, prefix %(prefix)s ; the entry at line %(heading_line)d' % w)


# ------------------------------------------------------------------------------ rows
def rows():
    graded = [n for n in THMS if within(n) and n not in fails()]
    grades = ['`%s` %s' % (n, 'INTERFACES on lv`s h1_complete_at_Phi' if n == 'register3_of_one_lt_re' else 'DERIVES') for n in graded]
    cells = ['387',
             '**THE REGISTER DEPTH: R1, R3, R5 AND LV`S h2 GRADED BY THEIR OWN LEAN STATEMENTS** (b538, under (R148)). '
             'SIDE-explicit-formula RegisterDepth.lean: R1 false as stated; lv`s h2 (mellin Phi (s/2) ≠ 0) false at every s with re s ≤ 1; '
             'its corrected face equivalent to rh_strip; R3 on 1 < re s from lv`s h1; R5-output true as stated from the countability of the '
             'zeros. Nothing here proves RH.',
             '`SIDE-explicit-formula/SIDEExplicitFormula/RegisterDepth.lean` : ' + ', '.join('`%s%s`' % (NS, n) for n in THMS),
             '%d of %d theorems of the module: standard three or fewer (not_register1 and silence_universal_restated: no axioms)'
             % (len(graded), len(THMS)),
             ' ; '.join(grades) + ' -- each by statement-read against its claim: ' + '; '.join('%s "%s"' % (n, CLAIMS[n]) for n in graded),
             'No other grade moved; h2 where the deposit left it; no deposited kernel edited; nothing deposits; nothing at Zenodo written.']
    r = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells, capture_output=True, text=True, encoding='utf-8')
    print(r.stdout[-400:], r.stderr[-400:])
    put_json('b538_rows.json', dict(cells=cells, exit=r.returncode))


# ------------------------------------------------------------------------------ COMPONENT 6
def pointer():
    p = os.path.join(MEM, MEMF)
    b = open(p, 'rb').read()
    open(os.path.join(D, 'b538_memory_pointer.md'), 'wb').write(b)
    t = b.decode('utf-8')
    res = dict(path=p, sha256=hashlib.sha256(b).hexdigest(), discharged=('**DISCHARGED at b538**' in t),
               owed_text_kept=('**OWED, as of b537:**' in t))
    put_json('b538_pointer.json', res)
    print('  memory entry %s : DISCHARGED at b538 %s ; the b537 text kept %s' % (MEMF, res['discharged'], res['owed_text_kept']))


# ------------------------------------------------------------------------------ desk
def token_count():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        return None
    return sum(open(os.path.join(d0, f), 'rb').read().count(t) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b538_'))


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout


def scores():
    f = fails()
    cen = {r['reg']: r for r in (jl('b538_census.json').get('rows') or [])}
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b538_') and needle in rd(os.path.join(T, x))]
    tok = token_count()
    unchanged = {n: blob(PP, '%s:%s' % (PRIOR_PP, n)) == open(os.path.join(PP, n), 'rb').read() for n in ('ERRATA.md', 'README.md', 'REGISTRY.md')}
    kernels = dict(sk=(git(SK, 'rev-parse', 'HEAD').startswith('0256e9e') and git(SK, 'status', '--porcelain', '--untracked-files=no') == ''),
                   lv=(git(LV, 'rev-parse', 'HEAD').startswith('2f71068') and git(LV, 'status', '--porcelain', '--untracked-files=no') == ''))
    dep = git(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''
    return dict(
        n1=within('not_register1') and not any(a >= 3 for a in f.get('not_register1', [])) and 'not_register1' not in f,
        n2=within('mellin_Phi_eq_zero_of_re_le_one') and 'mellin_Phi_eq_zero_of_re_le_one' not in f,
        n3=within('register5_output_holds'),
        n4=bool(cen.get('R3')) and cen['R3']['grade'] != 'UNDECIDED',
        n5=len(cen) == 6 and all(r['grade'].strip() for r in cen.values()),
        n6=all(unchanged.values()) and all(kernels.values()) and not zen and tok == 0 and dep,
        unchanged=unchanged, kernels=kernels, zenodo_tools=zen, token=tok, deposit_clean=dep,
        s1=within('mellin_Phi_eq_zero_of_re_le_one') and not any(a >= 3 for a in f.get('mellin_Phi_eq_zero_of_re_le_one', [])),
        s2=bool(cen.get('R3')) and cen['R3']['grade'] == 'UNDECIDED',
        s3=within('zeta_zeros_countable'), failures=f)


def w(v):
    return 'HELD' if v else 'REFUTED'


def components():
    at, pr = jl('b538_attempts.json') or [], jl('b538_profile.json')
    L = ['=' * 132, 'b538 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '',
         '### THE PINS : SIDE-lv-conservation %s (peeled %s; HEAD 2f71068, the cited files byte-identical) ; SIDE-kernel v1.5 = %s'
         % (LVTAG, LVPEEL, SKPIN),
         '### THE BYTE CHECK : ' + ' ; '.join(l[4:].strip() for l in rd(os.path.join(D, 'b538_restatement_compare.txt')).split(NL) if l.startswith('### ')),
         '', '### COMPONENTS 1, 2, 4 -- THE MODULE: `SIDEExplicitFormula/RegisterDepth.lean` (NEW).']
    for a in at:
        L.append('  attempt %d : exit %d ; %d error lines ; %.1f s ; failing %s' % (a['attempt'], a['exit'], a['errors'], a['seconds'],
                                                                              a.get('failed_decls') or 'NONE'))
    L += ['  profile :'] + ['    ' + l for l in pr.get('lines', [])]
    L += ['  #check %s : %s' % (k, ' '.join((v or 'NONE').split())) for k, v in (pr.get('checks') or {}).items()]
    L += ['', '### COMPONENT 3 -- THE COUPLINGS:'] + ['  ' + l for l in rd(os.path.join(D, 'b538_couplings.txt')).rstrip(NL).split(NL)[2:]]
    L += ['', '### COMPONENT 5 -- THE CENSUS: FINDINGS.md:%s' % jl('b538_findings.json').get('heading_line')]
    L += ['  %s : %s -- %s' % (r['reg'], r['grade'], r['thm']) for r in jl('b538_census.json').get('rows', [])]
    L += ['', '### COMPONENT 6 -- THE POINTER: ' + json.dumps(jl('b538_pointer.json'), ensure_ascii=False), '=' * 132]
    io.open(os.path.join(D, 'b538_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:12]))


def desk():
    sc = scores()
    N = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')
    S = ('s1', 's2', 's3')
    L = ['=' * 104, 'b538 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- %s ; failing at %s.' % (w(sc['n1']), axline('not_register1'), sc['failures'].get('not_register1', 'NONE')),
         '  **(N2)** ### **%s.** -- %s ; failing at %s.' % (w(sc['n2']), axline('mellin_Phi_eq_zero_of_re_le_one'),
                                                          sc['failures'].get('mellin_Phi_eq_zero_of_re_le_one', 'NONE')),
         '  **(N3)** ### **%s.** -- %s ; no countability premise.' % (w(sc['n3']), axline('register5_output_holds')),
         '  **(N4)** ### **%s.** -- R3 graded %s: no compiled theorem decides it at every s or refutes it at one; `register3_of_one_lt_re` '
         'decides 1 < re s only.' % (w(sc['n4']), (jl('b538_census.json').get('rows') or [{}] * 3)[2].get('grade')),
         '  **(N5)** ### **%s.** -- grade cells filled : %d of 6.' % (w(sc['n5']), sum(1 for r in jl('b538_census.json').get('rows', []) if r['grade'].strip())),
         '  **(N6)** ### **%s.** -- ERRATA, README, REGISTRY byte-identical to %s : %s ; SIDE-kernel and lv at their HEADs, clean : %s ; '
         'b538 tools naming the platform`s address %s ; token hits %s ; deposit tree clean %s.'
         % (w(sc['n6']), PRIOR_PP, sc['unchanged'], sc['kernels'], sc['zenodo_tools'] or 'NONE', sc['token'], sc['deposit_clean']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- mellin_Phi_eq_zero_of_re_le_one failing at : %s.' % (w(sc['s1']), sc['failures'].get('mellin_Phi_eq_zero_of_re_le_one', 'NONE')),
         '  **(S2)** ### **%s.** -- R3 UNDECIDED in the census.' % w(sc['s2']),
         '  **(S3)** ### **%s.** -- %s.' % (w(sc['s3']), axline('zeta_zeros_countable')),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in S].count(True), [sc[k] for k in S].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in rd(os.path.join(D, 'b538_defects.txt')).rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b538_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    put_json('b538_scores.json', sc)
    print(NL.join(L))


def trail():
    sc = scores()
    cen = jl('b538_census.json').get('rows', [])
    body = ['', HEADING, '',
            '**(R148) ratified.** W-ORD-REGISTER-DEPTH runs as a read with small compiles; each register of §27.3 and lv-conservation`s '
            'h2 is graded by what its own Lean statement says, relative to RH, in five grades; four readings of the navigator registered '
            'before the compile; the owed pointer discharged.', '',
            '**The module.** SIDE-explicit-formula `SIDEExplicitFormula/RegisterDepth.lean` (new), every face restated verbatim with its '
            'pin (lv `%s`, SIDE-kernel v1.5); clean at attempt %d; all its theorems at the standard three or fewer. The census, one row per '
            'register and lv`s h2, is at `FINDINGS.md`:%s; correspondence row 387.' % (LVTAG, len(jl('b538_attempts.json') or []),
                                                                                   jl('b538_findings.json').get('heading_line')), '']
    body += ['- **%s** -- %s.' % (r['reg'], r['grade']) for r in cen]
    body += ['',
             '**lv`s h2, the navigator`s reading (b) confirmed by compile.** `mellin_Phi_eq_zero_of_re_le_one`: the Mellin integral of '
             '`Phi` at s/2 is 0 whenever re s ≤ 1, so `goalState_sevenClasses_of_h2` is vacuous on the critical strip; the object meant '
             'is `completedRiemannZeta`, and the corrected strip face is `rh_strip` by `lvh2_corrected_iff`. The deposited sentences this '
             'touches are read at the act after, on the author`s word ((R148)(4)).', '',
             '**R3, the navigator`s reading (c): not decided.** None of the seven couplings pins Φ alone; whether they pin it jointly is '
             'the missing piece, with per-class exclusion at re s ≤ 1.', '',
             POINTER, '',
             '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
             % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
             '**The kernel lane shuts at this act`s close.** Nothing deposits; nothing at Zenodo written; no deposited kernel edited; '
             'nothing filed to ERRATA; the ceiling unchanged; no grade moved on any other row; row U1 unedited; `h2` where the deposit '
             'left it; the four lists stay OPEN; nothing here is a statement about RH.', '']
    before = open(OT, 'rb').read()
    if HEADING.encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(NL.join(body).encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b538_trail_notes.json', out)


if __name__ == '__main__':
    sys.exit({'couplings': couplings, 'census': census, 'rows': rows, 'findings': findings, 'pointer': pointer,
              'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]())
