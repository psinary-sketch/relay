# -*- coding: utf-8 -*-
"""b609_record.py -- THE ACT'S RECORD TOOL, UNDER (R219). ### ONE SUBCOMMAND PER BANK.

### ### b609: LANE THREE, ACT THIRTY-SIX -- THE SIEVE AT v0.4 (THREE ROWS ADDED, THE EPSTEIN ROWS READ) AND THE MONOGRAPH AT v5.17
### (THE CONVERGENCE TABLE'S CELLS, §25.8'S QUALIFIED NAME); THE SECOND READER'S SEED BANKED.
### Subcommands write only `data/b609_*` unless the docstring names another file. Every bank is written through b602_record's
### `put_txt` / `put_json` (encode, temp file, `os.replace`), imported, never copied; every ledger append through b566's guarded
### `append_to`. The act's data is tools/b609_worklist.py's. No platform call. No Lean call: both pages are re-emitted from their
### banked probes. The templates are tools/b608_record.py (the monograph) and tools/b605_record.py (the sieve).
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
import b609_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
SKER = 'D:/SIDE-kernel'
RELAY = ROOT.replace('\\', '/')
PRE_PP = '3d2f67d'
PRE_RELAY = 'af1df8d6'
STEPZERO = '11970104'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/eec9660e-279c-42f1-bdfb-f149381f3e02/scratchpad'
SESSION_ID = 'eec9660e-279c-42f1-bdfb-f149381f3e02'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
HK_LIST = 'housekeeping_terminal_table.txt'
SV3, SV4, M16, M17 = K.SV3, K.SV4, K.M16, K.M17
CORR_HEAD = '## Correspondence *(added 2026-08-12'
B606_TAG = '<!-- b606 (R216) THE v5.14 EDITION`S BACK MATTER, 2026-10-03 -->'
B608_TAG = '<!-- b608 (R218) THE v5.16 EDITION`S BACK MATTER, 2026-10-03 -->'
B605_TAG = '<!-- b605 (R215) THE v0.3 EDITION`S BACK MATTER, 2026-10-03 -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, put_txt, put_json, jl, rd, sha, utc = R2.g, R2.put_txt, R2.put_json, R2.jl, R2.rd, R2.sha, R2.utc
_show = R4._show
CEILING = R4.CEILING


def _segs(l):
    return R4._segs(l)


def _poss(s):
    """### a backtick possessive (word`s) becomes ’s for a PLACE-papers file; a code span keeps its backticks."""
    return re.sub(r'(?<=\w)`(?=s\b)', '’', s)


def _count(ls):
    return sum(len(_segs(l)) for l in ls)


DEFECTS = [
    '(a) THE SEAT`S, IN COMPONENT 4: the χ page`s call was issued in parallel with the ζ page`s commit call and started in that '
    'call`s directory (PLACE-papers), where a relative `tools/b609_record.py` does not exist; Python could not open the file, so nothing '
    'ran and nothing was written (no page bank, no page byte). The call was re-run alone, after the ζ commit, with the tool`s absolute '
    'path; one page per call in the foreground held throughout.',
]
DEFECT_SHORT = ['(a) the seat’s: a page call issued in parallel started in the other call’s directory and could not open the tool -- '
                'nothing ran; re-run alone with the absolute path']


def defects():
    L = ['b609 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b609_defects.txt', L)


# ================================================================================ READING (1): THE READS
TT_NAMES = ['structural_exhaustiveness_proved', 'ConservationBridge.structural_exhaustiveness_proved', 'none_produce', 'seven_classes',
            'ostrowski_exhaustive_prime', '_root_.structural_exhaustiveness_proved',
            'techne_kernel_integration.rh_from_structural_exhaustiveness', 'techne_kernel_integration.structural_exhaustiveness_iff_rh']
PIECES_RE = r'structural_exhaustiveness_proved|seven_classes|none_produce|ostrowski_exhaustive'
READS = [
    ('the sieve`s current version v0.3, whole (the head`s counts, the tables, FD-01 and FD-02, RH-16, the bench, the back matter)', PP, PRE_PP,
     SV3, 'ALL', 260),
    ('OPEN_TRAILS: the form (:11864), W-ORD-SECOND-READER (:12212), the precedence order (:12228), the multi-act clause (:12496), the v0.4 '
     'work-list (:12518), the §22.4 item (:12520), b608`s record (:12522), b375`s census heading (:4049)', PP, PRE_PP, 'OPEN_TRAILS.md',
     [4047, 4049, 11864, 12212, 12228, 12496, 12518, 12520, 12522], 1200),
    ('OPEN_TRAILS: b608`s record, its CP-8 line (the seat`s list of the residue)', PP, PRE_PP, 'OPEN_TRAILS.md', ('GREP', r'^\*\*CP-8:\*\* closed'), 1400),
    ('the monograph`s current version v5.16: its version lines, §24.2`s GUE sentence, §24.4`s table and notes, §25.8`s head, table and '
     'opening row, the Route 1 note, the Correspondence heading and the era annotation', PP, PRE_PP, M16,
     [19, 20, 1478, 1494, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1504, 1506, 1664, 1666, 1672, 1673, 1674, 1690, 2240, 2281], 700),
    ('SIDE-explicit-formula v0.16: the detector', EFK, 'v0.16', 'SIDEExplicitFormula/Schema/Detector.lean', [96, 97, 98, 99, 100, 101, 102], 220),
    ('SIDE-explicit-formula v0.16: rhoE, the Epstein premises and epstein_not_h2_sign_cfg', EFK, 'v0.16', 'SIDEExplicitFormula/Schema/Epstein.lean',
     [32, 41, 55, 56, 57, 58, 59], 220),
    ('SIDE-explicit-formula v0.20: epstein_ef_at_window', EFK, 'v0.20', 'SIDEExplicitFormula/Schema/PlateauRamp.lean', [207, 208, 209, 210], 220),
    ('SIDE-kernel v1.5: the mechanism classes, their off-line predicates and the conjunction (TheBridgeComplete.lean, no namespace)', SKER, 'v1.5',
     'Bridge/TheBridgeComplete.lean', [20, 21, 22, 25, 79, 157, 158, 159, 160, 161, 162, 163, 198, 215, 216, 217, 249, 250, 251], 220),
    ('SIDE-kernel v1.5: Integration`s StructuralExhaustiveness, RH restated, and its iff', SKER, 'v1.5', 'Kernel/Integration.lean',
     [212, 213, 221, 252, 253], 220),
    ('SIDE-kernel v1.5: ConservationBridge`s namespace and its conditional structural_exhaustiveness_proved', SKER, 'v1.5',
     'Bridge/ConservationBridge.lean', [7, 46, 47], 220),
    ('the ζ page at PLACE-papers HEAD searched for the four compiled pieces (structural_exhaustiveness_proved, seven_classes, none_produce, '
     'ostrowski_exhaustive): none', PP, PRE_PP, PAGE, ('GREP', PIECES_RE), 200),
    ('the χ page searched for the four compiled pieces: none', PP, PRE_PP, DIR_PAGE, ('GREP', PIECES_RE), 200),
    ('the χ page: its pin line and the detector`s node (29)', PP, PRE_PP, DIR_PAGE, ('GREP', r'^(This page is generated|29\. |36\. )'), 260),
    ('relay data/terminal_table.json at relay HEAD: the rows of the mechanism pieces, by qualified name (pin, present_at, statement file)',
     RELAY, STEPZERO, 'data/terminal_table.json', ('TT', None), 0),
    ('SIMPLICITY v1.1.3: the super-repulsion sentence, the computation sentence, the GUE sentence, the open item', PP, PRE_PP,
     'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', [240, 319, 343, 371], 700),
    ('INSTRUMENTS.md at 847e433: I-7, the placement screen', PP, '847e433', 'phase1.5/method/INSTRUMENTS.md', [93, 148], 200),
    ('INVARIANCE_BARRIERS v1.4 at 1d0109f: Theorem 3.1 and Theorem 3.7', PP, '1d0109f', 'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md', [148, 259], 260),
    ('relay data/b608_edition_PLACE.txt: the residue`s nearest lines (no list of residue sentences is banked there; the seat`s list stands on '
     'b608`s trail record, its CP-8 line, read above)', RELAY, STEPZERO, 'data/b608_edition_PLACE.txt', ('GREP', r'^  X05 |^### THE WHOLE-DOCUMENT FIGURE'), 300),
    ('FINDINGS: b608`s record lines and entry', PP, PRE_PP, 'FINDINGS.md', [7154, 7156, 7158], 400),
    ('tools/banned_terms.py: the exception reading (the back-matter tag, the carried-by-history and name rows, the window)', RELAY, STEPZERO,
     'tools/banned_terms.py', [63, 64, 73, 112, 226, 227, 228, 235, 236, 248], 200),
    ('relay data/b608_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b608_closing_push_out.txt', 'ALL', 260),
    ('relay data/b608_scores.json (whole)', RELAY, STEPZERO, 'data/b608_scores.json', 'ALL', 300),
]


def _tt_rows(text):
    T = json.loads(text or '{}')
    return [r for r in T.get('rows') or [] if r.get('repo') == 'SIDE-kernel' and r.get('name') in TT_NAMES]


