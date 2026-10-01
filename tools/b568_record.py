# -*- coding: utf-8 -*-
"""b568_record.py -- THE ACT'S RECORD TOOL, UNDER (R178). ### ONE SUBCOMMAND PER BANK.

### ### b568: LANE THREE, ACT ONE -- CP-4, THE PAGE WITHOUT NARRATIVE. ### Subcommands, each writing only `data/b568_*`
### unless its docstring names a ledger: zetabounds, dichotomy, addendum, reads, weight, findings, trail, rows, scores,
### desk, components. ### Every bank is written through `put_txt` / `put_json` (encode first, then a temp file, then
### `os.replace`), so a failed encode leaves no zero-byte husk (b328's trap).
"""
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
EF = 'D:/SIDE-explicit-formula'
PP = 'D:/MY-DOwnloads/PLACE-papers'
SIDE = 'D:/SIDE-global-section'
V010 = '6baed63ae664a22db1f325177b81253e270de6e3'

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


# ### ### **(R178)(2)(i): THE 146 NAMES BY CLASS.** ### The set is b567's own (data/b567_zb_consumers.json `not_consumed`,
# ### 150 names less the 4 a later Zeta23 module consumes). The class is read from the declaration's LINE in
# ### Zeta23/FromPNTPlus/ZetaBounds.lean at v0.10 against the file's own blocks, the boundaries printed with the
# ### declaration that opens each: the strip bounds open at :1220 (b567's face, READING (5)) and run through the upper
# ### bounds for ζ and ζ′ (ZetaDerivUpperBnd :1827); the zero-free region's block opens at the near-1 and lower
# ### bounds it is built from (Tendsto_nhdsWithin_punctured_map_add :1851) and runs through ZetaZeroFree (:2485) and
# ### its consequences to the file's end. The names before :1220 are neither class: the continuation and residue
# ### block (the Abel representation, the residue at 1, holomorphy, HasDerivAtZeta0 and DerivZeta0EqDerivZeta).
ZB = 'Zeta23/FromPNTPlus/ZetaBounds.lean'
BLOCKS = [(1, 1219, 'CONTINUATION'), (1220, 1850, 'STRIP BOUNDS'), (1851, 10 ** 6, 'ZERO-FREE REGION')]
PAIR = ('HasDerivAtZeta0', 'DerivZeta0EqDerivZeta')


def zetabounds():
    src = g(EF, 'show', '%s:%s' % (V010, ZB))
    zj = jl('b567_zb_consumers.json')
    names = zj['not_consumed']
    lines = src.split(NL)
    where = {}
    for n in names:
        pat = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+)?(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev|irreducible_def)\s+'
                         + r'(?:[A-Z][\w]*\.)*' + re.escape(n) + r'(?![\w\'₀-₉])')
        hits = [i + 1 for i, l in enumerate(lines) if pat.match(l)]
        where[n] = hits
    unplaced = [n for n, h in where.items() if len(h) != 1]
    # ### THE MATCHER'S LINEAGE (b568): v1 matched the bare name and left 10 unplaced -- b567's list stores a namespaced
    # ### declaration (`Finset.Icc0_eq`, `Complex.cpow_tendsto`) by its last component; v2 allows a dotted capitalised prefix.
    v1 = sum(1 for n in names if len([l for l in lines if re.match(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+)?(?:noncomputable\s+)?'
             r'(?:theorem|lemma|def|abbrev|irreducible_def)\s+' + re.escape(n) + r'(?![\w\'₀-₉])', l)]) == 1)
    cls = {}
    for n, h in where.items():
        if len(h) == 1:
            cls[n] = [c for lo, hi, c in BLOCKS if lo <= h[0] <= hi][0]
    by = {c: sorted((n for n in cls if cls[n] == c), key=lambda x: where[x][0]) for _, _, c in BLOCKS}
    opener = {c: (by[c][0], where[by[c][0]][0]) if by[c] else None for c in by}
    L = ['b568 -- (R178)(2)(i): THE 146 ZETABOUNDS NAMES NOT CONSUMED BY A LATER ZETA23 MODULE, BY CLASS', '',
         '### the set : relay data/b567_zb_consumers.json `not_consumed` (%d names; b567 counted %d declarations and %d consumed)'
         % (len(names), zj['total'], len(zj['consumed'])),
         '### the file : %s at SIDE-explicit-formula v0.10 = %s (%d lines)' % (ZB, V010[:7], len(lines)),
         '### THE RULE (declared on the face, READING (3)(c)): the class is read from the declaration`s line against the file`s blocks --',
         '###   [:1, :1219] CONTINUATION (the Abel representation, the residue at 1, holomorphy) -- neither of the ruling`s two classes;',
         '###   [:1220, :1850] STRIP BOUNDS (upper bounds for ζ and ζ′ on 1 − A/log|t| ≤ σ ≤ 2, through ZetaDerivUpperBnd :1827);',
         '###   [:1851, end] ZERO-FREE REGION (the near-1 and lower bounds it is built from, ZetaZeroFree :2485, its consequences).',
         '### THE MATCHER`S LINEAGE: v1 (the bare name) placed %d of %d ; v2 (a dotted capitalised prefix allowed) placed %d of %d ;'
         ' unplaced by v2 %d %s' % (v1, len(names), len(cls), len(names), len(unplaced), unplaced),
         '### the HasDerivAt pair, inside the 146 and ATTEMPTED at b567 (analogues present at v0.10): %s' % ', '.join(
             '%s :%s %s' % (p, where.get(p, ['?'])[0], cls.get(p, '?')) for p in PAIR), '']
    for c in by:
        L.append('### %s : %d%s' % (c, len(by[c]), ('   (opens at %s :%d)' % opener[c]) if opener[c] else ''))
        for n in by[c]:
            L.append('    :%-5d %s%s' % (where[n][0], n, '   [ATTEMPTED at b567: analogue present]' if n in PAIR else ''))
        L.append('')
    unatt = {c: [n for n in by[c] if n not in PAIR] for c in by}
    L.append('### ### **BY CLASS : CONTINUATION %d ; STRIP BOUNDS %d ; ZERO-FREE REGION %d ; TOTAL %d.**'
             % (len(by['CONTINUATION']), len(by['STRIP BOUNDS']), len(by['ZERO-FREE REGION']), len(cls)))
    L.append('### ### **UNATTEMPTED (the pair excluded) : CONTINUATION %d ; STRIP BOUNDS %d ; ZERO-FREE REGION %d ; TOTAL %d.**'
             % (len(unatt['CONTINUATION']), len(unatt['STRIP BOUNDS']), len(unatt['ZERO-FREE REGION']),
                sum(len(v) for v in unatt.values())))
    L.append('### The ruling names two classes; the file`s first block is a third, and its names are printed under it, not folded into')
    L.append('### either. Two of the 146 (the HasDerivAt pair) were attempted at b567, so the unattempted set is 144, not 146.')
    put_txt('b568_zetabounds_names.txt', L)
    put_json('b568_zetabounds_names.json', dict(where={n: h for n, h in where.items()}, cls=cls, by=by, unattempted=unatt,
                                                 pair=list(PAIR), unplaced=unplaced, blocks=BLOCKS))


