# -*- coding: utf-8 -*-
"""b584_record.py -- THE ACT'S RECORD TOOL, UNDER (R194). ### ONE SUBCOMMAND PER BANK.

### ### b584: LANE THREE, ACT TWELVE -- CP-7 ACT NINE, THE EDITION OF INVARIANCE_BARRIERS; THE CEILING CENSUS OVER THE ROSTER; TWO
### WORK-ORDERS ENTERED. Subcommands write only `data/b584_*` unless the docstring names another file. Every bank is written through
### `put_txt` / `put_json` (encode first, then a temp file, then `os.replace`). This act makes no platform call. ### The template is
### b583_record.py.
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
PRE_PP = '9d11874'
MIRROR_PIN = '192077f'
CUR = 'phase1.5/method/INVARIANCE_BARRIERS.md'
ED = 'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
WL = 'data/b558_editions/INVARIANCE_BARRIERS.txt'
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
    '(a) THE FACE`S FIRST DRAFT CARRIED THREE COUNT-SHAPED PHRASES (U-1`s lexical counter: "two documents", "3 terminal" in "Route 3 '
    'terminal`s", "22 documents"); reg_satisfiable read NOT SATISFIABLE and the lock gate refused at 7 of 8 (relay '
    'data/b584_lockgate_notes.txt, its first run). The unsealed face was reworded at the three phrases, the gates re-run, and the lock '
    'permitted at 8 of 8 (data/b584_lockgate_notes2.txt); nothing was sealed before.',
    '(b) COMPONENT 1`S FIRST RUN STOPPED AT ITS SECOND APPEND: the work-order heading carried two backtick possessives ("TITLE`S", '
    '"author`s"), the append guard refused the unbalanced backticks, and FINDINGS already held the weight line (two lines). FINDINGS was '
    'restored from HEAD and the restoration printed (blob 70ce0bb = HEAD); the possessives were written ’, and Component 1 re-run whole. '
    'OPEN_TRAILS was not touched by the first run.',
    '(c) THE EDITION`S FIRST RUN REFUSED AT ITS OWN ANCHOR CHECK: the check tested :257 for a blank where :257 is Theorem 3.7 and :258 the '
    'blank (an off-by-one in the seat`s guard). Nothing was written; the guard was corrected and the edition written.',
    '(d) THREE CARRIED SUITE CONSTANTS WERE b583`S: G-H28B-COUNTED fixed the bound at 1 (this act`s is 2: the credit and the version '
    'line); G-COVERAGE-BANKED`s positive control set the coverage to 10 and G-H28B-COUNTED`s set the body difference to 2 -- each this '
    'act`s true value -- so neither control could fail (and G-ARMS-NO-LIVE-LIMB failed with them). Each was set off this act`s values in '
    'the uncommitted suite, found over two re-runs, and the suite re-run; no bank or corpus byte changed.',
]


def defects():
    put_txt('b584_defects.txt', ['### b584 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


RELAY = ROOT.replace('\\', '/')
ROWLINES = [382, 385, 386, 387, 390, 391, 393, 397, 398, 402]
SEARCH = (('Face E / keyhole', ('keyhole', 'Face E')), ('the T3 Tier-1 scope', ('Tier-1 scope', 'T3 Tier-1')))
READS = [
    ('relay the INVARIANCE_BARRIERS work-list, whole', RELAY, 'HEAD', WL, list(range(1, 56))),
    ('PLACE-papers INVARIANCE_BARRIERS, its head, Abstract and section 1.1', PP, PRE_PP, CUR, list(range(1, 32))),
    ('PLACE-papers INVARIANCE_BARRIERS, the marked, credit-anchor and ceiling-read lines', PP, PRE_PP, CUR,
     [63, 255, 257, 258, 350, 354, 427, 493, 499, 516, 520, 538, 580, 677, 711]),
    ('PLACE-papers INVARIANCE_BARRIERS, its version history, era annotation and tier block', PP, PRE_PP, CUR, list(range(526, 545)) + list(range(697, 748))),
    ('PLACE-papers the zeta page at the mirror`s pin, its pin line, nodes 7, 8, the open line and the mellin row', PP, MIRROR_PIN, PAGE, [3, 11, 12, 31, 138]),
    ('relay the CP-1b bank, its head and the INVARIANCE_BARRIERS rows', RELAY, 'HEAD', 'data/b558_cp1b.txt', list(range(1, 9)) + ROWLINES),
    ('PLACE-papers OPEN_TRAILS, b454`s ledger table and b455`s resolution', PP, PRE_PP, 'OPEN_TRAILS.md', [531, 6759, 6760, 6766, 6768, 6845, 6879]),
    ('PLACE-papers OPEN_TRAILS, the form, the order, its clauses and b583`s record', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11864, 11884, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 11974, 11976, 11994, 11996, 11998]),
    ('PLACE-papers FINDINGS, b583`s entry', PP, PRE_PP, 'FINDINGS.md', [6588]),
    ('relay the roster, CP-1`s 22 documents', RELAY, 'HEAD', 'data/b557_roster.txt', list(range(1, 27))),
    ('PLACE-papers README, the ceiling', PP, PRE_PP, 'README.md', list(range(104, 122))),
    ('relay tools/banned_terms.py, the stems and the exceptions', RELAY, 'HEAD', 'tools/banned_terms.py', list(range(1, 81))),
    ('relay b583`s closing push-out, its head', RELAY, 'HEAD', 'data/b583_closing_push_out.txt', list(range(1, 4))),
]
PINS = (('SIDE-kernel', 'v1.7', '2957e7d'), ('SIDE-kernel', 'v1.4', 'f374174'), ('SIDE-explicit-formula', 'v0.1', 'baed4df'),
        ('SIDE-explicit-formula', 'v0.2', '5c72cad'), ('SIDE-explicit-formula', 'v0.11', '19b7d1e'))


def _peel(repo, tag):
    p = 'D:/' + repo
    loc = g(p, 'rev-parse', tag + '^{}').strip()
    peeled = [l.split('\t')[0] for l in g(p, 'ls-remote', 'origin', 'refs/tags/%s^{}' % tag).split(NL) if l.strip()]
    rem = [l.split('\t')[0] for l in g(p, 'ls-remote', 'origin', 'refs/tags/%s' % tag).split(NL) if l.strip()]
    return loc, (peeled or rem or [''])[0]


def _search():
    out = []
    for label, needles in SEARCH:
        for led in ('FINDINGS.md', 'OPEN_TRAILS.md'):
            t = g(PP, 'show', '%s:%s' % (PRE_PP, led)).split(NL)
            for nd in needles:
                hits = [i + 1 for i, l in enumerate(t) if nd.lower() in l.lower()]
                out.append(dict(finding=label, ledger=led, needle=nd, hits=hits))
    return out


def reads():
    L = ['b584 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    L.append('### the fact clause`s read over INVARIANCE_BARRIERS` pins and the edition`s, each tag peeled locally and at the remote:')
    for repo, tag, cited in PINS:
        loc, r = _peel(repo, tag)
        L.append('    %s %s : cited %s ; local %s ; remote %s ; %s' % (repo, tag, cited, loc[:7], r[:7],
                                                                   'AGREE' if loc.startswith(cited) and r.startswith(cited) else '### DIFFER'))
    L.append('### the two b450 findings, searched by name in FINDINGS.md and OPEN_TRAILS.md at %s (every hit line printed):' % PRE_PP)
    for s in _search():
        L.append('    %-22s %-15s "%s" : %d hit(s) %s' % (s['finding'], s['ledger'], s['needle'], len(s['hits']), s['hits']))
    L += ['### the read of the hits: the T3 Tier-1 scope is LOCATED -- OPEN_TRAILS :6845 (b455) quotes the ledger line that states it',
          '    (OPEN_TRAILS-archive-2 :7971, "Euler-product consumption at Face E`s Tier-1 scope verbatim") and the specification`s row',
          '    ("T3 -- Consume the Euler product essentially. Face E`s barrier is Tier-1 and scoped verbatim"); Face E / keyhole is NOT',
          '    LOCATED -- OPEN_TRAILS :531 is a 2026-08-11 report heading naming a different keyhole item ("KEYHOLE (i)`s STATUS -- DISTINCT"),',
          '    :6759 is b454`s table recording it HELD BY NO LEDGER over 38 hand-read hits, FINDINGS :255 is a Face E scope log, and the',
          '    document`s own body carries no "keyhole"']
    put_txt('b584_reads.txt', L)


# ================================================================================ COMPONENT 1
FORM_HEAD = '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three'
ORDER_HEAD = '*Appended 2026-10-01 by b578, under the author’s ruling `(R188)`(3), to the critical path’s lane three'
B583_ENTRY = '## CP-7, act eight: the edition of R_CURVE_CRITERION'
SF_HEAD = '### `W-ORD-SIMPLICITY-FACE` -- THE TITLE’S CLAUSE AS A PROP AND THE PROPORTION, PRICED, NOT STARTED, appended 2026-10-01, b584, under the author’s ruling (R194)(3)'
PC_HEAD = '### `W-ORD-PNT-CHI` -- ψ(x, χ) WITH AN EXPLICIT ERROR TERM, PRICED, NOT STARTED, appended 2026-10-01, b584, under the author’s ruling (R194)(4)'
SF_LINES = [
    '**Items.** (a) The lemma walk over the vendored Zeta23 modules at `3635e748` for the Alpöge–Furman proportion (at least 2/3 of ζ’s zeros '
    'simple and on the line) by name -- present in the vendored set, or absent with the module that holds it named at the upstream pin. (b) The '
    'title’s clause stated as a Prop in SIDE-explicit-formula over the genuine configuration (every zero of multiplicity one), salt-checked, '
    'with the proportion compiled or vendored as a T0 fact beside it if (a) finds it. (c) The reading of what the three faces say about '
    'multiplicity -- carried as weight, constrained by none -- entered on the page’s back matter in one line. (d) The SIMPLICITY keystone’s '
    'claims read against (a)-(c) before its edition.',
    '**Hypotheses.** H29a -- the proportion is in the vendored set by name. H29b -- the title’s Prop salt-checks and no compiled fact in the '
    'federation implies it or its negation. H29c -- SIMPLICITY’s tier block (T2 majority) carries at least one sentence that the proportion '
    'makes MOVED-IN-MEANING.',
    '**Trigger:** the author’s word. **SIMPLICITY_OF_RIEMANN_ZEROS’ edition is HELD behind this work-order or the author’s ruling that it is '
    'out of scope.**',
]
PC_LINES = [
    '**Item.** For each fixed primitive χ, the χ-analogues of Zeta23’s zero-free region (the 39 names) and its zero count, joined to '
    '`EF_lit_chi_holds` to give ψ(x, χ) with an explicit de la Vallée Poussin error term, unconditionally, in the kernel; uniformity in q not in '
    'scope (Siegel).',
    '**Price:** the 39 names by the b571 method plus the count; the navigator expects the Gamma-factor and conductor dependence to be the '
    'substance. **Off the critical path. Trigger:** the author’s word.',
]


def c1_lines():
    """### PLACE-papers FINDINGS (b583's weight) and OPEN_TRAILS (the two work-orders; SIMPLICITY HELD in the order)."""
    Q = _Q()
    form, order, entry = Q.line_of(Q.OT, FORM_HEAD), Q.line_of(Q.OT, ORDER_HEAD), Q.line_of(Q.FIND, B583_ENTRY)
    if not (form == 11864 and order == 11884 and entry == 6588):
        sys.exit('### THE ADDRESSED LINES MOVED: form %s order %s entry %s -- NOTHING WRITTEN' % (form, order, entry))
    heads = dict(
        weight='*Appended 2026-10-01 by b584 to b583’s entry (:%d), under `(R194)`(1) -- b583 AT ITS WEIGHT:*' % entry,
        held='*Appended 2026-10-01 by b584 to the order of the editions (:%d), under the author’s ruling `(R194)`(3) -- SIMPLICITY HELD BEHIND ITS WORK-ORDER:*' % order,
    )
    for k, h in heads.items():
        Q.guard_absent(Q.FIND if k == 'weight' else Q.OT, h)
    Q.guard_absent(Q.OT, SF_HEAD)
    Q.guard_absent(Q.OT, PC_HEAD)
    out = [Q.append_to(Q.FIND, '\n%s `phase1.5/rcurve/R_CURVE_CRITERION_v0_2_2.md` beside v0.2.1 unedited: 10 rows as 9 sentences on 8 lines; '
                                 'every conditional on the exhaustiveness premise kept as a conditional, the premise named in its Weil form and '
                                 'cited to its equivalence with RH; lv’s h2 at Φ said false on the strip; :406’s finite-range certificate '
                                 'resting on two uncompiled literature premises (CP-1b :278); the simplicity sentences at :42 and :386 unchanged; '
                                 'the absent-pin item closed by E-2026-09-27-1 (ERRATA :757) and KEYSTONE_CENSUS :285, :287 with no credit; one '
                                 'stem correction; 18 ceiling corrections on 16 lines, the heading at :380 among them; three fact corrections at '
                                 ':350-:352, the derivative-engine rows’ branch pin, accepted as applied, the same kind as b582’s :395. The '
                                 'expectation on lv’s residue terminals had no object, recorded at zero cost. H28a, H28b (+1 against 1) and H28c '
                                 'held; (N4) refuted on both halves. The suite reads 69 of 69.\n' % heads['weight'])]
    out.append(Q.append_to(Q.OT, '\n' + NL.join([SF_HEAD, ''] + [x + NL for x in SF_LINES]).rstrip(NL) + '\n'))
    out.append(Q.append_to(Q.OT, '\n' + NL.join([PC_HEAD, ''] + [x + NL for x in PC_LINES]).rstrip(NL) + '\n'))
    out.append(Q.append_to(Q.OT, '\n%s SIMPLICITY_OF_RIEMANN_ZEROS’ edition, the tenth in the order, is HELD behind `W-ORD-SIMPLICITY-FACE` or the '
                                 'author’s ruling that the work-order is out of scope for it; the other editions keep their places.\n' % heads['held']))
    lines = {k: Q.line_of(Q.FIND if k == 'weight' else Q.OT, h) for k, h in heads.items()}
    lines['simplicity_face'] = Q.line_of(Q.OT, SF_HEAD)
    lines['pnt_chi'] = Q.line_of(Q.OT, PC_HEAD)
    put_json('b584_c1_lines.json', dict(form=form, order=order, entry=entry, lines=lines, heads=heads, sf_head=SF_HEAD, pc_head=PC_HEAD,
                                        sf_lines=SF_LINES, pc_lines=PC_LINES, appends=out))
    print(lines)


