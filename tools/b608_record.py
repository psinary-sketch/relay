# -*- coding: utf-8 -*-
"""b608_record.py -- THE ACT'S RECORD TOOL, UNDER (R218). ### ONE SUBCOMMAND PER BANK.

### ### b608: LANE THREE, ACT THIRTY-FIVE -- CP-8 ACT THREE: THE MONOGRAPH'S REMAINING CHAPTERS BY THE b558 WORK-LIST AND THE
### CLAUSES, §25.8 RE-PINNED, THE WHOLE DOCUMENT AS THE BOUND.
### Subcommands write only `data/b608_*` unless the docstring names another file. Every bank is written through b602_record's
### `put_txt` / `put_json` (encode, temp file, `os.replace`), imported, never copied; every ledger append through b566's guarded
### `append_to` (prefix-proving, stem- and backtick-checked). The work-list is tools/b608_worklist.py's data. No platform call. No
### Lean call: both pages are re-emitted from their banked probes. The template is tools/b607_record.py.
"""
import difflib
import hashlib
import io
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
import b608_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
SKER = 'D:/SIDE-kernel'
RELAY = ROOT.replace('\\', '/')
PRE_PP = '0800a6a'
PRE_RELAY = 'cb598e60'
STEPZERO = 'e73212a5'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7e7c9193-2e8e-4d7a-b6d6-00c3274c98d9/scratchpad'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/7e7c9193-2e8e-4d7a-b6d6-00c3274c98d9.jsonl'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CUR, ED, PREV, ORIG = K.CUR, K.ED, K.PREV, K.ORIG
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
CORR_HEAD = '## Correspondence *(added 2026-08-12'
B606_TAG = '<!-- b606 (R216) THE v5.14 EDITION`S BACK MATTER, 2026-10-03 -->'
B607_TAG = '<!-- b607 (R217) THE v5.15 EDITION`S BACK MATTER, 2026-10-03 -->'
SIEVE = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, put_txt, put_json, jl, rd, sha, utc = R2.g, R2.put_txt, R2.put_json, R2.jl, R2.rd, R2.sha, R2.utc
_show = R4._show
CEILING = R4.CEILING


def _segs(l):
    return R4._segs(l)


def _count(ls):
    return sum(len(_segs(l)) for l in ls)


DEFECTS = []
DEFECT_SHORT = []


def defects():
    L = ['b608 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b608_defects.txt', L)


# ================================================================================ READING (1): THE READS
READS = [
    ('the monograph`s current version v5.15: its head, version lines, :722, Part IV`s preamble, §22.4 and the chain sentence, chapter 24`s '
     'title and opening, §25.5`s table, §25.8 whole, Appendix H, the Correspondence block, the back-matter tags', PP, PRE_PP, CUR,
     [1, 19, 20, 21, 722, 1292, 1305, 1307, 1309, 1311, 1313, 1375, 1377, 1379, 1399, 1401, 1463, 1465, 1487, 1583, 1633, 1634]
     + list(range(1661, 1694)) + [2217, 2219, 2224, 2227, 2231, 2232, 2233, 2235, 2237, 2241, 2243, 2245, 2251, 2258, 2259, 2278, 2428], 300),
    ('relay data/b558_editions/A_Place_to_Stand.txt: the work-list whole (31 rows)', RELAY, STEPZERO, 'data/b558_editions/A_Place_to_Stand.txt', 'ALL', 300),
    ('relay data/b607_edition_PLACE.txt: the whole-document figure (the ceiling by kind, the scanner, the 154 by line)', RELAY, STEPZERO,
     'data/b607_edition_PLACE.txt', ('GREP', r'^### THE CEILING, every hit|^### THE SCANNER|^### THE WHOLE-DOCUMENT FIGURE|-- beyond \(act three'), 200),
    ('the ζ page at its own pin v0.20: its pin line and the nodes this act cites', PP, PRE_PP, PAGE,
     ('GREP', r'^(This page is generated|7\. |8\. |41\. |52\. )'), 260),
    ('the χ page at v0.21: its pin line and h2_sign_chi_iff_grh_chi', PP, PRE_PP, DIR_PAGE, ('GREP', r'^(This page is generated|12\. )'), 260),
    ('the ζ page searched for a SIDE-kernel node (§25.8`s seven): none', PP, PRE_PP, PAGE,
     ('GREP', r'structural_exhaustiveness_proved|spectral_cannon|ConservationBridge|rh_from_structural|SIDEKernel\.formation|all_pairs_excluded'), 200),
    ('the χ page searched for a SIDE-kernel node: none', PP, PRE_PP, DIR_PAGE,
     ('GREP', r'structural_exhaustiveness_proved|spectral_cannon|ConservationBridge|rh_from_structural|SIDEKernel\.formation|all_pairs_excluded'), 200),
    ('SIDE-kernel at v1.3: §25.8`s seven theorems', SKER, 'v1.3', 'Bridge/TheBridgeComplete.lean', [188], 200),
    ('SIDE-kernel at v1.5: TheBridgeComplete.lean (no namespace; structural_exhaustiveness_proved)', SKER, 'v1.5', 'Bridge/TheBridgeComplete.lean', [14, 249], 200),
    ('SIDE-kernel at v1.5: ConservationBridge.lean (its namespace, its conditional structural_exhaustiveness_proved, riemann_hypothesis)',
     SKER, 'v1.5', 'Bridge/ConservationBridge.lean', [7, 46, 47, 53, 54, 57], 200),
    ('SIDE-kernel at v1.5: spectral_cannon', SKER, 'v1.5', 'Kernel/SpectralCannonFull.lean', [11, 65], 200),
    ('SIDE-kernel at v1.5: the Integration theorems', SKER, 'v1.5', 'Kernel/Integration.lean', [55, 221, 252], 200),
    ('SIDE-kernel at v1.5: formation', SKER, 'v1.5', 'Kernel/Core.lean', [16, 53], 200),
    ('SIDE-kernel at v1.5: all_pairs_excluded', SKER, 'v1.5', 'Bridge/CrossClassExclusion.lean', [27, 80], 200),
    ('SIDE-kernel at v1.5: conservation_of_spectra', SKER, 'v1.5', 'Kernel/ProductFormula_Rat.lean', [72, 73], 200),
    ('relay data/terminal_table.json at relay HEAD: the rows of §25.8`s seven and conservation_of_spectra (pin, present_at, statement file)',
     RELAY, STEPZERO, 'data/terminal_table.json', ('TT', None), 0),
    ('tools/banned_terms.py: the exception reading (the back-matter tag, the carried-by-history and name rows, the window)', RELAY, STEPZERO,
     'tools/banned_terms.py', [63, 64, 73, 112, 226, 227, 228, 235, 236, 248], 200),
    ('OPEN_TRAILS: the form, the stem, ceiling, history, name-and-title, fact and restatement clauses, the era line, the precedence order, '
     'the author`s exhaustiveness reading, b605`s record, the multi-act clause and b607`s record', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11864, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 12072, 12082, 12190, 12192, 12194, 12228, 12458, 12496, 12498, 12500], 700),
    ('FINDINGS: b607`s record lines and entry', PP, PRE_PP, 'FINDINGS.md', [7128, 7130, 7132], 300),
    ('README: the ceiling and its rewordings', PP, PRE_PP, 'README.md', [106, 107, 113, 115], 300),
    ('ERRATA: E-2026-09-25-1, E-2026-09-25-5 (E5-01, E5-05, E5-11) and E-2026-09-25-6 (E6-11), as cited', PP, PRE_PP, 'ERRATA.md',
     [486, 617, 629, 631, 641, 643, 735, 737], 260),
    ('relay data/b558_cp1b.txt: the CP-1b rows this act cites', RELAY, STEPZERO, 'data/b558_cp1b.txt', [278, 513, 526, 529, 565, 573, 575], 240),
    ('relay data/b607_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b607_closing_push_out.txt', 'ALL', 260),
    ('relay data/b607_scores.json (whole)', RELAY, STEPZERO, 'data/b607_scores.json', 'ALL', 300),
]
TT_NAMES = ['structural_exhaustiveness_proved', 'ConservationBridge.structural_exhaustiveness_proved', 'SpectralCannonFull.spectral_cannon',
            'ConservationBridge.riemann_hypothesis', 'techne_kernel_integration.rh_from_structural_exhaustiveness',
            'techne_kernel_integration.structural_exhaustiveness_iff_rh', 'SIDEKernel.formation',
            'techne_kernel_cross_exclusion.all_pairs_excluded', 'conservation_of_spectra']


def _tt_rows(text):
    T = json.loads(text or '{}')
    out = []
    for r in T.get('rows') or []:
        if r.get('repo') == 'SIDE-kernel' and r.get('name') in TT_NAMES:
            out.append(r)
    return out


