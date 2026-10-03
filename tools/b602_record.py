# -*- coding: utf-8 -*-
"""b602_record.py -- THE ACT'S RECORD TOOL, UNDER (R212). ### ONE SUBCOMMAND PER BANK.

### ### b602: LANE THREE, ACT TWENTY-NINE -- THE AUDIT FILE REPAIRED AT v0.19.1; THE SIGN OF λ_1 AT T0; (E3)'S COMPILED WINDOW AT
### DETECTION-REGION. Subcommands write only `data/b602_*` unless the docstring names another file. Every bank is written through
### `put_txt` / `put_json` (encode, temp file, `os.replace`). No platform call. The template is b601_record.py.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
LVK = 'D:/SIDE-lv-conservation'
MLK = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
PRE_PP = 'ca841ca'
PRE_RELAY = '97485547'
PRE_KER = '5fc0c87'
STEPZERO = '7a60bad2'
TAG = 'v0.20'
POINT = 'v0.19.1'
BRANCH = 'sign-window-b602'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/5dce8424-ec16-4701-8f42-69078426fd40/scratchpad'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/5dce8424-ec16-4701-8f42-69078426fd40.jsonl'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
AUDIT = 'AxiomCheckKeiper.lean'
KFILES = dict(sign='SIDEExplicitFormula/KeiperSign.lean', ssign='SIDEExplicitFormula/SaltCheckKeiperSign.lean',
              win='SIDEExplicitFormula/Schema/PlateauRamp.lean', swin='SIDEExplicitFormula/Schema/SaltCheckPlateauRamp.lean')
KNS = dict(sign='SIDEExplicitFormula.KeiperSign.', ssign='SIDEExplicitFormula.KeiperSign.SaltCheck.',
           win='SIDEExplicitFormula.Schema.PlateauRamp.', swin='SIDEExplicitFormula.Schema.PlateauRamp.SaltCheck.')
AXF = dict(sign='AxiomCheckKeiperSign.lean', win='AxiomCheckPlateauRamp.lean')
AX_KEYS = dict(sign=('sign', 'ssign'), win=('win', 'swin'))
OWN = ('AxiomCheckKeiperSign.lean', 'AxiomCheckPlateauRamp.lean', 'SIDEExplicitFormula/KeiperSign.lean',
       'SIDEExplicitFormula/SaltCheckKeiperSign.lean', 'SIDEExplicitFormula/Schema/PlateauRamp.lean',
       'SIDEExplicitFormula/Schema/SaltCheckPlateauRamp.lean')
SN, WN = KNS['sign'], KNS['win']
SIGN_NODES = [SN + 'liCoeff_one_pos_iff', SN + 'threshold_lt_gamma', SN + 'liCoeff_one_pos']
WIN_NODES = [WN + 'window', WN + 'ClosedFormFT', WN + 'WindowInClassK', WN + 'PlateauRampWindow', WN + 'WindowObligations',
             WN + 'plateauRampWindow_of', WN + 'epstein_ef_at_window']
SIGN_ANCHOR = 'SIDEExplicitFormula.Keiper.liCoeff_one_keiper | kernel | added: (R211)(4), Keiper`s λ_1 = 1 + γ/2 − ½ log 4π, the n = 1 check against γ'
DET_ANCHOR_PREFIX = 'SIDEExplicitFormula.Schema.detector | kernel |'
SALT_S = [KNS['ssign'] + n for n in ('coarse_lower_insufficient', 'liCoeff_one_lt_tenth', 'liCoeff_one_pos_holds')]
SALT_W = [KNS['swin'] + n for n in ('box_transform_zero_at_pi', 'box_transform_ne_zero_at_half_pi', 'window_even_compact_at_seven')]
POINT_CHECKS = ['#check @SIDEExplicitFormula.Keiper.SaltCheck.keiperTaylor_zero_holds',
                '#check @SIDEExplicitFormula.Keiper.SaltCheck.bounds_form_satisfiable']
STD3 = ['propext', 'Classical.choice', 'Quot.sound']
BALPOS = 'phase1.5/spectral/BALANCE_AND_POSITIVITY_v0_9_5.md'
TFAS = 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))
    return b


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def jl(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def flat(t):
    return ' '.join(t.split())


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) THE SEAT`S page_arms SUBCOMMAND WAS DEFECTIVE AT ITS FIRST RUN, AFTER THE POINT TAG: it read this act`s node lists, which are '
    'written only after v0.20, and raised FileNotFoundError before any arm ran (nothing written). Corrected through the Edit tool to read '
    'the lists in force at each stage -- at c1 b601`s ζ list and b596`s χ list with their banked probes, at c2 this act`s -- and re-run.',
    '(b) A STOP OF THE HARNESS (an API stop), NOT OF THE ACT: it fell in Component 6 after the scores were banked '
    '(data/b602_scores.json at 2026-10-03T02:54:52Z) and before the first write of the record, the FINDINGS entry; the act resumed at '
    '2026-10-03T03:14:45Z on the author`s order. Read before anything was written: FINDINGS ends at 970309 bytes = the last Component 1 '
    'append`s recorded before 969892 + 417, OPEN_TRAILS at 1539240 = 1538748 + 492 -- the three Component 1 lines whole and standing; the '
    'entry and the trail record had not landed (no byte after them, no data/b602_findings.json or data/b602_trail.json), so nothing was '
    'cut back. Component 6 continued in its written order from the record.',
]


def defects():
    put_txt('b602_defects.txt', ['### b602 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
READS = [
    ('SIDE-explicit-formula v0.19 AxiomCheckKeiper.lean: the salt-check #check lines, the two omitted', EFK, 'v0.19', AUDIT,
     list(range(83, 95))),
    ('relay b601`s sealed suite: G-SALT-CHECK`s predicate and arm', RELAY, 'HEAD', 'tools/b601_checks.py', [398, 399, 400, 401, 613]),
    ('SIDE-explicit-formula v0.19 Keiper.lean: λ_1`s closed form', EFK, 'v0.19', 'SIDEExplicitFormula/Keiper.lean', [238, 239]),
    ('Mathlib at the pin: γ, its two sequences, their monotonicity and the bounds', MLK, 'HEAD', 'Mathlib/NumberTheory/Harmonic/EulerMascheroni.lean',
     [48, 53, 65, 80, 86, 100, 128, 156, 161, 167, 171]),
    ('Mathlib at the pin: π bounds', MLK, 'HEAD', 'Mathlib/Analysis/Real/Pi/Bounds.lean', [151, 163, 167, 172]),
    ('Mathlib at the pin: e and log 2 bounds', MLK, 'HEAD', 'Mathlib/Analysis/Complex/ExponentialBounds.lean', [35, 38, 83, 86]),
    ('Mathlib at the pin: log ≤ x − 1', MLK, 'HEAD', 'Mathlib/Analysis/SpecialFunctions/Log/Basic.lean', [307]),
    ('Mathlib at the pin: the convolution theorem (Schwartz only), compact support of a convolution, ∫ exp(cx)', MLK, 'HEAD',
     'Mathlib/Analysis/Fourier/Convolution.lean', [160, 167]),
    ('Mathlib at the pin: HasCompactSupport.convolution', MLK, 'HEAD', 'Mathlib/Analysis/Convolution.lean', [529]),
    ('Mathlib at the pin: integral_exp_mul_complex', MLK, 'HEAD', 'Mathlib/Analysis/SpecialFunctions/Integrals/Basic.lean', [242, 243]),
    ('PLACE-papers OPEN_TRAILS: the work-order (E3) at :12170 whole; b554`s closed-form route :11332-:11340, :11423; the re-scope '
     ':11512-:11517; the generator-run line and b600-b601`s lines', PP, PRE_PP, 'OPEN_TRAILS.md',
     [12170, 11332, 11334, 11336, 11337, 11338, 11339, 11340, 11423, 11512, 11516, 11517, 12288, 12352, 12354, 12356, 12358, 12374, 12392], 6000),
    ('PLACE-papers FINDINGS: the witness ratio (:6758); b601`s entry (:6972)', PP, PRE_PP, 'FINDINGS.md', [6758, 6972], 6000),
    ('SIDE-explicit-formula v0.16 Schema/Detector.lean: the detector`s base and statement', EFK, 'v0.16', 'SIDEExplicitFormula/Schema/Detector.lean',
     [33, 40, 99, 100, 101, 102, 120]),
    ('SIDE-explicit-formula v0.16 Schema/Epstein.lean: EpsteinPremises and epstein_not_h2_sign_cfg', EFK, 'v0.16',
     'SIDEExplicitFormula/Schema/Epstein.lean', [40, 41, 42, 43, 44, 57, 58, 59]),
    ('SIDE-explicit-formula v0.19 TwoPropertyWindow.lean: the kernel`s plateau and its ramp', EFK, 'v0.19', 'SIDEExplicitFormula/TwoPropertyWindow.lean',
     [11, 12, 15, 16, 17, 56, 57]),
    ('SIDE-explicit-formula v0.19 PowerWindow.lean: classK_of_real_even', EFK, 'v0.19', 'SIDEExplicitFormula/PowerWindow.lean', [51, 52]),
    ('SIDE-lv-conservation 2f71068 CouplingsAtPhi.lean: n_one_binding_instance, the non-strict constants form, prior art', LVK, 'HEAD',
     'SIDELvConservation/CouplingsAtPhi.lean', [349, 357, 362, 363, 366, 367]),
    ('PLACE-papers the ζ page at v0.19: the Li ladder and the Keiper rows', PP, PRE_PP, PAGE, [1, 3, 24, 25, 31]),
    ('PLACE-papers the χ page: head and the detector`s row', PP, PRE_PP, DIR_PAGE, [1, 3]),
    ('PLACE-papers the bearing candidates: BALANCE_AND_POSITIVITY v0.9.5 :398; THE_FINDINGS_AS_THEY_STAND :497', PP, PRE_PP, BALPOS, [396, 398, 400], 4000),
    ('PLACE-papers THE_FINDINGS_AS_THEY_STAND :497', PP, PRE_PP, TFAS, [497], 4000),
    ('relay b601`s closing push-out, committed at step zero', RELAY, 'HEAD', 'data/b601_closing_push_out.txt', list(range(1, 18))),
]


def reads():
    L = ['b602 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for rr in READS:
        label, repo, rev, path, sel = rr[:5]
        width = rr[5] if len(rr) > 5 else 900
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, at, len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### SIDE-explicit-formula: v0.19 = %s ; main = %s ; the checkout`s branch %s' % (
        g(EFK, 'rev-parse', '--short=7', 'v0.19^{commit}').strip(), g(EFK, 'rev-parse', '--short=7', 'main').strip(),
        g(EFK, 'branch', '--show-current').strip()),
          '### Mathlib (the kernel`s .lake/packages/mathlib) HEAD %s' % g(MLK, 'rev-parse', '--short=10', 'HEAD').strip(),
          '### chain_page.py`s hold: %s' % [l for l in io.open(os.path.join(ROOT, 'tools', 'chain_page.py'), encoding='utf-8').read().split(NL)
                                             if l.startswith('HOLD_MB')]]
    put_txt('b602_reads.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B601_ENTRY = '## The doubling corollary: Weil positivity of the schema without simplicity, at v0.19'
W_HEAD = '*Appended 2026-10-02 by b602 to b601’s entry (:%d), under `(R212)`(1) -- b601 AT ITS WEIGHT:*'
S_HEAD = '*Appended 2026-10-02 by b602 to the reading at :%d, under `(R212)`(1) -- THE READING STANDS:*'
SIEVE_HEAD = ('*Appended 2026-10-02 by b602, under `(R212)`(6), the author’s word -- THE EDITION OF THE_FINDINGS_AS_THEY_STAND AS A '
              'SIEVE TABLE, ENTERED:*')


def record_lines():
    """### PLACE-papers FINDINGS: b601's weight addressed to its entry, and the (R211)(2) reading recorded as standing; OPEN_TRAILS:
    ### the sieve-table edition entered after b603 as the author's word."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B601_ENTRY)
    reading = 6970
    if entry != 6972 or 'THE READING b600 ADDS' not in io.open(Q.FIND, encoding='utf-8').read().split(NL)[reading - 1]:
        sys.exit('### THE ADDRESSED LINES MOVED -- NOTHING WRITTEN')
    h1, h2 = W_HEAD % entry, S_HEAD % reading
    for h in (h1, h2):
        Q.guard_absent(Q.FIND, h)
    Q.guard_absent(Q.OT, SIEVE_HEAD)
    t1 = ('\n%s SIDE-explicit-formula v0.19 = 5fc0c87, the peeled tag matching the remote, the branch doubling-keiper-b601 kept. '
          'Doubling.lean: summing a configuration with itself doubles every multiplicity and the sum is Weil-positive exactly when the '
          'configuration is ((productLemma_holds C C).trans and_self_iff); positivity_not_imp_simplicity -- b596’s on-line toy doubled, '
          'printed positive with its point at multiplicity 2, failing allSimple. H35a, H35b, N1, N2 held. Keiper.lean and '
          'KeiperBounds.lean: the Stieltjes constants defined on Mathlib’s riemannZeta₀ at the pin; lemma (1), the Keiper–Taylor '
          'identity, at INTERFACES on four named obligations (the binomial transform, the split at 1, the power-series logarithm, the '
          'polygamma values at ½), with the identity at n = 0, three obligations at their opening index, and λ₁ = 1 + γ/2 − ½ log 4π '
          'proved at T0; lemma (2), the bounds, at INTERFACES on three named premises, every Stieltjes constant beyond γ a premise and '
          'none assumed; γ ∈ (½, ⅔) proved and too wide to fix λ₁’s sign; the Keiper sum checked against the three-way bench before the '
          'identity was stated, λ₁…λ₁₂ to every printed digit. H35d and N3 refuted in letter, the detector shown non-vacuous by a planted '
          'closed row; H35c, H35e held. The ζ page with the Keiper nodes after li_nonneg_iff_rh and the doubling nodes after Product, the '
          'χ page unchanged, page arms and the frozen control 2 of 2. Bearing: SIMPLICITY v1.1.3 :82 and :180 for the corollary; '
          'BALANCE_AND_POSITIVITY v0.9.5 :195 and :308 for the Keiper face. FINDINGS :6968, :6970, :6972; OPEN_TRAILS :12374, :12392. '
          'The suite 80 of 81, G-SALT-CHECK failing in its letter (defect (e)), repaired at v0.19.1 under `(R212)`(2). No prompt. '
          'Nothing deposited; no keystone edited.\n' % h1)
    t2 = ('\n%s the author’s strike item at :%d is not struck: the reading stands as entered -- positivity conjunctive over sums, the '
          'Dedekind reading carried as a reading until the factorisation is an instance in the kernel, and the schema’s silence on '
          'multiplicity given a constructive reason by the doubling corollary (:%d).\n' % (h2, reading, entry))
    t3 = ('\n%s after b603 (the family form over χ mod q, the research sequence’s fifth item), an edition of '
          'THE_FINDINGS_AS_THEY_STAND reorganised as a sieve table by cluster -- the quantifier shape, the register, the test that '
          'decided bright or dark and its instrument by pin. Entered as the author’s word in `(R212)`(6); priced at its own act; not '
          'started.\n' % SIEVE_HEAD)
    out = []
    for h, t in ((h1, t1), (h2, t2)):
        r = Q.append_to(Q.FIND, t)
        out.append(dict(head=h, line=Q.line_of(Q.FIND, h), append=r))
    r = Q.append_to(Q.OT, t3)
    sv = dict(head=SIEVE_HEAD, line=Q.line_of(Q.OT, SIEVE_HEAD), append=r)
    put_json('b602_record_lines.json', dict(entry=entry, reading=reading, lines=out, sieve=sv))
    for o in out + [sv]:
        print('  line :%s' % o['line'])


