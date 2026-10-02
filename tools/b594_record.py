# -*- coding: utf-8 -*-
"""b594_record.py -- THE ACT'S RECORD TOOL, UNDER (R204). ### ONE SUBCOMMAND PER BANK.

### ### b594: LANE THREE, ACT TWENTY-ONE -- CP-7 ACT SIXTEEN: THE EDITION OF FACES_OF_H2_AT_FINITE_INSTANCE BY THE FORM UNDER THE
### PRECEDENCE ORDER; THE THREE STANDING INSTRUCTIONS ENTERED.
### Subcommands write only `data/b594_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode, temp file, `os.replace`). No platform call. The template is b593_record.py.
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
EFK = 'D:/SIDE-explicit-formula'
LVK = 'D:/SIDE-lv-conservation'
PRE_PP = 'bf4e9f5'
PRE_RELAY = 'aea25c80'
STEPZERO = '2e7c89d6'
V016 = 'c404e727d7f7121b180318cca32eeb115452ed1b'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f7dd7aec-e7f8-492c-a0db-31ef189124e6/scratchpad'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CUR = 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md'
ED = 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE_v0_2.md'
WL = 'data/b558_editions/FACES_OF_H2_AT_FINITE_INSTANCE.txt'
NODES = {'zeta': 'b592_nodes.txt', 'chi': 'b592_nodes_chi.txt'}
PROBE = {'zeta': 'b592_probe_out.txt', 'chi': 'b592_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}

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
    '(a) THE READS BANK`S FIRST RUN ASKED b550`S READING BANK FOR A LINE IT DOES NOT HAVE (:21 of a twenty-line file) and printed NO '
    'SUCH LINE; the range was corrected through the Edit tool and the bank re-written before any component used it.',
    '(b) THE SUITE`S FIRST BUILD FROM b593`S HARNESS DROPPED THE HARNESS MIDDLE (put .. g2_names) AND RENAMED b593`S CLOSING TO b594`S: '
    'both found by the pre-run before the seal (a NameError, then G-PRIOR-CLOSED-PUSHED failing on an empty read), the generator '
    'corrected in the scratchpad and the closing name through the Edit tool, and the pre-run re-banked; the arm list did not change.',
    '(c) THE EDITION`S FIRST BANK MISREAD ITS OWN CEILING READ: three carried lines (:42, :47, :160) hold no hit of the case-sensitive '
    'pattern ("PROVED" in capitals, "unproved"), and one hit in the back matter`s own prose was classed "beyond" because only table '
    'rows counted as records; the carried list and the classifier were corrected through the Edit tool and the uncommitted edition, '
    'its scan, bank and re-pin re-run.',
    '(d) THE SEAT`S FACT READ MISSED ONE CITATION BEFORE THE EDITION COMMIT: b547`s dated blocks (the draft`s :213 and :219, carried '
    'at the edition`s :219 and :225) cite the register census as "FINDINGS.md:4787", a blank line; the census heading is :4788 '
    '(FINDINGS is append-only, so the citation was off by one when written). Found at the record step, after the edition commit; '
    'under the precedence order the history clause governs a dated block and carries it, and no history line names it -- for the '
    'author`s word at the closing.',
    '(e) THE SUITE`S FIRST PRE-PUSH RUN FOUND G-EDITION-CARRIES`S POSITIVE CONTROL PASSING: its mutation ("Sonin") touched only §2`s R4 '
    'row, a line the arm skips as changed, so the control could not fire (and G-ARMS-NO-LIVE-LIMB failed with it); the mutation was '
    'pointed through the Edit tool at a carried line ("NON-FUSION", the draft`s :12 and :59) and the suite re-run whole.',
    '(f) A CHAINED COMMAND RAN PAST A FAILED STEP: the closing-tool generator failed its first assertion, and the `;`-joined commit '
    'and push that followed it ran -- the commit found nothing staged and `push_gated.sh` refused for want of the branch push-b594 '
    '("ambiguous argument"); nothing was pushed (the remote main read back at aea25c80). Its capture is kept as '
    'data/b594_relay_push_out_attempt1.txt and the steps were re-run one by one.',
]


def defects():
    put_txt('b594_defects.txt', ['### b594 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay the FACES work-list, whole', RELAY, 'HEAD', WL, list(range(1, 12))),
    ('relay the CP-1b rows of FACES_OF_H2_AT_FINITE_INSTANCE (1 MOVED, 18 STANDS, 0 CREDIT)', RELAY, 'HEAD', 'data/b558_cp1b.txt', [46] + list(range(752, 771))),
    ('PLACE-papers FACES_OF_H2_AT_FINITE_INSTANCE, whole', PP, PRE_PP, CUR, list(range(1, 226))),
    ('PLACE-papers the ζ page at v0.16, the faces and the ladder', PP, PRE_PP, PAGE, [3, 12, 13, 14, 15, 24, 25]),
    ('PLACE-papers FACES_LEDGER, its head', PP, PRE_PP, 'FACES_LEDGER.md', list(range(1, 6))),
    ('PLACE-papers OPEN_TRAILS, the form, its clauses and lane three`s refined order', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11864, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 12044, 12062, 12188, 12190, 12192, 12194, 12210, 12212, 12214]),
    ('PLACE-papers FINDINGS, b593`s entry', PP, PRE_PP, 'FINDINGS.md', [6800]),
    ('relay the pole-term reading (b550, the ruling`s "b549")', RELAY, 'HEAD', 'data/b550_reading37.txt', list(range(14, 21))),
    ('relay b547`s faces bank, the h1_complete_at_Phi row', RELAY, 'HEAD', 'data/b547_faces.json', list(range(24, 34))),
    ('SIDE-lv-conservation v0.6.0 h1_complete_at_Phi', LVK, 'c80bdc2', 'SIDELvConservation/CouplingsAtPhi.lean', [418]),
    ('SIDE-explicit-formula v0.16 the ladder', EFK, V016, 'SIDEExplicitFormula/DetectionRegion.lean', [29, 47, 52]),
    ('relay b593`s closing push-out, its head', RELAY, 'HEAD', 'data/b593_closing_push_out.txt', list(range(1, 6))),
]


def reads():
    L = ['b594 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev + '^{}').strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:400]))
    hits = [h for h in g(PP, 'show', '%s:OPEN_TRAILS.md' % PRE_PP).split(NL)[6641].split('<br>') if 'FACES_OF_H2' in h]
    cw = [i for i, l in enumerate(g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL), 1) if re.search(r'circular', l, re.I)]
    L += ['', '### b450`s items for FACES_OF_H2_AT_FINITE_INSTANCE in its table (OPEN_TRAILS :6642): %d -- %s' % (len(hits), hits or 'none'),
          '### "circularity witness" searched in the current version (case-insensitive "circular"): lines %s -- %s' % (cw, 'NO OBJECT' if not cw else 'found')]
    put_txt('b594_reads.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B593_ENTRY = '## CP-7, act fifteen: the edition of BALANCE_AND_POSITIVITY from its tier block and work-list'
FORM = '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three (:11417) -- THE FORM OF AN EDITION'
ORDER = '*Appended 2026-10-01 by b586'


def weight_line():
    """### PLACE-papers FINDINGS: b593's weight, one appended line addressed to b593's entry."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B593_ENTRY)
    if entry != 6800:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    head = '*Appended 2026-10-02 by b594 to b593’s entry (:%d), under `(R204)`(1) -- b593 AT ITS WEIGHT:*' % entry
    Q.guard_absent(Q.FIND, head)
    text = ('\n%s BALANCE_AND_POSITIVITY v0.9.5 beside v0.9.4 unedited: 14 rows rewritten in place -- the register sentences (:72, :146, '
            ':553) through the b538 census as PATHS v0.7 reads them, the four h2-at-Φ sentences naming lv’s h2 false on the strip and the '
            'open clause h2_sign, the finite-range certificate naming its two literature premises (T1-lit); the R4 edge naming Li’s '
            'criterion compiled (li_nonneg_iff_rh v0.9, register4_positivity_liCoeff_iff_rh v0.11); the joint “RH ⟺ λ_Z(n) ≥ −λ_A(n)” '
            'cited at its five body uses (:21, :72, :146, :360, :430) with the channel-split note; four history lines beneath dated '
            'entries (the balance sentence’s compiled form scoped to the Bombieri–Lagarias family under the 2026-08-28 annotation; '
            'b545’s and b561’s Li entries superseded; two dated stem uses carried); one ceiling correction (:21, “of the reduction”), four '
            'stem corrections, no fact correction; body 870 against 865 (+5), back matter 112, re-pin 156 of 156; H28a-H28c held, the '
            'scanner clean; both pages re-emitted and 2 of 2. W-ORD-ACT-ROOT at OPEN_TRAILS :12210, W-ORD-SECOND-READER at :12212. (N2) '
            'refuted in its letter by the author’s own answer (the balance sentence carried, its compiled form in a history line). The '
            'suite read 66 of 66.\n' % head)
    r = Q.append_to(Q.FIND, text)
    put_json('b594_weight_line.json', dict(entry=entry, line=Q.line_of(Q.FIND, head), head=head, append=r))
    print('  weight line :%s' % Q.line_of(Q.FIND, head))