RELAY = ROOT.replace('\\', '/')
MATHLIB_DIR = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
READS = [
    # (label, repo, rev, path, [lines])
    ('kernel H2Sign', EF, V010, 'SIDEExplicitFormula/H2Sign.lean', [24, 29]),
    ('kernel Seam', EF, V010, 'SIDEExplicitFormula/Seam.lean', [101]),
    ('kernel H2Bridge', EF, V010, 'SIDEExplicitFormula/H2Bridge.lean', [33, 71]),
    ('kernel RegisterDepth', EF, V010, 'SIDEExplicitFormula/RegisterDepth.lean', [22]),
    ('kernel DetectionRegion', EF, V010, 'SIDEExplicitFormula/DetectionRegion.lean', [29, 47, 52]),
    ('kernel LiWeil', EF, V010, 'SIDEExplicitFormula/LiWeil.lean', [60, 243, 267, 359, 372]),
    ('kernel LiWeilSym', EF, V010, 'SIDEExplicitFormula/LiWeilSym.lean', [51, 1218]),
    ('kernel LiCriterionBridge', EF, V010, 'SIDEExplicitFormula/LiCriterionBridge.lean', [149, 179, 191]),
    ('kernel ResidueDischarge', EF, V010, 'SIDEExplicitFormula/ResidueDischarge.lean', [30, 34, 41]),
    ('kernel Chi/Statement (the E0 rule`s instance)', EF, V010, 'SIDEExplicitFormula/Chi/Statement.lean', [51, 59]),
    ('vendored Bulka ReverseDirection', EF, V010, 'Vendored/Bulka/Lc/LiCriterion/ReverseDirection.lean', [413]),
    ('vendored Bulka Basic', EF, V010, 'Vendored/Bulka/Lc/LiCriterion/Basic.lean', [541]),
    ('vendored Zeta23 Defs', EF, V010, 'Zeta23/Defs.lean', [136]),
    ('vendored Zeta23 ExplicitFormula', EF, V010, 'Zeta23/ExplicitFormula.lean', [86, 97]),
    ('vendored Zeta23 SeamClosed', EF, V010, 'Zeta23/Statement/SeamClosed.lean', [42]),
    ('vendored Zeta23 WeilEF/Main', EF, V010, 'Zeta23/WeilEF/Main.lean', [286]),
    ('kernel lean-toolchain', EF, V010, 'lean-toolchain', [1]),
    ('kernel lake-manifest (mathlib rev)', EF, V010, 'lake-manifest.json', [10, 11]),
    ('Mathlib RiemannZeta', MATHLIB_DIR, 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11',
     'Mathlib/NumberTheory/LSeries/RiemannZeta.lean', [121, 185]),
    ('Mathlib DirichletCharacter/Basic (the dichotomy)', MATHLIB_DIR, 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11',
     'Mathlib/NumberTheory/DirichletCharacter/Basic.lean', [533, 536, 538, 542]),
    ('PLACE-papers README (the ceiling sentence)', PP, 'HEAD', 'README.md', [121]),
    ('PLACE-papers REGISTRY (the ceiling sentence)', PP, 'HEAD', 'REGISTRY.md', [956]),
    ('PLACE-papers OPEN_TRAILS (W-ORD-GRH-WEIL; its lines; the critical path; lane three)', PP, 'HEAD', 'OPEN_TRAILS.md',
     [11373, 11407, 11417, 11565, 11613]),
    ('PLACE-papers FINDINGS (the tier law)', PP, 'HEAD', 'FINDINGS.md', [4819, 5812]),
    ('PLACE-papers FACES_LEDGER (ch_iff_rh`s row)', PP, 'HEAD', 'FACES_LEDGER.md', [497]),
    ('PLACE-papers THE_RESIDUE_OF_RH (residue_irreducible`s rows)', PP, 'HEAD', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md', [108, 228]),
    ('relay b539 ferry (the tiers)', RELAY, 'HEAD', 'data/b539_ferry.txt', list(range(20, 32))),
    ('relay banned_terms.py (the stems)', RELAY, 'HEAD', 'tools/banned_terms.py', [64]),
    ('relay b567_record.py (the E0 rule as b567 printed it)', RELAY, 'HEAD', 'tools/b567_record.py', [433, 434, 435, 436, 437]),
    ('relay terminal_table.py (its columns: a grade column, no tier column)', RELAY, 'HEAD', 'tools/terminal_table.py', [880]),
]


def reads():
    """### READING (1): every cited line printed from its blob at its pin. Read at the act's start; the pins are b567's
    ### post-push state (kernel 6baed63, PLACE-papers 5340891, relay d77bb7aa's tree for the tools read)."""
    L = ['b568 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, lines in READS:
        src = g(repo, 'show', '%s:%s' % (rev, path))
        rv = g(repo, 'rev-parse', '--short=8', rev).strip()
        L.append('### %s -- %s @ %s' % (label, path, rv))
        sl = src.split(NL)
        for n in lines:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:400]))
    L.append('')
    L.append('### the terminal table`s columns, read from relay data/terminal_table.md :6 (the generator writes a grade column; no tier column):')
    L.append('    ' + g(ROOT, 'show', 'HEAD:data/terminal_table.md').split(NL)[5])
    L.append('### push_gated.sh read WHOLE before its edit (relay 9de84b16, 75 lines); the suites` arms read at b566_checks.py :520-:527 and the')
    L.append('### face-reading code :83-:150 (HEAD 2625d82d carries the as-of edit; the reads were of the pre-edit text, d77bb7aa).')
    put_txt('b568_reads.txt', L)


