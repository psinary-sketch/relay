# -*- coding: utf-8 -*-
"""b587_record.py -- THE ACT'S RECORD TOOL, UNDER (R197). ### ONE SUBCOMMAND PER BANK.

### ### b587: LANE THREE, ACT FIFTEEN -- CP-7 ACT TWELVE, THE EDITION OF EXHAUSTIVENESS_LICENSE; THE TABLE RULE APPLIED; THE
### CONSTELLATION RE-READ ENTERED. Subcommands write only `data/b587_*` unless the docstring names another file. Every bank is written
### through `put_txt` / `put_json` (encode first, then a temp file, then `os.replace`). This act makes no platform call. ### The template
### is b586_record.py.
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
PRE_PP = '6e617c7'
MIRROR_PIN = '192077f'
CUR = 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md'
ED = 'phase1.5/method/EXHAUSTIVENESS_LICENSE_v0_2.md'
ENUM16 = 'phase1.5/method/ENUMERA_v1_6.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
WL = 'data/b558_editions/EXHAUSTIVENESS_LICENSE.txt'
ARCH = 'archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-historical-landings-and-programs.md'

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
    '(a) THE SUITE`S FIRST RUN FAILED G-OFFSET-LINE, G-DIFF-BANKED AND G-COVERAGE-BANKED LIVE: its generator`s blanket rename of '
    'b586`s suite left the diff bank named `b587_edition_ENUMERA.txt`, a file that does not exist, so each arm read an empty bank. The '
    'name was corrected to `b587_edition_LICENSE.txt` and the suite re-run whole -- the standing trap of a blanket rename (rule 19).',
    '(b) BEFORE THE SEAL, TWO EDITS TO THE ACT`S OWN UNSEALED TOOLS WERE ATTEMPTED THROUGH A SHELL HEREDOC, WHICH COLLAPSED THEIR BACKSLASHES: '
    'each refused on its own assertion before writing, and both were redone with the Edit tool -- the standing heredoc trap.',
]


def defects():
    put_txt('b587_defects.txt', ['### b587 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay the EXHAUSTIVENESS_LICENSE work-list, whole', RELAY, 'HEAD', WL, list(range(1, 27))),
    ('PLACE-papers EXHAUSTIVENESS_LICENSE, whole', PP, PRE_PP, CUR, list(range(1, 159))),
    ('PLACE-papers the zeta page at the mirror`s pin, its pin line and node 8', PP, MIRROR_PIN, PAGE, [3, 12]),
    ('PLACE-papers OPEN_TRAILS, b454`s ledger table row for the S2 Ostrowski seal and its count line', PP, PRE_PP, 'OPEN_TRAILS.md', [6754, 6755, 6763, 6766]),
    ('PLACE-papers the archived ledger line b454 found', PP, PRE_PP, ARCH, [8808]),
    ('relay b540`s tier reading of Route 1', RELAY, 'HEAD', 'data/b540_tiers.json', [104, 437]),
    ('relay b541`s census sentence on Route 1', RELAY, 'HEAD', 'data/b541_census.json', [3241]),
    ('PLACE-papers OPEN_TRAILS, the form, its clauses, the name exception and lane three`s order', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11417, 11864, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 12044, 12062, 12064]),
    ('PLACE-papers FINDINGS, b586`s entry', PP, PRE_PP, 'FINDINGS.md', [6650]),
    ('PLACE-papers ENUMERA v1.6, its Names excepted section', PP, PRE_PP, ENUM16, list(range(1095, 1110))),
    ('relay b586`s closing push-out, its head', RELAY, 'HEAD', 'data/b586_closing_push_out.txt', list(range(1, 4))),
]
SEARCH = 'S2 Ostrowski seal'


def reads():
    L = ['b587 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    L.append('### THE S2 SEAL, SEARCHED BY NAME ("%s") in PLACE-papers FINDINGS.md and OPEN_TRAILS.md at %s:' % (SEARCH, PRE_PP))
    for f in ('FINDINGS.md', 'OPEN_TRAILS.md'):
        sl = g(PP, 'show', '%s:%s' % (PRE_PP, f)).split(NL)
        hits = [i for i, l in enumerate(sl, 1) if SEARCH in l]
        L.append('    %s : %d hit(s) %s' % (f, len(hits), [':%d' % i for i in hits]))
        for i in hits:
            L.append('      :%d %s' % (i, sl[i - 1][:220]))
    L.append('### THE TWO BRANCHES AT THEIR REMOTES (fast-forwarded; no merge commit on the ancestry path):')
    for repo, br, tip in (('SIDE-lv-conservation', 'word-pairing-interface', '5a14205'), ('SIDE-effects', 'w-ladder-skeleton', 'a0dc376')):
        p = 'D:/' + repo
        rem = [l.split('\t') for l in g(p, 'ls-remote', 'origin', 'refs/heads/' + br, 'refs/heads/main').split(NL) if l.strip()]
        anc = subprocess.run(['git', '-C', p, 'merge-base', '--is-ancestor', tip, 'main']).returncode == 0
        merges = [x for x in g(p, 'rev-list', '--merges', '--ancestry-path', '%s..main' % tip).split(NL) if x.strip()]
        L.append('    %s %s : remote %s ; tip %s an ancestor of main %s ; merge commits on the path %d ; "%s"' % (
            repo, br, ['%s %s' % (s[:8], r) for s, r in rem], tip, 'yes' if anc else '### NO', len(merges), g(p, 'log', '-1', '--pretty=%s', tip).strip()[:80]))
    L.append('### the explicit-formula tag the edition cites:')
    loc = g('D:/SIDE-explicit-formula', 'rev-parse', 'v0.2^{}').strip()
    rem = [l.split('\t')[0] for l in g('D:/SIDE-explicit-formula', 'ls-remote', 'origin', 'refs/tags/v0.2^{}').split(NL) if l.strip()]
    L.append('    SIDE-explicit-formula v0.2 : cited 5c72cad ; local %s ; remote %s ; %s' % (loc[:7], (rem[0] if rem else '')[:7],
                                                                                           'AGREE' if loc.startswith('5c72cad') and rem and rem[0].startswith('5c72cad') else '### DIFFER'))
    put_txt('b587_reads.txt', L)


# ================================================================================ COMPONENT 1 -- THE RECORD LINES
B586_ENTRY = '## CP-7, act eleven: the edition of ENUMERA'
NAME_HEAD = '*Appended 2026-10-01 by b580, under the author’s answer before b580’s seal, to the form of an edition (:11864)'
LANE_ORDER = '*Appended 2026-10-01 by b586 to the critical path’s lane three (:11417)'
CR_HEAD = '*Appended 2026-10-01 by b587, under the author’s ruling `(R197)`(2), to the Names excepted rows above:*'
CR_TEXT = ('the seven names excepted there are the item names of the cited document, CRITICAL RESOLVE, as that document numbers them; they '
           'are renamed at that document’s own edition, if it has one.')
CON_HEAD = ('### `W-ORD-CONSTELLATION-RERUN` -- CONSTELLATION MODE OVER THE ROSTER TABLES AT THE CURRENT PINS, PRICED, NOT STARTED, appended '
            '2026-10-01, b587, under the author’s ruling (R197)(4)')
CON_LINES = [
    '**Items.** Constellation mode over the 19 roster tables of relay `data/b586_corroboration.txt` (its list of documents whose tables no '
    'constellation-mode run has re-read since b566) at the current pins -- SIDE-explicit-formula v0.15, lv v0.11.0, the others as REGISTRY '
    'states them; a rowgen diff per table; every moved cell printed and superseded in the table’s own form.',
    '**Reason.** The census found no roster table re-read since the kernel’s toolchain move, and the editions written since cite the pins the '
    'pages print, so the re-read closes the loop between page and table.',
    '**Price:** one act. **Trigger:** before CP-8, or the author’s word sooner.',
]
TABLE_LINES = [
    'TECHNE_TOOLKIT’s edition is written over its §XIII Correspondence table, the act after b587 per `(R197)`(6).',
    'E_DIFFICULTY_THEOREM takes a Correspondence table before its edition, written from its tier block’s terminals (its :236) by the house form '
    'in one housekeeping act, on the author’s word at that closing.',
    'ENUMERA, edited at b586 over its tier block without a table, is recorded as such, and its table is written the same way after CP-7 if the '
    'author so rules; THE_KEYSTONE_CENSUS is the census and takes none.',
]


def c1_lines():
    """### PLACE-papers FINDINGS (b586's weight) and OPEN_TRAILS (the name exception extended; the table rule's three lines; the work-order)."""
    Q = _Q()
    entry, name, order = Q.line_of(Q.FIND, B586_ENTRY), Q.line_of(Q.OT, NAME_HEAD), Q.line_of(Q.OT, LANE_ORDER)
    if not (entry == 6650 and name == 11934 and order == 12062):
        sys.exit('### THE ADDRESSED LINES MOVED: entry %s name %s order %s -- NOTHING WRITTEN' % (entry, name, order))
    heads = dict(
        weight='*Appended 2026-10-01 by b587 to b586’s entry (:%d), under `(R197)`(1) -- b586 AT ITS WEIGHT:*' % entry,
        name='*Appended 2026-10-01 by b587 to the name-and-title exception (:%d), under the author’s ruling `(R197)`(2) -- AN ITEM NAME OF A CITED PROGRAMME DOCUMENT:*' % name,
        table1='*Appended 2026-10-01 by b587 to lane three’s refined order (:%d), under the author’s ruling `(R197)`(3) -- THE TABLE RULE, TECHNE_TOOLKIT:*' % order,
        table2='*Appended 2026-10-01 by b587 to lane three’s refined order (:%d), under the author’s ruling `(R197)`(3) -- THE TABLE RULE, E_DIFFICULTY_THEOREM:*' % order,
        table3='*Appended 2026-10-01 by b587 to lane three’s refined order (:%d), under the author’s ruling `(R197)`(3) -- THE TABLE RULE, ENUMERA AND THE CENSUS:*' % order,
    )
    for k, h in heads.items():
        Q.guard_absent(Q.FIND if k == 'weight' else Q.OT, h)
    Q.guard_absent(Q.OT, CON_HEAD)
    out = [Q.append_to(Q.FIND, '\n%s `phase1.5/method/ENUMERA_v1_6.md` beside v1.5 unedited: 9 rows rewritten citing pinned declarations or '
                                 'bank lines; 8 ceiling corrections (:73 added under the answer’s principle, :895 not :896) and 6 carried; 6 '
                                 'stem corrections and the CR item labels excepted; no fact correction, the formation count (2, 3, 2, 0) = 7 '
                                 'agreeing with SIDE-kernel v1.5; H28a, H28b (+1 against 1) and H28c held, the scanner reading the edition '
                                 'CLEAN. `tools/banned_terms.py` (relay 3746a2a0) reads an edition’s back matter; INDEX v0.19 and AMC v0.2.4 '
                                 'read CLEAN, the mutant NOT CLEAN. The corroboration census banked: no table names a terminal in '
                                 'E_DIFFICULTY_THEOREM, ENUMERA or THE_KEYSTONE_CENSUS, TECHNE_TOOLKIT carries one at §XIII, and no roster '
                                 'table has been re-read by constellation mode since b566. (N2) refuted on its no-table half as the seat '
                                 'scored it. The suite reads 73 of 73.\n' % heads['weight'])]
    out.append(Q.append_to(Q.OT, '\n%s the exception gains the clause “an item name of a cited programme document”: such a name carries '
                                 'unchanged in an edition that cites the document, listed in the back matter with one line saying the name is '
                                 'that document’s and is renamed at its own edition if it has one. Applied at b586 to ENUMERA v1.6’s seven CR '
                                 'item names (their line appended at b587).\n' % heads['name']))
    for k, t in zip(('table1', 'table2', 'table3'), TABLE_LINES):
        out.append(Q.append_to(Q.OT, '\n%s %s\n' % (heads[k], t)))
    out.append(Q.append_to(Q.OT, '\n' + NL.join([CON_HEAD, ''] + [x + NL for x in CON_LINES]).rstrip(NL) + '\n'))
    lines = {k: Q.line_of(Q.FIND if k == 'weight' else Q.OT, h) for k, h in heads.items()}
    lines['constellation'] = Q.line_of(Q.OT, CON_HEAD)
    put_json('b587_c1_lines.json', dict(entry=entry, name=name, order=order, lines=lines, heads=heads, appends=out))
    print(lines)