def rule_lines():
    """### PLACE-papers OPEN_TRAILS: the precedence order addressed to the form (:11864), and the three standing instructions with the
    ### research sequence addressed to lane three's refined order (:12062). Two appended lines."""
    Q = _Q()
    f = Q.line_of(Q.OT, FORM)
    ls = io.open(Q.OT, encoding='utf-8').read().split(NL)
    lane = 12062
    if f != 11864 or 'lane three' not in ls[lane - 1].lower():
        sys.exit('### THE ADDRESSED LINES MOVED: form %s, lane three :%d "%s" -- NOTHING WRITTEN' % (f, lane, ls[lane - 1][:80]))
    heads = ['*Appended 2026-10-02 by b594, under the author’s ruling `(R204)`(2), to the form of an edition (:%d) -- THE PRECEDENCE ORDER:*' % f,
             ('*Appended 2026-10-02 by b594, under the author’s ruling `(R204)`(3), beneath lane three’s refined order (:%d) -- THE AUTHOR’S '
              'THREE STANDING INSTRUCTIONS, AND THE RESEARCH SEQUENCE:*' % lane)]
    for x in heads:
        Q.guard_absent(Q.OT, x)
    texts = ['\n%s where two clauses of the form meet on one sentence, the history clause governs, then the name-and-title exception, '
             'then the stem clause, then the ceiling clause, then the fact clause, then the restatement clause, each applying to what the '
             'earlier ones leave; the seat resolves the collision by that order without a prompt, lists every resolved collision in the '
             'back matter with the clauses named and both wordings, and the author strikes at the closing. A prompt is reserved for a '
             'sentence no clause reaches, a write outside the corpus, and anything irreversible. Applied first at b594 to '
             'FACES_OF_H2_AT_FINITE_INSTANCE.\n' % heads[0],
             '\n%s (i) research before conclusions -- the priced research items that can change a keystone sentence’s reading run before '
             'CP-6 and CP-8, in this order unless the author reorders, one or two acts each, as the next items after b596: '
             'W-ORD-SIMPLICITY-FACE (b596), the product lemma as REMAINDER 5, W-ORD-KEIPER-FACE, (E3)’s compiled window of the bench’s '
             'family, the family form over χ mod q; (ii) every finding read in mutual light -- each FINDINGS entry from b594 carries one '
             'line naming which earlier results the new one changes the reading of and which change its, cited by line; (iii) the '
             'programme’s own offerings named -- that line says, where it applies, which offering the act strengthens (the compiled star, '
             'the schema and its instances, the pages, the edition form, the relay’s record of whose reasoning failed), and the '
             'monograph’s v6 at CP-8 states them in the same register.\n' % heads[1]]
    out = []
    for x, t in zip(heads, texts):
        r = Q.append_to(Q.OT, t)
        out.append(dict(head=x, line=Q.line_of(Q.OT, x), append=r))
    put_json('b594_rule_lines.json', dict(form=f, lane=lane, lines=out))
    print('  rule lines :%s' % [o['line'] for o in out])


# ================================================================================ COMPONENT 2: THE EDITION
EF = 'SIDE-explicit-formula'
PIN = {'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'li_nonneg_iff_rh': 'v0.9 = `e5a5a83`', 'arith_limit_nonneg_iff_rh': 'v0.9 = `e5a5a83`',
       'h2_sign_iff_forall_upto': 'v0.3 = `04eda4a`', 'forall_upto_iff_rh': 'v0.3 = `04eda4a`'}
FQ = {'h2_sign_iff_rh': 'SIDEExplicitFormula.B321.h2_sign_iff_rh', 'li_nonneg_iff_rh': 'SIDEExplicitFormula.LiCriterionBridge.li_nonneg_iff_rh',
      'arith_limit_nonneg_iff_rh': 'SIDEExplicitFormula.LiCriterionBridge.arith_limit_nonneg_iff_rh',
      'h2_sign_iff_forall_upto': 'SIDEExplicitFormula.B321.h2_sign_iff_forall_upto', 'forall_upto_iff_rh': 'SIDEExplicitFormula.B321.forall_upto_iff_rh'}
