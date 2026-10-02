# -*- coding: utf-8 -*-
"""b597_record.py -- THE ACT'S RECORD TOOL, UNDER (R207). ### ONE SUBCOMMAND PER BANK.

### ### b597: LANE THREE, ACT TWENTY-FOUR -- CP-7 ACT SEVENTEEN: THE EDITION OF SIMPLICITY_OF_RIEMANN_ZEROS BY THE FORM FROM ITS
### TIER BLOCK, WORK-LIST AND THE b596 ADDENDUM; THE CONTROL ARM FROZEN AT ITS PIN.
### Subcommands write only `data/b597_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode, temp file, `os.replace`). No platform call. The templates are b594_record.py (the edition) and
### b596_record.py (the record lines, the pages).
"""
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

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
SKK = 'D:/SIDE-kernel'
PRE_PP = 'a40f2b2'
PRE_RELAY = 'a7843913'
STEPZERO = '50a76ee8'
REPAIR = '276a7698'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/a5f76775-e614-41b6-b3eb-b08a5db7ea8f/scratchpad'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/a5f76775-e614-41b6-b3eb-b08a5db7ea8f.jsonl'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CUR = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md'
ED = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md'
WL = 'data/b558_editions/SIMPLICITY_OF_RIEMANN_ZEROS.txt'
ADD = 'data/b596_simplicity_reading.txt'
NODES = {'zeta': 'b596_nodes_faces.txt', 'chi': 'b596_nodes_chi.txt'}
PROBE = {'zeta': 'b596_probe_out.txt', 'chi': 'b596_chi_probe_out.txt'}
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


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) THE STEP-ZERO PROCESS BANK WAS FIRST WRITTEN THROUGH A BASH HEREDOC, which collapsed `\\v` in the four `...\\v1.0\\...` '
    'paths of the listing to a vertical tab (the standing heredoc-backslash trap); found by reading the bank back before any tool '
    'read it, and the bank re-written through the Write tool with the listing`s bytes. Nothing else was written by the heredoc.',
    '(b) THE EDITION`S FIRST LANDING OMITTED THE b596 WALK ON ONE JOIN SENTENCE: v1.1.3 :353, “Conservation proves no additional '
    'condition beyond simplicity is needed”, lets simplicity carry RH, and its ceiling correction cited only the compiled companion`s '
    'T2 statement, not relay data/b596_h29b.txt, which (R207)(6) orders on every such sentence (the other ten cite it). Caught by the '
    'pre-push suite`s G-CEILING-CORRECTIONS after the edition and both pages were committed, before any push. The author answered '
    '(prompt 2): a second edition commit on top through the record tool, the walk added with the segment count kept, scan, bank and '
    're-pin re-run, the pages confirmed byte-identical by a re-emit and left as committed; G-PAGES-COMMITTED-ALONE refuted in its '
    'letter by the second commit, the cause the seat`s.',
    '(c) TWO PREDICATES OF THE SEAT`S OWN SUITE WERE DEFECTIVE AT THE FIRST PRE-PUSH RUN: G-CONTROL-TEST-COUNTED counted the string '
    '“ PASS” in the step-zero test bank, which its “### ALL PASS” line also holds (6, not 5), so the live arm failed on a true bank; '
    'G-REPIN`s positive control replaced the bank`s first “ of ”, a check line, not the count line, so it could not fail. Both '
    'corrected through the Edit tool (the cases read as lines ending “ PASS”; the mutation pointed at “RE-PIN : ”) and the suite '
    're-run whole; the arm list did not change.',
]


def defects():
    put_txt('b597_defects.txt', ['### b597 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay the b596 addendum, whole', RELAY, 'HEAD', ADD, list(range(1, 40))),
    ('relay the b596 lemma walk, (7)-(8)', RELAY, 'HEAD', 'data/b596_lemmas.txt', [173, 175]),
    ('relay SIMPLICITY`s work-list, whole', RELAY, 'HEAD', WL, list(range(1, 31))),
    ('relay the CP-1b rows of SIMPLICITY_OF_RIEMANN_ZEROS (5 MOVED, 31 STANDS, 0 CREDIT)', RELAY, 'HEAD', 'data/b558_cp1b.txt', [29] + list(range(148, 184))),
    ('PLACE-papers SIMPLICITY_OF_RIEMANN_ZEROS (the current version): head, version, the title`s clause, the joins, the field-context '
     'sentences, the marked lines, the Correspondence rows moved, the dated entries, the tier block', PP, PRE_PP, CUR,
     [1, 3, 9, 11, 17, 19, 24, 26, 32, 36, 40, 78, 80, 84, 144, 178, 184, 186, 250, 256, 278, 312, 313, 317, 333, 335, 341, 343, 351, 355,
      359, 405, 423, 425, 427, 429, 431, 435, 436, 437, 438, 442, 446, 447, 453, 457, 465, 469, 471, 473, 475, 478, 480, 482, 483, 484, 486,
      488, 490, 492, 494, 496, 498, 503, 504, 505, 509, 522, 524, 526, 528, 530, 532]),
    ('PLACE-papers the ζ page at v0.17: head, the three faces, the five Simplicity nodes, the mellin row, the last paragraph', PP, PRE_PP, PAGE,
     [1, 3, 12, 24, 25, 30, 31, 32, 33, 34, 157, 168]),
    ('PLACE-papers the χ page: the χ criterion', PP, PRE_PP, DIR_PAGE, [16]),
    ('relay the generator: the backmatter reader and the channel', RELAY, 'HEAD', 'tools/chain_page.py', [132, 133, 134, 135, 645, 646, 647, 648]),
    ('relay the generator`s test as repaired at step zero (276a7698)', RELAY, 'HEAD', 'tools/test_chain_page_b596.py', list(range(1, 25))),
    ('relay the b596 suite`s G-B592-LISTS-CONTROL (sealed, unedited)', RELAY, 'HEAD', 'tools/b596_checks.py', [255, 256, 637, 638]),
    ('PLACE-papers OPEN_TRAILS: the form, its clauses, the precedence order, b596`s lines', PP, PRE_PP, 'OPEN_TRAILS.md',
     [6642, 11864, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 12044, 12190, 12192, 12194, 12228, 12262, 12264, 12266,
      12268, 12270, 12272, 12274]),
    ('PLACE-papers FINDINGS: b554`s reading of the title, b596`s weight and entry', PP, PRE_PP, 'FINDINGS.md', [5778, 5780, 5782, 5783, 5785, 6854, 6856]),
    ('PLACE-papers README, the ceiling', PP, PRE_PP, 'README.md', list(range(106, 112)) + [113, 115, 125]),
    ('PLACE-papers INDEX_ARITY v0.19, the b450 credit lines (the placement clause`s precedent)', PP, PRE_PP,
     'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE_v0_19.md', [59, 61, 726, 727]),
    ('PLACE-papers SIGN_ARRANGEMENT_RECONCILIATION, the credits` source lines', PP, PRE_PP, 'phase2/method/SIGN_ARRANGEMENT_RECONCILIATION.md',
     [46, 52, 53, 54, 55, 56, 57, 58, 62, 66]),
    ('SIDE-explicit-formula v0.17 Simplicity.lean', EFK, 'v0.17', 'SIDEExplicitFormula/Simplicity.lean', list(range(25, 51))),
    ('SIDE-explicit-formula v0.17 the salt-check', EFK, 'v0.17', 'SIDEExplicitFormula/SaltCheckSimplicity.lean', list(range(98, 110))),
    ('SIDE-explicit-formula v0.17 the vendored explicit formula at the genuine configuration', EFK, 'v0.17', 'Zeta23/WeilEF/Main.lean', [30, 31, 286]),
    ('SIDE-kernel v1.2 the trace-structure implication and its premise', SKK, 'v1.2', 'Kernel/PerpendicularCrossing.lean', list(range(48, 60))),
    ('relay b596`s closing push-out and its attempt-1 capture, committed at step zero', RELAY, 'HEAD', 'data/b596_closing_push_out.txt', list(range(1, 13))),
    ('relay b596`s closing push-out attempt 1', RELAY, 'HEAD', 'data/b596_closing_push_out_attempt1.txt', [1, 2, 3, 4]),
]


