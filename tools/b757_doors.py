# -*- coding: utf-8 -*-
"""tools/b757_doors.py -- b757, (R367)(8)(v): THE TWO DESCRIPTIONS, SENT BY gh AS PASSED AND EACH READ BACK EQUAL. Carried from tools/b756_doors.py
(its gh read, its one send a door, its scrub of addresses and the owner's path, its rows bank); the README route and the phrase matcher of
(R366)(6) not carried, (R367)(8)(v) passing each description whole.

THE WORDS, (R367)(8)(v) (data/b757_ferry.txt :25): "THE TWO DESCRIPTIONS, passed by the author at these wordings and counted by the navigator at
302 and 328 characters, sent by gh from tools/b757_doors.py, carried from tools/b756_doors.py, each read back equal. PLACE-papers: "..."
SIDE-kernel: "..." A description is a repository setting and no write to a kernel's tree." Each text is cut at run time from the ferry bank
(the quoted text after its door's name and colon), never typed here; its length is computed here and printed beside the ruling's figure.

Every gh call this tool makes is rowed in data/b757_doors_rows.json with its kind (read, edit), its time and its exit, so a reader of the act
finds a call made from inside the tool by this rows bank ((R367)(8)(iii)'s teaching, tools/b757_ghcalls.py).

  python -X utf8 -u tools/b757_doors.py read            the two descriptions read by gh (one call each) beside the passed texts; nothing written
  python -X utf8 -u tools/b757_doors.py write <door>    the passed text sent by gh once a door and read back (door: PLACE-papers | SIDE-kernel)
  python -X utf8 -u tools/b757_doors.py bank            the controls, a read and each write's row banked as data/b757_doors.txt
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

FERRY = os.path.join(D, 'b757_ferry.txt')
DOORS = {'PLACE-papers': 'D:/MY-DOwnloads/PLACE-papers', 'SIDE-kernel': 'D:/SIDE-kernel'}
RULED = {'PLACE-papers': 302, 'SIDE-kernel': 328}   # ### the ruling's own figures, (R367)(8)(v): "counted by the navigator at 302 and 328 characters"
LIMIT = 350   # ### the server's own words at b756's two sends, "description cannot be more than 350 characters" (data/b756_doors_rows.json)
ROWS = os.path.join(D, 'b757_doors_rows.json')
CLAUSE_OPEN = '(8) FIVE REPAIRS'


def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout or '').replace('\r', ''), (r.stderr or '').replace('\r', '')


def dig(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


def scrub(t):
    """each address and each <owner>/<door> cut before any print or bank, so no account name reaches either (N5); pure (b756's, carried)."""
    t = re.sub(r'\(?https?://\S+\)?', '<address cut>', t or '')
    return re.sub(r'[\w.-]+/(%s)\b' % '|'.join(re.escape(k) for k in DOORS), r'<owner>/\1', t)


def passed(text=None):
    """{door: the passed text} cut from (8)'s line of the ferry bank: the quoted text after '<door>: "'; pure on `text` when given."""
    if text is None:
        L = io.open(FERRY, encoding='utf-8').read().replace('\r', '').split(NL)
        hit = [l for l in L if l.startswith(CLAUSE_OPEN)]
        if len(hit) != 1:
            return {}
        text = hit[0]
    out = {}
    for door in DOORS:
        key = '%s: "' % door
        if text.count(key) != 1:
            continue
        i = text.find(key) + len(key)
        j = text.find('"', i)
        if j > i:
            out[door] = text[i:j]
    return out


def rows():
    return json.load(io.open(ROWS, encoding='utf-8')).get('rows', []) if os.path.isfile(ROWS) else []


def _row(r):
    j = dict(rows=rows() + [r])
    with open(ROWS + '.tmp', 'wb') as f:
        f.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(ROWS + '.tmp', ROWS)


def gh_read(door, why):
    t0 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    rc, out, err = run(['gh', 'repo', 'view', '--json', 'description', '-q', '.description'], cwd=DOORS[door])
    _row(dict(kind='read', door=door, at=t0, rc=rc, why=why, digest=dig(out.strip()), chars=len(out.strip())))
    return rc, out.strip(), scrub(err.strip())[:300]


def controls():
    """the cut over planted clause texts and the scrub; pure."""
    out = []
    t = 'x PLACE-papers: "Alpha beta." SIDE-kernel: "Gamma -- the programme\u2019s delta." y'
    p = passed(t)
    out.append(('the cut over a planted clause: each door`s quoted text, the curly apostrophe kept', p == {'PLACE-papers': 'Alpha beta.',
                                                                                                        'SIDE-kernel': 'Gamma -- the programme\u2019s delta.'}))
    out.append(('a clause naming one door twice: that door not cut', 'PLACE-papers' not in passed('PLACE-papers: "a" PLACE-papers: "b"')))
    out.append(('a clause naming neither door: nothing cut', passed('no door here') == {}))
    out.append(('the scrub: an API address and an <owner>/<door> path cut, the server`s words kept',
                scrub('HTTP 422 (https://api.example.invalid/repos/someone/SIDE-kernel) too long someone/PLACE-papers')
                == 'HTTP 422 <address cut> too long <owner>/PLACE-papers'))
    return out


def read_lines(row_why):
    c = controls()
    L = ['## THE CONTROLS FIRST: %d of %d AS WANTED' % (sum(1 for _w, ok in c if ok), len(c))]
    L += ['    %s -> %s' % (w, 'AS WANTED' if ok else 'NOT AS WANTED') for w, ok in c]
    P = passed()
    L.append('')
    L.append('## THE PASSED TEXTS, CUT FROM THE FERRY BANK (data/b757_ferry.txt, the line opening %r)' % CLAUSE_OPEN)
    for door in DOORS:
        t = P.get(door)
        L.append('  %s: %s' % (door, ('%d characters (the ruling`s figure %d: %s) ; digest %s ; %s the server`s %d' % (
            len(t), RULED[door], 'EQUAL' if len(t) == RULED[door] else 'DIFFERS', dig(t), 'within' if len(t) <= LIMIT else 'ABOVE', LIMIT)) if t else '### NOT CUT'))
        if t:
            L.append('    THE TEXT: %s' % t)
    L.append('')
    L.append('## THE TWO DESCRIPTIONS, READ BY gh (one call each, from the clone; the description field alone)')
    res = {}
    for door in DOORS:
        rc, cur, err = gh_read(door, row_why)
        res[door] = dict(rc=rc, current=cur)
        L.append('  %s: gh exit %d%s ; %d characters ; digest %s ; EQUAL TO THE PASSED TEXT %s' % (
            door, rc, (' (%s)' % err) if rc else '', len(cur), dig(cur), bool(P.get(door)) and cur == P.get(door)))
        L.append('    CURRENT: %s' % cur)
    return L, res, all(ok for _w, ok in c) and len(P) == 2


def write(door):
    P = passed()
    new = P.get(door)
    if not new:
        sys.exit('### %s: the passed text not cut from the ferry bank -- NOTHING SENT' % door)
    if any(r.get('kind') == 'edit' and r['door'] == door for r in rows()):
        sys.exit('### %s: a write already sent and rowed (data/b757_doors_rows.json); one send a door -- NOTHING SENT' % door)
    rc0, cur, err0 = gh_read(door, 'before the send')
    if rc0 != 0:
        sys.exit('### gh read exit %d: %s -- NOTHING SENT' % (rc0, err0))
    t0 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    rc, out, err = run(['gh', 'repo', 'edit', '--description', new], cwd=DOORS[door])
    _row(dict(kind='edit', door=door, at=t0, rc=rc, err=scrub(err.strip())[:300], before=cur, before_digest=dig(cur), new=new, new_digest=dig(new)))
    rb_rc, back, rb_err = gh_read(door, 'the read-back after the send')
    eq = back == new
    print('%s WRITE %s description by gh repo edit: exit %d%s ; %d characters, digest %s ; READ BACK exit %d, EQUAL TO THE PASSED TEXT %s, equal to '
          'the before %s' % (t0, door, rc, (' ; ' + scrub(err.strip())[:300]) if rc else '', len(new), dig(new), rb_rc, eq, back == cur))
    if not (eq or (rc != 0 and back == cur)):
        sys.exit('### NEITHER WRITTEN AS PASSED NOR LEFT AS IT STOOD: the read-back differs from both')


def main(argv):
    mode = argv[0] if argv else ''
    if mode == 'read':
        print(NL.join(read_lines('the read mode')[0]))
    elif mode == 'write' and len(argv) == 2 and argv[1] in DOORS:
        write(argv[1])
    elif mode == 'bank':
        rl, res, cok = read_lines('the bank`s read')
        rs = rows()
        L = ['b757 -- (R367)(8)(v): THE TWO DESCRIPTIONS, SENT BY gh AS PASSED, EACH READ BACK (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
             '', '### written by tools/b757_doors.py bank; the passed texts cut from the ferry bank; the descriptions read by gh from each clone (the '
             'description field alone); a description is a repository setting, nothing of a kernel`s tree written', ''] + rl
        L += ['', '## EVERY gh CALL THIS TOOL MADE (data/b757_doors_rows.json)']
        for r in rs:
            if r.get('kind') == 'edit':
                L.append('  %s EDIT %s: gh repo edit --description exit %d%s ; before digest %s ; the passed text digest %s, %d characters' % (
                    r['at'], r['door'], r['rc'], (' ; THE SERVER`S ANSWER: %s' % r['err'].replace(NL, ' / ')) if r['rc'] else '', r['before_digest'],
                    r['new_digest'], len(r['new'])))
            else:
                L.append('  %s READ %s: gh repo view exit %d ; %d characters, digest %s (%s)' % (r['at'], r['door'], r['rc'], r['chars'], r['digest'], r['why']))
        edits = [r for r in rs if r.get('kind') == 'edit']
        P = passed()
        eq = [d for d in DOORS if res[d]['rc'] == 0 and P.get(d) and res[d]['current'] == P[d]]
        L.append('### ### **(8)(v): CONTROLS %s ; SENT %d OF 2 (EDIT CALLS %d) ; READ BACK EQUAL TO THE PASSED TEXT %d OF 2 (%s).**' % (
            'AS WANTED' if cok else 'NOT AS WANTED', len(set(r['door'] for r in edits)), len(edits), len(eq), ', '.join(eq) or 'none'))
        text = NL.join(L)
        with io.open(os.path.join(D, 'b757_doors.txt'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(text + NL)
        print(text)
        print('written data/b757_doors.txt')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
