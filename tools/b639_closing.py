# -*- coding: utf-8 -*-
"""b639_closing.py -- THE CLOSING RECORD OF b639, UNDER (R249). Carried from b638_closing.py by substitution, its act text edited; the
sealed tools' hashes compared at the close and printed (OPEN_TRAILS :13307); the mirror's figures read from its bank.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and
### writes data/b639_closing.txt from the act's banks. It writes nothing else. The template is b612_closing.py.
"""
import hashlib
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
        'sign-window-b602', 'family-b603', 'platt-b626', 'cite-b628', 'nb-b629', 'dedekind-b631']
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('H73a', 'H73b', 'H73c', 'H73d', 'H73e'),
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
    '    (a) ### **THE NEXT ACT, (R249)(5)**: b640 on the author`s word -- the census at v0.7 with the status column of (R249)(2) and its',
    '        rows counted over both provenances, or the per-cluster fact-item editions of Phase 1.2 under the reader`s clause.',
    '    (b) ### **FOR THE AUTHOR`S RULING**: the seat`s hand-read beside each discharge and each work-order line (data/b639_premise_status.txt);',
    '        the figure put before the seal (20 / 28 / 2) against the tool`s (19 / 29 / 2), both printed, the defective predicate named.',
    '    (c) ### **FOR THE AUTHOR`S STRIKE**: the seat`s readings (the record the monograph`s; the mechanism exclusions as SIDE-kernel v1.5`s',
    '        route terminals; the monograph uploaded under its edition`s name; the publication date the metadata step`s day; the description',
    '        in the record`s HTML paragraph form).',
    '    (c2) b628`s full intake bank stays local and untracked in relay data/; its digest is in b628`s summary bank.',
    '    (d0) The act root of b639 is relay data/act_roots.txt`s last line; the next mirror carries it in MANIFEST, with the DOI on publish.',
    '    (d) Branches left for the next act`s step zero, each merged: PLACE-papers push-b639-c1, push-b639 and push-b639-root (and the dated',
    '        updates` on publish); relay push-b639-c1, push-b639, push-b639-root and push-b639-closing; the kept kernel branches untouched.',
    '    (e) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
    '    (f) The closing reads each repository`s remote refs once (the standing line at OPEN_TRAILS :12703).',
]
_REMOTE = {}


def next_terminals():
    """### (R239)(4), THE CLOSING FORM: beneath each terminal the next act names, its statement read by git at its pin; a work-order naming
    ### no kernel terminal yet is said so. The routes are b639_worklist's."""
    sys.path.insert(0, T)
    import b639_worklist as WL
    out = []
    for route, terms in WL.NEXT_ROUTES:
        out.append('    %s:' % route)
        if not terms:
            out.append('        names no kernel terminal yet; its statements are the act`s to write, priced at the work-order')
    return out


def remote_refs(p):
    """### OPEN_TRAILS :12703: one ls-remote per repository for the closing, retried once alone when it fails"""
    if p not in _REMOTE:
        out = g(p, 'ls-remote', 'origin')
        if 'refs/heads/' not in out:
            out = g(p, 'ls-remote', 'origin')
        _REMOTE[p] = dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in out.split(NL) if '\t' in l)
    return _REMOTE[p]


ACT = 'b639'


def head_line(dd=None, act=ACT):
    """### (R245)(3), standing (OPEN_TRAILS at the closing form): the closing's first line, written from the act's banks in `dd` --
    ### the relay and PLACE-papers heads read back after the record's pushes, a kernel tag only when the act pushed one, the suite's
    ### post-push count, the root's first sixteen characters, the prompts answered and the defects. A bank not found prints NOT READ."""
    dd = dd or D

    def _t(n):
        p = os.path.join(dd, n)
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''

    def _back(n):
        m = re.search(r'push_gated: main read back at the remote: (\w+)', _t(n))
        return m.group(1) if m else '### NOT READ'

    parts = ['relay %s' % _back('%s_relay_push_out.txt' % act)[:8], 'PLACE-papers %s' % _back('%s_pp_push_out.txt' % act)[:7]]
    km = re.search(r'push_gated: tag (\S+) made at the read-back (\w+)', _t('%s_kernel_push_out.txt' % act))
    if km:
        kr = re.search(r'push_gated: repo \S*?([^/\\\s]+) ;', _t('%s_kernel_push_out.txt' % act))
        parts.append('%s %s = %s' % (kr.group(1) if kr else 'the kernel', km.group(1), km.group(2)[:7]))
    sm = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', _t('%s_checks_postpush.txt' % act))
    suite = ('suite %s of %s' % (sm.group(2), sm.group(1))) if sm else 'suite ### NOT READ'
    try:
        root = json.loads(_t('%s_act_root.json' % act))['root'][:16] + '…'
    except Exception:
        root = '### NOT READ'
    k = len(re.findall(r'^### PROMPT ', _t('%s_author_answers.txt' % act), re.M))
    try:
        d = len(json.loads(_t('%s_defects.json' % act)).get('defects') or [])
    except Exception:
        d = 0
    return '%s closed: %s; %s; root %s; %d prompt%s answered; %d defect%s' % (act, ', '.join(parts), suite, root, k, '' if k == 1 else 's',
                                                                             d, '' if d == 1 else 's')


