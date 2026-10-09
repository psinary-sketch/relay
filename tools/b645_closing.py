# -*- coding: utf-8 -*-
"""b645_closing.py -- THE CLOSING RECORD OF b645, UNDER (R255). Carried from b644_closing.py, its act text written for b645; the sealed tools'
hashes compared at the close and printed (OPEN_TRAILS :13307); the four tables' counts, the monograph's OVERREACHES rows in full for the
author, v6.0's agenda named as sent, the runs beneath the hold, the outsiders' readings and the next act, each read from its bank.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept branches at the
### remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and writes data/b645_closing.txt
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
         'SIDE-structural-error-correction']
SEC, SEC_BRANCH, SEC_TAG = 'D:/SIDE-structural-error-correction', 'sec-axiom-b623', 'v0.2.2'
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603', 'platt-b626', 'cite-b628', 'nb-b629', 'dedekind-b631']
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5'))


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
    '    (a) ### **THE NEXT ACT, (R255)(8) AND THE AUTHOR`S ANSWER**: b646, the seven companions through the intake form; b647, the other',
    '        kernels` docstrings by the generated rule; the two pages last, since they are generated from the kernels.',
    '    (b) ### **SENT TO THE AUTHOR AS A FILE**: relay data/b645_v6_agenda.txt -- the monograph`s OVERREACHES and UNLICENSED rows by chapter,',
    '        each with its re-cut or work-order, v6.0`s agenda, read before any re-cut is ruled.',
    '    (c) ### **FOR THE AUTHOR`S RULING**: test_chain_page_b638.py`s cases (4)-(7) still fail (carried from b643); RestrictedTensorLayer1 and',
    '        test_elab_reader_b634 RUN-BENEATH-HOLD, final (W-ORD-HOLD-FOOTPRINT entered and priced); two terminal-table rows read wrong by its',
    '        matchers -- h2_sign_upto graded DERIVES from a FINDINGS cell saying it is a definition (:6036), and the bare name',
    '        structural_exhaustiveness_proved resolved to ConservationBridge`s file, TheBridgeComplete`s unconditional theorem no row of its own.',
    '    (d) ### **FOR THE AUTHOR`S STRIKE**: the seat`s readings in the trail record`s list; the outsiders` readings (relay',
    '        data/b645_outsider_roster.txt); the monograph`s stated-as rule and its sample rate.',
    '    (e) b628`s full intake bank stays local and untracked in relay data/; its digest is in b628`s summary bank.',
    '    (f) The act root of b645 is relay data/act_roots.txt`s last line; the next mirror carries it in MANIFEST.',
    '    (g) Branches left for the next act`s step zero, each merged: the push-b645* branches of relay and PLACE-papers; the kept kernel',
    '        branches untouched.',
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


ACT = 'b645'


def head_line(dd=None, act=ACT):
    """### (R245)(3), standing: the closing's first line, written from the act's banks in `dd` -- the relay and PLACE-papers heads read back
    ### after the record's pushes, the suite's post-push count, the root's first sixteen characters, the prompts answered and the defects."""
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
    for tool, out in (('b307_handoff_census.py', 'b645_census_closing.txt'), ('b327_faces_census.py', 'b645_faces_census_closing.txt'),
                      ('b303_pins.py', 'b645_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b645'])
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
    K_ = 'D:/SIDE-explicit-formula'
    for b in KEPT:
        loc = g(K_, 'rev-parse', 'refs/heads/' + b)
        rem = remote_refs(K_).get('refs/heads/' + b, '')
        heads.append('      %-32s local %s ; remote %s ; %s (kept)' % (b, loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    sb, sm, st = g(SEC, 'rev-parse', 'refs/heads/' + SEC_BRANCH), g(SEC, 'rev-parse', 'main'), g(SEC, 'rev-parse', SEC_TAG + '^{commit}')
    srt = remote_refs(SEC).get('refs/tags/%s^{}' % SEC_TAG, '')
    heads.append('      %-32s local %s ; main %s ; %s peeled %s, at the remote %s ; %s (kept, local)' % (
        SEC_BRANCH, sb[:12], sm[:12], SEC_TAG, st[:12], srt[:12], 'AGREE' if sb and sb == sm == st == srt else '### DIFFER'))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED, NOT WRITTEN BY THIS ACT' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?'))
    S = jl('b645_scores.json')
    pre, post = rd('b645_checks.txt'), rd('b645_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b645 -- THE CLOSING RECORD. ### **LANE THREE, ACT SEVENTY-TWO: THE REVIEW PASS OPENED -- THE LICENSED-STATEMENT TABLE BUILT AND TESTED; '
         'THE SEAM ROWS, THE LOAD-BEARING MAP, SIDE-EXPLICIT-FORMULA`S DOCSTRINGS AT v0.26 AND THE MONOGRAPH`S CLAIMS EACH TO ONE VERDICT; THE '
         'CENSUS`S CLUSTER, PHASE AND MATURITY COLUMNS DEFINED; NO EDITION RE-CUT; THE DEPOSIT HELD, UNDER (R255).**', '=' * 104]
    sys.path.insert(0, T)
    import b645_worklist as WL
    rec_ = jl('b645_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b645_seal_hashes.json):'] + [
        '      %-24s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    SM, DJ, MJ, CJ = jl('b645_table_seam_map.json'), jl('b645_table_docstrings.json'), jl('b645_table_monograph.json'), jl('b645_census_columns.json')
    fmt = lambda c: ' ; '.join('%s %d' % (k, c.get(k, 0)) for k in ('MATCHES', 'UNDERSTATES', 'OVERREACHES', 'UNLICENSED'))   # noqa: E731
    mc = {}
    for r in SM.get('map') or []:
        mc[r['verdict']] = mc.get(r['verdict'], 0) + 1
    sc_ = {}
    for r in SM.get('seam') or []:
        sc_[r['verdict']] = sc_.get(r['verdict'], 0) + 1
    L += ['### THE PASS`S FINDINGS, THE FOUR TABLES (tools/licensed_table.py; relay data/b645_table_*.txt):',
          '      the seam rows (%d)        %s' % (len(SM.get('seam') or []), fmt(sc_)),
          '      the load-bearing map (%d) %s' % (len(SM.get('map') or []), fmt(mc)),
          '      the docstrings (%d)      %s ; the positive control flagged %s' % (len(DJ.get('rows') or []), fmt(DJ.get('counts') or {}),
                                                                                 bool((DJ.get('control') or {}).get('hand'))),
          '      the monograph (%d)       %s' % (len(MJ.get('rows') or []), fmt(MJ.get('counts') or {})),
          '      the columns: %d rows ; maturity %s ; the rest blank and marked' % (
              len(CJ.get('rows') or []), ', '.join('%s %s' % (r['id'], r['maturity']) for r in CJ.get('rows') or [] if r.get('maturity'))), '']
    L += ['### THE MONOGRAPH`S ROWS READING OVERREACHES, IN FULL, FOR THE AUTHOR ((R255)(4)(d); the UNLICENSED rows beside them in '
          'relay data/b645_v6_agenda.txt, sent as a file):']
    for r in sorted(MJ.get('rows') or [], key=lambda x: x['line']):
        if r['verdict'] == 'OVERREACHES':
            L += ['  :%d (%s) [%s, stated as %s%s] "%s"' % (r['line'], r['chapter'][:48], r['grade'], r['stated_as'],
                                                           (', ' + r['terminal']) if r['terminal'] else '', r['stated']),
                  '      ACTION %s' % r['action']]
    L += ['']
    HP = jl('b645_hold_preseal.json').get('rows') or []
    H0 = jl('b645_hold_retry.json').get('rows') or []
    L += ['### THE HOLD ((R255)(6) AND THE AUTHOR`S ANSWER): AT STEP ZERO %s ; BEFORE THE SEAL, FINAL:' % (
        ', '.join('%s %s' % (r['target'], r['verdict']) for r in H0))] + [
        '      %-26s lows %s MB ; RUN-BENEATH-HOLD, unbuilt, named' % (r['target'], r['lows']) for r in HP if r['verdict'] == 'RUN-BENEATH-HOLD'] + ['']
    L += ['    ' + l for l in rd('b645_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b645_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b645_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b645_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b645_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel source touched ; no edition, page or census re-cut ; every lean run detached under the watchdog with the stop, one module '
          'per call, the free-memory reading before each and the lows printed per run ; no worktree made or removed ; b628`s local intake bank '
          'untracked ; twelve helper readers of this session read the monograph from one brief, writing to the scratchpad alone ; '
          'no identifier of the author in any outbound request, the seat`s plain requests to github.com (its ls-remote reads and its pushes) within that rule ; '
          'no deposit route called and nothing published ; one line appended to data/act_roots.txt as the act`s last bank step ; ERRATA, '
          'SPIRAL_MAP, README, REGISTRY, the census, the pages, the map and the monograph untouched', '']
    OR = jl('b645_outsider_roster.json').get('rows') or []
    L += ['### THE OUTSIDERS ((R255)(7) AND THE AUTHOR`S ANSWER): EACH WORD BY A PRINTED READING (relay data/b645_outsider_roster.txt):'] + [
        '      %-38s %-13s %s' % (r['path'], r['word'], r['why'][:150]) for r in OR] + [
        '      and one local-only private repository, unnamed, STANDS ASIDE (the b590 rule); the author`s word at the closing replaces any reading it strikes', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b645_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