# ================================================================================ COMPONENT 2 -- THE CEILING CENSUS
PHRASE = re.compile(r'\b(prov(?:e|es|ed|en|ing)|proofs? of|establish(?:es|ed|ing|ment)?|holds?|holding|unconditional(?:ly)?)\b', re.I)
OBJECT = re.compile(r'\b(RH|GRH|Riemann Hypothesis|Generalized Riemann Hypothesis|h2|h2_sign|the clause)\b')
NEGATED = re.compile(r"\b(not|no|never|cannot|nor|without|neither)\b|n't", re.I)
HEDGED = re.compile(r'\b(if|once|under|conditional(?:ly)?|would|were|assum\w*|premise|suppos\w*|to the extent|equivalent|iff|whether|until|'
                    r'unless|could|might|may)\b|⟺|↔|⇔', re.I)
FOURTEEN = ['PATHS_TO_THE_CRITICAL_LINE', 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY', 'THE_UNCONDITIONAL_SURROUND',
            'GRH_CASCADE', 'R_CURVE_CRITERION', 'INVARIANCE_BARRIERS', 'INDEX_ARITY_AT_THE_CRITICAL_LINE', 'ENUMERA', 'SIMPLICITY_OF_RIEMANN_ZEROS',
            'EXHAUSTIVENESS_LICENSE', 'TECHNE_TOOLKIT', 'E_DIFFICULTY_THEOREM', 'THE_RESIDUE_OF_RH']
