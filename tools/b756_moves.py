# -*- coding: utf-8 -*-
"""b756, (R366)(5)(i) on the author's pass at the put (data/b756_author_answers.txt :4, :18, "Pass as placed (Recommended)": "the statuses
move by the orders tool's route in this act's trail, and W-ORD-LABEL-READER's predicate and control are done at this act"): THE TWELVE
STATUS LINES FOR THIS ACT'S TRAIL, composed from the placements banked at data/b756_orders_read.txt (tools/b756_orders.py's ORDERS, read
here, not copied), one line an order, each naming its order once and no other, in the grammar the standing orders tool reads
(tools/standing/orders.py: a status word standing directly after the order's name; DISCHARGED reads CLOSED, CARRIED reads OPEN):
  DONE            W-ORD-LEDGER-SPLIT-RESOLVER DISCHARGED, with the line that did it
  HERE            W-ORD-LABEL-READER DISCHARGED, with the standing change that did it at this act (tools/standing/ v1.34.8)
  WITH THE BUILD  five orders CARRIED, placed with the build
  LATER           five orders CARRIED, each with its trigger written again
The lines are written into OPEN_TRAILS only by this act's trail at the record (Component 6); this tool writes its bank alone. Its controls
read the lines through the orders tool's read() over OPEN_TRAILS at PLACE-papers HEAD with the lines appended, in memory: the two close, the
ten stay open, no other order's status moves; the same with the lines inside a hand section; a planted negated line moves nothing.
MODES  controls | dry | bank      BANKS data/b756_orders_moves.txt and .json
"""
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import orders as OR          # noqa: E402
import b756_orders as BO     # noqa: E402  (ORDERS, the placements as banked)

ACT = 'b756'
NL = '\n'
ANSWERS = 'data/b756_author_answers.txt'
OREAD = 'data/b756_orders_read.txt'
V1348 = ('5b7aa91e', 'data/b756_standing_v1348.txt')
TXT = os.path.join(RELAY, 'data', '%s_orders_moves.txt' % ACT)
JSN = os.path.join(RELAY, 'data', '%s_orders_moves.json' % ACT)
PASS = 'Pass as placed (Recommended)'
WANT = {'DONE': ('CLOSED', 'DISCHARGED'), 'HERE': ('CLOSED', 'DISCHARGED'), 'WITH THE BUILD': ('OPEN', 'CARRIED'), 'LATER': ('OPEN', 'CARRIED')}
# ### the trigger of each LATER order, written again in this act's words with no other order named and no quotation (the bank's own
# ### wording, data/b756_orders_read.txt, names a second order at (4) and quotes the old triggers)
TRIGGER = {
    'W-ORD-STORMER-CLASH': 'the next act that tags SIDE-kernel',
    'W-ORD-TESTS-WITH-THE-LISTS-IN-FORCE': 'the next act that edits tools/chain_page.py or the node lists it reads, the trigger it shares with the chain page’s b638 cases',
    'W-ORD-ROOT-BINARY-BANK': 'the next act that banks a binary file',
    'W-ORD-CHAIN-PAGE-B638-CASES': 'the next act that edits tools/chain_page.py or the node lists it reads',
    'W-ORD-CORRESPONDENCE-BEHIND-SCOPE': 'the next re-cut act of a document carrying a Correspondence table, among the prose pass and the re-cuts of `(R366)`(4)(iii)',
}


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace('\r', '')


def relay_head(path):
    rc, out = git(RELAY, 'show', 'HEAD:%s' % path)
    if rc:
        raise SystemExit('### %s NOT READ AT RELAY HEAD -- NOTHING DONE' % path)
    return out.split(NL)


def answer_lines():
    A = relay_head(ANSWERS)
    k = next((i for i, l in enumerate(A, 1) if l.startswith('### PROMPT 1 (Orders): ')), None)
    r = next((i for i, l in enumerate(A, 1) if l.startswith('RESULT (')), None)
    ok = bool(k and r) and ('Do the twelve placements pass?"="%s"' % PASS) in A[r - 1]
    return k, r, ok


