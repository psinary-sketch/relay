# -*- coding: utf-8 -*-
"""b648_closing.py -- THE CLOSING RECORD OF b648, UNDER (R258). Carried from b647_closing.py by the Write tool, its act text written for b648;
the sealed tools' hashes compared at the close and printed (OPEN_TRAILS :13307); the 37 sorry lines with their classification, entry date and
repair, in full; the two pages through the table before and after re-emission, the template repairs, the page arms and the frozen control; the
census at v0.8, the unplaced kernels under the author's word and the second reader; the h2 row; the re-cut order with the author's word; the
next act, each read from its bank.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept branches at the
### remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and writes data/b648_closing.txt
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
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']   # ### (R258)(2): the branches sorry-quarantine-<kernel>, pushed
RESTATE = [('SIDE-lv-conservation', 'b648-restate-SIDE-lv-conservation'), ('SIDE-effects', 'b648-restate-SIDE-effects')]   # ### local, unmerged
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


def carried(next_act):
    return [
        '    (a) ### **THE NEXT ACT, BY THE AUTHOR`S WORD ON THE RE-CUT ORDER** (relay data/b648_author_answers.txt): %s; b650 the reading act' % next_act,
        '        per (R256)(6).',
        '    (b) ### **FOR THE AUTHOR`S RULING**: the four RESTATED lines stand on their mains, their restatements on local branches unmerged while',
        '        their builds fall beneath the hold, so G-NO-SORRY-MAIN fails at the close for them; the three page rows held as data (glossary',
        '        entry 65 on both pages, the χ list`s backmatter sentence); the h2 docstring`s re-cut proposed (W-ORD-LV-H2-DOCSTRING); the',
        '        sixteen kernels the census leaves blank in cluster, fourteen split and two named by no keystone.',
        '    (c) test_chain_page_b638.py`s cases (4)-(7) still fail (carried from b643).',
        '    (d) b628`s full intake bank and the navigator`s export stay local and untracked in relay data/; the navigator repairs its memory',
        '        outside any act ((R258)(8)).',
        '    (e) The act root of b648 is relay data/act_roots.txt`s last line; the next mirror carries it in MANIFEST.',
        '    (f) Branches left for the next act`s step zero: the push-b648* branches of relay and PLACE-papers, each merged; in SIDE-kernel and',
        '        SIDE-lv-conservation the quarantine branches sorry-quarantine-<kernel> (pushed, kept) and the local b648-quarantine-* and',
        '        push-b648-quarantine work branches, merged; the local b648-restate-* branches, unmerged; the kept kernel branches untouched.',
        '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
        '    (h) The closing reads each repository`s remote refs once (the standing line at OPEN_TRAILS :12703).',
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


ACT = 'b648'


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
    for tool, out in (('b307_handoff_census.py', 'b648_census_closing.txt'), ('b327_faces_census.py', 'b648_faces_census_closing.txt'),
                      ('b303_pins.py', 'b648_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b648'])
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
    for k in QUARANTINE:
        p, b = 'D:/' + k, 'sorry-quarantine-' + k
        loc = g(p, 'rev-parse', 'refs/heads/' + b)
        rem = remote_refs(p).get('refs/heads/' + b, '')
        heads.append('      %-32s local %s ; remote %s ; %s (the quarantine)' % (b[:32], loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    for k, b in RESTATE:
        heads.append('      %-32s local %s ; at the remote %s (the restatement, unmerged)' % (
            b[:32], g('D:/' + k, 'rev-parse', 'refs/heads/' + b)[:12], 'yes' if ('refs/heads/' + b) in remote_refs('D:/' + k) else 'no'))
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
    S = jl('b648_scores.json')
    pre, post = rd('b648_checks.txt'), rd('b648_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b648 -- THE CLOSING RECORD. ### **LANE THREE, ACT SEVENTY-FIVE: THE SORRY LINES CLASSIFIED FOR THE AUTHOR`S WORD; THE TWO PAGES THROUGH '
         'THE TABLE AND RE-EMITTED; THE KEYSTONE CENSUS AT v0.8; THE h2 ROW; THE RE-CUT ORDER TO THE AUTHOR, UNDER (R258).**', '=' * 104]
    sys.path.insert(0, T)
    import b648_worklist as WL
    import b648_record as REC
    rec_ = jl('b648_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b648_seal_hashes.json):'] + [
        '      %-24s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    cl = jl('b648_sorry_classification.json').get('rows') or []
    L += ['### THE 37 SORRY LINES, EACH WITH ITS CLASSIFICATION BY THE AUTHOR`S WORD AND ITS ENTRY DATE, IN FULL ((R258)(2); relay '
          'data/b648_sorry_classification.txt):'] + [
        '    %-22s %s:%d  %-11s entered %s  %s' % (r['kernel'], r['file'], r['line'], r['proposed'], r['entered'], (r.get('decl') or '')[:60]) for r in cl] + [
        '    ' + verdict(rd('b648_sorry_repairs.txt'), r'QUARANTINED \d+, MERGED[^*]*'), '']
    tp, ta = jl('b648_table_pages.json').get('rows') or [], jl('b648_table_pages_after.json').get('rows') or []
    L += ['### THE TWO PAGES THROUGH THE TABLE ((R258)(3)): before, relay data/b648_table_pages.txt -- %s ; after re-emission, relay '
          'data/b648_table_pages_after.txt -- %s' % (verdict(rd('b648_table_pages.txt'), r'\d+ ROWS: [^*]*'), verdict(rd('b648_table_pages_after.txt'), r'\d+ ROWS: [^*]*')),
          '    the template repairs: relay b42db0ce (the table`s grade beside E0), ef4e5a2a (the χ-leg row), 87d3e6b9 (both gated on a node '
          'list`s mark, never UNGRADED); the page arms and the frozen control: ' + verdict(rd('b648_page_arms_c2.txt'), r'PAGE ARMS PASSING : \d of 2') +
          ' ; ' + verdict(rd('b648_page_arms_c2.txt'), r'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA PASSING : \d of 2'),
          '    the rows left non-MATCHES after re-emission:'] + [
        '      %s %s -- %s' % (r['id'], r['verdict'], r['licensed'][:200]) for r in ta if r['verdict'] != 'MATCHES'] + ['']
    cmp_ = jl('b648_reader_compare.json')
    L += ['### THE CENSUS AT v0.8 ((R258)(4); PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_8.md): ' +
          verdict(rd('b648_edition_diff.txt'), r'HUNKS \d+ \([^)]*\)[^*]*'),
          '    the unplaced kernels under the author`s word: ' + verdict(rd('b648_kernel_cites.txt'), r'KERNELS \d+: PLACED[^*]*'),
          '    the second reader (C:\\reader_b648): %s of 2 by the needles, %s of 2 by hand' % (cmp_.get('needles'), cmp_.get('hand')), '']
    L += ['### THE h2 ROW ((R258)(5); relay data/b648_h2_row.txt): ' + verdict(rd('b648_h2_row.txt'), r'ONE ROW, [^*]*'),
          '    the re-cut proposed, not applied: ' + REC.H2_RECUT, '']
    L += ['### THE RE-CUT ORDER ((R258)(6); relay data/b648_recut_order.txt): ' + verdict(rd('b648_recut_order.txt'), r'DOCUMENTS \d+ ;[^*]*'),
          '    the author`s word: %s' % REC._next_act(), '']
    L += ['    ' + l for l in rd('b648_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b648_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b648_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b648_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b648_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    kernel source touched after the author`s answer alone, on branches, the quarantines merged by push_gated.sh ; no lean call after '
          'the seal ; no worktree made or removed ; b628`s local intake bank and the navigator`s export untracked ; no identifier of the author '
          'in any outbound request, the seat`s plain requests to github.com (its ls-remote reads and its pushes) within that rule ; the deposit '
          'route untouched, the draft held at v4, publish never called ; the two pages re-emitted, the census written at v0.8 beside v0.7.1, '
          'tools/chain_page.py`s templates repaired, two node lists written, one line appended to data/act_roots.txt as the act`s last bank '
          'step ; ERRATA, SPIRAL_MAP, README, REGISTRY, the glossary, the map, the monograph and the companions untouched', '']
    L += ['### CARRIED FORWARD.'] + carried(REC._next_act()) + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b648_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
