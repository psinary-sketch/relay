# -*- coding: utf-8 -*-
"""b765 under (R375)(6)(d), the author's word of 2026-11-21 (Route A on W-ORD-H2-PI1; data/b765_author_words_preseal.txt :2-:16):
THE TWO FETCHES, AND NO OTHER. The word names two addresses and orders the seat to fetch these and no other, the one exception to (R375)(12)
and N1 on fetches: (i) arXiv 2311.09464, its text (the PDF at arxiv.org/pdf/2311.09464); (ii) the message at
cs.nyu.edu/pipermail/fom/2017-January/020249.html. One plain GET each, the User-Agent "Mozilla/5.0 (literature reader)" and no other
header naming anyone, no cookie, no retry; each text written into its own new, empty folder under the root given as the argument (the act's
local bank, untracked; no path of it is written by this tool into any tracked file). Prints, for each: the address, the final address after
redirects, the HTTP status, the content type, the size in bytes and the sha256. An address refused prints its status and writes nothing.

Route: `fetch <root>`, refused unless this file is committed and unchanged at the relay's HEAD, and refused where either folder exists.
Route: `again <name> <root>`: the same address of that name requested once more, alone, into its own new folder <name>_again -- the test
of whether a refusal is transient (b765's first run, 12:52:43Z: the arXiv text reached, HTTP 200; the FOM message HTTP 404). The same
address and no other; once."""
import datetime, hashlib, io, os, subprocess, sys, urllib.error, urllib.request

R = 'D:/relay'
ME = 'tools/b765_pi01_fetch.py'
ADDRESSES = (('arxiv', 'https://arxiv.org/pdf/2311.09464', 'pdf'),
             ('fom', 'https://cs.nyu.edu/pipermail/fom/2017-January/020249.html', 'html'))
UA = 'Mozilla/5.0 (literature reader)'


def git(*a):
    r = subprocess.run(['git', '-C', R] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout.strip() if r.returncode == 0 else ''


def self_commit():
    if git('hash-object', ME) != git('rev-parse', 'HEAD:' + ME) or git('status', '--porcelain', '--', ME):
        sys.exit('### %s differs from its blob at HEAD or is not committed -- nothing fetched' % ME)
    return git('rev-parse', '--short=8', 'HEAD')


def main():
    a = sys.argv[1:]
    if not ((len(a) == 2 and a[0] == 'fetch') or (len(a) == 3 and a[0] == 'again' and a[1] in [x[0] for x in ADDRESSES])):
        sys.exit('### usage: b765_pi01_fetch.py fetch <root> | again <arxiv|fom> <root>')
    root = os.path.abspath(a[-1])
    head = self_commit()
    todo = ADDRESSES if a[0] == 'fetch' else tuple((n + '_again', u, e) for n, u, e in ADDRESSES if n == a[1])
    for name, _, _ in todo:
        if os.path.exists(os.path.join(root, name)):
            sys.exit('### the folder %s exists under the root -- nothing fetched (each text into its own new, empty folder)' % name)
    print('### b765 (R375)(6)(d): %s, the tool committed at relay %s ; the User-Agent %r' % (
        'the two fetches' if a[0] == 'fetch' else 'the address %s once more, alone' % a[1], head, UA))
    for name, url, ext in todo:
        at = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                body = r.read()
                status, final, ctype = r.status, r.geturl(), r.headers.get('Content-Type', '')
        except urllib.error.HTTPError as e:
            print('  %s %s: HTTP %d %s at %s -- NOT REACHED, nothing written' % (name, url, e.code, e.reason, at))
            continue
        except Exception as e:   # noqa: BLE001
            print('  %s %s: %s at %s -- NOT REACHED, nothing written' % (name, url, type(e).__name__, at))
            continue
        d = os.path.join(root, name)
        os.makedirs(d)
        p = os.path.join(d, '%s.%s' % (name, ext))
        with io.open(p, 'wb') as f:
            f.write(body)
        print('  %s %s: at %s ; final %s ; HTTP %d ; %s ; %d bytes ; sha256 %s ; written into its own new folder' % (
            name, url, at, final, status, ctype, len(body), hashlib.sha256(body).hexdigest()))


if __name__ == '__main__':
    main()
