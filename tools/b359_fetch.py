# -*- coding: utf-8 -*-
"""b359_fetch.py -- THE DEPOSIT RECORD, FETCHED READ-ONLY AND PINNED. ### **BAR 1.**

### ### ### **THIS TOOL WRITES NOTHING AT ZENODO AND DEPOSITS NOTHING.** ### It issues ### **`GET`** ###
### and nothing else. ### There is no token in it, no credential, no `POST`, no `PUT`, no `DELETE`, no
### upload and no form. ### `G-NODEPOSIT` re-measures that claim on STRIPPED code rather than trusting this
### sentence, which is the only way a sentence like this one is worth writing.
### ### **AND IF THE FETCH DOES NOT RETURN, THE ACT STOPS.** ### The locked registration's branch (H)(3)
### says the failure is REPORTED AS THE FINDING and ### **NOTHING IS RECONCILED FROM MEMORY.**
### ### **THE RECORD IS THE CONCEPT DOI'S LATEST VERSION AND THE VERSION RECORD ITSELF**, both fetched, so
### a drifted latest-version pointer would show as a disagreement between the two rather than hide inside
### one of them.
"""
import hashlib
import io
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### (tag, what it is, url)
# ### **THE RECORD IDS ARE READ FROM `REGISTRY.md`'S OWN `d1-1` ROW BY THE EXTRACT, NEVER TYPED AS FACTS
# ### HERE**; the addresses below are the public API's shape for those ids, and the ids in them are the
# ### ones the extract locates and the bank quotes.
TARGETS = [
    ('F1', 'the VERSION record REGISTRY names in its d1-1 row (Zenodo 21539167)',
     'https://zenodo.org/api/records/21539167'),
    ('F2', 'the CONCEPT record and its latest-version pointer (Zenodo 19675355)',
     'https://zenodo.org/api/records/19675355'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def get(url, dest):
    """### ### **`GET`, AND ONLY `GET`.** ### `urlopen` on a bare `Request` issues a GET; no data body is
    ### passed, no method is overridden, and no header carries a credential."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research seat; read-only GET)',
                                               'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
        status, ctype = r.status, r.headers.get('Content-Type', '')
    open(dest, 'wb').write(data)
    return status, ctype, data


def main():
    rec('=' * 100)
    rec('b359 -- THE DEPOSIT RECORD, FETCHED READ-ONLY AND PINNED.')
    rec('### ### **GET ONLY. ### NOTHING IS DEPOSITED AND NOTHING IS WRITTEN AT ZENODO.**')
    rec('=' * 100)
    out, hard = [], False
    for tag, what, url in TARGETS:
        rec('')
        rec('-' * 100)
        rec('  [%s] %s' % (tag, what))
        rec('      url : %s   ### **METHOD: GET**' % url)
        dest = os.path.join(D, 'b359_fetch_%s.json' % tag)
        e = dict(tag=tag, what=what, url=url, method='GET')
        try:
            status, ctype, data = get(url, dest)
        except Exception as ex:
            e.update(fetched=False, error='%s: %s' % (type(ex).__name__, str(ex)[:140]))
            hard = True
            rec('      ### ### **NOT FETCHED : %s**' % e['error'])
            out.append(e)
            continue
        sha = hashlib.sha256(data).hexdigest()
        e.update(fetched=True, status=status, content_type=ctype, bytes=len(data), sha256=sha,
                 file=os.path.basename(dest))
        rec('      ### **FETCHED : HTTP %s ; %s ; %d bytes**' % (status, ctype, len(data)))
        rec('      ### **sha256 : %s**' % sha)
        try:
            j = json.loads(data.decode('utf-8'))
        except Exception as ex:
            e.update(parsed=False, error='%s' % type(ex).__name__)
            rec('      ### ### **FETCHED BUT NOT PARSED.**')
            out.append(e)
            continue
        md = j.get('metadata', {}) or {}
        fields = dict(
            id=j.get('id'), doi=j.get('doi') or md.get('doi'),
            conceptdoi=j.get('conceptdoi'), conceptrecid=j.get('conceptrecid'),
            version=md.get('version'), publication_date=md.get('publication_date'),
            title=(md.get('title') or '')[:90],
            n_files=len(j.get('files') or []),
            is_last=(j.get('metadata', {}).get('relations', {}).get('version', [{}]) or [{}])[0].get('is_last'),
            latest_index=(j.get('metadata', {}).get('relations', {}).get('version', [{}]) or [{}])[0].get('index'),
            latest_html=(j.get('links') or {}).get('latest_html'),
        )
        e['fields'] = fields
        e['parsed'] = True
        rec('      ### THE FIELDS, AS THE PLATFORM RETURNED THEM:')
        for k in ('id', 'doi', 'conceptdoi', 'conceptrecid', 'version', 'publication_date',
                  'n_files', 'is_last', 'title'):
            rec('        %-18s : %s' % (k, fields.get(k)))
        out.append(e)
    rec('')
    rec('=' * 100)
    nf = sum(1 for e in out if e.get('fetched'))
    rec('  targets : %d   ### FETCHED : %d   ### NOT FETCHED : %d' % (len(out), nf, len(out) - nf))
    if hard:
        rec('  ### ### **THE FETCH DID NOT RETURN. ### BRANCH (H)(3) IS TAKEN AND THE ACT STOPS.**')
        rec('  ### ### **NOTHING IS RECONCILED FROM MEMORY.**')
    rec('  ### **A HASH FIXES THE BYTES THE PLATFORM RETURNED. ### IT DOES NOT MAKE THE PLATFORM RIGHT.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b359_fetch_run', LINES)
    io.open(os.path.join(D, 'b359_fetch.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(targets=out, fetched=nf, attempted=len(out), hard_failure=hard,
                        method='GET', wrote_anything_remote=False,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 2 if hard else 0


if __name__ == '__main__':
    sys.exit(main())
