# -*- coding: utf-8 -*-
"""b598_record.py -- THE ACT'S RECORD TOOL, UNDER (R208). ### ONE SUBCOMMAND PER BANK.

### ### b598: LANE THREE, ACT TWENTY-FIVE -- CP-1b: THE TIER BLOCKS AND WORK-LISTS OF SILENCE_STAGES_DEALIGNMENT AND
### REPARAMETERIZATION BY THE b558 FORM.
### Subcommands write only `data/b598_*` and, for `bank <doc>`, the one file `data/b558_editions/<TITLE>.txt`, unless the docstring
### names another file. Every bank is written through `put_txt` / `put_json` (encode, temp file, `os.replace`). No platform call.
### The templates are b558_record.py (the citer matcher, the segments, the work-list form) and b597_record.py (the record lines).
### No document is written: b558's pointer line, appended to each work-listed document at b558, is NOT written here ((R208)(3), (N5)).
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
ED_DIR = os.path.join(D, 'b558_editions')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'eb9b057'
PRE_RELAY = '022d2bf0'
STEPZERO = 'cab56f31'
B537_PP = 'b7e0c52'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/c36c4b1c-6feb-4e3e-9e2c-aeb65eff6769/scratchpad'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/c36c4b1c-6feb-4e3e-9e2c-aeb65eff6769.jsonl'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
TEMPLATE = 'data/b558_editions/SIMPLICITY_OF_RIEMANN_ZEROS.txt'
SEC = 'D:/SIDE-structural-error-correction'
COS = 'D:/SIDE-cosmo'
SKK = 'D:/SIDE-kernel'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines, d=None):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(d or D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (p.replace('\\', '/').split('/relay/')[-1] if d is None or d.startswith(ROOT) else p, len(b)))
    return b


def put_json(name, obj, d=None):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(d or D, name)
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
    '(a) THE FINDINGS ENTRY`S FIRST LANDING OVER-CLAIMED ITS OFFERING: its mutual-light line called the CP-1b work-lists “now complete '
    'over the roster”, while b558 left five roster documents without one (relay data/b558_editions.json, “none”: SILENCE, REPARAM, LEDGER, '
    'IDC, CENSUS) and this act lists two of them. Found by the seat`s read-back of the uncommitted append, before any commit or push; '
    'FINDINGS cut back to the append`s banked `before` length (940587 bytes) after checking that the pre-act blob is a prefix, the '
    'sentence corrected in the record tool through the Edit tool, the entry re-run -- it lands at the same line, :6902, so the trail '
    'record`s citation stands.',
]


def defects():
    put_txt('b598_defects.txt', ['### b598 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ THE TWO DOCUMENTS
DOCS = {
    'SILENCE': dict(title='SILENCE_STAGES_DEALIGNMENT', path='phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md',
                    own=['no_domain_covers_line', 'single_domain_fault_not_logical', 'dealigned_of_lines_injective',
                         'fano_dealignment_decidable_example', 'fano_collapsed_line_rejected', 'fano_two_design',
                         'steane_parameters', 'knill_laflamme_t1']),
    'REPARAM': dict(title='REPARAMETERIZATION_BARRIERS_v0_1', path='phase2/method/REPARAMETERIZATION_BARRIERS_v0_1.md',
                    own=['invariance_barrier', 'derivability_barrier']),
}
ORDER = ('SILENCE', 'REPARAM')

# ### the tier block: every terminal the document cites, at the pin the document cites it at; the grade read from b557's tier bank
# ### (relay data/b557_tiers.txt, the fresh profile there) and checked against the terminal table at relay HEAD and both pages at v0.17.
# ### (key, terminal, qualified name the document writes, kernel repo, the document's pin cell, the rev the file is read at, file)
TERMS = {
    'SILENCE': [
        ('no_domain_covers_line', 'DeAlignment.no_domain_covers_line', SEC, 'v0.2.1 = 6a4f482', 'v0.2.1', 'SIDEStructuralErrorCorrection/DeAlignment.lean'),
        ('single_domain_fault_not_logical', 'DeAlignment.single_domain_fault_not_logical', SEC, 'v0.2.1 = 6a4f482', 'v0.2.1', 'SIDEStructuralErrorCorrection/DeAlignment.lean'),
        ('dealigned_of_lines_injective', 'DeAlignment.dealigned_of_lines_injective', SEC, 'v0.2.1 = 6a4f482', 'v0.2.1', 'SIDEStructuralErrorCorrection/DeAlignment.lean'),
        ('fano_dealignment_decidable_example', 'DeAlignment.fano_dealignment_decidable_example', SEC, 'v0.2.1 = 6a4f482', 'v0.2.1', 'SIDEStructuralErrorCorrection/DeAlignment.lean'),
        ('fano_collapsed_line_rejected', 'DeAlignment.fano_collapsed_line_rejected', SEC, 'v0.2.1 = 6a4f482', 'v0.2.1', 'SIDEStructuralErrorCorrection/DeAlignment.lean'),
        ('fano_two_design', 'DeAlignment.fano_two_design', SEC, 'v0.2.1 = 6a4f482', 'v0.2.1', 'SIDEStructuralErrorCorrection/DeAlignment.lean'),
        ('steane_parameters', 'steane_parameters', COS, 'c5cba30 (SIDE-cosmo main)', 'c5cba30', 'SIDECosmo/SteaneExemplar.lean'),
        ('knill_laflamme_t1', 'knill_laflamme_t1', COS, 'c5cba30 (SIDE-cosmo main)', 'c5cba30', 'SIDECosmo/SteaneExemplar.lean'),
        ('conservation_of_spectra', 'conservation_of_spectra', SKK, 'v1.5 = 0e5233f (the deposit; cited by the b558 alias "Conservation of Spectra")',
         'v1.5', 'Kernel/ProductFormula_Rat.lean'),
    ],
    'REPARAM': [
        ('invariance_barrier', 'InvarianceBarrier.invariance_barrier', SKK, '5e668b4 (the row`s pin; v1.7 = 2957e7d drafted)', '5e668b4', 'Kernel/Cascade/InvarianceBarrier.lean'),
        ('derivability_barrier', 'InvarianceBarrier.derivability_barrier', SKK, '5e668b4 (the row`s pin; v1.7 = 2957e7d drafted)', '5e668b4', 'Kernel/Cascade/InvarianceBarrier.lean'),
    ],
}
# ### definitions the document writes out (not terminals; E0 DEF, no tier): (doc, name, repo, rev, file, the document's line)
DEFS = [('REPARAM', 'DeterminedBy', SKK, '5e668b4', 'Kernel/Cascade/InvarianceBarrier.lean', 59),
        ('REPARAM', 'Derives', SKK, '5e668b4', 'Kernel/Cascade/InvarianceBarrier.lean', 66)]
# ### the tier and its reason, read from b557's tier bank at the line printed (b558's union settles conservation_of_spectra)
TIER = {
    'conservation_of_spectra': ('T2', 'states `∀ (s : Int), (1 : Rat) ^ s = 1`, a stipulation (THE_LOAD_BEARING_MAP :105, b539); b558`s union, S3',
                                'data/b558_moved_terminals.txt'),
}
T4ROWS = {'SILENCE': [210, 211], 'REPARAM': [225, 226, 227, 228, 229, 230, 231]}

# ================================================================================ THE READINGS OF THE DOCUMENTS' OWN ROWS
P_SEC = 'SIDE-structural-error-correction v0.2.1 = `6a4f482`'
P_COS = 'SIDE-cosmo `c5cba30`'
P_IB = 'SIDE-kernel `5e668b4` (blob `e4e8d23b`, the same at v1.7 = `2957e7d` and at main `0256e9e`)'
READ = {
    ('SILENCE', 109, 'conservation_of_spectra'): (
        'STANDS', 'b558`s reading, carried (relay `data/b558_cp1b.txt` :425): names the manuscript`s Conservation of Spectra and claims no '
        'compiled content, so the terminal`s T2 reading (`∀ (s : Int), (1 : Rat) ^ s = 1`, SIDE-kernel v1.5 = `0e5233f`, '
        '`Kernel/ProductFormula_Rat.lean` :72) leaves its meaning as it was.'),
    ('SILENCE', 176, 'no_domain_covers_line'): (
        'STANDS', 'states the consequence as the compiled statement has it: under `DealignedAt d L` no domain fault `domainFault d k` '
        'completes `L` (`DeAlignment.lean` :62, ' + P_SEC + '); the sentence keeps the condition-plus-consequence form of the statement, '
        'and the T2 tier (the file`s own `Line` structure and a domain map) leaves it as it was.'),
    ('SILENCE', 176, 'single_domain_fault_not_logical'): (
        'STANDS', 'the same consequence over a line family `lines : Fin n → Line P` under `Dealigned d lines` (`DeAlignment.lean` :75, '
        + P_SEC + '), as the sentence states it.'),
    ('SILENCE', 198, 'fano_two_design'): (
        'STANDS', 'the profile `[propext]` the sentence records is the profile b557 printed afresh at the pin (relay `data/b557_tiers.txt` '
        ':311-:318).'),
    ('SILENCE', 202, 'no_domain_covers_line'): (
        'STANDS', 'the claim cell is the statement (`DeAlignment.lean` :62, ' + P_SEC + '), axiom-free as printed; DERIVES is the '
        'document`s grade word and T2 (programme-type) the tier b557 entered beneath (:273), neither moving the claim.'),
    ('SILENCE', 203, 'single_domain_fault_not_logical'): (
        'STANDS', '“over any line family” is the statement`s `lines : Fin n → Line P` for every `n` (`DeAlignment.lean` :75, ' + P_SEC + ').'),
    ('SILENCE', 204, 'dealigned_of_lines_injective'): (
        'STANDS', 'the statement takes an injective domain map and a proper line (`L.Proper`, its three positions distinct) to '
        '`DealignedAt d L` (`DeAlignment.lean` :85, ' + P_SEC + '); the premise `L.Proper` is the well-formedness of a line, which the '
        'claim cell leaves implicit, and the claim stands.'),
    ('SILENCE', 205, 'fano_dealignment_decidable_example'): (
        'STANDS', 'the statement evaluates the check `dealignedCheck` on the identity assignment to `true` (`DeAlignment.lean` :113, '
        + P_SEC + '): the condition is checked by evaluation, as the claim cell says.'),
    ('SILENCE', 206, 'fano_collapsed_line_rejected'): (
        'STANDS', 'the statement evaluates the check on the assignment sending positions 1 and 3 to one domain to `false` '
        '(`DeAlignment.lean` :118, ' + P_SEC + '), the refusal the claim cell names.'),
    ('SILENCE', 207, 'fano_two_design'): (
        'STANDS', '`∀ p q : Fin 7, p ≠ q → pairCount p q = 1` by `decide`, profile `[propext]` (`DeAlignment.lean` :140, ' + P_SEC + '), '
        'the claim cell`s 2-design.'),
    ('SILENCE', 208, 'steane_parameters'): (
        'STANDS', 'the statement carries the three numbers: 7 as the formation total, 1 as `2 * visible_slots xi - xi.formation_total`, '
        'and distance 3 as no two columns of the parity map `H` summing to zero with the zero-sum triple `H 0 + H 1 + H 3 = 0` '
        '(`SIDECosmo/SteaneExemplar.lean` :81, ' + P_COS + '); that n and k are the CSS code`s block length and logical dimension is read '
        'off the formation tuple in the docstrings (:42-:51), and the claim cell names the parameters, not their derivation.'),
    ('SILENCE', 209, 'knill_laflamme_t1'): (
        'MOVED-IN-MEANING', 'names the Knill–Laflamme error-correction conditions with the grade DERIVES, and the terminal states only that '
        'the parity map `H : Fin 7 → ZMod 2 × ZMod 2 × ZMod 2` has nonzero, pairwise distinct columns (`Function.Injective H ∧ ∀ i : Fin '
        '7, H i ≠ 0`, `SIDECosmo/SteaneExemplar.lean` :76, ' + P_COS + '); that this is the Knill–Laflamme condition for every Pauli error '
        'of weight at most one in the CSS setting is its docstring`s (:72-:75), not compiled, so what is compiled is the t = 1 syndrome '
        'condition the name abbreviates.'),
    ('SILENCE', 243, 'fano_two_design'): (
        'STANDS', 'a dated version entry (v1.1, 2026-07-29) recording the §9 pass, read under the history clause; its `[propext]` on '
        '`fano_two_design` is the profile at the pin.'),
    ('REPARAM', 58, 'invariance_barrier'): (
        'STANDS', 'the code block`s statement, `agree x y → ¬(P x ↔ P y) → ¬ DeterminedBy agree P` (:58-:59), is the compiled one '
        '(`Kernel/Cascade/InvarianceBarrier.lean` :39, ' + P_IB + '), `DeterminedBy agree P := ∀ x y, agree x y → (P x ↔ P y)` (:31); '
        'the T2 tier (a schema over an abstract carrier, b556) is the reading the note gives it itself at :71-:73 (“deliberately weak — '
        'all the mathematical content of any barrier built on them sits in the two hypotheses”).'),
    ('REPARAM', 67, 'derivability_barrier'): (
        'STANDS', 'the code block`s statement is the compiled one (`Kernel/Cascade/InvarianceBarrier.lean` :60, ' + P_IB + '), with '
        '`Derives agree P x := ∀ z, agree x z → P z` (:50) as :66 writes it.'),
    ('REPARAM', 223, 'invariance_barrier'): (
        'STANDS', 'the row`s pin `5e668b4` holds the file byte for byte as v1.7 and main do (' + P_IB + '), axiom-free as re-printed; '
        'the claim cell is the statement (:39).'),
    ('REPARAM', 224, 'derivability_barrier'): (
        'STANDS', 'the same pin and blob (' + P_IB + '); “assumes nothing of the object of interest” is the statement`s premise `¬ P y` on '
        'the witness alone (:60).'),
}

# ### objects for the edition's other clauses, printed for b599 and graded by no row: (doc, lines, clause, the object)
OBJECTS = [
    ('SILENCE', ':210, :211 (and :97, :213, :235)', 'fact',
     'the rows say “no terminal” / “no kernel pin”, and the pin the section cites, ' + P_SEC + ', carries '
     '`SIDEStructuralErrorCorrection.d_eff_formula` (`Basic.lean` :103, `d_eff = 2 * S - 1` by `decide`, with `d_eff` defined as `2 * S - 1` '
     'at :97) and `silence_yields_protection` (:233, `num_compartments = S ∧ d_eff = 2 * num_compartments - 1`, `num_compartments := S` at '
     ':222): each restates its own definitions at the constant `S`, the general bound for every S is uncompiled, so the rows` '
     'manuscript-resident status stands and the words “no terminal” are the fact clause`s to read'),
    ('SILENCE', ':208, :209', 'fact',
     'the rows write `SteaneExemplar.steane_parameters` and `SteaneExemplar.knill_laflamme_t1`; the file `SIDECosmo/SteaneExemplar.lean` '
     'at ' + P_COS + ' opens no namespace, so the declarations are `steane_parameters` and `knill_laflamme_t1` at the root, as the '
     'terminal table names them'),
    ('SILENCE', ':21', 'restatement',
     '“We prove: the effective distance under formation-block errors equals 2S − 1” restates §3`s theorem, which :97 and the row :210 '
     'hold manuscript-resident with a proof sketch'),
    ('REPARAM', ':219', 'fact',
     '“the CURRENT kernel pin `5e668b4`”: SIDE-kernel main is `0256e9e`; `Kernel/Cascade/InvarianceBarrier.lean` is byte-identical '
     '(blob `e4e8d23b`) at `5e668b4`, v1.7 = `2957e7d` and `0256e9e`, and absent at the deposit v1.5 = `0e5233f`'),
    ('REPARAM', ':40-:41', 'restatement',
     '“the barrier is proved, not conjectured”: the compiled part is the schema (:223, :224); the witness pair (W1)-(W5) and the '
     'membership table are manuscript-resident (:225-:230)'),
]

# ### b450's items, located by name and placed (relay data/b450_components.txt), with b394's reading behind the RECONCILED mark
B450 = {
    'SILENCE': [
        ('relay `data/b450_components.txt` :21', '“10  SILENCE_STAGES_DEALIGNMENT  RECONCILED  2  -  read whole at b394 under b390`s rule”',
         'NO ITEM: b450 named the document only as RECONCILED, outside its batch, and carries no item for it'),
        ('relay `data/b394_components.txt` :79-:82 (OPEN_TRAILS :4540)', '“IT CARRIES NO CORRESPONDENCE TABLE”',
         'contradicted by the document: §9 “Correspondence” at :196, ten rows :202-:211, present in the blob b394 read (PLACE-papers '
         '`4cd1cd2`, 263 lines, §9 at :196) -- the heading opens “## 9.”, the shape b586 found a heading matcher can miss; it corrects '
         'the record`s claim about the document (the basis of b450`s RECONCILED), not a sentence of the document'),
        ('relay `data/b394_components.txt` :85-:87', '“THE RECORD -- REGISTRY.md line 244: | p2-24 | Dark Interface |”',
         'the record item b394 matched is another document`s row (p2-24, `phase2/philosophy/DARK_INTERFACE.md`, now REGISTRY :249); '
         'this document`s row is p2-16 (now REGISTRY :283); it corrects the record, not the document'),
    ],
    'REPARAM': [
        ('relay `data/b450_components.txt` :176', '“REPARAMETERIZATION_BARRIERS_v0_1  does not carry: the two-kinds windows verdict”',
         'carried since b454: the era annotation at :256-:262 (PLACE-papers `b4b0be2`, “VERDICT: `DISTINCT`”), placed beside the '
         'Correspondence and the work-orders; the item is in the document, so no credit line is owed at b599'),
        ('relay `data/b450_components.txt` :113', '“(i) registry row  None  a registry table row at REGISTRY.md:658 names the file and '
         'carries no version”',
         'the row is now REGISTRY :687, still with no version cell; a registry row is the author`s (b450`s own routing), not the edition`s'),
    ],
}
SECOND = ('Silence Principle', r'Silence Principle')
SECOND_NOTE = ('the b558 form`s matcher reads each union terminal by its name and the ferry`s four aliases only (relay '
               '`tools/b558_record.py` :330-:335); “Silence Principle” is none of them, so these segments are PRINTED AND NOT GRADED. The '
               'declarations they would meet: `silence_universal` (SIDE-silence-principle v0.2.0 = `667c254`, `SIDESilencePrinciple/Basic.lean`; '
               'T2-INTERFACES on `I.is_universal`, b557-b558) and the ζ page`s `silence_universal_restated` (SIDE-explicit-formula v0.17, '
               '`THE_CLAUSE_AND_ITS_COMPILED_FACES.md` :164, DERIVES, T0). The alias is the author`s to rule.')


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay the b558 form, the template bank read whole', RELAY, 'HEAD', TEMPLATE, list(range(1, 31))),
    ('relay CP-1b`s per-document counts and the two documents` rows', RELAY, 'HEAD', 'data/b558_cp1b.txt', [1, 3, 4, 38, 41, 425, 426, 472]),
    ('relay the b558 matcher: the aliases and the segments', RELAY, 'HEAD', 'tools/b558_record.py', [330, 331, 332, 333, 334, 335, 366, 367, 371]),
    ('PLACE-papers SILENCE_STAGES_DEALIGNMENT (current): head, version, abstract, scope, the citing sentences, §9, the history, the '
     'era annotation, b557`s block', PP, PRE_PP, DOCS['SILENCE']['path'],
     [1, 3, 9, 15, 21, 23, 97, 109, 121, 144, 150, 162, 170, 176, 196, 198, 200, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 213, 229,
      231, 233, 235, 241, 243, 245, 249, 257, 265, 267, 284, 287]),
    ('PLACE-papers REPARAMETERIZATION_BARRIERS_v0_1 (current): head, version, abstract, the schema, the citing sentences, the '
     'Correspondence, the work-orders, the history, b454`s and b557`s blocks', PP, PRE_PP, DOCS['REPARAM']['path'],
     [1, 6, 23, 41, 58, 59, 66, 67, 70, 71, 72, 73, 219, 221, 223, 224, 225, 229, 230, 231, 235, 243, 252, 256, 260, 262, 264, 266, 282, 285]),
    ('PLACE-papers the ζ page at v0.17: head and the silence row', PP, PRE_PP, PAGE, [1, 3, 164]),
    ('PLACE-papers the χ page at v0.17: head', PP, PRE_PP, DIR_PAGE, [1, 3]),
    ('PLACE-papers OPEN_TRAILS: the form, the precedence order, the generator-run line, the work-order, the DENSITY line, b394`s block',
     PP, PRE_PP, 'OPEN_TRAILS.md', [4538, 4540, 11864, 12228, 12288, 12290, 12296, 12298]),
    ('PLACE-papers FINDINGS: b557`s and b558`s entries, b597`s weight and entry', PP, PRE_PP, 'FINDINGS.md', [5870, 5990, 6878, 6880]),
    ('PLACE-papers REGISTRY: the two documents` rows and the row b394 matched (each cut after its version cell)', PP, PRE_PP, 'REGISTRY.md',
     [249, 283, 687], 116),
    ('relay b450`s components: the census rows and items of the two documents', RELAY, 'HEAD', 'data/b450_components.txt', [10, 21, 24, 29, 59, 112, 113, 176]),
    ('relay b394`s components: SILENCE_STAGES_DEALIGNMENT', RELAY, 'HEAD', 'data/b394_components.txt', list(range(75, 91))),
    ('relay b557`s tier bank: SILENCE_STAGES_DEALIGNMENT', RELAY, 'HEAD', 'data/b557_tiers.txt', [268, 271, 272, 274, 279, 287, 295, 303, 311, 313, 319, 320, 322, 327, 328, 330]),
    ('relay b557`s tier bank: REPARAMETERIZATION_BARRIERS_v0_1', RELAY, 'HEAD', 'data/b557_tiers.txt', [557, 560, 561, 563, 564, 568, 571]),
    ('SIDE-structural-error-correction v0.2.1 DeAlignment.lean', SEC, 'v0.2.1', 'SIDEStructuralErrorCorrection/DeAlignment.lean', [29, 62, 75, 85, 113, 118, 140, 142]),
    ('SIDE-structural-error-correction v0.2.1 Basic.lean: the definitions and the two restating theorems', SEC, 'v0.2.1',
     'SIDEStructuralErrorCorrection/Basic.lean', [36, 71, 97, 100, 103, 222, 233, 234]),
    ('SIDE-cosmo c5cba30 SteaneExemplar.lean', COS, 'c5cba30', 'SIDECosmo/SteaneExemplar.lean', [42, 43, 48, 51, 55, 58, 63, 68, 72, 73, 74, 75, 76, 77, 81, 82, 83, 84, 85]),
    ('SIDE-kernel 5e668b4 InvarianceBarrier.lean', SKK, '5e668b4', 'Kernel/Cascade/InvarianceBarrier.lean', [31, 32, 39, 50, 51, 60]),
    ('SIDE-kernel v1.5 ProductFormula_Rat.lean', SKK, 'v1.5', 'Kernel/ProductFormula_Rat.lean', [72, 73]),
    ('relay b597`s closing push-out, committed at step zero', RELAY, 'HEAD', 'data/b597_closing_push_out.txt', list(range(1, 9))),
]


def reads():
    L = ['b598 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for rr in READS:
        label, repo, rev, path, sel = rr[:5]
        width = rr[5] if len(rr) > 5 else 600
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev + '^{}').strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    T = jl('terminal_table.json')
    L += ['', '### the terminal table at relay HEAD (%s), its rows for every cited terminal and definition:' % g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()]
    for k in ORDER:
        for t in [x[0] for x in TERMS[k]] + [d[1] for d in DEFS if d[0] == k]:
            rs = _table_rows(T, t)
            L.append('    %-8s %-36s %s' % (k, t, ' ; '.join('%s %s grade %s profile %s present_at %s' % (r['repo'], r['name'], r['grade'], r['profile_state'],
                                                                                                          r['present_at']) for r in rs) or 'NO ROW'))
    L += ['', '### the two pages at v0.17, lines naming a cited terminal: ζ %s ; χ %s' % (
        _page_hits(PAGE), _page_hits(DIR_PAGE)),
          '### SIDE-kernel: InvarianceBarrier.lean blob at 5e668b4 %s, v1.7 %s, main %s, v1.5 %s ; 5e668b4 an ancestor of main: %s' % tuple(
              [g(SKK, 'rev-parse', '--short=8', '%s:Kernel/Cascade/InvarianceBarrier.lean' % r).strip() or 'ABSENT' for r in ('5e668b4', 'v1.7', 'main', 'v1.5')]
              + [subprocess.run(['git', '-C', SKK, 'merge-base', '--is-ancestor', '5e668b4', 'main']).returncode == 0]),
          '### SIDE-structural-error-correction: v0.2.1 = %s ; main = %s ; SIDE-cosmo main = %s' % (
              g(SEC, 'rev-parse', '--short=7', 'v0.2.1^{commit}').strip(), g(SEC, 'rev-parse', '--short=7', 'main').strip(),
              g(COS, 'rev-parse', '--short=7', 'main').strip()),
          '### SIDE-cosmo SteaneExemplar.lean opens a namespace: %s' % bool(re.search(r'^namespace ', g(COS, 'show', 'c5cba30:SIDECosmo/SteaneExemplar.lean'), re.M)),
          '### b394`s read of SILENCE_STAGES_DEALIGNMENT at PLACE-papers 4cd1cd2: %d lines, `## 9. Correspondence` at :%s' % (
              len(g(PP, 'show', '4cd1cd2:' + DOCS['SILENCE']['path']).rstrip(NL).split(NL)),
              next((i + 1 for i, l in enumerate(g(PP, 'show', '4cd1cd2:' + DOCS['SILENCE']['path']).split(NL)) if l.startswith('## 9. Correspondence')), None))]
    put_txt('b598_reads.txt', L)


def _table_rows(T, t):
    return [r for r in T['rows'] if r['name'] == t or r['name'].endswith('.' + t)]


def _page_hits(p):
    t = g(PP, 'show', '%s:%s' % (PRE_PP, p)).split(NL)
    names = [x[0] for k in ORDER for x in TERMS[k]]
    return [':%d %s' % (i + 1, n) for i, l in enumerate(t) for n in names if re.search(r'(?<![A-Za-z0-9_])' + n + r'(?![A-Za-z0-9_])', l)] or 'none'


# ================================================================================ COMPONENT 1: THE RECORD LINES
B597_ENTRY = '## CP-7, act seventeen: the edition of SIMPLICITY_OF_RIEMANN_ZEROS from its tier block, work-list and the b596 addendum'


def weight_line():
    """### PLACE-papers FINDINGS: b597's weight, one appended line addressed to b597's entry, in (R208)(1)'s facts; then the strike
    ### items as ruled, (R208)(2), one appended line."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B597_ENTRY)
    if entry != 6880:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    h1 = '*Appended 2026-10-02 by b598 to b597’s entry (:%d), under `(R208)`(1) -- b597 AT ITS WEIGHT:*' % entry
    h2 = '*Appended 2026-10-02 by b598 to b597’s entry (:%d), under `(R208)`(2) -- THE STRIKE ITEMS, AS RULED:*' % entry
    for h in (h1, h2):
        Q.guard_absent(Q.FIND, h)
    t1 = ('\n%s SIMPLICITY_OF_RIEMANN_ZEROS v1.1.3 beside v1.1.2, unedited: Chapter 1’s title naming the reduction the body states; '
          'simplicity a separate Prop cited to simplicity_iff at v0.17 with no compiled edge to h2_sign; the 40.77%% anchor replaced by '
          'the named premise SimpleProportion with thmB₀_mult’s upstream line; four work-list lines rewritten; 14 ceiling corrections (11 '
          'on sentences joining simplicity and RH or GRH, each citing the b596 walk), 4 fact corrections (the derivative-engine pin to its '
          'head 01e5633, the SIDE-grh-transfer pin to v0.5.0 = bfd2af7), 2 restatement rewrites, 3 history lines, 2 b450 credit lines, 12 '
          'collisions resolved by the precedence order and listed; body 551 against 545, back matter 134, re-pin 133 of 133; H28a-H28c '
          'held, no sentence held; both pages re-emitted one per call, each gaining a Placement row. The control '
          'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA at 2 of 2 before the seal and after both page commits, the edit in the test file '
          'alone. Relay fe1c68be with the closing at 022d2bf0; PLACE-papers eb9b057; TECHNE-Core untouched. The suite 75 of 76, its one '
          'refutation in letter (G-PAGES-COMMITTED-ALONE) by the correction commit 68c8dfa the author chose. (N2) and (N3) refuted, '
          '(N3) by the ruling’s own order that every join takes the ceiling, the navigator’s count. Two prompts banked verbatim; the '
          'ruling’s “relay ac8257a5” the navigator’s. Defects (a)-(c) the seat’s. Nothing deposited; no kernel touched.\n' % h1)
    t2 = ('\n%s the 12 collisions stand as resolved, the three CP-1b STANDS rows whose simplicity clauses went to the ceiling included; '
          ':24’s “established”, :144 and :278 stand as read by the letter; the b450 credit placement stands; the step-zero repair ran '
          'before the seal by Component 0’s letter, and the ruling’s “after the face is sealed” is the navigator’s, contradicted by its '
          'own ferry -- the ferry’s Component 0 governs an instrument repair ruled for step zero.\n' % h2)
    out = []
    for h, t in ((h1, t1), (h2, t2)):
        r = Q.append_to(Q.FIND, t)
        out.append(dict(head=h, line=Q.line_of(Q.FIND, h), append=r))
    put_json('b598_weight_line.json', dict(entry=entry, lines=out))
    for o in out:
        print('  line :%s' % o['line'])


