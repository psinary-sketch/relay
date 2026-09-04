# -*- coding: utf-8 -*-
"""b324_extract.py -- THE EXTRACT STEP. ### **THE CANONICAL DRIVE, NEVER THE PROJECT MIRROR.**

### ### **THE READING RULE THIS ACT RUNS UNDER, AND WHY IT IS SHARPER THAN USUAL.**
### The order forbids resemblance as evidence ### **BY NAME**: *shared words ("space", "wall",
### "margin", "room", "silence") decide nothing.* ### An act comparing a deposited corpus with a
### computational arc is exactly the act that would otherwise find agreement everywhere, because
### both write English about the same subject.
### ### **SO EVERY QUOTATION IS PULLED FROM THE EMITTING FILE WITH ITS LINE NUMBER**, and the
### comparison in the bank is made ### **CONSTITUENT BY CONSTITUENT AGAINST DEFINITIONS**, never
### between two sentences that sound alike.

### ### ### **AND THE PROVENANCE SPLIT THIS FILE EXISTS TO MAKE VISIBLE.**
### ### **THE DEPOSIT IS MS v5.10.2. ### THE RESIDUE KEYSTONE AND THE INTERNAL MONOGRAPH ARE
### ### v5.13.** ### `REGISTRY.md` d1-1 records the local canonical copy at
### `outputs/DEPOSITED-v1.1.2/`, *"fetched read-only and verified byte-level -- every file's md5
### matched Zenodo's published checksum"*, and records the internal line separately.
### ### **SO A SENTENCE FOUND IN `day1/` IS NOT THEREBY A DEPOSITED SENTENCE**, and this file reads
### the two paths separately and counts each phrase in both, so that the bank can type a contact as
### REFINEMENT-OF-DEPOSITED only when the claim it refines is actually in the deposit.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b324_extract_notes.txt')

DEPOSIT = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
INTERNAL = os.path.join(PP, 'day1')

# ### **THE TWO KEYSTONES THE PRECISE QUESTIONS TURN ON.** ### Both INTERNAL, and the file says so.
RESIDUE = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
BALANCE = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')

# ### **THE DEPOSITED SUPPORT TEXTS, AT THE VERIFIED LOCAL DEPOSIT COPY.**
SUPPORT = [
    ('the silence keystone', 'Silence_of_Foundations.md'),
    ('the confinement keystone', 'Which_Structure_Confines.md'),
    ('the third identity element', 'Third_Identity_Element.md'),
    ('spectral inertness', 'Spectral_Inertness.md'),
    ('the seven classes', 'Seven_Mechanism_Classes.md'),
    ('exhaustive enumeration', 'Exhaustive_Enumeration.md'),
    ('the monograph', 'A_Place_to_Stand.md'),
]

# ### (label, file, fragment) -- pulled with the WHOLE LINE and its number.
WANTED = [
    # ### ---- COMPONENT 1: THE WALL, at the residue keystone
    ('the wall, stated', RESIDUE, 'The space is the wall'),
    ('### the object the two eras cross at', RESIDUE, 'the positive space on the zeros'),
    ("### the space's existence as the open clause", RESIDUE, "the space's existence *is* the open"),
    ('### the standing disclaimer this record frames itself with', RESIDUE,
     'The existence of the zero-acting positive pairing'),
    ('### and the arc-source already graded in the realization map', RESIDUE, 'Connes'),
    # ### ---- COMPONENT 2: THE MARGIN, at the balance keystone
    ('the margin, defined', BALANCE, 'is the margin in the inequality'),
    ('### its positivity and its minimum', BALANCE, 'stays positive throughout'),
    ('### its growth', BALANCE, 'grows monotonically thereafter'),
    ('### where the inequality binds', BALANCE, 'The binding regime is exactly'),
    ('### and the channel that is not eventually positive', BALANCE,
     'The differential channel is not eventually positive'),
    # ### ---- THE DEPOSIT'S OWN REGISTER MAP
    ('the five registers', os.path.join(DEPOSIT, 'A_Place_to_Stand.md'), '**The five registers.**'),
    ('### the fourth register, the channel inequality', os.path.join(DEPOSIT,
     'A_Place_to_Stand.md'), 'the premise is the inequality'),
    ('### the fifth register, the spectral-realization distance', os.path.join(DEPOSIT,
     'A_Place_to_Stand.md'), 'no positive pairing is known'),
    ('### ONE PREMISE, FIVE REGISTERS', os.path.join(DEPOSIT, 'A_Place_to_Stand.md'),
     'A reader who discharges any one of them discharges all five'),
    ('### ### AND THE EQUIVALENCES DELIBERATELY NOT COMPILED', os.path.join(DEPOSIT,
     'A_Place_to_Stand.md'), 'deliberately **not** compiling the cross-register equivalences'),
    ('### h2, and its classical faces', os.path.join(DEPOSIT, 'A_Place_to_Stand.md'),
     'The obligation h2 is, in each of the classical faces'),
    ('### the ancestry of the channel decomposition', os.path.join(DEPOSIT,
     'A_Place_to_Stand.md'), 'Bombieri and Lagarias (1999)'),
]

# ### **THE PHRASE CENSUS. ### THE ONE MEASUREMENT THAT TYPES A CONTACT'S PROVENANCE.**
# ### A phrase present in `day1/` and ABSENT from `outputs/DEPOSITED-v1.1.2/` is INTERNAL, and a
# ### contact with it cannot be typed REFINEMENT-OF-DEPOSITED however familiar it sounds.
PHRASES = [
    'the space is the wall',
    'the positive space',
    'chiasmus',
    'no positive pairing is known',
    'the premise is the inequality',
    'cross-register equivalences',
    'Weil positivity',
    'Sonin',
]


def main():
    lines = []

    def rec(s=''):
        lines.append(s)

    rec('=' * 100)
    rec('b324_extract.py -- THE KEYSTONES, READ AT THE CANONICAL DRIVE.')
    rec('=' * 100)
    rec('  ### **RESEMBLANCE IS REFUSED AS EVIDENCE BY NAME.** ### Shared words -- "space", "wall",')
    rec('  ### "margin", "room", "silence" -- decide nothing here. ### Every quotation below carries')
    rec('  ### its file and its line, and the bank compares CONSTITUENTS AGAINST DEFINITIONS.')
    rec('')

    rec('-' * 100)
    rec('### (A) THE DRIVES, AND WHICH COPY IS BEING READ.')
    rec('-' * 100)
    rec('  ### **THE ORDER SAYS: THE CANONICAL DRIVE, NEVER THE PROJECT MIRROR.**')
    rec('  deposit copy   : outputs/DEPOSITED-v1.1.2/   (md5-verified against Zenodo, b236)')
    rec('  internal copy  : day1/                        (the working line, ms v5.13)')
    rec('  keystones      : phase1.5/proofs/ and phase1.5/spectral/  (INTERNAL, not deposited)')
    rec('  ### **THE PROJECT MIRROR (`mirror-refresh-*.zip`) IS NOT READ BY THIS ACT AT ALL.**')
    miss = 0
    for lbl, p in (('deposit dir', DEPOSIT), ('internal dir', INTERNAL),
                   ('residue keystone', RESIDUE), ('balance keystone', BALANCE)):
        ok = os.path.exists(p)
        rec('  %-18s present : %s   %s' % (lbl, ok, p.replace(PP, '<papers>')))
        if not ok:
            miss += 1
    rec('  ### ### **PATHS NOT PRESENT : %d**' % miss)

    rec('')
    rec('-' * 100)
    rec('### (B) THE PHRASE CENSUS. ### **DEPOSITED OR INTERNAL, COUNTED AND NOT ASSUMED.**')
    rec('-' * 100)
    rec('    %-38s %-10s %-10s %-12s %s'
        % ('phrase', 'deposit', 'internal', 'keystones', 'provenance'))
    dep_all = ''
    for _lbl, fn in SUPPORT:
        p = os.path.join(DEPOSIT, fn)
        if os.path.exists(p):
            dep_all += io.open(p, encoding='utf-8', errors='replace').read()
    int_all = ''
    for fn in os.listdir(INTERNAL):
        if fn.endswith('.md'):
            int_all += io.open(os.path.join(INTERNAL, fn),
                               encoding='utf-8', errors='replace').read()
    key_all = ''
    for p in (RESIDUE, BALANCE):
        if os.path.exists(p):
            key_all += io.open(p, encoding='utf-8', errors='replace').read()
    census = {}
    for ph in PHRASES:
        dc, ic, kc = dep_all.count(ph), int_all.count(ph), key_all.count(ph)
        prov = ('DEPOSITED' if dc else ('INTERNAL' if (ic or kc) else 'ABSENT FROM BOTH'))
        census[ph] = (dc, ic, kc, prov)
        rec('    %-38s %-10d %-10d %-12d %s' % (ph[:38], dc, ic, kc, prov))
    rec('  ### ### **A PHRASE ABSENT FROM THE DEPOSIT IS NOT A DEPOSITED CLAIM, HOWEVER FAMILIAR')
    rec('  ### ### IT SOUNDS.** ### This table is what lets a contact be typed honestly.')

    rec('')
    rec('-' * 100)
    rec('### (C) THE QUOTATIONS, EACH WITH ITS FILE AND ITS LINE.')
    rec('-' * 100)
    missing = 0
    for lbl, path, frag in WANTED:
        p = path if os.path.isabs(path) else os.path.join(PP, path)
        rec('')
        rec('### ==== %s' % lbl)
        if not os.path.exists(p):
            missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % p.replace(PP, '<papers>'))
            continue
        body = io.open(p, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        rec('###      %s | fragment %r | %d hit(s)'
            % (p.replace(PP, '<papers>').replace('\\', '/'), frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            t = ln.strip()
            rec('    | line %-5d %s' % (n, t[:520]))
            if len(t) > 520:
                rec('    |            ... [%d more characters on this line]' % (len(t) - 520))
    rec('')
    rec('  ### ### **QUOTATIONS NOT FOUND : %d**' % missing)

    rec('')
    rec('-' * 100)
    rec('### (D) THE SUPPORT TEXTS, AT THE VERIFIED DEPOSIT COPY, WITH THEIR SIZES.')
    rec('-' * 100)
    rec('    %-30s %-38s %-10s %-8s' % ('what', 'file', 'bytes', 'lines'))
    smiss = 0
    for lbl, fn in SUPPORT:
        p = os.path.join(DEPOSIT, fn)
        if not os.path.exists(p):
            smiss += 1
            rec('    %-30s %-38s ### **NOT PRESENT**' % (lbl, fn))
            continue
        t = io.open(p, encoding='utf-8', errors='replace').read()
        rec('    %-30s %-38s %-10d %-8d'
            % (lbl, fn, len(t.encode('utf-8')), len(t.splitlines())))
    rec('    ### ### **SUPPORT TEXTS NOT PRESENT : %d**' % smiss)
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    return 0 if not (miss or missing or smiss) else 5


if __name__ == '__main__':
    sys.exit(main())
