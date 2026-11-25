# -*- coding: utf-8 -*-
"""tools/b769_zenodo.py -- b769, (R379)(6): THE DEPOSITED RECORDS READ BACK. Nothing is written to Zenodo; no method but GET is reachable
from this file. Written by the Write tool and committed before its run (N2).

  ids        no network: the record ids REGISTRY names at the papers` repository's HEAD, read by the rule below, each with its lines and
             forms; the ids the records route will ask; its planted control. Writes nothing.
  records    THE RECORDS, by the route of tools/b726_zenodo_read.py: one anonymous GET of each public record the ids route gives, at
             zenodo.org/api/records/<id>, no token and no identity in any header (the User-Agent the generic reader's), two seconds
             between; kept, as b726 kept them, the title, version, publication date, description and notes, with the DOI, the concept id
             and the count of files beside; the creators dropped; the author's name and ORCID masked in every string; a record that does
             not answer printed and banked with its status and asked again by nothing at this act. Bank: data/b769_zenodo_read.json. The
             route refuses where the bank stands already: one GET a record at this act.
  draft      THE DRAFT 23228113, by the route of tools/b747_zenodo.py: one GET at zenodo.org/api/deposit/depositions/23228113 with the
             token read from the environment inside this process, sent in the Authorization header alone and printed nowhere; its state,
             version, files by name, size and md5, and its description's length and opening line; the creators as a count; where it does
             not answer, its status, asked again by nothing at this act. Bank: data/b769_draft_read.txt, refused where the token's bytes
             stand in it. The route refuses where the bank stands already.

THE IDS RULE: REGISTRY at HEAD, each line rule [Q] protects (its section and two lines either side of a line carrying the protected word,
as tools/b769_registry_block.py reads them) cited and not read; an id of six to nine digits after 10.5281/zenodo. or zenodo.org/records/
(form A), or of seven to nine after an ellipsis, REGISTRY's abbreviation of a DOI in its lineage notes (form C), or of seven to nine
with zenodo, record, concept or doi within the 40 characters before it (form B; the word deposit alone does not count: REGISTRY :95
carries a kernel's peeled commit of seven digits beside it). The draft's id is read by the draft route alone.

No PLACE-papers line is printed; the protected word is derived in memory, never printed; no git write.
"""
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

T = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b769_rulings as RU              # noqa: E402
import b766_registry_cells as R66      # noqa: E402
import b761_registry as R61            # noqa: E402

ACT, NL, PP, D = RU.ACT, RU.NL, RU.PP, RU.D
sha, git, utc, die, put = RU.sha, RU.git, RU.utc, RU.die, RU.put
DRAFT = '23228113'
UA = 'Mozilla/5.0 (literature reader)'
RBANK = os.path.join(D, 'b769_zenodo_read.json')
DBANK = os.path.join(D, 'b769_draft_read.txt')
B726 = ('19937590', '19938917', '21539167', '21539068', '21520474', '21436282')   # ### b726's six (tools/b726_zenodo_read.py :23), printed beside
KEEP = ('title', 'version', 'publication_date', 'description', 'notes')
FA = re.compile(r'(?:10\.5281/zenodo\.|zenodo\.org/(?:records?|deposit|uploads)/)(\d{6,9})\b')
FC = re.compile(r'(?:…|\.\.\.)(\d{7,9})(?![\w])')
FB = re.compile(r'(?<![\w.])(\d{7,9})(?![\w])')
WORDS = ('zenodo', 'record', 'concept', 'doi')


def scan(lines, P):
    ids = {}
    for k, l in enumerate(lines, 1):
        if k in P:
            continue
        for f, rx in (('A', FA), ('C', FC)):
            for m in rx.finditer(l):
                d = ids.setdefault(m.group(1), dict(lines=[], forms=[]))
                if k not in d['lines']:
                    d['lines'].append(k)
                if f not in d['forms']:
                    d['forms'].append(f)
        for m in FB.finditer(l):
            if any(w in l[max(0, m.start() - 40):m.start()].lower() for w in WORDS):
                d = ids.setdefault(m.group(1), dict(lines=[], forms=[]))
                if k not in d['lines']:
                    d['lines'].append(k)
                if 'B' not in d['forms']:
                    d['forms'].append('B')
    return ids


