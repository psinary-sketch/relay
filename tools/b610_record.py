# -*- coding: utf-8 -*-
"""b610_record.py -- THE ACT'S RECORD TOOL, UNDER (R220). ### ONE SUBCOMMAND PER BANK.

### ### b610: LANE THREE, ACT THIRTY-SEVEN -- THE PHASE-STATE READING: THE_KEYSTONE_CENSUS AT v0.3 AS ONE ROW PER PHASE AND
### CLUSTER, READ FROM THE LEDGERS, THE PAGES, THE REGISTRY AND THE REMOTES; THE KEYSTONE TEST RULED; SPIRAL_MAP AT v0.7 POINTING TO THE
### ROWS. Subcommands write only `data/b610_*` unless the docstring names another file. Every bank is written through b602_record's
### `put_txt` / `put_json` (encode, temp file, `os.replace`), imported, never copied; every ledger append through b566's guarded
### `append_to`. The act's data and resolvers are tools/b610_census.py's. No platform call. No Lean call: both pages are re-emitted from
### their banked probes. The templates are tools/b609_record.py and tools/b604_record.py (the reorganising edition).
"""
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b604_record as R4  # noqa: E402
import b610_census as C  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
RELAY = ROOT.replace('\\', '/')
PRE_PP = C.PRE_PP
PRE_RELAY = 'd121b88f'
STEPZERO = C.STEPZERO
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/8f2ff82c-2889-4443-a8e7-85de4d1b215f/scratchpad'
SESSION_ID = '8f2ff82c-2889-4443-a8e7-85de4d1b215f'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
CEN, CEN3, SPI, SPI7 = C.CENSUS, C.CENSUS3, C.SPIRAL, C.SPIRAL7

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
# ### `dry` anywhere on the command line routes every b610 bank's read and write to the seat's scratchpad, outside every repository
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail')   # ### for these two, `dry` prints and appends nothing
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b610_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b610_') else '', name, len(b)))
    return b


def put_json(name, obj):
    put_txt(name, [json.dumps(obj, indent=1, ensure_ascii=False)])


def jl(name):
    import io
    return json.load(io.open(_p(name), encoding='utf-8'))


