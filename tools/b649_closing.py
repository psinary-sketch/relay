# -*- coding: utf-8 -*-
"""b649_closing.py -- THE CLOSING RECORD OF b649, UNDER (R259). Carried from b648_closing.py by the Write tool, its act text written for b649;
the sealed tools' hashes compared at the close and printed (OPEN_TRAILS :13307); the three arms' opening runs with the findings of G-AXIOM-CLAIM
and G-MODULE-HEADER printed in full ((R259)(2)); the legacy maps; the lv-conservation build measured with its price; the name; the description
at v5, the sixth reader and the draft held; the next act, each read from its bank.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept branches at the
### remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and writes data/b649_closing.txt
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
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']   # ### b648's branches sorry-quarantine-<kernel>, each carrying its legacy map at b649
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


CARRIED = [
    '    (a) ### **THE NEXT ACT, (R259)(8)**: b650, the reading act per (R256)(6): no build, no deposit, no seal; the cross-field resonances entry',
    '        read against the corpus; a same-season-last-year bank from what the navigator and the author supply; the author`s word on which',
    '        questions have grown triggers. The re-cuts begin at b651 in the order the author gave at b648`s closing.',
    '    (b) ### **SENT TO THE AUTHOR AS A FILE**: relay data/b649_deposit_description.txt -- the description at v5, read back from the draft',
    '        byte for byte; its residue relay data/b649_desc_residue.txt. Publish is a separate word.',
    '    (c) ### **FOR THE AUTHOR`S RULING**: the findings of G-AXIOM-CLAIM and G-MODULE-HEADER printed above, rows of the licensed-statement',
    '        table to come; G-NO-SORRY-MAIN failing on the four RESTATED lines while their builds stand beneath the hold, the host`s price',
    '        written on OPEN_TRAILS (W-ORD-LV-BUILD-HOST); test_chain_page_b638.py`s cases (4)-(7) still fail (carried from b643).',
    '    (d) b628`s full intake bank and the navigator`s export stay local and untracked in relay data/; the navigator`s repairs are its own',
    '        ((R259)(7)).',
    '    (e) The act root of b649 is relay data/act_roots.txt`s last line; the next mirror carries it in MANIFEST.',
    '    (f) Branches left for the next act`s step zero: the push-b649* branches of relay and PLACE-papers, each merged; the quarantine',
    '        branches carry their legacy maps (pushed); the local b648-restate-* branches unmerged; the kept kernel branches untouched.',
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


ACT = 'b649'


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
    for tool, out in (('b307_handoff_census.py', 'b649_census_closing.txt'), ('b327_faces_census.py', 'b649_faces_census_closing.txt'),
                      ('b303_pins.py', 'b649_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b649'])
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
        heads.append('      %-32s local %s ; remote %s ; %s (the quarantine and its legacy map)' % (b[:32], loc[:12], rem[:12],
                                                                                                   'AGREE' if loc and loc == rem else '### DIFFER'))
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
    S = jl('b649_scores.json')
    pre, post = rd('b649_checks.txt'), rd('b649_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b649 -- THE CLOSING RECORD. ### **LANE THREE, ACT SEVENTY-SIX: THREE ARMS -- NO SORRY ON MAIN, AXIOM CLAIMS AGAINST PRINTS, MODULE '
         'HEADERS AGAINST FILES; THE LEGACY MAP; THE LV-CONSERVATION BUILD MEASURED; THE POSITIVITY CLAUSE NAMED; THE DESCRIPTION AT v5; THE '
         'DRAFT HELD, UNDER (R259).**', '=' * 104]
    sys.path.insert(0, T)
    import b649_worklist as WL
    rec_ = jl('b649_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b649_seal_hashes.json):'] + [
        '      %-24s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE THREE ARMS ((R259)(2)), their opening runs:',
          '    G-NO-SORRY-MAIN (relay data/b649_no_sorry_main.txt): ' + verdict(rd('b649_no_sorry_main.txt'), r'KERNELS \d+ ;[^*]*')] + [
        '      ' + l.strip() for l in rd('b649_no_sorry_main.txt').split(NL) if re.match(r'^  SIDE-\S+ \S+\.lean:\d+', l)]
    ac = jl('b649_axiom_claim.json').get('rows') or []
    L += ['    G-AXIOM-CLAIM (relay data/b649_axiom_claim.txt): ' + verdict(rd('b649_axiom_claim.txt'), r'CLAIMS \d+ ;[^*]*'),
          '    ### ITS CONTRADICTED CLAIMS, IN FULL:']
    for r in ac:
        if r['verdict'] == 'CONTRADICTED':
            L += ['      %s %s:%d (%s, %s): %s' % (r['kernel'], r['file'], r['line'], r['block'], r['kind'], r['sentence'])]
            L += ['          %s (%s) prints %s -- %s' % (x['decl'], x['how'], x['print'], x['source']) for x in r['contradicted']]
    L += ['    ### ITS UNVERIFIABLE CLAIMS, IN FULL:'] + ['      %s %s:%d (%s, %s, covers %d): %s' % (
        r['kernel'], r['file'], r['line'], r['block'], r['kind'], r['covered'], r['sentence']) for r in ac if r['verdict'] == 'UNVERIFIABLE']
    mh = jl('b649_module_header.json').get('rows') or []
    L += ['    G-MODULE-HEADER (relay data/b649_module_header.txt): ' + verdict(rd('b649_module_header.txt'), r'HEADERS \d+ ;[^*]*'),
          '    ### ITS OVERREACHES ROWS, IN FULL:'] + (['      %s %s:%d -- %s -- %s' % (r['kernel'], r['file'], r['line'], r['name'], r['why'])
                                                        for r in mh] or ['      NONE']) + ['']
    L += ['### THE LEGACY MAP ((R259)(3)): ' + ' ; '.join(verdict(rd('b649_legacy_map_%s.txt' % k), r'README ROWS \d+ ;[^*]*') for k in QUARANTINE), '']
    L += ['### THE LV-CONSERVATION BUILD MEASURED ((R259)(4); relay data/b649_lv_build.txt): ' + verdict(rd('b649_lv_build.txt'), r'MODULES 25 ;[^*]*'),
          '    ' + verdict(rd('b649_lv_build.txt'), r'### THE PRICE: [^\n]*'), '']
    L += ['### THE NAME ((R259)(5)): the glossary`s entry the positivity clause; the pages at PLACE-papers carrying it -- ' + verdict(
        rd('b649_page_arms_c1.txt'), r'PAGE ARMS PASSING : \d of 2') + ' ; ' + verdict(rd('b649_page_arms_c1.txt'),
                                                                                         r'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA PASSING : \d of 2'), '']
    DJ, CP_, Z = jl('b649_deposit_description.json'), jl('b649_reader_compare.json'), jl('b649_zenodo.json')
    L += ['### THE DESCRIPTION AT v5 ((R259)(6)): %s bytes against v4`s %s, sha256 %s ; %s ; the sixth reader %s of 3 by the needles, %s of 3 by '
          'hand ; the residue %s ; the draft %s: description read back byte for byte %s, files the same %s, submitted %s -- HELD, nothing published' % (
              DJ.get('bytes'), DJ.get('v4_bytes'), (DJ.get('sha256') or '')[:16], verdict(rd('b649_desc_test.txt'), r'FORBIDDEN-CONTENT \d+ of \d+'),
              CP_.get('needles'), CP_.get('hand'), verdict(rd('b649_desc_residue.txt'), r'RESIDUE \d+ PASSAGES[^;]*'), WL.DRAFT,
              (Z.get('read') or {}).get('exact'), (Z.get('read') or {}).get('files_same'), (Z.get('hold') or {}).get('submitted')), '']
    L += ['    ' + l for l in rd('b649_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b649_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b649_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b649_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b649_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel main moved ; the legacy maps committed on the quarantine branches alone ; no lean call after the seal ; no worktree made or'
          ' removed ; b628`s local intake bank and the navigator`s export untracked ;'
          ' no identifier of the author in any outbound request, the seat`s plain requests to github.com (its ls-remote reads and its pushes)'
          ' and the deposit route`s two calls within that rule ; the draft`s description replaced by v5, read back and held, publish never called ;'
          ' the two pages re-emitted, tools/chain_page.py`s templates edited for the name, three glossary entries appended, two node lists'
          ' written, one line appended to data/act_roots.txt as the act`s last bank step ; ERRATA, SPIRAL_MAP, README, REGISTRY, the census,'
          ' the map, the monograph and the companions untouched', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b649_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