# ================================================================================ COMPONENT 2: THE POINT TAG
def point_diff():
    """### the point tag's diff: v0.19..v0.19.1 (or v0.19..main before the tag), files and lines, banked."""
    rev = POINT if g(EFK, 'rev-parse', '--verify', '-q', POINT + '^{commit}').strip() else 'main'
    names = [x for x in g(EFK, 'diff', '--name-only', 'v0.19', rev).split(NL) if x.strip()]
    stat = g(EFK, 'diff', '--numstat', 'v0.19', rev).strip()
    body = g(EFK, 'diff', '-U0', 'v0.19', rev)
    added = [l[1:] for l in body.split(NL) if l.startswith('+') and not l.startswith('+++')]
    removed = [l[1:] for l in body.split(NL) if l.startswith('-') and not l.startswith('---')]
    L = ['b602 -- COMPONENT 2: THE POINT TAG`S DIFF, v0.19 = %s .. %s = %s (UTC %s)' % (
        g(EFK, 'rev-parse', '--short=7', 'v0.19^{commit}').strip(), rev, g(EFK, 'rev-parse', '--short=7', rev + '^{commit}').strip(), utc()),
         '### files %s ; numstat %s' % (names, stat), '### lines added %d ; lines removed %d' % (len(added), len(removed)), ''] + \
        ['    + ' + a for a in added] + ['    - ' + r for r in removed] + \
        ['', '### ### **%s**' % ('TWO LINES, ONE FILE, THE RULED #check LINES EXACTLY' if names == [AUDIT] and added == POINT_CHECKS and not removed
                                 else '### NOT THE RULED TWO LINES')]
    put_txt('b602_point_diff.txt', L)
    put_json('b602_point_diff.json', dict(rev=rev, files=names, added=added, removed=removed,
                                          exact=names == [AUDIT] and added == POINT_CHECKS and not removed))


def salt_rerun(logpath):
    """### G-SALT-CHECK, b601's sealed arm, re-run at v0.19.1 over the re-run audit's prints: the predicate imported from b601's
    ### suite, its sources b601's E0 banks and the new prints. Banks data/b602_prints_keip_point.* and data/b602_salt_rerun.txt."""
    import b569_record as R9
    src = io.open(logpath, encoding='utf-8').read().replace(chr(13), '')
    out = [l[4:] for l in src.split(NL) if l.startswith('  | ')]
    ex = [l for l in src.split(NL) if l.startswith('### EXIT')]
    txt = NL.join(out)
    ax = R9.prints_axioms(txt)
    put_txt('b602_prints_keip_point.txt', ['b602 -- THE PRINTS OF %s AT %s (the watchdog`s run)' % (AUDIT, POINT),
                                           '### %s' % (ex[-1] if ex else '### NO EXIT LINE'), ''] + out)
    pj = dict(axioms=ax, sorry=[n for n, a in ax.items() if 'sorryAx' in a], std3=all(set(a) <= set(STD3) for a in ax.values()),
              exit=ex[-1] if ex else None, errors=sum(1 for l in out if ': error' in l or l.startswith('error')), text=txt)
    put_json('b602_prints_keip_point.json', pj)
    sys.argv = ['x', '--prerun']
    import b601_checks as C1
    S = dict(e0={k: C1.jl('b601_e0_%s.json' % k) for k in C1.KEYS}, pr=dict(doub=C1.jl('b601_prints_doub.json'), keip=pj))
    arm = [a for a in C1.ARMS if a[0] == 'G-SALT-CHECK'][0]
    live = bool(arm[2](S))
    import copy
    pos = bool(arm[2](arm[3](copy.copy(S))))
    missing = [n for n in C1.SALT if (n + ' :') not in ((S['pr']['doub'].get('text') or '') + NL + txt)]
    L = ['b602 -- COMPONENT 2: G-SALT-CHECK (b601`s sealed arm, its predicate imported from tools/b601_checks.py) RE-RUN AT %s (UTC %s)' % (POINT, utc()),
         '### sources: b601`s E0 banks (data/b601_e0_*.json) ; the doubling prints data/b601_prints_doub.json ; the Keiper prints at %s, '
         'data/b602_prints_keip_point.json (%s)' % (POINT, ex[-1] if ex else '### NO EXIT'),
         '### salt theorems whose #check is not printed: %s' % (missing or 'NONE'),
         '    G-SALT-CHECK : LIVE %s ; POS (its own positive control) %s' % ('PASS' if live else 'FAIL', 'PASS -- DEFECTIVE' if pos else 'FAIL'),
         '### ### **G-SALT-CHECK AT %s : %s ; COUNTED 1 OF 1**' % (POINT, 'PASSES' if live and not pos else 'FAILS')]
    put_txt('b602_salt_rerun.txt', L)
    print(L[-3], L[-2], L[-1])