def reads():
    L = ['b609 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS:
        t = _show(repo, rev, path)
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH LINE (the blob does not exist)' % (label, path, at))
            continue
        if sel == ('TT', None):
            rows = _tt_rows(t)
            L.append('### %s -- %s @ %s (%d rows of %d names asked; absent: %s)' % (label, path, at, len(rows), len(TT_NAMES),
                                                                                   sorted(set(TT_NAMES) - set(r['name'] for r in rows))))
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
    L += ['', '### the pages` lists: the ζ page`s %s %s ; the χ page`s %s %s' % (
        NODES['zeta'], [l for l in rd(NODES['zeta']).split(NL) if l.startswith('# pin:')], NODES['chi'],
        [l for l in rd(NODES['chi']).split(NL) if l.startswith('# pin:')]),
        '### the sieve at %s: v0.3 blob %s ; v0.2 blob %s ; v0.1 blob %s' % (
            PRE_PP, g(PP, 'rev-parse', '%s:%s' % (PRE_PP, SV3)).strip()[:12], g(PP, 'rev-parse', '%s:%s' % (PRE_PP, K.SV2)).strip()[:12],
            g(PP, 'rev-parse', '%s:%s' % (PRE_PP, K.SV1)).strip()[:12]),
        '### the monograph at %s: v5.16 blob %s ; v5.15 blob %s ; v5.14 blob %s ; v5.13 blob %s' % (
            PRE_PP, g(PP, 'rev-parse', '%s:%s' % (PRE_PP, M16)).strip()[:12], g(PP, 'rev-parse', '%s:%s' % (PRE_PP, K.M15)).strip()[:12],
            g(PP, 'rev-parse', '%s:%s' % (PRE_PP, K.M14)).strip()[:12], g(PP, 'rev-parse', '%s:%s' % (PRE_PP, K.M13)).strip()[:12]),
        '### SIDE-kernel tags: v1.5 = %s ; main = %s ; SIDE-explicit-formula v0.16 = %s ; v0.20 = %s ; main = %s' % (
            g(SKER, 'rev-parse', '--short=7', 'v1.5^{}').strip(), g(SKER, 'rev-parse', '--short=7', 'main').strip(),
            g(EFK, 'rev-parse', '--short=7', 'v0.16^{}').strip(), g(EFK, 'rev-parse', '--short=7', 'v0.20^{}').strip(),
            g(EFK, 'rev-parse', '--short=7', 'main').strip()),
        '### TheBridgeComplete.lean at v1.5 declares no namespace (git grep "^namespace" exit %d)' % subprocess.run(
            ['git', '-C', SKER, 'grep', '-q', '^namespace', 'v1.5', '--', 'Bridge/TheBridgeComplete.lean']).returncode,
        '### a fact correction to the ferry`s letter, the navigator`s: the ferry reads “data/b608_edition_PLACE.txt`s residue sentences (the '
        'seat`s list)”; that bank holds no such list -- the seat`s list stands on b608`s trail record, its CP-8 line (read above), and it '
        'seeds this act`s bank data/b609_residue_seed.txt']
    put_txt('b609_reads.txt', L)


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
    L = ['### b609 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat (2026-10-03), banked verbatim with the options and the recommended '
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
    put_txt('b609_author_answers.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B608_ENTRY = '## CP-8, act three: the monograph’s v5.16 over the remaining chapters by the b558 work-list'
SR_LINE = '*Appended 2026-10-02 by b593 beside b592’s record (:12196), under the author’s ruling `(R203)`(3) -- W-ORD-SECOND-READER'
B375_HEAD = '### **b375 — THE KEYSTONE AND CLUSTER CENSUS (2026-09-08)**'
W_HEAD = '*Appended 2026-10-03 by b609 to b608’s entry (:%d), under `(R219)`(1) -- b608 AT ITS WEIGHT, CP-8 CLOSED:*'
I_HEAD = '*Appended 2026-10-03 by b609 to b608’s entry (:%d), under `(R219)`(2) -- THE SEAT’S ITEMS, RULED:*'
B_HEAD = ('*Appended 2026-10-03 by b609 to W-ORD-SECOND-READER (:%d), under `(R219)`(2)(iv) -- THE BATCH NAMED AND THE SEED BANKED, THE '
          'TRIGGER THE AUTHOR’S WORD:*')
P_HEAD = ('*Appended 2026-10-03 by b609 to b375’s keystone and cluster census (:%d), under `(R219)`(4) -- A PHASE-STATE READING, PRICED '
          'FOR THE AUTHOR’S WORD, NOT STARTED:*')


def _b608():
    S = json.loads(_show(RELAY, STEPZERO, 'data/b608_scores.json'))
    return {k: v[0] for k, v in S.items()}


def _b608_figures():
    """### b608`s figures read from its banks at the step-zero commit: changes, rows, the 154, act one`s lines` further hits, carried, re-pin."""
    E = json.loads(_show(RELAY, STEPZERO, 'data/b608_edition.json'))
    W = json.loads(_show(RELAY, STEPZERO, 'data/b608_worklist.json'))
    H = json.loads(_show(RELAY, STEPZERO, 'data/b608_h28.json'))
    rp = _show(RELAY, STEPZERO, 'data/b608_repin.txt') or ''
    m = re.search(r'RE-PIN : (\d+) of (\d+)', rp)
    used = set((x['line'], x['pos']) for x in W['d154'] if x.get('pos') is not None)
    others = [h for h in W['hits'] if (h['line'], h['pos']) not in used]
    a1 = [h for h in others if h['why'] is None or 'act two' not in (h['why'] or '')]
    return dict(changes=len(E['changes']), rw=W['rows_rewritten'], landed=W['rows_landed'], hist=W['rows_history'], c154=W['c154'],
                k154=W['k154'], u154=W['u154'], a1_corr=sum(1 for h in a1 if h['fate'] == 'corrected'),
                a1_car=sum(1 for h in a1 if h['fate'] == 'carried'), carried=H['carried_hits'], unexc=H['unexcepted'], live=H['live'],
                body_dn=H['body_dn'], allowed=H['allowed'], repin=(m.group(1), m.group(2)) if m else ('?', '?'))


def _texts(entry, srl, b375):
    s = _b608()
    f = _b608_figures()
    h1, h2, h3, h4 = W_HEAD % entry, I_HEAD % entry, B_HEAD % srl, P_HEAD % b375
    t1 = ('\n%s PLACE-papers `day1/A_Place_to_Stand_v5_16.md` (dcd4749) beside v5.15, v5.14 and v5.13 unedited, the pages 291f0ea and '
          'c18bc54, the record 3d2f67d: %d changes, each with both wordings; the b558 work-list’s 31 rows landed (%d rewritten -- the '
          'Conservation rows naming the T2 terminal (1 : ℚ)^s = 1, the route rows citing ch_iff_rh, the finite-range certificate T1-lit; '
          '%d already carried by act one’s replacements and checked by their wording; %d in the dated Correspondence with history lines '
          'beneath); of b607’s 154 ceiling hits %d corrected and %d carried under the three exceptions (a quoted source, the name-and-title '
          'exception, a dated entry), %d unread; of the further hits on act one’s own lines %d corrected and %d carried; the capitalised '
          'titles and labels the pattern misses corrected, §20.4’s Siegel-zero sentences conditional on GRH; Part IV’s preamble by the '
          'restatement clause; chapter 24 retitled; the stem at v5.15 :722 corrected to §18.1’s object; §22.4 carried with a history line '
          'citing spectral_cannon alone; §25.8’s seven entries moved by a pin column from v1.3 = 0bc21c0 to v1.5 = 0e5233f; body %+d '
          'against %d; %d ceiling hits in the body, each carried with its exception printed, %d unexcepted, %s live stems; re-pin %s of %s. '
          'The verdicts, as relay data/b608_scores.json prints them: H28a %s, H28b %s, H28c %s; H42a %s, H42b %s, H42c %s, H42d %s; N1 %s, '
          'N2 %s, N3 %s, N4 %s, N5 %s; S1-S5 %s. The suite 80 of 80 before and after the push. FINDINGS :7154, :7156, :7158; OPEN_TRAILS '
          ':12518, :12520, :12522. Relay e73212a5, ac6389d3, af1df8d6. No prompt, no defect. CP-8 CLOSED. Nothing deposited; no kernel '
          'touched.\n' % (
              h1, f['changes'], f['rw'], f['landed'], f['hist'], f['c154'], f['k154'], f['u154'], f['a1_corr'], f['a1_car'], f['body_dn'],
              f['allowed'], f['carried'], f['unexc'], f['live'], f['repin'][0], f['repin'][1], s['H28a'], s['H28b'], s['H28c'], s['H42a'],
              s['H42b'], s['H42c'], s['H42d'], s['N1'], s['N2'], s['N3'], s['N4'], s['N5'],
              'HELD' if all(s['S%d' % i] == 'HELD' for i in range(1, 6)) else [s['S%d' % i] for i in range(1, 6)]))
    t2 = ('\n%s (i) Reading R-8 stands: the Correspondence section of 2026-08-12 is a dated entry, its rows taking history lines. (ii) '
          '§25.8’s opening row: the bare name structural_exhaustiveness_proved resolves at the terminal table to the conditional theorem '
          'of Bridge/ConservationBridge.lean and at the concordance to the root theorem of Bridge/TheBridgeComplete.lean, the pin equal; the '
          'concordance row takes the qualified name at v5.17, a fact correction of one cell; no tool edited; the shortname ambiguity entered '
          'by name on the terminal table’s housekeeping list, opened at relay data/%s, no earlier list being found. (iii) The two fact '
          'corrections -- the Lean kernel is Chapter 25, Conservation of Spectra Chapter 13 -- recorded as the navigator’s. (iv) The residue '
          'the pattern cannot see is the second reader’s object by the form of `(R203)`(3); its batch is named at W-ORD-SECOND-READER '
          '(OPEN_TRAILS :%d, the batch line appended at the trails’ end) and the seat’s list banked as its seed, relay data/b609_residue_seed.txt; '
          'no sentence rewritten.\n' % (h2, HK_LIST, srl))
    R = jl('b609_residue.json') if os.path.exists(os.path.join(D, 'b609_residue.json')) else {}
    t3 = ('\n%s the batch is the monograph’s three acts -- v5.14 (b606, relay data/b606_edition_PLACE.txt), v5.15 (b607, '
          'data/b607_edition_PLACE.txt), v5.16 (b608, data/b608_edition_PLACE.txt) -- and the sieve’s two editions, v0.2 (b604, '
          'data/b604_edition_FINDINGS_STAND.txt) and v0.3 (b605, data/b605_edition_FINDINGS_STAND.txt), the five read as those in being '
          'when `(R219)` was written, the seat’s reading, strikeable (this act’s v0.4 and v5.17 fall outside it by the letter); the reader '
          'is handed each diff bank and the ceiling sentence and scores each substitution SAME-OBJECT, DIFFERENT-OBJECT or BEYOND-CEILING '
          'as the work-order fixes; the seed, banked at relay data/b609_residue_seed.txt, is the seat’s list of the sentences the ceiling '
          'pattern cannot see -- %s candidates of four matchers read by hand on v5.16’s body, %s marked kin, %s proof labels, %s dated, '
          '%s not kin, and the sieve’s %s, none kin -- each with its line and reason; the trigger is the author’s word; no sentence is '
          'rewritten by the seed.\n' % (h3, R.get('n16', '?'), R.get('kin', '?'), R.get('label', '?'), R.get('dated', '?'), R.get('not', '?'),
                                        R.get('n3', '?')))
    t4 = ('\n%s the REGISTRY’s phases and clusters (Phase 1 / Day 1, 1.2, 1.5 with its lettered clusters, 2 with its lettered clusters, '
          'the ANNEX) each read in one row -- the documents the registry lists, the keystones by the author-ruled tiers (K, KC, C, N, E), '
          'the edition state (edited by the form, work-list alone, neither), the sieve rows the cluster holds, the kernels anchoring it '
          'with their current tags, the deposit state -- entered as a refresh of THE_KEYSTONE_CENSUS or of SPIRAL_MAP §4A as the author '
          'chooses, every cell read from the ledgers and the pages and none from recall. The ruling it asks for ahead of the reads: which '
          'of the three “keystone” tests b375 found (this block, :%d) governs the census -- the reconciliation that census did not settle. '
          'Price: one act, reads and one census bank, one edition of the chosen document. Not started.\n' % (h4, b375))
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
    return Q, Q.line_of(Q.FIND, B608_ENTRY), Q.line_of(Q.OT, SR_LINE), Q.line_of(Q.OT, B375_HEAD)


def record_lines(*a):
    """### PLACE-papers FINDINGS: b608's weight and the seat's items ruled, addressed to b608's entry; OPEN_TRAILS: the second reader's
    ### batch addressed to W-ORD-SECOND-READER, and the phase-state reading priced, addressed to b375's census -- each appended at the end
    ### (the ledgers are append-only). Needs the seed bank first (its counts). `dry` prints."""
    Q, entry, srl, b375 = _addr()
    if (entry, srl, b375) != (7158, 12212, 4049):
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s, %s) -- NOTHING WRITTEN' % (entry, srl, b375))
    if 'dry' not in a and not os.path.exists(os.path.join(D, 'b609_residue.json')):
        sys.exit('### THE SEED IS NOT BANKED -- NOTHING WRITTEN')
    parts = _texts(entry, srl, b375)
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
    put_json('b609_record_lines.json', dict(entry=entry, srl=srl, b375=b375, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


HK_TEXT = [
    'b609 -- THE HOUSEKEEPING LIST OF THE TERMINAL TABLE (relay data/terminal_table.json, generated by tools/terminal_table.py), opened '
    'under (R219)(2)(ii); no earlier list found (searched: relay git ls-files data and tools; PLACE-papers git grep OPEN_TRAILS.md and '
    'FINDINGS.md for "housekeeping list" -- the one found is SIDE-lv-conservation`s, relay data/SIDE-lv-conservation_housekeeping.txt, '
    'opened by b603). Each entry is named, dated and not repaired here; a repair is a tool edit, which waits on its own ruling.',
    '',
    'H-TT-1 (2026-10-03, b609, (R219)(2)(ii)) -- THE SHORTNAME AMBIGUITY `structural_exhaustiveness_proved`: the table`s bare-name row '
    'reads its statement in Bridge/ConservationBridge.lean (:46 at v1.5, the conditional theorem of namespace ConservationBridge, which '
    'also has its own row as ConservationBridge.structural_exhaustiveness_proved), while the root-namespace theorem of '
    'Bridge/TheBridgeComplete.lean (:249 at v1.5 = 0e5233f; the file declares no namespace) has no row of its own; the pin agrees, v1.5 '
    '= 0e5233f. The monograph`s §25.8 opening row takes the qualified name `_root_.structural_exhaustiveness_proved` at v5.17 (a fact '
    'correction, one cell). Read beside it: of the conjunction`s three pieces only none_produce has a row (its statement file '
    'Bridge/TheBridgeComplete.lean); seven_classes and ostrowski_exhaustive_prime have none. No tool edited.',
]


def housekeeping():
    """### relay data/housekeeping_terminal_table.txt, opened (no earlier list), its first entry the shortname ambiguity."""
    p = os.path.join(D, HK_LIST)
    if os.path.exists(p):
        sys.exit('### THE LIST EXISTS -- NOTHING WRITTEN')
    put_txt(HK_LIST, HK_TEXT)
    print('  written %s (%d lines)' % (HK_LIST, len(HK_TEXT)))


def residue():
    """### data/b609_residue_seed.txt and data/b609_residue.json: the second reader's seed, (R219)(2)(iv)."""
    M = K.lines_of(_show(PP, PRE_PP, M16))
    S3 = K.lines_of(_show(PP, PRE_PP, SV3))
    if not M[K.M_CORR - 1].startswith(CORR_HEAD):
        sys.exit('### v5.16`S CORRESPONDENCE IS NOT AT :%d -- NOTHING WRITTEN' % K.M_CORR)
    hits = K.residue_hits(M, K.M_CORR - 1)
    unmarked = [(n, w) for _m, n, w in hits if (n, w) not in K.MARKS16]
    if unmarked:
        sys.exit('### UNREAD CANDIDATES %s -- NOTHING WRITTEN' % unmarked)
    L = ['b609 -- THE SECOND READER`S SEED, (R219)(2)(iv): the residue the ceiling pattern cannot see, the seat`s list, banked %s' % utc(),
         '### the object: sentences beyond the ceiling that carry no word of the pattern (relay tools/b604_record.py CEILING), and the proof '
         'labels of lemmas -- §18.1 “establish this conversion”, §18.3 “is resolved”, §4.5 “unfoldable”, the “*Proof.*” labels, and their '
         'kin (b608`s trail record, its CP-8 line); no sentence is rewritten by this bank',
         '### the documents read: the monograph`s v5.16 body (PLACE-papers %s @ %s, every line above its Correspondence heading :%d) and the '
         'sieve`s v0.3 (%s @ %s), the batch`s current versions' % (M16, PRE_PP, K.M_CORR, SV3, PRE_PP),
         '### the marks: KIN -- a sentence that says more than any compiled statement carries, without a word of the pattern; LABEL -- a '
         'proof label of a lemma within the ceiling; DATED -- inside a dated entry the history clause carries; NOT KIN -- a field fact, '
         'literature, a negation, a conditional, a name, or a fact at its own grade', '']
    for mid, desc, rx in K.RESIDUE_MATCHERS:
        n16 = sum(1 for m, _n, _w in hits if m == mid)
        n3 = sum(1 for i, l in enumerate(S3) for _x in rx.finditer(l))
        L.append('### MATCHER %s (%s): v5.16 body %d ; the sieve v0.3 %d ; pattern %s' % (mid, desc, n16, n3, rx.pattern))
    L += ['', '### v5.16`S BODY, EVERY CANDIDATE READ IN ITS SENTENCE:']
    rows = []
    for mid, n, w in sorted(hits, key=lambda x: (x[1], x[0])):
        l = M[n - 1]
        p = l.find(w) if not w.startswith('## ') else 0
        seg = next((s for s in _segs(l) if w in s), l)
        mark, why = K.MARKS16[(n, w)]
        rows.append(dict(matcher=mid, line=n, word=w, mark=mark, why=why, sentence=seg))
        L.append('  :%-5d %-4s %-7s [%s] %s' % (n, mid, mark, w, why))
        L.append('          “%s”' % seg[:600])
    L += ['', '### THE SIEVE v0.3, EVERY CANDIDATE (read by hand: each negated, inside a dated block, or a back-matter record):']
    srows = []
    for mid, desc, rx in K.RESIDUE_MATCHERS:
        for i, l in enumerate(S3):
            for m in rx.finditer(l):
                mark, why = K.sieve_mark(i + 1, l, m.group(0))
                srows.append(dict(matcher=mid, line=i + 1, word=m.group(0), mark=mark, why=why))
                L.append('  :%-5d %-4s %-7s [%s] %s -- “…%s…”' % (i + 1, mid, mark, m.group(0), why, l[max(0, m.start() - 70):m.start() + 50]))
    cnt = {k: sum(1 for r in rows if r['mark'] == k) for k in (K.KIN, K.LABEL, K.DATED, K.NOT)}
    L += ['', '### ### **THE SEED: v5.16`s body %d candidates -- KIN %d ; LABEL %d ; DATED %d ; NOT KIN %d ; the sieve v0.3 %d, KIN 0 ; '
          'unmarked %d.**' % (len(rows), cnt[K.KIN], cnt[K.LABEL], cnt[K.DATED], cnt[K.NOT], len(srows),
                              sum(1 for r in srows if r['mark'] is None))]
    if any(r['mark'] is None for r in srows):
        sys.exit('### A SIEVE CANDIDATE IS UNMARKED -- NOTHING WRITTEN')
    put_txt('b609_residue_seed.txt', L)
    put_json('b609_residue.json', dict(at=utc(), n16=len(rows), kin=cnt[K.KIN], label=cnt[K.LABEL], dated=cnt[K.DATED],
                                       n3=len(srows), rows=rows, sieve=srows, **{'not': cnt[K.NOT]}))
    print(L[-1])


# ================================================================================ COMPONENT 2: THE THREE ROWS, DRAFTED AND DECIDED
def rows():
    """### data/b609_rows_v04.txt and data/b609_rows.json: the three rows drafted with their instruments and verdicts, the mechanism row
    ### decided against the pages and the detector, FD-01 and FD-02 read -- banked before the edition is written."""
    ins = K.resolve_instruments()
    pages = {p: [l for l in (_show(PP, 'HEAD', p) or '').split(NL) if re.search(PIECES_RE, l)] for p in (PAGE, DIR_PAGE)}
    L = ['b609 -- COMPONENT 2: THE SIEVE`S THREE ROWS, DRAFTED, AND THE TWO READINGS (R219)(3)(a) -- BANKED BEFORE THE EDITION, %s' % utc(), '',
         '### PART A -- THE THREE ROWS, EACH WITH ITS INSTRUMENTS RESOLVED BY git AT THEIR PINS AND ONE VERDICT:']
    for r in K.NEW_ROWS:
        L += ['  %s (after %s) -- verdict %s ; test %s' % (r['id'], r['after'], r['verdict'], r['test']),
              '      the row: %s' % K.row_line(r)]
        for x in ins:
            if x['row'] == r['id']:
                L.append('      %s %s @ %s %s :%d -- %s' % ('RESOLVES' if x['ok'] else '### DOES NOT RESOLVE', x['repo'], x['rev'], x['path'], x['line'], x['text']))
    L += ['', '### PART B -- THE MECHANISM-ENUMERATION ROW, DECIDED AGAINST THE PAGES AND THE DETECTOR (H43b):',
          '  the navigator`s reading (OPEN_TRAILS :12518): %s' % K.MECH['navigator'],
          '  the seat`s verdict: %s, by the instrument of test 2 at its pin' % K.MECH['verdict']]
    for where, what in K.MECH['deciding']:
        L.append('    - %s: %s' % (where, what))
    for p, ls in pages.items():
        L.append('    - the four pieces on %s at PLACE-papers HEAD: %s' % (p, ls or 'NONE'))
    L += ['  the reading taken or refuted: %s' % K.MECH['refuted'].replace(':{FACE_LINE}', ':52 at v0.3'), '',
          '### PART C -- FD-01 AND FD-02, READ ONCE: %s' % K.FD_READ['decision'],
          '  the reason: %s' % K.FD_READ['reason'], '  the navigator`s stated reason: %s' % K.FD_READ['navigator']]
    for x in ins:
        if x['row'] == 'FD':
            L.append('      %s %s @ %s %s :%d -- %s' % ('RESOLVES' if x['ok'] else '### DOES NOT RESOLVE', x['repo'], x['rev'], x['path'], x['line'], x['text']))
    nok = sum(1 for x in ins if not x['ok'])
    L += ['', '### ### **THE ROWS: %d drafted ; instruments resolving %d of %d ; the mechanism row %s ; FD-01 and FD-02 %s.**' % (
        len(K.NEW_ROWS), len(ins) - nok, len(ins), K.MECH['verdict'], K.FD_READ['decision'])]
    if nok:
        sys.exit('### AN INSTRUMENT DOES NOT RESOLVE -- NOTHING WRITTEN')
    put_txt('b609_rows_v04.txt', L)
    put_json('b609_rows.json', dict(at=utc(), instruments=ins, pages=pages, rows=[dict(r, line=K.row_line(r)) for r in K.NEW_ROWS],
                                    mech=K.MECH, fd=K.FD_READ))
    print(L[-1])


# ================================================================================ COMPONENT 2: THE SIEVE AT v0.4
BM_TAG4 = '<!-- b609 (R219) THE v0.4 EDITION`S BACK MATTER, 2026-10-03 -->'


def _sv3():
    return K.lines_of(_show(PP, PRE_PP, SV3))


def _sv_map(S3):
    """### v0.3 line -> v0.4 line: the version line and its blank above :3, the three rows after RH-57."""
    i57 = next(i + 1 for i, l in enumerate(S3) if l.startswith('| RH-57 | '))
    w = {}
    for n in range(1, len(S3) + 1):
        w[n] = n + (2 if n >= 3 else 0) + (3 if n > i57 else 0)
    return w, i57


def _sv_repin(l, w, in605):
    """### a carried back-matter line of v0.2`s or v0.3`s, its own-line cells mapped to this file; returns (line, [(old, new)])."""
    subs = []

    def f(m, k=1):
        o = int(m.group(k + 1))
        subs.append((o, w[o]))
        return m.group(k) + str(w[o]) + (m.group(k + 2) if m.lastindex and m.lastindex >= k + 2 else '')
    l2 = re.sub(r'^(\| [A-Z]{2}-\d\d \(:)(\d+)(\) \|)', f, l)
    l2 = re.sub(r'^(\| [A-Z]{2}-\d\d \| :)(\d+)( \|)', f, l2)
    if in605:
        l2 = re.sub(r'^(\| :)(\d+)( \| )', f, l2)
        l2 = re.sub(r'(the clause’s one verdict \(:)(\d+)(\))', f, l2)
    return l2, subs


def sieve_edition(*a):
    """### PLACE-papers phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md beside v0.3 (unedited), from v0.3`s blob at 3d2f67d by line
    ### transforms (carry / rewrite / insert / re-pin); the re-pin step last (`sieve_repin`). Writes the edition and
    ### data/b609_sieve_edition.json; `dry` writes both to the scratchpad instead."""
    dry = 'dry' in a
    S3, bad = K.resolve_sieve()
    if bad:
        sys.exit('### THE SIEVE`S DATA DOES NOT RESOLVE %s -- NOTHING WRITTEN' % bad)
    if g(PP, 'rev-parse', 'HEAD:' + SV3).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, SV3)).strip():
        sys.exit('### v0.3 MOVED SINCE %s -- NOTHING WRITTEN' % PRE_PP)
    if not dry and not os.path.exists(os.path.join(D, 'b609_rows_v04.txt')):
        sys.exit('### THE ROWS ARE NOT BANKED -- NOTHING WRITTEN')
    dest = os.path.join(SP, 'b609_sieve_dry.md') if dry else os.path.join(PP, *SV4.split('/'))
    if not dry and os.path.exists(dest):
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    w, i57 = _sv_map(S3)
    i604 = S3.index(R4.BM_TAG) + 1
    i605 = S3.index(B605_TAG) + 1
    rew = {n: (old, new, what) for n, old, new, what in K.SV_REWRITES}
    E, rewd, ins, rep = [], [], [], []
    for n in range(1, len(S3) + 1):
        l = S3[n - 1]
        if n == 3:
            E.append(K.VERSION4)
            ins.append(dict(v4=len(E), text=K.VERSION4, what='the version line, above v0.3`s'))
            E.append('')
        if n in rew:
            old, new, what = rew[n]
            s = l.replace(old, new)
            E.append(s)
            rewd.append(dict(v3=n, v4=len(E), old=l, new=s, frag_old=old, frag_new=new, what=what))
        elif n >= i604:
            s, subs = _sv_repin(l, w, n >= i605)
            E.append(s)
            if subs:
                rep.append(dict(v3=n, v4=len(E), subs=subs, sec='v0.3`s' if n >= i605 else 'v0.2`s'))
        else:
            E.append(l)
        if w[n] != len(E):
            sys.exit('### THE MAP DRIFTED AT :%d' % n)
        if n == i57:
            for r in K.NEW_ROWS:
                E.append(K.row_line(r))
                ins.append(dict(v4=len(E), text=K.row_line(r), what='row %s, (R219)(3)(a)' % r['id']))
    pos = dict(rows={}, version=ins[0]['v4'])
    for i, l in enumerate(E, 1):
        m = re.match(r'^\| ([A-Z]{2}-\d\d) \| ', l)
        if m and i < w[i604]:
            pos['rows'][m.group(1)] = i
        if l.startswith('- **The super-repulsion fit.**'):
            pos['bench_sr'] = i
        if l.startswith('- **The Epstein witnesses.**'):
            pos['bench_ep'] = i
        if l.startswith('**The clause’s verdict, stated once:'):
            pos['clause'] = i
    E += _sv_bm(S3, w, rewd, ins, rep, pos)
    text = NL.join(E) + NL
    b = text.encode('utf-8')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    ed = text.split(NL)[:-1]
    body4, bm4 = R4._body_and_bm(ed)
    body3, bm3 = R4._body_and_bm(S3)
    b4i = set(i for i, _l in body4)
    J = dict(at=utc(), dry=dry, path=SV4, sha256=sha(b), bytes=len(b), lines=len(ed), v3_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, SV3)).strip(),
             n_v3_body=_count([l for _i, l in body3]), n_body=_count([l for _i, l in body4]), n_backmatter=_count([l for _i, l in bm4]),
             n_v3_backmatter=_count([l for _i, l in bm3]), n_full=_count(ed),
             version_lines=len(_segs(K.VERSION4)), ruled_insertions=sum(len(_segs(x['text'])) for x in ins if x['what'].startswith('row ')),
             credit=0, removals=0, rewrite_deltas=[dict(v3=x['v3'], v4=x['v4'], d=len(_segs(x['new'])) - len(_segs(x['old']))) for x in rewd],
             where={str(k): v for k, v in w.items()}, rew=rewd, ins=ins, rep=rep, pos=pos, bm4=ed.index(BM_TAG4) + 1,
             ceiling_in_body=[(i, m.group(0)) for i, l in body4 for m in CEILING.finditer(l)],
             inserted_in_body=all(x['v4'] in b4i for x in ins))
    if dry:
        io.open(os.path.join(SP, 'b609_sieve_dry.json'), 'w', encoding='utf-8').write(json.dumps(J, indent=1, ensure_ascii=False))
    else:
        put_json('b609_sieve_edition.json', J)
    print('  %s : %d lines, sha256 %s ; body v0.3 %d ; v0.4 %d (%+d) ; version %d ; ruled insertions %d ; rewrite deltas %s ; back matter %d '
          '(v0.3 %d) ; re-pinned lines %d (cells %d) ; ceiling in body %s ; rows %s' % (
              dest, len(ed), J['sha256'][:16], J['n_v3_body'], J['n_body'], J['n_body'] - J['n_v3_body'], J['version_lines'],
              J['ruled_insertions'], [(x['v3'], x['d']) for x in J['rewrite_deltas'] if x['d']], J['n_backmatter'], J['n_v3_backmatter'],
              len(rep), sum(len(x['subs']) for x in rep), J['ceiling_in_body'] or 'none',
              {k: pos['rows'].get(k) for k in ('RH-57', 'RH-58', 'RH-59', 'RH-60', 'FD-01', 'FD-02')}))