STD3 = ['propext', 'Classical.choice', 'Quot.sound']
# ### THE OPEN-LOOKING PROPS ON THE CHAIN, each with the node whose statement joins it to RiemannHypothesis (and so, through
# ### h2_sign_iff_rh, to h2_sign). The connective is READ from that node's printed statement, not typed: ' ↔ ' at the top of
# ### the statement is a compiled equivalence; a top-level ' → ' only is an implication.
OPEN_PROPS = [
    ('RiemannHypothesis', 'SIDEExplicitFormula.B321.h2_sign_iff_rh'),
    ('∀ L₀, h2_sign_upto L₀', 'SIDEExplicitFormula.B321.h2_sign_iff_forall_upto'),
    ('conservationHypothesis (ch_iff_rh`s left side)', 'SIDEExplicitFormula.B321.ch_iff_rh'),
    ('∀ n, 0 ≤ LiCoeff n (Li positivity)', 'SIDEExplicitFormula.LiCriterionBridge.li_nonneg_iff_rh'),
    ('∀ n L, Tendsto ... → 0 ≤ L.re (arithmetic-limit positivity)', 'SIDEExplicitFormula.LiCriterionBridge.arith_limit_nonneg_iff_rh'),
    ('Register4_positivity LiCoeff', 'SIDEExplicitFormula.ResidueDischarge.register4_positivity_liCoeff_imp_rh'),
    ('∀ n, 0 ≤ (taylorCoeff riemannXi n).re (Bulka`s positivity)', 'LiCriterion.positivity_implies_RH'),
]


def connective(stmt):
    """### the top-level connective of a theorem's printed type: the text after ' : ' of the header, its first ' ↔ ' or
    ### ' → ' at bracket depth 0."""
    t = stmt.split(' : ', 1)[1] if ' : ' in stmt else stmt
    d = 0
    for i, ch in enumerate(t):
        if ch in '([{':
            d += 1
        elif ch in ')]}':
            d -= 1
        elif d == 0 and t[i:i + 3] in (' ↔ ', ' → '):
            if t[i:i + 3] == ' → ' and t[:i].lstrip().startswith('∀'):
                continue
            return t[i + 1]
    return None


def nodes():
    """### COMPONENT 3: the node cells (from the generator's run, data/b568_node_cells.json), the additions and drops with their
    ### reasons and checks, H20a and H20b scored."""
    m = jl('b568_node_cells.json')
    cells, order = m['cells'], m['order']
    nl = [x['name'] for x in m['nodes']]
    L = ['b568 -- COMPONENT 3: THE NODE LIST, ITS CELLS, THE ADDITIONS AND DROPS, H20a AND H20b',
         '### input relay data/b568_nodes.txt (%d nodes) ; cells from relay tools/chain_page.py`s probe at v0.10 = 6baed63 '
         '(data/b568_probe_out.txt, data/b568_node_cells.json)' % len(nl), '']
    for i, n in enumerate(order, 1):
        c = cells[n]
        L.append('### %d. %s' % (i, n))
        L.append('    module:line   %s:%d (module %s)' % (c['path'], c['line'], c['module']))
        L.append('    entry         %s ; the source header at the entry tag equal to v0.10`s: %s' % (c['entry'], c.get('header_at_entry_equal', 'n/a (Mathlib)')))
        L.append('    statement     %s' % c['statement'])
        L.append('    kind          %s ; E0 %s ; premises %s ; record grade %s' % (c['kind'], c['grade'], c['premises'], c.get('record_grade')))
        L.append('    tier          %s (%s)' % (c['tier'], c['tier_source']))
        L.append('    axioms        %s ; the standard three %s' % (c['axioms'], c['std3']))
        L.append('    consumes      %s' % ', '.join(c['consumes']) or 'none')
    L.append('')
    roles = {x['name']: x['role'] for x in m['nodes']}
    adds = [(n, r) for n, r in roles.items() if r.startswith('added')]
    L.append('### ### **THE ADDITIONS : %d**' % len(adds))
    for n, r in adds:
        users = [u for u in order if n in cells[u]['consumes']]
        L.append('    %s -- %s ; consumed by %s' % (n, r, ', '.join(short(u) for u in users) or 'none'))
    L.append('### ### **THE DROPS : %d**' % len(m['drops']))
    for d in m['drops']:
        L.append('    %s -- %s ; declarations of that name at the pin: %d %s ; constants under it reached by any node: %s'
                 % (d['name'], d['why'], len(d['declarations_at_pin']), d['declarations_at_pin'][:2], d['watched_by_nodes'] or 'none'))
    consumers = {n: [u for u in order if n in cells[u]['consumes']] for n in order}
    L.append('### nodes no other node consumes (the chain`s tops): %s' % [short(n) for n in order if not consumers[n]])
    L.append('')
    thm = [n for n in order if cells[n]['kind'] == 'theorem']
    bad_a = [n for n in order if not cells[n]['std3']] + [n for n in thm if cells[n]['grade'] != 'DERIVES']
    rec_other = [(short(n), cells[n].get('record_grade')) for n in thm if cells[n].get('record_grade') not in (None, 'DERIVES', 'UNGRADED')]
    h20a = not bad_a
    L.append('### H20a -- every node prints the standard three with no sorry, every theorem node grades DERIVES (E0):')
    L.append('    nodes %d (theorems %d, definitions %d) ; beyond the three or not DERIVES: %s' % (len(order), len(thm), len(order) - len(thm), bad_a or 'NONE'))
    L.append('    the vendored converse: %s E0 %s, %s' % ('positivity_implies_RH', cells['LiCriterion.positivity_implies_RH']['grade'],
                                                       cells['LiCriterion.positivity_implies_RH']['axioms']))
    L.append('    a record grade other than DERIVES on a theorem node (carried, not the E0 grade): %s' % (rec_other or 'NONE'))
    L.append('### ### **H20a : %s**' % ('HELD' if h20a else 'REFUTED'))
    L.append('')
    L.append('### H20b -- exactly one open statement, h2_sign, every other open-looking Prop on the chain compiled equivalent to it:')
    rows, bad_b = [], []
    for p, j in OPEN_PROPS:
        k = connective(cells[j]['statement'])
        rows.append((p, short(j), k))
        if k != '↔':
            bad_b.append(p)
        L.append('    %-62s joined by %-40s top-level connective %s' % (p, short(j), k))
    L.append('    RiemannHypothesis is joined to h2_sign by h2_sign_iff_rh (↔); every ↔ above composes with it.')
    L.append('    open-looking Props joined by an implication only: %s' % (bad_b or 'NONE'))
    h20b = not bad_b
    L.append('### ### **H20b : %s**%s' % ('HELD' if h20b else 'REFUTED',
             '' if h20b else ' -- in its letter, at %d places: %s -- each joined to RiemannHypothesis by a compiled implication only. '
                             'No declaration at v0.10 states either converse; the pieces each converse would compose are compiled '
                             '(rh_imp_li_nonneg, liCoeff_zero, li_coeff_eq_taylorCoeff) but not composed.' % (len(bad_b), '; '.join(bad_b))))
    put_txt('b568_node_cells.txt', L)
    put_json('b568_h20ab.json', dict(h20a=h20a, h20b=h20b, bad_a=bad_a, bad_b=bad_b, rows=rows, n=len(order), adds=adds,
                                     drops=[d['name'] for d in m['drops']], rec_other=rec_other,
                                     tops=[short(n) for n in order if not consumers[n]],
                                     ch_consumers=consumers.get('SIDEExplicitFormula.B321.ch_iff_rh')))


