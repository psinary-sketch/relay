# -*- coding: utf-8 -*-
"""b690_closing.py -- THE CLOSING RECORD OF b690, UNDER (R300). Carried from b689_closing.py by the Write tool, its act text written for b690,
with no repair at carry time in its logic (relay data/b690_tool_repairs.txt): the remote reads one per call in sequence, an empty read re-read
alone before any row is declared (b674_rules.txt row 1); the tag rows reading a lightweight tag at its own line; each bank's verdict line and
not its title; the citation line from the banks, the mid-act check's header read in both wordings; the captures in b673's form, the head line
reading the record's capture with its branch and its tip's subject; the mirror export named from its bank. The sections this act's components
make: the record lines with the corrigendum, the route (reading 3, its aggregate and its twelve route banks), the faces line (regenerated on
the author's word, the header's tag read) and the kernels (none written; the face's reading and the root's banks); the scores read from the
scores bank and, for the readings that waited on a later bank, from the close's bank (data/b686_rules.txt row (1)). KEPT loses strip-free-b689,
deleted at step zero under (R300)(6).
`python tools/b690_closing.py dry` -- (R285)(2)'s rule row (relay data/b675_rules.txt row 1), the closing a gate step before the seal: the record
written to the scratchpad and its readings printed; the censuses run into the scratchpad; no bank of relay data/ written.
### Writes data/b690_closing.txt and the closing censuses and pins (each its own tool's output) and nothing else. The template is b612_closing.py.
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
import b690_worklist as WL   # noqa: E402

OUTD = WL.SP if DRY else D

REPOS = ['relay', 'MY-DOwnloads/PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
         'SIDE-effects', 'SIDE-silence-principle', 'SIDE-omega-b', 'SIDE-cosmo', 'SIDE-trivium', 'SIDE-residual-bridge',
         'SIDE-yang-mills-formation', 'SIDE-substrate-cluster', 'SIDE-constants', 'SIDE-simplicity', 'SIDE-bsd-formation-transfer',
         'SIDE-bsd-multiplicity', 'SIDE-t7-topology-cmb', 'SIDE-local-cosmic-interface', 'SIDE-quaternionic-dark-sector', 'SIDE-spinor',
         'SIDE-bijection', 'SIDE-class-coupling', 'SIDE-coupling', 'SIDE-formation-arithmetic', 'SIDE-meta', 'SIDE-orchestrator',
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-grh-transfer', 'SIDE-window', 'SIDE-class-number-anomaly',
         'SIDE-li-map']
SEC, SEC_BRANCH, SEC_TAG = 'D:/SIDE-structural-error-correction', 'sec-axiom-b623', 'v0.2.2'
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603', 'platt-b626', 'cite-b628', 'nb-b629', 'dedekind-b631']
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']
TAGS = [('SIDE-explicit-formula', 'v0.34'), ('SIDE-explicit-formula', 'v0.33'), ('SIDE-li-map', 'v0.1.1'), ('SIDE-spinor', 'v0.1.2'),
        ('SIDE-spinor', 'v0.1.1'), ('SIDE-class-number-anomaly', 'v0.2.1'), ('SIDE-window', 'v0.5.2'),
        ('SIDE-trivium', 'v0.1.2'), ('SIDE-silence-principle', 'v0.2.2'), ('SIDE-bijection', 'v0.2.1'), ('SIDE-grh-transfer', 'v0.5.1'),
        ('SIDE-cosmo', 'v0.3.1'), ('SIDE-effects', 'v0.1.1'), ('SIDE-carrier-spec', 'v0.4.2'), ('SIDE-structural-error-correction', 'v0.2.3'),
        ('SIDE-lv-conservation', 'v0.13.0'), ('SIDE-global-section', 'v0.3.0'), ('SIDE-kernel', 'v1.8')]
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3'))
R3_NAMES = ('licensed', 'corr', 'ceiling', 'orders', 'methods', 'lag', 'residues', 'rules', 'arms', 'p3', 'onecopy', 'pair')


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
    '    (a) ### **THE NEXT ACT, (R300)(9)**: b691, the re-cut act -- the tie between SIDE-archimedean and SIDE-rcurve at 2 broken by b674`s rule',
    '        read from the bank at that act`s step zero, rule (2) of relay data/b690_rules.txt binding, the arms for rules (1) and (2) sorted there',
    '        by data/b683_arms_sort.txt`s rule; b692 the research act, the author`s word at b691`s ruling between W-ORD-CIRCUIT-READING and',
    '        W-ORD-EPSTEIN-COUNT-LEAN, the one not taken carried to b694.',
    '    (b) W-ORD-CIRCUIT-READING (OPEN_TRAILS, the research act after b691), specified at relay data/b690_circuit_spec.txt; no tool written.',
    '    (c) P3 at Q0 read stated by two kernel docstrings, SIDE-explicit-formula Schema/EpsteinQ0.lean :106 and :110-:111, against its status of',
    '        record (derived, not compiled; relay data/b687_p3_status.txt) -- for W-ORD-EPSTEIN-COUNT-LEAN`s act; the faces page`s header tag',
    '        v0.26 = 82550e4 (the node list`s pin line) for a regeneration with a fresh probe.',
    '    (d) The residues R3b and SIDE-li-map`s two, carried with their triggers (relay data/b690_r3_residues.txt); W-ORD-CORRESPONDENCE-CARRIED-AT;',
    '        the one-copy partner`s 13 lines under W-ORD-ONE-COPY; W-ORD-LEDGER-SPLIT-RESOLVER (on the author`s word); W-ORD-ROOT-BINARY-BANK;',
    '        W-ORD-CHAIN-PAGE-B638-CASES; `W-ORD-TABLE-SHAPE`, `W-ORD-GRADE-MOVED`, `W-ORD-PRINT-TARGETS`, `W-ORD-ABSENT-DECLARATIONS`,',
    '        `W-ORD-PROSE-PINS`.',
    '    (e) b628`s full intake bank, the navigator`s export, b671`s uncompressed points file and b681`s units file stay local and untracked.',
    '    (f) The act root of b690 is relay data/act_roots.txt`s last line, chained from b689`s root; the mirror export carries it in MANIFEST.',
    '    (g) Branches left for the next act`s step zero: the push-b690* branches of relay and PLACE-papers, each merged, for the ruling to name.',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
    '    (i) The suite split for b691 (data/b684_rules.txt row (1)): this act`s pre-run part standing-b ran 463 s, above 450 s, its act-root chain',
    '        387 s of it (data/b690_arms_prerun.txt); b691`s runs take one more foreground part, each under 540 s.',
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


ACT = 'b690'
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
    cc, cj, dl = rd('b690_citation_check.txt'), jl('b690_citation_check.json'), rd('b690_defects.txt')
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
    j = jl('b690_mirror.json')
    if not j:
        return '### TO BE BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH (the b670 form, mirror-refresh-2026-10-19-b690.zip)'
    return '%s ; %d bytes ; sha256 %s ; MANIFEST md5 %s ; entries %d ; %s ; %s' % (
        j.get('zip'), j.get('bytes', 0), (j.get('zip_sha256') or '')[:16], j.get('manifest_md5'), j.get('entries', 0), j.get('root_line') or '### NO ROOT LINE',
        'CLEAN ON ALL THREE CLAUSES' if j.get('clean') else '### NOT CLEAN')


def scores_at_close():
    """the scores bank (written once, before the entry) with the close's bank laid over the readings that waited on a later bank."""
    S, C = jl('b690_scores.json'), jl('b690_scores_close.json')
    out = {}
    for ks in SCORE_KEYS:
        for k in ks:
            s = S.get(k) or ['?', '']
            c = C.get(k)
            out[k] = (c, 'close') if (s[0] == 'PENDING' and c) else (s, 'record')
    return out


