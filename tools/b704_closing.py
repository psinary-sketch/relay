# -*- coding: utf-8 -*-
"""b704_closing.py -- THE CLOSING RECORD OF b704, UNDER (R314). Carried from b703_closing.py by the Write tool, its act text written for b704:
the remote reads stored and looked up under ONE key (repo_key(), b694's repair, carried); the remote reads one per call in sequence, an empty read
re-read alone before any row is declared (b674_rules.txt row 1); the tag rows reading a lightweight tag at its own line; each bank's verdict line
and not its title; the citation line from the banks; the captures in b673's form; the defects row read from the bank (b693's repair); the head
line's prompt count the answers bank's rows plus one for the root's prompt, its defect count the defects bank's lettered rows read now (b700's
repair (9), carried). The act's sections are the corrigendum and the read rule, the faces probe, the cells, the README, the glossary, the re-cut,
the standing arms and the orders. b704 keeps no act branch on any kernel: the three branches it deleted are read absent at the close.
`python tools/b704_closing.py dry` -- (R285)(2)'s rule row (relay data/b675_rules.txt row 1), the closing a gate step before the seal: the record
written to the scratchpad and its readings printed; the censuses run into the scratchpad; no bank of relay data/ written.
`python tools/b704_closing.py defects-row <act>` -- the carried-forward defects row computed from relay data/<act>_defects.txt, printed only.
### Writes data/b704_closing.txt and the closing censuses and pins (each its own tool's output) and nothing else.
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
import b704_worklist as WL   # noqa: E402

OUTD = WL.SP if DRY else D

REPOS = ['relay', 'MY-DOwnloads/PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
         'SIDE-effects', 'SIDE-silence-principle', 'SIDE-omega-b', 'SIDE-cosmo', 'SIDE-trivium', 'SIDE-residual-bridge',
         'SIDE-yang-mills-formation', 'SIDE-substrate-cluster', 'SIDE-constants', 'SIDE-simplicity', 'SIDE-bsd-formation-transfer',
         'SIDE-bsd-multiplicity', 'SIDE-t7-topology-cmb', 'SIDE-local-cosmic-interface', 'SIDE-quaternionic-dark-sector', 'SIDE-spinor',
         'SIDE-bijection', 'SIDE-class-coupling', 'SIDE-coupling', 'SIDE-formation-arithmetic', 'SIDE-meta', 'SIDE-orchestrator',
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-grh-transfer', 'SIDE-window', 'SIDE-class-number-anomaly',
         'SIDE-li-map', 'SIDE-rcurve', 'SIDE-archimedean', 'SIDE-interfaces']
SEC, SEC_BRANCH, SEC_TAG = 'D:/SIDE-structural-error-correction', 'sec-axiom-b623', 'v0.2.2'
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603', 'platt-b626', 'cite-b628', 'nb-b629', 'dedekind-b631']
GONE = [('probe-b704', 'the faces probe`s scratch branch, deleted after its bank (the author`s word, (R314)(3))'),
        ('widening-b701', 'merged at v0.36, deleted on the author`s word ((R314)(8))'),
        ('epstein-b703', 'merged at v0.37, deleted on the author`s word ((R314)(8))')]
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']
TAGS_FIXED = [('SIDE-explicit-formula', 'v0.37'), ('SIDE-explicit-formula', 'v0.36'), ('SIDE-explicit-formula', 'v0.35'), ('SIDE-explicit-formula', 'v0.34.1'),
              ('SIDE-explicit-formula', 'v0.34'), ('SIDE-substrate-cluster', 'v0.4.1'),
              ('SIDE-substrate-cluster', 'v0.4'), ('SIDE-simplicity', 'v0.1.2'), ('SIDE-simplicity', 'v0.1.1'), ('SIDE-simplicity', 'v0.1.0'),
              ('SIDE-interfaces', 'v0.2.1'), ('SIDE-interfaces', 'v0.2'), ('SIDE-archimedean', 'v0.1.1'), ('SIDE-archimedean', 'v0.1.0'), ('SIDE-rcurve', 'v0.1.1'),
              ('SIDE-rcurve', 'v0.1.0'), ('SIDE-li-map', 'v0.1.1'), ('SIDE-spinor', 'v0.1.2'), ('SIDE-class-number-anomaly', 'v0.2.1'), ('SIDE-window', 'v0.5.2'),
              ('SIDE-trivium', 'v0.1.2'), ('SIDE-silence-principle', 'v0.2.2'), ('SIDE-bijection', 'v0.2.1'), ('SIDE-grh-transfer', 'v0.5.1'), ('SIDE-cosmo', 'v0.3.1'),
              ('SIDE-effects', 'v0.1.1'), ('SIDE-carrier-spec', 'v0.4.2'), ('SIDE-structural-error-correction', 'v0.2.3'), ('SIDE-lv-conservation', 'v0.13.0'),
              ('SIDE-lv-conservation', 'v0.10.0'), ('SIDE-global-section', 'v0.3.0'), ('SIDE-kernel', 'v1.8')]
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


def tags_now():
    """SIDE-explicit-formula's two latest tags first (v0.37, v0.36; no tag made this act), then the fixed list."""
    return TAGS_FIXED