def _sv_bm(S3, w, rewd, ins, rep, pos):
    q = lambda s: R4._cell(_poss(s))
    rowsJ = dict(instruments=K.resolve_instruments())
    L = ['', '---', '', BM_TAG4, '',
         '## Back matter of the v0.4 edition — written 2026-10-03 by b609 under the author’s ruling `(R219)`(3)(a), by the form of '
         '`(R187)`(5), its clauses and the precedence order', '',
         '*This file is v0.4 of THE_FINDINGS_AS_THEY_STAND, written beside v0.3 (`%s`, unedited) from that version’s blob at PLACE-papers %s '
         'and the rows bank (relay `data/b609_rows_v04.txt`) banked before the edition was written; v0.2 and the current version (read as '
         'v0.1) stand unedited too. The back matter of v0.2 and of v0.3 is carried above whole, its own-line cells re-pinned to this file’s '
         'lines (counted below). Every line cited in this section is this file’s own unless it is marked otherwise.*' % (SV3, PRE_PP), '',
         '### The readings, each the seat’s and strikeable', '',
         '- **R-1** the three rows enter the Simplicity / RH cascade’s other rows after RH-57, numbered RH-58 to RH-60 in the order of '
         'OPEN_TRAILS :12518; the head’s row and verdict counts and the cluster’s heading are re-stated to them.',
         '- **R-2** the registers the new rows read: the GUE row reads the super-repulsion fit’s register (spacing statistics of the '
         'ordinates); the computational range and the mechanism catalogue enter the registers’ list as two more.',
         '- **R-3** the mechanism enumeration is read as a candidate route toward the located clause and toward simplicity, so the five '
         'tests are asked of it; it reads DARK at test 2, the navigator’s BRIGHT refuted with the deciding lines below.',
         '- **R-4** FD-01 and FD-02 are read as two conclusions and stay two rows; their cells are unchanged.',
         '- **R-5** the bench, the mutual-light lines, the dated blocks and every other row are carried unchanged; the GUE row stands '
         'beside the super-repulsion fit’s bench entry (:%d), which keeps its wording.' % pos['bench_sr'], '',
         '### Removals', '', 'None.', '',
         '### The three rows added', '',
         '| row | this edition’s line | the verdict | test, instrument at pin | the sources, each resolved by git at its pin | Status |',
         '|:--|:--|:--|:--|:--|:--|']
    for r in K.NEW_ROWS:
        src = '; '.join('%s @ %s %s :%d' % (x['repo'], x['rev'], x['path'], x['line']) for x in rowsJ.get('instruments') or [] if x['row'] == r['id'])
        L.append('| %s | :%d | %s | %s | %s | added, (R219)(3)(a) |' % (r['id'], pos['rows'][r['id']], r['verdict'], r['test'], q(src or 'see the rows bank')))
    L += ['', '### The mechanism enumeration’s verdict, decided against the pages and the detector', '',
          '- The navigator’s reading (OPEN_TRAILS :12518): %s.' % q(K.MECH['navigator']),
          '- The verdict at this edition: %s, RH-60 (:%d).' % (K.MECH['verdict'], pos['rows']['RH-60'])]
    L += ['- %s: %s.' % (q(a_), q(b_)) for a_, b_ in K.MECH['deciding']]
    L += ['- The reading taken or refuted: %s.' % q(K.MECH['refuted'].replace('{FACE_LINE}', str(pos['clause']))), '',
          '### FD-01 and FD-02, read once', '',
          '- The decision: %s -- FD-01 (:%d), FD-02 (:%d).' % (K.FD_READ['decision'], pos['rows']['FD-01'], pos['rows']['FD-02']),
          '- The reason: %s.' % q(K.FD_READ['reason']),
          '- The navigator’s stated reason: %s.' % q(K.FD_READ['navigator']), '',
          '### Rewrites -- the registers, the head’s counts and the cluster’s headings', '',
          '| this edition’s line | v0.3’s line | v0.3’s wording | this edition’s wording | Status |', '|:--|:--|:--|:--|:--|']
    for x in rewd:
        L.append('| :%d | :%d | %s | %s | %s |' % (x['v4'], x['v3'], q(x['frag_old']), q(x['frag_new']), q(x['what'])))
    L += ['', '### Insertions ordered by the ruling', '', '| this edition’s line | the text | Status |', '|:--|:--|:--|']
    for x in ins:
        L.append('| :%d | %s | %s |' % (x['v4'], q(x['text'])[:300], q(x['what'])))
    L += ['', '### Re-pins of v0.3’s back matter', '',
          '%d own-line cells on %d lines of the carried back matter re-pinned to this file’s lines (v0.2’s: %d lines; v0.3’s: %d lines); '
          'every other line carried verbatim.' % (sum(len(x['subs']) for x in rep), len(rep), sum(1 for x in rep if x['sec'] == 'v0.2`s'),
                                                    sum(1 for x in rep if x['sec'] == 'v0.3`s')), '',
          '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this edition, v0.4 | `%s` | written at b609 |' % SV4,
          '| v0.3 | `%s` | unedited |' % SV3,
          '| v0.2 | `%s` | unedited |' % K.SV2,
          '| the current version, unnumbered (read as v0.1) | `%s` | unedited |' % K.SV1,
          '| the rows bank | relay `data/b609_rows_v04.txt` | banked at b609 before the edition |',
          '| the sentence-by-sentence diff | relay `data/b609_edition_FINDINGS_STAND.txt` | banked at b609 |', '',
          '### Correspondence', '',
          '| row | this edition’s line | v0.3’s line | the verdict at v0.3 | the verdict at v0.4 | Status |', '|:--|:--|:--|:--|:--|:--|']
    for r in K.NEW_ROWS:
        L.append('| %s | :%d | none | none | %s%s | added |' % (r['id'], pos['rows'][r['id']], r['verdict'],
                                                              ', test %s' % r['test'].split(' ')[0] if r['test'] != '—' else ''))
    i3 = {m.group(1): i + 1 for i, l in enumerate(S3[:S3.index(R4.BM_TAG)]) for m in [re.match(r'^\| (FD-0[12]) \| ', l)] if m}
    for f in ('FD-01', 'FD-02'):
        L.append('| %s | :%d | :%d | NOT A ROUTE | NOT A ROUTE | read once, kept |' % (f, pos['rows'][f], i3[f]))
    L += ['', '### Version history', '',
          '- **v0.4, 2026-10-03 (b609, `(R219)`(3)(a))**: three rows added -- RH-58 the computational range, NOT A ROUTE; RH-59 GUE '
          'statistics, DARK by test 1; RH-60 the mechanism enumeration, DARK by test 2 -- the Epstein rows read as two conclusions; the '
          'head’s counts re-stated, 87 rows: 2 BRIGHT, 7 DARK, 67 NOT A ROUTE, 11 FACE. v0.3 stands beside it, unedited.',
          '- **v0.3, 2026-10-03 (b605, `(R215)`(4))**: its own version history is carried above.', '']
    return L


