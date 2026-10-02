# -*- coding: utf-8 -*-
"""b588_record.py -- THE ACT'S RECORD TOOL, UNDER (R198). ### ONE SUBCOMMAND PER BANK.

### ### b588: LANE THREE, ACT SIXTEEN -- CP-7 ACT THIRTEEN, THE EDITION OF TECHNE_TOOLKIT OVER ITS §XIII TABLE; THE CENSUS /
### TOTALITY PAIR IN THE CANON. Subcommands write only `data/b588_*` unless the docstring names another file. Every bank is written
### through `put_txt` / `put_json` (encode first, then a temp file, then `os.replace`). This act makes no platform call. ### The template
### is b587_record.py.
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
PRE_PP = 'c6af5b1'
MIRROR_PIN = '192077f'
CUR = 'phase1.5/method/TECHNE_TOOLKIT.md'
ED = 'phase1.5/method/TECHNE_TOOLKIT_v8_3.md'
CANON = 'phase1.5/method/THE_METHOD_CANON.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
WL = 'data/b558_editions/TECHNE_TOOLKIT.txt'
ARCH = 'archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-historical-landings-and-programs.md'
ARCH_ALL = ['archive/2026-08-24-ledger-split/FINDINGS-archive-1-entries-through-2026-08-20c.md',
            'archive/2026-08-24-ledger-split/FINDINGS-archive-2-entries-2026-08-21-and-22.md',
            'archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-1-seam-records-through-nineteenth.md', ARCH]

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
    '(a) THE FIRST LOCK ATTEMPT WAS REFUSED BY THE LOCK GATE, WRITING NOTHING: the face carried a banned stem twice (a compound '
    'naming the search shape that ignores letter case), and the scan of the face read NOT CLEAN; the face and three ledger '
    'sentences of this act`s record tool were reworded to "case-insensitive" through the Edit tool, section (0) says so, the gate '
    'chain was re-run whole and the second attempt locked. The refused attempt`s notes stand at data/b588_lockgate_notes.txt, the '
    'passing one at data/b588_lockgate_notes2.txt.',
    '(b) THE SUITE`S GENERATOR`S BLANKET RENAME TURNED TWO DELIBERATE b587 NAMES INTO b588: the prior closing the suite reads '
    '(`b587_closing.txt`) and the deleted branch list (`push-b587*`); the rule-19 grep found both before the suite`s first run, and '
    'both were corrected through the Edit tool -- the standing trap of a blanket rename.',
]


def defects():
    put_txt('b588_defects.txt', ['### b588 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay the TECHNE_TOOLKIT work-list, whole', RELAY, 'HEAD', WL, list(range(1, 21))),
    ('PLACE-papers TECHNE_TOOLKIT, whole', PP, PRE_PP, CUR, list(range(1, 601))),
    ('PLACE-papers the zeta page at the mirror`s pin, its pin line and nodes 7 and 8', PP, MIRROR_PIN, PAGE, [3, 11, 12]),
    ('PLACE-papers OPEN_TRAILS, the index line of the S6 crossing landing', PP, PRE_PP, 'OPEN_TRAILS.md', [770, 771, 772, 773, 774]),
    ('PLACE-papers OPEN_TRAILS, b454`s ledger table row for the cross-link verdict and its count line', PP, PRE_PP, 'OPEN_TRAILS.md',
     [6754, 6755, 6761, 6766]),
    ('PLACE-papers the archived landing, its section 2 whole', PP, PRE_PP, ARCH, list(range(8837, 8848))),
    ('relay b450`s two items for the toolkit', RELAY, 'HEAD', 'data/b450_components.txt', [172, 173]),
    ('relay b450`s batch, the toolkit`s block and the two items', RELAY, 'HEAD', 'data/b450_batch.json', list(range(389, 413)) + [950, 951, 955, 956]),
    ('relay b454`s shapes for the verdict', RELAY, 'HEAD', 'data/b454_registration_2026-09-14.txt', [87]),
    ('relay b557`s tier block for the toolkit, the e_difficulty reading', RELAY, 'HEAD', 'data/b557_tiers.txt', list(range(201, 220))),
    ('relay b540`s tier reading of the three Routes', RELAY, 'HEAD', 'data/b540_tiers.json', [437]),
    ('PLACE-papers REGISTRY, the deposited pin and the citation rule', PP, PRE_PP, 'REGISTRY.md', [962]),
    ('PLACE-papers README, the ceiling', PP, PRE_PP, 'README.md', list(range(106, 112))),
    ('PLACE-papers OPEN_TRAILS, the form, its clauses, lane three and the table rule', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11417, 11864, 11884, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 11996, 12044, 12062, 12082, 12084, 12086,
      12088, 12090, 12098]),
    ('PLACE-papers FINDINGS, b587`s entry', PP, PRE_PP, 'FINDINGS.md', [6674]),
    ('PLACE-papers THE_METHOD_CANON, its head and its appended sections', PP, PRE_PP, CANON, [1, 251, 253, 255, 257, 259, 261, 263, 276, 293]),
    ('PLACE-papers ENUMERA v1.5 and EXHAUSTIVENESS_LICENSE v0.1, the four instance lines', PP, PRE_PP, 'phase1.5/method/ENUMERA.md', [54, 895, 1040]),
    ('PLACE-papers EXHAUSTIVENESS_LICENSE v0.1, its :59', PP, PRE_PP, 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md', [59]),
    ('relay b587`s closing push-out, its head', RELAY, 'HEAD', 'data/b587_closing_push_out.txt', list(range(1, 4))),
]
SEARCH = 'E-Difficulty cross-link'
SHAPE2 = re.compile(r'cross-link', re.I)
# ### every terminal the §XIII table and the marked line name, at the pin the document prints: (repo, pin, declaration needle)
TERMINALS = [
    (':507 formation', 'SIDE-kernel', 'v1.7', r'^theorem formation : 2 \+ 3 \+ 2 \+ 0 = 7'),
    (':509 e_difficulty', 'SIDE-kernel', 'v1.4', r'^theorem e_difficulty \(s : DeterminedSystem\)'),
    (':511 offLine_of_codim_two', 'SIDE-kernel', '0e5233f', r'^theorem offLine_of_codim_two '),
    (':513 partialPositivity_finiteRange', 'SIDE-lv-conservation', 'e3d08b6', r'^theorem partialPositivity_finiteRange'),
    (':515 h1_complete_at_Phi', 'SIDE-lv-conservation', 'e3d08b6', r'^theorem h1_complete_at_Phi'),
    (':514 SteaneLabeling (a module)', 'SIDE-substrate-cluster', '2e76426', None),
    (':414 structural_exhaustiveness_proved (Route 1)', 'SIDE-kernel', 'v1.4', r'^theorem structural_exhaustiveness_proved'),
    (':414 spectral_cannon (Route 2)', 'SIDE-kernel', 'v1.4', r'^theorem spectral_cannon '),
    (':414 ConservationBridge.riemann_hypothesis (Route 3)', 'SIDE-kernel', 'v1.4', r'^theorem riemann_hypothesis'),
]
TAGS = [('SIDE-kernel', 'v1.4', 'f374174'), ('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-kernel', 'v1.7', '2957e7d'),
        ('SIDE-lv-conservation', 'v0.9.0', 'e3d08b6'), ('SIDE-explicit-formula', 'v0.1', 'baed4df'), ('SIDE-explicit-formula', 'v0.2', '5c72cad')]


def _grep_terminals():
    out = []
    for label, repo, pin, rx in TERMINALS:
        p = 'D:/' + repo
        if rx is None:
            hit = [l for l in g(p, 'ls-tree', '-r', '--name-only', pin).split(NL) if l.endswith('SteaneLabeling.lean')]
            out.append((label, repo, pin, hit))
            continue
        hits = [l for l in g(p, 'grep', '-n', '-E', rx, pin, '--', '*.lean').split(NL) if l.strip()]
        out.append((label, repo, pin, hits))
    return out


def _tags():
    out = []
    for repo, tag, sha in TAGS:
        p = 'D:/' + repo
        loc = g(p, 'rev-parse', tag + '^{}').strip()
        rem = [l.split('\t')[0] for l in g(p, 'ls-remote', 'origin', 'refs/tags/%s^{}' % tag).split(NL) if l.strip()]
        out.append((repo, tag, sha, loc[:7], (rem[0] if rem else '')[:7]))
    return out


def reads():
    L = ['b588 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    L.append('### THE CROSS-LINK VERDICT, SEARCHED BY NAME at %s -- shape 1 the ferry`s words "%s" as written; shape 2 "cross-link" '
             'in any case with "DISTINCT" on the same line:' % (PRE_PP, SEARCH))
    for f in ['FINDINGS.md', 'OPEN_TRAILS.md'] + ARCH_ALL:
        sl = g(PP, 'show', '%s:%s' % (PRE_PP, f)).split(NL)
        h1 = [i for i, l in enumerate(sl, 1) if SEARCH in l]
        h2 = [i for i, l in enumerate(sl, 1) if SHAPE2.search(l) and 'DISTINCT' in l]
        L.append('    %s : shape 1 %d hit(s) %s ; shape 2 %d hit(s) %s' % (os.path.basename(f), len(h1), [':%d' % i for i in h1],
                                                                          len(h2), [':%d' % i for i in h2]))
        for i in sorted(set(h1) | set(h2)):
            L.append('      :%d %s' % (i, sl[i - 1][:220]))
    L.append('### THE TERMINALS AT THEIR PINS, by git grep (no elaboration):')
    for label, repo, pin, hits in _grep_terminals():
        L.append('    %-52s %s @ %s : %s' % (label, repo, pin, ('FOUND ' + ' | '.join(h[:110] for h in hits)) if hits else '### NOT FOUND'))
    L.append('### THE TAGS THE EDITION CITES, peeled, locally and at the remote:')
    for repo, tag, sha, loc, rem in _tags():
        L.append('    %s %s : cited %s ; local %s ; remote %s ; %s' % (repo, tag, sha, loc, rem, 'AGREE' if loc == sha and rem == sha else '### DIFFER'))
    put_txt('b588_reads.txt', L)


# ================================================================================ COMPONENT 1 -- THE RECORD LINES AND THE CANON
B587_ENTRY = '## CP-7, act twelve: the edition of EXHAUSTIVENESS_LICENSE'
CANON_TAG = '<!-- b588 (R198)(2) THE CENSUS / TOTALITY PAIR, 2026-10-01 -->'
CANON_HEAD = ('## XX. The census / totality pair (added 2026-10-01, b588, under the author’s ruling `(R198)`(2); a pattern of the clarified '
              'layer, lane three at OPEN_TRAILS :11417; the navigator’s draft, struck if the author words it at the closing)')
CANON_PAIR = ('Every over-ceiling claim the CP-7 editions have corrected was a true finite fact — a place count, a class count, a compiled '
              'formula — carrying the name of the open obligation on all zeros. The edition separates the counted object from the open '
              'clause in the sentence itself; the separation is the programme’s reduction read from the error’s side.')
CANON_INST = ('*Instances, under the ceiling clause (OPEN_TRAILS :11906): ENUMERA v1.5 :54, :895, :1040, corrected at v1.6 :56, :897, '
              ':1042 (b586); EXHAUSTIVENESS_LICENSE v0.1 :59, corrected at v0.2 :61 (b587). Appended by b588 on the strength of the '
              'author’s paste, the clause strikeable; no byte above it changes.*')


def _words(t):
    return len(re.findall(r'\S+', t.replace(' — ', ' ')))


def c1_lines():
    """### PLACE-papers FINDINGS (b587's weight) and THE_METHOD_CANON (the census / totality pair, appended)."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B587_ENTRY)
    if entry != 6674:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    canon = os.path.join(PP, *CANON.split('/'))
    if g(PP, 'rev-parse', 'HEAD:' + CANON).strip() != g(PP, 'hash-object', CANON).strip():
        sys.exit('### THE CANON DIFFERS FROM ITS HEAD BLOB -- NOTHING WRITTEN')
    if _words(CANON_PAIR) > 80:
        sys.exit('### THE PAIR IS OVER 80 WORDS (%d) -- NOTHING WRITTEN' % _words(CANON_PAIR))
    weight = '*Appended 2026-10-01 by b588 to b587’s entry (:%d), under `(R198)`(1) -- b587 AT ITS WEIGHT:*' % entry
    Q.guard_absent(Q.FIND, weight)
    Q.guard_absent(canon, CANON_HEAD)
    out = [Q.append_to(Q.FIND, '\n%s `phase1.5/method/EXHAUSTIVENESS_LICENSE_v0_2.md` beside v0.1 unedited: 4 rows naming the premise in its '
                                 'Weil form (h2_sign_iff_rh); the census / exhaustiveness pair applied once at :59, seven ceiling-shaped '
                                 'phrases read and carried; the S2 seal located at OPEN_TRAILS :6763 and credited beneath :59 as '
                                 'structural_exhaustiveness_proved’s place-count conjunct, T2; the three branch-state lines citing their '
                                 'fast-forward tips 5a14205 and a0dc376 (“merge commit” the navigator’s); H28a, H28b (+2 against 2) and H28c '
                                 'held, the scanner reading the edition CLEAN; all ten expectations held. ENUMERA v1.6’s line on the CR '
                                 'names appended as housekeeping (PLACE-papers 6518f68), the ferry’s omission the navigator’s. The name '
                                 'exception extended at OPEN_TRAILS :12082; the table rule at :12084-:12088; W-ORD-CONSTELLATION-RERUN at '
                                 ':12090. The suite reads 70 of 70.\n' % weight)]
    out.append(Q.append_to(canon, NL.join(['', CANON_TAG, '', CANON_HEAD, '', '> **%s**' % CANON_PAIR, '', CANON_INST]) + NL))
    lines = dict(weight=Q.line_of(Q.FIND, weight), canon_head=Q.line_of(canon, CANON_HEAD), canon_pair=Q.line_of(canon, '> **' + CANON_PAIR[:40]),
                 canon_inst=Q.line_of(canon, CANON_INST[:60]))
    put_json('b588_c1_lines.json', dict(entry=entry, lines=lines, heads=dict(weight=weight, canon=CANON_HEAD), pair=CANON_PAIR,
                                        pair_words=_words(CANON_PAIR), inst=CANON_INST, appends=out))
    print(lines, 'pair words', _words(CANON_PAIR))


