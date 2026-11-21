# -*- coding: utf-8 -*-
"""b765 under (R375)(6)(b): THE FEDERATION MAP'S FILES SET SIDE BY SIDE, a reading and no build; no line of either file is written.

SPIRAL_MAP.md and SPIRAL_MAP_v0_7.md at PLACE-papers' HEAD: each differing line (difflib's opcodes over the two files' lines), cited by path,
line and the sha256 of its bytes and never quoted; the act that wrote it by the file's history (git blame --line-porcelain at HEAD: the
commit, its date and the act token opening its subject; the subject itself is not written and no author header is read); and what a reader
of one file alone does not see, by range, count and act, with the seat's reading of each range in its own words (READINGS below, written
after the seat read the ranges through the masks, scratch mapread765.py, 12:56:54Z). The seat's recommendation for the root's question
stands at RECOMMENDATION. REGISTRY :1002 registers neither file.

Routes: `read` prints, writes nothing; `bank` writes data/b765_map_pair.txt, refused unless this file is committed and unchanged at the
relay's HEAD. Each route runs the reader's control first: a planted pair read for its opcodes, a planted subject for its act token, and
the digest of a planted line."""
import collections, datetime, difflib, hashlib, io, os, re, subprocess, sys

R = 'D:/relay'
PP = 'D:/MY-DOwnloads/PLACE-papers'
OLD, NEW = 'SPIRAL_MAP_v0_7.md', 'SPIRAL_MAP.md'
BANK = os.path.join(R, 'data', 'b765_map_pair.txt')
ME = 'tools/b765_map_pair.py'
NL = '\n'
ACT = re.compile(r'^(b\d{3,4})\b')
# ### the seat's reading of each range, by the opcode's index among the non-equal ones, in its own words, no line quoted
READINGS = {
    0: 'v0_7`s version line for its edition (b610, under (R220)(4)) and the blank after it; SPIRAL_MAP.md has no v0.7 version line',
    1: 'a stem sentence of the map`s opening section: v0_7 carries b610`s correction of it (its back matter`s reading R-3); SPIRAL_MAP.md carries the uncorrected wording of v0.6',
    2: 'a row of the kernel table (SIDE-class-coupling): the two wordings differ within the row',
    3: 'the heading of the Phase 1.2 checkpoints: v0_7`s corrected wording beside v0.6`s',
    4: 'the opening sentence under that heading: v0_7`s corrected wording beside v0.6`s',
    5: 'v0_7: b610`s census rows beneath the cluster table, a head line and one line per cluster pointing to the keystone census; SPIRAL_MAP.md in their place: one row of the cluster table, the Epstein instance seated at b750, which v0_7 does not carry',
    6: 'v0_7: the comment opening its back matter; SPIRAL_MAP.md: the heading of section 2D, the Epstein instance on SIDE-explicit-formula, appended by b743 under (R353)(4)(B)',
    7: 'v0_7: the back matter`s heading (b610, (R220)(4)); SPIRAL_MAP.md: section 2D`s appended-by line',
    8: 'v0_7: the heading of the back matter`s readings; SPIRAL_MAP.md: section 2D`s kernel table, its head and its one row',
    9: 'v0_7: the readings R-1 to R-3; SPIRAL_MAP.md: section 2D`s filed-by line',
    10: 'v0_7: the heading of the insertions the ruling ordered; SPIRAL_MAP.md: b745`s dated note to section 2D`s row',
    11: 'v0_7 alone: the rest of its back matter -- the table of its insertions by line, its stem corrections and what follows them; SPIRAL_MAP.md has none of it',
}
RECOMMENDATION = ('neither file carries the map whole: v0_7 holds b610`s edition (its version line, four corrected sentences of v0.6, the '
                  'census rows and the back matter that records them), and SPIRAL_MAP.md holds v0.6`s sentences uncorrected with the Epstein '
                  'instance`s row (b750), section 2D (b743) and its dated note (b745) appended. The standing tools read both names: the '
                  'roster`s rule of the current edition (tools/standing/v1345.py :101-:106) puts SPIRAL_MAP_v0_7.md in the Project`s set and '
                  'SPIRAL_MAP.md out, so a reader of the set does not see the Epstein instance`s rows, while a check reads the Epstein row '
                  'at SPIRAL_MAP.md (tools/standing/v1340.py :556). The seat recommends that one file carry the map whole by the author`s '
                  'ruling: SPIRAL_MAP.md, where the later rows stand and the check reads, with b610`s corrections and census rows carried '
                  'into it by a later act and its own back matter, v0_7 then standing as the frozen record of its edition and the roster`s '
                  'rule read again; the author rules which name carries the map, and no line of either file is written at b765.')


