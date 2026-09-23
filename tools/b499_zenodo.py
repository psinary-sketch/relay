# -*- coding: utf-8 -*-
"""b499_zenodo.py -- COMPONENTS 0, 1 AND 2. ### **THE TOKEN IS READ HERE AND NOWHERE WRITTEN.**

### `python tools/b499_zenodo.py c0|c1|c2`
### ### **THE TOKEN** is read from `os.environ['ZENODO_TOKEN']` at call time, sent only in the
### `Authorization` header, and never printed, logged, banked or passed on a command line. ### Every
### text this tool prints or banks passes `clean()`, which replaces the token string if it ever
### appears, and every bank is REFUSED if the token is found in it before writing.
### ### **THE SEALED RULES** of the face -- the EXTENT rule, the RECOVERY and the MATCH rule -- are
### implemented here as the face states them, and each is named where it is used.
"""
import difflib
import hashlib
import html
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
INPUT = os.path.join(D, 'zenodo_edits_2026-09-23_v2.txt')
RESULTS = os.path.join(D, 'b499_results.json')
API = 'https://zenodo.org/api'
ORDER = ('21539068', '21520474', '21539167')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def _tok():
    return os.environ.get('ZENODO_TOKEN') or ''


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
    with open(os.path.join(D, name), 'wb') as fh:
        fh.write(b)
    return hashlib.sha256(b).hexdigest()


def bank(name):
    bank_bytes(name, (NL.join(L) + NL).encode('utf-8'))
    print('  written: %s' % name)


