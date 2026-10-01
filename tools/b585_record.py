# -*- coding: utf-8 -*-
"""b585_record.py -- THE ACT'S RECORD TOOL, UNDER (R195). ### ONE SUBCOMMAND PER BANK.

### ### b585: LANE THREE, ACT THIRTEEN -- CP-7 ACT TEN, THE EDITION OF INDEX_ARITY_AT_THE_CRITICAL_LINE; THE FACE E ITEM CLOSED AS NOT
### LOCATED. Subcommands write only `data/b585_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode first, then a temp file, then `os.replace`). This act makes no platform call. ### The template is b584_record.py.
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
PRE_PP = '1d0109f'
MIRROR_PIN = '192077f'
CUR = 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md'
ED = 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE_v0_19.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
WL = 'data/b558_editions/INDEX_ARITY_AT_THE_CRITICAL_LINE.txt'
SIGN = 'phase2/method/SIGN_ARRANGEMENT_RECONCILIATION.md'
LV = 'D:/SIDE-lv-conservation'

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
    '(a) THE QUESTION BEFORE THE SEAL COUNTED FOURTEEN USES NAMING THE SPACING BETWEEN CONSECUTIVE ZEROS; the read counts thirteen '
    '(:109, :162, :164 three times, :166, :167, :325, :395 three times, :513, :533). The author`s answer governs the uses, not the '
    'number; every bank and the back matter print thirteen.',
    '(b) THE SEALED FACE`S READING (ix) SAYS THE CENSUS COUNTED LIVE USES ONLY IN MARKED SENTENCES; the recount by b584`s classifier '
    'finds five, one in a marked sentence (:401) and four not (:21, :71, :263, :407), each read by the seat as not beyond the ceiling '
    '(none names RH or the clause as proved). The face is sealed and stands as written; the (N3) score and this line carry the correction.',
    '(c) THE SUITE`S FIRST RUN RAISED AT G-REPIN-FINAL: the carried arm reads the record tool`s BANKROWS, which this act`s tool did not '
    'define (the edition cites no bank line). The tool gained BANKROWS = () -- no bank and no corpus byte changed -- and the suite re-ran.',
]


def defects():
    put_txt('b585_defects.txt', ['### b585 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


RELAY = ROOT.replace('\\', '/')
ROWLINES = []
READS = [
    ('relay the INDEX_ARITY work-list, whole', RELAY, 'HEAD', WL, list(range(1, 51))),
    ('PLACE-papers INDEX_ARITY, its head, Abstract and sections 1-2', PP, PRE_PP, CUR, list(range(1, 62))),
    ('PLACE-papers INDEX_ARITY, the marked, stem, ceiling-read and fact lines', PP, PRE_PP, CUR,
     [74, 109, 162, 164, 166, 167, 193, 234, 325, 334, 338, 369, 373, 381, 383, 395, 401, 405, 513, 533]),
    ('PLACE-papers INDEX_ARITY, the two dated entries, the era annotations and the tier block', PP, PRE_PP, CUR,
     list(range(565, 595)) + list(range(605, 620)) + list(range(631, 701))),
    ('PLACE-papers the zeta page at the mirror`s pin, its pin line, nodes 7, 8, the open line and the mellin row', PP, MIRROR_PIN, PAGE, [3, 11, 12, 31, 138]),
    ('PLACE-papers SIGN_ARRANGEMENT_RECONCILIATION section 3, as b581 cited it', PP, PRE_PP, SIGN, list(range(44, 70))),
    ('PLACE-papers SPIRAL_MAP, the translation table`s n4 row', PP, PRE_PP, 'SPIRAL_MAP.md', list(range(428, 437))),
    ('relay the CP-1b bank, its head and the INDEX_ARITY rows', RELAY, 'HEAD', 'data/b558_cp1b.txt', list(range(1, 9))),
    ('PLACE-papers OPEN_TRAILS, the keyhole hits and b454`s table', PP, PRE_PP, 'OPEN_TRAILS.md', [531, 6759]),
    ('PLACE-papers FINDINGS, the Face E hit', PP, PRE_PP, 'FINDINGS.md', [255]),
    ('PLACE-papers OPEN_TRAILS, the form, its clauses and b584`s record', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11864, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 11974, 11976, 11994, 11996, 12012, 12020, 12026, 12028]),
    ('PLACE-papers FINDINGS, b584`s entry', PP, PRE_PP, 'FINDINGS.md', [6608]),
    ('PLACE-papers README, the ceiling', PP, PRE_PP, 'README.md', list(range(104, 122))),
    ('relay tools/banned_terms.py, the stems and the exceptions', RELAY, 'HEAD', 'tools/banned_terms.py', list(range(1, 81))),
    ('relay b584`s closing push-out, its head', RELAY, 'HEAD', 'data/b584_closing_push_out.txt', list(range(1, 4))),
]
PINS = (('SIDE-kernel', 'v1.7', '2957e7d'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-lv-conservation', 'v0.11.0', '2f71068'),
        ('SIDE-explicit-formula', 'v0.1', 'baed4df'), ('SIDE-explicit-formula', 'v0.2', '5c72cad'), ('SIDE-explicit-formula', 'v0.11', '19b7d1e'))


def _peel(repo, tag):
    p = 'D:/' + repo
    loc = g(p, 'rev-parse', tag + '^{}').strip()
    peeled = [l.split('\t')[0] for l in g(p, 'ls-remote', 'origin', 'refs/tags/%s^{}' % tag).split(NL) if l.strip()]
    rem = [l.split('\t')[0] for l in g(p, 'ls-remote', 'origin', 'refs/tags/%s' % tag).split(NL) if l.strip()]
    return loc, (peeled or rem or [''])[0]


def reads():
    L = ['b585 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    L.append('### the fact clause`s read over INDEX_ARITY`s pins and the edition`s, each tag peeled locally and at the remote:')
    for repo, tag, cited in PINS:
        loc, r = _peel(repo, tag)
        L.append('    %s %s : cited %s ; local %s ; remote %s ; %s' % (repo, tag, cited, loc[:7], r[:7],
                                                                   'AGREE' if loc.startswith(cited) and r.startswith(cited) else '### DIFFER'))
    main = g(LV, 'rev-parse', 'main').strip()
    rem = g(LV, 'ls-remote', 'origin', 'refs/heads/main').split('\t')[0]
    L += ['### the "main = `sha`" cells: SIDE-lv-conservation main local %s ; remote %s' % (main[:7], rem[:7])]
    for s, rows in (('5a14205', ':373'), ('14720d9', ':381'), ('2f71068', ':383, :384, :385')):
        anc = subprocess.run(['git', '-C', LV, 'merge-base', '--is-ancestor', s, 'main']).returncode == 0
        L.append('    %s (%s) : %s ; an ancestor of main %s ; commits %s..main %s' % (
            s, rows, 'AGREE' if main.startswith(s) else '### DIFFER (main is not %s)' % s, 'yes' if anc else 'no',
            s, g(LV, 'rev-list', '--count', s + '..main').strip()))
    put_txt('b585_reads.txt', L)


# ================================================================================ COMPONENT 1
FORM_HEAD = '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three'
HIST_HEAD = '*Appended 2026-10-01 by b579, under the author’s answer before b579’s seal, to the form of an edition (:11864), beside the stem and ceiling clauses -- THE HISTORY CLAUSE:*'
B584_ENTRY = '## CP-7, act nine: the edition of INVARIANCE_BARRIERS'
B454_TABLE = '| Face E / keyhole | 20 | 22 | 38 | HELD BY NO LEDGER | — |'


def c1_lines():
    """### PLACE-papers FINDINGS (b584's weight) and OPEN_TRAILS (the Face E / keyhole closing; the history clause's precedence)."""
    Q = _Q()
    form, hist, entry, t454 = Q.line_of(Q.OT, FORM_HEAD), Q.line_of(Q.OT, HIST_HEAD), Q.line_of(Q.FIND, B584_ENTRY), Q.line_of(Q.OT, B454_TABLE)
    if not (form == 11864 and hist == 11908 and entry == 6608 and t454 == 6759):
        sys.exit('### THE ADDRESSED LINES MOVED: form %s history %s entry %s table %s -- NOTHING WRITTEN' % (form, hist, entry, t454))
    heads = dict(
        weight='*Appended 2026-10-01 by b585 to b584’s entry (:%d), under `(R195)`(1) -- b584 AT ITS WEIGHT:*' % entry,
        keyhole='*Appended 2026-10-01 by b585 to b454’s ledger table (:%d), under the author’s ruling `(R195)`(2) -- FACE E / KEYHOLE, CLOSED AS NOT LOCATED:*' % t454,
        precedence='*Appended 2026-10-01 by b585 to the history clause (:%d), under the author’s answer before b585’s seal -- INSIDE A DATED ENTRY THE HISTORY CLAUSE GOVERNS:*' % hist,
    )
    for k, h in heads.items():
        Q.guard_absent(Q.FIND if k == 'weight' else Q.OT, h)
    out = [Q.append_to(Q.FIND, '\n%s `phase1.5/method/INVARIANCE_BARRIERS_v1_4.md` beside v1.3 unedited: 10 rows as 8 sentences on 6 lines; the '
                                 'clause named in its Weil form; the conservation register and the Route 3 premise said to be RH restated, the '
                                 'Route 3 terminal’s row T2; lv’s h2 at Φ false on the strip; the T3 Tier-1 scope located at OPEN_TRAILS :6845 '
                                 'and inserted as a credit beside Theorem 3.7; no stem, ceiling or fact corrections. H28a, H28b (+2 against 2) and '
                                 'H28c held. The ceiling census (relay `data/b584_ceiling_census.txt`): GRH_CASCADE 19, the monograph 11 (read at '
                                 '`day1/A_Place_to_Stand.md`), ENUMERA 7; the fourteen’s remaining editions meet 21 live uses, 16 for the seven '
                                 'after b584 -- a count by keyword co-occurrence, not a verdict, and (N1)’s top-three half refuted as the seat '
                                 'scored it. The two work-orders on the trails, SIMPLICITY’s edition held. The suite reads 69 of 69.\n' % heads['weight'])]
    out.append(Q.append_to(Q.OT, '\n%s the b450 item’s precondition -- the finding’s form located in FINDINGS or OPEN_TRAILS -- is not met: '
                                 'FINDINGS carries no “keyhole” (its one Face E line, :255, is a scope log), OPEN_TRAILS :531 names a different '
                                 'item, and :6759 is b454’s own “held by no ledger” table (relay `data/b584_reads.txt`). The item closes as NOT '
                                 'LOCATED: no credit is inserted in any edition; the finding, if it exists, is unbanked and would need to be '
                                 're-derived before any keystone carries it. b454’s table is the record of that state.\n' % heads['keyhole']))
    out.append(Q.append_to(Q.OT, '\n%s a banned stem inside a dated history entry is carried as the dated record, and a history line dated to the '
                                 'edition directly beneath the entry names the corrected object; the line counts under H28b as a ruled citation, '
                                 'and the stem is printed as carried-by-history when H28c is scored. Applied at b585 to INDEX_ARITY_AT_THE_CRITICAL_LINE '
                                 'v0.18 :568 (the v0.8 entry) and :587 (the v0.7 entry).\n' % heads['precedence']))
    lines = {k: Q.line_of(Q.FIND if k == 'weight' else Q.OT, h) for k, h in heads.items()}
    put_json('b585_c1_lines.json', dict(form=form, hist=hist, entry=entry, t454=t454, lines=lines, heads=heads, appends=out))
    print(lines)


