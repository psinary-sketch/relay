# -*- coding: utf-8 -*-
"""b583_record.py -- THE ACT'S RECORD TOOL, UNDER (R193). ### ONE SUBCOMMAND PER BANK.

### ### b583: LANE THREE, ACT ELEVEN -- CP-7 ACT EIGHT, THE EDITION OF R_CURVE_CRITERION, THE ZETA PAGE AS ITS SPINE. Subcommands
### write only `data/b583_*` unless the docstring names another file. Every bank is written through `put_txt` / `put_json` (encode
### first, then a temp file, then `os.replace`). This act makes no platform call. ### The template is b582_record.py.
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

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '97da72c'
MIRROR_PIN = '192077f'
CUR = 'phase1.5/rcurve/R_CURVE_CRITERION.md'
ED = 'phase1.5/rcurve/R_CURVE_CRITERION_v0_2_2.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
WL = 'data/b558_editions/R_CURVE_CRITERION.txt'
SK = 'D:/SIDE-kernel'

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


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) G-SIMPLICITY-STANDS, AS FIRST WRITTEN, REQUIRED v0.2.1 :386 TO BE UNCHANGED AS A LINE; :386 also carries a ceiling '
    'correction in another sentence ("which is closed by the seven-class catalogue"), and only its simplicity sentence stands. '
    'The predicate now compares that sentence; the edition`s back-matter row, which said the lines were "carried unchanged", '
    'now says their sentences are, and the uncommitted edition was rewritten (`edition again`) and re-scanned. b582`s defect (c) '
    'species: an arm narrower than the edition it reads.',
]


def defects():
    put_txt('b583_defects.txt', ['### b583 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


RELAY = ROOT.replace('\\', '/')
ROWLINES = [261, 262, 264, 265, 267, 271, 272, 273, 275, 278]
READS = [
    ('relay the R_CURVE_CRITERION work-list, whole', RELAY, 'HEAD', WL, list(range(1, 56))),
    ('PLACE-papers R_CURVE_CRITERION, its head, correction note and Abstract', PP, PRE_PP, CUR, list(range(1, 26))),
    ('PLACE-papers R_CURVE_CRITERION, the marked, simplicity, ceiling, stem and fact lines', PP, PRE_PP, CUR,
     [42, 124, 148, 150, 152, 158, 164, 195, 234, 238, 242, 244, 250, 256, 260, 266, 339, 350, 351, 352, 355, 357, 358, 360, 380, 382, 384, 386,
      396, 398, 406, 416]),
    ('PLACE-papers R_CURVE_CRITERION, its version history, b397 disclosure and tier block', PP, PRE_PP, CUR, list(range(458, 505))),
    ('PLACE-papers the zeta page at the mirror`s pin, its pin line, nodes 8, 20, 24, the open line and the mellin row', PP, MIRROR_PIN, PAGE,
     [3, 12, 24, 28, 31, 138]),
    ('relay the CP-1b bank, its head and the R_CURVE_CRITERION rows', RELAY, 'HEAD', 'data/b558_cp1b.txt', list(range(1, 9)) + ROWLINES),
    ('PLACE-papers THE_KEYSTONE_CENSUS, the bd2ae1a sentence and b557`s two lines', PP, PRE_PP, 'phase2/method/THE_KEYSTONE_CENSUS.md', [119, 285, 287]),
    ('PLACE-papers ERRATA, E-2026-09-27-1', PP, PRE_PP, 'ERRATA.md', list(range(757, 768))),
    ('PLACE-papers THE_RESIDUE_OF_RH, the v0.11.0 and b567 lines', PP, PRE_PP, 'phase1.5/proofs/THE_RESIDUE_OF_RH.md', [247, 249, 253]),
    ('PLACE-papers OPEN_TRAILS, the form, its clauses and b582`s record', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11454, 11864, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 11974, 11976, 11978]),
    ('PLACE-papers FINDINGS, b582`s entry', PP, PRE_PP, 'FINDINGS.md', [6566]),
    ('relay the b555 ferry, the shells line', RELAY, 'HEAD', 'data/b555_ferry.txt', [95, 96, 97]),
    ('PLACE-papers README, the ceiling', PP, PRE_PP, 'README.md', list(range(104, 122))),
    ('relay tools/banned_terms.py, the stems and the exceptions', RELAY, 'HEAD', 'tools/banned_terms.py', list(range(1, 81))),
    ('relay b582`s closing push-out, its head', RELAY, 'HEAD', 'data/b582_closing_push_out.txt', list(range(1, 4))),
]
PINS = (('SIDE-rcurve', 'v0.1.0', 'd5f33b4'), ('SIDE-lv-conservation', 'v0.4.0', '0d2d74c'), ('SIDE-lv-conservation', 'v0.5.0', '1767bd6'),
        ('SIDE-lv-conservation', 'v0.5.1', 'bc4751e'), ('SIDE-lv-conservation', 'v0.6.0', 'c80bdc2'), ('SIDE-lv-conservation', 'v0.7.0', '2d86182'),
        ('SIDE-lv-conservation', 'v0.8.0', '6efa9e5'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-lv-conservation', 'v0.11.0', '2f71068'),
        ('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-explicit-formula', 'v0.2', '5c72cad'), ('SIDE-explicit-formula', 'v0.9', 'e5a5a83'),
        ('SIDE-explicit-formula', 'v0.11', '19b7d1e'))


def _peel(repo, tag):
    p = 'D:/' + repo
    loc = g(p, 'rev-parse', tag + '^{}').strip()
    peeled = [l.split('\t')[0] for l in g(p, 'ls-remote', 'origin', 'refs/tags/%s^{}' % tag).split(NL) if l.strip()]
    rem = [l.split('\t')[0] for l in g(p, 'ls-remote', 'origin', 'refs/tags/%s' % tag).split(NL) if l.strip()]
    return loc, (peeled or rem or [''])[0]


def reads():
    L = ['b583 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    L.append('### the fact clause`s read over R_CURVE_CRITERION`s pins and the edition`s, each tag peeled locally and at the remote:')
    for repo, tag, cited in PINS:
        loc, r = _peel(repo, tag)
        L.append('    %s %s : cited %s ; local %s ; remote %s ; %s' % (repo, tag, cited, loc[:7], r[:7],
                                                                   'AGREE' if loc.startswith(cited) and r.startswith(cited) else '### DIFFER'))
    loc = g(SK, 'rev-parse', 'refs/heads/derivative-engine').strip()
    rem = g(SK, 'ls-remote', 'origin', 'refs/heads/derivative-engine').split('\t')[0]
    L += ['### the branch the three rows print: SIDE-kernel branch derivative-engine, cited "= `27a3ae7`" :',
          '    head local %s ; remote %s ; %s' % (loc[:7], rem[:7], '### DIFFER (the head is not 27a3ae7)' if not loc.startswith('27a3ae7') else 'AGREE'),
          '    27a3ae7 an ancestor of the head : %s ; commits 27a3ae7..head : %s' % (
              'yes' if subprocess.run(['git', '-C', SK, 'merge-base', '--is-ancestor', '27a3ae7', loc]).returncode == 0 else 'no',
              g(SK, 'rev-list', '--count', '27a3ae7..' + loc).strip()),
          '    files changed 27a3ae7..head : %s' % [x for x in g(SK, 'diff', '--name-only', '27a3ae7', loc).split(NL) if x.strip()],
          '    Kernel/DerivativeEngine.lean changed : %s' % ('yes' if g(SK, 'diff', '--name-only', '27a3ae7', loc, '--', 'Kernel/DerivativeEngine.lean').strip() else 'no')]
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR))
    L.append('### bd2ae1a in the current version : %d hit(s), each in b556`s tier block : %s' % (
        cur.count('bd2ae1a'), [i + 1 for i, l in enumerate(cur.split(NL)) if 'bd2ae1a' in l]))
    put_txt('b583_reads.txt', L)


# ================================================================================ COMPONENT 1
FORM_HEAD = '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three'
B582_ENTRY = '## CP-7, act seven: the edition of GRH_CASCADE'
B582_TRAIL = '### b582 — lane three, act ten under (R192)'
N1_TEXT = ('the navigator’s advance readings covered 27 of 29 rows at PATHS, 14 of 16 at FOUNDATIONS, 12 of 13 at '
           'ADDITIVE_MULTIPLICATIVE_CONSPIRACY, 9 of 10 at THE_UNCONDITIONAL_SURROUND and 3 of 10 at GRH_CASCADE, and the form resolved '
           'the remainder in every case; from b583 the advance readings are entered as the navigator’s expectations and not as rulings -- '
           'the form is the ruling, and a reading that has no object is recorded at zero cost')


def c1_lines():
    """### PLACE-papers FINDINGS (b582's weight) and OPEN_TRAILS (the navigator's wording for the shells; the (N1) pattern)."""
    Q = _Q()
    form, entry, trail = Q.line_of(Q.OT, FORM_HEAD), Q.line_of(Q.FIND, B582_ENTRY), Q.line_of(Q.OT, B582_TRAIL)
    if not (form == 11864 and entry == 6566 and trail == 11978):
        sys.exit('### THE ADDRESSED LINES MOVED: form %s entry %s trail %s -- NOTHING WRITTEN' % (form, entry, trail))
    heads = dict(
        weight='*Appended 2026-10-01 by b583 to b582’s entry (:%d), under `(R193)`(1) -- b582 AT ITS WEIGHT:*' % entry,
        shells='*Appended 2026-10-01 by b583 to b582’s record (:%d), under the author’s ruling `(R193)`(1) -- THE SHELLS’ WORDING, THE NAVIGATOR’S:*' % trail,
        pattern='*Appended 2026-10-01 by b583 to the form of an edition (:%d), under the author’s ruling `(R193)`(2) -- THE (N1) PATTERN; ADVANCE READINGS ARE EXPECTATIONS:*' % form,
    )
    for k, h in heads.items():
        Q.guard_absent(Q.FIND if k == 'weight' else Q.OT, h)
    out = [Q.append_to(Q.FIND, '\n%s `phase1.5/spectral/GRH_CASCADE_v0_3_6.md` beside v0.3.5 unedited: 10 rows as 8 sentences on 7 '
                                 'lines; :43 and :143 naming the open piece per instance and citing the Dirichlet page by name and pin; the six '
                                 'no-conspiracy rows citing CP-1b; three sentences on the GRH composite stating its conclusion; the '
                                 'universal-silence premise named at :141 and :264; the tier block and the superseding line byte for byte; 50 '
                                 'ceiling corrections on 32 lines, four headings among them, entered at :6566 as a finding of the edition; 13 '
                                 'hedged or historical lines carried and listed; the footer at :395 corrected by the fact clause. H28a, H28b (+1 '
                                 'against 1) and H28c held. The suite reads 70 of 70.\n' % heads['weight'])]
    out.append(Q.append_to(Q.OT, '\n%s `(R192)`(4)’s wording for `GRH.grh_exclusion` and `LandauSiegel.no_ls_zero` (“`fun _ => True` at '
                                 '`c66f3c5` and HEAD”) entered the record through the navigator’s b555 ferry (relay `data/b555_ferry.txt` '
                                 ':95-:96) and differs from the kernel read: at SIDE-effects `c66f3c5` both are theorems over opaque Props '
                                 '(balance → ¬off-line), and at `a27415d` and HEAD both are retired to comments (`Structural.lean` :79, :84; '
                                 'relay `data/b582_reads.txt`). The wording is the navigator’s; the read governs.\n' % heads['shells']))
    out.append(Q.append_to(Q.OT, '\n%s %s.\n' % (heads['pattern'], N1_TEXT)))
    lines = {k: Q.line_of(Q.FIND if k == 'weight' else Q.OT, h) for k, h in heads.items()}
    put_json('b583_c1_lines.json', dict(form=form, entry=entry, trail=trail, lines=lines, heads=heads, appends=out))
    print(lines)


