# -*- coding: utf-8 -*-
"""tools/b759_corpus.py -- (R369)(9): THE CORPUS'S SENTENCES ABOUT THE CONTROL, RE-CUT. "The hold "no sentence of any paper edited" is lifted
for the fourteen lines of BLOCK D and for no other, by the author's word in this delivery. Each line's OLD is read to stand once in its file at
its line. Where it does, it is replaced by its NEW, one PLACE-papers commit a document through the one-call tool. Where it does not, or where the
tool or a standing arm refuses the write, the line is left, the refusal printed, and an order W-ORD-RECUT-<key> entered with the NEW text and the
trigger "the document's next edition". ... A deposited copy of a document is not touched: the act reads REGISTRY's deposit pins for each
document, and the ERRATA entry names the lines that stand otherwise in a deposited copy." (data/b759_ferry.txt :29)

THE LINES: BLOCK D of data/b759_text.txt, each marker `@@ <key> | <path> :<line> | <class>` with its OLD and NEW; a NEW's field (PIN) from
data/b759_fields.json. Each OLD read once in its line at PLACE-papers HEAD and once more in the line as an earlier key on the same line left it.
THE DEPOSIT PINS: REGISTRY at HEAD, each line naming the document's stem and reading PUBLISHED with a Zenodo DOI; the deposited copy is not read
(no Zenodo call) and stands as deposited.
PLACE-papers lines are banked by path, line and sha256 (16 hex) alone; the OLD and NEW are the text block's, a relay bank.

  control            the planted controls
  dry <doc|all>      the replacements composed and printed by key, nothing written
  write <doc>        one document written (its working copy equal to HEAD's blob first), its rows banked; the commit follows by the one-call tool
  confirm <doc>      after the commit: each re-cut line read at PLACE-papers HEAD equal to the line written, the commit read from the log
  bank               data/b759_corpus.txt: every key's state, the deposit pins, the orders entered for lines left, and (9)'s sentence filled
  <doc> is one of: findings simplicity capacity place controlled vocabulary barriers spiral wsc
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b759_worklist as K     # noqa: E402
import figbank as FB          # noqa: E402

ACT = 'b759'
PP = K.PP
NL = '\n'
TEXT = os.path.join(D, 'b759_text.txt')
FERRY = os.path.join(D, 'b759_ferry.txt')
FIELDS = os.path.join(D, 'b759_fields.json')
BANKJ = os.path.join(D, 'b759_corpus.json')
BANK = os.path.join(D, 'b759_corpus.txt')
LBR, RBR = '‹', '›'
DOCS = (('findings', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md'), ('simplicity', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md'),
        ('capacity', 'phase2/formation/CAPACITY.md'), ('place', 'day1/A_Place_to_Stand_v5_17.md'),
        ('controlled', 'phase1.5/experiments/CONTROLLED_EXPERIMENT.md'), ('vocabulary', 'phase1.5/structural/VOCABULARY.md'),
        ('barriers', 'phase1.5/method/INVARIANCE_BARRIERS.md'), ('spiral', 'SPIRAL_MAP.md'), ('wsc', 'day1/Which_Structure_Confines_v2_4_0.md'))
TRIGGER = 'the document`s next edition'


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a, raw=False):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, (r.stdout if raw else r.stdout.decode('utf-8', 'replace'))


def sha16(s):
    return hashlib.sha256(s if isinstance(s, bytes) else s.encode('utf-8')).hexdigest()[:16]


def block_d(text):
    """[(key, path, line, class, old, new)] in the block's order; a part not in its form refuses."""
    out = []
    for i, l in enumerate(text):
        m = re.match(r'^@@ (C\w+) \| (\S+) :(\d+) \| ([A-Z-]+)$', l)
        if not m:
            continue
        o, n = text[i + 1], text[i + 2]
        if not (o.startswith('OLD: ') and n.startswith('NEW: ')):
            raise SystemExit('### BLOCK D`S %s NOT IN ITS FORM -- NOTHING DONE' % m.group(1))
        out.append((m.group(1), m.group(2), int(m.group(3)), m.group(4), o[5:], n[5:]))
    return out


def fill(s, F):
    tag = LBR + 'PIN' + RBR
    if tag in s:
        if not F or not F.get('PIN'):
            return None
        s = s.replace(tag, F['PIN'])
    return None if LBR in s else s


