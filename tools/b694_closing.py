# -*- coding: utf-8 -*-
"""b694_closing.py -- THE CLOSING RECORD OF b694, UNDER (R304). Carried from b693_closing.py by the Write tool, its act text written for b694,
with ONE repair at carry time in its logic, under (R304)(2) and the author's answer at its prompt (relay data/b694_author_answers.txt, prompt 1;
data/b694_tool_repairs.txt row (1)): every remote read is stored, and every look-up made, under ONE key -- repo_key(), 'D:/' + the repository's
path below the drive -- so D:\\relay (os.path's form, the tool's ROOT), D:/relay (the reads' form) and /d/relay (the push tool's capture form)
resolve to the same reads; b693's row asked under D:\\relay what was stored under D:/relay and printed ABSENT (b693 defect (h)). The `lookup`
route is the repair's control (data/b694_lookup_control.txt). Otherwise as b693's: the remote reads one per call in sequence, an empty read
re-read alone before any row is declared (b674_rules.txt row 1); the tag rows reading a lightweight tag at its own line; each bank's verdict line
and not its title; the citation line from the banks; the captures in b673's form; the defects row read from the bank (b693's repair).
`python tools/b694_closing.py dry` -- (R285)(2)'s rule row (relay data/b675_rules.txt row 1), the closing a gate step before the seal: the record
written to the scratchpad and its readings printed; the censuses run into the scratchpad; no bank of relay data/ written.
`python tools/b694_closing.py lookup` -- the repair's control, (R304)(2) and the author's answer at prompt 6: the three spellings resolving to one
key; the repaired look-up over a read store seeded from b693's banked read-back (relay data/b693_root_branch_push_out.txt :9); the live read; the
planted old key; banked together as data/b694_lookup_control.txt.
`python tools/b694_closing.py defects-row <act>` -- the carried-forward defects row computed from relay data/<act>_defects.txt, printed only.
### Writes data/b694_closing.txt, data/b694_lookup_control.txt and the closing censuses and pins (each its own tool's output) and nothing else.
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
import b694_worklist as WL   # noqa: E402

OUTD = WL.SP if DRY else D

REPOS = ['relay', 'MY-DOwnloads/PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
         'SIDE-effects', 'SIDE-silence-principle', 'SIDE-omega-b', 'SIDE-cosmo', 'SIDE-trivium', 'SIDE-residual-bridge',
         'SIDE-yang-mills-formation', 'SIDE-substrate-cluster', 'SIDE-constants', 'SIDE-simplicity', 'SIDE-bsd-formation-transfer',
         'SIDE-bsd-multiplicity', 'SIDE-t7-topology-cmb', 'SIDE-local-cosmic-interface', 'SIDE-quaternionic-dark-sector', 'SIDE-spinor',
         'SIDE-bijection', 'SIDE-class-coupling', 'SIDE-coupling', 'SIDE-formation-arithmetic', 'SIDE-meta', 'SIDE-orchestrator',
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-grh-transfer', 'SIDE-window', 'SIDE-class-number-anomaly',
         'SIDE-li-map', 'SIDE-rcurve', 'SIDE-archimedean']
SEC, SEC_BRANCH, SEC_TAG = 'D:/SIDE-structural-error-correction', 'sec-axiom-b623', 'v0.2.2'
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603', 'platt-b626', 'cite-b628', 'nb-b629', 'dedekind-b631']
QUARANTINE = ['SIDE-kernel', 'SIDE-lv-conservation']
TAGS = [('SIDE-archimedean', 'v0.1.1'), ('SIDE-archimedean', 'v0.1.0'), ('SIDE-explicit-formula', 'v0.34.1'), ('SIDE-explicit-formula', 'v0.34'), ('SIDE-rcurve', 'v0.1.1'), ('SIDE-rcurve', 'v0.1.0'),
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


# ================================================================================ THE CARRIED-FORWARD DEFECTS ROW (b693's repair, carried)
def _span(letters):
    """consecutive letters joined into runs: a b c e -> (a)–(c), (e)."""
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


def defects_row(act, item='i'):
    """### the carried-forward defects row, its letters read from relay data/<act>_defects.txt through the record tool's defect-row reader
    ### (tools/b693_record.py DEFECT_ROW, imported), each row's kind read from its own head: a ruled exception, the navigator's, the seat's."""
    import b693_record as REC
    L = rd('%s_defects.txt' % act).split(NL)
    rows = [(REC.DEFECT_ROW.match(l).group(1), l) for l in L if REC.DEFECT_ROW.match(l)]
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
    return CARRIED_FIXED[:-1] + [defects_row('b694', 'g')] + CARRIED_FIXED[-1:]


