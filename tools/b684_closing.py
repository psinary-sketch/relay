# -*- coding: utf-8 -*-
"""b684_closing.py -- THE CLOSING RECORD OF b684, UNDER (R294). Carried from b683_closing.py by the Write tool, its act text written for b684,
with no repair at carry time in its logic (relay data/b684_tool_repairs.txt): the remote reads one per call in sequence, an empty read re-read
alone before any row is declared (b674_rules.txt row 1); the tag rows reading a lightweight tag at its own line; each bank's verdict line and
not its title; the citation line from the banks, the mid-act check's header read in both wordings; the captures in b673's form, the head line
reading the record's capture with its branch and its tip's subject; the mirror export named from its bank. The sections this act's components
make: the split, the next document, the residues; SIDE-class-number-anomaly joins the repositories read, and the four new tags the tag rows.
`python tools/b684_closing.py dry` -- (R285)(2)'s rule row (relay data/b675_rules.txt row 1), the closing a gate step before the seal: the record
written to the scratchpad and its readings printed; the censuses run into the scratchpad; no bank of relay data/ written.
### Writes data/b684_closing.txt and the closing censuses and pins (each its own tool's output) and nothing else. The template is b612_closing.py.
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
DRY = 'dry' in sys.argv[1:]
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, T)
import b684_worklist as WL   # noqa: E402

OUTD = WL.SP if DRY else D

REPOS = ['relay', 'MY-DOwnloads/PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
         'SIDE-effects', 'SIDE-silence-principle', 'SIDE-omega-b', 'SIDE-cosmo', 'SIDE-trivium', 'SIDE-residual-bridge',
         'SIDE-yang-mills-formation', 'SIDE-substrate-cluster', 'SIDE-constants', 'SIDE-simplicity', 'SIDE-bsd-formation-transfer',
         'SIDE-bsd-multiplicity', 'SIDE-t7-topology-cmb', 'SIDE-local-cosmic-interface', 'SIDE-quaternionic-dark-sector', 'SIDE-spinor',
         'SIDE-bijection', 'SIDE-class-coupling', 'SIDE-coupling', 'SIDE-formation-arithmetic', 'SIDE-meta', 'SIDE-orchestrator',
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-grh-transfer', 'SIDE-window', 'SIDE-class-number-anomaly']
SEC, SEC_BRANCH, SEC_TAG = 'D:/SIDE-structural-error-correction', 'sec-axiom-b623', 'v0.2.2'
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603', 'platt-b626', 'cite-b628', 'nb-b629', 'dedekind-b631']
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']
TAGS = [('SIDE-class-number-anomaly', 'v0.2.1'), ('SIDE-class-number-anomaly', 'v0.2'), ('SIDE-window', 'v0.5.2'), ('SIDE-window', 'v0.5.1'),
        ('SIDE-trivium', 'v0.1.2'), ('SIDE-trivium', 'v0.1.1'), ('SIDE-silence-principle', 'v0.2.2'), ('SIDE-silence-principle', 'v0.2.1'),
        ('SIDE-bijection', 'v0.2.1'), ('SIDE-explicit-formula', 'v0.33'), ('SIDE-explicit-formula', 'v0.32'), ('SIDE-grh-transfer', 'v0.5.1'),
        ('SIDE-cosmo', 'v0.3.1'), ('SIDE-effects', 'v0.1.1'), ('SIDE-carrier-spec', 'v0.4.2'), ('SIDE-structural-error-correction', 'v0.2.3'),
        ('SIDE-lv-conservation', 'v0.13.0'), ('SIDE-global-section', 'v0.3.0'), ('SIDE-kernel', 'v1.8')]
CUT_BRANCHES = (('SIDE-class-number-anomaly', 'recut-class-number-anomaly-b684'), ('SIDE-window', 'recut-window-b684r'),
                ('SIDE-trivium', 'recut-trivium-b684r'), ('SIDE-silence-principle', 'recut-silence-principle-b684r'))
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


VLINE = re.compile(r'^\s*### ### \*\*(.*?)\*\*\s*$', re.M)


def vline(text):
    """### b675's repair (2), carried: a bank's verdict line -- its last `### ### **...**` line -- and never a pattern that meets its title."""
    m = VLINE.findall(text or '')
    return m[-1].rstrip('.') if m else '### NO VERDICT LINE'


def verdict(text, pat):
    m = re.search(pat, text)
    return m.group(0) if m else '### NOT FOUND'