def _ed(path):
    t = io.open(os.path.join(PP, *path.split('/')), encoding='utf-8').read().replace(chr(13), '')
    return K.lines_of(t)


def _scan(path):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', path], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return r.stdout or ''


def sieve_termscan():
    """### the scanner (banned_terms.py --new) on v0.4, banked as data/b609_sieve_termscan.txt."""
    out = _scan(os.path.join(PP, *SV4.split('/')))
    put_txt('b609_sieve_termscan.txt', out.rstrip(NL).split(NL))
    print([l for l in out.split(NL) if 'live uses' in l or 'VERDICT' in l])


def sieve_carried(E, ed, S3):
    """### every non-blank v0.3 line: carried verbatim at its mapped line, rewritten with both fragments in this file`s rewrites table,
    ### or re-pinned (its own-line cells only)."""
    rw = {x['v3']: x for x in E['rew']}
    rp = {x['v3']: x for x in E['rep']}
    bm = NL.join(ed[E['bm4'] - 1:])
    ok, bad = 0, []
    for n in range(1, len(S3) + 1):
        if not S3[n - 1].strip():
            continue
        x4 = E['where'][str(n)]
        if n in rw:
            x = rw[n]
            good = ed[x4 - 1] == S3[n - 1].replace(x['frag_old'], x['frag_new']) and \
                ('| :%d | :%d | %s | %s |' % (x4, n, R4._cell(_poss(x['frag_old'])), R4._cell(_poss(x['frag_new'])))) in bm
        elif n in rp:
            s = S3[n - 1]
            good = ed[x4 - 1] == _sv_repin(s, {int(k): v for k, v in E['where'].items()}, n >= S3.index(B605_TAG) + 1)[0] and ed[x4 - 1] != s
        else:
            good = ed[x4 - 1] == S3[n - 1]
        ok += good
        if not good:
            bad.append(n)
    return ok, bad


