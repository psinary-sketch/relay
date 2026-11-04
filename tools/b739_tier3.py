# -*- coding: utf-8 -*-
"""b739_tier3.py -- (R349)(3): THE TIER 3 ACT, THE FIVE CURRENCY NOTES [104]-[108] WRITTEN TO THEIR ZENODO RECORDS, ONE RECORD PER RUN.

The route is b727's (tools/b727_sitting.py zenodo(), data/b727_sitting.txt [13]-[19]): actions/edit on the published deposition, the
description field alone set to the description as read with the note appended at its end, every other metadata field compared unmoved
before the publish (else DISCARDED, nothing edited), actions/publish, which edits the record in place: no file, no new version.

  record N      N in 104..108: (a) the note read verbatim from data/b736_sitting.txt at its row and its md5 checked; (b) the description read
                back anonymously before the edit, banked, its md5 printed; (c) the edit; (d) the record read back anonymously after it: the note
                found once at the end, other metadata, files, record DOI version, banked in data/b739_zenodo_readback.json; (e) the row in
                data/b739_tier3.txt. Any failure at (b)-(d): the act stops at the record, the rows before it standing, nothing retried.
  notes         (a) alone for all five, nothing read remotely, nothing written.
  bank          rewrites data/b739_tier3.txt from data/b739_tier3.json.

The token is read from the environment (ZENODO_TOKEN) and is never printed, banked or passed to any call but the Authorization header.
The rows must be run in order: a record is refused while the row before it is not PASS.
"""
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b739_worklist as K          # noqa: E402

SITTING = os.path.join(D, 'b736_sitting.txt')
ROWS = os.path.join(D, 'b739_tier3.json')
TEXT = os.path.join(D, 'b739_tier3.txt')
ZBANK = os.path.join(D, 'b739_zenodo_readback.json')
# ### the note md5s printed at step zero (data/b739_stepzero.txt), each checked before its record is touched
NOTE_MD5 = {104: 'aeb06a150c4e8bbc26e59acc9b1ce7c2', 105: '35b984c3f95e2266a22f082bb2e42c5d', 106: '5fbaa631b275023daf1b79f6f7d26778',
            107: 'ed8576a1c697545dc905b4217c63154e', 108: '9835de85fd3e6fd7ccdbfbbef648ff60'}
TIER3 = dict((n, (kernel, rec, line)) for n, kernel, rec, line in K.TIER3)
# ### the author's word at the [108] prompts (data/b739_amendments.json rows 1-2): b727's [18] note stands as 21520474's foot; of the [108]
# ### note only sentences (4)-(5), the two not in b727's note, are appended after it, verbatim
B727_SITTING = os.path.join(D, 'b727_sitting.txt')
B727_LINE = 164
FRAGMENT_ROWS = (108,)


def b727_note():
    with open(B727_SITTING, encoding='utf-8') as fh:
        L = fh.read().replace(chr(13), '').split(NL)
    l = L[B727_LINE - 1]
    if not l.startswith('  DRAFT WRITTEN: ') or 'Zenodo 10.5281/zenodo.21520474' not in L[B727_LINE - 5]:
        sys.exit('### data/b727_sitting.txt :%d is not [18]`s note on 21520474 -- NOTHING READ' % B727_LINE)
    return l[len('  DRAFT WRITTEN: '):]


def appended(n, t):
    """the text appended at the end: the note, or for [108] the note less b727's [18] note, its sentences (4)-(5)."""
    if n not in FRAGMENT_ROWS:
        return t, None
    b = b727_note()
    if not t.startswith(b + ' '):
        sys.exit('### [%d]: the note does not open with b727`s [18] note -- NOTHING READ' % n)
    frag = t[len(b) + 1:]
    k = len(re.findall(r'[.](?=\s|$)', frag))
    if k != 2:
        sys.exit('### [%d]: the fragment holds %d sentences, not the two of the author`s word -- NOTHING READ' % (n, k))
    return frag, b


def now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def plain(desc):
    """the description as a reader meets it: entities unescaped, tags dropped, spaces folded."""
    t = re.sub(r'<[^>]+>', ' ', html.unescape(desc or ''))
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()


