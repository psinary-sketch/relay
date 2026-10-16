# -*- coding: utf-8 -*-
"""b671_closing.py -- THE CLOSING RECORD OF b671, UNDER (R281). Carried from b670_closing.py by the Write tool, its act text written for b671;
the sealed tools' hashes compared at the close and printed (OPEN_TRAILS :13307); THE CITATION CHECK, the gate step, and the mid-act checks of
(R278)(4); THE RECORD LINES (b670 at its weight, the sequence line, the census items, the landing, the Bessel lines); THE DRY RUN, the gate's
step as its record prints it; THE PLAN; THE NARROWING, its four runs and the bank step; THE MAP, its one run on the narrowed balls and the
tie diagnostic; THE HYPOTHESES as the landing scores them; the prompts and the author's word; the next acts.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept branches at the
### remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and writes data/b671_closing.txt
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
        ('SIDE-global-section', 'v0.3.0')]
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3'))
HYP_KEYS = ('H1', 'H2', 'H3', 'H4')


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
    '    (a) ### **THE NEXT ACTS, (R281)(10)**: b672 the Correspondence generator in the re-cut slot, its ruling then; b673 V4 and V5 on',
    '        chi-li-b669. `W-ORD-MAP-ANGLE-FORM` (OPEN_TRAILS :14398) stands before the next narrowing act.',
    '    (b) `W-ORD-EPSTEIN-BALL-WIDTH` open (OPEN_TRAILS :14396), and the control half of `W-ORD-EPSTEIN-CERTIFY` with it: hQtie at Q0 18 of 41',
    '        on the 10^-24 balls, the 23 failed controls INSTRUMENT; its figure from the amplification about 10^-31, the linear estimate about',
    '        1.5 x 10^-40 beside it; trigger after `W-ORD-MAP-ANGLE-FORM`, the width re-read from the angle form.',
    '    (c) The kernel item for P1 and P2 re-dated with the narrowed balls as its data (OPEN_TRAILS :14406); a later act.',
    '    (d) `W-ORD-BESSEL-BOUND-TIGHTEN` (OPEN_TRAILS :14388) with the bar as its second object (:14408) and its measured cost above',
    '        height 100 (:14410).',
    '    (e) The converse at χ open on SIDE-explicit-formula`s branch chi-li-b669 (b804bf2), kept: V4 and V5 at b673.',
    '    (f) b628`s full intake bank, the navigator`s export and run 2`s uncompressed points file (data/b671_narrow_run2_points.jsonl,',
    '        88,175,649 bytes) stay local and untracked in relay data/; the points file`s .gz is committed with its hashes in',
    '        data/b671_large_banks.txt.',
    '    (g) The act root of b671 is relay data/act_roots.txt`s last line, taken without the binary bank data/b671_narrow_run2_points.jsonl.gz',
    '        (19 CR LF pairs), the chain reaching it through the LF hashes bank data/b671_large_banks.txt (`W-ORD-ROOT-BINARY-BANK`).',
    '    (h) Branches left for the next act`s step zero: the push-b671* branches of relay and PLACE-papers, deleted when the next ferry`s',
    '        list carries them (rules row 4); chi-li-b669 kept; the quarantine branches and the kept kernel branches untouched.',
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


ACT = 'b671'


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
    for tool, out in (('b307_handoff_census.py', 'b671_census_closing.txt'), ('b327_faces_census.py', 'b671_faces_census_closing.txt'),
                      ('b303_pins.py', 'b671_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b671'])
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
    S = jl('b671_scores.json')
    H = jl('b671_hypotheses.json')
    pre, post = rd('b671_checks.txt'), rd('b671_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b671 -- THE CLOSING RECORD. ### **LANE TWO, ACT NINETY-EIGHT, THE RESEARCH ACT: b670 AT ITS WEIGHT; THE SEQUENCE LINE ENTERED; Q0`S '
         'POINTS NARROWED TO 10^-24; THE CONTROLS; THE b663 CONTROL ON THE NARROWED BALLS, H3 REFUTED; NO KERNEL BYTE, UNDER (R281).**',
         '=' * 104]
    sys.path.insert(0, T)
    import b671_worklist as WL
    rec_ = jl('b671_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b671_seal_hashes.json):'] + [
        '      %-26s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    cc = rd('b671_citation_check.txt')
    L += ['### THE CITATION CHECK (the gate step, before the ferry was banked; relay data/b671_citation_check.txt): ' + verdict(
        cc, r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+') + ' ; the mid-act checks ((R278)(4)): ' + '; '.join(
        re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', cc)), '']
    RL = []
    for b_ in ('b671_record_lines.json', 'b671_landing.json', 'b671_bessel_lines.json'):
        RL += jl(b_).get('lines') or []
    L += ['### THE RECORD LINES ((R281)(1), (2), (8) and (7), the Bessel lines; relay data/b671_record_lines.json, data/b671_landing.json, '
          'data/b671_bessel_lines.json): ' + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b671_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b671_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+'), '']
    L += ['### THE PLAN ((R281)(3)-(5); relay data/b671_narrow_plan.txt): ' + verdict(rd('b671_narrow_plan.txt'), r'w = 1e-24: two decimal orders below [^,]*'), '']
    L += ['### THE NARROWING ((R281)(4); relay data/b671_narrow_log.txt, data/b671_epstein_zeros_narrowed.json.gz and its hashes): '
          + verdict(rd('b671_narrow_log.txt'), r'POINTS \d+ ; ON NARROWED[^*]*'),
          '    run 1 ' + verdict(rd('b671_narrow_run1.txt'), r'RUN 1 : [^*]*'),
          '    run 2 ' + verdict(rd('b671_narrow_run2.txt'), r'RUN 2 : [^*]*'),
          '    run 3 ' + verdict(rd('b671_narrow_run3.txt'), r'RUN 3 : [^*]*'), '']
    mj = jl('b671_map_reading.json')
    L += ['### THE MAP ((R281)(6) H3; relay data/b671_epstein_control_narrowed.txt, data/b671_map_reading.json, data/b671_tie_diagnostic.txt): '
          'the control %s (j0 %s) ; at Q0 hQtie %s, %s ; the tie diagnostic %s' % (
              'reproduced' if mj.get('control_reproduced') else '### NOT REPRODUCED', mj.get('control_j0'), mj.get('hqtie_controls'),
              mj.get('reading'), ' / '.join(mj.get('tie_words') or ['### NOT READ'])), '']
    L += ['### THE HYPOTHESES ((R281)(6); relay data/b671_landing.txt, data/b671_hypotheses.json): ' + ' ; '.join(
        '%s %s' % (k, (H.get(k) or ['?'])[0]) for k in HYP_KEYS), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b671_author_answers.txt): ' + verdict(rd('b671_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b671_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL:'] + ['    (%s) %s -- %s' % (k, (S.get(k) or ['?', ''])[0], (S.get(k) or ['', ''])[1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b671_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b671_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b671_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b671_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel main moved, no kernel file written, no dispatch, no merge, no tag ; no lean or lake run on this host ; no worktree made',
          '    or removed ; b628`s local intake bank, the navigator`s export and run 2`s uncompressed points file untracked ;',
          '    no identifier of the author in any outbound request ; no secret added ;',
          '    the seat`s plain requests to github.com (its ls-remote reads and its pushes) the act`s only outbound calls ; the deposit route',
          '    untouched, publish never called ; no shared tool edited ; FINDINGS and OPEN_TRAILS appended ; data/b663_epstein_control.txt and',
          '    data/b670_methods.txt each gaining one dated line ; one line appended to data/act_roots.txt as the act`s last bank step ; ERRATA,',
          '    SPIRAL_MAP, README, REGISTRY, the censuses, the pages, the map, the monograph and the companions untouched ; b667`s banks',
          '    unedited ; nothing of TECHNE or any patent written', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b671_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