def sieve_bank():
    """### data/b609_edition_FINDINGS_STAND.txt and data/b609_h28_sieve.json: the diff with its offset line, the rows, the counts, the
    ### ceiling, the scanner, H28a-H28c and H43a-H43b."""
    E = jl('b609_sieve_edition.json')
    ed = _ed(SV4)
    S3 = _sv3()
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### THE EDITION ON DISK IS NOT THE BANKED ONE -- NOTHING WRITTEN')
    RJ = jl('b609_rows.json')
    scan = rd('b609_sieve_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    ok, bad = sieve_carried(E, ed, S3)
    body, bm = R4._body_and_bm(ed)
    bi = set(i for i, _l in body)
    hits = [dict(line=i, hit=m.group(0), kind='body' if i in bi else 'record') for i, l in enumerate(ed, 1) for m in CEILING.finditer(l)]
    beyond = [h for h in hits if h['kind'] == 'body']
    bmt = NL.join(ed[E['bm4'] - 1:])
    P = E['pos']
    h28a_rows = [dict(id='v0.3 :%d' % x['v3'], line=x['v4'], recorded=('| :%d | :%d | ' % (x['v4'], x['v3'])) in bmt) for x in E['rew']]
    ins_ok = all(x['ok'] for x in RJ.get('instruments') or []) and bool(RJ.get('instruments'))
    rows_cite = all(ed[P['rows'][r['id']] - 1] == K.row_line(r) and r['face'] and ('| %s | :%d |' % (r['id'], P['rows'][r['id']])) in bmt for r in K.NEW_ROWS)
    h28a = 'HOLDS' if all(x['recorded'] for x in h28a_rows) and ins_ok and rows_cite else 'REFUTED'
    body_dn = E['n_body'] - E['n_v3_body']
    allowed = E['credit'] + E['removals'] + E['ruled_insertions'] + E['version_lines'] + sum(abs(x['d']) for x in E['rewrite_deltas'])
    strict = E['credit'] + E['removals'] + E['ruled_insertions'] + E['version_lines']
    h28b = 'HOLDS' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if clean and not beyond else 'REFUTED'
    VW = ('FACE', 'BRIGHT', 'DARK', 'NOT A ROUTE')
    one = []
    for r in K.NEW_ROWS:
        cells = [c.strip() for c in ed[P['rows'][r['id']] - 1].strip('|').split(' | ')]
        v = cells[4]
        res = [x for x in RJ.get('instruments') or [] if x['row'] == r['id']]
        good = v in VW and sum(1 for w in VW if v == w) == 1 and bool(res) and all(x['ok'] for x in res) and \
            ((v == 'NOT A ROUTE') == (cells[5] == '—')) and (v != 'DARK' or re.match(r'^[1-5] \(', cells[5]) is not None)
        one.append(dict(row=r['id'], line=P['rows'][r['id']], verdict=v, test=cells[5], sources=len(res), ok=good))
    h43a = 'HOLDS' if len(one) == 3 and all(x['ok'] for x in one) else 'REFUTED'
    mrow = ed[P['rows']['RH-60'] - 1]
    dec = [a_ for a_, _b in K.MECH['deciding']]
    h43b = 'HOLDS' if ('| DARK | %s |' % K.T2) in mrow and 'detector' in mrow and \
        all(('- %s: ' % R4._cell(_poss(a_))) in bmt for a_ in dec) and 'Detector.lean :99' in bmt and ':157, :159' in bmt else 'REFUTED'
    offs, last = [], None
    for n in range(1, len(S3) + 1):
        o = E['where'][str(n)] - n
        if o != last:
            offs.append((n, o))
            last = o
    L = ['### OFFSET FROM v0.3 (R190)(3): %s -- the offset changes at each v0.3 line printed (v0.3 line, offset); every v0.3 line`s v0.4 '
         'line is printed below (the map), and every edition line cited here is the final file`s own.' % ', '.join('%+d from :%d' % (o, n) for n, o in offs), '',
         'b609 -- COMPONENT 2: THE SIEVE AT v0.4, (R219)(3)(a), BY THE FORM OF (R187)(5), ITS CLAUSES AND THE PRECEDENCE ORDER', '',
         '### v0.3 : PLACE-papers %s @ %s (blob %s), %d lines' % (SV3, PRE_PP, E['v3_blob'][:8], len(S3)),
         '### v0.4 : PLACE-papers %s, %d lines, sha256 %s' % (SV4, E['lines'], E['sha256']), '',
         '### THE VERSION LINE, PRINTED: :%d %s' % (P['version'], ed[P['version'] - 1]), '',
         '### THE THREE ROWS, PRINTED, EACH WITH ONE VERDICT (H43a):']
    for x in one:
        L += ['  %s :%d -- %s ; test %s ; sources resolved %d -- %s' % (x['row'], x['line'], x['verdict'], x['test'], x['sources'], 'ONE VERDICT' if x['ok'] else '### FAILS'),
              '      %s' % ed[x['line'] - 1]]
    L += ['', '### THE MECHANISM ROW`S VERDICT AND THE LINES THAT DECIDE IT (H43b): %s -- the navigator`s reading %s' % (K.MECH['verdict'], K.MECH['navigator'])]
    L += ['    - %s: %s' % x for x in K.MECH['deciding']]
    L += ['    - %s' % K.MECH['refuted'].replace('{FACE_LINE}', str(P['clause'])), '',
          '### FD-01 AND FD-02 READ ONCE: %s -- %s' % (K.FD_READ['decision'], K.FD_READ['reason']), '',
          '### EVERY REWRITE (v0.4 line <- v0.3 line, its fragments, the segment change):']
    for x in E['rew']:
        L += ['  :%d <- :%d  %s (%+d)' % (x['v4'], x['v3'], x['what'], len(_segs(x['new'])) - len(_segs(x['old']))),
              '      was : %s' % x['frag_old'], '      now : %s' % x['frag_new']]
    L += ['', '### EVERY INSERTION (v0.4 line, its segments, what orders it):']
    L += ['  :%d (%d) %s' % (x['v4'], len(_segs(x['text'])), x['what']) for x in E['ins']]
    L += ['', '### THE RE-PINS OF THE CARRIED BACK MATTER (%d lines, %d cells: v0.3 line -> v0.4 line, its cells old -> new):' % (
        len(E['rep']), sum(len(x['subs']) for x in E['rep']))]
    L += ['  :%d -> :%d  %s %s' % (x['v3'], x['v4'], x['sec'], ', '.join(':%d -> :%d' % tuple(s) for s in x['subs'])) for x in E['rep']]
    L += ['', '### EVERY NON-BLANK v0.3 LINE -> ITS v0.4 LINE (%d carried verbatim, rewritten with its fragments recorded, or re-pinned ; '
          'failing %s):' % (ok, bad or 'none')]
    L += ['  :%s -> :%d' % (n, x) for n, x in sorted((int(k), v) for k, v in E['where'].items())]
    L += ['', '### THE COUNTS (relay tools/b558_record.py `segments`, imported): v0.3`s BODY %d ; v0.4`s BODY %d (%+d) ; the BACK MATTER %d '
          '(v0.2`s and v0.3`s carried, this act`s own, the history blocks included), printed separately ; the edition whole %d' % (
              E['n_v3_body'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled insertions %d (the three rows) + rewrites` '
          'segment changes %d + one version line %d = %d ; the strict count %d' % (
              body_dn, E['credit'], E['removals'], E['ruled_insertions'], sum(abs(x['d']) for x in E['rewrite_deltas']), E['version_lines'],
              allowed, strict), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s' % (h['line'], h['hit'], h['kind']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling in the body: %d' % len(beyond),
          '### THE SCANNER (banned_terms.py --new) on v0.4: live uses %s ; verdict %s' % (live.group(1) if live else None, 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED-IN-MEANING sentence (%d rewrites) recorded with both wordings; the three rows each citing its '
          'instruments, every source resolving.**' % (h28a, len(h28a_rows)),
          '### ### **H28b %s -- the body differs by %+d sentences against at most %d (strict %d); the back matter %d, excluded and printed.**' % (
              h28b, body_dn, allowed, strict, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s verdict %s; sentences beyond the ceiling in the body %d.**' % (h28c, 'CLEAN' if clean else 'NOT CLEAN', len(beyond)),
          '### ### **H43a %s -- the three rows resolve to their instruments at pins, each taking exactly one verdict.**' % h43a,
          '### ### **H43b %s -- the mechanism row`s verdict, %s, printed with the detector line and the kernel lines that decide it.**' % (h43b, K.MECH['verdict']),
          '### ### **THE SIEVE LANDS: NO SENTENCE HELD.**' if h28a == 'HOLDS' and not bad else '### ### **HELD AT A SENTENCE: see above.**']
    put_txt('b609_edition_FINDINGS_STAND.txt', L)
    put_json('b609_h28_sieve.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, H43a=h43a, H43b=h43b, h28a_rows=h28a_rows, body_dn=body_dn,
                                         allowed=allowed, strict=strict, backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None,
                                         clean=clean, beyond=len(beyond), hits=hits, carried_ok=ok, carried_bad=bad, one=one))
    print('H28a %s H28b %s H28c %s H43a %s H43b %s ; carried %d bad %s ; body_dn %d allowed %d strict %d ; beyond %d ; live %s' % (
        h28a, h28b, h28c, h43a, h43b, ok, bad, body_dn, allowed, strict, len(beyond), live.group(1) if live else None))


def sieve_repin():
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932), for v0.4. Writes data/b609_repin_sieve.txt."""
    E = jl('b609_sieve_edition.json')
    ed = _ed(SV4)
    S3 = _sv3()
    P = E['pos']
    w = {int(k): v for k, v in E['where'].items()}
    checks = []
    for x in E['rep']:
        for o, n in x['subs']:
            checks.append(('carried cell :%d -> :%d (at :%d)' % (o, n, x['v4']), w[o] == n and (ed[n - 1] == S3[o - 1] or any(
                y['v3'] == o and ed[n - 1] == y['new'] for y in E['rew']))))
    for r in K.NEW_ROWS:
        checks.append(('row %s on :%d' % (r['id'], P['rows'][r['id']]), ed[P['rows'][r['id']] - 1] == K.row_line(r)))
    for f in ('FD-01', 'FD-02'):
        checks.append(('%s on :%d' % (f, P['rows'][f]), ed[P['rows'][f] - 1].startswith('| %s | ' % f)))
    bm = NL.join(ed[E['bm4'] - 1:])
    for m in re.finditer(r'^\| (RH-\d\d|FD-0\d) \| :(\d+) \|', bm, re.M):
        checks.append(('v0.4`s back matter names %s at :%s' % (m.group(1), m.group(2)), P['rows'].get(m.group(1)) == int(m.group(2))))
    for m in re.finditer(r'^\| :(\d+) \| :(\d+) \| ', bm, re.M):
        a_, b_ = int(m.group(1)), int(m.group(2))
        checks.append(('the rewrites table`s :%d <- :%d' % (a_, b_), w.get(b_) == a_ and any(y['v4'] == a_ for y in E['rew'])))
    for m in re.finditer(r'^\| :(\d+) \| ', bm, re.M):
        a_ = int(m.group(1))
        checks.append(('a cited line :%d holds text' % a_, bool(ed[a_ - 1].strip())))
    for k in ('version', 'bench_sr', 'bench_ep', 'clause'):
        checks.append(('%s on :%d' % (k, P[k]), bool(ed[P[k] - 1].strip())))
    checks.append(('the clause line cited at :%d' % P['clause'], ('(:%d)' % P['clause']) in bm))
    checks.append(('the version line above v0.3`s', ed[P['version'] - 1] == K.VERSION4 and ed[P['version'] + 1] == S3[2]))
    bank = rd('b609_edition_FINDINGS_STAND.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM v0.3') and bank.count('### OFFSET FROM') == 1))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and hashlib.sha256(open(os.path.join(PP, *SV4.split('/')), 'rb').read()).hexdigest() == E['sha256']))
    for m in re.finditer(r'^  (RH-\d\d) :(\d+) -- ', bank, re.M):
        checks.append(('the diff bank`s %s at :%s' % (m.group(1), m.group(2)), P['rows'].get(m.group(1)) == int(m.group(2))))
    L = ['### b609 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % SV4, '']
    L += ['    %-100s %s' % (x[:100], 'OK' if ok else '### FAILS') for x, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _x, ok in checks), len(checks))]
    put_txt('b609_repin_sieve.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 3: THE MONOGRAPH AT v5.17
BM_TAG17 = '<!-- b609 (R219) THE v5.17 EDITION`S BACK MATTER, 2026-10-03 -->'
VERSION17 = ('**v5.17, 2026-10-03** — under `(R219)`(3)(b): §24.4’s three “no row” cells and its Epstein cell read to the sieve’s v0.4 '
             'rows, §25.8’s opening row given its qualified name, beside v5.16, which stands unedited; every change is recorded in the back '
             'matter.  ')
READINGS17 = [
    ('R-1', 'the next version by the document’s own series is v5.17, written beside v5.16 as day1/A_Place_to_Stand_v5_17.md; its version '
            'line goes above v5.16’s'),
    ('R-2', 'the body is every line above the monograph’s own Correspondence heading, as at v5.16; the back matter of v5.14, v5.15 and '
            'v5.16 is carried with its own-line cells re-pinned to this file'),
    ('R-3', 'the five cells are the whole of the change, (R219)(3)(b)’s “nothing else”: the table’s header, “Sieve verdict at v0.3 (test; '
            'row)”, and the analytic row’s cell citing RH-16 at v0.3 stand, each corrected cell naming v0.4 in its own words'),
    ('R-4', 'the qualified name of §25.8’s opening theorem is `_root_.structural_exhaustiveness_proved`: Bridge/TheBridgeComplete.lean '
            'declares no namespace, and Lean names the root namespace explicitly as `_root_`, the one form that cannot resolve to '
            'ConservationBridge.structural_exhaustiveness_proved'),
    ('R-5', 'the carried ceiling hits stand as v5.16 recorded them, each under its named exception, their lines re-pinned; the scanner’s '
            'carried-by-history row for the era annotation is listed again here, the scanner reading the exceptions of a file’s last back '
            'matter'),
]


def _mono_where(M):
    return {n: (n + 1 if n >= 19 else n) for n in range(1, len(M) + 1)}


REPIN17 = [
    r'(\*\*[A-Z0-9-]+\*\* :)(\d+)( \(v5\.1[3456] :)',
    r'^(- :)(\d+)( \(v5\.1[456] :)',
    r'(with the history line at :)(\d+)()',
    r'(^- :|and :)(\d+)( beneath :)',
    r'(:\d+ beneath :)(\d+)()',
    r'(\*\*H\d+\*\* :)(\d+)( beneath :)',
    r'^(- :)(\d+)(, carried-by-history)',
    r'(here the note is :)(\d+)()',
    r'(the body’s one live stem \(:)(\d+)(\))',
    r'(The depths sentence \(:)(\d+)(, )',
    r'(the scanner’s one live stem at :)(\d+)()',
    r'((?<=[:;,] ):)(\d+)((?= “))',
    r'(^- row \d+ \(v5\.13 :\d+, [^)]*\) — rewritten at :)(\d+)( by )',
    r'(^- row \d+ \(v5\.13 :\d+, [^)]*\) — :)(\d+)( — )',
]


def _mono_repin(l, w):
    subs = []
    for pat in REPIN17:
        def f(m):
            o = int(m.group(2))
            subs.append((o, w[o]))
            return m.group(1) + str(w[o]) + m.group(3)
        l = re.sub(pat, f, l)
    return l, subs


def _cells(spos):
    out = []
    for cid, n, old, new, clause, why, cites in K.CELLS:
        rs = lambda s: re.sub(r'\{S4:([A-Za-z0-9_-]+)\}', lambda m: str(spos['rows'].get(m.group(1)) or spos[m.group(1)]), s)
        out.append(dict(id=cid, line=n, old=old, new=rs(new), clause=clause, why=why, cites=rs(cites)))
    return out


def _spos(dry):
    J = json.load(io.open(os.path.join(SP, 'b609_sieve_dry.json'), encoding='utf-8')) if dry else jl('b609_sieve_edition.json')
    return J['pos']


def mono_edition(*a):
    """### PLACE-papers day1/A_Place_to_Stand_v5_17.md beside v5.16 (unedited): the five cells and the version line, nothing else; the
    ### back matter re-pinned and this act`s appended. Writes the edition and data/b609_mono_edition.json; `dry` to the scratchpad."""
    dry = 'dry' in a
    M, bad = K.resolve_cells()
    if bad:
        sys.exit('### THE CELLS DO NOT RESOLVE %s -- NOTHING WRITTEN' % bad)
    if not dry and not os.path.exists(os.path.join(D, 'b609_sieve_edition.json')):
        sys.exit('### THE SIEVE`S EDITION IS NOT BANKED -- NOTHING WRITTEN')
    dest = os.path.join(SP, 'b609_mono_dry.md') if dry else os.path.join(PP, *M17.split('/'))
    if not dry and os.path.exists(dest):
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    cells = _cells(_spos(dry))
    w = _mono_where(M)
    b6 = M.index(B606_TAG) + 1
    out, rep, seg_d = [], [], []
    for i, l in enumerate(M, 1):
        if i == 19:
            out.append(VERSION17)
        s = l
        mine = [c for c in cells if c['line'] == i]
        for c in mine:
            s = s.replace(c['old'], c['new'])
        if mine:
            seg_d.append(dict(line=i, ids=[c['id'] for c in mine], d=len(_segs(s)) - len(_segs(l))))
        if i >= b6:
            s2, subs = _mono_repin(s, w)
            if subs:
                rep.append(dict(v16=i, v17=w[i], subs=subs))
            s = s2
        out.append(s)
        if w[i] != len(out):
            sys.exit('### THE MAP DRIFTED AT :%d' % i)
    bm = _mono_bm(M, cells, w, rep)
    out2 = out + bm
    text = NL.join(out2) + NL
    b = text.encode('utf-8')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    ci, cm = _corr_idx(out2), _corr_idx(M)
    E = dict(at=utc(), dry=dry, path=M17, sha256=sha(b), lines=len(out2), where={str(k): v for k, v in w.items()}, version=19,
             corr=ci + 1, bm=out2.index(BM_TAG17) + 1, changes=cells, seg_d=seg_d, rep=rep,
             n_body=_count(out2[:ci]), n_cur_body=_count(M[:cm]), n_backmatter=_count(out2[ci:]), n_cur_backmatter=_count(M[cm:]),
             n_full=_count(out2), version_lines=len(_segs(VERSION17)), credit=0, removals=0, history_lines=0,
             cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, M16)).strip(),
             cell_hits=[(c['id'], [m.group(0) for m in CEILING.finditer(c['new'])]) for c in cells])
    if dry:
        io.open(os.path.join(SP, 'b609_mono_dry.json'), 'w', encoding='utf-8').write(json.dumps(E, indent=1, ensure_ascii=False))
    else:
        put_json('b609_mono_edition.json', E)
    print('  %s : %d lines, sha256 %s ; body %d (v5.16 %d, %+d) ; version line %d ; back matter %d (v5.16 %d) ; cells %d ; segment deltas %s ; '
          're-pinned lines %d (cells %d) ; ceiling hits in the new cells %s' % (
              dest, len(out2), E['sha256'][:16], E['n_body'], E['n_cur_body'], E['n_body'] - E['n_cur_body'], E['version_lines'],
              E['n_backmatter'], E['n_cur_backmatter'], len(cells), [(x['line'], x['d']) for x in seg_d if x['d']] or 'none', len(rep),
              sum(len(x['subs']) for x in rep), [x for x in E['cell_hits'] if x[1]] or 'none'))