# ================================================================================ COMPONENT 2: THE TWO BANKS
def _blame(rel):
    r = subprocess.run(['git', '-C', PP, 'blame', '--line-porcelain', PRE_PP, '--', rel], capture_output=True).stdout.decode('utf-8', 'replace')
    out, cur = [], None
    for l in r.split(NL):
        m = re.match(r'^([0-9a-f]{40}) \d+ \d+', l)
        if m:
            cur = m.group(1)[:7]
        elif l.startswith(chr(9)):
            out.append(cur)
    return out


def rows_of(k):
    """### the b558 form's citer rows over one document: every segment naming a union terminal or its alias (b558's matcher,
    ### imported) or a terminal of the document's own tier block, by name; the cascade's own lines (b538-b597) STANDS by default."""
    import b558_record as CP
    U = jl('b558_union.json')['union']
    d = DOCS[k]
    txt = g(PP, 'show', '%s:%s' % (PRE_PP, d['path'])).split(NL)
    bl = _blame(d['path'])
    window = set(x[:7] for x in g(PP, 'rev-list', '%s..%s' % (B537_PP, PRE_PP)).split())
    rows, fence = [], False
    for i, l in enumerate(txt):
        if l.strip().startswith('```'):
            fence = not fence
            continue
        for s in CP.segments(l):
            for t in d['own'] + U:
                hit = [a for a, p in CP.pats(t) if re.search(p, s)]
                if not hit:
                    continue
                c = bl[i] if i < len(bl) else None
                own = 'CASCADE' if c in window else 'DOCUMENT'
                if own == 'CASCADE':
                    v, rdg = 'STANDS', 'the cascade`s own line (b557, `%s`), written at or after the move; STANDS by the declared default.' % c
                else:
                    v, rdg = READ.get((k, i + 1, t), (None, None))
                rows.append(dict(doc=k, line=i + 1, terminal=t, by=hit, own=own, commit=c, sentence=s, verdict=v, reading=rdg,
                                 kind='code' if fence else ('table' if s.startswith('|') else ('heading' if s.startswith('#') else 'prose'))))
    second = [dict(line=i + 1, sentence=s) for i, l in enumerate(txt) for s in CP.segments(l) if re.search(SECOND[1], s)]
    return rows, second, txt