def enumera_line():
    """### PLACE-papers ENUMERA_v1_6.md: one dated line appended at its end, (R197)(2); committed alone as housekeeping by the seat."""
    p = os.path.join(PP, *ENUM16.split('/'))
    b = open(p, 'rb').read()
    head = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + ENUM16], capture_output=True).stdout
    if b != head:
        sys.exit('### ENUMERA v1.6 DIFFERS FROM ITS HEAD BLOB -- NOTHING WRITTEN')
    if CR_HEAD.encode('utf-8') in b:
        sys.exit('### THE LINE IS ALREADY THERE -- NOTHING WRITTEN')
    import banned_terms as BT
    text = '%s %s' % (CR_HEAD, CR_TEXT)
    if BT.PAT.search(text):
        sys.exit('### A BANNED STEM IN THE LINE -- NOTHING WRITTEN')
    nb = b + ('\n' + text + '\n').encode('utf-8')
    open(p + '.tmp', 'wb').write(nb)
    os.replace(p + '.tmp', p)
    put_json('b587_enumera_line.json', dict(path=ENUM16, before=len(b), after=len(nb), head_blob=g(PP, 'rev-parse', 'HEAD:' + ENUM16).strip(),
                                           line=nb.decode('utf-8').count('\n'), text=text))