# ================================================================================ COMPONENT 2 -- THE EDITION
EF = 'SIDE-explicit-formula'
PIN = {'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'mellin_Phi_eq_zero_of_re_le_one': 'v0.11 = `19b7d1e`', 'li_nonneg_iff_rh': 'v0.9 = `e5a5a83`'}
NS = {'h2_sign_iff_rh': 'B321', 'mellin_Phi_eq_zero_of_re_le_one': 'RegisterDepth', 'li_nonneg_iff_rh': 'LiCriterionBridge'}
WHERE = {'h2_sign_iff_rh': 'the zeta page, node 8, line 12',
         'mellin_Phi_eq_zero_of_re_le_one': 'the zeta page, Correspondence row, line 138 (the page`s pin)',
         'li_nonneg_iff_rh': 'the zeta page, node 20, line 24'}
H2 = '`h2_sign_iff_rh`, %s %s' % (EF, PIN['h2_sign_iff_rh'])
MP = '`mellin_Phi_eq_zero_of_re_le_one`, %s at the ζ page’s pin %s' % (EF, PIN['mellin_Phi_eq_zero_of_re_le_one'])
LI = '`li_nonneg_iff_rh`, %s %s' % (EF, PIN['li_nonneg_iff_rh'])
CPB = 'relay `data/b558_cp1b.txt` :%s'

REWRITES = [
    (13, 'the programme\'s single open premise `h2` (realization-totality at the ξ interface), carried openly,',
     'the programme\'s single open premise `h2` (realization-totality at the ξ interface), in its Weil form `h2_sign`, equivalent to RH '
     '(%s), so the conditional\'s premise is RH itself, carried openly,' % H2),
    (13, 'The certifiable surround `h1` (the eight couplings at Φ) is complete; only `h2` is open (goal ⇐ h1 ∧ h2).',
     'The certifiable surround `h1` (the eight couplings at Φ) is complete, and lv’s `h2` at Φ, `mellin Φ (s/2) ≠ 0`, is false at every s '
     'with re s ≤ 1 (%s), so the goal state (goal ⇐ h1 ∧ h2) closes nothing on the strip; the open clause is `h2_sign`, equivalent to RH '
     '(%s).' % (MP, H2)),
    (238, 'carried openly — see the correction note).*',
     'carried openly — see the correction note; in its Weil form `h2_sign`, equivalent to RH by %s, so the premise is RH itself).*' % H2),
    (242, 'the programme\'s single open leg carried openly —',
     'the programme\'s single open leg carried openly, in its Weil form `h2_sign`, equivalent to RH (%s), so the premise is RH itself —' % H2),
    (250, '*under the exhaustiveness premise* `h2`,',
     '*under the exhaustiveness premise* `h2`, in its Weil form `h2_sign` and equivalent to RH (%s),' % H2),
    (357, '| **DERIVES** — goal ⇐ h1 ∧ h2; h1 complete, **only h2 open** |',
     '| **DERIVES** — goal ⇐ h1 ∧ h2; h1 complete, and lv’s h2 at Φ false at every s with re s ≤ 1 (%s), so the goal state closes nothing on '
     'the strip; the open clause is `h2_sign`, equivalent to RH (%s) |' % (MP, H2)),
    (360, 'carried openly as the single open premise |',
     'carried openly as the single open premise, in its Weil form `h2_sign`, equivalent to RH (%s) |' % H2),
    (382, '*under* `h2`, off-line zeros do not occur.',
     '*under* `h2`, in its Weil form `h2_sign` and equivalent to RH (%s), off-line zeros do not occur.' % H2),
    (406, 'certifies the positivity up to the Voros detection threshold and no further',
     'certifies the positivity up to the Voros detection threshold and no further, and only under two uncompiled literature premises '
     '(Bombieri–Lagarias `ExplicitFormulaDecomp`, Voros `TailBoundPremise`) with `VerifiedZerosTo T`, T1-lit (%s), while Li positivity at '
     'every n is RH itself (%s)' % (CPB % '278', LI)),
]
RA = 'the programme’s RH argument'
HO = 'the open premise `h2`'
CEILS = [
    (23, 'the structural reason positivity holds.', 'the programme’s structural reason for positivity.'),
    (23, 'to close the effective dominance question — off-line zeros are excluded structurally,',
     'to the effective dominance question — off-line zeros excluded under %s,' % HO),
    (124, 'The positivity of $\\mathrm{Re}(\\xi\'/\\xi)$ rests on', 'The programme’s argument for the positivity of $\\mathrm{Re}(\\xi\'/\\xi)$ rests on'),
    (148, '— never crosses zero. $\\square$', '— does not cross zero on the 30 computed R-curves. $\\square$'),
    (150, 'The Beta Maintenance interpretation: $\\beta$ does not change sign on any R-curve because',
     'The Beta Maintenance interpretation, in the programme’s argument: $\\beta$ does not change sign on any R-curve because'),
    (152, 'The result confirms condition (iii) of the Equivalence Chain', 'The result argues for condition (iii) of the Equivalence Chain, which the chain makes equivalent to RH,'),
    (158, 'provides the structural floor that confines zeros to the critical line.',
     'provides the structural floor %s uses to confine zeros to the critical line.' % RA),
    (164, 'The structural picture of why positivity holds is given by', 'The programme’s structural picture of positivity is given by'),
    (234, 'The catalogue is exhaustive: Conservation of Spectra (proved within ZFC from Tate\'s thesis) establishes',
     'The catalogue’s exhaustiveness is %s, in its Weil form `h2_sign` equivalent to RH (%s), which the manuscript argues from Conservation '
     'of Spectra (proved within ZFC from Tate\'s thesis), read as establishing' % (HO, H2)),
    (256, 'The answer is no, by exhaustive enumeration from the finite specification.',
     'The programme’s answer is no, by exhaustive enumeration from the finite specification, its exhaustiveness %s.' % HO),
    (260, 'no off-line zeros (from the specification)', 'no off-line zeros (from the specification, under %s)' % HO),
    (266, 'it derives it as output.', 'it derives it as output, under %s.' % HO),
    (339, 'to the quantities that confine zeros.', 'to the quantities %s uses to confine zeros.' % RA),
    (380, '## Connection to the SIDE proof of RH', '## Connection to the SIDE argument for RH'),
    (384, 'and that the geometric condition holds for the specific structural reason', 'and argues that the geometric condition holds for the specific structural reason'),
    (384, 'direct mechanism enumeration (deposited proof)', 'direct mechanism enumeration (the deposited argument, %s)' % HO),
    (386, 'which is closed by the seven-class catalogue.', 'which the seven-class catalogue closes under %s.' % HO),
    (416, 'the criterion holds with a margin reflecting RH at the edge', 'the criterion holds on the computed range with a margin reflecting RH at the edge'),
]
HEADINGS = (380,)
STEMS = [(355, '(the all-n tail is the open gap)', '(the all-n tail is the open range)')]
B27 = 'SIDE-kernel branch `derivative-engine` = `27a3ae7`'
B27N = 'SIDE-kernel branch `derivative-engine` at `27a3ae7` (an ancestor three commits behind its head `01e5633`, `Kernel/DerivativeEngine.lean` unchanged)'
FACTS = [(350, B27, B27N), (351, B27, B27N), (352, B27, B27N)]
CARRIED = {
    17: 'the class exclusions as compiled: “excludes off-line zeros from the seven-class catalogue”; conditional: “with off-line zeros absent … follows”',
    42: 'the simplicity conditional, standing: “At a simple zero ρ_k, the perpendicular crossing theorem …”',
    195: 'true: the fixed constant “is unconditionally overwhelmed by the Gamma floor for t > 12.57”',
    238: 'the premise stated as an assumption: “*Assume* … (the seven-class catalogue is exhaustive at the ξ interface …)”',
    242: 'the class exclusions as compiled, its first sentence: “no mechanism class … produces a zero with σ ≠ 1/2”',
    256: 'the method’s claim, its first sentence: “SIDE breaks the circle by changing the question”',
    382: 'the class exclusions as compiled: “No class produces off-line zeros”',
    386: 'the simplicity conditional, standing: “the shielded perpendicular-crossing route, conditional on simplicity”',
    396: 'the manuscript’s Conservation of Spectra, not a statement about RH: “No external forces act”',
    398: 'the manuscript’s Conservation of Spectra, not a statement about RH: “Conservation guarantees …”',
}
SIMPLICITY = (42, 386)
VERSION = (9, '*v0.2.2, 2026-10-01*')
ASSIGN = {'RCURVE:13:208': 1, 'RCURVE:13:209': 1, 'RCURVE:238:211': 1, 'RCURVE:242:212': 1, 'RCURVE:250:214': 1, 'RCURVE:357:219': 1,
          'RCURVE:360:220': 1, 'RCURVE:382:222': 1}
READING_NAME = {0: 'none -- resolved by the form', 1: '(a) h2 takes h2_sign'}
CEILING = re.compile(r'RH proved|RH is proved|h2_sign proved|λ_n ≥ 0 proved|GRH proved|GRH reduced|reduction machine-verified|proof of RH|'
                     r'proves RH|RH proves|RH proof|[Pp]roof of GRH|GRH holds|[Tt]he proof\b|same proof\b|is a proof\b|GRH (?:is )?established|'
                     r'becomes? unconditional\b|is unconditional\b|\([Uu]nconditional\)|kernel-verified\)\.|positivity holds|that confines? zeros|'
                     r'excluded structurally|catalogue is exhaustive|The answer is no,|deposited proof|is closed by the seven|never crosses zero|'
                     r'confirms condition \(iii\)|criterion holds with a margin')
CEIL_RECORD = 'ceiling correction record:'
CARRY_RECORD = 'ceiling read, carried:'
STEM_RECORD = 'banned stem, correction record:'
BM_TAG = '<!-- b583 (R193) THE v0.2.2 EDITION`S BACK MATTER, 2026-10-01 -->'
BANKROWS = (('b558_cp1b.txt', 278),)


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _rows():
    return [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'RCURVE' and r['verdict'] == 'MOVED-IN-MEANING']


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    """### the edition's final line for a current-version line: +2 from :9 (the version line and a blank)."""
    return n + (2 if n >= VERSION[0] else 0)


OFFSET = ('+2 from :9 (the v0.2.2 version line and a blank, above the v0.2.1 version line); no other insertion -- v0.2.1 :n sits at the '
          'edition`s :n+2 for n >= 9')


def _all_changes():
    return REWRITES + CEILS + STEMS + FACTS


def edition(*a):
    """### PLACE-papers phase1.5/rcurve/R_CURVE_CRITERION_v0_2_2.md, beside the current version from its blob at 97da72c; the re-pin
    ### step run last over the final body."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE 97da72c -- NOTHING WRITTEN')
    edp = os.path.join(PP, *ED.split('/'))
    if os.path.exists(edp) and 'again' not in a:
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    if g(PP, 'ls-files', ED).strip():
        sys.exit('### THE EDITION FILE IS COMMITTED -- NOTHING WRITTEN')
    new = list(cur)
    for ln, old, rep in _all_changes():
        line = new[ln - 1]
        if line.count(old) != 1:
            sys.exit('### :%d -- THE FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE (%d): %s' % (ln, line.count(old), old[:80]))
        n0 = len(_segs(line))
        new[ln - 1] = line.replace(old, rep)
        if len(_segs(new[ln - 1])) != n0:
            sys.exit('### :%d -- THE REWRITE CHANGED THE LINE`S SEGMENT COUNT %d -> %d' % (ln, n0, len(_segs(new[ln - 1]))))
    if cur[VERSION[0] - 1] != '*v0.2.1, May 2026 (rev. 2026-07-23)*':
        sys.exit('### THE VERSION ANCHOR IS NOT WHERE THE FACE SAYS')
    diff = []
    for r in _rows():
        ln = r['line']
        k = _segs(cur[ln - 1]).index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d] in nw]
        banks = re.findall(r'relay `data/[^`]+` :\d+', nw)
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         reading=ASSIGN.get(r['id'], 0), cites=cites, banks=banks, supports=r['reading']))
    new[VERSION[0] - 1:VERSION[0] - 1] = [VERSION[1], '']
    body = list(new)
    changed = set(x[0] for x in _all_changes())
    if any(_edl(n) > len(body) or (n not in changed and body[_edl(n) - 1] != cur[n - 1]) for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL DOES NOT CARRY THE CURRENT VERSION')
    hits = [(i, m.group(0)) for i, l in enumerate(body, 1) for m in CEILING.finditer(l)]
    stray = sorted(set(i - (2 if i >= VERSION[0] + 2 else 0) for i, _ in hits) - set(CARRIED))
    if stray:
        sys.exit('### A CEILING HIT IN THE BODY IS NEITHER CORRECTED NOR CARRIED BY THE SEAT`S READ: current lines %s' % stray)
    bm = ['', BM_TAG, '',
          '## Back matter of the v0.2.2 edition -- written 2026-10-01 by b583 under the author’s ruling `(R193)`(3), by the form of `(R187)`(5)',
          '',
          '*This file is v0.2.2 of R_CURVE_CRITERION, the CP-7 edition written beside v0.2.1 (`%s`, unedited) from v0.2.1’s tier block (its '
          ':477, standing) and its CP-1b work-list (relay `%s`), the ζ page as its spine; it does not deposit and does not replace v0.2.1, and '
          'its promotion is CP-8’s. Every line cited below is this file’s own.*' % (CUR, WL), '',
          '### Removals', '',
          'None: every one of the 10 work-list rows resolves to a sentence rewritten in place to what its compiled fact says.', '',
          '### Credit lines', '',
          'None: the work-list places no CREDIT row, and the one b450 item for this document (relay `data/b450_batch.json`, “does not carry: '
          'the absent pin bd2ae1a”) is closed by the record, not by a credit: the document never carried that pin; it is the PLACE-papers '
          'sitting commit of 2026-07-25 (`ERRATA.md` :757, E-2026-09-27-1), and b557 corrected the census sentence that attributed it here '
          '(`phase2/method/THE_KEYSTONE_CENSUS.md` :285, :287).', '',
          '### Stem corrections', '', '| this edition’s line | v0.2.1 wording | v0.2.2 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in STEMS:
        bm.append('| :%d | %s %s (banned stem; correction record) | %s | corrected under the stem clause |' % (_edl(ln), STEM_RECORD, old, rep))
    bm += ['', '### Ceiling corrections', '', '| this edition’s line | v0.2.1 wording | v0.2.2 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in CEILS:
        bm.append('| :%d | %s %s | %s | corrected under the ceiling clause%s |' % (_edl(ln), CEIL_RECORD, old, rep,
                                                                                 ', a heading' if ln in HEADINGS else ''))
    bm += ['', '### Ceiling-shaped sentences read and carried', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(CARRIED):
        bm.append('| :%d | %s %s | carried as read |' % (_edl(ln), CARRY_RECORD, CARRIED[ln]))
    bm += ['', '### Fact corrections', '', '| this edition’s line | v0.2.1 wording | v0.2.2 wording | the printed fact | Status |', '|:--|:--|:--|:--|:--|']
    for ln, old, rep in FACTS:
        bm.append('| :%d | %s | %s | SIDE-kernel branch `derivative-engine` heads at `01e5633` locally and at the remote; `27a3ae7` is its '
                  'ancestor three commits back, `Kernel/DerivativeEngine.lean` unchanged between them (relay `data/b583_reads.txt`) | corrected '
                  'under the fact clause |' % (_edl(ln), old, rep))
    bm += ['', '### The navigator’s expectations of `(R193)`(3) with no sentence to write', '',
           '| object | the read | Status |', '|:--|:--|:--|',
           '| the simplicity conditional | its sentences at this edition’s :%d and :%d, carried unchanged; simplicity is outside the compiled faces | stands |' % (
               _edl(SIMPLICITY[0]), _edl(SIMPLICITY[1])),
           '| lv’s residue terminals at `v0.11.0` = `2f71068` | no sentence of v0.2.1 cites a residue terminal; the nearest row, the R4 positivity '
           'interface at this edition’s :%d, is unmarked and its pin `v0.7.0` = `2d86182` agrees with its tag | no object, nothing written |' % _edl(358),
           '| the tier block | v0.2.1 :477, at this edition’s :%d | stands |' % _edl(477),
           '', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v0.2.2 | `%s` | written at b583 |' % ED,
           '| the current version, v0.2.1 | `%s` | unedited |' % CUR,
           '| the spine | `%s` at PLACE-papers `%s` | read, unedited |' % (PAGE, MIRROR_PIN),
           '| the work-list | relay `%s` | read |' % WL,
           '| the erratum and the census lines | `ERRATA.md`, `phase2/method/THE_KEYSTONE_CENSUS.md` | read, unedited |',
           '| the sentence-by-sentence diff | relay `data/b583_edition_RCURVE.txt` | banked at b583 |',
           '', '### Correspondence', '',
           '| declaration or bank line | repository | pin as the page prints it | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    # ### THE RE-PIN STEP, LAST
    ed_lines = {d: [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l and PIN[d] in l] for d in PIN}
    for d in PIN:
        bm.append('| `SIDEExplicitFormula.%s.%s` | %s | %s | %s | cited at :%s of this edition |' % (
            NS[d], d, EF, PIN[d].replace('`', ''), WHERE[d], ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    bank_lines = {}
    for bank, n in BANKROWS:
        at = [i for i, l in enumerate(body, 1) if ('relay `data/%s` :%d' % (bank, n)) in l]
        bank_lines['%s:%d' % (bank, n)] = at
        bm.append('| `data/%s` :%d | relay | the CP-1b bank (b558) | not on a page | cited at :%s of this edition |' % (
            bank, n, ', :'.join(str(x) for x in at) or '### NONE'))
    bm.append('')
    full = body + bm
    if any('### NONE' in l for l in bm):
        sys.exit('### A CORRESPONDENCE ROW CITES NO LINE OF THE EDITION')
    b = (NL.join(full) + NL).encode('utf-8')
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    put_json('b583_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=0, removals=0, ruled_citations=0, version_lines=1, diff=diff, offset=OFFSET,
                                       ceils=CEILS, stems=STEMS, facts=FACTS, carried={str(k): v for k, v in CARRIED.items()},
                                       version=dict(above=VERSION[0], text=VERSION[1]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines,
                                       bank_lines=bank_lines))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))


def edition_bank():
    """### The diff with its offset line, the corrections, the counts, the ceiling read, H28a-H28c."""
    E = jl('b583_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(BM_TAG)
    scan = rd('b583_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    carried_ed = set(_edl(n) for n in CARRIED)
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            kind = ('record' if (i > cut and l.startswith('| :') and (CEIL_RECORD in l or CARRY_RECORD in l))
                    else 'carried' if (i < cut and i in carried_ed) else 'beyond')
            hits.append(dict(line=i, hit=m.group(0), kind=kind, ctx=l[max(0, m.start() - 60):m.end() + 20]))
    beyond = [h for h in hits if h['kind'] == 'beyond']
    h28a_bad = [d['id'] for d in E['diff'] if not d['changed'] or not (d['cites'] or d['banks'])]
    h28a = 'HELD' if not h28a_bad else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur']
    allowed = E['credit'] + E['removals'] + E['ruled_citations'] + E['version_lines']
    h28b = 'HELD' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HELD' if (live and int(live.group(1)) == 0 and clean and not beyond) else 'REFUTED'
    cur0 = _cur()
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % OFFSET, '',
         'b583 -- COMPONENT 2: THE EDITION OF R_CURVE_CRITERION, (R193)(3), BY THE FORM OF (R187)(5) AND ITS CLAUSES', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :9 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0], cur0[8]),
         '### its tier block : :477 "%s"' % cur0[476][:110],
         '### its version history : v0.1 (:458), v0.2 (:460), the head line v0.2.1 (:9); the b397 disclosure (:465)',
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE NAVIGATOR`S EXPECTATIONS OF (R193)(3) AGAINST THIS DOCUMENT: (a) sentences naming h2 take h2_sign -- 8 rows ; (b) the '
         'simplicity conditional -- no marked row; :42 and :386 carried unchanged ; (c) the bd2ae1a item -- closed by E-2026-09-27-1 and '
         'the census lines, no credit ; (d) lv`s residue terminals -- no object', '',
         '### THE WORK-LIST, ROW BY ROW (10 rows, 9 sentences, 8 lines) -- each row: v0.2.1`s line and the edition`s, the terminal, the '
         'expectation it falls under (the seat`s hand-read), what its sentence cites, the sentence before and after.', '']
    for d in E['diff']:
        L += ['  %s v0.2.1 :%d -> v0.2.2 :%d `%s` -- %s ; cites %s%s' % (d['id'], d['line'], d['ed_line'], d['terminal'], READING_NAME[d['reading']],
                                                                     ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']],
                                                                     (' ; bank ' + ', '.join(d['banks'])) if d['banks'] else ''),
              '      work-list: %s' % d['supports'],
              '      v0.2.1 : %s' % d['old'], '      v0.2.2 : %s' % d['new'], '']
    cov = [d for d in E['diff'] if d['reading']]
    L += ['### (N1) COVERAGE BY THE EXPECTATIONS OF (R193)(3), the seat`s hand-read: %d of %d rows -- (a) %d ; uncovered %s, resolved by the form'
          % (len(cov), len(E['diff']), sum(d['reading'] == 1 for d in E['diff']),
             [':%d `%s`' % (d['line'], d['terminal']) for d in E['diff'] if not d['reading']]), '',
          '### THE STEM CORRECTIONS:'] + ['    v0.2.1 :%d -> v0.2.2 :%d  "%s" -> "%s"' % (s[0], _edl(s[0]), s[1], s[2]) for s in E['stems']]
    L += ['### THE CEILING CORRECTIONS (%d, on %d lines; %d of them headings):' % (len(E['ceils']), len(set(c[0] for c in E['ceils'])),
                                                                               sum(1 for c in E['ceils'] if c[0] in HEADINGS))]
    L += ['    v0.2.1 :%d -> v0.2.2 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in E['ceils']]
    L += ['### THE CEILING-SHAPED SENTENCES READ AND CARRIED (%d lines):' % len(CARRIED)]
    L += ['    v0.2.1 :%d -> v0.2.2 :%d  %s' % (n, _edl(n), CARRIED[n]) for n in sorted(CARRIED)]
    L += ['### THE FACT CORRECTIONS (%d):' % len(E['facts'])]
    L += ['    v0.2.1 :%d -> v0.2.2 :%d  "%s" -> "%s" ; source: the branch head read locally and at the remote, the ancestry and the diff, '
          'printed in data/b583_reads.txt' % (f[0], _edl(f[0]), f[1], f[2]) for f in E['facts']]
    L += ['### THE VERSION LINE: above v0.2.1 :%d: %s' % (E['version']['above'], E['version']['text']),
          '### REMOVALS: none. ### CREDIT LINES: none (the bd2ae1a item closed by E-2026-09-27-1). ### HISTORY LINES: none.', '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d: the version '
          'line) ; the back matter %d ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d + one version line = %d' % (
              body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], {'record': 'quoted in a back-matter record, read by the seat',
                                                                 'carried': 'in a sentence the seat read and carried',
                                                                 'beyond': '### BEYOND THE CEILING'}[h['kind']], h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### the banned-stem scan of the edition (relay data/b583_edition_termscan.txt): live uses %s ; verdict %s' % (
              live.group(1) if live else '?', 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on the page at its pin, or a bank line%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- live banned stems %s, sentences beyond the ceiling %d.**' % (h28c, live.group(1) if live else '?', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b583_edition_RCURVE.txt', L)
    put_json('b583_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None, beyond=len(beyond), hits=hits,
                                   covered=len(cov), uncovered=[d['id'] for d in E['diff'] if not d['reading']], held=None,
                                   n_ceils=len(E['ceils']), n_ceil_lines=len(set(c[0] for c in E['ceils'])), n_facts=len(E['facts'])))
    H = jl('b583_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'covered', H['covered'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'],
          'live', H['live'], 'ceils', H['n_ceils'], 'facts', H['n_facts'])


