# -*- coding: utf-8 -*-
"""b576_zenodo.py -- COMPONENT 1, THE lv DESCRIPTION ANSWERED BY APPEND, (R186)(2), BY THE (R110) ROUTE. ### **THE TOKEN IS READ HERE AND
### NOWHERE WRITTEN.**

### `python tools/b576_zenodo.py draft|c0|c1|c2`
### ### Carried from relay `tools/b535_zenodo.py` (b535's form of the route): **THE TOKEN** is read from the environment
### variable at call time, sent only in the `Authorization` header, never printed, logged, banked or passed on a command line.
### Every printed or banked text passes `clean()`, and every bank is REFUSED if the token is found in it before writing.
### b499's sequence (edit, PUT with every other key carried, publish, ANONYMOUS fetch-back) and its recovery (discard) are
### carried. Carried from b575 for one record: the found sentence (the description's last, "Repository: ...") is replaced
### by itself, the paragraph's close and a new paragraph carrying E-2026-09-25-3's two replacement sentences, ERRATA :564's
### then :567's (reading (ii) of the sealed face, as the author ruled before the seal).
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
RESULTS = os.path.join(D, 'b576_zenodo_results.json')
API = 'https://zenodo.org/api'
ORDER = ('21539068',)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'b95e5c0'
NL = chr(10)
L = []
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### READING (v): each insertion -- (tag, record, the start phrase of the sentence the two follow).
INS = [
    ('Z21539068-E', '21539068', 'Repository: github.com/psinary-sketch/SIDE-lv-conservation'),
]
ERR_LINES = (564, 567)
TOKVAR = 'ZENODO' + '_TOKEN'


def _tok():
    return os.environ.get(TOKVAR) or ''


def clean(s):
    t = _tok()
    s = s if isinstance(s, str) else str(s)
    return s.replace(t, '[TOKEN REDACTED]') if t else s


def rec(s=''):
    s = clean(s)
    L.append(s)
    print(s)


def bank_bytes(name, b):
    t = _tok().encode('utf-8')
    if t and t in b:
        rec('### ### **REFUSED TO BANK %s: THE TOKEN STRING IS IN IT.**' % name)
        raise SystemExit(3)
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    return hashlib.sha256(b).hexdigest()


def bank(name):
    bank_bytes(name, (NL.join(L) + NL).encode('utf-8'))
    print('  written: %s' % name)


def merge(cells):
    R = json.loads(io.open(RESULTS, encoding='utf-8').read()) if os.path.exists(RESULTS) else {}
    R.update(cells)
    bank_bytes(os.path.basename(RESULTS), (json.dumps(R, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def utc():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def http(method, url, body=None, auth=True):
    h = {'User-Agent': 'relay-b576/1.0 (psinary-sketch)', 'Accept': 'application/json'}
    if auth:
        h['Authorization'] = 'Bearer ' + _tok()
    data = None
    if body is not None:
        data = json.dumps(body, ensure_ascii=False).encode('utf-8')
        h['Content-Type'] = 'application/json'
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def sentence_end_after(desc, i):
    """### the first sentence end at or after index i: a `.` followed by whitespace, `<`, or the end."""
    m = re.compile(r'\.(?=\s|<|$)').search(desc, i)
    return m.end() if m else None


def span_of(desc, start):
    c = desc.count(start)
    if c != 1:
        return None, c
    i = desc.find(start)
    j = sentence_end_after(desc, i + len(start) - 1)
    if j is None or re.search(r'</?p\b', desc[i:j]):
        return None, -1
    return (i, j), 1


def _ceiling_sentence(line):
    for opener in ("Supportable, the author's sentence: *", 'Supportable, the author’s sentence: *', 'Supportable: *', ':** *'):
        a = line.find(opener)
        if a >= 0:
            b = line.find('*', a + len(opener))
            return line[a + len(opener):b] if b > 0 else line[a + len(opener):]
    return None