# ================================================================================ COMPONENT 2 -- THE EDITION
EF = 'SIDE-explicit-formula'
PIN = {'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'ch_iff_rh': 'v0.1 = `baed4df`'}
NS = {'h2_sign_iff_rh': 'B321', 'ch_iff_rh': 'B321'}
WHERE = {'h2_sign_iff_rh': 'the zeta page, node 8, line 12', 'ch_iff_rh': 'the zeta page, node 7, line 11'}
CH = '`ch_iff_rh`, %s %s' % (EF, PIN['ch_iff_rh'])
H2 = '`h2_sign_iff_rh`, %s %s' % (EF, PIN['h2_sign_iff_rh'])

OLD_B = ('The route terminals **compose under the named premise `h2`** — **criterion + verified surround, not end-to-end**: the surround '
         '`h1_complete_at_Phi` is machine-checked, the finite range is certified to `N₀(T)=⌊2T²⌋`, and the census maps every route to the one '
         'open premise (EXCLUSION_ENGINE §VIII.0 Rule 3).')
NEW_B = ('The reduction **composes under the named premise `h2`**, in its Weil form `h2_sign` equivalent to RH (%s), so that the premise is '
         'RH itself — **criterion + verified surround, not end-to-end**: the surround `h1_complete_at_Phi` is machine-checked, the finite range '
         'is certified to `N₀(T)=⌊2T²⌋`, and the census maps every route to the one open premise (EXCLUSION_ENGINE §VIII.0 Rule 3), while no '
         'route terminal composes under it: Route 3 composes under `ConservationHypothesis`, RH restated, and Routes 1 and 2 are not routes '
         'to σ = 1/2, Route 1 being T2 by its decide-count conjunct and the C₇ stand-in and Route 2 T0, a fact about `completedRiemannZeta₀` '
         'on the line (relay `data/b540_tiers.json` :437).' % H2)
REWRITES = [
    (414, 'the three RH-route terminals `structural_exhaustiveness_proved` (Route 1),',
     'the three terminals the corpus has numbered as RH routes, `structural_exhaustiveness_proved` (Route 1),'),
    (414, 'ride post-v1.4 on `main`, tag untouched).',
     'ride post-v1.4 on `main`, tag untouched), and Route 3 is no route, its premise `ConservationHypothesis` being RH restated (%s), '
     'so that it formalizes RH ⇒ RH.' % CH),
    (414, OLD_B, NEW_B),
]
CEIL_RECORD = 'ceiling correction record:'
CARRY_RECORD = 'ceiling read, carried:'
STEM_RECORD = 'stem correction record:'
STEM_TAIL = ' (banned stem; correction record)'
FACT_RECORD = 'fact correction record:'
CEILS = [
    (239, 'The E-Difficulty equivalence (F-7) is proved.',
     'The E-Difficulty equivalence (F-7) is proved over the kernel\'s own `DeterminedSystem` type, the scope its terminal `e_difficulty` states.'),
    (475, '(the proof compiles end-to-end; it is not conditional)',
     '(the reduction compiles end-to-end under its named premise `h2`, which is named as a premise, not called a condition)'),
]
STEMS = [
    (128, 'every gap is a named task', 'every residue is a named task'),
    (481, 'where the old "gap" named nothing', 'where the old word named nothing'),
    (516, 'this is the honest grade, not a gap', 'this is the honest grade, not a deficiency'),
]
FACTS = [
    (414, '(deposit SIDE-kernel v1.4 = `f374174`;', '(SIDE-kernel v1.4 = `f374174`, the deposit being v1.5 = `0e5233f` (REGISTRY :962);'),
]
CARRIED = {
    10: 'a dated history entry: the v8.2 changelog records the RH route restated as criterion + verified surround under `h2` “rather '
        'than” the end-to-end framing, a negation, carried as the dated record under the history clause',
}
CREDIT = (239, '*Credit (b450 item, located at b588): the E-Difficulty cross-link verdict `DISTINCT` -- located by name at OPEN_TRAILS :773 '
               '(the index line of the `S6` crossing landing, 2026-08-12) and held whole at `%s` :8839-:8847 -- reads that E-Difficulty '
               'measures catalogue-closeability and that the dichotomy places RH on its in-scope, decidable side, so that `h2`’s difficulty '
               'lies inside that side and is not of the kind F-7 formalizes, while F-7’s terminal `e_difficulty` (SIDE-kernel v1.4 = '
               '`f374174`) states that a conserved `DeterminedSystem` is decidable iff a `DomainOstrowski` for it exists (relay '
               '`data/b557_tiers.txt` :213), T2, over the file’s own types (relay `data/b557_tiers.txt` :216).*' % ARCH)
VERSION = (8, '**v8.3, 2026-10-01** — *CP-7 edition (b588), written beside v8.2, which is unedited; its back matter closes the file.*')
CEILING = re.compile(r'RH proved|RH is proved|proof of RH|proves RH|RH proof|end-to-end|\bis proved\b|RH-route|RH routes?\b')
BM_TAG = '<!-- b588 (R198) THE v8.3 EDITION`S BACK MATTER, 2026-10-01 -->'
BANKROWS = (('b540_tiers.json', 437), ('b557_tiers.txt', 213), ('b557_tiers.txt', 216))
LEDGERS = (('OPEN_TRAILS :773', 'PLACE-papers `OPEN_TRAILS.md`', 'the index line of the S6 crossing landing, the verdict by name'),
           ('`%s` :8839-:8847' % ARCH, 'PLACE-papers archive', 'the landing`s section 2, the verdict whole'),
           ('REGISTRY :962', 'PLACE-papers `REGISTRY.md`', 'the deposited pin and the citation rule'))
READING_NAME = {0: 'none -- resolved by the form', 1: '(c) h2 takes h2_sign', 2: '(e) the T2 terminal says what it states'}
OFFSET = ('+1 from :8 (the v8.3 line, above the v8.2 line); +2 more from :240 (a blank and the credit line, beneath :239) -- v8.2 :n sits at the '
          'edition`s :n for n < 8, at :n+1 for 8 <= n <= 239 and at :n+3 for n >= 240')
XIII = (501, 518)


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _rows():
    return [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'TECHNE' and r['verdict'] == 'MOVED-IN-MEANING']


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    return n + (1 if n >= VERSION[0] else 0) + (2 if n > CREDIT[0] else 0)


def _all_changes():
    return REWRITES + CEILS + STEMS + FACTS


def edition(*a):
    """### PLACE-papers phase1.5/method/TECHNE_TOOLKIT_v8_3.md, beside the current version from its blob at c6af5b1; the re-pin step last."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE c6af5b1 -- NOTHING WRITTEN')
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
            sys.exit('### :%d -- THE CHANGE ALTERED THE LINE`S SEGMENT COUNT %d -> %d' % (ln, n0, len(_segs(new[ln - 1]))))
    if not cur[VERSION[0] - 1].startswith('**v8.2, 2026-07-23**'):
        sys.exit('### THE VERSION ANCHOR IS NOT WHERE THE FACE SAYS')
    if not cur[XIII[0] - 1].startswith('## XIII. Correspondence') or not cur[XIII[1] - 1].startswith('*Note on C₆/C₇'):
        sys.exit('### THE §XIII TABLE IS NOT WHERE THE FACE SAYS')
    for t in (CREDIT[1], VERSION[1]):
        if len(_segs(t)) != 1:
            sys.exit('### AN INSERTED LINE IS NOT ONE SENTENCE (%d): %s' % (len(_segs(t)), t[:60]))
    diff = []
    for r in _rows():
        ln = r['line']
        k = _segs(cur[ln - 1]).index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d] in nw]
        banks = ['%s:%d' % (b, n) for b, n in BANKROWS if ('relay `data/%s` :%d' % (b, n)) in nw]
        reading = 1 if r['terminal'] == 'h2_sign' else 2
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         reading=reading, cites=cites, banks=banks, supports=r['reading']))
    new[CREDIT[0]:CREDIT[0]] = ['', CREDIT[1]]
    new[VERSION[0] - 1:VERSION[0] - 1] = [VERSION[1]]
    body = list(new)
    changed = set(x[0] for x in _all_changes())
    if any(_edl(n) > len(body) or (n not in changed and body[_edl(n) - 1] != cur[n - 1]) for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL DOES NOT CARRY THE CURRENT VERSION')
    if body[_edl(CREDIT[0]) + 1] != CREDIT[1] or body[_edl(CREDIT[0])] != '':
        sys.exit('### THE CREDIT IS NOT BENEATH :239')
    inv = {_edl(n): n for n in range(1, len(cur) + 1)}
    hits = [(i, m.group(0)) for i, l in enumerate(body, 1) for m in CEILING.finditer(l)]
    stray = sorted(set(inv.get(i, -i) for i, _ in hits) - set(CARRIED) - changed)
    if stray:
        sys.exit('### A CEILING HIT IN THE BODY IS NEITHER CORRECTED, REWRITTEN NOR CARRIED BY THE SEAT`S READ: current lines %s' % stray)
    xs, xe = _edl(XIII[0]), _edl(XIII[1])
    bm = ['', BM_TAG, '',
          '## Back matter of the v8.3 edition -- written 2026-10-01 by b588 under the author’s ruling `(R198)`(3), by the form of `(R187)`(5)', '',
          '*This file is v8.3 of TECHNE_TOOLKIT, the CP-7 edition written beside v8.2 (`%s`, unedited) from v8.2’s tier block (its :569, '
          'standing: 10 rows, 6 terminal readings, T0 1, T1-lit 2, T2 3, five rows with no terminal) and its CP-1b work-list (relay `%s`), the '
          'ζ page as its spine and its §XIII table as its Correspondence table; it does not deposit and does not replace v8.2, and its '
          'promotion is CP-8’s. Every line cited below is this file’s own.*' % (CUR, WL), '',
          '### Removals', '', 'None: every one of the 3 work-list rows resolves to a sentence rewritten in place to what its compiled fact says.', '',
          '### Credit lines', '', '| this edition’s line | the item | Status |', '|:--|:--|:--|',
          '| :%d | the E-Difficulty cross-link verdict `DISTINCT` (b450, relay `data/b450_batch.json` :956), located by name at OPEN_TRAILS :773 '
          '| inserted beneath :%d, the claim it corrects (F-7), the author’s answer before b588’s seal |' % (_edl(CREDIT[0]) + 2, _edl(CREDIT[0])), '',
          '### Ceiling corrections', '', '| this edition’s line | v8.2 wording | v8.3 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in CEILS:
        bm.append('| :%d | %s %s | %s | corrected under the ceiling clause, the author’s answer before b588’s seal |' % (_edl(ln), CEIL_RECORD, old, rep))
    bm += ['', '### Ceiling-shaped sentences read and carried', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(CARRIED):
        bm.append('| :%d | %s %s | carried as read |' % (_edl(ln), CARRY_RECORD, CARRIED[ln]))
    bm += ['', '### Stem corrections', '', '| this edition’s line | v8.2 wording | v8.3 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in STEMS:
        bm.append('| :%d | %s %s%s | %s | corrected under the stem clause, the object the sentence names%s |' % (
            _edl(ln), STEM_RECORD, old, STEM_TAIL, rep,', the §XIII preamble’s own word (its :%d); no terminal or grade cell moves' % _edl(503) if ln == 516 else ''))
    bm += ['', '### Fact corrections', '', '| this edition’s line | v8.2 wording | v8.3 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in FACTS:
        bm.append('| :%d | %s %s | %s | corrected under the fact clause: REGISTRY :962 prints the deposit at v1.5 = `0e5233f` and the rule that '
                  'a sentence citing SIDE-kernel for the deposit cites v1.5; the tag v1.4 = `f374174` agrees locally and at the remote (relay '
                  '`data/b588_reads.txt`), the author’s answer before b588’s seal |' % (_edl(ln), FACT_RECORD, old, rep))
    bm += ['', '### The navigator’s expectations of `(R198)`(3)', '', '| expectation | the read | Status |', '|:--|:--|:--|',
           '| the E-Difficulty cross-link verdict `DISTINCT` located by name and credited | located at OPEN_TRAILS :773, held whole at the '
           'archived landing :8839-:8847 | credited beneath :%d |' % _edl(CREDIT[0]),
           '| b450’s “THERE IS NO TABLE” superseded by the §XIII location | §XIII at this edition’s :%d-:%d | superseded below, under Correspondence |' % (xs, xe),
           '| sentences naming h2 take `h2_sign` where the work-list marks them | 1 row, :%d | rewritten |' % _edl(414),
           '| the instrument descriptions stand unless a kernel fact prints otherwise | no instrument description moved; the one fact '
           'correction is a deposit pin | carried |',
           '| T2 terminals’ sentences say what each states | Route 1 at :%d; `e_difficulty` in the credit at :%d; the §XIII rows with the '
           'tier block beneath | rewritten and credited |' % (_edl(414), _edl(CREDIT[0]) + 2),
           '', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v8.3 | `%s` | written at b588 |' % ED,
           '| the current version, v8.2 | `%s` | unedited |' % CUR,
           '| the spine | `%s` at PLACE-papers `%s` | read, unedited |' % (PAGE, MIRROR_PIN),
           '| the work-list | relay `%s` | read |' % WL,
           '| the sentence-by-sentence diff | relay `data/b588_edition_TECHNE.txt` | banked at b588 |',
           '', '### Correspondence', '',
           '**The table.** This edition’s Correspondence table is its own §XIII, “Correspondence — technique entry → certificate grade”, at '
           ':%d-:%d, carried from v8.2 :%d-:%d with one cell’s wording corrected under the stem clause (:%d) and no terminal or grade cell '
           'moved; b557’s tier block beneath it (:%d) tiers its 10 rows. b450’s line “THERE IS NO TABLE” for this document (relay '
           '`data/b450_components.txt` :172; `data/b450_batch.json` :951) is superseded by that location, which b586’s census read as present '
           'under a Correspondence heading (relay `data/b586_corroboration.txt` :18), b450’s matcher having wanted a line beginning '
           '“## Correspondence” (relay `tools/b450_components.py` :296) where the heading reads “## XIII. Correspondence”.' % (xs, xe, XIII[0], XIII[1], _edl(516), _edl(569)), '',
           '| declaration, bank line or ledger line | repository | pin | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    ed_lines = {d: [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l and PIN[d] in l] for d in PIN}
    for d in PIN:
        bm.append('| `SIDEExplicitFormula.%s.%s` | %s | %s | %s | cited at :%s of this edition |' % (
            NS[d], d, EF, PIN[d].replace('`', ''), WHERE[d], ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    bank_lines = {}
    for bank, n in BANKROWS:
        at = [i for i, l in enumerate(body, 1) if ('relay `data/%s` :%d' % (bank, n)) in l]
        bank_lines['%s:%d' % (bank, n)] = at
        bm.append('| `data/%s` :%d | relay | the tier law`s read | not on the page | cited at :%s of this edition |' % (
            bank, n, ', :'.join(str(x) for x in at) or '### NONE'))
    ledger_lines = {}
    for needle, repo, what in LEDGERS:
        at = [i for i, l in enumerate(body, 1) if needle in l]
        ledger_lines[needle] = at
        bm.append('| %s | %s | %s | not on the page | cited at :%s of this edition |' % (needle, repo, what, ', :'.join(str(x) for x in at) or '### NONE'))
    bm.append('')
    if any('### NONE' in l for l in bm):
        sys.exit('### A CORRESPONDENCE ROW CITES NO LINE OF THE EDITION')
    full = body + bm
    b = (NL.join(full) + NL).encode('utf-8')
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    put_json('b588_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=1, removals=0, ruled_citations=0, version_lines=1, diff=diff, offset=OFFSET,
                                       ceils=CEILS, stems=STEMS, facts=FACTS, rewrites=REWRITES,
                                       credit_line=dict(after=CREDIT[0], at=_edl(CREDIT[0]) + 2, text=CREDIT[1]),
                                       carried={str(k): v for k, v in CARRIED.items()}, version=dict(above=VERSION[0], text=VERSION[1]),
                                       xiii=dict(cur=list(XIII), ed=[xs, xe]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines,
                                       bank_lines=bank_lines, ledger_lines=ledger_lines))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))


def edition_bank():
    """### The diff with its offset line, the corrections, the counts, the ceiling read, the scanner's verdict, H28a-H28c."""
    E = jl('b588_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(BM_TAG)
    scan = rd('b588_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    carried_ed = set(_edl(n) for n in CARRIED)
    corrected_ed = set(_edl(x[0]) for x in CEILS)
    rewritten_ed = set(_edl(x[0]) for x in REWRITES)
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            kind = ('record' if (i > cut and l.startswith('| :') and (CEIL_RECORD in l or CARRY_RECORD in l))
                    else 'carried' if (i < cut and i in carried_ed)
                    else 'corrected' if (i < cut and i in corrected_ed)
                    else 'rewritten' if (i < cut and i in rewritten_ed) else 'beyond')
            hits.append(dict(line=i, hit=m.group(0), kind=kind, ctx=l[max(0, m.start() - 60):m.end() + 40]))
    beyond = [h for h in hits if h['kind'] == 'beyond']
    h28a_bad = [d['id'] for d in E['diff'] if not d['changed'] or not (d['cites'] or d['banks'])]
    h28a = 'HELD' if not h28a_bad else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur']
    allowed = E['credit'] + E['removals'] + E['ruled_citations'] + E['version_lines']
    h28b = 'HELD' if abs(body_dn) <= allowed else 'REFUTED'
    live_n = int(live.group(1)) if live else None
    h28c = 'HELD' if (live_n == 0 and clean and not beyond) else 'REFUTED'
    cur0 = _cur()
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % OFFSET, '',
         'b588 -- COMPONENT 2: THE EDITION OF TECHNE_TOOLKIT, (R198)(3), BY THE FORM OF (R187)(5) AND ITS CLAUSES, OVER ITS §XIII TABLE', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :8 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0], cur0[7][:90]),
         '### its tier block : :569 "%s"' % cur0[568][:110],
         '### its §XIII table : :%d-:%d, read as the Correspondence table ("%s")' % (XIII[0], XIII[1], cur0[XIII[0] - 1][:70]),
         '### its version history : the version line :8 (v8.2, prior v8.1); the v8.2 changelog :10; §XII :457-:497; b450`s annotation '
         ':555-:564; b557`s tier block :567-:598; b558`s line :600',
         '### the cross-link verdict searched by name (relay data/b588_reads.txt): OPEN_TRAILS :773 -- LOCATED (shape 2; the ferry`s words as '
         'written meet only b454`s table row :6761 and the batch row :6642); held whole at the archived landing :8839-:8847',
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE WORK-LIST, ROW BY ROW (3 rows, 2 sentences, 1 line):', '']
    for d in E['diff']:
        L += ['  %s v8.2 :%d -> v8.3 :%d `%s` -- %s ; cites %s ; banks %s' % (d['id'], d['line'], d['ed_line'], d['terminal'], READING_NAME[d['reading']],
                                                                          ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']], d['banks']),
              '      work-list: %s' % d['supports'], '      v8.2 : %s' % d['old'], '      v8.3 : %s' % d['new'], '']
    cov = [d for d in E['diff'] if d['reading']]
    L += ['### COVERAGE BY THE EXPECTATIONS OF (R198)(3), the seat`s hand-read: %d of %d rows -- (c) %d, (e) %d' % (
        len(cov), len(E['diff']), sum(1 for d in cov if d['reading'] == 1), sum(1 for d in cov if d['reading'] == 2)), '',
          '### THE CREDIT LINE (the author`s answer): v8.3 :%d, beneath v8.2 :239' % E['credit_line']['at'], '      %s' % E['credit_line']['text'], '']
    L += ['### THE CEILING CORRECTIONS (%d), the author`s answers:' % len(E['ceils'])]
    L += ['    v8.2 :%d -> v8.3 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in E['ceils']]
    L += ['### THE CEILING-SHAPED SENTENCES READ AND CARRIED:'] + ['    v8.2 :%d -> v8.3 :%d  %s' % (n, _edl(n), CARRIED[n]) for n in sorted(CARRIED)]
    L += ['### THE STEM CORRECTIONS (%d), the stem clause, the author`s answer on :516:' % len(E['stems'])]
    L += ['    v8.2 :%d -> v8.3 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in E['stems']]
    L += ['### THE FACT CORRECTIONS (%d), the fact clause, the author`s answer:' % len(E['facts'])]
    L += ['    v8.2 :%d -> v8.3 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in E['facts']]
    L += ['      the source: PLACE-papers REGISTRY.md :962 @ %s "%s"' % (PRE_PP, g(PP, 'show', '%s:REGISTRY.md' % PRE_PP).split(NL)[961][:260])]
    L += ['      the tags, peeled (relay data/b588_reads.txt): ' + ' ; '.join(l.strip() for l in rd('b588_reads.txt').split(NL)
                                                                         if l.startswith('    SIDE-kernel v1.'))]
    L += ['### REMOVALS: none.',
          '### THE VERSION LINE: above v8.2 :%d: %s' % (E['version']['above'], E['version']['text']), '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d) ; the back '
          'matter %d ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d + one version line = %d' % (
              body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], {'record': 'quoted in a back-matter record, read by the seat',
                                                                 'carried': 'in a sentence the seat read and carried',
                                                                 'corrected': 'in a sentence corrected under the ceiling clause, its scope named',
                                                                 'rewritten': 'in a work-list sentence rewritten in place',
                                                                 'beyond': '### BEYOND THE CEILING'}[h['kind']], h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### THE SCANNER (banned_terms.py) on the edition: live uses %s ; verdict %s' % (live_n, 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on the page at its pin or a bank line%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s live count %s and verdict %s; sentences beyond the ceiling %d.**' % (
              h28c, live_n, 'CLEAN' if clean else 'NOT CLEAN', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b588_edition_TECHNE.txt', L)
    put_json('b588_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=live_n, clean=clean, beyond=len(beyond), hits=hits,
                                   covered=len(cov), held=None, n_ceils=len(E['ceils']), n_stems=len(E['stems']), n_facts=len(E['facts'])))
    H = jl('b588_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'covered', H['covered'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'],
          'live', H['live'], 'ceils', H['n_ceils'], 'stems', H['n_stems'], 'facts', H['n_facts'])


# ================================================================================ THE SCORING AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}


def _xiii_cells():
    """### the §XIII table's rows, v8.2 against v8.3, cell by cell: (line, column, old, new) for every cell that differs."""
    cur = _cur()
    ed = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read().replace(chr(13), '').split(NL)
    out = []
    for n in range(XIII[0], XIII[1] + 1):
        a, b = cur[n - 1], ed[_edl(n) - 1]
        if a.startswith('|') and b.startswith('|'):
            ca, cb = a.strip('|').split('|'), b.strip('|').split('|')
            out += [(n, k, x.strip(), y.strip()) for k, (x, y) in enumerate(zip(ca, cb)) if x != y]
            if len(ca) != len(cb):
                out.append((n, -1, str(len(ca)), str(len(cb))))
        elif a != b:
            out.append((n, -2, a[:60], b[:60]))
    return out


def scores():
    H, E = jl('b588_h28.json'), jl('b588_edition.json')
    reads_ = rd('b588_reads.txt')
    ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD') + NL +
                                g(PP, 'ls-files', '--others', '--exclude-standard', 'phase1.5', 'phase2')).split(NL) if x.strip()))
    kmain = g('D:/SIDE-explicit-formula', 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    cur_same = g(PP, 'hash-object', CUR).strip() == E['cur_blob']
    m = re.search(r'OPEN_TRAILS\.md : shape 1 (\d+) hit\(s\) (\[[^\]]*\]) ; shape 2 (\d+) hit\(s\) (\[[^\]]*\])', reads_)
    n1 = m is not None and "':773'" in m.group(4)
    n2 = H['H28a'] == 'HELD' and H['H28b'] == 'HELD' and H['H28c'] == 'HELD' and H['held'] is None
    n3 = H['n_ceils'] <= 3 and H['n_facts'] <= 1
    cells = _xiii_cells()
    terms = [l for l in reads_.split(NL) if re.match(r'^    :\d{3} ', l) and ' @ ' in l and (' : FOUND' in l or 'NOT FOUND' in l)]
    xiii_terms = [l for l in terms if not l.startswith('    :414')]
    terms_ok = len(xiii_terms) == 6 and all(' : FOUND' in l for l in terms)
    n4 = terms_ok and cells == []
    allowed_pp = {'FINDINGS.md', 'OPEN_TRAILS.md', ED, CANON}
    S = dict(
        N1=('HELD' if n1 else 'REFUTED', 'the verdict searched by name: OPEN_TRAILS :773 (the index line of the S6 crossing landing, by the '
            'case-insensitive shape; the ferry`s words as written meet only b454`s table row :6761 and the batch row :6642); held whole at the '
            'archived landing :8839-:8847 ; FINDINGS no hit'),
        N2=('HELD' if n2 else 'REFUTED', 'H28a %s, H28b %s (the body %+d against at most %d), H28c %s; no sentence held' % (
            H['H28a'], H['H28b'], H['body_dn'], H['allowed'], H['H28c'])),
        N3=('HELD' if n3 else 'REFUTED', 'the ceiling clause corrects %d (:239, :475), the fact clause %d (:414)' % (H['n_ceils'], H['n_facts'])),
        N4=('HELD' if n4 else 'REFUTED', 'the §XIII terminals print at their pins by git grep: %s; cells moved %s -- the one text cell '
            'corrected under the stem clause, as the author answered; no terminal or grade cell moved' % (
                'all %d FOUND' % len(xiii_terms) if terms_ok else '### NOT ALL FOUND', ['v8.2 :%d col %d "%s" -> "%s"' % c for c in cells])),
        N5=('HELD' if (kmain == V015 and heads_ok and cur_same and set(ch) <= allowed_pp) else 'REFUTED', 'nothing deposits; no kernel touched '
            '(%s); the current version unedited (%s); PLACE-papers changed at %s' % (
                'held' if kmain == V015 and heads_ok else '### MOVED', 'held' if cur_same else '### EDITED', ch)),
        S1=('HELD' if n1 else 'REFUTED', '(N1) holds at OPEN_TRAILS :773'),
        S2=('HELD' if n2 and H['body_dn'] == 2 and H['allowed'] == 2 else 'REFUTED', 'H28a-H28c held; the body +2 against 2'),
        S3=('HELD' if H['n_ceils'] == 2 and H['n_facts'] == 1 and H['n_stems'] == 3 else 'REFUTED',
            'the ceiling clause corrects 2, the fact clause 1, the stem clause 3'),
        S4=('HELD' if terms_ok and [(c[0], c[1]) for c in cells] == [(516, 2)] else 'REFUTED',
            '(N4) refuted in its letter at :516`s text cell alone, every terminal FOUND at its pin'),
        S5=('HELD' if (set(ch) | {'OPEN_TRAILS.md'}) == allowed_pp and set(ch) <= allowed_pp else 'REFUTED',
            'the PLACE-papers files changed are the four named on the face, OPEN_TRAILS by the trail record this scoring precedes '
            '(changed at scoring: %s; the suite`s G-CORPUS-SCOPE reads the four after it)' % ch),
        counts=dict(pp_changed=ch, body_dn=H['body_dn'], ceils=H['n_ceils'], facts=H['n_facts'], stems=H['n_stems'], cells=cells),
    )
    put_json('b588_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], S[k][1][:170]))


TITLE_HEAD = ('## CP-7, act thirteen: the edition of TECHNE_TOOLKIT from its tier block and §XIII table, the cross-link verdict located; '
              'the census / totality pair in the canon')
TITLE = TITLE_HEAD + '; written as v8.3 beside v8.2, no sentence held'
TRAIL_HEAD = ('### b588 — lane three, act sixteen under (R198): CP-7 act thirteen -- the edition of TECHNE_TOOLKIT written beside the '
              'current over its §XIII table; the census / totality pair in the canon')


def records_pp():
    Q = _Q()
    S, H, E, C1 = jl('b588_scores.json'), jl('b588_h28.json'), jl('b588_edition.json'), jl('b588_c1_lines.json')
    Q.guard_absent(Q.FIND, TITLE_HEAD)
    e = ['', TITLE, '',
         '*Filed at b588 on the author’s ruling `(R198)`. Banks: relay `data/b588_edition_TECHNE.txt` (the sentence-by-sentence diff, its '
         'offset line at its head), `data/b588_edition.json`, `data/b588_reads.txt`. Nothing deposits.*', '',
         '**The edition** (`(R198)`(3)): `%s`, v8.3, written beside v8.2 (`%s`, unedited) from v8.2’s tier block and its CP-1b work-list, the '
         'ζ page as its spine and its §XIII table as its Correspondence table, b450’s “THERE IS NO TABLE” superseded by that location. The 3 '
         'work-list rows resolve to 2 sentences on one line: the three terminals the corpus numbered as RH routes are no route to σ = 1/2, '
         'Route 3 formalizing RH ⇒ RH (ch_iff_rh), and the reduction composes under the open premise in its Weil form, equivalent to RH '
         '(h2_sign_iff_rh). The E-Difficulty cross-link verdict, located by name at OPEN_TRAILS :773 and held whole at the archived landing '
         ':8839-:8847, is credited beneath F-7, the claim it corrects. Two ceiling corrections (F-7’s scope named; the end-to-end parenthesis '
         'of §XII), three stem corrections (one a §XIII text cell) and one fact correction (the deposit pin, by REGISTRY :962), each as the '
         'author answered. No sentence is removed and none held.' % (ED, CUR), '',
         '**The counts.** v8.2 %d sentences; v8.3 %d (the body %d, the back matter %d); the body differs by %+d against the final bound, %d.'
         % (E['n_cur'], E['n_full'], E['n_body'], E['n_backmatter'], H['body_dn'], H['allowed']), '',
         '**H28a %s · H28b %s · H28c %s.** The scanner reads the edition %s.' % (H['H28a'], H['H28b'], H['H28c'], 'CLEAN' if H['clean'] else 'NOT CLEAN'), '',
         '**The record lines and the canon** (`(R198)`(1)-(2)): b587’s weight (FINDINGS :%d); the census / totality pair appended to '
         '`%s` as its §XX (:%d), %d words, the navigator’s draft, struck if the author words it at the closing, with the four instance lines '
         'cited (:%d).' % (C1['lines']['weight'], CANON, C1['lines']['canon_head'], C1['pair_words'], C1['lines']['canon_inst']), '',
         '**A predicate of b454, read again.** b454’s first shape for this verdict wanted the lower-case words “cross-link” and the ledger '
         'writes “CROSS-LINK”, so its table at OPEN_TRAILS :6761 reads HELD BY NO LEDGER where the case-insensitive shape finds :773; '
         'the “held by no ledger” rows of that table warrant a case-insensitive re-search at the constellation re-read, as the author answered.', '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R198)`(4): E_DIFFICULTY_THEOREM, which takes a Correspondence table before its edition per the table rule; the '
         'author rules at this closing whether the table is a housekeeping act (b589) with the edition after (b590), or the two in one act.', '',
         '*Nothing deposits; no kernel touched; v8.2, README, REGISTRY, ERRATA and both pages unwritten; nothing here is a statement about RH, '
         'GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R198) ratified.** (1) b587 at its weight. (2) The census / totality pair in THE_METHOD_CANON. (3) The edition of '
             'TECHNE_TOOLKIT by the form over its §XIII table. (4) The act after, E_DIFFICULTY_THEOREM, the author’s choice of shape left open.', '',
             '**Entered:** FINDINGS.md:%d (b587’s weight), :%d (the entry); `%s` :%d (the pair, appended); this record; PLACE-papers `%s` '
             '(created).' % (C1['lines']['weight'], Q.line_of(Q.FIND, TITLE_HEAD), CANON, C1['lines']['canon_head'], ED), '',
             '**Answered before the seal, by the author:** the parenthesis of v8.2 :475 corrected under the ceiling clause; :414’s deposit pin '
             'corrected under the fact clause by REGISTRY :962, the peeled tags printed; the credit beneath :239, with :239’s “is proved” '
             'taking its scope; the three stems corrected to their objects, :516 to the §XIII preamble’s “deficiency”, (N4) scored in its '
             'letter.', '',
             '**b454’s case-sensitive miss:** its first shape for the cross-link verdict wanted lower-case “cross-link”; the verdict is at '
             'OPEN_TRAILS :773 and archive :8839, both written “CROSS-LINK”; the HELD BY NO LEDGER rows of b454’s table (OPEN_TRAILS '
             ':6755-:6766) warrant a case-insensitive re-search at `W-ORD-CONSTELLATION-RERUN` (:12090), as the author answered.', '',
             '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
             % tuple(S[k][0] for k in SCORE_KEYS), '',
             '**Next:** per `(R198)`(4), E_DIFFICULTY_THEOREM, which takes a Correspondence table before its edition per the table rule '
             '(:12086); the author rules at this closing whether the table is written as a housekeeping act (b589) with the edition after '
             '(b590), or the two in one act.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
             'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b588_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE_HEAD), title=TITLE, append=r))
    put_json('b588_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r2))
    print(jl('b588_findings.json')['entry_line'], jl('b588_trail.json')['line'])


def desk():
    S = jl('b588_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b588 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b588_defects.txt').rstrip(NL).split(NL)
    put_txt('b588_desk_notes.txt', L)


def components():
    S, H, C1, fj, tj = (jl('b588_scores.json'), jl('b588_h28.json'), jl('b588_c1_lines.json'), jl('b588_findings.json'), jl('b588_trail.json'))
    L = ['b588 -- THE COMPONENTS, BANKED UNDER (R198).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b587`s closing push-out relay 5d58af69 ; push-b587* branches deleted by name '
         '(data/b588_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : b587`s weight FINDINGS :%d ; the census / totality pair THE_METHOD_CANON :%d (%d words), its instances :%d' % (
             C1['lines']['weight'], C1['lines']['canon_head'], C1['pair_words'], C1['lines']['canon_inst']),
         '### COMPONENT 2 : the edition %s ; 2 sentences rewritten (3 rows), %d ceiling corrections, %d stem corrections, %d fact correction, '
         '1 credit, the version line, 0 removals ; data/b588_edition_TECHNE.txt ; H28a %s H28b %s H28c %s ; N1 %s N2 %s N3 %s N4 %s' % (
             ED, H['n_ceils'], H['n_stems'], H['n_facts'], H['H28a'], H['H28b'], H['H28c'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0]),
         '### COMPONENT 3 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; next: E_DIFFICULTY_THEOREM, the author`s choice of shape open ; N5 %s'
         % (fj['entry_line'], tj['line'], S['N5'][0])]
    put_txt('b588_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b588_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