def note(n):
    """(a): the DRAFT WRITTEN line of row [n] at its line in data/b736_sitting.txt, verbatim; its md5 against step zero's."""
    kernel, rec, line = TIER3[n]
    with open(SITTING, encoding='utf-8') as fh:
        L = fh.read().replace(chr(13), '').split(NL)
    head = L[line - 1]
    if not head.startswith('[%d] PASS' % n) or ('Zenodo record %s' % rec) not in L[line]:
        sys.exit('### [%d]: data/b736_sitting.txt :%d is not the row of record %s -- NOTHING READ' % (n, line, rec))
    dl = [l for l in L[line:line + 8] if l.startswith('  DRAFT WRITTEN: ')]
    if len(dl) != 1:
        sys.exit('### [%d]: %d DRAFT WRITTEN lines in the row, not one -- NOTHING READ' % (n, len(dl)))
    t = dl[0][len('  DRAFT WRITTEN: '):]
    if md5(t) != NOTE_MD5[n]:
        sys.exit('### [%d]: the note`s md5 %s is not step zero`s %s -- NOTHING READ' % (n, md5(t), NOTE_MD5[n]))
    return t, line + [i for i, l in enumerate(L[line:line + 8], 1) if l.startswith('  DRAFT WRITTEN: ')][0]


def http(url, method='GET', body=None, token=None):
    h = {'User-Agent': 'relay-b739', 'Accept': 'application/json'}
    if token:
        h['Authorization'] = 'Bearer ' + token
    if body is not None:
        h['Content-Type'] = 'application/json'
    req = urllib.request.Request(url, method=method, headers=h, data=None if body is None else json.dumps(body).encode('utf-8'))
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            t = r.read().decode('utf-8')
            return r.status, json.loads(t) if t else {}
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', 'replace')[:600]


def anon(rec):
    st, j = http('https://zenodo.org/api/records/%s' % rec)
    if st != 200:
        return None, '%s %s' % (st, str(j)[:300])
    return j, None


WITHHELD = '[WITHHELD]'


def withhold(text):
    """### b739 defect (l), N5: the description as banked, each identifier of the author it carries (the four the address scan reads, held in
    memory, none printed) replaced by WITHHELD; the md5 banked beside it is the description's as read, so the record can be checked against it."""
    import b739_address_scan as SCAN
    out, k = text, 0
    for ident in (SCAN.previous_address(), SCAN.author_name(), SCAN.author_orcid(), SCAN.previous_username()):
        pat = re.compile(re.escape(ident), re.I)
        k += len(pat.findall(out))
        out = pat.sub(WITHHELD, out)
    return out, k


def redact():
    """rewrites data/b739_zenodo_readback.json with every banked description withheld as withhold() reads it; the md5s untouched."""
    z = load(ZBANK)
    tot = 0
    for n in sorted(z):
        for side in ('before', 'after'):
            r = z[n].get(side)
            if r and 'description' in r:
                r['description'], k = withhold(r['description'])
                r['withheld'] = r.get('withheld', 0) + k
                tot += k
    put(ZBANK, z)
    print('  data/b739_zenodo_readback.json: %d identifier occurrence(s) withheld across %d rows ; md5s as read' % (tot, len(z)))


def load(p):
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}


def put(p, obj):
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(obj, ensure_ascii=False, indent=1) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def stop(n, rows, row, why):
    row.update(state='STOPPED', why=why, at=now())
    rows[str(n)] = row
    put(ROWS, rows)
    bank()
    sys.exit('### [%d] STOPPED: %s -- the rows before it stand; the author`s word before any retry' % (n, why))


