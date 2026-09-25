# -*- coding: utf-8 -*-
"""b535_zenodo.py -- COMPONENT 3, THE PLATFORM EDITS OF (R145)(4). ### **THE TOKEN IS READ HERE AND NOWHERE WRITTEN.**

### `python tools/b535_zenodo.py c0|c1|c2`
### ### **THE TOKEN** is read from `os.environ['ZENODO_TOKEN']` at call time, sent only in the `Authorization` header, never
### printed, logged, banked or passed on a command line. Every printed or banked text passes `clean()`, and every bank is
### REFUSED if the token is found in it before writing. b499`s sequence (edit, PUT with every other key carried, publish,
### ANONYMOUS fetch-back) and its recovery (discard) are carried; the spans are READING (4)`s of the sealed face.
"""
import hashlib
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
RESULTS = os.path.join(D, 'b535_zenodo_results.json')
API = 'https://zenodo.org/api'
ORDER = ('21520474', '21539167')
NL = chr(10)
L = []
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### READING (4): each replacement -- (tag, record, start phrase, whole-old flag, new text in the record`s own HTML).
KERNEL_NEW = ("SIDE-kernel: the machine-verified architecture of the SIDE programme's route terminals. Its Route 3 premise is RH "
              "restated (E-2026-09-25-1); the programme's standing reduction is Weil positivity on classK, equivalent to RH on the "
              "kernel's zero configuration, compiled both ways in SIDE-explicit-formula v0.1.")
