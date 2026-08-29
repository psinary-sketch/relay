# -*- coding: utf-8 -*-
"""b236_deposit_fetch.py -- FETCH THE DEPOSIT'S 11 FILES READ-ONLY AND VERIFY THEM BYTE-LEVEL.

### THE RULING THIS EXECUTES (the author's, 2026-08-28): "The deposit's 11 files are fetched
### read-only and stored at outputs/DEPOSITED-v1.1.2/ as the canonical local copy, verified
### byte-level against the fetch."

### TRANSMISSION DISCIPLINE (b130's law): ### ONLY PUBLIC IDENTIFIERS GO OUT -- the record URL
### and the file links it publishes. ### NO PROGRAMME OBJECT, VALUE, CLAIM OR FILENAME IS SENT.

### ### WHAT "VERIFIED BYTE-LEVEL" MEANS HERE, AND THE FAILURE MODE IT GUARDS:
### ### A DOWNLOAD THAT SILENTLY RETURNS AN HTML ERROR PAGE IS STILL A FILE, AND IT WILL HASH
### ### TO SOMETHING. ### So the check is NOT that a file arrived; it is that its MD5 equals the
### ### one ZENODO PUBLISHES for that file. ### A file whose hash does not match IS NOT STORED
### ### AS CANONICAL and the mismatch is reported. ### This is b213's species one door along --
### ### a check that re-matches what the act itself produced.
"""
import hashlib
import io
import json
import os
import sys
import urllib.request

REC = 'https://zenodo.org/api/records/21539167'
DEST = r'D:\MY-DOwnloads\PLACE-papers\outputs\DEPOSITED-v1.1.2'
CACHE = (r'C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--'
         r'\2bde398e-07cf-4dd0-8608-0a3b93e6f10a\scratchpad\b236\record.json')


def md5(path):
    h = hashlib.md5()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    print('=' * 92)
    print('b236 -- THE DEPOSIT FETCH. ### READ-ONLY. ### PUBLIC IDENTIFIERS ONLY.')
    print('=' * 92)
    rec = json.load(io.open(CACHE, encoding='utf-8'))
    meta = rec.get('metadata', {})
    print('  record   : %s' % REC)
    print('  version  : %s      publication_date : %s' % (meta.get('version'),
                                                          meta.get('publication_date')))
    print('  doi      : %s' % rec.get('doi'))
    files = rec.get('files', [])
    print('  files    : %d' % len(files))
    if len(files) != 11:
        print('  ### REFUSED -- the record does not carry 11 files. Nothing stored.')
        return 2

    os.makedirs(DEST, exist_ok=True)
    print('\n  %-34s %9s  %-8s %s' % ('file', 'bytes', 'size ok', 'md5 vs PUBLISHED md5'))
    ok = True
    for f in files:
        key = f['key']
        want = f['checksum'].split(':', 1)[1]
        url = f['links']['self']
        out = os.path.join(DEST, key)
        try:
            with urllib.request.urlopen(url, timeout=120) as r, open(out, 'wb') as w:
                w.write(r.read())
        except Exception as e:
            print('  %-34s ### DOWNLOAD FAILED: %s' % (key, e))
            ok = False
            continue
        got = md5(out)
        size_ok = os.path.getsize(out) == f['size']
        match = (got == want)
        ok = ok and match and size_ok
        print('  %-34s %9d  %-8s %s' % (key, os.path.getsize(out),
                                        'yes' if size_ok else '### NO',
                                        'MATCH' if match else '### MISMATCH %s != %s' % (got, want)))
        if not match:
            # ### A FILE THAT DOES NOT MATCH IS NOT KEPT AS CANONICAL.
            os.rename(out, out + '.UNVERIFIED')
            print('      ### NOT STORED AS CANONICAL -- renamed .UNVERIFIED')

    print('\n' + '=' * 92)
    print('  ### ALL 11 FILES PRESENT AND MD5-MATCHED AGAINST THE PUBLISHED CHECKSUMS: %s'
          % ('YES' if ok else 'NO'))
    print('  ### "MATCH" MEANS THE STORED BYTES ARE THE DEPOSITED BYTES. ### It does not mean the')
    print('  ### deposit is correct about anything -- only that this copy is faithful to it.')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