def tier_block(k):
    T = jl('terminal_table.json')
    tiers = rd('b557_tiers.txt').split(NL)
    out = []
    for t, qn, repo, pincell, rev, path in TERMS[k]:
        src = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        ln = next((i + 1 for i, l in enumerate(src) if re.match(r'^theorem %s\b' % re.escape(t), l)), None)
        end = next((j for j in range(ln - 1, min(len(src), ln + 12)) if ':=' in src[j]), ln + 3) if ln else None
        stmt = ' '.join(x.strip() for x in src[ln - 1:end + 1]).split(':=')[0].strip() if ln else None
        if t in TIER:
            tier, reason, tsrc = TIER[t]
        else:
            ti = next((i for i, l in enumerate(tiers) if re.match(r'^### :\d+ (?:[A-Za-z]+\.)?%s \[' % re.escape(t), l)
                       and _within(tiers, i, DOCS[k]['title'])), None)
            tl = next((tiers[j] for j in range(ti, ti + 7) if tiers[j].strip().startswith('tier')), '') if ti is not None else ''
            pl = next((tiers[j] for j in range(ti, ti + 7) if tiers[j].strip().startswith('profile')), '') if ti is not None else ''
            m = re.match(r'^\s*tier\s*:\s*(T[0-9][A-Za-z0-9-]*)\s*--\s*(.*)$', tl)
            tier, reason = (m.group(1), m.group(2)) if m else ('### NOT READ', tl)
            tsrc = 'data/b557_tiers.txt :%d' % (ti + 1) if ti is not None else '### NOT FOUND'
            reason = reason + ' ; profile: ' + pl.split(':', 1)[-1].strip()
        trs = _table_rows(T, t)
        out.append(dict(terminal=t, written=qn, repo=os.path.basename(repo), pin=pincell, rev=rev, path=path, line=ln, statement=stmt,
                        tier=tier, reason=reason, tier_source=tsrc,
                        table=['%s grade %s, %s, present at %s' % (r['name'], r['grade'], r['profile_state'], ','.join(r['present_at'])) for r in trs] or ['NO ROW'],
                        page=_page_hits(PAGE) if t in str(_page_hits(PAGE)) else 'not a node on either page at v0.17'))
    return out


