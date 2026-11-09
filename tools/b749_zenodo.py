"""b749 -- (R359)(2): THE TIER 3 ACT OVER THE HELD ZENODO DRAFT 23228113 AT v1.2.0. ONE REQUEST PER ROUTE, EACH ROUTE ITS OWN COMMAND.

  plan             no request: the plan bank data/b749_tier3_plan.txt, (R359)(2)(i), composed from data/b747_zenodo_readback.txt, data/b747_author_answers.txt,
                   data/b747_zenodo_routes.txt, data/b749_ferry.txt and PLACE-papers REGISTRY.md :83, :983 and README.md :164 at HEAD; banked and committed
                   before any request
  reread           one GET of the draft deposition (the token), compared row by row with b747's read-back: state, version, title, the file list
                   (name, size, md5); a DIFFERS on any of them halts the act (exit 3), nothing deleted; (R359)(2)(iii)
  delete           one DELETE of the unpublished deposition 23228113 (the token), refused unless the re-read is banked with no DIFFERS and the
                   author's PASS at [Z1] is banked with its time (data/b749_author_answers.txt); its status printed and banked; (R359)(2)(iii)
  readback-draft   one GET of the draft's id (the token), its status printed (not found expected); (R359)(2)(iv)
  readback-concept one GET of the public record's latest version (no token): version, publication date, files (name, size, md5) and the
                   creators as a count, "author's fields present"; compared with REGISTRY d1-1 (:83), README :164 and the deposit's 11 files at
                   PLACE-papers outputs/DEPOSITED-v1.1.2/ (md5 of HEAD's blobs) as rows AGREES or DIFFERS; (R359)(2)(iv)

THE TOKEN is read from os.environ['ZENODO_TOKEN'] inside this process, sent only in the Authorization header, never printed, never written;
every bank text is checked for the token's bytes before it is written. No identifier of the author is printed: the creators field is a count.
Each route appends its section to data/b749_zenodo_call.txt (plan writes its own bank). `--dry` on a request route prints the request it
would send and sends nothing.
"""
import datetime
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

DEP = '23228113'
DEPOSIT_RECORD = '21539167'
CONCEPT = '19675355'
URL = 'https://zenodo.org/api/deposit/depositions/' + DEP
PUBLIC = 'https://zenodo.org/api/records/%s/versions/latest' % DEPOSIT_RECORD
PP = 'D:/MY-DOwnloads/PLACE-papers'
RELAY = 'D:/relay'
D = os.path.join(RELAY, 'data')
PLAN = os.path.join(D, 'b749_tier3_plan.txt')
CALL = os.path.join(D, 'b749_zenodo_call.txt')
ANSWERS = os.path.join(D, 'b749_author_answers.txt')
NL = '\n'
UA = 'relay-tier3/1.0'


def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def lines(path):
    return io.open(path, encoding='utf-8').read().replace('\r', '').split(NL)


def pp_lines(rel):
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + rel], capture_output=True, encoding='utf-8')
    if r.returncode != 0:
        sys.exit('### REFUSED: PLACE-papers HEAD:%s resolves to no file' % rel)
    return r.stdout.split(NL)


def token():
    tok = os.environ.get('ZENODO_TOKEN') or ''
    if len(tok) < 20:
        sys.exit('### REFUSED: no token in the environment; nothing sent')
    return tok


def request(method, url, tok=None):
    h = {'Accept': 'application/json', 'User-Agent': UA}
    if tok:
        h['Authorization'] = 'Bearer ' + tok
    req = urllib.request.Request(url, method=method, headers=h)
    t0 = datetime.datetime.now(datetime.timezone.utc)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            st, body = r.status, r.read()
    except urllib.error.HTTPError as e:
        st, body = e.code, e.read()
    secs = (datetime.datetime.now(datetime.timezone.utc) - t0).total_seconds()
    return st, body, secs