DONE = FOURTEEN[:6]
SPECTRAL = ('phase1.5/spectral/',)


def _roster():
    out = []
    for l in rd('b557_roster.txt').split(NL):
        m = re.match(r'^    (\S+).*?\s{2,}(\S+\.md)\s+:(\d+)\s*$', l)
        if m:
            name, path, tier = m.group(1), m.group(2), int(m.group(3))
            if name == 'A_Place_to_Stand':
                path, tier = 'day1/A_Place_to_Stand.md', None
            out.append((name, path, tier))
    return out


def _classify(text):
    import b558_record as CP
    c = dict(live=0, hedged=0, negated=0)
    for line in text.split(NL):
        for s in CP.segments(line):
            if not s or not OBJECT.search(s):
                continue
            n = len(PHRASE.findall(s))
            if not n:
                continue
            k = 'negated' if NEGATED.search(s) else 'hedged' if HEDGED.search(s) else 'live'
            c[k] += n
    return c


def census():
    """### data/b584_ceiling_census.txt and .json: the count per roster document at its current version, whole file and body above its
    ### tier block, live beside hedged and negated. No edit anywhere."""
    rows = []
    for name, path, tier in _roster():
        t = g(PP, 'show', '%s:%s' % (PRE_PP, path)).replace(chr(13), '')
        ls = t.split(NL)
        body = NL.join(ls[:tier - 1]) if tier else t
        rows.append(dict(name=name, path=path, tier=tier, lines=len(ls), whole=_classify(t), body=_classify(body),
                         spectral=path.startswith(SPECTRAL), mono=name == 'A_Place_to_Stand'))
    if len(rows) != 22:
        sys.exit('### THE ROSTER DID NOT READ AS 22 DOCUMENTS (%d)' % len(rows))
    order = sorted(rows, key=lambda r: -r['whole']['live'])
    rem8 = [r for r in rows if r['name'] in FOURTEEN and r['name'] not in DONE]
    rem7 = [r for r in rem8 if r['name'] != 'INVARIANCE_BARRIERS']
    L = ['b584 -- COMPONENT 2: THE CEILING CENSUS OVER CP-1`S ROSTER, (R194)(2). ### A BANK, NOT A DOCUMENT; NO EDIT ANYWHERE.', '',
         '### THE PHRASE LIST: %s' % PHRASE.pattern,
         '### APPLIED TO (the object, in the same sentence by relay tools/b558_record.py `segments`): %s' % OBJECT.pattern,
         '### A USE IS NEGATED when its sentence matches %s ; HEDGED when it matches %s and is not negated ; LIVE otherwise. Each phrase '
         'occurrence in an object-bearing sentence counts once.' % (NEGATED.pattern, HEDGED.pattern),
         '### THE TEXTS: each roster document at PLACE-papers %s, its current version (the editions written beside are not the current '
         'versions); the monograph read at day1/A_Place_to_Stand.md (the roster names FINDINGS, its tier map); WHOLE = the file, BODY = the '
         'lines above its tier-block line (the monograph has none).' % PRE_PP, '',
         '| document | path | lines | whole: live | hedged | negated | body: live | hedged | negated |', '|:--|:--|--:|--:|--:|--:|--:|--:|--:|']
    for r in order:
        L.append('| %s | %s | %d | %d | %d | %d | %d | %d | %d |' % (r['name'], r['path'], r['lines'], r['whole']['live'], r['whole']['hedged'],
                                                                   r['whole']['negated'], r['body']['live'], r['body']['hedged'], r['body']['negated']))
    tot = lambda rs, k: sum(r['whole'][k] for r in rs)
    L += ['', '### THE THREE LARGEST LIVE COUNTS (whole): %s' % ['%s %d%s' % (r['name'], r['whole']['live'], ' (spectral)' if r['spectral'] else
                                                                                ' (the monograph)' if r['mono'] else '') for r in order[:3]],
          '### THE FOURTEEN`S REMAINING EDITIONS (the eight not written when (R194) was ruled, INVARIANCE_BARRIERS among them): live %d, hedged %d, '
          'negated %d' % (tot(rem8, 'live'), tot(rem8, 'hedged'), tot(rem8, 'negated')),
          '### the seven after this act: live %d' % tot(rem7, 'live'),
          '### the roster`s total: live %d, hedged %d, negated %d' % (tot(rows, 'live'), tot(rows, 'hedged'), tot(rows, 'negated')),
          '### ### **A COUNT, NOT A VERDICT: a LIVE use is a sentence the classifier did not see hedged or negated; each still needs the seat`s '
          'read at its edition. No document was edited.**']
    put_txt('b584_ceiling_census.txt', L)
    put_json('b584_ceiling_census.json', dict(rows=rows, top3=[r['name'] for r in order[:3]], rem8=[r['name'] for r in rem8],
                                              rem8_live=tot(rem8, 'live'), rem7_live=tot(rem7, 'live'), total_live=tot(rows, 'live')))
    print('top3', [(r['name'], r['whole']['live']) for r in order[:3]], 'rem8', tot(rem8, 'live'), 'rem7', tot(rem7, 'live'))


