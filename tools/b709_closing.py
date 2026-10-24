# -*- coding: utf-8 -*-
"""b709_closing.py -- THE CLOSING RECORD OF b709, UNDER (R319). Carried from b708_closing.py by tools/b709_carry.py (the act names substituted,
data/b709_rules.txt row (1)), its act sections written for b709 by the Edit tool: the remote reads stored and looked up under ONE key (repo_key(),
b694's repair, carried); the remote reads one per call in sequence, an empty read re-read alone before any row is declared (b674_rules.txt row 1);
the tag rows reading a lightweight tag at its own line; each bank's verdict line and not its title; the citation line from the banks; the captures
in b673's form; the defects row read from the bank (b693's repair); the head line's prompt count the answers bank's rows plus one for the root's
prompt, its defect count the defects bank's lettered rows read now (b700's repair (9), carried). The act's sections are the record lines and the
corrigendum, the grid, the pairs, the port, the axis, the registrations and the standing arms; the report of the ferry's Component 6 prints in one
line each the onset per family with its rung and eigenvalue, the zeta control's lambda_min beside its tail bound, the twelve ratios, the port's
modules built and next failing line, and the four standing arms' figures beside b708's, from the bank the unsealed report tool writes after the
root's word (data/b709_rules.txt row (1)). SIDE-lv-conservation's port branch is read beside the mains at this act's one commit; the join kernel
and SIDE-explicit-formula read unmoved.
`python tools/b709_closing.py dry` -- (R285)(2)'s rule row (relay data/b675_rules.txt row 1), the closing a gate step before the seal: the record
written to the scratchpad and its readings printed; the censuses run into the scratchpad; no bank of relay data/ written.
`python tools/b709_closing.py defects-row <act>` -- the carried-forward defects row computed from relay data/<act>_defects.txt, printed only.
### Writes data/b709_closing.txt and the closing censuses and pins (each its own tool's output) and nothing else.
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
import b709_worklist as WL   # noqa: E402

OUTD = WL.SP if DRY else D

REPOS = ['relay', 'MY-DOwnloads/PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-faces-join', 'SIDE-kernel', 'SIDE-lv-conservation',
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
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']
TAGS_FIXED = [('SIDE-explicit-formula', 'v0.37'), ('SIDE-explicit-formula', 'v0.36'), ('SIDE-explicit-formula', 'v0.35'), ('SIDE-explicit-formula', 'v0.34.1'),
              ('SIDE-explicit-formula', 'v0.34'), ('SIDE-explicit-formula', 'v0.17'), ('SIDE-explicit-formula', 'v0.2'), ('SIDE-explicit-formula', 'v0.1'),
              ('SIDE-substrate-cluster', 'v0.4.1'), ('SIDE-substrate-cluster', 'v0.4'), ('SIDE-simplicity', 'v0.1.2'), ('SIDE-simplicity', 'v0.1.1'),
              ('SIDE-simplicity', 'v0.1.0'), ('SIDE-interfaces', 'v0.2.1'), ('SIDE-interfaces', 'v0.2'), ('SIDE-archimedean', 'v0.1.1'), ('SIDE-archimedean', 'v0.1.0'),
              ('SIDE-rcurve', 'v0.1.1'), ('SIDE-rcurve', 'v0.1.0'), ('SIDE-li-map', 'v0.1.1'), ('SIDE-spinor', 'v0.1.2'), ('SIDE-class-number-anomaly', 'v0.2.1'),
              ('SIDE-window', 'v0.5.2'), ('SIDE-trivium', 'v0.1.2'), ('SIDE-silence-principle', 'v0.2.2'), ('SIDE-bijection', 'v0.2.1'), ('SIDE-grh-transfer', 'v0.5.1'),
              ('SIDE-cosmo', 'v0.3.1'), ('SIDE-effects', 'v0.1.1'), ('SIDE-carrier-spec', 'v0.4.2'), ('SIDE-structural-error-correction', 'v0.2.3'),
              ('SIDE-lv-conservation', 'v0.13.0'), ('SIDE-lv-conservation', 'v0.10.0'), ('SIDE-global-section', 'v0.3.0'), ('SIDE-kernel', 'v1.8')]
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
    """the fixed list; no tag made this act (one commit on port-b707; no main moved)."""
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
    return CARRIED_FIXED[:-1] + [defects_row('b709', 'g')] + CARRIED_FIXED[-1:]


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


ACT = 'b709'
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
    k = len(re.findall(r'^### PROMPT ', _t('%s_author_answers.txt' % act), re.M)) + 1
    d = len([l for l in _t('%s_defects.txt' % act).split(NL) if DEFECT_ROW.match(l)])
    return '%s closed: %s; %s; root %s; %d prompt%s answered; %d defect%s' % (act, ', '.join(parts), suite, root, k, '' if k == 1 else 's',
                                                                             d, '' if d == 1 else 's')


def citation_line():
    cc, cj, dl = rd('b709_citation_check.txt'), jl('b709_citation_check.json'), rd('b709_defects.txt')
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
    j = jl('b709_mirror.json')
    if not j:
        return '### TO BE BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH (the b670 form, mirror-refresh-%s-b709.zip; over b708`s roster of 70 entries, the builder`s state file tools/mirror_prevbuild.json named in (W))' % WL.DATE
    return '%s ; %d bytes ; sha256 %s ; MANIFEST md5 %s ; entries %d ; %s ; %s ; %s ; the roster b708`s, 70 entries; tools/mirror_prevbuild.json written at the build and committed with this closing' % (
        j.get('zip'), j.get('bytes', 0), (j.get('zip_sha256') or '')[:16], j.get('manifest_md5'), j.get('entries', 0), j.get('root_line') or '### NO ROOT LINE',
        'CLEAN ON ALL THREE CLAUSES' if j.get('clean') else '### NOT CLEAN', j.get('span') or '### NO SPAN LINE')


def scores_at_close():
    S, C = jl('b709_scores.json'), jl('b709_scores_close.json')
    out = {}
    for ks in SCORE_KEYS:
        for k in ks:
            s = S.get(k) or ['?', '']
            c = C.get(k)
            out[k] = (c, 'close') if (s[0] == 'PENDING' and c) else (s, 'record')
    return out


# ================================================================================ THE REPORT (the ferry's Component 6: one line each, from the unsealed report tool's bank)
def report_lines():
    rj = jl('b709_report.json')
    ls = rj.get('lines') or []
    if len(ls) >= 5:
        return ['### THE REPORT (the ferry`s Component 6, one line each; relay data/b709_report.txt, by the unsealed tools/b709_report.py written after the root`s word, data/b709_rules.txt row (1)):'] + [
            '    (%d) %s' % (i + 1, l[:900]) for i, l in enumerate(ls)]
    return ['### THE REPORT (the ferry`s Component 6): ### data/b709_report.txt NOT YET WRITTEN (tools/b709_report.py is written after the root`s word and runs before the root)']


TITLE_LINE = ('b709 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND THIRTY-SIX, THE RESEARCH ACT: b708 AT ITS WEIGHT; THE NEEDLE AND THE CARRY BY '
              'DIFF; THE FINE GRID; THE PORT`S NEXT LINES; THE HIGHER PAIRS; THE NEXT AXIS, UNDER (R319).**')
# ### (R319)(2), the repaired needle`s ground: the banks below carry no verdict line BY THEIR FORM (the push tool`s capture); the closing prints
# ### "### NO VERDICT LINE" for them and the suite`s G-CLOSING-DRY-STEP exempts them by name (tools/b709_checks.py NO_VERDICT_EXEMPT).
NO_VERDICT_BY_FORM = ('b709_port_push_out.txt',)


def act_sections():
    return [('THE RECORD LINES AND THE CORRIGENDUM ((R319)(1)-(2))', [('the generated entry and the corrigenda row (29)', 'b709_corrigendum.txt'),
                                                                   ('the carry-time repairs, each with its diff bank; the act`s own sections named apart', 'b709_tool_repairs.txt'),
                                                                   ('the needle`s repaired reading against the old on b708`s gate record and mutated copies', 'b709_repair_controls.txt'),
                                                                   ('the carried tools and their read spans (N3)', 'b709_carry_spans.txt'),
                                                                   ('the root route`s dry run on the pre-root tree (data/b706_rules.txt row (1))', 'b709_root_banks_dry.txt')]),
            ('THE GRID ((R319)(3), N2)', [('the sign-onset radius on the fine grid per family, the controls before the figures', 'b709_grid.txt'),
                                          ('the grid`s binary bank, its hashes (data/b680_rules.txt row (1))', 'b709_grid_hashes.txt')]),
            ('THE PAIRS ((R319)(5), N2)', [('the detection law over the twelve higher pairs, the list extended to 325', 'b709_pairs.txt'),
                                           ('the pairs` binary bank, its hashes (data/b680_rules.txt row (1))', 'b709_pairs_hashes.txt')]),
            ('THE PORT ((R319)(4), N1, N4)', [('the one edit at :277, :380 read unedited, the diffs', 'b709_port_edit.txt'),
                                               ('the push in branch mode, read back (the push tool`s capture, no verdict line by its form)', 'b709_port_push_out.txt'),
                                               ('the one dispatch read by its run id, the artifact verified, the outcome by file and line', 'b709_port.txt')]),
            ('THE AXIS ((R319)(6))', [('the second axis registered for b711 before any number', 'b709_registrations.txt')]),
            ('THE REGISTRATIONS (N2)', [('the four registration banks re-read unchanged; the computed banks committed as they stand', 'b709_registrations_reread.txt')]),
            ('THE STANDING ARMS', [('the four figures against b708`s, read by b706`s tool', 'b709_standing_figures.txt')])]


KERNEL_LINES = [
    '    kernel mains written: none -- SIDE-lv-conservation`s port-b707 given this act`s one commit (C7OrderBounds.lean :277 edited by the Edit tool to',
    '    `isStrongFEPair_toStrongFEPair.hasMellin w`, :380 read again and left unedited as the cascade of :277), pushed alone in the push tool`s branch mode',
    '    and read back, dispatched once at its tip (run 40123142437) and read by run id with the artifact`s sha256 verified: conclusion failure, 11 of 12',
    '    modules built (b707: 6), C7OrderBounds building, DirichletC7Order held at :212:55 by the same changed signature, no grade claimed, the print step',
    '    not run (print_targets.txt absent at the branch) ; the branch HELD at its new tip for b711, no merge, no tag ; SIDE-lv-conservation`s main and its',
    '    deposit v0.10.0 unmoved ; SIDE-explicit-formula`s main at badaccc unmoved, every tag unmoved, no scratch branch ; SIDE-faces-join`s main at its',
    '    manifest commit unmoved, no tag ; the six push-b708* branches of relay and PLACE-papers deleted at step zero by name, one per command and each',
    '    its own message, nothing chained after any, their tips banked before the first delete ; one lean process on this host, the test`s at step zero',
    '    (defect (c)), none started by the seat ; no lakefile, manifest, toolchain or workflow of a kernel`s MAIN edited ; nothing vendored ; no worktree',
    '    made or removed ; b628`s local intake bank, the navigator`s export, b671`s uncompressed points file, b681`s units file, b694`s, b696`s and b707`s',
    '    units files and this act`s grid and pairs units files untracked ;',
    '    no identifier of the author in any outbound request or workflow file ; no secret added ; the seat`s plain requests to github.com (its git',
    '    reads and pushes, its one runner dispatch and its reads) the act`s only outbound calls ; the deposit route untouched, publish never called ;',
    '    FINDINGS and OPEN_TRAILS',
    '    appended ; no paper cut, written, moved or renamed ; data/act_roots.txt and the corrigenda bank appended ; no shared tool or shared data file',
    '    edited ; no REGISTRY byte ; no FOUNDATIONS byte ; no README or faces page byte ; the mirror zip written outside every repository over b708`s roster,',
    '    the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
]
CARRIED_FIXED = [
    '    (a) ### **THE NEXT ACTS, (R319)(10)**: b710, the reading act, reading 5: the standing-clauses bank (W-ORD-STANDING-CLAUSES-BANK) written and the',
    '        ferry carried by version from b711; the readfirst flip read against readings 3 and 4; the reading of the principles S, I, D and E against',
    '        the corpus; the moves-by-locus table drafted for the author`s word. b711, the research act: W-ORD-Q0-ZEROS-443 (the certified list from 325',
    '        to 443 in eight bands of 15 in the foreground form, 90-120 minutes per band by this act`s stamps, then pairs 11 and 15 by the registered',
    '        route, the banked candidate grids and counts above 310 its starting point); the join`s dispatch where the port completes -- port-b707 held at',
    '        92af8a34, DirichletC7Order.lean :212:55 the next line (a changed signature, the same hasMellin argument), then :212:6 and :193:0 heartbeat',
    '        timeouts, :333:8 a cascade, :501:31 and :500:82 broken proofs, :574:39 a changed signature; the second axis (e) representation coordinates',
    '        at the coarse radii as data/b709_registrations.txt registers it. For the next ruling: the carry rule`s provision for a carried tool`s',
    '        act-specific sections (defect (e)); the withheld bank carried by name with the tests tool (defect (c)); the five renames` readers in the',
    '        test files (data/b709_defects.txt, the events), no test edited this act.',
    '    (b) The orders: W-ORD-Q0-ZEROS-443 (entered this act at OPEN_TRAILS :15764, trigger b711); W-ORD-LV-FORWARD-PORT (continued: 11 of 12 modules,',
    '        DirichletC7Order :212:55 next); W-ORD-LV-CLOSURE-JOIN (the join held; its dispatch where the port completes); W-ORD-WORKFLOW-PROBE-STEP',
    '        (annotated DISCHARGED this act at :15762); W-ORD-ENTRY-TAG-PRINTS (read to its end at b708); W-ORD-EXPLICIT-FORMULA-C1; W-ORD-EPSTEIN-COUNT-LEAN;',
    '        W-ORD-STANDING-CLAUSES-BANK (trigger b710); W-ORD-KEYSTONE-HEADS; W-ORD-QUASI-RH-FIELD-WATCH; W-ORD-P3-CONTOUR-SIGMA (read at b705);',
    '        W-ORD-E0-MET-CLASSK (its content done at b705); W-ORD-README-FIGURE-SCOPE (repaired at b705). Discharged this act by a landing: none;',
    '        entered this act: W-ORD-Q0-ZEROS-443.',
    '    (c) For the author`s word: the one citation miss (the seat`s, b708`s kind for :380, the cascade of :277) entered by the fact clause and answered by',
    '        the edit and the run; N1 as worded REFUTED on the test`s lean run (defect (c)), its dispatch clause met; N3 as worded REFUTED on the three',
    '        carried tools read whole ((b), (e)); the higher pairs bounded at height 325 on the author`s word, pairs 11 and 15 beyond reach, not estimated,',
    '        W-ORD-Q0-ZEROS-443 for b711; the background band runs before that word, defect (d); the grid`s hypothesis and falsifier vacuous as worded,',
    '        read and printed with the discriminating reading (a rung for the band, a midpoint for rho_0); the report tool outside the sealed list until',
    '        the root`s word (data/b709_rules.txt row (1)); the draft held at v5.',
    '    (d) b628`s full intake bank, the navigator`s export, b671`s uncompressed points file, b681`s units file, data/b694_witness_units.jsonl,',
    '        data/b696_witness_balls_units.jsonl, data/b707_onset_units.jsonl, this act`s data/b709_grid_units*.jsonl and data/b709_pairs_units*.jsonl',
    '        (declared by prefix in their tools` heads) and the zero-byte `=` at relay`s root stay local and untracked; b705`s two units files and its',
    '        fetched PDF stand in an earlier session`s scratchpad, outside every repository.',
    '    (e) The act root of b709 is relay data/act_roots.txt`s last line, chained from b708`s root; the mirror export carries it in MANIFEST.',
    '    (f) Branches left for the next act`s step zero: the push-b709* branches of relay and PLACE-papers. KEPT, not for deletion: port-b707 of',
    '        SIDE-lv-conservation (the forward-port`s branch, at the remote at this act`s one commit 92af8a34).',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]


def main():
    for tool, out in (('b307_handoff_census.py', 'b709_census_closing.txt'), ('b327_faces_census.py', 'b709_faces_census_closing.txt'),
                      ('b303_pins.py', 'b709_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b709'])
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
    pl = g('D:/SIDE-lv-conservation', 'rev-parse', '--verify', '--quiet', 'refs/heads/' + WL.PORT_BRANCH)
    pr = remote_refs('D:/SIDE-lv-conservation').get('refs/heads/' + WL.PORT_BRANCH, '')
    heads.append('      %-32s local %s ; remote %s ; %s (the forward-port`s branch, (R319)(4): this act`s one commit on b707`s %s, held; DirichletC7Order.lean :212:55 next)' % (
        WL.PORT_BRANCH, pl[:12] or 'absent', pr[:12] or 'absent', 'AGREE' if pl and pl == pr == WL.PORT_TIP else '### DIFFER', WL.PORT_BASE[:8]))
    jt = g('D:/SIDE-faces-join', 'tag', '--list')
    jr = [x for x in remote_refs('D:/SIDE-faces-join') if x.startswith('refs/tags/')]
    heads.append('      %-32s tags local %s ; at the remote %s ; %s (the join held: no tag made)' % (
        'SIDE-faces-join', jt.split() or 'NONE', jr or 'NONE', 'AGREE' if not jt.strip() and not jr else '### A TAG STANDS'))
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
    sb, sm, st = g(SEC, 'rev-parse', 'refs/heads/' + SEC_BRANCH), g(SEC, 'rev-parse', 'main'), g(SEC, 'rev-parse', SEC_TAG + '^{commit}')
    srt, skind = remote_tag(SEC, SEC_TAG)
    heads.append('      %-32s local %s ; %s peeled %s, at the remote %s (%s) ; main %s (unmoved by this act) ; %s (kept, local)' % (
        SEC_BRANCH, sb[:12], SEC_TAG, st[:12], srt[:12], skind, sm[:12], 'AGREE' if sb and sb == st == srt else '### DIFFER'))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED, NOT WRITTEN BY THIS ACT' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?'))
    SC = scores_at_close()
    pre, post = rd('b709_checks.txt'), rd('b709_checks_postpush.txt')
    L = [head_line(), '=' * 104, TITLE_LINE, '=' * 104]
    rec_ = jl('b709_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in getattr(WL, 'SEALED', ()):
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b709_seal_hashes.json; the report tool unsealed by data/b709_rules.txt row (1)):'] + [
        '      %-30s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step at step zero; relay data/b709_citation_check.txt): ' + citation_line(), '']
    RL = jl('b709_record_lines.json').get('lines') or []
    L += ['### THE RECORD LINES ((R319)(1); relay data/b709_record_lines.json): ' + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b709_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b709_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+') + ' ; THE TRAIL`S DEFECTS LINE AGAINST THE BANK: ' + verdict(
        rd('b709_reg_gate.txt'), r'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK \w+') + ' ; THE TRAIL`S RESOLVED LINE AGAINST THE BANK: ' + verdict(
        rd('b709_reg_gate.txt'), r'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK \w+') + ' ; THE CLOSING`S DRY RUN (relay data/b675_rules.txt row 1): ' + verdict(
        rd('b709_reg_gate.txt'), r'THE CLOSING DRY-RUN STEP : [A-Z ]+'), '']
    for title, rows in act_sections():
        L += ['### %s:' % title] + ['    %s (relay data/%s): %s' % (lab, bk, vtail(rd(bk))) for lab, bk in rows]
        L += ['']
    L += report_lines() + ['']
    L += ['### THE KERNELS: the face`s reading of the kernels (relay data/b709_kernels_face.json): %d kernels read before the seal, the join kernel '
          'among them ; SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, no scratch branch ; SIDE-lv-conservation main %s (unmoved), '
          'v0.10.0 %s (the deposit), port-b707 %s (this act`s one commit, held) ; SIDE-faces-join main %s, no tag' % (
              len(jl('b709_kernels_face.json').get('kernels') or {}), g('D:/SIDE-explicit-formula', 'rev-parse', 'main')[:12],
              g('D:/SIDE-explicit-formula', 'rev-parse', 'v0.37^{commit}')[:12], g('D:/SIDE-explicit-formula', 'rev-parse', 'v0.17^{commit}')[:12],
              g('D:/SIDE-lv-conservation', 'rev-parse', 'main')[:12], g('D:/SIDE-lv-conservation', 'rev-parse', 'v0.10.0^{commit}')[:12], pl[:12] or '-',
              g('D:/SIDE-faces-join', 'rev-parse', 'main')[:12]), '']
    L += ['### THE ROOT`S BANKS (relay data/b709_root_banks.txt): ' + (
        vline(rd('b709_root_banks.txt')) if rd('b709_root_banks.txt') else 'TO BE READ AT THE ROOT, before it is computed'), '']
    L += ['### THE MIRROR (relay data/b709_mirror.txt, the b670 form, after the root and the last PLACE-papers push): ' + mirror_line(), '']
    L += ['### THE CARRY-TIME READING (the ferry`s Component 5; relay data/b709_tool_repairs.txt): ' + vtail(rd('b709_tool_repairs.txt')),
          '    the remote reads this run: %d repositories, one call each in sequence ; empty reads re-read alone: %s' % (
              len(_REMOTE), '; '.join(REREAD) or 'NONE'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b709_author_answers.txt): ' + verdict(rd('b709_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b709_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, SC[k][0][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL (relay data/b709_scores.json, written once before the entry; a reading that waited, from relay '
          'data/b709_scores_close.json):'] + ['    (%s) %s -- %s [%s]' % (k, SC[k][0][0], SC[k][0][1], SC[k][1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b709_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b709_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b709_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+'),
                                       verdict(rd('b709_faces_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b709_faces_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b709_pins_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b709_pins_closing.txt'), encoding='utf-8').read(),
                                    r'REPOS HARD-FAILING : \d+')]
    L += KERNEL_LINES + ['']
    L += ['### CARRIED FORWARD.'] + carried() + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(OUTD, 'b709_closing_dry.txt' if DRY else 'b709_closing.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    if DRY:
        print('  ### THE CLOSING DRY-RUN, its readings (written to the scratchpad, %s):' % p)
        for l in L:
            if l.startswith(('b709 closed', '### THE', '    the', '    (g)')):
                print('    ' + l[:400])
        print('  ### ### **THE CLOSING DRY-RUN : READ**')
    else:
        print(NL.join(L[-60:]))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'defects-row':
        print(defects_row(sys.argv[2]))
    else:
        main()