def bank_row(n):
    """the row number (k) of order `n` in data/b756_orders_read.txt at relay HEAD, read from its own heading line."""
    for l in relay_head(OREAD):
        m = re.match(r'^  \((\d+)\) (W-ORD-[A-Z0-9-]+) -- (.+)$', l)
        if m and m.group(2) == n:
            return int(m.group(1)), m.group(3)
    return None, None


def compose():
    k, r, ok = answer_lines()
    if not ok:
        raise SystemExit('### THE AUTHOR`S PASS AT PROMPT 1 NOT READ AS "%s" AT RELAY HEAD -- NOTHING DONE' % PASS)
    rows = []
    for n, place, _rk, _words, _trig in BO.ORDERS:
        row, banked = bank_row(n)
        if banked != place:
            raise SystemExit('### %s PLACED %s HERE AND %s IN THE BANK -- NOTHING DONE' % (n, place, banked))
        cite = 'relay %s (%d)' % (OREAD, row)
        pas = 'placed %s under `(R366)`(5)(i) on the author’s pass at the put (relay %s :%d, :%d)' % (place, ANSWERS, k, r)
        if place == 'DONE':
            s = ('`%s` DISCHARGED, %s: b754’s two cuts met FINDINGS’ size with the ledgers not split, no line of them moving and no cite changing '
                 '(relay tools/standing/cuts.py :5-:6, :13), so no cite needs the resolver the order priced (%s).' % (n, pas, cite))
        elif place == 'HERE':
            s = ('`%s` DISCHARGED, %s and done at this act: tools/standing/ v1.34.8 (relay %s), roster.version_of reading a version string after a '
                 'kernel’s name as no document’s label, ONE_PAGE_PROOF’s kernel tag planted as its control (relay %s; %s).' % (n, pas, V1348[0], V1348[1], cite))
        elif place == 'WITH THE BUILD':
            s = '`%s` CARRIED, %s, a kernel or research order taken up by the build (%s).' % (n, pas, cite)
        else:
            s = '`%s` CARRIED, %s, its trigger written again: %s (%s).' % (n, pas, TRIGGER[n], cite)
        rows.append((n, place, s))
    return rows, (k, r)


def read_with(O, lines):
    return dict(OR.read(O + lines))


