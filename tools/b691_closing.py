# -*- coding: utf-8 -*-
"""b691_closing.py -- THE CLOSING RECORD OF b691, UNDER (R301). Carried from b690_closing.py by the Write tool, its act text written for b691,
with no repair at carry time in its logic (relay data/b691_tool_repairs.txt): the remote reads one per call in sequence, an empty read re-read
alone before any row is declared (b674_rules.txt row 1); the tag rows reading a lightweight tag at its own line; each bank's verdict line and
not its title; the citation line from the banks, the mid-act check's header read in both wordings; the captures in b673's form, the head line
reading the record's capture with its branch and its tip's subject; the mirror export named from its bank. The sections this act's components
make: the record lines with the order, the re-cut (the tie, the cut, the quotation search, the prints), the generator (the repair, the dry,
the behind count, the run on the author's word), EpsteinQ0, the orders and the arms, and the kernels (SIDE-rcurve and SIDE-explicit-formula
written and tagged; the face's reading and the root's banks); the scores read from the scores bank and, for the readings that waited on a
later bank, from the close's bank (data/b686_rules.txt row (1)). The tag rows take v0.34.1 and SIDE-rcurve's two; the kept branches take this
act's two cut branches.
`python tools/b691_closing.py dry` -- (R285)(2)'s rule row (relay data/b675_rules.txt row 1), the closing a gate step before the seal: the record
written to the scratchpad and its readings printed; the censuses run into the scratchpad; no bank of relay data/ written.
### Writes data/b691_closing.txt and the closing censuses and pins (each its own tool's output) and nothing else. The template is b612_closing.py.
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
import b691_worklist as WL   # noqa: E402

OUTD = WL.SP if DRY else D

REPOS = ['relay', 'MY-DOwnloads/PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
         'SIDE-effects', 'SIDE-silence-principle', 'SIDE-omega-b', 'SIDE-cosmo', 'SIDE-trivium', 'SIDE-residual-bridge',
         'SIDE-yang-mills-formation', 'SIDE-substrate-cluster', 'SIDE-constants', 'SIDE-simplicity', 'SIDE-bsd-formation-transfer',
         'SIDE-bsd-multiplicity', 'SIDE-t7-topology-cmb', 'SIDE-local-cosmic-interface', 'SIDE-quaternionic-dark-sector', 'SIDE-spinor',
         'SIDE-bijection', 'SIDE-class-coupling', 'SIDE-coupling', 'SIDE-formation-arithmetic', 'SIDE-meta', 'SIDE-orchestrator',
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-grh-transfer', 'SIDE-window', 'SIDE-class-number-anomaly',
         'SIDE-li-map', 'SIDE-rcurve']
SEC, SEC_BRANCH, SEC_TAG = 'D:/SIDE-structural-error-correction', 'sec-axiom-b623', 'v0.2.2'
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603', 'platt-b626', 'cite-b628', 'nb-b629', 'dedekind-b631', 'recut-epstein-b691']
KEPT_RCURVE = ['recut-rcurve-b691']
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']
TAGS = [('SIDE-explicit-formula', 'v0.34.1'), ('SIDE-explicit-formula', 'v0.34'), ('SIDE-rcurve', 'v0.1.1'), ('SIDE-rcurve', 'v0.1.0'),
        ('SIDE-li-map', 'v0.1.1'), ('SIDE-spinor', 'v0.1.2'), ('SIDE-class-number-anomaly', 'v0.2.1'), ('SIDE-window', 'v0.5.2'),
        ('SIDE-trivium', 'v0.1.2'), ('SIDE-silence-principle', 'v0.2.2'), ('SIDE-bijection', 'v0.2.1'), ('SIDE-grh-transfer', 'v0.5.1'),
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


VLINE = re.compile(r'^\s*### ### \*\*(.*?)\*\*\s*$', re.M)


def vline(text):
    """### b675's repair (2), carried: a bank's verdict line -- its last `### ### **...**` line -- and never a pattern that meets its title."""
    m = VLINE.findall(text or '')
    return m[-1].rstrip('.') if m else '### NO VERDICT LINE'


def vtail(text):
    """a verdict that a bank wraps over two `### ` lines: the last bold line joined from its `### ### **` opening to its `**`."""
    m = re.findall(r'(?ms)^### ### \*\*(.*?)\*\*\s*$', text or '')
    return ' '.join(m[-1].replace('###', ' ').split()).rstrip('.') if m else '### NO VERDICT LINE'


def verdict(text, pat):
    m = re.search(pat, text)
    return m.group(0) if m else '### NOT FOUND'


