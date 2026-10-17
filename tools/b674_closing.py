# -*- coding: utf-8 -*-
"""b674_closing.py -- THE CLOSING RECORD OF b674, UNDER (R284). Carried from b673_closing.py by the Write tool, its act text written for b674,
with the two repairs (R284)(5) orders at carry time (relay data/b674_tool_repairs.txt): THE H5 LINE prints one line -- the H5 bank's verdict
line, anchored on its `**H5:` and ending at its `.**` -- and not the bank (b673's pattern `H5: [^*]*` matched the bank's header and ran to its
first asterisk, b673 defect (p) item 2); THE REMOTE READS are one per call, in sequence, and a read that returns empty is re-read alone after
the pass and before any row is declared, the re-read printed (b673 defect (p) item 1; relay data/b674_rules.txt row 1).
The sealed tools' hashes compared at the close and printed (OPEN_TRAILS :13307); THE CITATION CHECK, the gate step, and the mid-act checks of
(R278)(4); THE RECORD LINES; THE DRY RUN; THE DRAFTS (the ceiling's sites, the faces page); THE RE-CUT (the cut, the runs, the merge); THE
CLOSING TOOL'S REPAIRS; THE MIRROR; the prompts and the author's word; the next act.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept branches at the
### remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and writes data/b674_closing.txt
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
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-grh-transfer', 'SIDE-window']
SEC, SEC_BRANCH, SEC_TAG = 'D:/SIDE-structural-error-correction', 'sec-axiom-b623', 'v0.2.2'
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603', 'platt-b626', 'cite-b628', 'nb-b629', 'dedekind-b631']
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']
LOCAL = [('SIDE-window', 'recut-window-b674', 'the docstring cut, merged at e5b737a (Component 3); listed for deletion in the next ferry')]
TAGS = [('SIDE-window', 'v0.5.1'), ('SIDE-window', 'v0.5.0'), ('SIDE-explicit-formula', 'v0.32'), ('SIDE-grh-transfer', 'v0.5.1'),
        ('SIDE-cosmo', 'v0.3.1'), ('SIDE-effects', 'v0.1.1'), ('SIDE-carrier-spec', 'v0.4.2'), ('SIDE-structural-error-correction', 'v0.2.3'),
        ('SIDE-lv-conservation', 'v0.13.0'), ('SIDE-global-section', 'v0.3.0'), ('SIDE-kernel', 'v1.8')]
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
    '    (a) ### **THE NEXT ACT, (R284)(9)**: b675, a research act, its ruling then; the Li index at Q0 placed by the author as its bench or',
    '        a later one; b680 the reading act, reading 2 of 2.',
    '    (b) SIDE-window`s Sawtooth.lean header cut in part: the marker at :17 ("(a) ... COMPILED HERE") stands, the table`s ACTION covering',
    '        one of the header`s two claims (relay data/b674_cut.txt); SIDE-trivium`s docstrings at the next re-cut act.',
    '    (c) The walk`s reach into local binders, an item under `W-ORD-PRINT-TARGETS` (OPEN_TRAILS :14480).',
    '    (d) The run`s orders of b672 open: `W-ORD-ONE-COPY`, `W-ORD-TABLE-SHAPE`, `W-ORD-GRADE-MOVED`, `W-ORD-PRINT-TARGETS`,',
    '        `W-ORD-ABSENT-DECLARATIONS`, `W-ORD-PROSE-PINS`; the ledger split at the b680 reading act; the nine kernels without a print bank.',
    '    (e) b628`s full intake bank, the navigator`s export and b671`s uncompressed points file stay local and untracked in relay data/.',
    '    (f) The act root of b674 is relay data/act_roots.txt`s last line; the mirror export of this act carries it in MANIFEST.',
    '    (g) Branches left for the next act`s step zero: the push-b674* branches of relay, PLACE-papers and SIDE-window and',
    '        SIDE-window`s recut-window-b674, deleted when the next ferry`s list carries them; the quarantine and kept kernel branches untouched.',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
    '    (i) The closing reads each repository`s remote refs once, one call at a time in sequence, an empty read re-read alone before any row',
    '        is declared (relay data/b674_rules.txt row 1).',
]
_REMOTE = {}
REREAD = []


def _ls(p):
    out = g(p, 'ls-remote', 'origin')
    return dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in out.split(NL) if '\t' in l)


def read_remotes(paths):
    """### (R284)(5), the repair at carry: one ls-remote per repository, one call at a time, in sequence; every read that returns empty is
    ### re-read alone after the pass and before any row is declared, and the re-read printed (relay data/b674_rules.txt row 1)."""
    for p in paths:
        if p not in _REMOTE:
            _REMOTE[p] = _ls(p)
    for p in paths:
        if 'refs/heads/main' not in _REMOTE[p]:
            again = _ls(p)
            REREAD.append('%s : first read empty ; re-read alone: %s' % (os.path.basename(p), 'refs read' if 'refs/heads/main' in again else '### EMPTY AGAIN'))
            _REMOTE[p] = again


