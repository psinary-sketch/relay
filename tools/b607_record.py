# -*- coding: utf-8 -*-
"""b607_record.py -- THE ACT'S RECORD TOOL, UNDER (R217). ### ONE SUBCOMMAND PER BANK.

### ### b607: LANE THREE, ACT THIRTY-FOUR -- CP-8 ACT TWO: CHAPTERS 21 AND 22, §24.4 AND §27.3 OF THE MONOGRAPH READ AGAINST THE
### COMPILED FACES, THE DOUBLING COROLLARY AND THE SIEVE; THE MULTI-ACT CLAUSE; ERRATA'S POINTER RULE.
### Subcommands write only `data/b607_*` unless the docstring names another file. Every bank is written through b602_record's
### `put_txt` / `put_json` (encode, temp file, `os.replace`), imported, never copied; every ledger append through b566's guarded
### `append_to` (prefix-proving, stem- and backtick-checked). The work-list is tools/b607_worklist.py's data. No platform call. No
### Lean call: both pages are re-emitted from their banked probes.
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
import b607_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
RELAY = ROOT.replace('\\', '/')
PRE_PP = '2988bfa'
PRE_RELAY = 'e4808364'
STEPZERO = 'fa7722b7'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/1c5eb127-5f80-4edc-8462-5451c67ed29b/scratchpad'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/1c5eb127-5f80-4edc-8462-5451c67ed29b.jsonl'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
SIEVE = K.SIEVE
CUR, ED, ORIG = K.CUR, K.ED, K.ORIG
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
CORR_HEAD = '## Correspondence *(added 2026-08-12'
B606_TAG = '<!-- b606 (R216) THE v5.14 EDITION`S BACK MATTER, 2026-10-03 -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, put_txt, put_json, jl, rd, sha, utc = R2.g, R2.put_txt, R2.put_json, R2.jl, R2.rd, R2.sha, R2.utc
_show = R4._show
CEILING = R4.CEILING


def _segs(l):
    return R4._segs(l)


def _count(ls):
    return sum(len(_segs(l)) for l in ls)


DEFECTS = [
    '(a) A POSITIVE CONTROL ON A LINE ITS ARM DOES NOT READ (the b594 trap, repeated): G-EDITION-CARRIES`s control was carried from '
    'b606`s suite, which mutated the line mapped from v5.13 :31, the first ceiling use; at v5.14 :31 is a blank line, which the arm '
    'skips, so the control passed and G-ARMS-NO-LIVE-LIMB failed at the first pre-push run (77 of 79, the edition untouched). The '
    'control now mutates the line mapped from v5.14 :1337, a non-blank line the arm checks, through the Edit tool; the trail record, '
    'whose defect line had gone stale, was cut back to its banked length after a prefix check and re-appended, and the suite re-run '
    'whole. The seat`s.',
]
DEFECT_SHORT = ['(a) G-EDITION-CARRIES`s positive control on a blank line its arm skips, failing G-ARMS-NO-LIVE-LIMB at the first '
                'pre-push run, corrected through the Edit tool, the trail record cut back and re-appended, the seat`s']


def defects():
    L = ['b607 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b607_defects.txt', L)


# ================================================================================ READING (1): THE READS
READS = [
    ('the monograph`s current version v5.14: its head and version lines, chapters 21 and 22, §24.4 with its table and the 2026-09-22 '
     'note, §27.3, §25.8`s Route 2 row, its Correspondence heading and act one`s back-matter tag', PP, PRE_PP, CUR,
     [1, 19, 20] + [n for a, b, _t in K.SCOPE for n in range(a, b + 1)] + [1669, 2230, 2275], 260),
    ('relay data/b606_edition_PLACE.txt: the whole-document figure (the ceiling by kind, the scanner, H28c)', RELAY, STEPZERO,
     'data/b606_edition_PLACE.txt', ('GREP', r'^### THE CEILING, every hit|^### sentences beyond the ceiling|^### THE SCANNER|^### ### \*\*H28c'), 400),
    ('THE_FINDINGS_AS_THEY_STAND v0.3: the registers, the rows for Conrey`s proportion and the 2/3 (RH-16), simplicity (RH-15, RH-19), the '
     'Epstein witnesses (FD-01, FD-02) and the bench; GUE, the computational range, the mechanism enumeration and the geometric clause have '
     'no row (the grep below finds none)', PP, PRE_PP, SIEVE,
     ('GREP', r'^- \*\*(Bright|Dark) registers|^\| (RH-15|RH-16|RH-19|FD-01|FD-02) \||^- \*\*The (super-repulsion|0\.6725|Epstein)'), 420),
    ('the sieve searched for a row naming GUE, the computational range, the mechanism enumeration or the geometric clause', PP, PRE_PP, SIEVE,
     ('GREP', r'^\| [A-Z][A-Z]-\d+ \|.*(GUE|computational|10¹³|zero tables|mechanism enumeration|geometric clause|transversal)'), 300),
    ('relay data/b596_h29b.txt: the walk`s head and count', RELAY, STEPZERO, 'data/b596_h29b.txt', [1, 133, 136], 300),
    ('relay data/b596_lemmas.txt: the 2/3`s upstream line', RELAY, STEPZERO, 'data/b596_lemmas.txt', list(range(140, 147)), 300),
    ('simplicity_iff, SimpleProportion and exceptional_mass_le_third at v0.17', EFK, 'v0.17', 'SIDEExplicitFormula/Simplicity.lean', [34, 40, 45], 200),
    ('positivity_not_imp_simplicity at v0.19', EFK, 'v0.19', 'SIDEExplicitFormula/Doubling.lean', [70, 73], 200),
    ('Product.lean at v0.18 (the product lemma)', EFK, 'v0.18', 'SIDEExplicitFormula/Product.lean', [160, 169], 200),
    ('family_theorem at v0.21', EFK, 'v0.21', 'SIDEExplicitFormula/Schema/Family.lean', [213], 200),
    ('the register depths at v0.21: not_register1 and register5_output_holds (not page nodes)', EFK, 'v0.21', 'SIDEExplicitFormula/RegisterDepth.lean', [60, 297], 200),
    ('the ζ page at its own pin v0.20: its pin line and the nodes act two cites', PP, PRE_PP, PAGE,
     ('GREP', r'^(This page is generated|7\. |8\. |41\. |42\. |43\. |48\. |52\. )'), 260),
    ('the χ page at v0.21: its pin line and family_theorem', PP, PRE_PP, DIR_PAGE, ('GREP', r'^(This page is generated|23\. )'), 260),
    ('ERRATA: its form, E-2026-09-22-1 (its sentences and Status), E-2026-09-25-1 (its rows and what is not corrected), E-2026-09-25-6`s '
     'register rows and what is not corrected', PP, PRE_PP, 'ERRATA.md', [19, 401, 413, 414, 415, 416, 428, 486, 504, 505, 524, 693, 708,
                                                                           711, 714, 716, 751], 260),
    ('relay data/b532_rows.txt: the rows and their replacement lines', RELAY, STEPZERO, 'data/b532_rows.txt',
     [16, 19, 21, 24, 26, 29, 31, 34, 36, 39, 41, 44, 46, 49, 51, 54, 56, 59, 61, 64, 66, 69, 71, 74, 76, 79, 81, 84], 160),
    ('OPEN_TRAILS: the form, the stem, ceiling, history and restatement clauses, the era line, the precedence order, CP-8`s plan and b606`s '
     'record', PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 11904, 11906, 11908, 12192, 12194, 12228, 12474, 12476], 600),
    ('FINDINGS: b606`s record lines and entry', PP, PRE_PP, 'FINDINGS.md', [7104, 7106, 7108], 300),
    ('README: the ceiling', PP, PRE_PP, 'README.md', [106, 107], 300),
    ('relay data/b606_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b606_closing_push_out.txt', 'ALL', 260),
    ('relay data/b606_scores.json (whole)', RELAY, STEPZERO, 'data/b606_scores.json', 'ALL', 300),
]


def reads():
    L = ['b607 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
    b538 = json.loads(_show(RELAY, STEPZERO, 'data/b538_census.json') or '{}')
    L += ['', '### b538`s four depths (relay data/b538_census.json, every row`s grade): %s' % [
        (r.get('reg') or '?', r.get('grade')) for r in (b538.get('rows') or [])],
        '### the pages` pins: the ζ page`s list %s %s ; the χ page`s list %s %s' % (
            NODES['zeta'], [l for l in rd(NODES['zeta']).split(NL) if l.startswith('# pin:')], NODES['chi'],
            [l for l in rd(NODES['chi']).split(NL) if l.startswith('# pin:')]),
        '### the monograph`s v5.14 at %s: blob %s ; v5.13 at %s: blob %s' % (
            PRE_PP, g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip()[:12], PRE_PP, g(PP, 'rev-parse', '%s:%s' % (PRE_PP, ORIG)).strip()[:12]),
        '### a fact correction, the navigator`s: (R217)(4) reads §27.3`s registers "as E-2026-09-25-5`s replacements left them"; E-2026-09-25-5 '
        'reads the chapters before §26.1 (ERRATA :619, :687), and §27.3`s register sentences were rewritten at act one by E-2026-09-25-6`s '
        'replacements (E6-02, E6-03, E6-04, E6-05, E6-06; ERRATA :708-:722) with E-2026-09-25-1`s (M-20, M-22) and -4`s (v5.14 back matter '
        ':2324-:2327, :2348-:2352, :2368-:2369) -- read as E-2026-09-25-6`s']
    put_txt('b607_reads.txt', L)


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
    L = ['### b607 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat (2026-10-03), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % n, '']
    k = 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session 1c5eb127-5f80-4edc-8462-5451c67ed29b, transcript line %d)' % (cid, i))
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
    put_txt('b607_author_answers.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES AND ERRATA'S POINTERS
B606_ENTRY = '## CP-8, act one: the monograph’s next version, v5.14'
FORM = '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three (:11417) -- THE FORM OF AN EDITION, STANDING FOR CP-7:*'
W_HEAD = '*Appended 2026-10-03 by b607 to b606’s entry (:%d), under `(R217)`(1) -- b606 AT ITS WEIGHT:*'
F_HEAD = '*Appended 2026-10-03 by b607 to b606’s entry (:%d), under `(R217)`(1) -- TWO FACT CORRECTIONS, THE NAVIGATOR’S:*'
C_HEAD = ('*Appended 2026-10-03 by b607, under the author’s ruling `(R217)`(2), to the form of an edition (:%d) -- A CLAUSE OF THE FORM FOR '
          'MULTI-ACT EDITIONS:*')
ERR_FORM = 'what that deposit said, at the version it said it. Each entry lists: the'
ER_HEAD = '*Appended 2026-10-03 by b607 to this ledger’s form (:%d), under the author’s ruling `(R217)`(3) -- THE POINTER RULE, A HOUSEKEEPING LINE:*'
EP_HEAD = '*Appended 2026-10-03 by b607 to E-2026-09-25-1 (:%d), under `(R217)`(3) -- ITS POINTER LINE:*'
EN_HEAD = '*Appended 2026-10-03 by b607 to E-2026-09-22-1 (:%d), under `(R217)`(3) -- NO REPLACEMENT, IN ONE LINE:*'


def _b606():
    S = json.loads(_show(RELAY, STEPZERO, 'data/b606_scores.json'))
    H = json.loads(_show(RELAY, STEPZERO, 'data/b606_h28.json'))
    E = json.loads(_show(RELAY, STEPZERO, 'data/b606_edition.json'))
    W = json.loads(_show(RELAY, STEPZERO, 'data/b606_worklist.json'))
    rp = _show(RELAY, STEPZERO, 'data/b606_repin.txt') or ''
    return {k: v[0] for k, v in S.items()}, H, E, W, rp


def _scope_scan_b606(H):
    """### b606`s act scope under (R217)(2): its own sentences -- the changes it wrote, U09 carried, its history lines and its version line --
    ### and the scanner`s live uses and the ceiling hits on those lines that read beyond (none can: they are the act`s own)."""
    return dict(act_hits=H.get('act_hits'), live=H.get('live'), beyond=H.get('beyond'))