def entry_tags():
    """### the pages' nodes: is any node's module changed between v0.19 and v0.19.1? (an entry tag moves only if its declaration's
    ### file changes). The re-emission decision at the point tag, with its reason."""
    changed = set(x for x in g(EFK, 'diff', '--name-only', 'v0.19', POINT).split(NL) if x.strip())
    rows = []
    for page, lst in ((PAGE, 'b601_nodes_zeta.txt'), (DIR_PAGE, 'b596_nodes_chi.txt')):
        txt = g(PP, 'show', 'HEAD:' + page)
        files = sorted(set(re.findall(r'— (SIDEExplicitFormula/[^\s:]+\.lean|Zeta23/[^\s:]+\.lean|AxiomCheck[^\s:]*\.lean):\d+ —', txt)))
        hit = sorted(changed & set(files))
        rows.append(dict(page=page, list=lst, node_files=files, changed_files_on_page=hit))
    moves = any(r['changed_files_on_page'] for r in rows)
    L = ['b602 -- COMPONENT 2: THE PAGES` ENTRY TAGS AT THE POINT TAG (UTC %s)' % utc(),
         '### files changed v0.19..%s: %s' % (POINT, sorted(changed))]
    for r in rows:
        L.append('    %s : node files %d ; changed among them %s' % (r['page'], len(r['node_files']), r['changed_files_on_page'] or 'NONE'))
    L.append('### ### **THE DECISION: %s**' % (
        'RE-EMIT -- a node`s file changed' if moves else
        'NOT RE-EMITTED AT %s -- no node`s declaration file changed (the point tag touches %s alone, which declares no node), so no '
        'entry tag moves; both pages are re-emitted after v0.20 under (R212)(5)' % (POINT, AUDIT)))
    put_txt('b602_entry_tags.txt', L)
    put_json('b602_entry_tags.json', dict(changed=sorted(changed), rows=rows, reemit=moves))
    print(L[-1])


# ================================================================================ COMPONENTS 3-4: THE STATEMENTS
ITEMS = dict(
    sign=[
        ('λ₁ > 0 from the closed form proved at v0.19', 'ruling', 'liCoeff_one_pos', r'theorem liCoeff_one_pos : 0 < LiWeil\.LiCoeff 1 :='),
        ('which needs γ > log 4π − 2', 'ruling', 'liCoeff_one_pos_iff',
         r'theorem liCoeff_one_pos_iff :\n    0 < LiWeil\.LiCoeff 1 ↔ Real\.log \(4 \* Real\.pi\) - 2 < Real\.eulerMascheroniConstant'),
        ('the lower bound on γ from Mathlib\'s Euler–Mascheroni sequences at an index where the partial value exceeds that threshold',
         'ruling', 'gamma_gt_seq_fifteen', r'theorem gamma_gt_seq_fifteen : 1195757 / 360360 - 4 \* Real\.log 2 < Real\.eulerMascheroniConstant'),
        ('an upper bound on log 4π from Mathlib\'s π and log bounds', 'ruling', 'log_four_pi_lt',
         r'theorem log_four_pi_lt : Real\.log \(4 \* Real\.pi\) < 2\.5421'),
    ],
    win=[
        ('a compiled window of the bench’s plateau family', 'wo', 'PlateauRampWindow',
         r'def PlateauRampWindow \(W h : ℝ\) : Prop := ClosedFormFT W h ∧ WindowInClassK W h'),
        ('the plateau-ramp window defined in the kernel', 'wo', 'window', r'def window \(W h : ℝ\) : ℕ → ℝ → ℝ'),
        ('with its transform in closed form', 'wo', 'ClosedFormFT', r'def ClosedFormFT \(W h : ℝ\) : Prop :='),
        ('that window in classK', 'wo', 'WindowInClassK', r'def WindowInClassK \(W h : ℝ\) : Prop :='),
        ('the indicator of [-W, W] convolved with the order-p B-spline of half-width R', 'c1', 'window',
         r'\| p \+ 1 => conv \(window W h p\) \(nbox h\)'),
        ('φ̂(z) = sinc(zW)·sinc(zh/2)^p up to its normalisation', 'c1', 'ClosedFormFT',
         r'\(2 \* Complex\.sin \(z \* \(W : ℂ\)\) / z\) \* \(2 \* Complex\.sin \(z \* \(\(h / 2 : ℝ\) : ℂ\)\) / \(z \* \(h : ℂ\)\)\) \^ p'),
        ('`ContDiff ℝ 4`, even, compactly supported, for p ≥ 6', 'c2', 'WindowInClassK',
         r'∀ p : ℕ, 6 ≤ p → ContDiff ℝ 4 \(window W h p\) ∧ \(∀ x, window W h p \(-x\) = window W h p x\) ∧'),
    ],
)
DECL = re.compile(r'^(theorem|def|structure|noncomputable def|abbrev) (\S+)')


def _headers(text):
    ls = text.split(NL)
    out = []
    for i, l in enumerate(ls):
        m = DECL.match(l)
        if not m:
            continue
        h = [l]
        j = i
        while not re.search(r':=|\bwhere\b', ls[j]) and j + 1 < len(ls):
            j += 1
            h.append(ls[j])
        out.append(dict(kind=m.group(1), name=m.group(2), line=i + 1, head=NL.join(h)))
    return out


def _sources_of_words():
    ot = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8').read().split(NL)
    ferry = rd('b602_ferry.txt')
    r3 = ferry[ferry.index('(3) THE SIGN OF λ₁'):ferry.index('(4) (E3)')]
    return dict(wo=ot[12170 - 1], c1=ot[11336 - 1], c2=ot[11337 - 1], ruling=r3)


def statements(key, suffix=''):
    """### the statements of one kernel file as written on the branch, printed before its build; for `sign` against (R212)(3) and
    ### for `win` against the work-order :12170 and b554's C1-C2 (:11336, :11337), item by item."""
    rel = KFILES[key]
    b = open(os.path.join(EFK, rel), 'rb').read()
    t = b.decode('utf-8')
    hs = _headers(t)
    L = ['b602 -- THE STATEMENTS OF %s, PRINTED %s' % (rel, 'BEFORE THE BUILD' if not suffix else 'AGAIN AFTER THE FILE CHANGED (the first print kept beside)'), '']
    if suffix:
        first = {d['name']: d['head'] for d in jl('b602_statements_%s.json' % key)['decls']}
        now = {d['name']: d['head'] for d in hs}
        L += ['### against the first print: headers unchanged %d ; changed %s ; added %s ; gone %s' % (
            sum(1 for n in now if first.get(n) == now[n]), sorted(n for n in now if n in first and first[n] != now[n]),
            sorted(set(now) - set(first)), sorted(set(first) - set(now))), '']
    L += ['### written at (UTC) %s ; the branch %s (checked out: %s) ; the file`s sha256 %s ; its bytes %d' % (
        utc(), BRANCH, g(EFK, 'branch', '--show-current').strip(), sha(b), len(b)), '']
    items = []
    if key in ITEMS:
        W = _sources_of_words()
        if key == 'sign':
            L += ['### THE STATEMENT, (R212)(3) AS BANKED IN data/b602_ferry.txt (whitespace joined):', '    ' + flat(W['ruling']), '']
        else:
            L += ['### THE WORK-ORDER, OPEN_TRAILS :12170, WHOLE:', '    ' + W['wo'], '### b554`s C1 it cites, :11336, WHOLE:', '    ' + W['c1'],
                  '### b554`s C2 it cites, :11337, WHOLE:', '    ' + W['c2'], '']
        L.append('### THE STATEMENT, ITEM BY ITEM, BESIDE THE DECLARATION THAT CARRIES IT:')
        for words, src, name, rx in ITEMS[key]:
            inwo = flat(words) in flat(W[src])
            found = re.search(rx, t) is not None
            items.append(dict(words=words, source=src, decl=name, in_statement=inwo, declared=found))
            L.append('    %-84s [%s] -> %-24s in its statement %s ; declared as printed %s' % ('“%s”' % words[:82], src, name, inwo, found))
        L.append('### ### **%s**' % ('EVERY ITEM OF THE STATEMENT CARRIED BY A DECLARATION' if all(i['in_statement'] and i['declared'] for i in items)
                                     else '### AN ITEM NOT CARRIED'))
        L.append('')
    for h in hs:
        L.append('### :%d %s %s' % (h['line'], h['kind'], h['name']))
        L += ['    ' + x for x in h['head'].split(NL)]
    put_txt('b602_statements_%s%s.txt' % (key, suffix), L)
    put_json('b602_statements_%s%s.json' % (key, suffix), dict(file=rel, sha256=sha(b), at=utc(), decls=hs, items=items))


def bounds():
    """### Component 3: the Mathlib bounds by name and file with their values; the index chosen and its partial value against the
    ### threshold; every index's partial value printed (exact rationals for H_n, floats for the logs -- the bench, not the kernel)."""
    from fractions import Fraction as F
    import math
    thr = math.log(4 * math.pi) - 2
    L = ['b602 -- COMPONENT 3: THE MATHLIB BOUNDS AND THE INDEX (UTC %s)' % utc(),
         '### the bounds, by name and file at the pin (Mathlib de5ce8a9):',
         '    Real.eulerMascheroniSeq n = harmonic n - log (n + 1)            Mathlib/NumberTheory/Harmonic/EulerMascheroni.lean :48',
         '    Real.strictMono_eulerMascheroniSeq                                 EulerMascheroni.lean :53',
         '    Real.eulerMascheroniSeq_lt_eulerMascheroniConstant (n)            EulerMascheroni.lean :156',
         '    Real.one_half_lt_eulerMascheroniConstant : 1/2 < γ                EulerMascheroni.lean :167',
         '    Real.eulerMascheroniConstant_lt_two_thirds : γ < 2/3              EulerMascheroni.lean :171',
         '    Real.log_two_lt_d9 : log 2 < 0.6931471808                         Mathlib/Analysis/Complex/ExponentialBounds.lean :86',
         '    Real.log_two_gt_d9 : 0.6931471803 < log 2                         ExponentialBounds.lean :83',
         '    Real.exp_one_gt_d9 : 2.7182818283 < exp 1                         ExponentialBounds.lean :35',
         '    Real.exp_one_lt_d9 : exp 1 < 2.7182818286                         ExponentialBounds.lean :38',
         '    Real.pi_lt_d4 : π < 3.1416 ; Real.pi_gt_d4 : 3.1415 < π           Mathlib/Analysis/Real/Pi/Bounds.lean :172, :167',
         '    Real.log_le_sub_one_of_pos : log x ≤ x - 1                        Mathlib/Analysis/SpecialFunctions/Log/Basic.lean :307',
         '### the threshold log 4π − 2 = %.12f ; the upper bound the proof reaches: log 4π < 2.5421 (2·0.6931471808 + π/e, π/e < 1.1558), '
         'so the index must give a partial value above 0.5421' % thr, '',
         '### every index n ≤ 25, H_n − log(n + 1) (H_n exact, the log a float): ']
    for n in range(1, 26):
        h = sum(F(1, k) for k in range(1, n + 1))
        v = float(h) - math.log(n + 1)
        L.append('    n = %-3d H_n = %-22s partial %.6f   above the threshold %s ; above 0.5421 %s ; n + 1 a power of 2 %s' % (
            n, '%d/%d' % (h.numerator, h.denominator) if n <= 16 else '…', v, v > thr, v > 0.5421, (n + 1) & n == 0))
    h15 = sum(F(1, k) for k in range(1, 16))
    L += ['', '### ### **THE INDEX CHOSEN: 15** -- H_15 = %d/%d, log 16 = 4 log 2, the partial value %.6f against the threshold %.6f '
              '(margin %.6f) and against the reached bound 0.5421; the first index above the threshold at all is 10 (margin 5·10⁻⁵, log 11 '
              'needed); the first above 0.5421 is 14 (log 15 needed); 15 is the first above it with n + 1 a power of 2.' % (
                  h15.numerator, h15.denominator, float(h15) - math.log(16), thr, float(h15) - math.log(16) - thr)]
    put_txt('b602_bounds.txt', L)


