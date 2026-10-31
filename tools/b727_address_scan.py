# -*- coding: utf-8 -*-
"""b727_address_scan.py -- (R332)(9)(i): NO NEW OCCURRENCE OF THE AUTHOR'S NAME OR E-MAIL ADDRESS. Written whole at b722 by the Write tool,
carried to b727 (data/b727_carry_address_scan.txt), its carry-time repairs and the author's word at b727's Component 1 marked ### b727.
### b727, the carry's note: this file came from tools/b726_address_scan.py by the act names' shift alone, so every "### b727" mark below
### but the import line's repair was b726's own mark, shifted (the substitution class (R337)(2)(ix) names); the second name arm is b726's
### Component 1 work on the author's word, and the byline reader is tools/b722_llm_line.py.
### b727 carry-time repair (class (ix), (R337)(2)(v)'s): :2 and the bank's title name (R332)(9)(i) and b722 again, as tools/b722_address_scan.py
### :2 wrote them; the carries of b726 and b727 had shifted them to (R333)/(R336) and b723/b726.

  ### b727, the author's word at Component 1: a second name arm -- the previous user.name read from the history (the author field of
  ### 30c0b3c8, the last relay commit before b726's step zero 91cb997e), held in memory as the address is, its count printed alone as
  ### "PREVIOUS NAME: <count>"; its planted control in memory, the address and that name each counted once in one string built and dropped,
  ### AS WANTED when each count is 1; nothing written to disk by the control. The byline arm stands beside it.

  scan [--bank]   the previous address read from history -- the author and committer e-mails of relay's commits up to the act's base, less
                  the GitHub noreply form, which must leave exactly one address -- and the author's name read from the monograph's byline
                  (tools/b726_llm_line.py monograph(), at run time); both held in memory, neither printed. Counted, as NEW occurrences:
                  every commit of relay and PLACE-papers from the act's base to HEAD (author and committer names and e-mails, the message,
                  the lines the commit adds), the working trees' added lines not yet committed, and every untracked bank of the act under
                  relay data/ (its whole text). Occurrences already in the history stay as the record and are not read. Printed:
                  "PREVIOUS ADDRESS: <count>" and "THE AUTHOR'S NAME: <count>", each alone, with the places counted by kind -- never the
                  address or the name. THE CONTROLS FIRST: a planted line carrying each, counted 1 each, and a clean line counted 0.
                  --bank writes data/b727_address_scan.txt.
"""
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b727_worklist as K   # noqa: E402

ACT = 'b727'
PP = K.PP
NOREPLY = 'users.noreply.github.com'