def guard_write(path, text, tok=None, append=True):
    if tok and tok.encode('utf-8') in text.encode('utf-8'):
        sys.exit('### REFUSED: the token`s bytes are in the composed bank; nothing written')
    prior = io.open(path, encoding='utf-8').read() if (append and os.path.exists(path)) else ''
    body = prior + ('' if not prior else NL) + text.rstrip(NL) + NL
    with open(path + '.tmp', 'wb') as fh:
        fh.write(body.encode('utf-8'))
    os.replace(path + '.tmp', path)
    print('written %s' % os.path.relpath(path, RELAY).replace(os.sep, '/'))


# ================================================================================ plan, (R359)(2)(i)
def plan():
    rb = lines(os.path.join(D, 'b747_zenodo_readback.txt'))
    aa = lines(os.path.join(D, 'b747_author_answers.txt'))
    rt = lines(os.path.join(D, 'b747_zenodo_routes.txt'))
    fe = lines(os.path.join(D, 'b749_ferry.txt'))
    reg, rdm = pp_lines('REGISTRY.md'), pp_lines('README.md')
    rows = [(n, rb[n - 1]) for n in range(36, 42)]
    differ = [(n, l) for n, l in rows if ' DIFFERS ' in l]
    agree = [(n, l) for n, l in rows if ' AGREES ' in l]
    title = rb[10]
    bad = [w for w, ok in (('rows :36-:41 three DIFFER and three AGREE', len(differ) == 3 and len(agree) == 3),
                           ('the title at :11', title.strip().startswith('title') and 'A Place To Stand: the SIDE reduction' in title),
                           ('the title at :41', 'A Place To Stand: the SIDE reduction of the Riemann Hypothesis to a single located clause' in rb[40]),
                           ('state unsubmitted :8, submitted False :9, :37', 'unsubmitted' in rb[7] and 'False' in rb[8] and 'submitted False' in rb[36]),
                           ('the id 23228113 :6', DEP in rb[5]),
                           ('the answer at :29', aa[28].startswith('Discard (Tier 3 act): the v1.2.0 draft 23228113 discarded')),
                           ('REGISTRY :83 d1-1 with 21539167, 19675355 and v1.1.2', reg[82].startswith('| d1-1 |') and DEPOSIT_RECORD in reg[82] and CONCEPT in reg[82] and 'v1.1.2' in reg[82]),
                           ('REGISTRY :983 d1-1', reg[982].startswith('| d1-1 |')),
                           ('README :164 the deposit note', rdm[163].startswith('**Deposit note') and DEPOSIT_RECORD in rdm[163] and CONCEPT in rdm[163]),
                           ('the ruling (2) at ferry :11', fe[10].startswith('(2) THE TIER 3 ACT')),
                           ('the routes bank :9 NOT FOUND', 'NOT FOUND' in rt[8])) if not ok]
    if bad:
        sys.exit('### REFUSED: THE SOURCES NOT AS READ: %s -- NOTHING COMPOSED' % '; '.join(bad))
    tl = re.sub(r'^\s*title\s+', '', title)
    out = ['b749 -- (R359)(2)(i): THE PLAN OF THE TIER 3 ACT OVER THE HELD ZENODO DRAFT 23228113 AT v1.2.0, BANKED AND COMMITTED BEFORE ANY REQUEST TO THE API (%s)' % utc(), '',
           '### composed by tools/b749_zenodo.py plan from the banks and lines named beside each row; no request sent by this route.', '',
           '## (1) THE THREE DIFFER ROWS OF data/b747_zenodo_readback.txt, VERBATIM WITH THEIR LINE NUMBERS']
    out += ['  :%d %s' % (n, l) for n, l in differ]
    out += ['', '## (2) THE THREE AGREE ROWS OF data/b747_zenodo_readback.txt, VERBATIM WITH THEIR LINE NUMBERS']
    out += ['  :%d %s' % (n, l) for n, l in agree]
    out += ['', '## (3) THE DRAFT, AS THE READ-BACK CARRIES IT',
            '  the title, verbatim (data/b747_zenodo_readback.txt :11; the DIFFER row :41): %s' % tl,
            '  the id: %s (:6) ; the state: unsubmitted (:8) ; submitted: False (:9) ; the row :37 reads "the draft: state unsubmitted, submitted False"' % DEP,
            '  the version v1.2.0 (:10) ; files 14 (:16-:30) ; the related identifier isSupplementTo 10.5281/zenodo.19674312 (:33)', '',
            '## (4) THE RECORDS THIS ACT DOES NOT TOUCH, NAMED BY LINE',
            '  the deposited record %s at Zenodo v1.1.2 (manuscript v5.10.2) and the concept %s: PLACE-papers REGISTRY.md :83 (row d1-1, "PUBLISHED 2026-07-24: Zenodo v1.1.2 (ms v5.10.2), DOI 10.5281/zenodo.21539167 (concept 19675355)")' % (DEPOSIT_RECORD, CONCEPT),
            '  the same row`s version table: REGISTRY.md :983 (d1-1 | `REGISTRY.md:83`)',
            '  README.md :164, the deposit note ("the monograph at manuscript v5.10.2 / Zenodo v1.1.2 ([10.5281/zenodo.21539167] ...; concept [10.5281/zenodo.19675355] ...)")',
            '  no field of either record is read for writing, sent, or changed by this act; the README is not edited (it goes to b750`s sitting, (R359)(2)(v))', '',
            '## (5) THE ONE CALL, BY METHOD AND PATH',
            '  DELETE %s -- the delete of the unpublished deposition %s by its id; the token from the environment, in the Authorization header alone' % (URL, DEP),
            '  before it, on the author`s PASS at [Z1] alone: GET %s, compared row by row with data/b747_zenodo_readback.txt (state, version, title, file list); a DIFFERS on any halts the act with no delete' % URL,
            '  no other method is reachable from tools/b749_zenodo.py: GET and this one DELETE; no POST, PUT or publish action', '',
            '## (6) THE EXPECTED READ-BACK AFTER IT',
            '  GET %s (the token): not found (HTTP 404 or 410 expected), its status printed' % URL,
            '  GET %s (no token, the public record): the latest version still v1.1.2, the record %s, its file list unchanged -- the 11 files whose md5s match the deposit`s copies at PLACE-papers outputs/DEPOSITED-v1.1.2/ (REGISTRY :83, "every file`s md5 matched Zenodo`s published checksum"); the creators field printed as a count, "author`s fields present"' % (PUBLIC, DEPOSIT_RECORD),
            '  each compared with REGISTRY d1-1 (:83) and README :164 as rows AGREES or DIFFERS', '',
            '## (7) THE REASON, AS THE AUTHOR GAVE IT, AND THE NAVIGATOR`S READING BESIDE IT',
            '  the author, at b747`s root (data/b747_author_answers.txt :29, verbatim): %s' % aa[28],
            '  the navigator`s reading, in this ruling (data/b749_ferry.txt :5, :11 and :19, (R359) and (2)(v)): the held draft at v1.2.0 discarded, the deposit at v1.1.2 and the concept unchanged, "a fresh draft to be opened when the 1.5C paper reaches the rubric`s stage"; the one Zenodo write the delete of the unpublished deposition on the author`s word at [Z1]',
            '  the conversation of 2026-11-07: UNBANKED -- the lean toward discarding and the pros and cons were found in no bank line (data/b747_zenodo_routes.txt :9-:19, :29); this plan cites neither', '',
            '### ### **THE PLAN: DIFFER 3 (:%s), AGREE 3 (:%s) ; THE TITLE VERBATIM ; THE DRAFT %s, STATE unsubmitted, SUBMITTED False ; THE RECORDS NOT TOUCHED %s AND %s (REGISTRY :83, :983 ; README :164) ; THE ONE CALL DELETE %s ; NO REQUEST SENT.**' % (
                ', :'.join(str(n) for n, _l in differ), ', :'.join(str(n) for n, _l in agree), DEP, DEPOSIT_RECORD, CONCEPT, DEP)]
    text = NL.join(out)
    print(text)
    if '--bank' in sys.argv:
        guard_write(PLAN, text, append=False)


