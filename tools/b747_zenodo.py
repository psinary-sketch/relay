"""b747 -- (R357)(5): THE ZENODO v1.2.0 DRAFT READ BACK, no write.

ONE GET of the draft deposition 23228113 (a new version of record 21539167, FINDINGS :7893) through the deposit API: its metadata and its
file list come in the one response. THE TOKEN is read from os.environ['ZENODO_TOKEN'] inside this process, sent only in the Authorization
header, never printed, never written; the bank is checked for its bytes before it is written. No other method is reachable from this file.
The creators field is printed as a count with the words "author's fields present"; no name, address or ORCID is printed.
The comparison rows read REGISTRY.md row d1-1 (:83) and README.md :164 from PLACE-papers HEAD by `git show`.

    python -X utf8 -u tools/b747_zenodo.py            # dry: GET, print, write nothing
    python -X utf8 -u tools/b747_zenodo.py --bank     # GET, print, write data/b747_zenodo_readback.txt
"""
import os, sys, json, re, html, subprocess, datetime, urllib.request, urllib.error

DEP = '23228113'
URL = 'https://zenodo.org/api/deposit/depositions/' + DEP
PP = 'D:/MY-DOwnloads/PLACE-papers'
BANK = 'D:/relay/data/b747_zenodo_readback.txt'
NL = '\n'


def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def pp_line(path, n):
    t = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + path], capture_output=True, encoding='utf-8', check=True).stdout.split(NL)
    return t[n - 1]


def get():
    tok = os.environ.get('ZENODO_TOKEN') or ''
    if len(tok) < 20:
        sys.exit('### REFUSED: no token in the environment; nothing read')
    req = urllib.request.Request(URL, method='GET', headers={'Authorization': 'Bearer ' + tok, 'Accept': 'application/json',
                                                             'User-Agent': 'relay-readback/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read(), tok
    except urllib.error.HTTPError as e:
        return e.code, e.read(), tok


def main():
    at = utc()
    st, body, tok = get()
    out = ['b747 -- (R357)(5): THE ZENODO v1.2.0 DRAFT READ BACK, ONE GET, NO WRITE (%s)' % at, '',
           '### GET %s : HTTP %d ; %d bytes ; the token from the environment, in the Authorization header alone, printed nowhere' % (URL, st, len(body))]
    if st != 200:
        out.append('### ### **HTTP %d: NOTHING READ BACK; NO RETRY IN THIS RUN.**' % st)
        print(NL.join(out))
        sys.exit(3)
    d = json.loads(body.decode('utf-8'))
    m = d.get('metadata') or {}
    files = d.get('files') or []
    desc = m.get('description') or ''
    text = html.unescape(re.sub(r'<[^>]+>', '\n', desc))
    first = next((l.strip() for l in text.split('\n') if l.strip()), '')
    creators = m.get('creators') or []
    out += ['', '## THE RECORD',
            '  deposition id            %s' % d.get('id'),
            '  concept record id        %s' % d.get('conceptrecid'),
            '  state                    %s' % d.get('state'),
            '  submitted                %s' % d.get('submitted'),
            '  version                  %s' % m.get('version'),
            '  title                    %s' % m.get('title'),
            '  publication date         %s' % m.get('publication_date'),
            '  creators                 %d ; author\'s fields present' % len(creators),
            '  description              %d characters (HTML as served) ; its opening line: %s' % (len(desc), first[:300]),
            '', '## THE FILES (%d), name ; size in bytes ; md5' % len(files)]
    for f in files:
        out.append('  %-60s %10s  %s' % (f.get('filename'), f.get('filesize'), (f.get('checksum') or '').replace('md5:', '')))
    out += ['', '## THE RELATED IDENTIFIERS (%d)' % len(m.get('related_identifiers') or [])]
    for r in m.get('related_identifiers') or []:
        out.append('  %s ; %s ; %s' % (r.get('relation'), r.get('scheme'), r.get('identifier')))
    # the comparison with the live line
    reg = pp_line('REGISTRY.md', 83)
    rdm = pp_line('README.md', 164)
    names = [f.get('filename') or '' for f in files]
    mono = [n for n in names if n.startswith('A_Place_to_Stand')]
    ed = re.findall(r'v(\d+)_(\d+)(?:_(\d+))?', mono[0]) if mono else []
    ed_s = ('v' + '.'.join(x for x in ed[0] if x)) if ed else 'NONE READ'
    rows = [
        ('the record`s concept', 'concept 10.5281/zenodo.19675355 (REGISTRY :83 "concept 19675355"; README :164)', str(d.get('conceptrecid')),
         str(d.get('conceptrecid')) == '19675355' and '19675355' in reg and '19675355' in rdm),
        ('the deposit stands at v1.1.2', 'Zenodo v1.1.2 deposited, "Nothing deposits" (REGISTRY :83; README :164)',
         'state %s, submitted %s' % (d.get('state'), d.get('submitted')),
         d.get('submitted') is False and d.get('state') != 'done' and 'v1.1.2' in reg and 'v1.1.2' in rdm),
        ('the version string', 'the deposited version v1.1.2 (REGISTRY :83; README :164)', str(m.get('version')), m.get('version') == 'v1.1.2'),
        ('the monograph edition against the deposit', 'manuscript v5.10.2 (REGISTRY :83; README :164)', ed_s, ed_s == 'v5.10.2'),
        ('the monograph edition against the live line', 'the live monograph v5.18 (REGISTRY :83 "v5.18"; README :164)', ed_s, ed_s == 'v5.18'),
        ('the title', 'A Place to Stand (REGISTRY :83)', str(m.get('title')), 'A Place to Stand' in str(m.get('title'))),
    ]
    out += ['', '## THE COMPARISON WITH THE LIVE LINE (REGISTRY.md :83, row d1-1, and README.md :164, read at PLACE-papers HEAD)']
    for k, want, got, ok in rows:
        out.append('  %-44s %-8s the line: %s ; the draft: %s' % (k, 'AGREES' if ok else 'DIFFERS', want, got))
    na = sum(1 for r in rows if r[3])
    out += ['', '### ### **THE DRAFT %s READ BACK: STATE %s, VERSION %s, %d FILES, %d RELATED IDENTIFIERS ; ROWS %d: %d AGREE, %d DIFFER ; UNTOUCHED.**' % (
        DEP, d.get('state'), m.get('version'), len(files), len(m.get('related_identifiers') or []), len(rows), na, len(rows) - na)]
    text_out = NL.join(out) + NL
    if tok.encode('utf-8') in text_out.encode('utf-8'):
        sys.exit('### REFUSED: the token`s bytes are in the composed bank; nothing written or printed')
    print(text_out)
    print('  the token`s bytes in the bank: 0 ; in the response: %d' % body.count(tok.encode('utf-8')))
    if '--bank' in sys.argv:
        open(BANK, 'w', encoding='utf-8', newline='\n').write(text_out)
        print('written data/b747_zenodo_readback.txt')


if __name__ == '__main__':
    main()
