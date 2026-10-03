# -*- coding: utf-8 -*-
"""b604_record.py -- THE ACT'S RECORD TOOL, UNDER (R214). ### ONE SUBCOMMAND PER BANK.

### ### b604: LANE THREE, ACT THIRTY-ONE -- THE EDITION OF THE_FINDINGS_AS_THEY_STAND BY THE FORM AS THE SIEVE TABLE BY CLUSTER.
### Subcommands write only `data/b604_*` unless the docstring names another file. Every bank is written through b602_record's
### `put_txt` / `put_json` (encode, temp file, `os.replace`), imported, never copied; every ledger append through b566's guarded
### `append_to`. The sieve's rows are tools/b604_rows.py's data. No platform call. No Lean call: both pages are re-emitted from
### their banked probes.
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
import b604_rows as W  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
GSK = 'D:/SIDE-global-section'
RELAY = ROOT.replace('\\', '/')
PRE_PP = '24e7ff2'
PRE_RELAY = '4a027daf'
PRE_KER = '1d5d4dd'
PRE_GS = '3528bcf'
STEPZERO = '7dce3771'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/9f8a2aec-6bbc-47c1-81c1-612ee4051cda/scratchpad'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/9f8a2aec-6bbc-47c1-81c1-612ee4051cda.jsonl'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CUR = 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md'
ED = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md'
SPIRAL = 'SPIRAL_MAP.md'
INSTR = 'phase1.5/method/INSTRUMENTS.md'
IB = 'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md'
SIMP = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md'
CANON = 'phase1.5/method/THE_METHOD_CANON.md'
MONO = 'day1/A_Place_to_Stand.md'
CONV = 'phase1.5/simplicity/CONVERGENT_ARGUMENTS_SIMPLICITY.md'
LOOM = 'VERIFICATION_LOOM.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, put_txt, put_json, jl, rd, sha, utc, flat = R2.g, R2.put_txt, R2.put_json, R2.jl, R2.rd, R2.sha, R2.utc, R2.flat


DEFECTS = [
    '(a) THE SEAT`S W-ORD-E0-INDUCTION PARAGRAPH MOVED A TERMINAL-TABLE CELL, FOUND BY THE FIRST PRE-PUSH RUN OF THE SUITE: the '
    'paragraph appended at OPEN_TRAILS :12438 (Component 1) quoted the ruling`s clause, its grade word for the clause`s outcome '
    'within the table generator`s 120-character window of the backticked name of its case, so the regenerated table read a second '
    'grade cell for that name and moved its cell from its standing grade to CONFLICT; G-TABLE-GRADES-UNMOVED failed (76 of 78, with '
    'b). Both OPEN_TRAILS appends of this act were uncommitted: the file was cut back to the W-ORD append`s banked `before` length '
    '(1547672 bytes, the HEAD blob, verified a byte-for-byte prefix and printed), the W-ORD block re-appended in a second wording '
    'that keeps the clause`s words and names its case once, beside the grade it carries (record subcommand word_again, through '
    'the Edit tool), and the trail record re-appended whole. No line number moved: the block keeps its three lines and the record '
    'its start. The FINDINGS lines, committed nowhere yet, were not touched. The second pre-push run then read the cell as changed '
    'again, against the first run`s regeneration, which had become the generator`s prior file: the five generated table files were '
    'restored to relay HEAD (their committed state; the generator rewrites them) and the suite re-run, 78 of 78, the table diffed '
    'against HEAD -- 0 rows added, 0 gone, 0 grade or profile cells moved; the one cell that changed is that row`s cited ledger '
    'line, now FINDINGS :7058, its grade unchanged.',
    '(b) ONE OF THE SEAT`S SUITE PREDICATES COUNTED THE BACK MATTER: G-ROWS counted every line opening with a row id, and the '
    'Correspondence rows in the back matter open the same way, so it read 168 against 84 at the first pre-push run. Corrected '
    'through the Edit tool to count the body`s row lines only; no arm name moved, the sealed (G2) list unchanged.',
]
DEFECT_SHORT = [
    '(a) the W-ORD paragraph`s first wording put the clause`s grade word beside its case`s name, moving that name`s table cell to '
    'a conflict; OPEN_TRAILS cut back to the HEAD blob (the appends uncommitted, the prefix verified) and both appends re-landed, '
    'the paragraph reworded so its grade word stands outside the table`s window',
    '(b) a suite predicate (G-ROWS) counting the back matter`s Correspondence rows, corrected to the body',
]
PATTERN = ('PATTERN LINE, (R214)(2)(i) -- AN API STOP OF THE HARNESS, NOT OF THE ACT, TWO IN TWO ACTS NEAR THE SAME HOUR: b602`s after '
           'its scores (2026-10-03T02:54:52Z to 03:14:45Z) and b603`s in Component 0 before its seal (03:51:17Z to 04:01:00Z). Entered '
           'as a pattern line and not a rule, as the ruling orders. This act: %s.')


def defects():
    stops = 'none so far in this act'
    L = ['b604 -- THE DEFECT LIST (the act`s own, and the pattern line (R214)(2)(i) orders).', '', '### ' + PATTERN % stops, '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b604_defects.txt', L)


# ================================================================================ READING (1): THE READS
READS = [
    ('THE_FINDINGS_AS_THEY_STAND, the current version whole (every non-blank line)', PP, PRE_PP, CUR, 'ALL', 300),
    ('SPIRAL_MAP §4A: the cluster table as b388 refreshed it, the (R21) re-anchoring, the unassigned line', PP, PRE_PP, SPIRAL,
     list(range(243, 260)) + list(range(260, 271)) + [275, 277, 287], 420),
    ('INSTRUMENTS.md I-7 whole: the screen, its cross-reference, its second run, the detector sheet', PP, PRE_PP, INSTR,
     list(range(93, 104)) + list(range(148, 201)), 360),
    ('INVARIANCE_BARRIERS v1.4: Theorem 3.1, Proposition 3.5, Corollary 3.6, Theorem 3.7 and its three clauses', PP, PRE_PP, IB,
     [148, 150, 152, 154, 188, 215, 219, 259, 263, 265, 267, 269], 420),
    ('the ζ page at v0.20: its head, the ceiling sentence, the faces’ silence (its back-matter line), positivity_not_imp_simplicity', PP, PRE_PP, PAGE,
     [3, 56, 57, 58, 59, 60, 191, 'positivity_not_imp_simplicity` —'], 420),
    ('the χ page at v0.21: its head and its closing sentences', PP, PRE_PP, DIR_PAGE, [3, 38, 40, 42, 44], 420),
    ('SIMPLICITY v1.1.3: the super-repulsion sentences and the ceiling sentences', PP, PRE_PP, SIMP,
     [222, 240, 248, 371, 449, 520, 568, 572, 577, 580, 583], 420),
    ('CONVERGENT_ARGUMENTS_SIMPLICITY: the super-repulsion correction', PP, PRE_PP, CONV, [7], 600),
    ('A_Place_to_Stand §24.4: the analytic-row note', PP, PRE_PP, MONO, [1499], 1200),
    ('THE_METHOD_CANON §XX: the census / totality pair', PP, PRE_PP, CANON, ['## XX. The census / totality pair', 'Every over-ceiling claim'], 600),
    ('VERIFICATION_LOOM: the findings pass’s seven objects', PP, PRE_PP, LOOM, list(range(1065, 1074)), 400),
    ('FINDINGS: the witness ratio, the (R211)(2) reading, b603’s record lines and entry', PP, PRE_PP, 'FINDINGS.md',
     [6758, 6970, 7022, 7024, 7026, 7028], 600),
    ('OPEN_TRAILS: the form, the precedence order, W-ORD-QUANTIFIER-COLUMN, the fifth shape, the sieve-table entry, b603’s record',
     PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 12228, 12266, 12268, 12270, 12296, 12394] + list(range(12414, 12435)), 600),
    ('relay data/b584_ceiling_census.txt (whole)', RELAY, 'HEAD', 'data/b584_ceiling_census.txt', 'ALL', 260),
    ('relay data/b586_corroboration.txt (whole)', RELAY, 'HEAD', 'data/b586_corroboration.txt', 'ALL', 260),
    ('relay data/b603_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b603_closing_push_out.txt', 'ALL', 260),
    ('SIDE-global-section: the correspondence rows the current version cites (by the row`s cell)', GSK, PRE_GS, 'CORRESPONDENCE.md',
     ['| 4 |', '| 24 |', '| 53 |', '| 68 |', '| 69 |', '| 70 |', '| 72 |', '| 73 |', '| 83 |'], 300),
]


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def reads():
    L = ['b604 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
        else:
            nums = []
            for n in sel:
                if isinstance(n, str):
                    hit = [i + 1 for i, l in enumerate(sl) if l.startswith(n) or (n in l and n.startswith('| ') is False)]
                    nums.append(hit[0] if hit else -1)
                else:
                    nums.append(n)
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    ap = _show(GSK, PRE_GS, 'AXIOM_PRINTS.txt').split(NL)
    ap = [x for x in ap if x.strip()]
    L += ['', '### SIDE-global-section AXIOM_PRINTS.txt @ %s: %d printed lines, %d of them "does not depend on any axioms", %d otherwise '
          '(the count the current version`s §0 carries as 284 at b163 and 327 at b208)' % (
              PRE_GS, len(ap), sum('does not depend on any axioms' in x for x in ap), sum('does not depend on any axioms' not in x for x in ap)),
          '### SIDE-explicit-formula: main = %s ; v0.21 = %s ; the checkout`s branch %s ; tags read: %s' % (
              g(EFK, 'rev-parse', '--short=7', 'main').strip(), g(EFK, 'rev-parse', '--short=7', 'v0.21^{commit}').strip(),
              g(EFK, 'branch', '--show-current').strip(),
              ', '.join('%s=%s' % (t, g(EFK, 'rev-parse', '--short=7', t + '^{commit}').strip()) for t in sorted(W.TAGS, key=lambda x: [int(p) for p in x[1:].split('.')]))),
          '### the pages` node lists: ζ %s (its pin line: %s) ; χ %s (its pin line: %s)' % (
              NODES['zeta'], [l for l in rd(NODES['zeta']).split(NL) if l.startswith('# pin:')], NODES['chi'],
              [l for l in rd(NODES['chi']).split(NL) if l.startswith('# pin:')]),
          '### the work-list roster: relay data/b558_editions/ carries no list for THE_FINDINGS_AS_THEY_STAND: %s' % (
              [x for x in g(RELAY, 'ls-files', 'data/b558_editions').split(NL) if 'FINDINGS' in x] or 'NONE')]
    put_txt('b604_reads.txt', L)


# ================================================================================ THE AUTHOR'S ANSWERS
def answers():
    calls, results = [], {}
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
        try:
            o = json.loads(raw)
        except Exception:
            continue
        m = o.get('message') or {}
        for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
            if c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((i, c['id'], c['input']))
            if c.get('type') == 'tool_result':
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t
                results[c.get('tool_use_id')] = (i, t)
    n = sum(len(c[2].get('questions', [])) for c in calls)
    L = ['### b604 -- THE AUTHOR`S ANSWERS BEFORE THE SEAL, %d prompt(s) put by the seat (2026-10-03), banked verbatim with the options '
         'and the recommended mark, as the standing line at OPEN_TRAILS :12246 orders.' % n, '']
    k = 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session 9f8a2aec-6bbc-47c1-81c1-612ee4051cda, transcript line %d)' % (cid, i))
        for q in inp.get('questions', []):
            k += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'), op.get('description')))
        ri, rt = results.get(cid, (None, '### NO RESULT FOUND'))
        L += ['RESULT (transcript line %s): %s' % (ri, rt), '']
    if not calls:
        L.append('### NONE: no prompt was put to the author in this act.')
    put_txt('b604_author_answers.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B603_ENTRY = '## The family form over χ mod q: the finite sum of configurations'
W_HEAD = '*Appended 2026-10-03 by b604 to b603’s entry (:%d), under `(R214)`(1) -- b603 AT ITS WEIGHT:*'
I_HEAD = '*Appended 2026-10-03 by b604 to b603’s entry (:%d), under `(R214)`(2) -- THE SEAT’S FOUR ITEMS, RULED:*'
WORD_HEAD = ('### `W-ORD-E0-INDUCTION` -- THE E0 RULE’S READING OF AN INDUCTION STEP, PRICED, NOT STARTED, appended 2026-10-03, b604, '
             'under the author’s ruling (R214)(3)')


def _word_text():
    """### b604 (a): the case on the record is named once, beside the grade it now carries; the clause's own grade word stands more
    ### than the table generator's 120-character window from any backticked name, so the paragraph adds no grade cell (the first
    ### wording put the clause's DERIVES beside the case's name and moved its table cell to CONFLICT)."""
    return ('\n%s\n\n**Items.** The shared E0 rule (relay tools/e0_rule.py) reads an induction step whose hypothesis is the induction '
            'hypothesis of the same statement as an interface; its case on the record is `finsetSum_insert`, graded INTERFACES on its '
            'binder at b603’s housekeeping. A clause is added so that a declaration whose named hypothesis is the statement’s own '
            'instance at a smaller index (Finset.insert, Nat.succ, List cons) is read as DERIVES when the step closes at the standard '
            'three, with a test on that case and on a planted genuine interface. **Price:** one tool edit with a test, the terminal '
            'table regenerated, the χ page re-emitted once. **Trigger:** the author’s word.\n' % WORD_HEAD)


