# -*- coding: utf-8 -*-
"""tools/b756_doors.py -- b756, (R366)(6), THE README ROUTE WITH [B1] AND [B3] AND THE TWO DESCRIPTIONS THAT CARRY "verified surround".

THE WORDS, (R366)(6) (data/b756_ferry.txt :30): "[B3]'s phrase and the two descriptions that carry "verified surround" reading in its place "a
criterion for the Riemann Hypothesis proved in Lean 4, with the results around it that are proved unconditionally, each cited by theorem name
and version"". The two descriptions are PLACE-papers' ([A5], passed at b754, data/b754_ferry.txt :24) and SIDE-kernel's ([B4], passed at
b754, :30). The seat's reading of "its place": the noun phrase that carries the two words, opening "a" and ending "verified surround" (in
[A5] "a compiled criterion for the Riemann Hypothesis with its verified surround", in [B4] "a criterion with a verified surround"), since the
ruling's words are themselves a noun phrase opening "a criterion"; every other word of each description stands as gh reads it.

THE README ROUTE, HALTED ((R366)(8) against the commit and the push): (1) the one-call tool commits in the relay and PLACE-papers alone
(tools/standing/commit.py :71, :726), and plain git is the hook's PLAINGIT kind; (2) a README commit on a kernel's main moves that branch;
(3) every route that pushes a kernel's main needs a push-* or repair-* branch checked out (Rule 4.10: tools/push_gated.sh :167-:169, the
standing push; the tracked hook SIDE-explicit-formula/.githooks/pre-push :77-:83, which refuses a push to main from main); where (R366)(8)
reads "no branch of any kernel merged, created, moved or deleted". The `halt` mode reads each ground from its file and runs the tracked
hook over a planted push line from main (refused) and, as its positive control, the same hook text with only its branch read set to a
push-* name (passed); nothing is pushed, no branch made, no file of a kernel written. [B1] and [B3] are carried whole ((R366)(6): "carried
whole where the route's tool change is not reached").

  python -X utf8 -u tools/b756_doors.py read            the two descriptions read by gh (one call each), the phrase and the new text; nothing written
  python -X utf8 -u tools/b756_doors.py halt            the README route's halt with its positive control; nothing written
  python -X utf8 -u tools/b756_doors.py write <door>    the ruled text sent by gh once a door, the server's answer and the read-back banked (door: PLACE-papers | SIDE-kernel)
  python -X utf8 -u tools/b756_doors.py bank            the read, the halt and each write's row banked as data/b756_doors.txt
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NEW = ('a criterion for the Riemann Hypothesis proved in Lean 4, with the results around it that are proved unconditionally, each cited by '
       'theorem name and version')
PHRASE = re.compile(r'\ba (?:[A-Za-z]+ ){0,8}?criterion\b[^;:()]*?verified surround\b')
DOORS = {'PLACE-papers': 'D:/MY-DOwnloads/PLACE-papers', 'SIDE-kernel': 'D:/SIDE-kernel'}
LIMIT = 350   # ### GitHub's limit on a repository description as two secondary sources give it, not its documentation: printed beside each
#               text, never a refusal of the tool's; the server decides at the write, the ruled text sent as ruled, its answer banked. At b756
#               the server answered each send "description cannot be more than 350 characters" (data/b756_doors_rows.json)
ROWS = os.path.join(D, 'b756_doors_rows.json')
EF = 'D:/SIDE-explicit-formula'


def run(cmd, cwd=None, inp=None):
    r = subprocess.run(cmd, cwd=cwd, input=inp, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout or '').replace('\r', ''), (r.stderr or '').replace('\r', '')


def dig(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


def scrub(t):
    """gh's messages name the repository by its owner's path and the API's address: each address and each <owner>/<door> cut before any
    print or bank, so no account name reaches either (N5); pure."""
    t = re.sub(r'\(?https?://\S+\)?', '<address cut>', t or '')
    return re.sub(r'[\w.-]+/(%s)\b' % '|'.join(re.escape(k) for k in DOORS), r'<owner>/\1', t)


def gh_read(door):
    rc, out, err = run(['gh', 'repo', 'view', '--json', 'description', '-q', '.description'], cwd=DOORS[door])
    return rc, out.strip(), scrub(err.strip())[:300]


def plan(cur):
    """(the phrase found or None, the new text or None, why) -- pure."""
    hits = PHRASE.findall(cur or '')
    if len(hits) != 1:
        return None, None, 'the phrase carrying "verified surround" found %d times (one wanted)' % len(hits)
    new = cur.replace(hits[0], NEW, 1)
    return hits[0], new, 'the new text %d characters ; %s the limit of %d that two secondary sources give (the server decides at the write)' % (
        len(new), 'ABOVE' if len(new) > LIMIT else 'within', LIMIT)


def controls():
    """the matcher and the plan over the two b754 drafts and planted texts; pure."""
    a5 = ('Manuscripts, ledgers and registry of the PLACE TO STAND research programme: a compiled criterion for the Riemann Hypothesis with its '
          'verified surround, the RH-adjacent work')
    b4 = 'Lean 4 kernel (PLACE TO STAND): the logical structure of the approach, a criterion with a verified surround -- route terminals'
    out = []
    p1 = plan(a5)
    out.append(('the [A5] form: the phrase from "a compiled criterion" to "verified surround"', p1[0] == 'a compiled criterion for the Riemann Hypothesis with its verified surround'))
    p2 = plan(b4)
    out.append(('the [B4] form: the phrase "a criterion with a verified surround", the rest standing',
                p2[0] == 'a criterion with a verified surround' and p2[1] == b4.replace('a criterion with a verified surround', NEW)))
    out.append(('a text without the two words: no phrase, no write', plan('Lean 4 kernel: route terminals')[1] is None))
    p4 = plan('x' * 300 + ' a criterion with a verified surround')
    out.append(('a text past the limit after the change: sent as ruled, ABOVE printed', p4[1] is not None and 'ABOVE' in p4[2]))
    out.append(('the scrub: an API address and an <owner>/<door> path cut, the server`s words kept',
                scrub('HTTP 422: Validation Failed (https://api.example.invalid/repos/someone/SIDE-kernel) description cannot be more than 350 '
                      'characters someone/PLACE-papers') == 'HTTP 422: Validation Failed <address cut> description cannot be more than 350 characters '
                '<owner>/PLACE-papers'))
    return out


def read_lines():
    L = ['## THE TWO DESCRIPTIONS, READ BY gh (one call each, from the clone; the description field alone)']
    c = controls()
    L.append('### the matcher`s controls: %d of %d AS WANTED' % (sum(1 for _w, ok in c if ok), len(c)))
    L += ['    %s -> %s' % (w, 'AS WANTED' if ok else 'NOT AS WANTED') for w, ok in c]
    res = {}
    for door in DOORS:
        rc, cur, err = gh_read(door)
        ph, new, why = plan(cur) if rc == 0 else (None, None, 'gh exit %d: %s' % (rc, err))
        res[door] = dict(rc=rc, current=cur, phrase=ph, new=new, why=why)
        L += ['  %s: gh exit %d ; %d characters ; digest %s' % (door, rc, len(cur), dig(cur)),
              '    CURRENT: %s' % cur, '    THE PHRASE: %s' % ph, '    THE NEW TEXT: %s' % new, '    %s' % why]
    return L, res, all(ok for _w, ok in c)


def halt_lines():
    L = ['## THE README ROUTE, HALTED: THE COMMIT, THE BRANCH AND THE PUSH, EACH BARRED (THE ONE-CALL TOOL`S TABLE, (R366)(8), RULE 4.10)']
    sha = run(['git', '-C', EF, 'rev-parse', 'main'])[1].strip()
    line = 'refs/heads/main %s refs/heads/main %s\n' % (sha, sha)
    rc, out, err = run(['sh', '.githooks/pre-push', 'origin', 'not-read'], cwd=EF, inp=line)
    hook = run(['git', '-C', EF, 'show', 'main:.githooks/pre-push'])[1]
    ref = [l.strip() for l in err.split(NL) if 'REFUSED' in l]
    with tempfile.TemporaryDirectory(prefix='b756doors_') as d:
        alt = hook.replace('branch=$(git symbolic-ref --short HEAD 2>/dev/null)', 'branch=push-b756-control', 1)
        p = os.path.join(d, 'pre-push-control')
        with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write(alt)
        rc2, out2, err2 = run(['sh', p, 'origin', 'not-read'], cwd=EF, inp=line)
    sub = alt != hook
    pg = io.open(os.path.join(HERE, 'push_gated.sh'), encoding='utf-8').read().replace('\r', '').split(NL)
    pg_line = next((i + 1 for i, l in enumerate(pg) if 'must be push-* or repair-* (Rule 4.10)' in l), None)
    pg_nomain = next((i + 1 for i, l in enumerate(pg) if 'ALONE to its remote under the same name' in l and 'no main push' in l), None)
    cm = io.open(os.path.join(HERE, 'standing', 'commit.py'), encoding='utf-8').read().replace('\r', '').split(NL)
    cm_repos = [(i + 1, l.strip()) for i, l in enumerate(cm) if l.startswith('REPOS = {')]
    cm_refuse = next((i + 1 for i, l in enumerate(cm) if 'argv[0] not in REPOS' in l), None)
    keys = re.findall(r"'([a-z]+)':", cm_repos[0][1]) if cm_repos else []
    sk = DOORS['SIDE-kernel']
    sk_hp = run(['git', '-C', sk, 'config', '--get', 'core.hooksPath'])[1].strip()
    sk_pp = os.path.isfile(os.path.join(sk, '.git', 'hooks', 'pre-push'))
    sk_track = run(['git', '-C', sk, 'ls-tree', '--name-only', 'main', '.githooks/'])[1].strip()
    L += ['  (1) THE COMMIT: the one-call tool takes the repositories of its table alone (tools/standing/commit.py :%s, keys %s; :%s refuses any '
          'other before a write), so no route of it commits in a kernel, and a commit by plain git is the hook`s PLAINGIT kind'
          % (cm_repos[0][0] if cm_repos else None, keys, cm_refuse),
          '  (2) THE BRANCH: a README commit on a kernel`s main moves that branch, where (R366)(8) reads "no branch of any kernel merged, '
          'created, moved or deleted"',
          '  (3) THE PUSH: the standing push (tools/push_gated.sh :%s) pushes main from a push-* or repair-* branch alone (Rule 4.10), a branch '
          'made on the kernel, which (8) bars; its branch mode (:%s, "no main push" in its own head) named on main would pass the default '
          'mode`s Rule 4.10 check: a substitution, not a route' % (pg_line, pg_nomain),
          '  SIDE-explicit-formula`s tracked hook (.githooks/pre-push at main, %d lines, digest %s) over a planted push of main from main at %s, '
          'no network: exit %d ; %s' % (len(hook.split(NL)), dig(hook), sha[:8], rc, ref[0] if ref else '### NO REFUSAL LINE'),
          '  THE POSITIVE CONTROL: the same text, its branch read alone set to push-b756-control (substituted %s), over the same line: exit %d ; '
          'a refusal line %s' % (sub, rc2, any('REFUSED' in l for l in err2.split(NL))),
          '  SIDE-kernel: core.hooksPath %r ; a pre-push in its git folder %s ; a tracked .githooks %r: its main pushed by the standing route '
          'alone, refused at :%s for a branch not of the push-* form before any ref is read' % (sk_hp or 'none', sk_pp, sk_track or 'none', pg_line),
          '  N5: "no kernel is touched beyond a README under (6)"; (6): "carried whole where the route`s tool change is not reached"',
          '  THE ROUTES READ, none taken: a one-call route for a kernel (a standing change to the tool`s table: its commit still moves main, (2)); '
          'a plain commit and push from main (PLAINGIT; on SIDE-explicit-formula the tracked hook refuses it, above); the standing push '
          '(a push-* branch made, (3)); the branch mode on main (a substitution, (3)); a push past the hook (never).']
    ok = (rc != 0 and bool(ref) and rc2 == 0 and sub and not any('REFUSED' in l for l in err2.split(NL)) and pg_line is not None
          and pg_nomain is not None and keys == ['relay', 'pp'] and cm_refuse is not None)
    L.append('### ### **THE README ROUTE HALTED: %s ; [B1] AND [B3] CARRIED WHOLE ((R366)(6)), NO KERNEL WRITTEN, NO BRANCH MADE, NOTHING PUSHED.**' % (
        'THE HALT PROVED, THE HOOK REFUSING AND ITS POSITIVE CONTROL PASSING' if ok else '### THE HALT NOT PROVED'))
    return L, ok


def rows():
    return json.load(io.open(ROWS, encoding='utf-8')).get('rows', []) if os.path.isfile(ROWS) else []


def write(door):
    rc, cur, err = gh_read(door)
    if rc != 0:
        sys.exit('### gh read exit %d: %s -- NOTHING WRITTEN' % (rc, err))
    if any(r['door'] == door for r in rows()):
        sys.exit('### %s: a write already sent and banked (data/b756_doors_rows.json); one send a door -- NOTHING SENT' % door)
    ph, new, why = plan(cur)
    if new is None:
        sys.exit('### %s: %s -- NOTHING WRITTEN' % (door, why))
    t0 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    rc, out, err = run(['gh', 'repo', 'edit', '--description', new], cwd=DOORS[door])
    rb_rc, back, rb_err = gh_read(door)
    row = dict(door=door, at=t0, before=cur, before_digest=dig(cur), phrase=ph, new=new, new_digest=dig(new), edit_rc=rc,
               edit_err=scrub(err.strip())[:300], read_back=back, read_back_rc=rb_rc, equal=back == new, unchanged=back == cur)
    j = dict(rows=rows() + [row])
    s = json.dumps(j, indent=1, ensure_ascii=False) + NL
    with open(ROWS + '.tmp', 'wb') as f:
        f.write(s.encode('utf-8'))
    os.replace(ROWS + '.tmp', ROWS)
    print('%s WRITE %s description by gh repo edit: exit %d%s ; %d characters, digest %s ; READ BACK exit %d, equal to the new %s, equal to '
          'the before %s' % (t0, door, rc, (' ; ' + row['edit_err']) if rc else '', len(new), dig(new), rb_rc, back == new, back == cur))
    if not (back == new or (rc != 0 and back == cur)):
        sys.exit('### NEITHER WRITTEN AS RULED NOR LEFT AS IT STOOD: the read-back differs from both')


def main(argv):
    mode = argv[0] if argv else ''
    if mode == 'read':
        print(NL.join(read_lines()[0]))
    elif mode == 'halt':
        print(NL.join(halt_lines()[0]))
    elif mode == 'write' and len(argv) == 2 and argv[1] in DOORS:
        write(argv[1])
    elif mode == 'bank':
        rl, _res, _c = read_lines()
        hl, ok = halt_lines()
        rs = rows()
        L = ['b756 -- (R366)(6): THE README ROUTE WITH [B1] AND [B3] AND THE TWO DESCRIPTIONS THAT CARRY "verified surround" (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
             '', '### written by tools/b756_doors.py bank; the descriptions read by gh from each clone (the description field alone); no line of a '
             'kernel`s README quoted; nothing of a kernel written', ''] + hl + [''] + rl + ['', '## THE WRITES, EACH READ BACK (data/b756_doors_rows.json)']
        for r in rs:
            L.append('  %s %s: gh edit exit %d ; before digest %s ; the phrase %r ; the new text digest %s, %d characters ; read back exit %d, '
                     'EQUAL TO THE NEW %s, EQUAL TO THE BEFORE %s' % (r['at'], r['door'], r['edit_rc'], r['before_digest'], r['phrase'], r['new_digest'],
                                                                   len(r['new']), r['read_back_rc'], r['equal'], r['unchanged']))
            if r['edit_rc']:
                L.append('     THE SERVER`S ANSWER, as gh printed it (addresses and the owner`s path cut; its line break printed " / "): %s'
                         % r['edit_err'].replace(NL, ' / '))
        if not rs:
            L.append('  NONE')
        eq = sum(1 for r in rs if r['equal'])
        lim = [r['door'] for r in rs if r['edit_rc'] and r['unchanged'] and re.search(r'cannot be more than %d characters' % LIMIT, r['edit_err'])]
        if lim:
            L += ['', '## THE DESCRIPTIONS, CARRIED WHOLE WITH THE CONFLICT NAMED',
                  '  (R366)(6) orders each description to read the ruling`s words in the place of its phrase; with those words in place the texts run '
                  '%s characters, and the server takes %d at most, in its own words at each send above. The seat shortens neither the ruling`s '
                  'words nor any other word of a description, either being a text the author did not give: both descriptions stand as they '
                  'stood (each read back equal to the before), carried whole with [B1] and [B3] for the author`s wording.'
                  % (' and '.join('%d (%s)' % (len(r['new']), r['door']) for r in rs if r['door'] in lim), LIMIT)]
        L.append('### ### **THE DESCRIPTIONS: WRITTEN AS RULED AND READ BACK EQUAL %d of %d ; REFUSED BY THE SERVER FOR LENGTH, EACH READ BACK '
                 'UNCHANGED, %d (%s) ; THE README ROUTE %s.**' % (eq, len(DOORS), len(lim), ', '.join(lim) or 'none',
                                                                  'HALTED, [B1] AND [B3] CARRIED WHOLE' if ok else '### NOT PROVED HALTED'))
        text = NL.join(L)
        with io.open(os.path.join(D, 'b756_doors.txt'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(text + NL)
        print(text)
        print('written data/b756_doors.txt')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
