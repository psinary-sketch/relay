# -*- coding: utf-8 -*-
"""b765 under (R375)(6)(c): THE HELD BRANCHES OF SIDE-explicit-formula, READ, a reading and no build.

For each of the four branches (6)(c) names: its commits past main at 819e4a83, its files changed from its merge base with main, and for
each declaration it holds (new or changed from the merge base) whether main at 819e4a83 carries a declaration of that name and statement,
or which order still owes it. Local git alone: no fetch, no remote read. Kernel lines are read by predicate: a declaration's name and the
verdict SAME / ANOTHER STATEMENT / ABSENT are written, no statement text. The orders: the W-ORD names in the branch's own commit subjects
and on the OPEN_TRAILS lines that name the branch, read by line number and name alone, no line text written. The commit subjects pass
through the mask (the kernel's account, the github form, the author's name, address and identifier as tools/b765_address_scan.py reads
them). No branch is removed; nothing is written in the kernel.

Routes: `read` prints, writes nothing; `bank` writes data/b765_held_branches.txt, refused unless this file is committed and unchanged.
`control` runs the reader's own control: a planted text read for its declarations, and one declaration of main read SAME against itself
and ANOTHER STATEMENT against a planted change."""
import collections, datetime, hashlib, io, os, re, subprocess, sys

R = 'D:/relay'
K = 'D:/SIDE-explicit-formula'
PP = 'D:/MY-DOwnloads/PLACE-papers'
MAIN = '819e4a83'
BRANCHES = ('detection-region-b559', 'vendor-bulka-backport-b566', 'grh-weil-b569-held', 'challenge-b720-h2-sign-iff-rh')
BANK = os.path.join(R, 'data', 'b765_held_branches.txt')
ME = 'tools/b765_held_branches.py'
NL = '\n'
DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|partial|unsafe)\s+)*'
                  r'(theorem|lemma|def|abbrev|structure|class|instance|inductive|opaque|axiom)\s+([^\s:({\[]+)')
ORDER = re.compile(r'W-ORD-[A-Z0-9]+(?:-[A-Z0-9]+)*')
sys.path.insert(0, os.path.join(R, 'tools'))
import b765_address_scan as AS   # noqa: E402


def git(repo, *a, ok=False):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode != 0 and not ok:
        raise SystemExit('### git %s failed (exit %d) -- nothing written' % (' '.join(a[:2]), r.returncode))
    return r.stdout if r.returncode == 0 else None


def _account():
    u = git(K, 'remote', 'get-url', 'origin') or ''
    m = re.search(r'github\.com[:/]([^/\s]+)/', u)
    return m.group(1) if m else None


_NEEDLES = [x for x in (AS.author_name(), AS.author_orcid(), AS.previous_address(), _account()) if x and len(x) >= 4]
_GH = re.compile(r'github\.com/[A-Za-z0-9_.-]+')


def mask(s):
    s = _GH.sub('github.com/<account>', s)
    s = AS.ORCID_FORM.sub('<orcid>', s)
    for n in _NEEDLES:
        s = re.sub(re.escape(n), '<identifier>', s, flags=re.I)
    return s


def strip_comments(t):
    out, i, depth, n = [], 0, 0, len(t)
    while i < n:
        if t.startswith('/-', i):
            depth += 1
            i += 2
            continue
        if depth and t.startswith('-/', i):
            depth -= 1
            i += 2
            continue
        c = t[i]
        out.append(('\n' if c == '\n' else ' ') if depth else c)
        i += 1
    return NL.join(re.sub(r'--.*$', '', l) for l in ''.join(out).split(NL))