def record(n):
    if n not in TIER3:
        sys.exit('usage: b739_tier3.py record 104..108')
    rows = load(ROWS)
    for m in sorted(TIER3):
        if m < n and (rows.get(str(m)) or {}).get('state') != 'PASS':
            sys.exit('### [%d] REFUSED: the row [%d] before it is not PASS -- nothing read' % (n, m))
    if (rows.get(str(n)) or {}).get('state') in ('PASS', 'STOPPED'):
        sys.exit('### [%d] REFUSED: the row stands %s -- nothing read' % (n, rows[str(n)]['state']))
    kernel, rec, _line = TIER3[n]
    t, tl = note(n)
    print('  (a) [%d] %s, record %s ; the note at data/b736_sitting.txt :%d, md5 %s, verbatim:' % (n, kernel, rec, tl, md5(t)))
    print('      ' + t)
    row = dict(row=n, kernel=kernel, record=rec, note_line=tl, note_md5=md5(t))
    app, b727 = appended(n, t)
    if b727 is not None:
        row.update(fragment_md5=md5(app), b727_line=B727_LINE, b727_md5=md5(b727))
        print('      the author`s word (data/b739_amendments.json rows 1-2): the opening stands from b727 [18] (data/b727_sitting.txt :%d, md5 %s); appended, sentences (4)-(5), md5 %s:' % (
            B727_LINE, md5(b727), md5(app)))
        print('      ' + app)
    token = os.environ.get('ZENODO_TOKEN')
    if not token:
        sys.exit('### NO ZENODO TOKEN IN THE ENVIRONMENT -- NOTHING READ OR WRITTEN')
    before, err = anon(rec)
    if before is None:
        stop(n, rows, row, 'the anonymous read before the edit: %s' % err)
    bd = before['metadata'].get('description') or ''
    z = load(ZBANK)
    z.setdefault(str(n), {})['before'] = dict(record=rec, at=now(), description=withhold(bd)[0], withheld=withhold(bd)[1], md5=md5(bd), doi=before.get('doi'), version=before['metadata'].get('version'),
                                             files=sorted([f.get('key'), f.get('checksum')] for f in before.get('files', [])))
    put(ZBANK, z)
    row.update(before_md5=md5(bd), before_at=z[str(n)]['before']['at'])
    print('  (b) the description read back anonymously before the edit, banked (data/b739_zenodo_readback.json [%d] before): md5 %s, %d characters ; the text to append in it before: %d' % (
        n, md5(bd), len(bd), plain(bd).count(app)))
    if plain(bd).count(app):
        stop(n, rows, row, 'the text to append already stands in the description before the edit')
    if b727 is not None:
        print('      b727`s [18] note at the foot before: %s' % plain(bd).endswith(b727))
        if not plain(bd).endswith(b727):
            stop(n, rows, row, 'b727`s [18] note is not the foot of the description before the edit')
    base = 'https://zenodo.org/api/deposit/depositions/%s' % rec
    st, j = http(base + '/actions/edit', 'POST', None, token)
    if st not in (200, 201, 202):
        stop(n, rows, row, 'actions/edit: %s %s' % (st, str(j)[:300]))
    st, dep = http(base, 'GET', None, token)
    if st != 200:
        http(base + '/actions/discard', 'POST', None, token)
        stop(n, rows, row, 'the deposition read: %s -- DISCARDED, nothing edited' % st)
    meta = dep['metadata']
    prior = dict(meta)
    raw = meta['description']
    meta['description'] = '%s%s<p>%s</p>' % (raw, NL, html.escape(app, quote=False))
    st, j = http(base, 'PUT', {'metadata': meta}, token)
    if st != 200:
        http(base + '/actions/discard', 'POST', None, token)
        stop(n, rows, row, 'PUT: %s %s -- DISCARDED, nothing edited' % (st, str(j)[:300]))
    st, dep2 = http(base, 'GET', None, token)
    after = dep2['metadata'] if st == 200 else {}
    moved = sorted(k for k in set(prior) | set(after) if k != 'description' and prior.get(k) != after.get(k))
    if st != 200 or moved:
        http(base + '/actions/discard', 'POST', None, token)
        stop(n, rows, row, 'the draft moved other fields %s (read %s) -- DISCARDED, nothing edited' % (moved, st))
    print('  (c) the draft: the description alone set, the %s appended at its end ; the other %d metadata fields unmoved' % (
        'note' if b727 is None else 'fragment', len(prior) - 1))
    st, j = http(base + '/actions/publish', 'POST', None, token)
    if st not in (200, 201, 202):
        stop(n, rows, row, 'actions/publish: %s %s' % (st, str(j)[:300]))
    back = None
    for _ in range(12):
        time.sleep(5)
        back, err = anon(rec)
        if back is not None and plain(back['metadata'].get('description')).endswith(app):
            break
    if back is None:
        stop(n, rows, row, 'the anonymous read after the publish: %s' % err)
    ad = back['metadata'].get('description') or ''
    # ### the appended text found once at the end; for [108] the whole note then stands at the end, b727's [18] note and the fragment in turn
    once, at_end = plain(ad).count(app) == 1, plain(ad).endswith(app) and plain(ad).endswith(t)
    bm, am = dict(before['metadata']), dict(back['metadata'])
    bm.pop('description'), am.pop('description')
    bm.pop('relations', None), am.pop('relations', None)
    same_meta = bm == am
    bf = sorted((f.get('key'), f.get('checksum')) for f in before.get('files', []))
    af = sorted((f.get('key'), f.get('checksum')) for f in back.get('files', []))
    same_id = (before['id'], before['doi'], before['metadata'].get('version')) == (back['id'], back['doi'], back['metadata'].get('version'))
    prefix = plain(ad)[:len(plain(bd))] == plain(bd)
    z = load(ZBANK)
    z[str(n)]['after'] = dict(record=rec, at=now(), description=withhold(ad)[0], withheld=withhold(ad)[1], md5=md5(ad), note_once=once, note_at_end=at_end, before_kept=prefix,
                              other_metadata_equal=same_meta, files_equal=bf == af, record_doi_version_equal=same_id, files=len(af),
                              moved=sorted(k for k in set(bm) | set(am) if bm.get(k) != am.get(k)))
    z[str(n)]['confirmation'] = 'Zenodo %s read back anonymously %s (data/b739_zenodo_readback.json [%d]; other metadata %s, files %s, record DOI version %s)' % (
        rec, z[str(n)]['after']['at'], n, same_meta, bf == af, same_id)
    put(ZBANK, z)
    row.update(after_md5=md5(ad), readback_at=z[str(n)]['after']['at'], note_once=once, note_at_end=at_end, before_kept=prefix,
               other_metadata=same_meta, files=bf == af, record_doi_version=same_id, confirmation=z[str(n)]['confirmation'])
    print('  (d) %s ; the note found once %s, at the end %s ; the description before kept ahead of it %s ; md5 after %s' % (
        z[str(n)]['confirmation'], once, at_end, prefix, md5(ad)))
    if not (once and at_end and prefix and same_meta and bf == af and same_id):
        stop(n, rows, row, 'the read-back after the edit: once %s, at the end %s, before kept %s, other metadata %s (moved %s), files %s, record DOI version %s' % (
            once, at_end, prefix, same_meta, z[str(n)]['after']['moved'], bf == af, same_id))
    row.update(state='PASS', at=now())
    rows[str(n)] = row
    put(ROWS, rows)
    bank()
    print('  (e) the row banked: data/b739_tier3.txt [%d] PASS' % n)