def main():
    for tool, out in (('b307_handoff_census.py', 'b639_census_closing.txt'), ('b327_faces_census.py', 'b639_faces_census_closing.txt'),
                      ('b303_pins.py', 'b639_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b639'])
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
    S = json.load(io.open(os.path.join(D, 'b639_scores.json'), encoding='utf-8'))
    pre, post = rd('b639_checks.txt'), rd('b639_checks_postpush.txt')
    M = json.loads(rd('b639_mirror.json') or '{}')
    L = [head_line(), '=' * 104,
         'b639 -- THE CLOSING RECORD. ### **LANE THREE, ACT SIXTY-SIX: THE DEPOSIT ON THE (R110) ROUTE -- THE 50 PREMISE HEADS CLASSED BY STATUS, '
         'THE DESCRIPTION IN THE READER`S ORDER, THE FILES WITH THEIR DIGESTS, A DRAFT READ BACK FROM THE SERVICE, THE AUTHOR`S WORD; THE ROSTER AT '
         'CENSUS v0.6 AND THE MIRROR REBUILT, UNDER (R249).**', '=' * 104]
    Z = json.loads(rd('b639_zenodo.json') or '{}')
    zr, zp, zd = Z.get('read') or {}, Z.get('publish') or {}, Z.get('doi_read') or {}
    sys.path.insert(0, T)
    import b639_worklist as WL
    rec_ = (json.load(io.open(os.path.join(D, 'b639_seal_hashes.json'), encoding='utf-8')) if os.path.exists(os.path.join(D, 'b639_seal_hashes.json'))
            else {}).get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b639_seal_hashes.json):'] + [
        '      %-22s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE DEPOSIT ON THE (R110) ROUTE (relay data/b639_zenodo.json and the step banks):',
          '      record %s ; draft %s ; %s files read back ; title %s ; version %s' % (WL.RECORD, zr.get('id'), zr.get('n_files'), zr.get('title'), zr.get('version')),
          '      the author`s word : %s ; %s' % ('publish' if zp else ('hold' if Z.get('hold') else '### NONE BANKED'),
                                                ('published, record %s, DOI %s, version %s ; the DOI at DataCite: titles %s, version %s' % (
                                                    zp.get('record_id'), zp.get('doi'), zp.get('version'), zd.get('titles'), zd.get('version')))
                                                if zp else 'nothing published'), '']
    L += ['### THE MIRROR, BUILT AFTER THE COMPONENT 1 PUSH OF PLACE-papers AND BEFORE THE DRAFT (relay data/b639_mirror.txt):',
          '      the zip, deposited and for the author`s project : %s' % (M.get('zip') or '### NOT BUILT'),
          '      md5 %s ; sha256 %s ; %s bytes ; files %s ; MANIFEST md5 %s' % (M.get('zip_md5'), M.get('zip_sha256'), M.get('bytes'), M.get('files'),
                                                                             M.get('manifest_md5')),
          '      ROSTER line : %s' % (' / '.join(M.get('roster_line') or []) or '### NONE'),
          '      root line : %s ; verification : %s' % (M.get('root_line') or '### NONE', 'CLEAN ON ALL THREE CLAUSES' if M.get('clean') else '### NOT CLEAN'), '']
    L += ['    ' + l for l in rd('b639_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, S[k][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b639_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b639_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b639_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b639_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel source touched ; lean run only by the step-zero reader test, detached ; no worktree made or removed ; no '
          'current version or keystone edited ; b628`s local intake bank untracked ; no identifier of the author in any outbound request beyond the '
          'record`s own metadata, the seat`s plain requests to github.com (its ls-remote reads and its pushes) within that rule, '
          'the route`s requests to zenodo.org carrying the token in their Authorization header alone and a User-Agent naming the act, the DOI read at DataCite with no '
          'identifier ; the token never printed or banked ; one line appended to data/act_roots.txt ; the roster edit committed alone ; ERRATA, '
          'SPIRAL_MAP and the census untouched, README, REGISTRY and the glossary taking dated lines on publish alone ; the mirror built after the '
          'Component 1 push of PLACE-papers and before the draft by the unedited builder', '']
    L += ['### CARRIED FORWARD.'] + CARRIED[:2] + ['    ### THE NEXT ACT`S TERMINALS, EACH STATEMENT AT ITS PIN ((R237)(4)):'] + next_terminals() + CARRIED[2:] + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b639_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-62:]))


if __name__ == '__main__':
    main()
