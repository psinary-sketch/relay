# -*- coding: utf-8 -*-
"""b236_checks.py -- the b236 gates, routed through the amended b217 harness.

### THIS ACT'S RISKS:
###   (1) that a stored file is trusted because it ARRIVED rather than because it MATCHED.
###       ### A download that returns an HTML error page is still a file and hashes to
###       ### something. ### THE CHECK IS ZENODO'S PUBLISHED MD5.
###   (2) that the rename lost or altered content. ### Bytes asserted, not claimed.
###   (3) that the demarcation OVERCLAIMS. ### Its whole form invites a list of what we have
###       ### that they do not, so every added item must carry its limit in the same breath.
###   (4) that the mapping implies five registers while covering one.
### ### EVERY ABSENCE CARRIES A POSITIVE CONTROL.
"""
import hashlib
import io
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
PLACE = 'D:/MY-DOwnloads/PLACE-papers'
METHOD = os.path.join(PLACE, 'phase2', 'method')
D = os.path.join(ROOT, 'data')

BANK = os.path.join(D, 'b236_comprehension_read.txt')
REG = os.path.join(D, 'b236_registration_2026-08-28.txt')
RUN = os.path.join(D, 'b236_deposit_fetch_run.txt')
B235 = os.path.join(D, 'b235_phase11_conventions.txt')
B233 = os.path.join(D, 'b233_the_arrangement.txt')

DEPO = os.path.join(PLACE, 'outputs', 'DEPOSITED-v1.1.2')
MONO_D = os.path.join(DEPO, 'A_Place_to_Stand.md')
OLDSNAP = os.path.join(PLACE, 'outputs', 'DEPOSITED',
                       'A_Place_to_Stand.v5.4.EARLIER-DEPOSIT-SNAPSHOT.md')
FACES = os.path.join(METHOD, 'FACES_OF_H2_AT_FINITE_INSTANCE.md')
CHAIN = os.path.join(METHOD, 'THE_IDENTITY_CHAIN.md')
REGISTRY = os.path.join(PLACE, 'REGISTRY.md')
ERRATA = os.path.join(PLACE, 'ERRATA.md')
CACHE = (r'C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--'
         r'\2bde398e-07cf-4dd0-8608-0a3b93e6f10a\scratchpad\b236\record.json')


def md5(path):
    h = hashlib.md5()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b''):
            h.update(chunk)
    return h.hexdigest()


def all_files_match():
    """### THE CHECK IS ZENODO'S PUBLISHED MD5, NOT THE FILE'S EXISTENCE.
    ### Returns (n_files, n_matched)."""
    try:
        rec = json.load(io.open(CACHE, encoding='utf-8'))
    except Exception:
        return (-1, -1)
    n = ok = 0
    for f in rec.get('files', []):
        n += 1
        p = os.path.join(DEPO, f['key'])
        if os.path.isfile(p) and md5(p) == f['checksum'].split(':', 1)[1]:
            ok += 1
    return (n, ok)


def unmodified(repo, relpath):
    try:
        r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                           capture_output=True)
    except Exception:
        return False
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def old_path_resolvable():
    """### THE RENAME MUST NOT HAVE LOST THE OLD PATH FROM THE RECORD."""
    try:
        r = subprocess.run(['git', '-C', PLACE, 'cat-file', '-e',
                            'HEAD:outputs/DEPOSITED/A_Place_to_Stand.DEPOSITED.md'],
                           capture_output=True)
    except Exception:
        return False
    return r.returncode == 0


def rename_bytes_identical():
    """### BYTES ASSERTED, NOT CLAIMED: the renamed file against its HEAD blob."""
    try:
        r = subprocess.run(['git', '-C', PLACE, 'show',
                            'HEAD:outputs/DEPOSITED/A_Place_to_Stand.DEPOSITED.md'],
                           capture_output=True)
    except Exception:
        return False
    if r.returncode != 0 or not os.path.isfile(OLDSNAP):
        return False
    return hashlib.md5(r.stdout).hexdigest() == md5(OLDSNAP)


def deposit_silent_on_winf():
    """### THE SILENCE, MEASURED. ### POSITIVE CONTROL LIVES IN THE SAME GATE'S WITNESS."""
    if not os.path.isfile(MONO_D):
        return False
    t = io.open(MONO_D, encoding='utf-8', errors='replace').read()
    return ('W_\u221e' not in t) and ('W_inf' not in t)


def deposit_readable():
    """### THE POSITIVE CONTROL ON THAT SILENCE: the same file yields text we DO find."""
    if not os.path.isfile(MONO_D):
        return False
    t = io.open(MONO_D, encoding='utf-8', errors='replace').read()
    return ('The one open premise' in t) and ('v5.10.2' in t)