def apply_doc(lines, rows, F):
    """the document's lines with its keys applied in order: (new lines, [(key, line, at v1, at the line as left, state, why)])."""
    new, res = list(lines), []
    for key, _p, ln, _c, old, nw in rows:
        if not 0 < ln <= len(lines):
            res.append((key, ln, 0, 0, 'LEFT', 'the line beyond the file`s %d' % len(lines)))
            continue
        n0, n1 = lines[ln - 1].count(old), new[ln - 1].count(old)
        nf = fill(nw, F)
        if n0 != 1 or n1 != 1:
            res.append((key, ln, n0, n1, 'LEFT', 'the OLD stands %d time(s) in the line at HEAD, %d as an earlier key left it, not once' % (n0, n1)))
        elif nf is None:
            res.append((key, ln, n0, n1, 'LEFT', 'a field of the NEW not filled'))
        else:
            new[ln - 1] = new[ln - 1].replace(old, nf, 1)
            res.append((key, ln, n0, n1, 'RE-CUT', ''))
    return new, res


def deposits(reg_lines):
    """{path: [(REGISTRY line, record)]}: lines naming the document's stem, reading PUBLISHED and a Zenodo DOI."""
    out = {}
    for _k, p in DOCS:
        stem = re.sub(r'_v\d+(?:_\d+)*\.md$', '', p.split('/')[-1]).replace('.md', '')
        out[p] = [(i + 1, m) for i, l in enumerate(reg_lines) if stem in l and 'PUBLISHED' in l
                  for m in re.findall(r'DOI 10\.5281/zenodo\.(\d+)', l)[:1]]
    return out


def load():
    return json.load(io.open(BANKJ, encoding='utf-8')) if os.path.exists(BANKJ) else dict(rows=[], docs=[])