def build_bank(key, logpath):
    src = io.open(logpath, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    hdr = ('### b602 -- THE BUILD OF %s, ONE MODULE PER CALL, A DETACHED PROCESS WATCHED FROM THE FOREGROUND (OPEN_TRAILS :12356), THE '
           'WATCHDOG`S LOG (lean resident cap 3500 MB, free floor 900 MB; the seat starts no call below the 2560 MB hold), copied from the '
           'seat`s scratchpad' % key)
    put_txt('b602_build_%s.txt' % key, [hdr, ''] + src.rstrip(NL).split(NL))


def prints(key, logpath):
    import b569_record as R9
    src = io.open(logpath, encoding='utf-8').read().replace(chr(13), '')
    out = [l[4:] for l in src.split(NL) if l.startswith('  | ')]
    ex = [l for l in src.split(NL) if l.startswith('### EXIT')]
    txt = NL.join(out)
    ax = R9.prints_axioms(txt)
    L = ['b602 -- THE PRINTS: `lake env lean %s` at SIDE-explicit-formula %s (checked out: %s, HEAD %s), the watchdog`s run' % (
        AXF[key], BRANCH, g(EFK, 'branch', '--show-current').strip(), g(EFK, 'rev-parse', '--short=7', 'HEAD').strip()),
         '### %s' % (ex[-1] if ex else '### NO EXIT LINE'), ''] + out
    put_txt('b602_prints_%s.txt' % key, L)
    put_json('b602_prints_%s.json' % key, dict(axioms=ax, sorry=[n for n, a in ax.items() if 'sorryAx' in a],
                                               std3=all(set(a) <= set(STD3) for a in ax.values()), exit=ex[-1] if ex else None,
                                               errors=sum(1 for l in out if ': error' in l or l.startswith('error')), text=txt))
    print('  prints', len(ax), 'std3', all(set(a) <= set(STD3) for a in ax.values()))


def e0(key):
    import b569_record as R9
    import e0_rule as E0
    st = jl('b602_statements_%s_final.json' % key) if os.path.exists(os.path.join(D, 'b602_statements_%s_final.json' % key)) \
        else jl('b602_statements_%s.json' % key)
    axk = 'sign' if key in AX_KEYS['sign'] else 'win'
    P0 = jl('b602_prints_%s.json' % axk)['axioms']
    tip = g(EFK, 'rev-parse', BRANCH).strip()
    src = g(EFK, 'show', '%s:%s' % (tip, st['file']))
    rows = {}
    L = ['b602 -- THE E0 READ OF %s AT THE BRANCH TIP %s (%s)' % (st['file'], tip[:7], BRANCH)] + E0.RULE_TEXT + [
        '### the file at the tip is the one printed: %s' % (sha(src) == st['sha256']), '']
    for d in st['decls']:
        n = KNS[key] + d['name']
        kind = 'theorem' if d['kind'] == 'theorem' else 'def'
        head, _ln = R9.header_of(src, d['name'])
        gr, why, _b = E0.grade(head or '', kind)
        ax = P0.get(n)
        rows[n] = dict(grade=gr if kind == 'theorem' else 'DEF', why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3), head=head, kind=kind)
        L.append('    %-34s %-10s %s  -- %s' % (d['name'], rows[n]['grade'], 'std3' if rows[n]['std3'] else ax, (why or '')[:140]))
    gate = all(r['std3'] for r in rows.values()) and all(r['head'] is not None or r['kind'] == 'def' for r in rows.values())
    L.append('### ### **THE GATE: %s** -- declarations %d, theorems %d (DERIVES %d, INTERFACES %d)' % (
        'PASS' if gate else 'FAIL', len(rows), sum(1 for r in rows.values() if r['kind'] == 'theorem'),
        sum(1 for r in rows.values() if r['grade'] == 'DERIVES'), sum(1 for r in rows.values() if r['grade'] == 'INTERFACES')))
    put_txt('b602_e0_%s.txt' % key, L)
    put_json('b602_e0_%s.json' % key, dict(rows=rows, gate=gate, tip=tip, file=st['file'], same_file=sha(src) == st['sha256']))


RELATION = ('INDEPENDENT',
            'the window`s Props (ClosedFormFT, WindowInClassK, PlateauRampWindow) and their obligations (ConvStep, Smooth4) quantify over '
            'test functions and name no zero configuration and no arithmetic side; EpsteinPremises` two fields -- ef, the explicit formula '
            'for Z_Q over its configuration, and count, its local count -- are facts about a configuration that no statement of the window '
            'concludes, so nothing of EpsteinPremises is discharged (not DISCHARGES-PART); and no statement of the window has EpsteinPremises '
            'among its hypotheses (not NEEDS-IT). The compiled witness of the direction: epstein_ef_at_window takes EpsteinPremises AND the '
            'window`s obligations and evaluates ef at the window -- the premises consumed, the window an input. Beside the detector '
            '(v0.16): the detector`s base is `plateau` (Mathlib`s smoothTransition ramp) raised to a power 2^j; this window is the bench`s '
            'box ⋆ B-spline at its own width with no power -- a different family, as b546/b550 recorded; epstein_not_h2_sign_cfg is reached '
            'through the detector and uses no statement of this module.')


def relation():
    """### H36e: the window's relation to EpsteinPremises in one of the three words, its reason, the window file's hypotheses read."""
    t = g(EFK, 'show', '%s:%s' % (BRANCH, KFILES['win']))
    heads = _headers(t)
    with_ep = [h['name'] for h in heads if 'EpsteinPremises' in h['head']]
    concl_ep = [h['name'] for h in heads if re.search(r':\s*EpsteinPremises\b[^:]*:=\s*$', ' '.join(h['head'].split()))]
    L = ['b602 -- COMPONENT 4: THE WINDOW`S RELATION TO EpsteinPremises (UTC %s)' % utc(),
         '### declarations of Schema/PlateauRamp.lean at %s naming EpsteinPremises in their head: %s' % (BRANCH, with_ep or 'NONE'),
         '### of them, concluding EpsteinPremises (or a field of it): %s' % (concl_ep or 'NONE'),
         '### the window`s own Props and obligations naming EpsteinPremises: %s' % (
             [h['name'] for h in heads if h['name'] in ('ClosedFormFT', 'WindowInClassK', 'PlateauRampWindow', 'ConvStep', 'Smooth4',
                                                        'WindowObligations', 'plateauRampWindow_of') and 'EpsteinPremises' in h['head']] or 'NONE'),
         '', '### ### **THE RELATION: %s**' % RELATION[0], '    THE REASON: ' + RELATION[1]]
    put_txt('b602_relation.txt', L)
    put_json('b602_relation.json', dict(word=RELATION[0], reason=RELATION[1], with_ep=with_ep, concl_ep=concl_ep))


# ### THE FEDERATION WALK. Every kernel at HEAD (the explicit-formula kernel at the branch tip): a theorem header naming λ_1's sign or
# ### the window's Props; STRICT a conclusion that IS one of them or its negation; the lv kernel's constants form read by hand.
FED_PAT = r'LiCoeff 1\b|eulerMascheroniConstant \+ 2|PlateauRampWindow|ClosedFormFT|WindowInClassK|log \(4 \* (Real\.)?(pi|π)\)'
STRICT_POS = re.compile(r'^\s*(0\s*<\s*(SIDEExplicitFormula\.)?(LiWeil\.)?LiCoeff 1|(SIDEExplicitFormula\.)?(Schema\.)?(PlateauRamp\.)?'
                        r'PlateauRampWindow\s+\S+\s+\S+)\s*$')
STRICT_NEG = re.compile(r'^\s*((SIDEExplicitFormula\.)?(LiWeil\.)?LiCoeff 1\s*≤\s*0|¬\s*\(?\s*0\s*<\s*(LiWeil\.)?LiCoeff 1\s*\)?|'
                        r'¬\s*\(?\s*(PlateauRamp\.)?PlateauRampWindow\b.*)\s*$')
LOOSE = re.compile(r'(LiCoeff 1|eulerMascheroniConstant|log \(4|PlateauRamp|ClosedFormFT|WindowInClassK)')


def _strict_controls():
    return dict(pos_reads=bool(STRICT_POS.search(' 0 < LiWeil.LiCoeff 1')) and bool(STRICT_POS.search(' PlateauRampWindow W h')),
                pos_refuses=not STRICT_POS.search(' 0 ≤ LiCoeff n'),
                neg_reads=bool(STRICT_NEG.search(' LiCoeff 1 ≤ 0')) and bool(STRICT_NEG.search(' ¬ PlateauRampWindow W h')),
                neg_refuses=not STRICT_NEG.search(' ¬ h2_sign_cfg C'))