# ================================================================================ COMPONENT 2 -- THE EDITION
EF = 'SIDE-explicit-formula'
PIN = {'h2_sign_iff_rh': 'v0.2 = `5c72cad`'}
NS = {'h2_sign_iff_rh': 'B321'}
WHERE = {'h2_sign_iff_rh': 'the zeta page, node 8, line 12'}
H2 = '`h2_sign_iff_rh`, %s %s' % (EF, PIN['h2_sign_iff_rh'])

REWRITES = [
    (13, 'under the one open premise `h2` (monograph §27.3).',
     'under the one open premise `h2` (monograph §27.3), in its Weil form `h2_sign` equivalent to RH (%s), so that the premise is RH itself.' % H2),
    (59, '**The Riemann Hypothesis — THEOREM, conditional on `h2`.**',
     '**The Riemann Hypothesis — THEOREM, conditional on `h2`, in its Weil form `h2_sign` equivalent to RH (%s).**' % H2),
    (59, 'So RH\'s license reads **THEOREM at each stage of the count, conditional on `h2` for the totality**.',
     'So RH\'s license reads **THEOREM at each stage of the count, conditional on `h2` for the totality** -- and `h2` in its Weil form '
     '`h2_sign` is equivalent to RH (%s), so the totality’s condition is RH itself.' % H2),
    (116, '*The `h2`-conditionality of RH\'s grade is stated at §4 and is unchanged from the corpus\'s standing scope.',
     '*The `h2`-conditionality of RH\'s grade is stated at §4 and is unchanged from the corpus\'s standing scope, `h2` in its Weil form '
     '`h2_sign` being equivalent to RH (%s).' % H2),
]
MERGES = [
    (95, 'merged branch `word-pairing-interface`;', 'merged branch `word-pairing-interface` (fast-forwarded into main; tip `5a14205`);'),
    (101, 'MERGED from branch `w-ladder-skeleton`,', 'MERGED from branch `w-ladder-skeleton` (fast-forwarded into main; tip `a0dc376`),'),
    (112, 'MERGED — fast-forwarded into main, nothing deposited', 'MERGED — fast-forwarded into main; tip `a0dc376`, nothing deposited'),
]
MERGE_PRIOR = {95: 'held branch `word-pairing-interface`', 101: 'HELD on branch `w-ladder-skeleton`, SIDE-effects; main untouched',
               112: 'HELD — nothing merged, nothing deposited'}