def git(*a, repo=PP, ok=False):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode != 0 and not ok:
        raise SystemExit('### git %s failed (exit %d) -- nothing written' % (' '.join(a[:2]), r.returncode))
    return r.stdout if r.returncode == 0 else None


def lines_of(path):
    return io.open(os.path.join(PP, path), encoding='utf-8', errors='replace').read().replace('\r', '').split(NL)


def digest(l):
    return hashlib.sha256(l.encode('utf-8')).hexdigest()[:16]


def blame(path):
    """{final line: (commit short, ISO date, act token or None)}, from --line-porcelain at HEAD; only the sha line, committer-time and
    summary are read, the summary for its opening act token alone."""
    out, cur = {}, None
    commits = {}
    for l in git('blame', '--line-porcelain', 'HEAD', '--', path).split(NL):
        m = re.match(r'^([0-9a-f]{40}) \d+ (\d+)', l)
        if m:
            cur = [m.group(1), int(m.group(2)), None, None]
            continue
        if cur is None:
            continue
        if l.startswith('committer-time '):
            cur[2] = datetime.datetime.fromtimestamp(int(l.split()[1]), datetime.timezone.utc).strftime('%Y-%m-%d')
        elif l.startswith('summary '):
            m2 = ACT.match(l[len('summary '):])
            cur[3] = m2.group(1) if m2 else None
        elif l.startswith('\t'):
            commits[cur[1]] = (cur[0][:8], cur[2], cur[3])
            cur = None
    return commits


def control():
    a, b = ['x', 'y', 'z', 'w'], ['x', 'Y', 'z']
    ops = [o for o in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if o[0] != 'equal']
    ok1 = ops == [('replace', 1, 2, 1, 2), ('delete', 3, 4, 3, 3)]
    ok2 = ACT.match('b610 component 4: words') .group(1) == 'b610' and ACT.match('merge words') is None
    ok3 = digest('abc') == hashlib.sha256(b'abc').hexdigest()[:16]
    return ['  THE READER`S CONTROL: a planted pair read as one replace and one delete %s ; a planted subject`s act token read, and none where '
            'none opens it %s ; a planted line`s digest %s ; %s' % (ok1, ok2, ok3, 'AS WANTED' if ok1 and ok2 and ok3 else 'NOT AS WANTED')], \
        ok1 and ok2 and ok3


def self_commit():
    b = git('hash-object', ME, repo=R).strip()
    h = (git('rev-parse', 'HEAD:' + ME, repo=R, ok=True) or '').strip()
    if b != h or (git('status', '--porcelain', '--', ME, repo=R) or '').strip():
        raise SystemExit('### %s differs from its blob at HEAD or is not committed -- the bank refused, nothing written' % ME)
    return git('rev-parse', '--short=8', 'HEAD', repo=R).strip(), hashlib.sha256(io.open(os.path.join(R, ME), 'rb').read()).hexdigest()[:16]


def read():
    A, B = lines_of(OLD), lines_of(NEW)
    bA, bB = blame(OLD), blame(NEW)
    ops = [o for o in difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes() if o[0] != 'equal']
    return A, B, bA, bB, ops


