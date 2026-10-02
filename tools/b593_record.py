# -*- coding: utf-8 -*-
"""b593_record.py -- THE ACT'S RECORD TOOL, UNDER (R203). ### ONE SUBCOMMAND PER BANK.

### ### b593: LANE THREE, ACT TWENTY -- CP-7 ACT FIFTEEN: THE EDITION OF BALANCE_AND_POSITIVITY BY THE FORM; THE ACT ROOT AND
### THE SECOND READER ENTERED AS PRICED WORK-ORDERS.
### Subcommands write only `data/b593_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode, temp file, `os.replace`). No platform call. The template is b592_record.py.
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
PRE_PP = '111f27c'
PRE_RELAY = 'f93e1a58'
STEPZERO = 'cbcc37ec'
V016 = 'c404e727d7f7121b180318cca32eeb115452ed1b'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f7dd7aec-e7f8-492c-a0db-31ef189124e6/scratchpad'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CUR = 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'
ED = 'phase1.5/spectral/BALANCE_AND_POSITIVITY_v0_9_5.md'
WL = 'data/b558_editions/BALANCE_AND_POSITIVITY.txt'
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
    '(a) A DELETE ON A RELATIVE PATH: before the seal the seat removed its own scratch copy of this tool (relay tools/b593_record.py, '
    'made minutes earlier by a rename of b592`s and never committed) with `rm -f tools/b593_record.py` from relay`s directory -- a '
    'relative path, not the verified absolute path the standing delete rule names. The file was the act`s own and untracked; nothing '
    'else was touched (the following `ls` printed it absent). The tool was then written whole.',
    '(b) THE EDITION`S FIRST SCAN READ NOT CLEAN ON THE SEAT`S OWN BACK MATTER: the Rewrites row for :553 quoted the old wording with '
    'its banned stem and no correction-record marker within the scanner`s window; the row was given the "stem correction record:" '
    'prefix through the Edit tool and the uncommitted file re-written before the bank and the commit.',
    '(c) THE SEAT`S QUESTION ON THE JOINT`S LI FORM LISTED FOUR BODY USES AND MISSED THE FIFTH, v0.9.4 :21 (the Role line), which '
    'b545`s own block names; found on reading the written edition before its commit, put to the author, and cited as the author '
    'answered (answer 5).',
    '(d) THREE EDITS TO THIS UNSEALED TOOL WENT THROUGH A PYTHON HEREDOC, NOT THE EDIT TOOL THE FERRY NAMES (the :72 key helper`s two '
    'call sites, the :21 reason, the expectation row); no backslash or quote was in the replaced text, the tool compiled, and the '
    'replacements were printed and checked by grep; later edits went through the Edit tool.',
    '(e) THE SUITE`S FIRST PRE-PUSH RUN FAILED G-RULED-REWRITES LIVE ON ITS OWN PREDICATE, NOT ON THE EDITION: the arm looked for the '
    'iff`s pin written "`register4_positivity_liCoeff_iff_rh` (v0.11 = ..." where the edition writes it "(`register4_positivity_liCoeff_iff_rh`, '
    'v0.11 = ..." (every rewrite printed present at its line); the predicate was corrected through the Edit tool and the suite re-run whole.',
]


def defects():
    put_txt('b593_defects.txt', ['### b593 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay the BALANCE_AND_POSITIVITY work-list, whole', RELAY, 'HEAD', WL, list(range(1, 69))),
    ('relay the CP-1b rows of BALANCE_AND_POSITIVITY (14 MOVED, 22 STANDS, 1 CREDIT)', RELAY, 'HEAD', 'data/b558_cp1b.txt', [45] + list(range(600, 640))),
    ('PLACE-papers BALANCE_AND_POSITIVITY: head, version line, §II and the era annotation, the registers, B.3, B.6, C.3, C.6, App. D, '
     'the version history, the tier block, b545`s joint-forms block, b546`s line, b561`s line', PP, PRE_PP, CUR,
     [1, 13, 16, 18, 21, 23, 25, 53, 55, 57, 59, 61, 63, 65, 72, 146, 258, 274, 299, 350, 354, 355, 356, 357, 360, 430, 467, 469, 538, 544,
      553, 563, 565, 569, 624, 626, 638, 668, 675, 681, 682, 692, 764, 768, 770, 772, 776, 780, 782]),
    ('PLACE-papers the ζ page at v0.16 (b592), the nodes and rows the edition cites', PP, PRE_PP, PAGE, [3, 11, 12, 20, 24, 25, 28, 150, 151]),
    ('PLACE-papers PATHS v0.7, the goal state and the pentagon-to-star reading (b578)', PP, PRE_PP, 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md', [65, 69]),
    ('PLACE-papers OPEN_TRAILS, the form and its clauses through :12194', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11864, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 12044, 12188, 12190, 12192, 12194, 12196]),
    ('PLACE-papers FINDINGS, the credit at :274 and b592`s entry', PP, PRE_PP, 'FINDINGS.md', [5461, 5527, 6780]),
    ('relay the b538 census, R3', RELAY, 'HEAD', 'data/b538_census.json', [20, 21, 22, 23, 24]),
    ('SIDE-explicit-formula v0.16 the RegisterDepth statements', EFK, V016, 'SIDEExplicitFormula/RegisterDepth.lean', [60, 101]),
    ('relay b592`s closing push-out, its head', RELAY, 'HEAD', 'data/b592_closing_push_out.txt', list(range(1, 6))),
]


def reads():
    L = ['b593 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev + '^{}').strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:400]))
    hits = [h for h in g(PP, 'show', '%s:OPEN_TRAILS.md' % PRE_PP).split(NL)[6641].split('<br>') if 'BALANCE' in h]
    L += ['', '### b450`s items for BALANCE_AND_POSITIVITY in its table (OPEN_TRAILS :6642): %d -- %s' % (len(hits), hits or 'none')]
    put_txt('b593_reads.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B592_ENTRY = ('## CP-7, act fourteen: the edition of THE_RESIDUE_OF_RH from its tier block and work-list')
B592_TRAIL = '### b592 — lane three, act nineteen under (R202)'


def weight_line():
    """### PLACE-papers FINDINGS: b592's weight, one appended line addressed to b592's entry."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B592_ENTRY)
    if entry != 6780:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    head = '*Appended 2026-10-02 by b593 to b592’s entry (:%d), under `(R203)`(1) -- b592 AT ITS WEIGHT:*' % entry
    Q.guard_absent(Q.FIND, head)
    text = ('\n%s THE_RESIDUE_OF_RH v1.2 beside v1.1 unedited: the MOVED row naming h2_sign (h2_sign_iff_rh at v0.2); §7 :77 rewritten by '
            'the FINDINGS :6218 reading and the same reading carried to :79 (two sentences) and :88, each citing h2_sign_iff_rh, '
            'li_nonneg_iff_rh, register4_positivity_liCoeff_iff_rh and arith_limit_nonneg_iff_rh at their pins, :79’s third sentence '
            'carried as the realization form; the sign-face registers item located (OPEN_TRAILS :6764, the archive :3476) and credited '
            'beneath :77; three stem uses carried by history with lines beneath; body 260 against 256 (+4), back matter 65; H28a-H28c '
            'held, the scanner clean, the re-pin 50 of 50. Both pages at v0.16 = c404e72, twice byte-identical, re-emitted after the '
            'edition commit, both page arms 2 of 2; the generator (relay ac8257a5, 8 of 8) printing premises on the rows graded by a '
            'premise and matching a plain lower-case node name by qualification or backticks. The three form clauses at OPEN_TRAILS '
            ':12190-:12194. The suite read 76 of 76. (N2) refuted on the history and version lines, the navigator’s count.\n' % head)
    r = Q.append_to(Q.FIND, text)
    put_json('b593_weight_line.json', dict(entry=entry, line=Q.line_of(Q.FIND, head), head=head, append=r))
    print('  weight line :%s' % Q.line_of(Q.FIND, head))