def main():
    h = Harness(ROOT, 'b236')

    # 1 -- ### 11/11 STORED **AND MD5-MATCHED AGAINST ZENODO'S PUBLISHED CHECKSUMS**.
    h.run('eleven-files-md5-matched',
          check=lambda: all_files_match() == (11, 11),
          fixture=lambda: all_files_match() == (11, 0),
          witness=lambda: all_files_match()[0] == 11)

    # 2 -- ### THE CANONICAL COPY PROVES ITS OWN VERSION AT CONTENT.
    h.run('canonical-copy-is-v5-10-2',
          check=lambda: contains(MONO_D, 'v5.10.2, 2026-07-24'),
          fixture=lambda: contains(OLDSNAP, 'v5.10.2, 2026-07-24'),
          witness=lambda: contains(OLDSNAP, 'v5.4, May 2026'))

    # 3 -- ### THE RENAME: BYTES IDENTICAL AND THE OLD PATH STILL RESOLVABLE.
    h.run('rename-bytes-identical-old-path-kept',
          check=lambda: rename_bytes_identical() and old_path_resolvable(),
          fixture=lambda: rename_bytes_identical() and not old_path_resolvable(),
          witness=lambda: old_path_resolvable())

    # 4 -- ### THE DEPOSIT IS SILENT ON W_inf -- WITH ITS POSITIVE CONTROL IN THE SAME GATE.
    # ### WITHOUT THE CONTROL, "zero occurrences" could mean an unreadable file.
    h.run('deposit-silent-on-winf-with-control',
          check=lambda: deposit_silent_on_winf() and deposit_readable(),
          fixture=lambda: (not deposit_readable()),
          witness=lambda: deposit_readable())

    # 5 -- ### ERRATA UNTOUCHED: a silence is not a defect.
    h.run('errata-untouched-silence-not-defect',
          check=lambda: unmodified(PLACE, 'ERRATA.md') and contains(BANK, 'a silence is not a defect'),
          fixture=lambda: contains(ERRATA, 'a silence is not a defect'),
          witness=lambda: unmodified(PLACE, 'ERRATA.md'))

    # 6 -- ### THE DEPOSIT-VOICE QUOTES ARE REAL: found in the CANONICAL COPY, not paraphrased.
    Q = ['h1 is complete at the witness',
         'positivity of the Weil functional',
         'The one open premise',
         'criterion + verified surround, not end-to-end',
         'None of this discharges h2']
    h.run('deposit-quotes-found-at-source',
          check=lambda: all(contains(MONO_D, q) and contains(BANK, q) for q in Q),
          fixture=lambda: all(contains(OLDSNAP, q) for q in Q),
          witness=lambda: all(contains(MONO_D, q) for q in Q))

    # 7 -- ### THE MAPPING NAMES ITS LIMIT: five registers, one mapped.
    h.run('mapping-limit-five-registers-one-mapped',
          # ### BOTH THIS GATE AND GATE 9 FAILED ON THE FIRST RUN BECAUSE THE NEEDLE DID NOT
          # ### MATCH THE BANK'S OWN WORDING -- the GATE was wrong, not the bank, and the repair
          # ### is to the gate. ### A needle written from memory rather than from the file is
          # ### b227's species with the roles reversed.
          check=lambda: both(BANK, 'the deposit names five', 'over-transfer'),
          fixture=lambda: both(B235, 'the deposit names five', 'over-transfer'),
          witness=lambda: contains(CHAIN, 'maps ONE'))

    # 8 -- ### THE DEMARCATION CARRIES ITS CEILING, not just its additions.
    h.run('demarcation-carries-its-ceiling',
          check=lambda: all(contains(BANK, s) for s in
                            ('has NOT proved Weil positivity', 'NON-PROMOTION',
                             'RH-EQUIVALENT AND OPEN')),
          fixture=lambda: contains(B233, 'has NOT proved Weil positivity'),
          witness=lambda: contains(CHAIN, 'has NOT proved Weil positivity'))

    # 9 -- ### THE IMPORT IS QUOTED **AS** AN IMPORT, credited where CC credits it.
    h.run('weil-criterion-quoted-as-import',
          check=lambda: (both(BANK, 'credit it to A. Weil [33]', 'it is not ours')
                         and contains(CHAIN, 'credit to A. Weil [33]')),
          fixture=lambda: both(FACES, 'credit it to A. Weil [33]', 'it is not ours'),
          witness=lambda: contains(CHAIN, 'credit to A. Weil [33]'))

    # 10 -- ### THE FACES AMENDMENT IS ADDITIVE AND CARRIES THE DOCUMENT'S OWN LAW.
    h.run('faces-additive-non-fusion-carried',
          check=lambda: (contains(FACES, 'THE COMPREHENSION AGAINST A NOW-COMPLETE STATEMENT')
                         and contains(FACES, 'no cross-register equivalence is compiled or claimed')
                         and contains(FACES, 'THE FIVE FACES, EACH AT ITS TERMINAL')),
          fixture=lambda: contains(CHAIN, 'THE FIVE FACES, EACH AT ITS TERMINAL'),
          witness=lambda: contains(FACES, 'THE FIVE FACES, EACH AT ITS TERMINAL'))

    # 11 -- ### THE FACE-OFF IS A CHECKLIST AND NOTHING ON IT WAS RUN.
    h.run('faceoff-checklist-listed-not-run',
          check=lambda: all(contains(BANK, s) for s in
                            ('LISTED EXACTLY AND NOT RUN', 'definitional ruling',
                             'RIDING THE NEXT KERNEL-TOUCHING ACT')),
          fixture=lambda: contains(B235, 'LISTED EXACTLY AND NOT RUN'),
          witness=lambda: contains(BANK, 'definitional ruling'))

    # 12 -- ### REGISTRY NOTES THE LOCAL-COPY PATH, additively.
    h.run('registry-notes-local-copy-path',
          check=lambda: both(REGISTRY, 'DEPOSITED-v1.1.2', 'verified byte-level'),
          fixture=lambda: both(ERRATA, 'DEPOSITED-v1.1.2', 'verified byte-level'),
          witness=lambda: contains(REGISTRY, 'DEPOSITED-v1.1.2'))

    for row in h.rows:
        print('  %-42s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