def remote_refs(p):
    return _REMOTE.get(p, {})


ACT = 'b674'


def head_line(dd=None, act=ACT):
    """### (R245)(3), standing: the closing's first line, written from the act's banks."""
    dd = dd or D

    def _t(n):
        p = os.path.join(dd, n)
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''

    def _back(n):
        m = re.search(r'push_gated: main read back at the remote: (\w+)', _t(n))
        return m.group(1) if m else '### NOT READ'

    parts = ['relay %s' % _back('%s_relay_push_out.txt' % act)[:8], 'PLACE-papers %s' % _back('%s_pp_push_out.txt' % act)[:7],
             'SIDE-window %s v0.5.1' % _back('%s_window_merge_push_out.txt' % act)[:7]]
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


H5_LINE = re.compile(r'\*\*H5: ([^*]*?)\.\*\*')   # ### the repair at carry: the verdict line, anchored on `**H5:`, ending at `.**`


def main():
    for tool, out in (('b307_handoff_census.py', 'b674_census_closing.txt'), ('b327_faces_census.py', 'b674_faces_census_closing.txt'),
                      ('b303_pins.py', 'b674_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b674'])
        b = o.replace(chr(13), '').encode('utf-8')
        p = os.path.join(D, out)
        open(p + '.tmp', 'wb').write(b)
        os.replace(p + '.tmp', p)
    paths = ['D:/' + r for r in REPOS] + [SEC]
    read_remotes([p for p in paths if p not in _REMOTE])
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
    S = jl('b674_scores.json')
    pre, post = rd('b674_checks.txt'), rd('b674_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b674 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND ONE, THE RE-CUT ACT: b673 AT ITS WEIGHT; H5 THROUGH THE BRIDGE; THE '
         'TWO DRAFTS WRITTEN ON THE AUTHOR`S WORD; SIDE-window`S DOCSTRINGS CUT; THE CLOSING TOOL REPAIRED AT CARRY, UNDER (R284).**', '=' * 104]
    sys.path.insert(0, T)
    import b674_worklist as WL
    rec_ = jl('b674_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b674_seal_hashes.json):'] + [
        '      %-26s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    cc = rd('b674_citation_check.txt')
    L += ['### THE CITATION CHECK (the gate step, before the ferry was banked; relay data/b674_citation_check.txt): ' + verdict(
        cc, r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+') + ' (the seven misses raised and answered, the navigator`s (a)-(d) and (e`)) ; '
        'the mid-act checks ((R278)(4)): ' + '; '.join(re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', cc)), '']
    RL = []
    for b_ in ('b674_record_lines.json', 'b674_record_lines_c2.json'):
        RL += jl(b_).get('lines') or []
    L += ['### THE RECORD LINES ((R284)(1)-(3); relay data/b674_record_lines.json, data/b674_record_lines_c2.json): '
          + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b674_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b674_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+'), '']
    L += ['### THE DRAFTS ((R284)(3), the author`s word: write both): ' + verdict(rd('b674_ceiling_diff.txt'), r'THE \(R183\)\(3\) SENTENCE UNCHANGED[^*]*'),
          '    the faces page: ' + verdict(rd('b674_faces_diff.txt'), r'CONTROL \w+ ; ADDED \d+ ; REMOVED \d+[^*]*'), '']
    h5 = H5_LINE.search(rd('b673_h5.txt'))
    L += ['### H5 THROUGH THE BRIDGE ((R284)(2); relay data/b673_h5.txt, its verdict line): %s' % (h5.group(1) if h5 else '### NOT FOUND'), '']
    rows = jl('b674_runner_rows.json').get('rows') or []
    L += ['### THE RE-CUT ((R284)(4); relay data/b674_cut.txt): ' + verdict(rd('b674_cut.txt'), r'ROWS \d+ ; MATCHES AFTER[^*]*'),
          '    the runs: ' + ' ; '.join('%s %s at %s %s' % (r.get('label'), r.get('run_id'), (r.get('ref') or '')[:7], r.get('gate')) for r in rows),
          '    the prints: ' + verdict(rd('b674_prints_compare.txt'), r'PRINTS BEFORE[^*]*'),
          '    the merge: ' + verdict(rd('b674_window_merge_push_out.txt'), r'tag v0\.5\.1 peeled local \w+ remote \w+'), '']
    L += ['### THE CLOSING TOOL`S REPAIRS AT CARRY ((R284)(5); relay data/b674_tool_repairs.txt): ' + verdict(rd('b674_tool_repairs.txt'), r'REPAIRS \d+[^*]*'),
          '    the remote reads this run: %d repositories, one call each in sequence ; empty reads re-read alone: %s' % (
              len(_REMOTE), '; '.join(REREAD) or 'NONE'), '']
    mj = jl('b674_mirror.json')
    L += ['### THE MIRROR-REFRESH EXPORT (relay data/b674_mirror.txt), BUILT AFTER THE LAST PLACE-papers PUSH, for the author`s Project:',
          '    %s ; %s bytes ; sha256 %s ; MANIFEST md5 %s ; entries %s ; %s ; the verification %s' % (
              mj.get('zip', '### NOT BUILT'), mj.get('bytes'), (mj.get('zip_sha256') or '')[:16], mj.get('manifest_md5'), mj.get('entries'),
              mj.get('root_line') or '### NO ROOT LINE', 'CLEAN ON ALL THREE CLAUSES' if mj.get('clean') else '### NOT CLEAN'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b674_author_answers.txt): ' + verdict(rd('b674_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b674_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL:'] + ['    (%s) %s -- %s' % (k, (S.get(k) or ['?', ''])[0], (S.get(k) or ['', ''])[1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b674_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b674_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b674_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b674_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    SIDE-window`s main moved by the workflow commit (7c4a2e1) and the docstring merge (e5b737a, tag v0.5.1) alone, by the navigator`s',
          '    amendment of N5 ; two dispatches on the hosted runner, one per tree state ; no lean or lake run on this host ; no worktree made',
          '    or removed ; no file deleted ; b628`s local intake bank, the navigator`s export and b671`s uncompressed points file untracked ;',
          '    no identifier of the author in any outbound request ; no secret added ; the seat`s plain requests to github.com (its git reads and pushes, and the gh',
          '    workflow, run and artifact calls to the author`s own repositories) the act`s only outbound calls ; the deposit route untouched,',
          '    publish never called ; no shared tool edited ; FINDINGS and OPEN_TRAILS appended ; README and REGISTRY written at the successor`s',
          '    two sites alone, on the author`s word ; THE_CLAUSE_AND_ITS_COMPILED_FACES.md re-emitted by its generator ; one line appended to',
          '    data/act_roots.txt as the act`s last bank step ; nothing of TECHNE or any patent written', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b674_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