def bank():
    rows = load(ROWS)
    L = ['b739 -- THE TIER 3 ACT, (R349)(3): THE CURRENCY NOTES [104]-[108] WRITTEN TO THEIR ZENODO RECORDS, ONE RECORD PER MESSAGE (%s)' % now(), '',
         '### rows are records, in the ruling`s order; each: the row, the record, the note`s md5 (data/b736_sitting.txt, verbatim), the description`s md5 before and after,',
         '### the read-back time and its confirmation (data/b739_zenodo_readback.json). The route b727`s (data/b727_sitting.txt [13]-[19]): the description field alone,',
         '### the note appended at its end, no file, no new version, no other field; the token by env, in no bank. A row that fails stops the act at it.', '']
    for n in sorted(TIER3):
        r = rows.get(str(n))
        kernel, rec, _line = TIER3[n]
        if not r:
            L += ['[%d] NOT RUN' % n, '  RECORD: Zenodo %s (%s)' % (rec, kernel), '']
            continue
        L += ['[%d] %s' % (n, r['state']), '  RECORD: Zenodo %s (%s), the end of the description' % (rec, kernel),
              '  NOTE: data/b736_sitting.txt :%d, md5 %s' % (r['note_line'], r['note_md5'])]
        if r.get('fragment_md5'):
            L += ['  APPENDED, ON THE AUTHOR`S WORD (data/b739_amendments.json rows 1-2): the note`s sentences (4)-(5), md5 %s ; its opening three sentences stand from b727 [18] at data/b727_sitting.txt :%d (md5 %s), the record`s foot before the edit' % (
                r['fragment_md5'], r['b727_line'], r['b727_md5'])]
        L += [
              '  DESCRIPTION BEFORE: md5 %s (read %s)' % (r.get('before_md5'), r.get('before_at')),
              '  DESCRIPTION AFTER: md5 %s' % r.get('after_md5'),
              '  READ BACK: %s' % r.get('readback_at'),
              '  CONFIRMATION: %s ; the note once %s, at the end %s, the description before kept %s' % (r.get('confirmation'), r.get('note_once'), r.get('note_at_end'), r.get('before_kept'))]
        if r['state'] != 'PASS':
            L += ['  STOPPED: %s' % r.get('why')]
        L += ['  AT: %s' % r.get('at'), '']
    n_pass = sum(1 for n in TIER3 if (rows.get(str(n)) or {}).get('state') == 'PASS')
    stopped = [n for n in sorted(TIER3) if (rows.get(str(n)) or {}).get('state') == 'STOPPED']
    L += ['### ### **TIER 3: %d OF FIVE NOTES WRITTEN AND READ BACK ; STOPPED %s ; NOT RUN %d ; NO NEW VERSION, NO FILE, NO OTHER FIELD.**' % (
        n_pass, ', '.join('[%d]' % n for n in stopped) or 'NONE', sum(1 for n in TIER3 if str(n) not in rows))]
    with open(TEXT, 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['record'] and len(a) == 2:
        record(int(a[1]))
    elif a[:1] == ['notes']:
        for n in sorted(TIER3):
            t, tl = note(n)
            print('[%d] %s %s :%d md5 %s' % (n, TIER3[n][0], TIER3[n][1], tl, md5(t)))
    elif a[:1] == ['bank']:
        bank()
    elif a[:1] == ['redact']:
        redact()
    else:
        sys.exit(__doc__)