VLINE = re.compile(r'^\s*### ### \*\*(.*?)\*\*\s*$', re.M)


def vline(text):
    m = VLINE.findall(text or '')
    return m[-1].rstrip('.') if m else '### NO VERDICT LINE'


def vtail(text):
    m = re.findall(r'(?ms)^### ### \*\*(.*?)\*\*\s*$', text or '')
    return ' '.join(m[-1].replace('###', ' ').split()).rstrip('.') if m else '### NO VERDICT LINE'


def verdict(text, pat):
    m = re.search(pat, text)
    return m.group(0) if m else '### NOT FOUND'


# ================================================================================ THE CARRIED-FORWARD DEFECTS ROW (b693's repair, carried)
def _span(letters):
    runs, cur = [], []
    for x in letters:
        if cur and len(x) == 1 and len(cur[-1]) == 1 and ord(x) == ord(cur[-1]) + 1:
            cur.append(x)
        else:
            if cur:
                runs.append(cur)
            cur = [x]
    if cur:
        runs.append(cur)
    return ', '.join('(%s)' % r[0] if len(r) == 1 else '(%s)–(%s)' % (r[0], r[-1]) for r in runs)


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def defects_row(act, item='i'):
    L = rd('%s_defects.txt' % act).split(NL)
    rows = [(DEFECT_ROW.match(l).group(1), l) for l in L if DEFECT_ROW.match(l)]
    if not rows:
        return '    (%s) The defects: ### NO LETTERED ROW IN relay data/%s_defects.txt.' % (item, act)
    ruled = [x for x, l in rows if 'A RULED EXCEPTION' in l]
    nav = [x for x, l in rows if re.match(r"^    \([a-z]'?\) THE NAVIGATOR'S", l)]
    tail = []
    if ruled:
        tail.append('%s the ruled exception%s' % (_span(ruled), '' if len(ruled) == 1 else 's'))
    if nav:
        tail.append('%s the navigator`s for the author`s strike' % _span(nav))
    return '    (%s) The defects %s for the next ruling%s.' % (item, _span([x for x, _l in rows]), (', ' + ' and '.join(tail)) if tail else '')


def carried():
    return CARRIED_FIXED[:-1] + [defects_row('b704', 'g')] + CARRIED_FIXED[-1:]


# ================================================================================ THE REMOTE READS, ONE KEY (b694's repair, carried)
_REMOTE = {}
REREAD = []


def repo_key(p):
    s = str(p).replace('\\', '/')
    m = re.match(r'^/([a-zA-Z])/(.*)$', s)
    if m:
        s = '%s:/%s' % (m.group(1), m.group(2))
    m = re.match(r'^([a-zA-Z]):/*(.*)$', s)
    if m:
        s = '%s:/%s' % (m.group(1).upper(), m.group(2))
    return s.rstrip('/')


