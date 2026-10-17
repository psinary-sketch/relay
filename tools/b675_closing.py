# -*- coding: utf-8 -*-
"""b675_closing.py -- THE CLOSING RECORD OF b675, UNDER (R285). Carried from b674_closing.py by the Write tool, its act text written for b675,
with the three repairs (R285)(2) orders at carry time against b674's defect (m) and the capture naming against its defect (l) (relay
data/b675_tool_repairs.txt):
  (1) THE TAG ROWS read a tag at the remote by its peeled line where the remote carries one and, for a lightweight tag (no peeled line), by
      its own line, which is its commit; AGREE where the remote's commit equals the local peeled commit, and the kind printed (b674 (m)(1):
      SIDE-window's lightweight v0.5.0 printed DIFFER on a tag that agrees);
  (2) THE VERDICT LINES read each bank's verdict line -- its `### ### **...**` line -- and not a pattern that meets the bank's title first
      (b674 (m)(2): the prints line printed the bank's title and lines and not its verdict);
  (3) THE CITATION LINE credits nothing by the seat's text: the misses are read from the citation bank, the answers from the mid-act checks'
      needles, and the navigator's rows as the defects bank letters them (b674 (m)(3): the parenthesis named the navigator's (a)-(d) and (e')
      as the seven misses' answers, which were (a)-(c));
  (4) THE CAPTURES named in b673's form -- `_root_push_out` the push before the root (branch push-b675-root), plain `_push_out` the record's
      push (branch push-b675), `_closing_push_out` the closing's -- and the head line reads the record's capture with its branch checked
      (b674 (l): the head line named the pre-root pushes).
Carried unchanged: the remote reads one per call in sequence, an empty read re-read alone before any row is declared (b674_rules.txt row 1).
`python tools/b675_closing.py dry` -- (R285)(2)'s rule row, the closing a gate step before the seal: the record written to the scratchpad and its
readings printed; the censuses run into the scratchpad; no bank of relay data/ written.
### Writes data/b675_closing.txt and the closing censuses and pins (each its own tool's output) and nothing else. The template is b612_closing.py.
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
import b675_worklist as WL   # noqa: E402

OUTD = WL.SP if DRY else D

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
GONE = [('SIDE-window', 'recut-window-b674'), ('SIDE-explicit-formula', 'chi-li-b669')]   # ### deleted at step zero, local and remote ((R285)(3))
TAGS = [('SIDE-window', 'v0.5.1'), ('SIDE-window', 'v0.5.0'), ('SIDE-explicit-formula', 'v0.32'), ('SIDE-grh-transfer', 'v0.5.1'),
        ('SIDE-cosmo', 'v0.3.1'), ('SIDE-effects', 'v0.1.1'), ('SIDE-carrier-spec', 'v0.4.2'), ('SIDE-structural-error-correction', 'v0.2.3'),
        ('SIDE-lv-conservation', 'v0.13.0'), ('SIDE-global-section', 'v0.3.0'), ('SIDE-kernel', 'v1.8')]
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3'), ('H1', 'H2', 'H3', 'H4', 'H5', 'H6'))


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
    """### the repair at carry (2): a bank's verdict line -- its last `### ### **...**` line -- and never a pattern that meets its title."""
    m = VLINE.findall(text or '')
    return m[-1].rstrip('.') if m else '### NO VERDICT LINE'


def verdict(text, pat):
    m = re.search(pat, text)
    return m.group(0) if m else '### NOT FOUND'