WHERE = {'h2_sign_iff_rh': 'the ζ page, node 8, line 12', 'li_nonneg_iff_rh': 'the ζ page, node 20, line 24',
         'arith_limit_nonneg_iff_rh': 'the ζ page, node 21, line 25', 'h2_sign_iff_forall_upto': 'the ζ page, node 10, line 14',
         'forall_upto_iff_rh': 'the ζ page, node 11, line 15'}
BANKS = ['relay `data/b547_faces.json` :27', 'relay `data/b550_reading37.txt` :18']
WORKLIST = [
    (180, '`h1_complete_at_Phi` (the remainder = placement) at `SIDE-kernel` `v1.5 = 0e5233f`;',
     '`h1_complete_at_Phi` (the remainder = placement) at `SIDE-lv-conservation` `v0.6.0 = c80bdc2` (`CouplingsAtPhi.lean`:418, '
     'unchanged at `v0.10.0 = 93c27ec`, SIDE-kernel v1.5 declaring no such name; relay `data/b547_faces.json` :27);'),
]
RULED = [
    (39, '(`λ_n ≥ 0` as predicate; sharpest `λ_Z ≥ −λ_A`)',
     '(`λ_n ≥ 0` as predicate; sharpest `λ_Z ≥ −λ_A`; as compiled, RH in each of its three faces: the Weil form by `h2_sign_iff_rh`, '
     'SIDE-explicit-formula v0.2 = `5c72cad`, the Li form by `li_nonneg_iff_rh` and the arithmetic-limit form by '
     '`arith_limit_nonneg_iff_rh`, v0.9 = `e5a5a83`)'),
]
RULED_WHY = {39: '(R204)(4): §2’s R4 reading MOVED-IN-MEANING to h2_sign_iff_rh at v0.2 and the three faces; §2 is the draft’s own text, '
                 'not a dated entry, and no earlier clause of the precedence order reaches it'}
CEILS = []
STEMS = []
HIST = [(97, None, '*History line, 2026-10-02 (v0.2, b594): the ledger form `P + A − PR` that §1 records and the atlas’s cell-level object '
                   '`A − PR` named above as the same are not one object -- they share `A − PR` and differ by the pole term `P`, the sign '
                   '`0 ≤ P − PR + A` over every classK window being `h2_sign` (relay `data/b550_reading37.txt` :18), so §1’s form is the bench '
                   'functional and the cell’s sign is the convention’s object.*'),
        (119, None, '*History line, 2026-10-02 (v0.2, b594): the mapping above joins the deposit’s fourth register to a finite-instance '
                    'object, the sign of `A − PR` at one diagonal a² cell, while the compiled faces are RH-equivalents; the ladder between '
                    'them is the finite-support one -- the Weil form on the windows supported in [−L₀, L₀] (`h2_sign_upto`), whose holding '
                    'for every L₀ is `h2_sign` (`h2_sign_iff_forall_upto`, SIDE-explicit-formula v0.3 = `04eda4a`) and is RH '
                    '(`forall_upto_iff_rh`, v0.3 = `04eda4a`, with `h2_sign_iff_rh`, v0.2 = `5c72cad`), so a cell or a window is a rung and '
                    'not the face.*')]
HIST_WHY = {97: '(R204)(4)`s pole-term reading, where §4.1 (added 2026-08-28, a dated entry) equates §1’s `P + A − PR` with the atlas’s '
                '`A − PR`: the history clause governs by the precedence order, the reading carried in a line beneath',
            119: '(R204)(4)`s finite-support reading for the sentence that joins the finite-instance face to the compiled faces, §4.2’s '
                 'mapping (added 2026-08-28, a dated entry): the history clause governs by the precedence order'}
COLLISIONS = [
    (95, 'history clause; the restatement of (R204)(4)`s pole-term reading', 'history',
     'the sentence equating §1’s ledger form with the atlas’s convention sits in §4.1, a dated entry: carried unchanged, the reading in the history line beneath §4.1'),
    (116, 'history clause; (R204)(4)`s finite-support reading', 'history',
     'THE MAPPING sits in §4.2, a dated entry: carried unchanged, the ladder cited in the history line beneath §4.2'),
    (102, 'history clause; the ceiling clause ("the single premise the proof routes through")', 'history',
     'the deposit’s own words quoted in §4.2’s DEPOSIT-VOICE, a dated entry: carried unchanged as the dated record; the ceiling clause has nothing left'),
    (133, 'history clause; the name-and-title exception (`F2_gap_free`)', 'history',
     '§4.3, a dated entry: carried unchanged; the kernel name is also the scanner’s quoted identifier, so the exception has nothing left'),
    (180, 'the work-list row; the fact clause (the pin `SIDE-kernel v1.5 = 0e5233f`)', 'work-list',
     'the row is the form’s own and is rewritten to the compiled fact, the pin; the fact clause has nothing left'),
]
VERSION = (10, '**v0.2 — 2026-10-02** — *CP-7 edition (b594), written beside the draft of 2026-08-18, which carries no version number of its own '
               'and is read here as v0.1 and left unedited; its back matter closes the file.*')
CEILING = re.compile(r'\bprov(?:e|ed|en|es)\b|\bproof\b|RH-core|RH proved|proves RH|end-to-end|the whole of RH')
CARRIED = {
    27: 'the one-place limit’s E₁ positivity "at proof grade", a local reading tiered T4 in the tier block, not RH',
    39: '"proof at p = 2`s limit": the local E₁ statement at one place, not RH',
    44:'§2-bis, a dated entry: the column head of compiled lemmas',
    46: '§2-bis, a dated entry: `LocalLimit.inner_map_self_of_fixed`, a compiled lemma',
    49: '§2-bis, a dated entry: a proved obstruction (`real_no_compact_open_addSubgroup`), a compiled lemma',
    92: 'a negation in a dated entry: "Nothing is proved and nothing is closed"',
    102: 'the deposit’s words quoted in a dated entry (DEPOSIT-VOICE); listed among the collisions',
    183: 'the E₁ positivity at proof grade, a local reading (T4)',
    203: 'b547`s dated tier block: the same local reading, tiered T4',
    219: 'b547`s dated census table: `register3_of_one_lt_re` proves the register on re s > 1, a compiled lemma',
}
BM_TAG = '<!-- b594 (R204) THE v0.2 EDITION`S BACK MATTER, 2026-10-02 -->'
OFFSET = ('+2 from :10 (the v0.2 line and a blank, above the method-register line); +2 more from :98 and from :120 (a blank and a history '
          'line beneath :97 and :119) -- the draft`s :n sits at the edition`s :n for n < 10, :n+2 for 10 <= n <= 97, :n+4 for 98 <= n <= 119, '
          ':n+6 for n >= 120')


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    return n + (2 if n >= VERSION[0] else 0) + sum(2 for a, _s, _t in HIST if n > a)


