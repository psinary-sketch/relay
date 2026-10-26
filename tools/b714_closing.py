# -*- coding: utf-8 -*-
"""b714_closing.py -- THE CLOSING RECORD OF b714, UNDER (R324). Carried from b713_closing.py by tools/b714_carry.py (the act names substituted,
data/b713_rules.txt row (1)), its act sections written for b714 by the Edit tool: the remote reads stored and looked up under ONE key (repo_key(),
b694's repair, carried); the remote reads one per call in sequence, an empty read re-read alone before any row is declared (b674_rules.txt row 1);
the tag rows reading a lightweight tag at its own line; each bank's verdict line and not its title; the citation line from the banks; the captures
in b673's form; the defects row read from the bank (b693's repair); the head line's prompt count the answers bank's rows with nothing added and
its scores from the scores-close bank ((R324)(3)(iii), replacing b700's repair (9)), its defect count the defects bank's lettered rows read now;
the mirror line's sentence on the builder's state file read from its blob against its last commit ((R324)(3)(v)). The act's sections (Component 5, by the Edit
tool) are the record lines, the corrigendum and the repairs, the standing clauses at v5 and the hook, the tier moves (the lv tag, the re-cut's
merge), the head of the re-cut, the law, the residual, the rectangle, the Sonin price, the pilot and the standing arms; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the pilot in one line (the author's word (2)); the carried items
naming the SIDESystem finding and the nineteen NO PIN STATED names by keystone, file and line for b715 (the author's word (4)). The standing report
prints its lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD) from the bank the unsealed report tool writes before the root, its scores
line printed after the root by the tool's scores route and written nowhere. No kernel written this act: SIDE-lv-conservation's port branch given
the annotated tag v0.14.0 at cb0aea56 (tier one); lv-conservation's main and deposit, SIDE-faces-join and SIDE-explicit-formula read unmoved.
`python tools/b714_closing.py dry` -- (R285)(2)'s rule row (relay data/b675_rules.txt row 1), the closing a gate step before the seal: the record
written to the scratchpad and its readings printed; the censuses run into the scratchpad; no bank of relay data/ written.
`python tools/b714_closing.py defects-row <act>` -- the carried-forward defects row computed from relay data/<act>_defects.txt, printed only.
### Writes data/b714_closing.txt and the closing censuses and pins (each its own tool's output) and nothing else.
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
import b714_worklist as WL   # noqa: E402

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
              ('SIDE-lv-conservation', 'v0.14.0'), ('SIDE-lv-conservation', 'v0.13.0'), ('SIDE-lv-conservation', 'v0.10.0'), ('SIDE-global-section', 'v0.3.0'), ('SIDE-kernel', 'v1.8')]
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
    """the fixed list with this act's one tag, SIDE-lv-conservation v0.14.0 at port-b707's tip ((R324)(3)(i)); no kernel written; no main moved."""
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


PILOT_KEYSTONE = re.compile(r'^  ### (day1/\S+) -- its Correspondence')
PILOT_NOPIN = re.compile(r'^    :(\d+) +(\S+) +\| NO PIN STATED')


def nopin_rows(text=None):
    """the author's word (4)(3): the names the pilot read with NO PIN STATED (relay data/b714_pilot.txt (P1)), each by keystone, file and line:
    [(keystone, line, name)], in the bank's order."""
    out, cur = [], None
    for l in (rd('%s_pilot.txt' % ACT) if text is None else text).split(NL):
        m = PILOT_KEYSTONE.match(l)
        if m:
            cur = m.group(1)
            continue
        n = PILOT_NOPIN.match(l)
        if n and cur:
            out.append((cur, int(n.group(1)), n.group(2)))
    return out


def carried():
    rows = nopin_rows()
    by = []
    for k in dict.fromkeys(r[0] for r in rows):
        by.append('%s %s' % (k, ', '.join(':%d `%s`' % (n, x) for kk, n, x in rows if kk == k)))
    pin = ['    (i) The %d names with NO PIN STATED (relay data/b714_pilot.txt (P1); the author`s word (4)(3)), for b715: each Correspondence row' % len(rows),
           '        gains its repository and pin, read from the census at its current edition on main -- ' + '; '.join(by) + '.']
    return CARRIED_FIXED[:-1] + [defects_row(ACT, 'g')] + CARRIED_FIXED[-1:] + pin


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