# ================================================================================ COMPONENT 3 -- THE EDITION
EF = 'SIDE-explicit-formula'
PIN = {'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'ch_iff_rh': 'v0.1 = `baed4df`', 'mellin_Phi_eq_zero_of_re_le_one': 'v0.11 = `19b7d1e`'}
NS = {'h2_sign_iff_rh': 'B321', 'ch_iff_rh': 'B321', 'mellin_Phi_eq_zero_of_re_le_one': 'RegisterDepth'}
WHERE = {'h2_sign_iff_rh': 'the zeta page, node 8, line 12', 'ch_iff_rh': 'the zeta page, node 7, line 11',
         'mellin_Phi_eq_zero_of_re_le_one': 'the zeta page, Correspondence row, line 138 (the page`s pin)'}
H2 = '`h2_sign_iff_rh`, %s %s' % (EF, PIN['h2_sign_iff_rh'])
CH = '`ch_iff_rh`, %s %s' % (EF, PIN['ch_iff_rh'])
MP = '`mellin_Phi_eq_zero_of_re_le_one`, %s at the ζ page’s pin %s' % (EF, PIN['mellin_Phi_eq_zero_of_re_le_one'])

REWRITES = [
    (21, 'with the reduction machine-verified;',
     'with the clause compiled as equivalent to RH in its Weil form (%s) and the deposit’s Route 3 clause RH restated (%s);' % (H2, CH)),
    (31, 'equivalently, realization-totality at the ξ interface: the premise that every ξ-zero forces the Euler balance at some prime — Seale 2026c §27.3).',
     'in its Weil form `h2_sign`, equivalent to RH (%s); the conservation register Seale 2026c §27.3 names beside it, that every ξ-zero forces '
     'the Euler balance at some prime, is RH restated (%s)).' % (H2, CH)),
    (31, 'The reduction itself is machine-verified: `ConservationBridge.riemann_hypothesis` compiles at the standard three axioms {propext, '
         'Classical.choice, Quot.sound} (§ Correspondence).',
     'The deposit’s Route 3 terminal `ConservationBridge.riemann_hypothesis` compiles at the standard three axioms {propext, Classical.choice, '
     'Quot.sound} (§ Correspondence), and its premise `ConservationHypothesis` is RH restated (%s, E-2026-09-25-1), so it compiles RH ⇒ RH; the '
     'compiled reduction of RH is the Weil form (%s).' % (CH, H2)),
    (354, 'the SIDE method\'s proof of RH *under the open premise* `h2`',
     'the SIDE method\'s argument for RH *under the open premise* `h2`, in its Weil form `h2_sign` and equivalent to RH (%s),' % H2),
    (354, '(The SIDE proof runs goal ⇐ h1 ∧ h2 with only `h2` open — `h2` is realization-totality at the ξ interface, the premise that every '
          'ξ-zero forces the Euler balance at some prime, one of the five registers of Seale 2026c §27.3.',
     '(The SIDE argument runs goal ⇐ h1 ∧ h2, and lv’s `h2` at Φ is false at every s with re s ≤ 1 (%s), so that goal state closes nothing '
     'on the strip — `h2` read as realization-totality at the ξ interface, the premise that every ξ-zero forces the Euler balance at some '
     'prime, one of the five registers of Seale 2026c §27.3, is RH restated (%s).' % (MP, CH)),
    (427, 'the reduction to the single open premise `h2` is compiled and profiled (§1.1, § Correspondence)',
     'the reduction to the single open premise is compiled in its Weil form (%s), while the Route 3 terminal profiled in § Correspondence '
     'compiles RH ⇒ RH (%s)' % (H2, CH)),
    (499, '| Compiled — the reduction, not a proof of RH; `h2` carried open |',
     '| Compiled, T2 (b557’s tier block): its premise `ConservationHypothesis` is RH restated (%s, E-2026-09-25-1), so it compiles RH ⇒ RH; '
     'the reduction of RH is `h2_sign_iff_rh` (%s %s); `h2` carried open |' % (CH, EF, PIN['h2_sign_iff_rh'])),
    (516, '(1) the machine-verified reduction of RH to the single clause `h2`',
     '(1) the reduction of RH to the single clause `h2`, compiled in its Weil form (%s),' % H2),
]
CEILS = []
STEMS = []
FACTS = []
SIGN_LINE = 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'
CREDITS = [
    (257, 'b450 item: the T3 Tier-1 scope',
     '*Credit (b450, relay `data/b450_batch.json`, INVARIANCE_BARRIERS “the T3 Tier-1 scope”, located at b584 under `(R194)`(5)):* the '
     'technique specification’s `T3` -- consume the Euler product essentially -- scopes Face E’s barrier at Tier-1 verbatim (`%s` :7971, '
     'read at OPEN_TRAILS :6845 by b455), the scope Theorem 3.7’s barrier against T states; the era annotation below (b456) carries the same '
     'line.' % SIGN_LINE),
]
CARRIED = {
    63: 'hypothetical: “the idea that a proof of RH cannot relativize”',
    538: 'a dated history entry (v1.0.2), carried under the history clause',
}
VERSION = (15, 'v1.4, 2026-10-01')
ASSIGN = {'INVAR:21:382': 1, 'INVAR:31:385': 1, 'INVAR:31:386': 1, 'INVAR:354:390': 1, 'INVAR:354:391': 1, 'INVAR:427:393': 1,
          'INVAR:499:397': 1, 'INVAR:516:402': 1, 'INVAR:31:387': 2, 'INVAR:499:398': 2}
READING_NAME = {0: 'none -- resolved by the form', 1: '(a) h2 takes h2_sign', 2: '(c) a T2 terminal says what it states per the tier block'}
CEILING = re.compile(r'RH proved|RH is proved|h2_sign proved|λ_n ≥ 0 proved|GRH proved|GRH reduced|reduction machine-verified|proof of RH|'
                     r'proves RH|RH proves|RH proof|[Pp]roof of GRH|GRH holds|GRH (?:is )?established|'
                     r'becomes? unconditional\b|is unconditional\b|\([Uu]nconditional\)|kernel-verified\)\.|reduction itself is machine-verified|'
                     r'machine-verified reduction|SIDE proof runs')
CEIL_RECORD = 'ceiling correction record:'
CARRY_RECORD = 'ceiling read, carried:'
BM_TAG = '<!-- b584 (R194) THE v1.4 EDITION`S BACK MATTER, 2026-10-01 -->'
BANKROWS = ()


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _rows():
    return [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'INVAR' and r['verdict'] == 'MOVED-IN-MEANING']


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    """### the edition's final line for a current-version line: +2 from :15 (the version line and a blank), +2 more after :257 (the
    ### credit line and a blank)."""
    return n + (2 if n >= VERSION[0] else 0) + (2 if n > 257 else 0)


OFFSET = ('+2 from :15 (the v1.4 version line and a blank, above the v1.3 version line); +2 more after :257 (a blank and the T3 credit '
          'line) -- v1.3 :n sits at the edition`s :n+2 for 15 <= n <= 257, :n+4 after')


def _all_changes():
    return REWRITES + CEILS + STEMS + FACTS


def edition(*a):
    """### PLACE-papers phase1.5/method/INVARIANCE_BARRIERS_v1_4.md, beside the current version from its blob at 9d11874; the re-pin step
    ### run last over the final body."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE 9d11874 -- NOTHING WRITTEN')
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
    if not cur[VERSION[0] - 1].startswith('v1.3, 2026-08-02 (landed') or cur[257] != '' or not cur[256].startswith('**Theorem 3.7'):
        sys.exit('### AN ANCHOR IS NOT WHERE THE FACE SAYS')
    for c in CREDITS:
        if len(_segs(c[2])) != 1:
            sys.exit('### A CREDIT LINE IS NOT ONE SEGMENT')
    diff = []
    for r in _rows():
        ln = r['line']
        k = _segs(cur[ln - 1]).index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d] in nw]
        banks = re.findall(r'relay `data/[^`]+` :\d+', nw)
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         reading=ASSIGN.get(r['id'], 0), cites=cites, banks=banks, supports=r['reading']))
    new[257:257] = ['', CREDITS[0][2]]
    new[VERSION[0] - 1:VERSION[0] - 1] = [VERSION[1], '']
    body = list(new)
    changed = set(x[0] for x in _all_changes())
    if any(_edl(n) > len(body) or (n not in changed and body[_edl(n) - 1] != cur[n - 1]) for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL DOES NOT CARRY THE CURRENT VERSION')
    hits = [(i, m.group(0)) for i, l in enumerate(body, 1) for m in CEILING.finditer(l)]
    inv = {_edl(n): n for n in range(1, len(cur) + 1)}
    stray = sorted(set(inv.get(i, -i) for i, _ in hits) - set(CARRIED))
    if stray:
        sys.exit('### A CEILING HIT IN THE BODY IS NEITHER CORRECTED NOR CARRIED BY THE SEAT`S READ: current lines %s' % stray)
    at = [i for i, l in enumerate(body, 1) if l == CREDITS[0][2]][0]
    bm = ['', BM_TAG, '',
          '## Back matter of the v1.4 edition -- written 2026-10-01 by b584 under the author’s ruling `(R194)`(5), by the form of `(R187)`(5)',
          '',
          '*This file is v1.4 of INVARIANCE_BARRIERS, the CP-7 edition written beside v1.3 (`%s`, unedited) from v1.3’s tier block (its :718, '
          'standing) and its CP-1b work-list (relay `%s`), the ζ page as its spine; it does not deposit and does not replace v1.3, and its '
          'promotion is CP-8’s. Every line cited below is this file’s own.*' % (CUR, WL), '',
          '### Removals', '',
          'None: every one of the 10 work-list rows resolves to a sentence rewritten in place to what its compiled fact says.', '',
          '### Credit lines', '',
          '| inserted at this edition’s line | beside the sentence at | source | Status |', '|:--|:--|:--|:--|',
          '| :%d | :%d (Theorem 3.7, the barrier against T) | %s | inserted under the placement clause, the finding located at OPEN_TRAILS :6845 |'
          % (at, _edl(257), CREDITS[0][1]),
          '| -- | -- | b450 item: Face E / keyhole | not located in FINDINGS or OPEN_TRAILS (relay `data/b584_reads.txt`); no credit inserted |',
          '', '### Stem corrections', '', 'None: the banned-stem scan of v1.3 reads no live use.', '',
          '### Ceiling corrections', '', 'None: no unmarked sentence of v1.3 speaks beyond the ceiling; the marked ones are rewritten above.', '',
          '### Ceiling-shaped sentences read and carried', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(CARRIED):
        bm.append('| :%d | %s %s | carried as read |' % (_edl(ln), CARRY_RECORD, CARRIED[ln]))
    bm += ['', '### Fact corrections', '', 'None: every pin the document prints agrees with its tag, peeled at the remote (relay `data/b584_reads.txt`).', '',
           '### The navigator’s expectations of `(R194)`(5)', '',
           '| expectation | the read | Status |', '|:--|:--|:--|',
           '| (a) h2 takes `h2_sign` | 8 rows | rewritten |',
           '| (b) the two b450 items | the T3 Tier-1 scope located, credited at :%d; Face E / keyhole not located | one credit |' % at,
           '| (c) T2 terminals say what they state | the Route 3 terminal’s 2 rows, per the tier block at this edition’s :%d | rewritten |' % _edl(718),
           '', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v1.4 | `%s` | written at b584 |' % ED,
           '| the current version, v1.3 | `%s` | unedited |' % CUR,
           '| the spine | `%s` at PLACE-papers `%s` | read, unedited |' % (PAGE, MIRROR_PIN),
           '| the work-list | relay `%s` | read |' % WL,
           '| the sentence-by-sentence diff | relay `data/b584_edition_INVARIANCE.txt` | banked at b584 |',
           '', '### Correspondence', '',
           '| declaration or bank line | repository | pin as the page prints it | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    ed_lines = {d: [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l and PIN[d] in l] for d in PIN}
    for d in PIN:
        bm.append('| `SIDEExplicitFormula.%s.%s` | %s | %s | %s | cited at :%s of this edition |' % (
            NS[d], d, EF, PIN[d].replace('`', ''), WHERE[d], ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    bm.append('')
    full = body + bm
    if any('### NONE' in l for l in bm):
        sys.exit('### A CORRESPONDENCE ROW CITES NO LINE OF THE EDITION')
    b = (NL.join(full) + NL).encode('utf-8')
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    put_json('b584_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=len(CREDITS), removals=0, ruled_citations=0, version_lines=1, diff=diff, offset=OFFSET,
                                       ceils=CEILS, stems=STEMS, facts=FACTS, carried={str(k): v for k, v in CARRIED.items()},
                                       credits=[dict(after=c[0], id=c[1], text=c[2], at=at) for c in CREDITS],
                                       version=dict(above=VERSION[0], text=VERSION[1]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))


def edition_bank():
    """### The diff with its offset line, the credit, the counts, the ceiling read, H28a-H28c."""
    E = jl('b584_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(BM_TAG)
    scan = rd('b584_edition_termscan.txt')
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
    found = _search()
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % OFFSET, '',
         'b584 -- COMPONENT 3: THE EDITION OF INVARIANCE_BARRIERS, (R194)(5), BY THE FORM OF (R187)(5) AND ITS CLAUSES', '',
         '### THE TWO b450 FINDINGS, SEARCHED BY NAME IN FINDINGS.md AND OPEN_TRAILS.md (relay data/b584_reads.txt):']
    L += ['    %-22s %-15s "%s" : %d hit(s) %s' % (s['finding'], s['ledger'], s['needle'], len(s['hits']), s['hits']) for s in found]
    L += ['    ### the T3 Tier-1 scope : LOCATED at OPEN_TRAILS :6845 (b455, quoting the archive line :7971) -- credited',
          '    ### Face E / keyhole : NOT LOCATED -- recorded, no credit', '',
          '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :15 "%s"' % (
              CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0], cur0[14][:60]),
          '### its tier block : :718 "%s"' % cur0[717][:110],
          '### its version history : :526-:542 (v1.3 back to v1.0.1); the era annotation :697 (b456); the currency repair (b484)',
          '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
          '### THE WORK-LIST, ROW BY ROW (10 rows, 8 sentences, 6 lines) -- each row: v1.3`s line and the edition`s, the terminal, the '
          'expectation it falls under (the seat`s hand-read), what its sentence cites, the sentence before and after.', '']
    for d in E['diff']:
        L += ['  %s v1.3 :%d -> v1.4 :%d `%s` -- %s ; cites %s%s' % (d['id'], d['line'], d['ed_line'], d['terminal'], READING_NAME[d['reading']],
                                                                 ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']],
                                                                 (' ; bank ' + ', '.join(d['banks'])) if d['banks'] else ''),
              '      work-list: %s' % d['supports'],
              '      v1.3 : %s' % d['old'], '      v1.4 : %s' % d['new'], '']
    cov = [d for d in E['diff'] if d['reading']]
    L += ['### (N4) COVERAGE BY THE EXPECTATIONS OF (R194)(5), the seat`s hand-read: %d of %d rows -- (a) %d, (c) %d ; uncovered %s'
          % (len(cov), len(E['diff']), sum(d['reading'] == 1 for d in E['diff']), sum(d['reading'] == 2 for d in E['diff']),
             [':%d `%s`' % (d['line'], d['terminal']) for d in E['diff'] if not d['reading']]), '',
          '### THE CREDIT LINE:'] + ['    v1.4 :%d (after v1.3 :%d) %s : %s' % (c['at'], c['after'], c['id'], c['text']) for c in E['credits']]
    L += ['### THE CEILING-SHAPED SENTENCES READ AND CARRIED (%d lines):' % len(CARRIED)]
    L += ['    v1.3 :%d -> v1.4 :%d  %s' % (n, _edl(n), CARRIED[n]) for n in sorted(CARRIED)]
    L += ['### STEM, CEILING AND FACT CORRECTIONS: none.',
          '### THE VERSION LINE: above v1.3 :%d: %s' % (E['version']['above'], E['version']['text']),
          '### REMOVALS: none. ### HISTORY LINES: none.', '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d: the credit '
          'line and the version line) ; the back matter %d ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d + one version line = %d' % (
              body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], {'record': 'quoted in a back-matter record, read by the seat',
                                                                 'carried': 'in a sentence the seat read and carried',
                                                                 'beyond': '### BEYOND THE CEILING'}[h['kind']], h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### the banned-stem scan of the edition (relay data/b584_edition_termscan.txt): live uses %s ; verdict %s' % (
              live.group(1) if live else '?', 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on the page at its pin, or a bank line%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- live banned stems %s, sentences beyond the ceiling %d.**' % (h28c, live.group(1) if live else '?', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b584_edition_INVARIANCE.txt', L)
    put_json('b584_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None, beyond=len(beyond), hits=hits,
                                   covered=len(cov), uncovered=[d['id'] for d in E['diff'] if not d['reading']], held=None,
                                   located=['the T3 Tier-1 scope'], not_located=['Face E / keyhole'], search=found))
    H = jl('b584_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'covered', H['covered'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'], 'live', H['live'])