def registry_ids():
    base = RU.at_head(RU.REG)
    L = base.split(NL)[:-1]
    qw = R61.qword(L)
    Q = R66.q_section(L)
    WL = [k for k, l in enumerate(L, 1) if re.search(r'\b%s\b' % re.escape(qw), l, re.I)]
    P = Q | set(x for w in WL for x in range(max(1, w - 2), min(len(L), w + 2) + 1))
    ids = scan(L, P)
    head = git(PP, 'rev-parse', '--short=8', 'HEAD').strip()
    plant = scan(['the record 10.5281/zenodo.12345678 and its lineage (`…23456789`), deposit at 3456789, a commit `8537763`'], set())
    ctl = ('a planted line gives form A 12345678 and form C 23456789, and neither the deposit`s 3456789 nor the commit 8537763: %s' % sorted(plant),
           sorted(plant) == ['12345678', '23456789'])
    asked = [i for i in sorted(ids, key=lambda x: ids[x]['lines'][0]) if i != DRAFT]
    return dict(ids=ids, asked=asked, head=head, lines=len(L), protected=len(P), ctl=ctl, qw=qw)


def show_ids(R):
    print('## THE IDS REGISTRY NAMES at the papers` repository`s HEAD %s (lines %d, %d protected and not read): %d' % (R['head'], R['lines'], R['protected'], len(R['ids'])))
    for i in sorted(R['ids'], key=lambda x: R['ids'][x]['lines'][0]):
        d = R['ids'][i]
        print('  %s forms %s ; lines %d %s%s' % (i, ''.join(d['forms']), len(d['lines']), ', '.join(':%d' % k for k in d['lines'][:8]),
                                              ' ; THE DRAFT, read by the draft route alone' if i == DRAFT else ''))
    print('## b726`s six beside: %s' % ', '.join('%s %s' % (i, 'named' if i in R['ids'] else 'NOT NAMED') for i in B726))
    print('## THE CONTROL: %s %s' % (R['ctl'][0], 'AS WANTED' if R['ctl'][1] else 'NOT AS WANTED'))
    print('## THE RECORDS TO ASK, one GET each: %d -- %s' % (len(R['asked']), ', '.join(R['asked'])))


GH = re.compile(r'(?i)(?:https?://)?(?:www\.)?github\.com/[^\s"\'<>()\]]*')


def masker(I, acct):
    """the author's name, ORCID and address, the account and any link to the repository host masked, each case set aside; (text, count)."""
    def m(s):
        n = 0
        s, k = GH.subn('[a repository link]', s)
        n += k
        for v, w in ((I['name'], '[the author]'), (I['orcid'], '[the author`s ORCID]'), (I['address'], '[an address]'), (acct, '[the account]')):
            if v:
                s, k = re.subn(re.escape(v), w, s, flags=re.I)
                n += k
        return s, n
    return m


def leaks(text, I, acct):
    return [k for k, v in RU.idcount(text, I, acct).items() if v > 0]


def get(url, token=None):
    h = {'User-Agent': UA, 'Accept': 'application/json'}
    if token:
        h['Authorization'] = 'Bearer ' + token
    req = urllib.request.Request(url, method='GET', headers=h)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read(), time.time() - t0
    except urllib.error.HTTPError as e:
        return e.code, e.read(), time.time() - t0
    except Exception as e:   # ### a record that does not answer: its status printed, asked again by nothing
        return 0, ('%s' % type(e).__name__).encode('utf-8'), time.time() - t0


