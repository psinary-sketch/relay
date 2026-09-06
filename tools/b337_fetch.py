# -*- coding: utf-8 -*-
"""b337_fetch.py -- ONE READ-ONLY FETCH OF THE PUBLIC RECORD, AND THE THREE LEDGERS RECONCILED TO REGISTRY AGAINST IT.

### ### **TRANSMISSION DISCIPLINE (b130's law, b236's practice):** only the public record URL goes out; nothing of the
### programme is sent. ### **READ-ONLY:** a GET of the record's JSON; no write, no token, no login.
### ### **WHAT IS COMPARED, FIELD BY FIELD** (registration (C)): the record's version, publication date, DOI, concept DOI
### and file count against REGISTRY's `d1-1` row; the local canonical copy `outputs/DEPOSITED-v1.1.2/` re-hashed
### against the published MD5s; the three ledgers' own deposit statements (the lines the extract file located) scored
### CURRENT / DRIFT / ROUTED. ### A disagreement with REGISTRY is reported first. ### The record's JSON is kept at
### `data/b337_record.json` (public identifiers only).
"""
import hashlib
import io
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
REC = 'https://zenodo.org/api/records/21539167'
DEST = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
OUT = os.path.join(D, 'b337_fetch_run.txt')
OUTJ = os.path.join(D, 'b337_fetch.json')
RECJ = os.path.join(D, 'b337_record.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EXPECT = dict(version='v1.1.2', date='2026-07-24', doi='10.5281/zenodo.21539167', concept='10.5281/zenodo.19675355', nfiles=11)
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def md5(path):
    h = hashlib.md5()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b''):
            h.update(chunk)
    return h.hexdigest()


def registry_row():
    t = io.open(os.path.join(PP, 'REGISTRY.md'), encoding='utf-8', errors='replace').read()
    ln = [x for x in t.splitlines() if x.startswith('| d1-1 |')][0]
    return dict(line=ln, version=('v1.1.2' in ln), doi=('10.5281/zenodo.21539167' in ln), concept=('19675355' in ln), date=('2026-07-24' in ln))


def ledger_statements():
    loom = io.open(os.path.join(PP, 'VERIFICATION_LOOM.md'), encoding='utf-8', errors='replace').read()
    trails = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read()
    err = io.open(os.path.join(PP, 'ERRATA.md'), encoding='utf-8', errors='replace').read()
    return {
        'VERIFICATION_LOOM.md': ('the gate-1 pin', '21539167` returns **v1.1.2 \u00b7 2026-07-24 \u00b7 DOI 10.5281/zenodo.21539167 \u00b7 concept 19675355 \u00b7 11' in loom, 'v1.1.2', '2026-07-24', 11),
        'OPEN_TRAILS.md': ('the deposit-voice pin', '**Deposit-voice is pinned** by the read-only fetch of 2026-08-28: Zenodo **v1.1.2**, DOI' in trails, 'v1.1.2', '2026-07-24', 11),
        'ERRATA.md': ('the head', 'Zenodo **v1.1.1** ([10.5281/zenodo.21436278](https://doi.org/10.5281/zenodo.21436278);' in err, 'v1.1.1', None, None),
    }


def main():
    rec('=' * 100)
    rec('b337 -- THE FETCH, READ-ONLY, AND THE THREE LEDGERS RECONCILED TO REGISTRY AGAINST IT.')
    rec('=' * 100)
    rec('  record URL (the only thing sent) : %s' % REC)
    try:
        with urllib.request.urlopen(REC, timeout=90) as r:
            raw = r.read()
    except Exception as e:  # noqa: BLE001
        rec('  ### THE FETCH FAILED : %s -- NOTHING IS RECONCILED; the ledgers are ROUTED as a whole.' % e)
        rec('=' * 100)
        io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
        return 2
    j = json.loads(raw.decode('utf-8'))
    open(RECJ + '.tmp', 'wb').write((json.dumps(j, indent=1) + chr(10)).encode('utf-8'))
    os.replace(RECJ + '.tmp', RECJ)
    md = j.get('metadata', {})
    got = dict(version=md.get('version'), date=md.get('publication_date'), doi=j.get('doi') or md.get('doi'), concept=j.get('conceptdoi') or md.get('conceptdoi'),
               nfiles=len(j.get('files', [])))
    rec('  the record returns : version %s ; published %s ; DOI %s ; concept %s ; files %d' % (got['version'], got['date'], got['doi'], got['concept'], got['nfiles']))
    agree = {k: (got[k] == EXPECT[k]) for k in EXPECT}
    first = [k for k, v in agree.items() if not v]
    if first:
        rec('  ### ### **A FIELD DISAGREES WITH REGISTRY, REPORTED FIRST : %s** (record %s ; REGISTRY %s)' % (first, {k: got[k] for k in first}, {k: EXPECT[k] for k in first}))
    else:
        rec('  ### REGISTRY d1-1 AGREES WITH THE RECORD ON EVERY FIELD : version, date, DOI, concept, file count.')
    rr = registry_row()
    rec('  REGISTRY d1-1 row carries v1.1.2 %s ; the DOI %s ; the concept %s ; the date %s' % (rr['version'], rr['doi'], rr['concept'], rr['date']))
    # ### the local canonical copy against the published MD5s
    pub = {}
    for f in j.get('files', []):
        key = f.get('key') or f.get('filename')
        cs = f.get('checksum', '')
        pub[key] = cs.split(':', 1)[1] if ':' in cs else cs
    match, miss, bad = 0, [], []
    for key, h in sorted(pub.items()):
        p = os.path.join(DEST, key)
        if not os.path.exists(p):
            miss.append(key)
            continue
        if md5(p) == h:
            match += 1
        else:
            bad.append(key)
    rec('  the local canonical copy %s : %d of %d files match the published MD5 ; missing %s ; mismatching %s' % (os.path.basename(DEST), match, len(pub), miss or 'none', bad or 'none'))
    # ### the three ledgers
    rec('')
    rec('  THE THREE LEDGERS, EACH AGAINST THE FETCH:')
    scored = {}
    for name, (what, located, ver, date, nf) in ledger_statements().items():
        if not located:
            status = 'ROUTED (the statement the extract located is not in the file as read now)'
        elif ver == got['version'] and (date is None or date == got['date']) and (nf is None or nf == got['nfiles']):
            status = 'CURRENT'
        else:
            status = 'DRIFT (states %s against the record\'s %s)' % (ver, got['version'])
        scored[name] = dict(what=what, located=located, states=ver, status=status)
        rec('    %-22s %-22s located %s ; states %-7s : %s' % (name, what, located, ver, status))
    rec('  ### DRIFT is repaired by an APPENDED note (the ledgers are append-only); nothing is edited.')
    rec('=' * 100)
    out = dict(url=REC, got=got, expect=EXPECT, agree=agree, registry_row=rr, local_match=match, local_total=len(pub), missing=miss, mismatching=bad, ledgers=scored,
               files=[dict(key=k, md5=v) for k, v in sorted(pub.items())])
    open(OUTJ + '.tmp', 'wb').write((json.dumps(out, indent=1) + chr(10)).encode('utf-8'))
    os.replace(OUTJ + '.tmp', OUTJ)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    return 0 if (not first and not miss and not bad) else 1


if __name__ == '__main__':
    sys.exit(main())