def _all_changes():
    return WORKLIST + RULED + CEILS + STEMS


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def edition(*a):
    """### PLACE-papers phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE_v0_2.md beside the current version from its blob at bf4e9f5; the
    ### re-pin step last. Writes the edition file and data/b594_edition.json."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE bf4e9f5 -- NOTHING WRITTEN')
    edp = os.path.join(PP, *ED.split('/'))
    dry = 'dry' in a
    if not dry and os.path.exists(edp) and 'again' not in a:
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
            sys.exit('### :%d -- THE CHANGE ALTERED THE LINE`S SEGMENT COUNT %d -> %d: %s' % (ln, n0, len(_segs(new[ln - 1])), old[:60]))
    if not cur[VERSION[0] - 1].startswith('**Method register · ### DRAFT'):
        sys.exit('### THE VERSION ANCHOR IS NOT WHERE THE FACE SAYS')
    anchors = {97: 'decided at b235 from texts', 119: '> mapping makes the premise **legible at a cell**'}
    for n, s in anchors.items():
        if not cur[n - 1].startswith(s):
            sys.exit('### THE HISTORY ANCHOR :%d IS NOT WHERE THE FACE SAYS' % n)
    import banned_terms as BT
    for t in [VERSION[1]] + [h[2] for h in HIST]:
        if len(_segs(t)) != 1:
            sys.exit('### AN INSERTED LINE IS NOT ONE SENTENCE (%d): %s' % (len(_segs(t)), t[:60]))
    for t in [VERSION[1]] + [h[2] for h in HIST] + [x[2] for x in _all_changes()]:
        if BT.PAT.search(t):
            sys.exit('### A BANNED STEM IN AN INSERTED OR REWRITTEN TEXT: %s' % t[:80])
    rows = [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'FACES' and r['verdict'] == 'MOVED-IN-MEANING']
    diff = []
    for r in rows:
        ln = r['line']
        sg = _segs(cur[ln - 1])
        if r['sentence'] not in sg:
            sys.exit('### THE ROW %s`S SENTENCE IS NOT A SEGMENT OF :%d' % (r['id'], ln))
        k = sg.index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d].split(' = ')[1] in nw] + [b for b in BANKS if b in nw]
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         cites=cites, supports=r['reading'], kind='work-list'))
    for ln, old, rep in RULED:
        diff.append(dict(id='ruled:%d' % ln, line=ln, ed_line=_edl(ln), terminal='(R204)(4) reading', old=old, new=rep, changed=True,
                         cites=[d for d in PIN if ('`%s`' % d) in rep], supports=RULED_WHY[ln], kind='ruled'))
    for after, _s, t in sorted(HIST, reverse=True):
        new[after:after] = ['', t]
    new[VERSION[0] - 1:VERSION[0] - 1] = [VERSION[1], '']
    body = list(new)
    changed = set(x[0] for x in _all_changes())
    if any(_edl(n) > len(body) or (n not in changed and body[_edl(n) - 1] != cur[n - 1]) for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL DOES NOT CARRY THE CURRENT VERSION')
    for after, _s, t in HIST:
        if body[_edl(after) + 1] != t or body[_edl(after)] != '':
            sys.exit('### A HISTORY LINE IS NOT BENEATH :%d' % after)
    if body[_edl(VERSION[0]) - 3] != VERSION[1]:
        sys.exit('### THE VERSION LINE IS NOT ABOVE :10')
    inv = {_edl(n): n for n in range(1, len(cur) + 1)}
    hits = [(i, m.group(0)) for i, l in enumerate(body, 1) for m in CEILING.finditer(l)]
    stray = sorted(set(inv.get(i, -i) for i, _ in hits) - set(CARRIED) - changed)
    stray = [s for s in stray if s > 0 or abs(s) not in [_edl(h[0]) + 2 for h in HIST]]
    if stray:
        sys.exit('### A CEILING HIT IN THE BODY IS NEITHER REWRITTEN NOR CARRIED BY THE SEAT`S READ: current lines %s' % stray)
    hl = {str(a): _edl(a) + 2 for a, _s, _t in HIST}
    bm = ['', BM_TAG, '',
          '## Back matter of the v0.2 edition -- written 2026-10-02 by b594 under the author’s ruling `(R204)`(4), by the form of `(R187)`(5) '
          'and its precedence order', '',
          '*This file is v0.2 of FACES_OF_H2_AT_FINITE_INSTANCE, the CP-7 edition written beside the draft of 2026-08-18 (`%s`, unedited, '
          'read as v0.1: the draft carries no version number) from its tier block (b547, its :190 and :211, standing) and its CP-1b '
          'work-list (relay `%s`, one row), the ζ page as its spine. The document stays Tier N, a draft at question grade, '
          'reference-only; the edition promotes no reading. It does not deposit and does not replace the draft, and its promotion is '
          'CP-8’s. Every line cited below is this file’s own.*' % (CUR, WL), '',
          '### Removals', '', 'None: the work-list’s one row resolves to a sentence rewritten in place to what its compiled fact says.', '',
          '### Rewrites', '', '| this edition’s line | the draft’s wording | v0.2 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in WORKLIST:
        bm.append('| :%d | %s | %s | rewritten: the work-list’s MOVED-IN-MEANING row (the pin, rectified at the tier block’s :%d) |' % (
            _edl(ln), old, rep, _edl(205)))
    for ln, old, rep in RULED:
        bm.append('| :%d | %s | %s | rewritten by `(R204)`(4)’s reading: %s |' % (_edl(ln), old, rep, RULED_WHY[ln]))
    bm += ['', '### Collisions resolved by the precedence order (OPEN_TRAILS, the form’s block)', '',
           '| this edition’s line | the clauses that meet | the governing clause | Status |', '|:--|:--|:--|:--|']
    for ln, clauses, gov, why in COLLISIONS:
        bm.append('| :%d | %s | %s | %s |' % (_edl(ln), clauses.replace('`', '’'), gov, why.replace('`', '’')))
    bm += ['', '### Credit lines', '', 'None: CP-1b reads no CREDIT row for this document, and no b450 item names it (relay `data/b594_reads.txt`); '
           'the §2 R4 reading’s credit is the one b547 entered (FINDINGS, the census table’s R4 row here at :%d), not entered again.' % _edl(220), '',
           '### History lines', '', '| this edition’s history line | the dated entry | Status |', '|:--|:--|:--|']
    for after, s, t in HIST:
        bm.append('| :%d | beneath :%d of §4 (added 2026-08-28) | inserted under the history clause (OPEN_TRAILS :11908, :12044, :12194) by '
                  'the precedence order: %s |' % (hl[str(after)], _edl(after), HIST_WHY[after].replace('`', '’')))
    bm += ['', '### Ceiling corrections', '', 'None: every ceiling-shaped sentence is a compiled lemma, a negation, a local reading at proof '
           'grade, or the deposit’s words in a dated entry, read below and carried.', '',
           '### Stem corrections', '', 'None: the scanner reads the draft CLEAN (the one kernel name, `F2_gap_free`, a quoted identifier).', '',
           '### Ceiling-shaped sentences read and carried', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(CARRIED):
        bm.append('| :%d | ceiling read, carried: %s | carried as read |' % (_edl(ln), CARRIED[ln].replace('`', '’')))
    bm += ['', '### Fact corrections', '', 'None under the fact clause: the one wrong pin the body states (:%d) is the work-list’s row, '
           'rewritten above.' % _edl(180), '',
           '### The navigator’s expectations of `(R204)`(4)', '', '| expectation | the read | Status |', '|:--|:--|:--|',
           '| §2’s R4 reading MOVED-IN-MEANING to `h2_sign_iff_rh` at v0.2 and the three faces | :%d | rewritten |' % _edl(39),
           '| the convention (wInf := +A, A − PR) stands with its pins | :%d-:%d (`THE_IDENTITY_CHAIN` §34.6) | carried |' % (_edl(110), _edl(112)),
           '| the circularity witness stands with its pin | no sentence of the draft names a circularity witness (relay `data/b594_reads.txt`) | '
           'no object; recorded as the navigator’s |',
           '| the sentence joining the finite-instance faces to the compiled faces cites `h2_sign_iff_forall_upto` (v0.3) as the finite-support '
           'ladder | the history line :%d beneath §4.2’s mapping (:%d-:%d) | cited |' % (hl['119'], _edl(114), _edl(116)),
           '| the cell-level object and the bench functional differ by the pole term (b549), cited where the document conflates them | the '
           'history line :%d beneath §4.1 (:%d); the bank is b550’s, relay `data/b550_reading37.txt` :18, the ruling’s “b549” the '
           'navigator’s | cited |' % (hl['97'], _edl(95)),
           '| “proved” phrasings take the ceiling clause | every hit read above; none corrected | carried as read |', '',
           '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v0.2 | `%s` | written at b594 |' % ED,
           '| the current version, the draft of 2026-08-18 | `%s` | unedited |' % CUR,
           '| the spine | `%s`, at SIDE-explicit-formula v0.16 = `c404e72` | read |' % PAGE,
           '| the work-list | relay `%s` | read |' % WL,
           '| the sentence-by-sentence diff | relay `data/b594_edition_FACES.txt` | banked at b594 |', '',
           '### Correspondence', '', '| declaration | repository | pin | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    ed_lines = {d: [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l and PIN[d].split(' = ')[1] in l] for d in PIN}
    for d in PIN:
        bm.append('| `%s` | %s | %s | %s | cited at :%s of this edition |' % (FQ[d], EF, PIN[d].replace('`', ''), WHERE[d],
                                                                              ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    hl1 = [i for i, l in enumerate(body, 1) if '`h1_complete_at_Phi`' in l and 'c80bdc2' in l]
    bm.append('| `SIDELvConservation.h1_complete_at_Phi` | SIDE-lv-conservation | v0.6.0 = c80bdc2 | not on the page; `CouplingsAtPhi.lean`:418 | '
              'cited at :%s of this edition |' % ', :'.join(str(x) for x in hl1))
    bm.append('')
    if any('### NONE' in l for l in bm):
        sys.exit('### A CORRESPONDENCE ROW CITES NO LINE OF THE EDITION')
    full = body + bm
    b = (NL.join(full) + NL).encode('utf-8')
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))
    if dry:
        print('  DRY: nothing written; diff rows %d, cites %s' % (len(diff), [(d['id'], d['cites']) for d in diff]))
        return
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    put_json('b594_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=0, removals=0, ruled_citations=len(HIST), ruled_rewrites=len(RULED), version_lines=1, diff=diff,
                                       offset=OFFSET, worklist=WORKLIST, ruled=RULED, ceils=CEILS, stems=STEMS, hist=[list(h) for h in HIST],
                                       hist_at=hl, collisions=[list(c) for c in COLLISIONS], carried={str(k): v for k, v in CARRIED.items()},
                                       version=dict(above=VERSION[0], text=VERSION[1]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines))


def edition_bank():
    """### The diff with its offset line, the collisions, the counts, the ceiling read, the scanner's verdict, H28a-H28c."""
    E = jl('b594_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(BM_TAG)
    scan = rd('b594_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    hist_n = re.search(r'carried-by-history (\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    carried_ed = set(_edl(n) for n in CARRIED)
    rewritten_ed = set(_edl(x[0]) for x in _all_changes())
    hist_ed = set(_edl(a) + 2 for a, _s, _t in HIST)
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            kind = ('record' if i > cut else 'carried' if (i < cut and i in carried_ed)
                    else 'rewritten' if (i < cut and i in rewritten_ed) else 'history' if (i < cut and i in hist_ed) else 'beyond')
            hits.append(dict(line=i, hit=m.group(0), kind=kind, ctx=l[max(0, m.start() - 60):m.end() + 40]))
    beyond = [h for h in hits if h['kind'] == 'beyond']
    wl = [d for d in E['diff'] if d['kind'] == 'work-list']
    h28a_bad = [d['id'] for d in wl if not d['changed'] or not d['cites']]
    h28a = 'HELD' if not h28a_bad else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur']
    allowed = E['credit'] + E['removals'] + E['ruled_citations'] + E['version_lines']
    h28b = 'HELD' if abs(body_dn) <= allowed else 'REFUTED'
    live_n = int(live.group(1)) if live else None
    h28c = 'HELD' if (clean and not beyond) else 'REFUTED'
    cur0 = _cur()
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % OFFSET, '',
         'b594 -- COMPONENT 2: THE EDITION OF FACES_OF_H2_AT_FINITE_INSTANCE, (R204)(4), BY THE FORM OF (R187)(5), ITS CLAUSES AND THE PRECEDENCE ORDER', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :10 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0][:80], cur0[9][:90]),
         '### its tier block : :190 (b547, the Correspondence paragraph tiered) and :211 (b547, the census table) ; b558`s line :225',
         '### its version history : no version number; the draft dated 2026-08-18 (:10-:11), §2-bis 2026-08-18 (:42), §4 added 2026-08-28 (:77), '
         'the b547 blocks :188-:223, b558`s line :225 ; read as v0.1',
         '### b450`s items naming this document: none ; the "circularity witness": no object (relay data/b594_reads.txt)',
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE WORK-LIST, ROW BY ROW (1 row), AND THE RULED REWRITE (1):', '']
    for d in E['diff']:
        L += ['  %s draft :%d -> v0.2 :%d `%s` -- %s ; cites %s' % (d['id'], d['line'], d['ed_line'], d['terminal'], d['kind'], d['cites']),
              '      answers: %s' % d['supports'], '      draft : %s' % d['old'], '      v0.2  : %s' % d['new'], '']
    L += ['### THE COLLISIONS, RESOLVED BY THE PRECEDENCE ORDER WITHOUT A PROMPT (%d):' % len(E['collisions'])]
    L += ['    draft :%d -> v0.2 :%d  %s -- governs: %s -- %s' % (c[0], _edl(c[0]), c[1], c[2], c[3]) for c in E['collisions']]
    L += ['### THE HISTORY LINES:']
    for a, s, t in HIST:
        L += ['    v0.2 :%d, beneath draft :%d' % (E['hist_at'][str(a)], a), '      %s' % t]
    L += ['### THE CEILING CORRECTIONS: none.', '### THE STEM CORRECTIONS: none.', '### THE FACT CORRECTIONS: none (the one wrong pin is the work-list row).',
          '### THE CEILING-SHAPED SENTENCES READ AND CARRIED:'] + ['    draft :%d -> v0.2 :%d  %s' % (n, _edl(n), CARRIED[n]) for n in sorted(CARRIED)]
    L += ['### REMOVALS: none.', '### CREDIT LINES: none inserted.',
          '### THE VERSION LINE: above draft :%d: %s' % (E['version']['above'], E['version']['text']), '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d) ; the back '
          'matter %d ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d (the two history lines; the '
          'ruled rewrite keeps its line`s count) + one version line = %d' % (body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], h['kind'], h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### THE SCANNER (banned_terms.py --new) on the edition: live uses %s, carried-by-history %s ; verdict %s' % (
              live_n, hist_n.group(1) if hist_n else None, 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing its compiled fact at its pin or a bank line%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s verdict %s; sentences beyond the ceiling %d.**' % (h28c, 'CLEAN' if clean else 'NOT CLEAN', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b594_edition_FACES.txt', L)
    put_json('b594_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=live_n, history=int(hist_n.group(1)) if hist_n else 0, clean=clean,
                                   beyond=len(beyond), hits=hits, held=None, n_ceils=len(CEILS), n_facts=0, n_stems=len(STEMS), n_ruled=len(RULED),
                                   n_collisions=len(COLLISIONS)))
    H = jl('b594_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'], 'live', H['live'], 'collisions', H['n_collisions'])