CARRIED = [
    '    (a) ### **THE NEXT ACT, (R301)(11)**: b692, the research act -- the author`s word at b692`s ruling between W-ORD-CIRCUIT-READING and',
    '        W-ORD-EPSTEIN-COUNT-LEAN, the one not taken carried to b694; the stale-orders triage bank (relay data/b691_orders_triage.txt, 35 orders:',
    '        11 carried, 24 discharged by a reading, none retired) raised there for the author`s word; no ledger written by it.',
    '    (b) W-ORD-CORRESPONDENCE-BEHIND-SCOPE (OPEN_TRAILS :15010; the next re-cut act after b691): the behind count to the leading clause, the 19',
    '        rows that are not generator rows brought under the generator or marked as hand cells (relay data/b691_behind.txt).',
    '    (c) The residues carried: SIDE-rcurve`s four README lines (relay data/b691_cut.txt, R-1 to R-4, the next re-cut of SIDE-rcurve or a README',
    '        pass); the SIDE-kernel row`s :301 clause, v1.8 against the carry v1.3 = 0bc21c0 (R-K1); SIDE-li-map`s two (data/b690_r3_residues.txt).',
    '    (d) The faces page`s header tag v0.26 = 82550e4 (the node list`s pin line, data/b690_nodes_zeta.txt :81; tools/chain_page.py :87-:96),',
    '        carried to the next regeneration; W-ORD-STATUS-CELLS at the next re-cut act`s step zero; W-ORD-LEDGER-SPLIT-RESOLVER (on the author`s',
    '        word); W-ORD-ROOT-BINARY-BANK; W-ORD-CHAIN-PAGE-B638-CASES; `W-ORD-TABLE-SHAPE`, `W-ORD-GRADE-MOVED`, `W-ORD-PRINT-TARGETS`,',
    '        `W-ORD-ABSENT-DECLARATIONS`, `W-ORD-PROSE-PINS`, `W-ORD-ONE-COPY`.',
    '    (e) b628`s full intake bank, the navigator`s export, b671`s uncompressed points file and b681`s units file stay local and untracked.',
    '    (f) The act root of b691 is relay data/act_roots.txt`s last line, chained from b690`s root; the mirror export carries it in MANIFEST.',
    '    (g) Branches left for the next act`s step zero: the push-b691* branches of relay and PLACE-papers; SIDE-rcurve`s push-b691-main and',
    '        push-b691-merge, SIDE-explicit-formula`s push-b691-epstein-main and push-b691-epstein-merge (local, each merged); the cut branches',
    '        recut-rcurve-b691 and recut-epstein-b691 (local and at the remote, each merged), for the ruling to name.',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
    '    (i) The defects (a)-(d) of the seat`s keeping -- shell filters on reads, a redirect, two git writes in a message twice, branch pushes',
    '        outside the push tool -- for the next ruling; G-RULE-ONE-GIT-WRITE carried failing, as the face declares.',
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


ACT = 'b691'
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
    cc, cj, dl = rd('b691_citation_check.txt'), jl('b691_citation_check.json'), rd('b691_defects.txt')
    head = verdict(cc, r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+')
    misses = cj.get('misses') or []
    needles = re.findall(r"^### \(R278\)\(4\) THE MID-ACT CHECK \([^)]*\): the (?:navigator`s )?answer carrying '([^']*)'", cc, re.M)
    figs = re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', cc)
    tested = re.findall(r'### the miss tested directly by the seat \([^)]*\): ([0-9a-f]{7}) is a commit of (SIDE-[\w-]+)', cc)
    nav = re.findall(r"^    \(([a-z]'?)\) THE NAVIGATOR'S", dl, re.M)
    return ('%s ; the misses as the bank lists them: %d (%s) ; the answers checked ((R278)(4)), by their needles: %s, the prints %s ; the '
            'commit misses tested directly: %s ; entered as the defects bank letters them: the navigator`s %s' % (
                head, len(misses), '; '.join(m[:60] for m in misses) or 'NONE', '; '.join(needles) or 'NONE', '; '.join(figs) or 'NONE',
                '; '.join('%s (%s)' % t for t in tested) or 'NONE', ', '.join('(%s)' % x for x in nav) or 'NONE'))


def mirror_line():
    j = jl('b691_mirror.json')
    if not j:
        return '### TO BE BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH (the b670 form, mirror-refresh-2026-10-19-b691.zip)'
    return '%s ; %d bytes ; sha256 %s ; MANIFEST md5 %s ; entries %d ; %s ; %s' % (
        j.get('zip'), j.get('bytes', 0), (j.get('zip_sha256') or '')[:16], j.get('manifest_md5'), j.get('entries', 0), j.get('root_line') or '### NO ROOT LINE',
        'CLEAN ON ALL THREE CLAUSES' if j.get('clean') else '### NOT CLEAN')


def scores_at_close():
    """the scores bank (written once, before the entry) with the close's bank laid over the readings that waited on a later bank."""
    S, C = jl('b691_scores.json'), jl('b691_scores_close.json')
    out = {}
    for ks in SCORE_KEYS:
        for k in ks:
            s = S.get(k) or ['?', '']
            c = C.get(k)
            out[k] = (c, 'close') if (s[0] == 'PENDING' and c) else (s, 'record')
    return out


def main():
    for tool, out in (('b307_handoff_census.py', 'b691_census_closing.txt'), ('b327_faces_census.py', 'b691_faces_census_closing.txt'),
                      ('b303_pins.py', 'b691_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b691'])
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
    for k in QUARANTINE:
        p, b = 'D:/' + k, 'sorry-quarantine-' + k
        loc = g(p, 'rev-parse', 'refs/heads/' + b)
        rem = remote_refs(p).get('refs/heads/' + b, '')
        heads.append('      %-32s local %s ; remote %s ; %s (the quarantine and its legacy map)' % (b[:32], loc[:12], rem[:12],
                                                                                                   'AGREE' if loc and loc == rem else '### DIFFER'))
    for K_, kept in (('D:/SIDE-explicit-formula', KEPT), ('D:/SIDE-rcurve', KEPT_RCURVE)):
        for b in kept:
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
    SC = scores_at_close()
    pre, post = rd('b691_checks.txt'), rd('b691_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b691 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND EIGHTEEN, THE RE-CUT ACT: b690 AT ITS WEIGHT; SIDE-rcurve RE-CUT UNDER THE '
         'QUOTATION RULE; THE CORRESPONDENCE GENERATOR REPAIRED, ITS RUN ON THE AUTHOR`S WORD, THE BEHIND COUNT BY ROW; THE EPSTEINQ0 DOCSTRINGS '
         'RE-CUT; THE STALE ORDERS TRIAGED; FOUR RULE ARMS ADDED, UNDER (R301).**',
         '=' * 104]
    rec_ = jl('b691_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b691_seal_hashes.json):'] + [
        '      %-30s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step at step zero; relay data/b691_citation_check.txt): ' + citation_line(), '']
    RL = jl('b691_record_lines.json').get('lines') or []
    OL = jl('b691_orders_lines.json').get('lines') or []
    L += ['### THE RECORD LINES ((R301)(1), (3); relay data/b691_record_lines.json, data/b691_orders_lines.json): '
          + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL + OL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b691_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b691_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+') + ' ; THE CLOSING`S DRY RUN (relay data/b675_rules.txt row 1): ' + verdict(
        rd('b691_reg_gate.txt'), r'THE CLOSING DRY-RUN STEP : [A-Z ]+'), '']
    L += ['### THE RE-CUT ((R301)(2); relay data/b691_cut.txt): ' + vline(rd('b691_cut.txt')),
          '    the tie (relay data/b691_tie.txt): ' + vline(rd('b691_tie.txt')),
          '    the quotation search (relay data/b691_quote_rcurve.txt): ' + vline(rd('b691_quote_rcurve.txt')),
          '    the prints (relay data/b691_prints_SIDE-rcurve.txt): ' + vline(rd('b691_prints_SIDE-rcurve.txt')), '']
    L += ['### THE GENERATOR ((R301)(3); relay data/b691_tool_repairs.txt rows 1-2, data/b691_correspondence_dry.txt): ' + vline(rd('b691_correspondence_dry.txt')),
          '    the planted cases (relay data/b691_gen_test.txt): ' + vline(rd('b691_gen_test.txt')),
          '    the behind count (relay data/b691_behind.txt): ' + vline(rd('b691_behind.txt'))[:400],
          '    the run on the author`s word (relay data/b691_correspondence_run.txt): ' + vline(rd('b691_correspondence_run.txt'))[:300],
          '    the snapshot and the live run (relay data/b691_gen_snapshot.txt, data/b691_gen_live.txt): ' + vline(rd('b691_gen_snapshot.txt'))
          + ' / ' + vline(rd('b691_gen_live.txt')),
          '    the pages (relay data/b691_correspondence_run_PATHS.txt, _RCURVE.txt): ' + vline(rd('b691_correspondence_run_PATHS.txt'))
          + ' / ' + vline(rd('b691_correspondence_run_RCURVE.txt')), '']
    L += ['### THE EPSTEINQ0 DOCSTRINGS ((R301)(4); relay data/b691_epstein_cut.txt): ' + vline(rd('b691_epstein_cut.txt')),
          '    the lines before the branch (relay data/b691_epstein_lines.txt): ' + vline(rd('b691_epstein_lines.txt')),
          '    the quotation search (relay data/b691_quote_epstein.txt): ' + vline(rd('b691_quote_epstein.txt')),
          '    the prints (relay data/b691_prints_SIDE-explicit-formula.txt): ' + vline(rd('b691_prints_SIDE-explicit-formula.txt')), '']
    L += ['### THE ORDERS AND THE ARMS ((R301)(5)-(6)): the triage (relay data/b691_orders_triage.txt): ' + vline(rd('b691_orders_triage.txt')),
          '    the sort (relay data/b691_arms_sort.txt): ' + vline(rd('b691_arms_sort.txt')),
          '    the arms added (relay data/b691_arms_added.txt): ' + vline(rd('b691_arms_added.txt')),
          '    the per-part seconds (relay data/b691_arm_seconds.txt): ' + vline(rd('b691_arm_seconds.txt')), '']
    L += ['### THE KERNELS (SIDE-rcurve and SIDE-explicit-formula written, each merge on the runner`s gate reading, each tag the patch step):',
          '    the face`s reading of the kernels (relay data/b691_kernels_face.json): %d kernels read before the seal' % len(
              (jl('b691_kernels_face.json').get('kernels') or {})),
          '    the root`s banks before the root (relay data/b691_root_banks.txt): ' + (
              vline(rd('b691_root_banks.txt')) if rd('b691_root_banks.txt') else 'TO BE READ AT THE ROOT, before it is computed'), '']
    L += ['### THE MIRROR (relay data/b691_mirror.txt, the b670 form, after the root and the last PLACE-papers push): ' + mirror_line(), '']
    L += ['### THE CARRY-TIME READING (the ferry`s Component 5; relay data/b691_tool_repairs.txt): ' + vline(rd('b691_tool_repairs.txt')),
          '    the remote reads this run: %d repositories, one call each in sequence ; empty reads re-read alone: %s' % (
              len(_REMOTE), '; '.join(REREAD) or 'NONE'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b691_author_answers.txt): ' + verdict(rd('b691_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b691_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, SC[k][0][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL (relay data/b691_scores.json, written once before the entry; a reading that waited, from relay '
          'data/b691_scores_close.json):'] + ['    (%s) %s -- %s [%s]' % (k, SC[k][0][0], SC[k][0][1], SC[k][1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b691_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b691_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b691_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+'),
                                       verdict(rd('b691_faces_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b691_faces_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b691_pins_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b691_pins_closing.txt'), encoding='utf-8').read(),
                                    r'REPOS HARD-FAILING : \d+'),
          '    kernel mains written: SIDE-rcurve (bb14e89 workflow, 29885e5 print list, 54c9040 merge of the cut e3df866) and SIDE-explicit-formula',
          '    (9da7bc2 print list, e5fcda7 merge of the cut c5aa058) alone ; tags made v0.1.1 and v0.34.1, none moved ; the runner dispatched four',
          '    times, once per tree state, each read by its run id with its artifact`s sha256 checked first ; no lean or lake run on this host ; no',
          '    worktree made or removed ; no file deleted ; the branches (R301)(9) names deleted at step zero, one per command and each its own',
          '    message ; b628`s local intake bank, the navigator`s export, b671`s uncompressed points file and b681`s units file untracked ;',
          '    no identifier of the author in any outbound request or workflow file ; no secret added ; the seat`s plain requests to github.com (its git reads and pushes, its',
          '    four dispatches and its run and artifact reads) the act`s only outbound calls ; the deposit route untouched, publish never called ;',
          '    FINDINGS and OPEN_TRAILS appended ; the two Correspondence pages written by tools/correspondence_gen.py alone on the author`s word ;',
          '    data/act_roots.txt appended ; the shared tools edited the three repaired, each diff banked ; no README, REGISTRY or FOUNDATIONS',
          '    byte ; no faces-page byte ; the mirror zip written outside every repository ; nothing of TECHNE or any patent written', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(OUTD, 'b691_closing_dry.txt' if DRY else 'b691_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    if DRY:
        print('  ### THE CLOSING DRY-RUN, its readings (written to the scratchpad, %s):' % p)
        for l in L:
            if l.startswith(('b691 closed', '### THE CITATION', '### THE RE-CUT', '### THE GENERATOR', '### THE EPSTEINQ0', '### THE ORDERS',
                             '### THE KERNELS', '### THE MIRROR', '    SIDE-', '    its ', '    the ', '### THE CARRY-TIME', '### THE RECORD LINES',
                             '### THE DRY RUN')) or ' peeled ' in l:
                print('    ' + l[:400])
        print('  ### ### **THE CLOSING DRY-RUN : %s**' % ('READ' if all(x not in NL.join(L) for x in ('### NO VERDICT LINE',)) else 'A VERDICT LINE UNREAD'))
    else:
        print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