def _corr_idx(ls):
    return next(i for i, l in enumerate(ls) if l.startswith(CORR_HEAD))


def _mono_bm(M, cells, w, rep):
    q = _poss
    era =next(i + 1 for i, l in enumerate(M) if l.startswith('- :') and ', carried-by-history — the era annotation' in l and i > M.index(B608_TAG))
    era_line = int(re.match(r'^- :(\d+),', M[era - 1]).group(1))
    L = ['', '---', '', BM_TAG17, '', '## Back matter of v5.17 -- the convergence table’s cells and §25.8’s qualified name, 2026-10-03, '
         'under `(R219)`(3)(b)', '',
         '*This section records every change v5.17 makes to v5.16, which stands beside it unedited; each line cited is this file’s own. '
         'The back matter of v5.14, v5.15 and v5.16 above is carried with its own-line cells re-pinned to this file (%d lines, %d cells; '
         'reading R-2).*' % (len(rep), sum(len(x['subs']) for x in rep)), '',
         '### The act’s readings, each the seat’s and strikeable', '']
    L += ['- **%s** %s.' % (k, q(v)) for k, v in READINGS17]
    L += ['', '### The five cells', '']
    for c in cells:
        L.append('- **%s** :%d (v5.16 :%d) — %s — %s — was: “%s” — now: “%s” — cites: %s.' % (
            c['id'], w[c['line']], c['line'], q(c['clause']), q(c['why']), c['old'], c['new'], q(c['cites'])))
    L += ['', '### Collisions resolved by the precedence order', '',
          '- **CL1** :%d (v5.16 :1496) — the table’s header names the sieve at v0.3 while four of its cells now cite v0.4 — the ruling’s '
          '“nothing else” governs: the header and the analytic row’s cell stand, each corrected cell naming its version (reading R-3).' % w[1496],
          '- **CL2** :%d (v5.16 :1690) — the Route 1 note names the theorem by its bare name — carried: the ruling corrects the table’s '
          'opening row alone; the note’s module, read beside it, fixes the root theorem.' % w[1690], '',
          '### Removals', '', '- None: no sentence of v5.16 is removed.', '',
          '### Fact corrections', '',
          '- **V05** :%d (v5.16 :1674) — the qualified name; its two wordings above.' % w[1674], '',
          '### Stem corrections', '',
          '- :%d, carried-by-history — the era annotation of 2026-08-14 (v5.16 :%d, v5.15 :2272, v5.14 :2269, v5.13 :2264), carried as v5.14, '
          'v5.15 and v5.16 carried it; listed again here because the scanner reads the exceptions of a file’s last back matter.' % (w[era_line], era_line), '',
          '### Placement', '', '| object | path | status |', '|:--|:--|:--|',
          '| this edition, v5.17 | `%s` | written at b609 |' % M17,
          '| v5.16 | `%s` | unedited |' % M16,
          '| the sieve, v0.4, whose rows the cells cite | `%s` | written at b609 |' % SV4, '',
          '### Correspondence', '', '| claim, as v5.17 states it | the source | its line | status |', '|:--|:--|:--|:--|']
    for c in cells[:4]:
        L.append('| %s | the sieve v0.4 | %s | cited at %s |' % (q(c['why']).split(' (R219)')[0], q(c['cites']).replace('the sieve v0.4 ', ''), c['id']))
    L += ['| the concordance’s Route 1 theorem is the root one | SIDE-kernel v1.5 = 0e5233f, Bridge/TheBridgeComplete.lean | :249 | cited at V05 |',
          '', '### Version history', '',
          '- v5.17, 2026-10-03 — under `(R219)`(3)(b): §24.4’s cells V01-V04 read to the sieve’s v0.4 rows (RH-58, RH-59, RH-60; FD-01 and '
          'FD-02 read as two conclusions), §25.8’s opening row given the qualified name (V05); five cells, the version line, nothing else; '
          'v5.16 unedited beside it.', '']
    return L


def mono_termscan():
    out = _scan(os.path.join(PP, *M17.split('/')))
    put_txt('b609_mono_termscan.txt', out.rstrip(NL).split(NL))
    print([l for l in out.split(NL) if 'live uses' in l or 'VERDICT' in l or 'excepted' in l])


def _classify17(ed, E):
    """### every ceiling hit of v5.17`s body: a hit on a carried line takes v5.16`s classification (b608`s, its exceptions named); a hit
    ### in a corrected cell is UNEXCEPTED; the version line is a history record."""
    import b608_record as R8
    E8 = json.loads(_show(RELAY, STEPZERO, 'data/b608_edition.json'))
    M = K.lines_of(_show(PP, PRE_PP, M16))
    h16 = R8._classify(M, E8)
    by = {}
    for h in h16:
        by.setdefault(h['line'], []).append(h['kind'])
    w = {int(k): v for k, v in E['where'].items()}
    inv = {v: k for k, v in w.items()}
    changed = set(c['line'] for c in E['changes'])
    out = []
    for i, l in enumerate(ed[:E['corr'] - 1], 1):
        src = inv.get(i)
        hs = [m.group(0) for m in CEILING.finditer(l)]
        for k, hit in enumerate(hs):
            if src is None:
                kind = 'history' if i == E['version'] else 'UNEXCEPTED'
            elif src in changed:
                old = [m.group(0) for m in CEILING.finditer(M[src - 1])]
                kind = by.get(src, ['UNEXCEPTED'] * len(old))[k] if len(old) == len(hs) else 'UNEXCEPTED'
            else:
                kind = (by.get(src) or ['UNEXCEPTED'] * len(hs))[k] if len(by.get(src) or []) == len(hs) else 'UNEXCEPTED'
            out.append(dict(line=i, src=src, hit=hit, kind=kind))
    return out, h16


def mono_carried(E, ed, M):
    w = {int(k): v for k, v in E['where'].items()}
    bm = NL.join(ed[E['bm'] - 1:])
    byl = {}
    for c in E['changes']:
        byl.setdefault(c['line'], []).append(c)
    rp = {x['v16'] for x in E['rep']}
    ok, bad = 0, []
    for n in range(1, len(M) + 1):
        if not M[n - 1].strip():
            continue
        x = w[n]
        if n in byl:
            s = M[n - 1]
            for c in byl[n]:
                s = s.replace(c['old'], c['new'])
            good = ed[x - 1] == s and all(('was: “%s”' % c['old']) in bm and ('now: “%s”' % c['new']) in bm for c in byl[n])
        elif n in rp:
            good = ed[x - 1] == _mono_repin(M[n - 1], w)[0] and ed[x - 1] != M[n - 1]
        else:
            good = ed[x - 1] == M[n - 1]
        ok += good
        if not good:
            bad.append(n)
    return ok, bad