def _ls(p):
    out = g(p, 'ls-remote', 'origin')
    return dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in out.split(NL) if '\t' in l)


def read_remotes(paths):
    for p in paths:
        if repo_key(p) not in _REMOTE:
            _REMOTE[repo_key(p)] = _ls(p)
    for p in paths:
        if 'refs/heads/main' not in _REMOTE[repo_key(p)]:
            again = _ls(p)
            REREAD.append('%s : first read empty ; re-read alone: %s' % (os.path.basename(p), 'refs read' if 'refs/heads/main' in again else '### EMPTY AGAIN'))
            _REMOTE[repo_key(p)] = again


def remote_refs(p):
    return _REMOTE.get(repo_key(p), {})


def remote_tag(p, t):
    r = remote_refs(p)
    if 'refs/tags/%s^{}' % t in r:
        return r['refs/tags/%s^{}' % t], 'annotated, peeled'
    if 'refs/tags/%s' % t in r:
        return r['refs/tags/%s' % t], 'lightweight, its own line'
    return '', '### NOT AT THE REMOTE'


ACT = 'b704'
CAPTURES = (('relay', 'relay', ROOT), ('PLACE-papers', 'pp', 'D:/MY-DOwnloads/PLACE-papers'))


def head_line(dd=None, act=ACT):
    """the closing's head line: the prompts the answers bank's rows plus one for the root's prompt; the defects the defects bank's lettered
    rows read now (b700's repair (9), carried)."""
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
    k = len(re.findall(r'^### PROMPT ', _t('%s_author_answers.txt' % act), re.M)) + 1
    d = len([l for l in _t('%s_defects.txt' % act).split(NL) if DEFECT_ROW.match(l)])
    return '%s closed: %s; %s; root %s; %d prompt%s answered; %d defect%s' % (act, ', '.join(parts), suite, root, k, '' if k == 1 else 's',
                                                                             d, '' if d == 1 else 's')