# ================================================================================ THE REMOTE READS, ONE KEY ((R304)(2), THE REPAIR)
_REMOTE = {}
REREAD = []


def repo_key(p):
    """### (R304)(2), the carry-time repair: the one key every remote read is stored and looked up under -- 'D:/' + the repository's path below
    ### the drive, its separators forward. D:\\relay, D:/relay, d:/relay and /d/relay all give 'D:/relay'."""
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
    """### carried from b674's repair: one ls-remote per repository, one call at a time, in sequence; every read that returns empty is re-read
    ### alone after the pass and before any row is declared, and the re-read printed (relay data/b674_rules.txt row 1). Stored under repo_key."""
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


def lookup(*a):
    """the repair's control, banked as data/b694_lookup_control.txt: (1) the three spellings and the key each resolves to; (2) the repaired look-up
    over a read store seeded from b693's banked read-back (data/b693_root_branch_push_out.txt :9), under each spelling; (3) the live read of
    relay's remote for refs/heads/push-b693-root (one ls-remote); (4) the planted old key: b693's look-up, a dict get by the path as passed
    (tools/b693_closing.py :175-:176, :294), over the same seeded store under D:\\relay."""
    import time
    spell = ('D:\\relay', 'D:/relay', '/d/relay')
    cap = rd('b693_root_branch_push_out.txt').split(NL)
    m = re.match(r'^push_gated: branch (\S+) read back at the remote: ([0-9a-f]{40})$', cap[8] if len(cap) > 8 else '')
    if not m or m.group(1) != 'push-b693-root':
        sys.exit('### data/b693_root_branch_push_out.txt :9 IS NOT THE READ-BACK -- NOTHING WRITTEN')
    seeded = {repo_key('D:/relay'): {'refs/heads/push-b693-root': m.group(2)}}
    L = ['b694 -- THE CLOSING TOOL`S LOOK-UP REPAIR: ITS CONTROL, (R304)(2) AND THE AUTHOR`S ANSWERS AT PROMPTS 1 AND 6 (%s)' % time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### rows are prints: the three spellings and their key; the repaired look-up over the store seeded from b693`s banked read-back (relay',
         '### data/b693_root_branch_push_out.txt :9: "%s"), one row per spelling; the live read; the planted old key (b693`s look-up).' % cap[8], '',
         '### (1) THE SPELLINGS: ' + ' ; '.join('%s -> %s' % (s, repo_key(s)) for s in spell) + ' ; ONE KEY %s' % (len(set(repo_key(s) for s in spell)) == 1)]
    _REMOTE.clear()
    _REMOTE.update(seeded)
    ok = []
    for s in spell:
        rb = remote_refs(s).get('refs/heads/push-b693-root', '')
        ok.append(rb == m.group(2))
        L.append('### (2) THE SEEDED STORE, LOOKED UP UNDER %-9s : relay push-b693-root %s ; %s' % (s, rb[:12] or 'ABSENT', 'STANDS' if rb else '### ABSENT'))
    _REMOTE.clear()
    live = _ls('D:/relay')
    lv = live.get('refs/heads/push-b693-root', '')
    L.append('### (3) THE LIVE READ (one ls-remote of relay, %d refs, main %s) : relay push-b693-root %s' % (
        len(live), (live.get('refs/heads/main') or '')[:12], lv[:12] if lv else 'GONE -- deleted at step zero by (R304)(5) (data/b694_branches.txt)'))
    old = dict(seeded).get('D:\\relay', {}).get('refs/heads/push-b693-root', '')
    L.append('### (4) THE PLANTED OLD KEY (b693`s look-up, the path as passed, D:\\relay, over the seeded store) : relay push-b693-root %s ; %s' % (
        old[:12] or 'ABSENT', 'STANDS' if old else 'ABSENT (as b693`s closing printed it, data/b693_closing.txt :226)'))
    good = all(ok) and len(set(repo_key(s) for s in spell)) == 1 and not lv and not old
    L += ['', '### ### **THE THREE SPELLINGS ONE KEY ; THE SEEDED STORE STANDS AT %s UNDER EACH %s ; THE LIVE READ GONE %s ; THE OLD KEY ABSENT %s ; '
          'THE CONTROL AS WANTED %s.**' % (m.group(2)[:8], all(ok), not lv, not old, good)]
    p = os.path.join(D, 'b694_lookup_control.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(NL.join(L[5:]))


ACT = 'b694'
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
    cc, cj, dl = rd('b694_citation_check.txt'), jl('b694_citation_check.json'), rd('b694_defects.txt')
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
    j = jl('b694_mirror.json')
    if not j:
        return '### TO BE BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH (the b670 form, mirror-refresh-%s-b694.zip)' % WL.DATE
    return '%s ; %d bytes ; sha256 %s ; MANIFEST md5 %s ; entries %d ; %s ; %s' % (
        j.get('zip'), j.get('bytes', 0), (j.get('zip_sha256') or '')[:16], j.get('manifest_md5'), j.get('entries', 0), j.get('root_line') or '### NO ROOT LINE',
        'CLEAN ON ALL THREE CLAUSES' if j.get('clean') else '### NOT CLEAN')


def scores_at_close():
    S, C = jl('b694_scores.json'), jl('b694_scores_close.json')
    out = {}
    for ks in SCORE_KEYS:
        for k in ks:
            s = S.get(k) or ['?', '']
            c = C.get(k)
            out[k] = (c, 'close') if (s[0] == 'PENDING' and c) else (s, 'record')
    return out


# ### THE ACT'S OWN LINES, written at Component 4's carry
TITLE_LINE = ('b694 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND TWENTY-ONE, THE RESEARCH ACT: b693 AT ITS WEIGHT; THE CLOSING '
              'TOOL`S LOOKUP REPAIRED; THE DELETES RULE BANKED; THE CIRCUIT READING OVER THE CARRIED FACES KERNELS; THE WEIL-FACE WITNESS AT Q0, '
              'UNDER (R304).**')
ACT_SECTIONS = [
    ('THE CIRCUIT READING ((R304)(3))', [('the closure step', 'b694_closure_step.txt'), ('the dominance', 'b694_circuit_dominance.txt'),
                                         ('the readings again', 'b694_circuit_readings.txt')]),
    ('THE WITNESS AT Q0 ((R304)(4))', [('the plan', 'b694_witness_plan.txt'), ('the amendment', 'b694_witness_plan_amendment.txt'),
                                       ('the concentration', 'b694_witness_concentration.txt'), ('the reading', 'b694_witness.txt'),
                                       ('the controls', 'b694_witness_controls.txt')]),
]
KERNEL_LINES = [
    '    kernel mains written: SIDE-lv-conservation alone -- the closure step d38f3e8 (CircuitClosure.lean at the root and the workflow`s',
    '    closure step) alone on main by push_gated.sh ; no source module, no Zeta23 or vendored byte ; no tag ; the runner dispatched once, read',
    '    by its run id with its artifact`s sha256 checked first ; no lean or lake run on this host ; no worktree made or removed ; no file',
    '    deleted ; the ten (R304)(5) branches deleted at step zero by name, one per command and each its own message, nothing chained after any ;',
    '    b628`s local intake bank, the navigator`s export, b671`s uncompressed points file, b681`s units file and the witness`s units file',
    '    untracked ;',
    '    no identifier of the author in any outbound request or workflow file ; no secret added ; the seat`s plain requests to github.com (its git reads and pushes, its',
    '    one dispatch and its run and artifact reads) the act`s only outbound calls ; the deposit route untouched, publish never called ;',
    '    FINDINGS and OPEN_TRAILS appended ; data/act_roots.txt, the corrigenda bank and the orders bank appended ; no shared tool edited, the',
    '    carry-time repair in this act`s closing tool ; no README, REGISTRY or FOUNDATIONS byte ; no Correspondence cell ; no faces-page byte, the',
    '    witness`s row drafted and held ; the mirror zip written outside every repository ; nothing of TECHNE or any patent written',
]
CARRIED_FIXED = [
    '    (a) ### **THE NEXT ACT, (R304)(8)**: b695, the re-cut act: the licensed table`s next document by b652`s order and b674`s tie-break, rule (2)',
    '        of data/b690_rules.txt binding; the witness`s faces row (relay data/b694_faces_rows.txt) raised there; b696 the research act:',
    '        W-ORD-EPSTEIN-COUNT-LEAN or the regularity-uses bank on the author`s word.',
    '    (b) The orders entered: W-ORD-WITNESS-TAIL-BALLS (OPEN_TRAILS :15166, before any faces-page row carrying the witness is regenerated) and',
    '        W-ORD-B518-FLOAT (OPEN_TRAILS :15168, the reading act b700).',
    '    (c) The faces page (THE_CLAUSE_AND_ITS_COMPILED_FACES.md) carried to its next regeneration, as b693 carried it (test_chain_page.py (1), (14),',
    '        test_g_chain_page.py (1)).',
    '    (d) b628`s full intake bank, the navigator`s export, b671`s uncompressed points file, b681`s units file and data/b694_witness_units.jsonl stay',
    '        local and untracked (the witness`s units carried whole in data/b694_witness.json.gz).',
    '    (e) The act root of b694 is relay data/act_roots.txt`s last line, chained from b693`s root; the mirror export carries it in MANIFEST.',
    '    (f) Branches left for the next act`s step zero: the push-b694* branches of relay and PLACE-papers; SIDE-lv-conservation push-b694-lv-closure',
    '        (local).',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]


def main():
    for tool, out in (('b307_handoff_census.py', 'b694_census_closing.txt'), ('b327_faces_census.py', 'b694_faces_census_closing.txt'),
                      ('b303_pins.py', 'b694_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b694'])
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
    rb = remote_refs(ROOT).get('refs/heads/push-b693-root', '')
    heads.append('      %-32s remote %s ; %s (deleted at step zero by (R304)(5); read under the one key)' % (
        'relay push-b693-root', rb[:12] or 'GONE', '### STANDS' if rb else 'GONE'))
    sb, sm, st = g(SEC, 'rev-parse', 'refs/heads/' + SEC_BRANCH), g(SEC, 'rev-parse', 'main'), g(SEC, 'rev-parse', SEC_TAG + '^{commit}')
    srt, skind = remote_tag(SEC, SEC_TAG)
    heads.append('      %-32s local %s ; %s peeled %s, at the remote %s (%s) ; main %s (unmoved by this act) ; %s (kept, local)' % (
        SEC_BRANCH, sb[:12], SEC_TAG, st[:12], srt[:12], skind, sm[:12], 'AGREE' if sb and sb == st == srt else '### DIFFER'))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED, NOT WRITTEN BY THIS ACT' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?'))
    SC = scores_at_close()
    pre, post = rd('b694_checks.txt'), rd('b694_checks_postpush.txt')
    L = [head_line(), '=' * 104, TITLE_LINE, '=' * 104]
    rec_ = jl('b694_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in getattr(WL, 'SEALED', ()):
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b694_seal_hashes.json; the repaired '
          'tool among them):'] + [
        '      %-30s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step at step zero; relay data/b694_citation_check.txt): ' + citation_line(), '']
    RL = jl('b694_record_lines.json').get('lines') or []
    CL = jl('b694_corrigendum_landing.json').get('lines') or []
    L += ['### THE RECORD LINES ((R304)(1)-(2); relay data/b694_record_lines.json, data/b694_corrigendum_landing.json): ' + ' ; '.join(
        '%s :%s' % (x.get('file'), x.get('line')) for x in RL + CL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b694_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b694_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+') + ' ; THE CLOSING`S DRY RUN (relay data/b675_rules.txt row 1): ' + verdict(
        rd('b694_reg_gate.txt'), r'THE CLOSING DRY-RUN STEP : [A-Z ]+'), '']
    L += ['### THE CORRIGENDUM AND THE REPAIR ((R304)(2)): the corrigendum (relay data/b694_corrigendum.txt): ' + vline(rd('b694_corrigendum.txt')),
          '    the look-up`s control (relay data/b694_lookup_control.txt): ' + vline(rd('b694_lookup_control.txt')), '']
    for title, rows in ACT_SECTIONS:
        L += ['### %s:' % title] + ['    %s (relay data/%s): %s' % (lab, bk, vtail(rd(bk))) for lab, bk in rows] + ['']
    L += ['### THE KERNELS: the face`s reading of the kernels (relay data/b694_kernels_face.json): %d kernels read before the seal' % len(
        jl('b694_kernels_face.json').get('kernels') or {}), '']
    L += ['### THE ROOT`S BANKS (relay data/b694_root_banks.txt): ' + (
        vline(rd('b694_root_banks.txt')) if rd('b694_root_banks.txt') else 'TO BE READ AT THE ROOT, before it is computed'), '']
    L += ['### THE MIRROR (relay data/b694_mirror.txt, the b670 form, after the root and the last PLACE-papers push): ' + mirror_line(), '']
    L += ['### THE CARRY-TIME READING (the ferry`s Component 4; relay data/b694_tool_repairs.txt): ' + vline(rd('b694_tool_repairs.txt')),
          '    the remote reads this run: %d repositories, one call each in sequence ; empty reads re-read alone: %s' % (
              len(_REMOTE), '; '.join(REREAD) or 'NONE'), '']
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b694_author_answers.txt): ' + verdict(rd('b694_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b694_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, SC[k][0][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL (relay data/b694_scores.json, written once before the entry; a reading that waited, from relay '
          'data/b694_scores_close.json):'] + ['    (%s) %s -- %s [%s]' % (k, SC[k][0][0], SC[k][0][1], SC[k][1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b694_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b694_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b694_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+'),
                                       verdict(rd('b694_faces_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b694_faces_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b694_pins_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b694_pins_closing.txt'), encoding='utf-8').read(),
                                    r'REPOS HARD-FAILING : \d+')]
    L += KERNEL_LINES + ['']
    L += ['### CARRIED FORWARD.'] + carried() + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(OUTD, 'b694_closing_dry.txt' if DRY else 'b694_closing.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    if DRY:
        print('  ### THE CLOSING DRY-RUN, its readings (written to the scratchpad, %s):' % p)
        for l in L:
            if l.startswith(('b694 closed', '### THE', '    the', '      relay push-b693-root', '    (g)')):
                print('    ' + l[:400])
        print('  ### ### **THE CLOSING DRY-RUN : READ**')
    else:
        print(NL.join(L[-60:]))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'defects-row':
        print(defects_row(sys.argv[2]))
    elif len(sys.argv) > 1 and sys.argv[1] == 'lookup':
        lookup()
    else:
        main()
