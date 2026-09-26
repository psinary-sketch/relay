# -*- coding: utf-8 -*-
"""b541_record.py -- THE MONOGRAPH READ AGAINST THE RH-ANCHOR, ACT ONE: THE RECORD, UNDER (R151).
### `python tools/b541_record.py purpose | file | law | census | erratum5 | map | components | desk | trail`

### The monograph is READ, never written. Every selected sentence meets exactly one typed row or the declared default
### (READING (3)); a carried b532 row must agree with b532's verdict unless marked MOVED. ERRATA takes one append and one
### bullet; the map one append; FINDINGS two appends; OPEN_TRAILS one. This file deletes nothing.
"""
import hashlib, io, json, os, re, subprocess, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
LIVE = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
ERR = os.path.join(PP, 'ERRATA.md')
MAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
FIND = os.path.join(PP, 'FINDINGS.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
SCR = os.environ.get('B541_SCRATCH', '')
NL = chr(10)
HALT = '## 26.1'
MAPH = '### The tier law, (R151)(2), 2026-09-25 (appended by b541; the lines above are unedited)'
R5T = "## The deposited R5-output face is a theorem: its disclaimer disclaims a theorem ((R151)(3), 2026-09-25)"
FTITLE = '## A Place To Stand read against the RH-anchor: the sentence census and the chapter tier map, act one'
HEADING = ('### b541 — the monograph read against the RH-anchor, act one of two under (R151): E-2026-09-25-4 filed, the census '
           'to §25.8, E-2026-09-25-5 drafted, the chapter tier map')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def append_to(path, text):
    text = re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", text)
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE APPEND TO %s' % path)
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def outside_bt(text):
    return sum(l.count('`') % 2 for l in text.split(NL))


# ------------------------------------------------------------------------------ reads
ANCHOR = ['SIDEExplicitFormula.B321.h2_sign_iff_rh', 'SIDEExplicitFormula.B321.ch_iff_rh', 'SIDEExplicitFormula.RegisterDepth.not_register1',
          'SIDEExplicitFormula.RegisterDepth.mellin_Phi_eq_zero_of_re_le_one', 'SIDEExplicitFormula.RegisterDepth.lvh2_corrected_iff',
          'SIDEExplicitFormula.RegisterDepth.register5_output_holds', 'SIDEExplicitFormula.B321.b321_identity', 'SIDEExplicitFormula.B321.not_f4_needs']


def purpose():
    live, dep = rd(LIVE).split(NL), rd(DEP)
    b532 = next((l.strip() for l in rd(os.path.join(D, 'b532_extract.txt')).split(NL) if 'Zenodo 21539167 serves md5' in l), '')
    src = ['import SIDEExplicitFormula.RegisterDepth', ''] + ['#check @' + n for n in ANCHOR]
    p = os.path.join(SCR, 'b541_anchor_check.lean')
    io.open(p, 'w', encoding='utf-8', newline=NL).write(NL.join(src) + NL)
    head = subprocess.run(['git', '-C', KER, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    r = subprocess.run(['lake', 'env', 'lean', p], cwd=KER, capture_output=True, text=True, encoding='utf-8', errors='replace')
    L = ['b541 -- THE READS PRINTED BEFORE ANY WRITE', '',
         'the live monograph : day1/A_Place_to_Stand.md:19  %s' % live[18],
         '  md5 %s ; %d lines' % (md5(LIVE), len(live)),
         'the deposited copy : outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md  md5 %s' % md5(DEP),
         '  b532`s bank (data/b532_extract.txt) : %s' % b532, '',
         'the RH-anchor, fresh #check at SIDE-explicit-formula %s (exit %d):' % (head, r.returncode)]
    L += ['  ' + l for l in r.stdout.replace(chr(13), '').split(NL) if l.strip()]
    io.open(os.path.join(D, 'b541_reads.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:8]))
    print('  anchor #check lines : %d ; exit %d' % (len([l for l in r.stdout.split(NL) if re.match(r'^@?SIDEExplicitFormula\.\S+ :', l)]), r.returncode))


# ------------------------------------------------------------------------------ COMPONENT 1
STATUS4 = ("**Filed 2026-09-25 by b541, the monograph read's first act, on the author's ruling (R151)(1), as drafted at relay "
           "data/b540_erratum_draft.md, its bytes unchanged; the Status line's words \"DRAFT. Not filed.\" above are the draft's, retained "
           "as drafted. The whole-monograph read of (R151)(4) may extend this entry by a further entry, never by editing it.**")
BULLET4 = ("- `E-2026-09-25-4` — *DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2* (appended to this list by b541 under `(R151)`(1))")


def file():
    raw = open(ERR, 'rb').read()
    if b'## E-2026-09-25-4 ' in raw:
        sys.exit('### E-2026-09-25-4 IS ALREADY IN ERRATA -- REFUSING TO FILE IT TWICE.')
    lines = raw.decode('utf-8').split(NL)
    k = next(i for i, l in enumerate(lines) if l.startswith('- `E-2026-09-25-3` —'))
    before_lines = list(lines)
    lines = lines[:k + 1] + [BULLET4] + lines[k + 1:]
    open(ERR, 'wb').write(NL.join(lines).encode('utf-8'))
    kept = [l for i, l in enumerate(lines) if i != k + 1] == before_lines
    draft = io.open(os.path.join(D, 'b540_erratum_draft.md'), encoding='utf-8').read()
    w = append_to(ERR, NL + draft.rstrip(NL) + NL + NL + STATUS4 + NL)
    t = rd(ERR).split(NL)
    first = next(i for i, l in enumerate(t) if l.startswith('## E-2026-09-25-4 ')) + 1
    last = next(i for i, l in enumerate(t) if l.startswith('**Filed 2026-09-25 by b541')) + 1
    entry = NL.join(t[first - 1:last])
    res = dict(bullet_line=k + 2, prior_lines_kept=kept, append=w, entry_lines=[first, last], entry_equals_draft=(draft.rstrip(NL) in entry),
               backticks_outside_code=outside_bt(entry))
    put_json('b541_file.json', res)
    print('  bullet at ERRATA.md:%d (prior lines kept %s) ; E-2026-09-25-4 at ERRATA.md:%d-%d ; draft carried %s ; backticks outside code %d'
          % (k + 2, kept, first, last, res['entry_equals_draft'], res['backticks_outside_code']))


# ------------------------------------------------------------------------------ COMPONENT 2
def law():
    M = ['', '<!-- b541 (R151) TIER-LAW LINE, 2026-09-25 -->', '', MAPH, '',
         '- **`(R151)`(2), 2026-09-25:** T1-open requires the premise to be **EQUIVALENT-DEEP** to RH in the sense of b538`s census -- a '
         'theorem stands between it and RH -- and `h2_sign` is the one such premise the corpus holds. A premise **EQUIVALENT-REWORDING** '
         '(`ConservationHypothesis`, by `ch_iff_rh`; `Register5_output_HilbertPolya → RiemannHypothesis`, since '
         '`Register5_output_HilbertPolya` is a theorem, `register5_output_holds`) makes its terminal ENCODES-CONCLUSION and **T2**; '
         'b540`s readings of Route 3 and of `R5_output_HilbertPolya_to_RH` stand, and `(R150)`(3)`s parenthesis is corrected by it.', '']
    w1 = append_to(MAP, NL.join(M))
    F = ['', R5T, '',
         '*Entered at b541 on the author`s ruling `(R151)`(3), beside the register census (`FINDINGS.md:4787`).* **R5-output, as the deposit '
         'stated it in Lean, holds outright**: `register5_output_holds : Register5_output_HilbertPolya` (SIDE-explicit-formula '
         'RegisterDepth.lean at `81ae175`, standard three), witnessed by the constant pairing 1, the diagonal operator, and an '
         'enumeration of the countably many real parts of the nontrivial zeros (`zeta_zeros_countable`). So the deposit`s disclaimer '
         'of that face disclaims a theorem, and the Hilbert–Pólya content the disclaimer meant -- the ordinates as the spectrum of a '
         'self-adjoint operator on a Hilbert space -- is not in the sentence. The bridge `R5_output_HilbertPolya_to_RH` therefore takes '
         'RH itself as its premise and is ENCODES-CONCLUSION, T2 (`(R151)`(2)). The deposited §27.3 sentence disclaiming it is read at '
         'the act after (the monograph read`s second act).', '']
    w2 = append_to(FIND, NL.join(F))
    w2['heading_line'] = rd(FIND).split(NL).index(R5T) + 1
    put_json('b541_law.json', dict(map=w1, findings=w2))
    print('  map : %d bytes appended, prefix %s ; FINDINGS R5 entry at line %d' % (w1['added'], w1['prefix'], w2['heading_line']))


# ------------------------------------------------------------------------------ COMPONENT 3: the census
PAT = [('route', r'\b[Rr]outes?\b'), ('register', r'\b[Rr]egisters?\b'), ('h1/h2', r'\bh[12]\b'), ('goal state', r'goal[ -]state|goal ⇐'),
       ('machine-verified', r'[Mm]achine-verified|machine verified|machine-checked'), ('reduction', r'\b[Rr]eduction\b|\breduces\b'),
       ('complete', r'\b[Cc]omplete\b'), ('compiled', r'\b[Cc]ompiled\b'), ('exhaustive', r'\b[Ee]xhaustive(ness)?\b'),
       ('one open premise', r'one open premise|the one premise|single open premise'),
       ('named terminal', r'`[A-Za-z_][A-Za-z0-9_]*(?:[._][A-Za-z0-9_₀]+)+`')]
RUN1 = dict(yields={'route': 67, 'register': 26, 'h1/h2': 20, 'goal state': 6, 'machine-verified': 9, 'reduction': 16, 'complete': 28,
                    'compiled': 35, 'exhaustive': 71, 'one open premise': 4, 'named terminal': 94}, read=2600, selected=282, act_one=172)
DEFAULT_HITS = {'exhaustive', 'complete', 'reduction'}


def segs(lines):
    out, cur, start = [], [], None
    for i, l in enumerate(lines, 1):
        if re.match(r'^\s*(- |\* |```|#|>|\d+\. )', l) or not l.strip() or l.startswith('|'):
            if cur:
                out.append((start, ' '.join(cur)))
            cur, start = [], None
            if l.strip() and not l.strip().startswith('```'):
                out.append((i, l.strip()))
            continue
        if start is None:
            start = i
        cur.append(l.strip())
    if cur:
        out.append((start, ' '.join(cur)))
    return out


def census_of(path):
    rows, chap, top = [], None, 'front matter'
    for ln, seg in segs(rd(path).split(NL)):
        if seg.startswith('# ') and not seg.startswith('# Verify') and not seg.startswith('# Expected'):
            top = seg[2:70]
        if seg.startswith('# ') or seg.startswith('## '):
            chap = seg[:60]
        parts = [seg] if seg.startswith('|') else [p for p in re.split(r'(?<=[.!?])\s+(?=[A-Z*`(\[])', ' '.join(seg.split())) if p.strip()]
        for s in parts:
            rows.append(dict(line=ln, section=chap, chapter=top, sentence=s, hits=[n for n, p in PAT if re.search(p, s)]))
    sel = [r for r in rows if r['hits']]
    stop = next(i for i, r in enumerate(sel) if r['section'] and r['section'].startswith(HALT))
    return rows, sel, stop


def nz(s):
    return ' '.join(re.sub(r'[*`_]', '', s).split())


E1, E3, E4, E5, E914, E922 = 'E-2026-09-25-1', 'E-2026-09-25-3', 'E-2026-09-25-4', 'E-2026-09-25-5', 'E-2026-09-14-1', 'E-2026-09-22-1'
S1 = 'Route 3 counted as a route to σ = 1/2 or as a route of the verification: its premise ConservationHypothesis is RH restated (ch_iff_rh) -- E-2026-09-25-1`s subject'
RT = 'the route terminals'
# (src, line, needle, grade, tier, errata, subject, reason, replacement, carried)
GR = [
    ('L', 68, 'machine-checked redundancy', 'RESTS', 'T2', [E5], E1, S1,
     "The Lean kernel provides machine-checked companions to the argument's surround -- its route terminals, one of which (Route 3) is the implication from a premise that is RH restated (ch_iff_rh) -- not a second, redundant proof.", ''),
    ('L', 117, 'Formal verification:', 'RESTS', 'T2', [E5], E1,
     S1 + '; the terminals do not compose into RH under h2 in the deposited kernel',
     "Formal verification: the Lean 4 kernel checks the route terminals at their pins, each at zero sorry and zero custom axioms; they do not compose into RH -- Route 3's premise is RH restated (ch_iff_rh) -- and the named premise h2 is, in its Weil form, equivalent to RH (h2_sign_iff_rh, SIDE-explicit-formula v0.2).", ''),
    ('L', 117, 'The sorry-free core', 'STANDS', 'T2', [], '', 'b532 M-01: an inventory of route terminals and their profiles', '', 'M-01'),
    ('L', 125, 'The proof has one architecture', 'RESTS', 'T2', [E5], E1, S1,
     "The proof has one architecture applied through several layers -- seven mechanism classes, five identification paths, five closures, two strategies, three compiled route terminals (Route 3's premise RH restated, ch_iff_rh), and one open premise, RH-equivalent in its Weil form (h2_sign_iff_rh).", ''),
    ('L', 203, 'identified by five **convergent** routes', 'STANDS', 'T2', [], '', 'the corrected (2026-08-10) reading: convergent identifications sharing the involution', '', ''),
    ('L', 215, 'These five routes share no assumptions', 'STANDS', 'T4', [], '', 'the five identification paths, a manuscript reading', '', ''),
    ('L', 215, 'No route references any other', 'STANDS', 'T4', [], '', 'a manuscript reading', '', ''),
    ('L', 720, 'A reader who wants the destination', 'STANDS', 'T4', [], '', 'navigation', '', ''),
    ('L', 825, 'The Silence Principle is compiled', 'STANDS', 'T2', [], '', '`silence_universal` is stated per interface, as said (abstract lemma)', '', ''),
    ('L', 825, 'ten additional instances', 'STANDS', 'T2', [], '', 'instances compiled, as said', '', ''),
    ('L', 825, 'This hypothesis is one of five registers', 'RESTS', 'T2', [E5], '',
     'the register as stated -- every essential interface is universal -- is FALSE-AS-STATED (not_register1, b538)',
     "This hypothesis is the first of §27.3's five registers; stated universally, as the register states it, it is false (not_register1, SIDE-explicit-formula RegisterDepth.lean at 81ae175): an interface whose essentiality is an uninterpreted Prop need not be universal, so the register as stated is not a face of the premise.", ''),
    ('L', 827, 'distributive law is Mathlib', 'STANDS', 'T0', [], '', 'Mathlib`s mul_add; T0, not RH-anchor', '', ''),
    ('L', 1125, 'The five PATHS each independently identify', 'STANDS', 'T4', [], '', 'identification paths, a manuscript reading', '', ''),
    ('L', 1168, 'ledger`s sign structure'.replace('`', "'"), 'STANDS', 'T0', [], '', 'vonMangoldt_nonneg is Mathlib`s; T0, not RH-anchor', '', ''),
    ('L', 1349, 'This result is formally verified in Lean 4 as', 'RESTS', 'T0', [E5], '',
     'spectral_cannon states (deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0: its object is Mathlib`s completedRiemannZeta₀, not ξ',
     "This result is formally verified in Lean 4 as spectral_cannon: (deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0 for all real t -- the derivative of Mathlib's completedRiemannZeta₀, the entire part of the completed zeta -- compiled against Mathlib with zero sorry; the same fact for ξ′ is not compiled.", ''),
    ('L', 1395, 'Of these, C₁ derives', 'STANDS', 'T2', [], '', 'the derivative engine`s per-class reduction, as said', '', ''),
    ('L', 1421, 'the fifth independent route to σ = 1/2', 'STANDS', 'T4', [], '', 'the R-curve path as a manuscript route; its compiled part is one direction (T2)', '', ''),
    ('L', 1451, 'The R-curve path provides a fifth', 'STANDS', 'T4', [], '', 'a manuscript reading', '', ''),
    ('L', 1503, 'The geometric clause (canonical statement)', 'RESTS', 'T0', [E5], '',
     'the compiled perpendicular crossing is about completedRiemannZeta₀ (spectral_cannon), not ξ′',
     "The geometric clause (canonical statement). A zero ρ = ½ + iγ is simple iff ξ'(ρ) ≠ 0; by the perpendicular crossing (the derivative of completedRiemannZeta₀ is imaginary on the line, compiled as spectral_cannon; the same holds of ξ′, not compiled) this is Im ξ'(ρ) ≠ 0 -- uniform transversality.", ''),
    ('L', 1503, 'The five lines of the table', 'STANDS', 'T2', [], '', 'evidence, not proof, as said', '', ''),
    ('L', 1503, 'The mechanism catalogue reduces it per-class', 'STANDS', 'T2', [], '', 'as said', '', ''),
    ('L', 1530, '**Deposit (current: v1.5', 'RESTS', 'T2', [E5], '',
     'MOVED from b532`s STANDS (M-06): the product-formula chain it lists names ProductFormula_Prime.lean, at no version of SIDE-kernel (v1.0-v1.7, HEAD)',
     "... the product-formula chain (ProductFormula_Int.lean, ProductFormula_Rat.lean -- the ProductFormula_Prime.lean named here is at no version of the kernel) ...", 'M-06*'),
    ('L', 1532, 'The three classical theorems mathematically supporting', 'STANDS', 'T2', [], '', 'as said, the Stein pillar set aside open', '', ''),
    ('L', 1534, 'The CartanBBridge module also realigns', 'STANDS', 'T0', [], '', 'Mathlib API names, resolved', '', ''),
    ('L', 1538, 'The kernel formalizes three independent routes to σ = 1/2', 'RESTS', 'T2', [E5], E1, S1,
     "The kernel formalizes three route terminals, each compiled separately; Route 3's is the implication from ConservationHypothesis, which is RH restated (ch_iff_rh, E-2026-09-25-1).", ''),
    ('L', 1538, 'three routes, three theorems, one conclusion', 'RESTS', 'T2', [E5], E1, S1,
     "The kernel realizes this signature in part -- three route terminals, of which Route 3's conclusion is its premise restated (ch_iff_rh) and Route 2's is a fact about completedRiemannZeta₀ on the line.", ''),
    ('L', 1544, '**The Product Formula.** Three files', 'RESTS', 'T2', [E5], '',
     'ProductFormula_Prime.lean is at no version of SIDE-kernel (v1.0-v1.7, HEAD)',
     "The Product Formula. Two files -- ProductFormula_Int.lean and ProductFormula_Rat.lean -- on the product of the archimedean and p-adic absolute values; the ProductFormula_Prime.lean the deposited text names is at no version of the kernel.", ''),
    ('L', 1544, 'Proved using Mathlib', 'STANDS', 'T0', [], '', 'Mathlib names, resolved', '', ''),
] + [('L', ln, nd, 'STANDS', 'T2', [], '', 'a voice file and its terminal, named; a model statement (three voices one map, voice6 ENCODES, voice7 a stand-in)', '', '')
     for ln, nd in ((1551, 'Voice2'), (1552, 'Voice3 |'), (1553, 'Voice3b'), (1554, 'Voice5'), (1555, 'Voice6'), (1556, 'Voice7'))] + [
    ('L', 1558, '**The Formation Count.**', 'STANDS', 'T2', [], '', 'arithmetic by decide, as said', '', ''),
    ('L', 1560, '**The Perpendicular Crossing Probe.**', 'RESTS', 'T0', [E5], '',
     'the file proves deriv completedRiemannZeta₀ s = -(deriv completedRiemannZeta₀ (1 - s)) and the line fact for completedRiemannZeta₀ (proved_infrastructure, spectral_cannon); the sentence writes both as ξ′',
     "The Perpendicular Crossing Probe. Kernel/PerpendicularCrossing.lean proves that the derivative of Mathlib's completedRiemannZeta₀ -- the entire part of the completed zeta -- satisfies f′(s) = −f′(1−s) (deriv_fe) and Re f′(1/2 + it) = 0 for all real t (SpectralCannonFull.spectral_cannon); the same statements for ξ′ are not compiled.", ''),
    ('L', 1560, 'schwarz_deriv', 'STANDS', 'T2', [], '', 'as said', '', ''),
    ('L', 1562, '**The RH-reduction theorem.**', 'STANDS', 'T2', [], '', 'it names Integration.StructuralExhaustiveness a direct restatement of RH', '', ''),
    ('L', 1567, 'This is one of the building blocks of Route 3', 'STANDS', 'T2', [], '', 'b532 M-07', '', 'M-07'),
    ('L', 1567, 'is a different proposition', 'STANDS', 'T2', [], '', 'distinguishes Route 1`s proposition, as said', '', ''),
    ('L', 1571, 'The standard pattern for major theorems', 'STANDS', 'T4', [], '', 'a manuscript reading', '', ''),
    ('L', 1573, 'Three routes compile independently in Lean', 'STANDS', 'T2', [], '', 'b532 M-08', '', 'M-08'),
    ('L', 1577, 'The kernel`s core is a three-file chain'.replace('`', "'"), 'RESTS', 'T2', [E5], '',
     'prod_prime_power_absValues, prod_int_absValues, prod_rat_absValues and conservation_certificate are at no version of SIDE-kernel and in no local repository; ProductFormula_Prime.lean likewise',
     "The kernel's core is a product-formula chain in ProductFormula_Int.lean and ProductFormula_Rat.lean, the Rat file ending in conservation_of_spectra, stated as ∀ s : ℤ, (1 : ℚ) ^ s = 1 (a STIPULATION: the conservation reading is carried by the name); the terminals prod_prime_power_absValues, prod_int_absValues, prod_rat_absValues and conservation_certificate named in the deposited text are at no version of the kernel.", ''),
    ('L', 1579, '## 25.5 The Three Compiled Routes', 'STANDS', 'T2', [], '', 'a heading; the route terminals are compiled', '', ''),
    ('L', 1581, 'The kernel formalizes three routes to σ = 1/2.', 'RESTS', 'T2', [E5], E1, S1, "The kernel formalizes three route terminals.", ''),
    ('L', 1581, 'Each is independently compiled.', 'STANDS', 'T2', [], '', 'as said', '', ''),
    ('L', 1583, '**Route 1 — Structural Exhaustion.**', 'STANDS', 'T2', [], '', 'Route 1`s conjunction, as defined', '', ''),
    ('L', 1589, 'The conjunction is proved unconditionally', 'STANDS', 'T2', [], '', 'it is proved; its catalogue conjunct is a decide count (the On Route 1 note)', '', ''),
    ('L', 1589, 'The route uses `MechanismClass`', 'STANDS', 'T2', [], '', 'as said', '', ''),
    ('L', 1591, '**Route 2 — Codimension / Spectral Cannon.**', 'STANDS', 'T0', [], '', 'the chain compiles; T0, not RH-anchor', '', ''),
    ('L', 1597, 'This route uses complex analysis on ξ directly.', 'RESTS', 'T0', [E5], '',
     'the route`s compiled object is completedRiemannZeta₀, not ξ',
     "This route uses complex analysis on Mathlib's completedRiemannZeta₀, the entire part of the completed zeta, not on ξ.", ''),
    ('L', 1599, '**Route 3 — Conservation.**', 'RESTS', 'T2', [E1], E1, 'b532 M-09, listed in E-2026-09-25-1', '', 'M-09'),
    ('L', 1605, 'by combining Conservation with Voice 1', 'STANDS', 'T2', [], '', 'describes the chain', '', ''),
    ('L', 1607, '**Three routes, three theorems, one conclusion.**', 'RESTS', 'T2', [E5], E1, S1,
     "Three route terminals, three theorems -- not one conclusion: Route 3's conclusion is its premise restated (ch_iff_rh).", ''),
    ('L', 1609, 'For each mechanism class, `produces_offline`', 'STANDS', 'T2', [], '', 'as defined and refuted in the kernel', '', ''),
] + [('L', ln, nd, 'STANDS', 'T2', [], '', 'a per-class exclusion row: model algebra, named', '', '')
     for ln, nd in ((1613, 'C₁ Schwarz'), (1614, 'C₂ Euler'), (1615, 'C₃ Functional'), (1616, 'C₄ Modular'), (1617, 'C₅ Spectral'),
                    (1618, 'C₆ Cauchy-Riemann'), (1619, 'C₇ Hadamard'))] + [
    ('L', 1629, '| TheBridgeComplete.lean |', 'STANDS', 'T2', [], '', 'the conjunction proved; E-2026-09-14-1 reads the monograph`s own concordance as exact', '', ''),
    ('L', 1630, '| ConservationBridge.lean |', 'STANDS', 'T2', [], '', 'b532 M-11', '', 'M-11'),
    ('L', 1632, 'The per-class completability census', 'STANDS', 'T4', [], '', 'a pointer', '', ''),
    ('L', 1636, 'For a reader who wants the kernel`s three routes'.replace('`', "'"), 'STANDS', 'T2', [], '', 'the route terminals, in files', '', ''),
    ('L', 1638, '`Formation.lean`', 'STANDS', 'T2', [], '', 'a file list', '', ''),
    ('L', 1639, '`Voice1.lean`', 'STANDS', 'T2', [], '', 'a file list', '', ''),
    ('L', 1640, '`PoissonExhaustion.lean`', 'STANDS', 'T2', [], '', 'a file list', '', ''),
    ('L', 1641, '`TheBridgeComplete.lean` — Route 1 assembled.', 'STANDS', 'T2', [], '', 'a file list', '', ''),
    ('L', 1642, '`Voice3b.lean` and', 'STANDS', 'T0', [], '', 'a file list', '', ''),
    ('L', 1642, 'The Spectral Cannon`s three theorems compiled'.replace('`', "'"), 'STANDS', 'T0', [], '', 'as said', '', ''),
    ('L', 1643, '`ConservationBridge.lean` — Route 3 assembled.', 'STANDS', 'T2', [], '', 'b532 M-12', '', 'M-12'),
    ('L', 1645, 'has verified three independent routes to σ = 1/2', 'RESTS', 'T2', [E5], E1, S1,
     "A reader who verifies these six files has verified the three route terminals in Lean: the structural conjunction, the codimension chain, and the Conservation implication from a premise that is RH restated (ch_iff_rh).", ''),
    ('L', 1649, 'Together they formalize the three independent routes', 'RESTS', 'T2', [E5], E1, S1,
     "Together they formalize the three route terminals described in §25.5.", ''),
    ('L', 1651, 'machine-verified as Mathlib infrastructure matures', 'STANDS', 'T4', [], '', 'a forward statement', '', ''),
    ('L', 1653, 'in `ConservationBridge.lean` is the programme', 'RESTS', 'T2', [E1], E1, 'b532 M-13, listed in E-2026-09-25-1', '', 'M-13'),
    ('L', 1653, 'The kernel`s Route 3 closes the chain'.replace('`', "'"), 'RESTS', 'T2', [E1], E1, 'b532 M-14, listed in E-2026-09-25-1', '', 'M-14'),
    ('L', 1659, 'A clean entry reads', 'STANDS', 'T0', [], '', 'as said', '', ''),
    ('L', 1659, 'The Route 3 row`s statement changed'.replace('`', "'"), 'STANDS', 'T2', [], '', 'b532 M-15', '', 'M-15'),
    ('L', 1661, 'Deposit lineage:', 'STANDS', 'T2', [], '', 'a lineage record', '', ''),
    ('L', 1661, 'Every one preserves the axiom profiles', 'STANDS', 'T2', [], '', 'as said', '', ''),
    ('L', 1661, 'The refinements sharpen the source', 'STANDS', 'T2', [], '', 'as said', '', ''),
    ('L', 1663, 'It is **not an index', 'STANDS', 'T4', [], '', 'as said', '', ''),
    ('L', 1663, 'Deposited sentences found to assert a machine check', 'STANDS', 'T4', [], '', 'a pointer to E-2026-09-22-1', '', ''),
    ('L', 1663, 'See also the *On Route 1*', 'STANDS', 'T4', [], '', 'a pointer', '', ''),
    ('L', 1667, '| Route 1 — structural exhaustiveness, unconditional in Lean', 'STANDS', 'T2', [], '',
     'the row names the terminal`s own proposition; the On Route 1 note reads it per conjunct, as E-2026-09-14-1 says the concordance is exact', '', ''),
    ('L', 1668, '| Route 2 — perpendicular crossing', 'STANDS', 'T0', [], '', 'the completed-ζ derivative, as the terminal states; T0, not RH-anchor', '', ''),
    ('L', 1669, '| Route 3 — RH from the conservation interface', 'STANDS', 'T2', [], '', 'b532 M-16: the row states the implication', '', 'M-16'),
    ('L', 1670, '| Structural exhaustiveness yields RH', 'STANDS', 'T2', [], '', 'Integration`s proposition is RH restated, named so at :1562; the row states what the terminal states', '', ''),
    ('L', 1671, '| Structural exhaustiveness is equivalent to RH', 'STANDS', 'T2', [], '', 'as :1670', '', ''),
    ('L', 1672, '| The formation count', 'STANDS', 'T2', [], '', 'as said', '', ''),
    ('L', 1673, '| Inter-mechanism-class independence', 'STANDS', 'T2', [], '', 'as the terminal states', '', ''),
    ('L', 1679, '| The construction era`s global-section'.replace('`', "'"), 'STANDS', 'T0', [], '', 'as recorded at the pin', '', ''),
    ('L', 1681, 'Its terminals — `all_pairs_excluded`', 'STANDS', 'T2', [], '', 'as said', '', ''),
    ('L', 1681, 'This inter-class independence result is distinct', 'STANDS', 'T2', [], '', 'as said', '', ''),
    ('L', 1683, '**On Route 1.**', 'STANDS', 'T2', [], '', 'reads the conjunction exactly', '', ''),
    ('L', 1683, 'Read per conjunct:', 'STANDS', 'T2', [], '', 'reads the catalogue conjunct as a decide count, exactly', '', ''),
    ('L', 1683, '**C₆ now derives at model level**', 'STANDS', 'T2', [], '', 'as said', '', ''),
    ('L', 1685, '**On Route 3.**', 'STANDS', 'T2', [], '', 'b532 M-17', '', 'M-17'),
    ('L', 1685, 'Route 1 carries no such argument', 'STANDS', 'T2', [], '', 'as said', '', ''),
    ('L', 1687, '**Closure.**', 'STANDS', 'T0', [], '', 'as said', '', ''),
    ('L', 1687, 'Those are the only three sources', 'STANDS', 'T0', [], '', 'as said', '', ''),
    ('L', 1689, '**Route 2 housing.**', 'STANDS', 'T0', [], '', 'as said', '', ''),
    # ---- DEPOSIT-SOLE rows (lines in the deposited copy)
    ('D', 127, 'The three routes are the machine verification.', 'RESTS', 'T2', [E5], E1, S1,
     "The three route terminals are the machine-checked part; Route 3's premise is RH restated (ch_iff_rh).", ''),
    ('D', 129, 'The Lean kernel`s `SIDESystem` typeclass'.replace('`s ', "'s "), 'STANDS', 'T2', [], '', 'as compiled', '', ''),
    ('D', 201, 'identified by five independent routes', 'RESTS', 'T2', [E5], '',
     'the deposited "independent ... different machinery" is corrected in the live line (2026-08-10): three of the identifications are one map, σ ↦ 1 − σ',
     "The value σ = 1/2 is identified by five convergent routes, sharing the involution σ ↦ 1 − σ rather than using wholly different machinery (distinct from the five proof-paths of Chapter 16 and the five closures of §18.3).", ''),
    ('D', 203, '**Route 1 (Algebraic).**', 'STANDS', 'T4', [], '', 'an identification path', '', ''),
    ('D', 205, '**Route 2 (Analytic).**', 'STANDS', 'T4', [], '', 'an identification path', '', ''),
    ('D', 207, '**Route 3 (Topological).**', 'STANDS', 'T4', [], '', 'an identification path (not Route 3 of the kernel); b532 M-05', '', 'M-05'),
    ('D', 209, '**Route 4 (Arithmetic).**', 'STANDS', 'T4', [], '', 'an identification path', '', ''),
    ('D', 211, '**Route 5 (Spectral).**', 'STANDS', 'T4', [], '', 'an identification path', '', ''),
    ('D', 1655, 'Deposit lineage:', 'STANDS', 'T2', [], '', 'a lineage record', '', ''),
]


def grade_rows():
    lr, lsel, lstop = census_of(LIVE)
    dr, dsel, dstop = census_of(DEP)
    live1, dep1 = lsel[:lstop], dsel[:dstop]
    dt = {nz(r['sentence']): r for r in dsel}
    lt = {nz(r['sentence']) for r in lsel}
    rows = []
    for r in live1:
        m = dt.get(nz(r['sentence']))
        rows.append(dict(src='L', line=r['line'], dep_line=(m['line'] if m else 'LIVE-SOLE'), **{k: r[k] for k in ('section', 'chapter', 'sentence', 'hits')}))
    lpos = {}
    for i, r in enumerate(lsel):
        lpos.setdefault(nz(r['sentence']), (i, r['line']))
    past = [dict(dep_line=r['line'], live_line=lpos[nz(r['sentence'])][1], sentence=r['sentence'][:160]) for r in dep1
            if nz(r['sentence']) in lpos and lpos[nz(r['sentence'])][0] >= lstop and not any(nz(r['sentence']) == nz(x['sentence']) for x in live1)]
    for r in dep1:
        if nz(r['sentence']) not in lt:
            rows.append(dict(src='D', line='DEPOSIT-SOLE', dep_line=r['line'], **{k: r[k] for k in ('section', 'chapter', 'sentence', 'hits')}))
    b532 = {x['id']: x for x in jl('b532_rows.json')['rows']}
    used = set()
    for r in rows:
        key_line = r['line'] if r['src'] == 'L' else r['dep_line']
        g = [x for x in GR if x[0] == r['src'] and x[1] == key_line and x[2] in r['sentence']]
        if len(g) > 1:
            sys.exit('### MORE THAN ONE TYPED ROW MEETS :%s %s' % (key_line, r['sentence'][:100]))
        if g:
            _, _, nd, grade, tier, errs, subj, reason, rep, carried = g[0]
            used.add((g[0][0], g[0][1], g[0][2]))
            if carried and not carried.endswith('*') and b532.get(carried, {}).get('verdict') != grade:
                sys.exit('### CARRIED %s DISAGREES WITH b532 (%s vs %s)' % (carried, grade, b532.get(carried, {}).get('verdict')))
            r.update(grade=grade, tier=tier, errata=errs, subject=subj, reason=reason, replacement=rep, carried=carried, default=False)
        elif set(r['hits']) <= DEFAULT_HITS:
            r.update(grade='STANDS', tier='T4', errata=[], subject='', reason='the declared default: a manuscript reading no T0 result touches; the ceiling question was read at b493 and b532',
                     replacement='', carried='', default=True)
        else:
            sys.exit('### NO TYPED ROW AND NOT DEFAULT-ELIGIBLE :%s [%s] %s' % (key_line, r['src'], r['sentence'][:120]))
    unused = [(x[0], x[1], x[2]) for x in GR if (x[0], x[1], x[2]) not in used]
    if unused:
        sys.exit('### TYPED ROWS MEETING NO SENTENCE: %s' % unused)
    grade_rows.past = past
    return rows, lr, lsel, lstop, dsel, dstop


def census():
    rows, lr, lsel, lstop, dsel, dstop = grade_rows()
    run2 = dict(yields={n: sum(1 for r in lsel if n in r['hits']) for n, _ in PAT}, read=len(lr), selected=len(lsel), act_one=lstop)
    live_sel = [r for r in rows if r['src'] == 'L']
    counts = {g: sum(1 for r in rows if r['grade'] == g) for g in ('STANDS', 'RESTS', 'EXCEEDS')}
    by_err = {}
    for r in rows:
        for e in r['errata']:
            by_err[e] = by_err.get(e, 0) + 1
    halt = next(r for r in lsel if r['section'] and r['section'].startswith(HALT))
    ch14 = next((r for r in lr if 'unsolved goal' in r['sentence']), None)
    anchor_refs = [dict(line=r['line'], dep_line=r['dep_line'], chapter=r['chapter'], sentence=r['sentence'][:200]) for r in rows
                   if re.search(r'h2_sign|Weil positiv|Weil functional|\bLi\b|λ_n ≥ 0|Li`s|Li\'s', r['sentence'])]
    res = dict(run1=RUN1, run2=run2, lineage_agree=(RUN1['yields'] == run2['yields'] and RUN1['selected'] == run2['selected'] and RUN1['act_one'] == run2['act_one']),
               halt=dict(line=rd(LIVE).split(NL).index(halt['section'].strip()) + 1, first_act_two=halt['line'], section=halt['section'], act_one_live=lstop, act_two_live=len(lsel) - lstop,
                         deposit_act_one=dstop, deposit_total=len(dsel)),
               rows=rows, counts=counts, by_erratum=by_err, live_rows=len(live_sel), deposit_sole=sum(1 for r in rows if r['src'] == 'D'),
               live_sole=sum(1 for r in rows if r['dep_line'] == 'LIVE-SOLE'), past_halt=grade_rows.past, defaults=sum(1 for r in rows if r['default']),
               ch14=dict(line=ch14['line'], selected=bool(ch14['hits']), sentence=ch14['sentence']) if ch14 else None,
               anchor_refs=anchor_refs, tiers={t: sum(1 for r in rows if r['tier'] == t) for t in ('T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4')})
    put_json('b541_census.json', res)
    print('  ### the needles : %s' % [n for n, _ in PAT])
    print('  %-18s %6s %6s' % ('needle', 'run 1', 'run 2'))
    for n, _ in PAT:
        print('  %-18s %6d %6d' % (n, RUN1['yields'][n], run2['yields'][n]))
    print('  read %d / %d ; selected %d / %d ; act one %d / %d ; lineage agree %s' % (RUN1['read'], run2['read'], RUN1['selected'], run2['selected'],
                                                                                    RUN1['act_one'], run2['act_one'], res['lineage_agree']))
    print('  ### HALT : act one ends before the live heading :%d "%s" (act two`s first selected sentence :%d) ; act one %d live + %d DEPOSIT-SOLE = %d rows ; act two %d live'
          % (res['halt']['line'], halt['section'], halt['line'], lstop, res['deposit_sole'], len(rows), len(lsel) - lstop))
    print('  grades %s ; errata %s ; tiers %s ; defaults %d ; LIVE-SOLE %d' % (counts, by_err, res['tiers'], res['defaults'], res['live_sole']))
    print('  deposited act-one sentences whose live copy lies past the halt (read at act two) : %d' % len(grade_rows.past))
    for x in grade_rows.past:
        print('    dep :%(dep_line)s -> live :%(live_line)s  %(sentence).100s' % x)
    print('  Chapter 14`s "unsolved goal" sentence : %s' % (res['ch14'] if res['ch14'] else 'NOT FOUND'))
    print('  RH-anchor / Weil / Li references in act one : %s' % anchor_refs)


# ------------------------------------------------------------------------------ COMPONENT 4
def erratum5():
    cj = jl('b541_census.json')
    rows = [r for r in cj['rows'] if E5 in r['errata']]
    L = ['## E-2026-09-25-5 — The deposited monograph, read against the RH-anchor to §25.8: sentences that count Route 3 as a route, '
         'name terminals and a file no kernel holds, or read the registers and the perpendicular crossing past their compiled statements '
         '(DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2) — DRAFT, NOT FILED', '',
         '**Drafted 2026-09-25 (b541), on the author\'s ruling (R151)(4), from the census banked at b541 (relay data/b541_census.json), '
         'act one of the whole-monograph read (the chapters before §26.1); a further entry beside E-2026-09-25-1 and E-2026-09-25-4, '
         'extending them without editing them. TO BE FILED only on the author\'s word.',
         '### NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY. NOTHING WAS WRITTEN AT ZENODO.',
         '### THE RECORDS ARE IMMUTABLE AT THEIR VERSIONS AND ARE NOT ALTERED BY IT.**', '',
         '**Affected.** *A Place to Stand*, Zenodo version v1.1.2 ([10.5281/zenodo.21539167](https://doi.org/10.5281/zenodo.21539167)) — the '
         'monograph as deposited (PLACE-papers outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md, md5 e90e2d06d5cadc059c62c29a849e9f8c); the '
         'live line day1/A_Place_to_Stand.md v5.13 carries the same sentences where a live line is given; a row marked LIVE-SOLE is the live line\'s only, corpus-facing, '
         'listed so that the live line is corrected with the deposit.', '',
         '**What the kernels say, in their own words.** SIDE-explicit-formula at 81ae175, read fresh at b541: ch_iff_rh : '
         'conservationHypothesis ↔ RiemannHypothesis; h2_sign_iff_rh : h2_sign ↔ RiemannHypothesis; not_register1 : '
         '¬Register1_universalityHypothesis; register5_output_holds : Register5_output_HilbertPolya. SIDE-kernel v1.5: '
         'SpectralCannonFull.spectral_cannon : (deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0; the names prod_prime_power_absValues, '
         'prod_int_absValues, prod_rat_absValues, conservation_certificate and the file ProductFormula_Prime.lean are at no tag v1.0-v1.7 '
         'nor at HEAD, and in no local repository.', '',
         '**The sentences, each with its replacement:**', '']
    for r in rows:
        where = ('A_Place_to_Stand.md:%s at v1.1.2' % r['dep_line']) if r['dep_line'] != 'LIVE-SOLE' else 'LIVE-SOLE, not in the deposit (corpus-facing)'
        live = (', live :%s' % r['line']) if r['line'] != 'DEPOSIT-SOLE' else ''
        L += ['- **%s%s** (%s): *"%s"*' % (where, live, r['section'] or '', r['sentence'].replace('`', '').replace('*', '')),
              '  - reads **RESTS** — %s%s.' % (re.sub(r"(?<=[A-Za-z0-9])`s\b", "'s", r['reason']).replace('`', ''),
                                               ('; under %s\'s subject' % r['subject']) if r['subject'] and r['subject'] not in r['reason'] else ''),
              '  - replacement: *"%s"*' % r['replacement'].replace('`', '')]
    L += ['', '**What is not corrected.** Every STANDS row of the census (relay data/b541_census.json); the manuscript\'s readings of '
              'exhaustiveness by Ostrowski, read by default STANDS at T4; the ceiling question, read at b493 and b532. §26 onward is read at '
              'the act after, which may extend this entry by a further one.', '',
          '**Status.** DRAFT. Not filed. Retained at monograph v1.1.2. The filing is the author\'s word.', '']
    txt = NL.join(L)
    io.open(os.path.join(D, 'b541_erratum_draft.md'), 'w', encoding='utf-8', newline=NL).write(txt)
    put_json('b541_erratum5.json', dict(rows=len(rows), backticks=txt.count('`'), backticks_outside_code=outside_bt(txt)))
    print('  E-2026-09-25-5 draft : %d rows ; backticks %d' % (len(rows), txt.count('`')))


# ------------------------------------------------------------------------------ COMPONENT 5
CHAPTERS = [  # (top heading prefix, load-bearing claim, its tier)
    ('The Third Identity Element', 'RH by exhaustive enumeration over the seven classes (Ostrowski), per-class exclusion, under the named premise h2; the kernel carries three route terminals', 'T1-open'),
    ('PART I', 'Part I`s three operations meet at one point', 'T4'),
    ('Chapter 1:', 'the three identity elements of the arithmetic operations', 'T4'),
    ('Chapter 2:', 'the identity subspace, where all generating operations return identity', 'T4'),
    ('Chapter 3:', 'Størmer: the {2,3}-smooth consecutive pairs, the wall at seven', 'T4'),
    ('Chapter 4:', 'the Trivium vector in ℂ⁷', 'T4'),
    ('Chapter 5:', 'the spectral structure and the dark subspace', 'T4'),
    ('Chapter 6:', 'three threads meet at one point', 'T4'),
    ('Chapter 7:', 'the identity-formation bijection (a capstone, not a step)', 'T4'),
    ('PART II', 'the method', 'T4'),
    ('Chapter 8:', 'proof by exhaustive enumeration, the oldest method', 'T4'),
    ('Chapter 9:', 'Symmetry, Independence, Determination', 'T4'),
    ('Chapter 10:', 'the Mechanism Theorem: an exhaustive catalogue with no producer excludes the target (compiled as logic)', 'T2'),
    ('Chapter 11:', 'validation of the method', 'T4'),
    ('PART III', 'the proof', 'T1-open'),
    ('Chapter 12:', 'the completed zeta, specified n² → θ → ξ', 'T4'),
    ('Chapter 13:', 'Conservation of Spectra: the product formula is s-dark (compiled as (1 : ℚ) ^ s = 1, a STIPULATION)', 'T2'),
    ('Chapter 14:', 'the silence of foundations (silence_universal, per interface; its universal register false as stated)', 'T2'),
    ('Chapter 15:', 'the seven classes, exhaustive by Ostrowski (Route 1: the decide-count conjunct and the C₇ stand-in)', 'T2'),
    ('Chapter 16:', 'five paths identify σ = 1/2 (model statements; three one map)', 'T2'),
    ('Chapter 17:', 'the controlled experiment: Epstein lacks the Euler product and has off-line zeros (classical)', 'T4'),
    ('Chapter 18:', 'the codimension closure (model level, offLine_of_codim_two)', 'T2'),
    ('Chapter 19:', 'the assembly: all nontrivial zeros on the line, resting on the named premise h2, RH-equivalent in its Weil form', 'T1-open'),
    ('Chapter 20:', 'the extension to GRH (its premise not compiled for L-functions)', 'T4'),
    ('PART IV', 'the independent routes through simplicity', 'T4'),
    ('Chapter 21:', 'the simplicity reduction', 'T4'),
    ('Chapter 22:', 'Re ξ′ = 0 on the line (compiled for completedRiemannZeta₀, spectral_cannon); simplicity itself open', 'T0'),
    ('Chapter 23:', 'the R-curve path (one direction compiled over an abstract V)', 'T2'),
    ('Chapter 24:', 'three traditions converge on simplicity (evidence, not proof)', 'T4'),
    ('PART V', 'the formal verification', 'T2'),
    ('Chapter 25:', 'the kernel`s three route terminals compile at the standard three (Route 1 T2, Route 2 T0, Route 3 T2)', 'T2')]


def chapter_of(r):
    c = r['chapter'] or ''
    return next((k for k, _, _ in CHAPTERS if c.startswith(k) or c.startswith('# ' + k) or k in c), c[:30])


def map_():
    cj = jl('b541_census.json')
    per = {}
    for r in cj['rows']:
        per.setdefault(chapter_of(r), []).append(r)
    TI = ('T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4')
    L = ['', FTITLE, '',
         '*Filed at b541 on the author`s ruling `(R151)`(4)-(5): act one of two. The live line (v5.13, md5 `bb86aa65…a31e`) and the '
         'deposited v1.1.2 (md5 `e90e2d06…9e9f8c`, equal to Zenodo`s) read sentence by sentence where a sentence names a route, a register, '
         'h1/h2, the goal state, machine-verified, reduction, complete, compiled, exhaustive, the one open premise, or a named terminal; '
         'each graded against the RH-anchor and the tier law. Bank: relay `data/b541_census.json`. Nothing in the monograph is edited.*', '',
         '**The census.** %d live sentences selected of %d (both runs agree); act one takes %d live and %d DEPOSIT-SOLE, **%d rows**: '
         'STANDS %d · RESTS %d · EXCEEDS %d; RESTS by erratum %s; tiers %s. %d rows read by the declared default (STANDS, T4).'
         % (cj['run2']['selected'], cj['run2']['read'], cj['halt']['act_one_live'], cj['deposit_sole'], len(cj['rows']),
            cj['counts']['STANDS'], cj['counts']['RESTS'], cj['counts']['EXCEEDS'], cj['by_erratum'], cj['tiers'], cj['defaults']), '',
         '**A finding of the read.** The deposited §25.2 and §25.4 name a file, `ProductFormula_Prime.lean`, and four terminals, '
         '`prod_prime_power_absValues`, `prod_int_absValues`, `prod_rat_absValues` and `conservation_certificate`, that **no version of '
         'SIDE-kernel holds** (tags v1.0–v1.7 and HEAD) and no local repository holds; the conservation terminal the kernel carries is '
         '`conservation_of_spectra`, `(1 : ℚ) ^ s = 1`. Those sentences read RESTS on E-2026-09-25-5 (drafted).', '',
         '**The chapter tier map** (the load-bearing claim of each, its tier; the counts of the graded sentences it carries):', '',
         '| chapter | load-bearing claim | tier | sentences | ' + ' | '.join(TI) + ' | RESTS (errata) |',
         '|:--|:--|:--|--:|' + '--:|' * len(TI) + ':--|']
    for k, claim, tier in CHAPTERS:
        rs = per.get(k, [])
        rests = [r for r in rs if r['grade'] == 'RESTS']
        errs = sorted(set(e for r in rests for e in r['errata']))
        L.append('| %s | %s | **%s** | %d | %s | %d %s |' % (k.rstrip(':'), claim, tier, len(rs),
                                                            ' | '.join(str(sum(1 for r in rs if r['tier'] == t)) for t in TI),
                                                            len(rests), ('(' + ', '.join(errs) + ')') if errs else ''))
    other = [k for k in per if k not in [c[0] for c in CHAPTERS]]
    L += ['', 'Rows whose chapter heading the map does not name: %s.' % (other or 'none'), '',
          '**The RH-anchor in these chapters.** No act-one sentence names `h2_sign_iff_rh`, Weil positivity or the Li form; the anchor`s '
          'content enters these chapters only as the tier law`s readings (Route 3 RH restated, register 1 false as stated).'
          if not cj['anchor_refs'] else '**The RH-anchor in these chapters:** %s.' % cj['anchor_refs'], '',
          '**Halt line.** Act one ends before the live heading "%s" (:%d). The act after reads Chapter 26 to the file`s end (%d live '
          'sentences), §27.3 among them, and may extend E-2026-09-25-5 by a further entry.' % (cj['halt']['section'], cj['halt']['line'], cj['halt']['act_two_live']), '']
    w = append_to(FIND, NL.join(L))
    w['heading_line'] = rd(FIND).split(NL).index(FTITLE) + 1
    put_json('b541_map.json', w)
    print('  FINDINGS : %(added)d bytes added, prefix %(prefix)s ; entry at line %(heading_line)d' % w)


# ------------------------------------------------------------------------------ desk
def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout


PRIOR_PP = 'd57c31d'
FILES = ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md']


def subseq(old, new):
    it = iter(new.split(NL))
    return all(any(l == m for m in it) for l in old.split(NL))


def token_count():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        return None
    return sum(open(os.path.join(d0, f), 'rb').read().count(t) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b541_'))


def scores():
    cj, fj = jl('b541_census.json'), jl('b541_file.json')
    kept = {f: subseq(blob(PP, '%s:%s' % (PRIOR_PP, f)).decode('utf-8-sig').replace(chr(13), ''), rd(os.path.join(PP, f)))
            and (f == 'ERRATA.md' or open(os.path.join(PP, f), 'rb').read().startswith(blob(PP, '%s:%s' % (PRIOR_PP, f)))) for f in FILES}
    # the object git stores (hash-object applies the eol filter the checkout applied), and the working bytes' md5 against b532's bank
    mono = {f: git(PP, 'hash-object', f) == git(PP, 'rev-parse', '%s:%s' % (PRIOR_PP, f))
            for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')}
    mono['deposited md5 = e90e2d06 (Zenodo`s, b532)'] = md5(DEP) == 'e90e2d06d5cadc059c62c29a849e9f8c'
    mono['live md5 = bb86aa65 (the pre-seal read)'] = md5(LIVE) == 'bb86aa65025b49d2547016ef5000a31e'
    same = {f: blob(PP, '%s:%s' % (PRIOR_PP, f)) == open(os.path.join(PP, f), 'rb').read() for f in ('README.md', 'REGISTRY.md')}
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b541_') and needle in rd(os.path.join(T, x))]
    tok = token_count()
    dep = git(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''
    moved = [r for r in cj.get('rows', []) if str(r.get('carried', '')).endswith('*')]
    no_filed = [r for r in cj.get('rows', []) if r['grade'] == 'RESTS' and E5 in r['errata'] and not r['subject']]
    route1 = next((r for r in cj.get('rows', []) if r['line'] == 1667), {})
    t0z = [(r['line'], r['sentence'][:80]) for r in cj.get('rows', []) if r['tier'] == 'T0' and re.search(r'zeros? (lie|lies|are|is) on|all nontrivial zeros|Re\(ρ\) = 1/2|σ = 1/2 for every', r['sentence'])]
    return dict(
        n1=60 <= cj.get('run2', {}).get('selected', 0) <= 160, total=cj.get('run2', {}).get('selected'),
        n2=None,
        n3=not cj.get('anchor_refs') and not t0z, t0_zero=t0z,
        anchor_refs=cj.get('anchor_refs'), t0_chapters=sorted(set(chapter_of(r) for r in cj.get('rows', []) if r['tier'] == 'T0')),
        n4=cj.get('counts', {}).get('EXCEEDS', 1) == 0,
        n5=all(mono.values()) and all(kept.values()) and not zen, mono=mono, kept=kept,
        n6=dep and all(same.values()) and tok == 0, same=same, token=tok, deposit_clean=dep, zenodo_tools=zen,
        s1=bool(cj.get('lineage_agree')), s2=bool(no_filed), no_filed=[(r['line'], r['dep_line']) for r in no_filed],
        s3=route1.get('grade') == 'STANDS', moved=[(r['line'], r['carried']) for r in moved])


def w(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def components():
    cj = jl('b541_census.json')
    L = ['=' * 132, 'b541 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### THE READS:'] + ['  ' + l for l in rd(os.path.join(D, 'b541_reads.txt')).rstrip(NL).split(NL)[2:]]
    L += ['', '### COMPONENT 1 -- THE FILING : ' + json.dumps(jl('b541_file.json'), ensure_ascii=False),
          '### COMPONENT 2 -- THE TIER-LAW LINE AND THE R5 FINDING : ' + json.dumps(jl('b541_law.json'), ensure_ascii=False), '',
          '### COMPONENT 3 -- THE CENSUS : run 1 %s ; run 2 %s ; agree %s' % (cj['run1'], cj['run2'], cj['lineage_agree']),
          '  halt : %s' % cj['halt'], '  counts %s ; by erratum %s ; tiers %s ; defaults %d' % (cj['counts'], cj['by_erratum'], cj['tiers'], cj['defaults']),
          '  Chapter 14 : %s' % cj['ch14']]
    L += ['  %-6s %-12s %-7s %-7s %-40s %s' % (r['line'], r['dep_line'], r['grade'], r['tier'], ','.join(r['errata']) or '-', r['sentence'][:110])
          for r in cj['rows'] if not r['default']]
    L += ['', '### COMPONENT 4 -- E-2026-09-25-5 : ' + json.dumps(jl('b541_erratum5.json')),
          '### COMPONENT 5 -- THE CHAPTER TIER MAP : ' + json.dumps(jl('b541_map.json'), ensure_ascii=False), '=' * 132]
    io.open(os.path.join(D, 'b541_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:6]))


def desk():
    sc = scores()
    N = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')
    S = ('s1', 's2', 's3')
    L = ['=' * 104, 'b541 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- the census selects %s sentences (needles printed in the components).' % (w(sc['n1']), sc['total']),
         '  **(N2)** ### **NOT SCORABLE AT THIS ACT.** -- §27.3 lies past the halt line; it is read at the act after.',
         '  **(N3)** ### **%s.** -- act-one sentences naming the RH-anchor, Weil positivity or the Li form : %s ; T0 rows stating zero location : %s ; the T0 rows` chapters : %s.' % (w(sc['n3']), sc['anchor_refs'] or 'none', sc['t0_zero'] or 'none', sc['t0_chapters']),
         '  **(N4)** ### **%s.** -- EXCEEDS rows : %s.' % (w(sc['n4']), jl('b541_census.json').get('counts', {}).get('EXCEEDS')),
         '  **(N5)** ### **%s.** -- the monograph copies byte-identical %s ; written files` prior lines kept %s ; tools naming the platform %s.'
         % (w(sc['n5']), sc['mono'], sc['kept'], sc['zenodo_tools'] or 'NONE'),
         '  **(N6)** ### **%s.** -- deposit tree clean %s ; README, REGISTRY byte-identical %s ; token hits %s.' % (w(sc['n6']), sc['deposit_clean'], sc['same'], sc['token']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the two census runs agree needle by needle.' % w(sc['s1']),
         '  **(S2)** ### **%s.** -- RESTS rows under no filed erratum`s subject : %s.' % (w(sc['s2']), sc['no_filed']),
         '  **(S3)** ### **%s.** -- §25.8`s Route 1 row (live :1667).' % w(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE 1.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N if sc[k] is not None].count(True), [sc[k] for k in N if sc[k] is not None].count(False),
            [sc[k] for k in S].count(True), [sc[k] for k in S].count(False)),
         '  rows MOVED from b532`s verdict : %s' % sc['moved'],
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b541_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b541_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    io.open(os.path.join(D, 'b541_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    put_json('b541_scores.json', sc)
    print(NL.join(L))


def trail():
    sc, cj = scores(), jl('b541_census.json')
    body = ['', HEADING, '',
            '**(R151) ratified.** (1) E-2026-09-25-4 filed. (2) T1-open needs an EQUIVALENT-DEEP premise; h2_sign the one; a rewording '
            'premise makes its terminal T2. (3) R5-output as deposited is a theorem, its disclaimer disclaiming a theorem. (4) The monograph '
            'read whole, in two acts. (5) The chapter tier map. (6) BALANCE_AND_POSITIVITY after the read.', '',
            '**Filed:** E-2026-09-25-4 at `ERRATA.md`:%s-%s, its bullet at :%s. **Entered:** the tier-law line in the map; the R5 finding '
            'at `FINDINGS.md`:%s.' % (tuple(jl('b541_file.json')['entry_lines']) + (jl('b541_file.json')['bullet_line'], jl('b541_law.json')['findings']['heading_line'])), '',
            '**The census, act one** (halt before the live heading "%s", :%s): %d rows (%d live, %d DEPOSIT-SOLE) -- STANDS %d · RESTS %d · EXCEEDS %d; '
            'RESTS by erratum %s. **Found:** the deposited §25.2 and §25.4 name `ProductFormula_Prime.lean` and four terminals no version of '
            'SIDE-kernel holds. **E-2026-09-25-5 DRAFTED, NOT FILED** (relay `data/b541_erratum_draft.md`). The chapter tier map at '
            '`FINDINGS.md`:%s.' % (cj['halt']['section'], cj['halt']['line'], len(cj['rows']), cj['live_rows'], cj['deposit_sole'],
                                   cj['counts']['STANDS'], cj['counts']['RESTS'], cj['counts']['EXCEEDS'], cj['by_erratum'], jl('b541_map.json').get('heading_line')), '',
            '**Next:** the read`s second act, Chapter 26 to the end, §27.3 among it; then BALANCE_AND_POSITIVITY.', '',
            '**(N1) %s · (N2) NOT SCORABLE · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
            '**No kernel lane opened at this act.** Nothing deposits; nothing at Zenodo written; no kernel edited; no monograph byte changed; '
            'the ceiling unchanged; one b532 verdict moved (M-06, STANDS to RESTS on E-2026-09-25-5), no terminal-table grade moved; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; '
            'nothing here is a statement about RH.', '']
    before = open(OT, 'rb').read()
    if HEADING.encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    text = re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b541_trail_notes.json', out)


if __name__ == '__main__':
    sys.exit({'purpose': purpose, 'file': file, 'law': law, 'census': census, 'erratum5': erratum5, 'map': map_,
              'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]())