def _decl_heads(text):
    out = []
    for m in re.finditer(r'^[ \t]*(?:@\[[^\]]*\][ \t]*)?(?:(?:private|protected|nonrec)[ \t]+)*(theorem|lemma)[ \t]+(\S+)(.*?):=', text, re.M | re.S):
        out.append((text[:m.start()].count(NL) + 1, m.group(2), ' '.join((m.group(2) + m.group(3)).split())))
    return out


HAND = {
    ('SIDELvConservation/CouplingsAtPhi.lean', 'n_one_binding_instance'):
        'PRIOR ART, NOT THE PROP: γ + 2 ≥ log(4π), the NON-STRICT constants form (it allows λ_1 = 0), proved at SIDE-lv-conservation '
        '2f71068 (commit ef62027, 2026-07-17) by the index 12 and a bound on log 52π, over the constants and not LiCoeff 1, at another '
        'kernel and Mathlib pin; its docstring`s "WHY IT IS NOT PROVED HERE" is stale against its own proof. Cited in the record.',
    ('SIDEExplicitFormula/Keiper.lean', 'liCoeff_one_keiper'):
        'b601`s closed form λ_1 = 1 + γ/2 − ½ log 4π (v0.19), an identity with no sign: the input this act`s liCoeff_one_pos_iff consumes.',
    ('SIDEExplicitFormula/Keiper.lean', 'log_four_pi_ofReal'):
        'b601`s cast lemma, Complex.log (4π) as the real log 4π: an equality of casts, not a sign.',
    ('SIDEExplicitFormula/SaltCheckKeiper.lean', 'log_four_pi_pos'):
        'b601`s salt lemma 0 < log 4π: a bound on log 4π alone, not λ_1`s sign (it gives no threshold on γ).',
}


def fed_walk(head_of_ker=None):
    kernels = sorted(d for d in os.listdir('D:/') if d.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d, '.git')))
    rows, files = [], 0
    for k in kernels:
        rep = 'D:/' + k
        rev = head_of_ker if (k == 'SIDE-explicit-formula' and head_of_ker) else 'HEAD'
        out = g(rep, 'grep', '-l', '-I', '-E', FED_PAT, rev, '--', '*.lean')
        for f in [x.split(':', 1)[1] for x in out.split(NL) if x.strip()]:
            files += 1
            t = g(rep, 'show', '%s:%s' % (rev, f))
            for ln, name, head in _decl_heads(t):
                if not re.search(FED_PAT, head):
                    continue
                depth, cut = 0, -1
                for i, ch in enumerate(head):
                    if ch in '([{⟨':
                        depth += 1
                    elif ch in ')]}⟩':
                        depth -= 1
                    elif ch == ':' and depth == 0 and head[i:i + 2] != ':=':
                        cut = i
                concl = head[cut + 1:] if cut >= 0 else head
                own = k == 'SIDE-explicit-formula' and f in OWN
                if own:
                    cls = 'OWN'
                elif STRICT_NEG.search(concl):
                    cls = 'NEGATES'
                elif STRICT_POS.search(concl):
                    cls = 'CONCLUDES'
                elif LOOSE.search(concl):
                    cls = 'READ'
                else:
                    cls = 'OTHER'
                rows.append(dict(kernel=k, file=f, line=ln, name=name, cls=cls, conclusion=concl[:300], reading=HAND.get((f, name)) if cls == 'READ' else None))
    return rows, kernels, files


def grep_bank():
    tip = g(EFK, 'rev-parse', BRANCH).strip()
    rows, kernels, files = fed_walk(tip or None)
    bad = [r for r in rows if r['cls'] in ('CONCLUDES', 'NEGATES') or (r['cls'] == 'READ' and not r['reading'])]
    ctl = _strict_controls()
    L = ['b602 -- THE FEDERATION SEARCHED FOR A DECLARATION CONCLUDING λ_1`S SIGN, THE WINDOW`S PROP, OR A NEGATION (UTC %s)' % utc(), '',
         '### git grep -l -E "%s" at HEAD of every kernel (%d; SIDE-explicit-formula at %s, the branch tip %s), %d files; every theorem/lemma '
         'header naming one, its conclusion classified: CONCLUDES / NEGATES by the strict shapes, READ by the loose one (each hand-read), '
         'OTHER, OWN (this act`s files)' % (FED_PAT, len(kernels), BRANCH, tip[:7], files)]
    for r in rows:
        if r['cls'] != 'OTHER':
            L.append('    %-9s %s %s:%d %s -- %s' % (r['cls'], r['kernel'], r['file'], r['line'], r['name'], r['conclusion'][:180]))
            if r['cls'] == 'READ':
                L.append('              ### the seat`s hand reading: %s' % (r['reading'] or '### NONE -- COUNTED'))
    L += ['### OTHER rows %d: %s' % (sum(r['cls'] == 'OTHER' for r in rows),
                                     ', '.join('%s:%s' % (r['file'].split('/')[-1], r['name']) for r in rows if r['cls'] == 'OTHER')[:3000]),
          '### headers %d ; CONCLUDES %d ; NEGATES %d ; READ %d (hand-read %d) ; OTHER %d ; OWN %d' % (
              len(rows), sum(r['cls'] == 'CONCLUDES' for r in rows), sum(r['cls'] == 'NEGATES' for r in rows), sum(r['cls'] == 'READ' for r in rows),
              sum(r['cls'] == 'READ' and bool(r['reading']) for r in rows), sum(r['cls'] == 'OTHER' for r in rows), sum(r['cls'] == 'OWN' for r in rows)),
          '### the strict shapes, each exercised: %s' % ctl,
          '', '### ### **OUTSIDE THIS ACT`S OWN FILES, DECLARATIONS CONCLUDING λ_1`S SIGN OR THE WINDOW`S PROP OR A NEGATION, UNREAD : %d**' % len(bad)]
    put_txt('b602_grep.txt', L)
    put_json('b602_grep.json', dict(rows=rows, kernels=kernels, files=files, bad=bad, controls=ctl, tip=tip))
    print('  headers', len(rows), 'bad', len(bad), 'own', sum(r['cls'] == 'OWN' for r in rows), ctl)


# ================================================================================ THE NODE LISTS AND THE PAGES
NODE_HEAD_Z = ['# b602 -- THE ζ NODE LIST AT v0.20, (R212)(3), (5): b601`s list (relay data/b601_nodes_zeta.txt, every record line unchanged,',
               '# its backmatter record kept), the pin moved to v0.20; three declarations of KeiperSign.lean placed directly after',
               '# liCoeff_one_keiper`s record. Every cell is elaborated by the generator`s probe at the pin, never typed here.', '#']
SIGN_ADD = [SN + 'liCoeff_one_pos_iff | kernel | added: (R212)(3), λ_1 > 0 exactly when γ > log 4π − 2, by the closed form',
            SN + 'threshold_lt_gamma | kernel | added: (R212)(3), γ > log 4π − 2 from Mathlib`s sequence at 15 and its π, e and log 2 bounds',
            SN + 'liCoeff_one_pos | kernel | added: (R212)(3), the sign of λ_1, a single rung, not Li`s criterion']
NODE_HEAD_X = ['# b602 -- THE χ NODE LIST AT v0.20, (R212)(4)-(5): b596`s list (relay data/b596_nodes_chi.txt, every record line unchanged),',
               '# the pin moved to v0.20; seven declarations of Schema/PlateauRamp.lean placed directly after the detector`s record, the',
               '# schema page being where the detector stands. Every cell is elaborated by the generator`s probe at the pin, never typed here.', '#']
WIN_ADD = [WN + 'window | kernel | added: (R212)(4), (E3)`s plateau-ramp window, the box convolved with the order-p B-spline',
           WN + 'ClosedFormFT | kernel | added: (R212)(4), C1, the transform in closed form, a Prop',
           WN + 'WindowInClassK | kernel | added: (R212)(4), C2, the window in classK for p ≥ 6, a Prop',
           WN + 'PlateauRampWindow | kernel | added: (R212)(4), (E3)`s compiled window, C1 and C2',
           WN + 'WindowObligations | kernel | added: (R212)(4), the two named obligations, the convolution step and the smoothness',
           WN + 'plateauRampWindow_of | kernel | added: (R212)(4), the window at INTERFACES on its obligations',
           WN + 'epstein_ef_at_window | kernel | added: (R212)(4), the window an input to EpsteinPremises` explicit formula, INDEPENDENT']


def node_lists():
    z = rd('b601_nodes_zeta.txt').rstrip(NL).split(NL)
    x = rd('b596_nodes_chi.txt').rstrip(NL).split(NL)
    if z.count('# pin: v0.19') != 1 or not z[-1].startswith('# backmatter: ') or z.count(SIGN_ANCHOR) != 1:
        sys.exit('### b601`s ζ list: pin, backmatter or the anchor not as expected -- NOTHING WRITTEN')
    dets = [i for i, l in enumerate(x) if l.startswith(DET_ANCHOR_PREFIX)]
    if x.count('# pin: v0.17') != 1 or len(dets) != 1:
        sys.exit('### b596`s χ list: pin or the detector`s record not as expected -- NOTHING WRITTEN')
    zb = [('# pin: v0.20' if l == '# pin: v0.19' else l) for l in z[:-1]]
    i = zb.index(SIGN_ANCHOR) + 1
    zb = zb[:i] + SIGN_ADD + zb[i:]
    put_txt('b602_nodes_zeta.txt', NODE_HEAD_Z + zb + [z[-1]])
    xb = [('# pin: v0.20' if l == '# pin: v0.17' else l) for l in x]
    j = dets[0] + 1
    xb = xb[:j] + WIN_ADD + xb[j:]
    put_txt('b602_nodes_chi.txt', NODE_HEAD_X + xb)


NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b602_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b602_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NEWN = {'zeta': SIGN_NODES, 'chi': WIN_NODES}
PRIOR_LISTS = {'zeta': ('b601_nodes_zeta.txt', 'b601_probe_out.txt'), 'chi': ('b596_nodes_chi.txt', 'b596_chi_probe_out.txt')}


def free_mb():
    try:
        out = subprocess.run(['powershell', '-NoProfile', '-Command', '(Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory'],
                             capture_output=True, text=True).stdout
        return int(out.strip()) // 1024
    except Exception:
        return -1


def cr0(b):
    return (b or b'').replace(b'\r\n', b'\n')