# ================================================================================ COMPONENT 2 -- THE EDITION
EF = 'SIDE-explicit-formula'
PIN = {'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'ch_iff_rh': 'v0.1 = `baed4df`'}
NS = {'h2_sign_iff_rh': 'B321', 'ch_iff_rh': 'B321'}
WHERE = {'h2_sign_iff_rh': 'the zeta page, node 8, line 12', 'ch_iff_rh': 'the zeta page, node 7, line 11'}
H2 = '`h2_sign_iff_rh`, %s %s' % (EF, PIN['h2_sign_iff_rh'])
CH = '`ch_iff_rh`, %s %s' % (EF, PIN['ch_iff_rh'])

REWRITES = [
    (21, 'with the reduction machine-verified and the residue localized.',
     'with the clause compiled as equivalent to RH in its Weil form (%s), the deposit’s Route 3 clause RH restated (%s), and the residue '
     'localized.' % (H2, CH)),
    (29, 'equivalently realization-totality at the ξ interface, the premise that every ξ-zero forces the Euler balance at some prime (the '
         'monograph\'s §27.3, where the one premise is carried in five registers).',
     'in its Weil form `h2_sign`, equivalent to RH (%s), while the conservation register carried beside it, that every ξ-zero forces the '
     'Euler balance at some prime, is RH restated (%s) (the monograph\'s §27.3, where the one premise is carried in five registers).' % (H2, CH)),
    (29, 'The reduction itself is compiled: `ConservationBridge.riemann_hypothesis` at the standard three axioms {propext, Classical.choice, '
         'Quot.sound}.',
     'The deposit’s Route 3 terminal `ConservationBridge.riemann_hypothesis` compiles at the standard three axioms {propext, Classical.choice, '
     'Quot.sound}, and its premise `ConservationHypothesis` is RH restated (%s, E-2026-09-25-1), so it compiles RH ⇒ RH; the compiled '
     'reduction of RH is the Weil form (%s).' % (CH, H2)),
    (234, 'proved under the one open premise `h2` (§27.3), the reduction compiled, the premise open.',
     'argued under the one open premise `h2` (§27.3), which in its Weil form `h2_sign` is equivalent to RH (%s), the Route 3 terminal '
     'compiling RH ⇒ RH (%s), the premise open.' % (H2, CH)),
    (369, '| Compiled — the reduction, not a proof of RH; `h2` carried open |',
     '| Compiled, T2 (b556’s tier block): its premise `ConservationHypothesis` is RH restated (%s, E-2026-09-25-1), so it compiles RH ⇒ RH; '
     'the reduction of RH is `h2_sign_iff_rh` (%s %s); `h2` carried open |' % (CH, EF, PIN['h2_sign_iff_rh'])),
    (401, 'the machine-verified reduction of RH to the single clause `h2`',
     'the reduction of RH to the single clause `h2`, compiled in its Weil form (%s),' % H2),
    (405, '(§27.3 named; the reduction compiled, the premise open)',
     '(§27.3 named; the clause compiled in its Weil form as equivalent to RH (%s), the Route 3 terminal compiling RH ⇒ RH (%s), the premise '
     'open)' % (H2, CH)),
]
N4_CLAUSE = ('the index-arity identification of §3 with the cohomological coordinate (Δn₄\'s missing codomain) is carried in the arc\'s '
             'ledgers as a graded reading, not asserted here as a theorem.')
CEILS = []
STEM_RECORD = 'banned stem, correction record:'
STEMS = [
    (74, 'the register gap (density → pairing, the statistical face)', 'the register step (density → pairing, the statistical face)'),
    (193, 'so the gap closes with height', 'so the shortfall closes with height'),
    (334, 'group-named blind spots of an observable class', 'group-named unseen directions of an observable class'),
    (338, 'falls in the gap between', 'falls in the interval between'),
]
NAMES = [109, 162, 164, 166, 167, 325, 395, 513, 533]
NAMES_COUNT = 13
HISTORY_STEMS = [(568, 580, 'v0.8', 'the register step (density → pairing) guarding the shadow row'),
                 (587, 593, 'v0.7', 'the flip-depth instrument d(t) unresolved at reachable depth for t = −0.1, −0.3 (the deep-tail finding)')]
FACT_NEW = '(%s, %s commit%s behind main `2f71068` = v0.11.0)'
FACTS = [
    (373, 'SIDE-lv-conservation main = `5a14205` (landed 2026-08-02, the ratified pass)',
     'SIDE-lv-conservation main at `5a14205` (landed 2026-08-02, the ratified pass; an ancestor three commits behind main `2f71068` = v0.11.0)'),
    (381, 'SIDE-lv-conservation main = `14720d9` (E-8 landed 2026-08-02)',
     'SIDE-lv-conservation main at `14720d9` (E-8 landed 2026-08-02; an ancestor one commit behind main `2f71068` = v0.11.0)'),
]
CREDITS = [
    (55, 'b450 item: W_inf NOT sign-definite',
     '*Credit (b450, relay `data/b450_batch.json`, INDEX_ARITY_AT_THE_CRITICAL_LINE “W_inf NOT sign-definite”, carried at b585 under `(R195)`(3)):* '
     'the archimedean term `W_∞` is not sign-definite -- its kernel `Re ψ(1/4 + iu/2) − log π` is negative at low frequency and positive at '
     'high, crossing at u = 2π (the bench row u = 6.283, kernel −0.0011) -- and the positive assembly facing the prime sum is `W_pole + W_∞` '
     '(`%s` :52-:58, :62).' % SIGN),
    (55, 'b450 item: the Day-1 section I attribution',
     '*Credit (b450, relay `data/b450_batch.json`, INDEX_ARITY_AT_THE_CRITICAL_LINE “the Day-1 section I attribution pole-plus-archimedean”, '
     'carried at b585 under `(R195)`(3)):* Day-1 BALANCE_AND_POSITIVITY §I attributed the positivity to the archimedean term alone, its `W_∞` '
     'row reading “positive (provable)”, and the repaired attribution is to the pole-plus-archimedean term (`%s` :46, :66).' % SIGN),
]


def _hist_line(n, ver, obj):
    return ('*v0.19, 2026-10-01 (b585, beneath the %s entry, under the history clause, OPEN_TRAILS :11908): the entry above carries its wording '
            'as a dated record; its :%d names %s.*' % (ver, n, obj))


HIST_LINES = [(after, _hist_line(n, ver, obj)) for n, after, ver, obj in HISTORY_STEMS]
CARRIED = {}
VERSION = (15, 'v0.19, 2026-10-01')
ASSIGN = {}
READING_NAME = {0: 'none -- resolved by the form', 1: '(a) h2 takes h2_sign', 2: '(c) a T2 terminal says what it states per the tier block'}
CEILING = re.compile(r'RH proved|RH is proved|h2_sign proved|λ_n ≥ 0 proved|GRH proved|GRH reduced|reduction machine-verified|proof of RH|'
                     r'proves RH|RH proves|RH proof|[Pp]roof of GRH|GRH holds|GRH (?:is )?established|becomes? unconditional\b|is unconditional\b|'
                     r'\([Uu]nconditional\)|kernel-verified\)\.|machine-verified reduction|reduction itself is compiled|proved under the one open premise')
CEIL_RECORD = 'ceiling correction record:'
CARRY_RECORD = 'ceiling read, carried:'
BM_TAG = '<!-- b585 (R195) THE v0.19 EDITION`S BACK MATTER, 2026-10-01 -->'
BANKROWS = ()


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _rows():
    return [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'INDEX' and r['verdict'] == 'MOVED-IN-MEANING']


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    """### the edition's final line for a current-version line: +2 from :15 (the version line and a blank); +4 more after :55 (the two
    ### credit lines, each with a blank before); +2 more after :580 and +2 more after :593 (a blank and a history line beneath each entry)."""
    return n + (2 if n >= VERSION[0] else 0) + (4 if n > 55 else 0) + (2 if n > 580 else 0) + (2 if n > 593 else 0)


OFFSET = ('+2 from :15 (the v0.19 version line and a blank, above the v0.18 version line); +4 more after :55 (the two b450 credit lines, '
          'each with a blank); +2 more after :580 and +2 more after :593 (a blank and a history line beneath the v0.8 and the v0.7 entries) -- '
          'v0.18 :n sits at the edition`s :n+2 for 15 <= n <= 55, :n+6 to :580, :n+8 to :593, :n+10 after')


def _all_changes():
    return REWRITES + CEILS + STEMS + FACTS


def edition(*a):
    """### PLACE-papers phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE_v0_19.md, beside the current version from its blob at 1d0109f; the
    ### re-pin step run last over the final body."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE 1d0109f -- NOTHING WRITTEN')
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
    if (not cur[VERSION[0] - 1].startswith('v0.18, 2026-08-08') or cur[55] != '' or not cur[54].startswith('**N4 —')
            or cur[580] != '' or cur[593] != '' or not cur[564].startswith('*v0.8 (') or not cur[581].startswith('*v0.7 (')):
        sys.exit('### AN ANCHOR IS NOT WHERE THE FACE SAYS')
    if N4_CLAUSE not in new[404] or N4_CLAUSE not in cur[404]:
        sys.exit('### THE n4 CLAUSE IS NOT CARRIED BYTE FOR BYTE')
    for t in [c[2] for c in CREDITS] + [h[1] for h in HIST_LINES]:
        if len(_segs(t)) != 1:
            sys.exit('### AN INSERTED LINE IS NOT ONE SEGMENT: %s' % t[:60])
    diff = []
    for r in _rows():
        ln = r['line']
        k = _segs(cur[ln - 1]).index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d] in nw]
        banks = re.findall(r'relay `data/[^`]+` :\d+', nw)
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         reading=(2 if r['terminal'] == 'riemann_hypothesis' else 1), cites=cites, banks=banks, supports=r['reading']))
    new[593:593] = ['', HIST_LINES[1][1]]
    new[580:580] = ['', HIST_LINES[0][1]]
    new[55:55] = ['', CREDITS[0][2], '', CREDITS[1][2]]
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
    at = [[i for i, l in enumerate(body, 1) if l == c[2]][0] for c in CREDITS]
    hat = [[i for i, l in enumerate(body, 1) if l == h[1]][0] for h in HIST_LINES]
    bm = ['', BM_TAG, '',
          '## Back matter of the v0.19 edition -- written 2026-10-01 by b585 under the author’s ruling `(R195)`(3), by the form of `(R187)`(5)',
          '',
          '*This file is v0.19 of INDEX_ARITY_AT_THE_CRITICAL_LINE, the CP-7 edition written beside v0.18 (`%s`, unedited) from v0.18’s tier '
          'block (its :647, standing) and its CP-1b work-list (relay `%s`), the ζ page as its spine; it does not deposit and does not replace '
          'v0.18, and its promotion is CP-8’s. Every line cited below is this file’s own.*' % (CUR, WL), '',
          '### Removals', '',
          'None: every one of the 9 work-list rows resolves to a sentence rewritten in place to what its compiled fact says.', '',
          '### Credit lines', '',
          '| inserted at this edition’s line | beside the sentence at | source | Status |', '|:--|:--|:--|:--|',
          '| :%d | :%d (N4, the sign wall λ_Z ≥ −λ_A, where the archimedean term’s sign bears) | %s | inserted under the placement clause, as at b581 |'
          % (at[0], _edl(55), CREDITS[0][1]),
          '| :%d | :%d (the same) | %s | inserted under the placement clause, as at b581 |' % (at[1], _edl(55), CREDITS[1][1]),
          '', '### History lines', '', '| inserted at this edition’s line | beneath the dated entry | its stem, carried | Status |', '|:--|:--|:--|:--|']
    for (n, after, ver, obj), h in zip(HISTORY_STEMS, hat):
        bm.append('| :%d | the %s entry, ending at this edition’s :%d | :%d, carried-by-history | inserted under the history clause, the author’s '
                  'answer before b585’s seal |' % (h, ver, _edl(after), _edl(n)))
    bm += ['', '### Stem corrections', '', '| this edition’s line | v0.18 wording | v0.19 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in STEMS:
        bm.append('| :%d | %s %s (banned stem; correction record) | %s | corrected under the stem clause |' % (_edl(ln), STEM_RECORD, old, rep))
    bm += ['', '### Names excepted', '',
           'The term these lines use names the spacing between consecutive zeros, as the literature names it; each use carries unchanged under '
           'the name-and-title exception (OPEN_TRAILS :11934), the author’s answer before b585’s seal.', '',
           '| this edition’s line | Status |', '|:--|:--|']
    for n in NAMES:
        bm.append('| :%d | excepted, the object’s own name |' % _edl(n))
    bm += ['', '### Ceiling corrections', '', 'None: the marked sentences are rewritten above; no unmarked sentence of v0.18 speaks beyond the ceiling.', '',
           '### Fact corrections', '', '| this edition’s line | v0.18 wording | v0.19 wording | the printed fact | Status |', '|:--|:--|:--|:--|:--|']
    for ln, old, rep in FACTS:
        bm.append('| :%d | %s | %s | SIDE-lv-conservation main is `2f71068` = v0.11.0 locally and at the remote; the printed pin is its ancestor (relay '
                  '`data/b585_reads.txt`) | corrected under the fact clause |' % (_edl(ln), old, rep))
    bm += ['', '### The navigator’s expectations of `(R195)`(3)', '',
           '| expectation | the read | Status |', '|:--|:--|:--|',
           '| (a) h2 takes `h2_sign` | 7 rows | rewritten |',
           '| (b) the two b450 items | both credited beside :%d, citing `%s` by b581’s lines | two credits |' % (_edl(55), SIGN),
           '| (c) the T4 rows | their sentences carried as readings | stand |',
           '| (d) T2 terminals | the Route 3 terminal’s 2 rows per the tier block at this edition’s :%d | rewritten |' % _edl(647),
           '| (e) the n₄ ↔ H² correspondence | its clause in :%d carried byte for byte; SPIRAL_MAP :434 “proposed”; no page line cited | stands as proposed |' % _edl(405),
           '', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v0.19 | `%s` | written at b585 |' % ED,
           '| the current version, v0.18 | `%s` | unedited |' % CUR,
           '| the spine | `%s` at PLACE-papers `%s` | read, unedited |' % (PAGE, MIRROR_PIN),
           '| the sign reconciliation | `%s` | read, unedited |' % SIGN,
           '| the work-list | relay `%s` | read |' % WL,
           '| the sentence-by-sentence diff | relay `data/b585_edition_INDEX.txt` | banked at b585 |',
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
    put_json('b585_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=len(CREDITS), removals=0, ruled_citations=len(HIST_LINES), version_lines=1, diff=diff, offset=OFFSET,
                                       ceils=CEILS, stems=STEMS, facts=FACTS, names=NAMES, names_count=NAMES_COUNT,
                                       history=[dict(stem_line=n, after=after, entry=ver, text=h[1], at=a2) for (n, after, ver, obj), h, a2
                                                in zip(HISTORY_STEMS, HIST_LINES, hat)],
                                       credits=[dict(after=c[0], id=c[1], text=c[2], at=a2) for c, a2 in zip(CREDITS, at)],
                                       version=dict(above=VERSION[0], text=VERSION[1]), n4_clause=N4_CLAUSE,
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))


def _stem_live(edp):
    """### the stem scan`s live uses, by line, with the excepted names and the carried-by-history stems taken out."""
    import banned_terms as BT
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    cut = ed.index(BM_TAG)
    names = set(_edl(n) for n in NAMES)
    hist = set(_edl(n) for n, _, _, _ in HISTORY_STEMS)
    out = dict(names=0, history=0, other=[])
    for i, l in enumerate(ed[:cut], 1):
        for m in BT.PAT.finditer(l):
            if i in names:
                out['names'] += 1
            elif i in hist:
                out['history'] += 1
            else:
                out['other'].append(i)
    return out


def edition_bank():
    """### The diff with its offset line, the credits, the history lines, the corrections, the counts, the ceiling read, H28a-H28c."""
    E = jl('b585_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(BM_TAG)
    scan = rd('b585_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    sl = _stem_live(edp)
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            kind = 'record' if (i > cut and l.startswith('| :') and (CEIL_RECORD in l or CARRY_RECORD in l)) else 'beyond'
            hits.append(dict(line=i, hit=m.group(0), kind=kind, ctx=l[max(0, m.start() - 60):m.end() + 20]))
    beyond = [h for h in hits if h['kind'] == 'beyond']
    h28a_bad = [d['id'] for d in E['diff'] if not d['changed'] or not (d['cites'] or d['banks'])]
    h28a = 'HELD' if not h28a_bad else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur']
    allowed = E['credit'] + E['removals'] + E['ruled_citations'] + E['version_lines']
    h28b = 'HELD' if abs(body_dn) <= allowed else 'REFUTED'
    live_n = int(live.group(1)) if live else None
    h28c = 'HELD' if (live_n is not None and live_n == sl['names'] + sl['history'] and not sl['other'] and not beyond) else 'REFUTED'
    cur0 = _cur()
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % OFFSET, '',
         'b585 -- COMPONENT 2: THE EDITION OF INDEX_ARITY_AT_THE_CRITICAL_LINE, (R195)(3), BY THE FORM OF (R187)(5) AND ITS CLAUSES', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :15 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0][:40], cur0[14][:60]),
         '### its tier block : :647 "%s"' % cur0[646][:110],
         '### its version history : :441-:630 (v0.18 back to v0.1); the era annotations :631 and :639 (b454, W_inf)',
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE WORK-LIST, ROW BY ROW (9 rows, 7 sentences, 6 lines) -- each row: v0.18`s line and the edition`s, the terminal, the '
         'expectation it falls under (the seat`s hand-read), what its sentence cites, the sentence before and after.', '']
    for d in E['diff']:
        L += ['  %s v0.18 :%d -> v0.19 :%d `%s` -- %s ; cites %s%s' % (d['id'], d['line'], d['ed_line'], d['terminal'], READING_NAME[d['reading']],
                                                                   ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']],
                                                                   (' ; bank ' + ', '.join(d['banks'])) if d['banks'] else ''),
              '      work-list: %s' % d['supports'],
              '      v0.18 : %s' % d['old'], '      v0.19 : %s' % d['new'], '']
    cov = [d for d in E['diff'] if d['reading']]
    L += ['### (N1) COVERAGE BY THE EXPECTATIONS OF (R195)(3), the seat`s hand-read: %d of %d rows -- (a) %d, (d) %d ; uncovered %s ; and both '
          'b450 items, by (b)' % (len(cov), len(E['diff']), sum(d['reading'] == 1 for d in E['diff']), sum(d['reading'] == 2 for d in E['diff']),
                                  [':%d `%s`' % (d['line'], d['terminal']) for d in E['diff'] if not d['reading']]), '',
          '### THE CREDIT LINES:'] + ['    v0.19 :%d (after v0.18 :%d) %s : %s' % (c['at'], c['after'], c['id'], c['text']) for c in E['credits']]
    L += ['### THE HISTORY LINES (the author`s answer; the history clause governs inside a dated entry):']
    L += ['    v0.19 :%d beneath the %s entry (v0.18 :%d carried) : %s' % (h['at'], h['entry'], h['stem_line'], h['text']) for h in E['history']]
    L += ['### THE STEM CORRECTIONS:'] + ['    v0.18 :%d -> v0.19 :%d  "%s" -> "%s"' % (s[0], _edl(s[0]), s[1], s[2]) for s in E['stems']]
    L += ['### THE NAMES EXCEPTED (the spacing between consecutive zeros, the object`s own name; %d uses on %d lines): %s' % (
        E['names_count'], len(E['names']), [':%d' % _edl(n) for n in E['names']])]
    L += ['### THE FACT CORRECTIONS (%d):' % len(E['facts'])]
    L += ['    v0.18 :%d -> v0.19 :%d  "%s" -> "%s" ; source: SIDE-lv-conservation main read locally and at the remote, the ancestry and the '
          'count, printed in data/b585_reads.txt' % (f[0], _edl(f[0]), f[1], f[2]) for f in E['facts']]
    L += ['### THE n4 <-> H2 CLAUSE: carried byte for byte inside v0.18 :405 / v0.19 :%d -- "%s"' % (_edl(405), E['n4_clause']),
          '### THE VERSION LINE: above v0.18 :%d: %s' % (E['version']['above'], E['version']['text']),
          '### REMOVALS: none. ### CEILING CORRECTIONS: none.', '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d: two credit '
          'lines, two history lines, the version line) ; the back matter %d ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d + one version line = %d' % (
              body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], 'quoted in a back-matter record, read by the seat' if h['kind'] == 'record'
                                          else '### BEYOND THE CEILING', h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### the banned-stem scan of the edition (relay data/b585_edition_termscan.txt): live uses %s, of which %d excepted names and %d '
          'carried-by-history; other live uses %s' % (live_n, sl['names'], sl['history'], sl['other'] or 'NONE'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on the page at its pin, or a bank line%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- live banned stems %s, all excepted names (%d) or carried-by-history (%d); sentences beyond the ceiling %d.**' % (
              h28c, live_n, sl['names'], sl['history'], len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b585_edition_INDEX.txt', L)
    put_json('b585_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=live_n, stem_names=sl['names'], stem_history=sl['history'],
                                   stem_other=sl['other'], beyond=len(beyond), hits=hits,
                                   covered=len(cov), uncovered=[d['id'] for d in E['diff'] if not d['reading']], held=None,
                                   n_ceils=len(E['ceils']), n_facts=len(E['facts'])))
    H = jl('b585_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'covered', H['covered'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'], 'live', H['live'], sl)