def workorders():
    """### PLACE-papers OPEN_TRAILS: W-ORD-ACT-ROOT and W-ORD-SECOND-READER, two appended lines addressed to b592's record."""
    Q = _Q()
    at = Q.line_of(Q.OT, B592_TRAIL)
    if at != 12196:
        sys.exit('### THE ADDRESSED LINE MOVED: %s -- NOTHING WRITTEN' % at)
    heads = [('*Appended 2026-10-02 by b593 beside b592’s record (:%d), under the author’s ruling `(R203)`(2) -- W-ORD-ACT-ROOT, '
              'PRICED, NOT STARTED, trigger the author’s word:*' % at),
             ('*Appended 2026-10-02 by b593 beside b592’s record (:%d), under the author’s ruling `(R203)`(3) -- W-ORD-SECOND-READER, '
              'PRICED, NOT STARTED, trigger the author’s word, its form fixed now:*' % at)]
    for x in heads:
        Q.guard_absent(Q.OT, x)
    texts = ['\n%s the closing push-out bank’s as-of lines hashed into one act root (sha256 over the sorted repository heads, the kernel '
             'tags and the bank digests), the root written into the trail record and chained to the previous act’s root; the suite’s '
             'as-of arm reads the root and verifies the chain; the mirror MANIFEST carries the latest root. Price: one instrument edit '
             'with a test, one line per act from then on. The deposit description’s carrying of the root is a separate (R110)-route item '
             'for the author’s word.\n' % heads[0],
             '\n%s for a batch of editions, a reader with no context of the acts -- a fresh seat session from the ledgers alone, or a '
             'second model -- is handed each edition’s diff bank (both wordings, no reasons) and the ceiling sentence, and scores each '
             'substitution as SAME-OBJECT, DIFFERENT-OBJECT or BEYOND-CEILING with one line of reason; disagreements with the seat’s own '
             'back matter are printed and ruled by the author; the agreement rate per edition is banked. Price: one act per batch of five '
             'editions. The reason is the ruling’s: the substitutions are the one place the form’s judgment is a seat’s judgment with no '
             'printed check.\n' % heads[1]]
    out = []
    for x, t in zip(heads, texts):
        r = Q.append_to(Q.OT, t)
        out.append(dict(head=x, line=Q.line_of(Q.OT, x), append=r))
    put_json('b593_workorders.json', dict(addressed=at, lines=out))
    print('  work-order lines :%s' % [o['line'] for o in out])


# ================================================================================ COMPONENT 2: THE EDITION
EF = 'SIDE-explicit-formula'
PIN = {'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'li_nonneg_iff_rh': 'v0.9 = `e5a5a83`', 'arith_limit_nonneg_iff_rh': 'v0.9 = `e5a5a83`',
       'li_identity_sym': 'v0.7 = `1e4a007`', 'register4_positivity_liCoeff_iff_rh': 'v0.11 = `19b7d1e`', 'ch_iff_rh': 'v0.1 = `baed4df`',
       'not_register1': 'v0.16 = `c404e72`', 'mellin_Phi_eq_zero_of_re_le_one': 'v0.16 = `c404e72`'}
FQ = {'h2_sign_iff_rh': 'SIDEExplicitFormula.B321.h2_sign_iff_rh', 'li_nonneg_iff_rh': 'SIDEExplicitFormula.LiCriterionBridge.li_nonneg_iff_rh',
      'arith_limit_nonneg_iff_rh': 'SIDEExplicitFormula.LiCriterionBridge.arith_limit_nonneg_iff_rh',
      'li_identity_sym': 'SIDEExplicitFormula.LiWeil.li_identity_sym',
      'register4_positivity_liCoeff_iff_rh': 'SIDEExplicitFormula.PageConverses.register4_positivity_liCoeff_iff_rh',
      'ch_iff_rh': 'SIDEExplicitFormula.B321.ch_iff_rh', 'not_register1': 'SIDEExplicitFormula.RegisterDepth.not_register1',
      'mellin_Phi_eq_zero_of_re_le_one': 'SIDEExplicitFormula.RegisterDepth.mellin_Phi_eq_zero_of_re_le_one'}
WHERE = {'h2_sign_iff_rh': 'the ζ page, node 8, line 12', 'li_nonneg_iff_rh': 'the ζ page, node 20, line 24',
         'arith_limit_nonneg_iff_rh': 'the ζ page, node 21, line 25', 'li_identity_sym': 'the ζ page, node 16, line 20',
         'register4_positivity_liCoeff_iff_rh': 'the ζ page, node 24, line 28', 'ch_iff_rh': 'the ζ page, node 7, line 11',
         'not_register1': 'the ζ page, Correspondence row, line 151 (the page’s pin)',
         'mellin_Phi_eq_zero_of_re_le_one': 'the ζ page, Correspondence row, line 150 (the page’s pin)'}
PG = 'SIDE-explicit-formula at the page’s pin v0.16 = `c404e72`'
MELLIN = ('lv’s h2 at Φ, `mellin Phi (s/2) ≠ 0`, is false at every s with re s ≤ 1 (`mellin_Phi_eq_zero_of_re_le_one`, %s)' % PG)
OPEN_CL = 'the open clause being `h2_sign`, equivalent to RH (`h2_sign_iff_rh`, SIDE-explicit-formula v0.2 = `5c72cad`)'
CITE_IN = ('the channel split is this document’s, §B.6(2), and the kernel states the sign of their sum: `li_nonneg_iff_rh`, '
           'SIDE-explicit-formula v0.9 = `e5a5a83`, and `arith_limit_nonneg_iff_rh`, v0.9 = `e5a5a83`, through `li_identity_sym`, '
           'v0.7 = `1e4a007`')
CITE = ' (' + CITE_IN + ')'
DEPTHS_146 = ('Route 3\'s `ConservationHypothesis`, RH restated (`ch_iff_rh`, SIDE-explicit-formula v0.1 = `baed4df`); the one premise of '
              'the reduction analysis, in its Weil form `h2_sign` equivalent to RH (`h2_sign_iff_rh`, v0.2 = `5c72cad`); the '
              'balance→positivity distance, RH in the Li form (`li_nonneg_iff_rh`, v0.9 = `e5a5a83`)')
