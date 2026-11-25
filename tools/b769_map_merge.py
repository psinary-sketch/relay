# -*- coding: utf-8 -*-
"""tools/b769_map_merge.py -- b769, (R379)(4)(b): THE MAP'S MERGE, under W-ORD-MAP-MERGE (OPEN_TRAILS :19227, [M4] at :19225).

As the order reads: the 81 lines that SPIRAL_MAP_v0_7.md alone holds (relay data/b765_map_pair.txt) are merged into SPIRAL_MAP.md by a tool
committed before its run, whose control reads each of the 93 differing lines present afterward; SPIRAL_MAP_v0_7.md stands as an edition
and is written by nothing. Written by the Write tool at b769's Component 2 and committed before its first run, dry included (N2).

  dry      the pair read at HEAD against b765's bank, the merge composed, its controls read; nothing written
  write    the same; where every pre-control and control reads as wanted, SPIRAL_MAP.md written in the papers' repository and read back,
           SPIRAL_MAP_v0_7.md read again unchanged, data/b769_map_merge.txt and .json banked
  restore  SPIRAL_MAP.md put back to its bytes at the act's PRE_PP (the order's CARRIED form); nothing else written

THE FILES are read as b765's reader read them, each split at its line ends with the empty piece after the final line end kept, so that
every line number is the bank's (SPIRAL_MAP_v0_7.md :617 and SPIRAL_MAP.md :548 are those pieces). THE PRE-CONTROLS: each file's working
bytes its bytes at HEAD and at PRE_PP (N3's reference); no carriage return and a final line end; the pair's ranges at HEAD (difflib,
autojunk off, as b765) the bank's twelve, by opcode and lines; each differing line's sha256 the bank's; the counts 81 and 93.
THE MERGE, nothing of SPIRAL_MAP.md removed or moved: in ranges 1 to 6 (b765's numbering), each line SPIRAL_MAP.md holds stands as it is
and the lines of SPIRAL_MAP_v0_7.md are set after it (a range SPIRAL_MAP.md does not share, range 1, at its place); from range 7 on, where
the two files' tails hold different matter (section 2D of SPIRAL_MAP.md, appended by b743 and b745, beside b610's back matter of
SPIRAL_MAP_v0_7.md), SPIRAL_MAP.md's tail stands whole and SPIRAL_MAP_v0_7.md's tail from its :549 follows it whole, its blank lines
that the pair's alignment matched to SPIRAL_MAP.md's blanks among them, so that neither section is interleaved line by line.
THE CONTROLS: each of the 93 differing lines present afterward, at one place, its sha256 the bank's (the order's control); every line of
SPIRAL_MAP.md present in its order; the merged file less the lines set from SPIRAL_MAP_v0_7.md equal to SPIRAL_MAP.md; the lines set from
SPIRAL_MAP_v0_7.md in its order, each a differing line or a blank line of its tail; a planted merge with one line of SPIRAL_MAP_v0_7.md
taken out reads it not present (a control that can fire). Printed beside them, no control: the lines that stand in two wordings (ranges
2 to 5), and the cluster the merged table gives PATHS_TO_THE_CRITICAL_LINE, for the INTEGRATION line of (R379)(10).

No line of either file is printed but that cluster's cell; each line by its number and sha256; no git write.
"""
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b769_worklist as K   # noqa: E402

ACT, NL = 'b769', '\n'
PP, REF = K.PP, K.PRE_PP
OLD, NEW = 'SPIRAL_MAP_v0_7.md', 'SPIRAL_MAP.md'
PAIR = 'data/b765_map_pair.txt'
TAIL_RANGE = 7       # ### b765's range 7: SPIRAL_MAP_v0_7.md :549 (its back matter's opening comment) beside SPIRAL_MAP.md :537 (section 2D's heading)
TWO_WORDINGS = (2, 3, 4, 5)
KEYSTONE = 'PATHS_TO_THE_CRITICAL_LINE'
TOOL = 'tools/b769_map_merge.py'
BANK = os.path.join(D, 'b769_map_merge.txt')
BJSON = os.path.join(D, 'b769_map_merge.json')
RANGE_RX = re.compile(r'^## RANGE (\d+): (\w+) ; SPIRAL_MAP_v0_7\.md :(\d+)-:(\d+) \((\d+) lines\) ; SPIRAL_MAP\.md :(\d+)-:(\d+) \((\d+) lines\)')
LINE_RX = re.compile(r'^    (SPIRAL_MAP(?:_v0_7)?\.md) :(\d+) sha256 ([0-9a-f]{16}) ;')


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def digest(l):
    return hashlib.sha256(l.encode('utf-8')).hexdigest()[:16]


