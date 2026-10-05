# -*- coding: utf-8 -*-
"""b627_closing.py -- THE CLOSING RECORD OF b627, UNDER (R237).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and
### writes data/b627_closing.txt from the act's banks. It writes nothing else. The template is b612_closing.py.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPOS = ['relay', 'MY-DOwnloads/PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
         'SIDE-effects', 'SIDE-silence-principle', 'SIDE-omega-b', 'SIDE-cosmo', 'SIDE-trivium', 'SIDE-residual-bridge',
         'SIDE-yang-mills-formation', 'SIDE-substrate-cluster', 'SIDE-constants', 'SIDE-simplicity', 'SIDE-bsd-formation-transfer',
         'SIDE-bsd-multiplicity', 'SIDE-t7-topology-cmb', 'SIDE-local-cosmic-interface', 'SIDE-quaternionic-dark-sector', 'SIDE-spinor',
         'SIDE-bijection', 'SIDE-class-coupling', 'SIDE-coupling', 'SIDE-formation-arithmetic', 'SIDE-meta', 'SIDE-orchestrator',
         'SIDE-structural-error-correction']
SEC, SEC_BRANCH, SEC_TAG = 'D:/SIDE-structural-error-correction', 'sec-axiom-b623', 'v0.2.2'
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603', 'platt-b626']
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('H61a', 'H61b', 'H61c', 'H61d'),
              ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5'))


def run(args):
    r = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace',
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def g(repo, *a):
    return run(['git', '-C', repo] + list(a))[1].strip()


def rd(n):
    p = os.path.join(D, n)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def verdict(text, pat):
    m = re.search(pat, text)
    return m.group(0) if m else '### NOT FOUND'


CARRIED = [
    '    (a) ### **THE NEXT ACT, (R237)(6)**: b628 -- the cross-kernel discharge route (b) of W-ORD-VENDOR-FINALMULT (OPEN_TRAILS',
    '        :12970) if the author`s word falls there, else W-ORD-NYMAN-BEURLING-FACE (:12893); the author rules on the closing.',
    '    (b) ### **FOR THE AUTHOR`S RULING**: the sieve`s next version, at which its shape column takes BOUNDED; W-ORD-GATE-FROM-',
    '        ELABORATOR and W-ORD-BINDER-GRAMMAR, priced, waiting on the word.',
    '    (c) ### **FOR THE AUTHOR`S STRIKE**: the seat`s readings (H61c read on the bench`s scope; N3`s rung nodes the three carrying',
    '        rh_upto`s bounded quantifier; BOUNDED`s premise forms; the conventions` check; zeros2 as the named table; N5`s list).',
    '    (d0) The act root of b627 is relay data/act_roots.txt`s last line; every mirror build carries it in MANIFEST.',
    '    (d) Branches left for the next act`s step zero, each merged: PLACE-papers push-b627 and push-b627-root; relay push-b627,',
    '        push-b627-root and push-b627-closing; SIDE-global-section push-b627-gs.',
    '    (e) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
    '    (f) The closing reads each repository`s remote refs once (the standing line at OPEN_TRAILS :12703).',
]
_REMOTE = {}


def next_terminals():
    """### (R237)(4), THE CLOSING FORM: beneath each terminal the next act names, its statement read by git at its pin (the declaration
    ### line through its `:=` or the blank line ending it, at most eight lines, whitespace-joined); a work-order naming no kernel
    ### terminal yet is said so. The routes are b627_worklist's."""
    sys.path.insert(0, T)
    import b627_worklist as WL
    out = []
    for route, terms in WL.NEXT_ROUTES:
        out.append('    %s:' % route)
        if not terms:
            out.append('        names no kernel terminal yet; its statements are the act`s to write, priced at the work-order')
        for name, repo, pin, path, line in terms:
            r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (pin, path)], capture_output=True)
            t = r.stdout.decode('utf-8', 'replace').replace(chr(13), '').split(NL) if r.returncode == 0 else []
            body = []
            for l in t[line - 1:line + 7]:
                if body and not l.strip():
                    break
                body.append(l.split(':=')[0] + (':=' if ':=' in l else ''))
                if ':=' in l:
                    break
            st = ' '.join(' '.join(body).split()) if body else '### NOT READ AT THE PIN'
            out += ['        %s (%s @ %s, %s :%d)' % (name, repo.split('/')[-1], pin, path, line), '            %s' % st]
    return out


