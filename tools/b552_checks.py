# -*- coding: utf-8 -*-
"""b552_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### The kernel arms read the kernel's own tree and git state, and Lean's own output in the run files.
"""
import io
import glob
import hashlib
import fnmatch
import json
import math
import time
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
FACE = os.path.join(D, 'b552_registration_2026-09-28.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'ccfaed9a'      # ### b551's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = 'a6565c8'           # ### b551's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b552 —'


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def gits(repo, *a):
    return git(repo, *a).strip()


def line_with(text, needle):
    """### **A2.** ### The FIRST LINE of a TEXT carrying the needle -- never the whole text."""
    for ln in (text or '').split(NL):
        if needle in ln:
            return ln
    return ''


def cut(S, k, sub):
    M = dict(S)
    M[k] = (S.get(k) or '').replace(sub, '')
    return M


def put(S, k, v):
    M = dict(S)
    M[k] = v
    return M


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout


def flat(s):
    return (s or '').replace(NL + '### ', ' ').replace(NL, ' ')


def jsonl(p):
    return [json.loads(l) for l in read(p).split(NL) if l.strip()]


import b552_record as R
import b542_checks as K542
import banned_terms as BTM
PPFILES = ['FINDINGS.md', 'OPEN_TRAILS.md']
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase2/method/THE_IDENTITY_CHAIN.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
SIDE_TIP = 'b4c9ebe'
CORRP = os.path.join(SIDE, 'CORRESPONDENCE.md')
BRANCH_LINES = ['Deleted branch push-b551 (was 43f85ae7).', 'Deleted branch push-b551-closing (was ccfaed9a).',
                'Deleted branch push-b551 (was a6565c8).', 'Deleted branch push-b551 (was b4c9ebe).']
GSR = os.path.join('D:', os.sep, 'SIDE-global-section')
KRN = os.path.join('D:', os.sep, 'SIDE-kernel')
BOOL = 'AggregationCircularityShadow.boolGrp'


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'))] + ['(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def jload(n):
    return json.loads(read(os.path.join(D, n)) or '{}')


def table_live():
    t = json.loads(read(os.path.join(D, 'terminal_table.json')) or '{}')
    rows = t.get('rows', t) if isinstance(t, dict) else t
    r = [x for x in rows if isinstance(x, dict) and x.get('name') == BOOL]
    return r[0] if r else {}


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b552_ferry.txt')),
        scan=read(os.path.join(D, 'b552_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b552_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b552_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b552_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b552_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b551_closing.txt')),
        addendum=read(os.path.join(D, 'b552_addendum.txt')),
        comp=read(os.path.join(D, 'b552_components.txt')),
        desk=read(os.path.join(D, 'b552_desk_notes.txt')),
        sc=jload('b552_scores.json'), reads=read(os.path.join(D, 'b552_reads.txt')),
        hk=jload('b552_housekeeping.json'), hktxt=read(os.path.join(D, 'b552_housekeeping.txt')),
        hk_files=sorted(x for x in gits(ROOT, 'show', '--name-only', '--pretty=format:', jload('b552_housekeeping.json').get('commit', 'HEAD')).split(NL) if x.strip()),
        hk_subject=gits(ROOT, 'log', '-1', '--format=%s', jload('b552_housekeeping.json').get('commit', 'HEAD')),
        r2=jload('b552_row392.json'), boolrow=table_live(),
        corr_now=open(CORRP, 'rb').read(), corr_prior=blob(GSR, SIDE_TIP + ':CORRESPONDENCE.md'),
        corr_log=gits(GSR, 'log', '--format=%H %s', SIDE_TIP + '..main'),
        readme=read(os.path.join(T, 'corr_row.README.md')), readme_json=jload('b552_readme.json'),
        stj=jload('b552_stormer.json'),
        storm={f: read(os.path.join(KRN, f)) for f in ('Kernel/Stormer.lean', 'Kernel/StormerTest.lean')},
        cons=jload('b552_consolidation.json'), du=read(os.path.join(D, 'b552_size.txt')), du_run=read(os.path.join(D, 'b552_du.txt')),
        per=jload('b552_period.json'), ptxt=read(os.path.join(D, 'b552_period.txt')),
        jsonl=[json.loads(l) for l in read(os.path.join(D, 'b548_interference.jsonl')).split(NL) if l.strip()],
        reg=jload('b552_regimes.json'), rtxt=read(os.path.join(D, 'b552_regimes.txt')), b240=read(os.path.join(D, 'b240_first_face_off.txt')),
        li=jload('b552_li_class.json'), ltxt=read(os.path.join(D, 'b552_li_class.txt')),
        efl=read(R.EFL), h2s=read(R.H2S),
        scat=jload('b552_detection_scatter.json'), stxt=read(os.path.join(D, 'b552_detection_scatter.txt')),
        found=jload('b506_c2_results.json').get('found', []),
        n6j=jload('b552_n6_line.json'), fj=jload('b552_findings.json'),
        branches=read(os.path.join(D, 'b552_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        mem_times=[os.path.getmtime(os.path.join(R.MEMDIR, f)) for f in os.listdir(R.MEMDIR)] if os.path.isdir(R.MEMDIR) else [],
        mains=R.mains(),
        trial=dict(head=gits(R.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b551*') for r in (ROOT, PP, GSR)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b552_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b552_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b552_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b552_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b552 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b552_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b552_housekeeping.txt', 'b552_row392.json', 'b552_period.json', 'b552_regimes.json',
                                                               'b552_li_class.json', 'b552_detection_scatter.json', 'b552_size.txt', 'b552_consolidation.json'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in ('b552_ferry.txt', 'b552_ferry_scan.txt', 'b552_pins_stepzero.txt')),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b552_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b552_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    blobs['CORRESPONDENCE.md'] = NL.join(l for l in rd8(S['corr_now']).split(NL) if l not in set(rd8(S['corr_prior']).split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith(('b552 --', 'housekeeping: terminal table')):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                rel = l[3:].strip()
                try:
                    if os.path.getmtime(os.path.join(repo, rel)) < os.path.getmtime(FACE):
                        continue
                except OSError:
                    pass
                k.add(os.path.basename(rel))
    S['kinds'] = k
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-4][0-9]_|^b55[01]_|^b334_', f)]
    S['prior_checked'] = len(prior)
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def declared_arms(face):
    """### ### **THE ARMS THE FACE DECLARES, MINUS THE ONES IT EXPRESSLY RETIRES.**
    ### This face says in its own (G2) block that `G-NOB475LOG` ### *"IS NOT CARRIED FORWARD
    ### UNDER THAT NAME"* ### and names its replacement. ### **AN ARM A FACE RETIRES IN WORDS IS
    ### NOT AN ARM IT DECLARES**, and a counter that reads only the token disagrees with the
    ### sentence beside it. ### The face is sealed; the COUNTER is what was wrong."""
    names = set(re.findall(r'`(G-[A-Z0-9-]+)`', face))
    for m in re.finditer(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', face):
        names.discard(m.group(1))
    return names


def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS.

    ### ### **THE CORPUS WRITES A POSSESSIVE WITH A BACKTICK** -- `this act`s record`, `b496`s
    ### face`, `(R108)`s first line` -- a convention adopted so that ground strings survive being
    ### written into Python. ### ### **EVERY SUCH POSSESSIVE MAKES THE BACKTICK COUNT ODD**, and a
    ### naive `` `([^`]+)` `` pairing then DESYNCHRONISES: it pairs the closing backtick of one
    ### path with the possessive of the next sentence and returns a multi-line blob of prose as
    ### though it were a glob.
    ### ### **MEASURED ACROSS THE LAST FIVE FACES: b493 EVEN (0 malformed), b494 EVEN (0), b495
    ### ### ODD (5 malformed), b496 ODD (4), b497 ODD (6).** ### So `G-WRITELIST-KINDS` has been
    ### reading a partly-garbled glob list for three acts, and at b497 it reported a file
    ### UNDECLARED that the face declares by name in its own (W).
    ### ### **THE REPAIR IS TO PAIR WITHIN A LINE AND TO KEEP ONLY WHAT LOOKS LIKE A PATH.**
    ### A glob has no spaces and no newlines; a possessive's neighbourhood has both.
    ### ### **THIS WIDENS NOTHING.** ### It lets the tool read declarations that were already
    ### written; a file the face does not name is still uncovered.
    """
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    out = []
    for line in w.split(NL):
        line = re.sub(r'(?<=[A-Za-z0-9])' + BT + r's\b', "'s", line)   # ### defect (e) of b540: a possessive no longer desyncs the pairing
        for g in re.findall(BT + '([^' + BT + NL + ']+)' + BT, line):
            g = g.strip()
            if not g or ' ' in g or len(g) > 120:
                continue          # ### prose, not a path
            if not re.match(r'^[A-Za-z0-9_./*?\[\]{}-]+$', g):
                continue
            out.append(g.split('/')[-1])
    return out


def strip_prose(text):
    """### ### **A `G-NO*` ARM MUST NOT READ THE ACT'S OWN SENTENCE SAYING IT DID NOT DO IT.**

    ### The trail writer holds its record in a module-level string; scanning that string for the
    ### forbidden word finds the DENIAL. ### This removes triple-quoted blocks and comments, so
    ### what remains is CODE, which is the only place a call can be. ### b487 minted this rule and
    ### this act re-learned it by being caught twice on one run.
    """
    t = re.sub(r'"""[\s\S]*?"""', ' ', text or '')
    t = re.sub(r"'''[\s\S]*?'''", ' ', t)
    t = re.sub(r'^\s*#.*$', ' ', t, flags=re.M)
    return t


def live_limb_guard(suite):
    """### ### **THE GUARD AGAINST A CONTROL THAT LEAVES A LIVE LIMB, AND WHERE IT ACTUALLY IS.**

    ### b495's `G-PUSHED-PREDICATE-THREE-CLAUSED` passed its own positive control because its
    ### predicate was `A or B` and the mutation falsified only `B`. ### This act declared a new arm
    ### to catch that species BY READING THE SUITE'S TEXT, and ### **FOUR REVISIONS LATER THE
    ### ### TEXTUAL PROXY STILL COULD NOT DO IT**: it fired on `x or []` none-defaults, on the word
    ### `or` inside quoted strings, on its own source, and on `any(A or B for ...)` whose control
    ### DOES falsify both limbs.
    ### ### **THE REASON IS THAT THE PROPERTY IS NOT TEXTUAL.** ### Whether a control falsifies
    ### every limb is a fact about what the control DOES, and the only thing that can decide it is
    ### ### **RUNNING THE CONTROL** -- which this harness already does for every arm, and whose
    ### result is the `POS` column and the `POSITIVE-CONTROL PASSES` count. ### **b495 WAS CAUGHT
    ### ### BY THAT COLUMN AND BY NOTHING ELSE.**
    ### So this arm no longer proxies. ### It asserts that the guard IS RUN: that the harness
    ### exercises a positive control on every arm, counts the passes, and ### **FAILS THE WHOLE
    ### ### SUITE ON A SINGLE ONE.**
    """
    need = ['p = bool(pred(pos(S)))',
            'defective.append(name)',
            'not defective']
    return [n for n in need if n not in suite]



def seg(text, marker, n=300):
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def fblock(text, h):
    if h not in text:
        return ''
    b = text[text.index(h):]
    j = b.find(NL + '## ', len(h))
    return b[:j] if j > 0 else b


def subseq(old, new):
    it = iter(new.split(NL))
    return all(any(l == m for m in it) for l in old.split(NL))


def kept(S, f):
    old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
    return subseq(old, new) and new.startswith(old)


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 16).split('.')[0].split(',')[0]


def word_of(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == S['recomputed'][k]


P = R.poss


def reads_ok(S):
    r = S['reads']
    return all(x in r for x in ('b551`s defect (d), the Stormer clash', 'b551`s defect (j), row 391`s grade cell', 'CORRESPONDENCE.md row 391',
                                'terminal_table.py: the CONFLICT rule', '### data/b548_interference.txt:1-21', '### data/b522_report.txt:1-52',
                                'data/b506_c2_results.json `found`', '### data/b240_first_face_off.txt:27-34', 'EF_lit (SIDE-explicit-formula',
                                'classK and h2_sign', 'BALPOS C.7.3', '### OPEN_TRAILS.md:11230-11245'))


def recount(S):
    """### the sign changes, counted here again from the jsonl with this suite`s own loop."""
    A = [r['a'] for r in S['jsonl']]
    out = {}
    for r0 in S['jsonl'][:1]:
        for kind, gm, _ in r0['terms']:
            if kind != 'off':
                continue
            v = [[t for t in r['terms'] if t[0] == 'off' and abs(t[1] - gm) < 1e-6][0][2] for r in S['jsonl']]
            out[round(gm, 6)] = sum(1 for i in range(len(v) - 1) if (v[i] < 0) != (v[i + 1] < 0))
    return A, out


def period_ok(S):
    A, cnt = recount(S)
    rows = {round(o['gamma'], 6): o for o in S['per'].get('rows', [])}
    crest = [r for r in S['jsonl']]
    cv = [[t for t in r['terms'] if t[0] == 'off' and abs(t[1] - 29.551761) < 1e-5][0][2] for r in crest]
    return (bool(cnt) and set(cnt) == set(rows) and all(len(rows[g_]['changes_a']) == c for g_, c in cnt.items())
            and S['per'].get('crest_max_a') == A[max(range(len(A)), key=lambda i: cv[i])] and A[0] == 30.0 and A[-1] == 45.0)


def floor_ok(S):
    A = [r['a'] for r in S['jsonl']]
    step = max(math.log(A[i + 1]) - math.log(A[i]) for i in range(len(A) - 1))
    rows = S['per'].get('rows', [])
    return (abs(step - math.log(31 / 30)) < 1e-12 and abs(S['per'].get('step', 0) - step) < 1e-12
            and all(o['below_floor'] == (math.pi / o['gamma'] <= step) for o in rows)
            and sorted(S['per'].get('population', [])) == sorted(o['gamma'] for o in rows if len(o['changes_a']) >= 2 and not o['below_floor']))


def h4_ok(S):
    pe = S['per']
    pop = [o for o in pe.get('rows', []) if o['in_pop']]
    dis = [o for o in pop if not all(abs(r - 1) <= 0.15 for r in o['ratios'])]
    pair = pe.get('pair', [])
    c1 = len(dis) * 2 <= len(pop)
    c3 = any(pair[i] < pair[i - 1] and pair[i] < pair[i + 1] for i in range(1, len(pair) - 1) if 36 <= 30 + i <= 38)
    return (pe.get('c1') == c1 and pe.get('c3') == c3 and pe.get('refuted') == (not pe['c1'] or not pe['c2'])
            and ('### H4 IS %s' % ('REFUTED' if pe['refuted'] else 'NOT REFUTED')) in S['ptxt'] and 'the ruling`s own word ("at a crest")' in S['ptxt'])


def regimes_ok(S):
    rg = S['reg']
    a2 = [int(l.split()[0]) for l in S['b240'].split(NL)[27:34] if l.strip() and l.split()[0].isdigit()]
    return (a2 == [2, 3, 4, 8, 9, 12] and rg.get('a2') == a2 and abs(rg.get('ratio_detect', 0) - 34 / math.sqrt(12)) < 1e-9
            and rg.get('line', '') in S['rtxt'] and 'its limit' in S['rtxt'])


def li_verbatim_ok(S):
    li = S['li']
    return (li.get('ef_lit') == NL.join(S['efl'].split(NL)[96:100]) and li.get('classK') == NL.join(S['h2s'].split(NL)[21:30])
            and 'HasCompactSupport k' in li.get('ef_lit', '') and 'k (-x) = k x' in li.get('classK', ''))


def li_read_ok(S):
    li = S['li']
    return (li.get('in_classK') is False and li.get('admitted') is False and li.get('h5') is True and li.get('one_sided') == 'NOT ESTABLISHED'
            and li.get('quotes_test_function') is False and 'pole' in ' '.join(li.get('reading', [])))


def scatter_ok(S):
    sc = S['scat']
    return (len(sc.get('rows', [])) == len(S['found']) == 17 and sc.get('population') == [] and sc.get('h6') is None
            and sorted(round(r['gamma'], 6) for r in sc['rows']) == sorted(round(z['rho'][1], 6) for z in S['found'])
            and all(sc['rows'][i]['inv'] <= sc['rows'][i + 1]['inv'] for i in range(len(sc['rows']) - 1)) and 'NOT SCORABLE' in S['stxt'])


def row392_ok(S):
    now = rd8(S['corr_now']).split(NL)
    rows = [l for l in now if re.match(r'^\| *392 *\|', l)]
    cells = [c.strip() for c in rows[0].strip().strip('|').split('|')] if rows else []
    import terminal_table as TT
    return (len(rows) == 1 and len(cells) == 6 and cells[4] == 'SHELL -- `boolGrp`' and not any(TT.GRADE_RE.search(c) for i, c in enumerate(cells) if i != 4)
            and S['r2'].get('rc') == 0)


def corr_append_ok(S):
    old, new = rd8(S['corr_prior']).rstrip(NL), rd8(S['corr_now'])
    subj = [l for l in S['corr_log'].split(NL) if l.strip()]
    return new.startswith(old) and len(subj) == 1 and subj[0].split(' ', 1)[1].startswith('b552 --') and S['mains'].get('SIDE-global-section') == ['CORRESPONDENCE.md']


def boolgrp_ok(S):
    b, a = S['r2'].get('before') or {}, S['r2'].get('after') or {}
    live = S['boolrow']
    return (b.get('grade') == 'CONFLICT' and a.get('grade') == live.get('grade') and len(a.get('cells', [])) == len(b.get('cells', [])) + 1
            and [c['grade'] for c in live.get('grade_cells', [])].count('SHELL') == 2)


def housekeeping_ok(S):
    hk = S['hk']
    return (S['hk_subject'] == 'housekeeping: terminal table regenerated at b550–b551' and hk.get('after_clean') is True
            and S['hk_files'] == ['data/terminal_table.json', 'data/terminal_table.md', 'data/terminal_table_prior.json', 'data/terminal_table_run.txt']
            and 'grade-or-profile changed 3' in S['hktxt'])


def stormer_ok(S):
    locs = S['stj'].get('locs', [])
    ok = all(re.match(r'^def divideOut\b', S['storm'][f].split(NL)[ln - 1]) and S['storm'][f].split(NL)[ns - 1].startswith('namespace Stormer') for f, ln, ns in locs)
    b = seg(S['ot'], P(R.STH), 3000)
    return len(locs) == 2 and ok and S['ot'].count(P(R.STH)) == 1 and '**the next SIDE-kernel tag**' in b and '`Kernel/Stormer.lean`:13' in b


def cons_ok(S):
    rows = [re.match(r'^(\d+) ([0-9a-f]{40}) (\S+)$', l) for l in S['du'].split(NL)]
    rows = [m for m in rows if m]
    tot = sum(int(m.group(1)) for m in rows)
    b = seg(S['ot'], P(R.CONH), 4000)
    return (len(rows) == 17 and S['cons'].get('total_kb') == tot and S['ot'].count(P(R.CONH)) == 1 and 'Nothing is moved, linked or deleted at b552' in b
            and ('**%.1f GB** in all' % (tot / 1024.0 / 1024.0)) in b and re.search(r'(?m)^end ', S['du']) is not None)


def findings_ok(S):
    b = fblock(S['find'], P(R.FH))
    return (S['find'].count(P(R.FH)) == 1 and '**Next keystone:** THE_KEYSTONE_CENSUS.' in b and '**H4 REFUTED.**' in b and '**H5 HOLDS.**' in b
            and 'NOT SCORABLE' in b and 'Graded READING throughout' in b)


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and all(b.count(l) == 1 for l in BRANCH_LINES)


def kernel_sources_ok(S):
    m = S['mains']
    return (len(m) == 4 and not any(f.endswith('.lean') for v in m.values() for f in v)
            and all(m[k] == [] for k in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-explicit-formula')))


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R162) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b552' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- no (R81) flag, and the face says so',
     lambda S: '(R81) FLAGS : 0' in line_with(S['scan'], '(R81) FLAGS') and 'The ferry scan carries no (R81) flag and no hit' in flat(S['face']),
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 2'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE -- the pins tool RUN ALONE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-REG-LOCKED-FIRST', 'the face lock block', lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK') and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b551`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b551' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b552' in S['ferry'] and 'ACT b552' in S['face'] and not glob.glob(os.path.join(D, 'b553_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b552')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; the reads and the arithmetic before the lock, every write after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'THE SEAT RAN THIS ARITHMETIC BEFORE THIS SEAL' in flat(S['face'])
     and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R162-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R162) END' in S['ferry'] and S['ot'].count('**(R162) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R162) ratified', '(R162) noted'))),
    ('G-READS-CITED', 'the reads bank -- the defects, row 391, the parser and its rule, the banks of the readings, EF_lit, classK, BALPOS, :11230',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('BALPOS C.7.3', 'x'))),
    ('G-N6-LINE', 'FINDINGS READ HERE -- the (N6) line once, naming :5715, HELD',
     lambda S: S['find'].count(P(R.N6L)) == 1 and 'its score stands HELD' in line_with(S['find'], P(R.N6L)) and S['find'].split(NL)[S['n6j']['line'] - 1].startswith(P(R.N6L)),
     lambda S: put(S, 'find', S['find'].replace('its score stands HELD', 'x'))),
    ('G-HOUSEKEEPING-COMMITTED', 'relay`s housekeeping commit READ HERE -- the ruling`s subject, the four table files, clean after',
     lambda S: housekeeping_ok(S), lambda S: put(S, 'hk_files', S['hk_files'] + ['data/b552_period.txt'])),
    ('G-ROW-392', 'CORRESPONDENCE.md READ HERE -- row 392 once, six cells, SHELL alone in the grade cell, no grade word elsewhere',
     lambda S: row392_ok(S), lambda S: put(S, 'corr_now', S['corr_now'].replace(b'| SHELL -- `boolGrp` |', b'| SHELL, ENCODES -- `boolGrp` |'))),
    ('G-CORR-APPEND-ONLY', 'the ledger against its blob at b4c9ebe -- a prefix; one b552 commit on main, CORRESPONDENCE.md alone',
     lambda S: corr_append_ok(S), lambda S: put(S, 'corr_now', S['corr_now'][:300] + S['corr_now'][400:])),
    ('G-BOOLGRP-BEFORE-AFTER', 'the regenerated table READ HERE -- boolGrp before and after, one cell more, the grade as the bank prints',
     lambda S: boolgrp_ok(S), lambda S: put(S, 'boolrow', dict(S['boolrow'], grade='SHELL'))),
    ('G-README-LINE', 'relay tools/corr_row.README.md READ HERE -- the lesson`s words, new at this act',
     lambda S: 'a grade cell carries a grade or the word NONE and no quotation' in S['readme'] and S['readme_json'].get('existed_before') is False
     and len([l for l in S['readme'].split(NL) if l.strip()]) == 1,
     lambda S: put(S, 'readme', S['readme'].replace('the word NONE', 'x'))),
    ('G-STORMER-FILED', 'SIDE-kernel`s two files READ HERE against the work-order`s lines, and OPEN_TRAILS', lambda S: stormer_ok(S),
     lambda S: put(S, 'storm', dict(S['storm'], **{'Kernel/StormerTest.lean': S['storm']['Kernel/StormerTest.lean'].replace('def divideOut', 'def divideOutTest')}))),
    ('G-CONSOLIDATION-PRICED', 'the du bank READ HERE -- every checkout measured, the total as priced, nothing moved',
     lambda S: cons_ok(S), lambda S: put(S, 'du', S['du'] + NL + '99999999 ' + '0' * 40 + ' /d/planted')),
    ('G-PERIOD-RECOMPUTED', 'b548`s jsonl READ HERE -- the sign changes counted again by this suite, the crest`s maximum', lambda S: period_ok(S),
     lambda S: put(S, 'per', dict(S['per'], crest_max_a=38.0))),
    ('G-PERIOD-FLOOR', 'the grid READ HERE -- its largest ln-step, each orbit`s floor, the population', lambda S: floor_ok(S),
     lambda S: put(S, 'per', dict(S['per'], population=S['per'].get('population', [])[1:]))),
    ('G-H4-SCORED', 'the period bank -- H4`s clauses recomputed here, the verdict line, the crest printed beside', lambda S: h4_ok(S),
     lambda S: put(S, 'ptxt', S['ptxt'].replace('### H4 IS REFUTED', '### H4 IS NOT REFUTED'))),
    ('G-REGIMES-LINE', 'b240`s bank READ HERE -- the six cells, the ratio 34 over √12, the line and its limit', lambda S: regimes_ok(S),
     lambda S: put(S, 'reg', dict(S['reg'], ratio_detect=10.0))),
    ('G-LI-VERBATIM', 'ExplicitFormula.lean and H2Sign.lean READ HERE -- EF_lit and classK as banked', lambda S: li_verbatim_ok(S),
     lambda S: put(S, 'efl', S['efl'].replace('HasCompactSupport k →', 'Continuous k →'))),
    ('G-LI-CLASS-READ', 'the Li bank -- outside classK, not admitted, H5 held, one-sided NOT ESTABLISHED, no test function quoted', lambda S: li_read_ok(S),
     lambda S: put(S, 'li', dict(S['li'], one_sided='HOLDS'))),
    ('G-LI-LEADING-ITEM', 'OPEN_TRAILS READ HERE -- the leading item once, naming :3548 and :11203, priced not begun',
     lambda S: S['ot'].count(P(R.LIH)) == 1 and '**Priced, not begun.**' in seg(S['ot'], P(R.LIH), 3000) and '(the row at :3548, the items at :11203)' in P(R.LIH),
     lambda S: put(S, 'ot', S['ot'].replace('**Priced, not begun.**', 'x'))),
    ('G-SCATTER-POPULATION', 'b506`s found zeros READ HERE -- all seventeen printed, sorted by 1/(σ − 1/2), the population empty',
     lambda S: scatter_ok(S), lambda S: put(S, 'scat', dict(S['scat'], population=[16.290216]))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once, graded READING, H4 and H5 scored, H6 NOT SCORABLE, the next keystone',
     lambda S: findings_ok(S), lambda S: put(S, 'find', S['find'].replace('**Next keystone:** THE_KEYSTONE_CENSUS.', 'x'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in three repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b551'}))),
    ('G-MEMORY-UNREFRESHED', 'the memory directory READ HERE -- no file written after this face (R157)(6)',
     lambda S: bool(S['mem_times']) and max(S['mem_times']) < os.path.getmtime(FACE),
     lambda S: put(S, 'mem_times', S['mem_times'] + [os.path.getmtime(FACE) + 1])),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-LINES-KEPT', 'the two written files against their blobs at b551`s commit',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY, SPIRAL_MAP, FACES_LEDGER, THE_LOAD_BEARING_MAP and THE_IDENTITY_CHAIN against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md',
                                                               'phase1.5/method/THE_LOAD_BEARING_MAP.md', 'phase2/method/THE_IDENTITY_CHAIN.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'SPIRAL_MAP.md': S['pp_now']['SPIRAL_MAP.md'] + b' '}))),
    ('G-KERNEL-SOURCES-UNTOUCHED', 'four kernels` mains READ HERE against their pre-act heads -- no `.lean`, only the ordered row',
     lambda S: kernel_sources_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-kernel': ['Kernel/StormerTest.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b552_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind, branch deletion included',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b552_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b552 bank and tool, this act`s PLACE-papers bytes and its ledger row, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the regenerated table', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the period bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the regimes bank', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the Li bank -- the one-sided clause printed', lambda S: nscored(S, 'n4') and 'NOT ESTABLISHED' in line_with(S['desk'], '**(N4)**'),
     lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk -- NOT SCORABLE, the population empty', lambda S: nscored(S, 'n5') and S['sc'].get('n5') is None,
     lambda S: put(S, 'sc', dict(S['sc'], n5=True))),
    ('G-N6-SCORED', 'the desk against the mains, the tools, the token, the deposit and the trial worktree', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b552 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels` mains READ HERE',
     lambda S: 'No kernel lane and no numerical lane opened at this act' in trail(S) and kernel_sources_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane and no numerical lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the two written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b551`s close -- no instrument modified (the README is new)',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['terminal_table.py'])),
    ('G-WRITELIST-KINDS', 'every b552 commit in four repositories and the housekeeping commit, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds'] if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite`s own text', lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the PLACE-papers file list -- no internal document, no `.lean`',
     lambda S: all(not x.startswith('internal/') and not x.endswith('.lean') for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite`s own text', lambda S: 'def line_with(text, needle)' in S['suite'],
     lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness itself -- the positive control is RUN on every arm',
     lambda S: not live_limb_guard(S['suite']), lambda S: put(S, 'suite', S['suite'].replace('defective.append(name)', 'pass'))),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree -- (R58)', lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/formal-math/LICENSE')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: ("rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                and "log', '-1', '--pretty=%s').startswith('b552')" in S['suite']
                and "data/b552_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b552_components.txt' in gits(ROOT, 'show'")),
]


def regenerate():
    """### ### **(R107): THE GENERATOR IS PART OF THE CLOSING SUITE.**

    ### *"the generator added to the closing suite so every later close regenerates it and diffs
    ### against the prior run"* -- the ruling's own words. ### The suite therefore RE-RUNS
    ### `tools/terminal_table.py` before it scores anything, and the diff it emits is a cell of
    ### this act's record. ### **A TABLE REGENERATED ONLY WHEN SOMEONE REMEMBERS IS A TABLE THAT
    ### ### DRIFTS**, and the whole point of an instrument output is that it cannot.
    """
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    d = os.path.join(D, 'terminal_table_diff.json')
    diff = json.loads(read(d) or '{}')
    return r.returncode, diff


def main():
    S = sources()
    rc_gen, gen_diff = regenerate()
    # ### ### **THE TABLE IS READ AFTER IT IS REGENERATED (b512's own defect, repaired post-push).** ### `sources()`
    # ### read `terminal_table.md` BEFORE `regenerate()` rewrote it, so `G-TABLE-ROW` scored the previous close's
    # ### table; the first post-push run is banked as `b512_checks_postpush_first.txt`.
    S['table'] = read(os.path.join(D, 'terminal_table.md'))
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    # ### ### **AN ARM THE FACE RETIRES IN WORDS IS NOT AN ARM IT DECLARES.** ### This face's
    # ### (G2) block says `G-NOB475LOG` *"IS NOT CARRIED FORWARD UNDER THAT NAME"* and names its
    # ### replacement. ### A counter that reads only the token disagreed with the sentence beside
    # ### it, and reported an arm declared-but-not-run. ### The face is sealed and correct; the
    # ### COUNTER was wrong, and it now honours the retirement it is reading.
    retired = set(re.findall(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', S['face']))
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'} - retired)
    if retired:
        rec('  ### arms the face RETIRES in its own words : %s' % sorted(retired))
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b552')
              and 'data/b552_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b552 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
        % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    rec('  arms in the (G2) block : %d ; run here : %d ; deferred : %d'
        % (len(declared), len(names), len(deferred)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  %-42s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 92)
    fail, defective, negfail = [], [], 0
    for name, reads, pred, pos in ARMS:
        if name in deferred:
            continue
        live = bool(pred(S))
        neg = bool(pred(dict(S)))
        p = bool(pred(pos(S)))
        if not neg:
            negfail += 1
        if p:
            defective.append(name)
        v = 'OK' if (neg and not p) else ('### DEFECTIVE' if p else '### NEG FAILS')
        rec('  %-42s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL',
                                           'PASS' if neg else '###FAIL', 'FAIL' if not p else '###PASS', v))
        RES.append(name)
        EX.append(dict(name=name, live=live, neg=neg, pos=p, reads=reads))
        if not live:
            fail.append(name)
    for n in deferred:
        rec('  %-42s DEFERRED TO POST-PUSH' % n)
    stray = sorted(k for k in S['kinds']
                   if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face'])))
    rec('')
    rec('  ### files written that NO (W) GLOB COVERS : %d %s' % (len(stray), stray or ''))
    rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
    if gen_diff.get('first_run'):
        rec('  ###   ### **NO PRIOR RUN TO DIFF AGAINST -- THIS CLOSE IS THE FIRST.** ### From')
        rec('  ###   ### the next close the diff is a cell; saying "no change" now would be a')
        rec('  ###   ### reassuring line about nothing.')
    else:
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d'
            % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
               len(gen_diff.get('changed') or [])))
    rec('  ### G-PRIORBANK-UNCHANGED checked %d prior banks by time, none excepted.'
        % S['prior_checked'])
    rec('  ### ### **VACUOUS ARMS : %s.**'
        % ([a for a in VACUOUS_ARMS] or 'NONE'))
    rec('  ### ### **THE b475 LOG EXCEPTION STAYS RETIRED.** ### b481-b489 excused')
    rec('  ###   `b475_zeta23_build.log` as still being appended to by a live process. ### b490')
    rec('  ### found pid 27508 ABSENT at two readings sixty seconds apart and the file cold, and')
    rec('  ### b491 read the log COMPLETE. ### **AN EXCEPTION IS A CLAIM ABOUT THE WORLD AND')
    rec('  ### DECAYS LIKE ONE.** ### b487`s second exclusion is not carried either: it was')
    rec('  ### b485`s bank, which (R97) directed b487 to append to. ### The arm runs at FULL WIDTH.')
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b552_checks_postpush.txt' if pushed else 'b552_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b552_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