def _within(tiers, i, title):
    for j in range(i, -1, -1):
        if tiers[j].startswith('### ') and '(phase' in tiers[j] and 'rows;' in tiers[j]:
            return tiers[j].startswith('### ' + title + ' ')
    return False


def bank(which='dry'):
    """### `bank dry` builds both banks into the scratchpad and data/b598_banks.json is NOT written; `bank SILENCE` / `bank REPARAM`
    ### writes the one file data/b558_editions/<TITLE>.txt and data/b598_bank_<k>.json."""
    keys = ORDER if which == 'dry' else (which,)
    if which not in ('dry',) + ORDER:
        sys.exit('usage: bank dry|SILENCE|REPARAM')
    for k in keys:
        d = DOCS[k]
        rows, second, txt = rows_of(k)
        bad = [(r['line'], r['terminal']) for r in rows if r['verdict'] not in ('STANDS', 'MOVED-IN-MEANING', 'CREDIT')]
        if bad:
            sys.exit('### ROWS WITHOUT ONE VERDICT: %s -- NOTHING WRITTEN' % bad)
        unused = [x for x in READ if x[0] == k and not any((r['line'], r['terminal']) == x[1:] for r in rows)]
        if unused:
            sys.exit('### READINGS WITH NO ROW: %s -- NOTHING WRITTEN' % unused)
        tb = tier_block(k)
        cnt = lambda rs: {x: sum(1 for r in rs if r['verdict'] == x) for x in ('STANDS', 'MOVED-IN-MEANING', 'CREDIT')}
        own = [r for r in rows if r['own'] == 'DOCUMENT']
        tiers = {}
        for e in tb:
            tiers[e['tier']] = tiers.get(e['tier'], 0) + 1
        head = g(PP, 'log', '-1', '--format=%h %ad', '--date=short', PRE_PP, '--', d['path']).strip()
        hist = [l.strip()[:160] for l in txt if re.match(r'^\*?\*?(v\d[\d.]*,? |Version history)', l.strip().lstrip('*'))]
        L = ['b598 -- THE TIER BLOCK AND EDITION WORK-LIST OF %s (%s) -- AN INPUT TO CP-7`S EDITION, NOT AN EDITION' % (d['title'], d['path']), '',
             '### written by the b558 form under (R208)(3): the tier block (every terminal the document cites, graded from relay '
             '`data/b557_tiers.txt` and checked against the terminal table at relay HEAD and both pages at SIDE-explicit-formula v0.17), then '
             'every sentence-row of the b558 matcher (relay `tools/b558_record.py` :330-:371: each union terminal by its name and the ferry`s '
             'four aliases, and each tier-block terminal by its name) in line order -- the line, the terminal, the sentence quoted, the '
             'verdict (STANDS / MOVED-IN-MEANING / CREDIT), what the compiled fact supports with the declaration by name and pin, and the '
             'informing work-order; then b450`s items placed. The document is read at PLACE-papers `%s`, last changed `%s`; it is not '
             'written, and b558`s pointer line is not appended to it.' % (PRE_PP, head), '',
             '### THE VERSION HISTORY, as the document carries it: ' + (' | '.join(hist) or 'none'), '',
             '## THE TIER BLOCK', '']
        for e in tb:
            L += ['`%s` -- %s %s, `%s` :%s' % (e['written'], e['repo'], e['pin'], e['path'], e['line']),
                  '    statement : %s' % e['statement'],
                  '    tier      : %s -- %s (%s)' % (e['tier'], e['reason'], e['tier_source']),
                  '    table     : %s' % ' ; '.join(e['table']),
                  '    pages     : %s' % e['page'], '']
        defs = [x for x in DEFS if x[0] == k]
        for _, n, repo, rev, path, dl in defs:
            src = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
            ln = next((i + 1 for i, l in enumerate(src) if re.match(r'^def %s\b' % n, l)), None)
            L += ['`InvarianceBarrier.%s` -- definition written out at :%d; %s %s, `%s` :%s -- `%s` -- E0 DEF, no tier (a definition is not '
                  'a terminal)' % (n, dl, os.path.basename(repo), rev, path, ln, ' '.join(x.strip() for x in src[ln - 1:ln + 1]) if ln else '?'), '']
        L += ['### rows naming no terminal (the document`s own manuscript-resident rows): %s -- T4 by b557`s block' % ', '.join(':%d' % n for n in T4ROWS[k]),
              '### ### **TIER BLOCK : %d terminals cited ; %s ; T2 majority %s.**' % (
                  len(tb), ' · '.join('%s %d' % (t, n) for t, n in sorted(tiers.items())), tiers.get('T2', 0) * 2 > len(tb)), '',
              '## THE WORK-LIST', '']
        for r in sorted(rows, key=lambda x: (x['line'], x['terminal'])):
            L += [':%d -- `%s` -- %s (%s%s)' % (r['line'], r['terminal'], r['verdict'], 'the document`s own' if r['own'] == 'DOCUMENT' else 'the cascade`s own',
                                                 ', by the alias “%s”' % r['by'][0] if r['by'][0] != r['terminal'] else ''),
                  '    the sentence: "%s"' % r['sentence'],
                  '    what the compiled fact supports: %s' % r['reading'],
                  '    informing work-order: none named on the critical path (OPEN_TRAILS :11407)%s' % (
                      '; the document`s own W-ORD-REPARAM-KERNEL (:243) bears on its manuscript-resident rows' if k == 'REPARAM' else ''), '']
        c_all, c_own = cnt(rows), cnt(own)
        L += ['### ### **WORK-LIST : %d sentence-rows (%d distinct lines) ; the document`s own %d -- STANDS %d · MOVED-IN-MEANING %d · CREDIT %d ; '
              'the cascade`s own %d, STANDS by default.**' % (len(rows), len(set(r['line'] for r in rows)), len(own), c_own['STANDS'],
                                                             c_own['MOVED-IN-MEANING'], c_own['CREDIT'], len(rows) - len(own)), '',
              '## b450`S ITEMS, LOCATED BY NAME AND PLACED', '']
        for where, quote, place in B450[k]:
            L += ['%s -- %s' % (where, quote), '    placed: %s' % place, '']
        L += ['## OBJECTS FOR THE EDITION`S OTHER CLAUSES, PRINTED FOR b599 (no work-list row; the precedence order reads them there)', '']
        for dk, lines, clause, obj in OBJECTS:
            if dk == k:
                L += ['%s -- the %s clause: %s.' % (lines, clause, obj), '']
        L += ['## THE SECOND SHAPE, PRINTED AND NOT APPLIED: “%s”' % SECOND[0], '', '### ' + SECOND_NOTE, '']
        L += [':%d -- "%s"' % (x['line'], x['sentence']) for x in second] or ['    none']
        L += ['', '### ### **SECOND SHAPE : %d segment(s).**' % len(second), '',
              '### ### **MOVED-IN-MEANING ROWS FOR THE b599 DECISION : %d.**' % c_all['MOVED-IN-MEANING']]
        J = dict(doc=k, title=d['title'], path=d['path'], head=head, tier_block=tb, tiers=tiers, rows=rows, counts=c_all, counts_own=c_own,
                 second=second, b450=B450[k], objects=[o for o in OBJECTS if o[0] == k], n_terms=len(tb), moved=c_all['MOVED-IN-MEANING'])
        if which == 'dry':
            b = put_txt('%s.txt' % d['title'], L, SP)
            print('  %s : terminals %d %s ; rows %d (own %d %s) ; second shape %d ; MOVED %d ; %d bytes' % (
                k, len(tb), tiers, len(rows), len(own), c_own, len(second), c_all['MOVED-IN-MEANING'], len(b)))
        else:
            b = put_txt('%s.txt' % d['title'], L, ED_DIR)
            J['sha256'] = sha(b)
            J['file'] = 'data/b558_editions/%s.txt' % d['title']
            put_json('b598_bank_%s.json' % k, J)
            print('  MOVED-IN-MEANING ROWS (%s) : %d' % (k, c_all['MOVED-IN-MEANING']))


