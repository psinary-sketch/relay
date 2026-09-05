# -*- coding: utf-8 -*-
"""b328_filings.py -- TWO APPEND-ONLY BLOCKS IN PLACE-papers, GENERATED FROM THE ACT'S OWN RECORDS.

### ### (1) `FACES_LEDGER.md` -- an UPDATE block naming row F7 and the pair F1-F7, written through the
### writer's `append_block` (b327_faces_row.py): the Epstein row's owed bridge `W-ORD-DISCRIMINATING-FAMILY`
### with its status as this act measured it; the rows above are never rewritten.
### ### (2) `OPEN_TRAILS.md` -- the trail's status block.
### ### **THE VERDICT WORDS AND NUMBERS ARE READ FROM `b328_family.json`, `b328_build.json` AND
### `b328_derive.json`**, never typed from memory of the run. ### Two paths, two run files.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEPOSIT_DIR = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def texts():
    fam = json.load(io.open(os.path.join(D, 'b328_family.json'), encoding='utf-8'))
    bld = json.load(io.open(os.path.join(D, 'b328_build.json'), encoding='utf-8'))
    der = json.load(io.open(os.path.join(D, 'b328_derive.json'), encoding='utf-8'))
    verdict = fam['verdict']
    e = [x for x in bld if x['kind'] == 'E']
    o = [x for x in bld if x['kind'] == 'O']
    ph_e = ', '.join('%.2f' % x['transform']['phase_deg'] for x in e)
    ph_o = ', '.join('%.3f' % x['transform']['phase_deg'] for x in o)
    cells = {(c['kind'], c['a']): c for c in fam['cells']}
    def sgn(c):
        return c['gate_q']['sign'], c['gate_z']['sign']
    tab = '; '.join('%s%g: Q %s (%+.3e), zeta %s (%+.3e), Q closes %s, zeta closes %s'
                    % (k, a, sgn(c)[0], c['channels']['places_q'], sgn(c)[1], c['channels']['places_z'],
                       c['closure']['status_q_all'], c['closure']['status_z'])
                    for (k, a), c in sorted(cells.items()))
    if verdict == 'SEES IT':
        status = 'PARTLY PAID -- the construction exists and the control ran to SEES IT at %s; what remains owed is the bridge to the arc\'s family (b326\'s verdict there stands) and the entailment\'s scope: this family, this instrument, this reach.' % fam['sees']
        trail_status = 'PARTLY PAID (b328)'
    elif verdict == 'ZETA FLIPS':
        status = 'NOT PAID -- the control returned a zeta flip at %s, reported as a defect in the chain and walked in the b328 bank; nothing about the family is claimed until the chain is cleared.' % fam['flips']
        trail_status = 'OPEN -- zeta flip under investigation (b328)'
    else:
        status = 'NOT PAID -- the construction exists and the control returned %s; the reason is named from the numbers in the b328 bank.' % verdict
        trail_status = 'OPEN -- construction built, control %s (b328)' % verdict
    faces = [
        '', '<!-- b328 update -->', '',
        '## UPDATE — filed 2026-09-05 (b328): row F7 and the pair F1–F7',
        '',
        '*Rows above are never rewritten; an update names the row it bears on. Written through the writer\'s `append_block`.*',
        '',
        '| row / pair | what b328 measured | the owed bridge, its status |',
        '|:--|:--|:--|',
        '| **F7** (the Epstein negative control) and **F1–F7** | THE CONDITION DERIVED (registration sealed before any run): for f = g ⋆ g♯ the four-term sum at an off-line quadruple is 4 Re[G(c)G(−c)]; for an even seed 4 ‖G‖² cos 2φ, negative only past 45° of phase; an odd component contributes −4 Re G_o², negative only below it. Checked against b326\'s banked four terms at the thirteen arc cells (their phases %.2f° to %.2f°, all below the threshold, every sign the banked sign). TWO SEEDS BUILT, both lawful at every width (Definition 3.1 scan; the pole conditions g̃(0) = g̃(1) = 0 measured): the sine-aimed even seed at phases %s° and the cosine-aimed odd seed at %s° (widths a = 20, 40, 81, 160). THE CONTROL: %s. **VERDICT: %s.** | `W-ORD-DISCRIMINATING-FAMILY` — %s |'
        % (min(der['B3']['phases']), max(der['B3']['phases']), ph_e, ph_o, tab, verdict, status),
        '',
        '*Nothing about totality, h2, or the roster. b326\'s DOES NOT SEE IT on the arc\'s family stands. Filed by b328 (relay `data/b328_the_discriminating_family.txt`).*',
    ]
    trails = [
        '', '<!-- b328 trail update -->', '',
        '### **`W-ORD-DISCRIMINATING-FAMILY` — UPDATED 2026-09-05 (b328): %s**' % trail_status,
        '',
        'The construction b326 priced was built at b328 as two seeds aimed at the Epstein function\'s first off-line zero (β = 0.953260, γ = 16.290216): a sine-aimed even seed (phase %s° at the zero, widths a = 20, 40, 81, 160) and a cosine-aimed odd seed (phase %s°), each lawful under the source\'s Definition 3.1 with the pole conditions the criterion requires measured to vanish. The control ran on both functions with both libraries (146 on-line and 17 off-line Epstein zeros; ζ\'s 10000 ordinates), the places sides computed with no zero: **%s** (%s). %s'
        % (ph_e, ph_o, verdict, tab, status),
        '',
        '*Species unchanged (CONSTRUCTION); trigger none; nothing deposits; h2 stands exactly where the deposit left it.*',
    ]
    return faces, trails, verdict


def main():
    fails = []
    rec('=' * 100)
    rec('b328 -- THE FILINGS. ### THE LEDGER UPDATE THROUGH THE WRITER; THE TRAIL UPDATE.')
    rec('=' * 100)
    faces, trails, verdict = texts()
    rec('  verdict read from the record : %s' % verdict)
    st, det = W.append_block('<!-- b328 update -->', faces)
    rec('  FACES_LEDGER.md   %-16s %s' % (st, det))
    if st not in ('WRITTEN', 'DUPLICATE'):
        fails.append('FACES_LEDGER')
    rel = 'OPEN_TRAILS.md'
    target = os.path.join(PP, rel)
    before = io.open(target, encoding='utf-8', errors='replace').read()
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + rel], capture_output=True).stdout.decode('utf-8', 'replace')
    mark = '<!-- b328 trail update -->'
    if mark in before:
        rec('  %-18s ALREADY FILED, nothing written (idempotent); block once : %s' % (rel, before.count(mark) == 1))
    else:
        new = before.rstrip('\n') + '\n' + '\n'.join(trails) + '\n'
        open(target + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(target + '.tmp', target)
        after = io.open(target, encoding='utf-8', errors='replace').read()
        pw = after.startswith(before.rstrip('\n'))
        pb = after.replace('\r\n', '\n').startswith(blob.replace('\r\n', '\n').rstrip('\n'))
        rec('  %-18s WRITTEN +%d lines ; working TRUE PREFIX %s ; blob TRUE PREFIX %s ; once %s' % (rel, len(after.splitlines()) - len(before.splitlines()), pw, pb, after.count(mark) == 1))
        if not (pw and pb):
            fails.append(rel)
    st2 = subprocess.run(['git', '-C', PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2'], capture_output=True, text=True).stdout.strip()
    rec('  git status over outputs/DEPOSITED-v1.1.2 : %r ; THE DEPOSIT IS BYTE-UNCHANGED : %s' % (st2, not st2))
    if st2:
        fails.append('DEPOSIT')
    rec('  ### FILING CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    wrote = any('WRITTEN' in x for x in LINES)
    # ### numbered like b327's writer: a second WRITING run (this act had one -- the ledger block was refused
    # ### on the first pass and written on the second) must not overwrite the first run's record. The
    # ### first pass of this act WAS overwritten before this line existed; declared in the bank.
    base = 'b328_filings_run' if wrote else 'b328_filings_rerun'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