def short(n):
    return n.split('.')[-1]


import b560_record as Q   # noqa: E402   ### the shared ledger helpers (append with the stem and backtick guards)
FIND, OT, CORR = Q.FIND, Q.OT, Q.CORR
PAGE = os.path.join(PP, 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')
C_TAG, C_ASOF, C_E0, C_GEN, C_ARM = 'f35256d8', '2625d82d', '09f7f60e', '3b3152f4', '65916c16'


def _count(path, needle):
    t = rd8(path)
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) (\[[^\]]*\])?', t)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4) or '[]') if m else None


def rd8(name):
    p = name if os.path.isabs(name) else os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def scores():
    """### every hypothesis and expectation, each on its bank."""
    h = jl('b568_h20ab.json')
    runs, live, pg = rd8('b568_page_runs.txt'), rd8('b568_g_chain_page_live.txt'), rd8('b568_page_checks.txt')
    term = rd8('b568_page_termscan.txt')
    r6a, r7a = _count('b568_b566_rerun_after.txt', ''), _count('b568_b567_rerun_after.txt', '')
    r6b = _count('b568_b566_rerun_before.txt', '')
    asof = rd8('b568_test_asof.txt')
    tpg = rd8('b568_test_push_gated.txt')
    h20c = 'cmp run1 run2 : BYTE-IDENTICAL' in runs and 'G-CHAIN-PAGE (against the page as written' in live and ': PASS --' in live
    h20d = (re.search(r'^\s*VERDICT\s+: CLEAN', term, re.M) is not None and 'hits found       : 0' in term
            and 'BYTE-IDENTICAL TO README :121 : True' in pg and 'NONE OF title, head, node line, open node, last derived line : 0**' in pg)
    n_nodes = h['n']
    k = g(EF, 'status', '--porcelain', '--untracked-files=no').strip()
    kmain = g(EF, 'rev-parse', 'main').strip()
    S = dict(
        H20a=('HELD' if h['h20a'] else 'REFUTED', 'every node prints the standard three, every theorem node grades DERIVES (E0); '
              'ch_iff_rh`s record grade ENCODES-CONCLUSION is carried beside it (data/b568_node_cells.txt)'),
        H20b=('HELD' if h['h20b'] else 'REFUTED', 'joined by an implication only: %s (data/b568_node_cells.txt)' % h['bad_b']),
        H20c=('HELD' if h20c else 'REFUTED', 'two runs byte-identical (sha256 882190fe...), G-CHAIN-PAGE live PASS (data/b568_page_runs.txt, '
              'data/b568_g_chain_page_live.txt)'),
        H20d=('HELD' if h20d else 'REFUTED', '0 banned-stem hits (data/b568_page_termscan.txt); the last line byte-identical to README :121; '
              'no line outside the page`s parts; the seat`s read finds no sentence of interpretation (data/b568_page_checks.txt)'),
        N1=('HELD' if (r6a and r6a[1] == 74 and '10 of 10 cases as wanted -- PASS' in asof) else 'REFUTED',
            'b566 under the as-of commit reads %s of %s, failing %s -- arms that read PLACE-papers at HEAD (G-CEILING-APPENDED, '
            'G-CORPUS-SCOPE), the kernel`s live refs (G-TAG-READ-BACK) and the clone b567 deleted (G-BULKA-KEPT), outside the relay '
            'tree the ruling names; before the change %s of %s; the two-sided test 10 of 10' % (r6a[1], r6a[0], r6a[3], r6b[1], r6b[0])),
        N2=('HELD' if ('B exit : wanted 4 ; got 4 ; PASS' in tpg and 'B NO tag made locally : wanted no ; got no ; PASS' in tpg) else 'REFUTED',
            'the mismatch run exits 4, no tag made or pushed (data/b568_test_push_gated.txt, 18 of 18)'),
        N3=('HELD' if 'NO LEMMA BUILT' in rd8('b568_dichotomy.txt') else 'REFUTED',
            'DirichletCharacter.even_or_odd, Basic.lean :538 at de5ce8a9 (data/b568_dichotomy.txt)'),
        N4=('HELD' if h['h20a'] and h['h20b'] else 'REFUTED', 'H20a %s, H20b %s' % ('HELD' if h['h20a'] else 'REFUTED', 'HELD' if h['h20b'] else 'REFUTED')),
        N5=('HELD' if 18 <= n_nodes <= 24 and len(h['adds']) <= 2 and len(h['drops']) <= 1 else 'REFUTED',
            '%d nodes; added %d; dropped %d (%s: no declaration carries either name)' % (n_nodes, len(h['adds']), len(h['drops']), ', '.join(h['drops']))),
        N6=('HELD' if h20c and h20d else 'REFUTED', 'H20c %s, H20d %s' % ('HELD' if h20c else 'REFUTED', 'HELD' if h20d else 'REFUTED')),
        N7=('HELD' if (not k and kmain.startswith('6baed63')) else 'REFUTED',
            'the kernel checkout clean at main %s; no kernel file written; nothing at Zenodo; nothing deposits; the kept branches at '
            'their heads (data/b568_branches.txt); the page carries nothing beyond the ceiling (H20d)' % kmain[:7]),
        S1=('HELD' if len(h['bad_b']) == 1 else 'REFUTED', 'H20b fails at %d places, not one: %s' % (len(h['bad_b']), h['bad_b'])),
        S2=('HELD' if ('ch_iff_rh', 'ENCODES-CONCLUSION') in [tuple(x) for x in h['rec_other']] else 'REFUTED',
            'ch_iff_rh record ENCODES-CONCLUSION (T2), E0 DERIVES'),
        S3=('HELD' if not h['ch_consumers'] else 'REFUTED', 'no node consumes ch_iff_rh: %s' % (h['ch_consumers'] or 'none')),
        counts=dict(b566_after=r6a, b566_before=r6b, b567_after=r7a),
    )
    put_json('b568_scores.json', S)
    for k2 in ('H20a', 'H20b', 'H20c', 'H20d', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'S1', 'S2', 'S3'):
        print('  %-5s %-8s %s' % (k2, S[k2][0], S[k2][1][:150]))


