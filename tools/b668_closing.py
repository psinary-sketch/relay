# -*- coding: utf-8 -*-
"""b668_closing.py -- THE CLOSING RECORD OF b668, UNDER (R278). Carried from b666_closing.py (the re-cut act before it) and b667_closing.py by
the Write tool, its act text written for b668; the sealed tools' hashes compared at the close and printed (OPEN_TRAILS :13307); THE CITATION
CHECK, the gate step, and the mid-act checks of (R278)(4); THE RECORD LINES (b667 at its weight, the plan form, the mid-act check, the research
order) and the two items of the author's word on the cut; THE DRY RUN, the gate's step as its record prints it; THE GRADES of SIDE-grh-transfer;
THE CUT; THE RUNNER, its run read back; THE MERGE on its gate reading; THE AXIOM CLAIM before and after; THE MIRROR export, its MANIFEST md5 and
last commit; the prompts and the author's word; the next act.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept branches at the
### remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and writes data/b668_closing.txt
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
LOCAL = [('SIDE-grh-transfer', 'docstrings-cut-SIDE-grh-transfer', 'the cut, merged on the runner`s gate reading'),
         ('SIDE-grh-transfer', 'push-b668-merge', 'the merge push'),
         ('SIDE-grh-transfer', 'push-b668-workflow', 'the workflow push')]
TAGS = [('SIDE-grh-transfer', 'v0.5.1'), ('SIDE-cosmo', 'v0.3.1'), ('SIDE-explicit-formula', 'v0.30'), ('SIDE-effects', 'v0.1.1'),
        ('SIDE-carrier-spec', 'v0.4.2'), ('SIDE-structural-error-correction', 'v0.2.3'), ('SIDE-lv-conservation', 'v0.13.0'),
        ('SIDE-global-section', 'v0.3.0')]
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3'))


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
    '    (a) ### **THE NEXT ACT, (R278)(8)**: b669, the χ-Li converse, its ruling then; then b670 the reading act (the two relative-entropy',
    '        questions and the EXTERNAL-ZFR-7/8 line, relay data/b668_b670_items.txt), b671 W-ORD-EPSTEIN-BALL-WIDTH, E2 after ((R278)(5)).',
    '    (b) SIDE-grh-transfer`s relay print bank: data/b668_prints_SIDE-grh-transfer.txt (53 declarations; the 21 of relay',
    '        data/b555_probe_g2.txt equal to their banked prints, the rest at the standard three or none), the reference from here.',
    '    (c) The census item (OPEN_TRAILS, b668`s items bank): 858cbf6, one commit past v0.5.0 untagged, read from its diff as a commit',
    '        addressed to SIDE-frobenius that landed in SIDE-grh-transfer (no .lean file); this act`s tag v0.5.1.',
    '    (d) The cell-refresh item (OPEN_TRAILS, b668`s items bank): the six ACTION cells write chi, chibar and sigma in ASCII beside the',
    '        files` symbols; no cell edited at b668.',
    '    (e) G-MERGES-ON-GATE fails at the close, declared on the face with defect (c): the merged tree is the built tree plus the workflow',
    '        file alone (no .lean byte differs); test_chain_page_b638.py (4)-(7) the standing test failure b666 and b667 carried.',
    '    (f) b628`s full intake bank and the navigator`s export stay local and untracked in relay data/.',
    '    (g) The act root of b668 is relay data/act_roots.txt`s last line; the mirror export of this act carries it in MANIFEST.',
    '    (h) Branches left for the next act`s step zero: the push-b668* branches of relay and PLACE-papers; push-b668-workflow and',
    '        push-b668-merge in SIDE-grh-transfer; docstrings-cut-SIDE-grh-transfer at the remote and local, merged, deleted in the house form',
    '        after --merged lists it, the remote delete alone in its command and turn; the quarantine branches and the kept kernel branches',
    '        untouched.',
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


ACT = 'b668'


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
    for tool, out in (('b307_handoff_census.py', 'b668_census_closing.txt'), ('b327_faces_census.py', 'b668_faces_census_closing.txt'),
                      ('b303_pins.py', 'b668_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b668'])
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
            b[:34], k[:21], loc[:12] or 'none', 'yes' if ('refs/heads/' + b) in remote_refs('D:/' + k) else 'no', merged, what))
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
    S = jl('b668_scores.json')
    pre, post = rd('b668_checks.txt'), rd('b668_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b668 -- THE CLOSING RECORD. ### **LANE THREE, ACT NINETY-FIVE, THE RE-CUT ACT: b667 AT ITS WEIGHT; SIDE-grh-transfer`S SENTENCES GRADED, '
         'CUT, BUILT ON THE RUNNER AND MERGED; THE PLAN-FORM SECTION AND THE MID-ACT CITATION CHECK ENTERED; THE MIRROR EXPORT, UNDER (R278).**',
         '=' * 104]
    sys.path.insert(0, T)
    import b668_worklist as WL
    rec_ = jl('b668_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b668_seal_hashes.json):'] + [
        '      %-26s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    cc = rd('b668_citation_check.txt')
    L += ['### THE CITATION CHECK (the gate step, before the ferry was banked; relay data/b668_citation_check.txt): ' + verdict(
        cc, r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+') + ' ; the mid-act checks ((R278)(4)): ' + '; '.join(
        re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', cc)), '']
    RL = (jl('b668_record_lines.json').get('lines') or []) + (jl('b668_items_lines.json').get('lines') or [])
    L += ['### THE RECORD LINES ((R278)(1), (3)-(5), and the author`s word on the cut; relay data/b668_record_lines.json, data/b668_items_lines.json): '
          + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b668_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b668_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+'), '']
    L += ['### THE GRADES ((R278)(2) and the author`s answer; relay data/b668_sentence_grades.txt): ' + verdict(
        rd('b668_sentence_grades.txt'), r'PARENT BLOCKS \d+[^*]*'), '']
    L += ['### THE CUT ((R278)(2); relay data/b668_cut_SIDE-grh-transfer.txt): ' + verdict(rd('b668_cut_SIDE-grh-transfer.txt'), r'CUT COMMITS \d+ IN \d+ FILES[^*]*'),
          '    the kernel files read from the cut bank ((R274)(4)): %s' % (jl('b668_cut_SIDE-grh-transfer.json').get('file_list') or '### NONE'), '']
    j = jl('b668_runner_rows.json')
    L += ['### THE RUNNER ((R263)(4), the workflow on main where absent, the print list from print_targets.txt; relay data/b668_runner_rows.json, '
          'data/b668_runner_SIDE-grh-transfer.txt, data/b668_prints_SIDE-grh-transfer.txt):']
    for r in (j.get('prior_runs') or []) + (j.get('rows') or []):
        w = WL.RUNNER.get(r['kernel']) or {}
        L.append('      %-12s %s at %s ; workflow %s ; dispatched at %s ; run %s %s ; artifact sha256 %s ; memory low %s MB ; gate %s' % (
            r['kernel'][:12], r['branch'], r['ref'][:8], w.get('workflow_commit'), w.get('dispatched_at'), r['run_id'], r['conclusion'],
            (r['artifact_sha256'] or '-')[:16], r['mem_low'], r['gate']))
    L += ['    ' + verdict(rd('b668_runner_SIDE-grh-transfer.txt'), r'RUN \d+ ; CONCLUSION[^*]*'),
          '    push-triggered runs beside the dispatch: %s' % ([p_.get('id') for p_ in j.get('push_runs') or []] or 'NONE (the kernel carries no other workflow)'), '']
    rr = (j.get('rows') or [{}])[0]
    L += ['### THE MERGE ((R278)(2), alone on the gate reading): %s merged %s, tag %s peeled %s, parents %s ; the merged tree the built tree %s '
          '(defect (c): the workflow file alone differs)' % (rr.get('kernel'), rr.get('merged'), rr.get('tag'), j.get('tag_peeled'),
                                                             j.get('merge_parents'), j.get('tree_equal')), '']
    L += ['### THE AXIOM CLAIM ((R278)(2); relay data/b668_axiom_claim_after.txt): ' + verdict(rd('b668_axiom_claim_after.txt'),
                                                                                              r'G-AXIOM-CLAIM BEFORE: CONTRADICTED \d+ ; AFTER: CONTRADICTED \d+'), '']
    mj = jl('b668_mirror.json')
    L += ['### THE MIRROR-REFRESH EXPORT ((R278)(6); relay data/b668_mirror.txt), BUILT AFTER THE LAST PLACE-papers PUSH, for the author`s Project:',
          '      %s ; md5 %s ; %s bytes ; files %s ; MANIFEST md5 %s ; PLACE-papers last commit %s (in MANIFEST %s) ; %s ; verification %s' % (
              mj.get('zip'), mj.get('zip_md5'), mj.get('bytes'), mj.get('files'), mj.get('manifest_md5'), mj.get('pp_head'),
              mj.get('last_commit_in_manifest'), mj.get('root_line'), 'CLEAN' if mj.get('clean') else '### NOT CLEAN'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b668_author_answers.txt): ' + verdict(rd('b668_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b668_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL:'] + ['    (%s) %s -- %s' % (k, (S.get(k) or ['?', ''])[0], (S.get(k) or ['', ''])[1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b668_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b668_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b668_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b668_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    kernel mains moved by the workflow where absent and the one merge on the hosted runner`s gate reading alone (SIDE-grh-transfer,',
          '    v0.5.1) ; no lean or lake run on this host ; no worktree made or removed ; b628`s local intake bank and the navigator`s export',
          '    untracked ; no identifier of the author in any outbound request, workflow file or input ; no secret added, the platform`s own',
          '    token alone ; the seat`s plain requests to github.com (its ls-remote reads, its pushes, the gh calls that dispatched the one run and',
          '    read it and its artifact back) the act`s only outbound calls ; the deposit route untouched, publish never called ; no shared',
          '    tool edited ; FINDINGS and OPEN_TRAILS appended ; one line appended to data/act_roots.txt as the act`s last bank step ; ERRATA,',
          '    SPIRAL_MAP, README, REGISTRY, the censuses, the pages, the map, the monograph and the companions untouched ; the mirror export',
          '    written to D:/MY-DOwnloads, outside every tree', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b668_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