def decls(text):
    """{full name: the statement normalized}: from the keyword to the first `:=` or a closing ` where`, comments removed, namespaces
    tracked by `namespace` / `section` / `end`."""
    L = strip_comments(text).split(NL)
    ns, out = [], {}
    for k, l in enumerate(L):
        m = re.match(r'^\s*namespace\s+(\S+)', l)
        if m:
            ns.append(m.group(1))
            continue
        if re.match(r'^\s*(?:noncomputable\s+)?section\b', l):
            ns.append(None)
            continue
        if re.match(r'^\s*end(?:\s+\S+)?\s*$', l):
            if ns:
                ns.pop()
            continue
        m = DECL.match(l)
        if not m or m.group(2).startswith(':'):
            continue
        buf = []
        for j in range(k, min(k + 60, len(L))):
            if j > k and DECL.match(L[j]):
                break
            buf.append(L[j])
            if ':=' in L[j] or re.search(r'\swhere\s*$', L[j]):
                break
        sig = ' '.join(buf).split(':=')[0]
        sig = re.sub(r'\swhere\s*$', '', sig)
        sig = re.sub(r'\s+', ' ', sig).strip()
        sig = re.sub(r'^(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|partial|unsafe)\s+)*', '', sig)
        name = m.group(2)
        full = name[len('_root_.'):] if name.startswith('_root_.') else '.'.join([x for x in ns if x] + [name])
        out[full] = sig
    return out


def show(rev, path):
    return git(K, 'show', '%s:%s' % (rev, path), ok=True)


def main_index(shorts):
    files = set()
    for s in shorts:
        for l in (git(K, 'grep', '-l', '-F', s, MAIN, '--', '*.lean', ok=True) or '').splitlines():
            files.add(l.split(':', 1)[1] if ':' in l else l)
    idx = collections.defaultdict(dict)
    for f in sorted(files):
        t = show(MAIN, f)
        if t is not None:
            for full, sig in decls(t).items():
                idx[full][f] = sig
    return idx


def verdict(full, sig, idx):
    m = idx.get(full) or {}
    if not m:
        return 'ABSENT', []
    same = sorted(f for f, s in m.items() if s == sig)
    if same:
        return 'SAME', same
    return 'ANOTHER STATEMENT', sorted(m)


def trail_orders(T, b):
    rows = []
    for n, l in enumerate(T, 1):
        if b in l:
            rows.append((n, sorted(set(ORDER.findall(l)))))
    return rows


def read_branch(b, T):
    ref = None
    for cand in ('refs/heads/' + b, 'refs/remotes/origin/' + b):
        if git(K, 'rev-parse', '--verify', '-q', cand, ok=True):
            ref = cand
            break
    if not ref:
        return dict(branch=b, ref=None)
    tip = git(K, 'rev-parse', ref).strip()
    base = git(K, 'merge-base', MAIN, tip).strip()
    commits = []
    for l in git(K, 'log', '--format=%h|%cI|%s', '%s..%s' % (MAIN, tip)).splitlines():
        h, d, s = l.split('|', 2)
        commits.append((h, d[:19], mask(s)))
    files = [tuple(l.split('\t')[::len(l.split('\t')) - 1]) for l in git(K, 'diff', '--name-status', base, tip).splitlines()]
    own = {}
    for st, path in files:
        if path.endswith('.lean') and st[0] in 'AMR':
            at_tip = decls(show(tip, path) or '')
            at_base = decls(show(base, path) or '') if st[0] != 'A' else {}
            for full, sig in at_tip.items():
                if at_base.get(full) != sig:
                    own[full] = (path, sig, 'new' if full not in at_base else 'changed')
    idx = main_index(sorted(set(n.split('.')[-1] for n in own)))
    rows = []
    for full in sorted(own):
        path, sig, how = own[full]
        v, where = verdict(full, sig, idx)
        rows.append((full, how, path, v, where))
    sub_orders = sorted(set(o for c in commits for o in ORDER.findall(c[2])))
    tl = trail_orders(T, b)
    return dict(branch=b, ref=ref, tip=tip, base=base, past=len(commits),
                behind=int(git(K, 'rev-list', '--count', '%s..%s' % (tip, MAIN)).strip()), commits=commits, files=files, rows=rows,
                sub_orders=sub_orders, trail=tl, trail_orders=sorted(set(o for _, os_ in tl for o in os_)))