def page(k):
    """### after v0.20: ONE page per call in the foreground, a full run at the new pin from this act's list (free memory read before
    ### the call against the hold; the probe banked). Writes the page only when it changed, and data/b602_page_<k>.json."""
    import shutil
    import difflib
    import chain_page as C
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b602_%s' % k)
    fm = free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, C.HOLD_MB))
    if 0 <= fm < C.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = C.build(os.path.join(D, NODES[k]), pdir, None)
    secs = int(time.time() - t0)
    for l in log:
        print('  %s: %s' % (k, l))
    if rc:
        put_json('b602_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    shutil.copyfile(os.path.join(pdir, 'chain_page_probe_out.txt'), os.path.join(D, PROBE[k]))
    shutil.copyfile(os.path.join(pdir, 'chain_page_probe.lean'), os.path.join(D, PROBE[k].replace('_out.txt', '.lean.txt')))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    new = [dict(name=n, grade=meta['cells'][n].get('grade'), tier=meta['cells'][n].get('tier'), premises=meta['cells'][n].get('premises'),
                axioms=meta['cells'][n].get('axioms'), entry=meta['cells'][n].get('entry'), module=meta['cells'][n].get('module'))
           for n in NEWN[k] if n in (meta.get('cells') or {})]
    lines = b.decode('utf-8').split(NL)
    rows = {n: [l for l in lines if ('`%s`' % n) in l][:2] for n in NEWN[k]}
    J = dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, at=utc(),
             free_mb_before=fm, seconds=secs, new=new, rows=rows, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), log=log)
    put_json('b602_page_%s.json' % k, J)
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))
    for x in new:
        print('    NEW NODE %s -- %s ; tier %s ; premises %s ; axioms %s ; entry %s' % (x['name'], x['grade'], x['tier'], x['premises'], x['axioms'], x['entry']))
    for x in dl[:80]:
        print('    ' + x[:240])


def page_arms(tag):
    import g_chain_page as GCP
    import test_chain_page_b596 as T
    L = ['b602 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    # ### at c1 (after the point tag, before the pages are re-emitted) the committed pages are b601's ζ list and b596's χ list
    lists = PRIOR_LISTS if tag == 'c1' else dict((k, (NODES[k], PROBE[k])) for k in NODES)
    L.append('### the lists read: %s' % lists)
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, lists[k][0]), os.path.join(SP, '_b602_gcp'), os.path.join(D, lists[k][1]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = T.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            T.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (T.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b602_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ THE BEARING
BEARING = [
    ('sign', BALPOS, 398, '**γ + 2 ≥ ln(4π)**',
     'The sentence gives the n = 1 binding instance, γ + 2 ≥ ln(4π) with slack 2λ₁, and the next sentence (:400) records it in the '
     'kernel as `n_one_binding_instance` and OPEN, "left as its own item". Both have moved. SIDE-lv-conservation at 2f71068 proves that '
     'non-strict constants form (commit ef62027, by the index 12 and a bound on log 52π), so :400`s OPEN is stale against the kernel it '
     'names; and SIDE-explicit-formula v0.20 proves the strict form over the programme`s own coefficient, `liCoeff_one_pos` -- 0 < '
     'LiCoeff 1, T0, by `threshold_lt_gamma` (γ > log 4π − 2 from Mathlib`s eulerMascheroniSeq at 15 and its π, e and log 2 bounds) '
     'through the closed form of v0.19. What does not move: a single rung; the sentence`s λ_A / λ_Z split at n = 1 is b601`s, and '
     'nothing here bears on any λ_n beyond n = 1.'),
    ('window', TFAS, 497, 'the instances differ',
     'The sentence separates the bench`s order-7 B-spline window, on which the numbers were taken, from the kernel`s named instance, '
     'the smooth bump. The bench`s family is now in the kernel by definition (`window W h p`, the box convolved p times with the '
     'normalised box, SIDE-explicit-formula v0.20), with its transform in closed form at p = 0, evenness and compact support proved; '
     'the theorems that hold for every C⁴ φ reach it once its C⁴ (`Smooth4`) and the convolution step (`ConvStep`) are discharged -- '
     'both named, `plateauRampWindow_of` at INTERFACES. Until then the instances still differ in what is compiled about them; the '
     'witness ratio (FINDINGS :6758) is unchanged, since the window has no compiled sign at any zero.'),
]


def bearing():
    L = ['b602 -- COMPONENT 5: THE BEARING -- THE KEYSTONE SENTENCES THE SIGN OF λ_1 AND (E3)`S WINDOW CHANGE THE READING OF, EACH PRINTED '
         'BY PATH AND LINE FROM ITS CURRENT VERSION AT PLACE-papers %s, THE READING BESIDE IT (UTC %s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc()),
         '### the search: the keystones` current versions grepped for λ_1 / λ₁ beside positive, margin, minimum, γ + 2, ln(4π); and for '
         'B-spline, plateau window, plateau family, witness ratio -- the residue hand-read.', '']
    rows = []
    for comp, path, ln, needle, reading in BEARING:
        line = g(PP, 'show', 'HEAD:' + path).split(NL)[ln - 1]
        ok = needle in line
        rows.append(dict(component=comp, path=path, line=ln, needle=needle, found=ok, sentence=line, reading=reading))
        L += ['### [%s] %s :%d%s' % (comp, path, ln, '' if ok else '   ### THE NEEDLE IS NOT ON THE CITED LINE'),
              '    THE SENTENCE: ' + line, '    THE READING: ' + reading, '']
    L.append('### ### **SENTENCES PRINTED AS BEARING : %d (the sign %d, the window %d) ; ON THEIR CITED LINES : %d**' % (
        len(rows), sum(r['component'] == 'sign' for r in rows), sum(r['component'] == 'window' for r in rows), sum(r['found'] for r in rows)))
    put_txt('b602_bearing.txt', L)
    put_json('b602_bearing.json', dict(rows=rows, at=utc()))


def answers():
    calls, results = [], {}
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
        try:
            o = json.loads(raw)
        except Exception:
            continue
        m = o.get('message') or {}
        for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
            if c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((i, c['id'], c['input']))
            if c.get('type') == 'tool_result':
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t
                results[c.get('tool_use_id')] = (i, t)
    L = ['### b602 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this session (b601-b602), banked verbatim with the options '
         'and the recommended mark, as the standing line at OPEN_TRAILS :12246 orders.' % sum(len(c[2].get('questions', [])) for c in calls), '']
    k = 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session 5dce8424-ec16-4701-8f42-69078426fd40, transcript line %d)' % (cid, i))
        for q in inp.get('questions', []):
            k += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'), op.get('description')))
        ri, rt = results.get(cid, (None, '### NO RESULT FOUND'))
        L += ['RESULT (transcript line %s): %s' % (ri, rt), '']
    if not calls:
        L.append('### NONE: no prompt was put to the author in this act.')
    put_txt('b602_author_answers.txt', L)


# ================================================================================ COMPONENT 6: THE SCORES AND THE RECORD
SCORE_KEYS = ('H36a', 'H36b', 'H36c', 'H36d', 'H36e', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')


def scores():
    E = {k: jl('b602_e0_%s.json' % k) for k in KFILES}
    PR = {k: jl('b602_prints_%s.json' % k) for k in AXF}
    ST = {k: jl('b602_statements_%s.json' % k) for k in ITEMS}
    gp, br, rel = jl('b602_grep.json'), jl('b602_bearing.json'), jl('b602_relation.json')
    Z, X = jl('b602_page_zeta.json'), jl('b602_page_chi.json')
    pdiff = jl('b602_point_diff.json')
    srr = rd('b602_salt_rerun.txt')
    rows = {n: r for e in E.values() for n, r in (e.get('rows') or {}).items()}
    g_ = lambda n: rows.get(n, {})
    all_std3 = all(e.get('gate') for e in E.values()) and all(not p.get('sorry') and p.get('std3') is True and p.get('errors') == 0 for p in PR.values())
    items_ok = {k: bool(ST[k].get('items')) and all(i['in_statement'] and i['declared'] for i in ST[k]['items']) for k in ITEMS}
    salt_s = all(g_(n).get('std3') and g_(n).get('grade') == 'DERIVES' for n in SALT_S)
    salt_w = all(g_(n).get('std3') and g_(n).get('grade') == 'DERIVES' for n in SALT_W)
    pos = g_(SN + 'liCoeff_one_pos')
    pos_ok = pos.get('grade') == 'DERIVES' and pos.get('std3') is True and 'no hypothesis binder' in (pos.get('why') or '')
    idx = 15 if 'Real.eulerMascheroniSeq 15' in g(EFK, 'show', '%s:%s' % (BRANCH, KFILES['sign'])) else None
    wof = g_(WN + 'plateauRampWindow_of')
    win_src = g(EFK, 'show', '%s:%s' % (BRANCH, KFILES['win']))
    closed_win = [n for n, r in rows.items() if r['kind'] == 'theorem' and r['grade'] == 'DERIVES' and r['std3']
                  and re.search(r':\s*PlateauRampWindow\s+\S+\s+\S+\s*:=', ' '.join((r.get('head') or '').split()))]
    carried_named = wof.get('grade') == 'INTERFACES' and 'structure WindowObligations (W h : ℝ) : Prop where' in win_src \
        and 'conv_step : ConvStep W h' in win_src and 'smooth : Smooth4 W h' in win_src
    word = rel.get('word')
    zplus = sum(1 for d in Z.get('diff', []) if d.startswith('+') and not d.startswith('+++'))
    xplus = sum(1 for d in X.get('diff', []) if d.startswith('+') and not d.startswith('+++'))
    zn, xn = {x['name'] for x in Z.get('new', [])}, {x['name'] for x in X.get('new', [])}
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
                                                                               'SIDE-structural-error-correction', 'SIDE-cosmo', 'SIDE-silence-principle')}
    tagc = g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip()
    kern_ok = kern['SIDE-explicit-formula'] == tagc and {k: v for k, v in kern.items() if k != 'SIDE-explicit-formula'} == {
        'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-structural-error-correction': '6a4f482', 'SIDE-cosmo': 'c5cba30',
        'SIDE-silence-principle': '667c254'}
    kfiles = sorted(x for x in g(EFK, 'diff', '--name-only', POINT, TAG).split(NL) if x.strip())
    kmerges = [x for x in g(EFK, 'rev-list', '--merges', '%s..%s' % (PRE_KER, TAG)).split(NL) if x.strip()]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md'] + [p['page'] for p in (Z, X) if p.get('changed')])
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b602_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b601_closing_push_out.txt'))
    bear = [r for r in br.get('rows', []) if r['found']]
    salt_pass = 'G-SALT-CHECK AT %s : PASSES' % POINT in srr
    S = dict(
        H36a=('HOLDS' if pos_ok and salt_s else 'REFUTED',
              'liCoeff_one_pos (0 < LiCoeff 1) %s at the standard three %s, no premise %s ; the salt-check`s three theorems DERIVES %s' % (
                  pos.get('grade'), pos.get('std3'), 'no hypothesis binder' in (pos.get('why') or ''), salt_s)),
        H36b=('HOLDS' if idx is not None and idx <= 25 and g_(SN + 'gamma_gt_seq_fifteen').get('grade') == 'DERIVES' else 'REFUTED',
              'the γ bound reached from Mathlib`s eulerMascheroniSeq at the index %s (≤ 25), gamma_gt_seq_fifteen %s (data/b602_bounds.txt)' % (
                  idx, g_(SN + 'gamma_gt_seq_fifteen').get('grade'))),
        H36c=('HOLDS' if items_ok['win'] and salt_w else 'REFUTED',
              'the window`s statement item by item against the work-order :12170 and b554`s C1-C2 carried %s (data/b602_statements_win.txt) ; '
              'the salt-check`s three theorems DERIVES at the standard three %s' % (items_ok['win'], salt_w)),
        H36d=('HOLDS' if closed_win or carried_named else 'REFUTED',
              'closed (a theorem concluding PlateauRampWindow with no premise): %s ; carried at INTERFACES on WindowObligations with both '
              'obligations named (ConvStep, Smooth4): %s' % (closed_win or 'NONE', carried_named)),
        H36e=('HOLDS' if word in ('DISCHARGES-PART', 'INDEPENDENT', 'NEEDS-IT') else 'REFUTED',
              'the relation printed as %s (data/b602_relation.txt), with its reason and the compiled witness epstein_ef_at_window %s' % (
                  word, g_(WN + 'epstein_ef_at_window').get('grade'))),
        N1=('HELD' if pdiff.get('exact') and salt_pass else 'REFUTED',
            'v0.19..v0.19.1: files %s, lines added %d, removed %d, the ruled two exactly %s ; G-SALT-CHECK at v0.19.1 passes %s' % (
                pdiff.get('files'), len(pdiff.get('added') or []), len(pdiff.get('removed') or []), pdiff.get('exact'), salt_pass)),
        N2=('HELD' if pos_ok else 'REFUTED', 'λ_1 > 0 at the standard three with no premise: %s' % pos_ok),
        N3=('HELD' if word == 'INDEPENDENT' else 'REFUTED', 'the relation reads %s' % word),
        N4=('HELD' if zplus >= 1 and xplus >= 1 and Z.get('changed') is True and X.get('changed') is True else 'REFUTED',
            'the ζ page re-emitted at %s gains %d lines (new nodes %d), changed %s ; the χ page gains %d lines (new nodes %d), changed %s' % (
                TAG, zplus, len(zn), Z.get('changed'), xplus, len(xn), X.get('changed'))),
        N5=('HELD' if kern_ok and not kmerges and kfiles == sorted(OWN) and pdiff.get('exact') and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
            'nothing deposits; SIDE-explicit-formula main at the tag %s, the other mains unmoved %s; the kernel`s files %s..%s %s, merges %d; '
            'the point tag the ruled two lines %s; PLACE-papers %s; relay files beyond the act`s own banks and tools and the table: %s' % (
                tagc, kern_ok, POINT, TAG, kfiles, len(kmerges), pdiff.get('exact'), pp_ch, relay_beyond)),
        S1=('HELD' if all_std3 else 'REFUTED',
            'every declaration of the four modules (%s) at the standard three, no sorryAx, no error: %s' % (
                ', '.join('%s %d' % (k, len(E[k].get('rows') or {})) for k in KFILES), all_std3)),
        S2=('HELD' if salt_s and salt_w else 'REFUTED',
            'the salt-checks` six theorems, each DERIVES at the standard three: %s' % [(n.split('.')[-1], g_(n).get('grade')) for n in SALT_S + SALT_W]),
        S3=('HELD' if pdiff.get('exact') else 'REFUTED', 'the point tag`s diff is the ruled two #check lines in %s and nothing else: %s' % (AUDIT, pdiff.get('exact'))),
        S4=('HELD' if gp.get('bad') == [] and all(gp.get('controls', {}).values()) and any(r['cls'] == 'OWN' for r in gp.get('rows', []))
            and any(r['name'] == 'n_one_binding_instance' and r['cls'] == 'READ' for r in gp.get('rows', [])) else 'REFUTED',
            'no unread declaration outside the act`s files concluding λ_1`s sign or the window`s Prop or a negation ; the lv kernel`s '
            'n_one_binding_instance found and hand-read %s ; the strict shapes exercised %s ; the act`s own found %s' % (
                any(r['name'] == 'n_one_binding_instance' and r['cls'] == 'READ' for r in gp.get('rows', [])), gp.get('controls'),
                any(r['cls'] == 'OWN' for r in gp.get('rows', [])))),
        S5=('HELD' if [(r['path'], r['line']) for r in bear] == [(BALPOS, 398), (TFAS, 497)] else 'REFUTED',
            'the bearing sentences: %s' % [(r['path'].split('/')[-1], r['line']) for r in bear]),
    )
    put_json('b602_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-6s %s -- %s' % (k, S[k][0], S[k][1][:220]))