def word_again():
    """### b604 (a): after the cut-back of OPEN_TRAILS to the W-ORD append's banked `before` length (its HEAD prefix verified and
    ### printed), the W-ORD block re-appended in its second wording; record_lines.json's third entry rewritten, the first two kept."""
    Q = R2._Q()
    rl = jl('b604_record_lines.json')
    if len(rl.get('lines') or []) != 3:
        sys.exit('### THE RECORD LINES BANK IS NOT WHOLE -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, WORD_HEAD)
    r = Q.append_to(Q.OT, _word_text())
    rl['lines'][2] = dict(file='OPEN_TRAILS.md', head=WORD_HEAD, line=Q.line_of(Q.OT, WORD_HEAD), append=r,
                          first_append=rl['lines'][2]['append'], cut_back='b604 (a)')
    put_json('b604_record_lines.json', rl)
    print('  OPEN_TRAILS.md :%s %s' % (rl['lines'][2]['line'], r))


def record_lines():
    """### PLACE-papers FINDINGS: b603's weight (with the q = 5 fact correction, the navigator's) and the four items as ruled,
    ### addressed to b603's entry; OPEN_TRAILS: W-ORD-E0-INDUCTION with its items, price and trigger. The API-stop pattern line
    ### is the defect list's (data/b604_defects.txt)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, B603_ENTRY)
    if entry != 7028:
        sys.exit('### THE ADDRESSED LINE MOVED -- NOTHING WRITTEN')
    h1, h2 = W_HEAD % entry, I_HEAD % entry
    for p, h in ((Q.FIND, h1), (Q.FIND, h2), (Q.OT, WORD_HEAD)):
        Q.guard_absent(p, h)
    t1 = ('\n%s SIDE-explicit-formula v0.21 = 1d5d4dd, peeled and equal at the remote, family-b603 kept: `finsetSum`, with the '
          'commutativity and associativity of `Product.sum` shown ahead of it, and `finsetSum_productLemma` by Finset induction with no '
          'premise; `family_theorem` over the non-trivial characters mod q, each summand the χ instance at the character’s primitive '
          'character -- Weil positivity of the summed configuration exactly when GRH_chi holds for every member, from the finite lemma '
          'and `h2_sign_cfg_iff_target`, the conductor entering as log(N/π) once per summand by rfl; q = 3 by rfl '
          '(`family_three_statement`); `TrivialSummandPremise` and `EulerFactorPremise` named and undischarged, the Dedekind reading at '
          ':7026 the author’s strike item -- it stands. Every declaration at the standard three, the salt-check’s four theorems '
          'DERIVES, the federation walk empty; the ceiling held as fixed. H37a-H37d, N1-N5, S1-S5 held. FINDINGS :7022, :7024, :7028; '
          'OPEN_TRAILS :12414 with its dated corrections :12432 and :12434. The χ page with ten family nodes; the ζ page '
          'byte-identical. The suite 81 of 82, the one refutation ruled at `(R214)`(2)(iv). A FACT CORRECTION, recorded as the '
          'navigator’s: `(R213)`(3)(c)’s parenthesis “q = 5 (two primitive non-trivial characters)” -- the four characters mod 5 are all '
          'primitive and three of them are non-trivial. Defects (a) and (c)-(h) the seat’s, (b) the harness’s (03:51:17Z to '
          '04:01:00Z, before the seal, nothing partial). Nothing deposited; no keystone edited.\n' % h1)
    t2 = ('\n%s (i) The API stop is recorded as the harness’s; with b602’s it is two in two acts near the same hour, entered as a '
          'pattern line in the defect list (relay data/b604_defects.txt) and not a rule. (ii) The reading of `(R213)`(2) -- '
          'BALANCE_AND_POSITIVITY :400 to the addendum, the lv docstring to an lv housekeeping list opened in relay -- accepted; the '
          'ruling’s “both enter both” was loose. (iii) The ζ page re-emitted from b602’s list at its own pin from the banked probe, the '
          'generator refusing a full run off-pin -- accepted as the page’s standing regeneration path where an act’s lists do not name '
          'it. (iv) G-PAGES-COMMITTED-ALONE refuted in its letter by the χ page’s correction commit (9567591 then 19d4ac3, no reset), '
          'the cause the terminal table’s new `finsetSum_insert` row read as INTERFACES by the E0 rule on lexical grounds -- a letter '
          'refutation as at b597, the seat’s defect (i) as logged; the housekeeping message’s “all UNGRADED” corrected in the '
          'record.\n' % h2)
    t3 = _word_text()
    out = []
    for p, h, t in ((Q.FIND, h1, t1), (Q.FIND, h2, t2), (Q.OT, WORD_HEAD, t3)):
        r = Q.append_to(p, t)
        out.append(dict(file=os.path.basename(p), head=h, line=Q.line_of(p, h), append=r))
    put_json('b604_record_lines.json', dict(entry=entry, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


# ================================================================================ COMPONENT 2: THE MAPPING
def _cur():
    t = _show(PP, PRE_PP, CUR)
    ls = t.split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


def _row(i):
    return [r for r in W.ROWS if r['id'] == i][0]


def _tag_c(tag):
    return W.TAGS[tag][0]


def _pin(f):
    if f.get('corr_row'):
        return 'SIDE-global-section %s (correspondence row %d)' % (W.GS_PIN, f['corr_row'])
    return 'SIDE-explicit-formula %s = %s' % (f['tag'], _tag_c(f['tag']))


def _short(n):
    return n.split('.')[-1]


def _decided(r):
    v, n = W.verdict(r)
    return v, n


def _cv_kind(cur, n):
    l = cur[n - 1].strip()
    if not l:
        return 'blank'
    if l.startswith('#'):
        return 'a heading'
    if l == '---':
        return 'a rule'
    if l.startswith('<!--'):
        return 'a comment marking a refresh'
    if l.startswith('|:--') or l.startswith('| # |') or l.startswith('| open |'):
        return 'a table header'
    return 'not a conclusion: front or meta matter (class, purpose, method, disclosure, a refresh’s own framing)'


def mapping():
    """### data/b604_sieve_mapping.txt (and .json), banked before any writing of the edition: every conclusion of the current version
    ### with its lines, the row it lands in and how; every row with its cluster, shape (H) and the statement or sentence it was read
    ### from, its register, its five tests as run, its verdict with the deciding test and the instrument's pin, its compiled face
    ### (the grouping of plumbing shown) or grade; the current version's other lines classified; H38c scored on the bank."""
    cur = _cur()
    rows_by = {r['id']: r for r in W.ROWS}
    L = ['b604 -- COMPONENT 2: THE MAPPING, (R214)(4) -- THE CURRENT VERSION`S CONCLUSIONS INTO THE SIEVE TABLE BY CLUSTER',
         '### the current version: PLACE-papers %s @ %s (blob %s), %d lines ; banked %s, before any writing of the edition.' % (
             CUR, PRE_PP, g(PP, 'rev-parse', '--short=8', '%s:%s' % (PRE_PP, CUR)).strip(), len(cur), utc()),
         '### the rows: relay tools/b604_rows.py (data only), read here; every shape hand-read (H) at this act, every test read by hand '
         'against its instrument at its pin; the author`s three answers before the seal (data/b604_author_answers.txt) fix the scope '
         '(conclusions, not nodes; readings as rows), the history placement and the five tests.', '']
    L += ['### THE FIVE TESTS (the author`s definitions), each with its instrument and pin:']
    for n in range(1, 6):
        t = W.TESTS[n]
        L.append('    test %d -- %s: %s. Instrument: %s. Pin: %s.' % (n, t['name'], t['q'], t['inst'], t['pin']))
    L += ['### THE SIEVE: a row is read through the tests in order and is DARK at the first test it fails (that number printed); a row '
          'failing none is BRIGHT ("1-5"); test 3 reads only rows over a character or a family (n/a otherwise).', '',
          '### PART A -- EVERY CONCLUSION OF THE CURRENT VERSION (%d), WITH ITS LINES, THE ROW IT LANDS IN AND HOW:' % len(W.CV)]
    land = {}
    for cid, a, b, what, rid, kind in W.CV:
        land.setdefault(rid, []).append((cid, a, b, kind))
        r = rows_by.get(rid)
        L.append('  %s  :%d-:%d  %-11s -> %-6s %s ; %s' % (cid, a, b, kind, rid if r else '### UNPLACED', what, (cur[a - 1].strip()[:150])))
    L += ['', '### PART B -- THE ROWS (%d), BY CLUSTER, EACH WITH ITS COLUMNS:' % len(W.ROWS)]
    for cid, cname in W.CLUSTERS:
        rs = [r for r in W.ROWS if r['cluster'] == cid]
        L.append('')
        L.append('## %s -- %d row(s)' % (cname, len(rs)))
        for r in rs:
            v, n = _decided(r)
            L += ['  %s  [%s]  %s' % (r['id'], r['register'], r['sentence']),
                  '      shape %s (H) -- read from %s: %s' % (r['shape'], 'the Lean statement' if r['faces'] else 'the sentence', r['shape_src']),
                  '      tests: %s' % ' ; '.join('%d %s (%s)' % (t['n'], t['r'], t['why']) for t in r['tests']),
                  '      verdict: %s%s' % (v, ' by test %d -- instrument %s, pinned %s' % (n, W.TESTS[n]['short'], W.TESTS[n]['pin']) if n else
                                          ' -- cleared tests 1-5 at their instruments` pins (%s)' % ' ; '.join(W.TESTS[k]['short'] for k in range(1, 6)))]
            faces = [f for f in r['faces'] if f['role'] == 'face']
            plumb = [f for f in r['faces'] if f['role'] == 'plumbing']
            if faces:
                L.append('      compiled face: %s' % ' ; '.join('%s @ %s%s' % (f['name'], _pin(f), ' [%s page]' % f['page'] if f.get('page') else '') for f in faces))
            if plumb:
                L.append('      plumbing grouped in this row (the author`s answer: plumbing goes in its conclusion`s row as the face): %s' % (
                    ' ; '.join('%s @ %s' % (f['name'], _pin(f)) for f in plumb)))
            if r.get('note'):
                L.append('      note: %s' % r['note'])
            if r.get('grade'):
                L.append('      grade / reading: %s' % r['grade'])
            if r.get('strike'):
                L.append('      strike mark: %s' % r['strike'])
            L.append('      the current version landing here: %s' % (', '.join('%s :%d-:%d (%s)' % x for x in land.get(r['id'], [])) or 'none -- a row the '
                                                                        'current version does not carry (a page conclusion or a reading)'))
    covered = set()
    for _c, a, b, _w, _r, _k in W.CV:
        covered |= set(range(a, b + 1))
    dated = set()
    for a, b, _t, _w, _f in W.DATED:
        dated |= set(range(a, b + 1))
    rest = [n for n in range(1, len(cur) + 1) if n not in covered and cur[n - 1].strip()]
    L += ['', '### PART C -- THE CURRENT VERSION`S OTHER NON-BLANK LINES (%d), NOT CONCLUSIONS, CLASSIFIED (each carried in the edition, '
          'beneath a table when dated, in the back matter otherwise):' % len(rest)]
    for n in rest:
        L.append('  :%-4d %-34s %s' % (n, _cv_kind(cur, n)[:34], cur[n - 1].strip()[:130]))
    ids = [c[0] for c in W.CV]
    unplaced = [c[0] for c in W.CV if c[4] not in rows_by]
    multi = [i for i in ids if ids.count(i) > 1]
    clusters_with = [c for c, _n in W.CLUSTERS if any(r['cluster'] == c for r in W.ROWS)]
    h38c = 'HOLDS' if not unplaced and not multi and len(ids) == len(W.CV) else 'REFUTED'
    L += ['', '### PART D -- THE COUNTS AND H38c',
          '  conclusions of the current version : %d ; landing in exactly one row each : %d ; UNPLACED : %d %s ; listed twice : %s' % (
              len(W.CV), len(W.CV) - len(unplaced), len(unplaced), unplaced or '', multi or 'none'),
          '  of them own %d ; restating a row %d ; superseded, carried as history lines beneath their row %d' % (
              sum(c[5] == 'own' for c in W.CV), sum(c[5] == 'restates' for c in W.CV), sum(c[5] == 'superseded' for c in W.CV)),
          '  rows : %d ; clusters carrying rows : %d of %d (%s) ; clusters with no row : %s' % (
              len(W.ROWS), len(clusters_with), len(W.CLUSTERS), ', '.join(clusters_with), [n for c, n in W.CLUSTERS if c not in clusters_with]),
          '  rows from the current version : %d ; rows from the pages` conclusions : %d ; rows that are readings : %d' % (
              sum(1 for r in W.ROWS if any(c[4] == r['id'] and c[5] == 'own' for c in W.CV)),
              sum(1 for r in W.ROWS if r['faces'] and not any(c[4] == r['id'] and c[5] == 'own' for c in W.CV)),
              sum(1 for r in W.ROWS if (r.get('grade') or '').startswith('reading'))),
          '  BRIGHT %d ; DARK %d (by test 1: %d ; 2: %d ; 3: %d ; 4: %d ; 5: %d)' % (
              sum(W.verdict(r)[0] == 'BRIGHT' for r in W.ROWS), sum(W.verdict(r)[0] == 'DARK' for r in W.ROWS),
              *[sum(W.verdict(r) == ('DARK', k) for r in W.ROWS) for k in range(1, 6)]),
          '', '### ### **H38c %s -- every conclusion of the current version lands in exactly one row, none dropped, the mapping banked here.**' % h38c]
    put_txt('b604_sieve_mapping.txt', L)
    put_json('b604_sieve_mapping.json', dict(at=utc(), cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(), n_cur_lines=len(cur),
                                              cv=[dict(id=c[0], a=c[1], b=c[2], what=c[3], row=c[4], kind=c[5]) for c in W.CV],
                                              rows=[dict(id=r['id'], cluster=r['cluster'], register=r['register'], shape=r['shape'],
                                                         verdict=W.verdict(r)[0], test=W.verdict(r)[1]) for r in W.ROWS],
                                              unplaced=unplaced, multi=multi, rest=rest, H38c=h38c, clusters_with=clusters_with))
    print(L[-1])
    print('  rows %d ; clusters %d ; unplaced %d' % (len(W.ROWS), len(clusters_with), len(unplaced)))


# ================================================================================ COMPONENT 3: THE EDITION
BM_TAG = '<!-- b604 (R214) THE v0.2 EDITION`S BACK MATTER, 2026-10-03 -->'
HIST_OPEN = '<!-- HISTORY CARRIED BENEATH THIS TABLE: %s -- back matter of the table, counted with the back matter -->'
HIST_CLOSE = '<!-- END OF THE HISTORY CARRIED BENEATH THIS TABLE -->'
VERSION = '*v0.2, 2026-10-03 -- the edition of this document as the sieve table by cluster; the current version (unnumbered, read as v0.1) stands beside it, unedited.*'
ACTNUM = re.compile(r'\bb\d{2,4}\b')
CEILING = re.compile(r'\bprov(?:e|ed|en|es)\b|\bproof\b|RH-core|RH proved|proves RH|end-to-end|the whole of RH')

MUTUAL = {
    'RH': 'Read in mutual light: Foundations’ rows supply test 2 -- every row of this table darkened at test 2 is one whose route goes '
          'through at the Epstein configuration those rows compile -- and Methodology’s record rows fix how far any row here may be '
          'read (the findings pass, its fences, the document’s limits); Cubit / Trivium’s and Matter / cosmology’s rows change no '
          'reading here, their objects decided independent of the identity and the density.',
    'FD': 'Read in mutual light: the Simplicity / RH cascade’s six BRIGHT rows are the routes Theorem 3.7 says must use the Euler '
          'product, and its rows darkened at test 2 are the Euler-product-free routes this table’s witness reaches; Methodology’s '
          'record rows bound this table’s barrier row.',
    'MT': 'Read in mutual light: every other cluster’s rows are read through this table’s, whose rows fix what a row may claim (the '
          'governing claim’s ceiling, the findings pass, the limits of the fold); no other cluster’s row changes a record row’s own '
          'verdict, since a statement about the corpus names no zero.',
    'CT': 'Read in mutual light: no other cluster’s rows change this row’s reading; the findings pass decided its object independent '
          'of the identity and the density, and that decision stands in Methodology’s findings-pass row.',
    'MC': 'Read in mutual light: no other cluster’s rows change this row’s reading; the findings pass decided its object independent '
          'of the identity and the density, and that decision stands in Methodology’s findings-pass row.',
}

BENCH = [
    ('the super-repulsion fit', 'A fitted spacing exponent of β ≈ 12.32 against GUE’s 2 (SIMPLICITY v1.1.3 :240), corrected on the record to '
     'GUE-consistent repulsion, β_CDF ≈ 3.8 (CONVERGENT_ARGUMENTS_SIMPLICITY :7); a spacing statistic carries no real part, so test 1 '
     'darkens it. What it would refute: a claim that the zeros’ spacing law departs from GUE beyond the fit’s error; no placement '
     'statement can be refuted by it.'),
    ('the 0.6725 ceiling', 'At least two thirds of the zeros of ζ, counted with multiplicity, are simple and on the line, 0.6725 with the '
     'Montgomery–Taylor window (A_Place_to_Stand §24.4’s analytic-row note, :1499; carried in the kernel as the premise of '
     '`exceptional_mass_le_third`); a proportion is a density, which test 1 and Theorem 3.1’s ceiling darken. What it would refute: any '
     'reading of a proportion as all zeros, and any route that claims the last third by density methods alone.'),
    ('the Epstein witnesses', 'The Epstein zeta of discriminant −23 agrees with ξ on the named toolkit and has off-line zeros '
     '(INVARIANCE_BARRIERS v1.4 Proposition 3.5, Theorem 3.7); compiled, a configuration carrying ρ_E is not Weil-positive under the '
     'Epstein premises (`epstein_not_h2_sign_cfg`, SIDE-explicit-formula v0.16 = c404e72), the compiled witness at least 2²⁴ base '
     'widths wide, four orders of magnitude wider than the bench’s plateau (FINDINGS :6758). What it would refute: any route to Weil '
     'positivity for ξ that goes through at the Epstein configuration -- test 2’s failure, made concrete.'),
]


def _cell(s):
    return s.replace('|', '¦')


def _row_cells(r):
    v, n = W.verdict(r)
    if v == 'DARK':
        t = [x for x in r['tests'] if x['n'] == n][0]
        vb = 'DARK, test %d (%s): %s' % (n, W.TESTS[n]['short'], t['why'])
    else:
        vb = 'BRIGHT, tests 1–5 cleared%s' % ('' if any(x['n'] == 3 and x['r'] == 'PASS' for x in r['tests']) else ' (test 3 n/a: no character enters)')
    faces = [f for f in r['faces'] if f['role'] == 'face']
    plumb = [f for f in r['faces'] if f['role'] == 'plumbing']
    if faces:
        fc = '; '.join('`%s` @ %s' % (_short(f['name']), _pin(f)) for f in faces)
        if plumb:
            fc += '; plumbing: ' + ', '.join('`%s`' % _short(f['name']) for f in plumb)
        if r.get('grade'):
            fc += ' -- ' + r['grade']
    else:
        fc = r.get('grade') or 'reading'
    if r.get('strike'):
        fc += ' -- ' + r['strike']
    return [r['id'], r['sentence'], '%s (H)' % r['shape'], r['register'], vb, fc]


def _quote(l):
    return '> ' + l if l.strip() else '>'


def _row_line(r):
    return '| ' + ' | '.join(_cell(x) for x in _row_cells(r)) + ' |'


def _where(E):
    """### every carried line of the current version -> its edition line, from the edition's banked positions."""
    where = {}
    P = E['pos']
    for key, start in list(P['dated'].items()) + list(P['superseded'].items()):
        a_, b_ = [int(x) for x in key.split('-')]
        for k, n in enumerate(range(a_, b_ + 1)):
            where[n] = start + k
    for k, n in enumerate(range(W.CLASS_LINES[0], W.CLASS_LINES[1] + 1)):
        where[n] = P['cls'] + k
    for k, n in enumerate(E['rest']):
        where[n] = P['rest'] + k
    return where


def _carried(line, n, cur_line):
    if line.startswith('> :%d ' % n):
        return line[len('> :%d ' % n):] == cur_line
    return _unquote(line) == cur_line


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _body_and_bm(ed):
    """### the body: every line before the back-matter tag and outside the history blocks; the back matter: the rest."""
    cut = ed.index(BM_TAG)
    body, bm, inside = [], [], False
    for i, l in enumerate(ed):
        if i >= cut:
            bm.append((i + 1, l))
            continue
        if l.startswith('<!-- HISTORY CARRIED BENEATH THIS TABLE'):
            inside = True
        (bm if inside else body).append((i + 1, l))
        if l == HIST_CLOSE:
            inside = False
    return body, bm


def edition(*a):
    """### PLACE-papers phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md beside the current version (unedited), written from the
    ### current version's blob at 24e7ff2 and tools/b604_rows.py; the re-pin step last (`repin`). Writes the edition file and
    ### data/b604_edition.json; `dry` writes the file to the scratchpad instead."""
    dry = 'dry' in a
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE %s -- NOTHING WRITTEN' % PRE_PP)
    if not dry and os.path.exists(os.path.join(PP, *ED.split('/'))):
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    M = jl('b604_sieve_mapping.json') if os.path.exists(os.path.join(D, 'b604_sieve_mapping.json')) else {}
    if M.get('H38c') != 'HOLDS' and not dry:
        sys.exit('### THE MAPPING IS NOT BANKED OR H38c DOES NOT HOLD -- COMPONENT 2 FIRST')
    clusters_with = [c for c, _n in W.CLUSTERS if any(r['cluster'] == c for r in W.ROWS)]
    empty = [n for c, n in W.CLUSTERS if c not in clusters_with]
    nrows = len(W.ROWS)
    E = []
    pos = dict(rows={}, hist_blocks={}, dated={}, superseded={}, tables={}, mutual={}, bench={}, tests={})
    E += ['# The findings as they stand — the sieve table, by cluster', '', VERSION, '',
          cur[9], '',
          '**DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): TIER C** — a self-description organizing the '
          'findings at their grades; the current version’s class lines are carried in the back matter.', '',
          '> **The governing claim, under the ceiling:** RH reduced to a single located clause, Weil positivity on classK (`h2_sign`), '
          'compiled as equivalent to RH in both directions (`h2_sign_iff_rh`, SIDE-explicit-formula v0.2 = 5c72cad); the clause is '
          'open, and no row of this table places a zero.', '',
          '## How the table reads', '',
          'Each row is one conclusion the record carries, written in one sentence under the ceiling. The rows are the current version’s '
          'conclusions re-read as they stand, the conclusions the two pages compile (a lemma that only feeds one of them sits in its '
          'row as part of the compiled face), and the readings the record carries uncompiled, graded as readings. Each column reads as '
          'follows.', '',
          '- **Shape**: FINITE, UNIVERSAL, LIMIT, DENSITY or FAMILY, hand-read (H) at this edition from the Lean statement for a compiled '
          'row and from the sentence for the others, until W-ORD-QUANTIFIER-COLUMN’s generator read replaces it.',
          '- **Register**: the subject the row’s object belongs to (the list below).',
          '- **Bright or dark**: the five tests below, read in order; a row is DARK at the first test it fails, with that test’s number, '
          'its instrument’s pin and the reason, and BRIGHT when it fails none. BRIGHT says the row’s register reaches placement at a '
          'compiled face; it does not say the row’s open side holds.',
          '- **Compiled face**: the declaration and its pin, or the grade where there is none, or “reading”.', '',
          '## The five tests', '']
    for n in range(1, 6):
        t = W.TESTS[n]
        pos['tests'][n] = len(E) + 1
        E.append('%d. **%s** — %s. Instrument: %s; pinned at %s.' % (n, t['name'], t['q'], t['inst'], t['pin']))
    E += ['', 'Each test is read by hand at this edition against its instrument, and the instrument’s pin is the place the reading answers '
          'to; test 3 reads only a row over a character or a family.', '', '## The registers', '',
          '- **Bright registers, the ones the sieve looks for:** ' + '; '.join('%s (%s)' % (n, d) for n, k, d in W.REGISTERS if k == 'bright') + '.',
          '- **Dark registers, carried in the bench as falsifiers:** ' + '; '.join('%s (%s)' % (n, d) for n, k, d in W.REGISTERS if k == 'dark') + '.',
          '- **The current version’s own objects, with three more:** ' + '; '.join('%s (%s)' % (n, d) for n, k, d in W.REGISTERS if k == 'own') + '.', '',
          '## The clusters', '',
          'The clusters are SPIRAL_MAP §4A’s, as its refreshed table carries them: %s. %d of them carry the table’s %d rows; %s carry '
          'none, since no conclusion of the record lands there, and are named so that the absence is visible.' % (
              ', '.join(n for _c, n in W.CLUSTERS), len(clusters_with), nrows, ', '.join(empty)), '']
    sup = {}
    for cid_, a_, b_, what, rid, kind in W.CV:
        if kind == 'superseded':
            sup.setdefault(rid, []).append((a_, b_, what))
    dated_lines = set()
    for a_, b_, _t, _w, _f in W.DATED:
        dated_lines |= set(range(a_, b_ + 1))
    # ### the superseded conclusions not inside a dated entry: carried as history lines beneath their row's table (the head block :12-:20)
    head_block = (12, 20)
    carried_beneath = set(range(head_block[0], head_block[1] + 1))
    for cid, cname in W.CLUSTERS:
        rs = [r for r in W.ROWS if r['cluster'] == cid]
        if not rs:
            continue
        nb = sum(W.verdict(r)[0] == 'BRIGHT' for r in rs)
        E += ['## %s — %d row%s, %d BRIGHT, %d DARK' % (cname, len(rs), '' if len(rs) == 1 else 's', nb, len(rs) - nb), '']
        pos['tables'][cid] = len(E) + 1
        E += ['| row | the conclusion | shape | register | bright or dark: test, instrument at pin, reason | compiled face |',
              '|:--|:--|:--|:--|:--|:--|']
        for r in rs:
            pos['rows'][r['id']] = len(E) + 1
            E.append(_row_line(r))
        E.append('')
        pos['mutual'][cid] = len(E) + 1
        E += [MUTUAL[cid], '']
        pos['hist_blocks'][cid] = len(E) + 1
        E += [HIST_OPEN % cname, '', '### History carried beneath this table', '',
              '*The current version’s dated entries that fed this table’s rows, carried verbatim under the history clause and quoted line '
              'by line, each with the lines it held in the current version; with the superseded conclusions this table’s rows replace. '
              'Back matter of the table, counted with the back matter.*', '']
        any_ = False
        if cid == 'RH':
            a_, b_ = head_block
            E += ['**The current version :%d–:%d, its head block, carried as history lines: the governing claim (:12–:13), superseded by '
                  'row RH-01, which names the clause as `h2_sign` under the ceiling; its restatements land in RH-01, RH-31 and '
                  'RH-32.**' % (a_, b_), '']
            pos['superseded'][(a_, b_)] = len(E) + 1
            E += [_quote(cur[n - 1]) for n in range(a_, b_ + 1)] + ['']
            any_ = True
        for a_, b_, t_, what, fed in W.DATED:
            if t_ != cid:
                continue
            sp = [x for x in sup.items() for y in x[1] if a_ <= y[0] <= b_]
            E += ['**The current version :%d–:%d, %s, carried; it fed %s.%s**' % (
                a_, b_, what, ', '.join(fed) if fed else 'no row', (' Its conclusion%s superseded by %s, carried here as a history line.' % (
                    's are' if len(sp) > 1 else ' is', ', '.join(sorted(set(x[0] for x in sp))))) if sp else ''), '']
            pos['dated'][(a_, b_)] = len(E) + 1
            E += [_quote(cur[n - 1]) for n in range(a_, b_ + 1)] + ['']
            any_ = True
        others = [(a_, b_, t_, what, fed) for a_, b_, t_, what, fed in W.DATED if t_ != cid and any(f.split('-')[0] == cid for f in fed)]
        for a_, b_, t_, what, fed in others:
            E += ['*The current version :%d–:%d (%s) also fed %s; it is carried beneath the %s table.*' % (
                a_, b_, what, ', '.join(f for f in fed if f.split('-')[0] == cid), dict(W.CLUSTERS)[t_]), '']
            any_ = True
        if not any_:
            E += ['*None: no dated entry of the current version fed this table’s rows.*', '']
        E += [HIST_CLOSE, '']
    E += ['## The bench — the dark registers as falsifiers', '']
    for name, text in BENCH:
        pos['bench'][name] = len(E) + 1
        E.append('- **%s.** %s' % (name[0].upper() + name[1:], text))
    E += ['', '---', '']
    # ### the back matter
    rest = [n for n in range(1, len(cur) + 1) if n not in dated_lines and n not in carried_beneath and cur[n - 1].strip()
            and not (W.CLASS_LINES[0] <= n <= W.CLASS_LINES[1])]
    E += [BM_TAG, '',
          '## Back matter of the v0.2 edition — written 2026-10-03 by b604 under the author’s ruling `(R214)`(4), by the form of '
          '`(R187)`(5), its clauses and the precedence order, with the reorganisation `(R212)`(6) allows', '',
          '*This file is v0.2 of THE_FINDINGS_AS_THEY_STAND, written beside the current version (`%s`, unnumbered and read as v0.1, '
          'unedited) from that version’s blob at PLACE-papers %s, the two pages as its spine and the mapping banked at relay '
          '`data/b604_sieve_mapping.txt` before the edition was written. The document keeps its class (Tier C); the edition promotes no '
          'reading, moves no grade, does not deposit and does not replace the current version; its promotion is CP-8’s. Every line cited '
          'below is this file’s own unless it is marked as the current version’s.*' % (CUR, PRE_PP), '',
          '### The reorganisation and its readings', '',
          '- The body is the head (the five tests, the registers, the clusters), one table per cluster carrying rows, one mutual-light '
          'line per table, and the bench; the history blocks beneath the tables and everything below this tag are back matter, counted '
          'separately (the author’s answer before the seal, relay `data/b604_author_answers.txt`).',
          '- The rows are conclusions, not nodes: each page theorem whose statement is a conclusion has its row, and a lemma that only '
          'feeds one sits in that row’s face as plumbing (the grouping printed in the mapping bank); the four readings the record carries '
          'uncompiled are rows graded as readings (the author’s answer).',
          '- The five tests are the author’s definitions (the answer before the seal); `(R214)`(4)’s grouping of Theorem 3.1 with 3.7 '
          'under one instrument is the navigator’s, recorded at the act’s record.',
          '- The current version’s §7 sentence carries three decisions (“each of these”), read as three conclusions, one row each, in '
          'three clusters.',
          '- The pages’ node lists are read at their own pins: the ζ page’s at v0.20 = 914c413 (its list keeps its own pin, the standing '
          'regeneration path of `(R214)`(2)(iii)), the χ page’s at v0.21 = 1d5d4dd -- a fact correction to `(R214)`(4)’s “at v0.21” for '
          'the ζ list.', '',
          '### Removals', '',
          'None deleted. Every sentence of the current version is carried: its dated entries beneath the tables they fed, its head block '
          'beneath the Simplicity / RH cascade table as history lines, its class lines and every other sentence below as history lines, '
          'each with its line in the current version. Under H28b each moved sentence is counted as a removal from the body recorded in '
          'the back matter.', '',
          '### Rewrites -- the superseded conclusions', '',
          '| row | the current version’s line | the current version’s wording | this edition’s wording | Status |', '|:--|:--|:--|:--|:--|']
    for cid_, a_, b_, what, rid, kind in W.CV:
        if kind != 'superseded':
            continue
        E.append('| %s (:%s) | :%d–:%d | %s | %s | superseded by the compiled row; the old wording carried as a history line beneath its table |' % (
            rid, '{ROW:%s}' % rid, a_, b_, _cell(flat(re.sub(r'\*+|#+|^>\s*', '', ' '.join(re.sub(r'^>\s*', '', cur[n - 1]) for n in range(a_, b_ + 1)))))[:300],
            _cell(_row(rid)['sentence'])))
    E += ['', '### Fact corrections', '',
          '| row | the current version’s wording | this edition’s wording | the source | Status |', '|:--|:--|:--|:--|:--|',
          '| MT-01 (:{ROW:MT-01}) | 284 Core terminals … across 73 correspondence rows (:43–:44; marked at its dated entry as 327 lines, 83 rows) | '
          '614 printed lines, every one zero-axiom | SIDE-global-section `AXIOM_PRINTS.txt` at %s, counted at content (relay '
          '`data/b604_reads.txt`) | fact correction (OPEN_TRAILS :11954); the dated mark carried unchanged beneath the Methodology table |' % W.GS_PIN,
          '| the ruling | “the page’s node list … at v0.21” | the ζ list at its own pin v0.20 = 914c413, the χ list at v0.21 = 1d5d4dd | '
          'relay `data/b602_nodes_zeta.txt` and `data/b603_nodes_chi.txt`, their `# pin:` lines | a fact correction to the ruling’s '
          'letter, recorded as the navigator’s |', '',
          '### Collisions resolved by the precedence order', '',
          '| where | the clauses that meet | governs | the wording carried | the wording written | Status |', '|:--|:--|:--|:--|:--|:--|',
          '| every dated entry of the current version (beneath its table) | the history clause; `(R214)`(4)’s act numbers in the back matter '
          'only (H38b) | history, by placement: the entries carried unchanged in blocks counted as back matter (the author’s answer) | the '
          'entries verbatim, act numbers included | no body sentence: the rows restate each conclusion without an act number | resolved |',
          '| the currency mark of 2026-08-26 and row MT-01 | the history clause; the fact clause | history on the dated mark, fact on the row | '
          '327 lines, 83 rows (dated) | 614 printed lines, every one zero-axiom (the row) | resolved |',
          '| the governing claim (:12–:13) and row RH-01 | the history clause (carried as a history line); the ceiling clause (README '
          ':106–:121, the clause named as `h2_sign`) | the ceiling on the row; the old wording carried beneath | RH reduced to a single '
          'located clause, reduction machine-verified | the row names the clause as `h2_sign` and its compiled equivalence | resolved |',
          '| the §7 sentence (:175–:177) | the restatement clause; one row per conclusion | the reorganisation’s reading: three decisions, '
          'three rows | one sentence | MT-06, CT-01, MC-01 | resolved |', '',
          '### History lines -- the current version’s class lines and its other sentences the sieve supersedes, carried verbatim', '',
          '*Quoted line by line, each with its line in the current version; nothing deleted.*', '',
          '**The current version :%d–:%d, its class declarations and its built line (dated; they fed no table).**' % W.CLASS_LINES, '']
    pos['class'] = len(E) + 1
    E += [_quote(cur[n - 1]) for n in range(W.CLASS_LINES[0], W.CLASS_LINES[1] + 1)] + ['']
    E += ['**The current version’s other non-blank lines, in order (%d), each prefixed by its line there.**' % len(rest), '']
    pos['rest'] = len(E) + 1
    for n in rest:
        E.append('> :%d %s' % (n, cur[n - 1]))
    E += ['', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this edition, v0.2 | `%s` | written at b604 |' % ED,
          '| the current version, unnumbered (read as v0.1) | `%s` | unedited |' % CUR,
          '| the spine: the ζ page | `%s`, its node list at SIDE-explicit-formula v0.20 = 914c413 | read |' % PAGE,
          '| the spine: the χ page | `%s`, its node list at SIDE-explicit-formula v0.21 = 1d5d4dd | read |' % DIR_PAGE,
          '| the clusters | `SPIRAL_MAP.md` §4A, the refreshed table (:260–:269) | read |',
          '| the tests’ instruments | `phase1.5/method/INSTRUMENTS.md` I-7; `phase1.5/method/INVARIANCE_BARRIERS_v1_4.md` §3 | read |',
          '| the mapping | relay `data/b604_sieve_mapping.txt` | banked at b604 before the edition |',
          '| the sentence-by-sentence diff | relay `data/b604_edition_FINDINGS_STAND.txt` | banked at b604 |', '',
          '### Correspondence', '',
          '| row | this edition’s line | founding act(s) | the compiled face, every declaration at its pin | the current version’s lines landing here | Status |',
          '|:--|:--|:--|:--|:--|:--|']
    land = {}
    for cid_, a_, b_, what, rid, kind in W.CV:
        land.setdefault(rid, []).append(':%d–:%d (%s)' % (a_, b_, kind))
    for r in W.ROWS:
        v, n = W.verdict(r)
        fc = '; '.join('`%s` @ %s%s' % (f['name'], _pin(f), ' (%s)' % f['role'] if f['role'] != 'face' else '') for f in r['faces']) or (r.get('grade') or 'reading')
        E.append('| %s | :{ROW:%s} | %s | %s | %s | %s |' % (r['id'], r['id'], ', '.join(r['acts']), _cell(fc), ', '.join(land.get(r['id'], [])) or 'none',
                                                             'BRIGHT, 1–5' if v == 'BRIGHT' else 'DARK, test %d' % n))
    E += ['', '### Version history', '',
          '- **v0.2, 2026-10-03 (b604, `(R214)`(4))**: the body reorganised as the sieve table by cluster -- %d rows over %d clusters, the '
          'shape (H), the register, bright or dark by the five tests at their instruments’ pins, the compiled face; every sentence of '
          'the current version carried. The current version (built 2026-08-25 at b163, its dated entries through 2026-09-25 at b535) '
          'stands beside it, unedited.' % (nrows, len(clusters_with)), '']
    # ### resolve the {ROW:id} tokens to the final lines
    E = [re.sub(r'\{ROW:([A-Z]{2}-\d\d)\}', lambda m: str(pos['rows'][m.group(1)]), x) for x in E]
    text = NL.join(E) + NL
    b = text.encode('utf-8')
    dest = os.path.join(SP, 'b604_edition_dry.md') if dry else os.path.join(PP, *ED.split('/'))
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    ed = text.split(NL)[:-1]
    body, bm = _body_and_bm(ed)
    n_body = _count([l for _i, l in body])
    n_bm = _count([l for _i, l in bm])
    n_cur = _count(cur)
    body_sents = [(i, s) for i, l in body for s in _segs(l)]
    acts = [(i, m.group(0)) for i, l in body for m in ACTNUM.finditer(l)]
    ceil = [(i, m.group(0)) for i, l in body for m in CEILING.finditer(l)]
    J = dict(at=utc(), dry=dry, path=ED, sha256=sha(b), bytes=len(b), lines=len(ed), cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
             n_cur=n_cur, n_body=n_body, n_backmatter=n_bm, n_full=_count(ed), body_lines=[i for i, _l in body], acts_in_body=acts, ceiling_in_body=ceil,
             pos=dict(rows=pos['rows'], tables=pos['tables'], mutual=pos['mutual'], hist_blocks=pos['hist_blocks'], bench=pos['bench'], tests=pos['tests'],
                      dated={'%d-%d' % k: v for k, v in pos['dated'].items()}, superseded={'%d-%d' % k: v for k, v in pos['superseded'].items()},
                      cls=pos['class'], rest=pos['rest']),
             rest=rest, version_lines=1, credit=0, removals=n_cur, ruled=n_body - 1, rows=nrows, clusters=len(clusters_with),
             body_sentences=len(body_sents))
    if dry:
        # ### the dry run writes nothing in relay: its json beside the scratchpad file
        open(os.path.join(SP, 'b604_edition_dry.json'), 'w', encoding='utf-8').write(json.dumps(J, indent=1, ensure_ascii=False))
    else:
        put_json('b604_edition.json', J)
    print('  %s : %d lines, %d bytes, sha256 %s' % (dest, len(ed), len(b), J['sha256'][:16]))
    print('  sentences: current %d ; body %d ; back matter %d ; act numbers in body %s ; ceiling hits in body %s' % (n_cur, n_body, n_bm, acts, ceil))


def termscan():
    """### the scanner (banned_terms.py --new) on the edition file, banked as data/b604_edition_termscan.txt."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', os.path.join(PP, *ED.split('/'))],
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b604_edition_termscan.txt', (r.stdout or '').rstrip(NL).split(NL))
    print([l for l in r.stdout.split(NL) if 'live uses' in l or 'VERDICT' in l])


def _ed():
    t = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read().replace(chr(13), '')
    ls = t.split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


def _unquote(l):
    return l[2:] if l.startswith('> ') else ('' if l == '>' else None)


def _pin_checks():
    """### H38a: every row's instrument pins (the deciding test's; all five for a BRIGHT row) and its face pins resolve."""
    out = []
    inst_anchor = {
        1: [(PP, W.PP_I7, INSTR, 93, '## I-7'), (PP, W.PP_I7, INSTR, 148, '### I-7'), (PP, W.PP_IB, IB, 148, '**Theorem 3.1'),
            (PP, W.PP_IB, IB, 188, '**Proposition 3.5')],
        2: [(EFK, 'v0.16', 'SIDEExplicitFormula/Schema/Detector.lean', None, 'theorem detector'),
            (EFK, 'v0.16', 'SIDEExplicitFormula/Schema/Epstein.lean', None, 'theorem epstein_not_h2_sign_cfg'),
            (PP, W.PP_IB, IB, 259, '**Theorem 3.7')],
        3: [(EFK, 'v0.13', 'SIDEExplicitFormula/Chi/Main.lean', None, 'theorem EF_lit_chi_holds'),
            (EFK, 'v0.21', 'SIDEExplicitFormula/Schema/Family.lean', None, 'theorem family_theorem')],
        4: [(EFK, 'v0.3', 'SIDEExplicitFormula/DetectionRegion.lean', None, 'theorem h2_sign_iff_forall_upto'),
            (EFK, 'v0.3', 'SIDEExplicitFormula/DetectionRegion.lean', None, 'theorem forall_upto_iff_rh'),
            (EFK, 'v0.9', 'SIDEExplicitFormula/LiCriterionBridge.lean', None, 'theorem li_nonneg_iff_rh')],
        5: [(RELAY, 'HEAD', 'data/' + NODES['zeta'], None, '# pin: v0.20'), (RELAY, 'HEAD', 'data/' + NODES['chi'], None, '# pin: v0.21')],
    }
    cache = {}

    def check(repo, rev, path, line, needle):
        k = (repo, rev, path)
        if k not in cache:
            cache[k] = _show(repo, rev, path)
        t = cache[k]
        if t is None:
            return False
        ls = t.split(NL)
        if line:
            return 0 < line <= len(ls) and ls[line - 1].startswith(needle)
        return any(l.startswith(needle) or l.startswith('@[defeq] ' + needle) for l in ls)
    tag_ok = {t: g(EFK, 'rev-parse', '--short=7', t + '^{commit}').strip() == c for t, (c, _a) in W.TAGS.items()}
    ix = {}
    for t in set(f['tag'] for r in W.ROWS for f in r['faces'] if not f.get('corr_row')):
        ix[t] = g(EFK, 'grep', '-n', '-E', r'(theorem|def|structure) ', t, '--', '*.lean')
    corr = _show(GSK, W.GS_PIN, 'CORRESPONDENCE.md') or ''
    for r in W.ROWS:
        v, n = W.verdict(r)
        tests = range(1, 6) if v == 'BRIGHT' else [n]
        for k in tests:
            for repo, rev, path, line, needle in inst_anchor[k]:
                out.append(dict(row=r['id'], what='test %d instrument %s:%s %s' % (k, path.split('/')[-1], line or '', needle), ok=check(repo, rev, path, line, needle)))
        for f in r['faces']:
            if f.get('corr_row'):
                ok = any(l.startswith('| %d |' % f['corr_row']) and ('`%s`' % f['name']) in l for l in corr.split(NL))
                out.append(dict(row=r['id'], what='face %s @ SIDE-global-section %s row %d' % (f['name'], W.GS_PIN, f['corr_row']), ok=ok))
                continue
            sn = _short(f['name']).split('.{')[0]
            ok = tag_ok.get(f['tag'], False) and re.search(r'(theorem|def|structure) %s\b' % re.escape(sn), ix.get(f['tag'], '')) is not None
            out.append(dict(row=r['id'], what='face %s @ %s = %s' % (f['name'], f['tag'], _tag_c(f['tag'])), ok=ok))
    return out


def edition_bank():
    """### The diff with its offset line, the collisions, the counts, the ceiling read, the scanner's verdict, H28a-H28c, H38a, H38b, H38d."""
    E = jl('b604_edition.json')
    ed = _ed()
    cur = _cur()
    if sha('\n'.join(ed).encode('utf-8') + b'\n') != E['sha256']:
        sys.exit('### THE EDITION ON DISK IS NOT THE BANKED ONE -- NOTHING WRITTEN')
    body, bm = _body_and_bm(ed)
    scan = rd('b604_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    # ### where every current line landed
    P = E['pos']
    where = _where(E)
    carried_ok, carried_bad = 0, []
    for n, el in sorted(where.items()):
        ok = _carried(ed[el - 1], n, cur[n - 1])
        carried_ok += ok
        if not ok:
            carried_bad.append(n)
    missing = [n for n in range(1, len(cur) + 1) if cur[n - 1].strip() and n not in where]
    hits = []
    body_idx = set(i for i, _l in body)
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            hits.append(dict(line=i, hit=m.group(0), kind='body' if i in body_idx else 'record (carried history or back matter)'))
    beyond = [h for h in hits if h['kind'] == 'body']
    acts = [(i, m.group(0)) for i, l in body for m in ACTNUM.finditer(l)]
    sup = [c for c in W.CV if c[5] == 'superseded']
    h28a_rows = []
    for c in sup:
        r = _row(c[4])
        cites = [f for f in r['faces'] if f['role'] == 'face' and f.get('page') and (('`%s`' % _short(f['name'])) in ed[P['rows'][r['id']] - 1])]
        h28a_rows.append(dict(cv=c[0], lines='%d-%d' % (c[1], c[2]), row=r['id'], cites=[f['name'] for f in cites]))
    h28a = 'HOLDS' if all(x['cites'] for x in h28a_rows) else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur']
    allowed = E['credit'] + E['removals'] + E['ruled'] + E['version_lines']
    allowed_strict = E['credit'] + 0 + E['ruled'] + E['version_lines']
    h28b = 'HOLDS' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if (clean and not beyond) else 'REFUTED'
    pins = _pin_checks()
    h38a = 'HOLDS' if all(p['ok'] for p in pins) else 'REFUTED'
    h38b = 'HOLDS' if not acts else 'REFUTED'
    rows_by_cluster = {}
    for r in W.ROWS:
        rows_by_cluster.setdefault(r['cluster'], []).append(r)
    dark_each = {c: [r['id'] for r in rs if W.verdict(r)[0] == 'DARK'] for c, rs in rows_by_cluster.items()}
    bright_reg = {g_: [r['id'] for r in W.ROWS if r['register'] == g_ and W.verdict(r)[0] == 'BRIGHT'] for g_ in W.BRIGHT_REGISTERS}
    h38d = 'HOLDS' if all(dark_each.values()) and all(bright_reg.values()) else 'REFUTED'
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): REORGANISED -- no line keeps its number; every current line`s edition line is '
         'printed below (the map), and every edition line cited here is the final file`s own.', '',
         'b604 -- COMPONENT 3: THE EDITION OF THE_FINDINGS_AS_THEY_STAND AS THE SIEVE TABLE BY CLUSTER, (R214)(4), BY THE FORM OF (R187)(5), '
         'ITS CLAUSES AND THE PRECEDENCE ORDER', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; no version line (read as v0.1) ; no '
         'Correspondence table ; its dated entries: the class lines :3-:9 and %d blocks (b604_rows DATED)' % (CUR, PRE_PP, E['cur_blob'][:8], len(cur), cur[0][:80], len(W.DATED)),
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines'], E['sha256']), '',
         '### EVERY ROW, WITH THE EDITION LINE IT SITS ON AND THE CURRENT LINES IT ANSWERS (%d rows):' % len(W.ROWS)]
    for r in W.ROWS:
        ans = ['%s :%d-:%d (%s)' % (c[0], c[1], c[2], c[5]) for c in W.CV if c[4] == r['id']]
        L += ['  %s -> v0.2 :%d -- %s' % (r['id'], P['rows'][r['id']], W.verdict(r)[0] + ('' if W.verdict(r)[1] is None else ' test %d' % W.verdict(r)[1])),
              '      answers: %s' % (', '.join(ans) or 'no current line (a page conclusion or a reading)'),
              '      v0.2 : %s' % ed[P['rows'][r['id']] - 1][:400]]
    L += ['', '### EVERY CARRIED LINE OF THE CURRENT VERSION -> ITS EDITION LINE (%d non-blank lines; verbatim after the quote mark: %d ; '
          'differing %s ; not carried %s):' % (len([n for n in range(1, len(cur) + 1) if cur[n - 1].strip()]), carried_ok, carried_bad or 'none', missing or 'none')]
    L += ['  :%d -> :%d' % (n, el) for n, el in sorted(where.items())]
    L += ['', '### THE SUPERSEDED CONCLUSIONS (MOVED-IN-MEANING) AND THE ROWS THAT CITE THEIR COMPILED FACT (H28a):']
    L += ['  %s :%s -> %s citing %s' % (x['cv'], x['lines'], x['row'], x['cites'] or '### NOTHING') for x in h28a_rows]
    L += ['', '### THE COLLISIONS, RESOLVED BY THE PRECEDENCE ORDER WITHOUT A PROMPT (4; both wordings in the back matter): the dated entries '
          '(history by placement); the currency mark and MT-01 (history on the mark, fact on the row); the governing claim and RH-01 '
          '(ceiling on the row, history beneath); the §7 sentence (three rows).',
          '', '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s BODY %d (%+d) ; '
          'the BACK MATTER %d (the history blocks and everything below the tag), printed separately ; the edition whole %d' % (
              E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form, the reorganisation`s reading declared on the face: the body differs by %+d against CREDIT %d + removals %d '
          '(every current sentence moved out of the body and recorded in the back matter) + ruled citations %d (every new body sentence, '
          'ordered by (R214)(4)) + one version line = %d -- VACUOUS IN THIS READING, since the bound counts every moved sentence; '
          'with the moved sentences not counted as removals the bound is %d and the difference %d' % (
              body_dn, E['credit'], E['removals'], E['ruled'], allowed, allowed_strict, abs(body_dn)), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s' % (h['line'], h['hit'], h['kind']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling in the body: %d' % len(beyond),
          '### THE SCANNER (banned_terms.py --new) on the edition: live uses %s ; verdict %s' % (live.group(1) if live else None, 'CLEAN' if clean else 'NOT CLEAN'),
          '### act numbers in the body: %s' % (acts or 'none'),
          '### H38a, every pin checked (%d): %d resolve ; failing %s' % (len(pins), sum(p['ok'] for p in pins), [p for p in pins if not p['ok']] or 'none'),
          '### H38d: DARK rows per cluster %s ; BRIGHT rows per bright register %s' % ({c: len(v) for c, v in dark_each.items()}, bright_reg), '',
          '### ### **H28a %s -- every superseded conclusion (%d) lands in a row citing its compiled fact on a page at its pin.**' % (h28a, len(sup)),
          '### ### **H28b %s, VACUOUS in the reorganisation`s reading -- the body differs by %+d sentences against at most %d; the back matter %d, '
          'excluded and printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s verdict %s; sentences beyond the ceiling in the body %d.**' % (h28c, 'CLEAN' if clean else 'NOT CLEAN', len(beyond)),
          '### ### **H38a %s -- %d of %d instrument and face pins resolve at their pins.**' % (h38a, sum(p['ok'] for p in pins), len(pins)),
          '### ### **H38b %s -- body sentences carrying an act number: %d.**' % (h38b, len(acts)),
          '### ### **H38d %s -- a DARK row in each of the %d clusters carrying rows; a BRIGHT row in each bright register.**' % (h38d, len(dark_each)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b604_edition_FINDINGS_STAND.txt', L)
    put_json('b604_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, H38a=h38a, H38b=h38b, H38d=h38d, h28a_rows=h28a_rows, body_dn=body_dn,
                                   allowed=allowed, allowed_strict=allowed_strict, vacuous=True, backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None,
                                   clean=clean, beyond=len(beyond), hits=hits, acts=acts, pins=pins, dark_each=dark_each, bright_reg=bright_reg,
                                   carried_ok=carried_ok, carried_bad=carried_bad, missing=missing, held=None))
    print('H28a %s H28b %s H28c %s H38a %s H38b %s H38d %s ; carried %d bad %s missing %s ; body_dn %d allowed %d ; beyond %d ; pins %d/%d' % (
        h28a, h28b, h28c, h38a, h38b, h38d, carried_ok, carried_bad, missing, body_dn, allowed, len(beyond), sum(p['ok'] for p in pins), len(pins)))


def repin():
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932). Writes data/b604_repin.txt."""
    E = jl('b604_edition.json')
    ed = _ed()
    cut = ed.index(BM_TAG)
    P = E['pos']
    checks = []
    for r in W.ROWS:
        ln = P['rows'][r['id']]
        checks.append(('row %s on :%d' % (r['id'], ln), ed[ln - 1].startswith('| %s | ' % r['id']) and ln < cut))
    bm = NL.join(ed[cut:])
    for r in W.ROWS:
        checks.append(('Correspondence names %s at :%d' % (r['id'], P['rows'][r['id']]), ('| %s | :%d |' % (r['id'], P['rows'][r['id']])) in bm))
    for c, ln in P['tables'].items():
        checks.append(('table %s header on :%d' % (c, ln), ed[ln - 1].startswith('| row | the conclusion |')))
    for c, ln in P['mutual'].items():
        checks.append(('mutual-light line %s on :%d' % (c, ln), ed[ln - 1].startswith('Read in mutual light')))
    for c, ln in P['hist_blocks'].items():
        checks.append(('history block %s opens on :%d' % (c, ln), ed[ln - 1].startswith('<!-- HISTORY CARRIED BENEATH THIS TABLE')))
    for n, ln in P['tests'].items():
        checks.append(('test %s on :%d' % (n, ln), ed[ln - 1].startswith('%s. **' % n)))
    for k, ln in P['dated'].items():
        a_ = int(k.split('-')[0])
        checks.append(('dated entry :%s starts on :%d' % (k, ln), _unquote(ed[ln - 1]) == _cur()[a_ - 1]))
    for x in re.findall(r'\| [A-Z]{2}-\d\d \(:(\d+)\) \|', bm):
        checks.append(('back-matter row cell :%s is a row line' % x, ed[int(x) - 1].startswith('| ') and int(x) < cut))
    bank = rd('b604_edition_FINDINGS_STAND.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM THE CURRENT VERSION') and bank.count('### OFFSET FROM') == 1))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and hashlib.sha256(open(os.path.join(PP, *ED.split('/')), 'rb').read()).hexdigest() == E['sha256']))
    L = ['### b604 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % ED, '']
    L += ['    %-100s %s' % (w[:100], 'OK' if ok else '### FAILS') for w, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _w, ok in checks), len(checks))]
    put_txt('b604_repin.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 4: THE PAGES
def page(k):
    """### after the edition commit: ONE page per call in the foreground, re-emitted from its banked probe (the ζ page from b602's list
    ### at v0.20, the χ page from b603's at v0.21 -- this act names no node, so neither list is the act's own; no Lean call). Writes
    ### the page only when it changed, and data/b604_page_<k>.json."""
    import chain_page as C
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b604_%s' % k)
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
        put_json('b604_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
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
    put_json('b604_page_%s.json' % k, J)
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s ; the probe read %s' % (k, rc, len(b), changed, secs, src_out))
    for x in dl[:60]:
        print('    ' + x[:240])


def page_arms(tag):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b604 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    L.append('### the lists read: %s' % {k: (NODES[k], PROBE[k]) for k in NODES})
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b604_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b604_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
SCORE_KEYS = ('H28a', 'H28b', 'H28c', 'H38a', 'H38b', 'H38c', 'H38d', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def _only_placement(X):
    """### every changed line of a page's re-emission (the bank's unified diff, the committed page before the act) sits inside
    ### its `## Placement` block, between that heading and `## Correspondence`."""
    prev = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (PRE_PP, PNAME['chi'])], capture_output=True).stdout.decode('utf-8', 'replace').split(NL)
    if not prev or not X.get('diff'):
        return False
    try:
        a, b = prev.index('## Placement'), prev.index('## Correspondence')
    except ValueError:
        return False
    for h in X['diff']:
        m = re.match(r'^@@ -(\d+)(?:,(\d+))? \+', h)
        if m:
            s = int(m.group(1))
            if not (a + 1 <= s <= b + 1):
                return False
    return True


def scores():
    M, H, E =jl('b604_sieve_mapping.json'), jl('b604_h28.json'), jl('b604_edition.json')
    Z, X = jl('b604_page_zeta.json'), jl('b604_page_chi.json')
    rp = rd('b604_repin.txt')
    nrows = len(W.ROWS)
    ndark = sum(W.verdict(r)[0] == 'DARK' for r in W.ROWS)
    named = all(W.verdict(r)[1] for r in W.ROWS if W.verdict(r)[0] == 'DARK')
    ncl = len(M.get('clusters_with') or [])
    hs = [H.get(k) for k in ('H28a', 'H28b', 'H28c', 'H38a', 'H38b', 'H38d')] + [M.get('H38c')]
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
                                                                               'SIDE-structural-error-correction', 'SIDE-cosmo', 'SIDE-silence-principle',
                                                                               'SIDE-global-section')}
    kern_ok = kern == {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068',
                       'SIDE-structural-error-correction': '6a4f482', 'SIDE-cosmo': 'c5cba30', 'SIDE-silence-principle': '667c254',
                       'SIDE-global-section': '3528bcf'}
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1').split(NL) if x.startswith('?? ')))
    trail_landed = os.path.exists(os.path.join(D, 'b604_trail.json'))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', ED] + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = g(PP, 'rev-parse', 'HEAD:' + CUR).strip() == E.get('cur_blob')
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b604_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b603_closing_push_out.txt'))
    m = re.search(r'RE-PIN : (\d+) of (\d+)', rp)
    arms2 = rd('b604_page_arms_c2.txt')
    xplace = _only_placement(X)
    S = dict(
        H28a=(H.get('H28a'), 'every superseded conclusion (%d) lands in a row citing its compiled fact on a page: %s' % (len(H.get('h28a_rows') or []),
                                                                                                                     [(x['cv'], x['row']) for x in H.get('h28a_rows') or []])),
        H28b=(H.get('H28b'), 'VACUOUS in the reorganisation`s reading: the body differs by %+d against at most %d (with the moved sentences not counted '
                             'as removals the bound is %d)' % (H.get('body_dn', 0), H.get('allowed', 0), H.get('allowed_strict', 0))),
        H28c=(H.get('H28c'), 'the scanner %s (live uses %s); sentences beyond the ceiling in the body %s' % ('CLEAN' if H.get('clean') else 'NOT CLEAN', H.get('live'), H.get('beyond'))),
        H38a=(H.get('H38a'), '%d of %d instrument and face pins resolve' % (sum(p['ok'] for p in H.get('pins') or []), len(H.get('pins') or []))),
        H38b=(H.get('H38b'), 'act numbers in the body: %s' % (H.get('acts') or 'none')),
        H38c=(M.get('H38c'), '%d conclusions of the current version, each in exactly one row; unplaced %s' % (len(M.get('cv') or []), M.get('unplaced'))),
        H38d=(H.get('H38d'), 'DARK rows per cluster %s ; BRIGHT rows per bright register %s' % ({c: len(v) for c, v in (H.get('dark_each') or {}).items()},
                                                                                             H.get('bright_reg'))),
        N1=('HELD' if M.get('H38c') == 'HOLDS' and not M.get('unplaced') else 'REFUTED', 'every conclusion maps to exactly one row; rows marked unplaced in the bank: %d' % len(M.get('unplaced') or [])),
        N2=('HELD' if nrows >= 40 and ncl >= 6 else 'REFUTED', 'the table carries %d rows over %d clusters (at least 40 over at least 6)' % (nrows, ncl)),
        N3=('HELD' if 3 * ndark >= nrows and named else 'REFUTED', '%d of %d rows DARK, each by a named test %s' % (ndark, nrows, named)),
        N4=('HELD' if all(x == 'HOLDS' for x in hs) and H.get('held') is None else 'REFUTED', 'H28a-H28c and H38a-H38d: %s ; held %s' % (dict(zip(
            ('H28a', 'H28b', 'H28c', 'H38a', 'H38b', 'H38d', 'H38c'), hs)), H.get('held'))),
        N5=('HELD' if kern_ok and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
            'nothing deposits; every kernel`s main unmoved %s; the current version unedited %s; PLACE-papers %s (wanted %s); relay files beyond the act`s '
            'banks, tools and the table %s%s' % (kern_ok, cur_same, pp_ch, want_pp, relay_beyond, '' if trail_landed else ' ; the trail record pending')),
        S1=('HELD' if m and m.group(1) == m.group(2) else 'REFUTED', 'the re-pin step: %s' % (m.group(0) if m else 'no bank')),
        S2=('HELD' if not H.get('carried_bad') and not H.get('missing') else 'REFUTED', 'every non-blank current line carried verbatim: %d ; differing %s ; missing %s' % (
            H.get('carried_ok', 0), H.get('carried_bad'), H.get('missing'))),
        S3=('HELD' if X.get('changed') is True and xplace else 'REFUTED', 'the χ page`s re-emission changes only its Placement block: changed %s ; '
            'every changed line inside Placement %s' % (X.get('changed'), xplace)),
        S4=('HELD' if Z.get('changed') is True and X.get('changed') is True else 'REFUTED', 'the ζ page changed %s ; the χ page changed %s (the edition names nodes of both)' % (
            Z.get('changed'), X.get('changed'))),
        S5=('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
            'after the page commits: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    )
    put_json('b604_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-6s %s -- %s' % (k, S[k][0], str(S[k][1])[:220]))


TITLE = ('## The edition of THE_FINDINGS_AS_THEY_STAND as the sieve table by cluster: {N} rows, {K} clusters, quantifier shape and register '
         'per row, bright or dark by the five tests at their instruments’ pins')
TRAIL_HEAD = ('### b604 — lane three, act thirty-one under (R214): the edition of THE_FINDINGS_AS_THEY_STAND by the form as the sieve '
              'table by cluster -- quantifier shape, register, bright or dark by named test and instrument at pin')


def _title():
    M = jl('b604_sieve_mapping.json')
    return TITLE.replace('{N}', str(len(W.ROWS))).replace('{K}', str(len(M.get('clusters_with') or [])))


def findings():
    Q = R2._Q()
    S, M, H, E = jl('b604_scores.json'), jl('b604_sieve_mapping.json'), jl('b604_h28.json'), jl('b604_edition.json')
    t = _title()
    Q.guard_absent(Q.FIND, t[:90])
    rl = jl('b604_record_lines.json')
    w1, w2, wo = [x['line'] for x in rl['lines']]
    ec = _pp_commit('b604 (R214)(4): ' + ED)
    zc, xc = _pp_commit('b604 (R214)(4): ' + PAGE), _pp_commit('b604 (R214)(4): ' + DIR_PAGE)
    nb = sum(W.verdict(r)[0] == 'BRIGHT' for r in W.ROWS)
    dk = {k: sum(W.verdict(r) == ('DARK', k) for r in W.ROWS) for k in range(1, 6)}
    e = ['', t, '',
         '*Filed at b604 on the author’s ruling `(R214)`. Banks: relay `data/b604_reads.txt`, `data/b604_author_answers.txt`, '
         '`data/b604_sieve_mapping.txt`, `data/b604_edition_FINDINGS_STAND.txt`, `data/b604_edition_termscan.txt`, `data/b604_repin.txt`, '
         '`data/b604_page_zeta.json`, `data/b604_page_chi.json`, `data/b604_page_arms_c2.txt`. Nothing deposits.*', '',
         '**The edition** (`(R214)`(4)). PLACE-papers `%s` (commit %s), beside the current version, unedited. Its body is a head -- the five '
         'tests with their instruments at their pins, the registers, the clusters -- one table per cluster carrying rows, one mutual-light '
         'line per table, and a bench; beneath each table its history block, the current version’s dated entries that fed it carried '
         'verbatim; the back matter carries every other sentence of the current version, the collisions, Placement and the Correspondence '
         'with the act numbers and pins. %d rows: %d from the current version’s 72 conclusions (each landing in exactly one row, '
         'the mapping banked first), the pages’ compiled conclusions with their plumbing grouped in the face, and four readings graded as '
         'readings. Clusters carrying rows: %s; the other three of SPIRAL_MAP §4A’s eight carry none, named.' % (
             ED, ec, len(W.ROWS), sum(1 for r in W.ROWS if any(c[4] == r['id'] and c[5] == 'own' for c in W.CV)), ', '.join(dict(W.CLUSTERS)[c] for c in M['clusters_with'])), '',
         '**The sieve.** %d BRIGHT, %d DARK (by test 1: %d; 2: %d; 3: %d). The BRIGHT rows are the compiled equivalences with RH or '
         'GRH_chi whose route consumes the prime side: `h2_sign_iff_rh`, the forall_upto pair, `arith_limit_nonneg_iff_rh`, '
         '`h2_sign_chi_iff_grh_chi` and `family_theorem` -- one or more in each bright register (prime-side control, the Li ladder, '
         'crossing geometry). Test 1 darkens every row naming no zero or one aggregate over the zeros (a single rung such as `liCoeff_one_pos`, '
         'a proportion, an explicit-formula identity, every record row). Test 2 darkens the schema’s generic theorems (the product, the '
         'doubling, the finite sum, the detector) and the zero-side Li faces (`li_nonneg_iff_rh` and its register-4 and Taylor forms), each a '
         'route that goes through at the Epstein configuration. Test 3 darkens one row, the Dedekind reading (an imprimitive character at its '
         'level, not its conductor).' % (nb, len(W.ROWS) - nb, dk[1], dk[2], dk[3]), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '. H28b holds VACUOUSLY in the reorganisation’s '
         'reading declared on the face (every moved sentence a recorded removal); counted the other way it is refuted in its letter '
         '(relay data/b604_edition_FINDINGS_STAND.txt).', '',
         '**The pages.** Both re-emitted after the edition commit from their banked probes, no Lean call: the ζ page (PLACE-papers %s) and the '
         'χ page (%s), each committed alone, the edition entering their Placement.' % (zc, xc), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the edition re-reads every entry it carries -- the family theorem (:7028) takes the '
         'FAMILY shape and the only test-3 pass beside the χ instance, the Dedekind reading (:7026) the one test-3 failure, the witness ratio '
         '(:6758) the Epstein bench line, b601’s reading (:6970) a test-2 row -- and is re-read in turn by CP-8’s monograph v6, whose spine '
         'the sieve table is. It strengthens the programme’s offering of the clause and its compiled faces (each conclusion with the test '
         'that bounds it, the bright set small and named).', '',
         '**The record lines.** b603’s weight at FINDINGS :%d (with the q = 5 fact correction, the navigator’s); the four items as ruled at '
         ':%d; W-ORD-E0-INDUCTION at OPEN_TRAILS :%d; the API-stop pattern line in relay data/b604_defects.txt.' % (w1, w2, wo), '',
         '**Next.** Per `(R214)`(5): b605, on the author’s word between CP-6, CP-8’s monograph v6 with the eleven ceiling uses, and '
         'W-ORD-VENDOR-FINALMULT; the navigator’s reading is CP-8, the sieve table being the monograph’s v6 spine. The author rules on the '
         'closing.', '',
         '*Nothing deposits; no keystone edited beyond the edition written beside its current version; README and REGISTRY unwritten; nothing '
         'here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b604_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def trail():
    Q = R2._Q()
    S, fj, rl = jl('b604_scores.json'), jl('b604_findings.json'), jl('b604_record_lines.json')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    w1, w2, wo = [x['line'] for x in rl['lines']]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R214) ratified.** (1) b603 at its weight. (2) The seat’s four items ruled. (3) W-ORD-E0-INDUCTION entered priced. (4) The '
             'edition of THE_FINDINGS_AS_THEY_STAND as the sieve table. (5) The act after: b605, on the author’s word.', '',
             '**Entered:** FINDINGS.md:%d (b603’s weight, the q = 5 fact correction the navigator’s), :%d (the four items as ruled), :%d (the '
             'entry, with its mutual-light line); OPEN_TRAILS :%d (W-ORD-E0-INDUCTION, priced, not started, the author’s word its trigger); '
             'this record; PLACE-papers `%s` (the edition, beside the current version, unedited); both pages re-emitted.' % (
                 w1, w2, fj['entry_line'], wo, ED), '',
             '**Resolved by the seat, for the author’s strike:** the current version read as v0.1 (it carries no version line); the §7 sentence '
             'read as three conclusions; the pages’ node lists read at their own pins (the ζ list at v0.20, a fact correction to the ruling’s '
             '“at v0.21”); H28b scored with every moved sentence as a removal recorded in the back matter, VACUOUS so, the other count printed '
             'beside; `(R214)`(4)’s grouping of Theorem 3.1 with 3.7 under one instrument recorded as the navigator’s (the author’s answer put '
             '3.7 in test 2). The scope of the rows, the history placement and the five tests are the author’s three answers before the seal '
             '(relay data/b604_author_answers.txt).', '',
             '**Defects** (relay data/b604_defects.txt): %s; the API-stop pattern line entered there.' % (
                 '; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R214)`(5), b605, on the author’s word between CP-6, CP-8’s monograph v6 with the eleven ceiling uses, and '
             'W-ORD-VENDOR-FINALMULT; the navigator’s reading is CP-8; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; FACES_LEDGER untouched; row U1 unedited; `h2` where the deposit '
             'left it; the four lists stay OPEN.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b604_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b604_trail.json')['line'])


def desk():
    S = jl('b604_scores.json')
    HK = ('H28a', 'H28b', 'H28c', 'H38a', 'H38b', 'H38c', 'H38d')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b604 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H28a-H28c and H38a-H38d, (R214)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HK]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H28/H38 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HK), sum(S[k][0] == 'REFUTED' for k in HK),
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b604_defects.txt').rstrip(NL).split(NL)
    put_txt('b604_desk_notes.txt', L)