def rd(name):
    import io
    p = _p(name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''
_show = R4._show
CEILING = R4.CEILING


def _segs(l):
    return R4._segs(l)


def _count(ls):
    return sum(len(_segs(l)) for l in ls)


def _cell(s):
    return s.replace('|', '¦')


DEFECTS = [
    '(a) THE SEAT`S, BEFORE THE SEAL: five replacements in this act`s own unsealed record tool (tools/b610_record.py -- routing the '
    'addendum check, the two edition banks and the trail check through the dry switch) were made by a python script passed through a '
    'bash heredoc, where the ferry`s procedural line orders unsealed tools edited through the Edit tool and not a heredoc. Each '
    'replacement was guarded to match exactly once, and each landed: the five lines were read back by grep, the file parses, and it '
    'carries no carriage return. Every later edit of the act`s tools went through the Edit tool.',
    '(b) THE SEAT`S, IN THE SUITE, FOUND AT THE PRE-PUSH RUN: G-SPIRAL-CARRIES` positive control appended to v0.7`s line 40, whose text '
    '(a table header) occurs twice in the file, so the arm still found v0.6`s line and passed its positive control (the harness marked it '
    'DEFECTIVE and G-ARMS-NO-LIVE-LIMB failed with it). Re-pointed through the Edit tool at line 20, v0.6`s version line, which occurs '
    'once; the suite re-run whole.',
    '(c) THE SEAT`S, IN THE SUITE, FOUND AT THE PRE-PUSH RUN: G-SPIRAL-POINTERS read the line two above the census rows` head line for the '
    'blank that precedes it, where the blank is the line directly above (v0.7 :278); the pointing lines themselves matched the census '
    'bank`s recomputation exactly. The index corrected through the Edit tool; the suite re-run whole.',
]
DEFECT_SHORT = ['(a) the seat’s, before the seal: five replacements in the act’s own record tool made through a heredoc script, not the '
                'Edit tool -- each matched once and was read back; later edits through the Edit tool',
                '(b) the seat’s: G-SPIRAL-CARRIES’ positive control mutated a line whose text recurs, so it passed -- re-pointed at a line that '
                'occurs once', '(c) the seat’s: G-SPIRAL-POINTERS read the wrong neighbour line for its blank -- the index corrected; the suite '
                're-run whole']


def defects():
    L = ['b610 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b610_defects.txt', L)


# ================================================================================ READING (1): THE READS
READS = [
    ('REGISTRY.md whole: its phase sections, rows, tier legend, version-log additions, deposit records and kernel blocks', PP, PRE_PP,
     'REGISTRY.md', 'ALL', 240),
    ('THE_KEYSTONE_CENSUS.md whole, the current version: its §0 test, §1 anomalies, its rows, the v0.2 section and its appended lines',
     PP, PRE_PP, CEN, 'ALL', 400),
    ('THE_DOCUMENT_CLASS_TAXONOMY.md whole: the tier definitions (:14-:20), the presumptive classes (:34-:37), the ruled borderlines '
     '(:39-:43) and (R19)`s KC (:55-:69)', PP, PRE_PP, 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', 'ALL', 400),
    ('SPIRAL_MAP.md: its head and version line, §1`s core list, §1.2`s heading and paragraph, §4A whole as b388 refreshed it, the ceiling '
     'and stem lines', PP, PRE_PP, SPI, list(range(1, 31)) + [62, 89, 98, 102, 104, 115, 148, 403, 439, 443, 488] + list(range(229, 325)), 400),
    ('OPEN_TRAILS: b375`s block (the three tests, the six clusters), (R17)`s block (b388), the form and its clauses, the reorganising '
     'clause, the multiple-act clause, b609`s lines and record', PP, PRE_PP, 'OPEN_TRAILS.md',
     list(range(4047, 4092)) + list(range(4391, 4420)) + [11864, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 12190, 12192,
                                                          12194, 12228, 12456, 12496, 12542, 12544, 12546, 12548, 12550], 1200),
    ('FINDINGS: b609`s record lines and entry', PP, PRE_PP, 'FINDINGS.md', [7182, 7184, 7186], 600),
    ('the sieve at v0.4: its clusters paragraph, its verdict head and every cluster heading', PP, PRE_PP, C.SIEVE4,
     ('GREP', r'^## |^5 of them|^The clusters are'), 400),
    ('README.md: the ceiling (:106-:121)', PP, PRE_PP, 'README.md', list(range(104, 112)), 400),
    ('the ζ page: its pin line and its Placement', PP, PRE_PP, PAGE, ('GREP', r'^This page is generated|^\| keystone naming a node|^## Placement'), 260),
    ('the χ page: its pin line and its Placement', PP, PRE_PP, DIR_PAGE, ('GREP', r'^This page is generated|^\| keystone naming a node|^## Placement'), 260),
    ('relay tools/mirror_roster.json (the mirror`s roster)', RELAY, STEPZERO, 'tools/mirror_roster.json', 'ALL', 400),
    ('relay data/b609_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b609_closing_push_out.txt', 'ALL', 260),
    ('relay data/b609_scores.json (whole)', RELAY, STEPZERO, 'data/b609_scores.json', 'ALL', 300),
    ('relay data/b577_edition_order.txt (the edition order and the roster`s no-list set)', RELAY, STEPZERO, 'data/b577_edition_order.txt', 'ALL', 200),
]


def reads():
    L = ['b610 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS:
        t = _show(repo, rev, path)
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH LINE (the blob does not exist)' % (label, path, at))
            continue
        sl = t.split(NL)
        if sl and sl[-1] == '':
            sl = sl[:-1]
        if sel == 'ALL':
            nums = [i + 1 for i, l in enumerate(sl) if l.strip()]
        elif isinstance(sel, tuple):
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    T = json.loads(_show(RELAY, STEPZERO, 'data/terminal_table.json') or '{}')
    L += ['', '### relay data/terminal_table.json @ %s: %d rows over %d repositories named; the rows carry no document column, so the census '
          'reads certification from the documents` own tier blocks (C.tier_block), not from the table' % (STEPZERO, len(T.get('rows') or []),
                                                                                                       T.get('repos_named') or 0),
          '### relay data/b558_editions/ @ %s: %s' % (STEPZERO, sorted(x.split('/')[-1] for x in g(RELAY, 'ls-tree', '--name-only', STEPZERO,
                                                                                                      'data/b558_editions/').split(NL) if x.strip())),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                       g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()),
          '### a fact correction to the ruling`s letter, the navigator`s: (R220)(3) writes "Tier E errata-class"; the author-ruled taxonomy '
          'defines Tier E as filing-facing (THE_DOCUMENT_CLASS_TAXONOMY :20, "written for counsel or a patent examiner"), and the census '
          'quotes the taxonomy`s definition']
    put_txt('b610_reads.txt', L)


# ================================================================================ THE AUTHOR'S ANSWERS
def answers():
    import io
    calls, results = [], {}
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            try:
                o = json.loads(raw)
            except Exception:
                continue
            m = o.get('message') or {}
            for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
                if not isinstance(c, dict):
                    continue
                if c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                    calls.append((i, c['id'], c['input']))
                if c.get('type') == 'tool_result':
                    t = c.get('content')
                    t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t
                    results[c.get('tool_use_id')] = (i, t)
    n = sum(len(c[2].get('questions', [])) for c in calls)
    L = ['### b610 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat (2026-10-03), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % n, '']
    k = 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, SESSION_ID, i))
        for q in inp.get('questions', []):
            k += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'), op.get('description')))
        ri, rt = results.get(cid, (None, '### NO RESULT FOUND'))
        L += ['RESULT (transcript line %s): %s' % (ri, rt), '']
    if not calls:
        L.append('### NONE: no prompt was put to the author in this act; the precedence order and the ruling`s letter reached every '
                 'reading, each declared on the face and strikeable.')
    put_txt('b610_author_answers.txt', L)


# ================================================================================ COMPONENT 1: THE ADDENDUM AND THE RECORD LINES
# ### (R220)(2): the second reader's addendum, every candidate of four matchers read by hand in its line. KIN: the line attributes the
# ### Euler product's content (the product, its factors, unique factorization, its zero-free region, the confinement, the prime sum) to
# ### C₂ or to the enumeration's step; NOT: C₂ named by its label alone, the compiled condition itself, or test 2's own instrument.
KIN, NOT = 'KIN', 'NOT KIN'
M17 = C.M17
ADD_MARKS = {
    ('clusters/IDENTITY_FORMATION_BIJECTION_CLUSTER_SYNTHESIS_2026-05-19.md', 17): (KIN, 'the classes said to be the classical tools, the Euler product among them'),
    ('clusters/RH_CASCADE_CLUSTER_SYNTHESIS_2026-05-19.md', 120): (KIN, 'reports a paper arguing the classes are the tools, Euler products among them'),
    ('clusters/RH_CASCADE_CLUSTER_SYNTHESIS_2026-05-19.md', 180): (KIN, 'the Euler/multiplicative class (C₂) said to govern the prime sum'),
    (M17, 848): (KIN, 'unique factorization and the Euler product assigned to C₂'),
    (M17, 870): (NOT, 'the class`s label in a tree, no content attributed'),
    (M17, 890): (KIN, 'the table gives C₂`s source as the multiplicative structure (Euler product)'),
    (M17, 905): (KIN, 'C₂ named as the Euler product`s balance; the compiled condition carries no product'),
    (M17, 931): (KIN, 'the zero-free region from σ = 1 assigned to C₂ (Euler product)'),
    (M17, 938): (NOT, 'the label and the balance equation, the compiled condition`s own content'),
    (M17, 945): (KIN, 'the Euler product read as the class Epstein lacks, separating the classes'),
    (M17, 984): (NOT, 'a method`s row naming C₂ by its label'),
    (M17, 985): (KIN, 'the explicit formula`s row: prime sums via the Euler product, set under C₂'),
    (M17, 987): (NOT, 'a method`s row naming C₂ by its label'),
    (M17, 989): (NOT, 'a method`s row naming C₂ by its label'),
    (M17, 991): (NOT, 'a method`s row naming C₂ by its label'),
    (M17, 993): (NOT, 'a method`s row naming C₂ by its label'),
    (M17, 1063): (NOT, 'a path`s row naming C₂ by its label'),
    (M17, 1065): (NOT, 'a path`s row naming C₂ by its label'),
    (M17, 1097): (KIN, 'the Euler product said to be mechanism class C₂'),
    (M17, 1099): (KIN, 'the Euler product (C₂) said to provide the confinement'),
    (M17, 1168): (KIN, 'the enumeration`s step (7): the Euler product said to identify σ = 1/2'),
    (M17, 1198): (KIN, 'removing C₂ read as removing the Euler product'),
    (M17, 1214): (KIN, 'the reduction`s enumeration said to apply results from the Euler product on'),
    (M17, 1218): (KIN, 'C₂ glossed as the Euler product`s identification of σ = 1/2'),
    (M17, 1392): (KIN, 'C₂ named as the Euler product'),
    (M17, 1491): (KIN, 'the per-class answer: the Euler product said to provide the balance'),
    (M17, 1622): (NOT, 'the compiled condition itself, ∃ σ ≠ 1/2, −σ = −(1 − σ), at its label'),
    (M17, 1884): (KIN, 'Epstein said to lack C₂ (Euler product)'),
    (M17, 1888): (KIN, 'the multiplicative monoid said to produce C₂ (the Euler product)'),
    ('internal/CATALOGOS.md', 129): (KIN, 'C₂`s row carries the product formula ζ(s) = ∏(1-p⁻ˢ)⁻¹'),
    ('internal/CATALOGOS.md', 157): (KIN, 'the Euler product written as C₂'),
    ('internal/CATALOGOS.md', 162): (KIN, 'the zero-free region from σ = 1 assigned to C₂'),
    ('internal/CATALOGOS.md', 759): (KIN, 'the enumeration`s completeness answered by removing the Euler product'),
    ('phase1.5/method/INVARIANCE_BARRIERS_v1_4.md', 23): (NOT, 'test 2`s own instrument: the toolkit with the Euler product excluded'),
    ('phase1.5/method/INVARIANCE_BARRIERS_v1_4.md', 49): (NOT, 'test 2`s own instrument: the toolkit with the Euler product excluded'),
    ('phase1.5/method/INVARIANCE_BARRIERS_v1_4.md', 356): (NOT, 'test 2`s own instrument: Theorem 3.7'),
    ('phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md', 99): (KIN, 'the Euler path touching C₂, said to close under the catalogue'),
    ('phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', 35): (KIN, 'covers_all said to transport the Euler product`s per-prime independence'),
    ('phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', 77): (NOT, 'the class`s label in a table'),
    ('phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', 92): (KIN, 'C₂ said to pair the Euler factors'),
    ('phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', 153): (KIN, 'the Euler zero-free region assigned to C₂'),
    ('phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 26): (KIN, 'the Euler product said to be essential to the mechanism-exclusion argument'),
    ('phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 116): (NOT, 'the kernel enumeration`s labels listed'),
    ('phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 120): (KIN, 'C₂`s contribution said to come from the Euler product expansion'),
    ('phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 124): (NOT, 'the label and the balance identity, the compiled condition`s content'),
    ('phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 323): (KIN, 'the mechanism enumeration said to carry an Euler-product class'),
    ('phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 369): (KIN, 'the Euler product said to be essential to off-line exclusion against the catalogue'),
    ('phase1.5/spectral/BALANCE_AND_POSITIVITY_v0_9_5.md', 272): (KIN, 'the table gives C₂`s source as the multiplicative structure (Euler product)'),
    ('phase1.5/spectral/GRH_CASCADE_v0_3_6.md', 51): (KIN, 'the classes said to transfer where the Euler product is active'),
    ('phase1.5/spectral/GRH_CASCADE_v0_3_6.md', 113): (NOT, 'the kernel enumeration`s labels listed'),
    ('phase1.5/spectral/GRH_CASCADE_v0_3_6.md', 130): (KIN, 'C₂ glossed as the Euler product, said to carry χ(p)'),
    ('phase1.5/spectral/GRH_CASCADE_v0_3_6.md', 157): (KIN, 'the balance constraint said to come from the Euler product / the enumeration'),
    ('phase2/formation/UNIVERSALITY.md', 42): (KIN, '(C₂) said to be unique factorization giving the Euler product'),
    ('phase2/formation/UNIVERSALITY.md', 160): (KIN, 'the primes said to act through the Euler product (C₂)'),
    ('phase2/formation/UNIVERSALITY.md', 162): (KIN, 'the Euler product class C₂ named'),
}
ADD_MATCHERS = [
    ('A1', 'the line names C₂ and Euler', re.compile(r'(?=.*(?:C₂|C_2|C_\{2\}|\bC2\b|C2_euler))(?=.*Euler)')),
    ('A2', 'the line names the enumeration or the classes and the Euler product', re.compile(
        r'(?=.*(?:enumerat|seven (?:mechanism )?classes|mechanism class|seven-class))(?=.*Euler product)')),
    ('A3', 'the line names the Euler product, an exclusion and a class', re.compile(r'(?=.*Euler product)(?=.*(?:exclu|rules? out))(?=.*class)')),
    ('A4', 'a sentence naming Euler, C₂ or the enumeration, with uses/requires/carries', C.ADD_RE),
]


def _add_docs(B):
    return sorted(set(C.latest(r['path']) for r in B['rows'] if r['tier'] in C.KEYSTONE_TIERS and r['path'] in C.tracked()))


def add_hits(B):
    out = []
    for p in _add_docs(B):
        ls = C.lines_of(C.show(p))
        if p == M17:
            ls = ls[:next(i for i, l in enumerate(ls) if l.startswith('## Correspondence'))]
        for i, l in enumerate(ls):
            ms = [mid for mid, _d, rx in ADD_MATCHERS if rx.search(l)]
            if ms:
                out.append((p, i + 1, ms, l))
    return out


def addendum(*a):
    """### data/b610_residue_addendum.txt and .json: (R220)(2)'s addendum to the batch's seed (data/b609_residue_seed.txt's KIN),
    ### banked beside it -- the prior bank is not edited."""
    B = C.build()
    hits = add_hits(B)
    un = [(p, n) for p, n, _m, _l in hits if (p, n) not in ADD_MARKS]
    gone = [k for k in ADD_MARKS if k not in set((p, n) for p, n, _m, _l in hits)]
    if un or gone:
        sys.exit('### UNREAD CANDIDATES %s ; MARKS WITH NO CANDIDATE %s -- NOTHING WRITTEN' % (un, gone))
    L = ['b610 -- THE SECOND READER`S ADDENDUM, (R220)(2): every monograph and keystone sentence saying the enumeration "uses" or '
         '"requires" the Euler product, or that C₂ carries it, banked %s' % utc(),
         '### ADDRESSED to the batch`s seed, relay data/b609_residue_seed.txt, its KIN marks (OPEN_TRAILS :12542); that bank is a prior '
         'bank and is not edited -- this addendum is banked beside it, as a ledger`s append is addressed to its line',
         '### the documents read: the monograph`s current version %s (its body, every line above its Correspondence heading) and every '
         'keystone the census reads at K, KC or C, each at its newest version at PLACE-papers %s -- %d documents' % (M17, PRE_PP, len(_add_docs(B))),
         '### the reading it answers to, (R220)(2): as compiled, the seven-class exclusion is a family of σ-conditions (SIDE-kernel v1.5, '
         'Bridge/TheBridgeComplete.lean :157-:159; C₂_euler`s condition σ ≠ 1/2 ∧ −σ = −(1 − σ)), and the prime side enters the compiled '
         'star at the explicit formula, not at the classes',
         '### the marks: KIN -- the line attributes the Euler product`s content (the product, its factors, unique factorization, its '
         'zero-free region, the confinement, the prime sum) to C₂ or to the enumeration`s step; NOT KIN -- C₂ named by its label alone, the '
         'compiled condition itself, or test 2`s own instrument; no sentence is rewritten by this bank', '']
    for mid, desc, rx in ADD_MATCHERS:
        L.append('### MATCHER %s (%s): %d lines' % (mid, desc, sum(1 for _p, _n, ms, _l in hits if mid in ms)))
    L += ['### the union, read by hand: %d lines' % len(hits), '']
    rows = []
    for p, n, ms, l in hits:
        mark, why = ADD_MARKS[(p, n)]
        rows.append(dict(path=p, line=n, matchers=ms, mark=mark, why=why))
        L.append('  %s :%-5d %-7s %s -- %s' % (p, n, mark, '+'.join(ms), why))
        L.append('          “%s”' % l.strip()[:600])
    k = sum(1 for r in rows if r['mark'] == KIN)
    L += ['', '### ### **THE ADDENDUM: %d lines read -- KIN %d ; NOT KIN %d ; unmarked 0.**' % (len(rows), k, len(rows) - k)]
    put_txt('b610_residue_addendum.txt', L)
    put_json('b610_residue_addendum.json', dict(at=utc(), n=len(rows), kin=k, docs=_add_docs(B), rows=rows))
    print(L[-1])


B609_ENTRY = '## The sieve at v0.4 with the computational range, GUE statistics and the mechanism enumeration as rows'
B375_HEAD = '### **b375 — THE KEYSTONE AND CLUSTER CENSUS (2026-09-08)**'
BATCH_LINE = '*Appended 2026-10-03 by b609 to W-ORD-SECOND-READER (:12212), under `(R219)`(2)(iv) -- THE BATCH NAMED AND THE SEED BANKED'
PHASE_LINE = '*Appended 2026-10-03 by b609 to b375’s keystone and cluster census (:4049), under `(R219)`(4) -- A PHASE-STATE READING'
W_HEAD = '*Appended 2026-10-03 by b610 to b609’s entry (:%d), under `(R220)`(1) -- b609 AT ITS WEIGHT, THE NAVIGATOR’S BRIGHT REFUTED:*'
E_HEAD = '*Appended 2026-10-03 by b610 to b609’s entry (:%d), under `(R220)`(2) -- THE ENUMERATION’S COMPILED FORM, A READING FOR THE RECORD:*'
T_HEAD = ('*Appended 2026-10-03 by b610 to b375’s keystone and cluster census (:%d) and to b609’s phase-state line (:%d), under `(R220)`(3) '
          '-- THE KEYSTONE TEST, RULED; b375’S ITEM CLOSED:*')
S_HEAD = '*Appended 2026-10-03 by b610, under `(R220)`(5), the author’s explicit ask -- THE SYNTHESIS SEQUENCE, ENTERED WITH ITS FORM:*'


def _b609():
    S = json.loads(_show(RELAY, STEPZERO, 'data/b609_scores.json'))
    return {k: v[0] for k, v in S.items()}


def _texts(entry, b375, pline, batch):
    s = _b609()
    h1, h2, h3, h4 = W_HEAD % entry, E_HEAD % entry, T_HEAD % (b375, pline), S_HEAD
    t1 = ('\n%s THE_FINDINGS_AS_THEY_STAND v0.4 (PLACE-papers b4eecfb), beside v0.3 unedited: RH-58 the computational range NOT A ROUTE; '
          'RH-59 GUE statistics DARK by test 1; RH-60 the mechanism enumeration DARK by test 2 -- the detector (Detector.lean :99) names no '
          'mechanism class, the compiled exclusions at SIDE-kernel v1.5 (TheBridgeComplete.lean :157-:159) are conditions on a real σ alone, '
          'C₂_euler’s being σ ≠ 1/2 ∧ −σ = −(1 − σ) with no Euler product in it, and the step from the classes to ξ’s zeros is '
          'Integration’s StructuralExhaustiveness (:213), RH restated; the navigator’s BRIGHT is refuted by the kernel’s own statements and '
          'recorded as such. FD-01 and FD-02 two rows, FD-02 naming no zero, so (N2)’s stated reason is the navigator’s. The head at 87 rows: '
          '2 BRIGHT, 7 DARK, 67 NOT A ROUTE, 11 FACE; re-pin 326 of 326. A_Place_to_Stand v5.17 (103b2bd), beside v5.16 unedited: §24.4’s '
          'four cells to the v0.4 rows, §25.8’s opening row `_root_.structural_exhaustiveness_proved`, the version line; re-pin 496 of 496; '
          'the 72 carried hits standing, 0 unexcepted. The verdicts, as relay data/b609_scores.json prints them: H28a-H28c %s, %s, %s for '
          'the sieve and %s, %s, %s for the monograph; H43a %s, H43b %s, H43c %s (by the version line, the navigator’s bound), H43d %s; N1 '
          '%s, N2 %s, N3-N5 %s; S1-S5 %s. The second reader’s batch read as the five editions in being at `(R219)`, accepted; its seed '
          'banked (42 candidates: 16 kin, 6 proof labels, 3 dated, 17 not kin); relay data/housekeeping_terminal_table.txt opened with '
          'H-TT-1; the §24.4 header and the analytic row’s cell standing under “nothing else”, accepted; the ferry’s “b608’s diff bank” for '
          'the residue list the navigator’s. FINDINGS :7182, :7184, :7186; OPEN_TRAILS :12542, :12544, :12546; the pages c686d09, 1e450c9. '
          'The suite 90 of 90 before and after the push. Defect (a) the seat’s; the refused push re-pushed under rule 14. Nothing deposited; '
          'no kernel touched.\n' % (h1, s['H28a-SIEVE'], s['H28b-SIEVE'], s['H28c-SIEVE'], s['H28a-MONO'], s['H28b-MONO'], s['H28c-MONO'],
                                    s['H43a'], s['H43b'], s['H43c'], s['H43d'], s['N1'], s['N2'],
                                    'HELD' if all(s['N%d' % i] == 'HELD' for i in (3, 4, 5)) else [s['N%d' % i] for i in (3, 4, 5)],
                                    'HELD' if all(s['S%d' % i] == 'HELD' for i in range(1, 6)) else [s['S%d' % i] for i in range(1, 6)]))
    A = jl('b610_residue_addendum.json') if os.path.exists(_p('b610_residue_addendum.json')) else {}
    t2 = ('\n%s as compiled, the seven-class exclusion is a family of σ-conditions and its joint step is RH restated; the enumeration '
          'located h2 as a reading of the classes, and the prime side enters the compiled star at the explicit formula, not at the classes. '
          'Every monograph and keystone sentence saying the enumeration “uses” or “requires” the Euler product, or that C₂ carries it, is '
          'a second reader’s item under test 2: the seat’s list is banked as the batch’s addendum, relay data/b610_residue_addendum.txt, '
          'addressed to data/b609_residue_seed.txt’s kin and the batch line (OPEN_TRAILS :%d), that prior bank not edited -- %s lines of '
          'four matchers read by hand over the monograph’s v5.17 body and the census’s keystones at their newest versions (%s documents), %s '
          'marked kin, each with its line and reason. No rewrite in this act.\n' % (h2, batch, A.get('n', '?'), len(A.get('docs') or []) or '?',
                                                                                 A.get('kin', '?')))
    t3 = ('\n%s the author-ruled taxonomy governs the census -- Tier K by certification at a pin, Tier KC by certification and cluster '
          'synthesis together (`(R19)`), Tier C by synthesis, Tier N notes, Tier E (the taxonomy’s :20 defines it as filing-facing; the '
          'ruling’s “errata-class” is the navigator’s wording); THE_KEYSTONE_CENSUS’s own three-part test (its §0, :12-:21) retires to the '
          'taxonomy, its line left beneath under the history clause in the census’s next version; the order’s rubric (synthesis against '
          'other content) is read as the KC obligation and not as a separate test. b375’s “three tests, one word” (:%d) closes under this '
          'clause; the phase-state reading priced at :%d is this act.\n' % (h3, b375, pline))
    t4 = ('\n%s the keystones the clusters lack, written from the clusters’ own papers, one act per cluster the census names (its §2, the '
          'clusters with documents and no keystone under `(R220)`(3)), in the census’s order, each act writing one new document in the '
          'cluster’s folder titled by its objects: the cluster’s papers read at address, their claims listed with the grade each paper’s '
          'own text supports (kernel-verified at a pin; theorem-supported; argument-supported; computationally-verified; '
          'synthesis-suggested; statement-grade); a Correspondence table after the front matter carrying every load-bearing claim with its '
          'grade; the sieve’s five tests applied to any claim that is a route; the ceiling as everywhere; Tier C unless a terminal at a pin '
          'certifies a claim, in which case the row says so and the document’s tier line reads KC; no claim entered that no paper of the '
          'cluster states; the no-disclosure arm run where a cluster touches TECHNE content. Each act prices the next. The acts are named '
          'one line per cluster on this act’s trail record, from the census; the first is b611, the census’s opening-listed cluster '
          '(`(R220)`(6)); W-ORD-QUANTIFIER-COLUMN’s generator follows the sequence.\n' % h4)
    return (h1, t1), (h2, t2), (h3, t3), (h4, t4)


def ledger_check(*texts):
    """### b604 (a): no appended line may put a grade word within the table generator's window of a backticked name."""
    import terminal_table as TT
    bad = []
    for t in texts:
        for ln in t.split(NL):
            if TT.GRADE_RE.search(ln) and TT._names_on(ln):
                bad.append((ln[:120], TT._names_on(ln)))
    return bad


def _addr():
    Q = R2._Q()
    return Q, Q.line_of(Q.FIND, B609_ENTRY), Q.line_of(Q.OT, B375_HEAD), Q.line_of(Q.OT, PHASE_LINE), Q.line_of(Q.OT, BATCH_LINE)


def record_lines(*a):
    """### PLACE-papers FINDINGS: b609's weight and the enumeration reading, addressed to b609's entry; OPEN_TRAILS: the keystone test
    ### ruled (addressed to b375's census and b609's phase-state line) and the synthesis sequence's form -- each appended at the end. Needs
    ### the addendum bank first (its counts). `dry` prints."""
    Q, entry, b375, pline, batch = _addr()
    if (entry, b375, pline, batch) != (7186, 4049, 12544, 12542):
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s, %s, %s) -- NOTHING WRITTEN' % (entry, b375, pline, batch))
    if 'dry' not in a and not os.path.exists(_p('b610_residue_addendum.json')):
        sys.exit('### THE ADDENDUM IS NOT BANKED -- NOTHING WRITTEN')
    parts = _texts(entry, b375, pline, batch)
    bad = ledger_check(*[t for _h, t in parts])
    print('  grade-word lines naming a backticked name: %s' % (bad or 'NONE'))
    if 'dry' in a:
        for _h, t in parts:
            print(t)
        return
    if bad:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME -- NOTHING WRITTEN')
    plan = [(Q.FIND, parts[0]), (Q.FIND, parts[1]), (Q.OT, parts[2]), (Q.OT, parts[3])]
    for p, (h, _t) in plan:
        Q.guard_absent(p, h)
    out = []
    for p, (h, t) in plan:
        r = Q.append_to(p, t)
        out.append(dict(file=os.path.basename(p), head=h, line=Q.line_of(p, h), append=r))
    put_json('b610_record_lines.json', dict(entry=entry, b375=b375, pline=pline, batch=batch, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


# ================================================================================ COMPONENT 2: THE CENSUS BANK
def _short(r):
    return r['id'] or os.path.basename(r['path'] or '?')


def _ks_cell(rs):
    by = {}
    for r in rs:
        if r['tier'] in C.KEYSTONE_TIERS:
            by.setdefault(r['tier'], []).append(_short(r))
    out = ['%s: %s' % (t, ', '.join(by[t])) for t in ('K', 'KC', 'C') if t in by]
    rest = {}
    for r in rs:
        if r['tier'] not in C.KEYSTONE_TIERS:
            rest.setdefault(r['tier'] or 'no tier read', []).append(_short(r))
    out += ['%s: %s' % (t, ', '.join(v)) for t, v in sorted(rest.items(), key=lambda x: str(x[0]))]
    return out


def _ed_cell(rs):
    e = ['%s %s' % (_short(r), r['edition'][1].split(' (')[0]) for r in rs if r['edition'][0] == 'EDITED']
    w = [_short(r) for r in rs if r['edition'][0] == 'WORK-LIST']
    n = sum(1 for r in rs if r['edition'][0] == 'NEITHER')
    out = ['edited by the form: %s' % (', '.join(e) or 'none')]
    if w:
        out.append('work-list alone: %s' % ', '.join(w))
    out.append('neither: %d' % n)
    mv = [_short(r) for r in rs if r['edition'][0] == 'MOVED']
    if mv:
        out.append('a moved row: %s' % ', '.join(mv))
    return out


def _sieve_cell(links):
    if not links:
        return ['none (no SPIRAL_MAP §4A cluster holds a member here)']
    return ['%s %s: %d row%s (via %s)' % (n, p, c, '' if c == 1 else 's', ', '.join(ms)) if p != '--' else '%s: 0 rows (the sieve carries none; via %s)' % (n, ', '.join(ms))
            for n, p, c, ms in links]


def _ker_cell(kern, remotes):
    out = []
    for k in sorted(kern):
        rt = remotes.get(k) or {}
        if not rt.get('ok'):
            out.append('%s: not read (%s)' % (k, rt.get('err') or 'no read'))
        elif not rt.get('current'):
            out.append('%s: no tag' % k)
        else:
            dep = (' ; deposit ' + C.KERNEL_DEPOSITS[k]) if k in C.KERNEL_DEPOSITS else ''
            out.append('%s %s = %s%s' % (k, rt['current'], rt['remote_peel'][:7], dep))
    return out or ['none named']


def _dep_cell(rs):
    d = [_short(r) for r in rs if r['deposit'][0] == 'DEPOSITED']
    m = [_short(r) for r in rs if r['deposit'][0] == 'MIRROR']
    n = sum(1 for r in rs if r['deposit'][0] == 'NEITHER')
    out = []
    if d:
        out.append('deposited at record %s: %s' % (C.DEPOSIT_RECORD[0], ', '.join(d)))
    if m:
        out.append('in the mirror alone: %s' % ', '.join(m))
    out.append('neither: %d' % n)
    mv = [_short(r) for r in rs if r['deposit'][0] == 'MOVED']
    if mv:
        out.append('a moved row: %s' % ', '.join(mv))
    return out


def _h44(B):
    rows = B['rows']
    keys = [r['census'] for r in rows]
    unplaced = [r for r in rows if not r['census']]
    sums = sum(sum(1 for r in rows if r['census'] == k) for k in C.KEYS)
    kl = C.keystone_less(B)
    rem = B['remotes']
    tagged = {k: v for k, v in rem.items() if v.get('ok') and v.get('current')}
    back = {k: v for k, v in tagged.items() if v.get('local_peel') and v['local_peel'] == v['remote_peel']}
    untagged = sorted(k for k, v in rem.items() if v.get('ok') and not v.get('current'))
    unread = sorted(k for k, v in rem.items() if not v.get('ok'))
    h44a = 'HOLDS' if not unplaced and sums == len(rows) and None not in keys else 'REFUTED'
    h44b = 'HOLDS' if 5 <= len(kl) <= 8 else 'REFUTED'
    h44c = 'HOLDS' if len(back) == len(tagged) and not unread else 'REFUTED'
    return dict(H44a=h44a, H44b=h44b, H44c=h44c, n_rows=len(rows), unplaced=len(unplaced), sums=sums, kl=kl, tagged=len(tagged),
                back=len(back), untagged=untagged, unread=unread, local_only={k: v.get('local_only') for k, v in rem.items() if v.get('local_only')})


def census(*a):
    """### data/b610_census.txt and data/b610_census.json: every registry row read and placed, the census rows with their columns, the
    ### kernels read by ls-remote, the clusters without a keystone -- banked BEFORE any edition is written; H44a-H44c scored on it."""
    B = C.build(read_remotes=True)
    rows = B['rows']
    H = _h44(B)
    L = ['b610 -- COMPONENT 2: THE CENSUS BANK, (R220)(4) -- every REGISTRY row read and placed, banked %s, before any edition is '
         'written' % utc(),
         '### the pins: PLACE-papers %s (REGISTRY.md, the documents, SPIRAL_MAP.md, the sieve v0.4, OPEN_TRAILS.md); relay %s (the mirror '
         'roster, the b558 work-lists); the remotes read by `git ls-remote --tags` at this bank`s time' % (PRE_PP, STEPZERO)]
    L += ['### ' + x.strip('# ').strip() for x in C.__doc__.split(NL) if x.strip().startswith('###') and ('POPULATION' in x or 'PLACEMENT' in x or 'TIER' in x)]
    L += ['### EDITION STATE: EDITED -- an edition by the form stands beside the registry`s file (a tracked `<base>_v<n>.md` in its folder, the '
          'trails` line naming it printed); WORK-LIST -- relay data/b558_editions/<base>.txt and no edition; NEITHER otherwise',
          '### SIEVE ROWS: a census row holds the sieve v0.4 rows of every SPIRAL_MAP §4A cluster (the b388 refreshed table) whose members -- '
          'read by REGISTRY ID or file name from that row`s own cells -- sit in it',
          '### KERNELS: the kernels its REGISTRY rows name, the frozen Phase 1.2 table`s for Phase 1.2 (REGISTRY :713-:718), and the '
          'federation column of every SPIRAL_MAP cluster whose members it holds; the current tag is the remote`s highest by ls-remote, '
          'read back against the clone`s peel',
          '### DEPOSIT: DEPOSITED -- the file`s copy is in the Day-1 record`s files (`outputs/DEPOSITED-v1.1.2/`, record 21539167); MIRROR -- '
          'the file is on the mirror roster; NEITHER otherwise; a kernel`s deposit is named in its kernel cell', '']
    L += ['### PART A -- THE REGISTRY ROWS, EACH READ AND PLACED (%d rows; %d title-layer references apart, Part E):' % (len(rows), len(B['refs']))]
    for r in rows:
        cert = r['cert']
        L.append('  :%-4d %-8s %-62s -> %-4s %s' % (r['line'], r['id'] or '—', r['path'] or '(no file)', r['census'], r['why']))
        L.append('        tier %s -- %s ; certification %s ; edition %s %s ; deposit %s %s' % (
            r['tier'] or 'NONE', r['tier_src'], ('tier block :%d, %d terminal row(s)' % (cert['line'], cert['terminal_rows'])) if cert else 'no tier block',
            r['edition'][0], r['edition'][1], r['deposit'][0], r['deposit'][1]))
    L += ['', '### PART B -- THE CENSUS ROWS, ONE PER PHASE AND CLUSTER, IN REGISTRY ORDER:']
    J = []
    for i, k in enumerate(C.KEYS, 1):
        rs = [r for r in rows if r['census'] == k]
        row = dict(n='R%02d' % i, key=k, label=C.LABEL[k], heading=B['heads'][k], rows=[dict(line=r['line'], id=r['id'], path=r['path'], tier=r['tier'],
                                                                                           tier_src=r['tier_src'], edition=r['edition'], deposit=r['deposit'])
                                                                                      for r in rs],
                   keystones=_ks_cell(rs), editions=_ed_cell(rs), sieve=_sieve_cell(B['sieve'][k]), kernels=_ker_cell(B['kern'][k], B['remotes']),
                   kernel_src={x: v for x, v in B['kern'][k].items()}, deposit=_dep_cell(rs),
                   has_keystone=any(r['tier'] in C.KEYSTONE_TIERS for r in rs))
        J.append(row)
        L.append('  ### %s %s (REGISTRY :%s) -- %d rows' % (row['n'], row['label'], row['heading'], len(rs)))
        L.append('      documents : %s' % ', '.join('%s :%d' % (('%s %s' % (r['id'], r['path'])) if r['id'] else (r['path'] or '?'), r['line']) for r in rs))
        for lab, v in (('keystones', row['keystones']), ('editions', row['editions']), ('sieve v0.4', row['sieve']), ('kernels', row['kernels']),
                       ('deposit', row['deposit'])):
            L.append('      %-10s: %s' % (lab, ' ; '.join(v)))
    L += ['', '### PART C -- THE KERNELS, READ BY ls-remote:']
    for k, rt in sorted(B['remotes'].items()):
        L.append('  %-36s %s ; via %s ; current %s ; remote peel %s ; clone peel %s ; read back %s ; local-only tags %s%s' % (
            k, 'READ' if rt['ok'] else 'NOT READ (%s)' % rt['err'], rt['via'], rt.get('current'), (rt.get('remote_peel') or '—')[:12],
            (rt.get('local_peel') or '—')[:12], (rt.get('local_peel') == rt.get('remote_peel')) if rt.get('current') else 'no tag',
            rt.get('local_only') or 'none', (' ; ' + C.KERNEL_DEPOSITS[k]) if k in C.KERNEL_DEPOSITS else ''))
    L += ['', '### PART D -- THE CLUSTERS WITH DOCUMENTS AND NO KEYSTONE UNDER (R220)(3), IN THE CENSUS`S ORDER:']
    for row in J:
        if not row['has_keystone']:
            L.append('  %s %s: %s' % (row['n'], row['label'], ', '.join(('%s %s' % (x['id'], x['path'])) if x['id'] else (x['path'] or '?') for x in row['rows'])))
    L += ['', '### PART E -- THE TITLE LAYER (REGISTRY :644-:668), REFERENCES TO ROWS THAT STAND ELSEWHERE, NOT COUNTED: %s' % (
        ', '.join('%s (:%d)' % (r['id'], r['line']) for r in B['refs']))]
    R = B['R']
    L += ['', '### PART F -- WHAT THE READING FOUND, STATED AND NOT REPAIRED:',
          '  (F1) %d kernels carry tags their remotes do not: %s' % (len(H['local_only']), '; '.join('%s %s' % (k, ', '.join('%s=%s' % t for t in v))
                                                                                                for k, v in sorted(H['local_only'].items()))),
          '  (F2) REGISTRY :787 reads “`internal/` (6 files, 2.5 MB) and `meta/` (5 files) have no `REGISTRY` section of any kind”, while '
          'REGISTRY :333 heads a table listing six `internal/` files (:337-:342); both lines stand, the census places the six rows by :333',
          '  (F3) rows naming no tracked file: %s' % ', '.join('%s :%d (%s)' % (r['id'] or '—', r['line'], r['path'] or 'no file') for r in rows if not r['tracked']),
          '  (F4) 1.5a-1 to 1.5a-4 sit in the 1.5A table (:142-:145) and land in Phase 1.2 by the phase attribute (:780); the 1.5A census '
          'row holds 1.5a-5 to 1.5a-8',
          '  (F5) the ruling`s “Tier E errata-class” is the navigator`s wording; the taxonomy defines Tier E as filing-facing (:20), and no '
          'registry row reads E',
          '  (F6) p2-3 is a moved row (REGISTRY :259) pointing at 1.5h-8`s document; it is placed in 2C and its tier is read on 1.5h-8`s row']
    L += ['', '### ### **H44a %s** -- %d rows, unplaced %d, the census rows` sum %d; each row placed by one rule, printed in Part A' % (
        H['H44a'], H['n_rows'], H['unplaced'], H['sums']),
          '### ### **H44b %s** -- the clusters with documents and no keystone number %d (%s), bound 5 to 8' % (
              H['H44b'], len(H['kl']), ', '.join('%s %s' % (row['n'], row['label'].split(':')[0]) for row in J if not row['has_keystone'])),
          '### ### **H44c %s** -- %d kernels read; %d carry a tag, %d read back at their remotes; with no tag %s ; not read %s ; local-only tags '
          'printed in Part C and (F1)' % (H['H44c'], len(B['remotes']), H['tagged'], H['back'], H['untagged'] or 'none', H['unread'] or 'none')]
    put_txt('b610_census.txt', L)
    put_json('b610_census.json', dict(at=utc(), pre_pp=PRE_PP, rows=J, registry_rows=[dict((x, r[x]) for x in ('line', 'id', 'path', 'census', 'why', 'tier',
                                                                                                             'tier_src', 'edition', 'deposit', 'tracked', 'pointer'))
                                                                                    for r in rows],
                                      refs=B['refs'], remotes=B['remotes'], h44=H, sieve_counts=B['sc']))
    for l in L[-3:]:
        print(l)


# ================================================================================ COMPONENT 3: THE CENSUS AT v0.3
BM_TAG3 = '<!-- b610 (R220) THE v0.3 EDITION`S BACK MATTER, 2026-10-03 -->'
VERSION3 = ('*v0.3, 2026-10-03 -- the phase-state reading: one row per phase and cluster as REGISTRY lists them, read from the ledgers, the '
            'pages, the registry and the remotes; the keystone test ruled to the taxonomy; the current version (v0.1 with its v0.2 section) '
            'stands beside it, unedited.*')
HIST3 = ('*History line, v0.3, 2026-10-03 (b610, under `(R220)`(3)): the three-part test above retires to the author-ruled taxonomy, read by '
         'the order of §0 above; the census reads tiers, not this test. b375’s “three tests, one word” (OPEN_TRAILS :4049) closes under that '
         'clause.*')
V01_TEST = (12, 21)      # ### v0.1's §0, kept in the body beneath the ruled test
V01_HEAD = (1, 11)       # ### the head and v0.1's version line, carried at the top


def _cur(path, rev=PRE_PP):
    return C.lines_of(_show(PP, rev, path))


def _census_body(J, H):
    """### the new body after the carried head: §0 ruled, v0.1's test beneath with its history line, §1 the rows, §2 the clusters
    ### without a keystone, §3 what the reading found."""
    S = []
    S += ['## §0 — THE KEYSTONE TEST, RULED *(v0.3, 2026-10-03, b610, under the author’s ruling `(R220)`(3))*', '',
          'The author-ruled taxonomy governs (`phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md`): **Tier K** by certification at a pin (:14), '
          '**Tier KC** by certification and cluster synthesis together (`(R19)`, :57), **Tier C** by synthesis (:16), **Tier N** notes and '
          'exploratory (:18), **Tier E** filing-facing (:20). A keystone in this census is a document read at K, KC or C. The order’s rubric of '
          'b375 (synthesis against other content) is read as the KC obligation, not as a separate test.', '',
          '**How a tier is read here, in order:** (1) the document’s own class line under the standing taxonomy; (2) a sentence of the '
          'document stating its tier; (3) a tier the author ruled by name (REGISTRY :669; the taxonomy :39-:43) or the registry’s own row; '
          '(4) the taxonomy’s presumptive class by name (:35, the cluster syntheses at C; :36, the consults at N); (5) certification at a pin '
          'read from the cascade, a CP-1 tier block with a terminal row at T0-T2 reading K. A document none of these reaches reads “no tier '
          'read” and is not a keystone; no document is reclassified by this census.', '']
    return S


def _census_rows(J):
    S = ['## §1 — THE PHASES AND CLUSTERS, ONE ROW EACH *(read 2026-10-03, b610; relay `data/b610_census.txt`)*', '',
         'One row per phase and cluster as REGISTRY lists them, in its order: the documents the registry lists (ID and REGISTRY line), the '
         'keystones by tier under §0, the edition state (edited by the form at its version; work-list alone; neither), the sieve rows the '
         'cluster holds at v0.4 through SPIRAL_MAP §4A’s members, the kernels anchoring it with their current tags read by ls-remote, and '
         'the deposit state. Each cell is read at PLACE-papers 7055f04 or at the remote, and none from recall; the rules are in the back '
         'matter’s readings.', '',
         '| row | phase and cluster | documents | keystones by tier | edition state | sieve rows at v0.4 | kernels, current tag | deposit state |',
         '|:--|:--|:--|:--|:--|:--|:--|:--|']
    for row in J:
        docs = '; '.join(('`%s` %s (:%d)' % (x['id'], os.path.basename(x['path'] or '') or 'no file', x['line'])) if x['id'] else
                         ('%s (:%d)' % (os.path.basename(x['path'] or '') or 'no file', x['line'])) for x in row['rows'])
        S.append('| %s | %s (REGISTRY :%s) | %s | %s | %s | %s | %s | %s |' % (
            row['n'], _cell(row['label']), row['heading'], _cell(docs), _cell(' ; '.join(row['keystones'])), _cell(' ; '.join(row['editions'])),
            _cell(' ; '.join(row['sieve'])), _cell(' ; '.join(row['kernels'])), _cell(' ; '.join(row['deposit']))))
    return S + ['']


def _census_nokey(J, H):
    S = ['## §2 — THE CLUSTERS WITH DOCUMENTS AND NO KEYSTONE *(under §0)*', '',
         'Each is a row of §1 whose documents read no tier at K, KC or C; its documents are named here, in the census’s order, which is the '
         'order of the synthesis sequence `(R220)`(5) enters on the trails.', '']
    for row in J:
        if not row['has_keystone']:
            docs = '; '.join(('`%s` `%s`' % (x['id'], x['path'])) if x['id'] else ('`%s`' % (x['path'] or 'no file')) for x in row['rows'])
            S.append('- **%s %s** (REGISTRY :%s): %s.' % (row['n'], row['label'], row['heading'], docs))
    S += ['', '%d of the census’s %d rows hold documents and no keystone; the other %d hold at least one document read at K, KC or C.'
          % (len(H['kl']), len(J), len(J) - len(H['kl'])), '']
    return S


def _census_found(H):
    S = ['## §3 — WHAT THE READING FOUND, STATED AND NOT REPAIRED', '',
         '- **Local tags the remotes do not carry.** %d kernels carry tags their remotes do not (relay `data/b610_census.txt`, Part C and '
         '(F1)); every current tag read by ls-remote reads back at the clone.' % len(H['local_only']),
         '- **`internal/`.** REGISTRY :787 says `internal/` has no REGISTRY section of any kind, while REGISTRY :333 heads a table listing six '
         '`internal/` files; both lines stand, and the census places those six rows by :333.',
         '- **Phase 1.2.** 1.5a-1 to 1.5a-4 sit in the 1.5A table and land in Phase 1.2 by the phase attribute (REGISTRY :780).',
         '- **The title layer.** The ratified-titles table (REGISTRY :644-:668) names rows that stand elsewhere; its entries are references '
         'and are not counted.', '',
         '*Nothing deposits; no document is reclassified, no registry row edited, no grade moved; the census reads and records.*', '']
    return S


def _census_edition(dry):
    cur = _cur(CEN)
    if not cur[V01_TEST[0] - 1].startswith('## §0 — THE CATEGORY, DEFINED BEFORE COUNTING') or not cur[9].startswith('**Method register · v0.1'):
        sys.exit('### THE CURRENT VERSION`S ANCHORS MOVED -- NOTHING WRITTEN')
    CJ = jl('b610_census.json')
    J, H = CJ['rows'], CJ['h44']
    head = cur[:9]
    out = head + [VERSION3, ''] + cur[9:11]
    body_new = _census_body(J, H)
    test_lines = cur[V01_TEST[0] - 1:V01_TEST[1]]
    hist_block = ['### The census’s own test of v0.1, carried beneath under the history clause', ''] + test_lines + ['', HIST3, '']
    out += body_new + hist_block + _census_rows(J) + _census_nokey(J, H) + _census_found(H)
    body_end = len(out)
    moved = cur[V01_TEST[1]:]          # ### v0.1 :22 onward (its §1-§9, act 3c, the v0.2 section and the appended lines)
    bm = [BM_TAG3, '',
          '## Back matter of the v0.3 edition — written 2026-10-03 by b610 under the author’s ruling `(R220)`(4), by the form of `(R187)`(5), its '
          'clauses and the precedence order, with the reorganisation `(R215)`(3) allows', '']
    return out, body_end, moved, bm, J, H, cur


def census_edition(*a):
    """### PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_3.md beside the current version (unedited), and data/b610_census_edition.json.
    ### `dry` writes the edition to the scratchpad instead."""
    dry = 'dry' in a
    out, body_end, moved, bm, J, H, cur = _census_edition(dry)
    nm = sum(1 for l in moved if l.strip())
    rd_ = ['### The readings, each the seat’s and strikeable', '',
           '- **R-1, the population.** A REGISTRY row is a table row outside a code fence whose first cell is a registry ID (d1-n, 1.5x-n, '
           'p2-n, p2-dn, m5-n) or whose first or second cell opens with a backticked document path, with the one block entry naming a document '
           'outside any table (the carrier specification, REGISTRY :117); the ratified-titles table (:644-:668) is a title layer over rows '
           'that stand elsewhere and is not counted.',
           '- **R-2, the placement.** A row lands in the row of the REGISTRY heading it sits under; 1.5a-1 to 1.5a-4 land in Phase 1.2 by the '
           'phase attribute (:780); a dated row addition lands in the cluster its heading names, else the cluster its own ID letter names, '
           'else, for a p2 ID, in Phase 2’s row of rows filed to no lettered cluster; the rows filed under no phase heading take a row of '
           'their own.',
           '- **R-3, the tier.** By §0’s order; the class line is read at the document’s newest version.',
           '- **R-4, the edition state.** Edited by the form: an edition stands beside the registry’s file and the trails name it; work-list '
           'alone: relay `data/b558_editions/<name>.txt` and no edition; neither otherwise.',
           '- **R-5, the sieve rows.** A row holds the sieve v0.4 rows of every SPIRAL_MAP §4A cluster whose members, read by REGISTRY ID or '
           'file name from that cluster’s own cells (the b388 table), sit in it.',
           '- **R-6, the kernels.** The kernels a row’s REGISTRY rows name, the frozen Phase 1.2 table’s for Phase 1.2 (:713-:718), and the '
           'federation column of every SPIRAL_MAP cluster whose members it holds; the current tag is the remote’s highest, read by '
           'ls-remote and read back against the clone.',
           '- **R-7, the deposit state.** Deposited: the file’s copy is among the Day-1 record’s files (`outputs/DEPOSITED-v1.1.2/`, record '
           '21539167); in the mirror alone: on the mirror roster; neither otherwise; a kernel’s deposit is named in its kernel cell.',
           '- **R-8, the reorganisation.** The current version’s lines from its :22 to its end -- v0.1’s §1-§9, act 3c, the v0.2 section and '
           'the lines appended beneath it -- are moved whole into this back matter, unchanged, under the reorganising clause (OPEN_TRAILS '
           ':12456); their own `:n` cite the current version, which stands beside this one unedited, and are not re-pinned.', '']
    rem = ['### Removals -- the body moved whole below (the reorganising clause)', '',
           '| current version’s lines | destination | non-blank lines | sentences |', '|:--|:--|:--|:--|',
           '| :%d-:%d | this back matter, “The census at v0.1 and v0.2, moved whole” | %d | %d |' % (V01_TEST[1] + 1, len(cur), nm, _count(moved)),
           '', 'No sentence is removed outright; no sentence is reworded.', '']
    hist = ['### History lines', '', '| line | beneath | clause | Status |', '|:--|:--|:--|:--|',
            '| {E:hist} | the current version’s §0 (:12-:21), carried at {E:test0}-{E:test1} | the history clause, `(R220)`(3) | inserted |', '']
    mv = ['### The census at v0.1 and v0.2, moved whole', ''] + moved + ['']
    pl = ['### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this edition, v0.3 | `%s` | written at b610 |' % CEN3,
          '| the current version (v0.1 with its v0.2 section) | `%s` | unedited |' % CEN,
          '| the census bank | relay `data/b610_census.txt` | banked before this edition |',
          '| the registry read | `REGISTRY.md` @ 7055f04 | read, unedited |',
          '| the cluster map pointing to the rows | `%s` | written at b610 beside `%s`, unedited |' % (SPI7, SPI), '']
    co = ['### Correspondence', '', '| row | this edition’s line | phase and cluster | REGISTRY rows (lines) | keystone | Status |', '|:--|:--|:--|:--|:--|:--|']
    for row in J:
        co.append('| %s | {E:%s} | %s | %s | %s | read |' % (row['n'], row['n'], _cell(row['label']),
                                                          ', '.join(':%d' % x['line'] for x in row['rows']), 'yes' if row['has_keystone'] else 'none'))
    co += ['']
    vh = ['### Version history', '',
          '- **v0.3, 2026-10-03 (b610, `(R220)`(3)-(4))**: the phase-state reading -- %d rows, one per phase and cluster, %d registry rows placed; '
          '%d clusters with documents and no keystone named with their documents; the keystone test ruled to the taxonomy, the census’s own '
          'test carried beneath with its history line. The current version stands beside it, unedited.' % (len(J), H['n_rows'], len(H['kl'])),
          '- **v0.2, 2026-09-28 (b553, `(R163)`(6))** and **v0.1, 2026-08-12**: carried above, moved whole.', '']
    lines = out + bm + rd_ + rem + hist + mv + pl + co + vh
    # ### the {E:n} tokens resolved against the final file
    pos = {}
    for i, l in enumerate(lines, 1):
        m = re.match(r'^\| (R\d\d) \| ', l)
        if m and i <= len(out):
            pos[m.group(1)] = i
    pos['hist'] = lines.index(HIST3) + 1
    pos['test0'] = next(i for i, l in enumerate(lines, 1) if l.startswith('## §0 — THE CATEGORY, DEFINED BEFORE COUNTING'))
    pos['test1'] = pos['test0'] + (V01_TEST[1] - V01_TEST[0])
    lines = [re.sub(r'\{E:(\w+)\}', lambda m: ':%d' % pos[m.group(1)], l) for l in lines]
    b = (NL.join(lines) + NL).encode('utf-8')
    dest = os.path.join(SP, 'b610_census_dry.md') if dry else os.path.join(PP, *CEN3.split('/'))
    if not dry and os.path.exists(dest):
        sys.exit('### v0.3 EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    bm_at = lines.index(BM_TAG3) + 1
    J2 = dict(at=utc(), path=CEN3, sha256=sha(b), bytes=len(b), lines=len(lines), body_end=body_end, bm=bm_at, pos=pos, n_moved=nm,
              moved_from=V01_TEST[1] + 1, cur_len=len(cur), version_lines=1, history_lines=1, removals=_count(moved),
              n_body=_count(lines[:bm_at - 1]), n_cur_body=_count(cur), n_backmatter=_count(lines[bm_at - 1:]),
              ruled=_count(_census_body(J, H) + _census_rows(J) + _census_nokey(J, H) + _census_found(H)) + _count(['### The census’s own test of v0.1, carried beneath under the history clause']))
    print('  %s : %d lines, %d bytes, sha256 %s ; body %d sentences (current %d) ; moved %d sentences ; back matter %d' % (
        'DRY ' + dest if dry else CEN3, len(lines), len(b), J2['sha256'][:16], J2['n_body'], J2['n_cur_body'], J2['removals'], J2['n_backmatter']))
    put_json('b610_census_edition.json', J2)


# ================================================================================ COMPONENT 3: SPIRAL_MAP AT v0.7
BM_TAG7 = '<!-- b610 (R220) THE v0.7 EDITION`S BACK MATTER, 2026-10-03 -->'
VERSION7 = ('**v0.7 — 2026-10-03** (revises v0.6 -- b610, under the author’s ruling `(R220)`(4): §4A’s cluster table takes one line per '
            'cluster pointing to THE_KEYSTONE_CENSUS v0.3’s rows, by `(R17)`’s form; one stem and three ceiling sentences corrected by the '
            'form’s clauses; v0.6 stands beside it, unedited)')
VLINE6 = 18
TABLE_LAST = 275
# ### the clause corrections, each (line at v0.6, old, new, clause, the object named)
SP_FIX = [
    (62, 'Mechanism Theorem and the proof of the Riemann Hypothesis',
     'Mechanism Theorem and the reduction of the Riemann Hypothesis to a single located clause', 'ceiling',
     'README :106, the supportable sentence’s object'),
    (98, 'Closes the abstract→concrete instantiation gap', 'Supplies the abstract→concrete instantiation', 'stem',
     'the instantiation the sentence names'),
    (102, '(alternative proof paths)', '(alternative paths to the critical line)', 'ceiling', 'the paths of PATHS_TO_THE_CRITICAL_LINE'),
    (104, 'the alternative-proof-paths census', 'the alternative-paths census', 'ceiling', 'the paths census the sentence names'),
]
# ### the ceiling pattern's other hits in v0.6, each read in its line and carried within the ceiling
SP_CARRY = {
    82: 'a negation: `EDifficultyTop` “never proved”',
    115: 'a compiled fact at its own grade: what SIDE-window’s terminals state, and its non-claims',
    148: 'a compiled fact at its own grade: composite kernels prove composite theorems',
    403: 'a compiled fact at its own grade: the kernel’s ζ(−1) theorem',
    439: 'a literature fact: the Lee–Yang circle theorem',
    443: 'a literature fact and its negation: the restricted-support theorem; Q “unproved”; five suppliers; “never of a proof”',
    488: 'a fact of the copy: byte identity proved per module by digests',
}


def _pointer_lines(J):
    """### one line per SPIRAL_MAP cluster pointing to the census rows that hold its members."""
    ix = {r['key']: r['n'] for r in J}
    CJ = jl('b610_census.json')
    reg = CJ['registry_rows']
    ids = {}
    for r in reg:
        if r['id']:
            ids[r['id']] = r['census']
        if r['path']:
            ids.setdefault(os.path.basename(r['path']), r['census'])
            ids.setdefault(os.path.basename(r['path'])[:-3], r['census'])
    out = []
    for name, p, mids, files in C.SPIRAL_CLUSTERS:
        by = {}
        for t in mids + files:
            k = ids.get(t)
            if k:
                by.setdefault(k, []).append(t)
        cells = ['%s (%s: %s)' % (ix[k], C.LABEL[k].split(':')[0].split(' (')[0], ', '.join('`%s`' % x for x in v)) for k, v in
                 sorted(by.items(), key=lambda kv: ix[kv[0]])]
        out.append('- **%s** → THE_KEYSTONE_CENSUS v0.3 §1, rows %s.' % (name, '; '.join(cells)))
    return out


def _spiral_edition(dry):
    cur = _cur(SPI)
    if not cur[VLINE6 - 1].startswith('**v0.6 — July 2026**') or not cur[TABLE_LAST - 1].startswith('| **cross-domain** (emergent)') or cur[TABLE_LAST] != '':
        sys.exit('### SPIRAL_MAP`S ANCHORS MOVED -- NOTHING WRITTEN')
    for n, old, _new, _c, _o in SP_FIX:
        if cur[n - 1].count(old) != 1:
            sys.exit('### :%d DOES NOT CARRY ITS OLD WORDING ONCE -- NOTHING WRITTEN' % n)
    J = jl('b610_census.json')['rows']
    point = ['**THE CENSUS ROWS — 2026-10-03 (b610), under RULING `(R220)`(4), by `(R17)`’s form.** One line per cluster of the table '
             'above, pointing to the rows of `%s` (its §1) that hold the cluster’s members, each member read by its REGISTRY ID or file '
             'name from the table’s own cells; the table above is not edited, and its federation column was read again by ls-remote '
             'for the census (relay `data/b610_census.txt`, Part C).' % C.CENSUS3, ''] + _pointer_lines(J) + ['']
    out, where = [], {}
    for i, l in enumerate(cur, 1):
        if i == VLINE6:
            out += [VERSION7, '']
        fix = [f for f in SP_FIX if f[0] == i]
        nl = l.replace(fix[0][1], fix[0][2]) if fix else l
        out.append(nl)
        where[i] = len(out)
        if i == TABLE_LAST + 1:
            out += point
    return cur, out, where, point


def spiral_edition(*a):
    """### PLACE-papers SPIRAL_MAP_v0_7.md beside SPIRAL_MAP.md (unedited), and data/b610_spiral_edition.json. `dry`: the scratchpad."""
    dry = 'dry' in a
    cur, out, where, point = _spiral_edition(dry)
    bm = [BM_TAG7, '', '## Back matter of the v0.7 edition — written 2026-10-03 by b610 under the author’s ruling `(R220)`(4), by `(R17)`’s '
          'form, the form of `(R187)`(5), its clauses and the precedence order', '',
          '### The readings, each the seat’s and strikeable', '',
          '- **R-1.** “One line per cluster pointing to the census row” is read as a block of lines beneath §4A’s refreshed table, one per '
          'cluster of that table, the table itself not edited; a cluster whose members sit in several census rows points to each.',
          '- **R-2.** The pointing lines are dated and name their source, the census bank; the members are read from the table’s own cells, '
          'as `(R17)`’s form reads moves, and none is added on the seat’s sense of subject.',
          '- **R-3.** The stem clause and the ceiling clause reach four unmarked sentences of v0.6; each is corrected to the object it names, '
          'the rest of the sentence unchanged; the ceiling pattern’s other hits are read in their lines and carried within the ceiling.', '',
          '### Insertions ordered by the ruling', '', '| line | what | Status |', '|:--|:--|:--|',
          '| {E:ver} | the version line, above v0.6’s | inserted |',
          '| {E:pt0}-{E:pt1} | the census rows: the head line and one line per cluster | inserted |', '',
          '### Stem corrections', '', '| line | v0.6 line | was | now | the object named |', '|:--|:--|:--|:--|:--|']
    for n, old, new, c, o in SP_FIX:
        if c == 'stem':
            bm.append('| {E:%d} | :%d | “%s” (banned stem; correction record) | “%s” | %s |' % (n, n, old, new, o))
    bm += ['', '### Ceiling corrections', '', '| line | v0.6 line | was | now | the object named |', '|:--|:--|:--|:--|:--|']
    for n, old, new, c, o in SP_FIX:
        if c == 'ceiling':
            bm.append('| {E:%d} | :%d | “%s” | “%s” | %s |' % (n, n, old, new, o))
    bm += ['', '### The ceiling pattern’s other hits, carried within the ceiling', '', '| line | v0.6 line | reading | Status |', '|:--|:--|:--|:--|']
    for n, why in sorted(SP_CARRY.items()):
        bm.append('| {E:%d} | :%d | %s | carried |' % (n, n, why))
    bm += ['', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v0.7 | `%s` | written at b610 |' % SPI7, '| v0.6, the current version | `%s` | unedited |' % SPI,
           '| the census the lines point to | `%s` | written at b610 |' % CEN3, '',
           '### Correspondence', '', '| cluster | this edition’s line | the refreshed table’s line | Status |', '|:--|:--|:--|:--|']
    for k, (name, _p, _i, _f) in enumerate(C.SPIRAL_CLUSTERS):
        bm.append('| %s | {E:p%d} | :%d (v0.6) | points |' % (name, k, C.spiral_rows()[name][0]))
    bm += ['', '### Version history', '',
           '- **v0.7, 2026-10-03 (b610, `(R220)`(4))**: §4A’s cluster table points each cluster to THE_KEYSTONE_CENSUS v0.3’s rows; one stem '
           'and three ceiling sentences corrected. v0.6 stands beside it, unedited.', '']
    lines = out + [''] + bm
    pos = {'ver': lines.index(VERSION7) + 1}
    pos['pt0'] = next(i for i, l in enumerate(lines, 1) if l.startswith('**THE CENSUS ROWS — 2026-10-03 (b610)'))
    pos['pt1'] = pos['pt0'] + len(point) - 2
    for k, (name, _p, _i, _f) in enumerate(C.SPIRAL_CLUSTERS):
        pos['p%d' % k] = next(i for i, l in enumerate(lines, 1) if l.startswith('- **%s** → THE_KEYSTONE_CENSUS v0.3' % name))
    for n in [f[0] for f in SP_FIX] + list(SP_CARRY):
        pos[str(n)] = where[n]
    lines = [re.sub(r'\{E:(\w+)\}', lambda m: ':%d' % pos[m.group(1)], l) for l in lines]
    b = (NL.join(lines) + NL).encode('utf-8')
    dest = os.path.join(SP, 'b610_spiral_dry.md') if dry else os.path.join(PP, SPI7)
    if not dry and os.path.exists(dest):
        sys.exit('### v0.7 EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    bm_at = lines.index(BM_TAG7) + 1
    seg_d = [dict(line=n, d=len(_segs(cur[n - 1].replace(o, w))) - len(_segs(cur[n - 1]))) for n, o, w, _c, _x in SP_FIX]
    J2 = dict(at=utc(), path=SPI7, sha256=sha(b), bytes=len(b), lines=len(lines), bm=bm_at, pos=pos, where={str(k): v for k, v in where.items()},
              fixes=[dict(line=n, at=where[n], old=o, new=w, clause=c, obj=x) for n, o, w, c, x in SP_FIX], carried=SP_CARRY,
              version_lines=1, ruled=_count(point), n_body=_count(lines[:bm_at - 1]), n_cur_body=_count(cur), seg_d=seg_d,
              n_backmatter=_count(lines[bm_at - 1:]), removals=0)
    print('  %s : %d lines, %d bytes, sha256 %s ; body %d sentences (current %d) ; ruled %d ; back matter %d ; seg_d %s' % (
        'DRY ' + dest if dry else SPI7, len(lines), len(b), J2['sha256'][:16], J2['n_body'], J2['n_cur_body'], J2['ruled'], J2['n_backmatter'],
        [x['d'] for x in seg_d]))
    put_json('b610_spiral_edition.json', J2)


# ================================================================================ THE SCANS, THE DIFF BANKS, THE RE-PINS AND H28
def _edpath(path):
    if DRY:
        return os.path.join(SP, 'b610_census_dry.md' if path == CEN3 else 'b610_spiral_dry.md')
    return os.path.join(PP, *path.split('/'))


def _ed(path):
    return C.lines_of(open(_edpath(path), encoding='utf-8').read().replace(chr(13), ''))


def _scan(path):
    return subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', _edpath(path)],
                          capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout


def census_termscan(*a):
    t = _scan(CEN3)
    put_txt('b610_census_termscan.txt', t.rstrip(NL).split(NL))


def spiral_termscan(*a):
    t = _scan(SPI7)
    put_txt('b610_spiral_termscan.txt', t.rstrip(NL).split(NL))


def _ceiling_body(lines, end):
    return [(i + 1, m.group(0)) for i, l in enumerate(lines[:end]) for m in CEILING.finditer(l)]


def _carried(cur, new, J, skip=()):
    """### every non-blank current line found verbatim in the new file, or as its recorded rewrite: (ok, [failing current lines])."""
    fix = dict((f['line'], f) for f in J.get('fixes') or [])
    nset = set(new)
    ok, bad = 0, []
    for i, l in enumerate(cur, 1):
        if not l.strip():
            continue
        if l in nset or (i in fix and l.replace(fix[i]['old'], fix[i]['new']) in nset):
            ok += 1
        else:
            bad.append(i)
    return ok, bad


def census_bank(*a):
    """### data/b610_edition_CENSUS.txt (the diff bank, its offset head once) and data/b610_h28_census.json: H28a-H28c scored."""
    E = jl('b610_census_edition.json')
    ed = _ed(CEN3)
    cur = _cur(CEN)
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### v0.3 ON DISK IS NOT THE BANKED BYTES -- NOTHING WRITTEN')
    scan = rd('b610_census_termscan.txt')
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', scan, re.M) is not None
    live = re.search(r'live uses\s*: (\d+)', scan)
    body = ed[:E['bm'] - 1]
    beyond = _ceiling_body(body, len(body))
    cok, cbad = _carried(cur, ed, E)
    allowed = E['removals'] + E['ruled'] + E['history_lines'] + E['version_lines']
    dn = E['n_body'] - E['n_cur_body']
    h28a = 'HOLDS'
    h28b = 'HOLDS' if abs(dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if clean and not beyond else 'REFUTED'
    CJ = jl('b610_census.json')
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): the head :1-:9 unmoved; +2 from :10 (the version line and its blank); the current '
         ':12-:21 at %s; the current :%d-:%d moved whole into the back matter (R-8)' % ('%d-%d' % (E['pos']['test0'], E['pos']['test1']), E['moved_from'], E['cur_len']),
         'b610 -- COMPONENT 3: THE DIFF BANK OF THE_KEYSTONE_CENSUS v0.3 against the current version at %s; the final file sha256 %s (%d lines, '
         '%d bytes)' % (PRE_PP, E['sha256'], E['lines'], E['bytes']), '',
         '### THE BODY: the current version`s %d sentences against v0.3`s %d; the removals (moved whole) %d; the ruled insertions (§0 ruled, §1 '
         'the rows, §2, §3) %d; the history line 1; the version line 1; the BACK MATTER %d' % (
             E['n_cur_body'], E['n_body'], E['removals'], E['ruled'], E['n_backmatter']),
         '### THE ROWS, EACH WITH ITS LINE IN v0.3 AND ITS REGISTRY LINES:']
    for row in CJ['rows']:
        L.append('  %s :%d -- %s -- REGISTRY %s -- keystone %s' % (row['n'], E['pos'][row['n']], row['label'], ', '.join(':%d' % x['line'] for x in row['rows']),
                                                                   'yes' if row['has_keystone'] else 'none'))
    L += ['### THE TEST RULED: §0 at its line; the current §0 carried at :%d-:%d; the history line at :%d' % (E['pos']['test0'], E['pos']['test1'], E['pos']['hist']),
          '### CARRIED: %d of %d non-blank current lines found verbatim in v0.3 (failing %s)' % (cok, sum(1 for l in cur if l.strip()), cbad or 'none'),
          '### THE SCANNER: %s, live %s ; the ceiling pattern in the body: %s' % ('CLEAN' if clean else 'NOT CLEAN', live.group(1) if live else '?', beyond or 'none'),
          '', '### ### **H28a %s** -- VACUOUS on its letter: the census has no work-list (b558 none), so no MOVED-IN-MEANING sentence; beside it, '
          'every row cites its REGISTRY lines and every cell its source (the bank`s Part A)' % h28a,
          '### ### **H28b %s** -- the body %+d against at most %d (removals %d + ruled %d + history 1 + version 1), VACUOUS in the reorganising '
          'reading as b604`s was; the strict figure printed: the ruled insertions and the moved whole are the body`s whole change' % (h28b, dn, allowed, E['removals'], E['ruled']),
          '### ### **H28c %s** -- the scanner %s, 0 live stems by its count %s; the ceiling pattern in the body %s' % (
              h28c, 'CLEAN' if clean else 'NOT CLEAN', live.group(1) if live else '?', len(beyond)),
          '### ### **THE CENSUS LANDS: NO SENTENCE HELD.**' if not cbad else '### ### **HELD AT %s.**' % cbad]
    put_txt('b610_edition_CENSUS.txt', L)
    put_json('b610_h28_census.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, body_dn=dn, allowed=allowed, clean=clean, live=int(live.group(1)) if live else None,
                                          beyond=len(beyond), carried_ok=cok, carried_bad=cbad, vacuous_a=True))
    print(L[-5:])


def spiral_bank(*a):
    E = jl('b610_spiral_edition.json')
    ed = _ed(SPI7)
    cur = _cur(SPI)
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### v0.7 ON DISK IS NOT THE BANKED BYTES -- NOTHING WRITTEN')
    scan = rd('b610_spiral_termscan.txt')
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', scan, re.M) is not None
    live = re.search(r'live uses\s*: (\d+)', scan)
    body = ed[:E['bm'] - 1]
    hits = _ceiling_body(body, len(body))
    carried_at = set(E['where'][str(n)] for n in SP_CARRY)
    beyond = [(n, w) for n, w in hits if n not in carried_at]
    cok, cbad = _carried(cur, ed, E)
    allowed = E['ruled'] + E['version_lines'] + sum(abs(x['d']) for x in E['seg_d'])
    dn = E['n_body'] - E['n_cur_body']
    fixed_ok = all(ed[f['at'] - 1].count(f['new']) == 1 and ed[f['at'] - 1].count(f['old']) == 0 for f in E['fixes'])
    h28a = 'HOLDS'
    h28b = 'HOLDS' if abs(dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if clean and not beyond and fixed_ok else 'REFUTED'
    L = ['### OFFSET FROM v0.6 (R190)(3): +2 from :%d (the version line and its blank); +%d more from :%d (the census rows)' % (
        VLINE6, E['pos']['pt1'] - E['pos']['pt0'] + 2, TABLE_LAST + 2),
         'b610 -- COMPONENT 3: THE DIFF BANK OF SPIRAL_MAP v0.7 against v0.6 at %s; the final file sha256 %s (%d lines, %d bytes)' % (
             PRE_PP, E['sha256'], E['lines'], E['bytes']), '',
         '### THE BODY: v0.6`s %d sentences against v0.7`s %d; the ruled insertions %d; the version line 1; the corrections` segment change %s; '
         'the BACK MATTER %d' % (E['n_cur_body'], E['n_body'], E['ruled'], [x['d'] for x in E['seg_d']], E['n_backmatter']),
         '### THE POINTING LINES at :%d-:%d:' % (E['pos']['pt0'], E['pos']['pt1'])]
    L += ['  :%d %s' % (E['pos']['p%d' % k], ed[E['pos']['p%d' % k] - 1][:400]) for k in range(len(C.SPIRAL_CLUSTERS))]
    L += ['### THE CORRECTIONS, BOTH WORDINGS:']
    L += ['  :%d (v0.6 :%d) %s -- was: “%s” ; now: “%s” ; %s' % (f['at'], f['line'], f['clause'], f['old'], f['new'], f['obj']) for f in E['fixes']]
    L += ['### THE CEILING PATTERN`S OTHER HITS, CARRIED: %s' % ['v0.7 :%d (v0.6 :%d) %s' % (E['where'][str(n)], n, w) for n, w in sorted(SP_CARRY.items())],
          '### CARRIED: %d of %d non-blank v0.6 lines found verbatim or as their recorded correction (failing %s)' % (
              cok, sum(1 for l in cur if l.strip()), cbad or 'none'),
          '### THE SCANNER: %s, live %s ; the ceiling pattern in the body: %d hits, %d carried, beyond %s' % (
              'CLEAN' if clean else 'NOT CLEAN', live.group(1) if live else '?', len(hits), len(hits) - len(beyond), beyond or 'none'),
          '', '### ### **H28a %s** -- VACUOUS on its letter: SPIRAL_MAP has no work-list (it is not on the b558 roster), so no MOVED-IN-MEANING '
          'sentence; beside it, every pointing line names its census row and its members` IDs' % h28a,
          '### ### **H28b %s** -- the body %+d against at most %d (ruled %d + version 1 + the corrections` segment change %d)' % (
              h28b, dn, allowed, E['ruled'], sum(abs(x['d']) for x in E['seg_d'])),
          '### ### **H28c %s** -- the scanner %s, 0 live stems by its count %s; the ceiling pattern`s %d hits in the body, %d corrected away and %d '
          'carried within it, beyond %d' % (h28c, 'CLEAN' if clean else 'NOT CLEAN', live.group(1) if live else '?', len(hits),
                                            sum(1 for f in E['fixes'] if f['clause'] == 'ceiling'), len(hits) - len(beyond), len(beyond)),
          '### ### **THE MAP LANDS: NO SENTENCE HELD.**' if not cbad else '### ### **HELD AT %s.**' % cbad]
    put_txt('b610_edition_SPIRAL.txt', L)
    put_json('b610_h28_spiral.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, body_dn=dn, allowed=allowed, clean=clean, live=int(live.group(1)) if live else None,
                                          hits=len(hits), beyond=len(beyond), carried_ok=cok, carried_bad=cbad, vacuous_a=True, fixed_ok=fixed_ok))
    print(L[-4:])


def _repin(path, J, label, bankname):
    ed = _ed(path)
    pos = J['pos']
    L = ['b610 -- THE RE-PIN STEP (R190)(3), THE FORM`S LAST: %s`s own cited lines read against its final file (sha256 %s)' % (label, J['sha256'][:16])]
    ok = n = 0
    for k, v in sorted(pos.items(), key=lambda kv: kv[1]):
        n += 1
        l = ed[v - 1] if 0 < v <= len(ed) else ''
        good = bool(l.strip())
        if k.startswith('R') and len(k) == 3:
            good = l.startswith('| %s | ' % k)
        elif k == 'hist':
            good = l == HIST3
        elif k == 'test0':
            good = l.startswith('## §0 — THE CATEGORY, DEFINED BEFORE COUNTING')
        elif k == 'ver':
            good = l == VERSION7
        elif k == 'pt0':
            good = l.startswith('**THE CENSUS ROWS — 2026-10-03 (b610)')
        elif k.startswith('p') and k[1:].isdigit():
            good = l.startswith('- **%s** → ' % C.SPIRAL_CLUSTERS[int(k[1:])][0])
        ok += good
        L.append('  {E:%s} -> :%d %s %s' % (k, v, 'HOLDS' if good else '### FAILS', l[:120]))
    bm = '\n'.join(ed[J['bm'] - 1:])
    unres = re.findall(r'\{E:\w+\}', bm)
    L += ['### unresolved tokens in the back matter: %s' % (unres or 'none'),
          '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (ok, n)]
    put_txt(bankname, L)
    print(L[-1])


def census_repin(*a):
    _repin(CEN3, jl('b610_census_edition.json'), 'THE_KEYSTONE_CENSUS v0.3', 'b610_repin_census.txt')


def spiral_repin(*a):
    _repin(SPI7, jl('b610_spiral_edition.json'), 'SPIRAL_MAP v0.7', 'b610_repin_spiral.txt')


# ================================================================================ COMPONENT 4: THE PAGES
def page(k):
    """### after both edition commits: ONE page per call in the foreground, re-emitted from its banked probe (the ζ page from b602`s list
    ### at v0.20, the χ page from b603`s at v0.21; no Lean call). Writes the page only when it changed, and data/b610_page_<k>.json."""
    import chain_page as CP
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b610_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    src_out = os.path.join(D, PROBE[k])
    rc, pg, meta, log = CP.build(os.path.join(D, NODES[k]), pdir, src_out)
    secs = int(time.time() - t0)
    for l in log:
        print('  %s: %s' % (k, l))
    if rc:
        put_json('b610_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    J = dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, at=utc(),
             free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), log=log)
    put_json('b610_page_%s.json' % k, J)
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s ; the probe read %s' % (k, rc, len(b), changed, secs, src_out))
    for x in dl[:60]:
        print('    ' + x[:240])


def page_arms(tag):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b610 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    L.append('### the lists read: %s' % {k: (NODES[k], PROBE[k]) for k in NODES})
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b610_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b610_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
HKEYS = ('H28a-CENSUS', 'H28b-CENSUS', 'H28c-CENSUS', 'H28a-SPIRAL', 'H28b-SPIRAL', 'H28c-SPIRAL', 'H44a', 'H44b', 'H44c', 'H44d')
SCORE_KEYS = HKEYS + ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068',
            'SIDE-structural-error-correction': '6a4f482', 'SIDE-cosmo': 'c5cba30', 'SIDE-silence-principle': '667c254',
            'SIDE-global-section': '3528bcf'}
CURRENTS = (CEN, SPI, 'REGISTRY.md', 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', C.SIEVE4)


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def _s3():
    """### every census row's REGISTRY lines resolve at the pin to a line naming the row's ID or file."""
    R = C.registry()
    CJ = jl('b610_census.json')
    n = ok = 0
    for row in CJ['rows']:
        for x in row['rows']:
            n += 1
            l = R[x['line'] - 1] if 0 < x['line'] <= len(R) else ''
            ok += bool((x['id'] and x['id'] in l) or (x['path'] and (x['path'] in l or os.path.basename(x['path']) in l)))
    return ok, n


def scores():
    HC, HSp = jl('b610_h28_census.json'), jl('b610_h28_spiral.json')
    EC, ES, CJ = jl('b610_census_edition.json'), jl('b610_spiral_edition.json'), jl('b610_census.json')
    Z, X = jl('b610_page_zeta.json'), jl('b610_page_chi.json')
    H = CJ['h44']
    rc, rs = rd('b610_repin_census.txt'), rd('b610_repin_spiral.txt')
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in KERN_PIN}
    kern_ok = kern == KERN_PIN
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1', SPI7).split(NL)
                         if x.startswith('?? ')))
    trail_landed = os.path.exists(_p('b610_trail.json'))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', CEN3, SPI7] + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = all(g(PP, 'rev-parse', 'HEAD:' + p).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, p)).strip()
                   and not g(PP, 'status', '--porcelain', '--', p).strip() for p in CURRENTS)
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b610_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b609_closing_push_out.txt'))
    m1, m2 = re.search(r'RE-PIN : (\d+) of (\d+)', rc), re.search(r'RE-PIN : (\d+) of (\d+)', rs)
    arms2 = rd('b610_page_arms_c2.txt')
    s3ok, s3n = _s3()
    h44d = 'HOLDS' if all(HC.get(k) == 'HOLDS' for k in ('H28a', 'H28b', 'H28c')) and all(HSp.get(k) == 'HOLDS' for k in ('H28a', 'H28b', 'H28c')) else 'REFUTED'
    S = {
        'H28a-CENSUS': (HC.get('H28a'), 'v0.3: VACUOUS on its letter (no work-list row); every row cites its REGISTRY lines'),
        'H28b-CENSUS': (HC.get('H28b'), 'v0.3: the body %+d against at most %d, VACUOUS in the reorganising reading' % (HC.get('body_dn', 0), HC.get('allowed', 0))),
        'H28c-CENSUS': (HC.get('H28c'), 'v0.3: the scanner %s, %s live; the ceiling pattern in the body %s' % ('CLEAN' if HC.get('clean') else 'NOT CLEAN', HC.get('live'), HC.get('beyond'))),
        'H28a-SPIRAL': (HSp.get('H28a'), 'v0.7: VACUOUS on its letter (no work-list row); every pointing line names its rows'),
        'H28b-SPIRAL': (HSp.get('H28b'), 'v0.7: the body %+d against at most %d' % (HSp.get('body_dn', 0), HSp.get('allowed', 0))),
        'H28c-SPIRAL': (HSp.get('H28c'), 'v0.7: the scanner %s, %s live; the ceiling pattern %s hits, beyond %s' % (
            'CLEAN' if HSp.get('clean') else 'NOT CLEAN', HSp.get('live'), HSp.get('hits'), HSp.get('beyond'))),
        'H44a': (H['H44a'], '%d registry rows, unplaced %d, the census rows` sum %d' % (H['n_rows'], H['unplaced'], H['sums'])),
        'H44b': (H['H44b'], '%d clusters with documents and no keystone (%s), bound 5 to 8' % (len(H['kl']), ', '.join(H['kl']))),
        'H44c': (H['H44c'], '%d of %d tagged kernels read back at their remotes; with no tag %s; local-only tags in %d kernels, printed' % (
            H['back'], H['tagged'], H['untagged'] or 'none', len(H['local_only']))),
        'H44d': (h44d, 'H28a-H28c: v0.3 %s %s %s ; v0.7 %s %s %s' % (HC.get('H28a'), HC.get('H28b'), HC.get('H28c'), HSp.get('H28a'), HSp.get('H28b'), HSp.get('H28c'))),
        'N1': ('HELD' if H['H44a'] == 'HOLDS' else 'REFUTED', 'every registry row lands in one census row: %d rows, unplaced %d' % (H['n_rows'], H['unplaced'])),
        'N2': ('HELD' if H['H44b'] == 'HOLDS' else 'REFUTED', '%d clusters have documents and no keystone under the taxonomy' % len(H['kl'])),
        'N3': ('HELD' if H['H44c'] == 'HOLDS' else 'REFUTED', '%d of %d current tags read back; %s with no tag' % (H['back'], H['tagged'], H['untagged'] or 'none')),
        'N4': ('HELD' if h44d == 'HOLDS' and not HC.get('carried_bad') and not HSp.get('carried_bad') else 'REFUTED',
               'H28a-H28c hold for both editions %s ; sentences held: v0.3 %s, v0.7 %s' % (h44d, HC.get('carried_bad'), HSp.get('carried_bad'))),
        'N5': ('HELD' if kern_ok and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
               'nothing deposits; every kernel`s main unmoved %s; every current version unedited %s; PLACE-papers %s (wanted %s); relay files '
               'beyond the act`s banks, tools and the table %s%s' % (kern_ok, cur_same, pp_ch, want_pp, relay_beyond, '' if trail_landed else ' ; the trail record pending')),
        'S1': ('HELD' if m1 and m2 and m1.group(1) == m1.group(2) and m2.group(1) == m2.group(2) else 'REFUTED',
               'the re-pin steps: v0.3 %s ; v0.7 %s' % (m1.group(0) if m1 else 'no bank', m2.group(0) if m2 else 'no bank')),
        'S2': ('HELD' if not HC.get('carried_bad') and not HSp.get('carried_bad') else 'REFUTED',
               'every non-blank line carried: the census %s (failing %s) ; SPIRAL_MAP %s (failing %s)' % (
                   HC.get('carried_ok'), HC.get('carried_bad'), HSp.get('carried_ok'), HSp.get('carried_bad'))),
        'S3': ('HELD' if s3n and s3ok == s3n else 'REFUTED', 'every census row`s REGISTRY lines resolve at %s to a line naming its row: %d of %d' % (PRE_PP, s3ok, s3n)),
        'S4': ('HELD' if Z.get('changed') is False and X.get('changed') is False else 'REFUTED',
               'neither page changes: the ζ page changed %s ; the χ page changed %s' % (Z.get('changed'), X.get('changed'))),
        'S5': ('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
               'after the editions: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    }
    put_json('b610_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-12s %s -- %s' % (k, S[k][0], str(S[k][1])[:230]))


def _title():
    CJ = jl('b610_census.json')
    return ('## The phase-state reading: THE_KEYSTONE_CENSUS at v0.3 as one row per phase and cluster -- %d rows, %d clusters without a '
            'keystone named with their documents; the keystone test ruled to the taxonomy; SPIRAL_MAP at v0.7 pointing to the rows'
            % (len(CJ['rows']), len(CJ['h44']['kl'])))


TRAIL_HEAD = ('### b610 — lane three, act thirty-seven under (R220): the phase-state reading -- THE_KEYSTONE_CENSUS at v0.3 one row per '
              'phase and cluster, the keystone test ruled to the taxonomy, SPIRAL_MAP at v0.7 pointing to the rows; the synthesis sequence named')
SEQ_START = 611


def _sequence():
    CJ = jl('b610_census.json')
    folders = {}
    for row in CJ['rows']:
        if not row['has_keystone']:
            ds = sorted(set(os.path.dirname(x['path']) for x in row['rows'] if x['path'] and '/' in x['path']))
            folders[row['n']] = ds
    out = []
    k = SEQ_START
    for row in CJ['rows']:
        if not row['has_keystone']:
            out.append(('b%d' % k, row['n'], row['label'], folders[row['n']] or ['outside the repository tree'], [x['id'] or x['path'] for x in row['rows']]))
            k += 1
    return out


def _finding_text():
    S, HC, HSp, EC, ES, CJ = (jl('b610_scores.json'), jl('b610_h28_census.json'), jl('b610_h28_spiral.json'), jl('b610_census_edition.json'),
                              jl('b610_spiral_edition.json'), jl('b610_census.json'))
    rl, A = jl('b610_record_lines.json'), jl('b610_residue_addendum.json')
    w1, w2, t1, s1 = [x['line'] for x in rl['lines']]
    cc, sc = _pp_commit('b610 (R220)(4): ' + CEN3), _pp_commit('b610 (R220)(4): ' + SPI7)
    H = CJ['h44']
    kl = [r for r in CJ['rows'] if not r['has_keystone']]
    t = _title()
    e = ['', t, '',
         '*Filed at b610 on the author’s ruling `(R220)`. Banks: relay `data/b610_reads.txt`, `data/b610_census.txt`, `data/b610_edition_CENSUS.txt`, '
         '`data/b610_edition_SPIRAL.txt`, `data/b610_repin_census.txt`, `data/b610_repin_spiral.txt`, `data/b610_residue_addendum.txt`, '
         '`data/b610_page_arms_c2.txt`. Nothing deposits.*', '',
         '**The census at v0.3** (`(R220)`(4)). PLACE-papers `%s` (commit %s) beside the current version, unedited: %d registry rows read and '
         'placed, one rule each, in %d rows, one per phase and cluster as REGISTRY lists them (Phase 1 / Day 1; Phase 1.2; 1.5A to 1.5H; 2A '
         'to 2G; Phase 2’s rows filed to no lettered cluster; the support tier; the internal works; the global-section era; the annex; the '
         'rows under no phase heading); each row with its documents, its keystones by tier, its edition state, the sieve rows it holds at '
         'v0.4, its kernels with their current tags read by ls-remote, and its deposit state. The current version’s body moved whole into '
         'the back matter under the reorganising clause; its §0 test carried beneath the ruled test with its history line.' % (
             CEN3, cc, H['n_rows'], len(CJ['rows'])), '',
         '**The clusters with documents and no keystone** (its §2): %s.' % '; '.join('%s %s' % (r['n'], r['label']) for r in kl), '',
         '**The keystone test, ruled** (`(R220)`(3)). The taxonomy governs: K by certification at a pin, KC (`(R19)`), C by synthesis, N, E; '
         'b375’s three tests close (OPEN_TRAILS :%d).' % t1, '',
         '**SPIRAL_MAP at v0.7** (`(R220)`(4)). PLACE-papers `%s` (commit %s) beside v0.6, unedited: §4A’s table takes one line per cluster '
         'pointing to the census rows, by `(R17)`’s form; one stem and three ceiling sentences corrected by the form’s clauses.' % (SPI7, sc), '',
         '**The kernels.** %d read by ls-remote; %d tagged, %d read back at their remotes; %s with no tag; %d carry local tags their remotes '
         'do not, printed and not repaired.' % (len(CJ['remotes']), H['tagged'], H['back'], ', '.join(H['untagged']) or 'none', len(H['local_only'])), '',
         '**The second reader’s addendum** (`(R220)`(2)). relay `data/b610_residue_addendum.txt`: %s lines read, %s kin; no sentence rewritten.' % (
             A.get('n'), A.get('kin')), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the census re-reads b375’s census (OPEN_TRAILS :4049, its six clusters without a '
         'keystone under its own test) under the ruled taxonomy, and b388’s refreshed cluster table (:4391, SPIRAL_MAP §4A) against the '
         'registry’s phases; its sieve column reads b609’s v0.4 (FINDINGS :7186) by cluster. It strengthens the programme’s offering of the '
         'census: every registry row has one row, one tier read and its source, and the clusters the synthesis sequence takes are named '
         'from the registry and the taxonomy rather than from a directory.', '',
         '**The record lines.** b609’s weight at FINDINGS :%d; the enumeration reading at :%d; the keystone test ruled at OPEN_TRAILS :%d; '
         'the synthesis sequence’s form at :%d.' % (w1, w2, t1, s1), '',
         '**Next.** Per `(R220)`(6): b611, the synthesis act for the census’s opening-listed cluster, %s; W-ORD-QUANTIFIER-COLUMN’s generator '
         'follows the sequence. The author rules on the closing.' % ('%s %s' % (kl[0]['n'], kl[0]['label']) if kl else '?'), '',
         '*Nothing deposits; no keystone edited beyond the two editions written beside their current versions; README and REGISTRY unwritten; '
         'nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    return t, NL.join(e)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    bad = ledger_check(e)
    print('  grade-word lines naming a backticked name: %s' % (bad or 'NONE'))
    if 'dry' in a:
        print(e)
        return
    if bad:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b610_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def _trail_text():
    S, fj, rl = jl('b610_scores.json'), jl('b610_findings.json'), jl('b610_record_lines.json')
    w1, w2, t1, s1 = [x['line'] for x in rl['lines']]
    seq = _sequence()
    rows_ = ['', TRAIL_HEAD, '',
             '**(R220) ratified.** (1) b609 at its weight, the navigator’s BRIGHT refuted. (2) The enumeration’s compiled form, a reading for '
             'the record, the second reader’s addendum listed. (3) The keystone test ruled to the taxonomy; b375’s item closed. (4) The '
             'phase-state reading, the act: THE_KEYSTONE_CENSUS at v0.3, SPIRAL_MAP at v0.7; H44a-H44d. (5) The synthesis sequence, entered. '
             '(6) The act after: b611.', '',
             '**Entered:** FINDINGS.md:%d (b609’s weight), :%d (the enumeration reading), :%d (the entry, with its mutual-light line); '
             'OPEN_TRAILS :%d (the keystone test ruled, addressed to b375’s census :4049 and b609’s phase-state line :12544), :%d (the synthesis '
             'sequence’s form); this record; PLACE-papers `%s` and `%s` (each beside its current version, unedited); both pages re-emitted, '
             'unchanged; relay data/b610_census.txt, data/b610_residue_addendum.txt.' % (w1, w2, fj['entry_line'], t1, s1, CEN3, SPI7), '',
             '**The synthesis sequence, one act per cluster the census names (its §2), in the census’s order** (`(R220)`(5)):']
    for act, n, label, folders, docs in seq:
        where = ('`%s`' % '`, `'.join(folders)) if folders != ['outside the repository tree'] else 'the download layer, outside the repository tree'
        rows_.append('- **%s** -- %s %s: one new document in the cluster’s folder, written from its papers (%s), which sit in %s.' % (
            act, n, label, ', '.join(docs), where))
    rows_ += ['', '**Resolved by the seat, for the author’s strike:** the census’s readings R-1 to R-8 (the population, the placement, the '
              'tier order, the edition state, the sieve rows by SPIRAL_MAP’s members, the kernels and their current tags, the deposit state, '
              'the body moved whole); SPIRAL_MAP’s R-1 to R-3 (the pointing lines beneath the table, the members from its cells, the four '
              'clause corrections); the addendum banked beside b609’s seed, that bank not edited. No prompt was put (relay '
              'data/b610_author_answers.txt).', '',
              '**For the author:** the ruling’s “Tier E errata-class” is the navigator’s wording -- the taxonomy defines Tier E as filing-facing '
              '(THE_DOCUMENT_CLASS_TAXONOMY :20); %d kernels carry local tags their remotes do not (relay data/b610_census.txt, Part C), '
              'among them SIDE-substrate-cluster’s v0.4, which REGISTRY’s row notes cite; REGISTRY :787 and :333 disagree on whether '
              '`internal/` has a section; the annex’s document lies outside the repository tree, and the sequence’s act for it is named here '
              'for the author to keep or strike; SPIRAL_MAP :104 says each Phase 1.2 kernel forces σ = 1/2, which REGISTRY :731 qualifies for '
              'SIDE-spinor -- not corrected here, the kernels’ statements not being among this act’s reads.' % len(jl('b610_census.json')['h44']['local_only']), '',
              '**Defects** (relay data/b610_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
              '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
              '**Next:** per `(R220)`(6), %s, the synthesis act for the census’s opening-listed cluster; W-ORD-QUANTIFIER-COLUMN’s generator '
              'follows the sequence; the author rules on the closing.' % (seq[0][0] if seq else 'b611'), '',
              '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; FACES_LEDGER untouched; row U1 unedited; `h2` where the '
              'deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def trail(*a):
    Q = R2._Q()
    e = _trail_text()
    bad = ledger_check(e)
    print('  grade-word lines naming a backticked name: %s' % (bad or 'NONE'))
    if 'dry' in a:
        print(e)
        return
    if bad:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b610_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r, sequence=_sequence()))
    print('  OPEN_TRAILS record :%s' % jl('b610_trail.json')['line'])


def desk():
    S = jl('b610_scores.json')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b610 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H28a-H28c for both editions and H44a-H44d, (R220)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H28/H44 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS),
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b610_defects.txt').rstrip(NL).split(NL)
    put_txt('b610_desk_notes.txt', L)


def components():
    S, fj, tj, rl = jl('b610_scores.json'), jl('b610_findings.json'), jl('b610_trail.json'), jl('b610_record_lines.json')
    Z, X = jl('b610_page_zeta.json'), jl('b610_page_chi.json')
    L = ['b610 -- THE COMPONENTS, BANKED UNDER (R220).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b609`s closing push-out relay %s ; push-b609* branches deleted by '
         'name (data/b610_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b610_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b609`s weight FINDINGS :%d ; the enumeration reading :%d ; the keystone test ruled OPEN_TRAILS :%d ; the synthesis '
         'sequence`s form :%d ; the addendum data/b610_residue_addendum.txt' % tuple(x['line'] for x in rl['lines']),
         '### COMPONENT 2 : the census bank data/b610_census.txt ; H44a %s, H44b %s, H44c %s' % (S['H44a'][0], S['H44b'][0], S['H44c'][0]),
         '### COMPONENT 3 : the census %s ; the diff data/b610_edition_CENSUS.txt ; H28a %s, H28b %s, H28c %s ; SPIRAL_MAP %s ; the diff '
         'data/b610_edition_SPIRAL.txt ; H28a %s, H28b %s, H28c %s ; H44d %s' % (
             CEN3, S['H28a-CENSUS'][0], S['H28b-CENSUS'][0], S['H28c-CENSUS'][0], SPI7, S['H28a-SPIRAL'][0], S['H28b-SPIRAL'][0], S['H28c-SPIRAL'][0], S['H44d'][0]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b610_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b611 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b610_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b610_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