def findings():
    """### FINDINGS: b567 at its weight (a line appended to b567's entry), and the act's entry. Appends only."""
    S = jl('b568_scores.json')
    zb = jl('b568_zetabounds_names.json')
    nb = {c: len(v) for c, v in zb['by'].items()}
    e567 = line_of(FIND, '## GRH-Weil, act three: the representation of L(s, χ)')
    w = ('\n*Appended 2026-10-01 by b568 to b567’s entry (:%d), under `(R178)`(1) -- b567 AT ITS WEIGHT:* SIDE-explicit-formula v0.10 = '
         '`6baed63`, tagged after main was read back at the remote; 32 new declarations at the standard three; no existing `.lean` '
         'file modified. `register4_positivity_liCoeff_imp_rh : Register4_positivity LiCoeff → RiemannHypothesis` discharges '
         '`residue_irreducible`’s `liCriterion` premise at λ := LiCoeff, with lv’s `Register4_positivity` restated from `2f71068`; '
         '`inequalityToPositivity` is not discharged. `LFunction_eq_mul_integral` -- L(s, χ) = s·∫₁^∞ S_χ(t) t^(−s−1) dt on 0 < Re s for '
         'χ ≠ 1 -- rests on Mathlib’s `LSeries_eq_mul_integral`, its Mellin differentiability and the identity theorem, with no '
         'analysis written in the kernel; the χ-analogues of `HasDerivAtZeta0`, `Zeta0EqZeta`, `DerivZeta0EqDerivZeta` and '
         '`ZetaBnd_aux1b` stand; `EF_lit_chi` is stated with the archimedean side by χ’s parity and HELD at its proof. H18a-H18c HELD. '
         '(N2) refuted as the seat read it: the distinct-rev count stays at 7 because `51e6992e` was SIDE-explicit-formula’s alone. '
         'W-ORD-DEPRECATIONS at 2,044 lines in 12 classes, all renames. The ceiling sentence of `(R177)`(2) at README :121 and '
         'REGISTRY :956 is the claim; nothing about ζ’s zeros is proved; `h2` is open. **H18b’s clause, as `(R178)`(2)(i) rewrites '
         'it:** “ZetaBounds’ χ-analogue completed” means the names later Zeta23 modules consume (the four ZetaBounds names and the '
         'HasDerivAt pair); the other names were not attempted -- relay `data/b568_b567_h18b_addendum.txt`, b567’s sealed face '
         'unedited. By the file’s own blocks the 146 are continuation %d, strip bounds %d, zero-free region %d; the HasDerivAt pair '
         'is among the 146 and was attempted, so 144 were not (relay `data/b568_zetabounds_names.txt`).\n'
         % (e567, nb['CONTINUATION'], nb['STRIP BOUNDS'], nb['ZERO-FREE REGION']))
    title = ('## CP-4, act one: the page of the compiled chain from Mathlib’s RiemannHypothesis to the ceiling, generated from '
             'SIDE-explicit-formula v0.10')
    guard_absent(FIND, title)
    h = jl('b568_h20ab.json')
    c = S['counts']
    e = ['', title, '',
         '*Filed at b568 on the author’s ruling `(R178)`. Banks: relay `data/b568_nodes.txt`, `data/b568_probe_out.txt`, '
         '`data/b568_node_cells.txt`, `data/b568_page_runs.txt`, `data/b568_page_checks.txt`, `data/b568_page_termscan.txt`, '
         '`data/b568_g_chain_page_live.txt`, `data/b568_dichotomy.txt`, `data/b568_zetabounds_names.txt`, `data/b568_test_push_gated.txt`, '
         '`data/b568_test_asof.txt`, `data/b568_b566_rerun_after.txt`, `data/b568_b567_rerun_after.txt`. Nothing about the zeros of ζ '
         'is claimed beyond the compiled statements’ own words.*', '',
         '**The page.** `THE_CLAUSE_AND_ITS_COMPILED_FACES.md` at the corpus root, generated by relay `tools/chain_page.py` (`%s`) from '
         'the node list relay `data/b568_nodes.txt`: a head of three sentences, %d node lines in dependency order, the open-node line '
         'in `(R178)`(5)’s words, the last derived line -- README :121’s 853 bytes, byte-identical -- and the Placement and '
         'Correspondence tables. Every cell is Lean’s own print at v0.10 = `6baed63` (Lean v4.34.0-rc1, Mathlib `de5ce8a9`) or a '
         'committed blob: `#print` for a definition, `#print sig` for a theorem, `#print axioms`, the declaration range, a consumption '
         'read over the kernel’s, Zeta23’s and Bulka’s modules; the E0 grade by relay `tools/e0_rule.py` on the source header; the '
         'tier from a record cell where one carries it, else the tier law on the grade and the print. Two runs byte-identical '
         '(sha256 `882190fe…`); the arm G-CHAIN-PAGE (`%s`) regenerates and compares.' % (C_GEN, h['n'], C_ARM), '',
         '**The chain.** %d nodes: the ruling’s list less `h2` and `RegisterDepth` -- no declaration carries either name at v0.10 -- '
         'plus `LiCriterion.taylorCoeff` and `ResidueDischarge.Register4_positivity`, the objects two node statements are about. The '
         'chain’s tops (no node consumes them): %s. `ch_iff_rh` is consumed by no node.' % (h['n'], ', '.join('`%s`' % x for x in h['tops'])), '',
         '**H20a %s** -- every node prints [propext, Classical.choice, Quot.sound]; every theorem node grades DERIVES under the E0 rule, '
         'the vendored converse included; ch_iff_rh’s grade of record is ENCODES-CONCLUSION (FACES_LEDGER :497), its tier T2, and '
         'the page prints both cells as read. **H20b %s** -- in its letter: Register4_positivity LiCoeff and Bulka’s '
         'Taylor-coefficient positivity are each joined to RiemannHypothesis by a compiled implication only; no declaration at v0.10 '
         'states either converse, though the pieces each would compose are compiled (rh_imp_li_nonneg, liCoeff_zero, '
         'li_coeff_eq_taylorCoeff). Every other open-looking Prop on the chain is joined to h2_sign by a compiled ↔ through '
         'h2_sign_iff_rh. **H20c %s. H20d %s** -- 0 banned-stem hits; no line outside the page’s parts.'
         % (S['H20a'][0], S['H20b'][0], S['H20c'][0], S['H20d'][0]), '',
         '**The four items.** (i) H18b’s clause rewritten by a declared-reading addendum; the 146 banked by class. (ii) The suite’s '
         'as-of commit (relay `%s`, alone, its test 10 of 10): b566 re-run reads %d of %d, failing %s -- arms reading PLACE-papers at '
         'HEAD, the kernel’s live refs and a clone b567 deleted, outside the relay tree the ruling names (before the change %d of %d); '
         'b567 re-run reads %d of %d. (iii) Mathlib’s `DirichletCharacter.even_or_odd` printed by name at `de5ce8a9` (Basic.lean :538); '
         'the domain-condition rule written in relay `tools/e0_rule.py` (`%s`) with `gammaBracket_chi_of_even` and '
         '`gammaBracket_chi_of_not_even` as its instance. (iv) `D:/b567-lake-51e6992e` deleted by its verified absolute path: 142,306 '
         'files, 8,526,917,308 bytes; no worktree inside it.' % (C_ASOF, c['b566_after'][1], c['b566_after'][0], c['b566_after'][3],
                                                                c['b566_before'][1], c['b566_before'][0], c['b567_after'][1],
                                                                c['b567_after'][0], C_E0), '',
         '**The defects of b567.** (a) becomes standing as FERRY_STANDING A5: no instrument edit before the seal. (f) -- one '
         '`timeout` wrap -- stands as recorded; the rule is unchanged. (g) -- the tag made locally before main’s read-back -- is closed '
         'in the instrument: relay `tools/push_gated.sh` (`%s`) makes each tag itself at the SHA it has just read back equal, and '
         'refuses a tag that already exists; its mismatch run refuses the tag (18 of 18).' % C_TAG, '',
         '**The scores.** H20a %s; H20b %s; H20c %s; H20d %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s, (N7) %s; the '
         'seat’s (S1) %s, (S2) %s, (S3) %s.' % tuple(S[k][0] for k in ('H20a', 'H20b', 'H20c', 'H20d', 'N1', 'N2', 'N3', 'N4', 'N5',
                                                                     'N6', 'N7', 'S1', 'S2', 'S3')), '',
         '**Next.** b569, GRH-Weil act four, as `(R178)`(8) fixes it: `EF_lit_chi`’s proof on a branch from v0.10 by Zeta23’s route '
         'for ζ, W-ORD-BULKA-GENERIC in front, H21a-H21d carried.', '',
         '*Nothing deposits; nothing at Zenodo written; no statement of any kernel changed; no sentence here claims priority; nothing '
         'here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    r1 = append_to(FIND, w)
    r2 = append_to(FIND, NL.join(e))
    lw = line_of(FIND, '*Appended 2026-10-01 by b568 to b567’s entry')
    le = line_of(FIND, title)
    put_json('b568_findings.json', dict(weight_line=lw, entry_line=le, appends=[r1, r2], b567_entry=e567))
    print('  FINDINGS weight :%s entry :%s' % (lw, le))


WO = [
    ('W-ORD-LI-THREE-WAY', 'BENCH (graded READING)', 'λ_n at n ≤ 12 by three routes -- the zero sum (BALPOS C.7’s values), the arithmetic '
     'limit (b563’s extrapolation) and Keiper’s expansion at s = 1 -- with floors; hypothesis: the three agree within floor at every n',
     'one bench act', 'the author’s word'),
    ('W-ORD-KEIPER-FACE', 'KERNEL', 'Keiper’s definition of λ_n compiled and shown equal to `LiCoeff`, giving the Li face a finite-n T0 '
     'statement that interval arithmetic can certify in-kernel', 'one kernel act', 'W-ORD-LI-THREE-WAY’s agreement'),
    ('W-ORD-BULKA-GENERIC', 'READ', 'a read, not a build: Bulka’s 33 vendored modules classified by the b564 rule (generic or ζ-specific '
     'by whether `riemannZeta` is named), to say whether the converse is an argument over a ZeroConfig', 'a small read component',
     'inside GRH-Weil act four, per `(R178)`(8)'),
]


def trail():
    """### OPEN_TRAILS: the count line at W-ORD-GRH-WEIL, the deletion line, the act's record with the three work-orders. Appends."""
    S = jl('b568_scores.json')
    zb = jl('b568_zetabounds_names.json')
    nb = {c: len(v) for c, v in zb['by'].items()}
    ua = {c: len(v) for c, v in zb['unattempted'].items()}
    fj = jl('b568_findings.json')
    wg = line_of(OT, '### `W-ORD-GRH-WEIL` -- THE χ-SIDE OF THE WEIL ARC')
    t567 = line_of(OT, '### b567 — GRH-Weil act three under (R177)')
    head = ('### b568 — lane three, act one under (R178): CP-4, the page of the compiled chain generated from SIDE-explicit-formula '
            'v0.10; b567’s four items; the tag made by the push script; the suite’s as-of commit')
    guard_absent(OT, head)
    a1 = ('\n*Appended 2026-10-01 by b568, under the author’s ruling `(R178)`(2)(i), to the W-ORD-GRH-WEIL entry (:%d) -- THE '
          'UNATTEMPTED ZETABOUNDS NAMES BY CLASS:* of Zeta23’s ZetaBounds.lean, the 146 names no later Zeta23 module consumes '
          '(relay `data/b568_zetabounds_names.txt`, each with its line) class by the file’s own blocks as continuation %d (before :1220: '
          'the Abel representation, the residue at 1, holomorphy), strip bounds %d ([:1220, :1850], through `ZetaDerivUpperBnd`), '
          'zero-free region %d (from :1851, `ZetaZeroFree` :2485 and its consequences). The HasDerivAt pair is among them and was '
          'attempted at b567, so the unattempted count is %d (continuation %d, strip bounds %d, zero-free region %d). The subset '
          '`EF_lit_chi`’s proof consumes is act four’s object (`(R178)`(8)).\n'
          % (wg, nb['CONTINUATION'], nb['STRIP BOUNDS'], nb['ZERO-FREE REGION'], sum(ua.values()), ua['CONTINUATION'],
             ua['STRIP BOUNDS'], ua['ZERO-FREE REGION']))
    a2 = ('\n*Appended 2026-10-01 by b568, under the author’s ruling `(R178)`(2)(iv), to b567’s record (:%d) -- THE OLD BUILD TREE '
          'DELETED:* `D:/b567-lake-51e6992e` (SIDE-explicit-formula’s former `.lake`, Mathlib `51e6992e`), 142,306 files, '
          '8,526,917,308 bytes (7.941 GiB), no worktree inside it (`git worktree list` printed), deleted by its verified absolute path '
          'in the same command; the kernel’s pin is `de5ce8a9` and the lv re-measure item targets `de5ce8a9` (relay '
          '`data/b568_oldlake.txt`).\n' % t567)
    rows = ['', head, '',
            '**(R178) ratified.** (1) b567 entered at its weight. (2) The seat’s four items ruled. (3) The defects closed; the tag '
            'made by the push script. (4) Lane three opened for the ζ-leg: CP-4. (5) The page’s form. (6) H20a-H20d. (7) Three trail '
            'lines entered as work-orders. (8) GRH-Weil act four fixed for b569.', '',
            '**Entered:** FINDINGS.md:%d (b567 at its weight, H18b’s clause rewritten) and :%d (the entry); OPEN_TRAILS.md (the '
            'W-ORD-GRH-WEIL count line, the deletion line, this record); PLACE-papers `THE_CLAUSE_AND_ITS_COMPILED_FACES.md` (new, '
            'generated); relay `tools/FERRY_STANDING.md` A5; SIDE-global-section CORRESPONDENCE.md row 413. Relay commits: the tag '
            'instrument `%s`, the as-of commit `%s`, the E0 rule `%s`, the generator `%s`, the arm `%s`, each alone with its test.'
            % (fj['weight_line'], fj['entry_line'], C_TAG, C_ASOF, C_E0, C_GEN, C_ARM), '',
            '**Component 0:** push-b567 branches deleted by name; the old build tree deleted. **Component 1:** the weight, the H18b '
            'addendum, the 146 by class, the dichotomy by name, the E0 rule, A5. **Component 2:** the two instruments; b566 re-run %s '
            'of %s, b567 re-run %s of %s. **Component 3:** %d nodes, two added, two dropped. **Component 4:** the generator, the page, '
            'G-CHAIN-PAGE.' % (S['counts']['b566_after'][1], S['counts']['b566_after'][0], S['counts']['b567_after'][1],
                                S['counts']['b567_after'][0], jl('b568_h20ab.json')['n']), '',
            '### The three work-orders of `(R178)`(7) -- entered 2026-10-01, b568, not started, each strikeable', '',
            '| # | ID | kind | the item | price | trigger |', '|:--|:--|:--|:--|:--|:--|']
    for i, (wid, kind, item, price, trig) in enumerate(WO, 1):
        rows.append('| **%d** | `%s` | **%s** | %s | %s | **%s** |' % (i, wid, kind, item, price, trig))
    rows += ['', '*Filed, not started.*', '',
             '**Next:** b569, GRH-Weil act four, as `(R178)`(8) fixes it: EF_lit_chi’s proof attempted on a branch from v0.10 by the '
             'route Zeta23’s EF_lit takes for ζ, the unattempted ZetaBounds names classified and the consumed subset attempted in '
             'import order, HELD at the earliest obstacle with the fact named; W-ORD-BULKA-GENERIC as a small read component in front. '
             'H21a (the consumed subset is the strip bounds, not the zero-free region), H21b (the strip bounds’ χ-analogues compile with '
             'no new analytic input), H21c (EF_lit_chi lands DERIVES at the standard three, or is HELD at a named fact), H21d '
             '(Bulka’s argument names riemannZeta in at most three of its 33 modules) carried.', '',
             '**H20a %s · H20b %s · H20c %s · H20d %s. (N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s · (N7) %s.** The seat’s '
             'own: (S1) %s, (S2) %s, (S3) %s.' % tuple(S[k][0] for k in ('H20a', 'H20b', 'H20c', 'H20d', 'N1', 'N2', 'N3', 'N4', 'N5',
                                                                         'N6', 'N7', 'S1', 'S2', 'S3')),
             '**No kernel written; no branch or tag of any kernel made; no `sorry` on any `main`.** Nothing deposits; nothing at Zenodo '
             'written; no existing statement changed; no Zeta23 or vendored file edited or added; no monograph byte changed; ERRATA '
             'untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here '
             'is a statement about RH, GRH or any zero beyond the compiled statements’ own words.', '']
    r = [append_to(OT, a1), append_to(OT, a2), append_to(OT, NL.join(rows))]
    put_json('b568_trail.json', dict(count_line=line_of(OT, '*Appended 2026-10-01 by b568, under the author’s ruling `(R178)`(2)(i)'),
                                     delete_line=line_of(OT, '*Appended 2026-10-01 by b568, under the author’s ruling `(R178)`(2)(iv)'),
                                     line=line_of(OT, head), wo=[w[0] for w in WO], appends=r))
    print(json.dumps(jl('b568_trail.json'), ensure_ascii=False)[:400])


ROW8 = '413'


def rows():
    """### the act's correspondence row through relay tools/corr_row.py. No grade word: the page grades nothing on a ledger."""
    if [l for l in Q.rd(CORR).split(NL) if l.startswith('| %s |' % ROW8)]:
        sys.exit('### ROW %s ALREADY PRESENT' % ROW8)
    h = jl('b568_h20ab.json')
    act = [ROW8,
           '**CP-4, THE PAGE WITHOUT NARRATIVE** (b568, under (R178)(4)-(5)). PLACE-papers THE_CLAUSE_AND_ITS_COMPILED_FACES.md, '
           'generated by relay tools/chain_page.py from relay data/b568_nodes.txt at SIDE-explicit-formula v0.10 = 6baed63: the '
           'compiled chain from Mathlib’s RiemannHypothesis to the ceiling sentence, %d nodes in dependency order, the open node '
           'h2_sign, the last derived line README :121. Nothing here proves RH.' % h['n'],
           'PLACE-papers THE_CLAUSE_AND_ITS_COMPILED_FACES.md (sha256 882190fe...) ; relay tools/chain_page.py, tools/g_chain_page.py',
           '%d of %d nodes print [propext, Classical.choice, Quot.sound], no sorryAx (relay data/b568_probe_out.txt, '
           'data/b568_node_cells.txt)' % (h['n'], h['n']),
           'no grade written by this row: the page prints the E0 reading and carries the record grades as read',
           'a corpus document generated from the kernel; no kernel written; nothing deposits; nothing at Zenodo written.']
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), CORR] + act, capture_output=True, text=True,
                       encoding='utf-8')
    put_json('b568_rows.json', dict(row=ROW8, exit=r.returncode, tail=(r.stdout + r.stderr)[-400:], act=act))
    print('  row %s exit %d' % (ROW8, r.returncode))