def sha(b):
    return hashlib.sha256(b).hexdigest()[:16]


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout, r.returncode


def blob(rev, path):
    out, rc = git(PP, 'show', '%s:%s' % (rev, path))
    return out if rc == 0 else None


def working(path):
    with open(os.path.join(PP, path), 'rb') as f:
        return f.read()


def put(path, text):
    with open(path + '.tmp', 'wb') as f:
        f.write(text.encode('utf-8'))
    os.replace(path + '.tmp', path)


def committed(rel):
    """the relay file at `rel` committed and unchanged at the relay's HEAD (b765's self_commit form)."""
    h = git(RELAY, 'hash-object', rel)[0].decode().strip()
    b = git(RELAY, 'rev-parse', 'HEAD:' + rel)[0].decode().strip()
    st = git(RELAY, 'status', '--porcelain', '--', rel)[0].decode().strip()
    return bool(h) and h == b and not st


def read_pair():
    """b765's bank: its ranges [(k, op, a1, a2, b1, b2)] (1-based, as printed) and {(file, line): sha256}."""
    with open(os.path.join(RELAY, PAIR), encoding='utf-8') as f:
        L = f.read().split(NL)
    R, Dg = [], {}
    for l in L:
        m = RANGE_RX.match(l)
        if m:
            R.append((int(m.group(1)), m.group(2), int(m.group(3)), int(m.group(4)), int(m.group(6)), int(m.group(7))))
        m = LINE_RX.match(l)
        if m:
            Dg[(m.group(1), int(m.group(2)))] = m.group(3)
    return R, Dg


def compose(A, B, ops, ti, drop=None):
    """the merged lines and each line's origin ('A', i) or ('B', j); `drop` an A index left out (the planted control alone)."""
    M, org = [], []

    def take(src, S, a, b):
        for x in range(a, b):
            if src == 'A' and x == drop:
                continue
            M.append(S[x])
            org.append((src, x))
    for tag, i1, i2, j1, j2 in ops[:ti]:
        if tag in ('equal', 'insert'):
            take('B', B, j1, j2)
        elif tag == 'delete':
            take('A', A, i1, i2)
        else:
            take('B', B, j1, j2)
            take('A', A, i1, i2)
    _t, ia, _i2, jb, _j2 = ops[ti]
    take('B', B, jb, len(B))
    take('A', A, ia, len(A))
    return M, org


def present(M, org, dA, dB):
    pos = dict((o, k) for k, o in enumerate(org))
    res = []
    for src, rows in (('A', dA), ('B', dB)):
        for k, d in rows:
            m = pos.get((src, k - 1))
            res.append((src, k, m is not None and digest(M[m]) == d, (m + 1) if m is not None else None))
    return res


def cells(l):
    return [re.sub(r'[*`]', '', x).strip() for x in l.strip().strip('|').split('|')]