CARRIED = [
    '    (a) ### **THE NEXT ACT, (R294)(8)**: b685, the research act: W-ORD-EPSTEIN-COUNT, the count law for Z_Q that P3 (Q0Count) names, by route',
    '        (i) in the literature or route (ii) certified by the argument principle under the (3c) bound, its plan to read',
    '        data/b675_hypotheses.txt, data/b683_map_h.txt and data/b667_epstein_plan.txt before any route is chosen; b690 the reading act.',
    '    (b) The silence-principle introduction (SIDESilencePrinciple/Basic.lean :7-:12 at v0.2.2), carried: its row`s reason does not reach it',
    '        (relay data/b684_residue_actions.txt R3b) -- for the next reading act`s census.',
    '    (c) Three FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md cells (:628-:630) naming SIDE-silence-principle v0.2.1, which the generator would',
    '        carry to v0.2.2 -- not written; carried to the next act that regenerates the cells.',
    '    (d) The licensed table`s next documents at 3: SIDE-spinor (15 rows) and SIDE-li-map (13 rows).',
    '    (e) W-ORD-EPSTEIN-COUNT; W-ORD-LEDGER-SPLIT-RESOLVER (on the author`s word); W-ORD-ROOT-BINARY-BANK; W-ORD-CHAIN-PAGE-B638-CASES; the',
    '        run`s orders of b672 open: `W-ORD-ONE-COPY`, `W-ORD-TABLE-SHAPE`, `W-ORD-GRADE-MOVED`, `W-ORD-PRINT-TARGETS`,',
    '        `W-ORD-ABSENT-DECLARATIONS`, `W-ORD-PROSE-PINS`.',
    '    (f) b628`s full intake bank, the navigator`s export, b671`s uncompressed points file and b681`s units file stay local and untracked.',
    '    (g) The act root of b684 is relay data/act_roots.txt`s last line, chained from b683`s root; the mirror export carries it in MANIFEST.',
    '    (h) Branches left for the next act`s step zero: the push-b684* branches of relay and PLACE-papers; push-b684-main and push-b684-merge',
    '        of SIDE-class-number-anomaly, push-b684r-merge of SIDE-window, SIDE-trivium and SIDE-silence-principle; the four cut branches',
    '        (recut-class-number-anomaly-b684, recut-window-b684r, recut-trivium-b684r, recut-silence-principle-b684r), local and remote, each',
    '        merged; the quarantine and kept kernel branches untouched.',
    '    (i) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]
_REMOTE = {}
REREAD = []


def _ls(p):
    out = g(p, 'ls-remote', 'origin')
    return dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in out.split(NL) if '\t' in l)


def read_remotes(paths):
    """### carried from b674's repair: one ls-remote per repository, one call at a time, in sequence; every read that returns empty is re-read
    ### alone after the pass and before any row is declared, and the re-read printed (relay data/b674_rules.txt row 1)."""
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


def remote_tag(p, t):
    r = remote_refs(p)
    if 'refs/tags/%s^{}' % t in r:
        return r['refs/tags/%s^{}' % t], 'annotated, peeled'
    if 'refs/tags/%s' % t in r:
        return r['refs/tags/%s' % t], 'lightweight, its own line'
    return '', '### NOT AT THE REMOTE'


ACT = 'b684'
CAPTURES = (('relay', 'relay', ROOT), ('PLACE-papers', 'pp', 'D:/MY-DOwnloads/PLACE-papers'))


def head_line(dd=None, act=ACT):
    dd = dd or D

    def _t(n):
        p = os.path.join(dd, n)
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''

    def _back(n, repo):
        t = _t(n)
        m = re.search(r'push_gated: main read back at the remote: (\w+)', t)
        b = re.search(r'push_gated: repo \S+ ; branch (\S+) ; tip (\w+)', t)
        if not m or not b:
            return '### NOT READ'
        subj = g(repo, 'log', '-1', '--format=%s', b.group(2))
        if b.group(1) != 'push-%s' % act or not subj.startswith('%s record' % act):
            return '### %s IS NOT THE RECORD`S CAPTURE (branch %s, tip %s "%s")' % (n, b.group(1), b.group(2)[:8], subj[:40])
        return m.group(1)

    parts = []
    for name, key, repo in CAPTURES:
        v = _back('%s_%s_push_out.txt' % (act, key), repo)
        parts.append('%s %s' % (name, v if v.startswith('###') else v[:8 if key == 'relay' else 7]))
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