def _texts(entry, form):
    s, H, E, W, rp = _b606()
    m = re.search(r'RE-PIN : (\d+) of (\d+)', rp)
    nre = sum(1 for t in W['targets'] if t['line'] and t['new'] is not None and t.get('act', '').startswith('rewritten'))
    h1, h2, h3 = W_HEAD % entry, F_HEAD % entry, C_HEAD % form
    t1 = ('\n%s PLACE-papers `day1/A_Place_to_Stand_v5_14.md` (137985c) beside v5.13 unedited, the pages re-emitted each alone (f2a9cec, '
          '64102d2), the record 2988bfa: the eleven uses re-derived by b584’s classifier at the census pin, the monograph’s blob there equal '
          'to HEAD’s; nine rewritten by the ceiling clause, U09 (:1562) carried because its “proves” governs the compiled reduction printed '
          'beneath it -- accepted -- and U11 (:1946) taking E-2026-09-25-6’s replacement; 16 ERRATA entries naming the monograph, five with '
          'live lines, %d sentences rewritten by their replacements, E-2026-09-22-1’s three carried with two history lines; collisions C1-C4; '
          'readings R-1 to R-7 standing, R-4 included; re-pin %s of %s. The verdicts, as relay data/b606_scores.json prints them: H28a %s, '
          'H28b %s, H28c %s; H40a %s, H40b %s, H40c %s, H40d %s; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s; S1-S5 %s. Under the multi-act clause '
          '`(R217)`(2), H28c, H40c and N4 are re-read on act one’s scope -- its sentences, the scanner finding no live stem among them and '
          'none of their ceiling hits beyond (relay data/b606_h28.json: act-scope hits %s, every one inside a sentence the act wrote) -- '
          'HELD on scope, REFUTED in letter over the whole body (the scanner’s one live stem, :721, and %s ceiling hits outside act one’s '
          'sentences), both printed. FINDINGS :7104, :7106, :7108; OPEN_TRAILS :12474, :12476. Relay e5fd0a8d, 9fbdf960, e4808364; the '
          'suite 79 of 79 before and after the push. Defects (a)-(d) the seat’s. Nothing deposited; no kernel touched.\n' % (
              h1, nre, m.group(1) if m else '?', m.group(2) if m else '?', s['H28a'], s['H28b'], s['H28c'], s['H40a'], s['H40b'], s['H40c'],
              s['H40d'], s['N1'], s['N2'], s['N3'], s['N4'], s['N5'], 'HELD' if all(s['S%d' % i] == 'HELD' for i in range(1, 6)) else
              [s['S%d' % i] for i in range(1, 6)], H.get('act_hits'), H.get('beyond')))
    t2 = ('\n%s the pages’ pins crossed in `(R216)`’s ferry -- the ζ page stands at its own pin v0.20 and the χ page at v0.21, as their pin '
          'lines read; and “v6” in the navigator’s earlier prose -- the monograph’s series is v5.x, its next version v5.14 by its own version '
          'line. Each is recorded as the navigator’s; no reading of b606 moves.\n' % h2)
    t3 = ('\n%s where a document’s next versions are written over several acts under a plan on the trails, H28c’s scanner and any '
          'hypothesis bound on the whole body are scored on the act’s own scope -- the sentences its work-list names -- with the '
          'whole-document figure printed beside the score; the whole-document figure is the bound for the plan’s final act, and each act’s '
          'record carries the figure it hands the next. b606’s H28c, H40c and N4 are re-read under this clause as HELD on scope, REFUTED in '
          'letter, both printed (FINDINGS, b607’s weight line for b606).\n' % h3)
    return (h1, t1), (h2, t2), (h3, t3)


def ledger_check(*texts):
    """### b604 (a): no appended line may put a grade word within the table generator's window of a backticked name."""
    import terminal_table as TT
    bad = []
    for t in texts:
        for ln in t.split(NL):
            if TT.GRADE_RE.search(ln) and TT._names_on(ln):
                bad.append((ln[:120], TT._names_on(ln)))
    return bad


def record_lines(*a):
    """### PLACE-papers FINDINGS: b606's weight (with the three letter-refutations re-read under (2)) and the two fact corrections,
    ### addressed to b606's entry; OPEN_TRAILS: the multi-act clause, appended at the end addressed to the form's block :11864 (the
    ### ledgers are append-only). `dry` prints."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, B606_ENTRY)
    form = Q.line_of(Q.OT, FORM)
    if entry != 7108 or form != 11864:
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s) -- NOTHING WRITTEN' % (entry, form))
    (h1, t1), (h2, t2), (h3, t3) = _texts(entry, form)
    bad = ledger_check(t1, t2, t3)
    print('  grade-word lines naming a backticked name: %s' % (bad or 'NONE'))
    if 'dry' in a:
        for t in (t1, t2, t3):
            print(t)
        return
    if bad:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME -- NOTHING WRITTEN')
    for p, h in ((Q.FIND, h1), (Q.FIND, h2), (Q.OT, h3)):
        Q.guard_absent(p, h)
    out = []
    for p, h, t in ((Q.FIND, h1, t1), (Q.FIND, h2, t2), (Q.OT, h3, t3)):
        r = Q.append_to(p, t)
        out.append(dict(file=os.path.basename(p), head=h, line=Q.line_of(p, h), append=r))
    put_json('b607_record_lines.json', dict(entry=entry, form=form, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


def _errata_text(fl, e251, e221):
    r = ER_HEAD % fl
    p = EP_HEAD % e251
    n = EN_HEAD % e221
    t = ('\n%s an ERRATA entry whose replacement text lives in a relay bank carries a pointer line naming the bank by path and line; an '
         'entry that gives no replacement says so in one line and the edition carries the sentence with a history line, as b606 did. '
         'Applied first by the two lines below. No line above is edited.\n\n'
         '%s the replacement text of this entry’s sentences lives in relay `data/b532_rows.txt` (:16-:84, one row for each sentence listed '
         'above): the monograph’s ten rows M-02, M-04, M-09, M-13, M-14, M-18, M-20, M-22, M-23 and M-24 at :16-:64, each row’s replacement '
         'on its fourth line (:19, :24, :29, :34, :39, :44, :49, :54, :59, :64); the kernel record’s K-01 at :66 (its replacement :69); the '
         'Zenodo rows Z21520474-01, -02 and Z21539167-01 at :71, :76 and :81 (their replacements :74, :79, :84). The monograph’s edition '
         'v5.14 rewrote nine of the ten monograph sentences by these replacements, and M-04 by E-2026-09-25-6’s, which extends it '
         '(`day1/A_Place_to_Stand_v5_14.md`, its back matter, collision C2). No line above is edited.\n\n'
         '%s this entry gives no replacement for its sentences -- its Status leaves any narrowing to the wave under `(R66)` -- and the '
         'monograph’s edition v5.14 carries three of its live sentences unchanged, with history lines beneath their paragraphs '
         '(`day1/A_Place_to_Stand_v5_14.md` :1796, :1802); its fourth, the monograph’s :68, takes E-2026-09-25-5’s replacement (its back '
         'matter, collision C3). No line above is edited.\n' % (r, p, n))
    return (r, p, n), t


def errata(*a):
    """### PLACE-papers ERRATA.md: the pointer rule addressed to the ledger's form, E-2026-09-25-1's pointer line and E-2026-09-22-1's one
    ### line, appended at the ledger's end, each addressed to its entry (no line moves; the edition's ERRATA citations hold). The id
    ### appender (tools/errata_append.py) refuses an id already in the file by design, so the append goes through b566's guarded append,
    ### which proves the prior bytes a prefix. `dry` prints. The commit, ERRATA.md alone, is the seat's."""
    Q = R2._Q()
    path = os.path.join(PP, 'ERRATA.md')
    fl = Q.line_of(path, ERR_FORM)
    e251 = Q.line_of(path, '## E-2026-09-25-1 — ')
    e221 = Q.line_of(path, '## E-2026-09-22-1 — ')
    if (fl, e251, e221) != (19, 486, 401):
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s, %s) -- NOTHING WRITTEN' % (fl, e251, e221))
    heads, t = _errata_text(fl, e251, e221)
    v14 = K.lines_of(_show(PP, PRE_PP, CUR))
    hist_ok = v14[1795].startswith('*v5.14, 2026-10-03, a history line under E-2026-09-22-1') and v14[1801].startswith('*v5.14, 2026-10-03, a history line under E-2026-09-22-1')
    b532 = rd('b532_rows.txt').split(NL)
    rows_ok = all(b532[n - 1].startswith('  REPLACEMENT') for n in (19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84)) and \
        [b532[n - 1].split()[0] for n in (16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81)] == [
            'M-02', 'M-04', 'M-09', 'M-13', 'M-14', 'M-18', 'M-20', 'M-22', 'M-23', 'M-24', 'K-01', 'Z21520474-01', 'Z21520474-02', 'Z21539167-01']
    print('  the cited lines: v5.14 history lines %s ; b532 rows and replacement lines %s' % (hist_ok, rows_ok))
    bad = ledger_check(t)
    if 'dry' in a:
        print(t)
        return
    if bad or not hist_ok or not rows_ok:
        sys.exit('### A CITED LINE DOES NOT READ AS WRITTEN, OR A GRADE LINE -- NOTHING WRITTEN')
    for h in heads:
        Q.guard_absent(path, h)
    r = Q.append_to(path, t)
    put_json('b607_errata.json', dict(heads=list(heads), lines=[Q.line_of(path, h) for h in heads], append=r, form=fl, e251=e251, e221=e221))
    print('  ERRATA :%s' % [Q.line_of(path, h) for h in heads], r)