def run(mode):
    if mode == 'restore':
        b = blob(REF, NEW)
        if not b:
            die('SPIRAL_MAP.md NOT READ AT %s' % REF)
        with open(os.path.join(PP, NEW), 'wb') as f:
            f.write(b)
        print('restored SPIRAL_MAP.md to its bytes at %s (sha256 %s, %d bytes)' % (REF[:8], sha(b), len(b)))
        return 0
    hb = dict((p, blob('HEAD', p)) for p in (OLD, NEW))
    rb = dict((p, blob(REF, p)) for p in (OLD, NEW))
    wb = dict((p, working(p)) for p in (OLD, NEW))
    head = git(PP, 'rev-parse', '--short=8', 'HEAD')[0].decode().strip()
    A = wb[OLD].decode('utf-8').split(NL)
    B = wb[NEW].decode('utf-8').split(NL)
    ops = difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes()
    ne = [k for k, o in enumerate(ops) if o[0] != 'equal']
    R, Dg = read_pair()
    got = [(n + 1, ops[k][0], ops[k][1] + 1, ops[k][2], ops[k][3] + 1, ops[k][4]) for n, k in enumerate(ne)]
    dA = [(i + 1, digest(A[i])) for k in ne for i in range(ops[k][1], ops[k][2])]
    dB = [(j + 1, digest(B[j])) for k in ne for j in range(ops[k][3], ops[k][4])]
    pre = [('each file`s working bytes its bytes at HEAD %s and at PRE_PP %s (N3`s reference)' % (head, REF[:8]),
            all(hb[p] is not None and hb[p] == wb[p] == rb[p] for p in (OLD, NEW))),
           ('no carriage return and a final line end in each (%s %d lines, %s %d, as b765 counts them)' % (OLD, len(A), NEW, len(B)),
            all(b'\r' not in wb[p] and wb[p].endswith(b'\n') for p in (OLD, NEW))),
           ('the pair read at HEAD in the twelve ranges of %s, by opcode and lines: %d ranges read, %d banked' % (PAIR, len(got), len(R)), got == R),
           ('each differing line`s sha256 the bank`s: %d of %s and %d of %s, %d in the bank' % (len(dA), OLD, len(dB), NEW, len(Dg)),
            len(dA) + len(dB) == len(Dg) and all(Dg.get((OLD, k)) == d for k, d in dA) and all(Dg.get((NEW, k)) == d for k, d in dB)),
           ('the counts the order names: %d lines that %s alone holds and %d differing (wanted 81 and 93)' % (len(dA), OLD, len(dA) + len(dB)),
            len(dA) == 81 and len(dA) + len(dB) == 93),
           ('%s committed and unchanged at the relay`s HEAD, and %s' % (TOOL, PAIR), committed(TOOL) and committed(PAIR))]
    ok_pre = all(o for _w, o in pre)
    P = ['%s -- (R379)(4)(b): THE MAP`S MERGE, UNDER W-ORD-MAP-MERGE (%s)' % (ACT, utc()), '',
         '### tools/b769_map_merge.py %s; the papers` repository at HEAD %s; %s and %s read as b765`s reader read them. Each line by its number and' % (
             mode, head, OLD, NEW),
         '### the sha256 of its bytes (16 hex), never quoted; SPIRAL_MAP_v0_7.md written by nothing.', '', '## THE PRE-CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in pre]
    if not ok_pre:
        P += ['', '### ### **THE MAP`S MERGE: A PRE-CONTROL NOT AS WANTED ; NOTHING COMPOSED ; HELD, NOTHING WRITTEN.**']
        print(NL.join(P))
        return 1
    ti = ne[TAIL_RANGE - 1]
    M, org = compose(A, B, ops, ti)
    new = NL.join(M)
    pr = present(M, org, dA, dB)
    aset = set(k - 1 for k, _d in dA)
    aseq = [x for s, x in org if s == 'A']
    bseq = [x for s, x in org if s == 'B']
    extra = [x for x in aseq if x not in aset]
    Mp, orgp = compose(A, B, ops, ti, drop=dA[len(dA) // 2][0] - 1)
    prp = present(Mp, orgp, dA, dB)
    ctl = [('each of the 93 differing lines present afterward at one place, its sha256 the bank`s: %d of %d' % (sum(1 for x in pr if x[2]), len(pr)),
            len(pr) == 93 and all(x[2] for x in pr) and len(set(x[3] for x in pr)) == 93),
           ('every line of %s present in its order: %d of %d' % (NEW, len(bseq), len(B)), bseq == list(range(len(B)))),
           ('the merged file less the lines set from %s equal to %s' % (OLD, NEW), [M[k] for k, o in enumerate(org) if o[0] == 'B'] == B),
           ('the lines set from %s in its order, %d: the 81 differing and %d blank lines of its tail that the alignment matched to blanks (%s)' % (
               OLD, len(aseq), len(extra), ', '.join(':%d' % (x + 1) for x in extra) or 'none'),
            aseq == sorted(aseq) and len(set(aseq)) == len(aseq) and aset <= set(aseq) and all(A[x] == '' and x >= ops[ti][1] for x in extra)),
           ('PLANTED: the merge with %s :%d taken out reads it not present: %d of %d present' % (
               OLD, dA[len(dA) // 2][0], sum(1 for x in prp if x[2]), len(prp)), sum(1 for x in prp if not x[2]) == 1)]
    ok = all(o for _w, o in ctl)
    nM = len(M)
    P += ['', '## THE MERGE: %s %d lines to %d (as b765 counts them, the piece after the final line end included); set from %s %d; removed 0' % (
        NEW, len(B), nM, OLD, len(aseq)),
          '  ranges 1 to %d: %s`s lines stand, %s`s set after them; from range %d (%s :%d, %s :%d) %s`s tail stands whole and %s`s follows it whole' % (
              TAIL_RANGE - 1, NEW, OLD, TAIL_RANGE, OLD, ops[ti][1] + 1, NEW, ops[ti][3] + 1, NEW, OLD)]
    pos = dict((o, k) for k, o in enumerate(org))
    for n, k in enumerate(ne, 1):
        tag, i1, i2, j1, j2 = ops[k]
        P.append('  RANGE %d (%s): %s :%d-:%d at merged :%s ; %s :%d-:%d at merged :%s' % (
            n, tag, OLD, i1 + 1, i2, ','.join(str(pos[('A', i)] + 1) for i in range(i1, i2))[:200] or '-',
            NEW, j1 + 1, j2, ','.join(str(pos[('B', j)] + 1) for j in range(j1, j2)) or '-'))
    two = []
    for n in TWO_WORDINGS:
        tag, i1, i2, j1, j2 = ops[ne[n - 1]]
        two.append((n, [pos[('B', j)] + 1 for j in range(j1, j2)], [pos[('A', i)] + 1 for i in range(i1, i2)]))
    P += ['', '## THE LINES THAT STAND IN TWO WORDINGS (ranges %s, printed, no control): %s' % (
        ', '.join(str(n) for n in TWO_WORDINGS), '; '.join('range %d: %s`s at merged :%s, %s`s at :%s' % (
            n, NEW, ','.join(map(str, b)), OLD, ','.join(map(str, a))) for n, b, a in two))]
    rows = [(k + 1, cells(l)) for k, l in enumerate(M) if l.startswith('|') and KEYSTONE in l]
    integ = rows[0][1][0] if rows and rows[0][1] else None
    P += ['## THE CLUSTER THE MERGED TABLE GIVES %s ((R379)(10)): %s' % (
        KEYSTONE, '; '.join(':%d, its first cell "%s"' % (k, c[0]) for k, c in rows) or 'no row names it, so "Phase 1.2"')]
    P += ['', '## THE CONTROLS (the order`s, and the merge`s own)'] + ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    m5 = ('the %d lines that SPIRAL_MAP_v0_7.md alone held merged into SPIRAL_MAP.md, each of the %d differing lines read present afterward' % (
        len(dA), len(pr)))
    P += ['', '## [M5]`S FIELDS: %s' % (m5 if ok else 'CARRIED: the control read %d of %d lines present' % (sum(1 for x in pr if x[2]), len(pr))), '',
          '### ### **THE MAP`S MERGE: %d LINES OF %s SET INTO %s ; %d OF %d DIFFERING LINES PRESENT ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
              len(dA), OLD, NEW, sum(1 for x in pr if x[2]), len(pr), sum(1 for _w, o in ctl if o), len(ctl),
              ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD, NOTHING WRITTEN')]
    final = NL.join(P) + NL
    print(final, end='')
    if mode == 'dry' or not ok:
        return 0 if ok else 1
    with open(os.path.join(PP, NEW), 'wb') as f:
        f.write(new.encode('utf-8'))
    if working(NEW) != new.encode('utf-8'):
        die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    if working(OLD) != wb[OLD]:
        die('SPIRAL_MAP_v0_7.md CHANGED')
    put(BANK, final)
    put(BJSON, json.dumps(dict(at=utc(), act=ACT, pp_head=head, ref=REF, old=OLD, new=NEW, lines_before=len(B), lines_after=nM,
                               sha_before=sha(wb[NEW]), sha_after=sha(new.encode('utf-8')), old_sha=sha(wb[OLD]), set_from_old=len(aseq),
                               blank_tail_lines=[x + 1 for x in extra], differing_old=len(dA), differing=len(pr),
                               present=[[s, k, p_, m] for s, k, p_, m in pr], two_wordings=[[n, b, a] for n, b, a in two],
                               integration_cluster=integ, integration_rows=[[k, c[:2]] for k, c in rows], m5=m5,
                               pre=[[w, o] for w, o in pre], controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written SPIRAL_MAP.md (%d lines to %d); SPIRAL_MAP_v0_7.md unchanged; data/b769_map_merge.txt and .json' % (len(B), nM))
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] not in (['dry'], ['write'], ['restore']):
        sys.exit(__doc__)
    sys.exit(run(a[0]))
