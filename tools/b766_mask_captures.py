# -*- coding: utf-8 -*-
"""b766, (R376)(7) [K23], by the author's word of 2026-11-22 ("The seven captures: mask the account."): b765's captures written with the
account masked. The eight files are named here, the seven of b765's pushes and the closing's push-out bank of its (g)
(data/b766_misses.txt (1)); each is untracked (read by `git ls-files` before anything), so no pushed bank is rewritten (N4), and the
fifteen captures of b763 and b764 are never opened. The masks are tools/push_gated.sh's (v1.38.23): the name after github.com/ or
github.com: in a remote's address, and the name before /PLACE-project-set (the trail's pattern), each written <account>. The account's own
name is read from the relay's origin address by the first mask's pattern and used for one count alone, its occurrences in any form and case
before and after; it is never printed or written. Every other byte of a file stands: the replacements are the only change, its line ends
kept as they are.

  python -X utf8 -u tools/b766_mask_captures.py control   a planted capture in a scratch folder masked and read back; writes nothing here
  python -X utf8 -u tools/b766_mask_captures.py dry       the eight read and counted; writes nothing
  python -X utf8 -u tools/b766_mask_captures.py write     the eight written masked, and data/b766_capture_mask.txt
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = '\n'
BANK = os.path.join(D, 'b766_capture_mask.txt')
CAPTURES = ('b765_SIDE-explicit-formula_push-b765-centre_push_out.txt', 'b765_SIDE-explicit-formula_push-b765-planted_push_out.txt',
            'b765_relay_push-b765-preroot_push_out.txt', 'b765_PLACE-papers_push-b765-preroot_push_out.txt',
            'b765_relay_push-b765-record_push_out.txt', 'b765_PLACE-papers_push-b765-record_push_out.txt',
            'b765_PLACE-project-set_push-b765-set_push_out.txt', 'b765_relay_push-b765-closing_push_out.txt')
MASKS = ((re.compile(r'(github\.com[/:])[A-Za-z0-9][A-Za-z0-9-]*'), r'\1<account>'),
         (re.compile(r'[A-Za-z0-9][A-Za-z0-9-]*/PLACE-project-set'), '<account>/PLACE-project-set'))


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')


def account():
    """the account's name from the relay's origin address, by the first mask's pattern; refused where none is read. Never printed."""
    m = re.search(r'github\.com[/:]([A-Za-z0-9][A-Za-z0-9-]*)', git('remote', 'get-url', 'origin').stdout)
    if not m:
        sys.exit('### THE ACCOUNT NOT READ FROM THE RELAY`S ORIGIN -- NOTHING READ, NOTHING WRITTEN')
    return m.group(1)


def mask(text):
    """(masked text, hits of the first mask, hits of the second)."""
    t1, n1 = MASKS[0][0].subn(MASKS[0][1], text)
    t2, n2 = MASKS[1][0].subn(MASKS[1][1], t1)
    return t2, n1, n2


def literal(text, acct):
    return len(re.findall(re.escape(acct), text, re.I))


def sha(b):
    return hashlib.sha256(b.replace(b'\r\n', b'\n')).hexdigest()[:16]


def read_one(path, acct):
    raw = open(path, 'rb').read()
    text = raw.decode('utf-8')
    new, n1, n2 = mask(text)
    return dict(raw=raw, new=new.encode('utf-8'), lines=text.count('\n'), n1=n1, n2=n2, before=literal(text, acct), after=literal(new, acct))