# ================================================================================ reread, (R359)(2)(iii)
def readback_rows():
    rb = lines(os.path.join(D, 'b747_zenodo_readback.txt'))
    f = {}
    for k, n in (('state', 8), ('submitted', 9), ('version', 10), ('title', 11)):
        f[k] = re.sub(r'^\s*%s\s+' % k, '', rb[n - 1]).strip()
    files = []
    for l in rb[16:30]:
        m = re.match(r'^\s+(\S+)\s+(\d+)\s+([0-9a-f]{32})\s*$', l)
        if m:
            files.append((m.group(1), int(m.group(2)), m.group(3)))
    f['files'] = sorted(files)
    return f


def reread():
    if '--dry' in sys.argv:
        print('DRY: would send GET %s with the token in the Authorization header; nothing sent' % URL)
        return
    if not os.path.exists(PLAN) or subprocess.run(['git', '-C', RELAY, 'ls-files', '--error-unmatch', 'data/b749_tier3_plan.txt'], capture_output=True).returncode != 0:
        sys.exit('### REFUSED: THE PLAN IS NOT BANKED AND COMMITTED (data/b749_tier3_plan.txt); nothing sent')
    tok = token()
    at = utc()
    st, body, secs = request('GET', URL, tok)
    out = ['## THE RE-READ BEFORE THE DELETE, (R359)(2)(iii) (%s)' % at,
           '  GET %s : HTTP %d ; %d bytes ; %.2f s ; the token from the environment, in the Authorization header alone, printed nowhere' % (URL, st, len(body), secs)]
    if st != 200:
        out.append('  ### ### **THE RE-READ: HTTP %d ; HALT -- NO DELETE.**' % st)
        guard_write(CALL, NL.join(out), tok)
        print(NL.join(out))
        sys.exit(3)
    d = json.loads(body.decode('utf-8'))
    m = d.get('metadata') or {}
    got = dict(state=str(d.get('state')), submitted=str(d.get('submitted')), version=str(m.get('version')), title=str(m.get('title')),
               files=sorted((x.get('filename'), int(x.get('filesize') or 0), (x.get('checksum') or '').replace('md5:', '')) for x in d.get('files') or []))
    want = readback_rows()
    rows = []
    for k in ('state', 'submitted', 'version', 'title'):
        rows.append((k, want[k], got[k], want[k] == got[k]))
    rows.append(('the file list (name ; size ; md5), %d files' % len(want['files']), '%d files' % len(want['files']), '%d files' % len(got['files']), want['files'] == got['files']))
    for w_, g_ in zip(want['files'], got['files']):
        if w_ != g_:
            out.append('  ### FILE DIFFERS: read-back %s ; now %s' % (' ; '.join(map(str, w_)), ' ; '.join(map(str, g_))))
    out.append('  the creators: %d ; author`s fields present' % len(m.get('creators') or []))
    out.append('  the comparison with data/b747_zenodo_readback.txt (:8-:11, :17-:30), row by row:')
    for k, w_, g_, ok in rows:
        out.append('    %-44s %-8s the read-back: %s ; now: %s' % (k, 'AGREES' if ok else 'DIFFERS', w_, g_))
    nd = sum(1 for r in rows if not r[3])
    out.append('  ### ### **THE RE-READ: HTTP %d ; ROWS %d: %d AGREE, %d DIFFER ; %s.**' % (st, len(rows), len(rows) - nd, nd, 'THE DELETE MAY RUN ON THE AUTHOR`S PASS' if not nd else 'HALT -- NO DELETE'))
    text = NL.join(out)
    print(text)
    print('  the token`s bytes in the section: 0 ; in the response: %d' % body.count(tok.encode('utf-8')))
    guard_write(CALL, text, tok)
    if nd:
        sys.exit(3)


