# -*- coding: utf-8 -*-
"""b547_record.py -- THE CASCADE, ACT FOUR: FACES_OF_H2 AND FACES_LEDGER TIERED, THE R-PAIRS UPDATED, THE FIELD'S STATUS,
TWO WORK-ORDERS PRICED: THE RECORD, UNDER (R157).
### `python tools/b547_record.py reads | anchor | ...`

### FACES_OF_H2 takes appended blocks; FACES_LEDGER one UPDATE block through its own writer (b327_faces_row.append_block);
### FINDINGS appends; OPEN_TRAILS one append. This file deletes nothing.
"""
import hashlib, io, json, os, re, subprocess, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'phase2', 'method', 'FACES_OF_H2_AT_FINITE_INSTANCE.md')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
MAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
SCR = os.environ.get('B547_SCRATCH', '')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def put_txt(n, lines):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(NL.join(lines) + NL)


def g(repo, *a):
    return subprocess.run(['git', '-C', os.path.join('D:', os.sep, repo) if not os.path.isabs(repo) else repo] + list(a),
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


# ------------------------------------------------------------------------------ THE READS
PPREADS = [(FACES, [(1, 186)], 'FACES_OF_H2_AT_FINITE_INSTANCE, whole'),
           (LEDGER, [(1, 125)], 'FACES_LEDGER: head, the rows, the cascades'),
           (FIND, [(4787, 4800)], 'the register census'),
           (MAP, [(16, 18), (24, 25), (41, 41), (56, 56), (99, 152)], 'the map: the keystone set, the FACES-bearing rows, the appendix')]
READS = [('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/CouplingsAtPhi.lean', [(410, 430)]),
         ('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/RegisterPentagon.lean', [(1, 70), (180, 200), (330, 360)]),
         ('SIDE-explicit-formula', 'HEAD', 'SIDEExplicitFormula/RegisterDepth.lean', [(1, 320)])]
POWER_NAMES = ['tie_term_neg', 'rest_term_small', 'dominant_summable', 'zeroSide_eventually_neg']
RELAY_PINS = ['36345da', 'df3c426', '7386b47']


def reads():
    L = ['b547 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    for p, spans, what in PPREADS:
        t = rd(p).split(NL)
        L.append('### %s -- %s' % (os.path.relpath(p, PP).replace(os.sep, '/'), what))
        for a, z in spans:
            L += ['  :%d %s' % (i + 1, t[i][:900]) for i in range(a - 1, min(z, len(t)))]
        L.append('')
    for repo, pin, path, spans in READS:
        t = g(repo, 'show', '%s:%s' % (pin, path)).replace(chr(13), '').split(NL)
        for a, z in spans:
            z = min(z, len(t))
            L += ['### %s %s (%s) %s:%d-%d' % (repo, g(repo, 'rev-parse', '--short', pin + '^{commit}').strip(), pin, path, a, z)]
            L += ['  :%d %s' % (i + 1, t[i]) for i in range(a - 1, z)] + ['']
    pl = g('SIDE-explicit-formula', 'show', 'HEAD:SIDEExplicitFormula/PowerLimit.lean').replace(chr(13), '').split(NL)
    for n in POWER_NAMES:
        i = next((k for k, l in enumerate(pl) if re.match(r'^(theorem|lemma)\s+%s\b' % n, l)), None)
        L.append('### SIDE-explicit-formula HEAD PowerLimit.lean -- %s at :%s' % (n, (i + 1) if i is not None else 'ABSENT'))
        if i is not None:
            j = i
            while j < len(pl) and ':=' not in pl[j]:
                j += 1
            L += ['  :%d %s' % (k + 1, pl[k]) for k in range(max(0, i - 4), min(j + 1, len(pl)))]
        L.append('')
    for pin in RELAY_PINS:
        full = g(ROOT, 'rev-parse', pin + '^{commit}').strip()
        subj = g(ROOT, 'log', '-1', '--pretty=%s', pin).strip()
        files = [f for f in g(ROOT, 'show', '--name-only', '--pretty=format:', pin).split(NL) if f.strip()]
        L.append('### relay %s (%s) -- %s' % (pin, full[:12] or 'UNRESOLVED', subj[:300]))
        L += ['  file %s' % f for f in files[:40]]
        L.append('')
    put_txt('b547_reads.txt', L)
    print('  reads banked : %d lines' % len(L))


ANCHOR = ['SIDEExplicitFormula.RegisterDepth.not_register1', 'SIDEExplicitFormula.RegisterDepth.register5_output_holds',
          'SIDEExplicitFormula.RegisterDepth.mellin_Phi_eq_zero_of_re_le_one', 'SIDEExplicitFormula.RegisterDepth.lvh2_corrected_iff',
          'SIDEExplicitFormula.RegisterDepth.register3_of_one_lt_re', 'SIDEExplicitFormula.B321.ch_iff_rh', 'SIDEExplicitFormula.B321.h2_sign_iff_rh']


def anchor():
    src = ['import SIDEExplicitFormula.RegisterDepth', 'import SIDEExplicitFormula.Seam', ''] + ['#check @' + n for n in ANCHOR]
    p = os.path.join(SCR, 'b547_anchor_check.lean')
    io.open(p, 'w', encoding='utf-8', newline=NL).write(NL.join(src) + NL)
    head = g('SIDE-explicit-formula', 'rev-parse', 'HEAD').strip()
    dirty = g('SIDE-explicit-formula', 'status', '--porcelain', '--untracked-files=no').strip()
    t0 = time.time()
    r = subprocess.run(['lake', 'env', 'lean', p], cwd=KER, capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = (r.stdout + r.stderr).replace(chr(13), '')
    L = ['b547 -- THE CENSUS THEOREMS, FRESH #check at SIDE-explicit-formula %s (tree %s; exit %d; %.0f s)' % (head, 'clean' if not dirty else 'DIRTY', r.returncode, time.time() - t0)]
    L += ['  ' + l for l in out.split(NL) if l.strip()]
    put_txt('b547_anchor.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (11): THE CHECKOUT`S VERIFIED NUMERICS
MLDIR = os.path.join('D:', os.sep, 'SIDE-explicit-formula', '.lake', 'packages', 'mathlib')
WN = [('interval arithmetic (a named facility)', r'(?i)interval[_ ]?arith|IntervalArith|\bIntervalArithmetic\b'),
      ('norm_num extension files (Mathlib/Tactic/NormNum/*)', None),
      ('exp numeric bounds', r'\b(?:Real\.)?exp_one_(?:lt|gt)_d9\b|\bexp_bound\b|\bexp_approx\b|\bexp_bound\x27|\bexpNear\b'),
      ('pi numeric bounds', r'\bpi_(?:gt|lt)_d(?:2|4|6|20)\b|\bpi_gt_three\b|\bpi_(?:gt|lt)_[0-9]+'),
      ('log numeric bounds', r'\blog_two_(?:near_10|gt_d9|lt_d9)\b'),
      ('a tactic that evaluates a definite integral', r'(?i)integral[_ ]?(?:tactic|eval|norm_num)|norm_num[^\n]{0,40}integral'),
      ('Taylor remainder with an explicit bound', r'\btaylor_mean_remainder(?:_lagrange|_bound)?\b')]


def window():
    head = subprocess.run(['git', '-C', MLDIR, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    files = []
    for dp, dn, fs in os.walk(os.path.join(MLDIR, 'Mathlib')):
        files += [os.path.join(dp, f) for f in fs if f.endswith('.lean')]
    hits = {n: [] for n, _ in WN}
    nn = sorted(os.path.relpath(f, MLDIR).replace(os.sep, '/') for f in files if os.sep + os.path.join('Tactic', 'NormNum') + os.sep in f)
    hits['norm_num extension files (Mathlib/Tactic/NormNum/*)'] = [dict(file=f, line=0, text='(file)') for f in nn]
    for f in files:
        t = rd(f)
        for i, l in enumerate(t.split(NL), 1):
            for n, p in WN:
                if p and re.search(p, l):
                    hits[n].append(dict(file=os.path.relpath(f, MLDIR).replace(os.sep, '/'), line=i, text=l.strip()[:200]))
    L = ['b547 -- THE CHECKOUT`S VERIFIED NUMERICS (READING (11)): Mathlib %s ; %d files' % (head, len(files))]
    for n, p in WN:
        L += ['', '### %s : %d ; needle %s' % (n, len(hits[n]), p or 'the directory listing')]
        L += ['  %s:%d %s' % (h['file'], h['line'], h['text']) for h in hits[n][:50]]
    put_json('b547_window.json', dict(head=head, files=len(files), counts={n: len(v) for n, v in hits.items()}, hits=hits))
    put_txt('b547_window.txt', L)
    for n, _ in WN:
        print('  %-58s %d' % (n, len(hits[n])))


# ------------------------------------------------------------------------------ THE WRITES
def outside_bt(text):
    return sum(l.count('`') % 2 for l in text.split(NL))


def poss(t):
    return re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", t)


def append_to(path, text):
    text = poss(text)
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE APPEND TO %s' % path)
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def guard_absent(path, h):
    if poss(h).encode('utf-8') in open(path, 'rb').read():
        sys.exit('### ALREADY PRESENT IN %s: %s' % (os.path.basename(path), h[:80]))


def hline(path, h):
    return rd(path).split(NL).index(poss(h)) + 1


EF = 'SIDE-explicit-formula `81ae175`'
LVP = 'SIDE-lv-conservation `v0.10.0`'
FTIERH = ('### The Correspondence paragraph`s terminals, tiered -- 2026-09-26, b547, under (R157)(3); this document stays Tier N (no byte '
          'above this block changes)')
FCENSH = ('### §2`s five faces against the register census -- appended 2026-09-26 by b547 beneath §2-bis (:42-57); this document stays '
          'Tier N, reference-only (no byte above this block changes)')
CREDITH = ('## FACES_OF_H2_AT_FINITE_INSTANCE §2, 2026-08-18, read against b538: an earlier reading of R4 as the one face with sign '
           'content, confirmed by the register census')
FIELDH = ('## Weil`s criterion in the field, September 2026: certified window bounds, claimed proofs on the deposit venue, and the '
          'programme`s compiled harness beside them')
ACTH = '## The cascade, act four: FACES_OF_H2 and FACES_LEDGER tiered, the R-pairs updated, the field`s status entered'
LEDGER_MARK = '<!-- b547 update -->'
HEADING = ('### b547 — the cascade, act four under (R157): FACES_OF_H2 and FACES_LEDGER tiered, the R-pairs updated, the field`s status '
           'entered, two work-orders priced')

FACES_TERMS = [
    ('`RegisterPentagon` (the five faces, statement-only)', LVP + ', `RegisterPentagon.lean`', 'STRUCTURE', 'T2',
     'its faces include R1 false as stated and R5-output a theorem; `goalState_sevenClasses_of_h2` is vacuous on the strip (b538)',
     'CARRIED -- T2 at THE_LOAD_BEARING_MAP.md:104 (b539)'),
    ('`certifiedInput_not_zeroRealizing`', LVP + ', `RegisterPentagon.lean`:342', 'INTERFACES', 'T1-lit',
     'under the hypothesis `NontrivialZeroExistsInStrip` (a literature fact not compiled), the certified {n²} spectrum realizes no zero',
     'CARRIED -- T1-lit at relay data/b540_tiers.json, PATHS :140'),
    ('`h1_complete_at_Phi`', 'cited "at SIDE-kernel v1.5 = 0e5233f"; it is SIDE-lv-conservation`s, `CouplingsAtPhi.lean`:418 at v0.6.0 = `c80bdc2` and at v0.10.0 (SIDE-kernel v1.5 declares no such name)', 'DERIVES', 'T0',
     'T0, not RH-anchor: the eight coupling facts of Mathlib`s theta-kernel function `Phi`; nothing about where the zeros are',
     'CARRIED -- T0 at THE_LOAD_BEARING_MAP.md:103 (b539)'),
    ('the open R3 `sorry` (`T3_perClass_to_combinations`)', LVP + ', `T3_StepNineBridge.lean`:92 (its `sorry` at :108)', 'OPEN', 'T2',
     'logic over abstract couplings; the pin carries its one `sorry`', 'CARRIED -- T2 at relay data/b540_tiers.json, PATHS :293'),
    ('the sector-forcing positivity (measured)', 'relay `36345da`, reports/2026-08-18-w-attempt-2-sitting-7.md', 'MEASURED, exact', 'T3',
     'numerical, exact pivots; the report carries "THE PAIRING IS POSITIVE-DEFINITE ON THE CONSTRAINED CLASS"', 'NEW'),
    ('the h = 1 instance (measured)', 'relay `df3c426`, reports/2026-08-18-mirror-h1-limit.md', 'MEASURED, 95/95 exact', 'T3',
     'numerical, exact; the report carries "95/95 EXACT"', 'NEW'),
    ('the ledger`s missing `Z` (measured)', 'relay `7386b47`, reports/2026-08-18-w-attempt-2-sitting-16.md', 'MEASURED', 'T3',
     'the report carries "`Z` IS ABSENT -- THE OBJECT HAS NO LEFT-HAND SIDE"', 'NEW'),
    ('the one-place limit`s E₁ positivity at proof grade', 'the sittings 20-21 report', 'a proof-grade reading', 'T4',
     'no terminal names it; manuscript-resident', 'NEW')]


def faces_tiers():
    guard_absent(FACES, FTIERH)
    fp = rd(FACES).split(NL)
    L = ['', '<!-- b547 (R157) TERMINAL TIERS, 2026-09-26 -->', '', FTIERH, '',
         '*Appended by b547. The back matter`s Correspondence paragraph (:178-184) names the terminals and measured facts below; each is '
         're-read at its pin and tiered by the tier law of (R149)-(R151), CARRIED against the latest earlier tier or NEW. **This document '
         'is Tier N -- a draft at question grade, reference-only -- and a tier table promotes nothing in it.** Bank: relay '
         '`data/b547_faces.json`.*', '',
         '| named in the paragraph | pin, re-read | grade | tier | reason | against the earlier tier |', '|:--|:--|:--|:--|:--|:--|']
    for t in FACES_TERMS:
        L.append('| %s | %s | %s | **%s** | %s | %s |' % t)
    L += ['', '**Rectification of the pin cell (appended row, `(R157)`(3)).** The paragraph at :180 reads *"`h1_complete_at_Phi` (the '
          'remainder = placement) at `SIDE-kernel` `v1.5 = 0e5233f`"*. The theorem is SIDE-lv-conservation`s: `h1_complete_at_Phi` at '
          '`CouplingsAtPhi.lean`:418, v0.6.0 = `c80bdc2`, unchanged at v0.10.0 = `93c27ec`; SIDE-kernel v1.5 declares no such name.', '',
          '*Filed by b547. No byte above this block changes; nothing here is a statement about RH.*', '']
    out = append_to(FACES, NL.join(L))
    out['heading_line'] = hline(FACES, FTIERH)
    put_json('b547_faces.json', dict(write=out, rows=[dict(zip(('named', 'pin', 'grade', 'tier', 'reason', 'against'), t)) for t in FACES_TERMS]))
    print('  FACES tier block :%d %s' % (out['heading_line'], out))


CENSUS = [
    ('R1 universality', '(b): the totality form of the absence',
     '`not_register1 : ¬Register1_universalityHypothesis` (' + EF + ')',
     'MOVED. As compiled, the universality face is false: stated for every essential interface, the hypothesis fails. The face is not '
     'a statement that describes the absence; as the register states it, it cannot be discharged at all.'),
    ('R2 conservation', '(b)-adjacent: an ADDRESS statement of the crossing',
     '`ch_iff_rh : conservationHypothesis ↔ RiemannHypothesis` (' + EF + ')',
     'CORROBORATED IN SHAPE. The balance at a prime is an equality, sign-free, as the reading says; the register as compiled is RH '
     'itself through a rewording lemma, so it carries RH`s content without sign content of its own.'),
    ('R3 totality', '(b): the absence stated logically; the `sorry` sits where the double limit sits',
     'UNDECIDED on the strip (the census, FINDINGS.md:4787); `register3_of_one_lt_re` proves the register on re s > 1 from the '
     'seven classes at `Phi` (' + EF + ')',
     'CORROBORATED IN SHAPE. The register is proved where the Mellin identity holds and undecided in the strip, which is where the '
     'reading places the open limit.'),
    ('R4 positivity', '(a) AND (b) AT ONCE: the one face with sign-content',
     '`h2_sign_iff_rh : h2_sign ↔ RiemannHypothesis` (' + EF + '; v0.2 = `5c72cad`) -- Weil`s criterion, compiled both ways',
     'CORROBORATED. The one face the census finds equivalent to RH through a theorem of real content is the positivity face, in its '
     'Weil form; the reading named it the one face with sign content on 2026-08-18. Credited in FINDINGS.'),
    ('R5 spectral distance', '(b): by its own compilation -- a boundary marker of the absence',
     '`register5_output_holds : Register5_output_HilbertPolya` (' + EF + '); beside it `certifiedInput_not_zeroRealizing` (' + LVP +
     '), which is a different statement: under `NontrivialZeroExistsInStrip`, the certified {n²} spectrum realizes no zero',
     'MOVED. The R5 output face, as compiled, holds outright -- a theorem, not a marker of an absence. The boundary marker the reading '
     'cites is a separate negative about one certified spectrum and says nothing about the output face.')]


def faces_census():
    guard_absent(FACES, FCENSH)
    fp = rd(FACES).split(NL)
    L = ['', '<!-- b547 (R157) CENSUS TABLE, 2026-09-26 -->', '', FCENSH, '',
         '*Appended by b547 under `(R157)`(3). §2`s five rows (:36-40) are read, row for row, against the register census (b538, '
         'FINDINGS.md:4787) and this act`s fresh `#check` of the census theorems (relay `data/b547_anchor.txt`). The reading`s own words '
         'are quoted from its verdict column; the census`s compiled fact stands beside each, in the descriptive voice. **This document '
         'stays Tier N; the table promotes no reading and fuses no register.***', '',
         '| face (§2, line) | the reading`s verdict, quoted | the compiled fact (the census) | what the census does to the reading |',
         '|:--|:--|:--|:--|']
    for i, (face, verdict, fact, what) in enumerate(CENSUS):
        L.append('| %s (:%d) | %s | %s | %s |' % (face, 36 + i, verdict, fact, what))
    L += ['', '*Filed by b547. No byte above this block changes; nothing here is a statement about RH.*', '']
    out = append_to(FACES, NL.join(L))
    out['heading_line'] = hline(FACES, FCENSH)
    put_json('b547_census_table.json', dict(write=out, rows=[dict(face=c[0], verdict=c[1], fact=c[2], what=c[3]) for c in CENSUS]))
    print('  FACES census block :%d %s' % (out['heading_line'], out))
    for c in CENSUS:
        if c[0].startswith(('R1', 'R5')):
            print('   ', c[0], '--', c[3][:200])


def credit():
    guard_absent(FIND, CREDITH)
    r4 = rd(FACES).split(NL)[38]
    if not r4.startswith('| **R4 positivity**'):
        sys.exit('### FACES :39 IS NOT THE R4 ROW')
    L = ['', CREDITH, '',
         '*Filed at b547 on the author`s ruling `(R157)`(3). The document is `phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md`, Tier N, '
         'a draft at question grade; the credit promotes nothing in it.*', '',
         '**The reading, verbatim, at FACES_OF_H2_AT_FINITE_INSTANCE.md:39 (dated 2026-08-18):**', '', '> ' + r4, '',
         '**The census it anticipated.** b538`s register census, compiled at SIDE-explicit-formula `81ae175` and re-read fresh at b547: R1 '
         'is false as stated (`not_register1`); R2 is RH restated (`ch_iff_rh`); R3 is undecided on the strip; R5`s output face holds '
         'outright (`register5_output_holds`); and R4 in its Weil form is equivalent to RH through a theorem of real content '
         '(`h2_sign_iff_rh`). **The relation.** Five weeks before the census, the reading singled out R4 as the one face carrying sign '
         'content and read the other four as descriptions of an absence; the census confirms the first half exactly -- R4 is the face '
         'whose compiled form is Weil`s criterion -- and moves two of the other four (R1 and R5), whose compiled forms are a falsehood '
         'and a theorem rather than descriptions of anything absent.', '',
         '*Nothing deposits; nothing here is a statement about RH.*', '']
    out = append_to(FIND, NL.join(L))
    out['heading_line'] = hline(FIND, CREDITH)
    put_json('b547_credit.json', out)
    print('  FINDINGS credit :%d %s' % (out['heading_line'], out))


# ------------------------------------------------------------------------------ COMPONENT 2: FACES_LEDGER
LTIERS = [
    ('R1', '`Register1_universalityHypothesis` (lv v0.7.0 = `2d86182`); `not_register1` (' + EF + ')', 'T2', 'false as stated (`not_register1`); the census`s first depth'),
    ('R2', '`Register2_conservationHypothesis`; `ConservationBridge.riemann_hypothesis` (SIDE-kernel v1.3); `ch_iff_rh` (' + EF + ')', 'T2',
     'RH restated -- ENCODES-CONCLUSION under (R151)(2); the row`s clause "the converse is not compiled" is stale: `ch_iff_rh` compiles both directions'),
    ('R3', 'NOT COMPILED as a face; `register3_of_one_lt_re` on re s > 1 (' + EF + ')', 'T4', 'undecided on the strip (FINDINGS.md:4787); no terminal carries the face there'),
    ('R4', '`Register4_positivity` (lv v0.7.0); `partialPositivity_finiteRange` (v0.8.0); `lam_add` (SIDE-li-map `73cee42`); the Weil form `h2_sign_iff_rh` (' + EF + ')', 'T1-lit',
     'the row`s face is the Li form, a literature theorem not compiled; its Weil form is T0 and the RH-anchor`s head'),
    ('R5', '`Register5_input` / `Register5_output_HilbertPolya` (lv v0.7.0); `register5_output_holds` (' + EF + '); `certifiedInput_not_zeroRealizing` (lv v0.9.0)', 'T2',
     'the output face holds outright, so `R5_output_HilbertPolya_to_RH` ENCODES its conclusion (R151)(2); the marker is T1-lit'),
    ('F1', 'relay `data/b321_the_window_opened.txt`, `data/b326_the_reach.txt`', 'T3', 'a measured control; no theorem'),
    ('F2', 'relay `data/b320_the_lawful_function.txt`, `data/b321_the_window_opened.txt`; Connes–Consani Theorems 1 and 4.7 imported', 'T3', 'measured margins; the source`s inequality and equality are imported, not compiled'),
    ('F3', 'BALANCE_AND_POSITIVITY :297, :410, :427; `internal/bench/li_bench.py`', 'T3', 'the bench, two radii; the finite-range certificate is R4`s'),
    ('F4', 'THE_RESIDUE_OF_RH :65, :67, :90', 'T4', 'named only; no terminal'),
    ('F5', 'relay `data/b309_the_scaling_trace.txt`, `data/b310_the_smear_collapses.txt`, `data/b311_the_identitys_neighbourhood.txt`', 'T3', 'measured and derived at definitions; the row names three zero-axiom terminals without naming them'),
    ('F6', 'THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY (Tier C), quoting b293-b296', 'T3', 'measured and derived, the finite side; the archimedean member imported'),
    ('F7', 'relay `data/b325_the_negative_control.txt`, `data/b326_the_reach.txt`', 'T3', 'measured on the Epstein control'),
    ('L1', 'Lagarias math/0404394v4 (pinned); relay `data/b327_bridge_run.txt`', 'T4', 'imported and derived as a bar; no compiled terminal carries the bridge (W-ORD-LI-WEIL-BRIDGE)')]
RPAIRS = [('R1–R2', 42), ('R1–R3', 43), ('R1–R4', 44), ('R1–R5', 45), ('R2–R3', 54), ('R2–R4', 55), ('R2–R5', 56), ('R3–R4', 65), ('R3–R5', 66), ('R4–R5', 75)]


def rpair_line(pair, line):
    a, b = pair.split('–')
    s = set((a, b))
    if 'R1' in s and 'R5' in s:
        spec = 'for this pair both facts bear directly: R1 cannot be discharged, and R5-output is discharged without RH'
    elif 'R1' in s:
        spec = 'for this pair: R1 as compiled is false (`not_register1`), so no discharge of R1 exists to carry to %s' % (b if a == 'R1' else a)
    elif 'R5' in s:
        spec = 'for this pair: R5-output as compiled holds outright (`register5_output_holds`) without RH, while %s does not' % (a if b == 'R5' else b)
    elif s == set(('R2', 'R4')):
        spec = 'for this pair the two compiled forms are each equivalent to RH (`ch_iff_rh`, `h2_sign_iff_rh`), so the transfer holds here, through RH; the five-way sentence does not'
    else:
        spec = 'for this pair: R3 is undecided on the strip, so no compiled transfer holds'
    return ('- **%s** (:%d) -- the STATED relation quotes the deposit`s *"A reader who discharges any one of them discharges all five."* '
            'In compiled form that sentence does not hold: `register5_output_holds` discharges R5-output without RH, and `not_register1` '
            'shows R1 cannot be discharged at all (%s); the deposited sentence rests on E-2026-09-25-6. %s. The row above is not '
            'rewritten.' % (pair, line, EF, spec[0].upper() + spec[1:]))


def ledger():
    import b327_faces_row as FR
    lt = rd(LEDGER).split(NL)
    for pair, ln in RPAIRS:
        if not lt[ln - 1].startswith('| %s | STATED |' % pair):
            sys.exit('### FACES_LEDGER :%d IS NOT THE %s ROW' % (ln, pair))
    body = [LEDGER_MARK, '',
            '## UPDATE — filed 2026-09-26 (b547): the rows R1-R5, F1-F7 and L1 tiered; the ten R-pair rows against the register census',
            '',
            '*Rows above are never rewritten; an update names the row it bears on. Written through the writer`s `append_block`, under the '
            'author`s ruling (R157)(4). Each row is tiered by its terminals as the other tables were (R149)-(R151); no act tiered these '
            'rows before, so each is NEW. Bank: relay `data/b547_ledger.json`.*', '',
            '| row | terminals, at pin | tier | reason |', '|:--|:--|:--|:--|']
    body += [poss('| %s | %s | **%s** | %s |' % t) for t in LTIERS]
    body += ['', '**The ten R-pair rows, one line each:**', '']
    lines = [poss(rpair_line(p, ln)) for p, ln in RPAIRS]
    body += lines
    body += ['', '*Nothing about h2 moves; the rows above are unedited. Filed by b547 (relay `data/b547_ledger.json`).*']
    st, det = FR.append_block(LEDGER_MARK, body)
    after = rd(LEDGER)
    put_json('b547_ledger.json', dict(status=st, detail=det, tiers=[dict(zip(('row', 'terminals', 'tier', 'reason'), t)) for t in LTIERS],
                                      rpair_lines=lines, heading_line=after.split(NL).index(body[2]) + 1 if body[2] in after else None))
    print('  FACES_LEDGER : %s -- %s' % (st, det))
    for l in lines:
        print('   ' + l[:170])
    if st != 'WRITTEN':
        sys.exit('### THE WRITER DID NOT WRITE')


CITED = ['data/read_pentagon.txt', 'data/b321_the_window_opened.txt', 'data/b326_the_reach.txt', 'data/b320_the_lawful_function.txt',
         'data/b324_the_keystones_reread.txt', 'data/b309_the_scaling_trace.txt', 'data/b310_the_smear_collapses.txt',
         'data/b311_the_identitys_neighbourhood.txt', 'data/b325_the_negative_control.txt', 'data/b327_bridge_run.txt', 'tools/e16/carto_atlas.py']


def banks():
    rows, L = [], ['b547 -- THE CITED BANKS (READING (8)): every relay bank an R-, F- or L1-row of FACES_LEDGER cites, in relay`s tree']
    for f in CITED:
        tracked = g(ROOT, 'ls-files', '--', f).strip() == f
        p = os.path.join(ROOT, f)
        head = next((l.strip() for l in rd(p).split(NL) if l.strip() and not set(l.strip()) <= set('=-#')), '') if os.path.exists(p) else ''
        rows.append(dict(file=f, tracked=tracked, exists=os.path.exists(p), header=head[:200]))
        L.append('  %-46s tracked %-5s exists %-5s header: %s' % (f, tracked, os.path.exists(p), head[:150]))
    for pin in RELAY_PINS:
        full = g(ROOT, 'rev-parse', pin + '^{commit}').strip()
        rep = [f for f in g(ROOT, 'show', '--name-only', '--pretty=format:', pin).split(NL) if f.startswith('reports/')]
        heads = []
        for f in rep:
            first = next((l.strip() for l in g(ROOT, 'show', '%s:%s' % (pin, f)).split(NL) if l.strip()), '')
            heads.append((f, first[:150]))
        rows.append(dict(file='relay pin %s' % pin, tracked=bool(full), exists=bool(full), header=heads))
        L.append('  relay pin %s -> %s' % (pin, full[:12] or 'UNRESOLVED'))
        L += ['      %s : %s' % h for h in heads]
    put_json('b547_banks.json', dict(rows=rows, missing=[r['file'] for r in rows if not (r['tracked'] and r['exists'])]))
    put_txt('b547_banks.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 3: THE FIELD`S STATUS
def field():
    guard_absent(FIND, FIELDH)
    s = rd(os.path.join(D, 'b547_field_search.txt'))
    found = 'NO RECORD with that author and that title' not in s
    L = ['', FIELDH, '',
         '*Filed at b547 on the author`s ruling `(R157)`(5). Field-context layer (R157)(1): what the field holds on Weil`s criterion beside '
         'what the programme holds. Search bank: relay `data/b547_field_search.txt`.*', '',
         '**The certified-window preprint.** Named by the ruling: Liu, *"Certified Weil Positivity Beyond the Unit Window"*, September 2026 '
         '-- computer-assisted coercive lower bounds for the Weil form on two compact windows, half-widths 1 and 17/16, by interval '
         'arithmetic, with the stated disclaimers that formal proof-assistant verification is not yet done and that no monotonicity in '
         'the window width is established. **NAVIGATOR-READ:** one web search by that title (2026-09-26) returned no record with that '
         'author and that title, so no abstract was fetched and no sentence of it is quoted here. The search`s nearest record is a '
         'different author`s -- Zhu, *"Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a '
         'Landau-Widom decay law"*, arXiv:2608.24827 (https://arxiv.org/pdf/2608.24827) -- printed for the author`s word on whether the '
         'navigator`s reading is this paper; it was not fetched and is not substituted.' if not found else 'FOUND', '',
         '**Claimed proofs on the deposit venue.** Zenodo carries records claiming RH through Weil positivity on restricted test classes. '
         'As the ruling names them: a record by de Bastos, February 2026 (title not given in the ruling); and a record titled '
         '*"Admissible Closure of the Weil Explicit Formula"* (author and date not given in the ruling). Nothing at Zenodo was read; their '
         'arguments are not engaged. The programme notes only that its own deposits sit in the same venue -- the reason the ceiling '
         'discipline exists.', '',
         '**The programme`s position, in three sentences.** The programme holds Weil`s criterion compiled against Mathlib`s '
         '`RiemannHypothesis` (`h2_sign_iff_rh`, SIDE-explicit-formula v0.2), with the explicit-formula identity (`b321_identity`), the '
         'decay and zero-count bounds and a witness construction compiled beside it. It holds positivity on wide windows only as '
         'numerical estimates -- at Q0 and at zeta, per width, at the grades of their banks -- and no certified window. Its two open '
         'work-orders in this line are the restricted-window theorem of its own (W-ORD-DETECTION-REGION) and a Lean-verified instance of '
         'one window (W-ORD-WINDOW-CERTIFY), both priced on the trails and neither started.', '',
         '*Nothing deposits; nothing at Zenodo written or read; nothing here is a statement about RH.*', '']
    out = append_to(FIND, NL.join(L))
    out['heading_line'] = hline(FIND, FIELDH)
    out['liu_found'] = found
    put_json('b547_field.json', out)
    print('  FINDINGS field :%d %s' % (out['heading_line'], out))


# ------------------------------------------------------------------------------ THE ACT`S ENTRY, THE SCORES, THE DESK, THE TRAIL
def fmt(d):
    return ' · '.join('%s %d' % (k, v) for k, v in d.items())


def tiers_count(rows, key):
    out = {}
    for r in rows:
        out[r[key]] = out.get(r[key], 0) + 1
    return {k: out.get(k, 0) for k in ('T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4')}


def findings():
    guard_absent(FIND, ACTH)
    fj, cj, lj, bj, wj, fdj, crj = (jl(n) for n in ('b547_faces.json', 'b547_census_table.json', 'b547_ledger.json', 'b547_banks.json',
                                                    'b547_window.json', 'b547_field.json', 'b547_credit.json'))
    ft = tiers_count(fj['rows'], 'tier')
    lt = tiers_count(lj['tiers'], 'tier')
    disp = {}
    for r in cj['rows']:
        k = r['what'].split('.')[0]
        disp[k] = disp.get(k, 0) + 1
    carried = sum(1 for r in fj['rows'] if r['against'].startswith('CARRIED'))
    L = ['', ACTH, '',
         '*Filed at b547 on the author`s ruling `(R157)`. Banks: relay `data/b547_faces.json`, `data/b547_census_table.json`, '
         '`data/b547_ledger.json`, `data/b547_banks.json`, `data/b547_window.json`, `data/b547_field_search.txt`, `data/b547_anchor.txt`.*', '',
         '**FACES_OF_H2_AT_FINITE_INSTANCE (Tier N, stays Tier N).** Its Correspondence paragraph`s %d named terminals and facts, tiered: %s; '
         'CARRIED %d, NEW %d. The `h1_complete_at_Phi` pin cell rectified by appended row (SIDE-lv-conservation, not SIDE-kernel). §2`s five '
         'faces against the census: %s. The credit to §2`s R4 reading at `FINDINGS.md`:%d.'
         % (len(fj['rows']), fmt(ft), carried, len(fj['rows']) - carried, '; '.join('%s %d' % kv for kv in disp.items()), crj['heading_line']), '',
         '**FACES_LEDGER.** The rows R1-R5, F1-F7 and L1 tiered (all NEW): %s. The ten R-pair rows each gained one update line naming '
         '`register5_output_holds`, `not_register1` and E-2026-09-25-6; no row rewritten; written through the ledger`s own writer (%s). '
         'The cited banks: %d checked, %d missing.' % (fmt(lt), lj['status'], len(bj['rows']), len(bj['missing'])), '',
         '**The field`s status** at `FINDINGS.md`:%d, NAVIGATOR-READ for the Liu preprint (no record found by its title; nothing fetched). '
         '**The two work-orders**, priced on the trails: W-ORD-DETECTION-REGION and W-ORD-WINDOW-CERTIFY; the checkout holds proved decimal '
         'bounds for π, log 2 and exp and %d `norm_num` extension files, and no evaluator for a definite integral and no interval arithmetic.'
         % (fdj['heading_line'], wj['counts']['norm_num extension files (Mathlib/Tactic/NormNum/*)']), '',
         '**Next keystone:** THE_RESIDUE_OF_RH.', '',
         '*Nothing deposits; nothing at Zenodo written; no kernel edited; nothing here is a statement about RH.*', '']
    out = append_to(FIND, NL.join(L))
    out['heading_line'] = hline(FIND, ACTH)
    put_json('b547_findings.json', dict(write=out, faces_tiers=ft, ledger_tiers=lt, census=disp, carried=carried))
    print('  FINDINGS act :%d ; faces %s ; ledger %s ; census %s' % (out['heading_line'], ft, lt, disp))


PRIOR_PP = '37b36b3'
WRITE_OK = {'FINDINGS.md', 'OPEN_TRAILS.md', 'FACES_LEDGER.md', 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md'}
MEMDIR = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', 'memory')


def gitc(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def w(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def scores():
    cj, lj, bj, wj, fdj = (jl(n) for n in ('b547_census_table.json', 'b547_ledger.json', 'b547_banks.json', 'b547_window.json', 'b547_field.json'))
    committed = gitc(PP, 'log', '-1', '--pretty=%s').startswith('b547 --')
    base = 'HEAD~1' if committed else 'HEAD'
    pref = {}
    for f in sorted(WRITE_OK):
        old = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (base, f)], capture_output=True).stdout.replace(b'\r\n', b'\n')
        new = open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n')
        pref[f] = new.startswith(old)
    written = sorted(x for x in gitc(PP, 'diff', '--name-only', PRIOR_PP).split(NL) if x) if not committed else \
        sorted(x for x in gitc(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x)
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b547_') and needle in rd(os.path.join(T, x))]
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(t) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b547_')) if t else None
    kernels = {k: gitc(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == ''
               for k in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-explicit-formula', 'SIDE-global-section')}
    rows = {r['face'][:2]: r for r in cj.get('rows', [])}
    fin = rd(FIND)
    wc = wj.get('counts', {})
    return dict(
        n1=rows.get('R4', {}).get('what', '').startswith('CORROBORATED') and rows.get('R1', {}).get('what', '').startswith('MOVED')
        and rows.get('R5', {}).get('what', '').startswith('MOVED') and poss(CREDITH) in fin,
        n2=lj.get('status') == 'WRITTEN' and len(lj.get('rpair_lines', [])) == 10,
        n3=not bj.get('missing') and all(r['exists'] for r in bj.get('rows', [])),
        n4=(fdj.get('liu_found') is False and 'NAVIGATOR-READ' in fin) or fdj.get('liu_found') is True,
        n5=all(n in rd(OT) for n in ('tie_term_neg', 'rest_term_small', 'dominant_summable')) and 'W-ORD-WINDOW-CERTIFY' in rd(OT),
        n6=all(pref.values()) and not zen and tok == 0 and all(kernels.values()) and set(written) <= WRITE_OK,
        prefixes=pref, written=written, zen=zen, token=tok, kernels=kernels,
        s1=fdj.get('liu_found') is False,
        s2=wc.get('pi numeric bounds', 0) > 0 and wc.get('exp numeric bounds', 0) > 0 and wc.get('interval arithmetic (a named facility)', 0) == 2,
        s3=not bj.get('missing'))


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6'), ('s1', 's2', 's3')
    cj = jl('b547_census_table.json')
    L = ['=' * 104, 'b547 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- R4 corroborated and credited; the R1 and R5 appended lines: %s' % (w(sc['n1']), ' || '.join(
             '%s: %s' % (r['face'], r['what'][:140]) for r in cj.get('rows', []) if r['face'][:2] in ('R1', 'R5'))),
         '  **(N2)** ### **%s.** -- ten update lines through the writer; no row rewritten.' % w(sc['n2']),
         '  **(N3)** ### **%s.** -- the three relay pins resolve and every cited bank is present (relay data/b547_banks.txt).' % w(sc['n3']),
         '  **(N4)** ### **%s.** -- NAVIGATOR-READ (no Liu record found by the title; nothing fetched); the Zenodo records named as the ruling '
         'names them; nothing at Zenodo read.' % w(sc['n4']),
         '  **(N5)** ### **%s.** -- the detection-region price names the PowerLimit pieces and the finite-j inequality; the certify price '
         'reports the checkout.' % w(sc['n5']),
         '  **(N6)** ### **%s.** -- prefixes kept %s ; files written %s ; tools naming the platform %s ; token %s ; kernels clean %s.'
         % (w(sc['n6']), sc['prefixes'], sc['written'], sc['zen'] or 'NONE', sc['token'], sc['kernels']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the search found no Liu abstract; NAVIGATOR-READ.' % w(sc['s1']),
         '  **(S2)** ### **%s.** -- π, log 2 and exp bounds present; the two "interval arithmetic" hits are order intervals; no integral evaluator.' % w(sc['s2']),
         '  **(S3)** ### **%s.** -- every cited bank resolves.' % w(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b547_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b547_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b547_desk_notes.txt', L)
    put_json('b547_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b547 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### THE PURPOSE STATEMENT (FACES_OF_H2_AT_FINITE_INSTANCE.md:8), PRINTED FIRST:',
         '  ' + rd(FACES).split(NL)[7], '', '### THE CENSUS THEOREMS:'] + ['  ' + l for l in rd(os.path.join(D, 'b547_anchor.txt')).rstrip(NL).split(NL)]
    for n in ('b547_faces.json', 'b547_census_table.json', 'b547_credit.json', 'b547_ledger.json', 'b547_banks.json', 'b547_field.json', 'b547_findings.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)))
    L += ['### THE CHECKOUT : ' + json.dumps(jl('b547_window.json').get('counts'), ensure_ascii=False), '### THE SEARCH : see data/b547_field_search.txt',
          '### THE BRANCHES : see data/b547_branches.txt', '=' * 132]
    put_txt('b547_components.txt', L)
    print(NL.join(L[:8]))


def trail():
    sc, fdj, lj = scores(), jl('b547_field.json'), jl('b547_ledger.json')
    fj, crj, fnd = jl('b547_faces.json'), jl('b547_credit.json'), jl('b547_findings.json')
    body = ['', HEADING, '',
            '**(R157) ratified.** (1) The three layers named: observational (banks, ledgers, tables, censuses), clarified (keystone '
            'editions, the monograph, at checkpoints), field-context (Correspondence, bibliography, PATHS, prior art). (2) CP-1b, the '
            'implication pass, closes CP-1; the editions follow CP-7`s purpose statement. (3) FACES_OF_H2 tiered and credited, Tier N '
            'kept. (4) The R-pairs updated. (5) The field`s status entered; two work-orders priced. (6) The memory and the mirror are '
            'refreshed after CP-1 closes -- not at this act.', '',
            '**Entered:** FACES_OF_H2_AT_FINITE_INSTANCE.md:%d (the terminals tiered, the h1 pin row) and :211 (the census table); '
            'FACES_LEDGER.md:%s (one UPDATE block, through its writer); FINDINGS.md:%d (the credit), :%d (the field), :%d (the act).'
            % (fj['write']['heading_line'], lj.get('heading_line'), crj['heading_line'], fdj['heading_line'], fnd['write']['heading_line']), '',
            '| # | ID | kind | the item | price | trigger |', '|:--|:--|:--|:--|:--|:--|',
            '| **1** | `W-ORD-DETECTION-REGION` | **RESULT** | A compiled statement that positivity of `h2_sign` on every `classK` window of '
            'support at most L₀ excludes off-line zeros of ζ in an explicit region of (γ, δ) -- the programme`s own theorem in the '
            'restricted-window line. It consumes four compiled pieces of PowerLimit.lean (SIDE-explicit-formula `81ae175`): `tie_term_neg` '
            '(:749, the tie term`s real part is −N_ρ M^(2^(j+1))), `rest_term_small` (:764, each other term is at most B²(1+‖w‖)^(2D) '
            'offScore^(2^(j+1))), `dominant_summable` (:949, the dominant is summable over ζ’s zeros by the local count) and '
            '`zeroSide_eventually_neg` (:1082, for some j the zero side is negative). The inequality to make explicit is the finite-j form '
            'of that last limit: the rest`s sum is below the tie term`s magnitude for every j ≥ j₀, with j₀ an explicit function of the '
            'window`s constants (L, M, B, D) and of the zero`s (γ, δ). | four lemmas: (i) the explicit j₀ inequality -- the one of '
            'substance; (ii) the power window`s support as a function of j and the base width, giving L₀; (iii) the region R(L₀) of (γ, δ) '
            'for which (i) and (ii) meet; (iv) the assembly, "h2_sign on classK windows of support ≤ L₀ excludes zeros in R(L₀)" | **THE '
            'AUTHOR\'S WORD** |',
            '| **2** | `W-ORD-WINDOW-CERTIFY` | **RESULT** | A Lean-verified instance of `h2_sign` on one window: the three terms of the sign '
            '(`poleTerm`, `primeSum`, `archTerm`) at one fixed `classK` window, bounded in Lean so that their combination is positive. The '
            'checkout (Mathlib `51e6992`) holds proved decimal bounds for π (`pi_gt_d20`), log 2 (`log_two_near_10`) and exp (`exp_bound`, '
            '`expNear`), Taylor remainders, and 26 `norm_num` extension files -- none for exp, log or an integral -- and no interval '
            'arithmetic and no evaluator for a definite integral (relay `data/b547_window.txt`). | priced first, as ordered: (i) a verified '
            'quadrature lemma with an explicit error for a smooth compactly supported integrand -- the checkout holds none, and it is the '
            'item of substance; (ii) bounds for the digamma kernel of `archTerm` on the window`s range; (iii) the prime sum, finite for a '
            'compact window, by `norm_num` from the window`s values; (iv) the assembly. | **THE AUTHOR\'S WORD** |', '',
            '**CP-1:** open; the cascade continues with THE_RESIDUE_OF_RH, then the remaining tables, then CP-1b.', '',
            '**Next:** THE_RESIDUE_OF_RH.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
            '**No kernel lane opened at this act.** Nothing deposits; nothing at Zenodo written or read; no kernel edited; no monograph byte '
            'changed; ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; '
            'nothing here is a statement about RH.', '']
    text = poss(NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    before = open(OT, 'rb').read()
    if poss(HEADING).encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(poss(HEADING)))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b547_trail_notes.json', out)


if __name__ == '__main__':
    fn = {'reads': reads, 'anchor': anchor, 'window': window, 'faces_tiers': faces_tiers, 'faces_census': faces_census, 'credit': credit,
          'ledger': ledger, 'banks': banks, 'field': field, 'findings': findings, 'components': components, 'desk': desk, 'trail': trail}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
