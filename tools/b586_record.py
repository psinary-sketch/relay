# -*- coding: utf-8 -*-
"""b586_record.py -- THE ACT'S RECORD TOOL, UNDER (R196). ### ONE SUBCOMMAND PER BANK.

### ### b586: LANE THREE, ACT FOURTEEN -- CP-7 ACT ELEVEN, THE EDITION OF ENUMERA; THE STEM SCANNER TAUGHT THE FORM'S EXCEPTIONS;
### THE CORROBORATION CENSUS; LANE THREE'S ORDER REFINED. Subcommands write only `data/b586_*` unless the docstring names another
### file. Every bank is written through `put_txt` / `put_json` (encode first, then a temp file, then `os.replace`). This act makes no
### platform call. ### The template is b585_record.py.
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
PRE_PP = '7e9b771'
MIRROR_PIN = '192077f'
CUR = 'phase1.5/method/ENUMERA.md'
ED = 'phase1.5/method/ENUMERA_v1_6.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
WL = 'data/b558_editions/ENUMERA.txt'
INDEX19 = 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE_v0_19.md'
AMC24 = 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY_v0_2_4.md'

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
    '(a) THE QUESTION BEFORE THE SEAL NAMED THE POISSON EXHAUSTION ROW AS :896; it is :895 (:896 is the CONSERVATION OF SPECTRA row). '
    'The question quoted the row`s text, "Establishes exhaustiveness of seven-class catalogue", and the correction is made at :895.',
    '(b) THE SAME QUESTION MISSED A SITE OF THE SAME SHAPE: :73`s first sentence, "The seven-class catalogue is exhaustive.". It is '
    'corrected under the answer`s principle (the place count closed; the exhaustiveness at the xi interface the open premise) and named '
    'for the author, as b584 named :149.',
    '(c) THE SAME QUESTION`S LIST OF CEILING-SHAPED SENTENCES READ AND CARRIED MISSED :872 (a reader`s question quoted as an FAQ heading, '
    '"how much of the RH proof depends on it?") and :892 (CRITICAL RESOLVE`s role line in the source table, "Detailed RH proof"). The '
    'edition tool refused to write until each was read; both carry as read, declared on the face before the seal, the author`s "the rest '
    'unchanged" governing.',
    '(d) THE FIRST RUN OF `records_pp` WROTE THE FINDINGS ENTRY AND WAS THEN REFUSED AT THE TRAIL APPEND: the trail`s "For the author" '
    'line quoted the CR document`s item labels, which carry the banned stem, and the append guard refused before writing. FINDINGS was '
    'cut back to the byte before the entry (2884 bytes; HEAD`s blob verified a prefix, the weight line kept), the line reworded to cite '
    'the edition`s lines, and the subcommand re-run whole. On reading the landed trail, its ceiling-clause reading carried a sentence the '
    'author did not say (an added condition); FINDINGS and OPEN_TRAILS were cut back the same way (2884 and 2236 bytes, HEAD`s blobs '
    'verified prefixes, the weight and order lines kept), the reading reworded to the author`s words, and the subcommand re-run whole.',
    '(e) THE SUITE`S FIRST RUN FAILED G-CEILING-CARRIED AND G-NAMES-EXCEPTED LIVE: each compared a whole line, and :20 (a carried phrase '
    'beside a rewritten sentence) and :895 (an item label beside a ceiling correction) share their lines with another change -- b583`s '
    'species. Both now compare what carries (the ceiling hits; the stem uses), and the suite was re-run whole.',
]


def defects():
    put_txt('b586_defects.txt', ['### b586 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay the ENUMERA work-list, whole', RELAY, 'HEAD', WL, list(range(1, 51))),
    ('PLACE-papers ENUMERA, its head, claim-status note and overview', PP, PRE_PP, CUR, list(range(1, 62))),
    ('PLACE-papers ENUMERA, the marked, ceiling, stem and named lines', PP, PRE_PP, CUR,
     [73, 346, 536, 542, 544, 562, 696, 791, 854, 870, 893, 894, 895, 896, 898, 919, 921, 922, 923, 932, 946, 1040, 1044]),
    ('PLACE-papers ENUMERA, its version history and tier block', PP, PRE_PP, CUR, list(range(1028, 1066))),
    ('PLACE-papers the zeta page at the mirror`s pin, its pin line, nodes 7, 8, 20, the open line and the mellin row', PP, MIRROR_PIN, PAGE,
     [3, 11, 12, 24, 31, 138]),
    ('relay the b538 register census, R3', RELAY, 'HEAD', 'data/b538_census.json', list(range(18, 25))),
    ('relay the CP-1b bank, its head', RELAY, 'HEAD', 'data/b558_cp1b.txt', list(range(1, 9))),
    ('relay tools/banned_terms.py, its scope, window, exceptions and verdict line', RELAY, 'HEAD', 'tools/banned_terms.py',
     list(range(64, 78)) + [112, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 332, 344]),
    ('PLACE-papers INDEX_ARITY v0.19, its back matter`s exception rows', PP, PRE_PP, INDEX19, [712, 729, 733, 734, 745, 751, 759]),
    ('PLACE-papers AMC v0.2.4, its back matter`s exception rows', PP, PRE_PP, AMC24, [523, 533, 537, 538, 539]),
    ('PLACE-papers THE_KEYSTONE_CENSUS, the roster note', PP, PRE_PP, 'phase2/method/THE_KEYSTONE_CENSUS.md', [272]),
    ('PLACE-papers OPEN_TRAILS, b450`s "THERE IS NO TABLE" rows', PP, PRE_PP, 'OPEN_TRAILS.md', [6586, 6587]),
    ('PLACE-papers OPEN_TRAILS, lane three, the form, its clauses and b585`s record', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11417, 11864, 11884, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 11974, 11976, 11994, 11996, 12012, 12020,
      12026, 12028, 12042, 12044, 12046]),
    ('PLACE-papers FINDINGS, b585`s entry', PP, PRE_PP, 'FINDINGS.md', [6630]),
    ('relay the constellation-mode reports, their scope lines', RELAY, 'HEAD', 'reports/2026-08-09-correspondence-regrade-sitting-1.md',
     list(range(9, 34)) + [37, 39, 40]),
    ('relay b566`s rowgen bank, its head', RELAY, 'HEAD', 'data/b566_rowgen.txt', [1, 2, 3]),
    ('relay b585`s closing push-out, its head', RELAY, 'HEAD', 'data/b585_closing_push_out.txt', list(range(1, 4))),
]


def reads():
    L = ['b586 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    k = g('D:/SIDE-kernel', 'show', 'v1.5:Bridge/LocalZeta.lean').split(NL)
    L += ['### the fact clause`s read: the formation count against SIDE-kernel v1.5 -- Bridge/LocalZeta.lean :13 "%s"' % k[12].strip(),
          '### the explicit-formula tags the edition cites:']
    for tag, cited in (('v0.1', 'baed4df'), ('v0.2', '5c72cad'), ('v0.9', 'e5a5a83'), ('v0.11', '19b7d1e')):
        loc = g('D:/SIDE-explicit-formula', 'rev-parse', tag + '^{}').strip()
        rem = [l.split('\t')[0] for l in g('D:/SIDE-explicit-formula', 'ls-remote', 'origin', 'refs/tags/%s^{}' % tag).split(NL) if l.strip()]
        r = rem[0] if rem else ''
        L.append('    SIDE-explicit-formula %s : cited %s ; local %s ; remote %s ; %s' % (tag, cited, loc[:7], r[:7],
                                                                                     'AGREE' if loc.startswith(cited) and r.startswith(cited) else '### DIFFER'))
    L.append('### the constellation-mode and rowgen records since b566, by act: %s' % _since_b566())
    put_txt('b586_reads.txt', L)


def _since_b566():
    hits = []
    for f in sorted(os.listdir(D)):
        m = re.match(r'^b(5(?:6[6-9]|7\d|8[0-5]))_', f)
        if m and f.endswith('.txt') and 'ferry' not in f:
            t = rd(f)
            if re.search(r'constellation mode|rowgen\.diff IMPORTED', t, re.I):
                hits.append('b%s:%s' % (m.group(1), f))
    return hits


# ================================================================================ COMPONENT 1 -- THE SCANNER AND THE WEIGHT LINE
def scanner_bank():
    """### data/b586_scanner.txt: the test run, and the two editions re-scanned with their verdict lines."""
    t = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_banned_terms_backmatter.py')], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    L = ['b586 -- COMPONENT 1: THE STEM SCANNER TAUGHT THE FORM`S EXCEPTIONS, (R196)(2)', '',
         '### the test (tools/test_banned_terms_backmatter.py), exit %d:' % t.returncode] + ['    ' + l for l in t.stdout.strip().split(NL)]
    res = {}
    for rel in (INDEX19, AMC24):
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', os.path.join(PP, *rel.split('/'))],
                           capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
        keep = [l for l in r.stdout.split(NL) if re.search(r'hits found|live uses|excepted|VERDICT', l)]
        L += ['', '### re-scanned: %s (exit %d)' % (rel, r.returncode)] + ['    ' + l.strip() for l in keep]
        m = re.search(r'^\s*VERDICT\s*: (.+)$', r.stdout, re.M)
        res[rel] = dict(exit=r.returncode, verdict=m.group(1).strip() if m else None,
                        live=int(re.search(r'live uses\s*:\s*(\d+)', r.stdout).group(1)))
    put_txt('b586_scanner.txt', L)
    put_json('b586_scanner.json', dict(test_exit=t.returncode, test_out=t.stdout, rescans=res))


FORM_HEAD = '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three'
LANE3 = '> LANE THREE — THE CLARIFIED LAYER'
B585_ENTRY = '## CP-7, act ten: the edition of INDEX_ARITY_AT_THE_CRITICAL_LINE'
ORDER_TEXT = ("as ruled: “the editions continue in the ratified order through RESIDUE; then the two companions BALANCE_AND_POSITIVITY "
              "and FACES_OF_H2; then W-ORD-SIMPLICITY-FACE as a research act, then SIMPLICITY's edition; then one CP-1b act over "
              "SILENCE_STAGES and REPARAMETERIZATION and their editions; TECHNE and E_DIFFICULTY take a Correspondence table before their "
              "editions if the census shows none, by the author's word at that closing; then CP-6; then CP-8 with the monograph's ceiling "
              "uses. The research items that move no keystone's meaning — E1/E2, KEIPER-FACE, THREE-WAY, PNT-CHI, the lv toolchain "
              "re-measure — stay priced for the author's word between or after.” The census of this act (relay `data/b586_corroboration.txt`) "
              "reads a table under TECHNE_TOOLKIT's Correspondence heading and none naming a terminal in E_DIFFICULTY_THEOREM")


def c1_lines():
    """### PLACE-papers FINDINGS: b585's weight (Component 1)."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B585_ENTRY)
    if entry != 6630:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    h = '*Appended 2026-10-01 by b586 to b585’s entry (:%d), under `(R196)`(1) -- b585 AT ITS WEIGHT:*' % entry
    Q.guard_absent(Q.FIND, h)
    r = Q.append_to(Q.FIND, '\n%s `phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE_v0_19.md` beside v0.18 unedited: 9 rows as 7 sentences on 6 '
                            'lines; the clause in its Weil form; the conservation register and the Route 3 premise RH restated, the Route 3 '
                            'row T2; the two credits after :55; the n₄ ↔ H² clause of :405 byte for byte as a proposed reading; the thirteen '
                            'zero-spacing uses carried as the object’s name (the question said fourteen; the seat’s count governs); :568 and '
                            ':587 carried as dated records with history lines beneath; four stem corrections; two fact corrections '
                            '(SIDE-lv-conservation main printed at two ancestors of `2f71068`) accepted as applied. H28a, H28b (+5 against 5) '
                            'and H28c held; (N3) refuted on its fact half, (N4) in letter. The sealed face’s reading (ix) is corrected by the '
                            'seat’s recount -- of the census’s five, :401 alone is a marked sentence and the other four are keyword '
                            'co-occurrences, not over the ceiling -- and the (N3) score and defect (b) carry it. The suite reads 69 of 69.\n' % h)
    put_json('b586_c1_lines.json', dict(entry=entry, lines=dict(weight=Q.line_of(Q.FIND, h)), heads=dict(weight=h), appends=[r]))
    print(Q.line_of(Q.FIND, h))


# ================================================================================ COMPONENT 2 -- THE CORROBORATION CENSUS
EDITIONS = {'PATHS_TO_THE_CRITICAL_LINE': 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md',
            'FOUNDATIONS_OF_THE_SIDE_PROGRAMME': 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md',
            'ADDITIVE_MULTIPLICATIVE_CONSPIRACY': AMC24,
            'THE_UNCONDITIONAL_SURROUND': 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md',
            'GRH_CASCADE': 'phase1.5/spectral/GRH_CASCADE_v0_3_6.md',
            'R_CURVE_CRITERION': 'phase1.5/rcurve/R_CURVE_CRITERION_v0_2_2.md',
            'INVARIANCE_BARRIERS': 'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md',
            'INDEX_ARITY_AT_THE_CRITICAL_LINE': INDEX19}
NO_TABLE_B450 = {'TECHNE_TOOLKIT': 'OPEN_TRAILS :6586', 'E_DIFFICULTY_THEOREM': 'OPEN_TRAILS :6587'}
CONSTELLATION_LAST = {}
for _n in ('THE_RESIDUE_OF_RH', 'SILENCE_STAGES_DEALIGNMENT'):
    CONSTELLATION_LAST[_n] = '2026-07-29 (reports/2026-07-29-rowgen-constellation.md)'
for _n in ('PATHS_TO_THE_CRITICAL_LINE', 'THE_UNCONDITIONAL_SURROUND', 'SIMPLICITY_OF_RIEMANN_ZEROS', 'INDEX_ARITY_AT_THE_CRITICAL_LINE',
           'FOUNDATIONS_OF_THE_SIDE_PROGRAMME', 'GRH_CASCADE', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY', 'INVARIANCE_BARRIERS', 'EXHAUSTIVENESS_LICENSE',
           'REPARAMETERIZATION_BARRIERS_v0_1'):
    CONSTELLATION_LAST[_n] = '2026-08-09 (reports/2026-08-09-correspondence-regrade-sitting-1.md)'
QNAME = re.compile(r'`([A-Za-z_][\w′ₐ-ₜ₀-₉]*(?:\.[\w′ₐ-ₜ₀-₉]+)+)`')
SIDE_RX = re.compile(r'\bSIDE-[a-z]+(?:-[a-z]+)*\b')
PIN_RX = re.compile(r'`([0-9a-f]{7})`')


BT = re.compile(r'`([^`{}\s][^`{}]*?)`')
TERM = re.compile(r'^[A-Za-z_][\w′ₐ-ₜ₀-₉]*(?:\.[A-Za-z_][\w′ₐ-ₜ₀-₉]*)*$')


def _terms(l):
    """### the terminal-shaped backticked tokens of a table row: a Lean identifier, dotted or carrying an underscore, not a file name, a
    ### version, a SHA, a profile or a SIDE-* repository."""
    out = []
    for t in BT.findall(l):
        t = t.strip()
        if not TERM.match(t) or re.search(r'\.(md|lean|txt|json|py|tex|pdf)$', t) or re.match(r'^v\d', t) or re.match(r'^[0-9a-f]{7,}$', t) or re.match(r'^[A-Z][A-Z0-9_]*$', t) or re.search(r'_v\d', t):
            continue
        if '.' in t or ('_' in t and len(t) >= 6):
            out.append(t)
    return out


def _term_rows(body):
    """### (rows in a section headed Correspondence, rows elsewhere): the table rows (not separators) naming a terminal-shaped token."""
    corr, other, sec = [], [], None
    for i, l in enumerate(body, 1):
        m = re.match(r'^(#{1,6})\s', l)
        if m:
            lev = len(m.group(1))
            if re.search(r'correspond', l, re.I):
                sec = lev
            elif sec is not None and lev <= sec:
                sec = None
        if l.lstrip().startswith('|') and not re.match(r'^\s*\|\s*:?-{2,}', l) and _terms(l):
            (corr if sec is not None else other).append((i, l))
    return corr, other


def _roster():
    out = []
    for l in rd('b557_roster.txt').split(NL):
        m = re.match(r'^    (\S+).*?\s{2,}(\S+\.md)\s+:(\d+)\s*$', l)
        if m:
            out.append((m.group(1), m.group(2), int(m.group(3))))
    return out


def corroboration():
    """### data/b586_corroboration.txt and .json: one line per roster document at its current version (the edition where one exists);
    ### the two lists. No edit anywhere."""
    rows = []
    since = _since_b566()
    for name, path, tier in _roster():
        if name == 'A_Place_to_Stand':
            vpath, text, tline, tnote = 'day1/A_Place_to_Stand.md', g(PP, 'show', '%s:day1/A_Place_to_Stand.md' % PRE_PP), None, 'FINDINGS :4835 (the tier map)'
        else:
            vpath = EDITIONS.get(name, path)
            text = g(PP, 'show', '%s:%s' % (PRE_PP, vpath))
            curl = g(PP, 'show', '%s:%s' % (PRE_PP, path)).split(NL)[tier - 1]
            ls = text.split(NL)
            hit = [i + 1 for i, l in enumerate(ls) if l == curl]
            tline = hit[0] if hit else None
            tnote = ':%s' % tline
        ls = text.split(NL)
        body = ls[:tline - 1] if tline else ls
        corr, other = _term_rows(body)
        trows = corr or other
        names = sorted(set(n for _, l in trows for n in _terms(l)))
        kernels = sorted(set(k for _, l in trows for k in SIDE_RX.findall(l)))
        pins = sorted(set(p for _, l in trows for p in PIN_RX.findall(l)))
        form = ('CORRESPONDENCE' if corr else 'OTHER' if other else 'NONE')
        wl = os.path.exists(os.path.join(D, 'b558_editions', name + '.txt'))
        rows.append(dict(name=name, path=vpath, edition=name in EDITIONS, form=form, table=form == 'CORRESPONDENCE',
                         first=trows[0][0] if trows else None, terminals=len(names), names=names, kernels=kernels, pins=pins,
                         tier=tnote, constellation_since_b566='none', constellation_last=CONSTELLATION_LAST.get(name, 'no run recorded'),
                         worklist=wl, b450=NO_TABLE_B450.get(name)))
    if len(rows) != 22:
        sys.exit('### THE ROSTER DID NOT READ AS 22 (%d)' % len(rows))
    notable = [r['name'] for r in rows if r['form'] == 'NONE']
    othername = [r['name'] for r in rows if r['form'] == 'OTHER']
    unread = [r['name'] for r in rows if r['form'] != 'NONE']
    L = ['b586 -- COMPONENT 2: THE CORROBORATION CENSUS OVER CP-1`S ROSTER, (R196)(3). ### A BANK, NOT A DOCUMENT; NO EDIT ANYWHERE.', '',
         '### THE TEXTS: each roster document at PLACE-papers %s, its current version -- the edition where one exists (%d of them), the '
         'monograph at day1/A_Place_to_Stand.md (its tier map at FINDINGS :4835).' % (PRE_PP, len(EDITIONS)),
         '### THE TABLE, READ ABOVE THE TIER BLOCK: a table row naming a terminal-shaped backticked name (a Lean identifier, dotted or '
         'carrying an underscore; not a file name, a version, a SHA, a profile, an all-capitals document name). CORRESPONDENCE: such a row '
         'under a heading carrying "Correspondence"; OTHER: such rows only in a table of another name (named in the row); NONE: no such row. '
         'The terminals are the distinct such names in those rows (Mathlib names included, so a count and not a terminal list); the kernels '
         'the SIDE-* names and the pins the backticked 7-hex SHAs in those rows. b450 read a table only under a heading beginning '
         '"## Correspondence" or carrying "CORRESPONDENCE AT THE STANDARD" (relay tools/b450_components.py :296).',
         '### CONSTELLATION MODE SINCE b566 (the kernel`s last toolchain move): no act from b566 on ran it; the rowgen banks of the span are %s, '
         'and each diffs rows of the relay`s own correspondence register (403-441, tools/corr_row.py), not a roster table. The last recorded run '
         'per document is printed beside it.' % since, '',
         '| document | version read | table | terminals | kernels | pins | tier block | constellation since b566 | last recorded run | CP-1b work-list |',
         '|:--|:--|:--|--:|:--|:--|:--|:--|:--|:--|']
    for r in rows:
        L.append('| %s | %s | %s | %d | %s | %s | %s | %s | %s | %s |' % (
            r['name'], r['path'], {'CORRESPONDENCE': 'PRESENT, under a Correspondence heading', 'OTHER': 'a table of another name',
                                   'NONE': 'ABSENT'}[r['form']] + (' from :%d' % r['first'] if r['first'] else '') +
            (' (b450 "THERE IS NO TABLE", %s)' % r['b450'] if r['b450'] else ''),
            r['terminals'], ', '.join(r['kernels']) or '--', ', '.join(r['pins']) or '--', r['tier'], r['constellation_since_b566'],
            r['constellation_last'], 'present' if r['worklist'] else 'absent'))
    L += ['', '### THE DOCUMENTS WITH NO TABLE NAMING A TERMINAL (%d): %s' % (len(notable), notable),
          '### beside them, the documents whose terminals stand only in a table of another name (%d): %s' % (len(othername), othername),
          '### THE DOCUMENTS WHOSE TABLES HAVE NOT BEEN RE-READ BY CONSTELLATION MODE SINCE b566 (%d): %s' % (len(unread), unread),
          '### ### **A READ, NOT A VERDICT. No document was edited.**']
    put_txt('b586_corroboration.txt', L)
    put_json('b586_corroboration.json', dict(rows=rows, no_table=notable, other_name=othername, unread=unread, since_b566=since))
    print('no table', notable, '; unread', len(unread))


