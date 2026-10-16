# -*- coding: utf-8 -*-
"""b672_closing.py -- THE CLOSING RECORD OF b672, UNDER (R282). Carried from b671_closing.py by the Write tool, its act text written for b672;
the sealed tools' hashes compared at the close and printed (OPEN_TRAILS :13307); THE CITATION CHECK, the gate step, and the mid-act checks of
(R278)(4); THE RECORD LINES (b671 at its weight, the rules, the ledger split, the run's orders); THE DRY RUN, the gate's step as its record
prints it; THE GENERATOR, its planted cases and its commits; THE RUN, the diff bank's figures; READING (ii) after the run, both figures; THE
HYPOTHESES; THE MIRROR; the prompts and the author's word; the next acts.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept branches at the
### remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and writes data/b672_closing.txt
### from the act's banks. It writes nothing else. The template is b612_closing.py.
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
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-grh-transfer']
SEC, SEC_BRANCH, SEC_TAG = 'D:/SIDE-structural-error-correction', 'sec-axiom-b623', 'v0.2.2'
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603', 'platt-b626', 'cite-b628', 'nb-b629', 'dedekind-b631']
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']
LOCAL = [('SIDE-explicit-formula', 'chi-li-b669', 'the converse, open at V4 and V5, kept unmerged (N1)')]
TAGS = [('SIDE-explicit-formula', 'v0.31'), ('SIDE-grh-transfer', 'v0.5.1'), ('SIDE-cosmo', 'v0.3.1'), ('SIDE-effects', 'v0.1.1'),
        ('SIDE-carrier-spec', 'v0.4.2'), ('SIDE-structural-error-correction', 'v0.2.3'), ('SIDE-lv-conservation', 'v0.13.0'),
        ('SIDE-global-section', 'v0.3.0'), ('SIDE-kernel', 'v1.8')]
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3'))
HYP_KEYS = ('H1', 'H2', 'H3', 'H4', 'H5')


def run(args):
    r = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace',
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def g(repo, *a):
    return run(['git', '-C', repo] + list(a))[1].strip()


def rd(n):
    p = os.path.join(D, n)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def jl(n):
    try:
        return json.load(io.open(os.path.join(D, n), encoding='utf-8'))
    except Exception:
        return {}


def verdict(text, pat):
    m = re.search(pat, text)
    return m.group(0) if m else '### NOT FOUND'


CARRIED = [
    '    (a) ### **THE NEXT ACTS, (R282)(10)**: b673 V4 and V5 on chi-li-b669; b674 the re-cut act between SIDE-window and SIDE-trivium by',
    '        the tie rule.',
    '    (b) `W-ORD-ONE-COPY` open, its trigger re-written in full (OPEN_TRAILS :14450): REGISTRY`s file column read for every keystone with',
    '        two copies; every standing reader`s path a bank read; REGISTRY re-pointed where the author rules; then the moves.',
    '    (c) The run`s orders open: `W-ORD-TABLE-SHAPE` (:14442), `W-ORD-GRADE-MOVED` (:14444), `W-ORD-PRINT-TARGETS` (:14446),',
    '        `W-ORD-ABSENT-DECLARATIONS` (:14448), `W-ORD-PROSE-PINS` (:14452); the kernels without a print bank as runner items (:14440).',
    '    (d) The ledger split, archive-3, at the b680 reading act (OPEN_TRAILS :14438); b680`s reading (ii) reads the stable anchors of',
    '        relay data/b672_roster_read.json and prints both figures again.',
    '    (e) The converse at χ open on SIDE-explicit-formula`s branch chi-li-b669 (b804bf2), kept: V4 and V5 at b673.',
    '    (f) b628`s full intake bank, the navigator`s export and b671`s uncompressed points file stay local and untracked in relay data/.',
    '    (g) The act root of b672 is relay data/act_roots.txt`s last line; the mirror export of this act carries it in MANIFEST.',
    '    (h) Branches left for the next act`s step zero: the push-b672* branches of relay and PLACE-papers, deleted when the next ferry`s',
    '        list carries them; chi-li-b669 kept; the quarantine branches and the kept kernel branches untouched.',
    '    (i) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
    '    (j) The closing reads each repository`s remote refs once (the standing line at OPEN_TRAILS :12703).',
]
_REMOTE = {}


def remote_refs(p):
    """### OPEN_TRAILS :12703: one ls-remote per repository for the closing, retried once alone when it fails"""
    if p not in _REMOTE:
        out = g(p, 'ls-remote', 'origin')
        if 'refs/heads/' not in out:
            out = g(p, 'ls-remote', 'origin')
        _REMOTE[p] = dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in out.split(NL) if '\t' in l)
    return _REMOTE[p]