def remote_refs(p):
    """### OPEN_TRAILS :12703: one ls-remote per repository for the closing, retried once alone when it fails"""
    if p not in _REMOTE:
        out = g(p, 'ls-remote', 'origin')
        if 'refs/heads/' not in out:
            out = g(p, 'ls-remote', 'origin')
        _REMOTE[p] = dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in out.split(NL) if '\t' in l)
    return _REMOTE[p]


def main():
    for tool, out in (('b307_handoff_census.py', 'b627_census_closing.txt'), ('b327_faces_census.py', 'b627_faces_census_closing.txt'),
                      ('b303_pins.py', 'b627_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b627'])
        b = o.replace(chr(13), '').encode('utf-8')
        p = os.path.join(D, out)
        open(p + '.tmp', 'wb').write(b)
        os.replace(p + '.tmp', p)
    heads = []
    for r in REPOS:
        p = 'D:/' + r
        loc = g(p, 'rev-parse', 'main')
        rem = remote_refs(p).get('refs/heads/main', '')
        heads.append('      %-32s main %s ; remote %s ; %s' % (r.split('/')[-1], loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    K = 'D:/SIDE-explicit-formula'
    for b in KEPT:
        loc = g(K, 'rev-parse', 'refs/heads/' + b)
        rem = remote_refs(K).get('refs/heads/' + b, '')
        heads.append('      %-32s local %s ; remote %s ; %s (kept)' % (b, loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    sb, sm, st = g(SEC, 'rev-parse', 'refs/heads/' + SEC_BRANCH), g(SEC, 'rev-parse', 'main'), g(SEC, 'rev-parse', SEC_TAG + '^{commit}')
    srt = remote_refs(SEC).get('refs/tags/%s^{}' % SEC_TAG, '')
    heads.append('      %-32s local %s ; main %s ; %s peeled %s, at the remote %s ; %s (kept, local)' % (
        SEC_BRANCH, sb[:12], sm[:12], SEC_TAG, st[:12], srt[:12], 'AGREE' if sb and sb == sm == st == srt else '### DIFFER'))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED, NOT WRITTEN BY THIS ACT' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?'))
    S = json.load(io.open(os.path.join(D, 'b627_scores.json'), encoding='utf-8'))
    pre, post = rd('b627_checks.txt'), rd('b627_checks_postpush.txt')
    L = ['=' * 104,
         'b627 -- THE CLOSING RECORD. ### **LANE THREE, ACT FIFTY-FOUR: THE POSITIVITY MARGIN AT HEIGHT FROM THE PRIME SIDE AT THE '
         'LOWEST ZEROS; THE SEAM EQUIVALENCE RULED; THE BOUNDED SHAPE ENTERED; THE CLOSING FORM AMENDED, UNDER (R237).**', '=' * 104]
    L += ['    ' + l for l in rd('b627_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, S[k][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b627_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b627_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b627_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b627_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel touched and no Lean call made ; one CORRESPONDENCE row appended in SIDE-global-section ; no worktree made or '
          'removed ; no current version or keystone edited ; the generator with its test, and this tool`s carried section, each committed '
          'alone in relay ; the bench run twice in the foreground ; one line appended to data/act_roots.txt ; relay, PLACE-papers and '
          'SIDE-global-section pushed once before the root ; '
          'ERRATA, REGISTRY, README and SPIRAL_MAP untouched ; no MANIFEST written and no mirror built', '']
    L += ['### CARRIED FORWARD.'] + CARRIED[:2] + ['    ### THE NEXT ACT`S TERMINALS, EACH STATEMENT AT ITS PIN ((R237)(4)):'] + next_terminals() + CARRIED[2:] + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b627_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-62:]))


if __name__ == '__main__':
    main()