# ================================================================================ THE PROMPTS, BANKED VERBATIM
def answers():
    """### every AskUserQuestion of this session, with question, options, recommended mark and the answer, read from the session
    ### transcript (b595's method); data/b598_author_answers.txt."""
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
    L = ['### b598 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat (2026-10-02), banked verbatim with the options and the '
         'recommended mark, as the standing line at OPEN_TRAILS :12246 orders.' % sum(len(c[2].get('questions', [])) for c in calls), '']
    k = 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session c36c4b1c-6feb-4e3e-9e2c-aeb65eff6769, transcript line %d)' % (cid, i))
        for q in inp.get('questions', []):
            k += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'), op.get('description')))
        ri, rt = results.get(cid, (None, '### NO RESULT FOUND'))
        L += ['RESULT (transcript line %s): %s' % (ri, rt), '']
    if not calls:
        L.append('### NO PROMPT WAS PUT: the precedence order and the ruling`s letter reached every reading of this act.')
    put_txt('b598_author_answers.txt', L)


# ================================================================================ COMPONENT 3: THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
BANK_FILES = {k: 'data/b558_editions/%s.txt' % DOCS[k]['title'] for k in ORDER}


def _bank_commits():
    out = {}
    for k in ORDER:
        out[k] = [l for l in g(RELAY, 'log', '--format=%h', PRE_RELAY + '..HEAD', '--', BANK_FILES[k]).split(NL) if l.strip()]
    return out


