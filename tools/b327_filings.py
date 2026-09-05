# -*- coding: utf-8 -*-
"""b327_filings.py -- FOUR APPEND-ONLY BLOCKS IN PLACE-papers, GENERATED FROM THE ACT'S OWN RECORDS.

### ### **THE BLOCKS:** ### (1) `FINDINGS.md` -- the stable anchor `faces-ledger`, a pointer and what the
### ledger is not; ### (2) `VERIFICATION_LOOM.md` -- the dated entry recording the ledger's law; ### (3)
### `EMERGING_RESEARCH_PROGRAMMES.md` -- the two notes, as CONTACTS and not seeds; ### (4) `OPEN_TRAILS.md`
### -- the three owed bridges by ID. ### **NOTHING ELSE IS WRITTEN. ### NO DEPOSITED TEXT IS TOUCHED.**
### ### **THE VERDICT WORDS AND COUNTS ARE READ FROM `b327_bridge.json` AND `b327_notes.json`**, never
### typed from memory of the run. ### Each block is idempotent under its own marker, append-only against
### the working file AND the blob at `HEAD`, and two paths write two differently named run files.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEPOSIT_DIR = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def blocks():
    b = json.load(io.open(os.path.join(D, 'b327_bridge.json'), encoding='utf-8'))
    n = json.load(io.open(os.path.join(D, 'b327_notes.json'), encoding='utf-8'))
    q1, q2 = b['q1'], b['q2']
    ifsame = 'fires' if b['if_same_fires'] else 'does not fire'
    pts, lns = n['points'], n['lines']
    asst = 'as the order stated' if n['as_stated'] else 'NOT as the order stated -- the measured counts are filed'
    out = {}
    out['FINDINGS.md'] = ('<!-- b327 faces-ledger anchor -->', [
        '',
        '<!-- b327 faces-ledger anchor -->',
        '',
        '## THE FACES LEDGER — b327 *(filed 2026-09-05; a cross-reference instrument — it certifies nothing)*',
        '',
        '### the-faces-ledger',
        '<a id="faces-ledger"></a>*Stable anchor: `faces-ledger` · tag: synthesis-suggested (a ledger pointer); each row carries its owner\'s grade and no other\'s*',
        '',
        '**`FACES_LEDGER.md`, at the papers root**, is the ledger of every equivalence or face the corpus has met: the pentagon\'s five faces as the deposit states them, the finite-instance identity, the Sonin margin, the Li margin, the spectral-realization wall, the fixed-point silence, the two-radius family, the Epstein negative control at b326\'s result, and one live row — the Li-to-Weil bridge. Every row quotes its claim from the file that emits it (verified by the row-writer before writing), grades it as PROVED / MEASURED / IMPORTED / NAMED-ONLY, names the correspondence rows it touches, and types the bridges it owes. Its cascade section states, for every pair of rows, a relation the record already states (quoted), a bridge owed (typed, with a trail ID), or NONE.',
        '',
        '**What it is not.** It compiles no equivalence — the deposit\'s refusal (section 27.3, *"deliberately **not** compiling the cross-register equivalences"*) is quoted in its head and governs it. No face is promoted by its neighbours. It moves no grade.',
        '',
        '**The live row, as b327 read it under the import bar** (source: Lagarias, *Li coefficients for automorphic L-functions*, arXiv:math/0404394v4, pinned by hash; restating Bombieri–Lagarias 1999): the deposit\'s archimedean channel of the Li coefficient against the archimedean place on the Li family — **%s**; the Li margin and the Sonin margin as one functional on two families — **%s**. One distribution on two families, not one functional. The order\'s *if SAME* branch %s.' % (q1, q2, ifsame),
        '',
        '**The owed bridges, on the trails by ID:** `W-ORD-LI-WEIL-BRIDGE`, `W-ORD-DISCRIMINATING-FAMILY`, `W-ORD-LI-FAMILY-CONTROL`.',
        '',
        '### **h2 UNCHANGED. NOTHING PROMOTED. NOTHING DEPOSITS.**',
    ])
    out['VERIFICATION_LOOM.md'] = ('<!-- b327 loom entry -->', [
        '',
        '<!-- b327 loom entry -->',
        '',
        '### **THE FACES LEDGER\'S LAW — filed 2026-09-05 (b327)**',
        '',
        '`FACES_LEDGER.md` was built at the papers root as a cross-reference instrument (author-authorized 2026-09-04). **Its law, recorded here:** rows enter only through `relay/tools/b327_faces_row.py`, which refuses a duplicate id, refuses a cell with an unescaped pipe or a blank, refuses a struck clause or a banned stem, **verifies every quoted fragment against the file it names before writing**, and reads the file back after every write; the file is append-only against the working copy and the blob at `HEAD`; every pair of rows carries one of STATED / OWED / NONE and no pair is absent. ### **The ledger certifies nothing** — its class line is ROUTED, as the sibling ledgers\' are, and every row\'s grade is its owning act\'s. Registration `relay/data/b327_registration_2026-09-05.txt`, sealed before any instrument ran; the guard that fired during the seeding (a mis-typed pin fragment on the R4 row, refused, corrected, the row appended after F7) is on the record in `relay/data/b327_ledger_run.txt` and `_run2.txt`.',
        '',
        '*The bridge read (the live row): %s on the archimedean channel; %s on the two margins. Owed: `W-ORD-LI-WEIL-BRIDGE`, `W-ORD-DISCRIMINATING-FAMILY`, `W-ORD-LI-FAMILY-CONTROL`. Nothing deposits.*' % (q1, q2),
    ])
    out['EMERGING_RESEARCH_PROGRAMMES.md'] = ('<!-- b327 contacts -->', [
        '',
        '<!-- b327 contacts -->',
        '',
        '---',
        '',
        '## Contacts — filed 2026-09-05 (b327) *(not seeds: no promotion criterion is set; a contact carries anchors, one consequence, and no claim)*',
        '',
        '*Provenance of both: the navigator\'s conversation layer, 2026-09-04, ratified by the b327 ferry. Filed here and nowhere research-facing.*',
        '',
        '### Contact A — The Curie reading of the eigenvalue-one boundary',
        '',
        'The corpus\'s archimedean remainder is a mode sum whose weights are `lam_n^2/(1-lam_n^2)`, and the object\'s space `S(1,1)` is the eigenvalue-one eigenspace of the source\'s operator (b288: *"THE INSTRUMENTS\' WEIGHTS DIVERGE PRECISELY AS ONE APPROACHES THE OBJECT\'S SPACE"* — *"A JUXTAPOSITION, ROUTED, NOT COMPUTED"*, `W-ORD-WEIGHT-AT-EIGENVALUE-ONE`). The contact reads that divergence as a **susceptibility**: the remainder\'s weight diverging at the boundary the way a response function diverges at a critical point.',
        '- **Anchors:** relay `data/b288_the_family_and_the_complement.txt` (the weight, the eigenspace, the routing); b319\'s eigenvalue-one cut (`FINDINGS.md`, the archimedean instrument arc); b312\'s read of the source\'s Lemma 5.4 (the jump in the remainder\'s derivative at the identity).',
        '- **The one consequence:** sensitivity of the remainder to test-function perturbation near the boundary — *checkable on the instrument, not checked here.*',
        '- **No claim.** Nothing is computed; no limit is taken; the juxtaposition stays routed where b288 left it.',
        '',
        '### Contact B — The cubit reading of the 256 rules',
        '',
        'Each of the 256 elementary cellular-automaton rules is a function on `(Z/2)^3` — the corpus\'s cubit — and a rule with `000 → 0` has its one-set inside the Fano plane\'s seven points. Rule 110\'s one-set is a **%d-point** Fano subset containing **%d** of the seven lines (counted by `relay/tools/b327_notes.py`, %s; the two lines are `{001, 010, 011}` and `{011, 101, 110}`).' % (pts, lns, asst),
        '- **Anchors:** the balance keystone\'s Fano line (*"the Fano incidence is provably dark to all second-order statistics"*); the cubit `(Z/2)^3` and its Fano incidence (`FINDINGS.md`, the class-number-anomaly entry; the Trivium fields as Fano points).',
        '- **The one question, not answered here:** *which Fano subsets define universal rules.*',
        '- **No claim.** A count is filed; nothing about universality, the cubit, or any structure follows from it here.',
    ])
    out['OPEN_TRAILS.md'] = ('<!-- b327 owed bridges -->', [
        '',
        '<!-- b327 owed bridges -->',
        '',
        '---',
        '',
        '## THE FACES LEDGER\'S OWED BRIDGES — **THREE TRAILS, BY ID** *(filed 2026-09-05, b327; cross-filed from `FACES_LEDGER.md`, its cascade section)*',
        '',
        '| | trail | species | what is owed | price, as the record states it | trigger |',
        '|:--|:--|:--|:--|:--|:--|',
        '| **1** | `W-ORD-LI-WEIL-BRIDGE` | **RESULT or RULING** | b324\'s bridging statement, given its ID here: *a formula carrying the archimedean margin `W_infinity(f) - Tr(theta(f) S)` at a lawful test function to the Li margin `lambda_n` at an index `n`, or a proof that no such formula exists.* Sharpened by b327\'s read: the archimedean distribution is one on both families (the deposit\'s channel is the archimedean place plus the pole constant, %s); what is owed is a relation between the compressed square on the Sonin family and the finite-place channel on the Li family, or its impossibility. | unpriced; b324 filed it as the arc\'s most valuable open item | none |' % q1,
        '| **2** | `W-ORD-DISCRIMINATING-FAMILY` | **CONSTRUCTION** | the family that would let the instrument say no on the Epstein function: a lawful seed whose transform changes sign across `beta` and `1 - beta`, so that the off-line four-term sums on `g conv g^#` need not come out positive (b326, Component 4). | priced at b326 at one act, not built | none |',
        '| **3** | `W-ORD-LI-FAMILY-CONTROL` | **CONTROL** | the explicit formula closed on the Li family through the corpus\'s own channels: the zero side over the atlas\'s 10000 ordinates against `S_inf(n) - S_f(n) + 1`, with `S_inf` by a third route (the atlas\'s kernel against `G_n` on the line); its conditionally convergent `u`-tail and the `O(n log T / T)` zero tail bounded and registered first. | priced at b327 at one act, not run | none |',
        '',
        '*Nothing here is a route. No grade moves. h2 stands exactly where the deposit left it.*',
    ])
    return out


def main():
    fails = []
    rec('=' * 100)
    rec('b327 -- THE FILINGS. ### FOUR APPEND-ONLY BLOCKS, GENERATED FROM THE RECORDS.')
    rec('=' * 100)
    st0 = subprocess.run(['git', '-C', PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2'], capture_output=True, text=True).stdout.strip()
    rec('  git status over outputs/DEPOSITED-v1.1.2 BEFORE : %r' % st0)
    for rel, (mark, blk) in blocks().items():
        target = os.path.join(PP, rel)
        inside = os.path.abspath(target).startswith(os.path.abspath(DEPOSIT_DIR))
        if inside:
            rec('  ### REFUSING %s -- under the deposit path' % rel)
            fails.append(rel)
            continue
        before = io.open(target, encoding='utf-8', errors='replace').read()
        blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + rel], capture_output=True).stdout.decode('utf-8', 'replace')
        if mark in before:
            rec('  %-34s ALREADY FILED, nothing written (idempotent); block once : %s ; blob still a TRUE PREFIX : %s'
                % (rel, before.count(mark) == 1, before.replace('\r\n', '\n').startswith(blob.replace('\r\n', '\n').rstrip('\n'))))
            continue
        new = before.rstrip('\n') + '\n' + '\n'.join(blk) + '\n'
        open(target + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(target + '.tmp', target)
        after = io.open(target, encoding='utf-8', errors='replace').read()
        pw = after.startswith(before.rstrip('\n'))
        pb = after.replace('\r\n', '\n').startswith(blob.replace('\r\n', '\n').rstrip('\n'))
        rec('  %-34s WRITTEN +%d lines ; pre-append working file a TRUE PREFIX : %s ; blob at HEAD a TRUE PREFIX : %s ; block once : %s'
            % (rel, len(after.splitlines()) - len(before.splitlines()), pw, pb, after.count(mark) == 1))
        if not (pw and pb and after.count(mark) == 1):
            fails.append(rel)
    st1 = subprocess.run(['git', '-C', PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2'], capture_output=True, text=True).stdout.strip()
    rec('  git status over outputs/DEPOSITED-v1.1.2 AFTER  : %r ; ### THE DEPOSIT IS BYTE-UNCHANGED : %s' % (st1, not st1))
    if st1:
        fails.append('DEPOSIT MOVED')
    rec('=' * 100)
    rec('  ### FILING CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    wrote = any('WRITTEN' in x for x in LINES)
    name = 'b327_filings_run.txt' if wrote else 'b327_filings_rerun.txt'
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