def save(B):
    js = json.dumps(B, indent=1, ensure_ascii=False)
    with open(BANKJ + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(js + NL)
    os.replace(BANKJ + '.tmp', BANKJ)


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    t = ['x', '@@ C1 | a/B.md :2 | SUPERSEDED', 'OLD: old one', 'NEW: new one', '', '@@ C2a | a/B.md :2 | RE-CUT', 'OLD: two', 'NEW: 2 at %sPIN%s' % (LBR, RBR)]
    bd = block_d(t)
    c('BLOCK D read: key, path, line, class (a hyphen in it), OLD, NEW', bd,
      bd == [('C1', 'a/B.md', 2, 'SUPERSEDED', 'old one', 'new one'), ('C2a', 'a/B.md', 2, 'RE-CUT', 'two', '2 at %sPIN%s' % (LBR, RBR))])
    new, res = apply_doc(['h', 'the old one and two'], bd, {'PIN': 'the tag v9 (x)'})
    c('two keys on one line applied in order, the field filled', (new[1], [r[4] for r in res]),
      new[1] == 'the new one and 2 at the tag v9 (x)' and [r[4] for r in res] == ['RE-CUT', 'RE-CUT'])
    new2, res2 = apply_doc(['h', 'old one old one two'], bd, {})
    c('an OLD twice left; a NEW whose field cannot fill left; the line unchanged', ([r[4] for r in res2], new2[1]),
      [r[4] for r in res2] == ['LEFT', 'LEFT'] and new2[1] == 'old one old one two')
    dp = deposits(['| d1-1 | A_Place_to_Stand | v5 | PUBLISHED: Zenodo, DOI 10.5281/zenodo.21539167 |', '| x | SPIRAL_MAP | DOI 10.5281/zenodo.1 |'])
    c('the deposit pins: a PUBLISHED line with its DOI; a DOI on a line not PUBLISHED not taken', (dp['day1/A_Place_to_Stand_v5_17.md'], dp['SPIRAL_MAP.md']),
      dp['day1/A_Place_to_Stand_v5_17.md'] == [(1, '21539167')] and dp['SPIRAL_MAP.md'] == [])
    return L, ok


def doc_rows(D_, path):
    return [r for r in D_ if r[1] == path]


def cmd(argv):
    if argv[:1] == ['control']:
        L, ok = controls()
        print(NL.join(L))
        print('### CONTROLS %d OF %d AS WANTED' % (sum(ok), len(ok)))
        return
    L, ok = controls()
    if not all(ok):
        print(NL.join(L))
        sys.exit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    text = io.open(TEXT, encoding='utf-8').read().split(NL)
    BD = block_d(text)
    if len(BD) != 14:
        sys.exit('### BLOCK D READS %d LINES, NOT 14 -- NOTHING DONE' % len(BD))
    F = json.load(io.open(FIELDS, encoding='utf-8')) if os.path.exists(FIELDS) else None
    names = dict(DOCS)
    if argv[:1] in (['dry'], ['write'], ['confirm']):
        if len(argv) != 2 or (argv[1] not in names and not (argv[0] == 'dry' and argv[1] == 'all')):
            sys.exit(__doc__)
        B = load()
        for k in ([x for x, _p in DOCS] if argv[1] == 'all' else [argv[1]]):
            path = names[k]
            rows = doc_rows(BD, path)
            rc, hb = git(PP, 'show', 'HEAD:%s' % path, raw=True)
            p = os.path.join(PP, *path.split('/'))
            wb = open(p, 'rb').read()
            if argv[0] == 'confirm':
                done = [r for r in B['rows'] if r['path'] == path and r['state'] == 'RE-CUT']
                hl = hb.decode('utf-8').split(NL)
                eq = [(r['key'], r['line'], sha16(hl[r['line'] - 1]) == r['after_sha']) for r in done]
                _rc, last = git(PP, 'log', '-1', '--format=%H %s', '--', path)
                _rc, head = git(PP, 'rev-parse', 'HEAD')
                dd = [d for d in B['docs'] if d['path'] == path]
                ok_c = all(e for _k, _l, e in eq) and dd and last.split(' ')[0] == head.strip() and sha16(hb) == dd[-1]['new_sha']
                for kk, ll, e in eq:
                    print('  %s :%d at PLACE-papers HEAD %s' % (kk, ll, 'EQUAL TO THE LINE WRITTEN' if e else 'NOT THE LINE WRITTEN'))
                print('  %s: the last commit touching it %s, HEAD %s ; the blob %s the bytes written -> %s' % (
                    path, last.split(' ')[0][:8], head.strip()[:8], 'EQUAL TO' if dd and sha16(hb) == dd[-1]['new_sha'] else 'NOT', 'CONFIRMED' if ok_c else 'NOT CONFIRMED'))
                if ok_c:
                    dd[-1]['commit'] = head.strip()
                    dd[-1]['confirmed'] = stamp()
                    save(B)
                    print('  banked data/b759_corpus.json')
                continue
            if rc or hb != wb:
                print('### %s: THE WORKING COPY IS NOT HEAD`S BLOB (or not read) -- NOTHING DONE FOR IT' % path)
                continue
            if b'\r' in hb:
                print('### %s: THE BLOB CARRIES A CARRIAGE RETURN -- NOTHING DONE FOR IT' % path)
                continue
            lines = hb.decode('utf-8').split(NL)
            new, res = apply_doc(lines, rows, F)
            data = NL.join(new).encode('utf-8')
            print('## %s (%s): HEAD sha256 %s ; %d keys' % (k, path, sha16(hb), len(rows)))
            for (key, ln, n0, n1, st, why), r in zip(res, rows):
                print('  %s :%d %s %s -> %s%s ; the line %s -> %s' % (key, ln, r[3], 'OLD once' if n0 == 1 and n1 == 1 else 'OLD %d/%d' % (n0, n1), st,
                                                                         (' (%s)' % why) if why else '', sha16(lines[ln - 1]) if 0 < ln <= len(lines) else '-',
                                                                         sha16(new[ln - 1]) if 0 < ln <= len(new) else '-'))
            if argv[0] == 'dry':
                continue
            if any(r['path'] == path for r in B['rows']):
                sys.exit('### %s WRITTEN ALREADY (data/b759_corpus.json) -- NOTHING DONE' % path)
            if data != hb:
                with open(p, 'wb') as fh:
                    fh.write(data)
            back = open(p, 'rb').read()
            print('  written %d bytes, sha256 %s ; read back %s' % (len(back), sha16(back), 'EQUAL' if back == data else 'NOT EQUAL'))
            for (key, ln, n0, n1, st, why), r in zip(res, rows):
                B['rows'].append(dict(key=key, path=path, line=ln, cls=r[3], state=st, why=why, before_sha=sha16(lines[ln - 1]) if 0 < ln <= len(lines) else None,
                                      after_sha=sha16(new[ln - 1]) if 0 < ln <= len(new) else None, at=stamp()))
            B['docs'].append(dict(path=path, head_sha=sha16(hb), new_sha=sha16(back), written=stamp(), changed=data != hb, commit=None))
            save(B)
            print('  banked data/b759_corpus.json ; the commit next, by the one-call tool, then `confirm %s`' % k)
        return
    if argv[:1] == ['bank']:
        B = load()
        rc, reg = git(PP, 'show', 'HEAD:REGISTRY.md')
        dp = deposits(reg.replace('\r', '').split(NL))
        by = dict((r['key'], r) for r in B['rows'])
        out = ['%s -- (R369)(9): THE CORPUS`S SENTENCES ABOUT THE CONTROL, RE-CUT (%s, tools/b759_corpus.py bank)' % (ACT, stamp()), '',
               '## THE CONTROLS'] + L + ['', '## THE FOURTEEN LINES (PLACE-papers lines by path, line and sha256 alone)']
        recut, left = [], []
        for key, path, ln, cls, _o, nw in BD:
            r = by.get(key)
            dd = [d for d in B['docs'] if d['path'] == path]
            com = dd[-1]['commit'][:8] if dd and dd[-1].get('commit') else None
            st = r['state'] if r else 'NOT WRITTEN'
            if st == 'RE-CUT' and not com:
                st = 'WRITTEN, NOT CONFIRMED'
            (recut if st == 'RE-CUT' else left).append(key)
            out.append('  %-4s %s :%d %s -> %s%s ; the line %s -> %s%s' % (key, path, ln, cls, st, (' (%s)' % r['why']) if r and r['why'] else '',
                                                                       r['before_sha'] if r else '-', r['after_sha'] if r else '-', ' ; PLACE-papers %s' % com if com else ''))
        out += ['', '## THE DEPOSIT PINS (REGISTRY at PLACE-papers HEAD: a line naming the document, PUBLISHED, with a Zenodo DOI; the deposited copy not read, no Zenodo call)']
        for _k, p in DOCS:
            out.append('  %s: %s' % (p, ', '.join('REGISTRY :%d, Zenodo record %s' % x for x in dp[p]) if dp[p] else 'none'))
        orders = [dict(order='W-ORD-RECUT-%s' % key, key=key, path=path, line=ln, new=fill(nw, F) or nw, trigger=TRIGGER) for key, path, ln, _c, _o, nw in BD if key in left]
        out += ['', '## THE ORDERS ENTERED FOR THE LINES LEFT (for OPEN_TRAILS, by tools/b759_errata.py): %d' % len(orders)] + [
            '  %s: %s :%d ; trigger "%s"' % (o['order'], o['path'], o['line'], o['trigger']) for o in orders]
        c9 = [l for l in io.open(FERRY, encoding='utf-8').read().split(NL) if l.startswith('(9) ')][0]
        sent = re.findall(r'THE SENTENCE: "([^"]+)"', c9)
        date = time.strftime('%Y-%m-%d', time.gmtime())
        s = sent[0].replace('<r>', str(len(recut))).replace('<o>', str(len(left))).replace('<date>', date) if sent else None
        B['summary'] = dict(recut=recut, left=left, orders=orders, deposits=dict((p, dp[p]) for _k, p in DOCS), sentence=s, at=stamp())
        save(B)
        out += ['', '## THE SENTENCE OF (9), ITS FIELDS FILLED', '  %s' % s, '',
                '### ### **RE-CUT %d OF 14 ; LEFT %d ; ORDERS %d ; DEPOSITED COPIES %d ; CONTROLS %d OF %d.**' % (
                    len(recut), len(left), len(orders), sum(1 for _k, p in DOCS if dp[p]), sum(ok), len(ok))]
        r_ = FB.write(BANK, NL.join(out))
        print(NL.join(out))
        print('written data/b759_corpus.txt and data/b759_corpus.json ; figbank: %s' % r_['why'])
        return
    sys.exit(__doc__)


if __name__ == '__main__':
    cmd(sys.argv[1:])