def citation_line():
    cc, cj, dl = rd('b704_citation_check.txt'), jl('b704_citation_check.json'), rd('b704_defects.txt')
    head = verdict(cc, r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+')
    misses = cj.get('misses') or []
    needles = re.findall(r"^### \(R278\)\(4\) THE MID-ACT CHECK \([^)]*\): the (?:navigator`s )?answer carrying '([^']*)'", cc, re.M)
    figs = re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', cc)
    nav = re.findall(r"^    \(([a-z]'?)\) THE NAVIGATOR'S", dl, re.M)
    return ('%s ; the misses as the bank lists them: %d (%s) ; the answers checked ((R278)(4)), by their needles: %s, the prints %s ; entered as '
            'the defects bank letters them: the navigator`s %s' % (
                head, len(misses), '; '.join(str(m)[:60] for m in misses) or 'NONE', '; '.join(needles) or 'NONE', '; '.join(figs) or 'NONE',
                ', '.join('(%s)' % x for x in nav) or 'NONE'))


def mirror_line():
    j = jl('b704_mirror.json')
    if not j:
        return '### TO BE BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH (the b670 form, mirror-refresh-%s-b704.zip)' % WL.DATE
    return '%s ; %d bytes ; sha256 %s ; MANIFEST md5 %s ; entries %d ; %s ; %s ; %s' % (
        j.get('zip'), j.get('bytes', 0), (j.get('zip_sha256') or '')[:16], j.get('manifest_md5'), j.get('entries', 0), j.get('root_line') or '### NO ROOT LINE',
        'CLEAN ON ALL THREE CLAUSES' if j.get('clean') else '### NOT CLEAN', j.get('span') or '### NO SPAN LINE')


def scores_at_close():
    S, C = jl('b704_scores.json'), jl('b704_scores_close.json')
    out = {}
    for ks in SCORE_KEYS:
        for k in ks:
            s = S.get(k) or ['?', '']
            c = C.get(k)
            out[k] = (c, 'close') if (s[0] == 'PENDING' and c) else (s, 'record')
    return out


def faces_line():
    """the faces diff's changed lines by cause (relay data/b704_faces_diff.json), the author's word at the cells prompt."""
    j = jl('b704_faces_diff.json')
    bc = j.get('by_cause') or {}
    return 'changed lines %d ; without a cause %s ; by cause: %s' % (len(j.get('rows') or []), j.get('no_cause'),
                                                                     '; '.join('%s %s' % kv for kv in sorted(bc.items())) or '### NONE READ')


def reach_line():
    """the cells' reach (relay data/b704_cells_reach.txt) and the generator's reach (relay data/b704_standing_figures.json): the counts the author's
    word at the cells prompt puts in the closing's report beside the four that were equal."""
    t = rd('b704_cells_reach.txt')
    m = re.search(r'EQUAL (\d+) ; DIFFERS (\d+) ; NO PRINT BANK AT THE TAG (\d+) ; NO THEOREM OR NO TAG (\d+)', t)
    papers = re.findall(r'^  ([A-Z_0-9]+) \| \S+ :\d+ \| .* \| (EQUAL|DIFFERS|NO PRINT BANK AT THE TAG|NO THEOREM OR NO TAG READ)$', t, re.M)
    byp = {}
    for p, _v in papers:
        byp[p] = byp.get(p, 0) + 1
    fj = jl('b704_standing_figures.json')
    rc = (fj.get('reach') or {})
    return ('the mentions read: equal %s ; differs %s ; unbanked %s ; by paper: %s ; the generator`s parsed kernels %d, SIDE-explicit-formula among '
            'them %s' % (m.group(1) if m else '?', m.group(2) if m else '?', str(int(m.group(3)) + int(m.group(4))) if m else '?',
                         '; '.join('%s %d' % kv for kv in sorted(byp.items())) or '### NONE READ', len(rc.get('tabled') or []),
                         'SIDE-explicit-formula' in (rc.get('tabled') or [])))


TITLE_LINE = ('b704 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND THIRTY-ONE, THE RE-CUT ACT: b703 AT ITS WEIGHT; THE UNLETTERED READ '
              'BY CORRIGENDUM AND THE READ RULE SORTED INTO AN ARM; THE FACES CHAIN RE-PROBED AT v0.37 WITH TWO NODES; THE CORRESPONDENCE CELLS OF A '
              'MOVED TAG READ; THE README, THE GLOSSARY COMPANIONS AND ONE PAGE PROOF RE-CUT, UNDER (R314).**')


def act_sections():
    return [('THE CORRIGENDUM AND THE READ RULE ((R314)(1)-(2))', [('the generated entry and the corrigenda row (24)', 'b704_corrigendum.txt'),
                                                                 ('the read rule sorted by trace', 'b704_read_sort.txt'),
                                                                 ('the repaired read bank', 'b704_read_calls.txt'),
                                                                 ('the read arm`s controls', 'b704_read_arm_control.txt'),
                                                                 ('the carry-time repairs', 'b704_tool_repairs.txt')]),
            ('THE FACES PROBE ((R314)(3), N1-N2)', [('the probe branch`s one path', 'b704_probe_diff.txt'),
                                                     ('the run read by its id', 'b704_runner_SIDE-explicit-formula_probe.txt'),
                                                     ('the node list against b702`s', 'b704_nodes_diff.txt'),
                                                     ('the faces diff, each line with its cause', 'b704_faces_diff.txt')]),
            ('THE CELLS ((R314)(4), N3)', [('the generator`s dry run', 'b704_correspondence_dry.txt'), ('the generator`s run', 'b704_correspondence_run.txt'),
                                           ('the prose mentions read against the probe', 'b704_cells_reach.txt')]),
            ('THE README ((R314)(5))', [('the kernel line and the append', 'b704_readme.txt')]),
            ('THE GLOSSARY ((R314)(6))', [('the companions after E0 and the hand grade', 'b704_glossary.txt')]),
            ('THE RE-CUT ((R314)(7), N4)', [('the tie on the author`s word', 'b704_tie.txt'), ('the quotation search', 'b704_quote.txt'),
                                            ('the cut', 'b704_cut.txt')]),
            ('THE STANDING ARMS', [('the four figures against b703`s baseline, and the generator`s reach', 'b704_standing_figures.txt')]),
            ('THE ORDERS ((R314)(3)-(6))', [])]


KERNEL_LINES = [
    '    kernel mains written: none -- SIDE-explicit-formula main at v0.37 (38e2734) unmoved, no tag made ; one scratch branch, probe-b704, cut',
    '    from v0.37 with one commit (ad3db9f, the root CircuitClosure.lean alone, written by the generator), pushed in branch mode, dispatched',
    '    once (run 39721668586) and read by its run id with the artifact`s sha256 verified, then deleted locally and at the remote by name once',
    '    its bank was committed ; widening-b701 and epstein-b703 deleted locally and at the remote on the author`s word ; the eight push-b703*',
    '    branches deleted at step zero by name, one per command and each its own message, nothing chained after any, their tips banked before',
    '    the first delete ; no lean or lake run on this host ; no lakefile or workflow edited ; nothing vendored ; no worktree made or removed ;',
    '    b628`s local intake bank, the navigator`s export, b671`s uncompressed points file, b681`s units file, b694`s witness units file and',
    '    b696`s witness-balls units file untracked ; no identifier of the author in any outbound request or workflow file ; no secret added ; the',
    '    seat`s plain requests to github.com (its git reads and pushes, its one runner dispatch and its reads) the act`s only outbound calls ; the',
    '    deposit route untouched, publish never called ; FINDINGS and OPEN_TRAILS appended ; the README, the faces page and day1/ONE_PAGE_PROOF.md',
    '    written ; data/act_roots.txt, the corrigenda bank and the glossary appended ; no shared tool edited ; no REGISTRY or FOUNDATIONS byte ;',
    '    no paper moved or renamed ; the mirror zip written outside every repository ; nothing of TECHNE or any patent written',
]
CARRIED_FIXED = [
    '    (a) ### **THE NEXT ACTS, (R314)(11)**: b705, the research act, W-ORD-README-FIGURE-SCOPE`s repair at its carry time (the author`s',
    '        word at the README-figure prompt); the closure join on one dispatch at SIDE-explicit-formula`s pin,',
    '        W-ORD-P3-CONTOUR-SIGMA at its step zero, the detection law of (R313)(6)(ii) over the seventeen off-line pairs, the notched Weil window',
    '        with its controls, the I-6 ranking with the support-radius axis, W-ORD-E0-MET-CLASSK; b706 the re-cut act with',
    '        W-ORD-PAPER-PARTNER-COPIES`s disposition, W-ORD-WORKFLOW-PROBE-STEP and W-ORD-CORRESPONDENCE-EF-REACH; b710 the reading act, reading 5.',
    '    (b) The orders: W-ORD-EXPLICIT-FORMULA-C1; W-ORD-EPSTEIN-COUNT-LEAN; W-ORD-PAPER-PARTNER-COPIES; W-ORD-STANDING-CLAUSES-BANK;',
    '        W-ORD-LV-CLOSURE-JOIN; W-ORD-KEYSTONE-HEADS; W-ORD-QUASI-RH-FIELD-WATCH; W-ORD-P3-CONTOUR-SIGMA; W-ORD-E0-MET-CLASSK (its MET lexicon',
    '        for classK`, classKsum and acDeriv); W-ORD-WORKFLOW-PROBE-STEP; W-ORD-CORRESPONDENCE-EF-REACH; W-ORD-README-FIGURE-SCOPE.',
    '        W-ORD-FACES-PROBE-CURRENT discharged.',
    '    (c) For the author`s word: G-READ-RULE-STANDING failing at b704 on (i) and (o) and G-README-CURRENCY on README :135 (the append),',
    '        both declared on the face, N3 refuted on the second; G-WORKFLOW-FILES failing on the probe`s print step (46 of 109 names,',
    '        defect (p)), declared beside them; the eleven unbanked prose mentions of',
    '        relay data/b704_cells_reach.txt; the tie`s reach -- b674`s rule and b666`s not reaching a tie at the agenda`s count, settled on the word',
    '        by b674`s measures in their written order -- for b705`s ruling; the cut`s cells :90-:92 held; the draft held at v5.',
    '    (d) b628`s full intake bank, the navigator`s export, b671`s uncompressed points file, b681`s units file, data/b694_witness_units.jsonl,',
    '        data/b696_witness_balls_units.jsonl and the zero-byte `=` at relay`s root stay local and untracked.',
    '    (e) The act root of b704 is relay data/act_roots.txt`s last line, chained from b703`s root; the mirror export carries it in MANIFEST.',
    '    (f) Branches left for the next act`s step zero: the push-b704* branches of relay and PLACE-papers; none on any kernel.',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]


def main():
    for tool, out in (('b307_handoff_census.py', 'b704_census_closing.txt'), ('b327_faces_census.py', 'b704_faces_census_closing.txt'),
                      ('b303_pins.py', 'b704_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b704'])
        b = o.replace(chr(13), '').encode('utf-8')
        p = os.path.join(OUTD, out)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(b)
        os.replace(p + '.tmp', p)
    paths = ['D:/' + r for r in REPOS] + [SEC]
    read_remotes([p for p in paths if repo_key(p) not in _REMOTE])
    heads = []
    for r in REPOS:
        p = 'D:/' + r
        loc = g(p, 'rev-parse', 'main')
        rem = remote_refs(p).get('refs/heads/main', '')
        heads.append('      %-32s main %s ; remote %s ; %s' % (r.split('/')[-1], loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    for k, t in tags_now():
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
    for b, why in GONE:
        loc = g('D:/SIDE-explicit-formula', 'branch', '--list', b)
        rem = remote_refs('D:/SIDE-explicit-formula').get('refs/heads/' + b, '')
        heads.append('      %-32s local %s ; remote %s ; %s (%s)' % (b, 'PRESENT' if loc else 'absent', rem[:12] or 'absent',
                                                                  'GONE' if not loc and not rem else '### PRESENT', why))
    sb, sm, st = g(SEC, 'rev-parse', 'refs/heads/' + SEC_BRANCH), g(SEC, 'rev-parse', 'main'), g(SEC, 'rev-parse', SEC_TAG + '^{commit}')
    srt, skind = remote_tag(SEC, SEC_TAG)
    heads.append('      %-32s local %s ; %s peeled %s, at the remote %s (%s) ; main %s (unmoved by this act) ; %s (kept, local)' % (
        SEC_BRANCH, sb[:12], SEC_TAG, st[:12], srt[:12], skind, sm[:12], 'AGREE' if sb and sb == st == srt else '### DIFFER'))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED, NOT WRITTEN BY THIS ACT' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?'))
    SC = scores_at_close()
    pre, post = rd('b704_checks.txt'), rd('b704_checks_postpush.txt')
    L = [head_line(), '=' * 104, TITLE_LINE, '=' * 104]
    rec_ = jl('b704_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in getattr(WL, 'SEALED', ()):
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b704_seal_hashes.json):'] + [
        '      %-30s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step at step zero; relay data/b704_citation_check.txt): ' + citation_line(), '']
    RL = jl('b704_record_lines.json').get('lines') or []
    L += ['### THE RECORD LINES ((R314)(1); relay data/b704_record_lines.json): ' + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b704_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b704_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+') + ' ; THE TRAIL`S DEFECTS LINE AGAINST THE BANK: ' + verdict(
        rd('b704_reg_gate.txt'), r'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK \w+') + ' ; THE TRAIL`S RESOLVED LINE AGAINST THE BANK: ' + verdict(
        rd('b704_reg_gate.txt'), r'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK \w+') + ' ; THE CLOSING`S DRY RUN (relay data/b675_rules.txt row 1): ' + verdict(
        rd('b704_reg_gate.txt'), r'THE CLOSING DRY-RUN STEP : [A-Z ]+'), '']
    for title, rows in act_sections():
        L += ['### %s:' % title] + ['    %s (relay data/%s): %s' % (lab, bk, vtail(rd(bk))) for lab, bk in rows]
        if title.startswith('THE FACES PROBE'):
            L.append('    the faces diff by cause (relay data/b704_faces_diff.json): %s' % faces_line())
        if title.startswith('THE CELLS'):
            L.append('    the reach, beside the four equal (the author`s word at the cells prompt): %s' % reach_line())
        if title.startswith('THE ORDERS'):
            L.append('    the landing of the discharge, the two orders and the annotation (relay data/b704_orders_line.json): %s' % (
                ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in jl('b704_orders_line.json').get('lines') or []) or '### NOT LANDED'))
        L += ['']
    L += ['### THE KERNELS: the face`s reading of the kernels (relay data/b704_kernels_face.json): %d kernels read before the seal, after the probe '
          'branch`s deletes ; SIDE-explicit-formula main %s, v0.36 %s, v0.37 %s' % (
              len(jl('b704_kernels_face.json').get('kernels') or {}), g('D:/SIDE-explicit-formula', 'rev-parse', 'main')[:12],
              g('D:/SIDE-explicit-formula', 'rev-parse', 'v0.36^{commit}')[:12], g('D:/SIDE-explicit-formula', 'rev-parse', 'v0.37^{commit}')[:12]), '']
    L += ['### THE ROOT`S BANKS (relay data/b704_root_banks.txt): ' + (
        vline(rd('b704_root_banks.txt')) if rd('b704_root_banks.txt') else 'TO BE READ AT THE ROOT, before it is computed'), '']
    L += ['### THE MIRROR (relay data/b704_mirror.txt, the b670 form, after the root and the last PLACE-papers push): ' + mirror_line(), '']
    L += ['### THE CARRY-TIME READING (the ferry`s Component 5; relay data/b704_tool_repairs.txt): ' + vtail(rd('b704_tool_repairs.txt')),
          '    the remote reads this run: %d repositories, one call each in sequence ; empty reads re-read alone: %s' % (
              len(_REMOTE), '; '.join(REREAD) or 'NONE'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b704_author_answers.txt): ' + verdict(rd('b704_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b704_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, SC[k][0][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL (relay data/b704_scores.json, written once before the entry; a reading that waited, from relay '
          'data/b704_scores_close.json):'] + ['    (%s) %s -- %s [%s]' % (k, SC[k][0][0], SC[k][0][1], SC[k][1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b704_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b704_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b704_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+'),
                                       verdict(rd('b704_faces_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b704_faces_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b704_pins_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b704_pins_closing.txt'), encoding='utf-8').read(),
                                    r'REPOS HARD-FAILING : \d+')]
    L += KERNEL_LINES + ['']
    L += ['### CARRIED FORWARD.'] + carried() + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(OUTD, 'b704_closing_dry.txt' if DRY else 'b704_closing.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    if DRY:
        print('  ### THE CLOSING DRY-RUN, its readings (written to the scratchpad, %s):' % p)
        for l in L:
            if l.startswith(('b704 closed', '### THE', '    the', '    (g)')):
                print('    ' + l[:400])
        print('  ### ### **THE CLOSING DRY-RUN : READ**')
    else:
        print(NL.join(L[-60:]))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'defects-row':
        print(defects_row(sys.argv[2]))
    else:
        main()