# ================================================================================ THE SCORING AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}


def scores():
    H, E = jl('b583_h28.json'), jl('b583_edition.json')
    ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'ls-files', '--others', '--exclude-standard', 'phase1.5', 'phase2')).split(NL) if x.strip()))
    kmain = g('D:/SIDE-explicit-formula', 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    cur_same = g(PP, 'hash-object', CUR).strip() == E['cur_blob']
    n2 = H['H28a'] == 'HELD' and H['H28b'] == 'HELD' and H['H28c'] == 'HELD' and H['held'] is None
    allowed_pp = {'FINDINGS.md', 'OPEN_TRAILS.md', ED}
    edtxt = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read()
    n3 = E['credit'] == 0 and 'E-2026-09-27-1' in edtxt and 'Credit (' not in edtxt
    S = dict(
        N1=('HELD' if H['covered'] >= 5 else 'REFUTED', 'the expectations of (R193)(3) cover %d of the 10 MOVED rows by the seat`s hand-read '
            '(the h2 expectation); uncovered %s, resolved by the form' % (H['covered'], H['uncovered'])),
        N2=('HELD' if n2 else 'REFUTED', 'H28a %s, H28b %s (the body %+d against at most %d), H28c %s; no sentence held' % (
            H['H28a'], H['H28b'], H['body_dn'], H['allowed'], H['H28c'])),
        N3=('HELD' if n3 else 'REFUTED', 'the bd2ae1a item closed in the back matter by E-2026-09-27-1 and the census lines; credit lines %d'
            % E['credit']),
        N4=('HELD' if H['n_ceils'] < 10 and H['n_facts'] == 0 else 'REFUTED', 'the ceiling clause corrects %d phrases on %d lines (not fewer '
            'than ten); the fact clause finds %d (the three derivative-engine rows) -- both halves fail' % (H['n_ceils'], H['n_ceil_lines'], H['n_facts'])),
        N5=('HELD' if (kmain == V015 and heads_ok and cur_same and set(ch) <= allowed_pp) else 'REFUTED', 'nothing deposits; no kernel '
            'touched (%s); the current R_CURVE_CRITERION unedited (%s); PLACE-papers changed at %s' % (
                'held' if kmain == V015 and heads_ok else '### MOVED', 'held' if cur_same else '### EDITED', ch)),
        S1=('HELD' if H['covered'] == 8 else 'REFUTED', '(N1) holds at 8 of 10; :357`s h1 row and :406 resolved by the form'),
        S2=('HELD' if n2 and H['body_dn'] == 1 and H['allowed'] == 1 else 'REFUTED', 'H28a-H28c held; the body +1 against 1'),
        S3=('HELD' if n3 else 'REFUTED', '(N3) holds'),
        S4=('HELD' if H['n_ceils'] == 18 and H['n_facts'] == 3 else 'REFUTED', '(N4) refuted on both halves: 18 ceiling corrections, 3 fact corrections'),
        S5=('HELD' if set(ch) == allowed_pp else 'REFUTED', '(N5) holds: the files changed are the three its list names'),
        counts=dict(pp_changed=ch, body_dn=H['body_dn'], covered=H['covered'], ceils=H['n_ceils'], facts=H['n_facts']),
    )
    put_json('b583_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], S[k][1][:150]))


TITLE_HEAD = ('## CP-7, act eight: the edition of R_CURVE_CRITERION from its tier block and work-list, the simplicity conditional carried as a '
              'conditional')
TITLE = TITLE_HEAD + '; written as v0.2.2 beside v0.2.1, no sentence held'
TRAIL_HEAD = ('### b583 — lane three, act eleven under (R193): CP-7 act eight -- the edition of R_CURVE_CRITERION written beside the current, '
              'the ζ page as its spine')


def records_pp():
    Q = _Q()
    S, H, E, C1 = jl('b583_scores.json'), jl('b583_h28.json'), jl('b583_edition.json'), jl('b583_c1_lines.json')
    ln = C1['lines']
    Q.guard_absent(Q.FIND, TITLE_HEAD)
    e = ['', TITLE, '',
         '*Filed at b583 on the author’s ruling `(R193)`. Banks: relay `data/b583_edition_RCURVE.txt` (the sentence-by-sentence diff, its '
         'offset line at its head), `data/b583_edition.json`, `data/b583_reads.txt`. Nothing deposits.*', '',
         '**The edition** (`(R193)`(3)): `%s`, v0.2.2, written beside v0.2.1 (`%s`, unedited) from v0.2.1’s tier block and its CP-1b '
         'work-list, the ζ page as its spine. The 10 work-list rows resolve to 9 sentences on 8 lines, each rewritten in place: every '
         'conditional on the exhaustiveness premise kept as a conditional, its premise named in its Weil form and cited to its equivalence '
         'with RH, so that the premise is RH itself; lv’s goal state said to close nothing on the strip; the finite-range Li certificate said '
         'to rest on two uncompiled literature premises, with Li positivity at every n cited as RH itself. The simplicity conditional stands '
         'as a conditional. The one b450 item, the absent pin, closes by the erratum and the census lines, no credit inserted. One stem use, '
         '%d phrases beyond the ceiling on %d lines (one heading) and three branch pins are corrected; no sentence is removed and none held.'
         % (ED, CUR, H['n_ceils'], H['n_ceil_lines']), '',
         '**The counts.** v0.2.1 %d sentences; v0.2.2 %d (the body %d, the back matter %d); the body differs by %+d against the final bound, %d.'
         % (E['n_cur'], E['n_full'], E['n_body'], E['n_backmatter'], H['body_dn'], H['allowed']), '',
         '**H28a %s · H28b %s · H28c %s.** Coverage of the 10 rows by the navigator’s expectations: %d.' % (H['H28a'], H['H28b'], H['H28c'], H['covered']), '',
         '**The record lines** (`(R193)`(1)-(2)): b582’s weight (FINDINGS :%d); the shells’ wording recorded as the navigator’s (OPEN_TRAILS '
         ':%d); the (N1) pattern, advance readings entered as expectations (:%d).' % (ln['weight'], ln['shells'], ln['pattern']), '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R193)`(4): the edition of INVARIANCE_BARRIERS by the same form; the author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; v0.2.1, README, REGISTRY, ERRATA and both pages unwritten; nothing here is a statement about '
         'RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows = ['', TRAIL_HEAD, '',
            '**(R193) ratified.** (1) b582 at its weight, the shells’ wording the navigator’s. (2) The (N1) pattern: advance readings are '
            'expectations, the form the ruling. (3) The edition of R_CURVE_CRITERION by the form, the ζ page as its spine. (4) The act after.', '',
            '**Entered:** FINDINGS.md:%d (b582’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the shells’ wording), :%d (the (N1) pattern), '
            'this record; PLACE-papers `%s` (created).' % (ln['weight'], Q.line_of(Q.FIND, TITLE_HEAD), ln['shells'], ln['pattern'], ED), '',
            '**No question asked before the seal.** The expectation on lv’s residue terminals had no object (no sentence cites one) and is '
            'recorded at zero cost, as `(R193)`(2) orders. The three derivative-engine rows were corrected under the standing fact clause, '
            'the same species as b582’s footer pin.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
            % tuple(S[k][0] for k in SCORE_KEYS), '',
            '**Next:** per `(R193)`(4), CP-7 act nine, b584 -- the edition of INVARIANCE_BARRIERS by the same form, H28a-H28c scored; the '
            'author rules on the closing.', '',
            '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
            'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows))
    put_json('b583_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE_HEAD), title=TITLE, append=r))
    put_json('b583_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r2))
    print(jl('b583_findings.json')['entry_line'], jl('b583_trail.json')['line'])


def desk():
    S = jl('b583_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b583 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b583_defects.txt').rstrip(NL).split(NL)
    put_txt('b583_desk_notes.txt', L)


def components():
    S, H, C1, fj, tj = (jl('b583_scores.json'), jl('b583_h28.json'), jl('b583_c1_lines.json'), jl('b583_findings.json'), jl('b583_trail.json'))
    ln = C1['lines']
    L = ['b583 -- THE COMPONENTS, BANKED UNDER (R193).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b582`s closing push-out relay 4058782f ; push-b582* branches deleted by '
         'name (data/b583_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : b582`s weight FINDINGS :%d ; the shells` wording OPEN_TRAILS :%d ; the (N1) pattern :%d' % (
             ln['weight'], ln['shells'], ln['pattern']),
         '### COMPONENT 2 : the edition %s ; 9 sentences rewritten, 1 stem correction, %d ceiling corrections on %d lines, %d fact corrections, '
         'the version line, 0 removals, 0 credits ; data/b583_edition_RCURVE.txt ; H28a %s H28b %s H28c %s ; N1 %s N2 %s N3 %s N4 %s' % (
             ED, H['n_ceils'], H['n_ceil_lines'], H['n_facts'], H['H28a'], H['H28b'], H['H28c'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0]),
         '### COMPONENT 3 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; next: the edition of INVARIANCE_BARRIERS ; N5 %s'
         % (fj['entry_line'], tj['line'], S['N5'][0])]
    put_txt('b583_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b583_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