def control():
    """the reader's own control, as wanted: the planted text's five declarations read with their namespaces, the commented one not; a
    declaration of main read SAME against itself and ANOTHER STATEMENT against a planted change; the mask over a planted line."""
    planted = NL.join(['namespace A', '/-- doc theorem fake : 1 = 2 := rfl -/', 'theorem t1 (x : Nat) :', '    x = x := rfl',
                       '-- theorem commented : True := trivial', 'namespace B', 'def d1 : Nat := 1', 'end B', 'noncomputable section',
                       'structure S where', '  a : Nat', 'end', 'end A', 'lemma _root_.top_l : True := trivial', 'abbrev ab := 3'])
    got = decls(planted)
    want = {'A.t1': 'theorem t1 (x : Nat) : x = x', 'A.B.d1': 'def d1 : Nat', 'A.S': 'structure S', 'top_l': 'lemma _root_.top_l : True',
            'ab': 'abbrev ab'}
    ok1 = got == want
    t = show(MAIN, 'SIDEExplicitFormula/H2Sign.lean') or ''
    dm = decls(t)
    nm = 'SIDEExplicitFormula.B321.h2_sign_imp_aim'
    idx = {nm: {'SIDEExplicitFormula/H2Sign.lean': dm.get(nm)}}
    ok2 = dm.get(nm) is not None and verdict(nm, dm[nm], idx)[0] == 'SAME' and verdict(nm, dm[nm] + ' x', idx)[0] == 'ANOTHER STATEMENT' \
        and verdict(nm + 'Z', dm[nm], idx)[0] == 'ABSENT'
    # ### the ORCID needle is masked by its form to <orcid> before the needles are read, as scratch mask760.py's control reads it: either
    # ### placeholder is the mask (the first run, 12:46:59Z, wanted <identifier> alone and read NOT AS WANTED, nothing read further)
    ok3 = all(('<identifier>' in mask('a %s b' % n) or '<orcid>' in mask('a %s b' % n)) and n not in mask('a %s b' % n) for n in _NEEDLES) \
        and mask('see github.com/abc/def') == 'see github.com/<account>/def'
    lines = ['  THE READER`S CONTROL: the planted text read for its declarations %s (%d read, %d wanted) ; a declaration of main at %s '
             '(H2Sign.lean, h2_sign_imp_aim) read SAME against itself, ANOTHER STATEMENT against a planted change, ABSENT by another name '
             '%s ; the mask over each of its %d needles and the github form %s ; %s' % (
                 ok1, len(got), len(want), MAIN, ok2, len(_NEEDLES), ok3, 'AS WANTED' if ok1 and ok2 and ok3 else 'NOT AS WANTED')]
    return lines, ok1 and ok2 and ok3


def self_commit():
    blob = git(R, 'hash-object', ME).strip()
    head = (git(R, 'rev-parse', 'HEAD:' + ME, ok=True) or '').strip()
    st = (git(R, 'status', '--porcelain', '--', ME) or '').strip()
    if blob != head or st:
        raise SystemExit('### %s differs from its blob at HEAD or is not committed -- the bank refused, nothing written' % ME)
    return git(R, 'rev-parse', '--short=8', 'HEAD').strip(), hashlib.sha256(io.open(os.path.join(R, ME), 'rb').read()).hexdigest()[:16]


