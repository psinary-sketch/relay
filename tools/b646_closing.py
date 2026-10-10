# -*- coding: utf-8 -*-
"""b646_closing.py -- THE CLOSING RECORD OF b646, UNDER (R256). Carried from b645_closing.py, its act text written for b646; the sealed tools'
hashes compared at the close and printed (OPEN_TRAILS :13307); the seven companions' counts with their OVERREACHES and UNLICENSED rows in full
for the author ((R256)(3)), the MET entry's move, v3 sent as a file with the fourth reader's scores and the residue, the draft held, the
seat's memory table and its repairs, the run beneath the hold and the next act, each read from its bank.

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept branches at the
### remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and writes data/b646_closing.txt
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
COMPANIONS = ('Exhaustive_Enumeration', 'Which_Structure_Confines', 'Spectral_Inertness', 'Seven_Mechanism_Classes', 'Third_Identity_Element',
              'Silence_of_Foundations', 'ONE_PAGE_PROOF')


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
    '    (a) ### **THE NEXT ACT, (R256)(8), THE AUTHOR`S WORD PENDING**: b647, the other kernels` docstrings by the generated rule; the',
    '        navigator`s memory through the table (its export at relay data/b647_navigator_memory.txt, local and untracked, b647`s input); then',
    '        the pages; the re-cuts where the author names them.',
    '    (b) ### **SENT TO THE AUTHOR AS A FILE**: relay data/b646_deposit_description.txt -- the description at v3, read back from the draft byte',
    '        for byte; its residue relay data/b646_desc_residue.txt (six passages, not repaired this act).',
    '    (c) ### **FOR THE AUTHOR`S RULING**: test_chain_page_b638.py`s cases (4)-(7) still fail (carried from b643); test_elab_reader_b634',
    '        RUN-BENEATH-HOLD at step zero (W-ORD-HOLD-FOOTPRINT entered and priced at b645).',
    '    (d) ### **FOR THE AUTHOR`S STRIKE**: the seat`s readings in the trail record`s list; the seat-memory rule (relay',
    '        data/b646_seat_memory_rule.txt); the outsiders as b645 printed them.',
    '    (e) b628`s full intake bank stays local and untracked in relay data/; its digest is in b628`s summary bank.',
    '    (f) The act root of b646 is relay data/act_roots.txt`s last line; the next mirror carries it in MANIFEST.',
    '    (g) Branches left for the next act`s step zero, each merged: the push-b646* branches of relay and PLACE-papers; the kept kernel',
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


ACT = 'b646'


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
    for tool, out in (('b307_handoff_census.py', 'b646_census_closing.txt'), ('b327_faces_census.py', 'b646_faces_census_closing.txt'),
                      ('b303_pins.py', 'b646_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b646'])
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
    S = jl('b646_scores.json')
    pre, post = rd('b646_checks.txt'), rd('b646_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b646 -- THE CLOSING RECORD. ### **LANE THREE, ACT SEVENTY-THREE: THE EDIT-ROUTE ARM; THE SEVEN COMPANIONS THROUGH THE INTAKE FORM; THE '
         'DEPOSIT DESCRIPTION AT v3 UNDER COMPOSITION RULES, THE MET LIST WIDENED, dedekind_rhs` RE-GRADED, A FOURTH READER, THE DRAFT HELD; THE '
         'SEAT`S MEMORY THROUGH THE TABLE; THE CROSS-FIELD RESONANCES ENTRY, UNDER (R256).**', '=' * 104]
    sys.path.insert(0, T)
    import b646_worklist as WL
    rec_ = jl('b646_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b646_seal_hashes.json):'] + [
        '      %-24s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    fmt = lambda c: ' ; '.join('%s %d' % (k, c.get(k, 0)) for k in ('MATCHES', 'UNDERSTATES', 'OVERREACHES', 'UNLICENSED'))   # noqa: E731
    CJ = dict((n, jl('b646_table_%s.json' % n)) for n in COMPANIONS)
    tot = {}
    for j in CJ.values():
        for k, v in (j.get('counts') or {}).items():
            tot[k] = tot.get(k, 0) + v
    L += ['### THE SEVEN COMPANIONS THROUGH THE INTAKE FORM ((R256)(3); tools/licensed_table.py; relay data/b646_table_<companion>.txt):'] + [
        '      %-26s %4d claims ; %s' % (n, len(j.get('rows') or []), fmt(j.get('counts') or {})) for n, j in CJ.items()] + [
        '      %-26s %4d claims ; %s' % ('ALL SEVEN', sum(len(j.get('rows') or []) for j in CJ.values()), fmt(tot)), '']
    L += ['### THE COMPANIONS` ROWS READING OVERREACHES OR UNLICENSED, IN FULL, FOR THE AUTHOR ((R256)(3) and the ferry`s Component 2):']
    for n, j in CJ.items():
        for r in sorted(j.get('rows') or [], key=lambda x: x['line']):
            if r['verdict'] in ('OVERREACHES', 'UNLICENSED'):
                L += ['  %s :%d %s [%s, stated as %s%s] "%s"' % (n, r['line'], r['verdict'], r['grade'], r['stated_as'],
                                                               (', ' + r['terminal']) if r['terminal'] else '', r['stated']),
                      '      ACTION %s' % r['action']]
    L += ['']
    RG = jl('b646_regrade.json').get('moves') or []
    L += ['### THE MET LIST AND THE RE-GRADE ((R256)(4)(d); relay data/b646_regrade.txt, data/b646_table_diff.txt):'] + [
        '      %s -- %s : %s -> %s' % (m['part'][:60], m['name'], ' / '.join(m['before']), ' / '.join(m['after'])) for m in RG] + [
        '      ' + verdict(rd('b646_table_diff.txt'), r'ROWS MOVED \d+ ; ADDED \d+ ; GONE \d+ ; GRADE MOVED \d+'), '']
    DJ, CP, Z = jl('b646_deposit_description.json'), jl('b646_reader_d4_compare.json'), jl('b646_zenodo.json')
    L += ['### THE DESCRIPTION AT v3 ((R256)(4)): %s bytes against v2`s %s, sha256 %s ; the fourth reader %s of 3 by the needles, %s of 3 by hand ; '
          'the residue %s ; the draft %s: description read back byte for byte %s, files the same %s, submitted %s -- HELD, nothing published' % (
              DJ.get('bytes'), DJ.get('v2_bytes'), (DJ.get('sha256') or '')[:16], CP.get('needles'), CP.get('hand'),
              verdict(rd('b646_desc_residue.txt'), r'RESIDUE \d+ PASSAGES[^;]*'), WL.DRAFT, (Z.get('read') or {}).get('exact'),
              (Z.get('read') or {}).get('files_same'), (Z.get('hold') or {}).get('submitted')), '']
    MJ = jl('b646_table_seat_memory.json')
    L += ['### THE SEAT`S MEMORY THROUGH THE TABLE ((R256)(5) and the author`s answer; relay data/b646_table_seat_memory.txt):',
          '      ' + verdict(rd('b646_table_seat_memory.txt'), r'FILES \d+ ; UNITS READ \d+ ; ROWS \d+ ; NOT ROWS \d+ -- [^*]*'), '']
    BW = jl('b646_build_watch.json').get('rows') or []
    L += ['### THE HOLD: AT STEP ZERO %s' % ('; '.join('%s lows %s MB, RUN-BENEATH-HOLD, named' % (r['module'], r['lows']) for r in BW) or 'none'), '']
    L += ['    ' + l for l in rd('b646_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b646_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b646_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b646_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b646_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel source touched ; no edition, page or census re-cut ; the E0 rule`s MET list one line ; no lean call after the seal ; no '
          'worktree made or removed ; b628`s local intake bank and the navigator`s export untracked ; fourteen helper readers of this session '
          'read the seat`s memory from one brief, writing to the scratchpad alone ; no identifier of the author in any outbound request beyond '
          'the record`s own metadata, the seat`s plain requests to github.com (its ls-remote reads and its pushes) within that rule ; the '
          'draft`s description replaced by the deposit route, read back and held, publish never called ; one line appended to '
          'data/act_roots.txt as the act`s last bank step ; ERRATA, SPIRAL_MAP, README, REGISTRY, the census, the pages, the map, the '
          'monograph and the companions untouched', '']
    L += ['### THE OUTSIDERS ((R256)(7)): AS b645 READ THEM (relay data/b645_outsider_roster.txt), the author`s strike at any closing replacing a '
          'reading; the chain not widened by the seat.', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b646_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