def git(repo, *a):
    return subprocess.run(['git', '-C', repo, *a], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def previous_address():
    """the one address of relay's history up to the act's base that is not the noreply form; anything else refuses."""
    seen = set(x.strip().lower() for x in git(ROOT, 'log', '--format=%ae%n%ce', K.PRE_RELAY).split(NL) if x.strip())
    old = sorted(x for x in seen if not x.endswith(NOREPLY) and '@' in x)
    if len(old) != 1:
        sys.exit('### THE HISTORY CARRIES %d ADDRESSES OTHER THAN THE NOREPLY FORM, NOT ONE -- NOTHING READ' % len(old))
    return old[0]


def author_name():
    import b722_llm_line as LL   # ### b727 carry-time repair: the shift named b726_llm_line, which does not exist; b722's read, as b726 read it
    n = (LL.monograph()[5] or '').strip()
    if len(n) < 4:
        sys.exit('### THE BYLINE NOT READ -- NOTHING READ')
    return n


USERNAME_REF = '91cb997e~1'   # ### b727: 30c0b3c8, the last relay commit before b726's step zero (b726's act_current, 91cb997e)


def previous_username():
    """### b727, the author's word: the previous user.name, the author field of USERNAME_REF; refuses when it is unset or the login."""
    n = git(ROOT, 'log', '-1', '--format=%an', USERNAME_REF).strip()
    login = subprocess.run(['gh', 'api', 'user', '--jq', '.login'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()
    if len(n) < 2 or n == login:
        sys.exit('### THE PREVIOUS user.name NOT READ (unset, or the account login) -- NOTHING READ')
    return n


def count(text, needle):
    return text.lower().count(needle.lower())


def added(diff):
    return NL.join(l[1:] for l in diff.split(NL) if l.startswith('+') and not l.startswith('+++'))


SITTING_REPOS = (('D:/SIDE-archimedean', 'SIDE-archimedean', 'fcecc45'), ('D:/SIDE-frobenius', 'SIDE-frobenius', '2efe9f2'),
                 ('D:/SIDE-spinor', 'SIDE-spinor', '7e570ee'), ('D:/SIDE-rcurve', 'SIDE-rcurve', '54c9040'),
                 ('D:/SIDE-cosmo', 'SIDE-cosmo', 'ca04c8c'), ('D:/SIDE-kernel', 'SIDE-kernel', '70aba3c'),
                 ('D:/SIDE-lv-conservation', 'SIDE-lv-conservation', 'd38f3e8'))   # ### b727, (R337)(3): the seven repositories the sitting writes, at their heads before it
BYLINE_FILE = 'day1/Which_Structure_Confines_v2_4_0.md'   # ### b727, (R337)(3) and (5): item [46]'s byline and two self-citations, under I-23
BYLINE_KIND = 'THE [46] BYLINE, EXCEPTED UNDER I-23'
BYLINE_MAX = 3   # ### the byline and two self-citations, one occurrence each: more than three is not the exception


def split_byline(diff):
    """### b727: the diff less BYLINE_FILE's section, and that section's added lines."""
    rest, by = [], []
    for sec in ('\n' + diff).split('\ndiff --git '):
        (by if sec.split(NL, 1)[0].endswith('/' + BYLINE_FILE) else rest).append(sec)
    return '\ndiff --git '.join(rest), added(NL.join(by))


def places():
    """(kind, label, text): the new text the act wrote, by place."""
    out = []
    for repo, name, pre in ((ROOT, 'relay', K.PRE_RELAY), (PP, 'PLACE-papers', K.PRE_PP)) + tuple((r, n, p) for r, n, p in SITTING_REPOS):
        for h in [x for x in git(repo, 'rev-list', '--reverse', '%s..HEAD' % pre).split(NL) if x.strip()]:
            out.append(('commit fields', '%s %s' % (name, h[:8]), git(repo, 'log', '-1', '--format=%an%n%ae%n%cn%n%ce', h)))
            out.append(('commit message', '%s %s' % (name, h[:8]), git(repo, 'log', '-1', '--format=%B', h)))
            rest, by = split_byline(git(repo, 'show', '--format=', '--no-color', '--no-ext-diff', h))
            out.append(('commit added lines', '%s %s' % (name, h[:8]), added(rest)))
            if by:
                out.append((BYLINE_KIND, '%s %s' % (name, h[:8]), by))
        rest, by = split_byline(git(repo, 'diff', '--no-color', '--no-ext-diff', 'HEAD'))
        out.append(('working tree added lines', name, added(rest)))
        if by:
            out.append((BYLINE_KIND, name + ' working tree', by))
    tracked = set(git(ROOT, 'ls-files', '--', 'data/').split(NL))
    for f in sorted(os.listdir(D)):
        p = 'data/' + f
        if f.startswith(ACT + '_') and os.path.isfile(os.path.join(D, f)) and p not in tracked and not f.endswith(('.gz', '.png')):
            out.append(('untracked bank', p, open(os.path.join(D, f), encoding='utf-8', errors='replace').read()))
    return out


def scan(*a):
    t0 = time.time()
    addr, name, uname = previous_address(), author_name(), previous_username()
    ctl = [('a planted line carrying the address', count('x %s y' % addr, addr) == 1 and count('x %s y' % addr, name) == 0),
           ('a planted line carrying the name', count('x %s y' % name, name) == 1 and count('x %s y' % name, addr) == 0),
           ('a clean line', count('the noreply form ' + NOREPLY, addr) == 0 and count('the noreply form ' + NOREPLY, name) == 0
            and count('the noreply form ' + NOREPLY, uname) == 0)]
    s = 'control %s between %s end' % (addr, uname)   # ### b727: the author's word's control, one string built and dropped in memory
    ctl.append(('the address and the previous user.name, once each', count(s, addr) == 1 and count(s, uname) == 1))
    del s
    L = ['%s -- (R332)(9)(i): NO NEW OCCURRENCE OF THE AUTHOR`S NAME OR E-MAIL ADDRESS (%s)' % (ACT, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
         '', '### the previous address read from relay`s history to %s (author and committer e-mails less the noreply form: one address), the' % K.PRE_RELAY[:8],
         '### name from the monograph`s byline at run time, the previous user.name from 30c0b3c8`s author field (b727); all held in memory, none printed. New text only: the commits from relay %s and' % K.PRE_RELAY[:8],
         '### PLACE-papers %s to HEAD (fields, messages, added lines), the uncommitted added lines, the untracked banks of %s.' % (K.PRE_PP[:8], ACT), '',
         '## THE CONTROLS FIRST']
    L += ['  %-40s %s' % (w, 'AS WANTED' if ok else 'NOT AS WANTED') for w, ok in ctl]
    if not all(ok for _w, ok in ctl):
        print(NL.join(L))
        sys.exit('### A CONTROL NOT AS WANTED -- NOTHING COUNTED')
    P = places()
    by = {}
    exc = []
    na = nn = nu = 0
    for kind, label, text in P:
        x, y, z = count(text, addr), count(text, name), count(text, uname)
        if kind == BYLINE_KIND and x == 0 and y <= BYLINE_MAX and z <= BYLINE_MAX:   # ### b727: named in the bank, not counted; beyond this it counts
            exc.append('  %s: %s: address %d ; name %d ; previous user.name %d (at most %d)' % (kind, label, x, y, z, BYLINE_MAX))
            continue
        na, nn, nu = na + x, nn + y, nu + z
        k = by.setdefault(kind, [0, 0, 0, 0])
        k[0] += 1
        k[1] += x
        k[2] += y
        k[3] += z
    L += ['', '## THE PLACES READ, BY KIND (places ; address ; name ; previous user.name)']
    L += ['  %-28s %4d ; %d ; %d ; %d' % (k, v[0], v[1], v[2], v[3]) for k, v in sorted(by.items())]
    hits = sorted(set('%s %s' % (kind, label) for kind, label, text in P if kind != BYLINE_KIND and (count(text, addr) or count(text, name) or count(text, uname))))
    L += ['', '## THE PLACES WITH AN OCCURRENCE (by place, never the text): %s' % ('; '.join(hits) if hits else 'NONE')]
    L += ['', '## THE EXCEPTION OF (R337)(5), [46]`S BYLINE AND TWO SELF-CITATIONS AT %s, UNDER I-23, NAMED AND NOT COUNTED: %s' % (BYLINE_FILE, 'none yet' if not exc else '')] + exc
    L += ['', 'PREVIOUS ADDRESS: %d' % na, 'THE AUTHOR`S NAME: %d' % nn, 'PREVIOUS NAME: %d' % nu, '',
          '### ### **PREVIOUS ADDRESS: %d ; THE AUTHOR`S NAME: %d ; PREVIOUS NAME: %d ; PLACES %d ; CONTROLS %d OF %d AS WANTED ; %d s.**' % (
              na, nn, nu, len(P), len(ctl), len(ctl), int(time.time() - t0))]
    text = NL.join(L)
    if addr in text.lower() or name.lower() in text.lower() or uname.lower() in text.lower():
        sys.exit('### THE BANK WOULD CARRY THE ADDRESS OR THE NAME -- NOTHING PRINTED OR WRITTEN')
    print(text)
    if '--bank' in a:
        p = os.path.join(D, '%s_address_scan.txt' % ACT)
        with open(p + '.tmp', 'wb') as fh:
            fh.write((text + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_address_scan.txt' % ACT)
    return na, nn, nu


if __name__ == '__main__':
    fn = dict(scan=scan).get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        sys.exit('usage: b727_address_scan.py scan [--bank]')
    fn(*sys.argv[2:])