def scores():
    J = {k: jl('b598_bank_%s.json' % k) for k in ORDER}
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
                                                                               'SIDE-structural-error-correction', 'SIDE-cosmo')}
    kern_ok = kern == {'SIDE-explicit-formula': '5a1630b', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068',
                       'SIDE-structural-error-correction': '6a4f482', 'SIDE-cosmo': 'c5cba30'}
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b598_') and not os.path.basename(x).startswith('terminal_table')
                              and x not in BANK_FILES.values() and x != 'data/b597_closing_push_out.txt'))
    bc = _bank_commits()
    alone = {k: (len(bc[k]) == 1 and g(RELAY, 'show', '--name-only', '--format=', bc[k][0]).split() == [BANK_FILES[k]]) for k in ORDER}
    nt = {k: J[k]['n_terms'] for k in ORDER}
    t2maj = {k: J[k]['tiers'].get('T2', 0) * 2 > J[k]['n_terms'] for k in ORDER}
    moved = sum(J[k]['moved'] for k in ORDER)
    later = {k: [r for r in J[k]['rows'] if r['verdict'] == 'MOVED-IN-MEANING' and ('v0.17' in (r['reading'] or ''))] for k in ORDER}
    b450_named = {k: [x for x in J[k]['b450'] if not x[2].startswith('NO ITEM') and 'b450_components' in x[0]] for k in ORDER}
    table_dealign = [e for e in J['SILENCE']['tier_block'] if e['terminal'] in DOCS['SILENCE']['own'][:6] and e['table'] != ['NO ROW']]
    on_page = [e['terminal'] for k in ORDER for e in J[k]['tier_block'] if not e['page'].startswith('not a node')]
    S = dict(
        N1=('HELD' if all(nt[k] >= 10 and t2maj[k] for k in ORDER) else 'REFUTED',
            'terminals cited: SILENCE_STAGES_DEALIGNMENT %d, REPARAMETERIZATION_BARRIERS %d (at least 10 each wanted) ; T2 majority: %s' % (
                nt['SILENCE'], nt['REPARAM'], t2maj)),
        N2=('HELD' if moved <= 20 else 'REFUTED', 'MOVED-IN-MEANING rows across the two work-lists: %d (at most 20 wanted)' % moved),
        N3=('HELD' if all(later[k] for k in ORDER) else 'REFUTED',
            'MOVED rows citing a declaration at v0.17 or later than the document`s last pin: SILENCE %d of %d (its one row cites '
            'knill_laflamme_t1 at SIDE-cosmo c5cba30, the pin the row itself carries), REPARAM %d of %d' % (
                len(later['SILENCE']), J['SILENCE']['moved'], len(later['REPARAM']), J['REPARAM']['moved'])),
        N4=('HELD' if all(b450_named[k] for k in ORDER) else 'REFUTED',
            'b450 items located by name: SILENCE %d (b450 names the document RECONCILED by b394, no item), REPARAM %d' % (
                len(b450_named['SILENCE']), len(b450_named['REPARAM']))),
        N5=('HELD' if kern_ok and 'FINDINGS.md' in pp_ch and set(pp_ch) <= {'FINDINGS.md', 'OPEN_TRAILS.md'} and relay_beyond == [] else 'REFUTED',
            'nothing deposits; kernel mains %s; PLACE-papers files changed %s, with OPEN_TRAILS.md the trail record`s pending append after '
            'these scores (no current version); relay files beyond the act`s own banks, the two work-lists and the table: %s' % (
                'unmoved' if kern_ok else kern, pp_ch, relay_beyond or 'none')),
        S1=('HELD' if nt['SILENCE'] + nt['REPARAM'] == 11 and all(J[k]['tiers'] == {'T2': nt[k]} for k in ORDER) else 'REFUTED',
            'terminals cited %d, tiers %s' % (nt['SILENCE'] + nt['REPARAM'], {k: J[k]['tiers'] for k in ORDER})),
        S2=('HELD' if moved == 1 and sum(J[k]['counts']['CREDIT'] for k in ORDER) == 0 else 'REFUTED',
            'MOVED-IN-MEANING %d, CREDIT %d' % (moved, sum(J[k]['counts']['CREDIT'] for k in ORDER))),
        S3=('HELD' if not table_dealign and not on_page else 'REFUTED',
            'DeAlignment terminals with a table row: %d ; cited terminals on a page at v0.17: %s' % (len(table_dealign), on_page or 'none')),
        S4=('HELD' if len(J['SILENCE']['second']) == 5 and len(J['REPARAM']['second']) == 0 else 'REFUTED',
            'second-shape segments: SILENCE %d, REPARAM %d' % (len(J['SILENCE']['second']), len(J['REPARAM']['second']))),
        S5=('HELD' if all(alone.values()) else 'REFUTED', 'each bank committed alone: %s (%s)' % (alone, bc)),
    )
    put_json('b598_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-4s %s -- %s' % (k, S[k][0], S[k][1][:220]))