def records():
    if os.path.exists(RBANK):
        die('data/b769_zenodo_read.json STANDS: ONE GET A RECORD AT THIS ACT; NOTHING ASKED')
    R = registry_ids()
    show_ids(R)
    if not R['ctl'][1]:
        die('THE IDS RULE`S CONTROL NOT AS WANTED; NOTHING ASKED')
    I = RU.ids()
    acct = RU.account()
    mk = masker(I, acct)
    pm, pn = mk('by %s (%s), the account %s, see https://github.com/%s/SIDE-kernel' % (I['name'], I['orcid'], acct, acct))
    if leaks(pm, I, acct) or pn < 3:
        die('THE MASK`S PLANTED LINE NOT MASKED WHOLE (%d masked); NOTHING ASKED' % pn)
    print('## THE MASK: a planted line naming the author, the ORCID, the account and a link to its repository masked whole (%d masked, 0 surviving) AS WANTED' % pn)
    rows = []
    for i in R['asked']:
        st, body, secs = get('https://zenodo.org/api/records/' + i)
        if st == 0 and not rows:
            die('THE FIRST ASK REACHED NO SERVER (%s): NO HTTP STATUS, SO NO RECORD WAS READ; NOTHING BANKED' % body.decode('utf-8', 'replace'))
        row = dict(id=i, forms=R['ids'][i]['forms'], lines=R['ids'][i]['lines'], status=st, seconds=round(secs, 2), masked=0)
        if st == 200:
            o = json.loads(body.decode('utf-8'))
            m = o.get('metadata') or {}
            row.update(doi=o.get('doi'), conceptrecid=o.get('conceptrecid'), files=len(o.get('files') or []))
            for k in KEEP:
                s = m.get(k)
                if isinstance(s, str):
                    s, n = mk(s)
                    row['masked'] += n
                    row[k] = s
            print('## %s HTTP 200 %.2f s: v%s %s | %s (concept %s, files %d, masked %d)' % (
                i, secs, row.get('version'), row.get('publication_date'), row.get('title'), row.get('conceptrecid'), row['files'], row['masked']))
        else:
            row['answer'] = 'DID NOT ANSWER: HTTP %s; asked again by nothing at this act' % st
            print('## %s HTTP %s %.2f s: DID NOT ANSWER; ASKED AGAIN BY NOTHING AT THIS ACT' % (i, st, secs))
        if leaks(json.dumps(row, ensure_ascii=False), I, acct):
            for k in KEEP:
                row.pop(k, None)
            row['dropped'] = 'title, version, date, description and notes dropped: an identifier survived the mask'
            print('   %s: AN IDENTIFIER SURVIVED THE MASK; ITS KEPT FIELDS DROPPED FROM THE BANK' % i)
        rows.append(row)
        time.sleep(2)
    ok = sum(1 for r in rows if r['status'] == 200)
    J = dict(read_utc=utc(), act=ACT, route='tools/b769_zenodo.py records, by tools/b726_zenodo_read.py`s route', pp_head=R['head'],
             user_agent=UA, asked=len(rows), answered=ok, not_answering=[r['id'] for r in rows if r['status'] != 200], rows=rows)
    t = json.dumps(J, indent=1, ensure_ascii=False) + NL
    bad = [k for k, v in RU.idcount(t, I, acct).items() if v > 0]
    if bad:
        die('AN IDENTIFIER SURVIVES THE MASK (%s)' % ', '.join(bad))
    put(RBANK, t)
    print('### ### **THE PUBLIC RECORDS READ BACK: ASKED %d, ANSWERED %d%s ; NOTHING WRITTEN TO ZENODO ; WRITTEN data/b769_zenodo_read.json.**' % (
        len(rows), ok, (' ; NOT ANSWERING ' + ', '.join(J['not_answering'])) if J['not_answering'] else ''))