line_of, append_to, guard_absent = Q.line_of, Q.append_to, Q.guard_absent


def desk():
    S = jl('b568_scores.json')
    L = ['=' * 104, 'b568 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H20a-H20d ((R178)(6)).', '-' * 104]
    for k in ('H20a', 'H20b', 'H20c', 'H20d'):
        L.append('  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]))
    L += ['', '### THE NAVIGATOR`S SEVEN.', '-' * 104]
    for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7'):
        L.append('  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]))
    L += ['', '### THE SEAT`S THREE.', '-' * 104]
    for k in ('S1', 'S2', 'S3'):
        L.append('  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]))
    nh = sum(1 for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7') if S[k][0] == 'HELD')
    sh = sum(1 for k in ('S1', 'S2', 'S3') if S[k][0] == 'HELD')
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE 0.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; '
          'REFUTED %d.**' % (nh, 7 - nh, sh, 3 - sh),
          '### ### **H20 : %s.**' % ' ; '.join('%s %s' % (k, S[k][0]) for k in ('H20a', 'H20b', 'H20c', 'H20d')), '']
    L += rd8('b568_defects.txt').rstrip('\n').split(NL)
    put_txt('b568_desk_notes.txt', L)


def components():
    S = jl('b568_scores.json')
    h, fj, tj, rj = jl('b568_h20ab.json'), jl('b568_findings.json'), jl('b568_trail.json'), jl('b568_rows.json')
    c = S['counts']
    L = ['b568 -- THE COMPONENTS, BANKED UNDER (R178).', '',
         '### COMPONENT 0 : the process listing (no orphan, data/b568_procs_stepzero.txt) ; push-b567 and push-b567-closing deleted by '
         'name after --merged listed them (data/b568_branches.txt) ; D:/b567-lake-51e6992e: no worktree inside it, 142306 files, '
         '8526917308 bytes, deleted by its verified absolute path, ABSENT after (data/b568_oldlake.txt) ; the trail line OPEN_TRAILS :%s'
         % tj['delete_line'],
         '### COMPONENT 1 : the weight FINDINGS :%s ; the H18b addendum data/b568_b567_h18b_addendum.txt ; the 146 by class '
         'data/b568_zetabounds_names.txt, the count OPEN_TRAILS :%s ; the dichotomy data/b568_dichotomy.txt ; the E0 rule tools/e0_rule.py '
         '(relay %s) ; A5 in tools/FERRY_STANDING.md ; the (f) and (g) lines in the entry FINDINGS :%s' % (fj['weight_line'], tj['count_line'],
                                                                                                       C_E0, fj['entry_line']),
         '### COMPONENT 2 : the tag instrument relay %s (18 of 18) ; the as-of commit relay %s (10 of 10) ; b566 re-run %s of %s %s '
         '(before the change %s of %s) ; b567 re-run %s of %s' % (C_TAG, C_ASOF, c['b566_after'][1], c['b566_after'][0], c['b566_after'][3],
                                                              c['b566_before'][1], c['b566_before'][0], c['b567_after'][1], c['b567_after'][0]),
         '### COMPONENT 3 : data/b568_nodes.txt, %d nodes ; added %s ; dropped %s ; cells data/b568_node_cells.txt ; H20a %s, H20b %s'
         % (h['n'], [a[0] for a in h['adds']], h['drops'], S['H20a'][0], S['H20b'][0]),
         '### COMPONENT 4 : the generator relay %s (11 of 11) ; two runs byte-identical (sha256 882190fe...) ; the page at the corpus root ; '
         'its last line = README :121 ; 0 banned-stem hits ; G-CHAIN-PAGE relay %s (6 of 6), live PASS ; H20c %s, H20d %s'
         % (C_GEN, C_ARM, S['H20c'][0], S['H20d'][0]),
         '### COMPONENT 5 : the entry FINDINGS :%s ; the trail record OPEN_TRAILS :%s with W-ORD-LI-THREE-WAY, W-ORD-KEIPER-FACE, '
         'W-ORD-BULKA-GENERIC (not started) ; CORRESPONDENCE row %s (exit %d) ; next b569, GRH-Weil act four, H21a-H21d'
         % (fj['entry_line'], tj['line'], rj['row'], rj['exit'])]
    put_txt('b568_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b568_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn() or 0)