ACT = 'b714'
CAPTURES = (('relay', 'relay', ROOT), ('PLACE-papers', 'pp', 'D:/MY-DOwnloads/PLACE-papers'))


# ### (R324)(2)(k), a carry-time repair: the head-line builder's capture-name failures go to the events section (events_section) and never into
# ### the head line; filled at each head_line call and read by the section beneath the defects.
HEAD_EVENTS = []


def _captures(dd, act):
    """every push capture of the act but the closing's own (data/<act>_*push_out.txt), each read by its own lines: (name, its UTC stamp at :1,
    the repository at :2, the branch, the tip, the main read back at the remote)."""
    out = []
    for n in sorted(os.listdir(dd)):
        if not (n.startswith(act + '_') and n.endswith('push_out.txt')) or n == '%s_closing_push_out.txt' % act:
            continue
        t = io.open(os.path.join(dd, n), encoding='utf-8', errors='replace').read().replace(chr(13), '')
        s = re.search(r'^push_gated: capture on -> \S+ \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', t, re.M)
        b = re.search(r'^push_gated: repo (\S+) ; branch (\S+) ; tip (\w+)', t, re.M)
        m = re.search(r'^push_gated: main read back at the remote: (\w+)', t, re.M)
        out.append((n, s.group(1) if s else None, b.group(1) if b else None, b.group(2) if b else None, b.group(3) if b else None,
                    m.group(1) if m else None))
    return out


def head_line(dd=None, act=ACT, events=None):
    """(R324)(2)(k), repaired: each repository's record commit is the main its LAST push capture of the act read back at the remote (the
    closing's own capture excluded, the captures ordered by their own UTC stamps), printed in the head line; where b673's name for the record's
    capture (data/<act>_<key>_push_out.txt) is not that capture, or no capture reads main back, the failure goes to the events section and the
    head line carries the commit or `none read`, never the failure's text (b713's head line carried "IS NOT THE RECORD`S CAPTURE" for both)."""
    dd = dd or D
    ev = HEAD_EVENTS if events is None else events

    def _t(n):
        p = os.path.join(dd, n)
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''

    # ### (R324)(4)(v), standing clauses v4 row (66): THE HEAD LINE READS EACH REPOSITORY'S MAIN AT THE REMOTE by ls-remote (one read per
    # ### repository, an empty read re-read alone), not from the act's push captures -- b713 wrote no capture but the closing's, and its head line
    # ### read "none read" for both (events :48). The captures are still read, and a remote main no capture of the act read back goes to the
    # ### events section (a repair at b714, banked by diff).
    caps = _captures(dd, act)
    read_remotes([repo for _n, _k, repo in CAPTURES])
    parts = []
    for name, key, repo in CAPTURES:
        w = 8 if key == 'relay' else 7
        main = remote_refs(repo).get('refs/heads/main', '')
        if not main:
            ev.append('%s: ls-remote read no main at the remote, read twice; the head line carries none read' % name)
            parts.append('%s none read' % name)
            continue
        mine = [c for c in caps if c[2] and c[5] and repo_key(c[2]) == repo_key(repo)]
        if not any(c[5] == main for c in mine):
            ev.append('%s: the remote`s main %s is read back by no push capture of the act (%d captures of the repository)' % (name, main[:w], len(mine)))
        parts.append('%s %s' % (name, main[:w]))
    sm = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', _t('%s_checks_postpush.txt' % act))
    suite = ('suite %s of %s' % (sm.group(2), sm.group(1))) if sm else 'suite ### NOT READ'
    try:
        root = json.loads(_t('%s_act_root.json' % act))['root'][:16] + '…'
    except Exception:
        root = '### NOT READ'
    # ### (R324)(3)(iii), standing clauses v3: the prompt count is the answers bank's rows with nothing added (b700's "+ 1" for the root's
    # ### prompt counted it twice where the bank already holds it, b713's events :79), and the scores are read from the scores-close bank
    k = len(re.findall(r'^### PROMPT ', _t('%s_author_answers.txt' % act), re.M))
    d = len([l for l in _t('%s_defects.txt' % act).split(NL) if DEFECT_ROW.match(l)])
    try:
        sc = json.loads(_t('%s_scores_close.json' % act))
    except Exception:
        sc = {}
    keys = [x for ks in SCORE_KEYS for x in ks]
    held = sum(1 for x in keys if (sc.get(x) or [''])[0] == 'HELD')
    scores = ('scores %d of %d HELD' % (held, len(keys))) if all(x in sc for x in keys) else 'scores ### NOT READ'
    return '%s closed: %s; %s; root %s; %d prompt%s answered; %s; %d defect%s' % (act, ', '.join(parts), suite, root, k, '' if k == 1 else 's',
                                                                                 scores, d, '' if d == 1 else 's')


