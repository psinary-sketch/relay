# -*- coding: utf-8 -*-
"""tools/b757_readme.py -- (R367)(4)(iii): [B1], SIDE-explicit-formula's README lines as the author passed them, cut from the banks and read
against them, with (R366)(6)'s phrase where that text carries the words "verified surround"; the one write is README.md in the kernel's
working tree on push-b757-join, committed by the one-call tool.

THE SOURCES, each read at run time and none typed here: the lines replaced, as data/b754_doors.txt quotes them under [B1] (:24-:32), each read
against README.md at the join's HEAD; the replacement texts, [B1] as drafted in the author's ferry of b754 (data/b754_ferry.txt, the line
opening "[B1]"), its digest read against the one data/b754_agenda.txt gives beside it (b754's digest, sha256's first 16 of the line); the
phrase of (R366)(6), read from data/b756_ferry.txt (the line opening "(6)", the words after "reading in its place"). Where a replacement
text carries "verified surround", the tool stops: [B1]'s draft names no phrase for it to replace.

THE FORM: line :3 takes its text whole on one line, as :3 stands; :5-:7 take theirs wrapped at word boundaries to three lines and :23-:26 to
four, so that no other line of the README moves (lines of this README are cited by line in the corpus); no word of the author's changes.
The cites inside the texts (a backticked name beside a path and a line) are read at the join's HEAD and printed, EQUAL or DIFFERS; the text
is written as passed either way.

  plan     every read and the README as it would stand, printed; nothing written
  write    the same reads, then README.md written in the kernel's working tree and read back; then `commit.py SIDE-explicit-formula add README.md`
"""
import hashlib
import io
import os
import re
import subprocess
import sys
import textwrap

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b757_worklist as K        # noqa: E402

NL = '\n'
EF = K.EF_DIR
JOIN = 'push-b757-join'
REPLACED = ((3, 3), (5, 7), (23, 26))   # ### the spans [B1] names (data/b754_author_answers.txt :88: "README :3, :5-:7 and :23-:26")
SURROUND = 'verified surround'


