# -*- coding: utf-8 -*-
"""b667_closing.py -- THE CLOSING RECORD OF b667, UNDER (R277). Carried from b666_closing.py by the Write tool, its act text written for b667;
the sealed tools' hashes compared at the close and printed (OPEN_TRAILS :13307); THE CITATION CHECK, the gate step; THE RECORD LINE (b666 at
its weight); THE DRY RUN, the gate's step as its record prints it; THE PLAN and its amendments (3a)-(3d); THE OBSTRUCTIONS measured; THE
ISOLATION, its route checks, controls, region, band and squares; THE MAP ON THE BALLS; THE LANDING; the prompts and the author's word; the
next act.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept branches at the
### remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and writes data/b667_closing.txt
### from the act's banks. It writes nothing else. The template is b612_closing.py. Every python child runs as `python -X utf8`, no
### environment mapping passed (the ferry: environment variables left as they are).
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
         'SIDE-structural-error-correction', 'SIDE-carrier-spec']
SEC, SEC_BRANCH, SEC_TAG = 'D:/SIDE-structural-error-correction', 'sec-axiom-b623', 'v0.2.2'
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603', 'platt-b626', 'cite-b628', 'nb-b629', 'dedekind-b631']
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']
TAGS = [('SIDE-cosmo', 'v0.3.1'), ('SIDE-explicit-formula', 'v0.30'), ('SIDE-effects', 'v0.1.1'), ('SIDE-carrier-spec', 'v0.4.2'),
        ('SIDE-structural-error-correction', 'v0.2.3'), ('SIDE-lv-conservation', 'v0.13.0'), ('SIDE-global-section', 'v0.3.0')]
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3'))


def run(args):
    if args and args[0] == sys.executable:
        args = [sys.executable, '-X', 'utf8'] + args[1:]
    r = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace')
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
    '    (a) ### **THE NEXT ACT, (R277)(8)**: b668, the re-cut act on SIDE-grh-transfer under (R265)`s form (the tie at count, OPEN_TRAILS',
    '        :14238); then b669 the χ-Li converse, b670 the reading act.',
    '    (b) The kernel item for P1 and P2 (OPEN_TRAILS, placed by this act): SIDE-explicit-formula`s Schema/EpsteinQ0.lean`s decimal literals',
    '        replaced by the certified intervals of relay data/b667_epstein_zeros_certified.txt, P2 restated on the counts -- a later act.',
    '    (c) The precision bank carries this act`s Bessel rung (600 bits, (R277)(3a)) as a dated line beneath relay data/b627_margin_inputs.txt.',
    '    (d) b663`s negative control carries the dated line "ball-certified at b667"; its second caveat falls.',
    '    (e) b628`s full intake bank and the navigator`s export stay local and untracked in relay data/.',
    '    (f) The act root of b667 is relay data/act_roots.txt`s last line.',
    '    (g) Branches left for the next act`s step zero: the push-b667* branches of relay and PLACE-papers; the quarantine branches and the',
    '        kept kernel branches untouched; no kernel branch made by this act.',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
    '    (i) The closing reads each repository`s remote refs once (the standing line at OPEN_TRAILS :12703).',
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


ACT = 'b667'


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
    for tool, out in (('b307_handoff_census.py', 'b667_census_closing.txt'), ('b327_faces_census.py', 'b667_faces_census_closing.txt'),
                      ('b303_pins.py', 'b667_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b667'])
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
    S = jl('b667_scores.json')
    pre, post = rd('b667_checks.txt'), rd('b667_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b667 -- THE CLOSING RECORD. ### **LANE TWO, ACT NINETY-FOUR, THE RESEARCH ACT: b666 AT ITS WEIGHT; THE EVALUATION ROUTE RAISED IN A '
         'PLAN; Q0`S ZEROS BELOW 150 ISOLATED IN BALLS, THE LIST`S COMPLETENESS COUNTED, THE b663 CONTROL RE-RUN ON THE BALLS, UNDER (R277).**',
         '=' * 104]
    sys.path.insert(0, T)
    import b667_worklist as WL
    rec_ = jl('b667_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b667_seal_hashes.json):'] + [
        '      %-26s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step, before the ferry was banked; relay data/b667_citation_check.txt): ' + verdict(
        rd('b667_citation_check.txt'), r'CITES CHECKED \d+ ; OK \d+ ; MISSES \d+'), '']
    RL = jl('b667_record_lines.json').get('lines') or []
    L += ['### THE RECORD LINE ((R277)(1); relay data/b667_record_lines.json): ' + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b667_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b667_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+'), '']
    plan = rd('b667_epstein_plan.txt')
    L += ['### THE PLAN ((R277)(3), raised before any number; relay data/b667_epstein_plan.txt): the route Chowla-Selberg (sections 2, 11); the',
          '    amendments on the author`s word -- (3a) the Bessel rung at 600 bits, (3b) the derivative bound for the enclosure, (3c) R`s right edge',
          '    by the tail bound, (3d) T4 restated for |μ| ≤ 2 -- sections %s' % ', '.join(s for s in ('12', '13', '14', '15', '16') if ('== %s. ' % s) in plan), '']
    L += ['### THE OBSTRUCTIONS MEASURED (relay data/b667_bessel_obstruction.txt, data/b667_ball_obstruction.txt): ' + verdict(
        rd('b667_bessel_obstruction.txt'), r'AT 600 BITS: GRID POINTS \d+ ; ENCLOSED BELOW 2\^-60 AT EVERY TERM \d+ ; NOT \d+'), '']
    c = rd('b667_epstein_counts.txt')
    L += ['### THE ISOLATION ((R277)(3)-(5); relay data/b667_epstein_counts.txt, data/b667_epstein_zeros_certified.txt; the stopped runs banked',
          '    beside, data/b667_certify_run1.txt to run3.txt):']
    for pat in (r'\(3b\) [A-Z][^\n]*', r'\(3d\) [A-Z][^\n]*', r'V1 HOLDS[^\n]*', r'-> V2 [A-Z]+', r'-> V3 [A-Z]+', r'C1 READS AS FIXED[^\n]*',
                r'-> C2 READS AS FIXED', r'N\(R\) = [^\n]*', r'-> C3 READS AS FIXED', r'== B   [^\n]*', r'\(H1\) [^\n]*', r'\(H2\) [^\n]*',
                r'\(FE\) [^\n]*', r'\(H3\) [^\n]*', r'\(H5\) [^\n]*', r'the host`s free memory[^\n]*', r'Bessel factors taken at 600 bits: \d+'):
        L.append('    ' + verdict(c, pat)[:300])
    L += ['']
    L += ['### THE MAP ON THE BALLS ((R277)(5) H4; relay data/b667_epstein_control_balls.txt, data/b667_map_balls_diff.txt):',
          '    ' + verdict(rd('b667_epstein_control_balls.txt'), r'READING Q0 AT qE0: [^\n]*')[:300],
          '    ' + verdict(rd('b667_epstein_control_balls.txt'), r'H4 [A-Z][^\n]*')[:300],
          '    ' + verdict(rd('b667_epstein_control_balls.txt'), r'THE CONTROL (REPRODUCED|NOT REPRODUCED) \([^\n]*'), '']
    LD = jl('b667_landing.json').get('lines') or []
    L += ['### THE LANDING ((R277)(6)): the dated line beneath relay data/b663_epstein_control.txt %s ; ' % (
        'IN PLACE' if 'ball-certified at b667' in rd('b663_epstein_control.txt') else '### ABSENT') + ' ; '.join(
            '%s :%s' % (x.get('file'), x.get('line')) for x in LD) + ' ; ' + verdict(rd('b667_hypotheses.txt'), r'HELD \d OF 5'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b667_author_answers.txt): ' + verdict(rd('b667_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b667_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL:'] + ['    (%s) %s -- %s' % (k, (S.get(k) or ['?', ''])[0], (S.get(k) or ['', ''])[1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b667_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b667_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b667_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b667_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel main moved, no kernel file written, no dispatch ; no lean or lake run on this host ; no worktree made or removed ;',
          '    b628`s local intake bank and the navigator`s export untracked ; no identifier of the author in any outbound request ; the seat`s',
          '    plain requests to github.com (its ls-remote reads and its pushes) the act`s only outbound calls ; the deposit route untouched,',
          '    publish never called ; no shared tool edited ; FINDINGS and OPEN_TRAILS appended ; two dated lines beneath relay data banks (b663`s',
          '    control, b627`s precision bank) ; one line appended to data/act_roots.txt as the act`s last bank step ; b326`s banks unedited ;',
          '    ERRATA, SPIRAL_MAP, README, REGISTRY, the censuses, the pages, the map, the monograph and the companions untouched', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b667_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
