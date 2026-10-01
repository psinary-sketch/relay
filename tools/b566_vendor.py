# -*- coding: utf-8 -*-
"""b566_vendor.py -- THE COPY, UNDER (R176)(3) STEP ONE, TRIAL (a). ### **ZETA23`S FORM, CARRIED.**

### Copies the vendored set (relay data/b566_vendor_list.txt: Fidelity`s closure within Bulka`s tree at 35df682f, which
### contains the converse`s) from the clone at D:/audit-b565/bulka into SIDE-explicit-formula/Vendored/Bulka/ at the SAME
### relative paths, so no module path and no import line changes. Each file gets Zeta23`s attribution header PREPENDED; the
### body below it is the source blob at the pin, byte for byte. Bulka`s LICENSE is carried whole beside the files.
### ### **THE BODY IS READ FROM THE GIT BLOB AT THE PIN (`git show 35df682f:<path>`), NOT FROM THE WORKING FILE**, so the
### ### digest pair is blob against copy and a CRLF working tree cannot move it (feedback: byte-level traps).
### Writes: SIDE-explicit-formula/Vendored/Bulka/** and relay data/b566_vendor_digests.json. Refuses to overwrite a file
### that already exists (a second run is a defect to record, not a silent rewrite). Usage: b566_vendor.py [--dry]
"""
import hashlib
import io
import json
import os
import subprocess
import sys

CLONE = 'D:/audit-b565/bulka'
PIN = '35df682f3b709ffe5fbcfdd452dfa964bd622b87'
KERNEL = 'D:/SIDE-explicit-formula'
DEST = os.path.join(KERNEL, 'Vendored', 'Bulka')
RELAY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIST = os.path.join(RELAY, 'data', 'b566_vendor_list.txt')
OUT = os.path.join(RELAY, 'data', 'b566_vendor_digests.json')
NL = chr(10)

HEADER = """/-
VENDORED INTO SIDE-explicit-formula -- NOT WRITTEN HERE.

Source     : github.com/nicholasbulka/li-criterion-rh-equivalence-lean
Source path: {path}
Pin        : 35df682f3b709ffe5fbcfdd452dfa964bd622b87
Copied     : byte-identical; sha256 of the body below = {sha}
Licence    : Apache License 2.0 -- see Vendored/Bulka/LICENSE, carried whole from the source, and NOTICE.

SPIRAL_MAP section 7 rule 7 (composites vendor with attribution) is satisfied by this header.
SPIRAL_MAP section 7 rule 9 (vanilla Lean 4 syntax discipline) is WAIVED for this namespace:
a vendored file is not edited, and the waiver is recorded in SPIRAL_MAP beside rule 9 with
act b495 as its reason. This file was vendored by act b566 under the author's ruling (R176)(3).

NOTHING BELOW THIS BLOCK IS THIS PROGRAMME'S WORK, AND NOTHING BELOW IT HAS BEEN ALTERED.
-/
"""


def blob(path):
    return subprocess.run(['git', '-C', CLONE, 'show', '%s:%s' % (PIN, path)],
                          capture_output=True, check=True).stdout


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main(argv):
    dry = '--dry' in argv
    head = subprocess.run(['git', '-C', CLONE, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    if head != PIN:
        print('### REFUSING: the clone`s HEAD is %s, not the pin %s' % (head, PIN))
        return 2
    mods = [m.strip() for m in io.open(LIST, encoding='utf-8').read().split(NL) if m.strip()]
    rows = []
    for m in mods:
        rel = m.replace('.', '/') + '.lean'
        body = blob(rel)
        h = sha(body)
        hdr = HEADER.format(path=rel, sha=h).encode('utf-8')
        dst = os.path.join(DEST, *rel.split('/'))
        rows.append({'module': m, 'path': rel, 'source_blob_sha256': h, 'body_bytes': len(body),
                     'header_bytes': len(hdr), 'dest': 'Vendored/Bulka/' + rel})
        if dry:
            continue
        if os.path.exists(dst):
            print('### REFUSING TO OVERWRITE %s' % dst)
            return 3
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, 'wb').write(hdr + body)
        back = open(dst, 'rb').read()
        if not back.startswith(hdr) or sha(back[len(hdr):]) != h:
            print('### READ-BACK MISMATCH %s' % dst)
            return 4
        rows[-1]['copy_body_sha256_readback'] = sha(back[len(hdr):])
    lic = blob('LICENSE')
    lic_dst = os.path.join(DEST, 'LICENSE')
    if not dry:
        if os.path.exists(lic_dst):
            print('### REFUSING TO OVERWRITE %s' % lic_dst)
            return 3
        open(lic_dst, 'wb').write(lic)
    rec = {'clone': CLONE, 'pin': PIN, 'modules': len(rows), 'license_sha256': sha(lic),
           'license_dest': 'Vendored/Bulka/LICENSE', 'rows': rows, 'dry': dry}
    if not dry:
        d = (json.dumps(rec, indent=1, ensure_ascii=False) + NL).encode('utf-8')
        open(OUT + '.tmp', 'wb').write(d)
        os.replace(OUT + '.tmp', OUT)
    for r in rows:
        print('  %-48s %s  %6d bytes' % (r['module'], r['source_blob_sha256'][:16], r['body_bytes']))
    print('  modules %d ; licence sha256 %s ; dry %s' % (len(rows), sha(lic)[:16], dry))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