def mono_bank():
    """### data/b609_edition_PLACE.txt and data/b609_h28_mono.json: the five cells old and new, the counts, the ceiling, the scanner,
    ### H28a-H28c and H43c-H43d (the latter reading the sieve`s bank too)."""
    E = jl('b609_mono_edition.json')
    ed = _ed(M17)
    M = K.lines_of(_show(PP, PRE_PP, M16))
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### THE EDITION ON DISK IS NOT THE BANKED ONE -- NOTHING WRITTEN')
    w = {int(k): v for k, v in E['where'].items()}
    scan = rd('b609_mono_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    ok, bad = mono_carried(E, ed, M)
    hits, h16 = _classify17(ed, E)
    kinds = {k: sum(1 for h in hits if h['kind'] == k) for k in sorted(set(h['kind'] for h in hits))}
    unexc = [h for h in hits if h['kind'] == 'UNEXCEPTED']
    car = [h for h in hits if h['kind'].startswith('carried')]
    bm = NL.join(ed[E['bm'] - 1:])
    h28a_rows = [dict(id=c['id'], line=w[c['line']], cites=c['cites'], recorded=('was: “%s”' % c['old']) in bm and ('now: “%s”' % c['new']) in bm)
                 for c in E['changes']]
    h28a = 'HOLDS' if all(x['recorded'] and x['cites'] for x in h28a_rows) else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur_body']
    rw = sum(abs(x['d']) for x in E['seg_d'])
    allowed = E['credit'] + E['removals'] + E['history_lines'] + E['version_lines'] + rw
    strict = E['credit'] + E['removals'] + E['history_lines'] + E['version_lines']
    h28b = 'HOLDS' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if clean and not unexc else 'REFUTED'
    # ### H43c: exactly five cells -- the changed body lines are the five, each differing from v5.16 in its cell alone -- and the body count
    changed_lines = [n for n in range(1, E['corr'] - 1) if (w.get(n) and n < _corr_idx(M) + 1 and ed[w[n] - 1] != M[n - 1])]
    cell_only = []
    for c in E['changes']:
        a_, b_ = M[c['line'] - 1], ed[w[c['line']] - 1]
        ca, cb = a_.strip('|').split(' | '), b_.strip('|').split(' | ')
        cell_only.append(len(ca) == len(cb) and sum(1 for x, y in zip(ca, cb) if x != y) == 1)
    five = len(E['changes']) == 5 and sorted(changed_lines) == sorted(c['line'] for c in E['changes']) and all(cell_only)
    h43c = 'HOLDS' if five and body_dn == 0 else 'REFUTED'
    HS = jl('b609_h28_sieve.json')
    h43d = 'HOLDS' if all(HS.get(k) == 'HOLDS' for k in ('H28a', 'H28b', 'H28c')) and all(x == 'HOLDS' for x in (h28a, h28b, h28c)) else 'REFUTED'
    L = ['### OFFSET FROM v5.16 (R190)(3): +0 from :1, +1 from :19 -- the version line above v5.16`s; every v5.16 line`s v5.17 line is '
         'printed below (the map), and every edition line cited here is the final file`s own.', '',
         'b609 -- COMPONENT 3: THE MONOGRAPH`S NEXT VERSION, v5.17, (R219)(3)(b), BY THE FORM OF (R187)(5): FIVE CELLS AND THE VERSION LINE', '',
         '### v5.16 : PLACE-papers %s @ %s (blob %s), %d lines' % (M16, PRE_PP, E['cur_blob'][:8], len(M)),
         '### v5.17 : PLACE-papers %s, %d lines, sha256 %s' % (M17, E['lines'], E['sha256']), '',
         '### THE VERSION LINE, PRINTED: :%d %s' % (E['version'], ed[E['version'] - 1]), '',
         '### THE FIVE CELLS, OLD AND NEW:']
    for c in E['changes']:
        L += ['  %s  v5.16 :%d -> v5.17 :%d -- %s -- %s' % (c['id'], c['line'], w[c['line']], c['clause'], c['why']),
              '      old : %s' % c['old'], '      new : %s' % c['new'], '      cites: %s' % c['cites']]
    L += ['', '### THE CHANGED BODY LINES (v5.16 numbering): %s ; each differing in one cell alone: %s' % (changed_lines, cell_only),
          '### SEGMENT CHANGES ON THE CELL LINES: %s' % ([(x['line'], x['ids'], x['d']) for x in E['seg_d']]),
          '### THE CARRIED BACK MATTER RE-PINNED: %d lines, %d cells' % (len(E['rep']), sum(len(x['subs']) for x in E['rep'])), '',
          '### EVERY NON-BLANK v5.16 LINE -> ITS v5.17 LINE (%d carried verbatim, rewritten with both wordings recorded, or re-pinned ; '
          'failing %s):' % (ok, bad or 'none')]
    L += ['  :%s -> :%d' % (n, x) for n, x in sorted(w.items())]
    L += ['', '### THE COUNTS (relay tools/b558_record.py `segments`, imported): v5.16`s BODY %d ; v5.17`s BODY %d (%+d) ; the BACK MATTER %d '
          '(v5.16`s %d), printed separately ; the edition whole %d' % (E['n_cur_body'], E['n_body'], body_dn, E['n_backmatter'],
                                                                         E['n_cur_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + history lines %d + one version line %d + the cells` '
          'segment changes %d = %d ; the strict count %d' % (body_dn, E['credit'], E['removals'], E['history_lines'], E['version_lines'], rw,
                                                             allowed, strict),
          '### H43c`s body count, by its letter: v5.17`s body %d against v5.16`s %d (%+d), the version line`s %d segments the whole of it; '
          'the five cells change %d segments' % (E['n_body'], E['n_cur_body'], body_dn, E['version_lines'], sum(x['d'] for x in E['seg_d'])), '',
          '### THE CEILING, every hit in the body, by kind: %s' % kinds]
    L += ['    :%d (v5.16 :%s) "%s" -- %s' % (h['line'], h['src'], h['hit'], h['kind']) for h in hits]
    L += ['### THE SCANNER (banned_terms.py --new) on v5.17: live uses %s ; verdict %s' % (live.group(1) if live else None, 'CLEAN' if clean else 'NOT CLEAN'),
          '### the whole-document figure: %d ceiling hits in the body, each carried as v5.16 recorded it, unexcepted %d (v5.16`s %d, its '
          'unexcepted %d)' % (len(car), len(unexc), len(h16), sum(1 for h in h16 if h['kind'] == 'UNEXCEPTED')), '',
          '### ### **H28a %s -- every MOVED-IN-MEANING cell (%d) recorded with both wordings and citing what it rests on.**' % (h28a, len(h28a_rows)),
          '### ### **H28b %s -- the body differs by %+d sentences against at most %d (strict %d); the back matter %d, excluded and printed.**' % (
              h28b, body_dn, allowed, strict, E['n_backmatter']),
          '### ### **H28c %s -- the scanner %s; ceiling hits unexcepted %d.**' % (h28c, 'CLEAN' if clean else 'NOT CLEAN', len(unexc)),
          '### ### **H43c %s -- five cells changed, each alone on its line: %s ; the body count %s (%+d, the version line).**' % (
              h43c, five, 'unchanged' if body_dn == 0 else 'changed', body_dn),
          '### ### **H43d %s -- H28a-H28c for the sieve at v0.4 (%s, %s, %s) and the monograph at v5.17 (%s, %s, %s).**' % (
              h43d, HS.get('H28a'), HS.get('H28b'), HS.get('H28c'), h28a, h28b, h28c),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' if not bad else '### ### **HELD AT A SENTENCE: see above.**']
    put_txt('b609_edition_PLACE.txt', L)
    put_json('b609_h28_mono.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, H43c=h43c, H43d=h43d, h28a_rows=h28a_rows, body_dn=body_dn,
                                        allowed=allowed, strict=strict, rw=rw, backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None,
                                        clean=clean, unexcepted=len(unexc), carried_hits=len(car), kinds=kinds, hits=hits, carried_ok=ok,
                                        carried_bad=bad, five=five, changed_lines=changed_lines, cell_only=cell_only))
    print('H28a %s H28b %s H28c %s H43c %s H43d %s ; carried %d bad %s ; body_dn %d allowed %d strict %d ; live %s ; unexcepted %d ; carried hits %d ; five %s' % (
        h28a, h28b, h28c, h43c, h43d, ok, bad, body_dn, allowed, strict, live.group(1) if live else None, len(unexc), len(car), five))


def mono_repin():
    """### THE RE-PIN STEP, THE FORM'S LAST, for v5.17. Writes data/b609_repin_mono.txt."""
    E = jl('b609_mono_edition.json')
    ed = _ed(M17)
    M = K.lines_of(_show(PP, PRE_PP, M16))
    w = {int(k): v for k, v in E['where'].items()}
    changed = set(c['line'] for c in E['changes'])
    checks = []
    for x in E['rep']:
        for o, n in x['subs']:
            checks.append(('carried cell :%d -> :%d (at :%d)' % (o, n, x['v17']), w[o] == n and (ed[n - 1] == M[o - 1] or o in changed)))
    bm = NL.join(ed[E['bm'] - 1:])
    for m in re.finditer(r'^- \*\*([A-Z0-9-]+)\*\* :(\d+) \(v5\.16 :(\d+)\)', bm, re.M):
        a_, b_ = int(m.group(2)), int(m.group(3))
        checks.append(('this act`s %s cites :%d for v5.16 :%d' % (m.group(1), a_, b_), w.get(b_) == a_ and bool(ed[a_ - 1].strip())))
    for c in E['changes']:
        checks.append(('%s`s new wording on :%d' % (c['id'], w[c['line']]), ed[w[c['line']] - 1].count(c['new']) == 1))
        for m in re.finditer(r'\(v0\.4 :(\d+)\)', c['new']):
            sv = _ed(SV4) if os.path.exists(os.path.join(PP, *SV4.split('/'))) else []
            n4 = int(m.group(1))
            checks.append(('%s cites the sieve v0.4 :%d, a row or the bench' % (c['id'], n4), bool(sv) and 0 < n4 <= len(sv) and (
                sv[n4 - 1].startswith('| RH-') or sv[n4 - 1].startswith('| FD-') or sv[n4 - 1].startswith('- **The '))))
    era = re.search(r'^- :(\d+), carried-by-history — the era annotation of 2026-08-14 \(v5\.16 :(\d+),', bm, re.M)
    checks.append(('the era annotation re-listed at :%s for v5.16 :%s' % (era.group(1) if era else '?', era.group(2) if era else '?'),
                   bool(era) and w[int(era.group(2))] == int(era.group(1)) and ed[int(era.group(1)) - 1] == M[int(era.group(2)) - 1]))
    checks.append(('the version line on :19 above v5.16`s', ed[18] == VERSION17 and ed[19] == M[18] and M[18].startswith('**v5.16, 2026-10-03**')))
    checks.append(('the Correspondence heading on :%d' % E['corr'], ed[E['corr'] - 1].startswith(CORR_HEAD)))
    checks.append(('the back-matter tag on :%d' % E['bm'], ed[E['bm'] - 1] == BM_TAG17))
    for t in (B606_TAG, '<!-- b607 (R217) THE v5.15 EDITION`S BACK MATTER, 2026-10-03 -->', B608_TAG):
        checks.append(('the tag carried: %s' % t[5:30], t in ed and ed.index(t) + 1 == w[M.index(t) + 1]))
    bank = rd('b609_edition_PLACE.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM v5.16') and bank.count('### OFFSET FROM') == 1))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and hashlib.sha256(open(os.path.join(PP, *M17.split('/')), 'rb').read()).hexdigest() == E['sha256']))
    for m in re.finditer(r'v5\.16 :(\d+) -> v5\.17 :(\d+)', bank):
        checks.append(('the diff bank`s v5.16 :%s -> v5.17 :%s' % (m.group(1), m.group(2)), w.get(int(m.group(1))) == int(m.group(2))))
    L = ['### b609 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % M17, '']
    L += ['    %-100s %s' % (x[:100], 'OK' if ok else '### FAILS') for x, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _x, ok in checks), len(checks))]
    put_txt('b609_repin_mono.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 4: THE PAGES
def page(k):
    """### after both edition commits: ONE page per call in the foreground, re-emitted from its banked probe (the ζ page from b602`s list
    ### at v0.20, the χ page from b603`s at v0.21; no Lean call). Writes the page only when it changed, and data/b609_page_<k>.json."""
    import chain_page as C
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b609_%s' % k)
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
        put_json('b609_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
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
    put_json('b609_page_%s.json' % k, J)
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s ; the probe read %s' % (k, rc, len(b), changed, secs, src_out))
    for x in dl[:60]:
        print('    ' + x[:240])


def page_arms(tag):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b609 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    L.append('### the lists read: %s' % {k: (NODES[k], PROBE[k]) for k in NODES})
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b609_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b609_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
HKEYS = ('H28a-SIEVE', 'H28b-SIEVE', 'H28c-SIEVE', 'H43a', 'H43b', 'H28a-MONO', 'H28b-MONO', 'H28c-MONO', 'H43c', 'H43d')
SCORE_KEYS = HKEYS + ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068',
            'SIDE-structural-error-correction': '6a4f482', 'SIDE-cosmo': 'c5cba30', 'SIDE-silence-principle': '667c254',
            'SIDE-global-section': '3528bcf'}


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def scores():
    HS, HM = jl('b609_h28_sieve.json'), jl('b609_h28_mono.json')
    ES, EM, RJ = jl('b609_sieve_edition.json'), jl('b609_mono_edition.json'), jl('b609_rows.json')
    Z, X = jl('b609_page_zeta.json'), jl('b609_page_chi.json')
    rs, rm = rd('b609_repin_sieve.txt'), rd('b609_repin_mono.txt')
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in KERN_PIN}
    kern_ok = kern == KERN_PIN
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1').split(NL) if x.startswith('?? ')))
    trail_landed = os.path.exists(os.path.join(D, 'b609_trail.json'))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', SV4, M17] + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = all(g(PP, 'rev-parse', 'HEAD:' + p).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, p)).strip()
                   and not g(PP, 'status', '--porcelain', '--', p).strip() for p in (SV3, K.SV2, K.SV1, M16, K.M15, K.M14, K.M13))
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b609_') and not os.path.basename(x).startswith('terminal_table')
                              and x not in ('data/b608_closing_push_out.txt', 'data/' + HK_LIST)))
    m1, m2 = re.search(r'RE-PIN : (\d+) of (\d+)', rs), re.search(r'RE-PIN : (\d+) of (\d+)', rm)
    arms2 = rd('b609_page_arms_c2.txt')
    mrow = [r for r in RJ.get('rows') or [] if r['id'] == 'RH-60']
    mv = (mrow[0]['verdict'], mrow[0]['test']) if mrow else (None, None)
    fd_two = K.FD_READ['decision'].startswith('two conclusions')
    fd_zeros = False   # ### FD-02's statement names no zero (Schema/PlateauRamp.lean :209): the navigator's "two located zeros" does not hold
    instr = RJ.get('instruments') or []
    S = {
        'H28a-SIEVE': (HS.get('H28a'), 'v0.4: every rewrite recorded with both wordings, the three rows citing their instruments'),
        'H28b-SIEVE': (HS.get('H28b'), 'v0.4: the body differs by %+d against at most %d (strict %d)' % (HS.get('body_dn', 0), HS.get('allowed', 0), HS.get('strict', 0))),
        'H28c-SIEVE': (HS.get('H28c'), 'v0.4: the scanner %s, %s live; beyond the ceiling in the body %s' % ('CLEAN' if HS.get('clean') else 'NOT CLEAN', HS.get('live'), HS.get('beyond'))),
        'H43a': (HS.get('H43a'), 'the three rows: %s' % [(x['row'], x['verdict'], x['sources'], x['ok']) for x in HS.get('one') or []]),
        'H43b': (HS.get('H43b'), 'the mechanism row %s, test %s, printed with Detector.lean :99 and TheBridgeComplete.lean :157, :159' % mv),
        'H28a-MONO': (HM.get('H28a'), 'v5.17: every cell (%d) recorded with both wordings and citing' % len(HM.get('h28a_rows') or [])),
        'H28b-MONO': (HM.get('H28b'), 'v5.17: the body differs by %+d against at most %d (strict %d)' % (HM.get('body_dn', 0), HM.get('allowed', 0), HM.get('strict', 0))),
        'H28c-MONO': (HM.get('H28c'), 'v5.17: the scanner %s, %s live; unexcepted %s; carried %s' % ('CLEAN' if HM.get('clean') else 'NOT CLEAN', HM.get('live'), HM.get('unexcepted'), HM.get('carried_hits'))),
        'H43c': (HM.get('H43c'), 'five cells, each alone on its line: %s ; the body %+d by the version line, so not unchanged by the letter' % (HM.get('five'), HM.get('body_dn', 0))
                 if HM.get('body_dn') else 'five cells %s ; the body unchanged' % HM.get('five')),
        'H43d': (HM.get('H43d'), 'H28a-H28c: v0.4 %s %s %s ; v5.17 %s %s %s' % (HS.get('H28a'), HS.get('H28b'), HS.get('H28c'), HM.get('H28a'), HM.get('H28b'), HM.get('H28c'))),
        'N1': ('HELD' if mv[0] == 'BRIGHT' and str(mv[1]).startswith('2 ') else 'REFUTED',
               'the mechanism row reads %s by test %s -- not BRIGHT: the detector names no class and the compiled exclusions name no function' % (mv[0], str(mv[1])[:1])),
        'N2': ('HELD' if fd_two and fd_zeros else 'REFUTED', 'FD-01 and FD-02: %s, the decision HELD ; the stated reason (two located zeros, '
               'two witnesses) REFUTED -- one located point, ρ_E, enters FD-01 alone, FD-02 names none' % K.FD_READ['decision']),
        'N3': ('HELD' if HM.get('five') else 'REFUTED', 'v5.17 changes %d cells, each alone on its line: %s' % (len(EM.get('changes') or []), HM.get('five'))),
        'N4': ('HELD' if HM.get('H43d') == 'HOLDS' and not HS.get('carried_bad') and not HM.get('carried_bad') else 'REFUTED',
               'H28a-H28c hold for both editions %s ; sentences held: v0.4 %s, v5.17 %s' % (HM.get('H43d'), HS.get('carried_bad'), HM.get('carried_bad'))),
        'N5': ('HELD' if kern_ok and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
               'nothing deposits; every kernel`s main unmoved %s; every current version unedited %s; PLACE-papers %s (wanted %s); relay files '
               'beyond the act`s banks, tools, the table and the housekeeping list %s%s' % (kern_ok, cur_same, pp_ch, want_pp, relay_beyond,
                                                                                         '' if trail_landed else ' ; the trail record pending')),
        'S1': ('HELD' if m1 and m2 and m1.group(1) == m1.group(2) and m2.group(1) == m2.group(2) else 'REFUTED',
               'the re-pin steps: v0.4 %s ; v5.17 %s' % (m1.group(0) if m1 else 'no bank', m2.group(0) if m2 else 'no bank')),
        'S2': ('HELD' if not HS.get('carried_bad') and not HM.get('carried_bad') else 'REFUTED',
               'every non-blank line carried: v0.3 %s (failing %s) ; v5.16 %s (failing %s)' % (HS.get('carried_ok'), HS.get('carried_bad'),
                                                                                              HM.get('carried_ok'), HM.get('carried_bad'))),
        'S3': ('HELD' if instr and all(x['ok'] for x in instr if x['row'] in ('RH-60', 'FD')) else 'REFUTED',
               'the deciding lines resolve by git at their pins: %d of %d' % (sum(1 for x in instr if x['row'] in ('RH-60', 'FD') and x['ok']),
                                                                             sum(1 for x in instr if x['row'] in ('RH-60', 'FD')))),
        'S4': ('HELD' if Z.get('changed') is True and X.get('changed') is True else 'REFUTED', 'the ζ page changed %s ; the χ page changed %s' % (
            Z.get('changed'), X.get('changed'))),
        'S5': ('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
               'after the page commits: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    }
    put_json('b609_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-11s %s -- %s' % (k, S[k][0], str(S[k][1])[:230]))


def _title():
    return ('## The sieve at v0.4 with the computational range, GUE statistics and the mechanism enumeration as rows (the mechanism row '
            'DARK by test 2) and the Epstein rows read as two conclusions; the monograph at v5.17 with the convergence table’s four cells '
            'and §25.8’s qualified name')


TRAIL_HEAD = ('### b609 — lane three, act thirty-six under (R219): the sieve at v0.4 and the monograph at v5.17 -- three rows added and '
              'the Epstein rows read, the convergence table’s cells and §25.8’s qualified name; the second reader’s seed banked')


def _finding_text():
    S, HS, HM, ES, EM = jl('b609_scores.json'), jl('b609_h28_sieve.json'), jl('b609_h28_mono.json'), jl('b609_sieve_edition.json'), jl('b609_mono_edition.json')
    rl, R = jl('b609_record_lines.json'), jl('b609_residue.json')
    w1, w2, b1, p1 = [x['line'] for x in rl['lines']]
    sc, mc = _pp_commit('b609 (R219)(3)(a): ' + SV4), _pp_commit('b609 (R219)(3)(b): ' + M17)
    zc, xc = _pp_commit('b609 (R219)(3): ' + PAGE), _pp_commit('b609 (R219)(3): ' + DIR_PAGE)
    P = ES['pos']
    t = _title()
    e = ['', t, '',
         '*Filed at b609 on the author’s ruling `(R219)`. Banks: relay `data/b609_reads.txt`, `data/b609_rows_v04.txt`, '
         '`data/b609_edition_FINDINGS_STAND.txt`, `data/b609_edition_PLACE.txt`, `data/b609_repin_sieve.txt`, `data/b609_repin_mono.txt`, '
         '`data/b609_residue_seed.txt`, `data/b609_page_arms_c2.txt`. Nothing deposits.*', '',
         '**The sieve at v0.4** (`(R219)`(3)(a)). PLACE-papers `%s` (commit %s) beside v0.3, unedited: RH-58 the computational range '
         '(:%d), NOT A ROUTE, a bench fact; RH-59 GUE statistics (:%d), DARK by test 1, beside the bench’s super-repulsion fit; RH-60 the '
         'mechanism enumeration (:%d), DARK by test 2 -- its compiled exclusions are predicates on a real σ alone (SIDE-kernel v1.5, '
         'Bridge/TheBridgeComplete.lean :157-:159), naming no function, so they hold beside the Epstein configuration the detector meets '
         'at ρ_E; the navigator’s BRIGHT refuted with those lines printed. FD-01 and FD-02 read as two conclusions, two rows: the control '
         'on the located point and the explicit formula at a window that names no zero. The head re-stated: 87 rows, 2 BRIGHT, 7 DARK, 67 '
         'NOT A ROUTE, 11 FACE.' % (SV4, sc, P['rows']['RH-58'], P['rows']['RH-59'], P['rows']['RH-60']), '',
         '**The monograph at v5.17** (`(R219)`(3)(b)). PLACE-papers `%s` (commit %s) beside v5.16, unedited: §24.4’s three “no row” cells '
         'and the Epstein cell read to the v0.4 rows, §25.8’s opening row given the qualified name `_root_.structural_exhaustiveness_proved`, '
         'the version line, nothing else; the scanner %s, %s carried ceiling hits as v5.16 recorded them, %s unexcepted.' % (
             M17, mc, 'CLEAN' if HM.get('clean') else 'NOT CLEAN', HM.get('carried_hits'), HM.get('unexcepted')), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**The pages.** Both re-emitted after the two edition commits from their banked probes, no Lean call: the ζ page (PLACE-papers %s) '
         'and the χ page (%s), each committed alone, the editions entering their Placement.' % (zc, xc), '',
         '**The second reader’s seed.** relay `data/b609_residue_seed.txt`: %s candidates of four matchers on v5.16’s body read by hand, %s '
         'kin, %s proof labels, %s dated, %s not kin; the sieve’s %s none kin; no sentence rewritten.' % (
             R.get('n16'), R.get('kin'), R.get('label'), R.get('dated'), R.get('not'), R.get('n3')), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the rows complete the sieve’s reading of the monograph’s convergence table '
         '(FINDINGS :7132, b607’s sieve column; OPEN_TRAILS :12518, b608’s work-list), and RH-60 re-reads b605’s located clause (its FACE '
         'rows, BRIGHT by test 2 at :%d) against the route that located it -- the clause carries the prime side, the enumeration does not; '
         'the qualified name re-reads b608’s §25.8 pin column (FINDINGS :7158) against the terminal table. It strengthens the programme’s '
         'offering of the sieve: every row the monograph’s table cites now has a row of its own with one verdict and its deciding line, '
         'and the monograph’s column cites them.' % P['clause'], '',
         '**The record lines.** b608’s weight at FINDINGS :%d; the seat’s items ruled at :%d; the second reader’s batch at OPEN_TRAILS :%d; '
         'the phase-state reading priced at :%d.' % (w1, w2, b1, p1), '',
         '**Next.** Per `(R219)`(5): b610, the phase-state reading if the author gives the word and names the document, else '
         'W-ORD-QUANTIFIER-COLUMN’s generator. The author rules on the closing.', '',
         '*Nothing deposits; no keystone edited beyond the two editions written beside their prior versions; README and REGISTRY unwritten; '
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
    put_json('b609_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def _trail_text():
    S, fj, rl = jl('b609_scores.json'), jl('b609_findings.json'), jl('b609_record_lines.json')
    w1, w2, b1, p1 = [x['line'] for x in rl['lines']]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R219) ratified.** (1) b608 at its weight, CP-8 closed. (2) The seat’s items ruled: R-8 stands, the qualified name, the '
             'navigator’s two fact corrections, the second reader’s batch and seed. (3) The sieve at v0.4 and the monograph at v5.17, one '
             'act; H43a-H43d. (4) A phase-state reading priced for the author’s word. (5) The act after: b610.', '',
             '**Entered:** FINDINGS.md:%d (b608’s weight), :%d (the seat’s items, ruled), :%d (the entry, with its mutual-light line); '
             'OPEN_TRAILS :%d (the second reader’s batch, addressed to W-ORD-SECOND-READER :12212), :%d (the phase-state reading, priced, '
             'addressed to b375’s census :4049); this record; PLACE-papers `%s` and `%s` (each beside its prior version, unedited); both '
             'pages re-emitted; relay data/b609_residue_seed.txt, data/%s (opened).' % (w1, w2, fj['entry_line'], b1, p1, SV4, M17, HK_LIST), '',
             '**Resolved by the seat, for the author’s strike:** the sieve’s readings R-1 to R-5 (the rows’ place and numbers, the two '
             'registers added, the enumeration read as a route, FD-01 and FD-02 two rows, the rest carried) and the monograph’s R-1 to R-5 '
             '(v5.17 by the series, the body, the five cells as the whole change with the header and the analytic cell standing, `_root_` '
             'as the qualified name, the carried hits and the scanner’s re-listed row); the collisions CL1-CL2; the second reader’s batch '
             'read as the five editions in being when `(R219)` was written. No prompt was put (relay data/b609_author_answers.txt).', '',
             '**For the author:** the mechanism enumeration reads DARK by test 2, the navigator’s BRIGHT refuted -- the detector names no '
             'mechanism class, and C₂_euler’s compiled off-line condition, σ ≠ 1/2 ∧ -σ = -(1 - σ), carries no Euler product '
             '(SIDE-kernel v1.5, Bridge/TheBridgeComplete.lean :159); FD-01 and FD-02 stay two rows, though FD-02 names no zero, so '
             '(N2)’s reason does not hold; H43c by its letter: five cells, each alone, the body +%s by the version line alone. The ferry’s '
             '“data/b608_edition_PLACE.txt’s residue sentences” were read on b608’s trail record, its CP-8 line (that bank holds no such '
             'list) -- a fact correction, the navigator’s.' % jl('b609_h28_mono.json').get('body_dn'), '',
             '**Defects** (relay data/b609_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R219)`(5), b610, the phase-state reading of `(R219)`(4) if the author gives the word and names the document, '
             'else W-ORD-QUANTIFIER-COLUMN’s generator; the author rules on the closing.', '',
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
    put_json('b609_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b609_trail.json')['line'])


def desk():
    S = jl('b609_scores.json')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b609 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H28a-H28c for both editions and H43a-H43d, (R219)(3).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H28/H43 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS),
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b609_defects.txt').rstrip(NL).split(NL)
    put_txt('b609_desk_notes.txt', L)


def components():
    S, fj, tj, rl = jl('b609_scores.json'), jl('b609_findings.json'), jl('b609_trail.json'), jl('b609_record_lines.json')
    Z, X = jl('b609_page_zeta.json'), jl('b609_page_chi.json')
    L = ['b609 -- THE COMPONENTS, BANKED UNDER (R219).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b608`s closing push-out relay %s ; push-b608* branches deleted by '
         'name (data/b609_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b609_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b608`s weight FINDINGS :%d ; the seat`s items ruled :%d ; the second reader`s batch OPEN_TRAILS :%d ; the '
         'phase-state reading priced :%d ; the seed data/b609_residue_seed.txt ; the housekeeping list data/%s' % (
             tuple(x['line'] for x in rl['lines']) + (HK_LIST,)),
         '### COMPONENT 2 : the rows data/b609_rows_v04.txt ; the sieve %s ; the diff data/b609_edition_FINDINGS_STAND.txt ; H28a %s, H28b %s, '
         'H28c %s ; H43a %s, H43b %s' % (SV4, S['H28a-SIEVE'][0], S['H28b-SIEVE'][0], S['H28c-SIEVE'][0], S['H43a'][0], S['H43b'][0]),
         '### COMPONENT 3 : the monograph %s ; the diff data/b609_edition_PLACE.txt ; H28a %s, H28b %s, H28c %s ; H43c %s, H43d %s' % (
             M17, S['H28a-MONO'][0], S['H28b-MONO'][0], S['H28c-MONO'][0], S['H43c'][0], S['H43d'][0]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b609_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b610 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b609_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b609_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