# ================================================================================ THE SCORING AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}


def scores():
    H, E, C = jl('b584_h28.json'), jl('b584_edition.json'), jl('b584_ceiling_census.json')
    ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'ls-files', '--others', '--exclude-standard', 'phase1.5', 'phase2')).split(NL) if x.strip()))
    kmain = g('D:/SIDE-explicit-formula', 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    cur_same = g(PP, 'hash-object', CUR).strip() == E['cur_blob']
    n3 = H['H28a'] == 'HELD' and H['H28b'] == 'HELD' and H['H28c'] == 'HELD' and H['held'] is None
    allowed_pp = {'FINDINGS.md', 'OPEN_TRAILS.md', ED}
    rows = {r['name']: r for r in C['rows']}
    top3 = C['top3']
    top_ok = 'A_Place_to_Stand' in top3 and sum(1 for n in top3 if rows[n]['spectral']) == 2
    S = dict(
        N1=('HELD' if top_ok and C['rem8_live'] < 60 else 'REFUTED', 'the three largest live counts: %s ; the fourteen`s remaining editions '
            'total %d live (the seven after this act %d)' % (['%s %d' % (n, rows[n]['whole']['live']) for n in top3], C['rem8_live'], C['rem7_live'])),
        N2=('HELD' if H['located'] else 'REFUTED', 'located: %s ; not located: %s' % (H['located'], H['not_located'])),
        N3=('HELD' if n3 else 'REFUTED', 'H28a %s, H28b %s (the body %+d against at most %d), H28c %s; no sentence held' % (
            H['H28a'], H['H28b'], H['body_dn'], H['allowed'], H['H28c'])),
        N4=('HELD' if H['covered'] >= 5 else 'REFUTED', 'the expectations of (R194)(5) cover %d of the 10 MOVED rows; uncovered %s' % (
            H['covered'], H['uncovered'])),
        N5=('HELD' if (kmain == V015 and heads_ok and cur_same and set(ch) <= allowed_pp) else 'REFUTED', 'nothing deposits; no kernel '
            'touched (%s); the current INVARIANCE_BARRIERS unedited (%s); PLACE-papers changed at %s; the census a relay bank' % (
                'held' if kmain == V015 and heads_ok else '### MOVED', 'held' if cur_same else '### EDITED', ch)),
        S1=('HELD' if C['rem8_live'] < 60 else 'REFUTED', 'the remaining editions` live total is under 60 (%d)' % C['rem8_live']),
        S2=('HELD' if H['located'] == ['the T3 Tier-1 scope'] and H['not_located'] == ['Face E / keyhole'] else 'REFUTED',
            'the T3 scope located, Face E / keyhole not'),
        S3=('HELD' if n3 and H['body_dn'] == 2 and H['allowed'] == 2 else 'REFUTED', 'H28a-H28c held; the body +2 against 2'),
        S4=('HELD' if H['covered'] == 10 else 'REFUTED', '(N4) holds at 10 of 10'),
        S5=('HELD' if set(ch) == allowed_pp else 'REFUTED', '(N5) holds: the files changed are the three its list names'),
        counts=dict(pp_changed=ch, body_dn=H['body_dn'], covered=H['covered'], top3=top3, rem8_live=C['rem8_live']),
    )
    put_json('b584_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], S[k][1][:160]))


TITLE_HEAD = ('## CP-7, act nine: the edition of INVARIANCE_BARRIERS from its tier block and work-list, the T3 Tier-1 scope located and '
              'credited, Face E / keyhole not located; the ceiling census over the roster')
TITLE = TITLE_HEAD + '; written as v1.4 beside v1.3, no sentence held'
TRAIL_HEAD = ('### b584 — lane three, act twelve under (R194): CP-7 act nine -- the edition of INVARIANCE_BARRIERS written beside the current; '
              'the ceiling census; W-ORD-SIMPLICITY-FACE and W-ORD-PNT-CHI entered')


def records_pp():
    Q = _Q()
    S, H, E, C1, C = jl('b584_scores.json'), jl('b584_h28.json'), jl('b584_edition.json'), jl('b584_c1_lines.json'), jl('b584_ceiling_census.json')
    ln = C1['lines']
    rows = {r['name']: r for r in C['rows']}
    Q.guard_absent(Q.FIND, TITLE_HEAD)
    e = ['', TITLE, '',
         '*Filed at b584 on the author’s ruling `(R194)`. Banks: relay `data/b584_edition_INVARIANCE.txt` (the sentence-by-sentence diff, its '
         'offset line at its head), `data/b584_edition.json`, `data/b584_ceiling_census.txt`, `data/b584_reads.txt`. Nothing deposits.*', '',
         '**The edition** (`(R194)`(5)): `%s`, v1.4, written beside v1.3 (`%s`, unedited) from v1.3’s tier block and its CP-1b work-list, the '
         'ζ page as its spine. The 10 work-list rows resolve to 8 sentences on 6 lines, each rewritten in place: the clause named in its Weil '
         'form and cited to its equivalence with RH; the conservation register and the deposit’s Route 3 terminal said to be RH restated, so '
         'that terminal compiles RH ⇒ RH, its row graded as the tier block reads it; lv’s goal state said to close nothing on the strip. Of the '
         'two b450 items, the T3 Tier-1 scope is located at OPEN_TRAILS :6845 and credited beside Theorem 3.7; Face E / keyhole is not located '
         'in either ledger and no credit is inserted. No stem, ceiling or fact correction; no sentence removed and none held.' % (ED, CUR), '',
         '**The counts.** v1.3 %d sentences; v1.4 %d (the body %d, the back matter %d); the body differs by %+d against the final bound, %d.'
         % (E['n_cur'], E['n_full'], E['n_body'], E['n_backmatter'], H['body_dn'], H['allowed']), '',
         '**H28a %s · H28b %s · H28c %s.** Coverage of the 10 rows by the navigator’s expectations: %d.' % (H['H28a'], H['H28b'], H['H28c'], H['covered']), '',
         '**The ceiling census** (`(R194)`(2), relay `data/b584_ceiling_census.txt`, a bank and no edit): the three largest live counts are %s; '
         'the fourteen’s remaining editions total %d live uses; the roster %d. A count, not a verdict: each live use is read at its edition.'
         % (', '.join('%s %d' % (n, rows[n]['whole']['live']) for n in C['top3']), C['rem8_live'], C['total_live']), '',
         '**The record lines and the work-orders** (`(R194)`(1), (3)-(4)): b583’s weight (FINDINGS :%d); `W-ORD-SIMPLICITY-FACE` (OPEN_TRAILS '
         ':%d) and `W-ORD-PNT-CHI` (:%d), each priced and not started, trigger the author’s word; SIMPLICITY’s edition held behind its '
         'work-order (:%d).' % (ln['weight'], ln['simplicity_face'], ln['pnt_chi'], ln['held']), '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R194)`(6): the edition of INDEX_ARITY_AT_THE_CRITICAL_LINE by the same form; the author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; v1.3, README, REGISTRY, ERRATA and both pages unwritten; nothing here is a statement about RH, '
         'GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R194) ratified.** (1) b583 at its weight, the three pin corrections accepted. (2) The ceiling census over the roster, a bank. '
             '(3) `W-ORD-SIMPLICITY-FACE` entered; SIMPLICITY held behind it. (4) `W-ORD-PNT-CHI` entered. (5) The edition of INVARIANCE_BARRIERS '
             'by the form. (6) The act after.', '',
             '**Entered:** FINDINGS.md:%d (b583’s weight), :%d (the entry); OPEN_TRAILS.md:%d (`W-ORD-SIMPLICITY-FACE`), :%d (`W-ORD-PNT-CHI`), '
             ':%d (SIMPLICITY held), this record; PLACE-papers `%s` (created); relay `data/b584_ceiling_census.txt`.' % (
                 ln['weight'], Q.line_of(Q.FIND, TITLE_HEAD), ln['simplicity_face'], ln['pnt_chi'], ln['held'], ED), '',
             '**No question asked before the seal.** The two b450 items were searched by name before any build: the T3 Tier-1 scope located at '
             'OPEN_TRAILS :6845 (b455 quoting the archive line), credited beside Theorem 3.7; Face E / keyhole not located, recorded.', '',
             '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
             % tuple(S[k][0] for k in SCORE_KEYS), '',
             '**Next:** per `(R194)`(6), CP-7 act ten, b585 -- the edition of INDEX_ARITY_AT_THE_CRITICAL_LINE by the same form, H28a-H28c '
             'scored; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
             'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b584_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE_HEAD), title=TITLE, append=r))
    put_json('b584_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r2))
    print(jl('b584_findings.json')['entry_line'], jl('b584_trail.json')['line'])


def desk():
    S = jl('b584_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b584 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b584_defects.txt').rstrip(NL).split(NL)
    put_txt('b584_desk_notes.txt', L)


def components():
    S, H, C1, fj, tj, C = (jl('b584_scores.json'), jl('b584_h28.json'), jl('b584_c1_lines.json'), jl('b584_findings.json'),
                           jl('b584_trail.json'), jl('b584_ceiling_census.json'))
    ln = C1['lines']
    L = ['b584 -- THE COMPONENTS, BANKED UNDER (R194).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b583`s closing push-out relay 2129f47d ; push-b583* branches deleted by '
         'name (data/b584_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : b583`s weight FINDINGS :%d ; W-ORD-SIMPLICITY-FACE OPEN_TRAILS :%d ; W-ORD-PNT-CHI :%d ; SIMPLICITY held :%d' % (
             ln['weight'], ln['simplicity_face'], ln['pnt_chi'], ln['held']),
         '### COMPONENT 2 : data/b584_ceiling_census.txt ; top three %s ; remaining editions %d live ; N1 %s' % (C['top3'], C['rem8_live'], S['N1'][0]),
         '### COMPONENT 3 : the edition %s ; 8 sentences rewritten, 1 credit line, the version line, 0 removals, 0 corrections ; '
         'data/b584_edition_INVARIANCE.txt ; H28a %s H28b %s H28c %s ; N2 %s N3 %s N4 %s' % (
             ED, H['H28a'], H['H28b'], H['H28c'], S['N2'][0], S['N3'][0], S['N4'][0]),
         '### COMPONENT 4 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; next: the edition of INDEX_ARITY_AT_THE_CRITICAL_LINE ; N5 %s'
         % (fj['entry_line'], tj['line'], S['N5'][0])]
    put_txt('b584_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b584_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
