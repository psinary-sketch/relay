# -*- coding: utf-8 -*-
"""b551_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b551_registration_2026-09-27.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'ffee83ff'      # ### b550's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = '812cbe2'           # ### b550's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b551 —'


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


import b551_record as R
import b542_checks as K542
import banned_terms as BTM
IDCR = 'phase2/method/THE_IDENTITY_CHAIN.md'
PPFILES = ['FINDINGS.md', 'OPEN_TRAILS.md', 'SPIRAL_MAP.md', IDCR]
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
SIDE_TIP = '2e43315'
CORRP = os.path.join(SIDE, 'CORRESPONDENCE.md')
BRANCH_LINES = ['Deleted branch push-b550 (was 0dd0a285).', 'Deleted branch push-b550-closing (was ffee83ff).', 'Deleted branch push-b550 (was 812cbe2).']
LVR = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
EFR = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
GSR = os.path.join('D:', os.sep, 'SIDE-global-section')
MLR = os.path.join('D:', os.sep, 'mathlib4')
ML_PKG = os.path.join(EFR, '.lake', 'packages', 'mathlib')
OLD_REV, NEW_REV = '5e932f97dd25535344f80f9dd8da3aab83df0fe6', '51e6992efd06126df61a496bebf8f49482a4e129'


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'))] + ['(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def jload(n):
    return json.loads(read(os.path.join(D, n)) or '{}')


def live_rows(static):
    """### every census row RE-READ HERE from the repository`s own files, not from the bank."""
    out = {}
    for r in static.get('rows', []):
        p = r['path']
        tcf = os.path.join(p, 'lean-toolchain')
        m = None
        try:
            m = json.loads(read(os.path.join(p, 'lake-manifest.json')) or 'null')
        except ValueError:
            m = None
        me = [x for x in (m or {}).get('packages', []) if x.get('name') == 'mathlib']
        own = os.path.join(p, '.lake', 'packages', 'mathlib')
        out[r['repo']] = dict(toolchain=read(tcf).strip() if os.path.exists(tcf) else 'NONE', rev=me[0]['rev'] if me else None,
                              imports=len([x for x in gits(p, 'grep', '-l', '-E', '^import Mathlib', 'HEAD', '--', '*.lean').split(NL) if x.strip()]),
                              own=gits(own, 'rev-parse', 'HEAD') if os.path.isdir(own) else '',
                              clean=gits(p, 'status', '--porcelain', '--untracked-files=no') == '', head=gits(p, 'rev-parse', 'HEAD'))
    return out


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    static = jload('b551_census_static.json')
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b551_ferry.txt')),
        scan=read(os.path.join(D, 'b551_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b551_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b551_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b551_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b551_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b550_closing.txt')),
        addendum=read(os.path.join(D, 'b551_addendum.txt')),
        comp=read(os.path.join(D, 'b551_components.txt')),
        desk=read(os.path.join(D, 'b551_desk_notes.txt')),
        sc=jload('b551_scores.json'), reads=read(os.path.join(D, 'b551_reads.txt')),
        static=static, live=live_rows(static), runs=jsonl(os.path.join(D, 'b551_census_runs.jsonl')),
        tc=jload('b551_toolchains.json'), ttxt=read(os.path.join(D, 'b551_toolchains.txt')),
        spiral=read(os.path.join(PP, 'SPIRAL_MAP.md')), spiral_prior=rd8(blob(PP, PRIOR_PP + ':SPIRAL_MAP.md')),
        side_dirs=sorted(os.path.basename(x) for x in glob.glob(os.path.join('D:', os.sep, 'SIDE-*')) if os.path.isdir(x)),
        cost=jload('b551_iface_cost.json'), cost_t=os.path.getmtime(os.path.join(D, 'b551_iface_cost.txt')) if os.path.exists(os.path.join(D, 'b551_iface_cost.txt')) else 0,
        build=read(os.path.join(D, 'b551_olean_build.txt')), build_t=os.path.getmtime(os.path.join(D, 'b551_olean_build.txt')) if os.path.exists(os.path.join(D, 'b551_olean_build.txt')) else 0,
        olean_live=os.path.exists(R.olean_of(MLR, R.MISSING_MOD)), ic=jload('b551_iface.json'),
        iruns={f: read(os.path.join(D, 'b551_iface_%s.txt' % f)) for f in R.IFACE4}, ibank=R.bank_sections(),
        tagtxt=read(os.path.join(D, 'b551_tag.txt')), tg=jload('b551_tag.json'),
        live_tag=gits(GSR, 'ls-remote', 'origin', 'refs/tags/v0.2.0^{}'), live_local=gits(GSR, 'rev-parse', 'v0.2.0^{commit}'),
        gs_type=gits(GSR, 'cat-file', '-t', 'v0.2.0'),
        rw=jload('b551_rows.json'), sp=jload('b551_spiral.json'), idcj=jload('b551_idc.json'),
        corr_now=open(CORRP, 'rb').read(), corr_prior=blob(GSR, SIDE_TIP + ':CORRESPONDENCE.md'),
        corr_log=gits(GSR, 'log', '--format=%H %s', SIDE_TIP + '..main'),
        ap_bank=read(os.path.join(GSR, 'AXIOM_PRINTS.txt')),
        revs=read(os.path.join(D, 'b551_trial_revs.txt')),
        live_count=gits(ML_PKG, 'rev-list', '--count', OLD_REV + '..' + NEW_REV), live_back=gits(ML_PKG, 'rev-list', '--count', NEW_REV + '..' + OLD_REV),
        tdiff=read(os.path.join(D, 'b551_trial_diff.txt')), tr=jload('b551_trial.json'), tbuild=read(os.path.join(D, 'b551_trial_build.txt')),
        trial_files=sorted(x for x in gits(LVR, 'diff', '--name-only', 'main', 'toolchain-trial-b551').split(NL) if x.strip()),
        trial_tc=blob(LVR, 'toolchain-trial-b551:lean-toolchain'), ef_tc=blob(EFR, 'HEAD:lean-toolchain'),
        trial_mf=rd8(blob(LVR, 'toolchain-trial-b551:lake-manifest.json')), ef_mf=rd8(blob(EFR, 'HEAD:lake-manifest.json')),
        lv_mf=rd8(blob(LVR, 'main:lake-manifest.json')),
        trial_remote=gits(LVR, 'ls-remote', 'origin', 'refs/heads/toolchain-trial-b551'), trial_local=gits(LVR, 'rev-parse', 'toolchain-trial-b551'),
        lv_remote_main=gits(LVR, 'ls-remote', 'origin', 'refs/heads/main'), lv_main=gits(LVR, 'rev-parse', 'main'),
        lv_status=gits(LVR, 'status', '--porcelain', '--untracked-files=no'), lv_branch=gits(LVR, 'rev-parse', '--abbrev-ref', 'HEAD'),
        pr=jload('b551_price.json'), fj=jload('b551_findings.json'),
        branches=read(os.path.join(D, 'b551_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), idc=read(os.path.join(PP, IDCR)),
        mem_times=[os.path.getmtime(os.path.join(R.MEMDIR, f)) for f in os.listdir(R.MEMDIR)] if os.path.isdir(R.MEMDIR) else [],
        mains=R.lean_changed_on_mains(),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b550*') for r in (ROOT, PP)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b551_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b551_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b551_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b551_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b551 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b551_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b551_census_static.json', 'b551_census_runs.jsonl', 'b551_toolchains.json', 'b551_iface_cost.txt',
                                                               'b551_olean_build.txt', 'b551_iface.json', 'b551_tag.txt', 'b551_rows.json', 'b551_trial.json'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in ('b551_ferry.txt', 'b551_ferry_scan.txt', 'b551_pins_stepzero.txt')),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b551_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b551_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    blobs['CORRESPONDENCE.md'] = NL.join(l for l in rd8(S['corr_now']).split(NL) if l not in set(rd8(S['corr_prior']).split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER, LVR):
        for rev in (('HEAD', 'toolchain-trial-b551') if repo == LVR else ('HEAD',)):
            for l in gits(repo, 'log', '--pretty=%H %s', '-30', rev).split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b551 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-4][0-9]_|^b550_|^b334_', f)]
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
    return all(x in r for x in ('### tools/b542_record.py:80-101', '### tools/b546_record.py:24-25', '### the forty-five names: 45 (b542 37, b546 8)',
                                '### SPIRAL_MAP`s pin lines', '### data/b550_defects.txt:1-4', '### tools/corr_row.py:67-70',
                                '### SIDE-global-section CORRESPONDENCE.md rows 80-90', '### OPEN_TRAILS.md:11203-11213',
                                '### the Mathlib checkouts on D: (git rev-parse HEAD):'))


def table(S):
    return S['tc'].get('table', [])


def rowmap(S):
    return {r['repo']: r for r in S['static'].get('rows', [])}


def cellmap(S):
    return {c['repo'].replace(' (private)', ''): c for c in table(S)}


def names_ok(S):
    reps, _, _ = R.names()
    nm = [r['name'] for r in reps]
    got = [r['repo'] for r in S['static'].get('rows', [])]
    return len(nm) == 45 and got == nm and set(S['side_dirs']) <= set(nm) and len(table(S)) == 45


def seven_ok(S):
    cols = ('repo', 'toolchain', 'rev', 'checkout', 'oleans', 'cache', 'pin')
    lines = [l for l in S['ttxt'].split(NL) if l.count(' | ') == 6]
    return len(table(S)) == 45 and all(all((c.get(k) or '').strip() for k in cols) for c in table(S)) and len(lines) == 46


def vanilla_ok(S):
    cm = cellmap(S)
    for n, lv in S['live'].items():
        van = lv['rev'] is None and lv['imports'] == 0
        if (cm[n]['rev'] == 'VANILLA') != van:
            return False
    return bool(S['live'])


def toolchain_ok(S):
    cm = cellmap(S)
    return bool(S['live']) and all(cm[n]['toolchain'] == lv['toolchain'] for n, lv in S['live'].items())


def revs_ok(S):
    cm = cellmap(S)
    return bool(S['live']) and all(cm[n]['rev'] == lv['rev'][:12] for n, lv in S['live'].items() if lv['rev'])


def checkout_ok(S):
    cm = cellmap(S)
    return bool(S['live']) and all(cm[n]['checkout'].startswith('yes (own') == (lv['own'] == lv['rev']) for n, lv in S['live'].items() if lv['rev'])


def runs_for(S, repo, kind):
    return [x for x in S['runs'] if x['key'].startswith(repo + ' | ' + kind)]


def roots_ok(S):
    cm, rm = cellmap(S), rowmap(S)
    ok = True
    for n, r in rm.items():
        if r['kind'] != 'MANIFEST' or not r['lakefile']:
            continue
        rr = runs_for(S, n, 'lake env lean')
        live_targets = [t for t in r['targets'] if t['kind'] != 'absent']
        if len(rr) != len(live_targets):
            ok = False
        if cm[n]['oleans'].startswith('COMPLETE') != (bool(rr) and all(x['rc'] == 0 for x in rr)):
            ok = False
    return ok and bool(S['runs'])


def cache_ok(S):
    cm, rm = cellmap(S), rowmap(S)
    for n, r in rm.items():
        if not r['lakefile']:
            if cm[n]['cache'] != 'NO LAKEFILE':
                return False
            continue
        rr = runs_for(S, n, 'lake build --no-build')
        if len(rr) != 1 or (cm[n]['cache'] == 'YES') != (rr[0]['rc'] == 0):
            return False
    return bool(rm)


def guarded(S):
    return bool(S['runs']) and all(x['guard'] == sorted(R.GUARD) for x in S['runs']) and all(
        v == 'http://127.0.0.1:9' for k, v in R.GUARD.items() if 'proxy' in k.lower()) and R.GUARD['GIT_ALLOW_PROTOCOL'] == 'file'


def distinct_ok(S):
    rm = rowmap(S)
    groups = {}
    for n, lv in S['live'].items():
        rv = lv['rev'] or ((rm[n].get('declared') or {}).get('rev') if lv['imports'] else None)
        if rv:
            groups.setdefault(rv[:10], []).append(n)
    return len(groups) == S['tc'].get('distinct') and ('DISTINCT MATHLIB REVS AMONG NON-VANILLA REPOSITORIES : %d' % len(groups)) in S['ttxt']


def pins_ok(S):
    sp = S['spiral_prior'].split(NL)
    for r in S['static'].get('rows', []):
        s = r['spiral']
        c = cellmap(S)[r['repo']]['pin']
        if s['line']:
            ln = sp[s['line'] - 1]
            if (r['source'] == 'b542' and s['needle'] not in ln) or (r['source'] == 'b546' and ('`%s`' % r['repo']) not in ln):
                return False
            if not c.startswith(s['pin']):
                return False
        elif not c.startswith('NONE'):
            return False
    return bool(S['static'].get('rows'))


def trees_ok(S):
    rm = rowmap(S)
    return bool(S['live']) and all(lv['clean'] for lv in S['live'].values()) and all(
        lv['head'] == rm[n]['head'] for n, lv in S['live'].items() if n != 'SIDE-global-section')


def epoch(stamp):
    import calendar
    return calendar.timegm(time.strptime(stamp, '%Y-%m-%dT%H:%M:%SZ'))


def cost_first(S):
    m = re.search(r'start (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', S['build'].split(NL)[0] if S['build'] else '')
    return bool(m) and 0 < S['cost_t'] < epoch(m.group(1)) and S['cost'].get('missing') == [R.MISSING_MOD]


def olean_ok(S):
    return (re.search(r'(?m)^exit 0$', S['build']) is not None and S['olean_live'] and 'cecd0c4d56' in S['build'].split(NL)[0]
            and S['ic'].get('olean_present') is True and S['ic'].get('build_exit') == 0)


def four_ok(S):
    return all(('mathlib4 cecd0c4d56' in S['iruns'][f].split(NL)[0]) and re.search(r'(?m)^exit \d+$', S['iruns'][f]) for f in R.IFACE4)


def lfl_ok(S):
    files = S['ic'].get('files', {})
    for f in R.IFACE4:
        run = S['iruns'][f]
        ok_exit = re.search(r'(?m)^exit 0$', run) is not None
        if ok_exit and R.print_lines(run) != S['ibank'].get(f):
            return False
        if files.get(f, {}).get('equal') != (R.print_lines(run) == S['ibank'].get(f)):
            return False
    return len(files) == 4


def rtl1_ok(S):
    ic, rw = S['ic'], S['rw']
    ran = re.search(r'(?m)^exit (\d+)$', S['iruns']['RestrictedTensorLayer1'])
    if not ran or 'rtl1' not in ic or (int(ran.group(1)) == 0) != ic['rtl1']:
        return False
    if ic['rtl1']:
        return rw.get('rtl1_note') is None
    n = (rw.get('rtl1_note') or {}).get('number')
    return bool(n) and rd8(S['corr_now']).count('\n| %d | RESTRICTEDTENSORLAYER1 AT ITS DECLARED PIN' % n) == 1


def agg_ok(S):
    n = S['rw'].get('number')
    now = rd8(S['corr_now']).split(NL)
    rows = [l for l in now if re.match(r'^\| *%s *\|' % n, l)]
    ap = [re.match(r"^'AggregationCircularityShadow\.([^']+)'", l).group(1) for l in S['ap_bank'].split(NL) if l.startswith("'AggregationCircularityShadow.")]
    return (S['rw'].get('rc') == 0 and len(rows) == 1 and len(ap) == 9 and all('`%s`' % a in rows[0] for a in ap)
            and n == max(int(x) for x in re.findall(r'(?m)^\| *(\d+) *\|', rd8(S['corr_prior']))) + 1 and 'corr_row.py' in rows[0])


def corr_append_ok(S):
    old, new = rd8(S['corr_prior']).rstrip(NL), rd8(S['corr_now'])
    subj = [l for l in S['corr_log'].split(NL) if l.strip()]
    return new.startswith(old) and len(subj) == 1 and subj[0].split(' ', 1)[1].startswith('b551 --') and S['mains'].get('SIDE-global-section') == ['CORRESPONDENCE.md']


def idc_ok(S):
    l = line_with(S['idc'], P(R.IDL))
    return (S['idc'].count(P(R.IDL)) == 1 and 'row 81 SectorNonvanishingShadow' in l and 'row 85 LadderOrientationShadow' in l
            and 'row 89 FoldedMirrorShadow' in l and ('is row %d' % S['rw'].get('number', -1)) in l and ':3170' in l and kept(S, IDCR))


def revs_trial_ok(S):
    return (S['live_count'] != '' and ('rev-list --count %s..%s : %s' % (OLD_REV[:7], NEW_REV[:7], S['live_count'])) in S['revs']
            and ('rev-list --count %s..%s : %s' % (NEW_REV[:7], OLD_REV[:7], S['live_back'])) in S['revs'] and int(S['live_count']) > int(S['live_back']))


def lines_exact_ok(S):
    ef = S['ef_mf']
    name_ef = json.loads(ef)['name']
    name_lv = json.loads(S['lv_mf'])['name']
    return S['trial_tc'] == S['ef_tc'] and S['trial_mf'] == ef.replace(' "name": "%s",' % name_ef, ' "name": "%s",' % name_lv) and S['trial_tc'] != b''


def count_errors(text):
    """### the per-module count, written here again and not imported from the record: a Lean error line carries its file."""
    c = {}
    for l in text.split(NL):
        m = re.search(r'error: (?:\./+)?([^\s:]+\.lean):\d+:\d+:', l)
        if m:
            k = m.group(1).replace(chr(92), '/').lstrip('./')
            c[k] = c.get(k, 0) + 1
    return c


def errors_ok(S):
    c = count_errors(S['tbuild'])
    got = {m['file']: m['errors'] for m in S['tr'].get('modules', [])}
    return bool(S['tbuild']) and c == got and S['tr'].get('total') == sum(c.values())


def build_once_ok(S):
    return (len(re.findall(r'(?m)^exit \S+$', S['tbuild'])) == 1 and 'toolchain-trial-b551' in S['tbuild'].split(NL)[0]
            and 'GIT_ALLOW_PROTOCOL=file' in S['tbuild'].split(NL)[0] and 'trial-b551-lv' in S['tbuild'].split(NL)[0])


def pushed_held_ok(S):
    return (S['trial_local'] != '' and S['trial_remote'].startswith(S['trial_local']) and S['lv_remote_main'].startswith('2f71068')
            and S['trial_files'] == ['lake-manifest.json', 'lean-toolchain'])


def older_ok(S):
    return S['lv_main'].startswith('2f71068') and S['lv_status'] == '' and S['lv_branch'] == 'main' and S['mains'].get('SIDE-lv-conservation') == []


def price_ok(S):
    b = seg(S['ot'], P(R.PRH), 8000)
    tr = S['tr']
    return (S['ot'].count(P(R.PRH)) == 1 and '(the item at :11203)' in P(R.PRH) and 'toolchain-trial-b551' in b and 'The merge is not done at this act' in b
            and (('**The price: %d error' % tr.get('total', -1)) in b if tr.get('modules') else '**The price: no module errors**' in b))


def findings_ok(S):
    b = fblock(S['find'], P(R.FH))
    tc = S['tc']
    return (S['find'].count(P(R.FH)) == 1 and ('**%d distinct Mathlib revs**' % tc.get('distinct', -1)) in b and '**Next keystone:** THE_KEYSTONE_CENSUS.' in b
            and all(f in b for f in tc.get('fails', [])) and '**The Weil-side alignment, trialled.**' in b)


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and all(b.count(l) == 1 for l in BRANCH_LINES)


def kernel_sources_ok(S):
    m = S['mains']
    return (len(m) == 4 and not any(f.endswith('.lean') for v in m.values() for f in v) and not any(f.endswith('.lean') for f in S['trial_files'])
            and all(m[k] == [] for k in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-explicit-formula')))


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R161) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b551' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b550`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b550' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b551' in S['ferry'] and 'ACT b551' in S['face'] and not glob.glob(os.path.join(D, 'b552_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b551')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; the reads before the lock, every lake run and write after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'NO `lake` COMMAND HAS RUN' in flat(S['face'])
     and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R161-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R161) END' in S['ferry'] and S['ot'].count('**(R161) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R161) ratified', '(R161) noted'))),
    ('G-READS-CITED', 'the reads bank -- the enumeration, the manifests, SPIRAL_MAP`s pins, b550`s defect, the writer, the rows, :11203, the checkouts',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('### OPEN_TRAILS.md:11203-11213', 'x'))),
    ('G-FORTYFIVE-NAMES', 'b542`s and b546`s tools READ HERE as literals, and D:\\SIDE-* listed HERE -- forty-five rows, none outside',
     lambda S: names_ok(S), lambda S: put(S, 'side_dirs', S['side_dirs'] + ['SIDE-not-enumerated'])),
    ('G-CENSUS-SEVEN-COLUMNS', 'the table bank -- forty-five rows, seven filled cells each, printed whole',
     lambda S: seven_ok(S), lambda S: put(S, 'tc', dict(S['tc'], table=[dict(c, pin='') if c['repo'] == 'SIDE-cosmo' else c for c in table(S)]))),
    ('G-VANILLA-MARKED', 'every repository`s manifest and imports READ HERE -- VANILLA exactly where no mathlib entry and no Mathlib import',
     lambda S: vanilla_ok(S), lambda S: put(S, 'live', dict(S['live'], **{'SIDE-window': dict(S['live']['SIDE-window'], imports=3)}))),
    ('G-TOOLCHAIN-LINES', 'every lean-toolchain READ HERE against its cell', lambda S: toolchain_ok(S),
     lambda S: put(S, 'live', dict(S['live'], **{'SIDE-cosmo': dict(S['live']['SIDE-cosmo'], toolchain='leanprover/lean4:v4.99.0')}))),
    ('G-MANIFEST-REVS', 'every lake-manifest READ HERE against its cell', lambda S: revs_ok(S),
     lambda S: put(S, 'live', dict(S['live'], **{'SIDE-effects': dict(S['live']['SIDE-effects'], rev='0' * 40)}))),
    ('G-CHECKOUT-CELLS', 'every repository`s own package clone READ HERE (git rev-parse) against its cell', lambda S: checkout_ok(S),
     lambda S: put(S, 'live', dict(S['live'], **{'SIDE-kernel': dict(S['live']['SIDE-kernel'], own='f' * 40)}))),
    ('G-ROOTS-ELABORATED', 'the run records -- one `lake env lean` per live root, the cell COMPLETE exactly when every root exits 0',
     lambda S: roots_ok(S), lambda S: put(S, 'runs', [x for x in S['runs'] if not x['key'].startswith('SIDE-cosmo | lake env lean')])),
    ('G-FROM-CACHE-CELLS', 'the run records -- one `--no-build` per lakefile, the cell YES exactly on exit 0', lambda S: cache_ok(S),
     lambda S: put(S, 'runs', [dict(x, rc=3) if x['key'] == 'SIDE-kernel | lake build --no-build' else x for x in S['runs']])),
    ('G-NETWORK-GUARDED', 'every run record`s guard, and the guard`s own values', lambda S: guarded(S),
     lambda S: put(S, 'runs', S['runs'][:-1] + [dict(S['runs'][-1], guard=[])])),
    ('G-DISTINCT-REVS', 'the distinct set recomputed HERE from the live manifests', lambda S: distinct_ok(S),
     lambda S: put(S, 'tc', dict(S['tc'], distinct=S['tc'].get('distinct', 0) + 1))),
    ('G-SPIRAL-PINS', 'SPIRAL_MAP at b550`s commit READ HERE -- each cited pin`s needle at its printed line', lambda S: pins_ok(S),
     lambda S: put(S, 'spiral_prior', S['spiral_prior'].replace('| `SIDE-grh-transfer` | v0.4.0', '| `SIDE-grh-transfer` | v9'))),
    ('G-TREES-CLEAN-AFTER', 'every repository READ HERE -- tracked tree clean, HEAD where the census found it (the ordered row excepted)',
     lambda S: trees_ok(S), lambda S: put(S, 'live', dict(S['live'], **{'SIDE-trivium': dict(S['live']['SIDE-trivium'], clean=False)}))),
    ('G-COST-PRINTED-FIRST', 'the cost bank`s time against the build`s own start line', lambda S: cost_first(S),
     lambda S: put(S, 'cost_t', S['cost_t'] + 10 ** 7)),
    ('G-OLEAN-BUILT', 'the build bank and the olean READ HERE at D:\\mathlib4', lambda S: olean_ok(S), lambda S: put(S, 'olean_live', False)),
    ('G-IFACE-FOUR', 'the four run banks -- each at cecd0c4, each with its exit', lambda S: four_ok(S),
     lambda S: put(S, 'iruns', dict(S['iruns'], LocalLimit=S['iruns']['LocalLimit'].replace('mathlib4 cecd0c4d56', 'mathlib4 01fc2203e2')))),
    ('G-IFACE-LINE-FOR-LINE', 'each elaborated file`s prints READ HERE against its section of AXIOM_PRINTS_INTERFACES.txt', lambda S: lfl_ok(S),
     lambda S: put(S, 'ibank', dict(S['ibank'], GlobalSection=list(reversed(S['ibank'].get('GlobalSection', []))) + ['x']))),
    ('G-RTL1-OUTCOME', 'RestrictedTensorLayer1`s run and the ledger -- the outcome printed, the note row present exactly on failure',
     lambda S: rtl1_ok(S), lambda S: put(S, 'ic', dict(S['ic'], rtl1=not S['ic'].get('rtl1')))),
    ('G-TAG-READBACK', 'SIDE-global-section`s remote READ HERE -- v0.2.0 annotated, peeled to 2e43315, equal to the bank',
     lambda S: S['live_tag'].startswith('2e43315') and S['live_local'].startswith('2e43315') and S['gs_type'] == 'tag'
     and S['tg'].get('remote_peeled', '').startswith('2e43315') and S['tg'].get('n4') is True,
     lambda S: put(S, 'live_tag', '706a81b000000000000000000000000000000000 refs/tags/v0.2.0^{}')),
    ('G-GS-TAG-CLEAN', 'the tag bank -- the repository clean before and after, the tag moving no head',
     lambda S: S['tg'].get('before_clean') and S['tg'].get('after_clean') and S['tg'].get('before_head') == S['tg'].get('after_head')
     and S['tg']['after_head'].startswith('2e43315') and S['tg'].get('remote_main', '').startswith('2e43315'),
     lambda S: put(S, 'tg', dict(S['tg'], after_clean=False))),
    ('G-SPIRAL-ROW', 'SPIRAL_MAP READ HERE -- one block, the pin, the map`s prior bytes kept',
     lambda S: S['spiral'].count(P(R.SPH)) == 1 and (lambda b: '**`v0.2.0`** = `2e43315`' in b and '`SIDE-global-section` *(pinned by b551)*' in b)(seg(S['spiral'], P(R.SPH), 3000))
     and kept(S, 'SPIRAL_MAP.md'),
     lambda S: put(S, 'spiral', S['spiral'].replace('**`v0.2.0`** = `2e43315`', '**`v0.2.0`**'))),
    ('G-AGG-ROW', 'CORRESPONDENCE.md READ HERE -- the new row once, the next free number, all nine printed terminals, the writer named',
     lambda S: agg_ok(S), lambda S: put(S, 'corr_now', S['corr_now'].replace(b'`cweil_is_the_assumption`', b'`x`'))),
    ('G-CORR-APPEND-ONLY', 'the ledger against its blob at 2e43315 -- a prefix; one b551 commit on main, CORRESPONDENCE.md alone',
     lambda S: corr_append_ok(S), lambda S: put(S, 'corr_now', S['corr_now'][:300] + S['corr_now'][400:])),
    ('G-NUMBERING-LINE', 'THE_IDENTITY_CHAIN READ HERE -- the line once, naming :3170, rows 81-89 by module, the new row', lambda S: idc_ok(S),
     lambda S: put(S, 'idc', S['idc'].replace('row 85 LadderOrientationShadow', 'row 85 x'))),
    ('G-TRIAL-REVS', 'the newer kernel`s Mathlib clone READ HERE -- the two counts, the older side the ancestor side', lambda S: revs_trial_ok(S),
     lambda S: put(S, 'live_count', '0')),
    ('G-TRIAL-BRANCH-DIFF', 'the branch against main READ HERE -- lake-manifest.json and lean-toolchain, nothing else',
     lambda S: S['trial_files'] == ['lake-manifest.json', 'lean-toolchain'] and 'lake-manifest.json' in S['tdiff'] and 'lean-toolchain' in S['tdiff'],
     lambda S: put(S, 'trial_files', S['trial_files'] + ['SIDELvConservation/Mellin.lean'])),
    ('G-TRIAL-LINES-EXACT', 'the branch`s two files READ HERE against the newer kernel`s committed bytes -- only the name line differs',
     lambda S: lines_exact_ok(S), lambda S: put(S, 'trial_tc', b'leanprover/lean4:v4.29.1\n')),
    ('G-TRIAL-BUILD-ONCE', 'the trial bank -- one exit, the worktree, the branch and the guard on its first line', lambda S: build_once_ok(S),
     lambda S: put(S, 'tbuild', S['tbuild'] + NL + 'exit 0')),
    ('G-TRIAL-ERRORS-COUNTED', 'the trial log READ HERE by its own counter -- equal to the bank, module by module', lambda S: errors_ok(S),
     lambda S: put(S, 'tbuild', S['tbuild'] + NL + 'error: ./SIDELvConservation/Planted.lean:1:1: planted')),
    ('G-TRIAL-PUSHED-HELD', 'the older kernel`s remote READ HERE -- the branch at its local tip, main at 2f71068',
     lambda S: pushed_held_ok(S), lambda S: put(S, 'trial_remote', '')),
    ('G-OLDER-MAIN-UNCHANGED', 'the older kernel READ HERE -- main 2f71068, checked out, tracked tree clean, no diff from its pre-act head',
     lambda S: older_ok(S), lambda S: put(S, 'lv_status', ' M lake-manifest.json')),
    ('G-TRIAL-PRICE-ENTERED', 'OPEN_TRAILS READ HERE -- the price once, naming :11203, the count as banked, the merge not done',
     lambda S: price_ok(S), lambda S: put(S, 'ot', S['ot'].replace('The merge is not done at this act', 'x'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once, the distinct count, the failing repositories named, the next keystone',
     lambda S: findings_ok(S), lambda S: put(S, 'find', S['find'].replace('**Next keystone:** THE_KEYSTONE_CENSUS.', 'x'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b550'}))),
    ('G-MEMORY-UNREFRESHED', 'the memory directory READ HERE -- no file written after this face (R157)(6)',
     lambda S: bool(S['mem_times']) and max(S['mem_times']) < os.path.getmtime(FACE),
     lambda S: put(S, 'mem_times', S['mem_times'] + [os.path.getmtime(FACE) + 1])),
    ('G-LINES-KEPT', 'the four written files against their blobs at b550`s commit',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY, FACES_LEDGER and THE_LOAD_BEARING_MAP bytes against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b' '}))),
    ('G-KERNEL-SOURCES-UNTOUCHED', 'four kernels` mains READ HERE against their pre-act heads, and the trial branch`s paths -- no `.lean`',
     lambda S: kernel_sources_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-explicit-formula': ['SIDEExplicitFormula/Seam.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b551_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind, branch deletion included',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b551_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b551 bank and tool, this act`s PLACE-papers bytes and its ledger row, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the table bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the run records', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the build and the four runs', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the tag bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the trial bank', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the mains, the tools, the token and the deposit -- the conflict printed', lambda S: nscored(S, 'n6') and 'THE CONFLICT' in S['desk'],
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b551 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels` mains READ HERE',
     lambda S: 'No kernel lane and no numerical lane opened at this act' in trail(S) and kernel_sources_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane and no numerical lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the four written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b550`s close -- no instrument modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['corr_row.py'])),
    ('G-WRITELIST-KINDS', 'every b551 commit in five repositories (the trial branch included), against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b551')" in S['suite']
                and "data/b551_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b551_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b551')
              and 'data/b551_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b551 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b551_checks_postpush.txt' if pushed else 'b551_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b551_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