# ================================================================================ COMPONENT 2: THE WORK-LIST
def _b606_beyond():
    """### b606`s 171: the hits its diff bank prints as beyond, by v5.14 line."""
    t = _show(RELAY, STEPZERO, 'data/b606_edition_PLACE.txt') or ''
    return [(int(m.group(1)), m.group(2)) for m in re.finditer(r'^    :(\d+) "([^"]+)" -- beyond', t, re.M)]


def _scope_hits(M):
    out = []
    for a, b, tag in K.SCOPE:
        for i in range(a, b + 1):
            for k, s in enumerate(_segs(M[i - 1])):
                for m in CEILING.finditer(s):
                    out.append(dict(line=i, seg=k, hit=m.group(0), sentence=s, scope=tag))
    return out


def _hit_action(h, rows):
    """### a scope hit`s fate: the change that rewrites its sentence (its hit gone or kept), or the carry that reads it."""
    for r in rows:
        if r['line'] == h['line'] and r['old'] in h['sentence'] or (r['line'] == h['line'] and h['sentence'] in r['old']):
            kept = h['hit'] in [m.group(0) for m in CEILING.finditer(r['new'])]
            return ('rewritten, the hit kept (carried by its reason)' if kept else 'rewritten away'), r['id']
    for n, frag, why in K.CARRIES:
        if n == h['line'] and frag in h['sentence']:
            return 'carried', why
    return 'UNREAD', None


def _sieve_rows():
    sv = K.lines_of(_show(PP, PRE_PP, SIEVE) or '')
    rows = {}
    for i, l in enumerate(sv, 1):
        m = re.match(r'^\| ([A-Z][A-Z]-\d+) \| (.*)$', l)
        if m and m.group(1) not in rows:
            cells = [c.strip() for c in l.strip().strip('|').split('|')]
            rows[m.group(1)] = dict(line=i, verdict=cells[4] if len(cells) > 4 else None, test=cells[5] if len(cells) > 5 else None,
                                    register=cells[3] if len(cells) > 3 else None, text=l)
    return sv, rows


def worklist(*a):
    """### data/b607_worklist_PLACE.txt (and .json), banked before any writing of the edition."""
    L, data = _wl()
    put_txt('b607_worklist_PLACE.txt', L)
    put_json('b607_worklist.json', data)
    print('  joins %d ; table rows rowed %d of %d (exactly one %d) ; §27.3 %d ; scope hits %d (in the 171: %d) ; unread %d ; χ-side %d' % (
        data['joins'], sum(1 for t in data['tmap'] if t['ids']), len(data['tmap']), sum(1 for t in data['tmap'] if len(t['ids']) == 1),
        data['s273'], len(data['hits']), data['in171'], sum(1 for x in data['hits'] if x['act'] == 'UNREAD'), len(data['chi'])))


def _wl_data():
    p = os.path.join(D, 'b607_worklist.json')
    return jl('b607_worklist.json') if os.path.exists(p) else _wl()[1]


def _wl():
    M, rows, bad = K.resolve()
    if bad:
        sys.exit('### THE WORK-LIST DOES NOT RESOLVE: %s -- NOTHING WRITTEN' % bad)
    hits = _scope_hits(M)
    b171 = _b606_beyond()
    in171 = [x for x in b171 if K.in_scope(x[0])]
    sv, srows = _sieve_rows()
    L = ['b607 -- COMPONENT 2: CP-8 ACT TWO`S WORK-LIST, (R217)(4) -- ASSEMBLED BEFORE ANY WRITING, banked %s' % utc(),
         '### the current version: PLACE-papers %s @ %s, %d lines, blob %s; its version line :19 "%s"' % (
             CUR, PRE_PP, len(M), g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip()[:12], M[18][:80]),
         '### the next version by its own series: v5.15, written beside it as %s' % ED,
         '### the scope: %s' % '; '.join('%s :%d-:%d' % (t, a_, b_) for a_, b_, t in K.SCOPE), '',
         '### PART A -- CHAPTERS 21 AND 22: EVERY SENTENCE JOINING SIMPLICITY AND RH, WITH ITS LINE (reading R-4), AND WHAT IT TAKES:']
    joins = [r for r in rows if r['kind'] == 'join']
    for r in joins:
        L += ['  %s :%d (%s) -- %s' % (r['id'], r['line'], r['clause'], r['why']), '      old : %s' % r['old'], '      new : %s' % r['new'],
              '      cites: %s' % r['cites']]
    L.append('  ### join-shaped sentences that carry (reading R-4):')
    L += ['  :%d "%s" -- %s' % x for x in K.NOT_JOINS]
    L.append('  ### the ruling`s Conrey reading in chapter 21:')
    L += ['  %s :%d (%s)%s      old : %s%s      new : %s' % (r['id'], r['line'], r['clause'], NL, r['old'], NL, r['new']) for r in rows if r['kind'] == 'ruled']
    L.append('  ### standing, as the ruling names them:')
    L += ['  :%d -- %s' % x for x in K.STANDS if x[0] < 1420]
    L += ['', '### PART B -- §24.4`S TABLE, EVERY ROW WITH THE SIEVE ROW IT MAPS TO (THE_FINDINGS_AS_THEY_STAND v0.3 @ %s, read live):' % PRE_PP]
    tmap = []
    for (trad, ids, verdict, test, reg), r in zip(K.TABLE, [r for r in rows if r['id'] in ('T02', 'T03', 'T04', 'T05', 'T06')]):
        got = [(i, srows.get(i, {}).get('line'), srows.get(i, {}).get('verdict'), srows.get(i, {}).get('test')) for i in ids]
        ok = all(x[1] and x[2] == verdict for x in got)
        tmap.append(dict(row=trad, ids=ids, verdict=verdict, test=test, register=reg, got=got, ok=ok, line=r['line']))
        L += ['  :%d %s -> %s ; register: %s ; verdict %s, test %s ; read live: %s' % (r['line'], trad, ids or 'NO ROW', reg, verdict, test, got),
              '      the new cell: %s' % r['new'].rsplit('|', 2)[-2].strip()]
    nrowed = sum(1 for t in tmap if t['ids'])
    one = sum(1 for t in tmap if len(t['ids']) == 1)
    cite = sv[K.SIEVE_CITE_LINE - 1] if len(sv) >= K.SIEVE_CITE_LINE else ''
    v13 = K.lines_of(_show(PP, PRE_PP, ORIG))
    resolves = ':1499' in cite and v13[1498].startswith('**Analytic-row note (2026-09-22')
    L += ['  rows: %d ; rows with a sieve row: %d ; rows mapping to exactly one: %d ; rows with a verdict: %d' % (
        len(tmap), nrowed, one, sum(1 for t in tmap if t['verdict'])),
        '  the sieve`s own row for the table: v0.3 :%d "%s" -> A_Place_to_Stand (the current version the sieve read, v5.13) :1499 "%s" -- %s' % (
            K.SIEVE_CITE_LINE, cite[:160], v13[1498][:60], 'RESOLVES' if resolves else '### DOES NOT RESOLVE'),
        '  the ruling`s other §24.4 objects: the analytic-row note :1500 is a dated entry (2026-09-22) -- by the history clause the ruled '
        'SimpleProportion reading goes in a history line beneath it (reading R-6): %s' % K.HIST[1500][:200],
        '  T08 :1504 -- %s' % [r for r in rows if r['id'] == 'T08'][0]['why']]
    L += ['  :%d -- %s' % x for x in K.STANDS if 1490 <= x[0] <= 1505]
    L += ['', '### PART C -- §27.3: THE REGISTERS AS E-2026-09-25-6`S REPLACEMENTS LEFT THEM (the navigator`s "-5" read as -6, relay '
          'data/b607_reads.txt), RE-READ AGAINST THE PAGES AT THEIR PINS AND b538`S FOUR DEPTHS:',
          '  the depths sentence :1798 s0 (E6-04): %s' % _segs(M[1797])[0][:300],
          '  re-read: ch_iff_rh -> %s ; h2_sign_iff_rh -> %s ; not_register1 and register5_output_holds -> not page nodes, '
          'SIDE-explicit-formula RegisterDepth.lean :60 and :297 at 81ae175 and at v0.21 ; b538: false, equivalent, undecided, equivalent in '
          'its Weil form, holds -- the sentence AGREES' % (K.PINS['ch_iff_rh'][2], K.PINS['h2_sign_iff_rh'][2]),
          '  the residue, each with the clause that reaches it:']
    s273 = [r for r in rows if r['scope'] == '§27.3']
    for r in s273:
        L += ['  %s :%d (%s) -- %s' % (r['id'], r['line'], r['clause'], r['why']), '      old : %s' % r['old'], '      new : %s' % r['new']]
    L += ['  :%d -- %s' % x for x in K.STANDS if x[0] >= 1788]
    L.append('  §27.3`s further corrections after act one`s errata: %d' % len(s273))
    L += ['', '### PART D -- THE χ-SIDE SENTENCES IN SCOPE (reading R-9):']
    chi = [(i, s) for a_, b_, _t in K.SCOPE for i in range(a_, b_ + 1) for s in _segs(M[i - 1]) if K.CHI_RE.search(s)]
    L += ['  :%d %s' % (i, s[:260]) for i, s in chi]
    L.append('  -> %d sentence(s): the two naming the missing family speak of Katz–Sarnak`s ensemble for ξ, and the one naming GRH is '
             'Lagarias`s published bound in §27.3`s ancestry; no sentence in scope speaks of the χ family, so none cites productLemma_holds '
             '(v0.18) or family_theorem (v0.21) -- each carried (reading R-9)' % len(chi))
    L += ['', '### PART E -- THE CEILING HITS IN SCOPE (the ceiling pattern of tools/b604_record.py, case as written), AGAINST b606`S 171:']
    acts = []
    for h in hits:
        act, why = _hit_action(h, rows)
        tag171 = (h['line'], h['hit']) in [(x[0], x[1]) for x in in171]
        acts.append(dict(h, act=act, why=why, in171=tag171))
        L.append('  :%d s%d "%s" -- %s -- %s%s' % (h['line'], h['seg'], h['hit'], act, why, ' -- one of the 171' if tag171 else ''))
    unread = [x for x in acts if x['act'] == 'UNREAD']
    L += ['  scope hits %d ; of b606`s 171 beyond, in scope %d ; rewritten away %d ; carried %d ; unread %d' % (
        len(hits), len(in171), sum(1 for x in acts if x['act'] == 'rewritten away'),
        sum(1 for x in acts if x['act'] != 'rewritten away' and x['act'] != 'UNREAD'), len(unread)),
        '  the 171 less this scope`s %d: %d, act three`s figure before the edition is counted' % (len(in171), len(b171) - len(in171))]
    L += ['', '### PART F -- RESTATEMENTS OUTSIDE THE SCOPE, PRICED FOR ACT THREE:']
    L += ['  :%d "%s" -- %s' % x for x in K.OUTSIDE]
    L += ['', '### PART G -- AN OBSERVATION FOR THE AUTHOR, NOT ACTED ON: §22.4`s fold criterion (:1376) runs from a fold to an off-line '
          'zero; the chain`s last link (:1398, :1400) reads the step from the absence of folds to the absence of off-line zeros, the '
          'converse direction. The seat reads it as part of the open edge and writes nothing beyond the ceiling clause`s marker (J08).']
    return L, dict(at=utc(), rows=rows, tmap=tmap, cite_resolves=resolves, chi=chi, hits=acts, in171=len(in171), b171=len(b171),
                   joins=len(joins), s273=len(s273))