CARRIED = [
    '    (a) ### **THE NEXT ACT, (R285)(11)**: b676, the re-cut act, the document named by the tie-break rule of data/b674_rules.txt read from',
    '        the licensed table at step zero (SIDE-trivium at 5 the carried candidate), its ruling then; b677 the research act on',
    '        W-ORD-MAP-ANGLE-FORM; b680 the reading act, reading 2 of 2, the ledger split archive-3 and the census of the suite`s arms.',
    '    (b) The variant hypothesis HStrip on (-1/2, 3/2), which (3c) proves at Q0 at every height, named in relay data/b675_li_plan.txt section',
    '        7 with its question by Lean line (which of V5`s steps use the strip`s width), and ZeroConfig.strip (Zeta23/Defs.lean :142).',
    '    (c) T-COUNT, P3`s HCount Z 10 (Schema/EpsteinQ0.lean :104, :108), an ASSUMPTION of every U_n of this act: stated, not proved.',
    '    (d) The run`s orders of b672 open: `W-ORD-ONE-COPY`, `W-ORD-TABLE-SHAPE`, `W-ORD-GRADE-MOVED`, `W-ORD-PRINT-TARGETS`,',
    '        `W-ORD-ABSENT-DECLARATIONS`, `W-ORD-PROSE-PINS`; the ledger split at the b680 reading act; the nine kernels without a print bank.',
    '    (e) b628`s full intake bank, the navigator`s export and b671`s uncompressed points file stay local and untracked in relay data/.',
    '    (f) The act root of b675 is relay data/act_roots.txt`s last line.',
    '    (g) Branches left for the next act`s step zero: the push-b675* branches of relay and PLACE-papers, deleted when the next ferry`s list',
    '        carries them; the quarantine and kept kernel branches untouched.',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
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
    """### the repair at carry (1): (the remote's commit for tag t, its kind) -- the peeled line of an annotated tag, else the tag's own line,
    ### which for a lightweight tag is its commit."""
    r = remote_refs(p)
    if 'refs/tags/%s^{}' % t in r:
        return r['refs/tags/%s^{}' % t], 'annotated, peeled'
    if 'refs/tags/%s' % t in r:
        return r['refs/tags/%s' % t], 'lightweight, its own line'
    return '', '### NOT AT THE REMOTE'


ACT = 'b675'
CAPTURES = (('relay', 'relay', ROOT), ('PLACE-papers', 'pp', 'D:/MY-DOwnloads/PLACE-papers'))


def head_line(dd=None, act=ACT):
    """### (R245)(3), standing: the closing's first line, written from the act's banks; ### the repair at carry (4): each repository's record
    ### capture (b673's form: the plain `_push_out`, branch push-<act>) read with its branch and its tip, and the tip's commit subject read
    ### in the repository: a capture whose branch is not push-<act> or whose tip is not the act's record commit is printed as such, never
    ### as the record."""
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
    """### the repair at carry (3): the citation check's figures and misses from its bank, the answers from the mid-act checks' needles, the
    ### navigator's rows as the defects bank letters them -- no credit written by the seat's hand."""
    cc, cj, dl = rd('b675_citation_check.txt'), jl('b675_citation_check.json'), rd('b675_defects.txt')
    head = verdict(cc, r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+')
    misses = cj.get('misses') or []
    needles = re.findall(r"^### \(R278\)\(4\) THE MID-ACT CHECK \([^)]*\): the navigator`s answer carrying '([^']*)'", cc, re.M)
    figs = re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', cc)
    nav = re.findall(r"^    \(([a-z]'?)\) THE NAVIGATOR'S", dl, re.M)
    return ('%s ; the misses as the bank lists them: %d (%s) ; the answers checked before they were acted on ((R278)(4)), by their needles: '
            '%s, the prints %s ; entered as the defects bank letters them: the navigator`s %s' % (
                head, len(misses), '; '.join(m[:60] for m in misses) or 'NONE', '; '.join(needles) or 'NONE', '; '.join(figs) or 'NONE',
                ', '.join('(%s)' % x for x in nav) or 'NONE'))


def main():
    for tool, out in (('b307_handoff_census.py', 'b675_census_closing.txt'), ('b327_faces_census.py', 'b675_faces_census_closing.txt'),
                      ('b303_pins.py', 'b675_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b675'])
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
    for k, b in GONE:
        loc = g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b)
        rem = remote_refs('D:/' + k).get('refs/heads/' + b, '')
        heads.append('      %-34s %-21s local %s ; at the remote %s ; %s (deleted at step zero, (R285)(3))' % (
            b[:34], k[:21], loc[:12] or 'none', rem[:12] or 'none', 'GONE' if not loc and not rem else '### STANDS'))
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
    S = jl('b675_scores.json')
    pre, post = rd('b675_checks.txt'), rd('b675_checks_postpush.txt')
    L = [head_line(), '=' * 104,
         'b675 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND TWO, THE RESEARCH ACT: b674 AT ITS WEIGHT; THE KERNEL`S HYPOTHESES '
         'READ AT Q0; THE COMPOSITION BOUND INSTANTIATED AND TESTED AGAINST THE CERTIFIED ZEROS; THE CLOSING TOOL REPAIRED AT CARRY, UNDER (R285).**',
         '=' * 104]
    rec_ = jl('b675_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in WL.SEALED:
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b675_seal_hashes.json):'] + [
        '      %-26s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step, before the ferry was banked; relay data/b675_citation_check.txt): ' + citation_line(), '']
    RL = jl('b675_record_lines.json').get('lines') or []
    L += ['### THE RECORD LINES ((R285)(1); relay data/b675_record_lines.json): ' + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL)
          + ' ; the corrigenda: relay data/b675_corrigenda.txt', '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b675_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b675_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+') + ' ; THE CLOSING`S DRY RUN ((R285)(2) rule row): ' + verdict(
        rd('b675_reg_gate.txt'), r'THE CLOSING DRY-RUN STEP : [A-Z ]+'), '']
    L += ['### THE HYPOTHESES AT Q0 ((R285)(5); relay data/b675_hypotheses.txt): ' + vline(rd('b675_hypotheses.txt')), '']
    L += ['### THE PLAN ((R285)(6); relay data/b675_li_plan.txt): raised as one prompt before any sum; the navigator`s answers on the plan, the '
          'control and the constant (relay data/b675_author_answers.txt)', '']
    L += ['### THE BENCH ((R285)(7); relay data/b675_li_bench.txt): ' + vline(rd('b675_li_bench.txt')),
          '    the controls (relay data/b675_li_controls.txt): ' + vline(rd('b675_li_controls.txt')),
          '    the parts` seconds (relay data/b675_li_constants.json): %s' % dict((k, v.get('seconds')) for k, v in (jl('b675_li_constants.json').get('parts') or {}).items()),
          '    the readings, each cited to its row: relay data/b675_li_readings.txt', '']
    L += ['### THE CLOSING TOOL`S REPAIRS AT CARRY ((R285)(2); relay data/b675_tool_repairs.txt): ' + vline(rd('b675_tool_repairs.txt')),
          '    the remote reads this run: %d repositories, one call each in sequence ; empty reads re-read alone: %s' % (
              len(_REMOTE), '; '.join(REREAD) or 'NONE'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b675_author_answers.txt): ' + verdict(rd('b675_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b675_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, (S.get(k) or ['?'])[0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL:'] + ['    (%s) %s -- %s' % (k, (S.get(k) or ['?', ''])[0], (S.get(k) or ['', ''])[1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b675_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b675_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b675_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+'),
                                       verdict(rd('b675_faces_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b675_faces_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b675_pins_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b675_pins_closing.txt'), encoding='utf-8').read(),
                                    r'REPOS HARD-FAILING : \d+'),
          '    no kernel main written ; no runner dispatched ; no lean or lake run on this host ; no worktree made or removed ; no file deleted ;',
          '    the branches (R285)(3) names deleted at step zero, two of them at their remotes as the ruling names ; b628`s local intake bank, the',
          '    navigator`s export and b671`s uncompressed points file untracked ; no identifier of the author in any outbound request ; no',
          '    secret added ; the seat`s plain requests to github.com (its git reads, pushes and the two remote branch deletions) and one web',
          '    search for the Davenport-Heilbronn source (its query the theorem`s words alone) the act`s only outbound calls ; the deposit route',
          '    untouched, publish never called ; no shared tool edited ; FINDINGS and OPEN_TRAILS appended ; no README, REGISTRY or faces-page',
          '    byte ; one line appended to data/act_roots.txt as the act`s last bank step ; nothing of TECHNE or any patent written', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(OUTD, 'b675_closing_dry.txt' if DRY else 'b675_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    if DRY:
        print('  ### THE CLOSING DRY-RUN, its readings (written to the scratchpad, %s):' % p)
        for l in L:
            if l.startswith(('b675 closed', '### THE CITATION', '### THE HYPOTHESES', '### THE BENCH', '    the controls', '### THE CLOSING TOOL',
                             '### THE RECORD LINES', '### THE DRY RUN')) or ' peeled ' in l or 'deleted at step zero' in l:
                print('    ' + l[:400])
        print('  ### ### **THE CLOSING DRY-RUN : %s**' % ('READ' if all(x not in NL.join(L) for x in ('### NO VERDICT LINE',)) else 'A VERDICT LINE UNREAD'))
    else:
        print(NL.join(L[-60:]))


if __name__ == '__main__':
    main()