def merge(cells):
    R = json.loads(io.open(RESULTS, encoding='utf-8').read()) if os.path.exists(RESULTS) else {}
    R.update(cells)
    bank_bytes('b499_results.json', (json.dumps(R, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def http(method, url, body=None, auth=True):
    """### ### **RETURNS `(status, raw_bytes)`**; never raises on an HTTP status."""
    h = {'User-Agent': 'relay-b499/1.0 (psinary-sketch)', 'Accept': 'application/json'}
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


# ------------------------------------------------------------------------------ the banked input
def parse_input():
    """### The ten replacements, read from the BANKED copy in relay, between `----` lines."""
    txt = io.open(INPUT, encoding='utf-8').read().replace(chr(13), '')
    out = []
    record = None
    lines = txt.split(NL)
    i = 0
    while i < len(lines):
        l = lines[i]
        m = re.match(r'^=+ RECORD (\d+) ', l)
        if m:
            record = m.group(1)
        m = re.match(r'^\[(\d+)\] (.*)$', l)
        if m:
            n, head = int(m.group(1)), m.group(2)
            j = lines.index('----', i + 1)
            k = lines.index('----', j + 1)
            text = NL.join(lines[j + 1:k])
            if head.startswith('TITLE'):
                kind, start = 'title', None
            else:
                kind = 'description'
                start = re.search(r'the sentence beginning "(.*)" ->', head, re.I).group(1)
            out.append(dict(n=n, record=record, kind=kind, start=start, text=text))
            i = k
        i += 1
    return out


# ------------------------------------------------------------------------------ the sealed rules
def sentence_ends(s):
    """### A sentence end: a `.` followed by whitespace, by `<`, or by the end of the string."""
    return [m.end() for m in re.finditer(r'\.(?=\s|<|$)', s)]


def extent(desc, start, replacement):
    """### ### **THE EXTENT RULE, AS SEALED.** ### The span begins at the start phrase and ends at the
    ### K-th sentence end after it, K = the sentence ends in the REPLACEMENT. ### A span crossing a
    ### `<p>` or `</p>` is refused (returned as None with a reason)."""
    i = desc.find(start)
    k = len(sentence_ends(replacement))
    ends = [e for e in sentence_ends(desc[i:])]
    if len(ends) < k or k == 0:
        return None, k, 'fewer than K sentence ends after the start'
    span = desc[i:i + ends[k - 1]]
    if re.search(r'</?p\b', span):
        return None, k, 'the span crosses a paragraph tag'
    return (i, i + ends[k - 1]), k, ''


def text_of(h):
    """### "text": tags removed, entities decoded, whitespace runs collapsed."""
    t = re.sub(r'<[^>]+>', ' ', h or '')
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()


ENTITY = re.compile(r'&(?:#\d+|#[xX][0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]*);')


# ================================================================================================ c0
def c0():
    rec('=' * 104)
    rec('COMPONENT 0 -- THE TOKEN, PRESENT AND NOT SHOWN.')
    rec('=' * 104)
    t = _tok()
    rec('    ZENODO_TOKEN set : %s' % bool(t))
    rec('    ### ### **LENGTH : %d** ; ### **SHA256 PREFIX : %s**'
        % (len(t), hashlib.sha256(t.encode('utf-8')).hexdigest()[:8] if t else '-'))
    if not t:
        rec('    ### ### **STOP -- THE TOKEN IS NOT SET.**')
        merge(dict(c0=dict(set=False)))
        bank('b499_components_c0.txt')
        return 2
    st, b = http('GET', API + '/deposit/depositions/21539167')
    title = None
    try:
        title = json.loads(b.decode('utf-8'))['metadata']['title']
    except Exception:
        pass
    rec('    GET /api/deposit/depositions/21539167 : ### **HTTP %d**' % st)
    rec('    the record`s current title : %s' % title)
    ok = (st == 200)
    rec('    ### ### **%s**' % ('200 -- THE ACT PROCEEDS.' if ok else 'NOT 200 -- STOP.'))
    rec('=' * 104)
    merge(dict(c0=dict(set=True, length=len(t),
                       prefix=hashlib.sha256(t.encode('utf-8')).hexdigest()[:8],
                       status=st, title=title, proceed=ok)))
    bank('b499_components_c0.txt')
    return 0 if ok else 2


# ================================================================================================ c1
def c1():
    rec('=' * 104)
    rec('COMPONENT 1 -- THE PLAN, DRY. ### **NOTHING IS WRITTEN AT ZENODO IN THIS COMPONENT.**')
    rec('=' * 104)
    targets = parse_input()
    rec('    replacements parsed from the banked input : %d' % len(targets))
    before, plan, stop = {}, [], False
    entities = {}
    for rid in ORDER:
        st, b = http('GET', API + '/deposit/depositions/' + rid)
        h = bank_bytes('b499_before_%s.json' % rid, b)
        d = json.loads(b.decode('utf-8'))
        before[rid] = d
        md = d.get('metadata') or {}
        desc = md.get('description') or ''
        ents = ENTITY.findall(desc)
        entities[rid] = len(ents)
        rec('')
        rec('### RECORD %s -- HTTP %d ; banked `b499_before_%s.json` sha256 %s' % (rid, st, rid, h[:16]))
        rec('-' * 104)
        rec('    state %s ; submitted %s ; title : %s' % (d.get('state'), d.get('submitted'), md.get('title')))
        rec('    description : %d chars ; ### **ENTITY SITES : %d** %s'
            % (len(desc), len(ents), sorted(set(ents))))
        if st != 200:
            stop = True
            rec('    ### ### **NOT 200 -- STOP.**')
            continue
        for t in [x for x in targets if x['record'] == rid]:
            row = dict(n=t['n'], record=rid, kind=t['kind'], start=t['start'], text=t['text'])
            if t['kind'] == 'title':
                found = 'FOUND ONCE' if 'title' in md else 'NOT FOUND'
                row.update(found=found, old=md.get('title'))
                rec('    [%d] TITLE : ### **%s**' % (t['n'], found))
                rec('         old : %s' % md.get('title'))
                rec('         new : %s' % t['text'])
            else:
                c = desc.count(t['start'])
                found = ('FOUND ONCE' if c == 1 else 'NOT FOUND' if c == 0 else 'FOUND MORE THAN ONCE')
                row.update(found=found, count=c)
                rec('    [%d] "%s" : ### **%s** (%d)' % (t['n'], t['start'], found, c))
                if c == 1:
                    sp, k, why = extent(desc, t['start'], t['text'])
                    row.update(k=k)
                    if sp is None:
                        row.update(found='EXTENT REFUSED', why=why)
                        rec('         ### ### **EXTENT REFUSED : %s** (K = %d)' % (why, k))
                    else:
                        row.update(span=sp, old=desc[sp[0]:sp[1]])
                        rec('         K = %d ; the old span, WHOLE, as the field holds it:' % k)
                        rec('         | %s' % desc[sp[0]:sp[1]])
                        rec('         the replacement:')
                        rec('         | %s' % t['text'])
            if row['found'] != 'FOUND ONCE':
                stop = True
            plan.append(row)

    # ------------------------------------------------------------ the intended texts
    intended = {}
    for rid in ORDER:
        md = (before.get(rid) or {}).get('metadata') or {}
        title, desc = md.get('title'), md.get('description') or ''
        rows = [p for p in plan if p['record'] == rid]
        spans = sorted([p for p in rows if p['kind'] == 'description' and p.get('span')],
                       key=lambda p: p['span'][0], reverse=True)
        for p in spans:
            new = html.escape(p['text'], quote=False)
            desc = desc[:p['span'][0]] + new + desc[p['span'][1]:]
        for p in rows:
            if p['kind'] == 'title':
                title = p['text']
        intended[rid] = dict(title=title, description=desc)
    bank_bytes('b499_intended.json',
               (json.dumps(intended, indent=1, ensure_ascii=False) + NL).encode('utf-8'))

    # ------------------------------------------------------------ S2 and the lv title check
    mono_live = ((before.get('21539167') or {}).get('metadata') or {}).get('description')
    b359 = json.loads(io.open(os.path.join(D, 'b359_fetch_F2.json'), encoding='utf-8').read())

    def find(o, k):
        if isinstance(o, dict):
            for kk, v in o.items():
                if kk == k:
                    yield v
                else:
                    yield from find(v, k)
        elif isinstance(o, list):
            for v in o:
                yield from find(v, k)
    b359d = next(find(b359, 'description'), None)
    same = (mono_live == b359d)
    rec('')
    rec('    the monograph`s live description byte-identical to the b359 bank : ### **%s**' % same)
    lv_old = ((before.get('21539068') or {}).get('metadata') or {}).get('title') or ''
    lv_new = next((p['text'] for p in plan if p['n'] == 10), '')
    rec('    [10] against (R109)`s own words ("proof" replaced by "reduction") : %s'
        % (lv_old.replace('proof', 'reduction') == lv_new))
    once = sum(1 for p in plan if p['found'] == 'FOUND ONCE')
    rec('')
    rec('    ### ### **TARGETS FOUND ONCE : %d of %d** ; entity sites per record : %s'
        % (once, len(plan), entities))
    rec('    ### ### **%s**' % ('NO STOP -- COMPONENT 2 MAY WRITE.' if not stop and once == 10 else
                              'STOP BEFORE ANY WRITE. ### THE AUTHOR`S FILE IS THE OBJECT TO REPAIR.'))
    rec('=' * 104)
    merge(dict(c1=dict(targets=[{k: v for k, v in p.items()} for p in plan], once=once,
                       entities=entities, stop=bool(stop or once != 10),
                       mono_same_as_b359=same,
                       lv_title_is_r109_words=(lv_old.replace('proof', 'reduction') == lv_new))))
    bank('b499_components_c1.txt')
    return 2 if (stop or once != 10) else 0


# ================================================================================================ c2
def c2():
    R = json.loads(io.open(RESULTS, encoding='utf-8').read())
    if (R.get('c1') or {}).get('stop') is not False:
        print('### COMPONENT 1 DID NOT CLEAR -- COMPONENT 2 REFUSES TO RUN.')
        return 2
    intended = json.loads(io.open(os.path.join(D, 'b499_intended.json'), encoding='utf-8').read())
    plan = R['c1']['targets']
    rec('=' * 104)
    rec('COMPONENT 2 -- THE WRITES, ONE RECORD AT A TIME, THE MONOGRAPH LAST.')
    rec('=' * 104)
    out = {}
    for rid in ORDER:
        before = json.loads(io.open(os.path.join(D, 'b499_before_%s.json' % rid), encoding='utf-8').read())
        want = intended[rid]
        cell = dict(record=rid)
        rec('')
        rec('### RECORD %s' % rid)
        rec('-' * 104)
        base = API + '/deposit/depositions/' + rid

        st, b = http('POST', base + '/actions/edit')
        cell['edit'] = st
        rec('    POST actions/edit    : ### **%d** (expect 201)' % st)
        if st != 201:
            rec('    | %s' % clean(b.decode('utf-8', 'replace'))[:600])
            rec('    ### ### **STOP.** ### Nothing was changed on this record.')
            out[rid] = cell
            break

        md = dict(before['metadata'])
        keys_before = sorted(md)
        md['title'] = want['title']
        md['description'] = want['description']
        carried = all(md[k] == before['metadata'][k] for k in md if k not in ('title', 'description'))
        cell.update(keys=keys_before, other_keys_carried=carried, keys_same=(sorted(md) == keys_before))
        st, b = http('PUT', base, body={'metadata': md})
        cell['put'] = st
        rec('    PUT metadata         : ### **%d** (expect 200) ; keys %d, every other key carried %s'
            % (st, len(keys_before), carried))
        pub_body = b''
        if st == 200:
            st2, pub_body = http('POST', base + '/actions/publish')
            cell['publish'] = st2
            rec('    POST actions/publish : ### **%d** (expect 202)' % st2)
        if st != 200 or cell.get('publish') != 202:
            rec('    | %s' % clean((pub_body or b).decode('utf-8', 'replace'))[:800])
            sd, _ = http('POST', base + '/actions/discard')
            cell['discard'] = sd
            rec('    ### ### **THE RECOVERY: POST actions/discard : %d. STOP.**' % sd)
            out[rid] = cell
            break
        try:
            pub = json.loads(pub_body.decode('utf-8'))
            cell['published_id'] = str(pub.get('id') or pub.get('record_id'))
        except Exception:
            cell['published_id'] = None
        rec('    published record id  : %s' % cell['published_id'])

        # -------------------------------------------------- the fetch-back, ANONYMOUS
        got, tries = None, []
        for n in range(6):
            fs, fb = http('GET', API + '/records/' + rid, auth=False)
            try:
                gj = json.loads(fb.decode('utf-8'))
                gt = (gj.get('metadata') or {}).get('title')
            except Exception:
                gj, gt = None, None
            tries.append(dict(n=n + 1, status=fs, title_is_intended=(gt == want['title'])))
            rec('    fetch-back try %d : HTTP %d ; title is the intended one : %s'
                % (n + 1, fs, gt == want['title']))
            if fs == 200 and gt == want['title']:
                got = (fb, gj)
                break
            time.sleep(10)
        cell['tries'] = tries
        if got is None:
            rec('    ### ### **NO FETCH-BACK CARRIED THE INTENDED TITLE IN SIX TRIES -- MISMATCH. STOP.**')
            cell['match'] = False
            out[rid] = cell
            break
        fb, gj = got
        h = bank_bytes('b499_fetchback_%s.json' % rid, fb)
        cell['fetchback_sha256'] = h
        gmd = gj.get('metadata') or {}
        rt, rd = gmd.get('title'), gmd.get('description') or ''
        # -------------------------------------------------- THE MATCH RULE, AS SEALED
        rows = [p for p in plan if p['record'] == rid]
        limb1 = html.unescape(rt or '') == html.unescape(want['title'])
        tx = text_of(rd)
        limb2 = all(tx.count(text_of(html.escape(p['text'], quote=False))) == 1
                    for p in rows if p['kind'] == 'description')
        limb3 = all(text_of(p['old']) not in tx for p in rows if p['kind'] == 'description')
        limb4 = tx == text_of(want['description'])
        raw_same = (rd == want['description'])
        match = limb1 and limb2 and limb3 and limb4
        cell.update(limb1=limb1, limb2=limb2, limb3=limb3, limb4=limb4, raw_same=raw_same,
                    match=match, returned_title=rt,
                    returned_entities=len(ENTITY.findall(rd)),
                    same_id=(str(gj.get('id')) == rid),
                    files_before=sorted((f.get('checksum') or '') for f in before.get('files') or []),
                    files_after=sorted(((f.get('checksum') or '').split(':')[-1])
                                       for f in (gj.get('files') or [])))
        rec('    banked `b499_fetchback_%s.json` sha256 %s' % (rid, h))
        rec('    (i) title exact %s ; (ii) each replacement once %s ; (iii) no old span left %s ;'
            % (limb1, limb2, limb3))
        rec('    (iv) text equal %s ; raw bytes equal %s ; same record id %s'
            % (limb4, raw_same, cell['same_id']))
        rec('    returned title : %s' % rt)
        rec('    ### ### **%s**' % ('MATCH' if match else 'MISMATCH'))
        out[rid] = cell
        if not match:
            for dl in difflib.unified_diff(text_of(want['description']).split('. '),
                                           tx.split('. '), 'intended', 'returned', lineterm='', n=0):
                rec('      ' + dl[:300])
            rec('    ### ### **STOP. THE OTHER RECORDS ARE LEFT UNTOUCHED.**')
            break
    n_match = sum(1 for c in out.values() if c.get('match'))
    rec('')
    rec('    ### ### **FETCH-BACKS THAT MATCH : %d of 3**' % n_match)
    rec('=' * 104)
    merge(dict(c2=dict(records=out, matches=n_match)))
    bank('b499_components_c2.txt')
    return 0 if n_match == 3 else 2


if __name__ == '__main__':
    sys.exit({'c0': c0, 'c1': c1, 'c2': c2}[sys.argv[1]]())