# ================================================================================ COMPONENT 3: THE EDITION
BM_TAG = '<!-- b607 (R217) THE v5.15 EDITION`S BACK MATTER, 2026-10-03 -->'
VERSION = ('**v5.15, 2026-10-03** — CP-8 act two under `(R217)`: chapters 21 and 22, §24.4 and §27.3 read against the compiled faces, '
           'the doubling corollary and the sieve, beside v5.14, which stands unedited; every change is recorded in the back matter.  ')
READINGS = [
    ('R-1', 'the next version by the document`s own series is v5.15, written beside v5.14 as day1/A_Place_to_Stand_v5_15.md; its version '
            'line goes above v5.14`s'),
    ('R-2', 'the body of the H28b count is every line above the monograph`s own Correspondence heading; that section, v5.14`s back matter '
            'and this act`s are back matter, counted beside'),
    ('R-3', 'the scope is chapters 21 and 22 (v5.14 :1316-:1418), §24.4 (:1490-:1505) and §27.3 (:1788-:1820), read whole; Part IV`s '
            'preamble (:1291-:1314) and §24.1-§24.3 are outside it, act three`s, their restatements priced'),
    ('R-4', 'a join sentence is a sentence or a title of the monograph`s own argument that lets simplicity carry RH or RH carry simplicity; '
            'literature reports of published theorems (Montgomery, Gallagher-Mueller, Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh) are not '
            'joins of the programme`s argument and carry within the ceiling; "This direction is new" names the direction`s novelty and carries'),
    ('R-5', 'the ceiling clause reads every hit of the ceiling pattern in scope; a hit within the ceiling -- a published theorem`s "proved", '
            'a negated "proves", a compiled kernel fact, a Lean proof term, a general maxim -- carries with its reason; for the programme`s '
            'own argument the object is the reduction, the argument or the open direction'),
    ('R-6', 'the analytic-row note is a dated entry (2026-09-22): the history clause governs first, so the ruled SimpleProportion reading '
            'goes in a history line beneath it, not inside it'),
    ('R-7', 'the sieve column: each row`s verdict as THE_FINDINGS_AS_THEY_STAND v0.3 prints it, by row id and line; a row the sieve does '
            'not row says "no row at v0.3" and the seat supplies no verdict; a register whose falsifier stands in the bench is cited by the '
            'bench`s line'),
    ('R-8', '§27.3`s register sentences are E-2026-09-25-6`s replacements (with -1`s and -4`s), not -5`s, the navigator`s fact read as '
            'corrected; re-read against the pages and b538`s four depths, the depths sentence agrees, and the two sentences restating "one '
            'premise in five registers" take the restatement clause'),
    ('R-9', 'χ-side: no sentence in scope speaks of the χ family; the "missing family" of §24.4 and §27.3 is Katz-Sarnak`s ensemble for '
            'ξ, and Lagarias`s bound under GRH in §27.3`s ancestry a literature report; each carries'),
    ('R-10', 'the multi-act clause, (R217)(2): H28c and every bound on the whole body are scored on this act`s scope, the whole-document '
             'figure printed beside and handed to act three'),
    ('R-11', 'v5.14`s back matter is carried with its own-line cells re-pinned to this file; its v5.13, ERRATA and live-line numbers stand'),
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
    """### a v5.14 back-matter line with its own-line cells mapped to this file; its v5.13 and ERRATA numbers kept."""
    l = re.sub(r'(\*\*[A-Z0-9-]+\*\* :)(\d+)( \(v5\.13 :)', lambda m: m.group(1) + str(w[int(m.group(2))]) + m.group(3), l)
    l = re.sub(r'(with the history line at :)(\d+)', lambda m: m.group(1) + str(w[int(m.group(2))]), l)
    l = re.sub(r'(^- |and ):(\d+) beneath :(\d+)', lambda m: '%s:%d beneath :%d' % (m.group(1), w[int(m.group(2))], w[int(m.group(3))]), l)
    l = re.sub(r'^- :(\d+), carried-by-history', lambda m: '- :%d, carried-by-history' % w[int(m.group(1))], l)
    return l


def _build():
    """### the edition from v5.14`s blob by line transforms (carry / rewrite / re-pin / insert); returns the lines, the map and the record."""
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


def _act1_lines14():
    """### act one`s own lines in v5.14 numbering: the lines it rewrote, U09`s carry, its history lines and its version line."""
    E = json.loads(_show(RELAY, STEPZERO, 'data/b606_edition.json'))
    w13 = {int(k): v for k, v in E['where'].items()}
    s = set(w13[c['line']] for c in E['changes']) | set(E['hist'].values()) | {E['version'], w13[1562]}
    return s


COLLISIONS = [
    ('C1', 1337, 'U06 (act one`s ceiling rewrite, v5.14`s words) and J02, J03 (this act`s ceiling clause with (R217)(4)`s citations)',
     'J02 rewrites U06`s sentence by the ceiling clause again, its words kept and the ruled citations added; J03 is its own sentence'),
    ('C2', 1408, 'U07, U08 (act one) and J12, J13, J14 on one line', 'J12 adds the ruled citations to U08`s sentence; U07`s carries; J13 '
     'and J14 are their own sentences'),
    ('C3', 1500, 'the history clause (the dated analytic-row note) and (R217)(4)`s SimpleProportion reading', 'the history clause governs: '
     'the note carries unchanged and the reading goes in the history line beneath it (reading R-6)'),
    ('C4', 1504, 'E5-06 (act one`s erratum replacement, the geometric clause, STANDING) and T08 (the ceiling clause)', 'each applies to its '
     'own sentence: the canonical statement and "an open premise carried openly" stand; T08 rewrites the sentence naming Part III`s proof'),
    ('C5', 1798, 'E6-04 and U10 (act one) and S03 (the restatement clause)', 'each applies to its own sentence; S03 rewrites the sentence '
     'that restates what E6-04 corrected'),
    ('C6', 1819, 'E4-04 (act one`s erratum replacement) and S04 (the ceiling clause)', 'each applies to its own sentence'),
]


def _decl_cites(text):
    return [k for k in K.PINS if k in text]


def _bm(M, rows, w, out, repinned):
    """### this act`s back matter, appended after v5.14`s last line; every line it cites is the edition`s own."""
    W = _wl_data()
    L = ['', '---', '', BM_TAG, '', '## Back matter of v5.15 -- CP-8 act two, 2026-10-03, under `(R217)`', '',
         '*This section records every change v5.15 makes to v5.14, which stands beside it unedited; each line cited is this file’s own. '
         'v5.14’s back matter above is carried with its own-line cells re-pinned to this file (%d lines; reading R-11).*' % len(repinned), '',
         '### The act’s readings, each the seat’s and strikeable', '']
    L += ['- **%s** %s.' % (k, v.replace('`', '’')) for k, v in READINGS]
    L += ['', '### Chapters 21 and 22: the join sentences (relay `data/b607_worklist_PLACE.txt`, PART A)', '']
    for r in rows:
        if r['kind'] in ('join', 'ruled'):
            L.append('- **%s** :%d (v5.14 :%d) — %s — %s — was: “%s” — now: “%s” — cites: %s.' % (
                r['id'], w[r['line']], r['line'], r['clause'].replace('`', '’'), r['why'].replace('`', '’'), r['old'], r['new'], r['cites'].replace('`', '’')))
    for i, (n, frag, why) in enumerate(K.NOT_JOINS, 1):
        L.append('- **NJ%d** :%d (v5.14 :%d) — carried, not a join (reading R-4) — “%s” — %s.' % (i, w[n], n, frag, why.replace('`', '’')))
    for i, (n, why) in enumerate(K.STANDS, 1):
        if n < 1420:
            L.append('- **ST%d** :%d (v5.14 :%d) — stands — %s.' % (i, w[n], n, why.replace('`', '’')))
    L += ['', '### §24.4: the convergence table carrying the sieve’s verdicts, and the history line (PART B)', '']
    for r in rows:
        if r['kind'] == 'table' or r['id'] == 'T08':
            L.append('- **%s** :%d (v5.14 :%d) — %s — %s — was: “%s” — now: “%s” — cites: %s.' % (
                r['id'], w[r['line']], r['line'], r['clause'].replace('`', '’'), r['why'].replace('`', '’'), r['old'], r['new'], r['cites'].replace('`', '’')))
    L.append('- **H1** :%d beneath :%d (v5.14 :1500) — the history line under the dated analytic-row note — cites: %s.' % (
        w[1500] + 2, w[1500], K.HIST_CITE[1500].replace('`', '’')))
    L.append('- The sieve’s own row for the table, THE_FINDINGS_AS_THEY_STAND v0.3 :%d, cites the note at the current version’s :1499 '
             '(v5.13); here the note is :%d — %s.' % (K.SIEVE_CITE_LINE, w[1500], 'it resolves' if W.get('cite_resolves') else 'it does not resolve'))
    for i, (n, why) in enumerate(K.STANDS, 1):
        if 1490 <= n <= 1505:
            L.append('- **ST%d** :%d (v5.14 :%d) — stands — %s.' % (i, w[n], n, why.replace('`', '’')))
    L += ['', '### §27.3: the registers re-read at the pages’ pins and b538’s four depths (PART C)', '',
          '- The depths sentence (:%d, E6-04’s) agrees with the pages (ch_iff_rh, %s; h2_sign_iff_rh, %s) and with b538; not_register1 and '
          'register5_output_holds are not page nodes (SIDE-explicit-formula RegisterDepth.lean :60, :297 at 81ae175 and v0.21).' % (
              w[1798], K.PINS['ch_iff_rh'][2], K.PINS['h2_sign_iff_rh'][2])]
    for r in rows:
        if r['scope'] == '§27.3':
            L.append('- **%s** :%d (v5.14 :%d) — %s — %s — was: “%s” — now: “%s” — cites: %s.' % (
                r['id'], w[r['line']], r['line'], r['clause'].replace('`', '’'), r['why'].replace('`', '’'), r['old'], r['new'], r['cites'].replace('`', '’')))
    for i, (n, why) in enumerate(K.STANDS, 1):
        if n >= 1788:
            L.append('- **ST%d** :%d (v5.14 :%d) — stands — %s.' % (i, w[n], n, why.replace('`', '’')))
    L += ['', '### The scope’s ceiling hits, read (PART E)', '']
    for h in W.get('hits') or []:
        if h['act'] != 'rewritten away':
            L.append('- :%d (v5.14 :%d) “%s” — %s — %s.' % (w[h['line']], h['line'], h['hit'], h['act'], str(h['why']).replace('`', '’')))
    L.append('- Rewritten away: %s.' % ', '.join(':%d “%s” (%s)' % (w[h['line']], h['hit'], h['why']) for h in (W.get('hits') or []) if h['act'] == 'rewritten away'))
    L += ['', '### χ-side sentences (PART D)', '',
          '- None in scope speaks of the χ family (reading R-9): %s.' % '; '.join(':%d “%s…”' % (w[i], s[:60]) for i, s in (W.get('chi') or []))]
    L += ['', '### Collisions resolved by the precedence order (OPEN_TRAILS :12228) and the act’s readings', '']
    for cid, line, who, how in COLLISIONS:
        L.append('- **%s** :%d (v5.14 :%d) — %s — %s.' % (cid, w[line], line, who.replace('`', '’'), how.replace('`', '’')))
    L += ['', '### History lines', '', '- :%d beneath :%d: the analytic-row note’s, carrying `(R217)`(4)’s SimpleProportion reading.' % (w[1500] + 2, w[1500]),
          '', '### Removals', '', '- None: no sentence of v5.14 is removed.', '',
          '### Fact corrections', '', '- None in the text: the navigator’s “E-2026-09-25-5” for §27.3’s registers is read as E-2026-09-25-6 (reading R-8), a '
          'correction to the ruling’s letter, not to this file.', '',
          '### Stem corrections', '', '- None in scope: the body’s one live stem (:%d) is act three’s.' % w[721],
          '- :%d, carried-by-history — the era annotation of 2026-08-14 (v5.14 :2269, v5.13 :2264), carried as v5.14 carried it (its back '
          'matter above, reading R-4 there); listed again here because the scanner reads the exceptions of a file’s last back matter.' % w[2269], '',
          '### Placement', '', '| page | node this edition names | its pin as the page prints it | status |', '|:--|:--|:--|:--|']
    for k, (q, pin, where_) in K.PINS.items():
        L.append('| %s | `%s` | %s | named in v5.15, %s |' % (PAGE, q, pin, where_))
    L += ['', '### Correspondence', '', '| claim, as v5.15 states it | kernel | terminal | pin | status |', '|:--|:--|:--|:--|:--|',
          '| simplicity is the second located clause, a Prop beside the faces | SIDE-explicit-formula | `SIDEExplicitFormula.Simplicity.simplicity_iff` | v0.17 = 5a1630b | compiled; cited at J02, J06, J10, J12 |',
          '| within the schema Weil positivity does not imply simplicity | SIDE-explicit-formula | `SIDEExplicitFormula.Doubling.positivity_not_imp_simplicity` | v0.19 = 5fc0c87 | compiled; cited at J02, J06, J12 |',
          '| the two thirds is a named premise, not a compiled fact | SIDE-explicit-formula | `SIDEExplicitFormula.Simplicity.SimpleProportion` | v0.17 = 5a1630b | a named premise (structure); cited at L01 and the history line |',
          '| under the premise a dyadic window’s exceptional mass is at most a third plus ε | SIDE-explicit-formula | `SIDEExplicitFormula.Simplicity.exceptional_mass_le_third` | v0.17 = 5a1630b | compiled on the named premise; cited at the history line |',
          '| the second register is RH restated | SIDE-explicit-formula | `SIDEExplicitFormula.B321.ch_iff_rh` | v0.1 = baed4df | compiled; cited at S03 |',
          '| Weil positivity on classK is equivalent to RH | SIDE-explicit-formula | `SIDEExplicitFormula.B321.h2_sign_iff_rh` | v0.2 = 5c72cad | compiled; cited at S03 and T08 |',
          '', '### The whole-document figure handed to act three (the multi-act clause, `(R217)`(2))', '',
          '- {WHOLE}', '', '### Version history', '',
          '- v5.15, 2026-10-03 — CP-8 act two under `(R217)`: %d join sentences of chapters 21 and 22 under the ceiling clause, one ruled '
          'reading of Conrey’s figure, the convergence table’s sieve column (%d table lines), one history line under the dated note, %d ceiling '
          'and %d restatement corrections in §24.4 and §27.3; v5.14 unedited beside it.' % (
              sum(1 for r in rows if r['kind'] == 'join'), sum(1 for r in rows if r['kind'] == 'table'),
              sum(1 for r in rows if r['kind'] == 'ceiling'), sum(1 for r in rows if r['kind'] == 'restatement'))]
    return L


def _classify(ed, E):
    """### every ceiling hit of the edition by kind: record (after the Correspondence heading), scope (rewritten / carried / UNREAD),
    ### act one`s (the lines act one read, mapped), history, beyond."""
    w = {int(k): v for k, v in E['where'].items()}
    inv = {v: k for k, v in w.items()}
    ci = E['corr']
    a1 = set(w[n] for n in E['act1_lines14'])
    hist = set(E['hist'].values()) | {E['version']}
    hits = []
    for i, l in enumerate(ed, 1):
        src = inv.get(i)
        for k, s in enumerate(_segs(l)):
            for m in CEILING.finditer(s):
                if i >= ci:
                    kind = 'record'
                elif i in hist:
                    kind = 'history'
                elif src and K.in_scope(src):
                    carried = any(n == src and frag in s for n, frag, _w in K.CARRIES)
                    kind = 'scope, carried' if carried else 'scope, UNREAD'
                elif i in a1:
                    kind = 'act one`s'
                else:
                    kind = 'beyond (act three`s)'
                hits.append(dict(line=i, src=src, hit=m.group(0), kind=kind))
    return hits


def edition(*a):
    """### PLACE-papers day1/A_Place_to_Stand_v5_15.md beside v5.14 (unedited), from v5.14`s blob at 2988bfa and the work-list; the
    ### re-pin step last (`repin`). Writes the edition and data/b607_edition.json; `dry` writes both to the scratchpad instead."""
    dry = 'dry' in a
    if not dry and not os.path.exists(os.path.join(D, 'b607_worklist_PLACE.txt')):
        sys.exit('### THE WORK-LIST IS NOT BANKED -- NOTHING WRITTEN')
    M, rows, out, w, seg_d, repinned = _build()
    E = dict(where={str(k): v for k, v in w.items()}, version=19, hist={str(k): w[k] + 2 for k in K.HIST}, corr=_corr_idx(out) + 1,
             act1_lines14=sorted(_act1_lines14()))
    hits = _classify(out, E)
    whole = sum(1 for h in hits if h['kind'].startswith('beyond'))
    scan_live = None
    bm = _bm(M, rows, w, out, repinned)
    out2 = out + bm
    i_whole = out2.index('- {WHOLE}')
    out2[i_whole] = ('- Ceiling hits in the body beyond the sentences acts one and two read: %d (v5.14’s 171 less this scope’s %d); the '
                     'scanner’s one live stem at :%d. This is act three’s bound.' % (whole, _wl_data().get('in171', 0), w[721]))
    text = NL.join(out2) + NL
    b = text.encode('utf-8')
    ci, cm = _corr_idx(out2), _corr_idx(M)
    bm_at = out2.index(BM_TAG) + 1
    E.update(at=utc(), lines=len(out2), sha256=sha(b), bm=bm_at, changes=rows, seg_d=seg_d, repinned=repinned, whole=whole,
             n_body=_count(out2[:ci]), n_cur_body=_count(M[:cm]), n_backmatter=_count(out2[ci:]), n_cur_backmatter=_count(M[cm:]),
             n_full=_count(out2), credit=0, removals=0, history_lines=len(K.HIST), version_lines=1,
             cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(), scan_live=scan_live)
    if dry:
        p = os.path.join(SP, 'b607_edition_dry.md')
        open(p + '.tmp', 'wb').write(b)
        os.replace(p + '.tmp', p)
        json.dump(E, io.open(os.path.join(SP, 'b607_edition_dry.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('  DRY: %s ; %d lines ; body %d (v5.14 %d, %+d) ; back matter %d ; changes %d ; re-pinned %d ; whole %d' % (
            p, len(out2), E['n_body'], E['n_cur_body'], E['n_body'] - E['n_cur_body'], E['n_backmatter'], len(rows), len(repinned), whole))
        return
    dest = os.path.join(PP, *ED.split('/'))
    if os.path.exists(dest):
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    put_json('b607_edition.json', E)
    print('  %s ; %d lines ; sha256 %s ; body %d (v5.14 %d, %+d) ; back matter %d ; whole %d' % (
        ED, len(out2), E['sha256'][:16], E['n_body'], E['n_cur_body'], E['n_body'] - E['n_cur_body'], E['n_backmatter'], whole))


def termscan():
    """### the scanner (banned_terms.py --new) on the edition file, banked as data/b607_edition_termscan.txt."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', os.path.join(PP, *ED.split('/'))],
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b607_edition_termscan.txt', (r.stdout or '').rstrip(NL).split(NL))
    print([l for l in r.stdout.split(NL) if 'live uses' in l or 'VERDICT' in l or 'LIVE USE' in l])


def _ed():
    t = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read().replace(chr(13), '')
    return K.lines_of(t)


def carried(E, ed, M):
    """### every non-blank v5.14 line: carried verbatim at its mapped line, rewritten with every change recorded in the back matter,
    ### or (v5.14`s own back matter) re-pinned by the map."""
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
            good = ed[x - 1] == s and all(('was: “%s” — now: “%s”' % (c['old'], c['new'])) in bm for c in byl[n])
        elif n in rp:
            good = ed[x - 1] == _repin_line(M[n - 1], w) and ed[x - 1] != M[n - 1]
        else:
            good = ed[x - 1] == M[n - 1]
        ok += good
        if not good:
            bad.append(n)
    return ok, bad


def _scope_live(scan, E):
    """### the scanner`s live uses on the scope`s lines (this file`s numbering)."""
    w = {int(k): v for k, v in E['where'].items()}
    lines = set(w[n] for a, b, _t in K.SCOPE for n in range(a, b + 1)) | set(E['hist'].values())
    live = [int(m.group(1)) for m in re.finditer(r':(\d+)\s+### LIVE USE', scan)]
    return [n for n in live if n in lines], live


def edition_bank():
    """### The diff with its offset line, every change, the collisions, the counts, the ceiling read by kind, the scanner on scope and
    ### whole, H28a-H28c under the multi-act clause, H41a-H41d."""
    E = jl('b607_edition.json')
    W = jl('b607_worklist.json')
    ed = _ed()
    M = K.lines_of(_show(PP, PRE_PP, CUR))
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### THE EDITION ON DISK IS NOT THE BANKED ONE -- NOTHING WRITTEN')
    w = {int(k): v for k, v in E['where'].items()}
    scan = rd('b607_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    scope_live, all_live = _scope_live(scan, E)
    ok, bad = carried(E, ed, M)
    hits = _classify(ed, E)
    kinds = {k: sum(1 for h in hits if h['kind'] == k) for k in sorted(set(h['kind'] for h in hits))}
    unread = [h for h in hits if h['kind'] == 'scope, UNREAD']
    whole = sum(1 for h in hits if h['kind'].startswith('beyond'))
    bm = NL.join(ed[E['bm'] - 1:])
    h28a_rows = []
    for c in E['changes']:
        rec = ('was: “%s” — now: “%s”' % (c['old'], c['new'])) in bm
        h28a_rows.append(dict(id=c['id'], line=w[c['line']], cites=c['cites'], recorded=rec))
    h28a = 'HOLDS' if all(x['recorded'] and x['cites'] for x in h28a_rows) else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur_body']
    rw = sum(abs(x['d']) for x in E['seg_d'] if x['line'] < _corr_idx(M) + 1)
    allowed = E['credit'] + E['removals'] + E['history_lines'] + E['version_lines'] + rw
    strict = E['credit'] + E['removals'] + E['history_lines'] + E['version_lines']
    h28b = 'HOLDS' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if (not scope_live and not unread) else 'REFUTED'
    h28c_letter = 'HOLDS' if (clean and whole == 0) else 'REFUTED'
    joins = [c for c in E['changes'] if c['kind'] == 'join']
    # ### b582`s trap: a rewrite that appends keeps the old wording as a prefix (J01), so the old wording`s count is compared, not its absence
    joins_ok = [c['id'] for c in joins if ed[w[c['line']] - 1].count(c['new']) == 1
                and ed[w[c['line']] - 1].count(c['old']) == c['new'].count(c['old'])]
    h41a = 'HOLDS' if len(joins_ok) == len(joins) and joins else 'REFUTED'
    tmap = W.get('tmap') or []
    h41b = 'HOLDS' if tmap and all(t['ids'] and t['verdict'] for t in tmap) and W.get('cite_resolves') else 'REFUTED'
    s273 = [c for c in E['changes'] if c['scope'] == '§27.3']
    h41c = 'HOLDS' if len(s273) <= 2 else 'REFUTED'
    removed = W.get('in171', 0)
    h41d = 'HOLDS' if removed >= 40 else 'REFUTED'
    offs, last = [], None
    for n in range(1, len(M) + 1):
        o = w[n] - n
        if o != last:
            offs.append((n, o))
            last = o
    L = ['### OFFSET FROM v5.14 (R190)(3): %s -- the offset changes at each v5.14 line printed (v5.14 line, offset); every v5.14 line`s '
         'v5.15 line is printed below (the map), and every edition line cited here is the final file`s own.' % ', '.join('%+d from :%d' % (o, n) for n, o in offs), '',
         'b607 -- COMPONENT 3: THE MONOGRAPH`S NEXT VERSION, v5.15, (R217)(4), BY THE FORM OF (R187)(5), ITS CLAUSES, THE PRECEDENCE ORDER AND '
         'THE MULTI-ACT CLAUSE (R217)(2)', '',
         '### v5.14 : PLACE-papers %s @ %s (blob %s), %d lines, its head "%s"' % (CUR, PRE_PP, E['cur_blob'][:8], len(M), M[0]),
         '### v5.15 : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines'], E['sha256']), '',
         '### THE VERSION LINE, PRINTED: :%d %s' % (E['version'], ed[E['version'] - 1]), '',
         '### EVERY REWRITTEN SENTENCE (%d), WITH THE WORK-LIST LINE IT ANSWERS AND WHAT IT CITES:' % len(E['changes'])]
    for c in E['changes']:
        L += ['  %s  v5.14 :%d -> v5.15 :%d -- %s -- %s -- %s' % (c['id'], c['line'], w[c['line']], c['kind'], c['clause'], c['why']),
              '      was : %s' % c['old'], '      now : %s' % c['new'], '      cites: %s' % c['cites']]
    L += ['', '### THE HISTORY LINE (the history clause, reading R-6):']
    L += ['  :%s beneath v5.14 :%s (v5.15 :%d) : %s -- cites %s' % (v, k, w[int(k)], ed[v - 1][:240], K.HIST_CITE[int(k)]) for k, v in E['hist'].items()]
    L += ['', '### CARRIED IN SCOPE (each hit read, reading R-5), NOT JOINS (reading R-4) AND STANDING (the ruling):']
    L += ['  v5.14 :%d -> :%d "%s" -- %s' % (n, w[n], f, why) for n, f, why in K.CARRIES]
    L += ['  v5.14 :%d -> :%d "%s" -- not a join: %s' % (n, w[n], f, why) for n, f, why in K.NOT_JOINS]
    L += ['  v5.14 :%d -> :%d -- stands: %s' % (n, w[n], why) for n, why in K.STANDS]
    L += ['', '### COLLISIONS, BOTH WORDINGS IN THE WORK-LIST BANK AND THE BACK MATTER:']
    L += ['  %s v5.14 :%d -- %s -- %s' % c for c in COLLISIONS]
    L += ['', '### SEGMENT CHANGES ON REWRITTEN LINES (b558 segments): %s' % [(x['line'], x['ids'], x['d']) for x in E['seg_d'] if x['d']] or 'none',
          '### v5.14`S BACK MATTER RE-PINNED: %d lines (reading R-11): %s' % (len(E['repinned']), E['repinned']), '',
          '### EVERY NON-BLANK v5.14 LINE -> ITS v5.15 LINE (%d carried verbatim, rewritten with every change recorded, or re-pinned ; '
          'failing %s):' % (ok, bad or 'none')]
    L += ['  :%s -> :%d' % (n, x) for n, x in sorted(w.items())]
    L += ['', '### THE COUNTS (relay tools/b558_record.py `segments`, imported): v5.14`s BODY %d ; v5.15`s BODY %d (%+d) ; the BACK MATTER %d '
          '(v5.14`s %d, the Correspondence onward, and this act`s), printed separately ; the edition whole %d' % (
              E['n_cur_body'], E['n_body'], body_dn, E['n_backmatter'], E['n_cur_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + the history line the ruling`s reading takes %d + '
          'one version line %d + rewritten lines` segment changes %d = %d ; the strict count %d' % (
              body_dn, E['credit'], E['removals'], E['history_lines'], E['version_lines'], rw, allowed, strict), '',
          '### THE CEILING, every hit in the edition, by kind: %s' % kinds]
    L += ['    :%d (v5.14 :%s) "%s" -- %s' % (h['line'], h['src'], h['hit'], h['kind']) for h in hits]
    L += ['### THE SCANNER (banned_terms.py --new) on the edition: on scope, live uses %d %s ; whole, live uses %s at %s, verdict %s' % (
        len(scope_live), scope_live, live.group(1) if live else None, all_live, 'CLEAN' if clean else 'NOT CLEAN'),
        '### THE WHOLE-DOCUMENT FIGURE, HANDED TO ACT THREE: %d ceiling hits beyond the sentences acts one and two read, and %s live stem(s) '
        '(the scanner) -- b606 handed 171 and 1; this scope held %d of the 171' % (whole, len(all_live), removed), '',
        '### H28a: rewritten sentences %d ; each recorded with both wordings %d ; each citing a declaration, a page line, a sieve row or a '
        'bank line %d' % (len(h28a_rows), sum(x['recorded'] for x in h28a_rows), sum(1 for x in h28a_rows if x['cites'])),
        '### the joins: %d, rewritten in the edition %d %s' % (len(joins), len(joins_ok), joins_ok),
        '### the table: %s ; the sieve`s own citation resolves %s' % ([(t['row'], t['ids'], t['verdict']) for t in tmap], W.get('cite_resolves')), '',
        '### ### **H28a %s -- every MOVED-IN-MEANING sentence (%d) recorded with both wordings and citing what it rests on.**' % (h28a, len(h28a_rows)),
        '### ### **H28b %s -- the body differs by %+d sentences against at most %d (strict %d); the back matter %d, excluded and printed.**' % (
            h28b, body_dn, allowed, strict, E['n_backmatter']),
        '### ### **H28c %s ON SCOPE under the multi-act clause -- the scanner`s live uses on the scope %d, the scope`s hits unread %d; WHOLE '
        'printed beside: %s (the scanner %s, %d live; beyond the read sentences %d).**' % (
            h28c, len(scope_live), len(unread), h28c_letter, 'CLEAN' if clean else 'NOT CLEAN', len(all_live), whole),
        '### ### **H41a %s -- the join sentences of chapters 21-22: %d, every one rewritten under the ceiling clause, none held.**' % (h41a, len(joins)),
        '### ### **H41b %s -- §24.4`s table: %d rows, %d carrying a sieve verdict, %d with a sieve row; the sieve`s own row for the table '
        'resolves %s.**' % (h41b, len(tmap), sum(1 for t in tmap if t['verdict']), sum(1 for t in tmap if t['ids']), W.get('cite_resolves')),
        '### ### **H41c %s -- §27.3 takes %d further corrections after act one`s errata (bound 2).**' % (h41c, len(s273)),
        '### ### **H41d %s -- the scope holds %d of b606`s 171 (bound 40), every one read; %d hits remain beyond, act three`s figure.**' % (
            h41d, removed, whole),
        '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b607_edition_PLACE.txt', L)
    put_json('b607_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, H28c_letter=h28c_letter, H41a=h41a, H41b=h41b, H41c=h41c, H41d=h41d,
                                   h28a_rows=h28a_rows, body_dn=body_dn, allowed=allowed, strict=strict, rw=rw, backmatter=E['n_backmatter'],
                                   live=int(live.group(1)) if live else None, scope_live=scope_live, clean=clean, unread=len(unread),
                                   whole=whole, removed=removed, kinds=kinds, hits=hits, carried_ok=ok, carried_bad=bad, joins=len(joins),
                                   joins_ok=joins_ok, s273=len(s273), held=None))
    print('H28a %s H28b %s H28c %s (letter %s) H41a %s H41b %s H41c %s H41d %s ; carried %d bad %s ; body_dn %d allowed %d strict %d ; '
          'whole %d ; unread %d ; scope live %s' % (h28a, h28b, h28c, h28c_letter, h41a, h41b, h41c, h41d, ok, bad, body_dn, allowed, strict,
                                                    whole, len(unread), scope_live))


def repin():
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932). Writes data/b607_repin.txt."""
    E = jl('b607_edition.json')
    ed = _ed()
    M = K.lines_of(_show(PP, PRE_PP, CUR))
    w = {int(k): v for k, v in E['where'].items()}
    bml = ed[E['bm'] - 1:]
    bm = NL.join(bml)
    checks = []
    for m in re.finditer(r'^- \*\*([A-Z0-9-]+)\*\* :(\d+) \(v5\.14 :(\d+)\)', bm, re.M):
        i, a_, b_ = m.group(1), int(m.group(2)), int(m.group(3))
        checks.append(('back matter %s cites :%d for v5.14 :%d' % (i, a_, b_), w.get(b_) == a_ and bool(ed[a_ - 1].strip())))
    for m in re.finditer(r'^- :(\d+) \(v5\.14 :(\d+)\) “([^”]+)”', bm, re.M):
        a_, b_, hit = int(m.group(1)), int(m.group(2)), m.group(3)
        checks.append(('the read hit :%d “%s” for v5.14 :%d' % (a_, hit, b_), w.get(b_) == a_ and hit in ed[a_ - 1]))
    for c in E['changes']:
        a_ = w[c['line']]
        checks.append(('%s`s new sentence on :%d' % (c['id'], a_), ed[a_ - 1].count(c['new']) == 1))
    for k, v in E['hist'].items():
        checks.append(('history line :%d beneath :%s' % (v, k), ed[v - 1] == K.HIST[int(k)] and ed[v - 2] == '' and w[int(k)] == v - 2))
    for cid, line, _w, _h in COLLISIONS:
        checks.append(('collision %s at :%d' % (cid, w[line]), ('**%s** :%d (v5.14 :%d)' % (cid, w[line], line)) in bm))
    b6 = M.index(B606_TAG) + 1
    for n in E['repinned']:
        checks.append(('v5.14`s back matter :%d re-pinned at :%d' % (n, w[n]), n >= b6 and ed[w[n] - 1] == _repin_line(M[n - 1], w)))
    for n in range(b6, len(M) + 1):
        for m in re.finditer(r'\*\*[A-Z0-9-]+\*\* :(\d+) \(v5\.13 :(\d+)\)', ed[w[n] - 1]):
            a_ = int(m.group(1))
            src = {v: k for k, v in w.items()}.get(a_)
            checks.append(('carried row at :%d cites :%d' % (w[n], a_), bool(src) and bool(ed[a_ - 1].strip())))
    checks.append(('the version line on :%d above v5.14`s' % E['version'], ed[E['version'] - 1] == VERSION and ed[E['version']] == M[18]
                   and M[18].startswith('**v5.14, 2026-10-03**') and ed[E['version'] + 1] == '**v5.13, 2026-07-27**'))
    checks.append(('the Correspondence heading on :%d' % E['corr'], ed[E['corr'] - 1].startswith(CORR_HEAD)))
    checks.append(('the back-matter tag on :%d' % E['bm'], ed[E['bm'] - 1] == BM_TAG))
    checks.append(('act one`s tag carried on :%d' % w[b6], ed[w[b6] - 1] == B606_TAG))
    bank = rd('b607_edition_PLACE.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM v5.14') and bank.count('### OFFSET FROM') == 1))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and hashlib.sha256(open(os.path.join(PP, *ED.split('/')), 'rb').read()).hexdigest() == E['sha256']))
    for m in re.finditer(r'v5\.14 :(\d+) -> v5\.15 :(\d+)', bank):
        b_, a_ = int(m.group(1)), int(m.group(2))
        checks.append(('the diff bank`s v5.14 :%d -> v5.15 :%d' % (b_, a_), w.get(b_) == a_))
    L = ['### b607 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % ED, '']
    L += ['    %-100s %s' % (x[:100], 'OK' if ok else '### FAILS') for x, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _x, ok in checks), len(checks))]
    put_txt('b607_repin.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 4: THE PAGES
def page(k):
    """### after the edition commit: ONE page per call in the foreground, re-emitted from its banked probe (the ζ page from b602's list
    ### at v0.20, the χ page from b603's at v0.21; no Lean call). Writes the page only when it changed, and data/b607_page_<k>.json."""
    import chain_page as C
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b607_%s' % k)
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
        put_json('b607_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
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
    put_json('b607_page_%s.json' % k, J)
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s ; the probe read %s' % (k, rc, len(b), changed, secs, src_out))
    for x in dl[:60]:
        print('    ' + x[:240])


def page_arms(tag):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b607 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    L.append('### the lists read: %s' % {k: (NODES[k], PROBE[k]) for k in NODES})
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b607_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b607_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
SCORE_KEYS = ('H28a', 'H28b', 'H28c', 'H41a', 'H41b', 'H41c', 'H41d', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')


def _elines(ej):
    return ', :'.join(str(x) for x in (ej.get('lines') or []))


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def scores():
    WJ, H, E = jl('b607_worklist.json'), jl('b607_h28.json'), jl('b607_edition.json')
    Z, X = jl('b607_page_zeta.json'), jl('b607_page_chi.json')
    rp = rd('b607_repin.txt')
    tmap = WJ.get('tmap') or []
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
                                                                               'SIDE-structural-error-correction', 'SIDE-cosmo', 'SIDE-silence-principle',
                                                                               'SIDE-global-section')}
    kern_ok = kern == {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068',
                       'SIDE-structural-error-correction': '6a4f482', 'SIDE-cosmo': 'c5cba30', 'SIDE-silence-principle': '667c254',
                       'SIDE-global-section': '3528bcf'}
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1').split(NL) if x.startswith('?? ')))
    trail_landed = os.path.exists(os.path.join(D, 'b607_trail.json'))
    want_pp = sorted(['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', ED] + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = all(g(PP, 'rev-parse', 'HEAD:' + p).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, p)).strip()
                   and not g(PP, 'status', '--porcelain', '--', p).strip() for p in (CUR, ORIG))
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b607_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b606_closing_push_out.txt'))
    m = re.search(r'RE-PIN : (\d+) of (\d+)', rp)
    arms2 = rd('b607_page_arms_c2.txt')
    joins = WJ.get('joins', 0)
    ed = _ed() if os.path.exists(os.path.join(PP, *ED.split('/'))) else []
    bmt = NL.join(ed[E['bm'] - 1:]) if ed and E else ''
    carried_listed = [h for h in (WJ.get('hits') or []) if h['act'] != 'rewritten away' and ('“%s” — %s' % (h['hit'], h['act'])) not in bmt]
    S = dict(
        H28a=(H.get('H28a'), 'every MOVED-IN-MEANING sentence (%d) recorded with both wordings and citing what it rests on: %d' % (
            len(H.get('h28a_rows') or []), sum(1 for x in H.get('h28a_rows') or [] if x['recorded'] and x['cites']))),
        H28b=(H.get('H28b'), 'the body differs by %+d against at most %d (strict %d)' % (H.get('body_dn', 0), H.get('allowed', 0), H.get('strict', 0))),
        H28c=(H.get('H28c'), 'ON SCOPE under the multi-act clause: the scanner`s live uses on the scope %s, unread %s; WHOLE printed beside: %s '
                             '(%s live stem; %s hits beyond the read sentences, act three`s figure)' % (
                                 H.get('scope_live'), H.get('unread'), H.get('H28c_letter'), H.get('live'), H.get('whole'))),
        H41a=(H.get('H41a'), 'join sentences %s, rewritten %s, none held' % (H.get('joins'), len(H.get('joins_ok') or []))),
        H41b=(H.get('H41b'), 'rows %d ; with a verdict %d ; with a sieve row %d ; the sieve`s own row for the table resolves %s' % (
            len(tmap), sum(1 for t in tmap if t['verdict']), sum(1 for t in tmap if t['ids']), WJ.get('cite_resolves'))),
        H41c=(H.get('H41c'), '§27.3`s further corrections %s (bound 2)' % H.get('s273')),
        H41d=(H.get('H41d'), 'the scope held %s of the 171 (bound 40), each read; %s remain, act three`s' % (H.get('removed'), H.get('whole'))),
        N1=('HELD' if joins >= 6 and H.get('H41a') == 'HOLDS' else 'REFUTED', 'join sentences in chapters 21-22: %d, each under the ceiling clause' % joins),
        N2=('HELD' if len(tmap) == 5 and all(len(t['ids']) == 1 for t in tmap) else 'REFUTED',
            'rows %d ; each row`s sieve rows: %s' % (len(tmap), [(t['row'], t['ids']) for t in tmap])),
        N3=('HELD' if (H.get('s273') or 0) <= 2 else 'REFUTED', '§27.3 corrections beyond act one`s: %s' % H.get('s273')),
        N4=('HELD' if (H.get('removed') or 0) >= 40 and all(H.get(k) == 'HOLDS' for k in ('H28a', 'H28b', 'H28c')) else 'REFUTED',
            'removed of the 171: %s (bound 40) ; H28a %s, H28b %s, H28c %s on scope' % (H.get('removed'), H.get('H28a'), H.get('H28b'), H.get('H28c'))),
        N5=('HELD' if kern_ok and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
            'nothing deposits; every kernel`s main unmoved %s; v5.14 and v5.13 unedited %s; PLACE-papers %s (wanted %s); relay files beyond '
            'the act`s banks, tools and the table %s%s' % (kern_ok, cur_same, pp_ch, want_pp, relay_beyond, '' if trail_landed else ' ; the trail record pending')),
        S1=('HELD' if m and m.group(1) == m.group(2) else 'REFUTED', 'the re-pin step: %s' % (m.group(0) if m else 'no bank')),
        S2=('HELD' if not H.get('carried_bad') else 'REFUTED', 'every non-blank v5.14 line carried verbatim, rewritten with every change '
                                                              'recorded, or re-pinned: %d ; failing %s' % (H.get('carried_ok', 0), H.get('carried_bad'))),
        S3=('HELD' if H.get('unread') == 0 and not carried_listed else 'REFUTED', 'the scope`s hits unread %s ; carried hits missing from the '
            'back matter %s' % (H.get('unread'), [(h['line'], h['hit']) for h in carried_listed] or 'none')),
        S4=('HELD' if Z.get('changed') is True and X.get('changed') is True else 'REFUTED', 'the ζ page changed %s ; the χ page changed %s' % (
            Z.get('changed'), X.get('changed'))),
        S5=('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
            'after the page commits: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    )
    put_json('b607_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-6s %s -- %s' % (k, S[k][0], str(S[k][1])[:220]))


TITLE = ('## CP-8, act two: the monograph’s v5.15 over chapters 21–22, §24.4 and §27.3 — simplicity as the second located clause, the '
         'convergence table carrying the sieve’s verdicts where the sieve rows them, the registers re-read at the pages’ pins')
TRAIL_HEAD = ('### b607 — lane three, act thirty-four under (R217): CP-8 act two -- chapters 21 and 22, §24.4 and §27.3 of the monograph '
              'read against the compiled faces, the doubling corollary and the sieve')


def _finding_text():
    S, WJ, H, E = jl('b607_scores.json'), jl('b607_worklist.json'), jl('b607_h28.json'), jl('b607_edition.json')
    rl, ej = jl('b607_record_lines.json'), jl('b607_errata.json')
    w1, w2, mc = [x['line'] for x in rl['lines']]
    ec = _pp_commit('b607 (R217)(4): ' + ED)
    zc, xc = _pp_commit('b607 (R217)(4): ' + PAGE), _pp_commit('b607 (R217)(4): ' + DIR_PAGE)
    erc = _pp_commit('b607 (R217)(3): ERRATA.md')
    tmap = WJ.get('tmap') or []
    rows = E['changes']
    e = ['', TITLE, '',
         '*Filed at b607 on the author’s ruling `(R217)`. Banks: relay `data/b607_reads.txt`, `data/b607_worklist_PLACE.txt`, '
         '`data/b607_edition_PLACE.txt`, `data/b607_edition_termscan.txt`, `data/b607_repin.txt`, `data/b607_page_zeta.json`, '
         '`data/b607_page_chi.json`, `data/b607_page_arms_c2.txt`, `data/b607_errata.json`. Nothing deposits.*', '',
         '**The edition** (`(R217)`(4)). PLACE-papers `%s` (commit %s), the monograph’s v5.15 beside v5.14, unedited; %d join sentences of '
         'chapters 21 and 22 under the ceiling clause, simplicity named the second located clause (simplicity_iff, v0.17) beside the '
         'doubling corollary’s non-implication (positivity_not_imp_simplicity, v0.19) and the b596 walk (0 of 117), the '
         'perpendicular-crossing theorem standing with its pin; Conrey’s figure read with the analytic-row note, and the two thirds named '
         'the premise SimpleProportion with its upstream line in a history line beneath the dated note; §24.4’s table carrying a sieve '
         'column, %d of its %d rows with a sieve row; %d corrections in §24.4 and §27.3, the registers re-read at the pages’ pins and '
         'b538’s four depths, “convergent, not independent” carried. The back matter records every change with both wordings, every scope '
         'hit read, the collisions C1-C6, the Placement and the Correspondence.' % (
             ED, ec, sum(1 for r in rows if r['kind'] == 'join'), sum(1 for t in tmap if t['ids']), len(tmap),
             sum(1 for r in rows if r['kind'] in ('ceiling', 'restatement'))), '',
         '**The work-list** (`(R217)`(4), relay `data/b607_worklist_PLACE.txt`, banked before the writing): the joins of chapters 21-22 by '
         'line; the table’s rows against THE_FINDINGS_AS_THEY_STAND v0.3 by row -- the 0.6725 ceiling RH-16 (DARK, test 1), the GUE '
         'register in the bench (DARK, test 1, no row), the Epstein witnesses FD-01 and FD-02 (NOT A ROUTE), the computational range and '
         'the mechanism enumeration with no row; §27.3’s residue; no χ-side sentence in scope; the scope’s %d ceiling hits, %d of b606’s '
         '171.' % (len(WJ.get('hits') or []), WJ.get('in171', 0)), '',
         '**The multi-act clause and the pointer rule.** The clause at OPEN_TRAILS :%d, addressed to the form’s block :11864, and b606’s '
         'weight at FINDINGS :%d re-reading its H28c, H40c and N4 under it (HELD on scope, REFUTED in letter); ERRATA’s pointer rule and '
         'the two dated appends to E-2026-09-25-1 and E-2026-09-22-1 at ERRATA :%s, committed alone as housekeeping (%s).' % (
             mc, w1, _elines(ej), erc), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '. H28c holds on scope under the multi-act clause, '
         'the whole-document figure printed beside it: %s ceiling hits beyond the read sentences and %s live stem, act three’s bound. H41b '
         'and N2 refuted by the table: two rows have no sieve row and the Epstein row has two; H41c and N3 refuted: §27.3 took %s further '
         'corrections; H41d and N4 refuted: the scope held %s of the 171.' % (H.get('whole'), H.get('live'), H.get('s273'), H.get('removed')), '',
         '**The pages.** Both re-emitted after the edition commit from their banked probes, no Lean call: the ζ page (PLACE-papers %s) and '
         'the χ page (%s), each committed alone, the edition entering their Placement.' % (zc, xc), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the edition carries into the monograph the walk of b596 (FINDINGS :6856), the '
         'doubling corollary of b601 (:6972), the sieve’s verdicts of b605 (:7084) and act one’s v5.14 (:7108), and E-2026-09-25-6’s '
         'register depths (b543); it is re-read in turn by CP-8’s act three, which takes the whole-document figure as its bound. It '
         'strengthens the programme’s offering of the monograph: Part IV now names simplicity as the second located clause the kernel '
         'carries and its argument as an open direction, and §24.4’s evidence table says which of its lines the sieve rows and how.', '',
         '**The record lines.** b606’s weight at FINDINGS :%d; the two fact corrections, the navigator’s, at :%d; the multi-act clause at '
         'OPEN_TRAILS :%d.' % (w1, w2, mc), '',
         '**Next.** Per `(R217)`(5): b608, CP-8 act three -- the remaining chapters by the b558 work-list where one exists and by the '
         'ceiling and stem clauses otherwise, §25.8 re-pinned, the whole-document figure as its bound. The author rules on the closing.', '',
         '*Nothing deposits; no keystone edited beyond the edition written beside its prior version; README and REGISTRY unwritten; '
         'nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    return TITLE, NL.join(e)


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
    put_json('b607_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def _three_price():
    E = jl('b607_edition.json')
    w = {int(k): v for k, v in E['where'].items()}
    b558 = _show(RELAY, STEPZERO, 'data/b558_editions/A_Place_to_Stand.txt') or ''
    n558 = len(re.findall(r'^:\d+ -- ', b558, re.M))
    return ('act three’s work-list, priced from what this act found, by v5.15’s lines: the whole-document figure, %s ceiling hits beyond '
            'the sentences acts one and two read and the one live stem (:%d), as its bound; the b558 work-list for the monograph (relay '
            '`data/b558_editions/A_Place_to_Stand.txt`, %d rows); the restatements outside act two’s scope -- Part IV’s preamble (:%d, '
            ':%d, :%d, :%d: “the conditional (simplicity → RH) is proved”, “We establish it here”, the theorem stated in ZFC) and '
            'Chapter 24’s opening (:%d) and title; §25.8’s Kernel Concordance re-pinned' % (
                E.get('whole'), w[721], n558, w[1304], w[1306], w[1308], w[1310], w[1464]))


def _trail_text():
    S, fj, rl, ej = jl('b607_scores.json'), jl('b607_findings.json'), jl('b607_record_lines.json'), jl('b607_errata.json')
    H = jl('b607_h28.json')
    w1, w2, mc = [x['line'] for x in rl['lines']]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R217) ratified.** (1) b606 at its weight, its three letter-refutations re-read under (2). (2) The multi-act clause. (3) '
             'ERRATA’s pointer rule. (4) CP-8 act two: chapters 21 and 22, §24.4 and §27.3; H41a-H41d. (5) The act after: b608, CP-8 act '
             'three.', '',
             '**Entered:** FINDINGS.md:%d (b606’s weight), :%d (the two fact corrections), :%d (the entry, with its mutual-light line); '
             'OPEN_TRAILS :%d (the multi-act clause, addressed to :11864); ERRATA.md :%s (the pointer rule and the two dated appends, '
             'committed alone); this record; PLACE-papers `%s` (v5.15, beside v5.14, unedited); both pages re-emitted.' % (
                 w1, w2, fj['entry_line'], mc, _elines(ej), ED), '',
             '**Resolved by the seat, for the author’s strike:** readings R-1 to R-11 of the edition’s back matter -- v5.15 by the series, '
             'the body above the Correspondence, the scope read whole, a join defined as the programme’s own argument (literature '
             'conditionals and “This direction is new” carried), every scope hit read, the dated analytic-row note taking a history line, '
             'the sieve column naming no verdict where the sieve has no row, §27.3’s registers read as E-2026-09-25-6’s, no χ-side sentence '
             'in scope, the multi-act clause, v5.14’s back matter re-pinned; the collisions C1-C6; ERRATA’s three lines appended at the '
             'ledger’s end, each addressed to its entry, so that no ERRATA line the editions cite moves. No prompt was put (relay '
             'data/b607_author_answers.txt).', '',
             '**For the author:** H41b and N2 refuted by the table -- the computational range and the mechanism enumeration have no sieve '
             'row, GUE’s register stands in the bench, and the Epstein row maps to two rows; H41c and N3 refuted -- §27.3 took %s further '
             'corrections (the present proof, the proof’s own foundation, and the two sentences restating one premise in five registers); '
             'H41d and N4 refuted -- the scope held %s of b606’s 171. A fact correction, the navigator’s: §27.3’s registers stand as '
             'E-2026-09-25-6’s replacements left them, not -5’s. An observation, not acted on: §22.4’s fold criterion runs from a fold to an '
             'off-line zero, and the chain’s last link reads the converse step; the seat marked it as part of the open direction and wrote '
             'nothing more.' % (H.get('s273'), H.get('removed')), '',
             '**Act three, priced:** %s.' % _three_price(), '',
             '**Defects** (relay data/b607_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R217)`(5), b608, CP-8 act three; the author rules on the closing.', '',
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
    put_json('b607_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b607_trail.json')['line'])


def desk():
    S = jl('b607_scores.json')
    HK = ('H28a', 'H28b', 'H28c', 'H41a', 'H41b', 'H41c', 'H41d')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b607 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H28a-H28c (under the multi-act clause) and H41a-H41d, (R217)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HK]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H28/H41 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HK), sum(S[k][0] == 'REFUTED' for k in HK),
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b607_defects.txt').rstrip(NL).split(NL)
    put_txt('b607_desk_notes.txt', L)