def order_line():
    """### PLACE-papers OPEN_TRAILS: lane three's refined order, beneath the critical path's lane three clause (Component 3)."""
    Q = _Q()
    lane = Q.line_of(Q.OT, LANE3)
    if lane != 11417:
        sys.exit('### THE LANE THREE CLAUSE MOVED: %s -- NOTHING WRITTEN' % lane)
    h = '*Appended 2026-10-01 by b586 to the critical path’s lane three (:%d), under the author’s ruling `(R196)`(4) -- LANE THREE’S ORDER, REFINED:*' % lane
    Q.guard_absent(Q.OT, h)
    r = Q.append_to(Q.OT, '\n%s %s.\n' % (h, ORDER_TEXT))
    put_json('b586_order.json', dict(lane=lane, head=h, line=Q.line_of(Q.OT, h), append=r))
    print(Q.line_of(Q.OT, h))


# ================================================================================ COMPONENT 4 -- THE EDITION
EF = 'SIDE-explicit-formula'
PIN = {'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'ch_iff_rh': 'v0.1 = `baed4df`', 'li_nonneg_iff_rh': 'v0.9 = `e5a5a83`',
       'mellin_Phi_eq_zero_of_re_le_one': 'v0.11 = `19b7d1e`'}
NS = {'h2_sign_iff_rh': 'B321', 'ch_iff_rh': 'B321', 'li_nonneg_iff_rh': 'LiCriterionBridge', 'mellin_Phi_eq_zero_of_re_le_one': 'RegisterDepth'}
WHERE = {'h2_sign_iff_rh': 'the zeta page, node 8, line 12', 'ch_iff_rh': 'the zeta page, node 7, line 11',
         'li_nonneg_iff_rh': 'the zeta page, node 20, line 24', 'mellin_Phi_eq_zero_of_re_le_one': 'the zeta page, Correspondence row, line 138 (the page`s pin)'}