def compose(rs, cl, at, tool):
    L = ['b765 -- THE HELD BRANCHES OF SIDE-explicit-formula, READ UNDER (R375)(6)(c): A READING AND NO BUILD (%s)' % at, '',
         '### the reader tools/b765_held_branches.py%s; local git alone, no fetch and no remote read; main at %s (%s). For each branch: its '
         'commits past main,' % ((', sha256 %s, committed at relay %s before its run' % (tool[1], tool[0])) if tool else '', MAIN,
                                    git(K, 'rev-parse', MAIN).strip()[:12]),
         '### its files changed from its merge base with main, and for each declaration it holds (new or changed from the merge base) its '
         'verdict: SAME (main carries',
         '### a declaration of that name and statement), ANOTHER STATEMENT (the name on main, its statement differing) or ABSENT (no '
         'declaration of that name on main),',
         '### read by predicate, no statement text written. The orders: the W-ORD names in the branch`s own commit subjects and on the '
         'OPEN_TRAILS lines naming the branch,',
         '### by line number and name alone. No branch of the four is removed.', '']
    L += cl + ['']
    summ = []
    for r in rs:
        b = r['branch']
        L.append('## %s' % b)
        if not r['ref']:
            L.append('  NO LOCAL REF: not read')
            summ.append((b, None))
            continue
        L.append('  the ref %s at %s ; the merge base with main %s ; commits past main %d ; main past the branch %d' % (
            r['ref'], r['tip'][:8], r['base'][:8], r['past'], r['behind']))
        for h, d, s in r['commits']:
            L.append('    commit %s %s %s' % (h, d, s))
        L.append('  files changed from the merge base: %d' % len(r['files']))
        for st, p in r['files']:
            L.append('    %s %s' % (st, p))
        c = collections.Counter(x[3] for x in r['rows'])
        L.append('  its declarations, new or changed from the merge base: %d ; SAME %d ; ANOTHER STATEMENT %d ; ABSENT %d' % (
            len(r['rows']), c['SAME'], c['ANOTHER STATEMENT'], c['ABSENT']))
        for full, how, path, v, where in r['rows']:
            L.append('    %s ; %s ; %s ; %s%s' % (full, how, path, v, (' (%s)' % ', '.join(where)) if where and v != 'SAME' or (where and where != [path]) else ''))
        owed = sorted(set(r['sub_orders']) | set(r['trail_orders']))
        L.append('  the orders: in its commit subjects %s ; on the OPEN_TRAILS lines naming it %s (lines %s)' % (
            r['sub_orders'] or 'none', r['trail_orders'] or 'none', ', '.join(':%d' % n for n, _ in r['trail']) or 'none'))
        absent = [x[0].split('.')[-1] for x in r['rows'] if x[3] != 'SAME']
        same = [x[0].split('.')[-1] for x in r['rows'] if x[3] == 'SAME']
        if not r['rows']:
            field = 'no declaration of its own'
        elif not absent:
            field = 'carried on main by its %d declarations, each of that name and statement' % len(same)
        elif not same:
            field = 'still owed under %s, none of its %d declarations on main by name and statement' % (' and '.join(owed) or 'no order named', len(absent))
        else:
            field = 'carried on main by %d of its %d declarations (%s); %s still owed under %s' % (
                len(same), len(r['rows']), ', '.join(same) if len(same) <= 8 else '%d named above' % len(same),
                ', '.join(absent) if len(absent) <= 8 else '%d named above' % len(absent), ' and '.join(owed) or 'no order named')
        L.append('  [B2]`S FIELD FOR IT: %s' % field)
        L.append('')
        summ.append((b, field))
    L.append('## THE READING')
    for b, f in summ:
        L.append('  %s: %s' % (b, f if f else 'not read'))
    L.append('  no branch removed')
    return L, summ


def main():
    a = sys.argv[1:]
    if not a or a[0] not in ('read', 'bank', 'control'):
        sys.exit('### usage: b765_held_branches.py read | bank | control')
    cl, ok = control()
    print(NL.join(cl))
    if not ok:
        sys.exit('### THE READER`S CONTROL NOT AS WANTED -- nothing read further, nothing written')
    if a[0] == 'control':
        return
    tool = self_commit() if a[0] == 'bank' else None
    T = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read().replace('\r', '').split(NL)
    rs = [read_branch(b, T) for b in BRANCHES]
    at = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    L, summ = compose(rs, cl, at, tool)
    for r in rs:
        if r['ref']:
            c = collections.Counter(x[3] for x in r['rows'])
            print('  %s at %s: past main %d ; files %d ; declarations %d ; SAME %d ; ANOTHER STATEMENT %d ; ABSENT %d ; orders %s %s ; trail lines %s' % (
                r['branch'], r['tip'][:8], r['past'], len(r['files']), len(r['rows']), c['SAME'], c['ANOTHER STATEMENT'], c['ABSENT'],
                r['sub_orders'], r['trail_orders'], [n for n, _ in r['trail']]))
            for full, how, path, v, where in r['rows']:
                if v != 'SAME':
                    print('    %s ; %s ; %s ; %s' % (full, how, path, v))
        else:
            print('  %s: NO LOCAL REF' % r['branch'])
    for b, f in summ:
        print('  [B2] %s: %s' % (b, f))
    if a[0] == 'bank':
        s = NL.join(L) + NL
        with io.open(BANK, 'w', encoding='utf-8', newline='\n') as f:
            f.write(s)
        print('written data/b765_held_branches.txt: %d lines, %d bytes, sha256 %s' % (len(L), len(s.encode('utf-8')),
                                                                                      hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]))


if __name__ == '__main__':
    main()