CEIL_RECORD = 'ceiling correction record:'
CARRY_RECORD = 'ceiling read, carried:'
CEILS = [
    (59, 'The seven-class mechanism catalogue\'s completeness rests on classification theorems at every stage of the formation count (2+3+2+0):',
     'The seven-class mechanism catalogue\'s per-stage counts rest on classification theorems at every stage of the formation count (2+3+2+0), '
     'its completeness at the ξ interface being the open premise `h2`, as below:'),
]
CARRIED = {
    13: 'a definition: “the certificate that the catalogue is complete” names the object the license grades, not a claim that it holds',
    35: 'a grade defined: the SEARCH grade’s “complete as far as it has been searched”, not a claim of completeness',
    59: 'the totality named: “that the seven-stage catalogue is complete at the ξ interface” is stated as the open premise `h2`',
    149: 'the tier block quoting :108`s claim cell (b557), carried with the block',
    61:'a stage described: the zero-interface count (n₄ = 0) rests on Tate`s classification, one stage of the formation count, not the totality',
    108: 'a terminal`s computed grade: `RH_grade` returns THEOREM by `rfl` from the per-stage evidence, the row`s own reading',
    134: 'a ledger line quoted: b454`s era annotation quotes the archived seal verbatim; the credit beneath :59 says what its terminal states',
}
CREDIT = (59, '*Credit (b450 item, located at b587): the `S2` Ostrowski seal -- located by name at OPEN_TRAILS :6763 (b454’s ledger table, '
              'FOUND), first held at `%s` :8808 -- names `structural_exhaustiveness_proved` (SIDE-kernel v1.5 = `0e5233f`), the conjunction '
              'whose place-count conjunct is `ostrowski_exhaustive_prime` (relay `data/b541_census.json` :3241), T2 by relay '
              '`data/b540_tiers.json` :437, while the exhaustiveness at the ξ interface is the open premise `h2` -- the census and '
              'exhaustiveness pair; b454’s era annotation below carries unchanged.*' % ARCH)
STEMS = []
NAMES = []
FACTS = []
VERSION = (9, '*v0.2 — 2026-10-01 (CP-7 edition, b587; v0.1 beside it, unedited)*')
CEILING = re.compile(r'completeness rests on classification theorems|exhaustiveness rests on a proved classification|RH=THEOREM|'
                     r'Ostrowski `COMPILED`|catalogue is (?:exhaustive|complete)\b|RH proved|RH is proved|proof of RH|proves RH|RH proof')
BM_TAG = '<!-- b587 (R197) THE v0.2 EDITION`S BACK MATTER, 2026-10-01 -->'
BANKROWS = (('b541_census.json', 3241), ('b540_tiers.json', 437))
COMMITS = (('SIDE-lv-conservation', '5a14205'), ('SIDE-effects', 'a0dc376'))
READING_NAME = {0: 'none -- resolved by the form', 1: '(d) h2 takes h2_sign'}
OFFSET = ('+2 from :9 (the v0.2 line and a blank, above the v0.1 line); +2 more from :60 (a blank and the credit line, beneath :59) -- '
          'v0.1 :n sits at the edition`s :n+2 for 9 <= n <= 59 and at :n+4 for n >= 60')


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _rows():
    return [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'LIC' and r['verdict'] == 'MOVED-IN-MEANING']


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    return n + (2 if n >= VERSION[0] else 0) + (2 if n > CREDIT[0] else 0)


def _all_changes():
    return REWRITES + MERGES + CEILS + STEMS + FACTS