H2 = '`h2_sign_iff_rh`, %s %s' % (EF, PIN['h2_sign_iff_rh'])
CH = '`ch_iff_rh`, %s %s' % (EF, PIN['ch_iff_rh'])
LI = '`li_nonneg_iff_rh`, %s %s' % (EF, PIN['li_nonneg_iff_rh'])
MP = '`mellin_Phi_eq_zero_of_re_le_one`, %s at the ζ page’s pin %s' % (EF, PIN['mellin_Phi_eq_zero_of_re_le_one'])
R3B = 'relay `data/b538_census.json` :23'

REWRITES = [
    (13, 'under the one open premise `h2` (§27.3), carried openly — the ∎ kept, its reason attached.',
     'under the one open premise `h2` (§27.3), in its Weil form `h2_sign` equivalent to RH (%s), so that its premise is RH itself, carried '
     'openly — the ∎ kept, its reason attached.' % H2),
    (20, 'bent from unconditional to *goal ⇐ h1 ∧ h2*, only `h2` open',
     'bent from unconditional to *goal ⇐ h1 ∧ h2*, a goal state that closes nothing on the strip, lv’s `h2` at Φ being false at every s with '
     're s ≤ 1 (%s), the open clause being `h2_sign`, equivalent to RH (%s)' % (MP, H2)),
    (21, '— equivalently **realization-totality at the ξ interface**, the **R4 positivity face** (λ_Z(n) ≥ −λ_A(n) at every n), or the goal '
         'state\'s Mellin-nonvanishing clause `mellin Φ (s/2) ≠ 0` off the line: one premise in **§27.3\'s five registers**',
     '— a form that is RH restated (%s), beside which §27.3\'s registers name separate statements and not one premise: '
     '**realization-totality at the ξ interface** is undecided (%s), the **R4 positivity face** (λ_Z(n) ≥ −λ_A(n) at every n) is RH in the '
     'Li form (%s), and the goal state\'s `mellin Φ (s/2) ≠ 0` is false at every s with re s ≤ 1 (%s); in its Weil form the clause is '
     '`h2_sign`, equivalent to RH (%s)' % (CH, R3B, LI, MP, H2)),
    (23, 'the RH-[PROVED] closure composes under the one open premise `h2` (§27.3),',
     'the RH-[PROVED] closure composes under the one open premise `h2` (§27.3), in its Weil form `h2_sign` equivalent to RH (%s),' % H2),
    (73, '*under the exhaustiveness premise `h2`, carried openly as open*',
     '*under the exhaustiveness premise `h2`, carried openly as open*, the premise in its Weil form `h2_sign` equivalent to RH (%s)' % H2),
    (536, '| RH | **PROVED under `h2`** via SIDE exclusion — `h2` (catalogue exhaustiveness at the ξ interface) open;',
     '| RH | **argued under `h2`** via SIDE exclusion — `h2` (catalogue exhaustiveness at the ξ interface), in its Weil form `h2_sign` '
     'equivalent to RH (%s), open;' % H2),
    (932, '— is not discharged here.',
     '— is not discharged here; in the Euler-balance form it is RH restated (%s), and in its Weil form `h2_sign` it is equivalent to RH (%s).' % (CH, H2)),
    (946, 'RH follows by SIDE Exclusion — conditional on `h2`.**',
     'RH follows by SIDE Exclusion — conditional on `h2`, in its Weil form `h2_sign` equivalent to RH (%s).**' % H2),
    (1044, '*under the exhaustiveness premise `h2`* (`h2` open;',
     '*under the exhaustiveness premise `h2`*, in its Weil form `h2_sign` equivalent to RH (%s) (`h2` open;' % H2),
]
CEIL_RECORD = 'ceiling correction record:'
CARRY_RECORD = 'ceiling read, carried:'
HO = 'the open premise `h2`'
CEILS = [
    (54, 'Ostrowski\'s theorem closes the catalogue', 'Ostrowski\'s theorem closes the place count (n₂ = 3); the catalogue\'s exhaustiveness at the ξ interface is the open premise h2'),
    (73, '**The load-bearing claim:** The seven-class catalogue is exhaustive.',
     '**The load-bearing claim:** The seven-class catalogue closes the place count (n₂ = 3); its exhaustiveness at the ξ interface is %s.' % HO),
    (542, '### 35. RH IS SIMPLE — [ESTABLISHED]', '### 35. THE RH ARGUMENT IS SIMPLE — [ESTABLISHED]'),
    (544, 'The theorem is at rest.', 'The statement is at rest.'),
    (544, 'The proof is pointing at rest.', 'The programme\'s argument is pointing at rest.'),
    (544, 'The difficulty was not the theorem;', 'The difficulty was not the statement;'),
    (895, 'Establishes exhaustiveness of seven-class catalogue.',
     'Closes the place count; the seven-class catalogue\'s exhaustiveness at the ξ interface is %s (the claim-status note above).' % HO),
    (1040, 'Ostrowski\'s theorem closes exhaustiveness → **[PROVED]**',
     'Ostrowski\'s theorem closes the place count (n₂ = 3) → **[PROVED]**; the catalogue\'s exhaustiveness at the ξ interface is %s' % HO),
]
HEADINGS = (542,)
STEM_RECORD = 'banned stem, correction record:'
STEMS = [
    (346, 'the structural gap between identity', 'the structural distance between identity'),
    (562, 'is not a gap to fill;', 'is not an absence to fill;'),
    (696, 'Does the Dense → Equidistributed gap persist uniformly?', 'Does the Dense → Equidistributed difference persist uniformly?'),
    (791, '**Gap:** Step 4 requires', '**Open step:** Step 4 requires'),
    (854, '| Gap at step 4 |', '| Open at step 4 |'),
    (870, 'can\'t close the gap because', 'can\'t close the remaining step because'),
]
NAMES = [894, 895, 919, 921, 922, 923]
NAMES_COUNT = 7
CARRIED = {
    18: 'quoted: the claim-status note quotes the closure`s earlier wording verbatim, as a record',
    20: 'the tag taxonomy described: “the [PROVED] kept, its reason attached”',
    49: 'conditional: “[PROVED under h2 — h2 open]”',
    872: 'a question quoted: the FAQ heading is a reader`s question set in quotation marks, answered beneath',
    892: 'a source document described: CRITICAL RESOLVE`s own role line in the source table',
    898: 'a source document described: the SIDE Exclusion Principle proved in SIDE DOOR, not RH',
}
FACTS = []
VERSION = (11, '**Version 1.6** | 2026-10-01')
READING_NAME = {0: 'none -- resolved by the form', 1: '(a) h2 takes h2_sign'}
CEILING = re.compile(r'RH proved|RH is proved|h2_sign proved|λ_n ≥ 0 proved|GRH proved|GRH reduced|reduction machine-verified|proof of RH|'
                     r'proves RH|RH proves|RH proof|[Pp]roof of GRH|GRH holds|GRH (?:is )?established|RH IS SIMPLE|[Tt]he theorem is at rest|'
                     r'The proof is pointing|closes the catalogue\b|Establishes exhaustiveness|closes exhaustiveness|catalogue is exhaustive\.')