# ================================================================================ delete, (R359)(2)(iii)
def z1_pass():
    if not os.path.exists(ANSWERS):
        return None
    t = io.open(ANSWERS, encoding='utf-8').read()
    m = re.search(r'^\[Z1\] (PASS) .*?(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z)', t, re.M)
    return m.group(2) if m else None


def delete():
    call = io.open(CALL, encoding='utf-8').read() if os.path.exists(CALL) else ''
    rr = re.findall(r'THE RE-READ: HTTP (\d+) ; ROWS (\d+): (\d+) AGREE, (\d+) DIFFER', call)
    z1 = z1_pass()
    if not rr or rr[-1][0] != '200' or rr[-1][3] != '0':
        sys.exit('### REFUSED: NO RE-READ BANKED WITH HTTP 200 AND NO DIFFERS (data/b749_zenodo_call.txt); nothing sent')
    if not z1:
        sys.exit('### REFUSED: THE AUTHOR`S PASS AT [Z1] IS NOT BANKED WITH ITS TIME (data/b749_author_answers.txt); nothing sent')
    if 'THE DELETE: HTTP' in call:
        sys.exit('### REFUSED: THE DELETE IS BANKED ALREADY; ONE DELETE IN THIS ACT')
    if '--dry' in sys.argv:
        print('DRY: would send DELETE %s with the token in the Authorization header; [Z1] PASS at %s ; nothing sent' % (URL, z1))
        return
    tok = token()
    at = utc()
    st, body, secs = request('DELETE', URL, tok)
    out = ['## THE DELETE, (R359)(2)(iii) (%s)' % at,
           '  on the author`s PASS at [Z1] (data/b749_author_answers.txt, %s) and the re-read with no DIFFERS above' % z1,
           '  DELETE %s : HTTP %d ; %d bytes in the response ; %.2f s ; the token from the environment, in the Authorization header alone, printed nowhere' % (URL, st, len(body), secs),
           '  ### ### **THE DELETE: HTTP %d ; %s.**' % (st, 'DONE (204 No Content)' if st == 204 else 'NOT AS EXPECTED, PRINTED AS RETURNED')]
    text = NL.join(out)
    print(text)
    guard_write(CALL, text, tok)