def main():
    for tool, out in (('b307_handoff_census.py', 'b690_census_closing.txt'), ('b327_faces_census.py', 'b690_faces_census_closing.txt'),
                      ('b303_pins.py', 'b690_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b690'])
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
    SC = scores_at_close()
    pre, post = rd('b690_checks.txt'), rd('b690_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b690 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND SEVENTEEN, THE READING ACT, READING 3: b689 AT ITS WEIGHT; ITS POST-SEAL '
         'FAILURE BY CORRIGENDUM; THE CENSUS; P3 ACROSS THE CORPUS; THE FACES LINE AT Q0 REGENERATED; THE DEPENDENCY-CIRCUIT READING SPECIFIED; '
         'THREE RULES BANKED, UNDER (R300).**',
         '=' * 104]
    rec_ = jl('b690_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b690_seal_hashes.json):'] + [
        '      %-30s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step at step zero; relay data/b690_citation_check.txt): ' + citation_line(), '']
    RL = jl('b690_record_lines.json').get('lines') or []
    CL = jl('b690_corrigendum_landing.json').get('lines') or []
    OL = jl('b690_orders_lines.json').get('lines') or []
    L += ['### THE RECORD LINES ((R300)(1)-(2), (4); relay data/b690_record_lines.json, data/b690_corrigendum_landing.json, data/b690_orders_lines.json): '
          + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL + CL + OL),
          '    the corrigendum (relay data/b690_corrigendum.txt): ' + vline(rd('b690_corrigendum.txt')), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b690_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b690_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+') + ' ; THE CLOSING`S DRY RUN (relay data/b675_rules.txt row 1): ' + verdict(
        rd('b690_reg_gate.txt'), r'THE CLOSING DRY-RUN STEP : [A-Z ]+'), '']
    L += ['### THE ROUTE ((R300)(3), reading 3; relay data/b690_reading3.txt, the route banks committed before it): ' + vtail(rd('b690_reading3.txt'))]
    L += ['    the %s route (relay data/b690_r3_%s.txt): %s' % (n, n, vline(rd('b690_r3_%s.txt' % n))[:300]) for n in R3_NAMES]
    L += ['    the per-arm seconds (relay data/b690_arm_seconds.txt): ' + vline(rd('b690_arm_seconds.txt')), '']
    L += ['### THE FACES LINE ((R300)(3) and the author`s two words; relay data/b690_faces_diff.txt, the page regenerated by the generator): '
          + vline(rd('b690_faces_diff.txt')),
          '    the rows bank (relay data/b689_faces_rows.txt, the diff, the tail and the amended row appended): ' + vtail(rd('b689_faces_rows.txt')),
          '    the instrument (relay data/b690_circuit_spec.txt): ' + vtail(rd('b690_circuit_spec.txt')), '']
    L += ['### THE KERNELS (none written in this act):',
          '    the face`s reading of the kernels (relay data/b690_kernels_face.json): %d kernels read before the seal' % len(
              (jl('b690_kernels_face.json').get('kernels') or {})),
          '    the root`s banks before the root (relay data/b690_root_banks.txt): ' + (
              vline(rd('b690_root_banks.txt')) if rd('b690_root_banks.txt') else 'TO BE READ AT THE ROOT, before it is computed'), '']
    L += ['### THE MIRROR (relay data/b690_mirror.txt, the b670 form, after the root and the last PLACE-papers push): ' + mirror_line(), '']
    L += ['### THE CARRY-TIME READING (the ferry`s Component 4; relay data/b690_tool_repairs.txt): ' + vline(rd('b690_tool_repairs.txt')),
          '    the remote reads this run: %d repositories, one call each in sequence ; empty reads re-read alone: %s' % (
              len(_REMOTE), '; '.join(REREAD) or 'NONE'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b690_author_answers.txt): ' + verdict(rd('b690_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b690_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, SC[k][0][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL (relay data/b690_scores.json, written once before the entry; a reading that waited, from relay '
          'data/b690_scores_close.json):'] + ['    (%s) %s -- %s [%s]' % (k, SC[k][0][0], SC[k][0][1], SC[k][1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b690_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b690_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b690_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+'),
                                       verdict(rd('b690_faces_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b690_faces_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b690_pins_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b690_pins_closing.txt'), encoding='utf-8').read(),
                                    r'REPOS HARD-FAILING : \d+'),
          '    kernel mains written: none ; no tag moved ; no runner dispatched ; no lean or lake run on this host ; no worktree made or removed ;',
          '    no file deleted ; the branches (R300)(6) names deleted at step zero, one per command and each its own message ; b628`s local intake',
          '    bank, the navigator`s export, b671`s uncompressed points file and b681`s units file untracked ;',
          '    no identifier of the author in any outbound request or workflow file ; no secret added ; the seat`s plain requests to github.com (its git reads and pushes) the',
          '    act`s only outbound calls ; the deposit route untouched, publish never called ; FINDINGS and OPEN_TRAILS appended ; the faces page',
          '    regenerated by tools/chain_page.py on the author`s word and by nothing else ; data/act_roots.txt, the corrigenda bank and b689`s faces',
          '    rows bank appended ; no shared tool edited ; no README, REGISTRY or FOUNDATIONS byte ; no Correspondence cell written ; the mirror zip',
          '    written outside every repository ; nothing of TECHNE or any patent written', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(OUTD, 'b690_closing_dry.txt' if DRY else 'b690_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    if DRY:
        print('  ### THE CLOSING DRY-RUN, its readings (written to the scratchpad, %s):' % p)
        for l in L:
            if l.startswith(('b690 closed', '### THE CITATION', '### THE ROUTE', '### THE FACES LINE', '### THE KERNELS', '### THE MIRROR', '    SIDE-',
                             '    its ', '    the ', '### THE CARRY-TIME', '### THE RECORD LINES', '### THE DRY RUN')) or ' peeled ' in l:
                print('    ' + l[:400])
        print('  ### ### **THE CLOSING DRY-RUN : %s**' % ('READ' if all(x not in NL.join(L) for x in ('### NO VERDICT LINE',)) else 'A VERDICT LINE UNREAD'))
    else:
        print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