def _title():
    S = jl('b602_scores.json')
    win = 'proved' if 'NONE' not in S['H36d'][1].split(';')[0] else 'carried to 2 named obligations'
    return ('## The sign of λ₁ at T0 from Mathlib’s γ and π bounds; (E3)’s window at DETECTION-REGION %s, its relation to '
            'EpsteinPremises INDEPENDENT; the Keiper audit file at v0.19.1' % win)


TRAIL_HEAD = ('### b602 — lane three, act twenty-nine under (R212): the audit file repaired at v0.19.1; the sign of λ₁ at T0; (E3)’s '
              'compiled window at DETECTION-REGION')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


FINDINGS_BODY = [
    '**The point tag** (`(R212)`(2)). SIDE-explicit-formula v0.19.1 = `{POINTC}`: the two #check lines of b601’s defect (e) added to '
    'AxiomCheckKeiper.lean on main, one file, two lines, nothing removed (relay data/b602_point_diff.txt); the audit re-run and read back; '
    'committed alone, tagged by push_gated.sh, the peeled tag matching the remote; v0.19 not moved. b601’s sealed G-SALT-CHECK, its '
    'predicate imported, passes at v0.19.1 (relay data/b602_salt_rerun.txt). No node’s declaration file changed, so no entry tag moved '
    'and neither page was re-emitted at the point tag (relay data/b602_entry_tags.txt); the page arms and the frozen control 2 of 2 after '
    'it.', '',
    '**The sign of λ₁** (`(R212)`(3)). SIDE-explicit-formula v0.20 = `{TAGC}`, `SIDEExplicitFormula/KeiperSign.lean`: by the closed form '
    'of v0.19, λ₁ > 0 exactly when γ > log 4π − 2 (`liCoeff_one_pos_iff`); Mathlib’s eulerMascheroniSeq at the index 15 is '
    '1195757/360360 − 4 log 2 ≈ 0.5456 and lies below γ; log 4π < 2.5421 from Mathlib’s log 2, π and e bounds through log π ≤ π/e; so '
    '`threshold_lt_gamma` and `liCoeff_one_pos`, 0 < LiCoeff 1 with no premise, at the standard three. The index: the first above the '
    'threshold is 10 with a margin of 5·10⁻⁵, the first above the reachable bound 14, and 15 the first of those with n + 1 a power of '
    '2 (relay data/b602_bounds.txt). The salt-check: at Mathlib’s coarse γ > ½ the closed form is negative, so the index carries the '
    'sign; 0 < λ₁ < 1/10. A single rung: not Li’s criterion, nothing about any λ_n beyond n = 1. PRIOR ART: SIDE-lv-conservation at '
    '2f71068 proves `n_one_binding_instance`, γ + 2 ≥ log 4π (commit ef62027, 2026-07-17, by the index 12) -- the non-strict constants '
    'form, which allows λ₁ = 0, over the constants and at another pin; its docstring’s “not proved here” is stale against its own '
    'proof.', '',
    '**(E3)’s window** (`(R212)`(4), by the work-order at OPEN_TRAILS :12170 and b554’s C1-C2 at :11336, :11337). '
    '`SIDEExplicitFormula/Schema/PlateauRamp.lean`: the bench’s plateau family defined in the kernel -- the box of half-width W convolved '
    'p times with the normalised box of width h (Mathlib’s convolution) -- with C1, its transform in closed form, and C2, the window in '
    'classK for p ≥ 6, as Props joined in `PlateauRampWindow`. Proved: the box’s and the normalised box’s transforms in closed form, C1 '
    'at p = 0, the window even and compactly supported at every p. Carried to 2 named obligations in `WindowObligations` -- the '
    'convolution step (Mathlib at the pin holds the convolution theorem for Schwartz functions only) and the C⁴ smoothness for p ≥ 6 -- '
    'by `plateauRampWindow_of`. The salt-check: the closed form vanishes at π for the unit box and not at π/2; the window at the bench’s '
    'p = 7 even and compactly supported with no obligation. The relation to EpsteinPremises: INDEPENDENT -- no statement of the window '
    'concludes a field of the premises or assumes them; `epstein_ef_at_window` evaluates the premises’ explicit formula at the window, '
    'the premises consumed and the window an input (relay data/b602_relation.txt). The detector (v0.16) is a different family, the '
    'smoothTransition plateau raised to 2^j, and `epstein_not_h2_sign_cfg` uses nothing of this module. The federation walk finds no '
    'declaration outside this act’s files concluding the sign, the window or a negation ({HEADERS} headers, the lv kernel’s constants '
    'form and b601’s Keiper lemmas read by hand).', '',
    '**The pages.** The ζ page at v0.20 (PLACE-papers {ZCOMMIT}): `liCoeff_one_pos_iff`, `threshold_lt_gamma` and `liCoeff_one_pos` '
    'directly after `liCoeff_one_keiper`, each T0. The χ page at v0.20 (PLACE-papers {XCOMMIT}), its pin moved from v0.17: the window’s '
    'seven declarations directly after the detector, `plateauRampWindow_of` and `epstein_ef_at_window` with their premises printed. '
    'Page arms and the frozen control 2 of 2.', '',
    '**Its bearing** (relay data/b602_bearing.txt). For the sign: BALANCE_AND_POSITIVITY v0.9.5 :398, the n = 1 binding instance γ + 2 '
    '≥ ln(4π) with slack 2λ₁, whose next sentence (:400) calls it OPEN -- stale against the lv kernel’s non-strict proof and now against '
    'the strict form over LiCoeff 1. For the window: THE_FINDINGS_AS_THEY_STAND :497, “the instances differ” -- the bench’s B-spline '
    'window is now in the kernel by definition, the theorems for every C⁴ φ reaching it once its two obligations are discharged; the '
    'witness ratio (FINDINGS :6758) unchanged.', '',
    '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the sign re-reads b601’s closed form (:6972) and BALANCE_AND_POSITIVITY’s channel '
    'row at n = 1, and meets SIDE-lv-conservation’s `n_one_binding_instance` (ledger archive :1415) as prior art in the non-strict '
    'form; the window re-reads b554’s closed-form route, b590’s detector and Epstein premises (:6740) and b591’s witness ratio (:6758), '
    'which it leaves where it was; both are re-read by b603’s family form over χ mod q and by any act that discharges the window’s '
    'obligations. The point tag closes b601’s defect (e). It strengthens the programme’s offerings of the compiled star (the first '
    'finite rung of the Li ladder signed at T0) and of the schema and its instances (the bench’s window family in the kernel, its '
    'relation to the Epstein premises stated).', '',
    '**The record lines.** b601’s weight at FINDINGS :{W1}; the `(R211)`(2) reading recorded as standing at :{W2}; the sieve-table edition '
    'entered at OPEN_TRAILS :{SIEVE}.', '',
]
TRAIL_BODY = [
    '**Entered:** FINDINGS.md:{W1} (b601’s weight), :{W2} (the reading stands), :{ENTRY} (the entry, with its mutual-light line); '
    'OPEN_TRAILS.md:{SIEVE} (the sieve-table edition, the author’s word), this record; SIDE-explicit-formula v0.19.1 = `{POINTC}` (the '
    'two #check lines) and v0.20 = `{TAGC}` (KeiperSign.lean, SaltCheckKeiperSign.lean, Schema/PlateauRamp.lean, '
    'Schema/SaltCheckPlateauRamp.lean, AxiomCheckKeiperSign.lean, AxiomCheckPlateauRamp.lean; the branch sign-window-b602 kept); both '
    'pages re-emitted at v0.20.', '',
    '**The obligations, named where the proof stops** (the window carried, not closed): `ConvStep`, the convolution step of the transform '
    'on the family, and `Smooth4`, the window C⁴ for p ≥ 6, in `WindowObligations` at `plateauRampWindow_of`. Each a priced item for a '
    'later act; none started.', '',
    '**Resolved by the seat, for the author’s strike:** the sign’s index 15 (n + 1 a power of 2, log 16 = 4 log 2) over the first index '
    'above the threshold, 10, whose margin of 5·10⁻⁵ the reachable log bounds do not meet; the prior art SIDE-lv-conservation '
    '`n_one_binding_instance` (non-strict, over the constants, another pin) cited and not consumed, the sign component standing as ruled, '
    'its stale docstring and BALANCE_AND_POSITIVITY :400’s “OPEN” left for their next editions; the window under Schema/ beside the '
    'detector, its nodes on the χ page with its pin moved from v0.17 to v0.20, so the schema page carries it and the ζ page never does; '
    'no re-emission at the point tag, no node’s file having changed; the shared E0 rule reads a width parameter named h as a hypothesis '
    'binder on three non-node declarations of the window module, no page grade moved by it.', '',
    '**Defects (a)-(b)** (relay data/b602_defects.txt): (a) the seat’s page-arm subcommand read this act’s lists before they existed, '
    'corrected and re-run; (b) an API stop of the harness, not of the act, after the scores at 2026-10-03T02:54:52Z and before the '
    'record’s first write, resumed at 03:14:45Z with the ledgers read first -- the Component 1 lines whole, the record not yet landed, '
    'nothing cut back.', '',
]