# ================================================================================ readback-draft, readback-concept, (R359)(2)(iv)
def readback_draft():
    if '--dry' in sys.argv:
        print('DRY: would send GET %s with the token; nothing sent' % URL)
        return
    tok = token()
    at = utc()
    st, body, secs = request('GET', URL, tok)
    out = ['## THE READ-BACK OF THE DRAFT`S ID AFTER THE DELETE, (R359)(2)(iv) (%s)' % at,
           '  GET %s : HTTP %d ; %d bytes ; %.2f s ; the token in the Authorization header alone' % (URL, st, len(body), secs),
           '  ### ### **THE DRAFT %s: HTTP %d ; %s.**' % (DEP, st, 'NOT FOUND, AS EXPECTED' if st in (404, 410) else 'NOT AS EXPECTED')]
    text = NL.join(out)
    print(text)
    guard_write(CALL, text, tok)


def deposit_md5s():
    out = {}
    r = subprocess.run(['git', '-C', PP, 'ls-files', 'outputs/DEPOSITED-v1.1.2/'], capture_output=True, encoding='utf-8')
    for rel in [x for x in r.stdout.split(NL) if x]:
        b = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + rel], capture_output=True).stdout
        out[rel.split('/')[-1]] = (len(b), hashlib.md5(b).hexdigest())
    return out