REPL = [
    ('Z21520474-01', '21520474',
     'SIDE-kernel: the machine-verified architecture of the SIDE reduction of the Riemann Hypothesis to a single located clause.',
     KERNEL_NEW),
    ('Z21520474-02', '21520474',
     'and ConservationBridge.riemann_hypothesis (the compiled exclusion syllogism',
     "and ConservationBridge.riemann_hypothesis (the compiled implication from ConservationHypothesis, which the kernel's own "
     "balance_theorem shows is RH restated &mdash; E-2026-09-25-1)."),
    ('Z21539167-01', '21539167',
     'the third is the compiled implication from the named interface ConservationHypothesis',
     "the third is the compiled implication from ConservationHypothesis, which the kernel's own balance_theorem shows is RH "
     "restated, E-2026-09-25-1)."),
]


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
    bank_bytes(os.path.basename(RESULTS), (json.dumps(R, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def http(method, url, body=None, auth=True):
    h = {'User-Agent': 'relay-b535/1.0 (psinary-sketch)', 'Accept': 'application/json'}
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


def c0():
    rec('=' * 104)
    rec('b535 COMPONENT 3, STEP 0 -- THE TOKEN, PRESENT AND NOT SHOWN.')
    rec('=' * 104)
    t = _tok()
    rec('    ZENODO_TOKEN set : %s ; length %d' % (bool(t), len(t)))
    if not t:
        rec('    ### ### **STOP -- THE TOKEN IS NOT SET.**')
        merge(dict(c0=dict(set=False)))
        bank('b535_zenodo_c0.txt')
        return 2
    st, b = http('GET', API + '/deposit/depositions/21520474')
    title = None
    try:
        title = json.loads(b.decode('utf-8'))['metadata']['title']
    except Exception:
        pass
    rec('    GET /api/deposit/depositions/21520474 : ### **HTTP %d** ; title : %s' % (st, title))
    ok = st == 200
    rec('    ### ### **%s**' % ('200 -- THE ACT PROCEEDS.' if ok else 'NOT 200 -- STOP.'))
    merge(dict(c0=dict(set=True, length=len(t), status=st, title=title, proceed=ok)))
    bank('b535_zenodo_c0.txt')
    return 0 if ok else 2


def c1():
    rec('=' * 104)
    rec('b535 COMPONENT 3, STEP 1 -- THE PLAN, DRY. ### **NOTHING IS WRITTEN AT ZENODO IN THIS STEP.**')
    rec('=' * 104)
    before, plan, stop = {}, [], False
    for rid in ORDER:
        st, b = http('GET', API + '/deposit/depositions/' + rid)
        h = bank_bytes('b535_before_%s.json' % rid, b)
        d = json.loads(b.decode('utf-8'))
        before[rid] = d
        md = d.get('metadata') or {}
        desc = md.get('description') or ''
        rec('')
        rec('### RECORD %s -- HTTP %d ; banked `b535_before_%s.json` sha256 %s ; state %s ; description %d chars'
            % (rid, st, rid, h[:16], d.get('state'), len(desc)))
        if st != 200:
            stop = True
            continue
        for tag, r, start, new in [x for x in REPL if x[1] == rid]:
            sp, c = span_of(desc, start)
            row = dict(tag=tag, record=rid, start=start, new=new, count=c)
            if sp is None:
                stop = True
                row.update(found=False)
                rec('    [%s] start phrase found %d time(s) or its span crosses a paragraph : ### **STOP**' % (tag, c))
            else:
                row.update(found=True, span=list(sp), old=desc[sp[0]:sp[1]])
                rec('    [%s] ### **FOUND ONCE** ; the old span, whole:' % tag)
                rec('         | %s' % desc[sp[0]:sp[1]])
                rec('         the new text:')
                rec('         | %s' % new)
            plan.append(row)
    intended = {}
    for rid in ORDER:
        desc = ((before.get(rid) or {}).get('metadata') or {}).get('description') or ''
        for p in sorted([p for p in plan if p['record'] == rid and p.get('found')], key=lambda p: p['span'][0], reverse=True):
            desc = desc[:p['span'][0]] + p['new'] + desc[p['span'][1]:]
        intended[rid] = desc
    bank_bytes('b535_intended.json', (json.dumps(intended, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    once = sum(1 for p in plan if p.get('found'))
    rec('')
    rec('    ### ### **SPANS FOUND ONCE : %d of %d** ; ### **%s**' % (once, len(REPL), 'NO STOP -- STEP 2 MAY WRITE.' if not stop and once == len(REPL)
                                                                     else 'STOP BEFORE ANY WRITE.'))
    merge(dict(c1=dict(plan=plan, once=once, stop=bool(stop or once != len(REPL)))))
    bank('b535_zenodo_c1.txt')
    return 2 if (stop or once != len(REPL)) else 0


def c2():
    R = json.loads(io.open(RESULTS, encoding='utf-8').read())
    if (R.get('c1') or {}).get('stop') is not False:
        print('### STEP 1 DID NOT CLEAR -- STEP 2 REFUSES TO RUN.')
        return 2
    intended = json.loads(io.open(os.path.join(D, 'b535_intended.json'), encoding='utf-8').read())
    plan = R['c1']['plan']
    rec('=' * 104)
    rec('b535 COMPONENT 3, STEP 2 -- THE WRITES, ONE RECORD AT A TIME, THE MONOGRAPH LAST.')
    rec('=' * 104)
    out = {}
    for rid in ORDER:
        before = json.loads(io.open(os.path.join(D, 'b535_before_%s.json' % rid), encoding='utf-8').read())
        want = intended[rid]
        cell = dict(record=rid)
        base = API + '/deposit/depositions/' + rid
        rec('')
        rec('### RECORD %s' % rid)
        st, b = http('POST', base + '/actions/edit')
        cell['edit'] = st
        rec('    POST actions/edit    : ### **%d** (expect 201)' % st)
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
            rec('    POST actions/publish : ### **%d** (expect 202)' % st2)
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
            try:
                gj = json.loads(fb.decode('utf-8'))
                gd = (gj.get('metadata') or {}).get('description')
            except Exception:
                gj, gd = None, None
            tries.append(dict(n=n + 1, status=fs, identical=(gd == want)))
            rec('    fetch-back try %d : HTTP %d ; description byte-identical to the intended : %s' % (n + 1, fs, gd == want))
            if fs == 200 and gd == want:
                got = (fb, gj)
                break
            time.sleep(10)
        cell['tries'] = tries
        if got is None:
            fb2 = fb if fs == 200 else b''
            if fb2:
                cell['fetchback_sha256'] = bank_bytes('b535_fetchback_%s.json' % rid, fb2)
            rec('    ### ### **NO FETCH-BACK BYTE-IDENTICAL IN SIX TRIES -- MISMATCH PRINTED, STOP.**')
            cell['match'] = False
            out[rid] = cell
            break
        fb, gj = got
        cell['fetchback_sha256'] = bank_bytes('b535_fetchback_%s.json' % rid, fb)
        gd = gj['metadata']['description']
        rows = []
        for p in [p for p in plan if p['record'] == rid]:
            m = gd.count(p['new']) == 1 and p['old'] not in gd and gd == want
            rows.append(dict(tag=p['tag'], match=m))
            rec('    [%s] ### **%s**' % (p['tag'], 'MATCH' if m else 'MISMATCH'))
        cell.update(rows=rows, match=all(r['match'] for r in rows), same_id=(str(gj.get('id')) == rid),
                    files_same=(sorted(f.get('checksum', '') for f in before.get('files') or []) ==
                                sorted(('md5:' + (f.get('checksum') or '').split(':')[-1]) if not str(f.get('checksum', '')).startswith('md5:')
                                       else f.get('checksum') for f in (gj.get('files') or []))))
        rec('    banked `b535_fetchback_%s.json` sha256 %s ; same record id %s' % (rid, cell['fetchback_sha256'], cell['same_id']))
        out[rid] = cell
    allm = all((out.get(r) or {}).get('match') for r in ORDER) and len(out) == len(ORDER)
    rec('')
    rec('    ### ### **%s**' % ('MATCH AT EVERY REPLACEMENT.' if allm else 'NOT ALL MATCHED -- SEE ABOVE.'))
    merge(dict(c2=dict(records=out, all_match=allm)))
    bank('b535_zenodo_c2.txt')
    return 0 if allm else 2


if __name__ == '__main__':
    sys.exit({'c0': c0, 'c1': c1, 'c2': c2}[sys.argv[1]]())