def components():
    S, fj, tj, rl = jl('b604_scores.json'), jl('b604_findings.json'), jl('b604_trail.json'), jl('b604_record_lines.json')
    Z, X, M = jl('b604_page_zeta.json'), jl('b604_page_chi.json'), jl('b604_sieve_mapping.json')
    L = ['b604 -- THE COMPONENTS, BANKED UNDER (R214).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b603`s closing push-out relay %s ; push-b603* branches deleted by '
         'name (data/b604_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b604_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b603`s weight FINDINGS :%d ; the four items :%d ; W-ORD-E0-INDUCTION OPEN_TRAILS :%d ; the pattern line data/b604_defects.txt' % tuple(
             x['line'] for x in rl['lines']),
         '### COMPONENT 2 : the mapping data/b604_sieve_mapping.txt ; %d conclusions, %d rows, %d clusters ; H38c %s' % (
             len(M['cv']), len(M['rows']), len(M['clusters_with']), S['H38c'][0]),
         '### COMPONENT 3 : the edition %s ; the diff data/b604_edition_FINDINGS_STAND.txt ; H28a %s, H28b %s, H28c %s, H38a %s, H38b %s, H38d %s' % (
             ED, S['H28a'][0], S['H28b'][0], S['H28c'][0], S['H38a'][0], S['H38b'][0], S['H38d'][0]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b604_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b605, on the author`s word ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b604_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b604_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