def components():
    S, fj, tj, rl, ej = jl('b607_scores.json'), jl('b607_findings.json'), jl('b607_trail.json'), jl('b607_record_lines.json'), jl('b607_errata.json')
    Z, X = jl('b607_page_zeta.json'), jl('b607_page_chi.json')
    L = ['b607 -- THE COMPONENTS, BANKED UNDER (R217).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b606`s closing push-out relay %s ; push-b606* branches deleted by '
         'name (data/b607_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b607_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b606`s weight FINDINGS :%d ; the fact corrections :%d ; the multi-act clause OPEN_TRAILS :%d ; ERRATA :%s (the '
         'pointer rule and the two appends, committed alone)' % (tuple(x['line'] for x in rl['lines']) + (_elines(ej),)),
         '### COMPONENT 2 : the work-list data/b607_worklist_PLACE.txt',
         '### COMPONENT 3 : the edition %s ; the diff data/b607_edition_PLACE.txt ; H28a %s, H28b %s, H28c %s ; H41a %s, H41b %s, H41c %s, H41d %s' % (
             ED, S['H28a'][0], S['H28b'][0], S['H28c'][0], S['H41a'][0], S['H41b'][0], S['H41c'][0], S['H41d'][0]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b607_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b608, CP-8 act three ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b607_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b607_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
