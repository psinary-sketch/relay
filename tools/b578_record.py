# -*- coding: utf-8 -*-
"""b578_record.py -- THE ACT'S RECORD TOOL, UNDER (R188). ### ONE SUBCOMMAND PER BANK.

### ### b578: LANE THREE, ACT SIX -- CP-7 ACT THREE, THE EDITION OF PATHS_TO_THE_CRITICAL_LINE. Subcommands write only
### `data/b578_*` unless the docstring names another file. Every bank is written through `put_txt` / `put_json` (encode
### first, then a temp file, then `os.replace`). This act makes no platform call.
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
PRE_PP = '7bd8954'
MIRROR_PIN = '192077f'
CUR = 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md'
ED = 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
WT = 'D:/b577-rerun-b576'
RECITED = 'WRITE-LIST ADDENDUM: tools/mirror_prevbuild.json, carried by (R187)(4)'
REFUSED = 'WRITE-LIST ADDENDUM: tools/mirror_prevbuild.json, carried by (R186)(5)'

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
    '(a) THIS TOOL`S FIRST RUN DID NOT PARSE: two old-sentence literals were patched through a bash heredoc, which collapsed `\\\'` to '
    '`\'` (the standing heredoc trap) and left two unterminated strings. Nothing was written by that run; the two literals were '
    're-written double-quoted and the tool parsed before its next run.',
    '(b) THE RE-RUN COUNTED ITS OWN SCAFFOLDING: reading (ii) placed relay data/b577_ferry.txt in the worktree so the form could read '
    '(R187), and b577`s re-run had left data/b577_b576_rerun.txt there; b576`s write-list arm counts every untracked file of the '
    'worktree as written, and neither is a b576_* file, so G-WRITELIST-KINDS fails on these two and no longer on '
    'tools/mirror_prevbuild.json. The face did not foresee it. The count is banked as it stands (data/b578_b576_rerun.txt), each cause '
    'printed (data/b578_rerun_diagnosis.txt); no file was removed from the worktree to improve the count.',
    '(c) THE SUITE`S FIRST PRE-PUSH RUN READ 65 OF 67 ON TWO ARMS OF ITS OWN BUILDING: G-DELETE-FREE`s added needle (the worktree-removal '
    'subcommand) matched the prose "the worktree removed" in this act`s record tool -- a needle that caught a word, not a call -- and was bounded '
    'to a call (`\\b`); the first repair went through sed, which collapsed `\\\\b` to `b` (the heredoc species again), caught by reading '
    'the line back before the run. G-H28A-CITES compared a pin with its backticks stripped against the page`s line 3, which keeps them, '
    'and so refused every Correspondence-row citation; it now strips both sides. Nothing else changed; the second run read 67 of 67.',
]


def rerun_diagnosis():
    """### Each failing arm of b576`s re-run, its cause read on its own evidence: data/b578_rerun_diagnosis.txt."""
    import addenda as ADD
    rr = rd('b578_b576_rerun.txt')
    m = re.search(r"uncovered (\[[^\]]*\])", rr)
    unc = json.loads(m.group(1).replace("'", '"')) if m else []
    acc = ADD.accepted_bases(rd('b576_writelist_addendum.txt'), ADD.paste_reader(D))
    still = [f for f in unc if f.split('/')[-1] not in acc]
    pdj = jl('b576_purpose_drafts.json')
    fb = {r: g(PP, 'show', '%s:FINDINGS.md' % r) for r in (MIRROR_PIN, 'HEAD')}
    drafts = {k: (v['text'][:80] in fb[MIRROR_PIN], v['text'][:80] in fb['HEAD']) for k, v in pdj['drafts'].items()}
    src = re.search(r'source HEAD: (\w+)', rd('b576_mirror_build.txt'))
    remote = g(PP, 'ls-remote', 'origin', 'refs/heads/main')[:7]
    fail = re.search(r"LIVE FAILING : \d+ (\[[^\]]*\])", rr)
    L = ['b578 -- COMPONENT 1: b576`S RE-RUN, EACH FAILING ARM READ ON ITS OWN EVIDENCE', '',
         '### the re-run: %s' % (re.search(r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\.', rr).group(0) if 'ARMS RUN' in rr else '?'),
         '### failing: %s' % (fail.group(1) if fail else '?'), '',
         '### G-WRITELIST-KINDS -- the arm`s glob-uncovered list as the suite printed it: %s' % unc,
         '    the accepted addenda carry: %s' % sorted(acc),
         '    uncovered by globs AND addenda: %s -- the re-run`s own scaffolding in the worktree (defect (b)); '
         'tools/mirror_prevbuild.json is carried: %s' % (still, 'mirror_prevbuild.json' in acc),
         '### G-DOC-UNWRITTEN -- b576`s suite reads PLACE-papers` live HEAD; each b576 draft`s first 80 characters in FINDINGS at %s / at '
         'HEAD: %s -- Draft B was appended by b577 (FINDINGS :6448), after b577`s own re-run' % (MIRROR_PIN, drafts),
         '### G-MIRROR-AFTER-PUSH -- the mirror build`s source HEAD %s against PLACE-papers` remote main %s now: %s -- b577 pushed '
         'PLACE-papers 7bd8954 after b577`s re-run' % (src.group(1) if src else '?', remote, 'EQUAL' if src and src.group(1) == remote else 'DIFFER'),
         '', '### ### **ONE OF THE THREE IS THE ADDENDUM`S ARM, AND IT NO LONGER FAILS ON THE ADDENDUM`S FILE; TWO READ THE CORPUS AS IT '
         'STANDS AT b578, NOT AS IT STOOD AT b576`S PUSH.**']
    put_txt('b578_rerun_diagnosis.txt', L)
    put_json('b578_rerun_diagnosis.json', dict(uncovered=unc, still=still, carried='mirror_prevbuild.json' in acc, drafts=drafts,
                                               mirror_src=src.group(1) if src else None, remote=remote))


def defects():
    put_txt('b578_defects.txt', ['### b578 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay the PATHS work-list, whole', RELAY, 'HEAD', 'data/b558_editions/PATHS_TO_THE_CRITICAL_LINE.txt', list(range(1, 151))),
    ('PLACE-papers PATHS, its head', PP, PRE_PP, CUR, list(range(1, 20))),
    ('PLACE-papers PATHS, I-bis and the doors', PP, PRE_PP, CUR, list(range(45, 68))),
    ('PLACE-papers PATHS, the two CREDIT lines', PP, PRE_PP, CUR, [240, 291]),
    ('PLACE-papers PATHS, ANNEX A`s honest boundary', PP, PRE_PP, CUR, [359]),
    ('PLACE-papers PATHS, ANNEX B', PP, PRE_PP, CUR, list(range(363, 397))),
    ('PLACE-papers PATHS, the tier block`s head', PP, PRE_PP, CUR, list(range(542, 547))),
    ('PLACE-papers the zeta page at the mirror`s pin, nodes 7, 8, 11, 20', PP, MIRROR_PIN, PAGE, [11, 12, 15, 24]),
    ('PLACE-papers the zeta page, Correspondence rows', PP, MIRROR_PIN, PAGE, [138, 139, 142]),
    ('relay the b538 register census, the five register rows', RELAY, 'HEAD', 'data/b538_census.json', list(range(1, 46))),
    ('PLACE-papers OPEN_TRAILS, the form', PP, PRE_PP, 'OPEN_TRAILS.md', [11864]),
    ('PLACE-papers FINDINGS, the two credits', PP, PRE_PP, 'FINDINGS.md', [5904, 5918]),
    ('relay tools/banned_terms.py, the stems', RELAY, 'HEAD', 'tools/banned_terms.py', list(range(1, 50))),
]


def reads():
    L = ['b578 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    put_txt('b578_reads.txt', L)


# ================================================================================ COMPONENT 1
def addendum_write():
    """### relay data/b576_writelist_addendum.txt rewritten as (R188)(2) orders: the re-cited line, the refused line beneath."""
    t = rd('b576_writelist_addendum.txt').strip()
    if t != REFUSED:
        sys.exit('### THE BANK IS NOT THE REFUSED LINE ALONE -- NOTHING WRITTEN: %r' % t)
    b = (RECITED + NL + REFUSED + NL).encode('utf-8')
    p = os.path.join(D, 'b576_writelist_addendum.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: b576_writelist_addendum.txt (%d bytes)' % len(b))


def addendum_bank():
    """### The bank's two lines, the form's verdicts, the re-run in the worktree."""
    import addenda as ADD
    t = rd('b576_writelist_addendum.txt')
    v = ADD.writelist_addenda(t, ADD.paste_reader(D))
    rr = rd('b578_b576_rerun.txt')
    wt = rd('b578_worktree.txt')
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', rr)
    wt_head = re.search(r'### the worktree`s HEAD before removal : ([0-9a-f]{40})', wt)
    L = ['b578 -- COMPONENT 1: THE ADDENDUM RE-CITED AND THE RE-RUN, (R188)(2)', '',
         '### relay data/b576_writelist_addendum.txt, as rewritten (the re-cited line, the refused line beneath it):']
    L += ['    ' + l for l in t.strip().split(NL)]
    L += ['', '### the form (relay tools/addenda.py, (R177)(3)(g)) on each line:']
    L += ['    %s -> %s ; accepted %s' % (a['line'], a['why'], a['accepted']) for a in v]
    L += ['', '### the re-run of b576`s suite in the kept worktree %s (HEAD %s), the rewritten bank and relay data/b577_ferry.txt '
          'placed in it:' % (WT, wt_head.group(1)[:8] if wt_head else '?')]
    L += ['    ' + l.strip() for l in rr.split(NL) if 'ARMS RUN' in l or 'VERDICT' in l or 'uncovered' in l or 'ADDENDUM' in l]
    acc = [a['accepted'] for a in v]
    L += ['', '### ### **THE RE-CITED LINE IS %s; THE REFUSED LINE BENEATH IT IS %s; THE RE-RUN READS %s OF %s.**'
          % ('ACCEPTED' if acc[:1] == [True] else 'REFUSED', 'REFUSED' if acc[1:2] == [False] else 'ACCEPTED',
             m.group(2) if m else '?', m.group(1) if m else '?')]
    put_txt('b578_addendum.txt', L)
    put_json('b578_addendum.json', dict(lines=[a['line'] for a in v], accepted=acc, why=[a['why'] for a in v],
                                        rerun_run=int(m.group(1)) if m else None, rerun_passing=int(m.group(2)) if m else None,
                                        worktree_head=wt_head.group(1) if wt_head else None))
    print(jl('b578_addendum.json'))


def worktree_before():
    """### `git worktree list` and the worktree's HEAD, before the removal (the seat removes it by its command)."""
    lst = g(RELAY, 'worktree', 'list', '--porcelain')
    head = g(WT, 'rev-parse', 'HEAD').strip()
    L = ['b578 -- COMPONENT 1: THE WORKTREE, (R188)(2)', '', '### `git worktree list` BEFORE the removal:']
    L += ['    ' + l for l in g(RELAY, 'worktree', 'list').strip().split(NL)]
    L += ['### the worktree`s HEAD before removal : %s' % head,
          '### its path listed : %s' % ('worktree ' + WT in lst)]
    put_txt('b578_worktree.txt', L)


def worktree_after():
    """### appends `git worktree list` AFTER the removal, and the path's absence, to the worktree bank."""
    L = rd('b578_worktree.txt').rstrip(NL).split(NL)
    if any(l.startswith('### `git worktree list` AFTER') for l in L):
        sys.exit('### THE AFTER-READING IS ALREADY BANKED')
    lst = g(RELAY, 'worktree', 'list', '--porcelain')
    L += ['', '### `git worktree list` AFTER the removal:']
    L += ['    ' + l for l in g(RELAY, 'worktree', 'list').strip().split(NL)]
    L += ['### its path listed : %s ; the path exists : %s' % ('worktree ' + WT in lst, os.path.exists(WT)),
          '### ### **THE WORKTREE IS %s.**' % ('REMOVED' if ('worktree ' + WT not in lst and not os.path.exists(WT)) else '### NOT REMOVED')]
    put_txt('b578_worktree.txt', L)


def c1_lines():
    """### PLACE-papers OPEN_TRAILS (the re-cited line at b576`s record) and FINDINGS (b577`s weight)."""
    Q = _Q()
    A = jl('b578_addendum.json')
    tr = Q.line_of(Q.OT, '### b576 — lane three, act four under (R186)')
    refused_at = Q.line_of(Q.OT, '*Appended 2026-10-01 by b577 to b576’s record (:%s), under the author’s ruling `(R187)`(4) -- THE WRITE-LIST ADDENDUM:*' % tr)
    wt = rd('b578_worktree.txt')
    gone = '### ### **THE WORKTREE IS REMOVED.**' in wt
    h = '*Appended 2026-10-01 by b578 to b576’s record (:%s), under the author’s ruling `(R188)`(2) -- THE WRITE-LIST ADDENDUM, RE-CITED:*' % tr
    Q.guard_absent(Q.OT, h)
    out = [Q.append_to(Q.OT, '\n%s %s. Written in place of the refused line at :%s, which stays beneath it as the record of the refusal '
                             '(relay `data/b576_writelist_addendum.txt` carries both, the re-cited line first). Read by the form of '
                             '`(R177)`(3)(g): %s -- `(R187)`(4) names the file. b576’s suite, re-run in the kept worktree D:\\b577-rerun-b576 '
                             '(HEAD %s), reads %s of %s (relay `data/b578_b576_rerun.txt`); the worktree was then %s by its verified absolute '
                             'path after `git worktree list` showed it (relay `data/b578_worktree.txt`).\n'
                             % (h, RECITED, refused_at, 'ACCEPTED' if A['accepted'][:1] == [True] else 'REFUSED',
                                (A['worktree_head'] or '?')[:8], A['rerun_passing'], A['rerun_run'], 'removed' if gone else 'NOT removed'))]
    e = Q.line_of(Q.FIND, '## CP-7, act two: the purpose statement appended to FINDINGS')
    hw = '*Appended 2026-10-01 by b578 to b577’s entry (:%s), under `(R188)`(1) -- b577 AT ITS WEIGHT:*' % e
    Q.guard_absent(Q.FIND, hw)
    out.append(Q.append_to(Q.FIND, '\n%s the purpose statement stands at :6448 (Draft B with the two amendments, the supersession line for '
                                    ':7; :7 and :9 unchanged); the head placement struck as the navigator’s, the shift recorded (10 lines; about '
                                    '115 citations in PLACE-papers, 874 in relay); the edition form standing for CP-7 at OPEN_TRAILS :11864; the '
                                    'order printed; the suite 61 of 61 at b577; b576’s re-run still 68 of 69 then, because the cited clause did not '
                                    'name the file; the seat’s refusal to re-cite without the author’s word correct.\n' % hw))
    put_json('b578_c1_lines.json', dict(trail=tr, refused_at=refused_at, ot_line=Q.line_of(Q.OT, h), weight=Q.line_of(Q.FIND, hw),
                                        entry=e, appends=out))
    print(jl('b578_c1_lines.json'))


# ================================================================================ COMPONENT 2
ORDER_TEXT = ('PATHS (29), FOUNDATIONS (16), ADDITIVE_MULTIPLICATIVE_CONSPIRACY (13), then SURROUND, GRH_CASCADE, R_CURVE, INVARIANCE '
              '(10 each, census order), INDEX_ARITY, ENUMERA (9), SIMPLICITY (5), LICENSE (4), TECHNE (3), E_DIFFICULTY (2), RESIDUE (1)')


def order_line():
    """### PLACE-papers OPEN_TRAILS: the ratified order, the three placements and the two holds, at lane three and the form."""
    Q = _Q()
    lane = Q.line_of(Q.OT, "> LANE THREE — THE CLARIFIED LAYER, after lane two's (a) and (b) at least")
    form = Q.line_of(Q.OT, '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three')
    h = ('*Appended 2026-10-01 by b578, under the author’s ruling `(R188)`(3), to the critical path’s lane three (:%s) and the form of an '
         'edition (:%s) -- THE ORDER OF THE EDITIONS, RATIFIED AS PRINTED:*' % (lane, form))
    Q.guard_absent(Q.OT, h)
    r = Q.append_to(Q.OT, '\n%s %s. Placed: the monograph (31) is CP-8’s object and its edition is v6, not a CP-7 act; '
                          'BALANCE_AND_POSITIVITY (14) and FACES_OF_H2 (1) take editions by the same form after the fourteen, in that order, '
                          'as Tier K companions. HELD: SILENCE_STAGES and REPARAMETERIZATION, having no work-list, until CP-1b’s instrument '
                          'is run on them in one act after the fourteen, or ruled unchanged by the author then (relay '
                          '`data/b577_edition_order.txt`, `data/b578_ferry.txt`).\n' % (h, ORDER_TEXT))
    put_json('b578_order.json', dict(line=Q.line_of(Q.OT, h), lane=lane, form=form, text=ORDER_TEXT, append=r))
    print(jl('b578_order.json'))


# ================================================================================ COMPONENT 3 -- THE EDITION
PIN = {  # ### the declaration, and its pin AS THE ZETA PAGE PRINTS IT (reading (iv))
    'ch_iff_rh': 'v0.1 = `baed4df`', 'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'li_nonneg_iff_rh': 'v0.9 = `e5a5a83`',
    'not_register1': 'v0.11 = `19b7d1e`', 'mellin_Phi_eq_zero_of_re_le_one': 'v0.11 = `19b7d1e`',
    'register5_output_holds': 'v0.11 = `19b7d1e`',
}
PAGE_NODE = {'ch_iff_rh': 7, 'h2_sign_iff_rh': 8, 'li_nonneg_iff_rh': 20}
PAGE_ROW = {'not_register1': 139, 'mellin_Phi_eq_zero_of_re_le_one': 138, 'register5_output_holds': 142}
EF = 'SIDE-explicit-formula'
CH = '`ch_iff_rh`, %s %s' % (EF, PIN['ch_iff_rh'])
H2 = '`h2_sign_iff_rh`, %s %s' % (EF, PIN['h2_sign_iff_rh'])
LI = '`li_nonneg_iff_rh`, %s %s' % (EF, PIN['li_nonneg_iff_rh'])
MP = '`mellin_Phi_eq_zero_of_re_le_one`, %s at the page’s pin %s' % (EF, PIN['mellin_Phi_eq_zero_of_re_le_one'])
NR = '`not_register1`, %s at the page’s pin %s' % (EF, PIN['not_register1'])
R5 = '`register5_output_holds`, %s at the page’s pin %s' % (EF, PIN['register5_output_holds'])
R3B = 'relay `data/b538_census.json` :23'
LIT = 'two uncompiled literature premises (Bombieri–Lagarias `ExplicitFormulaDecomp`, Voros `TailBoundPremise`) and verified zeros'

# ### (line, the fragment of the line replaced, its replacement, the reading the sentence falls under, the declarations cited)
# ### A row whose marked sentence is a whole table row keeps its cells; the fragment is the cell text the work-list moves.
REWRITES = [
    (45, '`goal ⇐ h1 ∧ h2`; **h1 complete at Φ** (only h2 open)',
     '`goal ⇐ h1 ∧ h2`; **h1 complete at Φ**, and lv’s h2 at Φ, `mellin Φ (s/2) ≠ 0`, is false at every s with re s ≤ 1 (%s), so the goal '
     'state closes nothing on the strip -- the open clause is `h2_sign`, equivalent to RH (%s)' % (MP, H2), 3),
    (46, 'finite-range certificate λ_n ≥ 0 for n ≤ N₀(T)≈2T² (Voros threshold), on-line term proved; **finite-set conjunct now DERIVES** '
         '(`lowFinset_mem_iff`, v0.10.0); all-n tail open',
     'finite-range λ_n ≥ 0 for n ≤ N₀(T)≈2T² (Voros threshold), a certificate conditional on %s -- T1-lit; on-line term proved; '
     '**finite-set conjunct now DERIVES** (`lowFinset_mem_iff`, v0.10.0); the all-n statement is RH itself (%s)' % (LIT, LI), 2),
    (59, 'so `ConservationHypothesis` can be discharged rather than assumed',
     'and `ConservationHypothesis` is RH restated (%s), so discharging it is proving RH' % CH, 1),
    (63, '**The goal state.** The programme reduces to `goal ⇐ h1 ∧ h2`.',
     '**The goal state.** lv’s goal state is `goal ⇐ h1 ∧ h2`, and its h2 at Φ, `mellin Φ (s/2) ≠ 0`, is false at every s with re s ≤ 1 '
     '(%s), so that reduction closes nothing on the strip.' % MP, 0),
    (63, '**`h2` is the single open premise — and it is a statement, not a count:** *every ξ-zero forces the Euler balance at some prime* '
         '(the conservation register, in the W-7 existential form — balance at *some* prime, kernel v1.3 = `0bc21c0`).',
     '**`h2_sign` is the single open premise — and it is a statement, not a count:** Weil positivity on classK, equivalent to RH (%s), '
     'whose conservation register, *every ξ-zero forces the Euler balance at some prime* (the W-7 existential form, kernel v1.3 = '
     '`0bc21c0`), is RH restated (%s).' % (H2, CH), 3),
    (67, '**The positivity door, ajar (II.7).** The R4 face already carries a finite-range certificate: '
         '`PartialPositivity.partialPositivity_finiteRange` (SIDE-lv-conservation v0.8.0 = `6efa9e5`), λ_n ≥ 0 for 1 ≤ n ≤ N₀(T) ≈ 2T², '
         'with on-line-term nonnegativity **proved** (`blTerm_nonneg_of_onLine`).',
     '**The positivity door, ajar (II.7).** The R4 face carries a finite-range certificate conditional on %s, T1-lit: '
     '`PartialPositivity.partialPositivity_finiteRange` (SIDE-lv-conservation v0.8.0 = `6efa9e5`), λ_n ≥ 0 for 1 ≤ n ≤ N₀(T) ≈ 2T² under '
     'those premises, with on-line-term nonnegativity **proved** (`blTerm_nonneg_of_onLine`), while λ_n ≥ 0 at every n is RH itself (%s).'
     % (LIT, LI), 2),
    (67, 'This is the **nearest-approach** door: the all-doors proximity, farthest first, runs R5 → R3 (h2 raw) → R1/R2 (named premises) → '
         '**R4 (here)**.',
     'Read against the b538 census and the page, the five registers are not doors at five distances but a star on RH: R1 is false as '
     'stated (%s), R2 is RH restated (%s), R4 is RH in the Weil form and in the Li form (%s, and %s), R5’s output face is a theorem as '
     'stated (%s), and R3 is undecided (%s).' % (NR, CH, H2, LI, R5, R3B), 1),
    (255, "C₅-output (Hilbert–Pólya) stays disclaimed; h2 remains the bracket's outstanding obligation, research-reach.*",
     'C₅-output (Hilbert–Pólya) stays disclaimed; the bracket’s h2 at Φ is false at every s with re s ≤ 1 (%s), so the obligation it '
     'leaves is `h2_sign`, equivalent to RH (%s), research-reach.*' % (MP, H2), 3),
    (257, "`h1_complete_at_Phi` discharges h1's certifiable surround, so h2 stands alone as the single open proposition — localization "
          'sharpened, h2 itself not shortened; the register-equivalence and partial-positivity interfaces are its doors (Program Two iii, '
          'iv), to be opened only at statement-read + price + ruling.',
     '`h1_complete_at_Phi` discharges h1’s certifiable surround, and lv’s h2 at Φ is false at every s with re s ≤ 1 (%s), so the single '
     'open proposition is `h2_sign`, equivalent to RH (%s) — localization sharpened, the clause itself not shortened, the conservation '
     'register and Li positivity compiled as faces of that clause (%s, and %s), not doors to it (Program Two iii, iv).' % (MP, H2, CH, LI), 3),
    (259, 'R5-output was repaired at P2 from a trivially-true draft to the positive-definite-pairing + operator schema of Hilbert–Pólya '
          '(analytic content disclaimed, the C₅ distance, O.18). h1 done, h2 the one open obligation.',
     'R5-output was repaired at P2 from a trivially-true draft to the positive-definite-pairing + operator schema of Hilbert–Pólya '
     '(analytic content disclaimed, the C₅ distance, O.18), and the repaired face is true as stated (%s). h1 done, lv’s h2 at Φ false on '
     'the strip (%s), `h2_sign` the one open obligation, equivalent to RH (%s).' % (R5, MP, H2), 3),
    (294, 'C₅-output disclaimed, h2 outstanding',
     'C₅-output disclaimed; lv’s h2 at Φ false at every s with re s ≤ 1 (%s); the outstanding clause is `h2_sign`, equivalent to RH (%s)'
     % (MP, H2), 3),
    (295, '(the T3 shared-witness edge; sevenClasses h1 via `h1_complete_at_Phi`, only h2 open)',
     '(the T3 shared-witness edge; sevenClasses h1 via `h1_complete_at_Phi`; its h2 at Φ is false at every s with re s ≤ 1, so the edge is '
     'vacuous on the strip, %s; the open clause is `h2_sign`, %s)' % (MP, H2), 1),
    (297, 'named premise: `ConservationHypothesis` (the statement is',
     'named premise: `ConservationHypothesis`, which is RH restated (%s), so the terminal encodes its conclusion (the statement is' % CH, 1),
    (322, '| **discharge h2** | implication compiled; live math sits in the open antecedent |',
     '| **prove RH** — the antecedent `ConservationHypothesis` is RH restated (%s) | implication compiled; it encodes its conclusion: the '
     'live mathematics in the antecedent is RH itself |' % CH, 1),
    (323, '| **conditional-A** *(on h2)* | **discharge h2** | h1 closed (`h1_complete_at_Phi`); h2 open |',
     '| **conditional-A** *(on lv’s h2, false on the strip)* | **none on the strip** — lv’s h2 at Φ is false at every s with re s ≤ 1 (%s), '
     'so the goal state is vacuous there | h1 closed (`h1_complete_at_Phi`); the open clause is `h2_sign`, equivalent to RH (%s) |' % (MP, H2), 3),
    (326, '| **discharge h2** (effective dominance = catalogue exhaustiveness) |',
     '| **discharge `h2_sign`** (effective dominance = catalogue exhaustiveness), and `h2_sign` is equivalent to RH (%s), so the '
     'conditional’s premise is RH itself |' % H2, 0),
    (332, '**RH proper** is reached only *conditionally on h2* (Route 3, T3 goal state) or as a *B-with-named-tail* (R4).',
     '**RH proper** is reached by no conditional route short of RH: Route 3’s condition is RH restated (%s), the T3 goal state is vacuous on '
     'the strip (%s), and R4’s named tail at every n is RH itself (%s).' % (CH, MP, LI), 1),
    (332, 'Every conditional route turns on the one hinge, h2 — highest-leverage move;',
     'Every conditional route turns on the one hinge, `h2_sign`, equivalent to RH (%s) — highest-leverage move;' % H2, 3),
    (379, '| proven **in-kernel** — a **certificate, not RH** (cutoff = the detection threshold) |',
     '| compiled **in-kernel under %s** -- T1-lit, a **conditional certificate, not RH** (cutoff = the detection threshold); at every n it '
     'is RH (%s) |' % (LIT, LI), 2),
    (450, 'on which `partialPositivity_finiteRange` proves positivity **to the detection threshold N₀**.',
     'on which `partialPositivity_finiteRange` gives positivity **to the detection threshold N₀** only under %s (T1-lit), positivity at '
     'every n being RH (%s).' % (LIT, LI), 2),
]
READING_NAME = {0: 'none -- resolved by the form', 1: '(i) the pentagon', 2: '(ii) the honest boundary', 3: '(iii) the single open premise'}

# ### reading (vi), the author's answer: each use takes the object the sentence names, no synonym for the stem
STEMS = [
    (67, '(the all-n tail is the open gap)', '(the all-n tail is the open clause)'),
    (261, '(the all-n tail is the open gap)', '(the all-n tail is the open tail premise)'),
    (304, 'the all-n tail is the open gap.', 'the all-n tail is the open all-n range.'),
    (329, 'the gap is identification→exclusion (= the h2/RH gap)', 'the clause is identification→exclusion (= the h2/RH clause)'),
]

CREDITS = [
    (240, 'PATHS:240:23', 5904,
     '*Credit (CP-1b, b558, FINDINGS :5904):* the sentence above cites on 2026-07-17 the load-bearing flag “treating H as weaker than RH '
     're-commits the ConservationHypothesis error”, the reading `ch_iff_rh` (%s %s) compiled at b531–b532.' % (EF, PIN['ch_iff_rh'])),
    (308, 'PATHS:291:35', 5918,
     '*Credit (CP-1b, b558, FINDINGS :5918):* the Conservation-frame row of this table (v0.6 :291) prints `conservation_of_spectra` as '
     '`∀ s : ℤ, (1 : ℚ) ^ s = 1` with its conservation reading a STIPULATION carried by the namespace, on 2026-08-09, the reading b539 '
     'tiered T2 on 2026-09-25.'),
]
BOUNDARY = (359, '*Beside it, compiled since (reading of `(R188)`(4)):* λ_n ≥ 0 at every n is equivalent to RH over Mathlib’s zeros, '
                 '`li_nonneg_iff_rh` (%s %s).' % (EF, PIN['li_nonneg_iff_rh']))

# ### reading (xi): the ceiling's Not-supportable phrases; a hit inside a negation is read by the seat and printed as such
CEILING = re.compile(r'RH proved|RH is proved|h2_sign proved|λ_n ≥ 0 proved|GRH reduced|GRH proved|reduction machine-verified|proof of RH|proves RH')
NEGATED = {261: 'NOT a proof of RH', 386: 'would *be* a proof of RH'}

# ### reading (ix): the seat's hand-read assignment of each of the 29 rows, by (line, the start of its sentence)
ASSIGN = {(45, '| **centre**'): 3, (46, '| **R4'): 2, (59, '| **3'): 1, (63, '**The goal state.**'): 0, (63, '**`h2` is'): 3,
          (67, '**The positivity'): 2, (67, 'This is the'): 1, (255, 'C₅-output'): 3, (257, '`h1_complete'): 3, (259, 'R5-output'): 3,
          (294, '| h1 complete'): 3, (295, '| **Register'): 1, (297, '| Register'): 1, (322, '| Route 3'): 1, (323, '| T3 goal'): 3,
          (326, '| R-curve'): 0, (332, '**RH proper**'): 1, (332, 'Every conditional'): 3, (379, '| A7'): 2, (450, '**Our FE-even'): 2}
MATCHER = {1: r'\bR[1-5]\b|[Pp]entagon|ConservationHypothesis|riemann_hypothesis\b|[Rr]egister',
           2: r'partialPositivity|TailBoundPremise|all-n tail|N₀|[Ff]inite-[Rr]ange',
           3: r'single open|one open|only h2 open|h2 open|h2 outstanding|outstanding obligation|one hinge|stands alone'}


def _cp():
    import b558_record as CP
    return CP


def _count(lines):
    CP = _cp()
    return sum(len([s for s in CP.segments(l) if s]) for l in lines)


def _rows():
    return [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'PATHS' and r['verdict'] == 'MOVED-IN-MEANING']


def _status_blanks(lines):
    """### every table whose header names a Status column, read cell by cell: (line, row) of each blank Status cell."""
    out, hdr = [], None
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if not s.startswith('|'):
            hdr = None
            continue
        cells = [c.strip() for c in s.strip('|').split('|')]
        if hdr is None:
            hdr = [c.lower().strip('* ') for c in cells]
            continue
        if set(s.replace('|', '').replace(':', '').replace('-', '').strip()) == set():
            continue
        for k, h in enumerate(hdr):
            if h.startswith('status') and (k >= len(cells) or not cells[k]):
                out.append(i)
    return out


def edition(*a):
    """### PLACE-papers phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md, created beside the current version from its blob at
    ### 7bd8954, and the sentence-by-sentence diff bank. ### `again` rewrites an edition this act already wrote (never a committed one)."""
    CP = _cp()
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    if cur and cur[-1] == '':
        cur = cur[:-1]
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE 7bd8954 -- NOTHING WRITTEN')
    edp = os.path.join(PP, *ED.split('/'))
    if os.path.exists(edp) and 'again' not in a:
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    if g(PP, 'ls-files', ED).strip():
        sys.exit('### THE EDITION FILE IS COMMITTED -- NOTHING WRITTEN')
    new = list(cur)
    rows = _rows()
    diff = []
    # ### (a) the marked sentences
    for ln, old, rep, reading in REWRITES:
        line = new[ln - 1]
        if line.count(old) != 1:
            sys.exit('### :%d -- THE FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE (%d): %s' % (ln, line.count(old), old[:80]))
        segs_before = [s for s in CP.segments(line) if s]
        new[ln - 1] = line.replace(old, rep)
        segs_after = [s for s in CP.segments(new[ln - 1]) if s]
        if len(segs_after) != len(segs_before):
            sys.exit('### :%d -- THE REWRITE CHANGED THE LINE`S SEGMENT COUNT %d -> %d' % (ln, len(segs_before), len(segs_after)))
    # ### (b) the stem corrections
    for ln, old, rep in STEMS:
        line = new[ln - 1]
        if line.count(old) != 1:
            sys.exit('### :%d -- THE STEM FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE: %s' % (ln, old))
        n0 = len([s for s in CP.segments(line) if s])
        new[ln - 1] = line.replace(old, rep)
        if len([s for s in CP.segments(new[ln - 1]) if s]) != n0:
            sys.exit('### :%d -- THE STEM CORRECTION CHANGED THE SEGMENT COUNT' % ln)
    # ### the diff, row by row: each row's sentence in the current line, and the sentence that replaces it
    for r in rows:
        ln = r['line']
        olds = [s for s in CP.segments(cur[ln - 1]) if s]
        news = [s for s in CP.segments(new[ln - 1]) if s]
        k = olds.index(r['sentence'])
        key = [kk for kk in ASSIGN if kk[0] == ln and r['sentence'].startswith(kk[1])]
        if len(key) != 1:
            sys.exit('### :%d -- NO UNIQUE ASSIGNMENT FOR THE ROW' % ln)
        cites = [d for d in PIN if ('`%s`' % d) in news[k] and PIN[d] in news[k]]
        banks = re.findall(r'relay `data/[^`]+` :\d+', news[k])
        diff.append(dict(id=r['id'], line=ln, terminal=r['terminal'], old=r['sentence'], new=news[k], changed=news[k] != r['sentence'],
                         reading=ASSIGN[key[0]], matcher=[m for m, p in MATCHER.items() if re.search(p, r['sentence'])],
                         cites=cites, banks=banks, supports=r['reading']))
    # ### (c), (d) the insertions, bottom up so the line numbers above stay the current version's
    ins = [(ln, ['', t]) for ln, _, _, t in CREDITS] + [(BOUNDARY[0], ['', BOUNDARY[1]])]
    for ln, add in sorted(ins, key=lambda x: -x[0]):
        new[ln:ln] = add
    body = list(new)
    # ### (e) the back matter
    ed_lines = {}
    for d in PIN:
        ed_lines[d] = [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l and PIN[d] in l]
    bm = ['', '<!-- b578 (R188) THE v0.7 EDITION`S BACK MATTER, 2026-10-01 -->', '',
          '## Back matter of the v0.7 edition -- written 2026-10-01 by b578 under the author’s ruling `(R188)`(4), by the form of `(R187)`(5)',
          '',
          '*This file is v0.7 of PATHS_TO_THE_CRITICAL_LINE, the CP-7 edition written beside v0.6 (`%s`, unedited) from v0.6’s tier block '
          '(its :542) and its CP-1b work-list (relay `data/b558_editions/PATHS_TO_THE_CRITICAL_LINE.txt`), the zeta page as its spine; it '
          'does not deposit and does not replace v0.6, and its promotion is CP-8’s.*' % CUR, '',
          '### Removals', '',
          'None: every one of the 20 marked sentences (29 work-list rows) is rewritten to what its compiled fact says, and no marked sentence '
          'is one the compiled facts fail to support.', '',
          '### Stem corrections', '',
          '| v0.6 line | v0.6 wording | v0.7 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in STEMS:
        # ### the v0.6 wording quoted verbatim inside this correction record -- banned_terms.py's declared exception, matched in its
        # ### 40-character window on both sides of every hit
        bm.append('| :%d | banned stem, correction record: %s (banned stem; correction record) | %s | corrected under `(R188)`, the '
                  'author’s answer before b578’s seal |' % (ln, old, rep))
    bm += ['', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v0.7 | `%s` | written at b578 |' % ED,
           '| the current version, v0.6 | `%s` | unedited |' % CUR,
           '| the spine | `%s` at PLACE-papers `%s` | read, unedited |' % (PAGE, MIRROR_PIN),
           '| the work-list | relay `data/b558_editions/PATHS_TO_THE_CRITICAL_LINE.txt` | read |',
           '| the sentence-by-sentence diff | relay `data/b578_edition_PATHS.txt` | banked at b578 |',
           '| the two credits | `FINDINGS.md` :5904, :5918 | filed at b558 |',
           '| the register census | relay `data/b538_census.json` | read |',
           '', '### Correspondence', '',
           '| declaration | repository | pin as the zeta page prints it | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    for d in PIN:
        where = ('node %d, line %d' % (PAGE_NODE[d], PAGE_NODE[d] + 4)) if d in PAGE_NODE else ('Correspondence row, line %d' % PAGE_ROW[d])
        bm.append('| `SIDEExplicitFormula.%s.%s` | %s | %s | %s | cited at :%s of this edition |' % (
            'B321' if d in ('ch_iff_rh', 'h2_sign_iff_rh') else ('LiCriterionBridge' if d == 'li_nonneg_iff_rh' else 'RegisterDepth'),
            d, EF, PIN[d].replace('`', ''), where, ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    bm.append('')
    full = body + bm
    b = (NL.join(full) + NL).encode('utf-8')
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    n_bm = n_full - n_body
    n_ins = len(CREDITS) + 1
    put_json('b578_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_bm, n_inserted=n_ins,
                                       credit=len(CREDITS), removals=0, diff=diff, stems=STEMS,
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full),
                                       cited_lines=ed_lines, credits=[dict(after=c[0], id=c[1], findings=c[2], text=c[3]) for c in CREDITS],
                                       boundary=dict(after=BOUNDARY[0], text=BOUNDARY[1])))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_bm))


def edition_bank():
    """### The sentence-by-sentence diff, the stems, the counts, the ceiling read, H28a-H28c: data/b578_edition_PATHS.txt."""
    E = jl('b578_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    scan = rd('b578_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    # ### the ceiling: every hit in the whole edition, its line, and whether it sits in a sentence this act wrote
    act_text = [d['new'] for d in E['diff']] + [c['text'] for c in E['credits']] + [E['boundary']['text']]
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            ctx = l[max(0, m.start() - 60):m.end() + 20]
            mine = any(m.group(0) in t for t in act_text) and any(ctx.strip()[:30] in t for t in act_text)
            v6 = [k for k, w in NEGATED.items() if w in l]
            hits.append(dict(line=i, hit=m.group(0), ctx=ctx, act=mine, negated_at_v06=v6[0] if v6 else None))
    beyond = [h for h in hits if h['act'] or h['negated_at_v06'] is None]
    # ### H28a: every MOVED row resolves to a sentence citing a page declaration at its pin, or a bank line
    h28a_bad = [d['id'] for d in E['diff'] if not d['changed'] or not (d['cites'] or d['banks'])]
    h28a = 'HELD' if not h28a_bad else 'REFUTED'
    allowed = E['credit'] + E['removals']
    dn = E['n_full'] - E['n_cur']
    h28b = 'HELD' if abs(dn) <= allowed else 'REFUTED'
    h28c = 'HELD' if (live and int(live.group(1)) == 0 and clean and not beyond) else 'REFUTED'
    L = ['b578 -- COMPONENT 3: THE EDITION OF PATHS_TO_THE_CRITICAL_LINE, (R188)(4), BY THE FORM OF (R187)(5)', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :19 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)[0],
             g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)[18][:90]),
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE WORK-LIST, ROW BY ROW (29 rows, 20 sentences, 17 lines) -- each row: the line, the terminal, the reading it falls under '
         '(the seat`s hand-read), the declarations its rewrite cites with their pins, the sentence before and after.', '']
    for d in E['diff']:
        L += ['  %s :%d `%s` -- %s ; cites %s%s' % (d['id'], d['line'], d['terminal'], READING_NAME[d['reading']],
                                                    ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']],
                                                    (' ; bank ' + ', '.join(d['banks'])) if d['banks'] else ''),
              '      work-list: %s' % d['supports'],
              '      v0.6 : %s' % d['old'], '      v0.7 : %s' % d['new'], '']
    cov = [d for d in E['diff'] if d['reading']]
    mat = [d for d in E['diff'] if d['matcher']]
    L += ['### (N2) COVERAGE BY THE THREE READINGS OF (R188)(4), the seat`s hand-read: %d of %d rows -- (i) %d, (ii) %d, (iii) %d ; '
          'uncovered %s, resolved by the form' % (len(cov), len(E['diff']), sum(d['reading'] == 1 for d in E['diff']),
                                                  sum(d['reading'] == 2 for d in E['diff']), sum(d['reading'] == 3 for d in E['diff']),
                                                  [':%d %s' % (d['line'], d['old'][:40]) for d in E['diff'] if not d['reading']]),
          '### the regex matcher`s yield, printed as lineage and not the count: %d of %d rows (a permissive filter)' % (len(mat), len(E['diff'])),
          '', '### THE STEM CORRECTIONS (reading (vi), the author`s answer):']
    L += ['    :%d  "%s" -> "%s"' % tuple(s) for s in E['stems']]
    L += ['', '### THE CREDIT LINES:'] + ['    after v0.6 :%d (%s, FINDINGS :%d): %s' % (c['after'], c['id'], c['findings'], c['text']) for c in E['credits']]
    L += ['### THE CITATION BESIDE ANNEX A :359 (reading (v)): after v0.6 :%d: %s' % (E['boundary']['after'], E['boundary']['text']),
          '### REMOVALS: none.', '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (+%d: the '
          'credit lines %d and the citation 1) ; the back matter %d ; the edition whole %d ; difference %+d against CREDIT + removals = %d' % (
              E['n_cur'], E['n_body'], E['n_body'] - E['n_cur'], E['credit'], E['n_backmatter'], E['n_full'], dn, allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']),
          '', '### THE CEILING (reading (xi)), every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], ('IN THIS ACT`S TEXT' if h['act'] else
                                                                  ('carried from v0.6 :%d, inside a negation, read by the seat' % h['negated_at_v06'])
                                                                  if h['negated_at_v06'] else '### UNREAD'), h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### the banned-stem scan of the edition (relay data/b578_edition_termscan.txt): live uses %s ; verdict %s' % (
              live.group(1) if live else '?', 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on the page at its pin, or a bank line%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- the whole edition differs from the current version by %+d sentences, against at most %d (CREDIT %d + removals 0)'
          '; the body by %+d (the two credit lines and the ruled citation), the back matter %d.**' % (
              h28b, dn, allowed, E['credit'], E['n_body'] - E['n_cur'], E['n_backmatter']),
          '### ### **H28c %s -- live banned stems %s, sentences beyond the ceiling %d.**' % (h28c, live.group(1) if live else '?', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b578_edition_PATHS.txt', L)
    put_json('b578_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, dn=dn, allowed=allowed, body_dn=E['n_body'] - E['n_cur'],
                                   backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None, beyond=len(beyond), hits=hits,
                                   covered=len(cov), matcher=len(mat), uncovered=[d['line'] for d in E['diff'] if not d['reading']], held=None))
    print(jl('b578_h28.json')['H28a'], jl('b578_h28.json')['H28b'], jl('b578_h28.json')['H28c'], 'covered', len(cov), 'dn', dn)


# ================================================================================ THE SCORING AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}


def scores():
    A, H, E = jl('b578_addendum.json'), jl('b578_h28.json'), jl('b578_edition.json')
    ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'ls-files', '--others', '--exclude-standard', 'phase1.5')).split(NL) if x.strip()))
    kmain = g('D:/SIDE-explicit-formula', 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    cur_same = g(PP, 'hash-object', CUR).strip() == E['cur_blob']
    n1 = A['accepted'][:1] == [True] and A['rerun_passing'] == 69 and A['rerun_run'] == 69
    n3 = H['H28a'] == 'HELD' and H['H28b'] == 'HELD' and H['H28c'] == 'HELD' and H['held'] is None
    n4 = H['dn'] == E['credit'] + E['removals']
    n5_core = kmain == V015 and heads_ok and cur_same and set(ch) <= {'FINDINGS.md', 'OPEN_TRAILS.md', ED}
    # ### the writes the expectation's list does not name: the prior bank rewritten, the worktree removed
    extra = ([x for x in g(RELAY, 'status', '--porcelain', '--', 'data/b576_writelist_addendum.txt').split(NL) if x.strip()]
             + (['the worktree removed'] if '### ### **THE WORKTREE IS REMOVED.**' in rd('b578_worktree.txt') else []))
    S = dict(
        N1=('HELD' if n1 else 'REFUTED', 'the re-cited line %s by the form ((R187)(4) names the file), the refused line beneath it %s; '
            'b576`s suite re-run in the kept worktree (HEAD %s) reads %s of %s (relay data/b578_b576_rerun.txt): G-WRITELIST-KINDS fails '
            'on the re-run`s own scaffolding in the worktree, no longer on mirror_prevbuild.json, and G-DOC-UNWRITTEN and '
            'G-MIRROR-AFTER-PUSH read PLACE-papers as b577 left it (relay data/b578_rerun_diagnosis.txt)' % (
                A['why'][0], A['why'][1] if len(A['why']) > 1 else '?', (A['worktree_head'] or '?')[:8], A['rerun_passing'], A['rerun_run'])),
        N2=('HELD' if H['covered'] >= 20 else 'REFUTED', 'the three readings cover %d of the 29 MOVED rows by the seat`s hand-read; uncovered '
            ':%s, resolved by the form; the regex matcher`s yield %d, printed as lineage' % (H['covered'], ', :'.join(str(x) for x in H['uncovered']), H['matcher'])),
        N3=('HELD' if n3 else 'REFUTED', 'H28a %s, H28b %s (%+d against at most %d), H28c %s; the edition lands, no sentence HELD%s' % (
            H['H28a'], H['H28b'], H['dn'], H['allowed'], H['H28c'],
            '' if n3 else ' -- refuted in letter on H28b: the back matter the form requires (%d) and the ruled citation beside :359 (1) '
                          'lie outside the CREDIT-plus-removals bound' % H['backmatter'])),
        N4=('HELD' if n4 else 'REFUTED', 'the edition`s count differs from the current version`s by %+d; CREDIT %d + removals %d = %d; the '
            'difference is the two credit lines, the citation beside :359 and the back matter (%d)' % (H['dn'], E['credit'], E['removals'],
                                                                                                         E['credit'] + E['removals'], H['backmatter'])),
        N5=('HELD' if (n5_core and not extra) else 'REFUTED', 'nothing deposits; no kernel touched (%s); the current PATHS unedited (%s); '
            'PLACE-papers changed at %s -- but the addendum bank was rewritten, the worktree deleted and relay banks written, as (R188)(2) '
            'orders, which the expectation`s list does not name' % ('held' if kmain == V015 and heads_ok else '### MOVED',
                                                                     'held' if cur_same else '### EDITED', ch)),
        S1=('HELD' if n1 and A['accepted'][1:2] == [False] else 'REFUTED', 'expected the re-cited line ACCEPTED, the refused line beneath REFUSED, and 69 of 69; read: ACCEPTED, REFUSED, %s of %s' % (
            A['rerun_passing'], A['rerun_run'])),
        S2=('HELD' if H['covered'] == 27 and H['uncovered'] == [63, 326] else 'REFUTED', '27 of 29; uncovered :63 and :326'),
        S3=('HELD' if (H['H28a'] == 'HELD' and H['H28c'] == 'HELD' and H['H28b'] == 'REFUTED' and H['held'] is None) else 'REFUTED',
            'H28a and H28c held, no hold, H28b refuted in letter by the back matter'),
        S4=('HELD' if (not n4 and E['removals'] == 0) else 'REFUTED', '(N4) refuted: the credit lines, the citation and the back matter; no removals'),
        S5=('HELD' if n5_core else 'REFUTED', '(N5) refuted in letter by the bank rewrite, the deletion and the relay banks; its other clauses hold'),
        counts=dict(pp_changed=ch, dn=H['dn'], covered=H['covered']),
    )
    put_json('b578_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s' % (k, S[k][0]))


TITLE_HEAD = '## CP-7, act three: the edition of PATHS_TO_THE_CRITICAL_LINE from its tier block and work-list, the pentagon read as the star'
TITLE = TITLE_HEAD + '; written as v0.7 beside v0.6, no sentence held'
TRAIL_HEAD = ('### b578 — lane three, act six under (R188): CP-7 act three -- the edition of PATHS_TO_THE_CRITICAL_LINE written beside '
              'the current; the addendum re-cited; the order ratified; the re-run worktree deleted')
NAV_READING = ('the form’s clause `(R187)`(5) is read as permitting stem corrections on unmarked sentences -- the navigator’s reading, '
               'entered at the author’s answer before b578’s seal')


def records_pp():
    Q = _Q()
    S, H, E, A, C1, O = (jl('b578_scores.json'), jl('b578_h28.json'), jl('b578_edition.json'), jl('b578_addendum.json'),
                         jl('b578_c1_lines.json'), jl('b578_order.json'))
    Q.guard_absent(Q.FIND, TITLE_HEAD)
    e = ['', TITLE, '',
         '*Filed at b578 on the author’s ruling `(R188)`. Banks: relay `data/b578_edition_PATHS.txt` (the sentence-by-sentence diff), '
         '`data/b578_edition.json`, `data/b578_addendum.txt`, `data/b578_worktree.txt`. Nothing deposits.*', '',
         '**The edition** (`(R188)`(4)): `%s`, v0.7, written beside v0.6 (`%s`, unedited) from v0.6’s tier block and its CP-1b work-list, '
         'the zeta page as its spine. The 29 work-list rows resolve to 20 sentences on 17 lines; each is rewritten in place to what its '
         'compiled fact says, citing the page’s declaration at the pin the page prints, or the b538 census by its bank line. The pentagon '
         'is read as the star: R1 false as stated, R2 and R4 compiled equal to RH, R5’s output face a theorem as stated, R3 undecided. '
         'ANNEX A’s honest-boundary sentence stands, with the Li equivalence cited beside it. Two credit lines are inserted beside their '
         'lines; five live uses of a banned stem in unmarked sentences take the object each sentence names, listed in the back matter. '
         'No sentence is removed and none is held.' % (ED, CUR), '',
         '**The counts.** v0.6 %d sentences; v0.7 %d (the body %d, the back matter %d); the difference %+d against CREDIT plus removals, %d.'
         % (E['n_cur'], E['n_full'], E['n_body'], E['n_backmatter'], H['dn'], H['allowed']), '',
         '**H28a %s · H28b %s · H28c %s.** Coverage of the 29 rows by the three readings of `(R188)`(4): %d.' % (
             H['H28a'], H['H28b'], H['H28c'], H['covered']), '',
         '**The addendum** (`(R188)`(2)), re-cited to the clause that names the file and ACCEPTED by its form; b576’s suite re-run in the kept '
         'worktree reads %d of %d, not the 69 expected: the write-list arm no longer fails on tools/mirror_prevbuild.json but on the '
         're-run’s own scaffolding in the worktree, and two arms read PLACE-papers as b577 left it (relay `data/b578_rerun_diagnosis.txt`); '
         'the worktree deleted (OPEN_TRAILS :%d). **The order** (`(R188)`(3)) ratified, the outside items placed, '
         'two held (OPEN_TRAILS :%d).' % (A['rerun_passing'], A['rerun_run'], C1['ot_line'], O['line']), '',
         '**A reading, the navigator’s:** %s.' % NAV_READING, '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R188)`(5): CP-7 act four -- the edition of FOUNDATIONS_OF_THE_SIDE_PROGRAMME by the same form; the author rules on '
         'the closing.', '',
         '*Nothing deposits; no kernel touched; v0.6, README, REGISTRY and both pages unwritten; nothing here is a statement about RH, GRH or '
         'any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows = ['', TRAIL_HEAD, '',
            '**(R188) ratified.** (1) b577 at its weight. (2) The addendum re-cited; the worktree deleted. (3) The order ratified; three '
            'placed; two held. (4) The edition of PATHS_TO_THE_CRITICAL_LINE by the form, three readings entered. (5) The act after.', '',
            '**Entered:** FINDINGS.md:%d (b577’s weight), :%d (the entry); OPEN_TRAILS.md:%d (b576’s record: the re-cited addendum and the '
            'deletion), :%d (the order), this record; PLACE-papers `%s` (created). Relay: `data/b576_writelist_addendum.txt` rewritten as '
            'ruled; the worktree D:\\b577-rerun-b576 removed.' % (C1['weight'], Q.line_of(Q.FIND, TITLE_HEAD), C1['ot_line'], O['line'], ED), '',
            '**Answered before the seal, by the author:** the honest-boundary sentence is ANNEX A :359’s; the title lines carry unchanged; the '
            'five stem uses take the object each sentence names. **Recorded as the navigator’s:** %s.' % NAV_READING, '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
            % tuple(S[k][0] for k in SCORE_KEYS), '',
            '**For the author:** H28b, as fixed, counts the back matter the form itself requires and the citation `(R188)`(4) orders; the '
            'edition’s body differs from v0.6 by %+d, the back matter adds %d. b576’s re-run reads %d of %d, not 69: the addendum now '
            'carries its file, the write-list arm fails on the re-run’s own scaffolding, and two arms read PLACE-papers as b577 left it '
            '(relay `data/b578_rerun_diagnosis.txt`); a re-run at 69 would need PLACE-papers read at b576’s push, which b576’s suite does not '
            'do.' % (H['body_dn'], H['backmatter'], jl('b578_addendum.json')['rerun_passing'], jl('b578_addendum.json')['rerun_run']), '',
            '**Next:** per `(R188)`(5), CP-7 act four, b579 -- the edition of FOUNDATIONS_OF_THE_SIDE_PROGRAMME by the same form, H28a-H28c '
            'scored; the author rules on the closing.', '',
            '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
            'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows))
    put_json('b578_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE_HEAD), title=TITLE, append=r))
    put_json('b578_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r2))
    print(jl('b578_findings.json')['entry_line'], jl('b578_trail.json')['line'])


def desk():
    S = jl('b578_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b578 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b578_defects.txt').rstrip(NL).split(NL)
    put_txt('b578_desk_notes.txt', L)


def components():
    S, H, E, A, C1, O, fj, tj = (jl('b578_scores.json'), jl('b578_h28.json'), jl('b578_edition.json'), jl('b578_addendum.json'),
                                 jl('b578_c1_lines.json'), jl('b578_order.json'), jl('b578_findings.json'), jl('b578_trail.json'))
    L = ['b578 -- THE COMPONENTS, BANKED UNDER (R188).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b577`s closing push-out relay faa78619 ; push-b577* branches deleted by '
         'name (data/b578_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : the addendum re-cited, ACCEPTED by its form, the refused line beneath ; b576`s re-run in the worktree %d of %d ; '
         'the worktree removed (data/b578_worktree.txt) ; OPEN_TRAILS :%d ; N1 %s' % (A['rerun_passing'], A['rerun_run'], C1['ot_line'], S['N1'][0]),
         '### COMPONENT 2 : the order ratified, three placed, two held, OPEN_TRAILS :%d ; b577`s weight FINDINGS :%d' % (O['line'], C1['weight']),
         '### COMPONENT 3 : the edition %s ; 20 sentences rewritten, 4 stem corrections (5 uses), 2 credit lines, 1 citation, 0 removals ; '
         'data/b578_edition_PATHS.txt ; H28a %s H28b %s H28c %s ; N2 %s N3 %s N4 %s' % (ED, H['H28a'], H['H28b'], H['H28c'],
                                                                                    S['N2'][0], S['N3'][0], S['N4'][0]),
         '### COMPONENT 4 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; next: the edition of FOUNDATIONS_OF_THE_SIDE_PROGRAMME ; N5 %s'
         % (fj['entry_line'], tj['line'], S['N5'][0])]
    put_txt('b578_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b578_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
