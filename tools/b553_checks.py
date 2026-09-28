# -*- coding: utf-8 -*-
"""b553_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b553_registration_2026-09-28.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'a5a4eb43'      # ### b552's closing housekeeping commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = 'c0af276'           # ### b552's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b553 —'


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


import b553_record as R
import b542_checks as K542
import banned_terms as BTM
CENSR = 'phase2/method/THE_KEYSTONE_CENSUS.md'
PPFILES = ['FINDINGS.md', 'OPEN_TRAILS.md', CENSR]
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase2/method/THE_IDENTITY_CHAIN.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
SIDE_TIP = '64faaa7'
CORRP = os.path.join(SIDE, 'CORRESPONDENCE.md')
BRANCH_LINES = ['Deleted branch push-b552 (was 4b21802a).', 'Deleted branch push-b552-closing (was a5a4eb43).',
                'Deleted branch push-b552 (was c0af276).', 'Deleted branch push-b552 (was 64faaa7).']
GSR = os.path.join('D:', os.sep, 'SIDE-global-section')
TOOL_COMMIT_SUBJ = "b553 -- tools/terminal_table.py: THE SUPERSESSION RULE, under the author's ruling (R163)(1)"


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'))] + ['(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def jload(n):
    return json.loads(read(os.path.join(D, n)) or '{}')


def grades_live():
    t = json.loads(read(os.path.join(D, 'terminal_table.json')) or '{}')
    rows = t.get('rows', t) if isinstance(t, dict) else t
    return {'%s|%s' % (r['repo'], r['name']): r['grade'] for r in rows if isinstance(r, dict) and 'name' in r}


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    tc = [l for l in gits(ROOT, 'log', '--format=%H %s', '-40').split(NL) if l.split(' ', 1)[-1] == TOOL_COMMIT_SUBJ]
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b553_ferry.txt')),
        scan=read(os.path.join(D, 'b553_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b553_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b553_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b553_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b553_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b552_closing.txt')),
        addendum=read(os.path.join(D, 'b553_addendum.txt')),
        comp=read(os.path.join(D, 'b553_components.txt')),
        desk=read(os.path.join(D, 'b553_desk_notes.txt')),
        sc=jload('b553_scores.json'), reads=read(os.path.join(D, 'b553_reads.txt')),
        su=jload('b553_supersede.json'), stxt=read(os.path.join(D, 'b553_supersede.txt')), before=jload('b553_table_before.json'),
        live=grades_live(),
        tool_commits=tc, tool_commit_files=(sorted(x for x in gits(ROOT, 'show', '--name-only', '--pretty=format:', tc[0].split()[0]).split(NL) if x.strip()) if tc else []),
        tool_commit_msg=(gits(ROOT, 'log', '-1', '--format=%B', tc[0].split()[0]) if tc else ''),
        tool_src=read(os.path.join(T, 'terminal_table.py')),
        tool_diff=git(ROOT, 'diff', PRIOR_RELAY, '--', 'tools/terminal_table.py'),
        corr_now=open(CORRP, 'rb').read(), corr_prior=blob(GSR, SIDE_TIP + ':CORRESPONDENCE.md'),
        corr_log=gits(GSR, 'log', '--format=%H %s', SIDE_TIP + '..main'),
        readme=read(os.path.join(T, 'corr_row.README.md')), readme_prior=rd8(blob(ROOT, PRIOR_RELAY + ':tools/corr_row.README.md')),
        older=jload('b553_older.json'), otxt=read(os.path.join(D, 'b553_older.txt')),
        cj=jload('b553_corrections.json'),
        pf=jload('b553_period_fine.json'), ptxt=read(os.path.join(D, 'b553_period_fine.txt')),
        jsonl=[json.loads(l) for l in read(os.path.join(D, 'b548_interference.jsonl')).split(NL) if l.strip()],
        plc=read(os.path.join(D, 'b553_powerlimit_check.txt')), pl=jload('b553_powerlimit.json'), br=jload('b553_bridge.json'),
        cz=jload('b553_census.json'), ctxt=read(os.path.join(D, 'b553_census.txt')),
        an=jload('b553_ancestry.json'), atxt=read(os.path.join(D, 'b553_ancestry.txt')), aread=read(os.path.join(D, 'b553_ancestry_read.txt')),
        am=jload('b553_anomaly.json'), cv=jload('b553_census_v02.json'),
        census_prior=rd8(blob(PP, PRIOR_PP + ':' + CENSR)),
        ker_head=gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'rev-parse', 'HEAD'),
        pp_bd2=gits(PP, 'rev-parse', '--verify', '-q', 'bd2ae1a^{commit}'),
        fj=jload('b553_findings.json'),
        branches=read(os.path.join(D, 'b553_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), census=read(os.path.join(PP, CENSR)),
        mem_times=[os.path.getmtime(os.path.join(R.MEMDIR, f)) for f in os.listdir(R.MEMDIR)] if os.path.isdir(R.MEMDIR) else [],
        mains=R.mains(),
        trial=dict(head=gits(R.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b552*') for r in (ROOT, PP, GSR)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b553_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b553_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b553_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b553_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b553 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b553_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b553_table_before.json', 'b553_supersede.json', 'b553_period_fine.json', 'b553_census.json',
                                                               'b553_ancestry.json', 'b553_powerlimit_check.txt', 'b553_bridge.json'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in ('b553_ferry.txt', 'b553_ferry_scan.txt', 'b553_pins_stepzero.txt')),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b553_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b553_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    blobs['CORRESPONDENCE.md'] = NL.join(l for l in rd8(S['corr_now']).split(NL) if l not in set(rd8(S['corr_prior']).split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith(('b553 --', 'housekeeping: terminal table regenerated at b553')):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-4][0-9]_|^b55[0-2]_|^b334_', f)]
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
BOOLK = 'SIDE-global-section|AggregationCircularityShadow.boolGrp'


def reads_ok(S):
    r = S['reads']
    return all(x in r for x in ('BEFORE THE EDIT: the CONFLICT rule', 'CORRESPONDENCE.md row 391', 'CORRESPONDENCE.md row 392', 'corr_row.README.md',
                                'carries "read per zero (R131)"', 'the ladder`s window and orbit term', '### data/b548_interference.txt:64-77',
                                '### OPEN_TRAILS.md:11265-11267', 'THE_KEYSTONE_CENSUS.md entire (v0.1)', 'the act-3 detector: none banked',
                                '### SIDE-kernel HEAD'))


def confined_ok(S):
    d = S['tool_diff']
    removed = [l for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    added = [l for l in d.split(NL) if l.startswith('+') and not l.startswith('+++')]
    return (removed == [] and any('uniq = supersede(uniq)' in l for l in added) and any('def supersede(cells):' in l for l in added)
            and [x for x in S['tools_edited'] if x.endswith('.py')] == ['terminal_table.py'])


def supersede_test_ok(S):
    su = S['su']
    before = S['before'].get('grades', {})
    live = S['live']
    changed = sorted(k for k in live if live[k] != before.get(k))
    return (su.get('noop_changed') == [] and changed == [BOOLK] and live.get(BOOLK) == 'SHELL' and before.get(BOOLK) == 'CONFLICT'
            and len(S['before'].get('conflicts', [])) == len(su.get('conflicts_before', [])) and len(live) == len(before))


def row393_ok(S):
    now = rd8(S['corr_now']).split(NL)
    rows = [l for l in now if re.match(r'^\| *393 *\|', l)]
    cells = [c.strip() for c in rows[0].strip().strip('|').split('|')] if rows else []
    import terminal_table as TT
    return (len(rows) == 1 and len(cells) == 6 and cells[4] == 'SUPERSEDES row 391: SHELL -- `boolGrp`'
            and not any(TT.GRADE_RE.search(c) for i, c in enumerate(cells) if i != 4) and S['su'].get('rc') == 0)


def corr_append_ok(S):
    old, new = rd8(S['corr_prior']).rstrip(NL), rd8(S['corr_now'])
    subj = [l for l in S['corr_log'].split(NL) if l.strip()]
    return new.startswith(old) and len(subj) == 1 and subj[0].split(' ', 1)[1].startswith('b553 --') and S['mains'].get('SIDE-global-section') == ['CORRESPONDENCE.md']


def readme_ok(S):
    return (S['readme'].startswith(S['readme_prior'].rstrip(NL)) and 'SUPERSEDES row N: <grade>' in S['readme']
            and len([l for l in S['readme'].split(NL) if l.strip()]) == len([l for l in S['readme_prior'].split(NL) if l.strip()]) + 1)


def tool_commit_ok(S):
    m = S['tool_commit_msg']
    return (len(S['tool_commits']) == 1 and S['tool_commit_files'] == ['tools/terminal_table.py'] and 'THE TEST' in m
            and 'CONFLICT 15' in m and 'CONFLICT 14' in m and 'CONFLICT -> SHELL, and no other' in m)


def older_ok(S):
    o = S['older']
    acts = [c['act'] for c in o.get('cells', [])]
    return (o.get('branch1') is False and o.get('row_written') is False and 'b538' not in acts and len(acts) == 3
            and 'NO ROW IS WRITTEN' in S['otxt'] and not re.search(r'(?m)^\| *394 *\|', rd8(S['corr_now'])))


def corrections_ok(S):
    return (S['find'].count(P(R.CF)) == 1 and S['ot'].count(P(R.CO)) == 1 and ':5533' in line_with(S['find'], P(R.CF))
            and 'H6 is carried unscored' in line_with(S['find'], P(R.CF)) and ('(the record at :%d)' % S['cj'].get('b546_line', -1)) in line_with(S['ot'], P(R.CO)))


def control_ok(S):
    ctrl = [x for k in ('crest', 'pair') for x in S['pf']['res'][k]['control']]
    bank = {}
    for r in S['jsonl']:
        if r['a'] <= 45:
            off = [t[2] for t in r['terms'] if t[0] == 'off' and abs(t[1] - 29.551761) < 1e-5]
            bank[('crest', r['a'])] = off[0]
            bank[('pair', r['a'])] = r['pair']
    ok = all(abs(x[2] - bank[(k, x[0])]) == 0 for k in ('crest', 'pair') for x in S['pf']['res'][k]['control'])
    return len(ctrl) == 32 and ok and S['pf'].get('control_max', 1) < 1e-9


def fine_ok(S):
    c, p = S['pf']['res']['crest'], S['pf']['res']['pair']
    x = 29.551761098629115 - 16.290216
    return (S['pf'].get('grid_n', 0) >= 139 and abs(c['pred_mean'] - 4 * math.pi / (7 * x)) < 1e-9 and len(c['changes_ln']) >= 3
            and all(abs(c['periods'][i] - (c['changes_ln'][i + 2] - c['changes_ln'][i])) < 1e-12 for i in range(len(c['periods'])))
            and p['sign'] == 'NEG' and len(p['changes_ln']) == 0)


def h7_ok(S):
    pf = S['pf']
    c, p = pf['res']['crest'], pf['res']['pair']
    h71 = all(abs(r - 1) <= 0.03 for r in c['per_ratios'])
    return (pf['h71_crest'] == h71 and pf['h72'] == (p['n_30_45'] >= 2) and pf['ref2'] == p['monotone']
            and pf['refuted'] == (not h71 or p['monotone'] or not pf['h72']) and ('### H7 IS %s' % ('REFUTED' if pf['refuted'] else 'NOT REFUTED')) in S['ptxt'])


def derivation_first_ok(S):
    f = flat(S['face'])
    return ('THE DERIVATION, FROM THAT FORMULA ALONE, BEFORE ANY EVALUATION' in f and 'MEAN is 4π/(7x) = 0.13537' in f
            and 'PREDICTED: NO SIGN CHANGE' in f and 'NO EVALUATION OF THE TRANSFORM' in f and os.path.getmtime(FACE) < os.path.getmtime(os.path.join(D, 'b553_period_fine.json')))


def powerlimit_ok(S):
    st = S['pl'].get('statements', {})
    return (S['pl'].get('exit') == 0 and all(st.get(n) for n in ('rest_term_small', 'dominant_summable', 'rest_tendsto_zero'))
            and 'SIDE-explicit-formula 81ae175' in S['plc'].split(NL)[0])


def bridge_ok(S):
    b = seg(S['ot'], P(R.BRH), 8000)
    return (S['ot'].count(P(R.BRH)) == 1 and '**Priced, not attempted.**' in b and all('**%s**' % t[0] in b for t in R.TRUNC + R.FORWARD)
            and S['br'].get('trunc') == len(R.TRUNC) and S['br'].get('forward') == len(R.FORWARD))


def census_control_ok(S):
    o = S['cz'].get('old_counts', {})
    return o.get('raw') == 20 and o.get('cc') == 9 and 'THE CONTROL at 0d4a6fe~1' in S['ctxt'] and S['cz'].get('iii_old_fail') == ['EXHAUSTIVENESS_LICENSE']


def census_live_ok(S):
    cz = S['cz']
    return (sorted(cz.get('keystones', [])) == sorted(R.V01) and cz.get('entrants') == [] and cz.get('leavers') == []
            and cz['new_counts']['KEYSTONE'] == 16 and 'THE_KEYSTONE_CENSUS' not in cz.get('keystones', []))


def ancestry_ok(S):
    an = S['an']
    return (an.get('named5', {}).get('bd2ae1a') == 'ANCESTOR' and S['pp_bd2'].startswith('bd2ae1a') and sorted(an.get('fails', [])) == ['21433177', '27a3ae7', '5e932f97', '6e8638a']
            and 'RESOLVED IN PLACE-papers' in S['aread'] and 'THE_H2_PROGRAMME_CHARTER.md:116' in S['aread'])


def anomaly_ok(S):
    am = S['am']
    return am.get('head') == S['ker_head'] and am.get('latest_tag') == 'v1.7' and am.get('head_is_latest_tag') is False and am.get('v15') == '0e5233f'


def v02_ok(S):
    b = seg(S['census'], P(R.V02H), 8000)
    return (S['census'].count(P(R.V02H)) == 1 and S['census'].count(P(R.S9H)) == 1 and kept(S, CENSR)
            and '**Next:** `SIMPLICITY_OF_RIEMANN_ZEROS`.' in b and 'superseded' in seg(S['census'], P(R.S9H), 1500))


def roster_ok(S):
    per = S['an'].get('per_doc', {})
    order = sorted(S['cz']['keystones'], key=lambda s: (-per.get(s, 0), R.V01.index(s)))
    rem = [s for s in order if s not in R.TIERED]
    return S['cv'].get('remaining') == rem and S['cv'].get('next') == rem[0]


def findings_ok(S):
    b = fblock(S['find'], P(R.FH))
    return (S['find'].count(P(R.FH)) == 1 and '**Next keystone:** `SIMPLICITY_OF_RIEMANN_ZEROS`.' in b and '**H7 REFUTED.**' in b
            and 'bd2ae1a' in b and 'KEYSTONE 16' in b)


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
     lambda S: 'RULING (R163) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b553' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b552`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b552' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b553' in S['ferry'] and 'ACT b553' in S['face'] and not glob.glob(os.path.join(D, 'b554_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b553')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; the reads before the lock, every evaluation and write after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R163-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R163) END' in S['ferry'] and S['ot'].count('**(R163) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R163) ratified', '(R163) noted'))),
    ('G-READS-CITED', 'the reads bank -- the tool before the edit, rows 391-392, the README, :5533, the window, the census, the kernel',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('THE_KEYSTONE_CENSUS.md entire (v0.1)', 'x'))),
    ('G-SUPERSEDE-EDIT-CONFINED', 'the tool`s diff against b552`s close READ HERE -- additions only, the rule and its call, no other tool modified',
     lambda S: confined_ok(S), lambda S: put(S, 'tool_diff', S['tool_diff'] + NL + '-GRADE_RE = x')),
    ('G-SUPERSEDE-TEST', 'the regenerated table READ HERE against the before-snapshot -- only boolGrp moved, CONFLICT -> SHELL',
     lambda S: supersede_test_ok(S), lambda S: put(S, 'live', dict(S['live'], **{'SIDE-kernel|e_difficulty': 'DERIVES'}))),
    ('G-ROW-393', 'CORRESPONDENCE.md READ HERE -- row 393 once, six cells, the supersession form in the grade cell alone',
     lambda S: row393_ok(S), lambda S: put(S, 'corr_now', S['corr_now'].replace(b'| SUPERSEDES row 391: SHELL -- `boolGrp` |', b'| SHELL -- `boolGrp` |'))),
    ('G-CORR-APPEND-ONLY', 'the ledger against its blob at 64faaa7 -- a prefix; one b553 commit on main, CORRESPONDENCE.md alone',
     lambda S: corr_append_ok(S), lambda S: put(S, 'corr_now', S['corr_now'][:300] + S['corr_now'][400:])),
    ('G-README-RULE', 'relay tools/corr_row.README.md READ HERE against its blob at b552`s close -- the rule appended, nothing above changed',
     lambda S: readme_ok(S), lambda S: put(S, 'readme', S['readme'].replace('SUPERSEDES row N: <grade>', 'x'))),
    ('G-TOOL-COMMIT-ALONE', 'relay`s log READ HERE -- the tool`s commit carries that file alone and quotes the test',
     lambda S: tool_commit_ok(S), lambda S: put(S, 'tool_commit_files', S['tool_commit_files'] + ['data/b553_supersede.txt'])),
    ('G-OLDER-CONFLICT-READ', 'the older-conflict bank and the ledger -- no b538 cell, neither branch, no row written',
     lambda S: older_ok(S), lambda S: put(S, 'older', dict(S['older'], row_written=True))),
    ('G-CORRECTION-LINES', 'FINDINGS and OPEN_TRAILS READ HERE -- each correction once, naming :5533 and b546`s record',
     lambda S: corrections_ok(S), lambda S: put(S, 'find', S['find'].replace('H6 is carried unscored', 'x'))),
    ('G-PERIOD-CONTROL', 'b548`s jsonl READ HERE against the fresh integer-width values -- equal to the last digit',
     lambda S: control_ok(S), lambda S: put(S, 'jsonl', [dict(r, pair=r['pair'] + 1e-6) for r in S['jsonl']])),
    ('G-PERIOD-FINE', 'the fine bank -- the derived mean recomputed here, the periods from the crossings, the pair`s sign',
     lambda S: fine_ok(S), lambda S: put(S, 'pf', dict(S['pf'], res=dict(S['pf']['res'], pair=dict(S['pf']['res']['pair'], sign='MIXED'))))),
    ('G-H7-SCORED', 'the fine bank -- H7`s clauses recomputed here, the verdict line', lambda S: h7_ok(S),
     lambda S: put(S, 'ptxt', S['ptxt'].replace('### H7 IS REFUTED', '### H7 IS NOT REFUTED'))),
    ('G-DERIVATION-FIRST', 'the sealed face against the fine bank`s time -- the derivation and its prediction sealed before any evaluation',
     lambda S: derivation_first_ok(S), lambda S: put(S, 'face', S['face'].replace('PREDICTED: NO SIGN CHANGE', 'x'))),
    ('G-POWERLIMIT-FRESH', 'the #check run READ HERE -- exit 0 at 81ae175, the three statements printed', lambda S: powerlimit_ok(S),
     lambda S: put(S, 'pl', dict(S['pl'], exit=1))),
    ('G-BRIDGE-PRICED', 'OPEN_TRAILS READ HERE -- the price once, every item of both lists, not attempted', lambda S: bridge_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Priced, not attempted.**', 'x'))),
    ('G-CENSUS-CONTROL', 'the census bank -- the raw 20 and 9 reproduced at 0d4a6fe~1, the (iii) discrepancy named', lambda S: census_control_ok(S),
     lambda S: put(S, 'cz', dict(S['cz'], old_counts=dict(S['cz']['old_counts'], raw=21)))),
    ('G-CENSUS-LIVE', 'the census bank against v0.1`s published sixteen -- the live list, no entrant, no leaver', lambda S: census_live_ok(S),
     lambda S: put(S, 'cz', dict(S['cz'], entrants=['BALANCE_AND_POSITIVITY']))),
    ('G-ANCESTRY', 'PLACE-papers READ HERE for bd2ae1a, and the ancestry banks -- the failures, the hand-read, the five', lambda S: ancestry_ok(S),
     lambda S: put(S, 'pp_bd2', '')),
    ('G-ANOMALY-READ', 'SIDE-kernel READ HERE against the anomaly bank -- HEAD, v1.7, v1.5', lambda S: anomaly_ok(S),
     lambda S: put(S, 'ker_head', '5e668b4')),
    ('G-CENSUS-V02', 'THE_KEYSTONE_CENSUS READ HERE against its blob -- the §9 block and v0.2 once each, v0.1 kept', lambda S: v02_ok(S),
     lambda S: put(S, 'census', S['census'].replace(P(R.V02H), 'x'))),
    ('G-ROSTER-NEXT', 'the roster recomputed here from the ancestry counts and v0.1`s order', lambda S: roster_ok(S),
     lambda S: put(S, 'cv', dict(S['cv'], next='ADDITIVE_MULTIPLICATIVE_CONSPIRACY'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once, H7, bd2ae1a, the count, the next keystone', lambda S: findings_ok(S),
     lambda S: put(S, 'find', S['find'].replace('**H7 REFUTED.**', 'x'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in three repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b552'}))),
    ('G-MEMORY-UNREFRESHED', 'the memory directory READ HERE -- no file written after this face (R157)(6)',
     lambda S: bool(S['mem_times']) and max(S['mem_times']) < os.path.getmtime(FACE),
     lambda S: put(S, 'mem_times', S['mem_times'] + [os.path.getmtime(FACE) + 1])),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-LINES-KEPT', 'the three written files against their blobs at b552`s commit',
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
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'REGISTRY.md': S['pp_now']['REGISTRY.md'] + b' '}))),
    ('G-KERNEL-SOURCES-UNTOUCHED', 'four kernels` mains READ HERE against their pre-act heads -- no `.lean`, only the ordered row',
     lambda S: kernel_sources_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-kernel': ['Kernel/StormerTest.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b553_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b553_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b553 bank and tool, this act`s PLACE-papers bytes and its ledger row, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the supersession bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the older-conflict bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the fine bank and the sealed derivation', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the bridge bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the census bank', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the ancestry bank', lambda S: nscored(S, 'n6'), lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-N7-SCORED', 'the desk against the mains, the tools, the token, the deposit and the trial worktree', lambda S: nscored(S, 'n7'),
     lambda S: put(S, 'sc', dict(S['sc'], n7=not S['sc'].get('n7')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b553 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels` mains READ HERE',
     lambda S: 'No kernel lane opened at this act' in trail(S) and kernel_sources_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the three written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-INSTRUMENTS-EDITED-AS-ORDERED', 'relay`s tools against b552`s close -- terminal_table.py modified, and no other',
     lambda S: [x for x in S['tools_edited'] if x.endswith('.py')] == ['terminal_table.py'], lambda S: put(S, 'tools_edited', ['corr_row.py', 'terminal_table.py'])),
    ('G-WRITELIST-KINDS', 'every b553 commit in four repositories and the housekeeping commit, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b553')" in S['suite']
                and "data/b553_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b553_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b553')
              and 'data/b553_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b553 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b553_checks_postpush.txt' if pushed else 'b553_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b553_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