def draft():
    """### The two sentences read from ERRATA :564 and :567 at PLACE-papers b95e5c0, each between its row's quotation marks."""
    rec('=' * 104)
    rec('b576 COMPONENT 1, STEP D -- THE TEXT FROM ERRATA. ### **NOTHING IS WRITTEN AT ZENODO IN THIS STEP.**')
    rec('=' * 104)
    er = subprocess.run(['git', '-C', PP, 'show', PRE_PP + ':ERRATA.md'], capture_output=True).stdout.decode('utf-8').split(NL)
    out, ok = [], True
    for n in ERR_LINES:
        l = er[n - 1]
        m = re.search(r'replacement: \*"(.*)"\*\s*$', l)
        s_ = m.group(1) if m else ''
        bad = [c for c in '<>&' if c in s_]
        ok = ok and bool(s_) and not bad and s_.endswith('.')
        out.append(s_)
        rec('')
        rec('### ERRATA :%d at %s -- a replacement row: %s ; HTML-special characters %s' % (n, PRE_PP, bool(m), bad or 'NONE'))
        rec('    ERRATA   | %s' % l.strip())
        rec('    sentence | %s' % s_)
    rec('')
    rec('### E-2026-09-25-3`s rows they answer: :562 ("Rather than leaving that clause as prose ...") and :565 ("The one deliberately '
        'open obligation ..."), both left standing on the record.')
    rec('### ### **THE TWO SENTENCES READ FROM ERRATA: %s.**' % ok)
    bank_bytes('b576_intended_meta.json', (json.dumps(dict(sentences=out, ok=ok, lines=list(ERR_LINES)), indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    merge(dict(draft=dict(ok=ok)))
    bank('b576_zenodo_draft.txt')
    return 0 if ok else 2


def c0():
    rec('=' * 104)
    rec('b576 COMPONENT 1, STEP 0 -- THE TOKEN, PRESENT AND NOT SHOWN.')
    rec('=' * 104)
    t = _tok()
    rec('    %s set : %s ; length %d' % (TOKVAR, bool(t), len(t)))
    if not t:
        rec('    ### ### **STOP -- THE TOKEN IS NOT SET.**')
        merge(dict(c0=dict(set=False)))
        bank('b576_zenodo_c0.txt')
        return 2
    st, b = http('GET', API + '/deposit/depositions/21539068')
    title = None
    try:
        title = json.loads(b.decode('utf-8'))['metadata']['title']
    except Exception:
        pass
    rec('    GET /api/deposit/depositions/21539068 : ### **HTTP %d** ; title : %s' % (st, title))
    ok = st == 200
    rec('    ### ### **%s**' % ('200 -- THE ACT PROCEEDS.' if ok else 'NOT 200 -- STOP.'))
    merge(dict(c0=dict(set=True, length=len(t), status=st, title=title, proceed=ok)))
    bank('b576_zenodo_c0.txt')
    return 0 if ok else 2


def c1():
    R = json.loads(io.open(RESULTS, encoding='utf-8').read())
    if not (R.get('draft') or {}).get('ok') or not (R.get('c0') or {}).get('proceed'):
        print('### THE DRAFT CHECK OR STEP 0 DID NOT CLEAR -- STEP 1 REFUSES TO RUN.')
        return 2
    SA, SB = json.loads(io.open(os.path.join(D, 'b576_intended_meta.json'), encoding='utf-8').read())['sentences']
    prior = {r: json.loads(io.open(os.path.join(D, 'b575_fetch_%s.json' % r), encoding='utf-8').read()) for r in ORDER}
    rec('=' * 104)
    rec('b576 COMPONENT 1, STEP 1 -- THE PLAN, DRY. ### **NOTHING IS WRITTEN AT ZENODO IN THIS STEP.**')
    rec('=' * 104)
    rec('### THE CALL, PREPARED, the token redacted:')
    for rid in ORDER:
        for m, u in (('POST', '/actions/edit'), ('PUT', ''), ('POST', '/actions/publish')):
            rec('    %-4s %s/deposit/depositions/%s%s ; Authorization: Bearer [TOKEN REDACTED]%s' % (
                m, API, rid, u, ' ; body {"metadata": <every key as fetched, description replaced>}' if m == 'PUT' else ''))
        rec('    GET  %s/records/%s ; no Authorization header (the fetch-back)' % (API, rid))
    before, plan, stop = {}, [], False
    for rid in ORDER:
        st, b = http('GET', API + '/deposit/depositions/' + rid)
        h = bank_bytes('b576_before_%s.json' % rid, b)
        d = json.loads(b.decode('utf-8'))
        before[rid] = d
        md = d.get('metadata') or {}
        desc = md.get('description') or ''
        same = desc == ((prior[rid].get('metadata') or {}).get('description') or '')
        rec('')
        rec('### RECORD %s -- HTTP %d ; banked `b576_before_%s.json` sha256 %s ; state %s ; description %d chars ; equal to b575`s '
            'anonymous fetch : %s' % (rid, st, rid, h[:16], d.get('state'), len(desc), same))
        if st != 200 or not same:
            stop = True
            continue
        for tag, r, start in [x for x in INS if x[1] == rid]:
            sp, c = span_of(desc, start)
            row = dict(tag=tag, record=rid, start=start, count=c)
            if sp is None:
                stop = True
                row.update(found=False)
                rec('    [%s] start phrase found %d time(s) or its span crosses a paragraph : ### **STOP**' % (tag, c))
            else:
                old = desc[sp[0]:sp[1]]
                new = old + '</p>' + NL + '<p>' + SA + ' ' + SB
                row.update(found=True, span=list(sp), old=old, new=new)
                rec('    [%s] ### **FOUND ONCE** ; the description`s last sentence, whole:' % tag)
                rec('         | %s' % old)
                rec('         its replacement (the sentence, the paragraph`s close, the new paragraph):')
                rec('         | %s' % new)
            plan.append(row)
    intended = {}
    for rid in ORDER:
        desc = ((before.get(rid) or {}).get('metadata') or {}).get('description') or ''
        for p in sorted([p for p in plan if p['record'] == rid and p.get('found')], key=lambda p: p['span'][0], reverse=True):
            desc = desc[:p['span'][0]] + p['new'] + desc[p['span'][1]:]
        intended[rid] = desc
    bank_bytes('b576_intended.json', (json.dumps(intended, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    once = sum(1 for p in plan if p.get('found'))
    rec('')
    rec('    ### ### **SPANS FOUND ONCE : %d of %d** ; ### **%s**' % (once, len(INS), 'NO STOP -- STEP 2 MAY WRITE.' if not stop and once == len(INS)
                                                                    else 'STOP BEFORE ANY WRITE.'))
    merge(dict(c1=dict(plan=plan, once=once, stop=bool(stop or once != len(INS)))))
    bank('b576_zenodo_c1.txt')
    return 2 if (stop or once != len(INS)) else 0


def c2():
    R = json.loads(io.open(RESULTS, encoding='utf-8').read())
    if (R.get('c1') or {}).get('stop') is not False:
        print('### STEP 1 DID NOT CLEAR -- STEP 2 REFUSES TO RUN.')
        return 2
    if R.get('c2'):
        print('### STEP 2 HAS ALREADY RUN -- IT DOES NOT RUN TWICE.')
        return 2
    intended = json.loads(io.open(os.path.join(D, 'b576_intended.json'), encoding='utf-8').read())
    plan = R['c1']['plan']
    rec('=' * 104)
    rec('b576 COMPONENT 1, STEP 2 -- THE WRITE, ONE RECORD.')
    rec('=' * 104)
    out = {}
    for rid in ORDER:
        before = json.loads(io.open(os.path.join(D, 'b576_before_%s.json' % rid), encoding='utf-8').read())
        want = intended[rid]
        cell = dict(record=rid)
        base = API + '/deposit/depositions/' + rid
        rec('')
        rec('### RECORD %s' % rid)
        st, b = http('POST', base + '/actions/edit')
        cell['edit'] = st
        rec('    POST actions/edit    : ### **%d** (expect 201) at %s' % (st, utc()))
        if st != 201:
            rec('    | %s' % clean(b.decode('utf-8', 'replace'))[:600])
            rec('    ### ### **STOP.** Nothing was changed on this record.')
            out[rid] = cell
            break
        md = dict(before['metadata'])
        keys_before = sorted(md)
        md['description'] = want
        carried = all(md[k] == before['metadata'][k] for k in md if k != 'description')
        cell.update(other_keys_carried=carried, keys_same=(sorted(md) == keys_before))
        st, b = http('PUT', base, body={'metadata': md})
        cell['put'] = st
        rec('    PUT metadata         : ### **%d** (expect 200) ; every other key carried %s' % (st, carried))
        pub_body = b''
        if st == 200:
            st2, pub_body = http('POST', base + '/actions/publish')
            cell['publish'] = st2
            rec('    POST actions/publish : ### **%d** (expect 202) at %s' % (st2, utc()))
        if st != 200 or cell.get('publish') != 202:
            rec('    | %s' % clean((pub_body or b).decode('utf-8', 'replace'))[:800])
            sd, _ = http('POST', base + '/actions/discard')
            cell['discard'] = sd
            rec('    ### ### **THE RECOVERY: POST actions/discard : %d. STOP.**' % sd)
            out[rid] = cell
            break
        got, tries = None, []
        for n in range(6):
            fs, fb = http('GET', API + '/records/' + rid, auth=False)
            at = utc()
            try:
                gj = json.loads(fb.decode('utf-8'))
                gd = (gj.get('metadata') or {}).get('description')
            except Exception:
                gj, gd = None, None
            tries.append(dict(n=n + 1, status=fs, at=at, identical=(gd == want)))
            rec('    fetch-back try %d at %s : HTTP %d ; description byte-identical to the intended : %s' % (n + 1, at, fs, gd == want))
            if fs == 200 and gd == want:
                got = (fb, gj, at)
                break
            time.sleep(10)
        cell['tries'] = tries
        if got is None:
            fb2 = fb if fs == 200 else b''
            if fb2:
                cell['fetchback_sha256'] = bank_bytes('b576_fetchback_%s.json' % rid, fb2)
            import difflib
            dd = list(difflib.unified_diff(want.split('. '), (gd or '').split('. '), 'intended', 'fetched-back', lineterm='', n=0))
            rec('    ### the diff, sentence by sentence:')
            for x in dd[:40]:
                rec('    | %s' % x[:400])
            rec('    ### ### **NO FETCH-BACK BYTE-IDENTICAL IN SIX TRIES -- MISMATCH PRINTED, STOP. THE ACT IS HELD AT (R186)(2).**')
            cell['match'] = False
            out[rid] = cell
            break
        fb, gj, at = got
        cell['fetchback_at'] = at
        cell['fetchback_sha256'] = bank_bytes('b576_fetchback_%s.json' % rid, fb)
        gd = gj['metadata']['description']
        rows = []
        for p in [p for p in plan if p['record'] == rid]:
            m = gd.count(p['new']) == 1 and gd == want
            rows.append(dict(tag=p['tag'], match=m))
            rec('    [%s] ### **%s**' % (p['tag'], 'MATCH' if m else 'MISMATCH'))
            rec('         the fetched-back paragraph`s inserted text: | %s' % p['new'][len(p['old']):].strip())
        cell.update(rows=rows, match=all(r['match'] for r in rows), same_id=(str(gj.get('id')) == rid),
                    version=(gj.get('metadata') or {}).get('version'),
                    files_same=(sorted(f.get('checksum', '') for f in before.get('files') or []) ==
                                sorted(('md5:' + (f.get('checksum') or '').split(':')[-1]) if not str(f.get('checksum', '')).startswith('md5:')
                                       else f.get('checksum') for f in (gj.get('files') or []))))
        rec('    banked `b576_fetchback_%s.json` sha256 %s ; same record id %s ; version %s ; files unchanged %s'
            % (rid, cell['fetchback_sha256'], cell['same_id'], cell['version'], cell['files_same']))
        out[rid] = cell
    allm = all((out.get(r) or {}).get('match') for r in ORDER) and len(out) == len(ORDER)
    rec('')
    rec('    ### ### **%s**' % ('MATCH.' if allm else 'NOT MATCHED -- THE ACT IS HELD AT (R186)(2); SEE ABOVE.'))
    merge(dict(c2=dict(records=out, all_match=allm)))
    bank('b576_zenodo_c2.txt')
    return 0 if allm else 2


if __name__ == '__main__':
    sys.exit({'draft': draft, 'c0': c0, 'c1': c1, 'c2': c2}[sys.argv[1]]())