TITLE = ('## CP-1b: the tier blocks and work-lists of SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION_BARRIERS from b557’s tiers, the '
         'terminal table and the pages at v0.17 -- one row moved in meaning, at the Knill–Laflamme row')
TRAIL_HEAD = ('### b598 — lane three, act twenty-five under (R208): CP-1b -- the tier blocks and work-lists of SILENCE_STAGES_DEALIGNMENT '
              'and REPARAMETERIZATION by the b558 form')


def findings():
    Q = _Q()
    S, wl = jl('b598_scores.json'), jl('b598_weight_line.json')
    J = {k: jl('b598_bank_%s.json' % k) for k in ORDER}
    bc = _bank_commits()
    Q.guard_absent(Q.FIND, TITLE[:90])
    s, r = J['SILENCE'], J['REPARAM']
    e = ['', TITLE, '',
         '*Filed at b598 on the author’s ruling `(R208)`. Banks: relay `%s` (%s), `%s` (%s), `data/b598_reads.txt`, '
         '`data/b598_bank_SILENCE.json`, `data/b598_bank_REPARAM.json`. Nothing deposits; no document written.*' % (
             BANK_FILES['SILENCE'], bc['SILENCE'][0] if bc['SILENCE'] else '?', BANK_FILES['REPARAM'], bc['REPARAM'][0] if bc['REPARAM'] else '?'), '',
         '**The tier blocks** (`(R208)`(3), by the b558 form): SILENCE_STAGES_DEALIGNMENT cites %d terminals -- six of '
         'SIDE-structural-error-correction’s de-alignment theorems at v0.2.1 = 6a4f482, two of SIDE-cosmo’s Steane theorems at c5cba30, and '
         'conservation_of_spectra by the b558 alias at :109 -- all T2 by b557’s tier bank; REPARAMETERIZATION_BARRIERS cites %d, the two '
         'invariance-barrier schemata at SIDE-kernel 5e668b4, both T2, and writes out the two definitions they use. The terminal table at '
         'relay HEAD carries no row for any of the six de-alignment theorems (their kernel prints no axioms into an artefact and no ledger '
         'grades them), the Steane and barrier rows UNGRADED; no cited terminal is a node of either page at v0.17.' % (s['n_terms'], r['n_terms']), '',
         '**The work-lists.** SILENCE_STAGES_DEALIGNMENT: %d sentence-rows, the document’s own %d -- STANDS %d, MOVED-IN-MEANING %d, CREDIT '
         '%d; the moved row is §9’s :209, whose claim cell names the Knill–Laflamme error-correction conditions while knill_laflamme_t1 '
         'states that the parity map’s seven columns are nonzero and distinct, the t = 1 syndrome condition, its equivalence with '
         'correctability carried by the docstring. REPARAMETERIZATION_BARRIERS: %d rows, the document’s own %d, all STANDS -- the schema '
         'the note writes out is the compiled one, byte-identical at its pin, v1.7 and SIDE-kernel main. Five sentences of the first '
         'document meet the Silence Principle by name, which the form’s matcher does not read; they are printed and not graded, for the '
         'author’s ruling on the alias.' % (len(s['rows']), len(s['rows']) - (len(s['rows']) - sum(1 for x in s['rows'] if x['own'] == 'DOCUMENT')),
                                             s['counts_own']['STANDS'], s['counts_own']['MOVED-IN-MEANING'], s['counts_own']['CREDIT'],
                                             len(r['rows']), sum(1 for x in r['rows'] if x['own'] == 'DOCUMENT')), '',
         '**b450’s items.** REPARAMETERIZATION_BARRIERS’ “does not carry: the two-kinds windows verdict” is carried since b454 (its era '
         'annotation, PLACE-papers b4b0be2), so no credit line is owed. b450 names SILENCE_STAGES_DEALIGNMENT only as reconciled by b394, '
         'and b394’s reading behind that mark (OPEN_TRAILS :4540, relay data/b394_components.txt :79) says the document carries no '
         'correspondence table, while the blob b394 read (PLACE-papers 4cd1cd2) carries §9 at :196 with ten rows; its one record item is '
         'the registry row of another document, Dark Interface. Both correct the record’s claim about the document, not the document.', '',
         '**For the edition.** One MOVED row in all: by `(R208)`(3) the two editions follow at b599 in one act. The banks also print the '
         'objects the fact and restatement clauses will read there -- the “no terminal” rows of §9 beside d_eff_formula and '
         'silence_yields_protection, which restate their own definitions; the Steane names written with a namespace the file does not '
         'open; the “CURRENT kernel pin” of the barrier note, now SIDE-kernel main 0256e9e with the file unchanged.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b557’s tier blocks (:5870), carried at their grades, and '
         'extends b558’s CP-1b (:5990) by its own matcher to the two keystones (R208) names among the five it left without work-lists '
         '(relay data/b558_editions.json, “none”; FACES_LEDGER, THE_IDENTITY_CHAIN and THE_KEYSTONE_CENSUS still have none), nineteen '
         'work-lists now in relay data/b558_editions/; it re-reads b394’s and b450’s reconciliation of SILENCE_STAGES_DEALIGNMENT and '
         'finds the table b394 said was absent; it is re-read by b599’s two editions. It strengthens two of the programme’s offerings: '
         'the CP-1b work-lists as the editions’ input, now covering both held keystones, and the de-alignment condition’s compiled scope, '
         'every row of which stands.', '',
         '**The record lines.** b597’s weight at FINDINGS :%d; the strike items as ruled at :%d.' % (wl['lines'][0]['line'], wl['lines'][1]['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R208)`(4): b599, the editions of SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION_BARRIERS in one act by the '
         'form, their work-lists carrying one MOVED row together; then the research sequence from REMAINDER 5. The author rules on the '
         'closing.', '',
         '*Nothing deposits; no kernel written; neither document written; README, REGISTRY and ERRATA unwritten; nothing here is a '
         'statement about RH or any zero beyond the compiled statements’ own words.*', '']
    rr = Q.append_to(Q.FIND, NL.join(e))
    put_json('b598_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE[:90]), title=TITLE, append=rr))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, TITLE[:90]))


def trail():
    Q = _Q()
    S, fj, wl = jl('b598_scores.json'), jl('b598_findings.json'), jl('b598_weight_line.json')
    bc = _bank_commits()
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R208) ratified.** (1) b597 at its weight. (2) The strike items, as ruled. (3) CP-1b over SILENCE_STAGES_DEALIGNMENT and '
             'REPARAMETERIZATION by the b558 form, no edition written. (4) The act after: b599.', '',
             '**Entered:** FINDINGS.md:%d (b597’s weight), :%d (the strike items), :%d (the entry, with its mutual-light line); this record; '
             'relay `%s` (%s) and `%s` (%s), each committed alone.' % (
                 wl['lines'][0]['line'], wl['lines'][1]['line'], fj['entry_line'], BANK_FILES['SILENCE'], bc['SILENCE'][0] if bc['SILENCE'] else '?',
                 BANK_FILES['REPARAM'], bc['REPARAM'][0] if bc['REPARAM'] else '?'), '',
             '**Printed for the author’s ruling, not graded:** five sentences of SILENCE_STAGES_DEALIGNMENT naming the Silence Principle, '
             'which the b558 matcher’s aliases do not reach; b394’s “no correspondence table” for that document, contradicted by its §9.', '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R208)`(4), b599, the editions of SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION_BARRIERS in one act (one '
             'MOVED row between the two work-lists); then the research sequence from REMAINDER 5; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel written; neither document written; ERRATA untouched; FACES_LEDGER '
             'untouched; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b598_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b598_trail.json')['line'])


