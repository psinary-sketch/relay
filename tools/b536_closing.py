# -*- coding: utf-8 -*-
"""b536_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b536_*` and `relay/tools/b536_*` file, the corpus files this
### act writes, the terminal table, the tag object `v0.2`, and the patch and message of every commit of this act (subject
### beginning `b536`) in four repositories, plus any uncommitted change there.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
def read(p):
    return io.open(os.path.join(D, p), encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')
def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()
def git_bytes(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True).stdout


def tokenscan():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        res = dict(set=False)
    else:
        corpus = [os.path.join(PP, f) for f in ('FINDINGS.md', 'ERRATA.md', 'README.md', 'REGISTRY.md', 'OPEN_TRAILS.md')] + [
            os.path.join(SIDE, 'CORRESPONDENCE.md')] + glob.glob(os.path.join(D, 'terminal_table*'))
        files = sorted(set(glob.glob(os.path.join(D, 'b536_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b536_*')) + corpus))
        files = [f for f in files if not f.endswith('b536_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.relpath(f, 'D:\\')] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b536'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        tagb = git_bytes(KER, 'cat-file', 'tag', 'v0.2')
        if t in tagb:
            hits['tag v0.2'] = tagb.count(t)
        push_logs = sorted(os.path.basename(f) for f in files if os.path.basename(f).startswith('b536_') and 'push' in os.path.basename(f))
        warnings = [f for f in push_logs if b'WARNING' in open(os.path.join(D, f), 'rb').read()]
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, tag_scanned=bool(tagb), hits=hits,
                   hits_total=sum(hits.values()), push_logs=push_logs, warnings=warnings)
    io.open(os.path.join(D, 'b536_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b536_scores.json'))
HK = json.loads(read('b536_housekeeping.json'))['final']
CE = json.loads(read('b536_ceiling.json'))
PA = json.loads(read('b536_priorart.json'))
PF = json.loads(read('b536_profile.json'))
AT = json.loads(read('b536_attempts.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
std = sum(1 for v in (PF.get('std3') or {}).values() if v is True)
L = ['=' * 104, 'b536 -- THE CLOSING RECORD. ### **THE SEAM, THE HOUSEKEEPING, THE PRIOR ART, THE UNDERSTANDINGS ENTERED, UNDER (R146).**',
     '=' * 104,
     '    the seam : Seam.lean %d of %d standard three ; attempts %d ; %s' % (std, len(PF.get('std3') or {}), len(AT),
                                                                         lw(read('b536_profile_log.txt'), 'h2_sign_iff_rh :')),
     '    the tag : ' + ' ; '.join(l for l in read('b536_tag.txt').split(NL) if 'v0.2' in l)[:300],
     '    housekeeping : ERRATA heading :%s, line under it :%s ; the two bullets from :%s ; the span convention in the trail'
     % (HK['heading_line'], HK['line_under_heading'], HK['bullets_from']),
     '    prior art : FINDINGS.md:%s ; weil files %s, explicit-formula files %s ; README quotes %d'
     % (PA['heading_line'], PA['weil_count'], PA['ef_count'], len(PA['readme_quotes'])),
     '    the ceiling : README new at %s (old at %s kept) ; REGISTRY new at %s (old at %s kept) ; the trail'
     % (CE['README']['new_line'], CE['README']['old_line'], CE['REGISTRY']['new_line'], CE['REGISTRY']['old_line']),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else
                           'hits %s over %s files, %s commits, the tag and %s push logs ; limb WARNINGs %s'
                           % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'], len(TK['push_logs']), TK['warnings'] or 'NONE')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s'
     % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b536_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE TAG, THE CENSUSES. ### NO MIRROR ZIP -- (R145)(7).',
     '    pre-push : %s' % lw(read('b536_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b536_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'),
             ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula'), ('SIDE-kernel', 'D:/SIDE-kernel')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    censuses : %s / %s' % (lw(read('b536_census_closing.txt'), 'TOTAL MISSING'), lw(read('b536_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b536_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **ON THE AUTHOR`S WORD, (R145)(7)**: the mirror refresh (the author`s export) and the memory refresh.',
      '    (b) ### **THE ZENODO DESCRIPTIONS STILL CARRY (R145)(2)`S CEILING**: not re-edited for (R146)(2)`s, per (R66).',
      '    (c) ### **(S2) REFUTED**: the `weil` hit lines are Weilacher, Kurzweil and one Mordell-Weil -- no Weil criterion',
      '        in Mathlib or Zeta23 at the pins.',
      '=' * 104]
io.open(os.path.join(D, 'b536_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
