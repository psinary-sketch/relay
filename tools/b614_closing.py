# -*- coding: utf-8 -*-
"""b614_closing.py -- THE CLOSING RECORD OF b614, UNDER (R224).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and
### writes data/b614_closing.txt from the act's banks. It writes nothing else. The template is b612_closing.py.
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
         'SIDE-yang-mills-formation', 'SIDE-substrate-cluster', 'SIDE-constants']
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603']
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('H48a', 'H48b', 'H48c', 'H48d'),
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
    '    (a) ### **THE NEXT ACT, (R224)(5)**: b615, the synthesis for 2F, priced on the trail record (census R16: ZERO_SIMPLICITY,',
    '        BSD_TRANSFER, BSD_VIA_FORMATION_TRANSFER; 838 lines; BSD_TRANSFER names TECHNE once).',
    '    (b) ### **OWED TO THE NEXT ACT THAT TOUCHES OPEN_TRAILS**: the mirror`s figures, banked in relay data/b614_mirror.txt -- the zip',
    '        D:/MY-DOwnloads/mirror-refresh-2026-10-04.zip, its sha256 and the MANIFEST`s md5, built after the last PLACE-papers push',
    '        (STANDING b537, the author`s answer), CLEAN ON ALL THREE CLAUSES. The author uploads it to the project workspace.',
    '    (c) ### **FOR THE AUTHOR**: the 2D papers` findings on the trail record (OPEN_TRAILS :12675) -- CSC :72`s figures; MA :99`s three',
    '        places; MA :111 against FA :25; PO :17`s sums and :27, :54`s first primes; 12^{11/2} at FA :193 and UF :644; HC :48; YM :103, :118,',
    '        :341; ST :145 against :142; FA :143 at v0.1; ST :228`s image; the roster`s named ten against the diff`s editions, the navigator`s.',
    '    (d) ### **FOR THE AUTHOR`S STRIKE**: the pins read as cited, eight resolving, the tier KC; the era annotations` and rulings` pins',
    '        read as the papers` own text; the two routes` verdicts; UNIFICATION_OF_FORCES synthesised with its DEFUNCT status on the face;',
    '        (N1) scored after the build, REFUTED in letter on its count of syntheses (four named, the navigator`s two), its floor held.',
    '    (e) Branches left for the next act`s step zero, each merged: PLACE-papers push-b614; relay push-b614 and push-b614-closing.',
    '    (f) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
    '    (g) Transient ls-remote failures, each kept and each claim tested directly before a re-run alone: the first scores run read',
    '        every cited pin`s remote as absent (data/b614_scores_attempt1.json); a pre-push suite run failed G-GRADES-IN-RULE and',
    '        G-DOC-TIER-LINE (data/b614_checks_attempt1.txt); two post-push runs failed the pin arms (data/b614_checks_postpush_attempt1.txt,',
    '        _attempt2.txt); the first closing pins run read relay`s remote unresolved (data/b614_pins_closing_attempt1.txt);',
    '        twenty sequential ls-remote calls all answered, so the failures come in the suite`s bursts of calls --',
    '        the next suite resolves each pin once per run. The append guard refused the first trail record (the stem twice in one',
    '        item), writing nothing; OPEN_TRAILS read at its banked length; the item rephrased and appended.',
]


def main():
    for tool, out in (('b307_handoff_census.py', 'b614_census_closing.txt'), ('b327_faces_census.py', 'b614_faces_census_closing.txt'),
                      ('b303_pins.py', 'b614_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b614'])
        b = o.replace(chr(13), '').encode('utf-8')
        p = os.path.join(D, out)
        open(p + '.tmp', 'wb').write(b)
        os.replace(p + '.tmp', p)
    heads = []
    for r in REPOS:
        p = 'D:/' + r
        loc = g(p, 'rev-parse', 'main')
        rem = g(p, 'ls-remote', 'origin', 'refs/heads/main').split('\t')[0]
        heads.append('      %-32s main %s ; remote %s ; %s' % (r.split('/')[-1], loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    K = 'D:/SIDE-explicit-formula'
    for b in KEPT:
        loc = g(K, 'rev-parse', 'refs/heads/' + b)
        rem = g(K, 'ls-remote', 'origin', 'refs/heads/' + b).split('\t')[0]
        heads.append('      %-32s local %s ; remote %s ; %s (kept)' % (b, loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED, NOT WRITTEN BY THIS ACT' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?'))
    S = json.load(io.open(os.path.join(D, 'b614_scores.json'), encoding='utf-8'))
    pre, post = rd('b614_checks.txt'), rd('b614_checks_postpush.txt')
    L = ['=' * 104,
         'b614 -- THE CLOSING RECORD. ### **LANE THREE, ACT FORTY-ONE: THE SYNTHESIS FOR CLUSTER 2D -- ONE DOCUMENT FROM THE CLUSTER`S '
         'EIGHT PAPERS, EVERY CLAIM GRADED, THE ROUTES READ; THE 2B FINDINGS ENTERED; THE MIRROR AFTER THE LAST PUSH, UNDER (R224).**', '=' * 104]
    L += ['    ' + l for l in rd('b614_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, S[k][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b614_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b614_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b614_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b614_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel written, tagged or branched ; no Lean call ; no worktree made or removed ; the eight papers, the 2B papers, the census and REGISTRY '
          'unedited ; the synthesis written in the cluster`s folder ; ERRATA not written ; the roster`s rows committed alone ; the mirror built after '
          'the last PLACE-papers push, nothing written to PLACE-papers after it', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b614_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-62:]))


if __name__ == '__main__':
    main()