def desk():
    S = jl('b598_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b598 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '']
    L += ['### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b598_defects.txt').rstrip(NL).split(NL)
    put_txt('b598_desk_notes.txt', L)


def components():
    S, fj, tj, wl = jl('b598_scores.json'), jl('b598_findings.json'), jl('b598_trail.json'), jl('b598_weight_line.json')
    J = {k: jl('b598_bank_%s.json' % k) for k in ORDER}
    bc = _bank_commits()
    L = ['b598 -- THE COMPONENTS, BANKED UNDER (R208).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b597`s closing push-out relay %s ; push-b597* branches deleted by name '
         '(data/b598_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b598_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b597`s weight FINDINGS :%d ; the strike items as ruled :%d' % (wl['lines'][0]['line'], wl['lines'][1]['line']),
         '### COMPONENT 2 : %s (sha256 %s, relay %s) : terminals %d, rows %d, MOVED %d ; %s (sha256 %s, relay %s) : terminals %d, rows %d, MOVED %d ; '
         'MOVED-IN-MEANING ROWS FOR THE b599 DECISION : %d' % (
             BANK_FILES['SILENCE'], J['SILENCE']['sha256'][:16], ','.join(bc['SILENCE']), J['SILENCE']['n_terms'], len(J['SILENCE']['rows']), J['SILENCE']['moved'],
             BANK_FILES['REPARAM'], J['REPARAM']['sha256'][:16], ','.join(bc['REPARAM']), J['REPARAM']['n_terms'], len(J['REPARAM']['rows']), J['REPARAM']['moved'],
             J['SILENCE']['moved'] + J['REPARAM']['moved']),
         '### COMPONENT 3 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b599, the two editions in one act ; N1 %s, N2 %s, '
         'N3 %s, N4 %s, N5 %s' % (fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b598_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b598_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