def _fill(x, extra):
    for k, v in extra.items():
        x = x.replace('{%s}' % k, str(v))
    return x


def _fills():
    rl, gp = jl('b602_record_lines.json'), jl('b602_grep.json')
    return dict(TAGC=g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip(), POINTC=g(EFK, 'rev-parse', '--short=7', POINT + '^{commit}').strip(),
                ZCOMMIT=_pp_commit('b602 (R212)(5): ' + PAGE), XCOMMIT=_pp_commit('b602 (R212)(5): ' + DIR_PAGE),
                HEADERS=len(gp.get('rows') or []), W1=rl['lines'][0]['line'], W2=rl['lines'][1]['line'], SIEVE=rl['sieve']['line'])


def findings():
    Q = _Q()
    S = jl('b602_scores.json')
    title = _title()
    Q.guard_absent(Q.FIND, title[:90])
    F = _fills()
    e = ['', title, '',
         '*Filed at b602 on the author’s ruling `(R212)`. Banks: relay `data/b602_point_diff.txt`, `data/b602_salt_rerun.txt`, '
         '`data/b602_entry_tags.txt`, `data/b602_bounds.txt`, `data/b602_statements_sign.txt`, `data/b602_statements_win.txt`, '
         '`data/b602_build_*.txt`, `data/b602_prints_sign.txt`, `data/b602_prints_win.txt`, `data/b602_e0_*.txt`, `data/b602_relation.txt`, '
         '`data/b602_grep.txt`, `data/b602_page_zeta.json`, `data/b602_page_chi.json`, `data/b602_page_arms_c2.txt`, `data/b602_bearing.txt`, '
         '`data/b602_reads.txt`. Nothing deposits.*', ''] + [_fill(x, F) for x in FINDINGS_BODY] + [
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R212)`(6): b603, the family form over χ mod q, the research sequence’s fifth item; then the edition of '
         'THE_FINDINGS_AS_THEY_STAND as a sieve table, on the author’s word. The author rules on the closing.', '',
         '*Nothing deposits; no keystone edited; README and REGISTRY unwritten; nothing here is a statement about RH, GRH or any zero beyond '
         'the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b602_findings.json', dict(entry_line=Q.line_of(Q.FIND, title[:90]), title=title, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, title[:90]))


def trail():
    Q = _Q()
    S, fj = jl('b602_scores.json'), jl('b602_findings.json')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    F = _fills()
    F['ENTRY'] = fj['entry_line']
    rows_ = ['', TRAIL_HEAD, '',
             '**(R212) ratified.** (1) b601 at its weight; the `(R211)`(2) reading stands. (2) Defect (e) repaired by the point tag '
             'v0.19.1. (3) The sign of λ₁, a finite rung. (4) (E3)’s compiled window at DETECTION-REGION. (5) The tag v0.20 and the pages. '
             '(6) The act after: b603; then the sieve-table edition, on the author’s word.', ''] + [_fill(x, F) for x in TRAIL_BODY] + [
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R212)`(6), b603, the family form over χ mod q, the research sequence’s fifth item; then the edition of '
             'THE_FINDINGS_AS_THEY_STAND as a sieve table (:{SIEVE}); the author rules on the closing.'.replace('{SIEVE}', str(F['SIEVE'])), '',
             '**No `sorry` on any `main`.** Nothing deposits; no keystone edited; FACES_LEDGER untouched; row U1 unedited; `h2` where the '
             'deposit left it; the four lists stay OPEN.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b602_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b602_trail.json')['line'])


def desk():
    S = jl('b602_scores.json')
    HK = ('H36a', 'H36b', 'H36c', 'H36d', 'H36e')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b602 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H36a-H36e, (R212)(3)-(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HK]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H36 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HK), sum(S[k][0] == 'REFUTED' for k in HK),
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b602_defects.txt').rstrip(NL).split(NL)
    put_txt('b602_desk_notes.txt', L)


def components():
    S, fj, tj, rl = jl('b602_scores.json'), jl('b602_findings.json'), jl('b602_trail.json'), jl('b602_record_lines.json')
    Z, X = jl('b602_page_zeta.json'), jl('b602_page_chi.json')
    F = _fills()
    L = ['b602 -- THE COMPONENTS, BANKED UNDER (R212).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b601`s closing push-out relay %s ; push-b601* branches deleted by name '
         '(data/b602_branches.txt) ; the kept branches untouched ; the work-order :12170 printed whole (data/b602_reads.txt) ; the suite run at '
         'HEAD before the face (data/b602_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b601`s weight FINDINGS :%d ; the reading standing :%d ; the sieve-table edition OPEN_TRAILS :%d' % (
             rl['lines'][0]['line'], rl['lines'][1]['line'], rl['sieve']['line']),
         '### COMPONENT 2 : SIDE-explicit-formula %s = %s, the ruled two lines ; G-SALT-CHECK re-run (data/b602_salt_rerun.txt) ; the pages` '
         'entry tags (data/b602_entry_tags.txt) ; N1 %s, S3 %s' % (POINT, F['POINTC'], S['N1'][0], S['S3'][0]),
         '### COMPONENT 3 : the sign of λ_1, KeiperSign.lean and SaltCheckKeiperSign.lean ; H36a %s, H36b %s' % (S['H36a'][0], S['H36b'][0]),
         '### COMPONENT 4 : (E3)`s window, Schema/PlateauRamp.lean and Schema/SaltCheckPlateauRamp.lean ; H36c %s, H36d %s, H36e %s' % (
             S['H36c'][0], S['H36d'][0], S['H36e'][0]),
         '### COMPONENT 5 : SIDE-explicit-formula %s = %s on %s merged ; the ζ page changed %s, the χ page changed %s ; the bearing '
         'data/b602_bearing.txt' % (TAG, F['TAGC'], BRANCH, Z.get('changed'), X.get('changed')),
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b603, the family form over χ mod q ; N1 %s, '
         'N2 %s, N3 %s, N4 %s, N5 %s' % (fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b602_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b602_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