def draft():
    if os.path.exists(DBANK):
        die('data/b769_draft_read.txt STANDS: ONE GET OF THE DRAFT AT THIS ACT; NOTHING ASKED')
    at = utc()
    tok = os.environ.get('ZENODO_TOKEN') or ''
    url = 'https://zenodo.org/api/deposit/depositions/' + DRAFT
    out = ['b769 -- (R379)(6): THE DRAFT %s READ BACK, ONE GET, NO WRITE (%s), by the route of tools/b747_zenodo.py' % (DRAFT, at), '']
    if len(tok) < 20:
        out += ['### NO TOKEN IN THE ENVIRONMENT: NOTHING ASKED; ASKED AGAIN BY NOTHING AT THIS ACT', '',
                '### ### **THE DRAFT %s NOT READ: NO TOKEN ; NOTHING WRITTEN TO ZENODO.**' % DRAFT]
        text = NL.join(out) + NL
        print(text)
        put(DBANK, text)
        print('written data/b769_draft_read.txt')
        return
    st, body, secs = get(url, tok)
    if st == 0:
        die('THE ASK REACHED NO SERVER (%s): NO HTTP STATUS, SO THE DRAFT WAS NOT READ; NOTHING BANKED' % body.decode('utf-8', 'replace'))
    out.append('### GET %s : HTTP %s ; %d bytes ; %.2f s ; the token from the environment, in the Authorization header alone, printed nowhere' % (url, st, len(body), secs))
    if st != 200:
        out += ['', '### ### **THE DRAFT %s: HTTP %s ; NOTHING READ BACK ; ASKED AGAIN BY NOTHING AT THIS ACT ; NOTHING WRITTEN TO ZENODO.**' % (DRAFT, st)]
    else:
        I = RU.ids()
        mk = masker(I, RU.account())
        d = json.loads(body.decode('utf-8'))
        m = d.get('metadata') or {}
        files = d.get('files') or []
        desc = m.get('description') or ''
        text_ = html.unescape(re.sub(r'<[^>]+>', '\n', desc))
        first, _n = mk(next((l.strip() for l in text_.split('\n') if l.strip()), ''))
        title, _n2 = mk(str(m.get('title')))
        out += ['', '## THE DRAFT',
                '  deposition id            %s' % d.get('id'),
                '  concept record id        %s' % d.get('conceptrecid'),
                '  state                    %s' % d.get('state'),
                '  submitted                %s' % d.get('submitted'),
                '  version                  %s' % m.get('version'),
                '  title                    %s' % title,
                '  creators                 %d ; author`s fields present' % len(m.get('creators') or []),
                '  description              %d characters (HTML as served) ; its opening line: %s' % (len(desc), first[:300]),
                '', '## THE FILES (%d), name ; size in bytes ; md5' % len(files)]
        for f in files:
            out.append('  %-60s %10s  %s' % (f.get('filename'), f.get('filesize'), (f.get('checksum') or '').replace('md5:', '')))
        out += ['', '### ### **THE DRAFT %s READ BACK: STATE %s, VERSION %s, %d FILES ; NOTHING WRITTEN TO ZENODO.**' % (
            DRAFT, d.get('state'), m.get('version'), len(files))]
    I, acct = RU.ids(), RU.account()
    tb = tok.encode('utf-8')
    for k, l in enumerate(out):
        if tb in l.encode('utf-8') or leaks(l, I, acct):
            out[k] = '  [a line dropped: the token`s bytes or an identifier stood in it]'
    text = NL.join(out) + NL
    if tb in text.encode('utf-8') or leaks(text, I, acct):
        die('THE TOKEN`S BYTES OR AN IDENTIFIER IN THE COMPOSED BANK')
    print(text)
    print('  the token`s bytes in the bank: 0')
    put(DBANK, text)
    print('written data/b769_draft_read.txt')


if __name__ == '__main__':
    m = sys.argv[1] if len(sys.argv) > 1 else ''
    if m == 'ids':
        show_ids(registry_ids())
    elif m == 'records':
        records()
    elif m == 'draft':
        draft()
    else:
        sys.exit(__doc__)
