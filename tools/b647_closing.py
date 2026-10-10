# -*- coding: utf-8 -*-
"""b647_closing.py -- THE CLOSING RECORD OF b647, UNDER (R257). Carried from b646_closing.py by the Write tool, its act text written for b647;
the sealed tools' hashes compared at the close and printed (OPEN_TRAILS :13307); every kernel's counts with the three classes and the generated
rule's misses; every sorry on every kernel's main by file and line, in full (the author's answer at Component 2, (ii)); the navigator's
UNDERSTATES, OVERREACHES and UNLICENSED rows in full ((R257)(3)); v4 sent as a file with the fifth reader's scores and the residue, the draft
held; the glossary block; the census columns; the watchdog's peaks and the next act, each read from its bank.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept branches at the
### remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and writes data/b647_closing.txt
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
    '    (a) ### **THE NEXT ACT, (R257)(7), THE AUTHOR`S WORD PENDING**: b648, the two pages through the table, the census at v0.8, and the',
    '        order of the re-cuts raised to the author with the agenda`s counts per document; b650 the reading act per (R256)(6).',
    '    (b) ### **SENT TO THE AUTHOR AS A FILE**: relay data/b647_deposit_description.txt -- the description at v4, read back from the draft byte',
    '        for byte; its residue relay data/b647_desc_residue.txt. Publish is a separate word, given by the author after reading v4.',
    '    (c) ### **FOR THE AUTHOR`S RULING**: the sorries on the mains, printed above in full -- the standing rule that no sorry reaches any main',
    '        stands refuted at those lines; the twenty kernels no cluster rule places, blank for a hand placement; test_chain_page_b638.py`s',
    '        cases (4)-(7) still fail (carried from b643).',
    '    (d) ### **FOR THE NAVIGATOR**: the UNDERSTATES and OVERREACHES rows of its memory, printed above in full, to repair on the author`s word.',
    '    (e) ### **FOR THE AUTHOR`S STRIKE**: the seat`s readings in the trail record`s list.',
    '    (f) b628`s full intake bank and the navigator`s export stay local and untracked in relay data/.',
    '    (g) The act root of b647 is relay data/act_roots.txt`s last line; the next mirror carries it in MANIFEST.',
    '    (h) Branches left for the next act`s step zero, each merged: the push-b647* branches of relay and PLACE-papers; the kept kernel',
    '        branches untouched.',
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


ACT = 'b647'


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
    for tool, out in (('b307_handoff_census.py', 'b647_census_closing.txt'), ('b327_faces_census.py', 'b647_faces_census_closing.txt'),
                      ('b303_pins.py', 'b647_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b647'])
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
    S = jl('b647_scores.json')
    pre, post = rd('b647_checks.txt'), rd('b647_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b647 -- THE CLOSING RECORD. ### **LANE THREE, ACT SEVENTY-FOUR: EVERY KERNEL`S DOCSTRINGS THROUGH THE LICENSED-STATEMENT TABLE; THE '
         'NAVIGATOR`S MEMORY THROUGH THE TABLE; THE DESCRIPTION AT v4 WITH ITS GLOSSARY ENTRIES, A FIFTH READER, THE DRAFT HELD; THE WATCHDOG ON '
         'THE PROCESS TREE; THE CENSUS COLUMNS EXTENDED, UNDER (R257).**', '=' * 104]
    sys.path.insert(0, T)
    import b647_worklist as WL
    rec_ = jl('b647_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b647_seal_hashes.json):'] + [
        '      %-24s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    kt = rd('b647_table_kernels.txt').split(NL)
    L += ['### EVERY KERNEL`S DOCSTRINGS ((R257)(2) and the author`s answer; relay data/b647_table_kernels.txt):'] + [
        '    ' + l for l in kt[2:] if l.strip()] + ['']
    sc = rd('b647_sorry_census.txt').split(NL)
    L += ['### EVERY sorry ON EVERY KERNEL`S MAIN, BY FILE AND LINE, IN FULL (the author`s answer at Component 2, (ii); relay data/b647_sorry_census.txt):'] + [
        '    ' + l.strip() for l in sc if re.search(r'\| (BUILT|TRACKED ONLY) \|', l) or l.startswith('### ### **')] + ['']
    nav = jl('b647_table_navigator_memory.json')
    L += ['### THE NAVIGATOR`S MEMORY ((R257)(3); relay data/b647_table_navigator_memory.txt): ' +
          verdict(rd('b647_table_navigator_memory.txt'), r'UNITS READ \d+ ; ROWS \d+ ; NOT ROWS \d+ -- [^*]*'),
          '### ITS UNDERSTATES, OVERREACHES AND UNLICENSED ROWS, IN FULL, FOR THE NAVIGATOR (who repairs its own files on the author`s word):']
    for r in nav.get('rows') or []:
        if r['verdict'] != 'MATCHES':
            L += ['  %s %s (%s)' % (r['id'], r['verdict'], r['file']), '      STATED:   ' + r['stated'], '      LICENSED: ' + r['licensed'],
                  '      CITED:    ' + '; '.join(r['cited']), '      ACTION:   ' + r['action']]
    L += ['']
    DJ, CP, Z = jl('b647_deposit_description.json'), jl('b647_reader_d5_compare.json'), jl('b647_zenodo.json')
    L += ['### THE DESCRIPTION AT v4 ((R257)(4)): %s bytes against v3`s %s, sha256 %s ; the glossary block %s ; the composer`s edit tests %s ; the '
          'fifth reader %s of 3 by the needles, %s of 3 by hand ; the residue %s ; the draft %s: description read back byte for byte %s, files the '
          'same %s, submitted %s -- HELD, nothing published' % (
              DJ.get('bytes'), DJ.get('v3_bytes'), (DJ.get('sha256') or '')[:16],
              verdict(rd('b647_glossary_block.txt'), r'THE BLOCK \d+ LINES, WAS \d+'), verdict(rd('b647_desc_test.txt'), r'EDIT TESTS EXIT \d+'),
              CP.get('needles'), CP.get('hand'), verdict(rd('b647_desc_residue.txt'), r'RESIDUE \d+ PASSAGES[^;]*'), WL.DRAFT,
              (Z.get('read') or {}).get('exact'), (Z.get('read') or {}).get('files_same'), (Z.get('hold') or {}).get('submitted')), '']
    L += ['### THE CENSUS COLUMNS ((R257)(6); relay data/b647_census_columns.txt): ' +
          verdict(rd('b647_census_columns.txt'), r'ROWS \d+ \(ROSTER \d+, COMPANIONS \d+, KERNELS \d+\)[^*]*'), '']
    PK = jl('b647_build_peaks.json').get('rows') or []
    L += ['### THE WATCHDOG ON THE PROCESS TREE ((R257)(5); relay data/b647_build_peaks.json): %s' % (
        '; '.join('%s driver %s MB, tree %s MB, host low %s MB' % (r.get('module'), r.get('driver_peak'), r.get('tree_peak'), r.get('host_low'))
                  for r in PK) or 'no run'), '']
    L += ['    ' + l for l in rd('b647_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b647_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b647_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b647_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b647_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel source touched ; no edition, page or census re-cut ; no lean call after the seal ; no worktree made or removed ; b628`s '
          'local intake bank and the navigator`s export untracked ; helper readers of this session read the kernels` docstrings and the '
          'navigator`s memory from banked briefs, writing to the scratchpad alone ; no identifier of the author in any outbound request beyond '
          'the record`s own metadata, the seat`s plain requests to github.com (its ls-remote reads and its pushes) within that rule ; the '
          'draft`s description replaced by the deposit route, read back and held, publish never called ; two entries appended to '
          'data/glossary.txt and one line to data/act_roots.txt as the act`s last bank step ; ERRATA, SPIRAL_MAP, README, REGISTRY, the census, '
          'the pages, the map, the monograph and the companions untouched', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b647_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