def events_section(act=ACT, dd=None):
    """(R324)(2)(i), standing clauses v2 row (52): a finding made after the seal is entered here and not lettered in the defects bank (the next
    act's corrigendum letters it) -- the rows of data/<act>_events.txt as the seat entered them (by the Write or the Edit tool; every line of
    the bank from its third, indented), and the head-line builder's capture-name failures (HEAD_EVENTS)."""
    p = os.path.join(dd or D, '%s_events.txt' % act)
    t = io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''
    rows = [l for l in t.split(NL)[2:] if l.startswith('    ')]
    return ['### THE EVENTS AFTER THE SEAL (standing clauses v2 row (52); relay data/%s_events.txt, unlettered, for the next act`s corrigendum):' % act] + (
        rows or ['    NONE ENTERED IN THE EVENTS BANK']) + ['    THE HEAD LINE: ' + e for e in HEAD_EVENTS] + [
        '    ### EVENTS %d ; THE HEAD LINE`S %d' % (len([l for l in rows if not l.startswith('     ')]), len(HEAD_EVENTS))]


def citation_line():
    cc, cj, dl = rd('b714_citation_check.txt'), jl('b714_citation_check.json'), rd('b714_defects.txt')
    head = verdict(cc, r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+')
    misses = cj.get('misses') or []
    needles = re.findall(r"^### \(R278\)\(4\) THE MID-ACT CHECK \([^)]*\): the (?:navigator`s )?answer carrying '([^']*)'", cc, re.M)
    figs = re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', cc)
    nav = re.findall(r"^    \(([a-z]'?)\) THE NAVIGATOR'S", dl, re.M)
    return ('%s ; the misses as the bank lists them: %d (%s) ; the answers checked ((R278)(4)), by their needles: %s, the prints %s ; entered as '
            'the defects bank letters them: the navigator`s %s' % (
                head, len(misses), '; '.join(str(m)[:60] for m in misses) or 'NONE', '; '.join(needles) or 'NONE', '; '.join(figs) or 'NONE',
                ', '.join('(%s)' % x for x in nav) or 'NONE'))


def state_file_sentence(path='tools/mirror_prevbuild.json', repo=ROOT):
    """(R324)(3)(v): the closing's sentence about a state file read from its blob against the last commit before it says "committed": the
    working file's blob (git hash-object) against HEAD's blob of the path and the last commit that touched it."""
    work = g(repo, 'hash-object', '--', path).strip()
    head = g(repo, 'rev-parse', '--verify', '--quiet', 'HEAD:' + path).strip()
    last = g(repo, 'log', '-1', '--format=%h %s', '--', path).strip()
    if work and head and work == head:
        return '%s unchanged since its last commit %s (blob %s, equal at HEAD and in the working tree), not committed with this closing' % (
            path, last[:8] or '### NONE', work[:8])
    return '%s written at the build (blob %s, HEAD`s %s), committed with this closing' % (path, work[:8] or '### NONE', head[:8] or '### NONE')


def mirror_line():
    j = jl('b714_mirror.json')
    if not j:
        return '### TO BE BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH (the b670 form, mirror-refresh-%s-b714.zip; over b713`s roster of 70 entries, the builder`s state file tools/mirror_prevbuild.json named in (W))' % WL.DATE
    return '%s ; %d bytes ; sha256 %s ; MANIFEST md5 %s ; entries %d ; %s ; %s ; %s ; the roster b713`s, 70 entries; %s' % (
        j.get('zip'), j.get('bytes', 0), (j.get('zip_sha256') or '')[:16], j.get('manifest_md5'), j.get('entries', 0), j.get('root_line') or '### NO ROOT LINE',
        'CLEAN ON ALL THREE CLAUSES' if j.get('clean') else '### NOT CLEAN', j.get('span') or '### NO SPAN LINE', state_file_sentence())


def scores_at_close():
    S, C = jl('b714_scores.json'), jl('b714_scores_close.json')
    out = {}
    for ks in SCORE_KEYS:
        for k in ks:
            s = S.get(k) or ['?', '']
            c = C.get(k)
            out[k] = (c, 'close') if (s[0] == 'PENDING' and c) else (s, 'record')
    return out


# ================================================================================ THE STANDING REPORT ((R324)(3): its lines in footing order, from the unsealed report tool's bank)
def report_lines():
    rj = jl('b714_report.json')
    ls = rj.get('lines') or []
    if len(ls) >= 9:
        return ['### THE STANDING REPORT ((R324)(3), its lines in footing order KERNEL, CERTIFIED, REGISTERED, HELD; relay data/b714_report.txt, by the unsealed tools/b714_report.py before the root; its scores line printed after the root by `tools/b714_report.py scores`, written nowhere):'] + [
            '    (%d) %s' % (i + 1, l[:900]) for i, l in enumerate(ls)]
    return ['### THE STANDING REPORT ((R324)(3)): ### data/b714_report.txt NOT YET WRITTEN (tools/b714_report.py bank runs before the root)']


TITLE_LINE = ('b714 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND FORTY-ONE, THE KEYSTONE HEADS ACT: b713 AT ITS WEIGHT; THE TIERS AND '
              'THE VISIBILITY MAP; THE lv TAG AND THE RE-CUT`S MERGE; THE HEAD OF THE RE-CUT; THE CORRIGENDUM WITH NEW AND REPEAT; THE STANDING CLAUSES AT '
              'v5; THE LAW`S IDENTITY; THE RESIDUAL; PAIR 7`S RECTANGLE; THE SONIN PRICE; THE PILOT, UNDER (R324).**')
# ### the banks below carry no verdict line BY THEIR FORM; the closing prints "### NO VERDICT LINE" for them, and the suite`s G-CLOSING-DRY-STEP
# ### reads each such bank itself ((R324)(2)(iii): the line passes where the bank exists and carries no verdict line by this tool`s own reader,
# ### tools/b714_checks.py no_verdict_line_ok; no list of names). None this act: every bank below carries its verdict line.
NO_VERDICT_BY_FORM = ()


def act_sections():
    return [('THE CORRIGENDUM AND THE REPAIRS ((R324)(5)-(6))', [
                ('the generated entry for b713`s post-seal items, NEW and REPEAT, and the corrigenda row (34)', 'b714_corrigendum.txt'),
                ('the repairs: three tools repaired, four new', 'b714_tool_repairs.txt'),
                ('the repairs` two-instance controls, 11 cases', 'b714_repair_controls.txt'),
                ('the root route`s dry run on the pre-root tree (data/b706_rules.txt row (1))', 'b714_root_banks_dry.txt')]),
            ('THE STANDING CLAUSES AND THE HOOK ((R324)(2), (6))', [('v5 written at step zero, v4`s rows unchanged, the deltas` control', 'b714_standing_control.txt'),
                                                                   ('the hook`s offline control ((R324)(6)(iv))', 'b714_hook_control.txt')]),
            ('THE TIER MOVES ((R324)(3))', [('(i) the lv port`s tag on the author`s word, v0.11.0 taken', 'b714_lv_tag.txt'),
                                            ('(ii) the re-cut merged into main, the additive check on main', 'b714_recut_additive.txt')]),
            ('THE HEAD OF THE RE-CUT ((R324)(4))', [('the keystone head redrafted, footed and held for the root`s prompt', 'b714_heads_draft.txt')]),
            ('THE READINGS ((R324)(7)-(10), N3)', [('(7) the law`s identity, read first, its controls before its figures', 'b714_law.txt'),
                                                   ('(8) the residual over b713`s onsets, no onset computed', 'b714_residual.txt'),
                                                   ('(9) pair 7`s rectangle in Re s > 1', 'b714_rect.txt'),
                                                   ('(10) the Sonin face priced as a restriction', 'b714_sonin_price.txt')]),
            ('THE PILOT (the author`s word (2))', [('(P1) declarations, (P2) prose lint, (P3) a blueprint`s price', 'b714_pilot.txt')]),
            ('THE STANDING ARMS', [('the four figures against b713`s, read by b706`s tool', 'b714_standing_figures.txt')])]


KERNEL_LINES = [
    '    kernels written: none -- port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT and not deleted, local and remote, no commit',
    '    this act; tagged v0.14.0 there, annotated (tier one, (R324)(3)(i), on the author`s word: v0.11.0 taken), its peel read back, no GitHub',
    '    release ; SIDE-lv-conservation`s main and its deposit v0.10.0 unmoved ; SIDE-faces-join`s main 11a472b9 with its one tag v0.1.0 unmoved ;',
    '    SIDE-explicit-formula`s main at badaccc unmoved, every tag unmoved ; N1: no runner dispatch and no lean process on this host ; the five',
    '    push-b713* branches of relay and PLACE-papers deleted at step zero by name, one per command and each its own message, nothing chained',
    '    after any ; no toolchain, workflow or manifest of a kernel written ; nothing vendored ; no worktree made or removed ; b628`s local intake',
    '    bank, the navigator`s export, b671`s uncompressed points file, the earlier acts` units files and b714`s rectangle units file untracked ;',
    '    no identifier of the author in any outbound request header, URL, input or payload, or in any workflow file ; no secret added ; the',
    '    seat`s plain requests to github.com (its git reads and pushes) and the one release listing read by gh at the tag the act`s outbound',
    '    calls ; the deposit route untouched, publish never called ; FINDINGS and OPEN_TRAILS appended ; recut-b712-silence merged into PLACE-papers',
    '    main at a86c9429 ((R324)(3)(ii), tier two), the branch kept until b715`s step zero ; the head of day1/Silence_of_Foundations.md written',
    '    on main only on the author`s word before the root ((R324)(4)) ; no other paper cut, written, moved or renamed ; data/act_roots.txt and the',
    '    corrigenda bank appended ; the shared banks data/standing_clauses_v5.txt and data/repo_visibility.txt written ((R324)(2), (6)), named in',
    '    (W) ; the shared tools tools/act_close.py and tools/push_gated.sh repaired and tools/act_letters.py new, named in (W) ; the hook set in',
    '    D:/.claude/settings.json ((R324)(6)(iv)) ; no REGISTRY byte ; no FOUNDATIONS byte ; no README or faces page byte ; the mirror zip written',
    '    outside every repository over b713`s roster, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ;',
    '    nothing of TECHNE or any patent written',
]
CARRIED_FIXED = [
    '    (a) ### **THE NEXT ACT, (R324)(14)**: b715, the registrations act: the composition law for the least negative index sharpened from',
    '        n = 24 and n = 48 and their exponents, registered with its falsifier for discriminant -39 and priced; a residual law registered from',
    '        (R324)(8) where its reading supports one; the Sonin restriction compiled where (R324)(10) prices it within one act.',
    '    (b) The orders: W-ORD-LV-PORT-TAG DISCHARGED at v0.14.0 ((R324)(3)(i)); W-ORD-KEYSTONE-HEADS (the head on the author`s word);',
    '        W-ORD-LV-FORWARD-PORT; W-ORD-LV-CLOSURE-JOIN; W-ORD-Q0-ZEROS-443; W-ORD-READING5-INDEPENDENCE; W-ORD-MOVES-BY-LOCUS;',
    '        W-ORD-ENTRY-TAG-PRINTS; W-ORD-EXPLICIT-FORMULA-C1; W-ORD-EPSTEIN-COUNT-LEAN; W-ORD-QUASI-RH-FIELD-WATCH; W-ORD-P3-CONTOUR-SIGMA;',
    '        W-ORD-E0-MET-CLASSK; W-ORD-README-FIGURE-SCOPE. Entered this act: none.',
    '    (c) For b715 on the author`s word (4): the word on the six FOR THE AUTHOR lint hits of the pilot`s (P2), banked in relay',
    '        data/b714_author_words.txt and applied in b715, not in this act; the SIDESystem finding (relay data/b714_pilot.txt :20-:21):',
    '        Silence_of_Foundations` Correspondence row at :212 names SIDE-kernel where the declaration is SIDEMeta/Meta/SIDESystem.lean :99 in',
    '        SIDE-meta, and names a typeclass where the declaration is a structure -- the row not edited in this act; the second-order term of',
    '        the residual ((R324)(8)) named for registration at b715 and not computed here; THE_UNCONDITIONAL_SURROUND :183 (phase1.5/proofs),',
    '        pinned at SIDE-lv-conservation v0.13.0, whose `T3_perClass_to_combinations` reads a changed statement at the tag v0.14.0 (the',
    '        Correspondence figure 1, relay data/b714_records.txt (9)) -- the row restated at v0.14.0 or its pin kept, on the author`s word; the',
    '        report tool outside the sealed list; the draft held at v5.',
    '    (d) b628`s full intake bank, the navigator`s export, b671`s uncompressed points file, b681`s units file, data/b694_witness_units.jsonl,',
    '        data/b696_witness_balls_units.jsonl, data/b707_onset_units.jsonl, b709`s grid and pairs units files, b711`s and b713`s units files,',
    '        b714`s rectangle units file and its record tool`s hashes bank (declared in their tools` heads) and the zero-byte `=` at relay`s root',
    '        stay local and untracked.',
    '    (e) The act root of b714 is relay data/act_roots.txt`s last line, chained from b713`s root; the mirror export carries it in MANIFEST.',
    '    (f) Branches left for the next act`s step zero: the push-b714* branches of relay and PLACE-papers, and recut-b712-silence of',
    '        PLACE-papers (merged at a86c9429, kept until b715`s step zero by (R324)(3)(ii)). KEPT, not for deletion: port-b707 of',
    '        SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0).',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]


def _guard(name):
    """(R324)(2)(ii), standing clauses v2 row (53), the membrane: a write to relay data/ refused once the act's root is appended, unless the
    act's ROOT_EXCLUDE takes the bank out (the closing's banks, its censuses and pins are excluded kinds); the dry run writes to the scratchpad."""
    if DRY:
        return
    import act_membrane as MEM
    import b714_record as REC
    MEM.guard(ACT, name, REC.R.ROOT_EXCLUDE)


def main():
    for tool, out in (('b307_handoff_census.py', 'b714_census_closing.txt'), ('b327_faces_census.py', 'b714_faces_census_closing.txt'),
                      ('b303_pins.py', 'b714_pins_closing.txt')):
        _guard(out)
        rc, o = run([sys.executable, os.path.join(T, tool), ACT])
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
    heads.append('      %-32s local %s ; remote %s ; %s (the forward-port`s branch, KEPT under (R324)(11): b712`s tip %s, no commit this act, tagged %s)' % (
        WL.PORT_BRANCH, pl[:12] or 'absent', pr[:12] or 'absent', 'AGREE' if pl and pl == pr == WL.PORT_NEW_TIP else '### DIFFER', WL.PORT_TIP[:8], WL.LV_TAG))
    PP_ = 'D:/MY-DOwnloads/PLACE-papers'
    rl_ = g(PP_, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + WL.RECUT_BRANCH)
    rr_ = remote_refs(PP_).get('refs/heads/' + WL.RECUT_BRANCH, '')
    mp_ = g(PP_, 'rev-parse', WL.C2_PP_MERGE + '^2')
    heads.append('      %-32s local %s ; remote %s ; %s (the re-cut, MERGED into main at %s, its second parent %s; kept until b715`s step zero, (R324)(3)(ii))' % (
        WL.RECUT_BRANCH, rl_[:12] or 'absent', rr_[:12] or 'absent', 'AGREE' if rl_ and rl_ == rr_ == WL.RECUT_TIP == mp_ else '### DIFFER',
        WL.C2_PP_MERGE[:8], mp_[:8] or '-'))
    jt = g('D:/SIDE-faces-join', 'tag', '--list')
    jr = [x for x in remote_refs('D:/SIDE-faces-join') if x.startswith('refs/tags/')]
    jp = g('D:/SIDE-faces-join', 'rev-parse', WL.JOIN_TAG[0] + '^{commit}')
    heads.append('      %-32s tags local %s ; at the remote %s ; %s peeled %s ; %s (the join`s tag, b712`s, unmoved)' % (
        'SIDE-faces-join', jt.split() or 'NONE', jr or 'NONE', WL.JOIN_TAG[0], jp[:12] or '-',
        'AGREE' if jt.split() == [WL.JOIN_TAG[0]] and jp == WL.JOIN_TAG[2] and ('refs/tags/' + WL.JOIN_TAG[0]) in jr else '### DIFFER'))
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
    pre, post = rd('b714_checks.txt'), rd('b714_checks_postpush.txt')
    L = [head_line(), '=' * 104, TITLE_LINE, '=' * 104]
    rec_ = jl('b714_seal_hashes.json').get('tools') or {}
    seal = []
    for t_ in getattr(WL, 'SEALED', ()):
        p_ = os.path.join(T, t_)
        now = hashlib.sha256(open(p_, 'rb').read()).hexdigest() if os.path.exists(p_) else None
        seal.append((t_, rec_.get(t_), now, 'ABSENT' if (now is None or t_ not in rec_) else ('AGREE' if rec_[t_] == now else '### DIFFER')))
    L += ['### THE SEALED TOOLS` HASHES AT THE CLOSE (OPEN_TRAILS :13307; recorded at the seal, relay data/b714_seal_hashes.json; the report tool unsealed by data/b708_rules.txt row (1)):'] + [
        '      %-30s seal %s ; close %s ; %s' % (t_, (a_ or '-')[:16], (b_ or '-')[:16], v) for t_, a_, b_, v in seal] + [
        '      ### AGREE %d of %d' % (sum(1 for x in seal if x[3] == 'AGREE'), len(seal)), '']
    L += ['### THE CITATION CHECK (the gate step at step zero; relay data/b714_citation_check.txt): ' + citation_line(), '']
    RL = jl('b714_record_lines.json').get('lines') or []
    L += ['### THE RECORD LINES ((R324)(1); relay data/b714_record_lines.json): ' + ' ; '.join('%s :%s' % (x.get('file'), x.get('line')) for x in RL), '']
    L += ['### THE DRY RUN ((R267)(2), standing; relay data/b714_reg_gate.txt, the gate`s step before the lock): ' + verdict(
        rd('b714_reg_gate.txt'), r'THE DRY-RUN STEP : [A-Z ]+') + ' ; THE TRAIL`S DEFECTS LINE AGAINST THE BANK: ' + verdict(
        rd('b714_reg_gate.txt'), r'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK \w+') + ' ; THE TRAIL`S RESOLVED LINE AGAINST THE BANK: ' + verdict(
        rd('b714_reg_gate.txt'), r'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK \w+') + ' ; THE CLOSING`S DRY RUN (relay data/b675_rules.txt row 1): ' + verdict(
        rd('b714_reg_gate.txt'), r'THE CLOSING DRY-RUN STEP : [A-Z ]+'), '']
    for title, rows in act_sections():
        L += ['### %s:' % title] + ['    %s (relay data/%s): %s' % (lab, bk, vtail(rd(bk))) for lab, bk in rows]
        L += ['']
    L += report_lines() + ['']
    L += ['### THE KERNELS: the face`s reading of the kernels (relay data/b714_kernels_face.json): %d kernels read before the seal, none written '
          '; SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, no scratch branch ; SIDE-lv-conservation main %s (unmoved), '
          'v0.10.0 %s (the deposit), port-b707 %s (b712`s tip, KEPT, no commit this act), %s peeled %s (the act`s tag) ; SIDE-faces-join main %s '
          '(unmoved), its tag v0.1.0 unmoved' % (
              len(jl('b714_kernels_face.json').get('kernels') or {}), g('D:/SIDE-explicit-formula', 'rev-parse', 'main')[:12],
              g('D:/SIDE-explicit-formula', 'rev-parse', 'v0.37^{commit}')[:12], g('D:/SIDE-explicit-formula', 'rev-parse', 'v0.17^{commit}')[:12],
              g('D:/SIDE-lv-conservation', 'rev-parse', 'main')[:12], g('D:/SIDE-lv-conservation', 'rev-parse', 'v0.10.0^{commit}')[:12], pl[:12] or '-',
              WL.LV_TAG, g('D:/SIDE-lv-conservation', 'rev-parse', WL.LV_TAG + '^{commit}')[:12], g('D:/SIDE-faces-join', 'rev-parse', 'main')[:12]), '']
    L += ['### THE ROOT`S BANKS (relay data/b714_root_banks.txt): ' + (
        vline(rd('b714_root_banks.txt')) if rd('b714_root_banks.txt') else 'TO BE READ AT THE ROOT, before it is computed'), '']
    L += ['### THE MIRROR (relay data/b714_mirror.txt, the b670 form, after the root and the last PLACE-papers push): ' + mirror_line(), '']
    L += ['### THE CARRY-TIME READING (the ferry`s Component 5; relay data/b714_tool_repairs.txt): ' + vtail(rd('b714_tool_repairs.txt')),
          '    the remote reads this run: %d repositories, one call each in sequence ; empty reads re-read alone: %s' % (
              len(_REMOTE), '; '.join(REREAD) or 'NONE'), '']
    import act_close as AC0
    import b714_record as REC_
    L += ['### THE PILOT, IN ONE LINE (the author`s word (2)): ' + REC_.pilot_line(), '']
    L += AC0.author_words_section(ACT) + ['']   # ### (R324)(6)(i), v5 row (74): the author's word after the seal, from its bank
    L += ['### THE AUTHOR`S ANSWERS AND WORDS (relay data/b714_author_answers.txt): ' + verdict(rd('b714_author_answers.txt'), r'\d+ prompt\(s\)[^;]*')]
    L += ['    ' + l for l in rd('b714_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, SC[k][0][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THE SCORES IN FULL (relay data/b714_scores.json, written once before the entry; a reading that waited, from relay '
          'data/b714_scores_close.json):'] + ['    (%s) %s -- %s [%s]' % (k, SC[k][0][0], SC[k][0][1], SC[k][1]) for ks in SCORE_KEYS for k in ks] + ['']
    L += ['### THIS ACT`S DEFECTS (the desk), THE SEAT`S AND THE NAVIGATOR`S.'] + rd('b714_defects.txt').rstrip(NL).split(NL) + ['']
    L += events_section() + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b714_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b714_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+'),
                                       verdict(rd('b714_faces_census_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b714_faces_census_closing.txt'), encoding='utf-8').read(),
                                               r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b714_pins_closing.txt') if not DRY else io.open(os.path.join(OUTD, 'b714_pins_closing.txt'), encoding='utf-8').read(),
                                    r'REPOS HARD-FAILING : \d+')]
    L += KERNEL_LINES + ['']
    L += ['### CARRIED FORWARD.'] + carried() + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    _guard('b714_closing.txt')
    # ### (R324)(4)(iv) and (vi), standing clauses v4 rows (65) and (68), a repair at b714: the dry run is step [3] of the close's order and
    # ### writes its bank to relay data/ (b713 wrote it to the scratchpad, so its order left no evidence of the step), refused once the lock
    # ### is written; the closing is step [25], refused while a lower step's evidence is absent
    import act_close as AC
    r = AC.lock_refuses(ACT, 'b714_closing_dry.txt') if DRY else AC.close_refuses(ACT, 25)
    if r:
        print(r, flush=True)
        sys.exit(5)
    p = os.path.join(D, 'b714_closing_dry.txt') if DRY else os.path.join(OUTD, 'b714_closing.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    if DRY:
        print('  ### THE CLOSING DRY-RUN, its readings (written to relay data/, %s):' % p)
        for l in L:
            if l.startswith(('b714 closed', '### THE', '    the', '    (g)')):
                print('    ' + l[:400])
        print('  ### ### **THE CLOSING DRY-RUN : READ**')
    else:
        print(NL.join(L[-60:]))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'defects-row':
        print(defects_row(sys.argv[2]))
    else:
        main()