OLD2 = 'Route 3\'s `ConservationHypothesis`; the one premise of the reduction analysis; the balance→positivity distance'
WORKLIST = [
    (72, 'are four registers of a single open joint — and with the C₅ input/output distance of §D.2, five.',
     'are four registers which the b538 census sets at different depths and not as one joint — the universality hypothesis false as '
     'stated (`not_register1`, %s), `ConservationHypothesis` RH restated (`ch_iff_rh`, v0.1 = `baed4df`), the one premise in its Weil '
     'form `h2_sign` equivalent to RH (`h2_sign_iff_rh`, v0.2 = `5c72cad`), the balance→positivity distance RH in the Li form '
     '(`li_nonneg_iff_rh`, v0.9 = `e5a5a83`) — and with the C₅ input/output distance of §D.2, five.' % PG),
    (146, 'The premise, in the four registers established in §IV: the universality hypothesis of `silence_universal`;',
     'The premise, in the four registers established in §IV, which the b538 census sets at different depths and not as one premise: '
     'the universality hypothesis of `silence_universal`, false as stated (`not_register1`, %s);' % PG),
    (146, OLD2 + '.', DEPTHS_146 + '.'),
    (553, '**The gap between them is the premise\'s fifth register.** §IV of this paper lists four registers of one open joint (the '
          'universality hypothesis of `silence_universal`;',
     '**The distance between them is the premise\'s fifth register.** §IV of this paper lists four registers, which the b538 census '
     'sets at different depths and not as one joint (the universality hypothesis of `silence_universal`, false as stated, '
     '`not_register1`, %s;' % PG),
    (553, OLD2 + ').', DEPTHS_146 + ').'),
    (258, '**Discharge the premise = supply h1 and h2 for the seven classes at T1\'s Φ.**',
     '**Discharge the premise = supply h1 and h2 for the seven classes at T1\'s Φ -- and %s, so this discharge closes nothing on the '
     'strip, %s.**' % (MELLIN, OPEN_CL)),
    (274, 'Then h2 is the analytic content: `mellin Phi (s/2) ≠ 0` for s off the critical line.',
     'Then h2 is the analytic content: `mellin Phi (s/2) ≠ 0` for s off the critical line, which is false at every s with re s ≤ 1 '
     '(`mellin_Phi_eq_zero_of_re_le_one`, %s), so h2 at Φ fails on the strip and %s.' % (PG, OPEN_CL.replace('being', 'is'))),
    (356, 'which are the premise, restated, not a proof of it.',
     'which are the premise, restated, not a proof of it, and %s, so `T3′` closes nothing on the strip.' % MELLIN),
    (467, '`partialPositivity_finiteRange` *proves* λ_n ≥ 0 for 1 ≤ n ≤ N₀(T) ≈ 2T², but',
     '`partialPositivity_finiteRange` *proves* λ_n ≥ 0 for 1 ≤ n ≤ N₀(T) ≈ 2T² under two uncompiled literature premises '
     '(Bombieri–Lagarias `ExplicitFormulaDecomp`, Voros `TailBoundPremise`) and verified zeros, T1-lit (the tier block, :682), while '
     'λ_n ≥ 0 at every n is RH itself (`li_nonneg_iff_rh`, SIDE-explicit-formula v0.9 = `e5a5a83`), but'),
    (469, '(h1: the seven couplings at Φ; h2: the Mellin nonvanishing)',
     '(h1: the seven couplings at Φ; h2: the Mellin nonvanishing, false at every s with re s ≤ 1 (`mellin_Phi_eq_zero_of_re_le_one`, '
     '%s), %s)' % (PG, OPEN_CL)),
]
RULED = [
    (72, 'its `R4_positivity_to_RH` edge is exactly the Li-criterion equivalence below (INTERFACES, Li\'s criterion as named premise).',
     'its `R4_positivity_to_RH` edge is exactly the Li-criterion equivalence below (INTERFACES in lv, Li\'s criterion as named premise), '
     'the premise discharged in SIDE-explicit-formula, where Li\'s criterion is compiled as an equivalence over Mathlib\'s zeros '
     '(`li_nonneg_iff_rh`, v0.9 = `e5a5a83`) and in the register\'s own vocabulary at λ := `LiCoeff` '
     '(`register4_positivity_liCoeff_iff_rh`, v0.11 = `19b7d1e`).'),
    (72, '(notation of §III).', '(notation of §III; ' + CITE_IN + ').'),
    (146, '**RH ⟺ λ_Z(n) ≥ −λ_A(n) for every n.**', '**RH ⟺ λ_Z(n) ≥ −λ_A(n) for every n**' + CITE + '.'),
    (360, 'RH ⟺ λ_Z(n) ≥ −λ_A(n) for every n.*', 'RH ⟺ λ_Z(n) ≥ −λ_A(n) for every n' + CITE + '.*'),
    (430, 'RH ⟺ λ_Z(n) ≥ −λ_A(n) ∀n is an exact restatement', 'RH ⟺ λ_Z(n) ≥ −λ_A(n) ∀n' + CITE + ' is an exact restatement'),
    (21, 'RH ⟺ λ_Z(n) ≥ −λ_A(n) for every n (§II, §III).', 'RH ⟺ λ_Z(n) ≥ −λ_A(n) for every n (§II, §III; ' + CITE_IN + ').'),
]


def _rkey(ln, old):
    return ('72a' if 'R4_positivity_to_RH' in old else '72b') if ln == 72 else ln
RULED_WHY = {'72a': '(R203)(4): the R4 face`s edge MOVED-IN-MEANING to li_nonneg_iff_rh at v0.9, the premise discharged in SIDE-explicit-formula, lv`s edge keeping its grade in lv',
             '72b': 'the author`s answer 2: the joint`s Li form cited at its four body uses', 146: 'the author`s answer 2', 360: 'the author`s answer 2',
             430: 'the author`s answer 2', 21: 'the author`s answer 5 before the seal: the fifth body use, the seat`s first question having listed four'}
CEILS = [(21, 'the **sign core** of the proof', 'the **sign core** of the reduction')]
STEMS = [(354, 'the all-n tail is the open gap', 'the all-n tail is the open clause'),
         (563, 'The gap between the function-field and number-field cases', 'The distance between the function-field and number-field cases'),
         (565, 'naming the C₅ input/output gap as', 'naming the C₅ input/output distance as'),
         (569, 'it is the C₅-output gap seen from the geometry side', 'it is the C₅-output distance seen from the geometry side')]
HIST = [(23, 23, '*History line, 2026-10-02 (v0.9.5, b593): the dated currency note above carries its 2026-07-24 wording as the record; '
                 'the side it names is the side of the open clause, and the all-n tail it names is the open clause.*'),
        (65, None, '*History line, 2026-10-02 (v0.9.5, b593): the repaired balance sentence of the annotation above is compiled for the '
                   'Bombieri–Lagarias family `symMember n δ`, δ → 0⁺ -- the explicit formula’s arithmetic side on it tends to the Li '
                   'coefficient (`li_identity_sym`, SIDE-explicit-formula v0.7 = `1e4a007`), and the non-negativity of every such limit is '
                   'equivalent to Mathlib’s `RiemannHypothesis` (`arith_limit_nonneg_iff_rh`, v0.9 = `e5a5a83`), while the sentence’s '
                   '“every admissible g” remains the Weil face, `h2_sign` equivalent to RH (`h2_sign_iff_rh`, v0.2 = `5c72cad`); the '
                   'original sentence above the annotation carries unchanged under the annotation’s own clause.*'),
        (638, 638, '*History line, 2026-10-02 (v0.9.5, b593): the dated v0.7 entry above carries its 2026-07-13 wording as the record; the '
                   'object its sentence names is the distance between C₅-input and C₅-output, the premise’s fifth register.*'),
        (782, None, '*History line, 2026-10-02 (v0.9.5, b593): the dated entries above that call the Li form’s equivalence to RH not '
                    'compiled (v0.9.4 :770, b545), the bridge classical and not compiled (v0.9.4 :772, b545) and the Li form’s converse '
                    'T1-lit (v0.9.4 :782, b561) are superseded -- Li’s criterion is compiled as an equivalence over Mathlib’s zeros '
                    '(`li_nonneg_iff_rh`, SIDE-explicit-formula v0.9 = `e5a5a83`), the Li coefficient as the limit of the explicit '
                    'formula’s arithmetic side on the Bombieri–Lagarias family (`li_identity_sym`, v0.7 = `1e4a007`) with every such '
                    'limit’s non-negativity equivalent to RH (`arith_limit_nonneg_iff_rh`, v0.9 = `e5a5a83`), and the Weil form '
                    'equivalent to RH (`h2_sign_iff_rh`, v0.2 = `5c72cad`), so the sentence that the Li coefficients are Weil positivity '
                    'written in a basis stands with the three faces cited.*')]