def control():
    """a planted capture (a remote address in each form, the trail's form, a line with no name) in a scratch folder: masked and read back,
    the planted name 0 after, the line with no name and the line count unchanged; a second, unplanted file left byte for byte."""
    planted = 'planted-acct'
    lines = ['push_gated: capture on -> D:/x/b765_relay_push-b765-record_push_out.txt (2026-11-22T00:00:00Z)',
             'To https://github.com/%s/relay.git' % planted, 'To git@github.com:%s/SIDE-explicit-formula.git' % planted,
             'remote:      https://github.com/%s/PLACE-papers/pull/new/push-b765-record' % planted,
             'cloned to %s/PLACE-project-set' % planted, 'push_gated: DONE -- branch push-b765-record pushed alone and read back']
    tmp = tempfile.mkdtemp(prefix='b766mask_')
    try:
        a_, b_ = os.path.join(tmp, 'planted.txt'), os.path.join(tmp, 'clean.txt')
        with open(a_, 'w', encoding='utf-8', newline='\r\n') as fh:
            fh.write(NL.join(lines) + NL)
        with open(b_, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(lines[0] + NL + lines[-1] + NL)
        r = read_one(a_, planted)
        c = read_one(b_, planted)
        out_l = r['new'].decode('utf-8').split('\r\n')
    finally:
        if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b766mask_'):
            shutil.rmtree(tmp, ignore_errors=True)
    rows = [('the planted name before', r['before'], 4), ('after', r['after'], 0), ('first-mask hits', r['n1'], 3), ('second-mask hits', r['n2'], 1),
            ('<account> after', sum(l.count('<account>') for l in out_l), 4), ('the line with no name unchanged', int(out_l[5] == lines[-1]), 1),
            ('the line count', r['lines'], 6), ('the CRLF line ends kept', int(r['new'].count(b'\r\n') == 6), 1),
            ('the unplanted file`s hits', c['n1'] + c['n2'], 0), ('the unplanted file byte for byte', int(c['new'] == c['raw']), 1)]
    L = ['  (control) %s: %d, wanted %d -- %s' % (w, g, x, 'AS WANTED' if g == x else 'NOT AS WANTED') for w, g, x in rows]
    ok = all(g == x for _w, g, x in rows)
    return L + ['### ### **THE MASK`S CONTROL: %d OF %d AS WANTED.**' % (sum(1 for _w, g, x in rows if g == x), len(rows))], ok


def main(argv):
    route = argv[0] if argv else ''
    if route == 'control':
        L, ok = control()
        print(NL.join(L))
        sys.exit(0 if ok else 1)
    if route not in ('dry', 'write'):
        sys.exit(__doc__)
    paths = [os.path.join(D, n) for n in CAPTURES]
    missing = [n for n, p in zip(CAPTURES, paths) if not os.path.isfile(p)]
    tracked = [n for n in CAPTURES if git('ls-files', '--error-unmatch', 'data/' + n).returncode == 0]
    if missing or tracked:
        sys.exit('### REFUSED: missing %s ; tracked %s -- a pushed capture is never rewritten (N4), NOTHING WRITTEN' % (missing, tracked))
    acct = account()
    L0, ok0 = control()
    if not ok0:
        sys.exit(NL.join(L0) + NL + '### THE CONTROL NOT AS WANTED -- NOTHING WRITTEN')
    rows = [(n, read_one(p, acct)) for n, p in zip(CAPTURES, paths)]
    L = ['b766 -- b765`S EIGHT CAPTURES WITH THE ACCOUNT MASKED, (R376)(7) [K23] (%s, tools/b766_mask_captures.py %s)' % (
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), route), '',
         '### each file: its lines; the first mask`s hits (the name after github.com/ or github.com:) and the second`s (the name before',
         '### /PLACE-project-set); the account`s name in any form and case, before and after (read from the relay`s origin, never printed); the',
         '### sha256 of its LF bytes before and after (16 hex). The fifteen captures of b763 and b764 not opened.', '']
    for n, r in rows:
        L.append('  data/%s: lines %d ; hits %d + %d ; the name %d -> %d ; sha256 %s -> %s' % (n, r['lines'], r['n1'], r['n2'], r['before'], r['after'],
                                                                                     sha(r['raw']), sha(r['new'])))
    tot = (sum(r['n1'] for _n, r in rows), sum(r['n2'] for _n, r in rows), sum(r['before'] for _n, r in rows), sum(r['after'] for _n, r in rows))
    L += [''] + L0
    clean = tot[3] == 0
    L.append('### ### **FILES %d ; HITS %d + %d ; THE NAME %d BEFORE, %d AFTER ; %s.**' % (len(rows), tot[0], tot[1], tot[2], tot[3],
                                                                                     'MASKED WHOLE' if clean else 'NOT MASKED WHOLE, NOTHING WRITTEN'))
    print(NL.join(L))
    if route == 'write':
        if not clean:
            sys.exit(1)
        for (n, r), p in zip(rows, paths):
            with open(p + '.tmp', 'wb') as fh:
                fh.write(r['new'])
            os.replace(p + '.tmp', p)
        with open(BANK + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(NL.join(L) + NL)
        os.replace(BANK + '.tmp', BANK)
        back = [literal(open(p, 'rb').read().decode('utf-8'), acct) for p in paths]
        print('  WRITTEN the eight and data/b766_capture_mask.txt ; read back: the name %d in all' % sum(back))
    sys.exit(0 if clean else 1)


if __name__ == '__main__':
    main(sys.argv[1:])
