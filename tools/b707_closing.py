# -*- coding: utf-8 -*-
"""b707_closing.py -- THE CLOSING RECORD OF b707, UNDER (R317). Carried from b706_closing.py by the Write tool, its act text written for b707:
the remote reads stored and looked up under ONE key (repo_key(), b694's repair, carried); the remote reads one per call in sequence, an empty read
re-read alone before any row is declared (b674_rules.txt row 1); the tag rows reading a lightweight tag at its own line; each bank's verdict line
and not its title; the citation line from the banks; the captures in b673's form; the defects row read from the bank (b693's repair); the head
line's prompt count the answers bank's rows plus one for the root's prompt, its defect count the defects bank's lettered rows read now (b700's
repair (9), carried). The act's sections are the repairs and the corrigendum, the onset, the registrations, the port, the standing arms and the
orders; the report of the ferry's Component 6 prints in one line each the onset per frequency, the port's hold, the repairs' controls, the
registrations and the four standing arms' figures beside b706's. SIDE-lv-conservation's port branch is read beside the mains (kept at the
remote, not merged, not tagged); the join kernel and SIDE-explicit-formula read unmoved.
`python tools/b707_closing.py dry` -- (R285)(2)'s rule row (relay data/b675_rules.txt row 1), the closing a gate step before the seal: the record
written to the scratchpad and its readings printed; the censuses run into the scratchpad; no bank of relay data/ written.
`python tools/b707_closing.py defects-row <act>` -- the carried-forward defects row computed from relay data/<act>_defects.txt, printed only.
### Writes data/b707_closing.txt and the closing censuses and pins (each its own tool's output) and nothing else.
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
import b707_worklist as WL   # noqa: E402

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
    """the fixed list; no tag made this act (the port on its branch, not tagged; the deposit v0.10.0 unmoved)."""
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
    return CARRIED_FIXED[:-1] + [defects_row('b707', 'g')] + CARRIED_FIXED[-1:]


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


ACT = 'b707'
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
    cc, cj, dl = rd('b707_citation_check.txt'), jl('b707_citation_check.json'), rd('b707_defects.txt')
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
    j = jl('b707_mirror.json')
    if not j:
        return '### TO BE BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH (the b670 form, mirror-refresh-%s-b707.zip; its roster re-pointed to 70 entries under (R317)(2))' % WL.DATE
    return '%s ; %d bytes ; sha256 %s ; MANIFEST md5 %s ; entries %d ; %s ; %s ; %s ; the roster re-pointed to 70 entries under (R317)(2)' % (
        j.get('zip'), j.get('bytes', 0), (j.get('zip_sha256') or '')[:16], j.get('manifest_md5'), j.get('entries', 0), j.get('root_line') or '### NO ROOT LINE',
        'CLEAN ON ALL THREE CLAUSES' if j.get('clean') else '### NOT CLEAN', j.get('span') or '### NO SPAN LINE')


def scores_at_close():
    S, C = jl('b707_scores.json'), jl('b707_scores_close.json')
    out = {}
    for ks in SCORE_KEYS:
        for k in ks:
            s = S.get(k) or ['?', '']
            c = C.get(k)
            out[k] = (c, 'close') if (s[0] == 'PENDING' and c) else (s, 'record')
    return out


# ================================================================================ THE REPORT (the ferry's Component 6: one line each, through tools/b707_report.py's bank)
def report_lines():
    rj = jl('b707_report.json')
    ls = rj.get('lines') or []
    if len(ls) == 5:
        return ['### THE REPORT (the ferry`s Component 6, one line each; relay data/b707_report.txt, by tools/b707_report.py):'] + ['    (%d) %s' % (i + 1, l[:900]) for i, l in enumerate(ls)]
    return ['### THE REPORT (the ferry`s Component 6): ### data/b707_report.txt NOT YET WRITTEN (tools/b707_report.py runs before the root)']


TITLE_LINE = ('b707 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND THIRTY-FOUR, THE RESEARCH ACT: b706 AT ITS WEIGHT; THE RENAMES` READERS '
              'AND THE SPLIT ARM REPAIRED; THE SIGN-ONSET RADIUS AT Q0; THE HIGHER PAIRS` ROUTE REGISTERED; lv-CONSERVATION`S FORWARD-PORT OPENED, UNDER (R317).**')


def act_sections():
    return [('THE REPAIRS AND THE CORRIGENDUM ((R317)(1)-(2))', [('the carry-time repairs: the three readers and the carry`s three, each a diff', 'b707_tool_repairs.txt'),
                                                             ('the repaired readings against the old on real state and mutated copies (the roster`s control, tools/mirror_verify.py run dry against b706`s export, in data/b707_roster_control.txt)', 'b707_repair_controls.txt'),
                                                             ('the table`s scope: the regeneration against b706`s final table', 'b707_table_scope.txt'),
                                                             ('the root route`s dry run on the pre-root tree (data/b706_rules.txt row (1))', 'b707_root_banks_dry.txt'),
                                                             ('the generated entry and the corrigenda row (27)', 'b707_corrigendum.txt')]),
            ('THE ONSET ((R317)(3), N2, N3)', [('the controls before any Q0 figure: the rung structure, C1 at zeta, C2 on the registered windows', 'b707_onset_controls.txt'),
                                               ('the form on the family at Q0 over the ladder, the onset per frequency (the binary bank beside its hashes, data/b707_onset_hashes.txt)', 'b707_onset.txt')]),
            ('THE REGISTRATIONS ((R317)(4), N2)', [('the twelve higher pairs` route, committed alone before any computation', 'b707_registrations.txt'),
                                                   ('the registrations re-read unchanged after the computations; the next axis', 'b707_registrations_reread.txt')]),
            ('THE PORT ((R317)(5), N1)', [('the five files printed before the one commit', 'b707_port_files.txt'),
                                          ('the run read by its id; the outcome by file and line', 'b707_port.txt')]),
            ('THE STANDING ARMS', [('the four figures against b706`s, read by b706`s tool', 'b707_standing_figures.txt')]),
            ('THE ORDERS ((R317)(2), (5))', [])]


KERNEL_LINES = [
    '    kernel mains written: none -- SIDE-lv-conservation`s port branch port-b707 cut at its deposit v0.10.0 = 93c27ec under (R317)(5) and the author`s',
    '    word, five files on it (lean-toolchain, lake-manifest.json and lakefile.lean at the shared pin Lean v4.34.0-rc1 / Mathlib de5ce8a9,',
    '    GammaBounds.lean :177`s rw given its beta-reduced goal, SIDE-explicit-formula`s build-module.yml at main carried verbatim), each printed',
    '    before the one commit 69e239d with its diff banked, pushed alone in the push tool`s branch mode and read back, dispatched once at the branch',
    '    (run 39888369981) and read by its run id with the artifact`s sha256 verified: the cache served, 6 of 12 modules built (GammaBounds among',
    '    them), the build HELD at SIDELvConservation/C7OrderBounds.lean :277:55, the print step not run (print_targets.txt absent at 93c27ec), no',
    '    grade claimed; the branch kept at the remote, not merged, not tagged, port-b707 deleted under no answer ; SIDE-lv-conservation`s main and its',
    '    deposit unmoved ; SIDE-explicit-formula`s main at badaccc unmoved, every tag unmoved ; SIDE-faces-join`s main at its manifest commit unmoved, no',
    '    tag ; the eight push-b706* branches deleted at step zero by name, one per command and each its own message, nothing chained after any, their',
    '    tips banked before the first delete ; no lean or lake run on this host ; no lakefile, manifest, toolchain or workflow of a kernel`s MAIN edited',
    '    (the four on the port branch alone) ; nothing vendored ; no worktree made or removed ; b628`s local intake bank, the navigator`s export, b671`s',
    '    uncompressed points file, b681`s units file, b694`s and b696`s units files and this act`s onset units file untracked ;',
    '    no identifier of the author in any outbound request or workflow file ; no secret added ; the seat`s plain requests to github.com (its git',
    '    reads and pushes, its one runner dispatch and its reads) the act`s only outbound calls ; the deposit route untouched, publish never called ;',
    '    FINDINGS and OPEN_TRAILS',
    '    appended ; data/act_roots.txt and the corrigenda bank appended ; tools/terminal_table.py and tools/rule_arms.py edited by the Edit tool under',
    '    (R317)(2) with their controls, tools/mirror_roster.json re-pointed to 70 entries by the Edit tool on the author`s word, no other shared file',
    '    edited ; no paper written, moved or renamed ; no REGISTRY byte ; no FOUNDATIONS byte ; no README or faces page byte ; the mirror zip written',
    '    outside every repository over the re-pointed roster ; nothing of TECHNE or any patent written',
]
CARRIED_FIXED = [
    '    (a) ### **THE NEXT ACTS, (R317)**: b708, the re-cut act: the opening probe through the workflow`s step; the two remaining entry-tag prints',
    '        (SIMPLICITY :442 at v0.17 priced one dispatch; FACES_LEDGER :20 none); the licensed table`s next document. b709 the research act: the',
    '        higher pairs` route as data/b707_registrations.txt registers it (256 bits, the onset cap 1.5 n*, the new certification above 149.72 the',
    '        main cost); the port`s next dispatch on port-b707 (C7OrderBounds.lean :277 and :380 first); the next axis (e) representation',
    '        coordinates. b710 the reading act, reading 5, with W-ORD-STANDING-CLAUSES-BANK. For the next ruling: the five renames` readers in the',
    '        test files (data/b707_defects.txt, the events), no test edited this act.',
    '    (b) The orders: W-ORD-LV-FORWARD-PORT (OPEN: port-b707 held at C7OrderBounds.lean :277, 6 of 12 built); W-ORD-ENTRY-TAG-PRINTS`s remainder',
    '        (the two unbanked mentions entered, trigger b708); W-ORD-LV-CLOSURE-JOIN (the join held at lv-conservation`s module, re-dispatched only at a',
    '        port that builds 12 of 12); W-ORD-EXPLICIT-FORMULA-C1; W-ORD-EPSTEIN-COUNT-LEAN; W-ORD-STANDING-CLAUSES-BANK; W-ORD-KEYSTONE-HEADS;',
    '        W-ORD-QUASI-RH-FIELD-WATCH; W-ORD-P3-CONTOUR-SIGMA (read at b705); W-ORD-E0-MET-CLASSK (its content done at b705); W-ORD-README-FIGURE-SCOPE',
    '        (repaired at b705). Discharged this act: none; entered this act: W-ORD-LV-FORWARD-PORT.',
    '    (c) For the author`s word: G-WORKFLOW-FILES, G-RUNNER-READ and G-RUNNER-GATE failing on the held port run, declared on the face; the roster',
    '        re-pointed to 70 entries (four re-pointed, thirteen duplicates struck) on the author`s word, the ruling`s "17 names" the navigator`s (f);',
    '        the port of five files on the author`s word, the ruling`s "nothing else edited" the navigator`s (g); the family of the onset named at',
    '        b707 as span{C, N} at two frequencies, the band zero`s and rho_0`s; a* at the ladder`s last rung at the band zero`s family (the family',
    '        adding no earlier negative direction) and at the first prime rung at rho_0`s (the ladder coarse there, b696`s finer ladder placing it in',
    '        (2 log 24, 2 log 32]); the ruling`s root count 100 (114), (l)`s owner and "the tag each cites" the navigator`s (c), (d), (e); the',
    '        draft held at v5.',
    '    (d) b628`s full intake bank, the navigator`s export, b671`s uncompressed points file, b681`s units file, data/b694_witness_units.jsonl,',
    '        data/b696_witness_balls_units.jsonl, data/b707_onset_units.jsonl and the zero-byte `=` at relay`s root stay local and untracked; b705`s',
    '        two units files and its fetched PDF stand in the earlier session`s scratchpad, outside every repository.',
    '    (e) The act root of b707 is relay data/act_roots.txt`s last line, chained from b706`s root; the mirror export carries it in MANIFEST.',
    '    (f) Branches left for the next act`s step zero: the push-b707* branches of relay and PLACE-papers. KEPT, not for deletion: port-b707 of',
    '        SIDE-lv-conservation (the forward-port`s branch, at the remote).',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]


def main():
    for tool, out in (('b307_handoff_census.py', 'b707_census_closing.txt'), ('b327_faces_census.py', 'b707_faces_census_closing.txt'),
                      ('b303_pins.py', 'b707_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b707'])
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
    heads.append('      %-32s local %s ; remote %s ; %s (the forward-port`s branch, (R317)(5): kept, not merged, not tagged; held at C7OrderBounds.lean :277)' % (
        WL.PORT_BRANCH, pl[:12] or 'absent', pr[:12] or 'absent', 'AGREE' if pl and pl == pr == WL.PORT_COMMIT else '### DIFFER'))
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
    pre, post = rd('b707_checks.txt'), rd('b707_checks_postpush.txt')
    L = [head_line(), '=' * 104, TITLE_LINE, '=' * 104]
    rec_ = jl('b707_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in getattr(WL, 'SEALED', ()):
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b707_seal_hashes.json):'] + [
        '      %-30s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step at step zero; relay data/b707_citation_check.txt): ' + citation_line(), '']
    RL = jl('b707_record_lines.json').get('lines') or []
    L += ['### THE RECORD LINES ((R317)(1); relay data/b707_record_lines.json): ' + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b707_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b707_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+') + ' ; THE TRAIL`S DEFECTS LINE AGAINST THE BANK: ' + verdict(
        rd('b707_reg_gate.txt'), r'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK \w+') + ' ; THE TRAIL`S RESOLVED LINE AGAINST THE BANK: ' + verdict(
        rd('b707_reg_gate.txt'), r'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK \w+') + ' ; THE CLOSING`S DRY RUN (relay data/b675_rules.txt row 1): ' + verdict(
        rd('b707_reg_gate.txt'), r'THE CLOSING DRY-RUN STEP : [A-Z ]+'), '']
    for title, rows in act_sections():
        L += ['### %s:' % title] + ['    %s (relay data/%s): %s' % (lab, bk, vtail(rd(bk))) for lab, bk in rows]
        if title.startswith('THE ORDERS'):
            ls = (jl('b707_orders.json').get('lines') or []) + (jl('b707_orders_1.json').get('lines') or [])
            L.append('    the landings at OPEN_TRAILS (relay data/b707_orders.json, data/b707_orders_1.json): %s' % (
                ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in ls) or '### NOT LANDED'))
        L += ['']
    L += report_lines() + ['']
    L += ['### THE KERNELS: the face`s reading of the kernels (relay data/b707_kernels_face.json): %d kernels read before the seal, the join kernel '
          'among them ; SIDE-lv-conservation main %s (unmoved), v0.10.0 %s (the deposit, the port`s base), port-b707 %s (its one commit, held at '
          'C7OrderBounds.lean :277) ; SIDE-explicit-formula main %s (unmoved), v0.17 %s ; SIDE-faces-join main %s, no tag' % (
              len(jl('b707_kernels_face.json').get('kernels') or {}), g('D:/SIDE-lv-conservation', 'rev-parse', 'main')[:12],
              g('D:/SIDE-lv-conservation', 'rev-parse', 'v0.10.0^{commit}')[:12], pl[:12] or '-',
              g('D:/SIDE-explicit-formula', 'rev-parse', 'main')[:12], g('D:/SIDE-explicit-formula', 'rev-parse', 'v0.17^{commit}')[:12],
              g('D:/SIDE-faces-join', 'rev-parse', 'main')[:12]), '']
    L += ['### THE ROOT`S BANKS (relay data/b707_root_banks.txt): ' + (
        vline(rd('b707_root_banks.txt')) if rd('b707_root_banks.txt') else 'TO BE READ AT THE ROOT, before it is computed'), '']
    L += ['### THE MIRROR (relay data/b707_mirror.txt, the b670 form, after the root and the last PLACE-papers push): ' + mirror_line(), '']
    L += ['### THE CARRY-TIME READING (the ferry`s Components 1 and 5; relay data/b707_tool_repairs.txt): ' + vtail(rd('b707_tool_repairs.txt')),
          '    the remote reads this run: %d repositories, one call each in sequence ; empty reads re-read alone: %s' % (
              len(_REMOTE), '; '.join(REREAD) or 'NONE'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b707_author_answers.txt): ' + verdict(rd('b707_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b707_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, SC[k][0][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL (relay data/b707_scores.json, written once before the entry; a reading that waited, from relay '
          'data/b707_scores_close.json):'] + ['    (%s) %s -- %s [%s]' % (k, SC[k][0][0], SC[k][0][1], SC[k][1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b707_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b707_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b707_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+'),
                                       verdict(rd('b707_faces_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b707_faces_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b707_pins_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b707_pins_closing.txt'), encoding='utf-8').read(),
                                    r'REPOS HARD-FAILING : \d+')]
    L += KERNEL_LINES + ['']
    L += ['### CARRIED FORWARD.'] + carried() + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(OUTD, 'b707_closing_dry.txt' if DRY else 'b707_closing.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    if DRY:
        print('  ### THE CLOSING DRY-RUN, its readings (written to the scratchpad, %s):' % p)
        for l in L:
            if l.startswith(('b707 closed', '### THE', '    the', '    (g)')):
                print('    ' + l[:400])
        print('  ### ### **THE CLOSING DRY-RUN : READ**')
    else:
        print(NL.join(L[-60:]))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'defects-row':
        print(defects_row(sys.argv[2]))
    else:
        main()
