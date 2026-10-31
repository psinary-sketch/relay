# -*- coding: utf-8 -*-
"""b726, (R336)(5): THE DEPOSITED RECORDS' CURRENT WORDS, READ ANONYMOUSLY. One GET of each public record by its id at zenodo.org/api/records, no
token, no identity in any header, nothing written to Zenodo. Banked with the creators dropped and the author's name masked in every string (the name
held in memory, read as tools/b726_address_scan.py reads it; the bank refuses itself if an identifier survives).

  python -X utf8 tools/b726_zenodo_read.py dry | bank          -> data/b726_zenodo_read.json"""
import json
import os
import re
import sys
import time
import urllib.request

T = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, T)
import b726_address_scan as SC  # noqa: E402

D = os.path.join(os.path.dirname(T), 'data')
BANK = os.path.join(D, 'b726_zenodo_read.json')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
# ### every record REGISTRY :83, :102, :107 and :416 and data/zenodo_fetch_2026-08-10.jsonl name; the May records, the wave's, T7's
RECORDS = [('May', '19937590'), ('May', '19938917'), ('wave', '21539167'), ('wave', '21539068'), ('wave', '21520474'), ('T7', '21436282')]
KEEP = ('title', 'version', 'publication_date', 'description', 'notes')


def fetch(rid):
    r = urllib.request.Request('https://zenodo.org/api/records/' + rid, headers={'User-Agent': 'relay-read', 'Accept': 'application/json'})
    with urllib.request.urlopen(r, timeout=60) as f:
        return json.loads(f.read().decode('utf-8'))


def main(mode):
    name, user, addr = SC.author_name(), SC.previous_username(), SC.previous_address()
    out = []
    for kind, rid in RECORDS:
        o = fetch(rid)
        m = o.get('metadata', {})
        row = dict(kind=kind, id=rid, doi=o.get('doi'), masked=0)
        for k in KEEP:
            s = m.get(k)
            if isinstance(s, str):
                row['masked'] += s.count(name)
                s = s.replace(name, '[the author]')
                row[k] = s
        out.append(row)
        print('## %s %s v%s %s | %s (masked %d)' % (kind, rid, row.get('version'), row.get('publication_date'), row.get('title'), row['masked']))
        print('   ' + re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', row.get('description', '')))[:1500])
        if row.get('notes'):
            print('   NOTES: ' + re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', row['notes']))[:500])
        time.sleep(2)
    t = json.dumps(dict(read_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=out), indent=1, ensure_ascii=False) + '\n'
    if SC.count(t, name) or SC.count(t, user) or SC.count(t, addr):
        sys.exit('### AN IDENTIFIER SURVIVES THE MASK -- NOTHING WRITTEN')
    if mode == 'bank':
        with open(BANK + '.tmp', 'wb') as f:
            f.write(t.encode('utf-8'))
        os.replace(BANK + '.tmp', BANK)
        print('written data/b726_zenodo_read.json')


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') not in ('dry', 'bank'):
        sys.exit(__doc__)
    main(sys.argv[1])