def reads():
    L = ['b608 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS:
        t = _show(repo, rev, path)
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH LINE (the blob does not exist)' % (label, path, at))
            continue
        if sel == ('TT', None):
            rows = _tt_rows(t)
            L.append('### %s -- %s @ %s (%d rows)' % (label, path, at, len(rows)))
            for r in rows:
                L.append('    %-62s pin %s = %s ; present_at %s ; statement_file %s ; head %s' % (
                    r['name'], r.get('pin'), (r.get('pin_sha') or '')[:7], r.get('present_at'), r.get('statement_file'), (r.get('head') or '')[:7]))
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
    L += ['', '### the pages` pins: the ζ page`s list %s %s ; the χ page`s list %s %s' % (
        NODES['zeta'], [l for l in rd(NODES['zeta']).split(NL) if l.startswith('# pin:')], NODES['chi'],
        [l for l in rd(NODES['chi']).split(NL) if l.startswith('# pin:')]),
        '### the monograph at %s: v5.15 blob %s ; v5.14 blob %s ; v5.13 blob %s' % (
            PRE_PP, g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip()[:12], g(PP, 'rev-parse', '%s:%s' % (PRE_PP, PREV)).strip()[:12],
            g(PP, 'rev-parse', '%s:%s' % (PRE_PP, ORIG)).strip()[:12]),
        '### SIDE-kernel tags: v1.3 = %s ; v1.5 = %s ; main = %s' % (
            g(SKER, 'rev-parse', '--short=7', 'v1.3^{}').strip(), g(SKER, 'rev-parse', '--short=7', 'v1.5^{}').strip(),
            g(SKER, 'rev-parse', '--short=7', 'main').strip()),
        '### SIDE-global-section tags: v0.1.0 = %s ; v0.2.0 = %s ; main = %s' % (
            g('D:/SIDE-global-section', 'rev-parse', '--short=7', 'v0.1.0^{}').strip(),
            g('D:/SIDE-global-section', 'rev-parse', '--short=7', 'v0.2.0^{}').strip(), g('D:/SIDE-global-section', 'rev-parse', '--short=7', 'main').strip()),
        '### a fact correction, the navigator`s, carried from (R218)(1): "E-2026-09-25-5" for §27.3`s registers in (R217)(4) -- they stand as '
        'E-2026-09-25-6`s replacements (with -1`s and -4`s) left them, as b607 read (its reading R-8)']
    put_txt('b608_reads.txt', L)


# ================================================================================ THE AUTHOR'S ANSWERS
def answers():
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
    L = ['### b608 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat (2026-10-03), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % n, '']
    k = 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session 7e7c9193-2e8e-4d7a-b6d6-00c3274c98d9, transcript line %d)' % (cid, i))
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
    put_txt('b608_author_answers.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B607_ENTRY = '## CP-8, act two: the monograph’s v5.15 over chapters 21–22'
B605_RECORD = '### b605 — lane three, act thirty-two under (R215): the sieve table at v0.3'
B607_RECORD = '### b607 — lane three, act thirty-four under (R217): CP-8 act two'
W_HEAD = '*Appended 2026-10-03 by b608 to b607’s entry (:%d), under `(R218)`(1) -- b607 AT ITS WEIGHT:*'
F_HEAD = '*Appended 2026-10-03 by b608 to b607’s entry (:%d), under `(R218)`(1) -- A FACT CORRECTION, THE NAVIGATOR’S:*'
V_HEAD = ('*Appended 2026-10-03 by b608 to b605’s record of the sieve at v0.3 (:%d), under `(R218)`(2) -- THE SIEVE’S v0.4 WORK-LIST, '
          'ENTERED FOR b609, THE ACT AFTER CP-8, NOT THIS ONE:*')
G_HEAD = '*Appended 2026-10-03 by b608 to b607’s record (:%d), under `(R218)`(3) -- THE §22.4 ITEM, ENTERED ON ACT THREE’S WORK-LIST:*'


def _b607():
    S = json.loads(_show(RELAY, STEPZERO, 'data/b607_scores.json'))
    return {k: v[0] for k, v in S.items()}


def _texts(entry, srec, rec7):
    s = _b607()
    rp = _show(RELAY, STEPZERO, 'data/b607_repin.txt') or ''
    m = re.search(r'RE-PIN : (\d+) of (\d+)', rp)
    h1, h2, h3, h4 = W_HEAD % entry, F_HEAD % entry, V_HEAD % srec, G_HEAD % rec7
    t1 = ('\n%s PLACE-papers `day1/A_Place_to_Stand_v5_15.md` (f74ada0) beside v5.14 and v5.13 unedited, ERRATA 3550569 alone, the '
          'pages 2d8c2c9 and ae4c82c, the record 0800a6a: chapters 21–22, 14 sentences and titles joining simplicity and RH taken to the '
          'ceiling, simplicity the second located clause (simplicity_iff v0.17) beside positivity_not_imp_simplicity (v0.19) and the b596 '
          'walk, the perpendicular-crossing theorem standing; §24.4’s analytic-row note dated, so the SimpleProportion reading in a history '
          'line beneath it by the precedence order -- correct; the table’s sieve column (Conrey to RH-16, DARK, test 1; GUE to the bench’s '
          'fit, DARK, test 1, no row of its own; computation, no row; the Epstein witnesses to FD-01 and FD-02, NOT A ROUTE; the mechanism '
          'enumeration, no row); §27.3 at four corrections (two ceiling, two restatements of the five-registers claim E6-04 had corrected), '
          '“convergent, not independent” carried; re-pin %s of %s; handed to act three: 154 ceiling hits and the live stem at v5.15 :722. '
          'The verdicts, as relay data/b607_scores.json prints them: H28a %s, H28b %s, H28c %s on scope (the whole document refuted in '
          'letter, printed); H41a %s; H41b %s, H41c %s, H41d %s; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s; S1-S5 %s -- H41b-H41d and N2-N4 '
          'refuted by the material (the three rows without a sieve row, §27.3’s four against two, 17 of 171 against 40), the navigator’s '
          'bounds, each recorded as such. FINDINGS :7128, :7130, :7132; OPEN_TRAILS :12496, :12498; ERRATA :835, :837, :839, appended at '
          'the ledger’s end addressed to their entries because insertion would move lines v5.14 cites -- correct, the placement law of the '
          'trails. Relay fa7722b7, 3de4485f, cb598e60; the suite 79 of 79 before and after the push. Defect (a) the seat’s (a positive '
          'control on a blank line), corrected and the suite re-run whole. Nothing deposited; no kernel touched.\n' % (
              h1, m.group(1) if m else '?', m.group(2) if m else '?', s['H28a'], s['H28b'], s['H28c'], s['H41a'], s['H41b'], s['H41c'],
              s['H41d'], s['N1'], s['N2'], s['N3'], s['N4'], s['N5'],
              'HELD' if all(s['S%d' % i] == 'HELD' for i in range(1, 6)) else [s['S%d' % i] for i in range(1, 6)]))
    t2 = ('\n%s “E-2026-09-25-5” for §27.3’s registers in `(R217)`(4) -- the registers stand as E-2026-09-25-6’s replacements (with -1’s '
          'and -4’s) left them, as b607 read them (its reading R-8). Recorded as the navigator’s; no reading of b607 moves.\n' % h2)
    t3 = ('\n%s three rows the monograph’s convergence table (§24.4) needs that THE_FINDINGS_AS_THEY_STAND v0.3 lacks -- (i) the '
          'computational range (10¹³ zeros simple and on the line; FINITE; NOT A ROUTE, a bench fact); (ii) GUE statistics as a row of its '
          'own beside the super-repulsion fit (DENSITY-shaped statistics; DARK by test 1); (iii) the mechanism enumeration (the seven '
          'classes, Ostrowski-exhaustive; the route that located h2, so BRIGHT by test 2, with the detector as the instrument that shows C₂ '
          'is the class the control removes) -- each verdict here the navigator’s reading, marked as a reading, for the seat to print '
          'against the pages at b609; and the Epstein witnesses’ two rows FD-01 and FD-02, read once for whether they are one conclusion or '
          'two. At v0.4 the table’s “no row” cells are corrected to the new rows, and the monograph’s sieve column at its next version. '
          'Nothing of this is done at b608.\n' % h3)
    t4 = ('\n%s the seat’s reading accepted -- the fold criterion (§22.4) runs from a fold to an off-line zero while the chain’s last link '
          'reads the converse; the sentence stating the link names its direction and marks the converse as the open direction, citing the '
          'perpendicular-crossing theorem for what is compiled and nothing for what is not, carried with a history line beneath it and not '
          'rewritten past the ceiling (relay data/b608_worklist_PLACE.txt, PART E; H42d).\n' % h4)
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
    return Q, Q.line_of(Q.FIND, B607_ENTRY), Q.line_of(Q.OT, B605_RECORD), Q.line_of(Q.OT, B607_RECORD)


def record_lines(*a):
    """### PLACE-papers FINDINGS: b607's weight and the navigator's fact correction, addressed to b607's entry; OPEN_TRAILS: the sieve's
    ### v0.4 work-list addressed to b605's record of the sieve at v0.3, and the §22.4 item addressed to b607's record (where act three's
    ### work-list is priced) -- each appended at the end (the ledgers are append-only). `dry` prints."""
    Q, entry, srec, rec7 = _addr()
    if (entry, srec, rec7) != (7132, 12458, 12498):
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s, %s) -- NOTHING WRITTEN' % (entry, srec, rec7))
    parts = _texts(entry, srec, rec7)
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
    put_json('b608_record_lines.json', dict(entry=entry, srec=srec, rec7=rec7, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


# ================================================================================ COMPONENT 2: THE WORK-LIST
def _b154():
    """### b607`s 154: the hits its diff bank prints as beyond, by v5.15 line."""
    t = _show(RELAY, STEPZERO, 'data/b607_edition_PLACE.txt') or ''
    return [(int(m.group(1)), m.group(2)) for m in re.finditer(r'^    :(\d+) \(v5\.14 :\d+\) "([^"]+)" -- beyond', t, re.M)]


def _a2_carries():
    """### act two`s carried hits (b607`s CARRIES, their v5.14 lines mapped to v5.15 by b607`s own map)."""
    import b607_worklist as K7
    E7 = json.loads(_show(RELAY, STEPZERO, 'data/b607_edition.json'))
    w7 = {int(k): v for k, v in E7['where'].items()}
    return [(w7[n], frag, why) for n, frag, why in K7.CARRIES]


def _a1_hits():
    t = _show(RELAY, STEPZERO, 'data/b607_edition_PLACE.txt') or ''
    return [(int(m.group(1)), m.group(2)) for m in re.finditer(r'^    :(\d+) \(v5\.14 :\d+\) "([^"]+)" -- act one`s$', t, re.M)]


def _hit_fate(M, n, p, rows_by_line, a2):
    """### the fate of the hit at position p of v5.15 line n: the change whose old span holds it, the carry whose fragment holds it, act
    ### two`s carry whose sentence holds it, or UNREAD."""
    l = M[n - 1]
    for c in rows_by_line.get(n, []):
        a = l.index(c['old'])
        if a <= p < a + len(c['old']):
            return 'corrected', c['id']
    for m, frag, exc, why in K.CARRIES:
        if m == n:
            a = l.index(frag)
            if a <= p < a + len(frag):
                return 'carried', '%s -- %s' % (exc, why)
    for m, frag, why in K.PRIOR_CARRIES:
        if m == n:
            a = l.index(frag)
            if a <= p < a + len(frag):
                return 'carried', 'a carry of act one -- %s' % why
    acc = 0
    for s in _segs(l):
        k = l.find(s, acc)
        if k <= p < k + len(s) and any(m == n and frag in s for m, frag, _w in a2):
            why = next(w for m, frag, w in a2 if m == n and frag in s)
            return 'carried', 'a carry of act two, ratified at (R218)(1) -- %s' % why
        acc = k + len(s) if k >= 0 else acc
    return 'UNREAD', None


def _body_hits(M, rows):
    by = {}
    for r in rows:
        by.setdefault(r['line'], []).append(r)
    a2 = _a2_carries()
    out = []
    for n in range(1, K.CORR_LINE):
        for h in CEILING.finditer(M[n - 1]):
            fate, why = _hit_fate(M, n, h.start(), by, a2)
            out.append(dict(line=n, pos=h.start(), hit=h.group(0), fate=fate, why=why))
    return out


def worklist(*a):
    """### data/b608_worklist_PLACE.txt (and .json), banked before any writing of the edition."""
    L, data = _wl()
    put_txt('b608_worklist_PLACE.txt', L)
    put_json('b608_worklist.json', data)
    print('  rows %d (rewritten %d, landed %d, history lines %d) ; the 154: corrected %d, carried %d, unread %d ; body hits %d, unread %d ; '
          '§25.8 entries %d, moved %d' % (
              len(data['rows']), data['rows_rewritten'], data['rows_landed'], data['rows_history'], data['c154'], data['k154'], data['u154'],
              len(data['hits']), sum(1 for h in data['hits'] if h['fate'] == 'UNREAD'), len(data['conc']), sum(1 for c in data['conc'] if c['moved'])))


def _wl_data():
    p = os.path.join(D, 'b608_worklist.json')
    return jl('b608_worklist.json') if os.path.exists(p) else _wl()[1]


def _conc():
    T = json.loads(_show(RELAY, STEPZERO, 'data/terminal_table.json') or '{}')
    trows = {r['name']: r for r in T.get('rows') or [] if r.get('repo') == 'SIDE-kernel'}
    zp = _show(PP, PRE_PP, PAGE) or ''
    xp = _show(PP, PRE_PP, DIR_PAGE) or ''
    out = []
    for n, thm, mod, a_, b_, tt in K.CONCORDANCE:
        short = thm.split('.')[-1]
        f3 = _show(SKER, 'v1.3', mod) or ''
        f5 = _show(SKER, 'v1.5', mod) or ''
        fm = _show(SKER, 'main', mod) or ''
        def at(t, ln):
            ls = t.split(NL)
            return ls[ln - 1] if 0 < ln <= len(ls) else ''
        ok3 = re.search(r'theorem %s\b' % re.escape(short), at(f3, a_)) is not None
        ok5 = re.search(r'theorem %s\b' % re.escape(short), at(f5, b_)) is not None
        okm = re.search(r'theorem %s\b' % re.escape(short), at(fm, b_)) is not None
        r = trows.get(tt) or {}
        out.append(dict(line=n, thm=thm, module=mod, v13=a_, v15=b_, ok_v13=ok3, ok_v15=ok5, ok_main=okm,
                        table_name=tt, table_pin=r.get('pin'), table_pin_sha=(r.get('pin_sha') or '')[:7], table_present=r.get('present_at'),
                        table_file=r.get('statement_file'), on_zeta=short in zp, on_chi=short in xp, moved=True,
                        resolved=ok5 and r.get('pin') == 'v1.5'))
    return out


def _wl():
    M, rows, bad = K.resolve()
    if bad:
        sys.exit('### THE WORK-LIST DOES NOT RESOLVE: %s -- NOTHING WRITTEN' % bad)
    hits = _body_hits(M, rows)
    b154 = _b154()
    b558 = _show(RELAY, STEPZERO, 'data/b558_editions/A_Place_to_Stand.txt') or ''
    v13 = K.lines_of(_show(PP, PRE_PP, ORIG))
    L = ['b608 -- COMPONENT 2: CP-8 ACT THREE`S WORK-LIST, (R218)(4) -- ASSEMBLED BEFORE ANY WRITING, banked %s' % utc(),
         '### the current version: PLACE-papers %s @ %s, %d lines, blob %s; its version line :19 "%s"' % (
             CUR, PRE_PP, len(M), g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip()[:12], M[18][:80]),
         '### the next version by its own series: v5.16, written beside it as %s' % ED,
         '### the bound: the whole document under the multi-act clause (OPEN_TRAILS :12496) -- the plan`s final act', '',
         '### PART A -- THE b558 WORK-LIST`S 31 ROWS (relay data/b558_editions/A_Place_to_Stand.txt, numbered by v5.13), READ LINE BY LINE, '
         'EACH WITH ITS v5.15 LINE AND ITS LANDING:']
    rws = re.findall(r'^:(\d+) -- `([^`]+)`\n    the sentence: "(.*)"\n    what the compiled fact supports: (.*)$', b558, re.M)
    cid = {r['id']: r for r in rows}
    rows_out = []
    for (k, n13, term, n15, landing, needle), (bn, bterm, bsent, bsup) in zip(K.ROWS, rws):
        same = int(bn) == n13 and bterm == term
        L += ['  row %d :%d `%s` -> v5.15 :%d -- %s%s' % (k, n13, term, n15, landing, '' if same else ' ### THE ROW DOES NOT MATCH THE BANK'),
              '      the sentence (v5.13): %s' % bsent[:400], '      what the compiled fact supports: %s' % bsup[:300]]
        if landing.startswith('rewritten'):
            c = cid[landing.split(': ')[1]]
            L += ['      v5.15 : %s' % c['old'], '      v5.16 : %s' % c['new'], '      cites : %s' % c['cites']]
        elif landing.startswith('landed'):
            L.append('      v5.15 :%d holds “%s” -- %s' % (n15, needle, needle in M[n15 - 1]))
        else:
            L.append('      v5.15 :%d -- %s' % (n15, M[n15 - 1][:200]))
        rows_out.append(dict(row=k, v13=n13, term=term, v15=n15, landing=landing, needle=needle, matches=same,
                             holds=(needle in M[n15 - 1]) if needle else None))
    L.append('  rows %d ; rewritten %d ; landed at act one %d ; history lines (the dated Correspondence) %d ; the bank`s rows matched %d' % (
        len(rows_out), sum(1 for r in rows_out if r['landing'].startswith('rewritten')), sum(1 for r in rows_out if r['landing'].startswith('landed')),
        sum(1 for r in rows_out if r['landing'].startswith('history')), sum(1 for r in rows_out if r['matches'])))
    L += ['', '### PART B -- THE 154 CEILING HITS BY LINE (relay data/b607_edition_PLACE.txt), EACH WITH ITS DISPOSITION, AND THE BODY`S OTHER HITS:']
    by_ln = {}
    for h in hits:
        by_ln.setdefault(h['line'], []).append(h)
    used, d154 = {}, []
    for n, w in b154:
        cand = [h for h in by_ln.get(n, []) if h['hit'] == w and (n, h['pos']) not in used]
        h = cand[0] if cand else None
        if h:
            used[(n, h['pos'])] = True
        d154.append(dict(line=n, hit=w, fate=h['fate'] if h else 'MISSING', why=h['why'] if h else None, pos=h['pos'] if h else None))
        L.append('  :%d "%s" -- %s -- %s' % (n, w, d154[-1]['fate'], d154[-1]['why']))
    c154 = sum(1 for x in d154 if x['fate'] == 'corrected')
    k154 = sum(1 for x in d154 if x['fate'] == 'carried')
    u154 = len(d154) - c154 - k154
    L.append('  the 154: corrected %d ; carried under a named exception %d ; unread or missing %d' % (c154, k154, u154))
    a1 = _a1_hits()
    L.append('  ### the body`s other hits (act one`s lines, act two`s carries), each with its fate:')
    others = [h for h in hits if (h['line'], h['pos']) not in used]
    for h in others:
        L.append('  :%d "%s" -- %s -- %s' % (h['line'], h['hit'], h['fate'], h['why']))
    L.append('  body hits %d ; corrected %d ; carried %d ; unread %d ; act one`s lines` hits in b607`s bank %d' % (
        len(hits), sum(1 for h in hits if h['fate'] == 'corrected'), sum(1 for h in hits if h['fate'] == 'carried'),
        sum(1 for h in hits if h['fate'] == 'UNREAD'), len(a1)))
    L.append('  ### the case-insensitive sweep (titles and labels the case-sensitive pattern does not read) and the χ side:')
    for r in rows:
        if r['id'].startswith('L') or r['id'].startswith('X'):
            L.append('  %s :%d -- %s -- was "%s" -> "%s"' % (r['id'], r['line'], r['why'], r['old'][:90], r['new'][:120]))
    conc = _conc()
    L += ['', '### PART C -- §25.8`S KERNEL CONCORDANCE, ENTRY BY ENTRY: ITS PIN AS THE CHAPTER READS IT (v1.3 = 0bc21c0, 2026-07-16), THE PIN '
          'IT RESOLVES TO AT THE PAGES AND THE TERMINAL TABLE (relay data/terminal_table.json at %s), EACH THEOREM READ BY git AT v1.3, v1.5 AND '
          'main:' % STEPZERO]
    for c in conc:
        L.append('  :%d %s (%s) -- v1.3 :%d %s ; v1.5 :%d %s ; main :%d %s ; the ζ page %s, the χ page %s ; the table: %s pin %s = %s, present at %s, '
                 'statement file %s -- RESOLVES TO v1.5 = 0e5233f%s' % (
                     c['line'], c['thm'], c['module'], c['v13'], c['ok_v13'], c['v15'], c['ok_v15'], c['v15'], c['ok_main'],
                     'names it' if c['on_zeta'] else 'no node', 'names it' if c['on_chi'] else 'no node', c['table_name'], c['table_pin'],
                     c['table_pin_sha'], c['table_present'], c['table_file'], '' if c['resolved'] else ' ### UNRESOLVED'))
    L += ['  the moved pins: %d of %d (v1.3 = 0bc21c0 -> v1.5 = 0e5233f); lines moved %d; unresolved %d' % (
        sum(1 for c in conc if c['moved']), len(conc), sum(1 for c in conc if c['v13'] != c['v15']), sum(1 for c in conc if not c['resolved'])),
        '  the table`s bare-name row `structural_exhaustiveness_proved` reads its statement in Bridge/ConservationBridge.lean (:46, a '
        'conditional theorem in namespace ConservationBridge); the concordance`s theorem is the root-namespace one in Bridge/TheBridgeComplete.lean '
        '(:249 at v1.5, no namespace) -- the pin agrees, the statement file differs; printed, no tool edited',
        '  :%d the live-layer row (2026-08-20): %s -- %s' % (K.LIVE_ROW[0], K.LIVE_ROW[1], K.LIVE_ROW[2])]
    L += ['', '### PART D -- THE STEM AT :722, PART IV`S PREAMBLE (:1305-:1311), CHAPTER 24`S TITLE AND OPENING, PRINTED, WITH THEIR CHANGES:']
    for n in [K.STEM_LINE] + K.PREAMBLE + K.CH24:
        L.append('  :%d %s' % (n, M[n - 1]))
        for r in rows:
            if r['line'] == n:
                L.append('      %s (%s) -- %s%s        old : %s%s        new : %s%s        cites: %s' % (
                    r['id'], r['clause'], r['why'], NL, r['old'], NL, r['new'], NL, r['cites']))
    L += ['', '### PART E -- THE §22.4 ITEM OF (R218)(3): the chain sentence, carried, with its history line beneath:',
          '  §22.4`s criterion (:1377): %s' % M[1376][:200],
          '  the sentence stating the link (:%d), carried unchanged: %s' % (K.S224, M[K.S224 - 1]),
          '  the history line beneath it: %s' % K.HIST[K.S224], '  cites: %s' % K.HIST_CITE[K.S224]]
    L += ['', '### PART F -- THE HISTORY LINES IN THE DATED CORRESPONDENCE (2026-08-12), FOR ROWS 27-31:']
    for n in sorted(K.HIST):
        if n != K.S224:
            L += ['  beneath :%d (%s): %s' % (n, M[n - 1][:120], K.HIST[n]), '      cites: %s' % K.HIST_CITE[n]]
    L += ['', '### PART G -- EVERY CHANGE, WITH THE CLAUSE THAT REACHES IT (%d):' % len(rows)]
    for r in rows:
        L += ['  %s :%d %s -- %s -- %s' % (r['id'], r['line'], r['kind'], r['clause'], r['why']), '      old : %s' % r['old'],
              '      new : %s' % r['new'], '      cites: %s' % r['cites']]
    L += ['', '### PART H -- THE CARRIED HITS` FRAGMENTS, EACH UNDER ITS NAMED EXCEPTION (%d):' % len(K.CARRIES)]
    L += ['  :%d "%s" -- %s -- %s' % x for x in K.CARRIES]
    L += ['  :%d "%s" -- a carry of act one -- %s' % x for x in K.PRIOR_CARRIES]
    return L, dict(at=utc(), rows=rows_out, changes=rows, hits=hits, d154=d154, c154=c154, k154=k154, u154=u154, conc=conc,
                   rows_rewritten=sum(1 for r in rows_out if r['landing'].startswith('rewritten')),
                   rows_landed=sum(1 for r in rows_out if r['landing'].startswith('landed')),
                   rows_history=sum(1 for r in rows_out if r['landing'].startswith('history')))


# ================================================================================ COMPONENT 3: THE EDITION
BM_TAG = '<!-- b608 (R218) THE v5.16 EDITION`S BACK MATTER, 2026-10-03 -->'
VERSION = ('**v5.16, 2026-10-03** — CP-8 act three under `(R218)`: the remaining chapters by the b558 work-list and by the stem, ceiling, '
           'restatement, fact and history clauses, §25.8 re-pinned, the whole document read by the scanner, beside v5.15, which stands '
           'unedited; every change is recorded in the back matter.  ')
READINGS = [
    ('R-1', 'the next version by the document’s own series is v5.16, written beside v5.15 as day1/A_Place_to_Stand_v5_16.md; its version '
            'line goes above v5.15’s'),
    ('R-2', 'the body of the H28b count is every line above the monograph’s own Correspondence heading; that section, v5.14’s and v5.15’s '
            'back matter and this act’s are back matter, counted beside'),
    ('R-3', 'the bound is the whole document under the multi-act clause, this being the plan’s final act: H28c, H42b and every bound on '
            'the body are scored on the whole body'),
    ('R-4', 'the b558 work-list’s rows are numbered by v5.13 and mapped to v5.15 by b606’s and b607’s banked maps; a row whose sentence act '
            'one already rewrote by an erratum’s replacement lands there and is verified by its words, not rewritten again'),
    ('R-5', 'the ceiling clause reads every hit of the ceiling pattern in the body; a hit carries only under a named exception -- the '
            'name-and-title exception, a dated entry under the history clause, or a quoted source (a published theorem attributed to its '
            'author, a quotation verbatim, an erratum’s replacement text) -- printed beside it; every other hit is corrected, the programme’s '
            'own argument taking “the reduction” or “the argument”, a compiled fact taking “compiled”'),
    ('R-6', 'the case-insensitive sweep: titles and labels the case-sensitive pattern does not read (“The Proof”, “*Proof.*” of RH or GRH) '
            'take the ceiling clause as the pattern’s hits do; proof labels of lemmas within the ceiling carry unread'),
    ('R-7', 'the restatement clause extends the work-list rows’ readings -- Conservation of Spectra “Lean-verified”, three “routes”, the '
            '“one counted premise”, the finite range proved -- and act one’s erratum readings (E5-05’s perpendicular crossing for '
            'completedRiemannZeta₀) and act two’s joins (J02, J06, J07, J12) to the sentences restating them'),
    ('R-8', 'the Correspondence block (added 2026-08-12) is a dated entry: by the history clause its marked sentences carry as its record '
            'and a history line goes beneath each, the README’s verbatim register also a quoted source; act one’s erratum rewrite inside the '
            'block was a ruled replacement'),
    ('R-9', 'the version-history entries (v5.5-v5.13) are dated entries: their hits carry as the dated record, without history lines'),
    ('R-10', 'the exhaustiveness sentences take the author’s reading at OPEN_TRAILS :12072: Ostrowski closes the place count, the catalogue’s '
             'exhaustiveness at ξ is the open premise h2'),
    ('R-11', '§25.8 is re-pinned by a new column, each entry’s pin as the terminal table at relay HEAD prints it (v1.5 = 0e5233f), its '
             'line at v1.5 and at v1.3 read by git, and whether a page names it (none does); the dated live-layer row carries'),
    ('R-12', 'the §22.4 item: the chain sentence carries unchanged and a history line beneath it names the direction, the converse the open '
             'direction, citing spectral_cannon for what is compiled and nothing for what is not'),
    ('R-13', 'v5.14’s and v5.15’s back matter are carried with their own-line cells re-pinned to this file; their v5.13, v5.14, ERRATA, '
             'README, sieve and page numbers stand; the era annotation’s carried-by-history row is listed again here'),
    ('R-14', 'the carries of acts one and two stand as their acts recorded them (ratified at (R217)(1) and (R218)(1)), each printed with its '
             'reason in the whole-document reading'),
]


def _where(M):
    w, out = {}, 0
    for i in range(1, len(M) + 1):
        if i == 19:
            out += 1
        out += 1
        w[i] = out
        if i in K.HIST:
            out += 2
    return w


def _repin_line(l, w):
    """### a carried back-matter line with its own-line cells mapped to this file; its v5.13, v5.14, ERRATA and other numbers kept."""
    l = re.sub(r'(\*\*[A-Z0-9-]+\*\* :)(\d+)( \(v5\.1[345] :)', lambda m: m.group(1) + str(w[int(m.group(2))]) + m.group(3), l)
    l = re.sub(r'^(- :)(\d+)( \(v5\.1[45] :)', lambda m: m.group(1) + str(w[int(m.group(2))]) + m.group(3), l)
    l = re.sub(r'(with the history line at :)(\d+)', lambda m: m.group(1) + str(w[int(m.group(2))]), l)
    l = re.sub(r'(^- |and ):(\d+) beneath :(\d+)', lambda m: '%s:%d beneath :%d' % (m.group(1), w[int(m.group(2))], w[int(m.group(3))]), l)
    l = re.sub(r'(\*\*H\d+\*\* ):(\d+) beneath :(\d+)', lambda m: '%s:%d beneath :%d' % (m.group(1), w[int(m.group(2))], w[int(m.group(3))]), l)
    l = re.sub(r'^- :(\d+), carried-by-history', lambda m: '- :%d, carried-by-history' % w[int(m.group(1))], l)
    l = re.sub(r'(here the note is :)(\d+)', lambda m: m.group(1) + str(w[int(m.group(2))]), l)
    l = re.sub(r'(the body’s one live stem \(:)(\d+)(\))', lambda m: m.group(1) + str(w[int(m.group(2))]) + m.group(3), l)
    l = re.sub(r'(The depths sentence \(:)(\d+)(, )', lambda m: m.group(1) + str(w[int(m.group(2))]) + m.group(3), l)
    l = re.sub(r'(the scanner’s one live stem at :)(\d+)', lambda m: m.group(1) + str(w[int(m.group(2))]), l)
    l = re.sub(r'(?<=[:;,] ):(\d+)(?= “)', lambda m: ':%d' % w[int(m.group(1))], l)
    return l


def _build():
    """### the edition from v5.15`s blob by line transforms (carry / rewrite / re-pin / insert); returns the lines, the map and the record."""
    M, rows, bad = K.resolve()
    if bad:
        sys.exit('### THE WORK-LIST DOES NOT RESOLVE -- NOTHING WRITTEN')
    w = _where(M)
    b6 = M.index(B606_TAG) + 1
    seg_d, repinned = [], []
    out = []
    for i, l in enumerate(M, 1):
        if i == 19:
            out.append(VERSION)
        mine = [r for r in rows if r['line'] == i]
        s = l
        for r in mine:
            s = s.replace(r['old'], r['new'])
        if mine:
            seg_d.append(dict(line=i, ids=[r['id'] for r in mine], d=len(_segs(s)) - len(_segs(l))))
        if i >= b6:
            s2 = _repin_line(s, w)
            if s2 != s:
                repinned.append(i)
            s = s2
        out.append(s)
        if w[i] != len(out):
            sys.exit('### THE MAP DRIFTED AT :%d' % i)
        if i in K.HIST:
            out += ['', K.HIST[i]]
    return M, rows, out, w, seg_d, repinned


def _corr_idx(ls):
    return next(i for i, l in enumerate(ls) if l.startswith(CORR_HEAD))


COLLISIONS = [
    ('CL1', 722, 'the stem clause (S01) and the ceiling clause (C001, C002) on one line', 'the stem clause first by the precedence order (OPEN_TRAILS :12228), then the ceiling clause, each on its own phrase'),
    ('CL2', 1150, 'the name-and-title exception and the ceiling clause (L05)', 'the name “Riemann’s Theorem”, the monograph’s own title, carries; the theorem label takes the object, the reduction'),
    ('CL3', 1305, 'act one’s U05 (the first sentence) and P01-P03 (the restatement and ceiling clauses)', 'each applies to its own sentence'),
    ('CL4', 1274, 'act one’s U04 and X02, X03 (the ceiling clause)', 'each applies to its own sentence: the label and “this proof” are corrected, U04’s sentence stands'),
    ('CL5', 1818, 'act two’s carries (its reading R-5) and the work-list row W15', 'W15 rewrites the certificate’s clause to T1-lit; the hits act two carried stay carried'),
    ('CL6', 2243, 'the history clause (the dated Correspondence of 2026-08-12) and work-list rows 27-31', 'the history clause governs first: the rows carry as the dated record with history lines beneath; act one’s E6-11 inside the same block was an erratum’s ruled replacement'),
    ('CL7', 2245, 'a quoted source (README :106 verbatim) and the history clause', 'the quotation carries; the history line beneath states the README’s own rewordings'),
    ('CL8', 533, 'the ceiling clause and the fact clause on one parenthesis (C028)', 'the ceiling clause precedes the fact clause; each takes its own word (“proved”, the chapter)'),
    ('CL9', 801, 'the fact clause and the restatement clause on one sentence (R06)', 'the fact clause precedes the restatement clause; the chapter is corrected and the claim restated'),
    ('CL10', 1603, 'act one’s E1-M-09 (its first sentence) and C068, C069 (the ceiling clause)', 'each applies to its own sentence'),
    ('CL11', 1712, 'act one’s E6-01 and E1-M-18 and C075, C076 (the ceiling clause)', 'each applies to its own sentence'),
    ('CL12', 1564, 'act one’s E5-11 (a quoted source, carried) and R12 (the restatement clause)', 'each applies to its own sentence'),
    ('CL13', 2203, 'the history clause (the dated entry v5.12) and the ceiling clause', 'the history clause governs: the entry’s hits carry as the dated record'),
]


def _bm(M, rows, w, out, repinned):
    """### this act`s back matter, appended after v5.15`s last line; every line it cites is the edition`s own."""
    W = _wl_data()
    q = lambda s: s.replace('`', '’')
    L = ['', '---', '', BM_TAG, '', '## Back matter of v5.16 -- CP-8 act three, 2026-10-03, under `(R218)`', '',
         '*This section records every change v5.16 makes to v5.15, which stands beside it unedited; each line cited is this file’s own. '
         'v5.14’s and v5.15’s back matter above are carried with their own-line cells re-pinned to this file (%d lines; reading R-13).*' % len(repinned), '',
         '### The act’s readings, each the seat’s and strikeable', '']
    L += ['- **%s** %s.' % (k, q(v)) for k, v in READINGS]

    def chg(r):
        if r['kind'] == 'stem':
            return '- **%s** :%d (v5.15 :%d) — %s — %s — was: “%s” (banned stem; correction record) — now: “%s” — cites: %s.' % (
                r['id'], w[r['line']], r['line'], q(r['clause']), q(r['why']), r['old'], r['new'], q(r['cites']))
        return '- **%s** :%d (v5.15 :%d) — %s — %s — was: “%s” — now: “%s” — cites: %s.' % (
            r['id'], w[r['line']], r['line'], q(r['clause']), q(r['why']), r['old'], r['new'], q(r['cites']))
    L += ['', '### The b558 work-list’s 31 rows (relay `data/b608_worklist_PLACE.txt`, PART A)', '']
    by_id = {r['id']: r for r in rows}
    done = set()
    for k, n13, term, n15, landing, needle in K.ROWS:
        if landing.startswith('rewritten'):
            i = landing.split(': ')[1]
            L.append('- row %d (v5.13 :%d, %s) — rewritten at :%d by %s.' % (k, n13, term, w[n15], i))
            if i not in done:
                L.append(chg(by_id[i]))
                done.add(i)
        elif landing.startswith('landed'):
            L.append('- row %d (v5.13 :%d, %s) — :%d — %s; the line holds “%s”.' % (k, n13, term, w[n15], landing, needle))
        else:
            L.append('- row %d (v5.13 :%d, %s) — :%d — carried by the history clause, the dated Correspondence of 2026-08-12; its history '
                     'line beneath (reading R-8).' % (k, n13, term, w[n15]))
    L += ['', '### Part IV’s preamble, chapter 24, the restatements and the χ side (PART D)', '']
    L += [chg(r) for r in rows if r['id'][0] in 'PTRX' and r['kind'] != 'row']
    L += ['', '### The stem and the ceiling corrections (PART B; the case-insensitive sweep, reading R-6)', '']
    L += [chg(r) for r in rows if r['id'][0] in 'SCL']
    L += ['', '### The carried ceiling hits, each under its named exception (PART B, PART H)', '']
    for h in W.get('hits') or []:
        if h['fate'] == 'carried':
            L.append('- :%d (v5.15 :%d) “%s” — carried — %s.' % (w[h['line']], h['line'], h['hit'], q(h['why'])))
    L += ['', '### §25.8: the Kernel Concordance re-pinned entry by entry (PART C)', '']
    L += [chg(r) for r in rows if r['kind'] == 'repin']
    for c in W.get('conc') or []:
        L.append('- :%d (v5.15 :%d) `%s` — the pin moved from v1.3 = 0bc21c0 to v1.5 = 0e5233f (the terminal table’s), %s — no page names it.' % (
            w[c['line']], c['line'], c['thm'], 'its line :%d -> :%d' % (c['v13'], c['v15']) if c['v13'] != c['v15'] else 'its line :%d unmoved' % c['v15']))
    L += ['- The table’s bare-name row `structural_exhaustiveness_proved` reads its statement in Bridge/ConservationBridge.lean (a conditional '
          'theorem in namespace ConservationBridge); the concordance’s is the root-namespace theorem of Bridge/TheBridgeComplete.lean — same pin, '
          'printed, no tool edited.',
          '- :%d (v5.15 :%d) the live-layer row (2026-08-20) — carried as a dated entry: SIDE-global-section v0.1.0 = 706a81b resolves; the table '
          'reads that repository at HEAD 3528bcf unpinned.' % (w[K.LIVE_ROW[0]], K.LIVE_ROW[0])]
    L += ['', '### The §22.4 item (PART E, `(R218)`(3))', '',
          '- **H1** :%d beneath :%d (v5.15 :%d) — the chain sentence carried unchanged, its direction named and the converse marked open — cites: %s.' % (
              w[K.S224] + 2, w[K.S224], K.S224, q(K.HIST_CITE[K.S224]))]
    L += ['', '### History lines', '']
    for n in sorted(K.HIST):
        L.append('- :%d beneath :%d (v5.15 :%d) — %s.' % (w[n] + 2, w[n], n, 'the §22.4 item' if n == K.S224 else
                                                          'the dated Correspondence’s, for work-list rows %s' % {2243: '27', 2245: '28', 2259: '29-31'}[n]))
    L += ['', '### Collisions resolved by the precedence order (OPEN_TRAILS :12228) and the act’s readings', '']
    for cid, line, who, how in COLLISIONS:
        L.append('- **%s** :%d (v5.15 :%d) — %s — %s.' % (cid, w[line], line, q(who), q(how)))
    L += ['', '### Removals', '', '- None: no sentence of v5.15 is removed.', '',
          '### Fact corrections', '',
          '- **R06** :%d (v5.15 :801) — the Lean kernel is Chapter 25, not Chapter 24 (v5.15 :1526).' % w[801],
          '- **C028** :%d (v5.15 :533) — Conservation of Spectra is Chapter 13, not Chapter 14 (v5.15 :759).' % w[533], '',
          '### Stem corrections', '',
          '- **S01** :%d (v5.15 :722) — the scanner’s one live stem, corrected by the stem clause; its two wordings above.' % w[722],
          '- :%d, carried-by-history — the era annotation of 2026-08-14 (v5.15 :2272, v5.14 :2269, v5.13 :2264), carried as v5.14 and v5.15 '
          'carried it; listed again here because the scanner reads the exceptions of a file’s last back matter.' % w[2272], '',
          '### Placement', '', '| page | node this edition names | its pin as the page prints it | status |', '|:--|:--|:--|:--|',
          '| %s | `SIDEExplicitFormula.B321.ch_iff_rh` | v0.1 = baed4df | named in v5.16, ζ page node 7 (:11) |' % PAGE,
          '| %s | `SIDEExplicitFormula.B321.h2_sign_iff_rh` | v0.2 = 5c72cad | named in v5.16, ζ page node 8 (:12) |' % PAGE,
          '| %s | `SIDEExplicitFormula.Simplicity.simplicity_iff` | v0.17 = 5a1630b | named in v5.16, ζ page node 41 (:45) |' % PAGE,
          '| %s | `SIDEExplicitFormula.Doubling.positivity_not_imp_simplicity` | v0.19 = 5fc0c87 | named in v5.16, ζ page node 52 (:56) |' % PAGE,
          '| %s | `SIDEExplicitFormula.GRHWeil.h2_sign_chi_iff_grh_chi` | v0.14 = 4dce7b9 | named in v5.16, χ page node 12 (:16) |' % DIR_PAGE,
          '', '### Correspondence', '', '| claim, as v5.16 states it | kernel | terminal | pin | status |', '|:--|:--|:--|:--|:--|',
          '| Weil positivity on classK is equivalent to RH; the reduction the monograph argues lands here | SIDE-explicit-formula | `SIDEExplicitFormula.B321.h2_sign_iff_rh` | v0.2 = 5c72cad | compiled; cited at the ceiling corrections |',
          '| Route 3’s premise is RH restated | SIDE-explicit-formula | `SIDEExplicitFormula.B321.ch_iff_rh` | v0.1 = baed4df | compiled; cited at W05, W07, W10, R01-R03 |',
          '| simplicity is the second located clause; within the schema positivity does not imply it | SIDE-explicit-formula | `SIDEExplicitFormula.Simplicity.simplicity_iff`, `SIDEExplicitFormula.Doubling.positivity_not_imp_simplicity` | v0.17 = 5a1630b, v0.19 = 5fc0c87 | compiled; cited at P02, P05, C082, C091 |',
          '| GRH for χ is equivalent to its located clause | SIDE-explicit-formula | `SIDEExplicitFormula.GRHWeil.h2_sign_chi_iff_grh_chi` | v0.14 = 4dce7b9 | compiled; cited at X01-X05 |',
          '| the conservation terminal states (1 : ℚ) ^ s = 1 | SIDE-kernel | `conservation_of_spectra` | v1.5 = 0e5233f | compiled, T2 (its reading carried by the name); cited at W01-W20, R04-R09 |',
          '| the completed-ζ derivative is imaginary on the line | SIDE-kernel | `SpectralCannonFull.spectral_cannon` | v1.5 = 0e5233f | compiled for completedRiemannZeta₀; cited at P06, R10-R12, C088 and the §22.4 history line |',
          '| finite-range Li positivity | SIDE-lv-conservation | `PartialPositivity.partialPositivity_finiteRange` | v0.8.0 = 6efa9e5 | T1-lit (two literature premises, verified zeros); cited at W15, R13 |',
          '', '### The whole document, read (the multi-act clause, the plan’s final act)', '',
          '- {WHOLE}', '', '### Version history', '',
          '- v5.16, 2026-10-03 — CP-8 act three under `(R218)`: the b558 work-list’s 31 rows landed (%d rewritten, %d landed at act one and '
          'verified, %d by history lines in the dated Correspondence); %d changes in all -- %d ceiling, %d restatement, %d title, %d stem, %d '
          '§25.8 pin-column lines; four history lines; the §22.4 item carried with its history line; v5.15 unedited beside it.' % (
              W.get('rows_rewritten', 0), W.get('rows_landed', 0), W.get('rows_history', 0), len(rows),
              sum(1 for r in rows if r['kind'] == 'ceiling'), sum(1 for r in rows if r['kind'] == 'restatement'),
              sum(1 for r in rows if r['kind'] == 'title'), sum(1 for r in rows if r['kind'] == 'stem'), sum(1 for r in rows if r['kind'] == 'repin'))]
    return L


def _classify(ed, E):
    """### every ceiling hit of the edition: body hits by fate (corrected hits are gone; carried under a named exception, a carry of an
    ### earlier act, or UNEXCEPTED), the history and version lines, and the back matter`s records (the Correspondence onward)."""
    w = {int(k): v for k, v in E['where'].items()}
    inv = {v: k for k, v in w.items()}
    ci = E['corr']
    hist = set(E['hist'].values()) | {E['version']}
    a2 = _a2_carries()
    out = []
    for i, l in enumerate(ed, 1):
        src = inv.get(i)
        for h in CEILING.finditer(l):
            p = h.start()
            if i >= ci:
                kind = 'record'
            elif i in hist:
                kind = 'history'
            else:
                kind = 'UNEXCEPTED'
                for m, frag, exc, why in K.CARRIES:
                    if m == src and frag in l and l.index(frag) <= p < l.index(frag) + len(frag):
                        kind = 'carried: %s' % exc
                for m, frag, why in K.PRIOR_CARRIES:
                    if m == src and frag in l and l.index(frag) <= p < l.index(frag) + len(frag):
                        kind = 'carried: act one`s'
                if kind == 'UNEXCEPTED':
                    acc = 0
                    for s in _segs(l):
                        k = l.find(s, acc)
                        if k <= p < k + len(s) and any(m == src and frag in s for m, frag, _w in a2):
                            kind = 'carried: act two`s, ratified'
                        acc = k + len(s) if k >= 0 else acc
            out.append(dict(line=i, src=src, hit=h.group(0), kind=kind))
    return out


def edition(*a):
    """### PLACE-papers day1/A_Place_to_Stand_v5_16.md beside v5.15 (unedited), from v5.15`s blob at 0800a6a and the work-list; the
    ### re-pin step last (`repin`). Writes the edition and data/b608_edition.json; `dry` writes both to the scratchpad instead."""
    dry = 'dry' in a
    if not dry and not os.path.exists(os.path.join(D, 'b608_worklist_PLACE.txt')):
        sys.exit('### THE WORK-LIST IS NOT BANKED -- NOTHING WRITTEN')
    M, rows, out, w, seg_d, repinned = _build()
    E = dict(where={str(k): v for k, v in w.items()}, version=19, hist={str(k): w[k] + 2 for k in K.HIST}, corr=_corr_idx(out) + 1)
    bm = _bm(M, rows, w, out, repinned)
    out2 = out + bm
    hits = _classify(out2, E)
    carried = [h for h in hits if h['kind'].startswith('carried')]
    unexc = [h for h in hits if h['kind'] == 'UNEXCEPTED']
    i_whole = out2.index('- {WHOLE}')
    out2[i_whole] = ('- The body’s ceiling hits after this act: %d, each carried under a named exception or as an earlier act’s carry '
                     '(%d under this act’s exceptions, %d of act two’s, %d of act one’s), unexcepted %d; the scanner’s live stems %s. The '
                     'plan’s bound is met when both read zero unexcepted.' % (
                         len(carried), sum(1 for h in carried if h['kind'] in ('carried: %s' % K.QS, 'carried: %s' % K.NT, 'carried: %s' % K.DE)),
                         sum(1 for h in carried if 'act two' in h['kind']), sum(1 for h in carried if 'act one' in h['kind']), len(unexc),
                         '{LIVE}'))
    text = NL.join(out2) + NL
    E.update(bm=out2.index(BM_TAG) + 1)
    # ### the scanner on the text as it would land; its live count goes into the whole-document line
    tmp = os.path.join(SP, 'b608_edition_scan_tmp.md')
    open(tmp + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(tmp + '.tmp', tmp)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', tmp], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    m = re.search(r'live uses\s*:\s*(\d+)', r.stdout or '')
    live = int(m.group(1)) if m else None
    out2[i_whole] = out2[i_whole].replace('{LIVE}', str(live))
    text = NL.join(out2) + NL
    b = text.encode('utf-8')
    ci, cm = _corr_idx(out2), _corr_idx(M)
    E.update(at=utc(), lines=len(out2), sha256=sha(b), changes=rows, seg_d=seg_d, repinned=repinned, carried=len(carried), unexcepted=len(unexc),
             live_pre=live, n_body=_count(out2[:ci]), n_cur_body=_count(M[:cm]), n_backmatter=_count(out2[ci:]), n_cur_backmatter=_count(M[cm:]),
             n_full=_count(out2), credit=0, removals=0, history_lines=sum(1 for n in K.HIST if n < K.CORR_LINE), version_lines=1,
             cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip())
    if dry:
        p = os.path.join(SP, 'b608_edition_dry.md')
        open(p + '.tmp', 'wb').write(b)
        os.replace(p + '.tmp', p)
        json.dump(E, io.open(os.path.join(SP, 'b608_edition_dry.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('  DRY: %s ; %d lines ; body %d (v5.15 %d, %+d) ; back matter %d ; changes %d ; re-pinned %d ; carried %d ; unexcepted %d ; live %s' % (
            p, len(out2), E['n_body'], E['n_cur_body'], E['n_body'] - E['n_cur_body'], E['n_backmatter'], len(rows), len(repinned),
            len(carried), len(unexc), live))
        return
    dest = os.path.join(PP, *ED.split('/'))
    if os.path.exists(dest):
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    put_json('b608_edition.json', E)
    print('  %s ; %d lines ; sha256 %s ; body %d (v5.15 %d, %+d) ; back matter %d ; carried %d ; unexcepted %d ; live %s' % (
        ED, len(out2), E['sha256'][:16], E['n_body'], E['n_cur_body'], E['n_body'] - E['n_cur_body'], E['n_backmatter'], len(carried),
        len(unexc), live))


def termscan():
    """### the scanner (banned_terms.py --new) on the edition file, banked as data/b608_edition_termscan.txt."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', os.path.join(PP, *ED.split('/'))],
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b608_edition_termscan.txt', (r.stdout or '').rstrip(NL).split(NL))
    print([l for l in r.stdout.split(NL) if 'live uses' in l or 'VERDICT' in l or 'LIVE USE' in l])


def _ed():
    t = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read().replace(chr(13), '')
    return K.lines_of(t)


def _recorded(bm, c):
    """### a change is recorded when one back-matter line holds both its wordings (the stem row carries a marker between them)."""
    return any(('was: “%s”' % c['old']) in x and ('now: “%s”' % c['new']) in x for x in bm.split(NL))


def carried(E, ed, M):
    """### every non-blank v5.15 line: carried verbatim at its mapped line, rewritten with every change recorded in the back matter,
    ### or (the back matter) re-pinned by the map."""
    bm = NL.join(ed[E['bm'] - 1:])
    w = {int(k): v for k, v in E['where'].items()}
    byl = {}
    for c in E['changes']:
        byl.setdefault(c['line'], []).append(c)
    rp = set(E['repinned'])
    ok, bad = 0, []
    for n in range(1, len(M) + 1):
        if not M[n - 1].strip():
            continue
        x = w.get(n)
        if not x:
            bad.append(n)
            continue
        if n in byl:
            s = M[n - 1]
            for c in byl[n]:
                s = s.replace(c['old'], c['new'])
            good = ed[x - 1] == s and all(_recorded(bm, c) for c in byl[n])
        elif n in rp:
            good = ed[x - 1] == _repin_line(M[n - 1], w) and ed[x - 1] != M[n - 1]
        else:
            good = ed[x - 1] == M[n - 1]
        ok += good
        if not good:
            bad.append(n)
    return ok, bad


def edition_bank():
    """### The diff with its offset line, every change, the collisions, the counts, the ceiling read by kind, the scanner on the whole,
    ### H28a-H28c on the whole document (the plan`s final act) and H42a-H42d."""
    E = jl('b608_edition.json')
    W = jl('b608_worklist.json')
    ed = _ed()
    M = K.lines_of(_show(PP, PRE_PP, CUR))
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### THE EDITION ON DISK IS NOT THE BANKED ONE -- NOTHING WRITTEN')
    w = {int(k): v for k, v in E['where'].items()}
    scan = rd('b608_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    all_live = [int(m.group(1)) for m in re.finditer(r':(\d+)\s+### LIVE USE', scan)]
    ok, bad = carried(E, ed, M)
    hits = _classify(ed, E)
    kinds = {k: sum(1 for h in hits if h['kind'] == k) for k in sorted(set(h['kind'] for h in hits))}
    unexc = [h for h in hits if h['kind'] == 'UNEXCEPTED']
    car = [h for h in hits if h['kind'].startswith('carried')]
    bm = NL.join(ed[E['bm'] - 1:])
    h28a_rows = [dict(id=c['id'], line=w[c['line']], cites=c['cites'], recorded=_recorded(bm, c)) for c in E['changes']]
    h28a = 'HOLDS' if all(x['recorded'] and x['cites'] for x in h28a_rows) else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur_body']
    rw = sum(abs(x['d']) for x in E['seg_d'] if x['line'] < _corr_idx(M) + 1)
    allowed = E['credit'] + E['removals'] + E['history_lines'] + E['version_lines'] + rw
    strict = E['credit'] + E['removals'] + E['history_lines'] + E['version_lines']
    h28b = 'HOLDS' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if (clean and not unexc) else 'REFUTED'
    # ### H42a: every row lands -- a rewritten row`s new wording on its line, a landed row`s needle on its line, a history row`s line beneath
    rows = W.get('rows') or []
    land = []
    for r in rows:
        x = w[r['v15']]
        if r['landing'].startswith('rewritten'):
            c = next(c for c in E['changes'] if c['id'] == r['landing'].split(': ')[1])
            good = ed[x - 1].count(c['new']) == 1
        elif r['landing'].startswith('landed'):
            good = r['needle'] in ed[x - 1]
        else:
            hl = {2243: 2243, 2245: 2245, 2251: 2259, 2258: 2259}[r['v15']]
            good = ed[w[hl] + 1] == K.HIST[hl] and ed[x - 1] == M[r['v15'] - 1]
        land.append(dict(row=r['row'], line=x, landing=r['landing'], ok=good))
    h42a = 'HOLDS' if len(land) == 31 and all(x['ok'] for x in land) else 'REFUTED'
    h42b = 'HOLDS' if (clean and not unexc and all(h['kind'] != 'UNEXCEPTED' for h in hits)) else 'REFUTED'
    conc = W.get('conc') or []
    kc = [c for c in E['changes'] if c['kind'] == 'repin' and c['id'] not in ('K00', 'K01')]
    conc_in_ed = all(('%s, :%d (from %s, :%d)' % (K.NEW_PIN, c['v15'], K.OLD_PIN, c['v13'])) in ed[w[c['line']] - 1] for c in conc)
    h42c = 'HOLDS' if len(conc) == 7 and all(c['resolved'] for c in conc) and conc_in_ed and len(kc) == 7 \
        and all(('the pin moved from v1.3 = 0bc21c0 to v1.5 = 0e5233f') in bm and ('`%s`' % c['thm']) in bm for c in conc) else 'REFUTED'
    s = K.S224
    hl = ed[w[s] + 1]
    h42d = 'HOLDS' if (ed[w[s] - 1] == M[s - 1] and ed[w[s]] == '' and hl == K.HIST[s] and not CEILING.search(hl)
                       and 'spectral_cannon' in hl and 'no compiled statement carries it' in hl) else 'REFUTED'
    offs, last = [], None
    for n in range(1, len(M) + 1):
        o = w[n] - n
        if o != last:
            offs.append((n, o))
            last = o
    L = ['### OFFSET FROM v5.15 (R190)(3): %s -- the offset changes at each v5.15 line printed (v5.15 line, offset); every v5.15 line`s '
         'v5.16 line is printed below (the map), and every edition line cited here is the final file`s own.' % ', '.join('%+d from :%d' % (o, n) for n, o in offs), '',
         'b608 -- COMPONENT 3: THE MONOGRAPH`S NEXT VERSION, v5.16, (R218)(4), BY THE FORM OF (R187)(5), ITS CLAUSES, THE PRECEDENCE ORDER AND '
         'THE MULTI-ACT CLAUSE, THE WHOLE DOCUMENT AS THE BOUND', '',
         '### v5.15 : PLACE-papers %s @ %s (blob %s), %d lines, its head "%s"' % (CUR, PRE_PP, E['cur_blob'][:8], len(M), M[0]),
         '### v5.16 : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines'], E['sha256']), '',
         '### THE VERSION LINE, PRINTED: :%d %s' % (E['version'], ed[E['version'] - 1]), '',
         '### EVERY REWRITTEN SENTENCE (%d), WITH THE WORK-LIST LINE IT ANSWERS AND WHAT IT CITES:' % len(E['changes'])]
    for c in E['changes']:
        seg = next((x for x in _segs(M[c['line'] - 1]) if c['old'] in x), c['old'])
        L += ['  %s  v5.15 :%d -> v5.16 :%d -- %s -- %s -- %s' % (c['id'], c['line'], w[c['line']], c['kind'], c['clause'], c['why']),
              '      was : %s' % seg, '      now : %s' % seg.replace(c['old'], c['new']), '      cites: %s' % c['cites']]
    L += ['', '### THE HISTORY LINES (the history clause):']
    L += ['  :%s beneath v5.15 :%s (v5.16 :%d) : %s -- cites %s' % (v, k, w[int(k)], ed[v - 1][:240], K.HIST_CITE[int(k)]) for k, v in E['hist'].items()]
    L += ['', '### THE 31 ROWS, LANDED:']
    L += ['  row %d -> :%d -- %s -- %s' % (x['row'], x['line'], x['landing'], 'LANDS' if x['ok'] else '### HELD') for x in land]
    L += ['', '### §25.8 RE-PINNED ENTRY BY ENTRY:']
    L += ['  v5.15 :%d -> v5.16 :%d %s -- %s -> %s, :%d -> :%d ; the table %s = %s ; %s' % (
        c['line'], w[c['line']], c['thm'], K.OLD_PIN, K.NEW_PIN, c['v13'], c['v15'], c['table_pin'], c['table_pin_sha'],
        'RESOLVED' if c['resolved'] else '### UNRESOLVED') for c in conc]
    L += ['', '### CARRIED HITS, EACH WITH ITS EXCEPTION, AND THE COLLISIONS:']
    L += ['  v5.16 :%d (v5.15 :%s) "%s" -- %s' % (h['line'], h['src'], h['hit'], h['kind']) for h in car]
    L += ['  %s v5.15 :%d -- %s -- %s' % c for c in COLLISIONS]
    L += ['', '### SEGMENT CHANGES ON REWRITTEN LINES (b558 segments): %s' % ([(x['line'], x['ids'], x['d']) for x in E['seg_d'] if x['d']] or 'none'),
          '### v5.15`S BACK MATTER RE-PINNED: %d lines (reading R-13): %s' % (len(E['repinned']), E['repinned']), '',
          '### EVERY NON-BLANK v5.15 LINE -> ITS v5.16 LINE (%d carried verbatim, rewritten with every change recorded, or re-pinned ; '
          'failing %s):' % (ok, bad or 'none')]
    L += ['  :%s -> :%d' % (n, x) for n, x in sorted(w.items())]
    L += ['', '### THE COUNTS (relay tools/b558_record.py `segments`, imported): v5.15`s BODY %d ; v5.16`s BODY %d (%+d) ; the BACK MATTER %d '
          '(the Correspondence onward: v5.14`s, v5.15`s and this act`s), printed separately ; the edition whole %d' % (
              E['n_cur_body'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + the history line the ruling`s reading takes %d + '
          'one version line %d + rewritten lines` segment changes %d = %d ; the strict count %d' % (
              body_dn, E['credit'], E['removals'], E['history_lines'], E['version_lines'], rw, allowed, strict), '',
          '### THE CEILING, every hit in the edition, by kind: %s' % kinds]
    L += ['    :%d (v5.15 :%s) "%s" -- %s' % (h['line'], h['src'], h['hit'], h['kind']) for h in hits]
    L += ['### THE SCANNER (banned_terms.py --new) on the whole edition: live uses %s at %s, verdict %s' % (
        live.group(1) if live else None, all_live, 'CLEAN' if clean else 'NOT CLEAN'),
        '### THE WHOLE-DOCUMENT FIGURE: %d ceiling hits in the body, every one carried under a named exception or as an earlier act`s carry, '
        'unexcepted %d; %s live stem(s) -- b607 handed 154 and 1' % (len(car), len(unexc), len(all_live)), '',
        '### H28a: rewritten sentences %d ; each recorded with both wordings %d ; each citing a declaration, a page line, a sieve row or a '
        'bank line %d' % (len(h28a_rows), sum(x['recorded'] for x in h28a_rows), sum(1 for x in h28a_rows if x['cites'])),
        '### the 154: corrected %s ; carried %s ; unread %s' % (W.get('c154'), W.get('k154'), W.get('u154')), '',
        '### ### **H28a %s -- every MOVED-IN-MEANING sentence (%d) recorded with both wordings and citing what it rests on.**' % (h28a, len(h28a_rows)),
        '### ### **H28b %s -- the body differs by %+d sentences against at most %d (strict %d); the back matter %d, excluded and printed.**' % (
            h28b, body_dn, allowed, strict, E['n_backmatter']),
        '### ### **H28c %s ON THE WHOLE DOCUMENT (the plan`s final act) -- the scanner %s, %d live; ceiling hits unexcepted %d.**' % (
            h28c, 'CLEAN' if clean else 'NOT CLEAN', len(all_live), len(unexc)),
        '### ### **H42a %s -- the 31 rows: %d land (rewritten %d, landed at act one %d, history lines %d), none held.**' % (
            h42a, sum(1 for x in land if x['ok']), W.get('rows_rewritten'), W.get('rows_landed'), W.get('rows_history')),
        '### ### **H42b %s -- the whole-document scanner reads %d live stems and %d unexcepted ceiling hits; %d carried hits, each printed with '
        'its exception.**' % (h42b, len(all_live), len(unexc), len(car)),
        '### ### **H42c %s -- §25.8: %d entries re-pinned, %d pins moved, each printed; unresolved %d.**' % (
            h42c, len(conc), sum(1 for c in conc if c['moved']), sum(1 for c in conc if not c['resolved'])),
        '### ### **H42d %s -- the §22.4 sentence carried unchanged at :%d, its history line beneath at :%d, no ceiling hit, citing spectral_cannon '
        'for what is compiled.**' % (h42d, w[s], w[s] + 2),
        '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' if h42a == 'HOLDS' else '### ### **HELD AT A SENTENCE: see the rows above.**']
    put_txt('b608_edition_PLACE.txt', L)
    put_json('b608_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, H42a=h42a, H42b=h42b, H42c=h42c, H42d=h42d, h28a_rows=h28a_rows,
                                   body_dn=body_dn, allowed=allowed, strict=strict, rw=rw, backmatter=E['n_backmatter'],
                                   live=int(live.group(1)) if live else None, all_live=all_live, clean=clean, unexcepted=len(unexc),
                                   carried_hits=len(car), kinds=kinds, hits=hits, carried_ok=ok, carried_bad=bad, land=land,
                                   c154=W.get('c154'), k154=W.get('k154'), u154=W.get('u154'),
                                   conc_moved=sum(1 for c in conc if c['moved']), conc_unresolved=sum(1 for c in conc if not c['resolved'])))
    print('H28a %s H28b %s H28c %s H42a %s H42b %s H42c %s H42d %s ; carried %d bad %s ; body_dn %d allowed %d strict %d ; live %s ; '
          'unexcepted %d ; carried hits %d' % (h28a, h28b, h28c, h42a, h42b, h42c, h42d, ok, bad, body_dn, allowed, strict,
                                               live.group(1) if live else None, len(unexc), len(car)))


def repin():
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932). Writes data/b608_repin.txt."""
    E = jl('b608_edition.json')
    ed = _ed()
    M = K.lines_of(_show(PP, PRE_PP, CUR))
    w = {int(k): v for k, v in E['where'].items()}
    inv = {v: k for k, v in w.items()}
    bml = ed[E['bm'] - 1:]
    bm = NL.join(bml)
    checks = []
    for m in re.finditer(r'^- \*\*([A-Z0-9-]+)\*\* :(\d+) \(v5\.15 :(\d+)\)', bm, re.M):
        i, a_, b_ = m.group(1), int(m.group(2)), int(m.group(3))
        checks.append(('back matter %s cites :%d for v5.15 :%d' % (i, a_, b_), w.get(b_) == a_ and bool(ed[a_ - 1].strip())))
    for m in re.finditer(r'^- :(\d+) \(v5\.15 :(\d+)\) “([^”]+)”', bm, re.M):
        a_, b_, hit = int(m.group(1)), int(m.group(2)), m.group(3)
        checks.append(('the carried hit :%d “%s” for v5.15 :%d' % (a_, hit, b_), w.get(b_) == a_ and hit in ed[a_ - 1]))
    for m in re.finditer(r'^- row (\d+) \(v5\.13 :(\d+), [^)]+\) — :(\d+) — ', bm, re.M):
        k, a_ = int(m.group(1)), int(m.group(3))
        r = next(x for x in K.ROWS if x[0] == k)
        checks.append(('row %d at :%d' % (k, a_), w.get(r[3]) == a_))
    for c in E['changes']:
        a_ = w[c['line']]
        checks.append(('%s`s new wording on :%d' % (c['id'], a_), ed[a_ - 1].count(c['new']) == 1))
    for k, v in E['hist'].items():
        checks.append(('history line :%d beneath :%s' % (v, k), ed[v - 1] == K.HIST[int(k)] and ed[v - 2] == '' and w[int(k)] == v - 2))
    for cid, line, _w, _h in COLLISIONS:
        checks.append(('collision %s at :%d' % (cid, w[line]), ('**%s** :%d (v5.15 :%d)' % (cid, w[line], line)) in bm))
    b6 = M.index(B606_TAG) + 1
    for n in E['repinned']:
        checks.append(('v5.15`s back matter :%d re-pinned at :%d' % (n, w[n]), n >= b6 and ed[w[n] - 1] == _repin_line(M[n - 1], w)))
    # ### every own-line cell of the carried back matter (v5.14`s and v5.15`s) now cites a line of this file that holds what it names
    for n in range(b6, len(M) + 1):
        for m in re.finditer(r'\*\*[A-Z0-9-]+\*\* :(\d+) \(v5\.1[345] :(\d+)\)', ed[w[n] - 1]):
            a_ = int(m.group(1))
            checks.append(('carried row at :%d cites :%d' % (w[n], a_), bool(inv.get(a_)) and bool(ed[a_ - 1].strip())))
        for m in re.finditer(r'^- :(\d+) \(v5\.14 :(\d+)\) “([^”]+)”', ed[w[n] - 1]):
            a_, hit = int(m.group(1)), m.group(3)
            checks.append(('carried hit row at :%d cites :%d “%s”' % (w[n], a_, hit), hit in ed[a_ - 1]))
    checks.append(('the version line on :%d above v5.15`s' % E['version'], ed[E['version'] - 1] == VERSION and ed[E['version']] == M[18]
                   and M[18].startswith('**v5.15, 2026-10-03**') and ed[E['version'] + 1].startswith('**v5.14, 2026-10-03**')))
    checks.append(('the Correspondence heading on :%d' % E['corr'], ed[E['corr'] - 1].startswith(CORR_HEAD)))
    checks.append(('the back-matter tag on :%d' % E['bm'], ed[E['bm'] - 1] == BM_TAG))
    checks.append(('act one`s tag carried on :%d' % w[b6], ed[w[b6] - 1] == B606_TAG))
    b7 = M.index(B607_TAG) + 1
    checks.append(('act two`s tag carried on :%d' % w[b7], ed[w[b7] - 1] == B607_TAG))
    bank = rd('b608_edition_PLACE.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM v5.15') and bank.count('### OFFSET FROM') == 1))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and hashlib.sha256(open(os.path.join(PP, *ED.split('/')), 'rb').read()).hexdigest() == E['sha256']))
    for m in re.finditer(r'v5\.15 :(\d+) -> v5\.16 :(\d+)', bank):
        b_, a_ = int(m.group(1)), int(m.group(2))
        checks.append(('the diff bank`s v5.15 :%d -> v5.16 :%d' % (b_, a_), w.get(b_) == a_))
    L = ['### b608 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % ED, '']
    L += ['    %-100s %s' % (x[:100], 'OK' if ok else '### FAILS') for x, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _x, ok in checks), len(checks))]
    put_txt('b608_repin.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 4: THE PAGES
def page(k):
    """### after the edition commit: ONE page per call in the foreground, re-emitted from its banked probe (the ζ page from b602's list
    ### at v0.20, the χ page from b603's at v0.21; no Lean call). Writes the page only when it changed, and data/b608_page_<k>.json."""
    import chain_page as C
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b608_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, C.HOLD_MB))
    if 0 <= fm < C.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    src_out = os.path.join(D, PROBE[k])
    rc, pg, meta, log = C.build(os.path.join(D, NODES[k]), pdir, src_out)
    secs = int(time.time() - t0)
    for l in log:
        print('  %s: %s' % (k, l))
    if rc:
        put_json('b608_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
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
    put_json('b608_page_%s.json' % k, J)
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s ; the probe read %s' % (k, rc, len(b), changed, secs, src_out))
    for x in dl[:60]:
        print('    ' + x[:240])


def page_arms(tag):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b608 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    L.append('### the lists read: %s' % {k: (NODES[k], PROBE[k]) for k in NODES})
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b608_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b608_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
SCORE_KEYS = ('H28a', 'H28b', 'H28c', 'H42a', 'H42b', 'H42c', 'H42d', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def scores():
    WJ, H, E = jl('b608_worklist.json'), jl('b608_h28.json'), jl('b608_edition.json')
    Z, X = jl('b608_page_zeta.json'), jl('b608_page_chi.json')
    rp = rd('b608_repin.txt')
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
                                                                               'SIDE-structural-error-correction', 'SIDE-cosmo', 'SIDE-silence-principle',
                                                                               'SIDE-global-section')}
    kern_ok = kern == {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068',
                       'SIDE-structural-error-correction': '6a4f482', 'SIDE-cosmo': 'c5cba30', 'SIDE-silence-principle': '667c254',
                       'SIDE-global-section': '3528bcf'}
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1').split(NL) if x.startswith('?? ')))
    trail_landed = os.path.exists(os.path.join(D, 'b608_trail.json'))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', ED] + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = all(g(PP, 'rev-parse', 'HEAD:' + p).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, p)).strip()
                   and not g(PP, 'status', '--porcelain', '--', p).strip() for p in (CUR, PREV, ORIG))
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b608_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b607_closing_push_out.txt'))
    m = re.search(r'RE-PIN : (\d+) of (\d+)', rp)
    arms2 = rd('b608_page_arms_c2.txt')
    ed = _ed() if os.path.exists(os.path.join(PP, *ED.split('/'))) else []
    bmt = NL.join(ed[E['bm'] - 1:]) if ed and E else ''
    car = [h for h in (H.get('hits') or []) if h['kind'].startswith('carried')]
    unlisted = [h for h in car if (':%d (v5.15 :%s) “%s” — carried' % (h['line'], h['src'], h['hit'])) not in bmt]
    S = dict(
        H28a=(H.get('H28a'), 'every MOVED-IN-MEANING sentence (%d) recorded with both wordings and citing what it rests on: %d' % (
            len(H.get('h28a_rows') or []), sum(1 for x in H.get('h28a_rows') or [] if x['recorded'] and x['cites']))),
        H28b=(H.get('H28b'), 'the body differs by %+d against at most %d (strict %d)' % (H.get('body_dn', 0), H.get('allowed', 0), H.get('strict', 0))),
        H28c=(H.get('H28c'), 'ON THE WHOLE DOCUMENT, the plan`s final act: the scanner %s, %s live; unexcepted ceiling hits %s' % (
            'CLEAN' if H.get('clean') else 'NOT CLEAN', H.get('live'), H.get('unexcepted'))),
        H42a=(H.get('H42a'), 'rows %d ; landing %d ; held %d' % (len(H.get('land') or []), sum(1 for x in H.get('land') or [] if x['ok']),
                                                                  sum(1 for x in H.get('land') or [] if not x['ok']))),
        H42b=(H.get('H42b'), 'the scanner`s live stems %s ; unexcepted ceiling hits %s ; carried %s, each printed with its exception' % (
            H.get('live'), H.get('unexcepted'), H.get('carried_hits'))),
        H42c=(H.get('H42c'), '§25.8 entries %d ; pins moved %s ; unresolved %s' % (len(WJ.get('conc') or []), H.get('conc_moved'), H.get('conc_unresolved'))),
        H42d=(H.get('H42d'), 'the §22.4 sentence carried with its history line beneath, no ceiling hit, spectral_cannon cited'),
        N1=('HELD' if H.get('H42a') == 'HOLDS' else 'REFUTED', 'the 31 rows: %d land, none held' % sum(1 for x in H.get('land') or [] if x['ok'])),
        N2=('HELD' if (H.get('c154') or 0) >= 100 and H.get('u154') == 0 and not unlisted else 'REFUTED',
            'of the 154: corrected %s (bound 100), carried %s, unread %s ; carried hits without a printed exception %s' % (
                H.get('c154'), H.get('k154'), H.get('u154'), [(h['line'], h['hit']) for h in unlisted] or 'none')),
        N3=('HELD' if (H.get('conc_moved') or 0) >= 5 and H.get('conc_unresolved') == 0 else 'REFUTED',
            '§25.8: pins moved %s (bound 5), unresolved %s' % (H.get('conc_moved'), H.get('conc_unresolved'))),
        N4=('HELD' if all(H.get(k) == 'HOLDS' for k in ('H28a', 'H28b', 'H28c')) and H.get('unexcepted') == 0 and H.get('clean') else 'REFUTED',
            'H28a %s, H28b %s, H28c %s on the whole document ; the scanner %s ; unexcepted %s' % (
                H.get('H28a'), H.get('H28b'), H.get('H28c'), 'CLEAN' if H.get('clean') else 'NOT CLEAN', H.get('unexcepted'))),
        N5=('HELD' if kern_ok and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
            'nothing deposits; every kernel`s main unmoved %s; v5.15, v5.14 and v5.13 unedited %s; PLACE-papers %s (wanted %s); relay files '
            'beyond the act`s banks, tools and the table %s%s' % (kern_ok, cur_same, pp_ch, want_pp, relay_beyond, '' if trail_landed else ' ; the trail record pending')),
        S1=('HELD' if m and m.group(1) == m.group(2) else 'REFUTED', 'the re-pin step: %s' % (m.group(0) if m else 'no bank')),
        S2=('HELD' if not H.get('carried_bad') else 'REFUTED', 'every non-blank v5.15 line carried verbatim, rewritten with every change '
                                                              'recorded, or re-pinned: %d ; failing %s' % (H.get('carried_ok', 0), H.get('carried_bad'))),
        S3=('HELD' if H.get('unexcepted') == 0 and not unlisted else 'REFUTED', 'the body`s hits unexcepted %s ; carried hits missing from the '
            'back matter %s' % (H.get('unexcepted'), [(h['line'], h['hit']) for h in unlisted] or 'none')),
        S4=('HELD' if Z.get('changed') is True and X.get('changed') is True else 'REFUTED', 'the ζ page changed %s ; the χ page changed %s' % (
            Z.get('changed'), X.get('changed'))),
        S5=('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
            'after the page commits: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    )
    put_json('b608_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-6s %s -- %s' % (k, S[k][0], str(S[k][1])[:220]))


def _title():
    H = jl('b608_h28.json')
    return ('## CP-8, act three: the monograph’s v5.16 over the remaining chapters by the b558 work-list, §25.8 re-pinned at the terminal '
            'table’s pins (no entry a page node), the whole document read by the scanner with %s carried hits under named exceptions' % H.get('carried_hits'))


TRAIL_HEAD = ('### b608 — lane three, act thirty-five under (R218): CP-8 act three -- the monograph’s remaining chapters by the b558 work-list '
              'and the clauses, §25.8 re-pinned, the whole document as the bound')


def _finding_text():
    S, WJ, H, E = jl('b608_scores.json'), jl('b608_worklist.json'), jl('b608_h28.json'), jl('b608_edition.json')
    rl = jl('b608_record_lines.json')
    w1, w2, v1, d1 = [x['line'] for x in rl['lines']]
    ec = _pp_commit('b608 (R218)(4): ' + ED)
    zc, xc = _pp_commit('b608 (R218)(4): ' + PAGE), _pp_commit('b608 (R218)(4): ' + DIR_PAGE)
    rows = E['changes']
    t = _title()
    e = ['', t, '',
         '*Filed at b608 on the author’s ruling `(R218)`. Banks: relay `data/b608_reads.txt`, `data/b608_worklist_PLACE.txt`, '
         '`data/b608_edition_PLACE.txt`, `data/b608_edition_termscan.txt`, `data/b608_repin.txt`, `data/b608_page_zeta.json`, '
         '`data/b608_page_chi.json`, `data/b608_page_arms_c2.txt`. Nothing deposits.*', '',
         '**The edition** (`(R218)`(4)). PLACE-papers `%s` (commit %s), the monograph’s v5.16 beside v5.15, unedited; the b558 work-list’s 31 '
         'rows landed -- %s rewritten, %s already rewritten at act one by their errata’s replacements and verified by their words, %s carried '
         'in the dated Correspondence of 2026-08-12 with history lines beneath; Part IV’s preamble restating act two’s joins, chapter 24’s '
         'title and opening, the stem at v5.15 :722, the case-insensitive titles (“The Proof in One Page”, “PART III: THE PROOF”, §19.1-§19.3, '
         '§28.6) and the χ side’s §20.3-§20.4 by the restatement, stem and ceiling clauses; the Conservation-of-Spectra and '
         'perpendicular-crossing restatements read as the rows and E-2026-09-25-5 read them; the exhaustiveness sentences by the author’s '
         'reading at OPEN_TRAILS :12072; %d changes in all, each recorded with both wordings in the back matter.' % (
             ED, ec, WJ.get('rows_rewritten'), WJ.get('rows_landed'), WJ.get('rows_history'), len(rows)), '',
         '**The ceiling, whole.** Of b607’s 154 hits, %s corrected and %s carried under a named exception (a quoted source, the name-and-title '
         'exception, a dated entry), none unread; act one’s lines’ hits corrected where its own sentences did not hold them; act two’s carries '
         'stand as ratified. After the act the body holds %s ceiling hits, every one carried and printed with its exception, unexcepted %s; '
         'the scanner reads %s live stem(s).' % (H.get('c154'), H.get('k154'), H.get('carried_hits'), H.get('unexcepted'), H.get('live')), '',
         '**§25.8, re-pinned.** The Kernel Concordance takes a pin column: its seven theorems move from v1.3 = 0bc21c0 to v1.5 = 0e5233f, the '
         'terminal table’s pin, each read by git at v1.3, v1.5 and main (four lines moved within their modules), none a node of either page; '
         'the dated live-layer row carries (SIDE-global-section v0.1.0 = 706a81b). The table reads the bare name structural_exhaustiveness_proved '
         'in Bridge/ConservationBridge.lean while the concordance’s theorem is the root one of Bridge/TheBridgeComplete.lean: printed, no tool edited.', '',
         '**The §22.4 item** (`(R218)`(3)). The chain sentence carried unchanged; a history line beneath it names the direction -- the fold '
         'criterion runs from a fold to an off-line zero, the link reads the converse, the open direction -- citing spectral_cannon for what is '
         'compiled and nothing for what is not.', '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**The pages.** Both re-emitted after the edition commit from their banked probes, no Lean call: the ζ page (PLACE-papers %s) and '
         'the χ page (%s), each committed alone, the edition entering their Placement.' % (zc, xc), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the edition closes the plan of OPEN_TRAILS :12474 over the whole document, '
         'carrying act one’s errata (FINDINGS :7108), act two’s joins and sieve column (:7132), the CP-1b work-list of b558, the author’s '
         'exhaustiveness reading (OPEN_TRAILS :12072) and the terminal table’s pins into one version; it is re-read in turn by b609, whose '
         'sieve v0.4 corrects the convergence table’s “no row” cells and the monograph’s column at its next version. It strengthens the '
         'programme’s offering of the monograph: the whole document now names its argument a reduction of RH to one located clause, its '
         'kernel concordance carries the pins a reader can check, and the scanner reads it clean.', '',
         '**The record lines.** b607’s weight at FINDINGS :%d; the navigator’s fact correction at :%d; the sieve’s v0.4 work-list for b609 at '
         'OPEN_TRAILS :%d; the §22.4 item at :%d.' % (w1, w2, v1, d1), '',
         '**Next.** Per `(R218)`(5): b609, the sieve’s v0.4 with the monograph’s column re-read; then the quantifier column’s generator '
         '(W-ORD-QUANTIFIER-COLUMN, OPEN_TRAILS :12266, the DENSITY line at :12296) on the author’s word. The author rules on the closing.', '',
         '*Nothing deposits; no keystone edited beyond the edition written beside its prior version; README and REGISTRY unwritten; '
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
    put_json('b608_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


RESIDUE = ('the residue the seat prints for the author, not swept by this act: sentences beyond the ceiling that carry no word of the '
           'pattern and sit on lines this act did not otherwise edit (for example §18.1’s “establish this conversion” and §18.3’s “is resolved '
           'not by one argument but by five”, §4.5’s “unfoldable”); the “*Proof.*” labels of the lemmas of chapters 7, 13 and 22, within '
           'the ceiling; and the sieve column’s “no row” cells, b609’s by `(R218)`(2)')


def _trail_text():
    S, fj, rl = jl('b608_scores.json'), jl('b608_findings.json'), jl('b608_record_lines.json')
    H = jl('b608_h28.json')
    w1, w2, v1, d1 = [x['line'] for x in rl['lines']]
    closed = all(H.get(k) == 'HOLDS' for k in ('H28c', 'H42a', 'H42b', 'H42c'))
    rows_ = ['', TRAIL_HEAD, '',
             '**(R218) ratified.** (1) b607 at its weight. (2) The sieve’s v0.4 work-list, for b609. (3) The §22.4 observation, taken into '
             'act three. (4) CP-8 act three: the remaining chapters, the whole document as the bound; H42a-H42d. (5) The act after: b609.', '',
             '**Entered:** FINDINGS.md:%d (b607’s weight), :%d (the navigator’s fact correction), :%d (the entry, with its mutual-light line); '
             'OPEN_TRAILS :%d (the sieve’s v0.4 work-list, addressed to b605’s record :12458), :%d (the §22.4 item, addressed to b607’s record '
             ':12498); this record; PLACE-papers `%s` (v5.16, beside v5.15, unedited); both pages re-emitted.' % (
                 w1, w2, fj['entry_line'], v1, d1, ED), '',
             '**Resolved by the seat, for the author’s strike:** readings R-1 to R-14 of the edition’s back matter -- v5.16 by the series, '
             'the body above the Correspondence, the whole document as the bound, the rows mapped by the banked maps and those act one '
             'already rewrote verified by their words, every hit corrected or carried under a named exception, the case-insensitive titles '
             'and labels, the restatements of the rows, of E5-05 and of act two’s joins, the dated Correspondence and the dated version '
             'history, the author’s exhaustiveness reading, §25.8’s pin column, the §22.4 history line, the back matter re-pinned, the '
             'earlier acts’ carries standing; the collisions CL1-CL13. No prompt was put (relay data/b608_author_answers.txt).', '',
             '**For the author:** the terminal table’s bare-name row structural_exhaustiveness_proved reads its statement in '
             'Bridge/ConservationBridge.lean (the conditional theorem of that namespace), not the root theorem of TheBridgeComplete.lean the '
             'concordance names -- the pin agrees, printed, no tool edited. Two fact corrections in the text: the s-darkness theorem’s Lean '
             'chapter (25, not 24) and Conservation of Spectra’s chapter (13, not 14). The monograph’s own title, “Riemann’s Theorem”, '
             'carries unchanged at :1, and at §19.1 under the name-and-title exception (collision CL2), the label there taking the reduction.', '',
             '**CP-8:** %s; %s.' % ('closed under the ruling’s bound -- the scanner clean and no ceiling hit unexcepted on the whole document'
                                   if closed else 'not closed: the residue below is its figure', RESIDUE), '',
             '**Defects** (relay data/b608_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R218)`(5), b609, the sieve’s v0.4 with the monograph’s column re-read, then the quantifier column’s generator on '
             'the author’s word; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; FACES_LEDGER untouched; row U1 unedited; `h2` where the deposit '
             'left it; the four lists stay OPEN.', '']
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
    put_json('b608_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b608_trail.json')['line'])


def desk():
    S = jl('b608_scores.json')
    HK = ('H28a', 'H28b', 'H28c', 'H42a', 'H42b', 'H42c', 'H42d')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b608 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H28a-H28c (the whole document, the plan`s final act) and H42a-H42d, (R218)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HK]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H28/H42 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HK), sum(S[k][0] == 'REFUTED' for k in HK),
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b608_defects.txt').rstrip(NL).split(NL)
    put_txt('b608_desk_notes.txt', L)


def components():
    S, fj, tj, rl = jl('b608_scores.json'), jl('b608_findings.json'), jl('b608_trail.json'), jl('b608_record_lines.json')
    Z, X = jl('b608_page_zeta.json'), jl('b608_page_chi.json')
    L = ['b608 -- THE COMPONENTS, BANKED UNDER (R218).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b607`s closing push-out relay %s ; push-b607* branches deleted by '
         'name (data/b608_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b608_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b607`s weight FINDINGS :%d ; the fact correction :%d ; the sieve`s v0.4 work-list OPEN_TRAILS :%d ; the §22.4 item :%d' % tuple(
             x['line'] for x in rl['lines']),
         '### COMPONENT 2 : the work-list data/b608_worklist_PLACE.txt',
         '### COMPONENT 3 : the edition %s ; the diff data/b608_edition_PLACE.txt ; H28a %s, H28b %s, H28c %s ; H42a %s, H42b %s, H42c %s, H42d %s' % (
             ED, S['H28a'][0], S['H28b'][0], S['H28c'][0], S['H42a'][0], S['H42b'][0], S['H42c'][0], S['H42d'][0]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b608_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b609 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b608_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b608_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
