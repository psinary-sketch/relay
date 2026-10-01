# -*- coding: utf-8 -*-
"""test_addenda_licence.py -- THE TEST OF (R177)(3)(h)'S LICENCE BLOB LINE (b567), committed with it.

### Cases on the reader (tools/addenda.py) and on b566's G-LICENCE-PRINTED arm itself, each printed with its verdict: the
### appended b566 line MATCHES the LICENSE blob on the kernel's main; a line carrying the CRLF working copy's digest (the
### b566 bank's own sha256) does NOT; a record with no blob line does NOT; a line of another shape is not read; a blob one
### byte different does NOT; and the arm, handed the real record, PASSES, and FAILS when handed the working-copy bytes.
"""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import addenda as ADD

D = os.path.join(ROOT, 'data')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
OUT = []


def case(name, got, want):
    ok = got == want
    OUT.append(ok)
    print('  %-78s got %-5s want %-5s %s' % (name, got, want, 'OK' if ok else '### WRONG'))


def main():
    print('### test_addenda_licence -- (R177)(3)(h)')
    rec = open(os.path.join(D, 'b566_step1_license.txt'), 'rb').read().decode('utf-8')
    blob = subprocess.run(['git', '-C', KER, 'cat-file', 'blob', 'main:Vendored/Bulka/LICENSE'], capture_output=True).stdout
    work = blob.replace(b'\n', b'\r\n')
    b = ADD.blob_line(rec)
    print('  the record`s blob line : %s' % b)
    print('  the blob on main       : %d bytes, sha256 %s' % (len(blob), hashlib.sha256(blob).hexdigest()))
    print('  its CRLF working form  : %d bytes, sha256 %s' % (len(work), hashlib.sha256(work).hexdigest()))
    case('the record carries a blob line, appended by (R177)(3)', bool(b) and b['rn'] == 'R177' and b['k'] == 3, True)
    case('the blob line MATCHES the LICENSE blob on the kernel`s main', ADD.blob_matches(rec, blob), True)
    case('MUTATION: the CRLF working form does NOT match', ADD.blob_matches(rec, work), False)
    case('MUTATION: a blob one byte longer does NOT match', ADD.blob_matches(rec, blob + b'\n'), False)
    wc = 'LICENCE BLOB SHA256: %s, blob %s, %d bytes, appended by (R177)(3)' % (
        hashlib.sha256(work).hexdigest(), b['blob'] if b else '0' * 40, len(work))
    case('MUTATION: a line carrying the WORKING-COPY digest does NOT match the blob', ADD.blob_matches(rec + '\n' + wc, blob), False)
    pre = rec[:rec.index('LICENCE BLOB SHA256:')] if 'LICENCE BLOB SHA256:' in rec else rec
    case('MUTATION: the record as b566 left it (no blob line) does NOT match', ADD.blob_matches(pre, blob), False)
    case('MUTATION: b566`s own digest line is not read as a blob line',
         ADD.blob_line('LICENSE blob d707a12f00206dd785af487026142534fa36120d; sha256 18ed520c9cda16a04467676a237d515f6410845e6a0de80de97f5c14731b2991'), None)

    import b566_checks as C
    arm = [a for a in C.ARMS if a[0] == 'G-LICENCE-PRINTED'][0]
    S = dict(lic=rec, lic_main_bytes=blob, lic_clone_bytes=None)
    case('ARM: the real record against the blob on main -> PASS', bool(arm[2](S)), True)
    case('ARM: the real record, a clone blob equal to main`s -> PASS', bool(arm[2](dict(S, lic_clone_bytes=blob))), True)
    case('ARM: the real record against the WORKING-COPY bytes -> FAIL', bool(arm[2](dict(S, lic_main_bytes=work))), False)
    case('ARM: a clone blob that differs -> FAIL', bool(arm[2](dict(S, lic_clone_bytes=work))), False)
    case('ARM: the record as b566 left it -> FAIL', bool(arm[2](dict(S, lic=pre))), False)
    case('ARM: its own positive control still FAILS', bool(arm[2](arm[3](dict(S)))), False)
    print('### %d of %d cases as wanted -- %s' % (sum(OUT), len(OUT), 'PASS' if all(OUT) else '### FAIL'))
    return 0 if all(OUT) else 1


if __name__ == '__main__':
    sys.exit(main())