def repin():
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932). Writes data/b594_repin.txt."""
    E = jl('b594_edition.json')
    ed = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read().replace(chr(13), '').split(NL)
    cut = ed.index(BM_TAG)
    checks = []
    for d in E['diff']:
        checks.append(('diff %s -> :%d carries the v0.2 wording' % (d['id'], d['ed_line']), d['new'] in ed[d['ed_line'] - 1]))
    for a, s, t in HIST:
        checks.append(('history line :%d beneath draft :%d' % (E['hist_at'][str(a)], a), ed[E['hist_at'][str(a)] - 1] == t))
    for c in COLLISIONS:
        checks.append(('collision row :%d is a body line' % _edl(c[0]), ed[_edl(c[0]) - 1].strip() != ''))
    for n in CARRIED:
        checks.append(('carried :%d holds a ceiling-shaped hit' % _edl(n), CEILING.search(ed[_edl(n) - 1]) is not None))
    for d, ls in E['cited_lines'].items():
        for x in ls:
            checks.append(('Correspondence: `%s` on :%d' % (d, x), ('`%s`' % d) in ed[x - 1] and x < cut))
    checks.append(('version line above the method-register line', ed[_edl(VERSION[0]) - 3] == VERSION[1]))
    bm = NL.join(ed[cut:])
    for n in sorted(set(int(x) for x in re.findall(r'\| :(\d+) \|', bm))):
        checks.append(('back-matter row :%d is a body line' % n, 0 < n < cut and ed[n - 1].strip() != ''))
    bank = rd('b594_edition_FACES.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM THE CURRENT VERSION') and bank.count('### OFFSET FROM') == 1))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and hashlib.sha256(
        open(os.path.join(PP, *ED.split('/')), 'rb').read()).hexdigest() == E['sha256']))
    L = ['### b594 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % ED, '']
    L += ['    %-90s %s' % (w[:90], 'OK' if ok else '### FAILS') for w, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _w, ok in checks), len(checks))]
    put_txt('b594_repin.txt', L)


# ================================================================================ THE PAGES AFTER THE EDITION (the page clause)
def _page_lines(b):
    return b.decode('utf-8').split(NL)


def pages_c2():
    """### after the edition commit: each page re-emitted twice from b592's v0.16 probe banks; the diff against HEAD printed. Writes the
    ### pages and data/b594_page_runs.txt, data/b594_pages.json."""
    import chain_page as C
    import difflib
    L = ['### b594 -- THE PAGE CLAUSE (OPEN_TRAILS :12190): THE PAGES RE-EMITTED AFTER THE EDITION COMMIT, TWICE EACH, FROM THE v0.16 PROBE BANKS', '']
    J = {}
    for k in ('zeta', 'chi'):
        outs = []
        for run, dest in ((1, os.path.join(SP, 'b594_%s_run1.md' % k)), (2, os.path.join(PP, PNAME[k]))):
            rc, page, meta, log = C.build(os.path.join(D, NODES[k]), os.path.join(SP, '_b594_c2'), os.path.join(D, PROBE[k]))
            if rc:
                sys.exit('### %s RE-EMIT FAILED, exit %d: %s' % (k, rc, log[-3:]))
            b = page.encode('utf-8')
            open(dest + '.tmp', 'wb').write(b)
            os.replace(dest + '.tmp', dest)
            outs.append(b)
            L.append('### %s run %d -> %s (%d bytes)' % (k, run, dest, len(b)))
        prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
        dl = [x for x in difflib.unified_diff(_page_lines(prev), _page_lines(outs[1]), 'HEAD', 'regenerated', lineterm='', n=0)]
        J[k] = dict(identical=outs[0] == outs[1], sha256=hashlib.sha256(outs[1]).hexdigest(), diff=dl, changed=prev != outs[1])
        L += ['### the two outputs: %s ; sha256 %s ; changed against HEAD: %s' % ('BYTE-IDENTICAL' if outs[0] == outs[1] else '### DIFFER',
                                                                              J[k]['sha256'], J[k]['changed']),
              '### the diff against the page at PLACE-papers HEAD (n=0):'] + ['    ' + x[:300] for x in dl] + ['']
    put_txt('b594_page_runs.txt', L)
    put_json('b594_pages.json', J)