def g(*a):
    return subprocess.run(['git', '-C', EF] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def rd(name):
    return io.open(os.path.join(D, name), encoding='utf-8').read().replace('\r', '').split(NL)


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def doors_lines():
    """{n: text} quoted under [B1] in data/b754_doors.txt."""
    L, out, inb = rd('b754_doors.txt'), {}, False
    for l in L:
        if l.startswith('  [B1]'):
            inb = True
            continue
        if inb and l.startswith('  [B') and not l.startswith('  [B1]'):
            break
        m = re.match(r'^      :(\d+) "(.*)"$', l)
        if inb and m:
            out[int(m.group(1))] = m.group(2)
    return out


def draft():
    """(the line, its digest, the agenda's digest, (text :3, text :5-:7, text :23-:26))."""
    F = rd('b754_ferry.txt')
    line = [l for l in F if l.strip().startswith('[B1]')]
    A = rd('b754_agenda.txt')
    i = A.index('[B1]') if '[B1]' in A else -1
    want = None
    for l in A[i:i + 14] if i >= 0 else []:
        m = re.search(r'DRAFTED \(data/b754_ferry\.txt :\d+, digest ([0-9a-f]{16})\)', l)
        if m:
            want = m.group(1)
    if len(line) != 1:
        sys.exit('### [B1] NOT READ ONCE IN data/b754_ferry.txt (%d lines) -- nothing written' % len(line))
    s = line[0].strip()
    m = re.search(r'Line :3 replaced by: "(.*?)" Lines :5-:7 replaced by: "(.*?)" Lines :23-:26 replaced by: "(.*?)"\s*$', s)
    if not m:
        sys.exit('### THE THREE REPLACEMENTS NOT READ FROM [B1]`S LINE -- nothing written')
    return s, digest(s), want, (m.group(1), m.group(2), m.group(3))


def phrase756():
    F = rd('b756_ferry.txt')
    l = [x for x in F if x.startswith('(6) ')]
    m = re.search(r'reading in its place "([^"]+)"', l[0]) if len(l) == 1 else None
    return m.group(1) if m else None


def wrap_to(text, n):
    """the text wrapped at word boundaries to n lines where it can be (the narrowest width giving at most n), no word cut."""
    lo, hi = max(len(w) for w in text.split()), len(text)
    best = [text]
    while lo <= hi:
        w = (lo + hi) // 2
        got = textwrap.wrap(text, w, break_long_words=False, break_on_hyphens=False)
        if len(got) <= n:
            best, hi = got, w - 1
        else:
            lo = w + 1
    return best


def cites(text, rev):
    """each parenthesised cite with a .lean path and lines: its backticked names, each read on one of those lines at rev."""
    out = []
    for grp in re.findall(r'\(([^()]*\.lean`?\s*:\d+(?:,\s*:\d+)*)\)', text):
        pm = re.search(r'`?((?:SIDEExplicitFormula|Zeta23)/[^`\s]+\.lean)`?\s*((?::\d+(?:,\s*)?)+)', grp)
        if not pm:
            continue
        path, ns = pm.group(1), [int(x) for x in re.findall(r':(\d+)', pm.group(2))]
        names = [x for x in re.findall(r'`([^`]+)`', grp) if not x.endswith('.lean')]
        src = g('show', '%s:%s' % (rev, path)).split(NL)
        for nm in names:
            hit = [n for n in ns if 0 < n <= len(src) and nm.split('.')[-1] in src[n - 1]]
            out.append((nm, path, ns, bool(hit)))
    return out


def plan(write=False):
    br = g('symbolic-ref', '--short', 'HEAD').strip()
    dirty = [l for l in g('status', '--porcelain', '--untracked-files=no').split(NL) if l.strip()]
    head = g('rev-parse', 'HEAD').strip()
    print('  the kernel on %s at %s ; tracked changes %d' % (br, head[:8], len(dirty)))
    if br != JOIN or dirty:
        sys.exit('### NOT ON %s CLEAN -- nothing written' % JOIN)
    R = g('show', 'HEAD:README.md').replace('\r', '').split(NL)
    if R and R[-1] == '':
        R = R[:-1]
    dl = doors_lines()
    want = sorted(n for a, b in REPLACED for n in range(a, b + 1))
    eq = [(n, n in dl and 0 < n <= len(R) and R[n - 1] == dl[n]) for n in want]
    print('  THE LINES REPLACED, data/b754_doors.txt against README.md at %s (%d lines): %s' % (head[:8], len(R), ' '.join(':%d %s' % (n, 'EQUAL' if e else 'DIFFERS') for n, e in eq)))
    s, dg, dw, texts = draft()
    print('  [B1] FROM data/b754_ferry.txt: %d characters ; digest %s ; the agenda`s %s -> %s' % (len(s), dg, dw, 'EQUAL' if dg == dw else 'DIFFERS'))
    ph = phrase756()
    sur = [t.count(SURROUND) for t in texts]
    print('  (R366)(6)`S PHRASE, read from data/b756_ferry.txt: %s ; "%s" in the three texts: %s' % ('%d characters' % len(ph) if ph else 'NOT READ', SURROUND, sur))
    if not all(e for _n, e in eq) or dg != dw or not ph:
        sys.exit('### A SOURCE NOT AS READ -- nothing written')
    if any(sur):
        sys.exit('### A TEXT CARRIES "%s" WHERE [B1] NAMES NO PHRASE -- nothing written; the seat stops at this write' % SURROUND)
    a, b, c = texts
    B, C = wrap_to(b, 3), wrap_to(c, 4)
    new = R[0:2] + [a] + [R[3]] + B + R[7:22] + C + R[26:]
    print('  THE FORM: :3 one line (%d characters) ; :5-:7 as %d lines ; :23-:26 as %d lines ; the README %d lines against %d -> %s' % (
        len(a), len(B), len(C), len(new), len(R), 'NO OTHER LINE MOVES' if len(B) == 3 and len(C) == 4 else 'LINES MOVE'))
    same = all(new[i] == R[i] for i in range(len(R)) if not any(x - 1 <= i <= y - 1 for x, y in REPLACED)) if len(new) == len(R) else False
    words = (' '.join(new[2:3]) == a, ' '.join(new[4:7]) == b, ' '.join(new[22:26]) == c)
    print('  READ BACK IN MEMORY: every other line equal at its number %s ; the three texts rejoined equal to the draft %s' % (same, words))
    for nm, path, ns, ok in cites(a + ' ' + c, 'HEAD'):
        print('  CITE %s at %s %s: %s' % (nm, path, ', '.join(':%d' % n for n in ns), 'EQUAL' if ok else 'DIFFERS'))
    rl = rd('b536_components.txt')
    print('  CITE h2_sign_iff_rh`s axiom line at relay data/b536_components.txt :12: %s' % ('EQUAL' if len(rl) >= 12 and 'h2_sign_iff_rh' in rl[11] else 'DIFFERS'))
    for i, l in enumerate(new[:28], 1):
        print('    %3d %s' % (i, l[:200] + (' ...' if len(l) > 200 else '')))
    if not (same and all(words)):
        sys.exit('### THE FORM NOT AS WANTED -- nothing written')
    if write:
        p = os.path.join(EF, 'README.md')
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(new) + NL)
        back = io.open(p, encoding='utf-8').read().split(NL)
        back = back[:-1] if back and back[-1] == '' else back
        print('  WRITTEN README.md in the kernel`s working tree: %d lines ; equal to the plan %s ; next: `commit.py SIDE-explicit-formula add README.md`' % (len(back), back == new))


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] not in ('plan', 'write'):
        sys.exit(__doc__)
    plan(write=a[0] == 'write')
