# -*- coding: utf-8 -*-
"""b669_closing.py -- THE CLOSING RECORD OF b669, UNDER (R279). Carried from b668_closing.py by the Write tool, its act text written for b669;
the sealed tools' hashes compared at the close and printed (OPEN_TRAILS :13307); THE CITATION CHECK, the gate step, and the mid-act checks of
(R278)(4); THE RECORD LINES (the N4 repair of (R279)(6), b668 at its weight); THE DRY RUN, the gate's step as its record prints it; THE PLAN
with its searches and consumers section; THE ATTEMPT, its runs read back and each declaration's landing; THE MERGE of the split and the open
branch; THE HYPOTHESES H1-H4; the prompts and the author's word; the next act. No mirror export is ruled this act.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept branches at the
### remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and writes data/b669_closing.txt
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
LOCAL = [('SIDE-explicit-formula', 'chi-li-b669', 'the converse, open at V4 and V5, unmerged'),
         ('SIDE-explicit-formula', 'chi-li-forward-b669', 'the split, merged on the runner`s gate reading'),
         ('SIDE-explicit-formula', 'push-b669-merge', 'the merge push')]
TAGS = [('SIDE-explicit-formula', 'v0.31'), ('SIDE-grh-transfer', 'v0.5.1'), ('SIDE-cosmo', 'v0.3.1'), ('SIDE-effects', 'v0.1.1'),
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
    '    (a) ### **THE NEXT ACT, (R279)(7)**: b670, the reading act as (R278)(5) orders it (the two relative-entropy questions and the',
    '        EXTERNAL-ZFR-7/8 line, relay data/b668_b670_items.txt); b671 W-ORD-EPSTEIN-BALL-WIDTH; E2 after.',
    '    (b) The converse at χ open on SIDE-explicit-formula`s branch chi-li-b669 (b804bf2): the next lemma of substance V4,',
    '        powerSum_re_le_neg_infinitely (SIDEExplicitFormula/Schema/LiConverseCfg.lean :129), V5 remainder_le (:139) beside it; V2, V3 and',
    '        V4`s two Cesàro steps DERIVES on the branch. W-ORD-LI-CONVERSE-NATIVE, its trigger "S5 DERIVES", named in the plan`s consumers section.',
    '    (c) The Li coefficient over the configuration and the forward half at χ on SIDE-explicit-formula`s main at v0.31: liCoeffCfg,',
    '        liCoeff_eq_liCoeffCfg, liCoeffCfg_summable, online_imp_liCoeffCfg_nonneg, grh_chi_imp_li_nonneg_chi, at the standard three.',
    '    (d) The ceiling sentence`s successor is not drafted: the converse did not land DERIVES ((R279)(4)).',
    '    (e) b628`s full intake bank and the navigator`s export stay local and untracked in relay data/.',
    '    (f) The act root of b669 is relay data/act_roots.txt`s last line.',
    '    (g) Branches left for the next act`s step zero: the push-b669* branches of relay and PLACE-papers; push-b669-merge and',
    '        chi-li-forward-b669 (merged) in SIDE-explicit-formula, deleted in the house form after --merged lists them, the remote branch alone in',
    '        its command and turn; chi-li-b669 kept, unmerged, at the remote; the quarantine branches and the kept kernel branches untouched.',
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


ACT = 'b669'


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
    for tool, out in (('b307_handoff_census.py', 'b669_census_closing.txt'), ('b327_faces_census.py', 'b669_faces_census_closing.txt'),
                      ('b303_pins.py', 'b669_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b669'])
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
    S = jl('b669_scores.json')
    pre, post = rd('b669_checks.txt'), rd('b669_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b669 -- THE CLOSING RECORD. ### **LANE TWO, ACT NINETY-SIX, THE RESEARCH ACT: b668 AT ITS WEIGHT; THE LI COEFFICIENT OVER THE '
         'CONFIGURATION; THE FORWARD HALF AT χ MERGED AT v0.31; THE CONVERSE PLANNED, PRICED AND ATTEMPTED ON ROUTE (P), OPEN AT THE POWER-SUM '
         'LEMMA, UNDER (R279).**',
         '=' * 104]
    sys.path.insert(0, T)
    import b669_worklist as WL
    rec_ = jl('b669_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b669_seal_hashes.json):'] + [
        '      %-26s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    cc = rd('b669_citation_check.txt')
    L += ['### THE CITATION CHECK (the gate step, before the ferry was banked; relay data/b669_citation_check.txt): ' + verdict(
        cc, r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+') + ' ; the mid-act checks ((R278)(4)): ' + '; '.join(
        re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', cc)), '']
    RL = (jl('b669_repair_lines.json').get('lines') or []) + (jl('b669_record_lines.json').get('lines') or [])
    L += ['### THE RECORD LINES ((R279)(6) the N4 repair, (R279)(1) b668 at its weight; relay data/b669_repair_lines.json, data/b669_record_lines.json): '
          + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b669_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b669_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+'), '']
    L += ['### THE PLAN ((R279)(3); relay data/b669_chi_li_plan.txt): ' + verdict(rd('b669_chi_li_plan.txt'), r'CENSUS SEARCHES \d+[^*]*'),
          '    the author`s word on the route (relay data/b669_author_answers.txt): (P), V4 generic, W-ORD-LI-CONVERSE-NATIVE named', '']
    j = jl('b669_runner_rows.json')
    L += ['### THE ATTEMPT ((R279)(4); relay data/b669_runner_rows.json, data/b669_zeta_walk.txt, data/b669_chi_li_landing.txt):']
    for r in j.get('rows') or []:
        L.append('      %-12s %s at %s ; run %s %s ; artifact sha256 %s ; memory low %s MB ; gate %s ; merged %s ; tag %s' % (
            r['kernel'][:12], r['branch'], r['ref'][:8], r['run_id'], r['conclusion'], (r['artifact_sha256'] or '-')[:16], r['mem_low'], r['gate'],
            (r.get('merged') or '-')[:8], r.get('tag') or '-'))
    L += ['    the ζ-naming walk: ' + verdict(rd('b669_zeta_walk.txt'), r'DECLARATIONS REACHED \d+ ; ζ-NAMING \d+[^*]*'),
          '    the landings: ' + verdict(rd('b669_chi_li_landing.txt'), r'DECLARATIONS \d+ ; [^*]*'), '']
    mg = jl('b669_chi_li_landing.json').get('merge') or {}
    L += ['### THE MERGE ((R279)(4), the split): %s merged alone at %s, tag %s peeled %s, the merged tree the built tree %s, sorry on main %s ; the '
          'converse`s branch %s at %s (the remote %s), unmerged' % (', '.join(n.split('.')[-1] for n in mg.get('names') or []), (mg.get('sha') or '?')[:8],
                                                                    mg.get('tag'), (mg.get('peeled') or '?')[:8], mg.get('tree_equal'),
                                                                    mg.get('sorry_on_main') or 'NONE', mg.get('open_branch'), (mg.get('open_tip') or '?')[:8],
                                                                    (mg.get('open_remote') or '?')[:8]), '']
    L += ['### THE HYPOTHESES ((R279)(4); relay data/b669_hypotheses.txt): ' + verdict(rd('b669_hypotheses.txt'), r'H1 \w+ ; H2 \w+ ; H3 \w+ ; H4 \w+'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b669_author_answers.txt): ' + verdict(rd('b669_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b669_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL:'] + ['    (%s) %s -- %s' % (k, (S.get(k) or ['?', ''])[0], (S.get(k) or ['', ''])[1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b669_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b669_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b669_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b669_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    kernel mains moved by the one merge on the hosted runner`s gate reading alone (SIDE-explicit-formula, v0.31) ; no lean or lake',
          '    run on this host ; no worktree made or removed ; b628`s local intake bank and the navigator`s export untracked ;',
          '    no identifier of the author in any outbound request, workflow file or input ; no secret added, the platform`s own token alone ;',
          '    the seat`s plain requests to github.com (its ls-remote reads, its pushes, the gh calls that dispatched the two runs and read them',
          '    and their artifacts back) the act`s only outbound calls ; the deposit route untouched, publish never called ; no shared tool edited ; FINDINGS and',
          '    OPEN_TRAILS appended ; one line appended to data/act_roots.txt as the act`s last bank step ; ERRATA, SPIRAL_MAP, README, REGISTRY,',
          '    the censuses, the pages, the map, the monograph and the companions untouched ; no bench number in a keystone', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b669_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