def page_arms(tag):
    """### G-CHAIN-PAGE and G-CHAIN-PAGE-CHI run at PLACE-papers HEAD; counts printed. Writes data/b594_page_arms_<tag>.txt."""
    import g_chain_page as GCP
    L = ['### b594 -- THE TWO PAGE ARMS RUN AT PLACE-papers HEAD %s (%s), relay tools/g_chain_page.py, from-output' % (
        g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b594_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok']
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    put_txt('b594_page_arms_%s.txt' % tag, L)


# ================================================================================ COMPONENT 3: THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
KERNELS = {'SIDE-explicit-formula': 'c404e727', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
           'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
           'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}


def scores():
    H, E, P = jl('b594_h28.json'), jl('b594_edition.json'), jl('b594_pages.json')
    a2 = rd('b594_page_arms_c2.txt')
    heads = {k: g('D:/' + k, 'rev-parse', 'main').strip() for k in KERNELS}
    kern_ok = all(heads[k].startswith(v) for k, v in KERNELS.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    lock = os.path.getmtime(os.path.join(D, 'b594_lockgate.json'))
    fresh = [x for x in g(RELAY, 'ls-files', '--others', '--exclude-standard', 'data/', 'tools/').split(NL)
             if x.strip() and os.path.getmtime(os.path.join(ROOT, x)) >= lock - 6 * 3600]
    relay_new = sorted(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD', '--', 'data/', 'tools/').split(NL) + fresh)
                       if x.strip() and not os.path.basename(x).startswith(('b594_', 'audit_b594_', 'terminal_table')) and x != 'data/b593_closing_push_out.txt')
    changed_pages = [PNAME[k] for k in ('zeta', 'chi') if P.get(k, {}).get('changed')]
    ed = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read()
    S = dict(
        N1=('HELD' if H['n_collisions'] >= 2 and not rd('b594_prompts_after_seal.txt') else 'REFUTED',
            'collisions resolved by the precedence order and listed: %d ; prompts put after the seal: none' % H['n_collisions']),
        N2=('HELD' if H['H28a'] == H['H28b'] == H['H28c'] == 'HELD' and H['held'] is None else 'REFUTED',
            'H28a %s, H28b %s, H28c %s ; held: %s' % (H['H28a'], H['H28b'], H['H28c'], H['held'] or 'none')),
        N3=('HELD' if H['n_ceils'] <= 4 and H['n_facts'] == 0 else 'REFUTED', 'ceiling corrections %d ; fact corrections %d' % (H['n_ceils'], H['n_facts'])),
        N4=('HELD' if ed.count('`h2_sign_iff_forall_upto`, SIDE-explicit-formula v0.3 = `04eda4a`') >= 1 else 'REFUTED',
            'h2_sign_iff_forall_upto cited at its pin: %d' % ed.count('`h2_sign_iff_forall_upto`, SIDE-explicit-formula v0.3 = `04eda4a`')),
        N5=('HELD' if kern_ok and pp_ch == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', ED] + changed_pages) and relay_new == [] else 'REFUTED',
            'nothing deposits; kernel heads %s; PLACE-papers %s; relay files beyond b594`s own %s' % ('unmoved' if kern_ok else heads, pp_ch, relay_new or 'none')),
        S1=('HELD' if H['n_collisions'] == 5 else 'REFUTED', 'collisions listed %d' % H['n_collisions']),
        S2=('HELD' if H['body_dn'] == 3 else 'REFUTED', 'body %+d (two history lines and the version line)' % H['body_dn']),
        S3=('HELD' if H['clean'] and H['live'] == 0 and H['n_stems'] == 0 else 'REFUTED', 'the scanner %s, live %s, stem corrections %d' % (
            'CLEAN' if H['clean'] else 'NOT CLEAN', H['live'], H['n_stems'])),
        S4=('HELD' if P and all(P[k]['identical'] for k in P) and changed_pages == [PAGE, DIR_PAGE] and 'PAGE ARMS PASSING : 2 of 2' in a2 else 'REFUTED',
            'pages changed by the edition %s, each twice byte-identical ; page arms %s' % (changed_pages,
                                                                                         re.search(r'PASSING : (\d of 2)', a2).group(1) if re.search(r'PASSING : (\d of 2)', a2) else '?')),
        S5=('HELD' if H['n_ceils'] == 0 else 'REFUTED', 'ceiling corrections %d' % H['n_ceils']),
    )
    S.update(H28a=(H['H28a'], 'the work-list row cites its pin and a bank line'), H28b=(H['H28b'], 'body %+d against at most %d' % (H['body_dn'], H['allowed'])),
             H28c=(H['H28c'], 'scanner CLEAN %s ; beyond the ceiling %d' % (H['clean'], H['beyond'])))
    put_json('b594_scores.json', S)
    for k in SCORE_KEYS + ('H28a', 'H28b', 'H28c'):
        print('  %-4s %s -- %s' % (k, S[k][0], S[k][1][:170]))


TITLE = ('## CP-7, act sixteen: the edition of FACES_OF_H2_AT_FINITE_INSTANCE from its tier block and work-list, the document’s finite-instance '
         'faces read against the compiled faces')
TRAIL_HEAD = ('### b594 — lane three, act twenty-one under (R204): CP-7 act sixteen -- the edition of FACES_OF_H2_AT_FINITE_INSTANCE written '
              'beside the draft under the precedence order; the three standing instructions entered')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def findings():
    Q = _Q()
    S, E, H, wl, rl = jl('b594_scores.json'), jl('b594_edition.json'), jl('b594_h28.json'), jl('b594_weight_line.json'), jl('b594_rule_lines.json')
    P = jl('b594_pages.json')
    Q.guard_absent(Q.FIND, TITLE[:90])
    pages = ', '.join(_pp_commit('b594 housekeeping -- the %s page' % s) for s in ('ζ', 'χ') if P.get({'ζ': 'zeta', 'χ': 'chi'}[s], {}).get('changed'))
    e = ['', TITLE, '',
         '*Filed at b594 on the author’s ruling `(R204)`. Banks: relay `data/b594_edition_FACES.txt`, `data/b594_edition.json`, '
         '`data/b594_edition_termscan.txt`, `data/b594_repin.txt`, `data/b594_page_runs.txt`. Nothing deposits.*', '',
         '**The edition** (`(R204)`(4), by the form at OPEN_TRAILS :11864, its clauses and the precedence order at :%d): `%s` beside the '
         'draft of 2026-08-18, which is unedited and is read as v0.1 (it carries no version number), sha256 `%s`. The work-list’s one '
         'row (the draft’s :180, `h1_complete_at_Phi` pinned at SIDE-kernel v1.5) rewritten to its pin, SIDE-lv-conservation v0.6.0 = '
         'c80bdc2. §2’s R4 reading (:39) names the three faces, each RH (h2_sign_iff_rh at v0.2, li_nonneg_iff_rh and '
         'arith_limit_nonneg_iff_rh at v0.9). Two readings of the ruling meet dated entries and the history clause governs: beneath '
         '§4.1 a history line says the ledger form P + A − PR and the cell’s A − PR differ by the pole term P (relay '
         'data/b550_reading37.txt :18 -- the ruling’s “b549” is b550’s bank); beneath §4.2’s mapping a history line names the '
         'finite-support ladder (h2_sign_iff_forall_upto and forall_upto_iff_rh at v0.3): a cell or a window is a rung, not the face. '
         'Five collisions resolved by the precedence order without a prompt and listed for the author’s strike; the “circularity '
         'witness” has no object in the draft. No ceiling, stem or fact correction. Body %d sentences against %d (%+d: two history '
         'lines and the version line); back matter %d. H28a %s, H28b %s, H28c %s; no sentence held. The pages re-emitted after the '
         'edition commit, each committed alone (PLACE-papers %s).' % (
             rl['lines'][0]['line'], ED, E['sha256'], E['n_body'], E['n_cur'], E['n_body'] - E['n_cur'], E['n_backmatter'],
             H['H28a'], H['H28b'], H['H28c'], pages or 'none changed'), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this edition changes the reading of the register census (FINDINGS :4788, '
         'b538) and its credit to this document’s R4 reading (FINDINGS :5563) only by naming the three faces beside the Weil form, and of b236’s §4 mapping by '
         'placing it on the finite-support ladder compiled at b559 (FINDINGS :6012); its own reading is changed by b550’s pole-term '
         'finding (relay data/b550_reading37.txt :18) and b567’s three faces (FINDINGS :6212). It strengthens two of the programme’s '
         'offerings: the compiled star (the finite-instance face set beside the RH-equivalent faces, not fused) and the edition form '
         '(its precedence order applied without a prompt).', '',
         '**The record lines.** b593’s weight at FINDINGS :%d; the precedence order at OPEN_TRAILS :%d; the three standing instructions '
         'and the research sequence at :%d.' % (wl['line'], rl['lines'][0]['line'], rl['lines'][1]['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R204)`(5): b595, the DELIBERATION_TREE module on the author’s ask, private and unpushed in TECHNE-Core; then '
         'b596, W-ORD-SIMPLICITY-FACE as the research act ahead of SIMPLICITY’s edition; the author rules on the closing.', '',
         '*Nothing deposits; no kernel written; the FACES draft unedited and still Tier N; README, REGISTRY and ERRATA unwritten; nothing '
         'here is a statement about RH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b594_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE[:90]), title=TITLE, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, TITLE[:90]))


def trail():
    Q = _Q()
    S, fj, wl, rl = jl('b594_scores.json'), jl('b594_findings.json'), jl('b594_weight_line.json'), jl('b594_rule_lines.json')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R204) ratified.** (1) b593 at its weight. (2) The precedence order. (3) The three standing instructions. (4) CP-7 act '
             'sixteen, the edition of FACES_OF_H2_AT_FINITE_INSTANCE. (5) The acts after: b595 the DELIBERATION_TREE module, b596 '
             'W-ORD-SIMPLICITY-FACE.', '',
             '**Entered:** FINDINGS.md:%d (b593’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS.md:%d (the precedence '
             'order), :%d (the three standing instructions and the research sequence), this record; PLACE-papers `%s` (the edition).' % (
                 wl['line'], fj['entry_line'], rl['lines'][0]['line'], rl['lines'][1]['line'], ED), '',
             '**Resolved by the seat under the precedence order, for the author’s strike:** five collisions (relay '
             'data/b594_edition_FACES.txt), the draft read as v0.1 for the edition’s version, and two of the ruling’s readings placed in '
             'history lines beneath dated §4 entries; no prompt was put.', '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R204)`(5), b595 the DELIBERATION_TREE module (TECHNE-Core, private, unpushed); then b596 '
             'W-ORD-SIMPLICITY-FACE; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel written; the FACES draft unedited; ERRATA untouched; FACES_LEDGER '
             'untouched; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b594_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b594_trail.json')['line'])


def desk():
    S = jl('b594_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b594 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H28a-H28c.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in ('H28a', 'H28b', 'H28c')]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)),
          '### ### **H28a %s ; H28b %s ; H28c %s.**' % (S['H28a'][0], S['H28b'][0], S['H28c'][0]), '']
    L += rd('b594_defects.txt').rstrip(NL).split(NL)
    put_txt('b594_desk_notes.txt', L)


def components():
    S, E, fj, tj, wl, rl = (jl('b594_scores.json'), jl('b594_edition.json'), jl('b594_findings.json'), jl('b594_trail.json'),
                            jl('b594_weight_line.json'), jl('b594_rule_lines.json'))
    L = ['b594 -- THE COMPONENTS, BANKED UNDER (R204).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b593`s closing push-out relay %s ; push-b593* branches deleted by name '
         '(data/b594_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b594_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b593`s weight FINDINGS :%d ; the precedence order OPEN_TRAILS :%d ; the three standing instructions :%d' % (
             wl['line'], rl['lines'][0]['line'], rl['lines'][1]['line']),
         '### COMPONENT 2 : the edition %s (sha256 %s) ; body %d vs %d ; back matter %d ; collisions %d ; H28a %s, H28b %s, H28c %s ; no '
         'sentence held ; the pages re-emitted after the edition commit (data/b594_page_runs.txt)' % (
             ED, E['sha256'][:16], E['n_body'], E['n_cur'], E['n_backmatter'], len(E['collisions']), S['H28a'][0], S['H28b'][0], S['H28c'][0]),
         '### COMPONENT 3 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b595 the DELIBERATION_TREE module, b596 '
         'W-ORD-SIMPLICITY-FACE ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b594_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b594_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