def controls(rows=None):
    out = []
    rows = rows or compose()[0]
    lines = [s for _n, _p, s in rows]
    k, r, ok = answer_lines()
    out.append(('the author`s pass at PROMPT 1 read at relay HEAD (%s :%s, :%s): "%s"' % (ANSWERS, k, r, PASS), ok, True))
    out.append(('twelve lines, one an order, in the bank`s order', [n for n, _p, _s in rows] == [o[0] for o in BO.ORDERS] and len(rows) == 12, True))
    out.append(('each line names its order once and no other', all(OR.NAME.findall(s) == [n] for n, _p, s in rows), True))
    out.append(('no line carries a quotation (the orders tool masks a quotation)', all(OR.mask(s) == s for s in lines), True))
    out.append(('each line`s backticks paired, each pair a code span and no apostrophe (the trail is markdown)',
                all(s.count('`') % 2 == 0 and not re.search(r'[A-Za-z0-9_]`s\b', s) for s in lines), True))
    rc, cm = git(RELAY, 'show', '--format=', '--name-only', V1348[0])
    vr = relay_head('tools/standing/VERSION')[0].strip()
    vb = relay_head(V1348[1])
    out.append(('the HERE work landed: relay %s carries tools/standing/roster.py and VERSION, VERSION at HEAD v1.34.8, its bank ALL AS WANTED' % V1348[0],
                rc == 0 and 'tools/standing/roster.py' in cm.split(NL) and 'tools/standing/VERSION' in cm.split(NL) and vr == 'v1.34.8'
                and any('ALL AS WANTED' in l for l in vb[-3:]), True))
    O = OR.trail('HEAD')
    before = dict(OR.read(O))
    head = ['', '### b756 — the trail as planted in memory', '']
    for label, extra in (('appended to OPEN_TRAILS at PLACE-papers HEAD', head), ('inside a hand section', head + ['*The lines above are the composer`s; ' +
                                                                                                                  OR.HAND_OPEN + '.*'])):
        after = read_with(O, extra + lines)
        got = [(after[n]['status'], after[n]['why']) for n, _p, _s in rows]
        want = [WANT[p] for _n, p, _s in rows]
        moved = sorted(n for n in after if n in before and after[n]['status'] != before[n]['status'])
        out.append(('%s: each order`s status and word as its place wants (2 CLOSED by DISCHARGED, 10 OPEN by CARRIED)' % label, got == want, True))
        out.append(('%s: the orders whose status moves, the two alone' % label, moved == ['W-ORD-LABEL-READER', 'W-ORD-LEDGER-SPLIT-RESOLVER'], True))
    out.append(('each of the twelve OPEN at PLACE-papers HEAD before the lines', all(before[n]['status'] == 'OPEN' for n, _p, _s in rows), True))
    neg = read_with(O, head + ['`W-ORD-KEIPER-FACE` not DISCHARGED by this planted line.'])
    out.append(('a planted negated closing word moves nothing', neg['W-ORD-KEIPER-FACE']['status'] == 'OPEN', True))
    for n, a, b in out:
        print('  CONTROL %s: %s (wanted %s)' % (n, a, b))
    good = sum(1 for _, a, b in out if a == b)
    print('### CONTROLS %d OF %d AS WANTED' % (good, len(out)))
    return good == len(out), good, len(out)


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def main(argv):
    step = argv[0] if argv else ''
    if step not in ('controls', 'dry', 'bank'):
        sys.exit(__doc__)
    rows, (k, r) = compose()
    ok, good, n = controls(rows)
    if step == 'controls':
        return 0 if ok else 1
    if not ok:
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    _, ph = git(OR.PP, 'rev-parse', '--short=8', 'HEAD')
    L = ['b756 -- (R366)(5)(i) ON THE AUTHOR`S PASS: THE TWELVE STATUS LINES FOR THIS ACT`S TRAIL (%s)' % stamp(), '',
         '### by tools/b756_moves.py, committed before its run, from the placements of relay %s on the author`s pass (relay %s :%d, :%d). Each line' % (OREAD, ANSWERS, k, r),
         '### below is written into OPEN_TRAILS by this act`s trail at the record and nowhere before; read through tools/standing/orders.py`s read()',
         '### over OPEN_TRAILS at PLACE-papers %s with the lines appended, in memory: CONTROLS %d OF %d AS WANTED. One line an order, unindented,' % (ph.strip(), good, n),
         '### between the two markers.', '', '#### THE LINES BEGIN']
    L += [s for _n, _p, s in rows] + ['#### THE LINES END', '']
    cnt = dict((p, sum(1 for _n, q, _s in rows if q == p)) for p in WANT)
    L.append('### ### **TWELVE STATUS LINES: DISCHARGED 2 (DONE %d, HERE %d) ; CARRIED 10 (WITH THE BUILD %d, LATER %d) ; THE ORDERS TOOL MOVES THE TWO ALONE ; '
             'WRITTEN BY THE TRAIL AT THE RECORD.**' % (cnt['DONE'], cnt['HERE'], cnt['WITH THE BUILD'], cnt['LATER']))
    print(NL.join(L))
    if step == 'bank':
        for path in (TXT, JSN):
            if os.path.exists(path):
                raise SystemExit('### %s STANDS ALREADY -- NOTHING WRITTEN' % os.path.relpath(path, RELAY))
        with open(TXT + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(NL.join(L) + NL)
        os.replace(TXT + '.tmp', TXT)
        with open(JSN + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(json.dumps({'act': ACT, 'answers': [ANSWERS, k, r], 'pp_head': ph.strip(), 'controls': [good, n],
                                 'lines': [{'order': nn, 'place': p, 'line': s} for nn, p, s in rows]}, indent=1, ensure_ascii=False) + NL)
        os.replace(JSN + '.tmp', JSN)
        print('### BANKED %s and %s at %s' % (os.path.relpath(TXT, RELAY), os.path.relpath(JSN, RELAY), stamp()))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