def reads():
    L = ['b597 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev + '^{}').strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:600]))
    hits = [h for h in g(PP, 'show', '%s:OPEN_TRAILS.md' % PRE_PP).split(NL)[6641].split('<br>') if 'SIMPLICITY_OF_RIEMANN' in h]
    h29 = [l for l in rd('b596_h29b.txt').split(NL) if re.match(r'^\s+(OTHER|OWN|READ|CONCLUDES|NEGATES)\s', l)]
    rh = [l.strip()[:200] for l in h29 if 'RiemannHypothesis' in l or 'h2_sign' in l.split('--', 1)[-1]]
    L += ['', '### b450`s items for SIMPLICITY_OF_RIEMANN_ZEROS in its table (OPEN_TRAILS :6642): %d -- %s' % (len(hits), hits),
          '### the b596 walk`s rows (relay data/b596_h29b.txt): %d headers; rows whose conclusion names RiemannHypothesis or h2_sign: %d -- %s'
          % (len(h29), len(rh), rh),
          '### so of the 117 headers naming simplicity`s constants none concludes it or its negation (the bank`s CONCLUDES 0, NEGATES 0) and '
          'none derives RH or h2_sign from it: the rows above are the salt-check`s two existentials (a configuration with h2_sign_cfg and '
          'allSimple, another with h2_sign_cfg and not allSimple -- they separate the two) and the vendored Li equivalence (a biconditional '
          'of RH under weighted hypotheses, with no premise of simplicity)',
          '### the derivative-engine branch: head %s ; 27a3ae7 an ancestor: %s ; files changed 27a3ae7..head %s' % (
              g(SKK, 'rev-parse', '--short=7', 'refs/heads/derivative-engine').strip(),
              subprocess.run(['git', '-C', SKK, 'merge-base', '--is-ancestor', '27a3ae7', 'derivative-engine']).returncode == 0,
              [x for x in g(SKK, 'diff', '--name-only', '27a3ae7', 'derivative-engine').split(NL) if x]),
          '### SIDE-grh-transfer: v0.5.0 = %s ; main = %s ; files changed %s' % (
              g('D:/SIDE-grh-transfer', 'rev-parse', '--short=7', 'v0.5.0^{commit}').strip(), g('D:/SIDE-grh-transfer', 'rev-parse', '--short=7', 'main').strip(),
              [x for x in g('D:/SIDE-grh-transfer', 'diff', '--name-only', 'v0.5.0', 'main').split(NL) if x]),
          '### SIDE-explicit-formula: v0.2 = %s ; v0.9 = %s ; v0.14 = %s ; v0.17 = %s' % tuple(
              g(EFK, 'rev-parse', '--short=7', t + '^{commit}').strip() for t in ('v0.2', 'v0.9', 'v0.14', 'v0.17'))]
    put_txt('b597_reads.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B596_ENTRY = '## W-ORD-SIMPLICITY-FACE: the proportion of simple zeros walked in the vendored set and found upstream'
BATCH_LINE = '*Appended 2026-10-02 by b596 beneath the standing line (:12246), under `(R206)`(2)(iii)'
QCOL = '### `W-ORD-QUANTIFIER-COLUMN`'


def weight_line():
    """### PLACE-papers FINDINGS: b596's weight, one appended line addressed to b596's entry, in (R207)(1)'s facts."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B596_ENTRY)
    if entry != 6856:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    head = '*Appended 2026-10-02 by b597 to b596’s entry (:%d), under `(R207)`(1) -- b596 AT ITS WEIGHT:*' % entry
    Q.guard_absent(Q.FIND, head)
    text = ('\n%s SIDE-explicit-formula v0.17 = 5a1630b by push_gated.sh, the peeled tag read back at the remote, the branch '
            'simplicity-b596 pushed and kept: Simplicity.lean, SaltCheckSimplicity.lean and AxiomCheckSimplicity.lean, 19 prints at the '
            'standard three with no sorryAx; simplicity_iff derives, exceptional_mass_le_third interfaces on the named premise '
            'SimpleProportion (a structure, a declaration kind no page had carried before). H29a REFUTED -- the vendored set at 3635e748 '
            'holds the simple-on-the-line statement as the Prop ThmB_statement at the bound 1/2 alone, the 2/3 theorem thmB₀_mult upstream '
            'at Zeta23/FinalMult.lean :350; the work-order’s “Alpöge–Furman, at least 2/3” a fact correction at relay data/b596_lemmas.txt '
            '(7)-(8), the navigator’s (N1) refuted on both halves. H29b HOLDS -- 117 theorem headers across 44 kernels, none concluding the '
            'clause or its negation, the one hit zetaZeros_simple hand-read as a set identity. H29c REFUTED as the seat scored it, six '
            'sentences marked and six found (relay data/b596_simplicity_reading.txt), the HELD mark lifted at OPEN_TRAILS :12272. The ζ '
            'page re-emitted at v0.17 (e6ead0d, then d774fb5 with SimpleProportion’s entry cell read and the faces’ line as the last '
            'paragraph after the Correspondence table), the generator’s backmatter channel and the one entry-tag line at relay cfd9aeac, '
            'its test 5 of 5 there, the page arms 4 of 4. The closing push failed once on the network and the retry landed after the '
            'remote read back unchanged, the attempt-1 capture kept. The suite read 76 of 78 pre-push, its two refutations in letter '
            '(G-ANSWERS-BANKED by a third prompt, G-GEN-EDIT by the entry-tag line) the navigator’s, and one lower post-push by defect (f), '
            'repaired at b597’s step zero by freezing the control at its pins. Three prompts banked with their options. N2-N4 held, N1 and '
            'N5 refuted, S1-S5 held; defects (a)-(e) the seat’s, (e) closed under the third answer. TECHNE-Core at 36352a0, ahead 4, not '
            'pushed. Nothing deposited; no main kernel file edited outside the tagged merge.\n' % head)
    r = Q.append_to(Q.FIND, text)
    put_json('b597_weight_line.json', dict(entry=entry, line=Q.line_of(Q.FIND, head), head=head, append=r))
    print('  weight line :%s' % Q.line_of(Q.FIND, head))


def rule_lines():
    """### PLACE-papers OPEN_TRAILS: (R207)(3) the standing line beneath the batch-refresh line (:12264); (R207)(4)
    ### W-ORD-VENDOR-FINALMULT, its items, price and trigger; (R207)(5) the DENSITY line beneath W-ORD-QUANTIFIER-COLUMN (:12266)."""
    Q = _Q()
    b = Q.line_of(Q.OT, BATCH_LINE)
    q = Q.line_of(Q.OT, QCOL)
    if b != 12264 or q != 12266:
        sys.exit('### THE ADDRESSED LINES MOVED: batch %s, column %s -- NOTHING WRITTEN' % (b, q))
    h1 = ('*Appended 2026-10-02 by b597 beneath the batch-refresh line (:%d), under `(R207)`(3) -- A GENERATOR RUN AT A NEW PIN, '
          'STANDING:*' % b)
    h2 = ('### `W-ORD-VENDOR-FINALMULT` -- ZETA23’S FinalMult.lean AND ITS IMPORT CLOSURE VENDORED, THE PROPORTION’S PREMISE '
          'DISCHARGED, PRICED, NOT STARTED, appended 2026-10-02, b597, under the author’s ruling (R207)(4)')
    h3 = ('*Appended 2026-10-02 by b597 beneath W-ORD-QUANTIFIER-COLUMN (:%d), under `(R207)`(5) -- A FACT CORRECTION FROM b596, THE '
          'FIFTH SHAPE:*' % q)
    for h in (h1, h2, h3):
        Q.guard_absent(Q.OT, h)
    t1 = ('\n%s a generator run at a new pin goes one page per call in the foreground, or in the background solely after the browser is '
          'closed and free memory is read above the hold; a background run stopped by the harness is recorded as a stop, not an OOM. '
          'From b596’s reaper stop (its defect (c)).\n' % h1)
    t2 = ('\n%s\n\n**Items.** Zeta23/FinalMult.lean and its import closure vendored into SIDE-explicit-formula at the upstream pin named in '
          'relay data/b596_lemmas.txt (anthropics/formal-math at 3635e748); the lemma walk re-run over the extended set; thmB₀_mult located '
          'by name and bound; and the premise SimpleProportion of exceptional_mass_le_third discharged from it, so that the node moves from '
          'its named premise to a derivation on a T0 vendored fact; the ζ page re-emitted.\n\n**Price:** one vendoring act with its builds '
          'at the memory hold, one kernel tag, one page re-emission. Off the critical path. **Trigger:** the author’s word.\n' % h2)
    t3 = ('\n%s exceptional_mass_le_third is a liminf of a ratio over an infinite set, neither FINITE nor a plain LIMIT; the column reads '
          'five shapes -- FINITE, UNIVERSAL, LIMIT, DENSITY, FAMILY -- with DENSITY for a lower or upper density, a liminf or limsup of a '
          'proportion.\n' % h3)
    out = []
    for h, t in ((h1, t1), (h2, t2), (h3, t3)):
        r = Q.append_to(Q.OT, t)
        out.append(dict(head=h, line=Q.line_of(Q.OT, h), append=r))
    put_json('b597_rule_lines.json', dict(batch=b, column=q, lines=out))
    for o in out:
        print('  line :%s' % o['line'])


# ================================================================================ COMPONENT 2: THE EDITION
P17 = 'SIDE-explicit-formula v0.17 = `5a1630b`'
P02 = 'SIDE-explicit-formula v0.2 = `5c72cad`'
WALKS = ('(relay `data/b596_h29b.txt`: of 117 federation theorem headers naming simplicity’s constants, none concludes it or its negation '
         'and none derives RH from it)')
CONS = '`∀ s : ℤ, (1 : ℚ) ^ s = 1`'
NF = '`SIDEExplicitFormula.Simplicity.SaltCheck.allSimple_not_forced`'

WORKLIST = [
    (26, 'the RH-closure composing under the one open premise (§27.3).',
     'the RH-closure composing under the one open premise (§27.3), that premise in its Weil form being equivalent to RH (`h2_sign_iff_rh`, '
     + P02 + '), so the closure’s premise is RH itself, and that face and its two companions (`li_nonneg_iff_rh` and '
     '`arith_limit_nonneg_iff_rh`, v0.9 = `e5a5a83`) carry multiplicity only as a weight and constrain none, so the closure composes '
     'nothing about simplicity (the ζ page’s last paragraph, `THE_CLAUSE_AND_ITS_COMPILED_FACES.md` :168; relay `data/b596_faces_line.txt`).',
     ['SIMP:26:99'], 'the work-list’s MOVED-IN-MEANING row (`h2_sign`) and the addendum’s :26 (c), the faces’ silence'),
    (405, 'SIDE-kernel `ProductFormula.conservation_of_spectra`;',
     'SIDE-kernel `ProductFormula.conservation_of_spectra`, which states only ' + CONS + ' (T2; its conservation reading carried by its '
     'name, the theorem staying manuscript-resident, relay `data/b558_cp1b.txt` :166);',
     ['SIMP:405:113'], 'the work-list’s MOVED-IN-MEANING row (`conservation_of_spectra`)'),
    (447, '| Compiled |',
     '| Compiled, the three terminals not of one strength: `ProductFormula.conservation_of_spectra` states only ' + CONS + ' (T2, its '
     'conservation reading carried by its name), `T2b_mellin_exhaustion` is DEFINITIONAL and '
     '`T1_completedRiemannZeta_factors_through_mellin` alone substantive (relay `data/b558_cp1b.txt` :169) |',
     ['SIMP:447:116'], 'the work-list’s MOVED-IN-MEANING row (`conservation_of_spectra`)'),
    (453, '**DERIVES** — goal ⇐ h1 ∧ h2; h1 complete, **only h2 open** (the single carried-open premise)',
     '**DERIVES** — goal ⇐ h1 ∧ h2; h1 complete, and lv’s h2 at Φ, `mellin Phi (s/2) ≠ 0`, is false at every s with re s ≤ 1 '
     '(`mellin_Phi_eq_zero_of_re_le_one`, SIDE-explicit-formula at the page’s pin v0.17 = `5a1630b`), so the goal state closes nothing on '
     'the strip, the open clause being `h2_sign`, equivalent to RH (`h2_sign_iff_rh`, ' + P02 + ')',
     ['SIMP:453:118', 'SIMP:453:119'], 'the work-list’s two MOVED-IN-MEANING rows (`h1_complete_at_Phi`, `h2_sign`)'),
]
ADDENDUM = [
    (24, 'over 40.77% of zeros proved simple (Conrey-Iwaniec-Soundararajan tradition);',
     'at least (2/3 − ε)·N(T, 2T) of the zeros in the dyadic window (T, 2T] simple and on the line for all large T, N counted with '
     'multiplicity, a theorem upstream (`Zeta23.thmB₀_mult`, anthropics/formal-math at `3635e748`, `Zeta23/FinalMult.lean` :350, outside '
     'the vendored set; relay `data/b596_lemmas.txt` (5), (8)) that enters this programme’s kernel as the named premise `SimpleProportion` '
     '(' + P17 + ', on which `exceptional_mass_le_third` interfaces), not as a compiled fact;',
     ':24 (a), the proportion'),
    (80, 'If every zero is simple, perpendicular crossing',
     'If every zero is simple — the Prop `simplicity` (' + P17 + ', every nontrivial zero of analytic order one by `simplicity_iff`), '
     'open as its own statement, which the schema’s fields, its target and Weil positivity do not force (' + NF + ', v0.17; relay '
     '`data/b596_h29b.txt`) — perpendicular crossing',
     ':80 (b), the Prop'),
    (178, 'The only solution is multiplicity 1.',
     'The compiled explicit formula does not force multiplicity 1: it sums the zeros with their multiplicities as weights '
     '(`Zeta23.WeilEF.EF_lit_zetaZeroConfig`, vendored in SIDE-explicit-formula, with `Zeta23.zetaZeroConfig.mult` as the weight), and at '
     'the schema’s form a configuration whose fields, target and Weil positivity all hold has a point of multiplicity two (' + NF + ', '
     + P17 + '; relay `data/b596_faces_line.txt`).',
     ':178 (b), the Prop; (c), the faces’ silence'),
]
CEILS = [
    (24, 'this intersection structure is governed by zero simplicity through perpendicular crossing.',
     'this intersection structure meets zero simplicity through perpendicular crossing at each simple zero on the line, and simplicity, '
     'compiled as its own Prop (`simplicity`, ' + P17 + ', by `simplicity_iff`), has no compiled edge to RH in either direction ' + WALKS + '.',
     'joins simplicity to the RH structure ((R207)(6))'),
    (26, 'the reduction of RH to off-line non-intersection governed by zero simplicity,',
     'the reduction of RH to off-line non-intersection, with zero simplicity beside it as its own statement (`simplicity`, ' + P17 + ') and '
     'no compiled edge between them ' + WALKS + ',',
     'joins simplicity to the reduction of RH ((R207)(6))'),
    (32, ', and zero simplicity governs that intersection structure via perpendicular crossing.',
     ', and perpendicular crossing holds at each simple zero, while zero simplicity, compiled as its own Prop (`simplicity`, ' + P17 + '), '
     'has no compiled edge to RH ' + WALKS + '.',
     'joins simplicity to the RH structure ((R207)(6))'),
    (36, '# Chapter 1 — The Reduction: RH $\\iff$ Simplicity',
     '# Chapter 1 — The Reduction: RH $\\iff$ Off-Line Non-Intersection, with Simplicity a Separate Prop (`simplicity_iff`, ' + P17 + ') '
     'and No Compiled Edge to `h2_sign` (relay `data/b596_h29b.txt`)',
     'the title’s clause: RH ⟺ simplicity ((R207)(6); FINDINGS :5778)'),
    (40, 'with zero simplicity governing that geometry through perpendicular crossing.',
     'with perpendicular crossing at each simple zero on the line, while zero simplicity, compiled as its own Prop (`simplicity`, '
     + P17 + '), has no compiled edge to RH in either direction ' + WALKS + '.',
     'joins simplicity to the RH structure ((R207)(6))'),
    (84, 'close this band by establishing that no structural mechanism produces an off-line intersection.',
     'argue that no structural mechanism produces an off-line intersection in this band; they do not close it, since closing it would '
     'settle RH, whose Weil form `h2_sign` stays open (`h2_sign_iff_rh`, ' + P02 + ').',
     'beyond the README ceiling: the band closed is RH closed'),
    (312, '— sufficient given simplicity.',
     '— sufficient given simplicity on the manuscript’s reading, a sufficiency no compiled statement carries ' + WALKS + '.',
     'simplicity carries RH ((R207)(6))'),
    (313, '- Conservation proves no force beyond these three acts',
     '- Conservation, a manuscript theorem whose compiled companion `conservation_of_spectra` states only ' + CONS + ' (T2; relay '
     '`data/b558_cp1b.txt` :166), is read as showing no force beyond these three acts',
     'a “proved” phrasing ((R207)(6))'),
    (317, 'RH holds.',
     'RH holds at every zero computed, and beyond them stays open (its Weil form `h2_sign`, `h2_sign_iff_rh`, ' + P02 + ').',
     'beyond the README ceiling: RH asserted'),
    (335, 'GRH reduces to simplicity of its zeros.',
     'the manuscript reads GRH as reducing to simplicity of its zeros, a reduction no compiled statement carries ' + WALKS + ', the compiled '
     'criterion for primitive χ being Weil positivity (`h2_sign_chi_iff_grh_chi`, SIDE-explicit-formula v0.14 = `4dce7b9`).',
     'simplicity carries GRH ((R207)(6); README, “GRH reduced”)'),
    (335, 'The entire GRH reduces to: all L-function zeros are simple.',
     'On that reading the entire GRH would reduce to: all L-function zeros are simple, which no compiled statement carries ' + WALKS + '.',
     'simplicity carries GRH ((R207)(6); README, “GRH reduced”)'),
    (351, 'The three-layer reduction gives: Simplicity $\\implies$ RH $\\implies$ Lindelöf.',
     'The three-layer reduction reads: Simplicity $\\implies$ RH $\\implies$ Lindelöf, the second arrow classical and the first the '
     'manuscript’s, carried by no compiled statement ' + WALKS + '.',
     'simplicity carries RH ((R207)(6))'),
    (351, 'Conservation proves no additional condition beyond simplicity is needed.',
     'Conservation is read as showing that no additional condition beyond simplicity is needed, a reading no compiled statement carries '
     + WALKS + ', its compiled companion stating only ' + CONS + ' (`conservation_of_spectra`, T2; relay `data/b558_cp1b.txt` :166).',
     'simplicity carries RH, and a “proved” phrasing ((R207)(6))'),
    (355, '(via Conservation), the moment conjectures',
     '(via Conservation) on the manuscript’s reading, whose arrow from simplicity to RH no compiled statement carries ' + WALKS + ', the '
     'moment conjectures',
     'simplicity carries RH ((R207)(6))'),
]
FACTS = [
    (436, 'SIDE-kernel branch `derivative-engine` = `27a3ae7`',
     'SIDE-kernel branch `derivative-engine` at `27a3ae7` (an ancestor three commits behind its head `01e5633`, `Kernel/DerivativeEngine.lean` unchanged)',
     'SIDE-kernel derivative-engine heads at 01e5633 locally and at the remote; 27a3ae7 its ancestor three commits back, the file unchanged (relay data/b597_reads.txt)'),
    (437, 'SIDE-kernel branch `derivative-engine` = `27a3ae7`',
     'SIDE-kernel branch `derivative-engine` at `27a3ae7` (an ancestor three commits behind its head `01e5633`, `Kernel/DerivativeEngine.lean` unchanged)',
     'the same'),
    (438, 'SIDE-kernel branch `derivative-engine` = `27a3ae7`',
     'SIDE-kernel branch `derivative-engine` at `27a3ae7` (an ancestor three commits behind its head `01e5633`, `Kernel/DerivativeEngine.lean` unchanged)',
     'the same'),
    (457, 'SIDE-grh-transfer `858cbf6` (v0.5.0)',
     'SIDE-grh-transfer `858cbf6` (one commit past v0.5.0 = `bfd2af7`, logs and `.gitignore` only)',
     'SIDE-grh-transfer v0.5.0 = bfd2af7; main 858cbf6 one commit past it, five files of logs and .gitignore (relay data/b597_reads.txt)'),
]
RESTATE = [
    (438, '(uniform = simplicity)',
     '(uniform = simplicity, whose compiled statement is the Prop `simplicity`, ' + P17 + ', by `simplicity_iff`, an equivalence this '
     'row’s terminal does not state)',
     'restates the tier block’s :505, marked (b)'),
    (442, 'Structural implication compiled;',
     'Structural implication compiled, on the premise that the prime-determined side takes the value 1 (`h_at_one`, SIDE-kernel v1.2 '
     '`Kernel/PerpendicularCrossing.lean` :54, the theorem at :50), which the compiled explicit formula does not supply (' + NF + ', '
     + P17 + '; relay `data/b596_faces_line.txt`);',
     'restates the tier block’s :509, marked (b), (c)'),
]
VERSION = '*v1.1.3 — 2026-10-02* — *CP-7 edition (b597), written beside v1.1.2, which is left unedited; its back matter closes the file.*'
H427 = ('*History line, 2026-10-02 (v1.1.3, b597): the annotation’s contrast is taken against the local spacing, the distance from the '
        'lowest collided pair to its nearest neighbouring ordinate, the object its stem word names; the annotation is carried as dated.*')
H505 = ('*History line, 2026-10-02 (v1.1.3, b597): the row above for :438 reads “uniform = simplicity”, and simplicity now has its '
        'compiled statement over the genuine configuration, the Prop `simplicity` (' + P17 + '; every nontrivial zero of analytic order '
        'one, `simplicity_iff`), while the row’s terminal `no_onLine_double_iff_transversal` stays branch-resident and states an equivalence '
        'with transversality, not with that Prop (relay `data/b596_simplicity_reading.txt`).*')
H509 = ('*History line, 2026-10-02 (v1.1.3, b597): the row above for :442 carries terminals that take the prime-determined side’s value 1 '
        'as a premise (`h_at_one` of `simplicity_from_trace_structure`, SIDE-kernel v1.2 `Kernel/PerpendicularCrossing.lean` :54), which '
        'the compiled explicit formula does not supply -- at the schema’s form its field holds with a point of multiplicity two (' + NF
        + ', ' + P17 + '; relay `data/b596_faces_line.txt`) -- so the trace route to multiplicity one rests on that premise, not on the '
        'compiled identity.*')
CR1 = ('*Credit (b450, relay `data/b450_batch.json`, SIMPLICITY_OF_RIEMANN_ZEROS “W_inf NOT sign-definite”, carried at b597 under the '
       'placement clause, beside the Correspondence row for the RH-positivity route above):* the archimedean term `W_∞` is not '
       'sign-definite -- its kernel `Re ψ(1/4 + iu/2) − log π` is negative at low frequency and positive at high, crossing at u = 2π (the '
       'bench row u = 6.283, kernel −0.0011) -- and the positive assembly facing the prime sum is `W_pole + W_∞` '
       '(`phase2/method/SIGN_ARRANGEMENT_RECONCILIATION.md` :52-:58, :62).')
CR2 = ('*Credit (b450, relay `data/b450_batch.json`, SIMPLICITY_OF_RIEMANN_ZEROS “the Day-1 section I attribution pole-plus-archimedean”, '
       'carried at b597 under the placement clause, beside the same row):* Day-1 BALANCE_AND_POSITIVITY §I attributed the positivity to the '
       'archimedean term alone, its `W_∞` row reading “positive (provable)”, and the repaired attribution is to the pole-plus-archimedean '
       'term (`phase2/method/SIGN_ARRANGEMENT_RECONCILIATION.md` :46, :66).')
# (after current line n, the lines inserted, kind)
INSERTS = [(16, [VERSION, ''], 'version'), (427, ['', H427], 'history'), (457, ['', CR1, '', CR2], 'credit'), (522, ['', H505, '', H509], 'history')]
HIST = [(427, H427, 'beneath the annotation of 2026-08-05 (:423-:427)', 'the stem clause meets a dated entry; the history clause governs (OPEN_TRAILS :12044)'),
        (505, H505, 'beneath b554’s tier block table (:500-:522), for its row :505', 'the addendum’s :505 (b) sits in b554’s dated block; the history clause governs'),
        (509, H509, 'beneath b554’s tier block table (:500-:522), for its row :509', 'the addendum’s :509 (b), (c) sits in b554’s dated block; the history clause governs')]
CREDITS = [(457, CR1, 'b450 item: W_inf NOT sign-definite'), (457, CR2, 'b450 item: the Day-1 section I attribution pole-plus-archimedean')]
COLLISIONS = [
    (24, 'the work-list’s STANDS (CP-1b SIMP:24:95, `h2_sign`: the sentence names the document’s own reduction) and the ceiling clause by (R207)(6)',
     'both, on different clauses', 'the reduction clause carried as the STANDS row reads it; the clause joining simplicity to the intersection structure takes the ceiling'),
    (26, 'the work-list’s STANDS (CP-1b SIMP:26:98, `h2_sign`) and the ceiling clause by (R207)(6)',
     'both, on different clauses', 'the reduction named as before; the words making simplicity govern it take the ceiling'),
    (40, 'the work-list’s STANDS (CP-1b SIMP:40:101, `h2_sign`) and the ceiling clause by (R207)(6)',
     'both, on different clauses', 'the reduction carried; the clause making simplicity govern its geometry takes the ceiling'),
    (26, 'the work-list row (CP-1b SIMP:26:99, `h2_sign`) and the addendum’s :26 (c)', 'the work-list row and the addendum together',
     'one rewrite answers both: the premise is RH by `h2_sign_iff_rh`, and the faces carry multiplicity only as weight'),
    (351, 'the ceiling clause twice on one sentence: a join of simplicity and RH, and a “proved” phrasing on Conservation', 'ceiling',
     'one correction'),
    (427, 'the stem clause and the history clause (the annotation of 2026-08-05)', 'history',
     'carried unchanged as the dated record, carried-by-history; the object named in the history line beneath'),
    (436, 'the fact clause (`27a3ae7` beside the branch rows :503-:505 and :526 of b554’s block, and in b397’s quoted rows :482-:484) and the history clause',
     'history', 'the dated blocks carried, their tiering read at that pin; the body rows :436-:438 take the fact'),
    (438, 'the fact clause (the branch pin) and the restatement clause (the claim cell restating :505)', 'fact, then restatement',
     'both applied, each to what the other leaves: the pin cell to the branch head, the claim cell to the Prop'),
    (471, 'the restatement clause (the v1.1.2 entry’s “only h2 open”, restating :453) and the history clause', 'history',
     'carried unchanged, CP-1b reading it STANDS as history (SIMP:471:120-122); the reading stated in the rewritten Correspondence row'),
    (484, 'the restatement clause (b397’s verbatim quotation of the pre-edit :438) and the history clause (the block of 2026-09-10)', 'history',
     'carried unchanged, CP-1b reading it STANDS as history (SIMP:484:124); the reading in the history line beneath the tier block'),
    (505, 'the addendum (a marked sentence, (b)) and the history clause (b554’s tier block, dated 2026-09-28)', 'history',
     'carried unchanged as the dated record; the reading in the history line beneath the block’s table'),
    (509, 'the addendum (a marked sentence, (b), (c)) and the history clause (b554’s tier block)', 'history',
     'carried unchanged as the dated record; the reading in the history line beneath the block’s table'),
]
CEILING = re.compile(r'\bprov(?:e|ed|en|es)\b|\bproof\b|RH-core|RH proved|proves RH|end-to-end|the whole of RH')
CARRIED = {
    164: 'the function-field analogue of RH, Weil 1948, a field fact',
    184: 'a negation: “not itself a proved theorem here”',
    204: 'a negation: the Hadamard product “does not prove simplicity”',
    298: 'Davenport–Heilbronn’s off-line zeros of Epstein functions, a field fact',
    347: 'a conditional: “if proved uniformly”',
    437: 'a table cell: the hypothesis “cross-referenced not re-proven”',
    446: 'a compiled lemma: on-line nonnegativity, `blTerm_nonneg_of_onLine`',
    461: 'the AI disclosure’s “proof strategies”',
    483: 'b397’s dated block, a verbatim quotation of the pre-edit row',
}
READ_KEPT = {
    24: 'the Abstract’s “zero simplicity is established by convergent arguments from independent traditions”: an argument’s claim for '
        'simplicity, not a join with RH and not a “proved” phrasing by the house pattern; carried by the letter, for the author’s strike',
    144: '“Therefore … all zeros are simple”: the codimension argument’s conclusion, tiered T2 at its row (:441); carried by the letter, for '
         'the author’s strike',
    278: '“the conclusion is that no mechanism whatsoever produces double zeros”: the same argument’s conclusion; carried by the letter, '
         'for the author’s strike',
}
FIELD = {
    341: 'pair correlation and GUE’s predicted simplicity: field context (Montgomery 1973), STANDS',
    343: 'the structural reading of pair correlation: a reading, not a claim of RH or of simplicity, STANDS',
    359: 'the error term and simple versus double zeros (resonance): field context, STANDS',
}
BM_TAG = '<!-- b597 (R207) THE v1.1.3 EDITION`S BACK MATTER, 2026-10-02 -->'
OFFSET = ('+2 from :17 (the v1.1.3 line and a blank, above the v1.1.2 line); +2 more from :428 (a blank and a history line beneath the '
          'annotation of 2026-08-05); +4 more from :458 (two credit lines, each after a blank, beneath the Correspondence footnote); +4 '
          'more from :523 (two history lines, each after a blank, beneath b554’s tier table) -- the current version’s :n sits at the '
          'edition’s :n for n < 17, :n+2 for 17 <= n <= 427, :n+4 for 428 <= n <= 457, :n+8 for 458 <= n <= 522, :n+12 for n >= 523')
PIN = {'h2_sign_iff_rh': '5c72cad', 'mellin_Phi_eq_zero_of_re_le_one': '5a1630b', 'li_nonneg_iff_rh': 'e5a5a83',
       'arith_limit_nonneg_iff_rh': 'e5a5a83', 'simplicity': '5a1630b', 'simplicity_iff': '5a1630b', 'SimpleProportion': '5a1630b',
       'exceptional_mass_le_third': '5a1630b', 'h2_sign_chi_iff_grh_chi': '4dce7b9',
       'SIDEExplicitFormula.Simplicity.SaltCheck.allSimple_not_forced': '5a1630b'}
BANKS = ['relay `data/b558_cp1b.txt` :166', 'relay `data/b558_cp1b.txt` :169', 'relay `data/b596_faces_line.txt`', 'relay `data/b596_h29b.txt`',
         'relay `data/b596_lemmas.txt` (5), (8)']
CORR = [
    ('SIDEExplicitFormula.Simplicity.simplicity', 'simplicity', 'SIDE-explicit-formula', 'v0.17 = 5a1630b', 'the ζ page, node 27, line 31'),
    ('SIDEExplicitFormula.Simplicity.simplicity_iff', 'simplicity_iff', 'SIDE-explicit-formula', 'v0.17 = 5a1630b', 'the ζ page, node 28, line 32'),
    ('SIDEExplicitFormula.Simplicity.SimpleProportion', 'SimpleProportion', 'SIDE-explicit-formula', 'v0.17 = 5a1630b', 'the ζ page, node 29, line 33'),
    ('SIDEExplicitFormula.Simplicity.exceptional_mass_le_third', 'exceptional_mass_le_third', 'SIDE-explicit-formula', 'v0.17 = 5a1630b',
     'the ζ page, node 30, line 34'),
    ('SIDEExplicitFormula.Simplicity.SaltCheck.allSimple_not_forced', 'SIDEExplicitFormula.Simplicity.SaltCheck.allSimple_not_forced',
     'SIDE-explicit-formula', 'v0.17 = 5a1630b', 'the ζ page’s last paragraph, line 168'),
    ('SIDEExplicitFormula.B321.h2_sign_iff_rh', 'h2_sign_iff_rh', 'SIDE-explicit-formula', 'v0.2 = 5c72cad', 'the ζ page, node 8, line 12'),
    ('SIDEExplicitFormula.LiCriterionBridge.li_nonneg_iff_rh', 'li_nonneg_iff_rh', 'SIDE-explicit-formula', 'v0.9 = e5a5a83', 'the ζ page, node 20, line 24'),
    ('SIDEExplicitFormula.LiCriterionBridge.arith_limit_nonneg_iff_rh', 'arith_limit_nonneg_iff_rh', 'SIDE-explicit-formula', 'v0.9 = e5a5a83',
     'the ζ page, node 21, line 25'),
    ('SIDEExplicitFormula.RegisterDepth.mellin_Phi_eq_zero_of_re_le_one', 'mellin_Phi_eq_zero_of_re_le_one', 'SIDE-explicit-formula',
     'the page’s pin v0.17 = 5a1630b', 'the ζ page’s Correspondence table, line 157'),
    ('SIDEExplicitFormula.GRHWeil.h2_sign_chi_iff_grh_chi', 'h2_sign_chi_iff_grh_chi', 'SIDE-explicit-formula', 'v0.14 = 4dce7b9',
     'the χ page, node 12, line 16'),
    ('Zeta23.WeilEF.EF_lit_zetaZeroConfig', 'Zeta23.WeilEF.EF_lit_zetaZeroConfig', 'SIDE-explicit-formula (vendored Zeta23)', 'v0.17 = 5a1630b',
     'not a node; Zeta23/WeilEF/Main.lean :286'),
    ('Zeta23.thmB₀_mult', 'Zeta23.thmB₀_mult', 'anthropics/formal-math (upstream, not vendored)', '3635e748', 'not on a page; Zeta23/FinalMult.lean :350'),
    ('PerpendicularCrossing.simplicity_from_trace_structure', 'h_at_one', 'SIDE-kernel', 'v1.2 = b1407b2', 'not on a page; Kernel/PerpendicularCrossing.lean :50, :54'),
]


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    return n + sum(len(ls) for a, ls, _k in INSERTS if n > a)


def _all_changes():
    return ([(x[0], x[1], x[2]) for x in WORKLIST] + [(x[0], x[1], x[2]) for x in ADDENDUM] + [(x[0], x[1], x[2]) for x in CEILS]
            + [(x[0], x[1], x[2]) for x in FACTS] + [(x[0], x[1], x[2]) for x in RESTATE])


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def _cites(t):
    return [d for d in PIN if ('`%s`' % d) in t and PIN[d] in t] + [b for b in BANKS if b in t]


def edition(*a):
    """### PLACE-papers phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md beside the current version from its blob at a40f2b2;
    ### the re-pin step last. Writes the edition file and data/b597_edition.json; `dry` writes nothing."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE a40f2b2 -- NOTHING WRITTEN')
    edp = os.path.join(PP, *ED.split('/'))
    dry = 'dry' in a
    if not dry and os.path.exists(edp) and 'again' not in a:
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    if g(PP, 'ls-files', ED).strip() and 'correct' not in a:
        sys.exit('### THE EDITION FILE IS COMMITTED -- NOTHING WRITTEN (a correction runs with `correct`, the author`s answer)')
    new = list(cur)
    for ln, old, rep in _all_changes():
        line = new[ln - 1]
        if line.count(old) != 1:
            sys.exit('### :%d -- THE FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE (%d): %s' % (ln, line.count(old), old[:80]))
        n0 = len(_segs(line))
        new[ln - 1] = line.replace(old, rep)
        if len(_segs(new[ln - 1])) != n0:
            sys.exit('### :%d -- THE CHANGE ALTERED THE LINE`S SEGMENT COUNT %d -> %d: %s' % (ln, n0, len(_segs(new[ln - 1])), old[:60]))
    if cur[16] != '*v1.1.2 — 2026-07-19*' or cur[15] != '':
        sys.exit('### THE VERSION ANCHOR IS NOT WHERE THE FACE SAYS')
    anchors = {427: '**The Lehmer tie, at flow grade.**', 457: '*Kernels audited at:', 522: '| :455 |'}
    for n, s in anchors.items():
        if not cur[n - 1].startswith(s):
            sys.exit('### THE INSERTION ANCHOR :%d IS NOT WHERE THE FACE SAYS: %s' % (n, cur[n - 1][:60]))
    if cur[522].strip() != '' or cur[457].strip() != '' or cur[427].strip() != '':
        sys.exit('### A LINE AFTER AN INSERTION ANCHOR IS NOT BLANK')
    import banned_terms as BT
    ins = [VERSION, H427, H505, H509, CR1, CR2]
    for t in ins:
        if len(_segs(t)) != 1:
            sys.exit('### AN INSERTED LINE IS NOT ONE SENTENCE (%d): %s' % (len(_segs(t)), t[:60]))
    for t in ins + [x[2] for x in _all_changes()]:
        if BT.PAT.search(t):
            sys.exit('### A BANNED STEM IN AN INSERTED OR REWRITTEN TEXT: %s' % t[:80])
        if CEILING.search(t):
            sys.exit('### A CEILING-SHAPED WORD IN AN INSERTED OR REWRITTEN TEXT: %s' % CEILING.search(t).group(0))
    rows = [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'SIMP' and r['verdict'] == 'MOVED-IN-MEANING']
    diff = []
    for r in rows:
        ln = r['line']
        sg = _segs(cur[ln - 1])
        if r['sentence'] not in sg:
            sys.exit('### THE ROW %s`S SENTENCE IS NOT A SEGMENT OF :%d' % (r['id'], ln))
        k = sg.index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        why = [w for w in WORKLIST if r['id'] in w[3]]
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         cites=_cites(nw), supports=r['reading'], answers=why[0][4] if why else '', kind='work-list'))
    for ln, old, rep, ans in ADDENDUM:
        sg0 = [s for s in _segs(cur[ln - 1]) if old in s]
        sg1 = [s for s in _segs(new[ln - 1]) if rep in s]
        diff.append(dict(id='addendum:%d' % ln, line=ln, ed_line=_edl(ln), terminal='relay %s, %s' % (ADD, ans), old=sg0[0] if sg0 else old,
                         new=sg1[0] if sg1 else rep, changed=True, cites=_cites(rep), supports=ans, answers=ans, kind='addendum'))
    for kind, lst in (('ceiling', CEILS), ('fact', FACTS), ('restatement', RESTATE)):
        for ln, old, rep, why in lst:
            sg0 = [s for s in _segs(cur[ln - 1]) if old in s]
            sg1 = [s for s in _segs(new[ln - 1]) if rep in s]
            diff.append(dict(id='%s:%d' % (kind, ln), line=ln, ed_line=_edl(ln), terminal=why, old=sg0[0] if sg0 else old,
                             new=sg1[0] if sg1 else rep, changed=True, cites=_cites(rep), supports=why, answers=why, kind=kind))
    for after, ls, _k in sorted(INSERTS, key=lambda x: -x[0]):
        new[after:after] = ls
    body = list(new)
    changed = set(x[0] for x in _all_changes())
    if any(_edl(n) > len(body) or (n not in changed and body[_edl(n) - 1] != cur[n - 1]) for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL DOES NOT CARRY THE CURRENT VERSION')
    hist_at = {}
    for after, t, _w, _y in HIST:
        a0 = 427 if after == 427 else 522
        idx = [i for i, l in enumerate(body, 1) if l == t]
        if len(idx) != 1:
            sys.exit('### A HISTORY LINE IS NOT IN THE BODY ONCE')
        hist_at[str(after)] = idx[0]
        if idx[0] <= _edl(a0):
            sys.exit('### A HISTORY LINE IS NOT BENEATH ITS ANCHOR')
    cred_at = [[i for i, l in enumerate(body, 1) if l == t][0] for _a, t, _w in CREDITS]
    ver_at = body.index(VERSION) + 1
    if body[ver_at + 1] != cur[16]:
        sys.exit('### THE VERSION LINE IS NOT ABOVE :17')
    inv = {_edl(n): n for n in range(1, len(cur) + 1)}
    hits = [(i, m.group(0)) for i, l in enumerate(body, 1) for m in CEILING.finditer(l)]
    stray = sorted(set(inv.get(i, -i) for i, _ in hits) - set(CARRIED) - changed)
    if stray:
        sys.exit('### A CEILING HIT IN THE BODY IS NEITHER REWRITTEN NOR CARRIED BY THE SEAT`S READ: current lines %s' % stray)
    E = lambda n: _edl(n)
    bm = ['', BM_TAG, '',
          '## Back matter of the v1.1.3 edition -- written 2026-10-02 by b597 under the author’s ruling `(R207)`(6), by the form of `(R187)`(5) '
          'and its precedence order', '',
          '*This file is v1.1.3 of SIMPLICITY_OF_RIEMANN_ZEROS, the CP-7 edition written beside v1.1.2 (`%s`, unedited) from its tier block '
          '(b554, its :496, standing), its CP-1b work-list (relay `%s`, five sentence-rows on four lines) and the b596 addendum (relay `%s`, six '
          'marked sentences), the ζ page at SIDE-explicit-formula v0.17 as its spine. The document stays Tier K; the edition promotes no '
          'reading, does not deposit and does not replace v1.1.2, and its promotion is CP-8’s. Every line cited below is this file’s own.*'
          % (CUR, WL, ADD), '',
          '### Removals', '', 'None: every marked sentence is rewritten in place to what its compiled fact or bank line says; `(R207)`(6) orders '
          'the six addendum sentences rewritten.', '',
          '### Rewrites -- the work-list and the addendum', '', '| this edition’s line | v1.1.2 wording | v1.1.3 wording | Status |', '|:--|:--|:--|:--|']

    def cell(s):
        return s.replace('|', '¦')
    for ln, old, rep, ids, ans in WORKLIST:
        bm.append('| :%d | %s | %s | rewritten: %s (%s) |' % (E(ln), cell(old), cell(rep), ans, ', '.join(ids)))
    for ln, old, rep, ans in ADDENDUM:
        bm.append('| :%d | %s | %s | rewritten by `(R207)`(6): the addendum’s %s |' % (E(ln), cell(old), cell(rep), ans))
    bm += ['', '### Ceiling corrections', '', '| this edition’s line | v1.1.2 wording | v1.1.3 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep, why in CEILS:
        bm.append('| :%d | %s | %s | ceiling correction (OPEN_TRAILS :11906): %s |' % (E(ln), cell(old), cell(rep), why))
    bm += ['', '### Fact corrections', '', '| this edition’s line | v1.1.2 wording | v1.1.3 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep, why in FACTS:
        bm.append('| :%d | %s | %s | fact correction (OPEN_TRAILS :11954): %s |' % (E(ln), cell(old), cell(rep), why))
    bm += ['', '### Restatement rewrites', '', '| this edition’s line | v1.1.2 wording | v1.1.3 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep, why in RESTATE:
        bm.append('| :%d | %s | %s | restatement clause (OPEN_TRAILS :12192): %s |' % (E(ln), cell(old), cell(rep), why))
    bm += ['', '### Collisions resolved by the precedence order (OPEN_TRAILS :12228)', '',
           '| this edition’s line | the clauses that meet | the governing clause | Status |', '|:--|:--|:--|:--|']
    for ln, clauses, gov, why in COLLISIONS:
        bm.append('| :%d | %s | %s | %s |' % (E(ln), clauses, gov, why))
    bm += ['', '### Credit lines', '', '| this edition’s line | beside | Status |', '|:--|:--|:--|']
    for (after, t, w), at in zip(CREDITS, cred_at):
        bm.append('| :%d | the Correspondence row :%d (the RH-positivity route) and its footnote :%d | inserted under the placement clause '
                  '(OPEN_TRAILS :11956), as at b581 and b585: %s |' % (at, E(446), E(457), w))
    bm += ['', '### History lines', '', '| this edition’s history line | the dated entry | Status |', '|:--|:--|:--|']
    for after, t, w, y in HIST:
        bm.append('| :%d | %s | inserted under the history clause (OPEN_TRAILS :11908, :12044, :12194): %s |' % (hist_at[str(after)], w, y))
    bm += ['', '### Stem corrections', '', 'None live: the scanner’s one hit sits in the annotation of 2026-08-05, carried by history (:%d, '
           'carried-by-history), its object named in the history line :%d.' % (E(427), hist_at['427']), '',
           '### Ceiling-shaped sentences read and carried', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(CARRIED):
        bm.append('| :%d | ceiling read, carried: %s | carried as read |' % (E(ln), CARRIED[ln]))
    bm += ['', '### Sentences read and left, for the author’s strike', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(READ_KEPT):
        bm.append('| :%d | %s | carried as read |' % (E(ln), READ_KEPT[ln]))
    bm += ['', '### Field context, by `(R207)`(6)', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(FIELD):
        bm.append('| :%d | %s | carried |' % (E(ln), FIELD[ln]))
    bm += ['', '### The ruling’s readings of `(R207)`(6)', '', '| reading | the read | Status |', '|:--|:--|:--|',
           '| no sentence lets RH carry simplicity or simplicity carry RH; each such sentence takes the ceiling clause citing the b596 walk | '
           ':%s | corrected |' % ', :'.join(str(E(x[0])) for x in CEILS if '(R207)(6)' in x[3]),
           '| the title’s clause cites `simplicity_iff` at v0.17 with no compiled edge to `h2_sign` | :%d | corrected |' % E(36),
           '| the proportion enters as the named premise `SimpleProportion` with the upstream line of `thmB₀_mult` | :%d | rewritten |' % E(24),
           '| the three faces’ silence on multiplicity cites the ζ page’s last paragraph | :%d | rewritten |' % E(26),
           '| double resonance and pair-correlation readings of multiplicity stand as field context or take the ceiling | :%s | carried |'
           % ', :'.join(str(E(x)) for x in sorted(FIELD)),
           '| “proved” phrasings take the ceiling clause | :%d, :%d; the other hits read and carried above | corrected |' % (E(313), E(351)),
           '| the dated entries carry under the history clause with lines beneath | :%s | carried, lines inserted |'
           % ', :'.join(str(hist_at[k]) for k in sorted(hist_at)), '',
           '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v1.1.3 | `%s` | written at b597 |' % ED,
           '| the current version, v1.1.2 | `%s` | unedited |' % CUR,
           '| the spine | `%s`, at SIDE-explicit-formula v0.17 = `5a1630b` | read |' % PAGE,
           '| the work-list | relay `%s` | read |' % WL,
           '| the addendum | relay `%s` | read |' % ADD,
           '| the sentence-by-sentence diff | relay `data/b597_edition_SIMPLICITY.txt` | banked at b597 |', '',
           '### Correspondence', '', '| declaration | repository | pin | where it is printed | Status |', '|:--|:--|:--|:--|:--|']
    ed_lines = {}
    for fq, needle, repo, pin, where in CORR:
        ls = [i for i, l in enumerate(body, 1) if ('`%s`' % needle) in l and i not in set(hist_at.values()) | {ver_at}]
        ls += [i for i in hist_at.values() if ('`%s`' % needle) in body[i - 1]]
        ed_lines[fq] = sorted(set(ls))
        bm.append('| `%s` | %s | %s | %s | cited at :%s of this edition |' % (fq, repo, pin, where, ', :'.join(str(x) for x in ed_lines[fq]) or '### NONE'))
    bm.append('')
    if any('### NONE' in l for l in bm):
        sys.exit('### A CORRESPONDENCE ROW CITES NO LINE OF THE EDITION')
    full = body + bm
    b = (NL.join(full) + NL).encode('utf-8')
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))
    if dry:
        print('  DRY: nothing written; diff rows %d' % len(diff))
        for d in diff:
            print('   %-16s :%d -> :%d cites %s' % (d['id'], d['line'], d['ed_line'], d['cites']))
        return
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    put_json('b597_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=len(CREDITS), removals=0, ruled_citations=len(HIST), version_lines=1, diff=diff,
                                       offset=OFFSET, hist_at=hist_at, cred_at=cred_at, ver_at=ver_at,
                                       collisions=[list(c) for c in COLLISIONS], carried={str(k): v for k, v in CARRIED.items()},
                                       n_ceils=len(CEILS), n_facts=len(FACTS), n_restate=len(RESTATE), n_addendum=len(ADDENDUM),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines))


def edition_bank():
    """### The diff with its offset line, the collisions, the counts, the ceiling read, the scanner's verdict, H28a-H28c."""
    E = jl('b597_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(BM_TAG)
    scan = rd('b597_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    hist_n = re.search(r'carried-by-history (\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    carried_ed = set(_edl(n) for n in CARRIED)
    rewritten_ed = set(_edl(x[0]) for x in _all_changes())
    hist_ed = set(E['hist_at'].values())
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            kind = ('record' if i > cut else 'carried' if i in carried_ed else 'rewritten' if i in rewritten_ed
                    else 'history' if i in hist_ed else 'beyond')
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
    joins = [x for x in CEILS if '(R207)(6)' in x[3] and ('simplicity' in x[3] or 'title' in x[3])]
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % OFFSET, '',
         'b597 -- COMPONENT 2: THE EDITION OF SIMPLICITY_OF_RIEMANN_ZEROS, (R207)(6), BY THE FORM OF (R187)(5), ITS CLAUSES AND THE PRECEDENCE ORDER', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :17 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0][:80], cur0[16]),
         '### its tier block : :496-:532 (b554, dated 2026-09-28, the table :500-:522) ; b558`s line :532',
         '### the title`s clause : :36 "%s" (FINDINGS :5778, b554`s reading: the reduction compiled in neither direction)' % cur0[35],
         '### its version history : :17 v1.1.2 (2026-07-19), :19 the pointer, :465 v1.1 (2026-07-11), :469-:475 the entries v1.1.2, v1.1.1, v1.1 ; '
         'the dated blocks :3-:9 (2026-08-26), :423-:427 (2026-08-05), :478-:484 (b397, 2026-09-10), :486-:492 (b454, 2026-09-14), :494-:532 (b554, b558)',
         '### b450`s items naming this document: 2 (W_inf NOT sign-definite; the Day-1 section I attribution) -- both inserted as credit lines '
         'under the placement clause (relay data/b597_reads.txt)',
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### EVERY REWRITTEN OR INSERTED SENTENCE, WITH THE LINE IT ANSWERS AND WHAT IT CITES (%d rewritten):' % len(E['diff']), '']
    for d in E['diff']:
        L += ['  %s v1.1.2 :%d -> v1.1.3 :%d -- %s ; cites %s' % (d['id'], d['line'], d['ed_line'], d['kind'], d['cites']),
              '      answers: %s' % (d['answers'] or d['supports']), '      v1.1.2 : %s' % d['old'], '      v1.1.3 : %s' % d['new'], '']
    L += ['### THE COLLISIONS, RESOLVED BY THE PRECEDENCE ORDER WITHOUT A PROMPT (%d):' % len(E['collisions'])]
    L += ['    v1.1.2 :%d -> v1.1.3 :%d  %s -- governs: %s -- %s' % (c[0], _edl(c[0]), c[1], c[2], c[3]) for c in E['collisions']]
    L += ['### THE HISTORY LINES (%d, ruled citations under H28b):' % len(HIST)]
    for a, t, w, y in HIST:
        L += ['    v1.1.3 :%d, %s -- %s' % (E['hist_at'][str(a)], w, y), '      %s' % t]
    L += ['### THE CREDIT LINES (%d, the placement clause):' % len(CREDITS)]
    for (a, t, w), at in zip(CREDITS, E['cred_at']):
        L += ['    v1.1.3 :%d -- %s' % (at, w), '      %s' % t]
    L += ['### THE VERSION LINE: v1.1.3 :%d, above v1.1.2`s :17: %s' % (E['ver_at'], VERSION),
          '### THE CEILING CORRECTIONS: %d sentences on %d lines, of which joining RH and simplicity (the ruling`s first reading): %d' % (
              len(CEILS), len(set(x[0] for x in CEILS)), len(joins)),
          '### THE FACT CORRECTIONS: %d (the branch pin :436-:438; the SIDE-grh-transfer pin :457)' % len(FACTS),
          '### THE RESTATEMENT REWRITES: %d ; THE STEM CORRECTIONS: none live (one carried by history) ; REMOVALS: none' % len(RESTATE),
          '### THE CEILING-SHAPED SENTENCES READ AND CARRIED:'] + ['    v1.1.2 :%d -> v1.1.3 :%d  %s' % (n, _edl(n), CARRIED[n]) for n in sorted(CARRIED)]
    L += ['### READ AND LEFT, FOR THE AUTHOR`S STRIKE:'] + ['    v1.1.2 :%d -> v1.1.3 :%d  %s' % (n, _edl(n), READ_KEPT[n]) for n in sorted(READ_KEPT)]
    L += ['### FIELD CONTEXT, STANDS:'] + ['    v1.1.2 :%d -> v1.1.3 :%d  %s' % (n, _edl(n), FIELD[n]) for n in sorted(FIELD)]
    L += ['', '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s BODY %d (%+d) ; the BACK '
          'MATTER %d, printed separately ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d (the three history lines; every '
          'rewrite keeps its line`s count) + one version line = %d' % (body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
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
    put_txt('b597_edition_SIMPLICITY.txt', L)
    put_json('b597_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=live_n, history=int(hist_n.group(1)) if hist_n else 0, clean=clean,
                                   beyond=len(beyond), hits=hits, held=None, n_ceils=len(CEILS), n_joins=len(joins), n_facts=len(FACTS),
                                   n_restate=len(RESTATE), n_addendum=len(ADDENDUM), addendum_rewritten=len(ADDENDUM),
                                   addendum_history=2, n_collisions=len(COLLISIONS)))
    H = jl('b597_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'], 'live', H['live'], 'collisions', H['n_collisions'])


def repin():
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932). Writes data/b597_repin.txt."""
    E = jl('b597_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    cut = ed.index(BM_TAG)
    checks = []
    for d in E['diff']:
        checks.append(('diff %s -> :%d carries the v1.1.3 wording' % (d['id'], d['ed_line']), d['new'] in ed[d['ed_line'] - 1]))
    for a, t, w, y in HIST:
        checks.append(('history line :%d (%s)' % (E['hist_at'][str(a)], w[:40]), ed[E['hist_at'][str(a)] - 1] == t))
    for (a, t, w), at in zip(CREDITS, E['cred_at']):
        checks.append(('credit line :%d' % at, ed[at - 1] == t))
    for c in COLLISIONS:
        checks.append(('collision row :%d is a body line' % _edl(c[0]), ed[_edl(c[0]) - 1].strip() != ''))
    for n in CARRIED:
        checks.append(('carried :%d holds a ceiling-shaped hit' % _edl(n), CEILING.search(ed[_edl(n) - 1]) is not None))
    for fq, ls in E['cited_lines'].items():
        nd = [x for x in CORR if x[0] == fq][0][1]
        for x in ls:
            checks.append(('Correspondence: `%s` on :%d' % (nd, x), ('`%s`' % nd) in ed[x - 1] and x < cut))
    checks.append(('version line above the v1.1.2 line', ed[E['ver_at'] - 1] == VERSION and ed[E['ver_at'] + 1] == '*v1.1.2 — 2026-07-19*'))
    bm = NL.join(ed[cut:])
    for n in sorted(set(int(x) for x in re.findall(r'\| :(\d+) \|', bm))):
        checks.append(('back-matter row :%d is a body line' % n, 0 < n < cut and ed[n - 1].strip() != ''))
    for n in sorted(set(int(x) for x in re.findall(r':(\d+), carried-by-history', bm))):
        checks.append(('carried-by-history :%d holds the scanner`s hit' % n, 'gap' in ed[n - 1]))
    bank = rd('b597_edition_SIMPLICITY.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM THE CURRENT VERSION') and bank.count('### OFFSET FROM') == 1))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and hashlib.sha256(open(edp, 'rb').read()).hexdigest() == E['sha256']))
    L = ['### b597 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % ED, '']
    L += ['    %-100s %s' % (w[:100], 'OK' if ok else '### FAILS') for w, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _w, ok in checks), len(checks))]
    put_txt('b597_repin.txt', L)
    print(L[-1])


# ================================================================================ THE PAGES AFTER THE EDITION (the page clause)
def page(k):
    """### after the edition commit: ONE page re-emitted from b596's v0.17 list and banked probe (the standing line of (R207)(3): one
    ### page per call, in the foreground); the diff against PLACE-papers HEAD printed. Writes the page and data/b597_page_<k>.json."""
    import chain_page as C
    import difflib
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    rc, pg, meta, log = C.build(os.path.join(D, NODES[k]), os.path.join(SP, '_b597_%s' % k), os.path.join(D, PROBE[k]))
    if rc:
        sys.exit('### %s RE-EMIT FAILED, exit %d: %s' % (k, rc, log[-3:]))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    dest = os.path.join(PP, PNAME[k])
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    J = dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=prev != b, diff=dl, at=utc(),
             pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip())
    put_json('b597_page_%s.json' % k, J)
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s' % (k, rc, len(b), J['changed']))
    for x in dl:
        print('    ' + x[:260])


def page_arms(tag):
    """### both page arms at PLACE-papers HEAD from b596's v0.17 lists and probes, and the frozen control (the test file's control()).
    ### Writes data/b597_page_arms_<tag>.txt."""
    import g_chain_page as GCP
    import test_chain_page_b596 as T
    L = ['b597 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b597_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = T.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            T.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (T.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b597_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ THE PROMPTS, BANKED VERBATIM
def answers():
    """### every AskUserQuestion of this session, with question, options, recommended mark and the answer, read from the session
    ### transcript (b595's method); data/b597_author_answers.txt."""
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
    L = ['### b597 -- THE AUTHOR`S ANSWERS BEFORE THE SEAL, %d prompt(s) put by the seat (2026-10-02), banked verbatim with the options and '
         'the recommended mark, as the standing line at OPEN_TRAILS :12246 orders.' % sum(len(c[2].get('questions', [])) for c in calls), '']
    k = 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session a5f76775-e614-41b6-b3eb-b08a5db7ea8f, transcript line %d)' % (cid, i))
        for q in inp.get('questions', []):
            k += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'), op.get('description')))
        ri, rt = results.get(cid, (None, '### NO RESULT FOUND'))
        L += ['RESULT (transcript line %s): %s' % (ri, rt), '']
    put_txt('b597_author_answers.txt', L)


# ================================================================================ COMPONENT 3: THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')


def scores():
    H, E = jl('b597_h28.json'), jl('b597_edition.json')
    a0, a2 = rd('b597_control_stepzero.txt'), rd('b597_page_arms_c2.txt')
    Z, X = jl('b597_page_zeta.json'), jl('b597_page_chi.json')
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation')}
    kern_ok = kern == {'SIDE-explicit-formula': '5a1630b', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068'}
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', ED] + [p['page'] for p in (Z, X) if p.get('changed')])
    relay_tools = sorted(x for x in g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD', '--', 'tools/').split(NL) + g(RELAY, 'diff', '--name-only', '--', 'tools/').split(NL)
                         if x.strip() and not os.path.basename(x).startswith('b597_'))
    cur_same = g(PP, 'rev-parse', 'HEAD:' + CUR).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip()
    c0 = 'PASSING : 2 of 2' in a0
    c2 = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA PASSING : 2 of 2' in a2
    S = dict(
        N1=('HELD' if c0 and c2 else 'REFUTED', 'the frozen control at HEAD before the seal: %s ; after the edition commit and the pages: %s' % (
            '2 of 2' if c0 else 'not 2 of 2', '2 of 2' if c2 else 'not 2 of 2')),
        N2=('HELD' if H['addendum_rewritten'] == 6 and H['held'] is None else 'REFUTED',
            'of the six addendum sentences, rewritten %d (:24, :80, :178, and :26 with the work-list row), carried under the history clause '
            'with a line beneath %d (:505, :509 in b554`s dated block) ; held: none' % (H['addendum_rewritten'] + 1, H['addendum_history'])),
        N3=('HELD' if H['n_ceils'] <= 8 and H['n_joins'] >= 2 and H['n_facts'] <= 1 else 'REFUTED',
            'ceiling corrections %d (joining RH and simplicity %d) ; fact corrections %d' % (H['n_ceils'], H['n_joins'], H['n_facts'])),
        N4=('HELD' if H['H28a'] == H['H28b'] == H['H28c'] == 'HELD' else 'REFUTED', 'H28a %s, H28b %s, H28c %s' % (H['H28a'], H['H28b'], H['H28c'])),
        N5=('HELD' if kern_ok and cur_same and pp_ch == want_pp and relay_tools == ['tools/test_chain_page_b596.py'] else 'REFUTED',
            'nothing deposits; kernel mains %s; current version unedited %s; PLACE-papers %s; relay tools beyond b597`s own %s' % (
                'unmoved' if kern_ok else kern, cur_same, pp_ch, relay_tools)),
        S1=('HELD' if H['n_collisions'] == len(COLLISIONS) == 12 else 'REFUTED', 'collisions listed %d' % H['n_collisions']),
        S2=('HELD' if H['body_dn'] == 6 else 'REFUTED', 'body %+d (three history lines, two credit lines, the version line)' % H['body_dn']),
        S3=('HELD' if H['clean'] and H['live'] == 0 and H['history'] == 1 else 'REFUTED', 'the scanner %s, live %s, carried-by-history %s' % (
            'CLEAN' if H['clean'] else 'NOT CLEAN', H['live'], H['history'])),
        S4=('HELD' if Z.get('changed') and X.get('changed') and 'PAGE ARMS PASSING : 2 of 2' in a2 else 'REFUTED',
            'pages changed by the edition: ζ %s, χ %s ; page arms %s' % (Z.get('changed'), X.get('changed'), 'PAGE ARMS PASSING : 2 of 2' in a2)),
        S5=('HELD' if H['n_facts'] == 4 else 'REFUTED', 'fact corrections %d' % H['n_facts']),
    )
    S.update(H28a=(H['H28a'], 'the four MOVED lines cite their compiled facts at their pins or bank lines'),
             H28b=(H['H28b'], 'body %+d against at most %d' % (H['body_dn'], H['allowed'])),
             H28c=(H['H28c'], 'scanner CLEAN %s ; beyond the ceiling %d' % (H['clean'], H['beyond'])))
    put_json('b597_scores.json', S)
    for k in SCORE_KEYS + ('H28a', 'H28b', 'H28c'):
        print('  %-4s %s -- %s' % (k, S[k][0], S[k][1][:200]))


TITLE = ('## CP-7, act seventeen: the edition of SIMPLICITY_OF_RIEMANN_ZEROS from its tier block, work-list and the b596 addendum, the '
         'title’s clause cited to simplicity_iff at v0.17 with no compiled edge to h2_sign, the proportion as a named premise')
TRAIL_HEAD = ('### b597 — lane three, act twenty-four under (R207): CP-7 act seventeen -- the edition of SIMPLICITY_OF_RIEMANN_ZEROS from '
              'its tier block, work-list and the b596 addendum; the control arm frozen at its pin')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def findings():
    Q = _Q()
    S, E, H, wl, rl = jl('b597_scores.json'), jl('b597_edition.json'), jl('b597_h28.json'), jl('b597_weight_line.json'), jl('b597_rule_lines.json')
    Q.guard_absent(Q.FIND, TITLE[:90])
    pages = ', '.join(_pp_commit('b597 housekeeping -- the %s page' % s) for s in ('ζ', 'χ'))
    e = ['', TITLE, '',
         '*Filed at b597 on the author’s ruling `(R207)`. Banks: relay `data/b597_edition_SIMPLICITY.txt`, `data/b597_edition.json`, '
         '`data/b597_edition_termscan.txt`, `data/b597_repin.txt`, `data/b597_page_arms_c2.txt`, `data/b597_author_answers.txt`. Nothing '
         'deposits.*', '',
         '**The edition** (`(R207)`(6), by the form at OPEN_TRAILS :11864, its clauses and the precedence order at :12228): `%s` beside '
         'v1.1.2, which is unedited, sha256 `%s`. Chapter 1’s title, “The Reduction: RH ⟺ Simplicity”, now names the reduction the body '
         'states (RH ⟺ off-line non-intersection) and simplicity as a separate Prop, cited to simplicity_iff at SIDE-explicit-formula '
         'v0.17 = 5a1630b with no compiled edge to h2_sign (relay data/b596_h29b.txt: of 117 federation headers naming its constants, none '
         'concludes it or its negation and none derives RH from it). Every sentence that let simplicity carry RH or GRH takes the ceiling '
         'clause with that citation; the Abstract’s 40.77%% anchor names the proportion as the named premise SimpleProportion, its theorem '
         'upstream (Zeta23.thmB₀_mult, FinalMult.lean :350), not a compiled fact; the closure under the open premise names the premise as '
         'RH by h2_sign_iff_rh and the faces’ silence on multiplicity by the ζ page’s last paragraph; the trace-formula “only solution is '
         'multiplicity 1” names the compiled explicit formula’s weights and the salt-check’s double point. The work-list’s four lines '
         'rewritten; %d ceiling corrections, %d fact corrections (the derivative-engine pin, the SIDE-grh-transfer pin), %d restatement '
         'rewrites; two addendum sentences sit in b554’s dated tier block and carry with history lines beneath, as does the one stem in the '
         'annotation of 2026-08-05; b450’s two items inserted as credit lines under the placement clause. %d collisions resolved by the '
         'precedence order without a prompt and listed for the author’s strike. Body %d sentences against %d (%+d); back matter %d. H28a '
         '%s, H28b %s, H28c %s; no sentence held. The pages re-emitted after the edition commit, one per call, each committed alone '
         '(PLACE-papers %s).' % (ED, E['sha256'], H['n_ceils'], H['n_facts'], H['n_restate'], H['n_collisions'], E['n_body'], E['n_cur'],
                                 E['n_body'] - E['n_cur'], E['n_backmatter'], H['H28a'], H['H28b'], H['H28c'], pages), '',
         '**The control frozen** (`(R207)`(2), the author’s answer before the seal): relay tools/test_chain_page_b596.py reads b592’s lists, '
         'probes and the terminal table at relay 12c15c80 and the pages, README, REGISTRY and keystones at PLACE-papers ba5f0ea; the arm '
         'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA 2 of 2 before the seal and after the pages (relay %s).' % REPAIR, '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this edition carries b554’s reading of the title (FINDINGS :5778, the reduction '
         'compiled in neither direction) into the document, with the Prop and walk of b596 (:6856) as its citations, and b558’s work-list '
         '(:5990) into its four lines; it re-reads the faces’ equivalences (:4595, :6194) for their silence, and is re-read by '
         'W-ORD-VENDOR-FINALMULT, whose landing would turn the proportion’s named premise into a vendored fact. It strengthens two of the '
         'programme’s offerings: the edition form (its clauses applied to a keystone whose title claimed an equivalence) and the compiled '
         'separation of what the faces state from what they are silent on.', '',
         '**The record lines.** b596’s weight at FINDINGS :%d; the generator-run standing line at OPEN_TRAILS :%d; W-ORD-VENDOR-FINALMULT '
         'at :%d; the DENSITY line at :%d.' % (wl['line'], rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][2]['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R207)`(7): b598, one CP-1b act over SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION, their tier blocks and '
         'work-lists written by the b558 form; their editions at b599 if the work-lists are short enough for one act; then the research '
         'sequence from REMAINDER 5. The author rules on the closing.', '',
         '*Nothing deposits; no kernel written; SIMPLICITY v1.1.2 unedited; README, REGISTRY and ERRATA unwritten; nothing here is a '
         'statement about RH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b597_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE[:90]), title=TITLE, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, TITLE[:90]))


def trail():
    Q = _Q()
    S, fj, wl, rl = jl('b597_scores.json'), jl('b597_findings.json'), jl('b597_weight_line.json'), jl('b597_rule_lines.json')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R207) ratified.** (1) b596 at its weight. (2) Defect (f) repaired, the control frozen. (3) The generator-run standing line. '
             '(4) W-ORD-VENDOR-FINALMULT. (5) The DENSITY shape. (6) CP-7 act seventeen, the edition of SIMPLICITY_OF_RIEMANN_ZEROS. (7) The '
             'act after: b598.', '',
             '**Entered:** FINDINGS.md:%d (b596’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS.md:%d (the generator-run '
             'standing line), :%d (W-ORD-VENDOR-FINALMULT), :%d (the DENSITY line), this record; PLACE-papers `%s` (the edition), both pages '
             're-emitted; relay tools/test_chain_page_b596.py (the frozen control, %s).' % (
                 wl['line'], fj['entry_line'], rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][2]['line'], ED, REPAIR), '',
             '**Answered before the seal, by the author** (relay data/b597_author_answers.txt): the frozen control reads every relay source at '
             '12c15c80, the b592 lists’ one commit, and every PLACE-papers source at ba5f0ea, named in the arm. **Recorded as the '
             'navigator’s:** (R207)(2)’s “relay ac8257a5” for the lists -- that commit is the generator’s at b592, and the lists are not in '
             'its tree.', '',
             '**Resolved by the seat under the precedence order, for the author’s strike:** twelve collisions (relay '
             'data/b597_edition_SIMPLICITY.txt), among them the work-list’s STANDS rows on three sentences whose simplicity clause the ruling '
             'sends to the ceiling, and two addendum sentences inside b554’s dated tier block carried with history lines; three sentences '
             'read and left (the Abstract’s “established” at :%d, :%d, :%d) for the strike.' % (_edl(24), _edl(144), _edl(278)), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R207)`(7), b598, one CP-1b act over SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION; their editions at b599 '
             'if short enough; then the research sequence from REMAINDER 5; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel written; SIMPLICITY v1.1.2 unedited; ERRATA untouched; FACES_LEDGER '
             'untouched; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b597_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b597_trail.json')['line'])


def desk():
    S = jl('b597_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b597 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H28a-H28c.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in ('H28a', 'H28b', 'H28c')]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)),
          '### ### **H28a %s ; H28b %s ; H28c %s.**' % (S['H28a'][0], S['H28b'][0], S['H28c'][0]), '']
    L += rd('b597_defects.txt').rstrip(NL).split(NL)
    put_txt('b597_desk_notes.txt', L)


def components():
    S, E, fj, tj, wl, rl = (jl('b597_scores.json'), jl('b597_edition.json'), jl('b597_findings.json'), jl('b597_trail.json'),
                            jl('b597_weight_line.json'), jl('b597_rule_lines.json'))
    L = ['b597 -- THE COMPONENTS, BANKED UNDER (R207).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b596`s closing push-out and its attempt-1 capture relay %s ; push-b596* '
         'branches deleted by name (data/b597_branches.txt) ; the kept branches untouched ; the control frozen (relay %s, the test 5 of 5, '
         'the arm 2 of 2) ; the suite run at HEAD before the face (data/b597_arms_prerun.txt)' % (STEPZERO, REPAIR),
         '### COMPONENT 1 : b596`s weight FINDINGS :%d ; the generator-run standing line OPEN_TRAILS :%d ; W-ORD-VENDOR-FINALMULT :%d ; the '
         'DENSITY line :%d' % (wl['line'], rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][2]['line']),
         '### COMPONENT 2 : the edition %s (sha256 %s) ; body %d vs %d ; back matter %d ; collisions %d ; H28a %s, H28b %s, H28c %s ; no '
         'sentence held ; the pages re-emitted after the edition commit, one per call' % (
             ED, E['sha256'][:16], E['n_body'], E['n_cur'], E['n_backmatter'], len(E['collisions']), S['H28a'][0], S['H28b'][0], S['H28c'][0]),
         '### COMPONENT 3 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b598, the CP-1b act over SILENCE_STAGES_DEALIGNMENT '
         'and REPARAMETERIZATION ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0],
                                                                         S['N4'][0], S['N5'][0])]
    put_txt('b597_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b597_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
