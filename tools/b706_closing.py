# -*- coding: utf-8 -*-
"""b706_closing.py -- THE CLOSING RECORD OF b706, UNDER (R316). Carried from b705_closing.py by the Write tool, its act text written for b706:
the remote reads stored and looked up under ONE key (repo_key(), b694's repair, carried); the remote reads one per call in sequence, an empty read
re-read alone before any row is declared (b674_rules.txt row 1); the tag rows reading a lightweight tag at its own line; each bank's verdict line
and not its title; the citation line from the banks; the captures in b673's form; the defects row read from the bank (b693's repair); the head
line's prompt count the answers bank's rows plus one for the root's prompt, its defect count the defects bank's lettered rows read now (b700's
repair (9), carried). The act's sections are the sort, the repairs and the corrigendum, the partner copies, the join, the workflow, the
generator, the entry-tag prints, the faces row, the standing arms and the orders; the report of the ferry's Component 6 prints in one line each
the pairs renamed and held, the join's grade, the generator's cell count, the 11 mentions' readings and the four standing arms' figures beside
b705's. The join kernel SIDE-faces-join is read beside the other repositories (its main moved by its manifest commit, no tag); the two scratch
branches of (R316)(7) are read GONE, locally and at the remote; SIDE-explicit-formula's main one commit past v0.37, the workflow's probe step.
`python tools/b706_closing.py dry` -- (R285)(2)'s rule row (relay data/b675_rules.txt row 1), the closing a gate step before the seal: the record
written to the scratchpad and its readings printed; the censuses run into the scratchpad; no bank of relay data/ written.
`python tools/b706_closing.py defects-row <act>` -- the carried-forward defects row computed from relay data/<act>_defects.txt, printed only.
### Writes data/b706_closing.txt and the closing censuses and pins (each its own tool's output) and nothing else.
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
import b706_worklist as WL   # noqa: E402

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
GONE = [(br, '(R316)(7): the scratch branch at %s, deleted by name locally and at the remote after its print bank was committed (relay %s)' % (tag, WL.C4_RELAY))
        for tag, br in WL.PRINT_BRANCHES]
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']
TAGS_FIXED = [('SIDE-explicit-formula', 'v0.37'), ('SIDE-explicit-formula', 'v0.36'), ('SIDE-explicit-formula', 'v0.35'), ('SIDE-explicit-formula', 'v0.34.1'),
              ('SIDE-explicit-formula', 'v0.34'), ('SIDE-explicit-formula', 'v0.2'), ('SIDE-explicit-formula', 'v0.1'), ('SIDE-substrate-cluster', 'v0.4.1'),
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
    """SIDE-explicit-formula's tags first (v0.37 its highest, unmoved; the entry tags v0.1 and v0.2 read at their peels, untouched by (R316)(7)),
    then the fixed list; no tag made this act (the join held)."""
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
    return CARRIED_FIXED[:-1] + [defects_row('b706', 'g')] + CARRIED_FIXED[-1:]


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


ACT = 'b706'
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
    cc, cj, dl = rd('b706_citation_check.txt'), jl('b706_citation_check.json'), rd('b706_defects.txt')
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
    j = jl('b706_mirror.json')
    if not j:
        return '### TO BE BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH (the b670 form, mirror-refresh-%s-b706.zip; its roster names as renamed under (R316)(3))' % WL.DATE
    return '%s ; %d bytes ; sha256 %s ; MANIFEST md5 %s ; entries %d ; %s ; %s ; %s ; the roster names as renamed under (R316)(3)' % (
        j.get('zip'), j.get('bytes', 0), (j.get('zip_sha256') or '')[:16], j.get('manifest_md5'), j.get('entries', 0), j.get('root_line') or '### NO ROOT LINE',
        'CLEAN ON ALL THREE CLAUSES' if j.get('clean') else '### NOT CLEAN', j.get('span') or '### NO SPAN LINE')


def scores_at_close():
    S, C = jl('b706_scores.json'), jl('b706_scores_close.json')
    out = {}
    for ks in SCORE_KEYS:
        for k in ks:
            s = S.get(k) or ['?', '']
            c = C.get(k)
            out[k] = (c, 'close') if (s[0] == 'PENDING' and c) else (s, 'record')
    return out


# ================================================================================ THE REPORT (the ferry's Component 6: one line each)
def report_lines():
    pj = jl('b706_partners.json').get('rows') or []
    ren = [r['doc'] for r in pj if str(r.get('reading', '')).startswith('RENAME')]
    held = [r['doc'] for r in pj if not str(r.get('reading', '')).startswith('RENAME')]
    jg = vtail(rd('b706_join_grade.txt'))
    gr = jl('b706_generator_reach.json')
    reach = (gr.get('reach') or {}).get('SIDE-explicit-formula') or {}
    cj = jl('b706_cells_reread.json').get('rows') or []
    eq = sum(1 for r in cj if r.get('verdict') == 'equal')
    df = sum(1 for r in cj if r.get('verdict') == 'differs')
    ub = len(cj) - eq - df
    fj, f5 = jl('b706_standing_figures.json'), jl('b705_standing_figures.json')
    figs = '; '.join('%s %s (b705 %s)' % (k, (fj.get(k) or {}).get('figure', '-'), (f5.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins'))
    return ['### THE REPORT (the ferry`s Component 6, one line each):',
            '    the pairs renamed and held (relay data/b706_partners.txt): %d of %d renamed in place, %d held%s' % (
                len(ren), len(pj), len(held), (' (%s)' % ', '.join(held)) if held else ''),
            '    the join`s grade (relay data/b706_join_grade.txt): %s' % jg,
            '    the generator`s cell count (relay data/b706_generator_reach.txt): %s kernels parsed, SIDE-explicit-formula among them %s, its citation-form cells %s ; the control equal %s' % (
                len(gr.get('kernels_new') or []), 'SIDE-explicit-formula' in (gr.get('kernels_new') or []), reach.get('cited', '-'), gr.get('equal')),
            '    the 11 mentions` readings (relay data/b706_cells_reread.txt): %d re-read ; equal %d ; differs %d ; unbanked %d' % (len(cj), eq, df, ub),
            '    the four standing arms` figures beside b705`s (relay data/b706_standing_figures.txt): %s' % figs]


TITLE_LINE = ('b706 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND THIRTY-THREE, THE RE-CUT ACT: b705 AT ITS WEIGHT; THE POST-SEAL '
              'FAILURES SORTED AND THREE TOOLS REPAIRED; THE PARTNER COPIES RENAMED IN PLACE; THE JOIN`S MANIFEST; THE WORKFLOW`S PROBE STEP; THE '
              'GENERATOR`S REACH; THE ENTRY-TAG PRINTS; THE FACES ROW, UNDER (R316).**')


def act_sections():
    return [('THE SORT, THE REPAIRS AND THE CORRIGENDUM ((R316)(1)-(2))', [('the ten arms sorted by cause, the six after the seal', 'b706_arm_sort.txt'),
                                                                        ('the carry-time repairs', 'b706_tool_repairs.txt'),
                                                                        ('the repaired readings against the old on b705`s banks', 'b706_repair_controls.txt'),
                                                                        ('the root route`s dry run on the pre-root tree (data/b706_rules.txt row (1))', 'b706_root_banks_dry.txt'),
                                                                        ('the generated entry and the corrigenda row (26)', 'b706_corrigendum.txt')]),
            ('THE PARTNER COPIES ((R316)(3), N2)', [('the 8 hand-edited lines read side by side first', 'b706_partners_read.txt'),
                                                     ('the generator`s run measured dry before any paper was written', 'b706_partners_dry.txt'),
                                                     ('the 17 pairs: the zero diff against the generator, the lines counted apart, the renames', 'b706_partners.txt'),
                                                     ('the 102 reader hits and the roster after the renames', 'b706_readers_after.txt'),
                                                     ('the generator`s roster at the unversioned names', 'b706_roster_read.txt')]),
            ('THE JOIN ((R316)(4), N1, N3)', [('the lakefile re-ordered, mathlib last, printed before the commit', 'b706_join_lakefile.txt'),
                                               ('the kernel`s files at its manifest commit', 'b706_join_files.txt'),
                                               ('the run read by its id', 'b706_runner_SIDE-faces-join_join.txt'),
                                               ('the grade, E0 and the salt-check; the join held with its cause by line', 'b706_join_grade.txt')]),
            ('THE WORKFLOW ((R316)(5))', [('the probe step after the print step and before the closure, its separate artifact', 'b706_workflow_step.txt')]),
            ('THE GENERATOR ((R316)(6), N4)', [('the cell forms printed before the edit', 'b706_generator_forms.txt'),
                                                 ('the parser`s reach after the edit and the byte-for-byte control', 'b706_generator_reach.txt')]),
            ('THE ENTRY-TAG PRINTS ((R316)(7), N1, N4)', [('the branch at v0.1: its files and the workflow`s blob', 'b706_print_files_prints-b706-v0.1.txt'),
                                                           ('the branch at v0.2: its files and the workflow`s blob', 'b706_print_files_prints-b706-v0.2.txt'),
                                                           ('the run at v0.1 read by its id', 'b706_runner_SIDE-explicit-formula_prints_v0_1.txt'),
                                                           ('the run at v0.2 read by its id', 'b706_runner_SIDE-explicit-formula_prints_v0_2.txt'),
                                                           ('the 11 mentions re-read against the new banks', 'b706_cells_reread.txt')]),
            ('THE FACES ROW ((R316)(8))', [('the join held: no prompt, no row changed, the hold named in the entry', 'b706_faces.txt')]),
            ('THE STANDING ARMS', [('the four figures against b705`s, read from this act`s roster', 'b706_standing_figures.txt')]),
            ('THE ORDERS ((R316)(3)-(7))', [])]


KERNEL_LINES = [
    '    kernel mains written: two -- SIDE-faces-join`s manifest commit b37a7b6 on main (its lakefile re-ordered, mathlib last at de5ce8a9, every',
    '    revision as at 732c1b49, no manifest written on this host), pushed in the push tool`s main mode and read back, dispatched once (run',
    '    39850337262) and read by its run id with the artifact`s sha256 verified: the cache served, Mathlib built, lv-conservation`s fifteen files',
    '    rebuilt at the shared pin and the build HELD at SIDELvConservation/GammaBounds.lean :177, faces_join not printed, the gate NOT DERIVES,',
    '    the join HELD with the error banked by line, no tag, no second dispatch ; SIDE-explicit-formula`s main one commit past v0.37, badaccc, the',
    '    workflow`s probe step alone ((R316)(5)), pushed in main mode and read back, no dispatch on main, every tag unmoved ; two scratch branches',
    '    prints-b706-v0.1 (748f2a9 at baed4df) and prints-b706-v0.2 (34e098a at 5c72cad) cut under (R316)(7), one dispatch each (runs 39852365437,',
    '    39852975531, both DERIVES), the probe step`s prints banked from the separate chain-probe artifacts, each branch deleted by name locally and',
    '    at the remote after its bank was committed, the tags untouched ; SIDE-lv-conservation at its deposit v0.10.0 unmoved ; the eight push-b705*',
    '    branches deleted at step zero by name, one per command and each its own message, nothing chained after any, their tips banked before the',
    '    first delete ; no lean or lake run on this host ; no lakefile or workflow of a kernel edited but the two the ruling names ; nothing vendored ;',
    '    no worktree made or removed ; b628`s local intake bank, the navigator`s export, b671`s uncompressed points file, b681`s units file, b694`s and',
    '    b696`s units files untracked ; no identifier of the author in any outbound request or workflow file ; no secret added ;',
    '    the seat`s plain requests to github.com (its git reads and pushes, its three runner dispatches and its reads) the act`s only outbound',
    '    calls ; the deposit route untouched, publish never called ; FINDINGS and OPEN_TRAILS appended ; data/act_roots.txt and the corrigenda bank appended ;',
    '    tools/correspondence_gen.py`s parser extended by the Edit tool under (R316)(6), its control byte for byte, no other shared tool edited ;',
    '    REGISTRY`s seventeen rows` version cells set to the tag under (R316)(3) ; the seventeen unversioned copies retired to',
    '    archive/2026-10-22-b706-partner-copies/ and the seventeen versioned copies renamed to the unversioned names, each pair by two git mv in one',
    '    commit alone, no other paper moved or renamed ; no FOUNDATIONS byte ; no README or faces page byte (the join held: no faces prompt) ; the',
    '    mirror zip written outside every repository, its roster names as renamed ; nothing of TECHNE or any patent written',
]
CARRIED_FIXED = [
    '    (a) ### **THE NEXT ACTS, (R316)(12)**: b707, the research act: the sign-onset radius at Q0 as data/b705_registrations.txt (iii) registered',
    '        it, with its controls; the top-ranked axis at full grade; the detection law`s twelve higher pairs priced by a route beyond b675`s',
    '        modulus rule, registered before any number. b708 the re-cut act with the opening probe through the workflow`s step. b710 the reading',
    '        act, reading 5. For the next ruling: the join held at lv-conservation`s module at the shared pin, the lv forward-port b703 priced.',
    '    (b) The orders: W-ORD-EXPLICIT-FORMULA-C1; W-ORD-EPSTEIN-COUNT-LEAN; W-ORD-STANDING-CLAUSES-BANK; W-ORD-LV-CLOSURE-JOIN (the join held at',
    '        lv-conservation`s GammaBounds.lean :177 at the shared pin, its manifest repaired); W-ORD-KEYSTONE-HEADS; W-ORD-QUASI-RH-FIELD-WATCH;',
    '        W-ORD-P3-CONTOUR-SIGMA (read at b705); W-ORD-E0-MET-CLASSK (its content done at b705); W-ORD-README-FIGURE-SCOPE (repaired at b705).',
    '        Discharged this act: W-ORD-PAPER-PARTNER-COPIES, W-ORD-FACES-JOIN-MANIFEST (entered and discharged), W-ORD-WORKFLOW-PROBE-STEP,',
    '        W-ORD-CORRESPONDENCE-EF-REACH, W-ORD-ENTRY-TAG-PRINTS.',
    '    (c) For the author`s word: G-WORKFLOW-FILES, G-RUNNER-READ and G-RUNNER-GATE failing on the held join, declared on the face; the join held',
    '        at the build of lv-conservation`s module and not at its manifest, Lake`s hint taken (mathlib last) on the author`s word and the ruling`s',
    '        order the navigator`s (b); the eight hand-edited lines resolved by their kind and the 107 remaining lines counted apart, every one the',
    '        versioned side`s, on the author`s two answers, the first put on an unmeasured premise (f); E_DIFFICULTY_THEOREM renamed with its table',
    '        in the versioned copy alone, no diff taken; N3 refuted on its first clause by the author`s word; the Project mirror`s roster names as',
    '        renamed from this act`s export; the draft held at v5.',
    '    (d) b628`s full intake bank, the navigator`s export, b671`s uncompressed points file, b681`s units file, data/b694_witness_units.jsonl,',
    '        data/b696_witness_balls_units.jsonl and the zero-byte `=` at relay`s root stay local and untracked; b705`s two units files and its',
    '        fetched PDF stand in the session`s scratchpad, outside every repository.',
    '    (e) The act root of b706 is relay data/act_roots.txt`s last line, chained from b705`s root; the mirror export carries it in MANIFEST.',
    '    (f) Branches left for the next act`s step zero: the push-b706* branches of relay and PLACE-papers; push-b706-join of SIDE-faces-join;',
    '        push-b706-ef of SIDE-explicit-formula.',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]


def main():
    for tool, out in (('b307_handoff_census.py', 'b706_census_closing.txt'), ('b327_faces_census.py', 'b706_faces_census_closing.txt'),
                      ('b303_pins.py', 'b706_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b706'])
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
    pre, post = rd('b706_checks.txt'), rd('b706_checks_postpush.txt')
    L = [head_line(), '=' * 104, TITLE_LINE, '=' * 104]
    rec_ = jl('b706_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in getattr(WL, 'SEALED', ()):
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b706_seal_hashes.json):'] + [
        '      %-30s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step at step zero; relay data/b706_citation_check.txt): ' + citation_line(), '']
    RL = jl('b706_record_lines.json').get('lines') or []
    L += ['### THE RECORD LINES ((R316)(1); relay data/b706_record_lines.json): ' + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b706_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b706_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+') + ' ; THE TRAIL`S DEFECTS LINE AGAINST THE BANK: ' + verdict(
        rd('b706_reg_gate.txt'), r'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK \w+') + ' ; THE TRAIL`S RESOLVED LINE AGAINST THE BANK: ' + verdict(
        rd('b706_reg_gate.txt'), r'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK \w+') + ' ; THE CLOSING`S DRY RUN (relay data/b675_rules.txt row 1): ' + verdict(
        rd('b706_reg_gate.txt'), r'THE CLOSING DRY-RUN STEP : [A-Z ]+'), '']
    for title, rows in act_sections():
        L += ['### %s:' % title] + ['    %s (relay data/%s): %s' % (lab, bk, vtail(rd(bk))) for lab, bk in rows]
        if title.startswith('THE ORDERS'):
            L.append('    the landings at OPEN_TRAILS (relay data/b706_orders.json): %s' % (
                ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in (jl('b706_orders.json').get('lines') or [])) or '### NOT LANDED'))
        L += ['']
    L += report_lines() + ['']
    L += ['### THE KERNELS: the face`s reading of the kernels (relay data/b706_kernels_face.json): %d kernels read before the seal, the join kernel '
          'among them ; SIDE-explicit-formula main %s (one commit past v0.37 %s: the workflow`s probe step), v0.1 %s, v0.2 %s ; SIDE-faces-join main %s, no tag ; '
          'SIDE-lv-conservation main %s, v0.10.0 %s' % (
              len(jl('b706_kernels_face.json').get('kernels') or {}), g('D:/SIDE-explicit-formula', 'rev-parse', 'main')[:12],
              g('D:/SIDE-explicit-formula', 'rev-parse', 'v0.37^{commit}')[:12], g('D:/SIDE-explicit-formula', 'rev-parse', 'v0.1^{commit}')[:12],
              g('D:/SIDE-explicit-formula', 'rev-parse', 'v0.2^{commit}')[:12],
              g('D:/SIDE-faces-join', 'rev-parse', 'main')[:12], g('D:/SIDE-lv-conservation', 'rev-parse', 'main')[:12],
              g('D:/SIDE-lv-conservation', 'rev-parse', 'v0.10.0^{commit}')[:12]), '']
    L += ['### THE ROOT`S BANKS (relay data/b706_root_banks.txt): ' + (
        vline(rd('b706_root_banks.txt')) if rd('b706_root_banks.txt') else 'TO BE READ AT THE ROOT, before it is computed'), '']
    L += ['### THE MIRROR (relay data/b706_mirror.txt, the b670 form, after the root and the last PLACE-papers push): ' + mirror_line(), '']
    L += ['### THE CARRY-TIME READING (the ferry`s Component 5; relay data/b706_tool_repairs.txt): ' + vtail(rd('b706_tool_repairs.txt')),
          '    the remote reads this run: %d repositories, one call each in sequence ; empty reads re-read alone: %s' % (
              len(_REMOTE), '; '.join(REREAD) or 'NONE'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b706_author_answers.txt): ' + verdict(rd('b706_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b706_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, SC[k][0][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL (relay data/b706_scores.json, written once before the entry; a reading that waited, from relay '
          'data/b706_scores_close.json):'] + ['    (%s) %s -- %s [%s]' % (k, SC[k][0][0], SC[k][0][1], SC[k][1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b706_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b706_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b706_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+'),
                                       verdict(rd('b706_faces_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b706_faces_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b706_pins_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b706_pins_closing.txt'), encoding='utf-8').read(),
                                    r'REPOS HARD-FAILING : \d+')]
    L += KERNEL_LINES + ['']
    L += ['### CARRIED FORWARD.'] + carried() + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(OUTD, 'b706_closing_dry.txt' if DRY else 'b706_closing.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    if DRY:
        print('  ### THE CLOSING DRY-RUN, its readings (written to the scratchpad, %s):' % p)
        for l in L:
            if l.startswith(('b706 closed', '### THE', '    the', '    (g)')):
                print('    ' + l[:400])
        print('  ### ### **THE CLOSING DRY-RUN : READ**')
    else:
        print(NL.join(L[-60:]))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'defects-row':
        print(defects_row(sys.argv[2]))
    else:
        main()