BM_TAG = '<!-- b586 (R196) THE v1.6 EDITION`S BACK MATTER, 2026-10-01 -->'
BANKROWS = (('b538_census.json', 23),)


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _rows():
    return [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'ENUMERA' and r['verdict'] == 'MOVED-IN-MEANING']


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    """### the edition's final line for a current-version line: +2 from :11 (the version line and a blank)."""
    return n + (2 if n >= VERSION[0] else 0)


OFFSET = '+2 from :11 (the Version 1.6 line and a blank, above the Version 1.5 line); no other insertion -- v1.5 :n sits at the edition`s :n+2 for n >= 11'


def _all_changes():
    return REWRITES + CEILS + STEMS + FACTS


def edition(*a):
    """### PLACE-papers phase1.5/method/ENUMERA_v1_6.md, beside the current version from its blob at 7e9b771; the re-pin step run last."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE 7e9b771 -- NOTHING WRITTEN')
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
    if not cur[VERSION[0] - 1].startswith('**Version 1.5** | **51 Findings**'):
        sys.exit('### THE VERSION ANCHOR IS NOT WHERE THE FACE SAYS')
    diff = []
    for r in _rows():
        ln = r['line']
        k = _segs(cur[ln - 1]).index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d] in nw]
        banks = re.findall(r'relay `data/[^`]+` :\d+', nw)
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         reading=1, cites=cites, banks=banks, supports=r['reading']))
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
    bm = ['', BM_TAG, '',
          '## Back matter of the v1.6 edition -- written 2026-10-01 by b586 under the author’s ruling `(R196)`(5), by the form of `(R187)`(5)', '',
          '*This file is v1.6 of ENUMERA, the CP-7 edition written beside v1.5 (`%s`, unedited) from v1.5’s tier block (its :1058, standing: no '
          'Correspondence table naming terminals, every claim T4) and its CP-1b work-list (relay `%s`), the ζ page as its spine; it does not '
          'deposit and does not replace v1.5, and its promotion is CP-8’s. Every line cited below is this file’s own.*' % (CUR, WL), '',
          '### Removals', '', 'None: every one of the 9 work-list rows resolves to a sentence rewritten in place to what its compiled fact says.', '',
          '### Credit lines', '', 'None: the work-list places no CREDIT row and relay `data/b450_batch.json` holds no item for this document.', '',
          '### Stem corrections', '', '| this edition’s line | v1.5 wording | v1.6 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in STEMS:
        bm.append('| :%d | %s %s (banned stem; correction record) | %s | corrected under the stem clause |' % (_edl(ln), STEM_RECORD, old, rep))
    bm += ['', '### Names excepted', '',
           'These lines carry the item labels of the CR document (CRITICAL RESOLVE) as that document numbers and names them; each use carries '
           'unchanged under the name-and-title exception (OPEN_TRAILS :11934), the seat’s reading.', '',
           '| this edition’s line | Status |', '|:--|:--|']
    for n in NAMES:
        bm.append('| :%d | excepted, the object’s own name (an item label of the CR document) |' % _edl(n))
    bm += ['', '### Ceiling corrections', '', '| this edition’s line | v1.5 wording | v1.6 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in CEILS:
        bm.append('| :%d | %s %s | %s | corrected under the ceiling clause%s |' % (_edl(ln), CEIL_RECORD, old, rep,
                                                                                 ', a heading' if ln in HEADINGS else ''))
    bm += ['', '### Ceiling-shaped sentences read and carried', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(CARRIED):
        bm.append('| :%d | %s %s | carried as read |' % (_edl(ln), CARRY_RECORD, CARRIED[ln]))
    bm += ['', '### Fact corrections', '', 'None: the formation count the document prints, (2,3,2,0) = 7, agrees with SIDE-kernel v1.5 '
           '(`Bridge/LocalZeta.lean` :13); the document names no other kernel number (relay `data/b586_reads.txt`).', '',
           '### The navigator’s expectations of `(R196)`(5)', '', '| expectation | the read | Status |', '|:--|:--|:--|',
           '| (a) h2 takes `h2_sign` | 9 rows | rewritten |',
           '| (b) the census’s live uses met by the ceiling clause | 8 corrections, the author’s answer; 4 lines read and carried | corrected |',
           '| (c) T2 terminals | the document names no terminal (its tier block, all T4) | no object |',
           '| (d) counts against kernel facts | the formation count agrees | no correction |',
           '', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v1.6 | `%s` | written at b586 |' % ED,
           '| the current version, v1.5 | `%s` | unedited |' % CUR,
           '| the spine | `%s` at PLACE-papers `%s` | read, unedited |' % (PAGE, MIRROR_PIN),
           '| the work-list | relay `%s` | read |' % WL,
           '| the sentence-by-sentence diff | relay `data/b586_edition_ENUMERA.txt` | banked at b586 |',
           '', '### Correspondence', '',
           '| declaration or bank line | repository | pin as the page prints it | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    ed_lines = {d: [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l and PIN[d] in l] for d in PIN}
    for d in PIN:
        bm.append('| `SIDEExplicitFormula.%s.%s` | %s | %s | %s | cited at :%s of this edition |' % (
            NS[d], d, EF, PIN[d].replace('`', ''), WHERE[d], ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    bank_lines = {}
    for bank, n in BANKROWS:
        at = [i for i, l in enumerate(body, 1) if ('relay `data/%s` :%d' % (bank, n)) in l]
        bank_lines['%s:%d' % (bank, n)] = at
        bm.append('| `data/%s` :%d | relay | the register census (b538) | not on the page | cited at :%s of this edition |' % (
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
    put_json('b586_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=0, removals=0, ruled_citations=0, version_lines=1, diff=diff, offset=OFFSET,
                                       ceils=CEILS, stems=STEMS, facts=FACTS, names=NAMES, names_count=NAMES_COUNT,
                                       carried={str(k): v for k, v in CARRIED.items()}, version=dict(above=VERSION[0], text=VERSION[1]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines,
                                       bank_lines=bank_lines))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))


def edition_bank():
    """### The diff with its offset line, the corrections, the counts, the ceiling read, the scanner's verdict, H28a-H28c."""
    E = jl('b586_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(BM_TAG)
    scan = rd('b586_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    exc = re.search(r'excepted \(back matter\)\s*:\s*names (\d+) ; carried-by-history (\d+)', scan)
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
         'b586 -- COMPONENT 4: THE EDITION OF ENUMERA, (R196)(5), BY THE FORM OF (R187)(5) AND ITS CLAUSES', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :11 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0], cur0[10][:60]),
         '### its tier block : :1058 "%s"' % cur0[1057][:110],
         '### its version history : :1030 onward ("Version History"); the claim-status note :17-:21 (2026-07-19, ARM 3)',
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE WORK-LIST, ROW BY ROW (9 rows, 9 sentences, 9 lines):', '']
    for d in E['diff']:
        L += ['  %s v1.5 :%d -> v1.6 :%d `%s` -- %s ; cites %s%s' % (d['id'], d['line'], d['ed_line'], d['terminal'], READING_NAME[d['reading']],
                                                                 ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']],
                                                                 (' ; bank ' + ', '.join(d['banks'])) if d['banks'] else ''),
              '      work-list: %s' % d['supports'], '      v1.5 : %s' % d['old'], '      v1.6 : %s' % d['new'], '']
    cov = [d for d in E['diff'] if d['reading']]
    L += ['### COVERAGE BY THE EXPECTATIONS OF (R196)(5), the seat`s hand-read: %d of %d rows -- (a) %d' % (len(cov), len(E['diff']), len(cov)), '',
          '### THE CEILING CORRECTIONS (%d, on %d lines; one heading), the author`s answer:' % (len(E['ceils']), len(set(c[0] for c in E['ceils'])))]
    L += ['    v1.5 :%d -> v1.6 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in E['ceils']]
    L += ['### THE CEILING-SHAPED SENTENCES READ AND CARRIED:'] + ['    v1.5 :%d -> v1.6 :%d  %s' % (n, _edl(n), CARRIED[n]) for n in sorted(CARRIED)]
    L += ['### THE STEM CORRECTIONS:'] + ['    v1.5 :%d -> v1.6 :%d  "%s" -> "%s"' % (s[0], _edl(s[0]), s[1], s[2]) for s in E['stems']]
    L += ['### THE NAMES EXCEPTED (the CR document`s item labels; %d uses on %d lines): %s' % (E['names_count'], len(E['names']),
                                                                                              [':%d' % _edl(n) for n in E['names']]),
          '### THE FACT CORRECTIONS: none -- the formation count agrees with SIDE-kernel v1.5 (data/b586_reads.txt)',
          '### THE VERSION LINE: above v1.5 :%d: %s' % (E['version']['above'], E['version']['text']),
          '### REMOVALS: none. ### CREDIT LINES: none.', '',
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
          '### THE SCANNER (banned_terms.py, reading the back matter since Component 1) on the edition: live uses %s ; excepted names %s, '
          'carried-by-history %s ; verdict %s' % (live_n, exc.group(1) if exc else '?', exc.group(2) if exc else '?', 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on the page at its pin, or a bank line%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s live count %s and verdict %s; sentences beyond the ceiling %d.**' % (
              h28c, live_n, 'CLEAN' if clean else 'NOT CLEAN', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b586_edition_ENUMERA.txt', L)
    put_json('b586_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=live_n, excepted_names=int(exc.group(1)) if exc else None,
                                   excepted_history=int(exc.group(2)) if exc else None, clean=clean, beyond=len(beyond), hits=hits,
                                   covered=len(cov), uncovered=[d['id'] for d in E['diff'] if not d['reading']], held=None,
                                   n_ceils=len(E['ceils']), n_ceil_lines=len(set(c[0] for c in E['ceils'])), n_facts=len(E['facts'])))
    H = jl('b586_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'covered', H['covered'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'],
          'live', H['live'], 'ceils', H['n_ceils'])


# ================================================================================ THE SCORING AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}


def scores():
    H, E, SC, C = jl('b586_h28.json'), jl('b586_edition.json'), jl('b586_scanner.json'), jl('b586_corroboration.json')
    ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'ls-files', '--others', '--exclude-standard', 'phase1.5', 'phase2')).split(NL) if x.strip()))
    kmain = g('D:/SIDE-explicit-formula', 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    cur_same = g(PP, 'hash-object', CUR).strip() == E['cur_blob']
    n3 = H['H28a'] == 'HELD' and H['H28b'] == 'HELD' and H['H28c'] == 'HELD' and H['held'] is None
    allowed_pp = {'FINDINGS.md', 'OPEN_TRAILS.md', ED}
    rs = SC['rescans']
    n1 = all(v['verdict'] == 'CLEAN' and v['live'] == 0 for v in rs.values()) and SC['test_exit'] == 0 and 'MUTANT NOT CLEAN' in SC['test_out']
    S = dict(
        N1=('HELD' if n1 else 'REFUTED', 'after the change: %s ; the test exit %d, its mutant %s' % (
            {os.path.basename(k): '%s (live %d)' % (v['verdict'], v['live']) for k, v in rs.items()}, SC['test_exit'],
            'NOT CLEAN' if 'MUTANT NOT CLEAN' in SC['test_out'] else '### NOT SHOWN')),
        N2=('HELD' if sorted(C['no_table']) == ['E_DIFFICULTY_THEOREM', 'TECHNE_TOOLKIT'] and len(C['unread']) >= 10 else 'REFUTED',
            'documents with no table: %s ; not re-read by constellation mode since b566: %d' % (C['no_table'], len(C['unread']))),
        N3=('HELD' if n3 else 'REFUTED', 'H28a %s, H28b %s (the body %+d against at most %d), H28c %s; no sentence held' % (
            H['H28a'], H['H28b'], H['body_dn'], H['allowed'], H['H28c'])),
        N4=('HELD' if 5 <= H['n_ceils'] <= 9 else 'REFUTED', 'the ceiling clause corrects %d phrases on %d lines' % (H['n_ceils'], H['n_ceil_lines'])),
        N5=('HELD' if (kmain == V015 and heads_ok and cur_same and set(ch) <= allowed_pp) else 'REFUTED', 'nothing deposits; no kernel '
            'touched (%s); the current ENUMERA unedited (%s); PLACE-papers changed at %s; the scanner and its test, the census, relay banks' % (
                'held' if kmain == V015 and heads_ok else '### MOVED', 'held' if cur_same else '### EDITED', ch)),
        S1=('HELD' if n1 else 'REFUTED', '(N1) holds'),
        S2=('HELD' if sorted(C['no_table']) == ['ENUMERA', 'E_DIFFICULTY_THEOREM', 'THE_KEYSTONE_CENSUS'] and len(C['unread']) >= 10 else 'REFUTED',
            '(N2) refuted on its first half: TECHNE_TOOLKIT carries a table under its Correspondence heading (b450`s matcher read only '
            'headings beginning "## Correspondence"), and ENUMERA and THE_KEYSTONE_CENSUS carry none; its second half holds'),
        S3=('HELD' if n3 and H['body_dn'] == 1 and H['allowed'] == 1 else 'REFUTED', 'H28a-H28c held; the body +1 against 1'),
        S4=('HELD' if H['n_ceils'] == 8 else 'REFUTED', '(N4) holds at 8'),
        S5=('HELD' if set(ch) == allowed_pp else 'REFUTED', '(N5) holds: the PLACE-papers files changed are the three its list names'),
        counts=dict(pp_changed=ch, body_dn=H['body_dn'], ceils=H['n_ceils'], no_table=C['no_table'], unread=len(C['unread'])),
    )
    put_json('b586_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], S[k][1][:170]))


TITLE_HEAD = ('## CP-7, act eleven: the edition of ENUMERA from its tier block and work-list; the corroboration census over the roster; the '
              'scanner reading the form’s exceptions')
TITLE = TITLE_HEAD + '; written as v1.6 beside v1.5, no sentence held'
TRAIL_HEAD = ('### b586 — lane three, act fourteen under (R196): CP-7 act eleven -- the edition of ENUMERA written beside the current; the '
              'scanner taught the exceptions; the corroboration census; lane three’s order refined')


def records_pp():
    Q = _Q()
    S, H, E, C1, C, SC, O = (jl('b586_scores.json'), jl('b586_h28.json'), jl('b586_edition.json'), jl('b586_c1_lines.json'),
                             jl('b586_corroboration.json'), jl('b586_scanner.json'), jl('b586_order.json'))
    Q.guard_absent(Q.FIND, TITLE_HEAD)
    e = ['', TITLE, '',
         '*Filed at b586 on the author’s ruling `(R196)`. Banks: relay `data/b586_edition_ENUMERA.txt` (the sentence-by-sentence diff, its '
         'offset line at its head), `data/b586_edition.json`, `data/b586_corroboration.txt`, `data/b586_scanner.txt`, `data/b586_reads.txt`. '
         'Nothing deposits.*', '',
         '**The edition** (`(R196)`(5)): `%s`, v1.6, written beside v1.5 (`%s`, unedited) from v1.5’s tier block and its CP-1b work-list, the '
         'ζ page as its spine. The 9 work-list rows resolve to 9 sentences, each rewritten in place: the closure’s premise named in its Weil '
         'form and cited to its equivalence with RH, the Euler-balance form cited as RH restated, the registers once read as one premise '
         'cited as the separate statements they are. Eight phrases beyond the ceiling are corrected, as the author answered: the heading and '
         'the paragraph that spoke of RH as a theorem at rest, and four sites asserting the catalogue’s exhaustiveness, each now naming the '
         'place count Ostrowski closes and the exhaustiveness at the ξ interface that stays the open premise. Six stem uses are corrected and '
         'seven item labels excepted as names. The document names no terminal, so no fact moves. No sentence is removed and none held.' % (ED, CUR), '',
         '**The counts.** v1.5 %d sentences; v1.6 %d (the body %d, the back matter %d); the body differs by %+d against the final bound, %d.'
         % (E['n_cur'], E['n_full'], E['n_body'], E['n_backmatter'], H['body_dn'], H['allowed']), '',
         '**H28a %s · H28b %s · H28c %s.** The scanner reads the edition %s.' % (H['H28a'], H['H28b'], H['H28c'], 'CLEAN' if H['clean'] else 'NOT CLEAN'), '',
         '**The scanner** (`(R196)`(2)): relay `tools/banned_terms.py` reads an edition’s back matter and reports a use listed there as an '
         'excepted name or title, or as carried-by-history, as EXCEPTED and not live; committed alone with its test. Re-scanned: %s.' % (
             '; '.join('%s %s' % (os.path.basename(k), v['verdict']) for k, v in SC['rescans'].items())), '',
         '**The corroboration census** (`(R196)`(3), a bank and no edit): documents with no table %s; documents whose tables no '
         'constellation-mode run has re-read since b566, %d of them -- no act from b566 on ran that mode.' % (C['no_table'], len(C['unread'])), '',
         '**The record lines** (`(R196)`(1), (4)): b585’s weight (FINDINGS :%d); lane three’s refined order (OPEN_TRAILS :%d).' % (
             C1['lines']['weight'], O['line']), '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R196)`(6): the edition of EXHAUSTIVENESS_LICENSE by the same form; the author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; v1.5, README, REGISTRY, ERRATA and both pages unwritten; nothing here is a statement about RH, '
         'GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R196) ratified.** (1) b585 at its weight, the two pin corrections accepted. (2) The stem scanner taught the form’s exceptions. '
             '(3) The corroboration census over the roster, a bank. (4) Lane three’s order refined. (5) The edition of ENUMERA by the form. (6) '
             'The act after.', '',
             '**Entered:** FINDINGS.md:%d (b585’s weight), :%d (the entry); OPEN_TRAILS.md:%d (lane three’s order), this record; PLACE-papers '
             '`%s` (created); relay `tools/banned_terms.py` and its test (committed alone), `data/b586_corroboration.txt`.' % (
                 C1['lines']['weight'], Q.line_of(Q.FIND, TITLE_HEAD), O['line'], ED), '',
             '**Answered before the seal, by the author:** ENUMERA’s ceiling reaches both kinds -- RH as a settled theorem (:542, :544) and the '
             'catalogue’s exhaustiveness asserted as proved (:54, :895, :1040; :73 of the same shape, named by the seat).', '',
             '**A reading on the ceiling clause, the author’s:** the pair “census proved / exhaustiveness open” -- Ostrowski’s theorem closes '
             'the place count (n₂ = 3), while the catalogue’s exhaustiveness at the ξ interface is the open premise `h2`, as ENUMERA’s '
             'claim-status note at its :18-:21 states; entered here “since the same shape will recur in EXHAUSTIVENESS_LICENSE next”.', '',
             '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
             % tuple(S[k][0] for k in SCORE_KEYS), '',
             '**For the author:** the seven uses in ENUMERA that are the CR document’s own item labels (:896, :897, :921, :923-:925 of the '
             'edition) are excepted as names under the name-and-title exception, the seat’s reading and not asked; strike it and they take the '
             'stem clause.', '',
             '**Next:** per `(R196)`(6), CP-7 act twelve, b587 -- the edition of EXHAUSTIVENESS_LICENSE by the same form, H28a-H28c scored; '
             'the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
             'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b586_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE_HEAD), title=TITLE, append=r))
    put_json('b586_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r2))
    print(jl('b586_findings.json')['entry_line'], jl('b586_trail.json')['line'])


def desk():
    S = jl('b586_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b586 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b586_defects.txt').rstrip(NL).split(NL)
    put_txt('b586_desk_notes.txt', L)


def components():
    S, H, C1, fj, tj, C, O = (jl('b586_scores.json'), jl('b586_h28.json'), jl('b586_c1_lines.json'), jl('b586_findings.json'),
                              jl('b586_trail.json'), jl('b586_corroboration.json'), jl('b586_order.json'))
    L = ['b586 -- THE COMPONENTS, BANKED UNDER (R196).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b585`s closing push-out relay 05087ba9 ; push-b585* branches deleted by name '
         '(data/b586_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : tools/banned_terms.py reads the back matter, committed alone with tools/test_banned_terms_backmatter.py ; '
         'data/b586_scanner.txt ; b585`s weight FINDINGS :%d ; N1 %s' % (C1['lines']['weight'], S['N1'][0]),
         '### COMPONENT 2 : data/b586_corroboration.txt ; no table %s ; not re-read since b566 %d ; N2 %s' % (C['no_table'], len(C['unread']), S['N2'][0]),
         '### COMPONENT 3 : lane three`s order OPEN_TRAILS :%d' % O['line'],
         '### COMPONENT 4 : the edition %s ; 9 sentences rewritten, %d ceiling and 6 stem corrections, 7 names excepted, the version line, 0 '
         'removals ; data/b586_edition_ENUMERA.txt ; H28a %s H28b %s H28c %s ; N3 %s N4 %s' % (
             ED, H['n_ceils'], H['H28a'], H['H28b'], H['H28c'], S['N3'][0], S['N4'][0]),
         '### COMPONENT 5 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; next: the edition of EXHAUSTIVENESS_LICENSE ; N5 %s'
         % (fj['entry_line'], tj['line'], S['N5'][0])]
    put_txt('b586_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b586_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