ACT = 'b672'


def head_line(dd=None, act=ACT):
    """### (R245)(3), standing: the closing's first line, written from the act's banks."""
    dd = dd or D

    def _t(n):
        p = os.path.join(dd, n)
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''

    def _back(n):
        m = re.search(r'push_gated: main read back at the remote: (\w+)', _t(n))
        return m.group(1) if m else '### NOT READ'

    parts = ['relay %s' % _back('%s_relay_push_out.txt' % act)[:8], 'PLACE-papers %s' % _back('%s_pp_push_out.txt' % act)[:7]]
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
    for tool, out in (('b307_handoff_census.py', 'b672_census_closing.txt'), ('b327_faces_census.py', 'b672_faces_census_closing.txt'),
                      ('b303_pins.py', 'b672_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b672'])
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
    for k, t in TAGS:
        p = 'D:/' + k
        loc = g(p, 'rev-parse', t + '^{commit}')
        rem = remote_refs(p).get('refs/tags/%s^{}' % t, '')
        heads.append('      %-32s %s peeled %s ; at the remote %s ; main %s ; %s' % (k, t, loc[:12], rem[:12], g(p, 'rev-parse', 'main')[:12],
                                                                                  'AGREE' if loc and loc == rem else '### DIFFER'))
    for k in QUARANTINE:
        p, b = 'D:/' + k, 'sorry-quarantine-' + k
        loc = g(p, 'rev-parse', 'refs/heads/' + b)
        rem = remote_refs(p).get('refs/heads/' + b, '')
        heads.append('      %-32s local %s ; remote %s ; %s (the quarantine and its legacy map)' % (b[:32], loc[:12], rem[:12],
                                                                                                   'AGREE' if loc and loc == rem else '### DIFFER'))
    for k, b, what in LOCAL:
        loc = g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b)
        merged = b in g('D:/' + k, 'branch', '--merged', 'main', '--list', b)
        heads.append('      %-34s %-21s local %s ; at the remote %s ; merged into main %s (%s)' % (
            b[:34], k[:21], loc[:12] or 'none', (remote_refs('D:/' + k).get('refs/heads/' + b) or 'no')[:12], merged, what))
    K_ = 'D:/SIDE-explicit-formula'
    for b in KEPT:
        loc = g(K_, 'rev-parse', 'refs/heads/' + b)
        rem = remote_refs(K_).get('refs/heads/' + b, '')
        heads.append('      %-32s local %s ; remote %s ; %s (kept)' % (b, loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    sb, sm, st = g(SEC, 'rev-parse', 'refs/heads/' + SEC_BRANCH), g(SEC, 'rev-parse', 'main'), g(SEC, 'rev-parse', SEC_TAG + '^{commit}')
    srt = remote_refs(SEC).get('refs/tags/%s^{}' % SEC_TAG, '')
    heads.append('      %-32s local %s ; %s peeled %s, at the remote %s ; main %s (unmoved by this act) ; %s (kept, local)' % (
        SEC_BRANCH, sb[:12], SEC_TAG, st[:12], srt[:12], sm[:12], 'AGREE' if sb and sb == st == srt else '### DIFFER'))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED, NOT WRITTEN BY THIS ACT' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?'))
    S = jl('b672_scores.json')
    H = jl('b672_hypotheses.json')
    pre, post = rd('b672_checks.txt'), rd('b672_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b672 -- THE CLOSING RECORD. ### **LANE THREE, ACT NINETY-NINE, THE TOOLING ACT: b671 AT ITS WEIGHT; THREE RULES; THE CORRESPONDENCE '
         'GENERATOR AND ITS PLANTED CASES; THE ROSTER`S TABLES REGENERATED; THE COPY OF RECORD AS REGISTRY NAMES IT, NOTHING MOVED; NO KERNEL '
         'BYTE, UNDER (R282).**', '=' * 104]
    sys.path.insert(0, T)
    import b672_worklist as WL
    rec_ = jl('b672_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b672_seal_hashes.json):'] + [
        '      %-26s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    cc = rd('b672_citation_check.txt')
    L += ['### THE CITATION CHECK (the gate step, before the ferry was banked; relay data/b672_citation_check.txt): ' + verdict(
        cc, r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+') + ' ; the mid-act checks ((R278)(4)): ' + '; '.join(
        re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', cc)), '']
    RL = []
    for b_ in ('b672_record_lines.json', 'b672_record_lines_c3.json', 'b672_record_lines_prosepins.json'):
        RL += jl(b_).get('lines') or []
    L += ['### THE RECORD LINES ((R282)(1), (2), (7) and the run`s orders; relay data/b672_record_lines.json, data/b672_record_lines_c3.json, '
          'data/b672_record_lines_prosepins.json): ' + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b672_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b672_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+'), '']
    L += ['### THE GENERATOR ((R282)(4); relay tools/correspondence_gen.py, tools/test_correspondence_gen.py, data/b672_gen_test.txt): '
          + verdict(rd('b672_gen_test.txt'), r'PLANTED CASES \d+ ; AS WANTED \d+ ; [A-Z]+') + ' ; committed alone at ' + ', '.join(WL.GEN_COMMITS), '']
    L += ['### THE RUN ((R282)(4); relay data/b672_correspondence_diff.txt): ' + verdict(rd('b672_correspondence_diff.txt'), r'TABLES \d+ ; SHAPED[^*]*'),
          '    the second pass (H1; relay data/b672_gen_rerun.txt): ' + verdict(rd('b672_gen_rerun.txt'), r'THE SECOND PASS CHANGES[^*]*'),
          '    the rows (H3; relay data/b672_rows_kept.txt): ' + verdict(rd('b672_rows_kept.txt'), r'H3: [^*]*'), '']
    L += ['### READING (ii) AFTER THE RUN ((R282)(6) H2; relay data/b672_correspondence_after.txt): ' + verdict(
        rd('b672_correspondence_after.txt'), r'ROWS WITH A COMMIT \d+ \(b670: 100\)[^*]*'),
          '    ' + verdict(rd('b672_correspondence_after.txt'), r'H2, OVER THE SHAPED TABLES, BY b670`S METHOD:[^*]*'),
          '    ' + verdict(rd('b672_correspondence_after.txt'), r'b670`S TABLES: ROWS WITH A COMMIT[^*]*'), '']
    L += ['### THE HYPOTHESES ((R282)(6); relay data/b672_hypotheses.txt): ' + ' ; '.join(
        '%s %s' % (k, (H.get(k) or ['?'])[0]) for k in HYP_KEYS), '']
    mj = jl('b672_mirror.json')
    L += ['### THE MIRROR-REFRESH EXPORT ((R282)(8); relay data/b672_mirror.txt), BUILT AFTER THE LAST PLACE-papers PUSH, for the author`s Project:',
          '    %s ; %s bytes ; sha256 %s ; MANIFEST md5 %s ; entries %s ; %s ; the verification %s ; moves in MANIFEST: none (nothing moved)' % (
              mj.get('zip', '### NOT BUILT'), mj.get('bytes'), (mj.get('zip_sha256') or '')[:16], mj.get('manifest_md5'), mj.get('entries'),
              mj.get('root_line') or '### NO ROOT LINE', 'CLEAN ON ALL THREE CLAUSES' if mj.get('clean') else '### NOT CLEAN'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b672_author_answers.txt): ' + verdict(rd('b672_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b672_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL:'] + ['    (%s) %s -- %s' % (k, (S.get(k) or ['?', ''])[0], (S.get(k) or ['', ''])[1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S, THE NAVIGATOR`S AND b670`S.'] + rd('b672_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b672_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b672_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b672_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel main moved, no kernel file written, no dispatch, no merge, no tag ; no lean or lake run on this host ; no worktree made',
          '    or removed ; nothing moved and no file deleted ; b628`s local intake bank, the navigator`s export and b671`s uncompressed points',
          '    file untracked ; no identifier of the author in any outbound request ; no secret added ;',
          '    the seat`s plain requests to github.com (its ls-remote reads, the generator`s one per kernel repository, and its pushes) the act`s',
          '    only outbound calls ; the deposit route untouched, publish never called ; no shared tool edited ; FINDINGS and OPEN_TRAILS',
          '    appended ; the roster`s Correspondence tables regenerated in 13 files and one partner, b651`s line carried to SIMPLICITY`s',
          '    v1.1.3 ; data/b670_state.txt gaining one dated line ; one line appended to data/act_roots.txt as the act`s last bank step ;',
          '    ERRATA, SPIRAL_MAP, README, REGISTRY, the censuses, the pages and the companions untouched ; nothing of TECHNE or any patent',
          '    written', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b672_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
