# -*- coding: utf-8 -*-
"""b664_closing.py -- THE CLOSING RECORD OF b664, UNDER (R274). Carried from b662_closing.py and b663_closing.py by the Write tool, its act
text written for b664; the sealed tools' hashes compared at the close and printed (OPEN_TRAILS :13307); THE CITATION CHECK, the gate step;
THE RECORD LINES (b663 at its weight, the two orders placed, the file-constant rule) and the no-disclosure re-run; THE DRY RUN, the gate's step
as its record prints it; THE GRADES of SIDE-effects and the five blocks without a cell; THE CUT; THE HOSTED RUNNER, its run read back and the
merge on its gate reading; THE MET TEST made durable; THE MIRROR export, its MANIFEST md5 and last commit; the prompts and the author's word;
the next act.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept branches at the
### remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and writes data/b664_closing.txt
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
         'SIDE-structural-error-correction', 'SIDE-carrier-spec']
SEC, SEC_BRANCH, SEC_TAG = 'D:/SIDE-structural-error-correction', 'sec-axiom-b623', 'v0.2.2'
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603', 'platt-b626', 'cite-b628', 'nb-b629', 'dedekind-b631']
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']
LOCAL = [('SIDE-effects', 'docstrings-cut-SIDE-effects', 'the cut, merged on the runner`s gate reading'),
         ('SIDE-effects', 'push-b664-merge', 'the merge push'),
         ('SIDE-effects', 'push-b664-workflow', 'the workflow push')]
TAGS = [('SIDE-effects', 'v0.1.1'), ('SIDE-explicit-formula', 'v0.29'), ('SIDE-carrier-spec', 'v0.4.2'), ('SIDE-structural-error-correction', 'v0.2.3'),
        ('SIDE-lv-conservation', 'v0.13.0'), ('SIDE-global-section', 'v0.3.0')]
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
    '    (a) ### **THE NEXT ACT, (R274)(8)**: b665, the research act: the Keiper face`s finite-n equality and the transform-bound order',
    '        (OPEN_TRAILS :14162, placed at :14186), its ruling then; then b667 W-ORD-EPSTEIN-CERTIFY (placed at :14188), b669 the χ-Li',
    '        converse, b670 the reading act; the close-pair bench after the companions.',
    '    (b) Listed for SIDE-effects` cell refresh, on the author`s word: the five Milestones.lean blocks restated at b648, UNRESOLVED-NO-CELL',
    '        in relay data/b664_sentence_grades.txt, the refresh owing b647-form cells for the restated text (the seat`s hand reading beside',
    '        them in data/b664_restated_reading.txt is a reading, not a grade); and AGENTS.md`s stale lines ("named-sorry" Milestones; Module 1',
    '        sorries) against the kernel at main, which has no sorry in code -- a file outside the act`s blocks, not edited.',
    '    (c) SIDE-effects` first relay print bank: data/b664_prints_SIDE-effects.txt (34 declarations at the standard three or none), the',
    '        reference from here; the README`s "Axiom-free" (:28) and "0 axioms beyond ZFC" (:103) read against it, not contradicted.',
    '    (d) The tag phase-1.5-module-1-v2 of SIDE-effects stands outside the v0.1 series, not moved (the author`s word).',
    '    (e) G-AXIOM-CLAIM`s one contradiction at HEAD, declared on the face: SIDE-cosmo SteaneExemplar.lean:6, declared until SIDE-cosmo`s',
    '        re-cut act ((R264)(5)).',
    '    (f) b628`s full intake bank and the navigator`s export stay local and untracked in relay data/.',
    '    (g) The act root of b664 is relay data/act_roots.txt`s last line; the mirror export of this act carries it in MANIFEST.',
    '    (h) Branches left for the next act`s step zero: the push-b664* branches of relay and PLACE-papers; push-b664-workflow and',
    '        push-b664-merge in SIDE-effects; docstrings-cut-SIDE-effects at the remote and local, merged, deleted in the house form after',
    '        --merged lists it, the remote delete alone in its command; the quarantine branches and the kept kernel branches untouched.',
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


ACT = 'b664'


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
    for tool, out in (('b307_handoff_census.py', 'b664_census_closing.txt'), ('b327_faces_census.py', 'b664_faces_census_closing.txt'),
                      ('b303_pins.py', 'b664_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b664'])
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
    S = jl('b664_scores.json')
    pre, post = rd('b664_checks.txt'), rd('b664_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b664 -- THE CLOSING RECORD. ### **LANE THREE, ACT NINETY-ONE, THE RE-CUT ACT: b663 AT ITS WEIGHT; THE TWO ORDERS PLACED; THE SUITE`S FILE '
         'CONSTANT MADE A BANK READ; SIDE-effects` SENTENCES GRADED, CUT, BUILT ON THE RUNNER AND MERGED; THE MIRROR EXPORT, UNDER (R274).**',
         '=' * 104]
    sys.path.insert(0, T)
    import b664_worklist as WL
    rec_ = jl('b664_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b664_seal_hashes.json):'] + [
        '      %-26s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step, before the ferry was banked; relay data/b664_citation_check.txt): ' + verdict(
        rd('b664_citation_check.txt'), r'CITES CHECKED \d+ ; OK \d+ ; MISSES \d+'), '']
    RL = jl('b664_record_lines.json').get('lines') or []
    L += ['### THE RECORD LINES ((R274)(1)-(4); relay data/b664_record_lines.json): ' + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL)]
    L += ['### THE NO-DISCLOSURE RE-RUN ((R274)(4), relay data/b664_nd_rerun.txt): ' + verdict(rd('b664_nd_rerun.txt'), r'THE FILE READ FROM THE BANK: [^*]*'), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b664_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b664_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+'), '']
    L += ['### THE GRADES ((R274)(5) and the author`s answer; relay data/b664_sentence_grades.txt): ' + verdict(
        rd('b664_sentence_grades.txt'), r'PARENT BLOCKS \d+[^*]*'), '']
    L += ['### THE CUT ((R274)(5); relay data/b664_cut_SIDE-effects.txt): ' + verdict(rd('b664_cut_SIDE-effects.txt'), r'CUT COMMITS \d+ IN \d+ FILES[^*]*'),
          '    the kernel files read from the cut bank ((R274)(4)): %s' % (jl('b664_cut_SIDE-effects.json').get('file_list') or '### NONE'), '']
    j = jl('b664_runner_rows.json')
    L += ['### THE HOSTED RUNNER ((R263)(4), the workflow on main where absent, the print list from print_targets.txt; relay data/b664_runner_rows.json, '
          'data/b664_runner_SIDE-effects.txt, data/b664_prints_SIDE-effects.txt):']
    for r in j.get('rows') or []:
        w = WL.RUNNER.get(r['kernel']) or {}
        L.append('      %-22s %s at %s ; workflow %s ; dispatched at %s ; run %s %s ; artifact sha256 %s ; memory low %s MB ; gate %s ; merged %s ; tag %s' % (
            r['kernel'][:22], r['branch'], r['ref'][:8], w.get('workflow_commit'), w.get('dispatched_at'), r['run_id'], r['conclusion'],
            (r['artifact_sha256'] or '-')[:16], r['mem_low'], r['gate'], r['merged'], r['tag']))
    L += ['    ' + verdict(rd('b664_runner_SIDE-effects.txt'), r'RUN \d+ ; CONCLUSION[^*]*'),
          '    the push-triggered build.yml runs beside, not the one dispatch: %s (the workflow`s push) ; %s (the merge`s push)' % (
              j.get('push_run'), j.get('merge_push_run')), '']
    L += ['### THE MET TEST ((R274)`s prompt, the author`s word; relay data/b664_tests_met_before.txt, data/b664_tests_met_after.txt): '
          'test_met_b646.py case (2) made durable -- before %s ; after %s' % (
              (jl('b664_tests_met_before.json').get('test_met_b646.py') or {}).get('last', '?'),
              (jl('b664_tests_met_after.json').get('test_met_b646.py') or {}).get('last', '?')), '']
    mj = jl('b664_mirror.json')
    L += ['### THE MIRROR-REFRESH EXPORT ((R274)(6); relay data/b664_mirror.txt), BUILT AFTER THE LAST PLACE-papers PUSH, for the author`s Project:',
          '      %s ; md5 %s ; %s bytes ; files %s ; MANIFEST md5 %s ; PLACE-papers last commit %s (in MANIFEST %s) ; %s ; verification %s' % (
              mj.get('zip'), mj.get('zip_md5'), mj.get('bytes'), mj.get('files'), mj.get('manifest_md5'), mj.get('pp_head'),
              mj.get('last_commit_in_manifest'), mj.get('root_line'), 'CLEAN' if mj.get('clean') else '### NOT CLEAN'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b664_author_answers.txt): ' + verdict(rd('b664_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b664_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL:'] + ['    (%s) %s -- %s' % (k, (S.get(k) or ['?', ''])[0], (S.get(k) or ['', ''])[1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b664_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b664_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b664_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b664_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    kernel mains moved by the workflow where absent and the one merge on the hosted runner`s gate reading alone (SIDE-effects) ;'
          ' no lean or lake run on this host ; no worktree made or removed ; b628`s local intake bank and the navigator`s export untracked ;'
          ' no identifier of the author in any outbound request, workflow file or input ; no secret added, the platform`s own token alone ; the'
          ' seat`s plain requests to github.com (its ls-remote reads, its pushes, the gh calls that dispatched the run and read it and its'
          ' artifact back) the act`s only outbound calls ; the deposit route untouched, publish never called ; no shared tool edited, the one'
          ' test repaired on the author`s word (tools/test_met_b646.py) ; FINDINGS and OPEN_TRAILS appended ; one line appended to'
          ' data/act_roots.txt as the act`s last bank step ; ERRATA, SPIRAL_MAP, README, REGISTRY, the censuses, the pages, the map, the'
          ' monograph and the companions untouched ; the mirror export written to D:/MY-DOwnloads, outside every tree', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b664_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