def readback_concept():
    if '--dry' in sys.argv:
        print('DRY: would send GET %s with no token; nothing sent' % PUBLIC)
        return
    at = utc()
    st, body, secs = request('GET', PUBLIC)
    out = ['## THE READ-BACK OF THE CONCEPT`S PUBLIC RECORD AFTER THE DELETE, NO TOKEN, (R359)(2)(iv) (%s)' % at,
           '  GET %s : HTTP %d ; %d bytes ; %.2f s ; no token sent' % (PUBLIC, st, len(body), secs)]
    if st != 200:
        out.append('  ### ### **THE CONCEPT`S RECORD: HTTP %d ; NOTHING READ BACK.**' % st)
        text = NL.join(out)
        print(text)
        guard_write(CALL, text)
        sys.exit(3)
    d = json.loads(body.decode('utf-8'))
    m = d.get('metadata') or {}
    files = d.get('files')
    if isinstance(files, dict):
        files = list((files.get('entries') or {}).values())
    fl = sorted(((x.get('key') or x.get('filename')), int(x.get('size') or x.get('filesize') or 0), (x.get('checksum') or '').replace('md5:', '')) for x in (files or []))
    ver, pub, rid, crid = str(m.get('version')), str(m.get('publication_date')), str(d.get('id')), str(d.get('conceptrecid'))
    out += ['  the record id: %s ; the concept: %s ; the latest version: %s ; the publication date: %s' % (rid, crid, ver, pub),
            '  the creators: %d ; author`s fields present' % len(m.get('creators') or []),
            '  the files (%d), name ; size in bytes ; md5:' % len(fl)]
    out += ['    %-60s %10d  %s' % f for f in fl]
    reg, rdm = pp_lines('REGISTRY.md')[82], pp_lines('README.md')[163]
    dep = deposit_md5s()
    md5s_dep = sorted(v[1] for v in dep.values())
    md5s_now = sorted(f[2] for f in fl)
    rows = [('the latest version is v1.1.2', 'Zenodo v1.1.2 (REGISTRY :83; README :164)', ver, ver in ('v1.1.2', '1.1.2') and 'v1.1.2' in reg and 'v1.1.2' in rdm),
            ('the latest record is the deposit %s' % DEPOSIT_RECORD, 'DOI 10.5281/zenodo.21539167 (REGISTRY :83; README :164)', rid, rid == DEPOSIT_RECORD and DEPOSIT_RECORD in reg and DEPOSIT_RECORD in rdm),
            ('the concept', 'concept 19675355 (REGISTRY :83; README :164)', crid, crid == CONCEPT and CONCEPT in reg and CONCEPT in rdm),
            ('the publication date', 'PUBLISHED 2026-07-24 (REGISTRY :83)', pub, pub == '2026-07-24' and 'PUBLISHED 2026-07-24' in reg),
            ('the file list unchanged: md5s against the 11 deposited copies', '%d files at PLACE-papers outputs/DEPOSITED-v1.1.2/ (REGISTRY :83)' % len(dep), '%d files' % len(fl), md5s_now == md5s_dep and len(fl) == 11)]
    out.append('  the comparison with REGISTRY d1-1 (:83), README :164 and the deposit`s copies, at PLACE-papers HEAD:')
    for k, w_, g_, ok in rows:
        out.append('    %-60s %-8s the line: %s ; the record: %s' % (k, 'AGREES' if ok else 'DIFFERS', w_, g_))
    nd = sum(1 for r in rows if not r[3])
    out.append('  ### ### **THE CONCEPT`S RECORD: HTTP %d ; LATEST %s, RECORD %s, %d FILES ; ROWS %d: %d AGREE, %d DIFFER ; UNCHANGED %s.**' % (st, ver, rid, len(fl), len(rows), len(rows) - nd, nd, 'YES' if not nd else 'NO'))
    text = NL.join(out)
    print(text)
    guard_write(CALL, text)


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = {'plan': plan, 'reread': reread, 'delete': delete, 'readback-draft': readback_draft, 'readback-concept': readback_concept}.get(r)
    if fn is None:
        sys.exit(__doc__)
    fn()
