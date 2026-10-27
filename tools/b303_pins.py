# -*- coding: utf-8 -*-
"""b303_pins.py -- THE PINS, ### **BY `ls-remote` ACROSS EVERY REPOSITORY THE ROSTER NAMES.**

### WHY THIS IS A TOOL AND NOT THREE SHELL LINES. ### b301 and b302 recorded their pins by typing
### what `git` printed. ### **THAT IS A SHELL-TYPED NUMBER IN EVERYTHING BUT NAME** -- the
### ahead/behind pair is COMPUTED, and `W-ORD-ADHOC-CHECK-FIXTURES` (b298) is about exactly this
### species. ### So the pair is computed here, by `git rev-list --left-right --count`, and the
### PARSER that reads it carries both polarities.

### ### **WHAT IT DOES NOT DO: ### IT DOES NOT PUSH.** ### It reads. ### A tool that could push
### while reporting the read-back would be reporting its own effect, and the read-back's whole
### value is that it is a SECOND observation of a state a DIFFERENT command produced.

### ### **THE EMPTY-SCOPE LAW (b167, and b299's `G-ADDITIVE` species): ### A REPO THAT DOES NOT
### ### RESOLVE IS REPORTED AS UNRESOLVED AND HARD-FAILS. ### IT IS NEVER SILENTLY 0/0**, because
### an unreachable remote and a synchronised remote print the same reassuring zero otherwise.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPOS = [
    ('relay', r'D:\relay'),
    ('SIDE-global-section', r'D:\SIDE-global-section'),
    ('PLACE-papers', r'D:\MY-DOwnloads\PLACE-papers'),
    ('SIDE-effects', r'D:\SIDE-effects'),
]

# ### b715, (R325)(6): THE ROSTER WIDENED -- every repository a day paper's Correspondence, the census v0.8.1 or FACES_LEDGER names, read
# ### from those texts on PLACE-papers main at the run; the four above kept first, as before. A name is read where it stands in a text as
# ### a repository of the account (data/repo_visibility.txt's rows) or as a SIDE-* name; `relay` is read from the four alone (the word is
# ### prose in every text). Each printed with its local head, ls-remote, behind/ahead and its visibility from data/repo_visibility.txt; a
# ### repository with no local clone at D:\<name> is printed UNRESOLVED and hard-fails, as the empty-scope law reads (no URL is built).
PP = r'D:\MY-DOwnloads\PLACE-papers'
VIS = os.path.join(ROOT, 'data', 'repo_visibility.txt')
TEXTS_WHOLE = ('phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md', 'FACES_LEDGER.md')
NAME = re.compile(r'(?<![\w.-])(SIDE-[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*)(?![\w-])')


def visibility():
    """{name: PRIVATE | PUBLIC} from data/repo_visibility.txt's rows `VIS | name | ...`."""
    out = {}
    for l in open(VIS, encoding='utf-8').read().split('\n') if os.path.isfile(VIS) else []:
        p = [x.strip() for x in l.split('|')]
        if len(p) >= 2 and p[0] in ('PRIVATE', 'PUBLIC'):
            out[p[1]] = p[0]
    return out


def correspondence(text):
    """every Correspondence section of a text: from its heading to the next heading of its level or above."""
    L, out, i = text.split('\n'), [], 0
    while i < len(L):
        m = re.match(r'^(#+) .*Correspondence', L[i])
        if m:
            lvl, j = len(m.group(1)), i + 1
            while j < len(L) and not (re.match(r'^#+ ', L[j]) and len(re.match(r'^(#+)', L[j]).group(1)) <= lvl):
                j += 1
            out.append('\n'.join(L[i:j]))
            i = j
        else:
            i += 1
    return '\n'.join(out)


def texts(rev='main'):
    """[(source, text)]: each day paper's Correspondence (day1/*.md on main carrying one, the superseded `_v<n>` copies out) and the
    census v0.8.1 and FACES_LEDGER whole."""
    rc, tree = git(PP, 'ls-tree', '-r', '--name-only', rev)
    out = []
    for p in sorted(x for x in tree.splitlines() if x.startswith('day1/') and x.endswith('.md') and not re.search(r'_v\d+(_\d+)*\.md$', x)):
        c = correspondence(git(PP, 'show', '%s:%s' % (rev, p))[1])
        if c:
            out.append(('%s (its Correspondence)' % p, c))
    for p in TEXTS_WHOLE:
        out.append((p, git(PP, 'show', '%s:%s' % (rev, p))[1]))
    return out