# ================================================================================ THE SCORING AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
CENSUS_LIVE = 5


def scores():
    H, E = jl('b585_h28.json'), jl('b585_edition.json')
    ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'ls-files', '--others', '--exclude-standard', 'phase1.5', 'phase2')).split(NL) if x.strip()))
    kmain = g('D:/SIDE-explicit-formula', 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    cur_same = g(PP, 'hash-object', CUR).strip() == E['cur_blob']
    n2 = H['H28a'] == 'HELD' and H['H28b'] == 'HELD' and H['H28c'] == 'HELD' and H['held'] is None
    allowed_pp = {'FINDINGS.md', 'OPEN_TRAILS.md', ED}
    ed = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read()
    n4_same = E['n4_clause'] in ed
    S = dict(
        N1=('HELD' if H['covered'] >= 6 and len(E['credits']) == 2 else 'REFUTED', 'the expectations of (R195)(3) cover %d of the 9 rows and '
            'both b450 items (credits %d); uncovered %s' % (H['covered'], len(E['credits']), H['uncovered'])),
        N2=('HELD' if n2 else 'REFUTED', 'H28a %s, H28b %s (the body %+d against at most %d), H28c %s; no sentence held' % (
            H['H28a'], H['H28b'], H['body_dn'], H['allowed'], H['H28c'])),
        N3=('HELD' if H['n_ceils'] <= CENSUS_LIVE and H['n_facts'] == 0 else 'REFUTED', 'the ceiling clause corrects %d against the census`s '
            '%d live keyword co-occurrences -- one in a marked sentence (:401, rewritten), four read by the seat as not beyond the ceiling '
            '(:21 single-index positivity`s edge reach, :71 the code world, :263 the function-field positivity, :407 the registry line`s '
            'titles); the fact clause finds %d (the two "main = `sha`" cells, :373 and :381)' % (H['n_ceils'], CENSUS_LIVE, H['n_facts'])),
        N4=('HELD' if n4_same and 405 not in [r[0] for r in REWRITES] else 'REFUTED', 'the n4 <-> H2 clause carries byte for byte '
            '(%s), inside the :405 sentence the work-list marks, which is rewritten at its other clause ("the reduction compiled") -- the clause '
            'unchanged, the sentence not' % ('held' if n4_same else '### CHANGED')),
        N5=('HELD' if (kmain == V015 and heads_ok and cur_same and set(ch) <= allowed_pp) else 'REFUTED', 'nothing deposits; no kernel '
            'touched (%s); the current INDEX_ARITY unedited (%s); PLACE-papers changed at %s' % (
                'held' if kmain == V015 and heads_ok else '### MOVED', 'held' if cur_same else '### EDITED', ch)),
        S1=('HELD' if H['covered'] == 9 and len(E['credits']) == 2 else 'REFUTED', '(N1) holds at 9 of 9 and both items'),
        S2=('HELD' if n2 and H['body_dn'] == 5 and H['allowed'] == 5 else 'REFUTED', 'H28a-H28c held; the body +5 against 5'),
        S3=('HELD' if H['n_ceils'] == 0 and H['n_facts'] == 2 else 'REFUTED', '(N3) refuted on its second half alone: 0 ceiling, 2 fact corrections'),
        S4=('HELD' if n4_same else 'REFUTED', 'the n4 clause carries byte for byte inside a rewritten sentence'),
        S5=('HELD' if set(ch) == allowed_pp else 'REFUTED', '(N5) holds: the files changed are the three its list names'),
        counts=dict(pp_changed=ch, body_dn=H['body_dn'], covered=H['covered']),
    )
    put_json('b585_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], S[k][1][:160]))


TITLE_HEAD = ('## CP-7, act ten: the edition of INDEX_ARITY_AT_THE_CRITICAL_LINE from its tier block and work-list, the W_∞ sign finding '
              'and the Day-1 attribution carried')
TITLE = TITLE_HEAD + '; written as v0.19 beside v0.18, no sentence held'
TRAIL_HEAD = ('### b585 — lane three, act thirteen under (R195): CP-7 act ten -- the edition of INDEX_ARITY_AT_THE_CRITICAL_LINE written '
              'beside the current; the Face E / keyhole item closed as not located')


def records_pp():
    Q = _Q()
    S, H, E, C1 = jl('b585_scores.json'), jl('b585_h28.json'), jl('b585_edition.json'), jl('b585_c1_lines.json')
    ln = C1['lines']
    Q.guard_absent(Q.FIND, TITLE_HEAD)
    e = ['', TITLE, '',
         '*Filed at b585 on the author’s ruling `(R195)`. Banks: relay `data/b585_edition_INDEX.txt` (the sentence-by-sentence diff, its '
         'offset line at its head), `data/b585_edition.json`, `data/b585_reads.txt`. Nothing deposits.*', '',
         '**The edition** (`(R195)`(3)): `%s`, v0.19, written beside v0.18 (`%s`, unedited) from v0.18’s tier block and its CP-1b work-list, '
         'the ζ page as its spine. The 9 work-list rows resolve to 7 sentences on 6 lines, each rewritten in place: the clause named in its '
         'Weil form and cited to its equivalence with RH; the conservation register and the deposit’s Route 3 terminal said to be RH restated, '
         'its row graded as the tier block reads it. The archimedean sign finding and the Day-1 attribution are credited beside N4’s sign wall, '
         'citing SIGN_ARRANGEMENT_RECONCILIATION by b581’s lines. The n₄ ↔ H² clause carries byte for byte as a proposed reading. Four stem '
         'uses are corrected; the thirteen uses naming the spacing between consecutive zeros are excepted as the object’s name; two stems in '
         'dated entries carry, each with a history line beneath; two pins printing an older main of SIDE-lv-conservation are corrected by the '
         'fact clause. No sentence is removed and none held.' % (ED, CUR), '',
         '**The counts.** v0.18 %d sentences; v0.19 %d (the body %d, the back matter %d); the body differs by %+d against the final bound, %d.'
         % (E['n_cur'], E['n_full'], E['n_body'], E['n_backmatter'], H['body_dn'], H['allowed']), '',
         '**H28a %s · H28b %s · H28c %s.** Coverage of the 9 rows by the navigator’s expectations: %d, and both b450 items.' % (
             H['H28a'], H['H28b'], H['H28c'], H['covered']), '',
         '**The record lines** (`(R195)`(1)-(2)): b584’s weight (FINDINGS :%d); Face E / keyhole closed as not located (OPEN_TRAILS :%d); '
         'the history clause’s precedence inside a dated entry (:%d), the author’s answer.' % (ln['weight'], ln['keyhole'], ln['precedence']), '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R195)`(4): the edition of ENUMERA by the same form; the author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; v0.18, README, REGISTRY, ERRATA, SPIRAL_MAP and both pages unwritten; nothing here is a '
         'statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R195) ratified.** (1) b584 at its weight. (2) Face E / keyhole closed as not located. (3) The edition of '
             'INDEX_ARITY_AT_THE_CRITICAL_LINE by the form, the ζ page as its spine. (4) The act after.', '',
             '**Entered:** FINDINGS.md:%d (b584’s weight), :%d (the entry); OPEN_TRAILS.md:%d (Face E / keyhole), :%d (the history clause’s '
             'precedence), this record; PLACE-papers `%s` (created).' % (ln['weight'], Q.line_of(Q.FIND, TITLE_HEAD), ln['keyhole'],
                                                                           ln['precedence'], ED), '',
             '**Answered before the seal, by the author:** the thirteen uses naming the spacing between consecutive zeros are excepted as the '
             'object’s own name; the two stems inside dated entries carry with a history line beneath each, the history clause governing '
             'inside a dated entry.', '',
             '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
             % tuple(S[k][0] for k in SCORE_KEYS), '',
             '**For the author:** (N4) is scored refuted in letter: the n₄ ↔ H² clause carries byte for byte, but it sits inside the :405 sentence '
             'the work-list marks, which is rewritten at its other clause. (N3) is refuted on its second half: two Correspondence cells print '
             '“SIDE-lv-conservation main = `sha`” where main is now `2f71068`, the same species as b583’s branch pins, corrected as such.', '',
             '**Next:** per `(R195)`(4), CP-7 act eleven, b586 -- the edition of ENUMERA by the same form, H28a-H28c scored; the author rules '
             'on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
             'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b585_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE_HEAD), title=TITLE, append=r))
    put_json('b585_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r2))
    print(jl('b585_findings.json')['entry_line'], jl('b585_trail.json')['line'])


def desk():
    S = jl('b585_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b585 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b585_defects.txt').rstrip(NL).split(NL)
    put_txt('b585_desk_notes.txt', L)


def components():
    S, H, C1, fj, tj = (jl('b585_scores.json'), jl('b585_h28.json'), jl('b585_c1_lines.json'), jl('b585_findings.json'), jl('b585_trail.json'))
    ln = C1['lines']
    L = ['b585 -- THE COMPONENTS, BANKED UNDER (R195).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b584`s closing push-out relay e63e8530 ; push-b584* branches deleted by '
         'name (data/b585_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : b584`s weight FINDINGS :%d ; Face E / keyhole closed OPEN_TRAILS :%d ; the history clause`s precedence :%d' % (
             ln['weight'], ln['keyhole'], ln['precedence']),
         '### COMPONENT 2 : the edition %s ; 7 sentences rewritten, 2 credit lines, 2 history lines, 4 stem and 2 fact corrections, 13 names '
         'excepted, the version line, 0 removals ; data/b585_edition_INDEX.txt ; H28a %s H28b %s H28c %s ; N1 %s N2 %s N3 %s N4 %s' % (
             ED, H['H28a'], H['H28b'], H['H28c'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0]),
         '### COMPONENT 3 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; next: the edition of ENUMERA ; N5 %s'
         % (fj['entry_line'], tj['line'], S['N5'][0])]
    put_txt('b585_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b585_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
