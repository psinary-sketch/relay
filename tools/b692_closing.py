# -*- coding: utf-8 -*-
"""b692_closing.py -- THE CLOSING RECORD OF b692, UNDER (R302). Carried from b691_closing.py by the Write tool, its act text written for b692,
with no repair at carry time in its logic (relay data/b692_tool_repairs.txt): the remote reads one per call in sequence, an empty read re-read
alone before any row is declared (b674_rules.txt row 1); the tag rows reading a lightweight tag at its own line; each bank's verdict line and
not its title; the citation line from the banks, the mid-act check's header read in both wordings; the captures in b673's form, the head line
reading the record's capture with its branch and its tip's subject; the mirror export named from its bank. The sections this act's components
make: the record lines and the corrigendum, the arm repaired, the closure step (its commits, its runs, the closure bank, the price), the
readings (the reader's banks, its controls, CLAUSE-DOMINANCE, READFIRST-CLOSURE, SUITE-LOAD, the spec's tenth row), INSTRUMENTS and the
orders, and the kernels (SIDE-explicit-formula's main; the scratch branch deleted at the close; the face's reading and the root's banks); the
scores read from the scores bank and, for the readings that waited on a later bank, from the close's bank (data/b686_rules.txt row (1)).
`python tools/b692_closing.py dry` -- (R285)(2)'s rule row (relay data/b675_rules.txt row 1), the closing a gate step before the seal: the record
written to the scratchpad and its readings printed; the censuses run into the scratchpad; no bank of relay data/ written.
### Writes data/b692_closing.txt and the closing censuses and pins (each its own tool's output) and nothing else. The template is b612_closing.py.
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
import b692_worklist as WL   # noqa: E402

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
        'sign-window-b602', 'family-b603', 'platt-b626', 'cite-b628', 'nb-b629', 'dedekind-b631']
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
    '    (a) ### **THE NEXT ACT, (R302)(9)**: b693, the re-cut act -- the licensed table`s next document by b652`s order and b674`s tie-break, rule',
    '        (2) of data/b690_rules.txt binding; tools/push_gated.sh`s branch mode (a branch pushed alone with the capture the main and tag modes',
    '        have) as a carry-time repair on the author`s word at (R302)(3)(b)`s prompt, closing b691`s (d).',
    '    (b) b694, the research act: W-ORD-EPSTEIN-COUNT-LEAN (OPEN_TRAILS :14892, its trigger read as met) or a candidate priced in relay',
    '        data/b692_candidates_priced.txt -- (i) the Weil-face witness at Q0, (ii) the regularity-uses bank -- on the author`s word;',
    '        SIDE-lv-conservation`s closure, the faces kernel the circuit step did not reach (relay data/b692_closure_step.txt).',
    '    (c) The orders: 12 carried at OPEN_TRAILS :15040-:15108 with their triggers as written; W-ORD-CORRESPONDENCE-BEHIND-SCOPE (OPEN_TRAILS',
    '        :15010; the next re-cut act); W-ORD-STATUS-CELLS at the next re-cut act`s step zero.',
    '    (d) The faces page`s header tag v0.26 = 82550e4 carried to the next regeneration; the residues of b691 (relay data/b691_cut.txt R-1 to',
    '        R-4, R-K1) carried as b691`s closing names them.',
    '    (e) b628`s full intake bank, the navigator`s export, b671`s uncompressed points file and b681`s units file stay local and untracked.',
    '    (f) The act root of b692 is relay data/act_roots.txt`s last line, chained from b691`s root; the mirror export carries it in MANIFEST.',
    '    (g) Branches left for the next act`s step zero: the push-b692* branches of relay and PLACE-papers; SIDE-explicit-formula`s',
    '        push-b692-closure, push-b692-closure-2 and push-b692-closure-3 (local, each merged); circuit-shorts-control-b692 deleted at this',
    '        act`s close by name, local and remote, one command each.',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
    '    (i) The defects (a)-(k) for the next ruling, (i) the ruled exception and (j)-(k) the navigator`s for the author`s strike.',
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


ACT = 'b692'
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
    cc, cj, dl = rd('b692_citation_check.txt'), jl('b692_citation_check.json'), rd('b692_defects.txt')
    head = verdict(cc, r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+')
    misses = cj.get('misses') or []
    needles = re.findall(r"^### \(R278\)\(4\) THE MID-ACT CHECK \([^)]*\): the (?:navigator`s )?answer carrying '([^']*)'", cc, re.M)
    figs = re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', cc)
    nav = re.findall(r"^    \(([a-z]'?)\) THE NAVIGATOR'S", dl, re.M)
    return ('%s ; the misses as the bank lists them: %d (%s) ; the answers checked ((R278)(4)), by their needles: %s, the prints %s ; entered as '
            'the defects bank letters them: the navigator`s %s' % (
                head, len(misses), '; '.join(m[:60] for m in misses) or 'NONE', '; '.join(needles) or 'NONE', '; '.join(figs) or 'NONE',
                ', '.join('(%s)' % x for x in nav) or 'NONE'))


def mirror_line():
    j = jl('b692_mirror.json')
    if not j:
        return '### TO BE BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH (the b670 form, mirror-refresh-2026-10-19-b692.zip)'
    return '%s ; %d bytes ; sha256 %s ; MANIFEST md5 %s ; entries %d ; %s ; %s' % (
        j.get('zip'), j.get('bytes', 0), (j.get('zip_sha256') or '')[:16], j.get('manifest_md5'), j.get('entries', 0), j.get('root_line') or '### NO ROOT LINE',
        'CLEAN ON ALL THREE CLAUSES' if j.get('clean') else '### NOT CLEAN')


def scores_at_close():
    S, C = jl('b692_scores.json'), jl('b692_scores_close.json')
    out = {}
    for ks in SCORE_KEYS:
        for k in ks:
            s = S.get(k) or ['?', '']
            c = C.get(k)
            out[k] = (c, 'close') if (s[0] == 'PENDING' and c) else (s, 'record')
    return out


def main():
    for tool, out in (('b307_handoff_census.py', 'b692_census_closing.txt'), ('b327_faces_census.py', 'b692_faces_census_closing.txt'),
                      ('b303_pins.py', 'b692_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b692'])
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
    for b in KEPT:
        loc = g('D:/SIDE-explicit-formula', 'rev-parse', 'refs/heads/' + b)
        rem = remote_refs('D:/SIDE-explicit-formula').get('refs/heads/' + b, '')
        heads.append('      %-32s local %s ; remote %s ; %s (kept)' % (b, loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    sl = g('D:/SIDE-explicit-formula', 'branch', '--list', WL.SHORTS_BRANCH)
    sr = remote_refs('D:/SIDE-explicit-formula').get('refs/heads/' + WL.SHORTS_BRANCH, '')
    heads.append('      %-32s local %s ; remote %s ; %s (the scratch branch, merged at no point, deleted at the close by name)' % (
        WL.SHORTS_BRANCH, sl or 'GONE', sr[:12] or 'GONE', 'DELETED' if not sl and not sr else '### STANDS'))
    sb, sm, st = g(SEC, 'rev-parse', 'refs/heads/' + SEC_BRANCH), g(SEC, 'rev-parse', 'main'), g(SEC, 'rev-parse', SEC_TAG + '^{commit}')
    srt, skind = remote_tag(SEC, SEC_TAG)
    heads.append('      %-32s local %s ; %s peeled %s, at the remote %s (%s) ; main %s (unmoved by this act) ; %s (kept, local)' % (
        SEC_BRANCH, sb[:12], SEC_TAG, st[:12], srt[:12], skind, sm[:12], 'AGREE' if sb and sb == st == srt else '### DIFFER'))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED, NOT WRITTEN BY THIS ACT' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?'))
    SC = scores_at_close()
    pre, post = rd('b692_checks.txt'), rd('b692_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b692 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND NINETEEN, THE RESEARCH ACT: b691 AT ITS WEIGHT; ITS POST-ROOT ITEMS BY '
         'CORRIGENDUM; THE SUITE-PARTS ARM REPAIRED; THE DEPENDENCY-CIRCUIT READING BUILT AND RUN; CLAUSE-DOMINANCE READ; THE TRIAGE RAISED BY '
         'CLASS, UNDER (R302).**',
         '=' * 104]
    rec_ = jl('b692_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b692_seal_hashes.json; the repaired '
          'rule arms and the reader among them):'] + [
        '      %-30s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step at step zero; relay data/b692_citation_check.txt): ' + citation_line(), '']
    RL = jl('b692_record_lines.json').get('lines') or []
    CL = jl('b692_corrigendum_landing.json').get('lines') or []
    OL = jl('b692_orders_lines.json').get('lines') or []
    L += ['### THE RECORD LINES ((R302)(1)-(2), (4); relay data/b692_record_lines.json, data/b692_corrigendum_landing.json, '
          'data/b692_orders_lines.json): ' + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL + CL)
          + (' ; OPEN_TRAILS.md :%s-:%s (%d entries)' % (OL[0].get('line'), OL[-1].get('line'), len(OL)) if OL else ''), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b692_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b692_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+') + ' ; THE CLOSING`S DRY RUN (relay data/b675_rules.txt row 1): ' + verdict(
        rd('b692_reg_gate.txt'), r'THE CLOSING DRY-RUN STEP : [A-Z ]+'), '']
    L += ['### THE CORRIGENDUM AND THE ARM ((R302)(2)): the corrigendum (relay data/b692_corrigendum.txt): ' + vline(rd('b692_corrigendum.txt')),
          '    the arm`s repair (relay data/b692_parts_after.txt): ' + vline(rd('b692_parts_after.txt')),
          '    the rule (relay data/b692_rules.txt): row (1), a commit made after the seal that fails an arm is left as it stands', '']
    L += ['### THE CLOSURE STEP ((R302)(3)(a); relay data/b692_closure_step.txt): ' + vtail(rd('b692_closure_step.txt')),
          '    the prints (relay data/b692_prints_SIDE-explicit-formula.txt): ' + vline(rd('b692_prints_SIDE-explicit-formula.txt')),
          '    the closure bank (relay data/%s): ' % WL.CLOSURE_BANK.replace('.jsonl.gz', '_hashes.txt') + vline(rd(WL.CLOSURE_BANK.replace('.jsonl.gz', '_hashes.txt'))), '']
    L += ['### THE READINGS ((R302)(3)(b)-(d)): the reading (relay data/%s): ' % WL.READING_BANK + vline(rd(WL.READING_BANK)),
          '    the bars (relay data/b692_circuit_bars.txt): ' + vline(rd('b692_circuit_bars.txt')),
          '    the controls (relay data/b692_circuit_controls.txt): ' + vline(rd('b692_circuit_controls.txt')),
          '    the shorts branch (relay data/b692_circuit_shorts_branch.txt): ' + vline(rd('b692_circuit_shorts_branch.txt')),
          '    CLAUSE-DOMINANCE (relay data/b692_circuit_dominance.txt): ' + vline(rd('b692_circuit_dominance.txt')),
          '    READFIRST-CLOSURE (relay data/b692_readfirst_diff.txt): ' + vline(rd('b692_readfirst_diff.txt')),
          '    SUITE-LOAD (relay data/b692_suite_load.txt): ' + vline(rd('b692_suite_load.txt')),
          '    the spec (relay data/b692_circuit_spec.txt): ' + vtail(rd('b692_circuit_spec.txt')), '']
    L += ['### INSTRUMENTS AND THE ORDERS ((R302)(3)(e), (4)): INSTRUMENTS (relay data/b692_instruments_diff.txt): ' + vline(rd('b692_instruments_diff.txt')),
          '    the triage by class (relay data/b692_triage_counts.txt): ' + vline(rd('b692_triage_counts.txt')),
          '    the candidates priced ((R302)(5); relay data/b692_candidates_priced.txt): ' + vtail(rd('b692_candidates_priced.txt')), '']
    L += ['### THE KERNELS (SIDE-explicit-formula`s main written by the closure step alone, no tag; the scratch branch deleted at the close):',
          '    the face`s reading of the kernels (relay data/b692_kernels_face.json): %d kernels read before the seal' % len(
              (jl('b692_kernels_face.json').get('kernels') or {})),
          '    the root`s banks before the root (relay data/b692_root_banks.txt): ' + (
              vline(rd('b692_root_banks.txt')) if rd('b692_root_banks.txt') else 'TO BE READ AT THE ROOT, before it is computed'), '']
    L += ['### THE MIRROR (relay data/b692_mirror.txt, the b670 form, after the root and the last PLACE-papers push): ' + mirror_line(), '']
    L += ['### THE CARRY-TIME READING (the ferry`s Component 5; relay data/b692_tool_repairs.txt): ' + vline(rd('b692_tool_repairs.txt')),
          '    the remote reads this run: %d repositories, one call each in sequence ; empty reads re-read alone: %s' % (
              len(_REMOTE), '; '.join(REREAD) or 'NONE'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b692_author_answers.txt): ' + verdict(rd('b692_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b692_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, SC[k][0][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL (relay data/b692_scores.json, written once before the entry; a reading that waited, from relay '
          'data/b692_scores_close.json):'] + ['    (%s) %s -- %s [%s]' % (k, SC[k][0][0], SC[k][0][1], SC[k][1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b692_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b692_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b692_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+'),
                                       verdict(rd('b692_faces_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b692_faces_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b692_pins_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b692_pins_closing.txt'), encoding='utf-8').read(),
                                    r'REPOS HARD-FAILING : \d+'),
          '    kernel mains written: SIDE-explicit-formula alone, the closure step`s three commits ccec1ba, 59a867c and 4313875 (CircuitClosure.lean',
          '    and the workflow`s closure step), no source module, no tag ; the scratch branch circuit-shorts-control-b692 (5866ff2) pushed alone on',
          '    the author`s word and deleted at the close ; the runner dispatched four times, once per tree state, each read by its run id with its',
          '    artifact`s sha256 checked first ; no lean or lake run on this host ; no worktree made or removed ; no file deleted ; the branches',
          '    (R302)(6) names deleted at step zero and the eight kernel branches on the author`s word, one per command and each its own message ;',
          '    b628`s local intake bank, the navigator`s export, b671`s uncompressed points file and b681`s units file untracked ;',
          '    no identifier of the author in any outbound request or workflow file ; no secret added ; the seat`s plain requests to github.com (its git reads and pushes, its',
          '    four dispatches and its run and artifact reads) the act`s only outbound calls ; the deposit route untouched, publish never called ;',
          '    FINDINGS and OPEN_TRAILS appended ; INSTRUMENTS.md I-40 appended ; data/act_roots.txt and the corrigenda bank appended ;',
          '    tools/rule_arms.py the one shared tool edited, its diff banked ; no README, REGISTRY or FOUNDATIONS byte ; no faces-page byte ;',
          '    the mirror zip written outside every repository ; nothing of TECHNE or any patent written', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(OUTD, 'b692_closing_dry.txt' if DRY else 'b692_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    if DRY:
        print('  ### THE CLOSING DRY-RUN, its readings (written to the scratchpad, %s):' % p)
        for l in L:
            if l.startswith(('b692 closed', '### THE', '    the', '      SIDE-explicit-formula', '      ' + WL.SHORTS_BRANCH)):
                print('    ' + l[:400])
        print('  ### ### **THE CLOSING DRY-RUN : READ**')
    else:
        print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