def citation_line():
    cc, cj, dl = rd('b684_citation_check.txt'), jl('b684_citation_check.json'), rd('b684_defects.txt')
    head = verdict(cc, r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+')
    misses = cj.get('misses') or []
    needles = re.findall(r"^### \(R278\)\(4\) THE MID-ACT CHECK \([^)]*\): the (?:navigator`s )?answer carrying '([^']*)'", cc, re.M)
    figs = re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', cc)
    nav = re.findall(r"^    \(([a-z]'?)\) THE NAVIGATOR'S", dl, re.M)
    return ('%s ; the misses as the bank lists them: %d (%s) ; the answers checked ((R278)(4)), by their needles: %s, the prints %s ; '
            'entered as the defects bank letters them: the navigator`s %s' % (
                head, len(misses), '; '.join(m[:60] for m in misses) or 'NONE', '; '.join(needles) or 'NONE', '; '.join(figs) or 'NONE',
                ', '.join('(%s)' % x for x in nav) or 'NONE'))


def mirror_line():
    j = jl('b684_mirror.json')
    if not j:
        return '### TO BE BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH (the b670 form, mirror-refresh-2026-10-18-b684.zip)'
    return '%s ; %d bytes ; sha256 %s ; MANIFEST md5 %s ; entries %d ; %s ; %s' % (
        j.get('zip'), j.get('bytes', 0), (j.get('zip_sha256') or '')[:16], j.get('manifest_md5'), j.get('entries', 0), j.get('root_line') or '### NO ROOT LINE',
        'CLEAN ON ALL THREE CLAUSES' if j.get('clean') else '### NOT CLEAN')


def main():
    for tool, out in (('b307_handoff_census.py', 'b684_census_closing.txt'), ('b327_faces_census.py', 'b684_faces_census_closing.txt'),
                      ('b303_pins.py', 'b684_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b684'])
        b = o.replace(chr(13), '').encode('utf-8')
        p = os.path.join(OUTD, out)
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
        rem, kind = remote_tag(p, t)
        heads.append('      %-32s %s peeled %s ; at the remote %s (%s) ; main %s ; %s' % (k, t, loc[:12], rem[:12], kind, g(p, 'rev-parse', 'main')[:12],
                                                                                       'AGREE' if loc and loc == rem else '### DIFFER'))
    for ck, cb in CUT_BRANCHES:
        loc = g('D:/' + ck, 'rev-parse', 'refs/heads/' + cb)
        rem = remote_refs('D:/' + ck).get('refs/heads/' + cb, '')
        heads.append('      %-32s local %s ; remote %s ; %s (a cut`s branch, merged at main)' % (cb[:32], loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
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
    srt, skind = remote_tag(SEC, SEC_TAG)
    heads.append('      %-32s local %s ; %s peeled %s, at the remote %s (%s) ; main %s (unmoved by this act) ; %s (kept, local)' % (
        SEC_BRANCH, sb[:12], SEC_TAG, st[:12], srt[:12], skind, sm[:12], 'AGREE' if sb and sb == st == srt else '### DIFFER'))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED, NOT WRITTEN BY THIS ACT' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?'))
    S = jl('b684_scores.json')
    pre, post = rd('b684_checks.txt'), rd('b684_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b684 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND ELEVEN, THE RE-CUT ACT: b683 AT ITS WEIGHT; THE LICENSED TABLE`S NEXT '
         'DOCUMENT CUT; THE THREE RESIDUES OF b674, b676 AND b678 RE-DERIVED AND APPLIED; THE STANDING PART SPLIT, UNDER (R294).**',
         '=' * 104]
    rec_ = jl('b684_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b684_seal_hashes.json):'] + [
        '      %-30s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step at step zero; relay data/b684_citation_check.txt): ' + citation_line(), '']
    RL = jl('b684_record_lines.json').get('lines') or []
    L += ['### THE RECORD LINES ((R294)(1); relay data/b684_record_lines.json): ' + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b684_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b684_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+') + ' ; THE CLOSING`S DRY RUN (relay data/b675_rules.txt row 1): ' + verdict(
        rd('b684_reg_gate.txt'), r'THE CLOSING DRY-RUN STEP : [A-Z ]+'), '']
    L += ['### THE SPLIT ((R294)(2); relay data/b684_rules.txt row (1)): ' + ' '.join(verdict(rd('b684_rules.txt'), r'A SUITE PART OVER 450 s SPLITS THE NEXT RUN').split())
          + ' ; the parts %s' % ', '.join(WL.PARTS),
          '    the pre-run (relay data/b684_arms_prerun.txt): ' + ' ; '.join(re.findall(r'(?m)^  ### PART [\w-]+ : ARMS \d+ ; \d+ s$', rd('b684_arms_prerun.txt'))).replace('  ### ', ''), '']
    L += ['### THE NEXT DOCUMENT ((R294)(3); relay data/b684_naming.txt): ' + vline(rd('b684_naming.txt')),
          '    the cut (relay data/b684_cut.txt): ' + (VLINE.findall(rd('b684_cut.txt')) or ['### NO VERDICT LINE'])[0].rstrip('.'),
          '    the runs: ' + ' ; '.join(vline(rd('b684_runner_SIDE-class-number-anomaly_%s.txt' % x)) for x in ('before', 'after')),
          '    the prints (relay data/b684_prints_SIDE-class-number-anomaly.txt): ' + vline(rd('b684_prints_SIDE-class-number-anomaly.txt')),
          '    the root`s banks before the root (relay data/b684_root_banks.txt): ' + (
              vline(rd('b684_root_banks.txt')) if rd('b684_root_banks.txt') else 'TO BE READ AT THE ROOT, before it is computed'), '']
    L += ['### THE RESIDUES ((R294)(4); relay data/b684_residues.txt, data/b684_residue_actions.txt, its verdict over two lines): ' + ' '.join(
        verdict(rd('b684_residue_actions.txt'), r'RESIDUES 3 ; ACTIONS RE-DERIVED[^*]*').replace('###', ' ').split()),
          '    the cuts (relay data/b684_cut.txt): ' + vline(rd('b684_cut.txt'))] + [
          '    %s: %s ; %s' % (k, vline(rd('b684_runner_%s_after.txt' % k)), vline(rd('b684_prints_%s.txt' % k)))
          for k in ('SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle')] + ['']
    L += ['### THE MIRROR (relay data/b684_mirror.txt, the b670 form, after the root and the last PLACE-papers push): ' + mirror_line(), '']
    L += ['### THE CARRY-TIME READING ((R294)`s ferry; relay data/b684_tool_repairs.txt): ' + vline(rd('b684_tool_repairs.txt')),
          '    the remote reads this run: %d repositories, one call each in sequence ; empty reads re-read alone: %s' % (
              len(_REMOTE), '; '.join(REREAD) or 'NONE'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b684_author_answers.txt): ' + verdict(rd('b684_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b684_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL:'] + ['    (%s) %s -- %s' % (k, (S.get(k) or ['?', ''])[0], (S.get(k) or ['', ''])[1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b684_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b684_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b684_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+'),
                                       verdict(rd('b684_faces_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b684_faces_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b684_pins_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b684_pins_closing.txt'), encoding='utf-8').read(),
                                    r'REPOS HARD-FAILING : \d+'),
          '    four kernel mains written, as (R294)(3)-(4) amend N5: SIDE-class-number-anomaly`s workflow and print list each alone, its docstring',
          '    merge and its tag v0.2.1; SIDE-window`s, SIDE-trivium`s and SIDE-silence-principle`s header merges and tags v0.5.2, v0.1.2, v0.2.2 ;',
          '    five runner dispatches, one per tree state ; no lean or lake run on this host ; no worktree made or removed ; no file deleted ; the',
          '    branches (R294)(5) names deleted at step zero, one per command and each its own message ; b628`s local intake bank, the navigator`s',
          '    export, b671`s uncompressed points file and b681`s units file untracked ; no identifier of the author in any outbound request ; no',
          '    secret added ; the seat`s plain requests to github.com (its git reads and pushes, the runner`s dispatches and reads) the act`s only',
          '    outbound calls ; the deposit route untouched, publish never called ; tools/rule_arms.py repaired at carry time ; FINDINGS and',
          '    OPEN_TRAILS appended ; data/act_roots.txt appended by the act`s root ; no README, REGISTRY, FOUNDATIONS or faces-page byte ; the mirror',
          '    zip written outside every repository ; nothing of TECHNE or any patent written', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(OUTD, 'b684_closing_dry.txt' if DRY else 'b684_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    if DRY:
        print('  ### THE CLOSING DRY-RUN, its readings (written to the scratchpad, %s):' % p)
        for l in L:
            if l.startswith(('b684 closed', '### THE CITATION', '### THE SPLIT', '### THE NEXT DOCUMENT', '### THE RESIDUES',
                             '### THE MIRROR', '    the ', '    SIDE-', '### THE CARRY-TIME', '### THE RECORD LINES', '### THE DRY RUN')) \
                    or ' peeled ' in l or 'next ferry' in l:
                print('    ' + l[:400])
        print('  ### ### **THE CLOSING DRY-RUN : %s**' % ('READ' if all(x not in NL.join(L) for x in ('### NO VERDICT LINE',)) else 'A VERDICT LINE UNREAD'))
    else:
        print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
