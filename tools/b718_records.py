# -*- coding: utf-8 -*-
"""b718_records.py -- (R328)(9), the records: route `watch` reads lean/QuasiRiemannHypothesis.lean at openai/math 7ef5c0cc5 through gh
(the repository's visibility first; the file located in the commit's tree by name, then printed whole with its blob sha and line count);
writes nothing (the trail entry is written by the Edit tool from this print). No identifier of the author is sent: gh's own token alone.
"""
import base64
import json
import subprocess
import sys

NL = chr(10)
REPO, COMMIT = 'openai/math', '7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def gh(path):
    r = subprocess.run(['gh', 'api', path], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip() else {'_error': (r.stderr or r.stdout).strip()[:300]}


def watch():
    v = gh('repos/%s' % REPO)
    print('### %s : visibility %s ; default branch %s' % (REPO, v.get('visibility'), v.get('default_branch')))
    t = gh('repos/%s/git/trees/%s?recursive=1' % (REPO, COMMIT))
    hits = [x for x in t.get('tree') or [] if 'quasi' in x['path'].lower() or ('riemann' in x['path'].lower() and x['path'].endswith('.lean'))]
    print('### the tree at %s : %d entries, truncated %s ; matching %d' % (COMMIT[:9], len(t.get('tree') or []), t.get('truncated'), len(hits)))
    for x in hits:
        print('  %s %s %s' % (x['type'], x['sha'][:12], x['path']))
    for x in hits:
        if x['type'] == 'blob' and x['path'].endswith('QuasiRiemannHypothesis.lean'):
            b = gh('repos/%s/git/blobs/%s' % (REPO, x['sha']))
            text = base64.b64decode(b.get('content') or '').decode('utf-8', 'replace')
            L = text.replace('\r', '').split(NL)
            print('### %s at %s (blob %s) : %d lines, %d bytes' % (x['path'], COMMIT[:9], x['sha'], len(L), len(text.encode('utf-8'))))
            for i, l in enumerate(L, 1):
                print('  %4d  %s' % (i, l))


if __name__ == '__main__':
    if sys.argv[1:] != ['watch']:
        sys.exit('usage: b718_records.py watch')
    watch()