HIST_WHY = {23: 'the author`s answer 4: the 2026-07-24 currency note a dated entry; its stem and its "RH-core side" carried',
            65: 'the author`s answer 1: the balance sentence`s compiled form beneath the 2026-08-28 annotation',
            638: 'the author`s answer 4: the v0.7 history entry; its stem carried',
            782: 'the author`s answer 3: the dated Li entries of b545 and b561 superseded by the compiled faces'}
VERSION = (16, '**v0.9.5 — 2026-10-02** — *CP-7 edition (b593), written beside v0.9.4, which is unedited; its back matter closes the file.*')
CEILING = re.compile(r'\bprov(?:e|ed|en|es)\b|\bproof\b|RH-core|RH proved|proves RH|end-to-end|RH-route|the whole of RH')
CARRIED = {
    23: 'a dated entry (the 2026-07-24 currency note), carried under the history clause with its history line beneath (the author`s answer 4)',
    25: '"the proven partial paths (A1–A10)" names PATHS ANNEX B`s partial results, not RH',
    68: '"the on-line contribution is proved harmless": the on-line term`s non-negativity, compiled (`blTerm_nonneg_of_onLine`)',
    125: 'the Fano theorem of §V, a finite combinatorial fact',
    131: '"the same proof-shape close over 𝔽_q": Weil`s proof over function fields',
    135: 'the disclosure`s "proof strategies"',
    190: 'a negation: "It proves no positivity, no bound, and nothing about RH"',
    253: '`T3″` proves a commutation false, a compiled negative',
    354: 'B.6(1) names the certificate`s inputs (verified zeros, the Bombieri–Lagarias decomposition, the Voros tail bound) beside "proves", '
         'and its K3 note grades them as premises; carried as read',
    369: 'couplings proved at the fixed witness Φ, compiled lemmas',
    440: 'a negation: "is not proved"',
    441: 'a negation: "Nothing here proves positivity of λ_n for all n"',
    454: 'Voros`s unconditional asymptotic, a literature result',
    455: 'the unconditional proof of S̄_n`s asymptotic, a literature result',
    482: 'the archimedean half`s unconditional asymptotic, a literature result',
    487: 'Oesterlé`s constant proved unconditionally, a literature result',
    538: 'Weil`s 1948 proof over 𝔽_q, field context (R203)(4)',
    540: 'Weil`s 1948 proof over 𝔽_q, field context',
    557: 'C₅-input proved at Φ, a compiled lemma',
    559: 'a negation: "a localization, not a proof"',
    563: 'Weil`s 1948 proof over 𝔽_q, field context',
    570: 'the standing proof that C₃ alone does not confine (Davenport–Heilbronn), a literature result',
    613: 'a constant proved in-kernel, a compiled lemma',
    618: 'C₇-order proved in-kernel, a compiled lemma',
    626: 'a dated history entry (v0.9.4), carried as the record',
    640: 'a dated history entry (v0.6): Voros`s unconditional asymptotic',
    662: 'b324`s owed bridging statement, "or a proof that no such formula exists", not RH',
    725: 'b545`s dated tier block: `lam_add` proves additivity, a compiled lemma',
    732: 'b545`s dated tier block quoting :258 as it stood',
    741: 'b545`s dated tier block quoting :356 as it stood',
    776: 'b546`s dated line: C₂ at Φ proved, a compiled lemma',
}
BM_TAG = '<!-- b593 (R203) THE v0.9.5 EDITION`S BACK MATTER, 2026-10-02 -->'
OFFSET = ('+1 from :16 (the v0.9.5 line, above the v0.9.4 line); +2 more from :24, :66, :639 and :783 (a blank and a history line beneath '
          ':23, :65, :638 and :782) -- v0.9.4 :n sits at the edition`s :n for n < 16, :n+1 for 16 <= n <= 23, :n+3 for 24 <= n <= 65, :n+5 '
          'for 66 <= n <= 638, :n+7 for 639 <= n <= 782')


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    return n + (1 if n >= VERSION[0] else 0) + sum(2 for a, _s, _t in HIST if n > a)