def names_in(text, known):
    """the account's repositories a text names: SIDE-* names, and every other known name standing as a word (`relay` excepted)."""
    got = set(NAME.findall(text))
    for n in known:
        if not n.startswith('SIDE-') and n != 'relay' and re.search(r'(?<![\w.-])%s(?![\w-])' % re.escape(n), text):
            got.add(n)
    return got


def path_of(name):
    return dict(REPOS).get(name, os.path.join('D:\\', name))


def roster(src=None):
    """the widened roster: [(name, path, sources)], the four first, then every name the texts carry, sorted."""
    known = visibility()
    src = texts() if src is None else src
    named = {}
    for s, t in src:
        for n in names_in(t, known):
            named.setdefault(n, []).append(s)
    out = [(n, p, named.get(n, ['b714`s roster'])) for n, p in REPOS]
    out += [(n, path_of(n), named[n]) for n in sorted(named) if n not in dict(REPOS)]
    return out, src


def git(repo, *args):
    """### RETURNS `(rc, stdout)`. ### **stderr IS NOT SWALLOWED INTO stdout** -- a tool that
    reads an error message as data is how a miss becomes a value."""
    p = subprocess.Popen(['git', '-C', repo] + list(args),
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _err = p.communicate()
    return p.returncode, out.decode('utf-8', 'replace').strip()


def parse_left_right(text):
    """### `git rev-list --left-right --count A...B` prints `behind<TAB>ahead`.

    ### **RETURNS `None` ON ANYTHING IT DOES NOT UNDERSTAND**, rather than a pair of zeros --
    ### which is the whole reason this is a function with fixtures instead of a `split()`.
    """
    parts = text.split()
    if len(parts) != 2:
        return None
    try:
        return int(parts[0]), int(parts[1])
    except ValueError:
        return None


def self_test(verbose=True):
    """### **BOTH POLARITIES ON THE PARSER, AND THE NEAR-MISSES ARE THE POINT.**"""
    cases = [
        ('a real pair, tab-separated', '0\t1', (0, 1)),
        ('a real pair, space-separated', '2 3', (2, 3)),
        ('both zero -- the synchronised state', '0\t0', (0, 0)),
        ('### an error message, NOT a pair', 'fatal: bad revision', None),
        ('### empty output -- the silent-zero trap', '', None),
        ('### one number only', '4', None),
        ('### three numbers', '1 2 3', None),
        ('### a non-integer', 'a\tb', None),
    ]
    bad = 0
    if verbose:
        print('  %-46s %-22s %s' % ('parser fixture', 'got/expected', 'agree'))
    for lbl, text, expect in cases:
        got = parse_left_right(text)
        ok = (got == expect)
        bad += 0 if ok else 1
        if verbose:
            print('  %-46s %-22s %s' % (lbl, '%s/%s' % (got, expect),
                                        'YES' if ok else '### NO ###'))
    return bad == 0


def control():
    """(R325)(6)'s control: the four repositories of b714's roster read as before (first, at their paths), and a repository named in no
    text not added (the record: a repository of the visibility map no text names; the constructed: a planted text naming one name)."""
    known = visibility()
    ros, src = roster()
    names = [n for n, _p, _s in ros]
    res = []

    def case(kind, what, got, want):
        res.append(got == want)
        print('  %-11s %s : got %s ; wanted %s ; %s' % (kind, what, got, want, 'AS WANTED' if got == want else '### NOT AS WANTED'))
    case('RECORD', 'the four of b714`s roster first, at their paths', [(n, p) for n, p, _s in ros[:4]], REPOS)
    unnamed = sorted(n for n in known if not any(n in names_in(t, known) for _s, t in src) and n != 'relay')
    case('RECORD', 'the repositories of the visibility map no text names (%d, e.g. %s): none in the roster' % (len(unnamed), unnamed[:3]),
         [n for n in unnamed if n in names], [])
    planted, _ = roster([('a planted text', 'see SIDE-kernel and glassbead-game; the relay is prose')])
    case('CONSTRUCTED', 'a planted text naming SIDE-kernel and glassbead-game: the roster the four and those two',
         [n for n, _p, _s in planted], [n for n, _p in REPOS] + ['SIDE-kernel', 'glassbead-game'])
    case('CONSTRUCTED', 'the same text with neither name: the four alone', [n for n, _p, _s in roster([('a planted text', 'no names here')])[0]],
         [n for n, _p in REPOS])
    print('  ### ### **PINS ROSTER CONTROLS %d ; AS WANTED %d ; ALL AS WANTED %s.**' % (len(res), sum(res), all(res)))
    return 0 if all(res) else 1


def main(argv):
    label = argv[0] if argv else 'PINS'
    if label == 'control':
        return control()
    ros, src = roster()
    vis = visibility()
    print('=' * 100)
    print('b303_pins.py -- %s. ### BY `ls-remote`, ALL %d REPOS THE ROSTER NAMES (the four of b714`s roster, then every repository the '
          'texts name: %d texts read from PLACE-papers main).' % (label, len(ros), len(src)))
    print('=' * 100)
    ok_suite = self_test()
    print('  parser self-test : %s' % ('PASS' if ok_suite else '### FAIL ###'))
    if not ok_suite:
        print('  ### REFUSING TO REPORT PINS FROM A PARSER THAT FAILS ITS OWN FIXTURES.')
        return 2
    print()

    hard = 0
    for name, path, srcs in ros:
        print('--- %s   (%s)   visibility %s   named by %s' % (name, path, vis.get(name, '### NOT IN data/repo_visibility.txt'),
                                                          '; '.join(srcs)))
        if not os.path.isdir(os.path.join(path, '.git')):
            print('    ### HARD FAILURE -- NOT A GIT REPOSITORY.')
            hard += 1
            continue
        rc_h, head = git(path, 'rev-parse', 'HEAD')
        rc_r, rem = git(path, 'ls-remote', 'origin', 'refs/heads/main')
        remote_sha = rem.split()[0] if (rc_r == 0 and rem.split()) else None
        print('    local HEAD   : %s' % (head if rc_h == 0 else '### UNRESOLVED'))
        print('    ls-remote    : %s' % (remote_sha or '### UNRESOLVED'))
        if rc_h != 0 or not remote_sha:
            print('    ### HARD FAILURE -- A REPO THAT DOES NOT RESOLVE IS NOT 0/0.')
            hard += 1
            continue
        rc_c, cnt = git(path, 'rev-list', '--left-right', '--count',
                        '%s...HEAD' % remote_sha)
        pair = parse_left_right(cnt) if rc_c == 0 else None
        if pair is None:
            print('    ### HARD FAILURE -- THE AHEAD/BEHIND PAIR DID NOT PARSE: %r' % cnt)
            hard += 1
            continue
        behind, ahead = pair
        print('    behind/ahead : %d / %d' % (behind, ahead))
        print('    equal        : %s' % (head == remote_sha))
        rc_d, dirty = git(path, 'status', '--porcelain')
        untracked = [l for l in dirty.splitlines() if l.startswith('??')]
        tracked = [l for l in dirty.splitlines() if not l.startswith('??')]
        print('    working tree : %d tracked change(s), %d untracked'
              % (len(tracked), len(untracked)))

    print()
    print('  ### REPOS HARD-FAILING : %d' % hard)
    print('  ### **A PIN IS A SHA READ BACK FROM THE REMOTE. ### IT SAYS WHAT IS THERE,')
    print('  ### NOT THAT WHAT IS THERE IS RIGHT.**')
    print('=' * 100)
    return 0 if hard == 0 else 2


class _Tee(object):
    def __init__(self, *s):
        self.s = s

    def write(self, x):
        for s in self.s:
            s.write(x)

    def flush(self):
        for s in self.s:
            s.flush()


def bank(argv):
    """(R325)(6): the run's print banked whole as data/<act>_pins_census.txt, <act> read from data/act_current.json (b715)."""
    import contextlib
    import io
    import json
    act = json.load(open(os.path.join(ROOT, 'data', 'act_current.json'), encoding='utf-8'))['act']
    buf = io.StringIO()
    with contextlib.redirect_stdout(_Tee(sys.stdout, buf)):
        rc = main(argv or ['THE PINS CENSUS, WIDENED'])
        print('  exit %d' % rc)
        control()
    p = os.path.join(ROOT, 'data', '%s_pins_census.txt' % act)
    with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        f.write(buf.getvalue())
    os.replace(p + '.tmp', p)
    print('bank', p)
    return rc


if __name__ == '__main__':
    if sys.argv[1:2] == ['bank']:
        sys.exit(bank(sys.argv[2:]))
    sys.exit(main(sys.argv[1:]))