def edition(*a):
    """### PLACE-papers phase1.5/method/EXHAUSTIVENESS_LICENSE_v0_2.md, beside the current version from its blob at 6e617c7; the re-pin step last."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE 6e617c7 -- NOTHING WRITTEN')
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
    if not cur[VERSION[0] - 1].startswith('*v0.1 — 2026-07-25'):
        sys.exit('### THE VERSION ANCHOR IS NOT WHERE THE FACE SAYS')
    if len(_segs(CREDIT[1])) != 1:
        sys.exit('### THE CREDIT LINE IS NOT ONE SENTENCE (%d)' % len(_segs(CREDIT[1])))
    diff = []
    for r in _rows():
        ln = r['line']
        k = _segs(cur[ln - 1]).index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d] in nw]
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         reading=1, cites=cites, banks=[], supports=r['reading']))
    new[CREDIT[0]:CREDIT[0]] = ['', CREDIT[1]]
    new[VERSION[0] - 1:VERSION[0] - 1] = [VERSION[1], '']
    body = list(new)
    changed = set(x[0] for x in _all_changes())
    if any(_edl(n) > len(body) or (n not in changed and body[_edl(n) - 1] != cur[n - 1]) for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL DOES NOT CARRY THE CURRENT VERSION')
    if body[_edl(CREDIT[0]) + 1] != CREDIT[1] or body[_edl(CREDIT[0])] != '':
        sys.exit('### THE CREDIT IS NOT BENEATH :59')
    inv = {_edl(n): n for n in range(1, len(cur) + 1)}
    hits = [(i, m.group(0)) for i, l in enumerate(body, 1) for m in CEILING.finditer(l)]
    stray = sorted(set(inv.get(i, -i) for i, _ in hits) - set(CARRIED))
    if stray:
        sys.exit('### A CEILING HIT IN THE BODY IS NEITHER CORRECTED NOR CARRIED BY THE SEAT`S READ: current lines %s' % stray)
    bm = ['', BM_TAG, '',
          '## Back matter of the v0.2 edition -- written 2026-10-01 by b587 under the author’s ruling `(R197)`(5), by the form of `(R187)`(5)', '',
          '*This file is v0.2 of EXHAUSTIVENESS_LICENSE, the CP-7 edition written beside v0.1 (`%s`, unedited) from v0.1’s tier block (its :140, '
          'standing: 6 rows, every terminal T2, one T2-INTERFACES) and its CP-1b work-list (relay `%s`), the ζ page as its spine; it does not '
          'deposit and does not replace v0.1, and its promotion is CP-8’s. Every line cited below is this file’s own.*' % (CUR, WL), '',
          '### Removals', '', 'None: every one of the 4 work-list rows resolves to a sentence rewritten in place to what its compiled fact says.', '',
          '### Credit lines', '', '| this edition’s line | the item | Status |', '|:--|:--|:--|',
          '| :%d | the `S2` Ostrowski seal (b450, relay `data/b450_batch.json`), located by name at OPEN_TRAILS :6763 | inserted beneath :%d, '
          'the author’s answer before b587’s seal |' % (_edl(CREDIT[0]) + 2, _edl(CREDIT[0])), '',
          '### The merged state, cited', '',
          'b454’s currency annotation (2026-09-14, this file’s :%d-:%d) rewrote the three lines to the merged state before this edition; there is '
          'no merge commit, both branches having been fast-forwarded, and each line now cites its fast-forward tip, the author’s answer before '
          'b587’s seal (`(R197)`(5)’s “merge commit” recorded as the navigator’s).' % (_edl(118), _edl(128)), '',
          '| this edition’s line | the state before b454 | the state at v0.1 | v0.2 | Status |', '|:--|:--|:--|:--|:--|']
    for ln, old, rep in MERGES:
        bm.append('| :%d | %s | %s | %s | the tip cited, an ancestor of main with no merge commit on the path (relay `data/b587_reads.txt`) |' % (
            _edl(ln), MERGE_PRIOR[ln], old, rep))
    bm += ['', '### Ceiling corrections', '', '| this edition’s line | v0.1 wording | v0.2 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in CEILS:
        bm.append('| :%d | %s %s | %s | corrected under the ceiling clause, the census and exhaustiveness pair of `(R196)` |' % (_edl(ln), CEIL_RECORD, old, rep))
    bm += ['', '### Ceiling-shaped sentences read and carried', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(CARRIED):
        bm.append('| :%d | %s %s | carried as read |' % (_edl(ln), CARRY_RECORD, CARRIED[ln]))
    bm += ['', '### Stem corrections', '', 'None: the scanner finds no use of a banned stem in v0.1.', '',
           '### Fact corrections', '', 'None: the formation count (2+3+2+0) and the pins the document prints (SIDE-kernel v1.5 = `0e5233f`) agree '
           'with the federation; the dated version line at :%d (“kernel skeleton HELD on branch, main untouched”) carries as a dated record '
           'under the history clause.' % _edl(9), '',
           '### The navigator’s expectations of `(R197)`(5)', '', '| expectation | the read | Status |', '|:--|:--|:--|',
           '| the `S2` Ostrowski seal located by name and inserted as a credit | located at OPEN_TRAILS :6763 | credited |',
           '| the three superseded-form lines rewritten to the merged state, citing the merge commit | merged since b454; no merge commit | the fast-forward tips cited |',
           '| the census and exhaustiveness pair wherever exhaustiveness is asserted as proved | :%d | corrected |' % _edl(59),
           '| sentences naming h2 take `h2_sign` where the work-list marks them | 4 rows | rewritten |',
           '', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v0.2 | `%s` | written at b587 |' % ED,
           '| the current version, v0.1 | `%s` | unedited |' % CUR,
           '| the spine | `%s` at PLACE-papers `%s` | read, unedited |' % (PAGE, MIRROR_PIN),
           '| the work-list | relay `%s` | read |' % WL,
           '| the sentence-by-sentence diff | relay `data/b587_edition_LICENSE.txt` | banked at b587 |',
           '', '### Correspondence', '',
           '| declaration, commit or bank line | repository | pin | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    ed_lines = {d: [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l and PIN[d] in l] for d in PIN}
    for d in PIN:
        bm.append('| `SIDEExplicitFormula.%s.%s` | %s | %s | %s | cited at :%s of this edition |' % (
            NS[d], d, EF, PIN[d].replace('`', ''), WHERE[d], ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    commit_lines = {}
    for repo, sha in COMMITS:
        at = [i for i, l in enumerate(body, 1) if ('tip `%s`' % sha) in l]
        commit_lines[sha] = at
        bm.append('| commit `%s` | %s | the fast-forward tip | not on the page | cited at :%s of this edition |' % (
            sha, repo, ', :'.join(str(x) for x in at) or '### NONE'))
    bank_lines = {}
    for bank, n in BANKROWS:
        at = [i for i, l in enumerate(body, 1) if ('relay `data/%s` :%d' % (bank, n)) in l]
        bank_lines['%s:%d' % (bank, n)] = at
        bm.append('| `data/%s` :%d | relay | the tier law`s read of Route 1 | not on the page | cited at :%s of this edition |' % (
            bank, n, ', :'.join(str(x) for x in at) or '### NONE'))
    bm.append('')
    if any('### NONE' in l for l in bm):
        sys.exit('### A CORRESPONDENCE ROW CITES NO LINE OF THE EDITION')
    full = body + bm
    b = (NL.join(full) + NL).encode('utf-8')
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    put_json('b587_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=1, removals=0, ruled_citations=0, version_lines=1, diff=diff, offset=OFFSET,
                                       ceils=CEILS, merges=MERGES, stems=STEMS, facts=FACTS, credit_line=dict(after=CREDIT[0], at=_edl(CREDIT[0]) + 2, text=CREDIT[1]),
                                       carried={str(k): v for k, v in CARRIED.items()}, version=dict(above=VERSION[0], text=VERSION[1]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines,
                                       commit_lines=commit_lines, bank_lines=bank_lines))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))


def edition_bank():
    """### The diff with its offset line, the corrections, the counts, the ceiling read, the scanner's verdict, H28a-H28c."""
    E = jl('b587_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(BM_TAG)
    scan = rd('b587_edition_termscan.txt')
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
    live_n = int(live.group(1)) if live else None
    h28c = 'HELD' if (live_n == 0 and clean and not beyond) else 'REFUTED'
    cur0 = _cur()
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % OFFSET, '',
         'b587 -- COMPONENT 2: THE EDITION OF EXHAUSTIVENESS_LICENSE, (R197)(5), BY THE FORM OF (R187)(5) AND ITS CLAUSES', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :9 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0], cur0[8]),
         '### its tier block : :140 "%s"' % cur0[139][:110],
         '### its version history : the one version line :9 (v0.1); b454`s annotations :118-:136; b557`s tier block :138-:156; b558`s line :158',
         '### the S2 seal searched by name (relay data/b587_reads.txt): OPEN_TRAILS :6763 -- LOCATED',
         '### the two fast-forward tips: SIDE-lv-conservation word-pairing-interface `5a14205`; SIDE-effects w-ladder-skeleton `a0dc376`',
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE WORK-LIST, ROW BY ROW (4 rows, 4 sentences, 3 lines):', '']
    for d in E['diff']:
        L += ['  %s v0.1 :%d -> v0.2 :%d `%s` -- %s ; cites %s' % (d['id'], d['line'], d['ed_line'], d['terminal'], READING_NAME[d['reading']],
                                                               ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']]),
              '      work-list: %s' % d['supports'], '      v0.1 : %s' % d['old'], '      v0.2 : %s' % d['new'], '']
    cov = [d for d in E['diff'] if d['reading']]
    L += ['### COVERAGE BY THE EXPECTATIONS OF (R197)(5), the seat`s hand-read: %d of %d rows -- (d) %d' % (len(cov), len(E['diff']), len(cov)), '',
          '### THE CREDIT LINE (the author`s answer): v0.2 :%d, beneath v0.1 :59' % E['credit_line']['at'], '      %s' % E['credit_line']['text'], '',
          '### THE MERGED STATE CITED (the author`s answer; the three superseded-form lines):']
    L += ['    v0.1 :%d -> v0.2 :%d  "%s" -> "%s"' % (m[0], _edl(m[0]), m[1], m[2]) for m in E['merges']]
    L += ['### THE CEILING CORRECTIONS (%d), the census and exhaustiveness pair:' % len(E['ceils'])]
    L += ['    v0.1 :%d -> v0.2 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in E['ceils']]
    L += ['### THE CEILING-SHAPED SENTENCES READ AND CARRIED:'] + ['    v0.1 :%d -> v0.2 :%d  %s' % (n, _edl(n), CARRIED[n]) for n in sorted(CARRIED)]
    L += ['### THE STEM CORRECTIONS: none. ### THE FACT CORRECTIONS: none. ### REMOVALS: none.',
          '### THE VERSION LINE: above v0.1 :%d: %s' % (E['version']['above'], E['version']['text']), '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d) ; the back '
          'matter %d ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d + one version line = %d' % (
              body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], {'record': 'quoted in a back-matter record, read by the seat',
                                                                 'carried': 'in a sentence the seat read and carried',
                                                                 'beyond': '### BEYOND THE CEILING'}[h['kind']], h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### THE SCANNER (banned_terms.py) on the edition: live uses %s ; verdict %s' % (live_n, 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on the page at its pin%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s live count %s and verdict %s; sentences beyond the ceiling %d.**' % (
              h28c, live_n, 'CLEAN' if clean else 'NOT CLEAN', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b587_edition_LICENSE.txt', L)
    put_json('b587_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=live_n, clean=clean, beyond=len(beyond), hits=hits,
                                   covered=len(cov), held=None, n_ceils=len(E['ceils']), n_merges=len(E['merges']), n_facts=len(E['facts'])))
    H = jl('b587_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'covered', H['covered'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'],
          'live', H['live'], 'ceils', H['n_ceils'])


# ================================================================================ THE SCORING AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}


def scores():
    H, E = jl('b587_h28.json'), jl('b587_edition.json')
    reads_ = rd('b587_reads.txt')
    ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD') + NL +
                                g(PP, 'ls-files', '--others', '--exclude-standard', 'phase1.5', 'phase2')).split(NL) if x.strip()))
    kmain = g('D:/SIDE-explicit-formula', 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    cur_same = g(PP, 'hash-object', CUR).strip() == E['cur_blob']
    located = re.search(r'OPEN_TRAILS\.md : (\d+) hit\(s\)', reads_)
    n1 = located is not None and int(located.group(1)) >= 1
    ed = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read().split(NL)
    cur = _cur()
    keep_moved = [n for n in range(1, len(cur) + 1) if ed[_edl(n) - 1] != cur[n - 1]]
    merge_lines = [m[0] for m in MERGES]
    others = sorted(set(keep_moved) - set(merge_lines))
    # ### (N2) read on its own object: each of the three lines differs from v0.1 by its inserted tip alone (the face's reading)
    n2 = all(('tip `%s`' % sha) in ed[_edl(ln) - 1] and ed[_edl(ln) - 1].replace(rep, old) == cur[ln - 1]
             for (ln, old, rep), sha in zip(MERGES, ('5a14205', 'a0dc376', 'a0dc376')))
    n3 = H['H28a'] == 'HELD' and H['H28b'] == 'HELD' and H['H28c'] == 'HELD' and H['held'] is None
    allowed_pp = {'FINDINGS.md', 'OPEN_TRAILS.md', ED, ENUM16}
    S = dict(
        N1=('HELD' if n1 else 'REFUTED', 'the seal searched by name: OPEN_TRAILS :6763 (b454`s ledger table, FOUND) ; FINDINGS no hit'),
        N2=('HELD' if n2 and set(others) == {13, 59, 116} else 'REFUTED', 'the three lines cite their fast-forward tips (merged since b454; '
            'no merge commit), each differing from v0.1 by its tip alone ; the other lines moved %s are the work-list rows and the ceiling '
            'correction, which the form orders' % others),
        N3=('HELD' if n3 else 'REFUTED', 'H28a %s, H28b %s (the body %+d against at most %d), H28c %s; no sentence held' % (
            H['H28a'], H['H28b'], H['body_dn'], H['allowed'], H['H28c'])),
        N4=('HELD' if H['n_ceils'] <= 4 and H['n_ceils'] >= 1 else 'REFUTED', 'the ceiling clause corrects %d, the census and exhaustiveness pair at :59' % H['n_ceils']),
        N5=('HELD' if (kmain == V015 and heads_ok and cur_same and set(ch) <= allowed_pp) else 'REFUTED', 'nothing deposits; no kernel touched '
            '(%s); the current version unedited (%s); PLACE-papers changed at %s -- ENUMERA v1.6`s appended line the ruling`s, not the ferry`s' % (
                'held' if kmain == V015 and heads_ok else '### MOVED', 'held' if cur_same else '### EDITED', ch)),
        S1=('HELD' if n1 else 'REFUTED', '(N1) holds at OPEN_TRAILS :6763'),
        S2=('HELD' if n2 else 'REFUTED', '(N2) holds as the face reads it: the merged state was b454`s, and the citation is the tip'),
        S3=('HELD' if n3 and H['body_dn'] == 2 and H['allowed'] == 2 else 'REFUTED', 'H28a-H28c held; the body +2 against 2'),
        S4=('HELD' if H['n_ceils'] == 1 else 'REFUTED', '(N4) holds at 1'),
        S5=('HELD' if set(ch) == allowed_pp else 'REFUTED', 'the PLACE-papers files changed are the four named on the face'),
        counts=dict(pp_changed=ch, body_dn=H['body_dn'], ceils=H['n_ceils'], others=others),
    )
    put_json('b587_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], S[k][1][:170]))


TITLE_HEAD = ('## CP-7, act twelve: the edition of EXHAUSTIVENESS_LICENSE from its tier block and work-list, the three superseded forms '
              'citing their fast-forward tips, the S2 seal located')
TITLE = TITLE_HEAD + '; written as v0.2 beside v0.1, no sentence held'
TRAIL_HEAD = ('### b587 — lane three, act fifteen under (R197): CP-7 act twelve -- the edition of EXHAUSTIVENESS_LICENSE written beside the '
              'current; the table rule applied; W-ORD-CONSTELLATION-RERUN entered')


def records_pp():
    Q = _Q()
    S, H, E, C1, EL = jl('b587_scores.json'), jl('b587_h28.json'), jl('b587_edition.json'), jl('b587_c1_lines.json'), jl('b587_enumera_line.json')
    Q.guard_absent(Q.FIND, TITLE_HEAD)
    e = ['', TITLE, '',
         '*Filed at b587 on the author’s ruling `(R197)`. Banks: relay `data/b587_edition_LICENSE.txt` (the sentence-by-sentence diff, its '
         'offset line at its head), `data/b587_edition.json`, `data/b587_reads.txt`. Nothing deposits.*', '',
         '**The edition** (`(R197)`(5)): `%s`, v0.2, written beside v0.1 (`%s`, unedited) from v0.1’s tier block and its CP-1b work-list, the '
         'ζ page as its spine. The 4 work-list rows resolve to 4 sentences on 3 lines, each naming the premise in its Weil form and citing its '
         'equivalence with RH. The census and exhaustiveness pair corrects one phrase at :59: the catalogue’s per-stage counts rest on '
         'classification theorems, its completeness at the ξ interface is the open premise. The `S2` Ostrowski seal, located by name at '
         'OPEN_TRAILS :6763, is credited beneath :59 as what its terminal states, the place-count conjunct, T2. The three superseded-form '
         'lines, merged since b454, each cite their fast-forward tip; there is no merge commit. No sentence is removed and none held.' % (ED, CUR), '',
         '**The counts.** v0.1 %d sentences; v0.2 %d (the body %d, the back matter %d); the body differs by %+d against the final bound, %d.'
         % (E['n_cur'], E['n_full'], E['n_body'], E['n_backmatter'], H['body_dn'], H['allowed']), '',
         '**H28a %s · H28b %s · H28c %s.** The scanner reads the edition %s.' % (H['H28a'], H['H28b'], H['H28c'], 'CLEAN' if H['clean'] else 'NOT CLEAN'), '',
         '**The record lines** (`(R197)`(1)-(4)): b586’s weight (FINDINGS :%d); the name exception extended (OPEN_TRAILS :%d); the table rule '
         '(:%d, :%d, :%d); `W-ORD-CONSTELLATION-RERUN`, priced and not started, trigger before CP-8 or the author’s word sooner (:%d); ENUMERA '
         'v1.6’s line on the CR names appended at its :%d, committed alone as housekeeping.' % (
             C1['lines']['weight'], C1['lines']['name'], C1['lines']['table1'], C1['lines']['table2'], C1['lines']['table3'],
             C1['lines']['constellation'], EL['line']), '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R197)`(6): the edition of TECHNE_TOOLKIT by the same form, over its §XIII table; the author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; v0.1, README, REGISTRY, ERRATA and both pages unwritten; nothing here is a statement about RH, '
         'GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R197) ratified.** (1) b586 at its weight. (2) The CR item names excepted as the cited document’s; the name exception extended. '
             '(3) The table rule applied. (4) `W-ORD-CONSTELLATION-RERUN` entered. (5) The edition of EXHAUSTIVENESS_LICENSE by the form. (6) '
             'The act after.', '',
             '**Entered:** FINDINGS.md:%d (b586’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the name exception), :%d, :%d, :%d (the table '
             'rule), :%d (`W-ORD-CONSTELLATION-RERUN`), this record; PLACE-papers `%s` (created); `%s` :%d (appended, housekeeping).' % (
                 C1['lines']['weight'], Q.line_of(Q.FIND, TITLE_HEAD), C1['lines']['name'], C1['lines']['table1'], C1['lines']['table2'],
                 C1['lines']['table3'], C1['lines']['constellation'], ED, ENUM16, EL['line']), '',
             '**Answered before the seal, by the author:** the three superseded-form lines keep their words and each gains its fast-forward tip '
             '(word-pairing-interface `5a14205`, w-ladder-skeleton `a0dc376`), b454’s rewrite recorded in the back matter as the prior state, '
             '`(R197)`(5)’s “merge commit” recorded as the navigator’s; one credit beneath :59 naming `structural_exhaustiveness_proved` as the '
             'conjunction whose place-count conjunct is `ostrowski_exhaustive_prime`, T2, the exhaustiveness at the ξ interface the open premise '
             '`h2`, b454’s annotation carried unchanged; the line on the CR names appended to ENUMERA v1.6 and committed alone as housekeeping, '
             'its omission from the ferry’s write list recorded as the navigator’s.', '',
             '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
             % tuple(S[k][0] for k in SCORE_KEYS), '',
             '**Next:** per `(R197)`(6), CP-7 act thirteen, b588 -- the edition of TECHNE_TOOLKIT by the same form, over its §XIII table, '
             'H28a-H28c scored; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
             'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b587_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE_HEAD), title=TITLE, append=r))
    put_json('b587_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r2))
    print(jl('b587_findings.json')['entry_line'], jl('b587_trail.json')['line'])


def desk():
    S = jl('b587_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b587 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b587_defects.txt').rstrip(NL).split(NL)
    put_txt('b587_desk_notes.txt', L)


def components():
    S, H, C1, fj, tj, EL = (jl('b587_scores.json'), jl('b587_h28.json'), jl('b587_c1_lines.json'), jl('b587_findings.json'),
                            jl('b587_trail.json'), jl('b587_enumera_line.json'))
    L = ['b587 -- THE COMPONENTS, BANKED UNDER (R197).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b586`s closing push-out relay 7750d0c7 ; push-b586* branches deleted by name '
         '(data/b587_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : b586`s weight FINDINGS :%d ; the name exception OPEN_TRAILS :%d ; the table rule :%d :%d :%d ; '
         'W-ORD-CONSTELLATION-RERUN :%d ; ENUMERA v1.6 :%d (housekeeping)' % (
             C1['lines']['weight'], C1['lines']['name'], C1['lines']['table1'], C1['lines']['table2'], C1['lines']['table3'],
             C1['lines']['constellation'], EL['line']),
         '### COMPONENT 2 : the edition %s ; 4 sentences rewritten, %d ceiling correction, 3 tips cited, 1 credit, the version line, 0 removals ; '
         'data/b587_edition_LICENSE.txt ; H28a %s H28b %s H28c %s ; N1 %s N2 %s N3 %s N4 %s' % (
             ED, H['n_ceils'], H['H28a'], H['H28b'], H['H28c'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0]),
         '### COMPONENT 3 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; next: the edition of TECHNE_TOOLKIT ; N5 %s'
         % (fj['entry_line'], tj['line'], S['N5'][0])]
    put_txt('b587_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b587_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