def _all_changes():
    return WORKLIST + RULED + CEILS + STEMS


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def edition(*a):
    """### PLACE-papers phase1.5/spectral/BALANCE_AND_POSITIVITY_v0_9_5.md, beside the current version from its blob at 111f27c; the re-pin
    ### step last. Writes the edition file and data/b593_edition.json."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE 111f27c -- NOTHING WRITTEN')
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
    if not cur[VERSION[0] - 1].startswith('**v0.9.4 — 2026-07-19**'):
        sys.exit('### THE VERSION ANCHOR IS NOT WHERE THE FACE SAYS')
    anchors = {23: '*Kernel currency (2026-07-24 deposit)', 65: '*Provenance: `SIGN_ARRANGEMENT_RECONCILIATION.md` §3', 638: '*v0.7 (2026-07-13, fifth sitting)',
               782: '*Appended 2026-09-29 by b561 beneath the block at :764'}
    for n, s in anchors.items():
        if not cur[n - 1].startswith(s):
            sys.exit('### THE HISTORY ANCHOR :%d IS NOT WHERE THE FACE SAYS' % n)
    import banned_terms as BT
    for t in [VERSION[1]] + [h[2] for h in HIST] + [x[2] for x in _all_changes()]:
        if len(_segs(t)) != 1 and t in (VERSION[1],) + tuple(h[2] for h in HIST):
            sys.exit('### AN INSERTED LINE IS NOT ONE SENTENCE (%d): %s' % (len(_segs(t)), t[:60]))
        if BT.PAT.search(t):
            sys.exit('### A BANNED STEM IN AN INSERTED OR REWRITTEN TEXT: %s' % t[:80])
    rows = [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'BALPOS' and r['verdict'] == 'MOVED-IN-MEANING']
    diff = []
    for r in rows:
        ln = r['line']
        sg = _segs(cur[ln - 1])
        if r['sentence'] not in sg:
            sys.exit('### THE ROW %s`S SENTENCE IS NOT A SEGMENT OF v0.9.4 :%d' % (r['id'], ln))
        k = sg.index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d].split(' = ')[1] in nw]
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         cites=cites, supports=r['reading'], kind='work-list'))
    for i, (ln, old, rep) in enumerate(RULED):
        key = _rkey(ln, old)
        diff.append(dict(id='ruled:%s' % key, line=ln, ed_line=_edl(ln), terminal='(R203)(4) reading', old=old, new=rep, changed=True,
                         cites=[d for d in PIN if ('`%s`' % d) in rep], supports=RULED_WHY[key], kind='ruled'))
    for after, _s, t in sorted(HIST, reverse=True):
        new[after:after] = ['', t]
    new[VERSION[0] - 1:VERSION[0] - 1] = [VERSION[1]]
    body = list(new)
    changed = set(x[0] for x in _all_changes())
    if any(_edl(n) > len(body) or (n not in changed and body[_edl(n) - 1] != cur[n - 1]) for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL DOES NOT CARRY THE CURRENT VERSION')
    for after, _s, t in HIST:
        if body[_edl(after) + 1] != t or body[_edl(after)] != '':
            sys.exit('### A HISTORY LINE IS NOT BENEATH :%d' % after)
    if body[_edl(VERSION[0]) - 2] != VERSION[1]:
        sys.exit('### THE VERSION LINE IS NOT ABOVE :16')
    inv = {_edl(n): n for n in range(1, len(cur) + 1)}
    hits = [(i, m.group(0)) for i, l in enumerate(body, 1) for m in CEILING.finditer(l)]
    stray = sorted(set(inv.get(i, -i) for i, _ in hits) - set(CARRIED) - changed)
    stray = [s for s in stray if s > 0 or abs(s) not in [_edl(h[0]) + 2 for h in HIST]]
    if stray:
        sys.exit('### A CEILING HIT IN THE BODY IS NEITHER REWRITTEN NOR CARRIED BY THE SEAT`S READ: current lines %s' % stray)
    hl = {str(a): _edl(a) + 2 for a, _s, _t in HIST}
    bm = ['', BM_TAG, '',
          '## Back matter of the v0.9.5 edition -- written 2026-10-02 by b593 under the author’s ruling `(R203)`(4), by the form of `(R187)`(5)', '',
          '*This file is v0.9.5 of BALANCE_AND_POSITIVITY, the CP-7 edition written beside v0.9.4 (`%s`, unedited) from v0.9.4’s tier block '
          '(its :668, standing) and its CP-1b work-list (relay `%s`, 14 rows on 8 lines), the ζ page as its spine; it does not deposit and '
          'does not replace v0.9.4, and its promotion is CP-8’s. Every line cited below is this file’s own.*' % (CUR, WL), '',
          '### Removals', '', 'None: every one of the 14 work-list rows resolves to a sentence rewritten in place to what its compiled fact says.', '',
          '### Rewrites', '', '| this edition’s line | v0.9.4 wording | v0.9.5 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in WORKLIST:
        stem = ln == 553 and old.startswith('**The ' + 'gap')
        bm.append('| :%d | %s%s | %s | rewritten: the work-list’s MOVED-IN-MEANING row%s |' % (
            _edl(ln), 'stem correction record: ' if stem else '', old, rep,
            ' (its banned stem replaced by the object the sentence names, the document’s own word)' if stem else ''))
    for i, (ln, old, rep) in enumerate(RULED):
        key = _rkey(ln, old)
        bm.append('| :%d | %s | %s | rewritten by `(R203)`(4)’s reading: %s |' % (_edl(ln), old, rep, RULED_WHY[key].replace('`', '’')))
    bm += ['', '### Credit lines', '', 'None inserted: the CP-1b CREDIT row at v0.9.4 :274 (B.6(4)’s credit, b546’s line at v0.9.4 :776) is the credit '
           'already entered at FINDINGS :5461 as corrected at :5527, not entered again; no b450 item names this document (relay `data/b593_reads.txt`).', '',
           '### History lines', '', '| this edition’s history line | the dated entry | the stem’s line | Status |', '|:--|:--|:--|:--|']
    for after, s, t in HIST:
        bm.append('| :%d | beneath v0.9.4 :%d | %s | inserted under the history clause (OPEN_TRAILS :11908, :12044, :12194): %s |' % (
            hl[str(after)], after, (':%d, carried-by-history' % _edl(s)) if s else 'no stem', HIST_WHY[after].replace('`', '’')))
    bm += ['', '### Ceiling corrections', '', '| this edition’s line | v0.9.4 wording | v0.9.5 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in CEILS:
        bm.append('| :%d | ceiling correction record: %s | %s | corrected under the ceiling clause, the object the sentence names |' % (_edl(ln), old, rep))
    bm += ['', '### Stem corrections', '', '| this edition’s line | v0.9.4 wording | v0.9.5 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in STEMS:
        bm.append('| :%d | stem correction record: %s (banned stem; correction record) | %s | corrected under the stem clause, the object the '
                  'sentence names (the document’s own word) |' % (_edl(ln), old, rep))
    bm += ['', '### Ceiling-shaped sentences read and carried', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(CARRIED):
        bm.append('| :%d | ceiling read, carried: %s | carried as read |' % (_edl(ln), CARRIED[ln].replace('`', '’')))
    bm += ['', '### Fact corrections', '', 'None: no pin, toolchain, count or import the body states is contradicted by the seat’s printed read '
           '(relay `data/b593_reads.txt`).', '',
           '### The navigator’s expectations of `(R203)`(4), and the author’s answers', '', '| expectation | the read | Status |', '|:--|:--|:--|',
           '| the balance sentence takes `arith_limit_nonneg_iff_rh` and `li_identity_sym` as its compiled form | the history line :%d beneath '
           'the 2026-08-28 annotation (the author’s answer 1); the original at :%d carries | cited |' % (hl['65'], _edl(55)),
           '| “RH ⟺ λ_Z(n) ≥ −λ_A(n) for every n” cited to the same | :%d (the author’s answer 5), :%d, :%d, :%d, :%d (the author’s answer 2) | cited |' % (_edl(21), _edl(72), _edl(146), _edl(360), _edl(430)),
           '| the R4 face’s edge MOVED to `li_nonneg_iff_rh` at v0.9, lv’s edge keeping its grade in lv | :%d | rewritten |' % _edl(72),
           '| “the Li coefficients are Weil positivity, written in a basis” stands with the three faces cited | the history line :%d (the author’s answer 3) | stands, cited |' % hl['782'],
           '| App. D’s Weil 1948 reading stands as field context | :%d, :%d | carried |' % (_edl(538), _edl(540)),
           '| the W_∞ ERA ANNOTATION carries as a dated record | :%d-:%d | carried |' % (_edl(57), _edl(65)),
           '| the register sentences take the b538 census as PATHS v0.7 took it (its :69) | :%d, :%d (two sentences), :%d (two sentences) | rewritten |' % (_edl(72), _edl(146), _edl(553)),
           '| “proved” phrasings take the ceiling clause | :%d corrected; :%d rewritten (the work-list row); the rest read and carried above | corrected and carried |' % (_edl(21), _edl(467)),
           '| the credit at B.6(4) :274 among the rows | the CP-1b CREDIT row, entered at FINDINGS :5461 / :5527, not entered again | recorded |', '',
           '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v0.9.5 | `%s` | written at b593 |' % ED,
           '| the current version, v0.9.4 | `%s` | unedited |' % CUR,
           '| the spine | `%s`, at SIDE-explicit-formula v0.16 = `c404e72` | read |' % PAGE,
           '| the work-list | relay `%s` | read |' % WL,
           '| the sentence-by-sentence diff | relay `data/b593_edition_BALPOS.txt` | banked at b593 |', '',
           '### Correspondence', '', '| declaration | repository | pin | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    ed_lines = {d: [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l and PIN[d].split(' = ')[1] in l] for d in PIN}
    for d in PIN:
        bm.append('| `%s` | %s | %s | %s | cited at :%s of this edition |' % (FQ[d], EF, PIN[d].replace('`', ''), WHERE[d],
                                                                              ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    pl = [i for i, l in enumerate(body, 1) if '`partialPositivity_finiteRange`' in l]
    bm.append('| `SIDELvConservation.PartialPositivity.partialPositivity_finiteRange` | SIDE-lv-conservation | v0.8.0 = 6efa9e5 | not on the page; '
              'this document’s tier block, :%d, T1-lit | named at :%s of this edition |' % (_edl(682), ', :'.join(str(x) for x in pl)))
    bm.append('')
    if any('### NONE' in l for l in bm):
        sys.exit('### A CORRESPONDENCE ROW CITES NO LINE OF THE EDITION')
    full = body + bm
    b = (NL.join(full) + NL).encode('utf-8')
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))
    if dry:
        print('  DRY: nothing written; diff rows %d, cites %s' % (len(diff), [(d['id'], len(d['cites'])) for d in diff if d['kind'] == 'work-list']))
        return
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    put_json('b593_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=0, removals=0, ruled_citations=len(HIST), ruled_rewrites=len(RULED), version_lines=1, diff=diff,
                                       offset=OFFSET, worklist=WORKLIST, ruled=RULED, ceils=CEILS, stems=STEMS, hist=[list(h) for h in HIST],
                                       hist_at=hl, carried={str(k): v for k, v in CARRIED.items()}, version=dict(above=VERSION[0], text=VERSION[1]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines))


def edition_bank():
    """### The diff with its offset line, the corrections, the counts, the ceiling read, the scanner's verdict, H28a-H28c."""
    E = jl('b593_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(BM_TAG)
    scan = rd('b593_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    hist_n = re.search(r'carried-by-history (\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    carried_ed = set(_edl(n) for n in CARRIED)
    rewritten_ed = set(_edl(x[0]) for x in _all_changes())
    hist_ed = set(_edl(a) + 2 for a, _s, _t in HIST)
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            kind = ('record' if (i > cut and l.startswith('| ')) else 'carried' if (i < cut and i in carried_ed)
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
         'b593 -- COMPONENT 2: THE EDITION OF BALANCE_AND_POSITIVITY, (R203)(4), BY THE FORM OF (R187)(5) AND ITS CLAUSES', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :16 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0], cur0[15][:90]),
         '### its tier block : :668 "%s"' % cur0[667][:110],
         '### its version history : the version line :16 (v0.9.4, 2026-07-19); the Version History section :624-:660; the dated '
         'annotations and blocks :57-:65, :668-:760, :764-:774, :776, :778, :780, :782',
         '### b450`s items naming this document: none (relay data/b593_reads.txt)',
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE WORK-LIST, ROW BY ROW (14 rows, 8 lines), AND THE RULED REWRITES (%d on 4 lines):' % len(RULED), '']
    for d in E['diff']:
        L += ['  %s v0.9.4 :%d -> v0.9.5 :%d `%s` -- %s ; cites %s' % (d['id'], d['line'], d['ed_line'], d['terminal'], d['kind'],
                                                                       ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']]),
              '      answers: %s' % d['supports'], '      v0.9.4 : %s' % d['old'], '      v0.9.5 : %s' % d['new'], '']
    L += ['### THE HISTORY LINES (the history clause, the author`s answers 1, 3 and 4):']
    for a, s, t in HIST:
        L += ['    v0.9.5 :%d, beneath v0.9.4 :%d%s' % (E['hist_at'][str(a)], a, (' (the stem`s line v0.9.4 :%d -> v0.9.5 :%d, carried-by-history)' % (s, _edl(s))) if s else ''),
              '      %s' % t]
    L += ['### THE CEILING CORRECTIONS (%d):' % len(CEILS)] + ['    v0.9.4 :%d -> v0.9.5 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in CEILS]
    L += ['### THE STEM CORRECTIONS (%d), in place:' % len(STEMS)] + ['    v0.9.4 :%d -> v0.9.5 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in STEMS]
    L += ['### THE CEILING-SHAPED SENTENCES READ AND CARRIED:'] + ['    v0.9.4 :%d -> v0.9.5 :%d  %s' % (n, _edl(n), CARRIED[n]) for n in sorted(CARRIED)]
    L += ['### THE FACT CORRECTIONS: none.', '### REMOVALS: none.', '### CREDIT LINES: none inserted (the :274 credit already entered, FINDINGS :5461 / :5527).',
          '### THE VERSION LINE: above v0.9.4 :%d: %s' % (E['version']['above'], E['version']['text']), '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d) ; the back '
          'matter %d ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d (the four history lines; the '
          'ruled rewrites keep their lines` counts) + one version line = %d' % (body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], {'record': 'quoted in a back-matter row, read by the seat',
                                                                 'carried': 'in a sentence the seat read and carried',
                                                                 'rewritten': 'in a sentence rewritten or corrected in place',
                                                                 'history': 'in a history line',
                                                                 'beyond': '### BEYOND THE CEILING'}[h['kind']], h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### THE SCANNER (banned_terms.py --new) on the edition: live uses %s, carried-by-history %s ; verdict %s' % (
              live_n, hist_n.group(1) if hist_n else None, 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on the page at its pin%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s verdict %s (live uses carried by history %s); sentences beyond the ceiling %d.**' % (
              h28c, 'CLEAN' if clean else 'NOT CLEAN', hist_n.group(1) if hist_n else None, len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b593_edition_BALPOS.txt', L)
    put_json('b593_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=live_n, history=int(hist_n.group(1)) if hist_n else None, clean=clean,
                                   beyond=len(beyond), hits=hits, held=None, n_ceils=len(CEILS), n_facts=0, n_stems=len(STEMS), n_ruled=len(RULED)))
    H = jl('b593_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'], 'live', H['live'], 'history', H['history'])


def repin():
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932). Writes data/b593_repin.txt."""
    E = jl('b593_edition.json')
    ed = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read().replace(chr(13), '').split(NL)
    cut = ed.index(BM_TAG)
    cur = _cur()
    checks = []
    for d in E['diff']:
        checks.append(('diff %s -> :%d carries the v0.9.5 wording' % (d['id'], d['ed_line']), d['new'] in ed[d['ed_line'] - 1]))
    for a, s, t in HIST:
        checks.append(('history line :%d beneath v0.9.4 :%d' % (E['hist_at'][str(a)], a), ed[E['hist_at'][str(a)] - 1] == t))
        if s:
            checks.append(('the stem`s line :%d is v0.9.4 :%d unchanged' % (_edl(s), s), ed[_edl(s) - 1] == cur[s - 1]))
    for ln, old, rep in CEILS + STEMS:
        checks.append(('correction :%d carries the new wording' % _edl(ln), rep in ed[_edl(ln) - 1]))
    for n in CARRIED:
        checks.append(('carried :%d holds a ceiling-shaped hit' % _edl(n), CEILING.search(ed[_edl(n) - 1]) is not None))
    for d, ls in E['cited_lines'].items():
        for x in ls:
            checks.append(('Correspondence: `%s` on :%d' % (d, x), ('`%s`' % d) in ed[x - 1] and x < cut))
    checks.append(('version line above the v0.9.4 line', ed[_edl(VERSION[0]) - 2] == VERSION[1]))
    bm = NL.join(ed[cut:])
    for n in sorted(set(int(x) for x in re.findall(r'\| :(\d+) \|', bm))):
        checks.append(('back-matter row :%d is a body line' % n, 0 < n < cut and ed[n - 1].strip() != ''))
    bank = rd('b593_edition_BALPOS.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM THE CURRENT VERSION') and bank.count('### OFFSET FROM') == 1))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and hashlib.sha256(
        open(os.path.join(PP, *ED.split('/')), 'rb').read()).hexdigest() == E['sha256']))
    L = ['### b593 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % ED, '']
    L += ['    %-90s %s' % (w[:90], 'OK' if ok else '### FAILS') for w, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _w, ok in checks), len(checks))]
    put_txt('b593_repin.txt', L)


# ================================================================================ THE PAGES AFTER THE EDITION (the page clause)
def _page_lines(b):
    return b.decode('utf-8').split(NL)


def pages_c2():
    """### after the edition commit: each page re-emitted twice from its v0.16 probe bank (scratchpad, then PLACE-papers); the diff
    ### against HEAD printed. Writes the two pages and data/b593_page_runs.txt, data/b593_pages.json."""
    import chain_page as C
    import difflib
    L = ['### b593 -- THE PAGE CLAUSE (OPEN_TRAILS :12190): THE PAGES RE-EMITTED AFTER THE EDITION COMMIT, TWICE EACH, FROM THE v0.16 PROBE BANKS', '']
    J = {}
    for k in ('zeta', 'chi'):
        outs = []
        for run, dest in ((1, os.path.join(SP, 'b593_%s_run1.md' % k)), (2, os.path.join(PP, PNAME[k]))):
            rc, page, meta, log = C.build(os.path.join(D, NODES[k]), os.path.join(SP, '_b593_c2'), os.path.join(D, PROBE[k]))
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
        L += ['### the two outputs: %s ; sha256 %s' % ('BYTE-IDENTICAL' if outs[0] == outs[1] else '### DIFFER', J[k]['sha256']),
              '### the diff against the page at PLACE-papers HEAD (n=0):'] + ['    ' + x[:300] for x in dl] + ['']
    put_txt('b593_page_runs.txt', L)
    put_json('b593_pages.json', J)


def page_arms(tag):
    """### G-CHAIN-PAGE and G-CHAIN-PAGE-CHI run at PLACE-papers HEAD; counts printed. Writes data/b593_page_arms_<tag>.txt."""
    import g_chain_page as GCP
    L = ['### b593 -- THE TWO PAGE ARMS RUN AT PLACE-papers HEAD %s (%s), relay tools/g_chain_page.py, from-output' % (
        g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b593_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok']
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    put_txt('b593_page_arms_%s.txt' % tag, L)


# ================================================================================ COMPONENT 3: THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
KERNELS = {'SIDE-explicit-formula': 'c404e727', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
           'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
           'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
REGISTER = ('ch_iff_rh', 'h2_sign', 'silence_universal')


def scores():
    H, E, P = jl('b593_h28.json'), jl('b593_edition.json'), jl('b593_pages.json')
    a2 = rd('b593_page_arms_c2.txt')
    heads = {k: g('D:/' + k, 'rev-parse', 'main').strip() for k in KERNELS}
    kern_ok = all(heads[k].startswith(v) for k, v in KERNELS.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    lock = os.path.getmtime(os.path.join(D, 'b593_lockgate.json'))
    fresh = [x for x in g(RELAY, 'ls-files', '--others', '--exclude-standard', 'data/', 'tools/').split(NL)
             if x.strip() and os.path.getmtime(os.path.join(ROOT, x)) >= lock - 6 * 3600]
    relay_new = sorted(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD', '--', 'data/', 'tools/').split(NL) + fresh)
                       if x.strip() and not os.path.basename(x).startswith(('b593_', 'audit_b593_', 'terminal_table')) and x != 'data/b592_closing_push_out.txt')
    wl = [d for d in E['diff'] if d['kind'] == 'work-list']
    reg = [d for d in wl if d['line'] in (72, 146, 553)]
    ceil_row = [d for d in wl if d['line'] == 467]
    hl = H['hits']
    S = dict(
        N1=('HELD' if len(reg) + len(ceil_row) >= 10 else 'REFUTED',
            'rows covered by (R203)(4)`s readings %d of 14: the register reading (the b538 census, PATHS v0.7 :69) %d -- :72 x3, :146 x3, :553 '
            'x3 -- and the "proved"-phrasing reading %d (:467); the four h2-at-Φ rows (:258, :274, :356, :469) resolved by the form with '
            'PATHS v0.7 :65`s reading, which (R203)(4) does not name' % (len(reg) + len(ceil_row), len(reg), len(ceil_row))),
        N2=('REFUTED', 'in its letter: the balance sentence has no rewrite -- by the author`s answer 1 it carries, and the history line '
                       'beneath the 2026-08-28 annotation (:%s) cites arith_limit_nonneg_iff_rh at v0.9 and li_identity_sym at v0.7' % E['hist_at']['65']),
        N3=('HELD' if H['H28a'] == H['H28b'] == H['H28c'] == 'HELD' and H['held'] is None else 'REFUTED',
            'H28a %s, H28b %s, H28c %s ; held: %s' % (H['H28a'], H['H28b'], H['H28c'], H['held'] or 'none')),
        N4=('HELD' if H['n_ceils'] <= 8 and H['n_facts'] <= 1 else 'REFUTED', 'ceiling corrections %d ; fact corrections %d' % (H['n_ceils'], H['n_facts'])),
        N5=('HELD' if kern_ok and pp_ch == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', PAGE, DIR_PAGE, ED]) and relay_new == [] else 'REFUTED',
            'nothing deposits; kernel heads %s; PLACE-papers %s; relay files beyond b593`s own %s' % ('unmoved' if kern_ok else heads, pp_ch, relay_new or 'none')),
        S1=('HELD' if len(wl) == 14 and all(d['changed'] and d['cites'] for d in wl) else 'REFUTED',
            'work-list rows rewritten in place, each citing a declaration at its pin: %d of %d' % (sum(1 for d in wl if d['changed'] and d['cites']), len(wl))),
        S2=('HELD' if H['clean'] and H['history'] == 2 else 'REFUTED', 'the scanner`s verdict %s ; carried-by-history %s' % ('CLEAN' if H['clean'] else 'NOT CLEAN', H['history'])),
        S3=('HELD' if H['n_ceils'] == 1 else 'REFUTED', 'ceiling corrections %d' % H['n_ceils']),
        S4=('HELD' if P and all(P[k]['identical'] and len([x for x in P[k]['diff'] if x.startswith('+| keystone')]) == 1 for k in ('zeta', 'chi'))
            and 'PAGE ARMS PASSING : 2 of 2' in a2 else 'REFUTED',
            'after the edition commit: ζ +%d, χ +%d Placement rows, each twice byte-identical ; page arms %s' % (
                len([x for x in P.get('zeta', {}).get('diff', []) if x.startswith('+| keystone')]),
                len([x for x in P.get('chi', {}).get('diff', []) if x.startswith('+| keystone')]),
                re.search(r'PASSING : (\d of 2)', a2).group(1) if re.search(r'PASSING : (\d of 2)', a2) else '?')),
        S5=('HELD' if H['body_dn'] == 5 else 'REFUTED', 'body %+d (four history lines and the version line)' % H['body_dn']),
    )
    S.update(H28a=(H['H28a'], 'the 14 work-list rows each cite a declaration at its pin'), H28b=(H['H28b'], 'body %+d against at most %d' % (H['body_dn'], H['allowed'])),
             H28c=(H['H28c'], 'scanner CLEAN %s ; beyond the ceiling %d' % (H['clean'], H['beyond'])))
    put_json('b593_scores.json', S)
    for k in SCORE_KEYS + ('H28a', 'H28b', 'H28c'):
        print('  %-4s %s -- %s' % (k, S[k][0], S[k][1][:170]))


TITLE = ('## CP-7, act fifteen: the edition of BALANCE_AND_POSITIVITY from its tier block and work-list, the balance sentence cited to the '
         'arithmetic-limit face, the R4 edge to Li’s criterion compiled')
TRAIL_HEAD = ('### b593 — lane three, act twenty under (R203): CP-7 act fifteen -- the edition of BALANCE_AND_POSITIVITY written beside '
              'v0.9.4; the act root and the second reader entered as priced work-orders')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def findings():
    Q = _Q()
    S, E, H, wl, wo = jl('b593_scores.json'), jl('b593_edition.json'), jl('b593_h28.json'), jl('b593_weight_line.json'), jl('b593_workorders.json')
    Q.guard_absent(Q.FIND, TITLE[:90])
    e = ['', TITLE, '',
         '*Filed at b593 on the author’s ruling `(R203)`. Banks: relay `data/b593_edition_BALPOS.txt`, `data/b593_edition.json`, '
         '`data/b593_edition_termscan.txt`, `data/b593_repin.txt`, `data/b593_page_runs.txt`, `data/b593_author_answers.txt`. Nothing deposits.*', '',
         '**The edition** (`(R203)`(4), by the form at OPEN_TRAILS :11864 and its clauses): `%s` beside v0.9.4, which is unedited, sha256 `%s`. '
         'The 14 work-list rows on 8 lines rewritten in place: the register sentences (v0.9.4 :72, :146, :553) read by the b538 census as '
         'PATHS v0.7 :69 reads them -- the registers at different depths, not one joint (the universality hypothesis false as stated, '
         'the conservation hypothesis RH restated, the one premise in its Weil form and the balance distance in its Li form each '
         'equivalent to RH); the four h2-at-Φ sentences (:258, :274, :356, :469) naming lv’s h2 at Φ false on the strip and the open '
         'clause as h2_sign; the finite-range certificate (:467) with its two literature premises named and T1-lit. By the ruling’s '
         'reading and the author’s answers: the R4 edge’s Li criterion named compiled at v0.9 and v0.11 (:72); the joint’s Li form '
         'cited at its five body uses to li_nonneg_iff_rh and arith_limit_nonneg_iff_rh through li_identity_sym (:21, :72, :146, :360, '
         ':430);the balance sentence’s compiled form in a history line beneath the 2026-08-28 annotation, for the Bombieri–Lagarias '
         'family, its “every admissible g” remaining the Weil face; the dated Li entries of b545 and b561 superseded by one history line; '
         'the two dated stems carried with lines beneath. One ceiling correction (:21, the sign core of the reduction), four stems in '
         'place, no fact correction, no credit inserted (the :274 credit already entered at :5461 / :5527). Body %d sentences against %d '
         '(%+d: four history lines and the version line); back matter %d. H28a %s, H28b %s, H28c %s; no sentence held.' % (
             ED, E['sha256'], E['n_body'], E['n_cur'], E['n_body'] - E['n_cur'], E['n_backmatter'], H['H28a'], H['H28b'], H['H28c']), '',
         '**The pages** (the page clause): each re-emitted after the edition commit for its one new Placement row and committed alone '
         '(PLACE-papers %s, %s), twice byte-identical.' % (_pp_commit('b593 housekeeping -- the ζ page'), _pp_commit('b593 housekeeping -- the χ page')), '',
         '**The record lines.** b592’s weight at FINDINGS :%d; W-ORD-ACT-ROOT at OPEN_TRAILS :%d and W-ORD-SECOND-READER at :%d, each '
         'priced and not started, trigger the author’s word.' % (wl['line'], wo['lines'][0]['line'], wo['lines'][1]['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R203)`(5): FACES_OF_H2_AT_FINITE_INSTANCE by the same form, the second companion; then W-ORD-SIMPLICITY-FACE or '
         'the author’s ruling that SIMPLICITY is out of scope; the author rules on the closing.', '',
         '*Nothing deposits; no kernel written; BALANCE_AND_POSITIVITY v0.9.4 unedited; README, REGISTRY and ERRATA unwritten; nothing here '
         'is a statement about RH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b593_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE[:90]), title=TITLE, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, TITLE[:90]))


def trail():
    Q = _Q()
    S, fj, wl, wo = jl('b593_scores.json'), jl('b593_findings.json'), jl('b593_weight_line.json'), jl('b593_workorders.json')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R203) ratified.** (1) b592 at its weight. (2) W-ORD-ACT-ROOT entered priced. (3) W-ORD-SECOND-READER entered priced, its '
             'form fixed. (4) CP-7 act fifteen, the edition of BALANCE_AND_POSITIVITY. (5) The act after: FACES_OF_H2_AT_FINITE_INSTANCE.', '',
             '**Entered:** FINDINGS.md:%d (b592’s weight), :%d (the entry); OPEN_TRAILS.md:%d (W-ORD-ACT-ROOT), :%d (W-ORD-SECOND-READER), '
             'this record; PLACE-papers `%s` (the edition).' % (wl['line'], fj['entry_line'], wo['lines'][0]['line'], wo['lines'][1]['line'], ED), '',
             '**Answered before the seal, by the author** (relay data/b593_author_answers.txt): the balance sentence’s compiled form in a '
             'history line beneath the 2026-08-28 annotation, its “every admissible g” the Weil face; the joint’s Li form cited at its five '
             'body uses (the fifth, :21, on the author’s answer 5 after the seat’s question had listed four);the dated Li entries of b545 and b561 superseded by one history line, the basis sentence standing with the three '
             'faces cited; the currency note and the v0.7 entry carried as dated records with lines beneath.', '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R203)`(5), FACES_OF_H2_AT_FINITE_INSTANCE by the same form; then W-ORD-SIMPLICITY-FACE or the author’s '
             'ruling that SIMPLICITY is out of scope; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel written; BALANCE_AND_POSITIVITY v0.9.4 unedited; ERRATA untouched; '
             'FACES_LEDGER untouched; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b593_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b593_trail.json')['line'])


def desk():
    S = jl('b593_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b593 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H28a-H28c.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in ('H28a', 'H28b', 'H28c')]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)),
          '### ### **H28a %s ; H28b %s ; H28c %s.**' % (S['H28a'][0], S['H28b'][0], S['H28c'][0]), '']
    L += rd('b593_defects.txt').rstrip(NL).split(NL)
    put_txt('b593_desk_notes.txt', L)


def components():
    S, E, fj, tj, wl, wo = (jl('b593_scores.json'), jl('b593_edition.json'), jl('b593_findings.json'), jl('b593_trail.json'),
                            jl('b593_weight_line.json'), jl('b593_workorders.json'))
    L = ['b593 -- THE COMPONENTS, BANKED UNDER (R203).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b592`s closing push-out relay %s ; push-b592* branches deleted by name '
         '(data/b593_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b593_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b592`s weight FINDINGS :%d ; W-ORD-ACT-ROOT OPEN_TRAILS :%d ; W-ORD-SECOND-READER :%d' % (
             wl['line'], wo['lines'][0]['line'], wo['lines'][1]['line']),
         '### COMPONENT 2 : the edition %s (sha256 %s) ; body %d vs %d ; back matter %d ; H28a %s, H28b %s, H28c %s ; no sentence held ; '
         'the pages re-emitted after the edition commit (data/b593_page_runs.txt)' % (
             ED, E['sha256'][:16], E['n_body'], E['n_cur'], E['n_backmatter'], S['H28a'][0], S['H28b'][0], S['H28c'][0]),
         '### COMPONENT 3 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: FACES_OF_H2_AT_FINITE_INSTANCE ; '
         'N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b593_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b593_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