def compose(A, B, bA, bB, ops, cl, at, tool):
    head = git('rev-parse', '--short=8', 'HEAD').strip()
    L = ['b765 -- THE FEDERATION MAP`S FILES SET SIDE BY SIDE UNDER (R375)(6)(b): A READING AND NO BUILD (%s)' % at, '',
         '### the reader tools/b765_map_pair.py%s; PLACE-papers at %s; %s (%d lines) and %s (%d lines). Each differing line by path, line and '
         'the sha256 of its bytes (16 hex), never quoted;' % ((', sha256 %s, committed at relay %s before its run' % (tool[1], tool[0])) if tool else '',
                                                             head, OLD, len(A), NEW, len(B)),
         '### the act that wrote it by git blame at HEAD (the commit, its date, the act token opening its subject). REGISTRY :1002 registers '
         'neither file. No line of either file is written.', '']
    L += cl + ['']
    actsA, actsB = collections.Counter(), collections.Counter()
    for k, o in enumerate(ops):
        L.append('## RANGE %d: %s ; %s :%d-:%d (%d lines) ; %s :%d-:%d (%d lines)' % (k + 1, o[0], OLD, o[1] + 1, o[2], o[2] - o[1], NEW, o[3] + 1, o[4], o[4] - o[3]))
        L.append('  THE SEAT`S READING: %s' % READINGS.get(k, '(no reading written for this range)'))
        for i in range(o[1], o[2]):
            c = bA.get(i + 1, ('?', '?', None))
            actsA[c[2] or 'no act token'] += 1
            L.append('    %s :%d sha256 %s ; written by %s at %s (%s)' % (OLD, i + 1, digest(A[i]), c[2] or 'no act token', c[0], c[1]))
        for i in range(o[3], o[4]):
            c = bB.get(i + 1, ('?', '?', None))
            actsB[c[2] or 'no act token'] += 1
            L.append('    %s :%d sha256 %s ; written by %s at %s (%s)' % (NEW, i + 1, digest(B[i]), c[2] or 'no act token', c[0], c[1]))
        L.append('')
    nA, nB = sum(o[2] - o[1] for o in ops), sum(o[4] - o[3] for o in ops)
    L.append('## WHAT A READER OF ONE FILE ALONE DOES NOT SEE')
    L.append('  a reader of %s alone does not see the %d lines of %s in the %d ranges above, written by %s' % (
        NEW, nA, OLD, len(ops), ', '.join('%s %d' % kv for kv in sorted(actsA.items()))))
    L.append('  a reader of %s alone does not see the %d lines of %s in them, written by %s' % (
        OLD, nB, NEW, ', '.join('%s %d' % kv for kv in sorted(actsB.items()))))
    L.append('  the two files differ in %d lines (%d of %s and %d of %s), in %d ranges' % (nA + nB, nA, OLD, nB, NEW, len(ops)))
    L.append('')
    L.append('## THE SEAT`S RECOMMENDATION, printed beside the root`s question')
    L.append('  ' + RECOMMENDATION)
    return L, nA, nB, actsA, actsB


def main():
    a = sys.argv[1:]
    if not a or a[0] not in ('read', 'bank'):
        sys.exit('### usage: b765_map_pair.py read | bank')
    cl, ok = control()
    print(NL.join(cl))
    if not ok:
        sys.exit('### THE READER`S CONTROL NOT AS WANTED -- nothing read further, nothing written')
    tool = self_commit() if a[0] == 'bank' else None
    A, B, bA, bB, ops = read()
    at = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    L, nA, nB, actsA, actsB = compose(A, B, bA, bB, ops, cl, at, tool)
    print('  %s %d lines ; %s %d lines ; ranges %d ; differing lines %d (%d and %d) ; acts on %s`s lines %s ; on %s`s %s' % (
        OLD, len(A), NEW, len(B), len(ops), nA + nB, nA, nB, OLD, dict(actsA), NEW, dict(actsB)))
    if a[0] == 'bank':
        s = NL.join(L) + NL
        with io.open(BANK, 'w', encoding='utf-8', newline='\n') as f:
            f.write(s)
        print('written data/b765_map_pair.txt: %d lines, %d bytes, sha256 %s' % (len(L), len(s.encode('utf-8')), hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]))


if __name__ == '__main__':
    main()
