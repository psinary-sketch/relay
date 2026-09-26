# -*- coding: utf-8 -*-
"""b548_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b548_registration_2026-09-26.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'f272e2e0'      # ### b547's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = '2549901'           # ### b547's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b548 —'


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


import b548_record as R
import b542_checks as K542
PPFILES = ['FINDINGS.md', 'OPEN_TRAILS.md']
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
SIDE_TIP = '2e43315'
CORRP = os.path.join(SIDE, 'CORRESPONDENCE.md')
HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': '2e43315'}
BRANCH_LINES = ['Deleted branch push-b547 (was 91cbda06).', 'Deleted branch push-b547-closing (was f272e2e0).', 'Deleted branch push-b547 (was 2549901).']
ORDERS = [3, 5, 7, 9, 11]
GRID = [float(a) for a in range(10, 61)]


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'))] + ['(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def jload(n):
    return json.loads(read(os.path.join(D, n)) or '{}')


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b548_ferry.txt')),
        scan=read(os.path.join(D, 'b548_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b548_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b548_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b548_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b548_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b547_closing.txt')),
        addendum=read(os.path.join(D, 'b548_addendum.txt')),
        comp=read(os.path.join(D, 'b548_components.txt')),
        desk=read(os.path.join(D, 'b548_desk_notes.txt')),
        sc=jload('b548_scores.json'), reads=read(os.path.join(D, 'b548_reads.txt')),
        itxt=read(os.path.join(D, 'b548_interference.txt')), ij=jload('b548_interference.json'),
        irows=jsonl(os.path.join(D, 'b548_interference.jsonl')), b522=jsonl(os.path.join(D, 'b522_cells.jsonl')),
        q=jsonl(os.path.join(D, 'b548_sweep_q.jsonl')), xi=jsonl(os.path.join(D, 'b548_sweep_xi.jsonl')),
        qtxt=read(os.path.join(D, 'b548_sweep_q0.txt')), xtxt=read(os.path.join(D, 'b548_sweep_xi.txt')),
        h2txt=read(os.path.join(D, 'b548_h2.txt')), sj=jload('b548_sweep.json'),
        fs=jload('b548_field_sources.json'), fdj=jload('b548_field.json'), fnd=jload('b548_findings.json'),
        branches=read(os.path.join(D, 'b548_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        corr_now=open(CORRP, 'rb').read(), corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md'),
        mem_times=[os.path.getmtime(os.path.join(R.MEMDIR, f)) for f in os.listdir(R.MEMDIR)] if os.path.isdir(R.MEMDIR) else [],
        kernels={k: gits(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == '' and
                 gits(os.path.join('D:', os.sep, k), 'rev-parse', '--short', 'HEAD').startswith(h) for k, h in HEADS.items()},
        branch_lists={r: gits(r, 'branch', '--list', 'push-b547*') for r in (ROOT, PP)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b548_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b548_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b548_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b548_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b548 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b548_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b548_interference.jsonl', 'b548_sweep_q.jsonl', 'b548_sweep_xi.jsonl',
                                                               'b548_field_sources.json', 'b548_field.json', 'b548_findings.json'))),
        before_lock=os.path.getmtime(os.path.join(D, 'b548_ferry.txt')) < os.path.getmtime(FACE),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b548_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b548_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b548 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-9]_|^b54[01234567]_|^b334_', f)]
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


def outside_bt(text):
    return sum(l.count('`') % 2 for l in text.split(NL))


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
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0].split(',')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == S['recomputed'][k]


P = R.poss


def reads_ok(S):
    r = S['reads']
    return all(x in r for x in ('### tools/b521_tail.py:44-128', '### tools/b519_window.py:185-245', 'FINDINGS.md:5529-5531',
                                'FINDINGS.md:5575-5580', 'b522_run_log.txt', 'the xi bank: tools/e16/zeta_ordinates.npy, first 10000'))


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and all(b.count(l) == 1 for l in BRANCH_LINES)


def match_ok(S):
    rows = {r['a']: r for r in S['irows']}
    bank = {c['a']: c for c in S['b522']}
    return (sorted(rows) == [float(a) for a in range(30, 46)]
            and all(a in bank and abs(rows[a]['h2'] - bank[a]['h2']) <= rows[a]['Eround'] for a in rows))


def split_ok(S):
    return len(S['irows']) == 16 and all(abs(r['pair'] + r['rest'] - r['Z']) <= r['Eround'] and abs(r['pair'] - r['pair_check']) <= r['Eround']
                                         and abs(r['rest'] - r['rest_check']) <= r['Eround'] for r in S['irows'])


def contrib_ok(S):
    t = S['itxt']
    out = True
    for a in (36, 37, 38):
        blk = seg(t, '  a = %d : pair' % a, 4000).split(NL)[1:11]
        out = out and len(blk) == 10 and all(l.strip().startswith(('on ', 'off ')) and 'contribution' in l for l in blk)
    return out


def kstar_of(row):
    pos = sorted([x[2] for x in row['terms'] if x[2] > 0], reverse=True)
    ex = row['rest'] - abs(row['pair'])
    if ex <= 0:
        return 0
    cum = 0.0
    for k, v in enumerate(pos, 1):
        cum += v
        if row['rest'] - cum - abs(row['pair']) <= 0:
            return k
    return None


def h1_ok(S):
    rows = {r['a']: r for r in S['irows']}
    ks = {a: kstar_of(rows[a]) for a in (36.0, 37.0, 38.0)}
    H = S['ij'].get('H1', {})
    c1 = all(rows[a]['rest'] > abs(rows[a]['pair']) for a in (36.0, 37.0, 38.0))
    c1b = all(not rows[a]['rest'] > abs(rows[a]['pair']) for a in (34.0, 35.0, 39.0, 40.0, 41.0))
    lines = [line_with(S['itxt'], x) for x in ('H1.1', 'H1.2', 'H1.3', 'H1.4', 'REFUTER 1', 'REFUTER 2', 'REFUTER 3')]
    return (all(lines) and H.get('c1') == c1 and H.get('c1b') == c1b and H.get('c2') == all(v is not None and v <= 5 for v in ks.values())
            and {float(k): v for k, v in S['ij'].get('kstar', {}).items()} == ks and ('HOLDS' in lines[0]) == c1)


def cells_ok(S):
    for c in S['q'] + S['xi']:
        sign = 'NEGATIVE' if c['h2'] < -c['B'] else ('POSITIVE' if c['h2'] > c['B'] else 'UNDECIDED')
        reach = 'IN' if c['Etail'] <= c['Bprime'] else 'OUT'
        ver = abs(c['r']) <= c['B']
        status = ('VERIFIED-EST' if reach == 'IN' else 'VERIFIED-EST-TAIL') if (ver and sign != 'UNDECIDED') else ('VERIFIED-EST' if ver else 'UNVERIFIED')
        if (sign, reach, status) != (c['sign'], c['reach'], c['status']) or abs(c['B'] - (c['Eu'] + c['Ek'] + c['Etail'] + c['Eround'])) > 1e-9 * c['B']:
            return False
    return True


def complete_ok(S):
    want = sorted((p, a) for p in ORDERS for a in GRID)
    return all(sorted((c['p'], c['a']) for c in S[o]) == want for o in ('q', 'xi'))


def changes(S, o, p):
    F_ = [c['h2'] for c in sorted([c for c in S[o] if c['p'] == p], key=lambda c: c['a'])]
    d = [F_[i + 1] - F_[i] for i in range(len(F_) - 1)]
    return [int(10 + i + 1) for i in range(len(d) - 1) if (d[i] > 0) != (d[i + 1] > 0)]


def diffs_ok(S):
    for o, txt, key in (('q', S['qtxt'], 'q'), ('xi', S['xtxt'], 'xi')):
        for p in ORDERS:
            ch = changes(S, o, p)
            if S['sj'].get(key, {}).get(str(p), {}).get('dF_sign_changes') != ch:
                return False
            if ('### n = %d : dF/da sign changes at a = %s' % (p, ch)) not in txt:
                return False
    return True


def smallest(S, p):
    neg = sorted(c['a'] for c in S['q'] if c['p'] == p and c['sign'] == 'NEGATIVE')
    return neg[0] if neg else None


def h2_ok(S):
    H = S['sj'].get('H2', {})
    sn = {str(p): smallest(S, p) for p in ORDERS}
    x1 = all(c['h2'] >= -c['Eround'] for c in S['xi'])
    q2 = sn['7'] is not None and sn['9'] is not None and sn['11'] is not None and sn['11'] < sn['9'] < sn['7']
    q3 = any(c['sign'] == 'NEGATIVE' for c in S['q'] if c['p'] in (3, 5))
    t = S['h2txt']
    return (H.get('smallest_negative') == sn and H.get('x1') == x1 and H.get('q2') == q2 and H.get('ref3') == q3
            and all(line_with(t, x) for x in ('H2.xi.1', 'H2.xi.2', 'H2.q.1', 'H2.q.2', 'REFUTER 1', 'REFUTER 2', 'REFUTER 3'))
            and ('FIRES' in line_with(t, 'REFUTER 3')) == q3)


def pointer_ok(S):
    ls = [l for l in S['find'].split(NL) if l.startswith(P(R.PTR))]
    act = S['fnd'].get('write', {}).get('heading_line')
    return len(ls) == 1 and ('`FINDINGS.md`:%d' % act) in ls[0] and S['find'].split(NL)[act - 1] == P(R.ACTH) and 'READING' in ls[0]


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R158) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b548' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b547`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b547' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b548' in S['ferry'] and 'ACT b548' in S['face'] and not glob.glob(os.path.join(D, 'b549_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b548')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; no cell and no web request before the lock, the cells and fetches after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'NO CELL WAS COMPUTED FOR THIS ACT BEFORE THE SEAL' in flat(S['face'])
     and 'no web request made' in flat(S['face']) and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R158-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R158) END' in S['ferry'] and S['ot'].count('**(R158) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R158) ratified', '(R158) noted'))),
    ('G-READS-CITED', 'the reads bank -- the window and cell verbatim, the banks, the two FINDINGS anchors, the run log',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('FINDINGS.md:5529-5531', 'x'))),
    ('G-MATCH-B522', 'the interference cells READ HERE against b522`s cell bank -- 16 widths, each within its floor',
     lambda S: match_ok(S), lambda S: put(S, 'irows', [dict(r, h2=r['h2'] + 1.0) if r['a'] == 37.0 else r for r in S['irows']])),
    ('G-SPLIT-SUMS', 'the interference cells -- pair + rest = Z, and each against its term-by-term check, to the floor',
     lambda S: split_ok(S), lambda S: put(S, 'irows', [dict(r, rest=r['rest'] + 1e-3) if r['a'] == 36.0 else r for r in S['irows']])),
    ('G-CONTRIBUTORS', 'the interference bank -- ten ranked contributors printed at each of 36, 37, 38',
     lambda S: contrib_ok(S), lambda S: put(S, 'itxt', S['itxt'].replace('  a = 37 : pair', '  a = 37 pair'))),
    ('G-H1-SCORED', 'the interference cells READ HERE -- k* and the clauses recomputed, the bank`s rows and json agree',
     lambda S: h1_ok(S), lambda S: put(S, 'ij', dict(S['ij'], kstar={'36.0': 6, '37.0': 1, '38.0': 1}))),
    ('G-INTERFERENCE-BANK', 'the bank`s own sections (a)-(d)',
     lambda S: all(x in S['itxt'] for x in ('### (a)-(b)', '### (c)', '### (d) H1, clause by clause')),
     lambda S: put(S, 'itxt', S['itxt'].replace('### (d) H1, clause by clause', 'x'))),
    ('G-SWEEP-COMPLETE', 'the two cell banks READ HERE -- every (n, a) of the grid once at each object, 510 cells',
     lambda S: complete_ok(S) and len(S['q']) + len(S['xi']) == 510, lambda S: put(S, 'xi', S['xi'][:-1])),
    ('G-CELL-RULE', 'every banked cell READ HERE -- sign, reach and status recomputed from its own numbers by READING (2)',
     lambda S: cells_ok(S), lambda S: put(S, 'q', [dict(c, status='VERIFIED-EST') if c['p'] == 3 else c for c in S['q']])),
    ('G-DIFFERENCES', 'the cell banks against the sweep banks -- dF/da sign changes recomputed and printed per n and object',
     lambda S: diffs_ok(S), lambda S: put(S, 'qtxt', S['qtxt'].replace('### n = 7 : dF/da', '### n = 7 : dF'))),
    ('G-H2-SCORED', 'the cell banks READ HERE -- the smallest negative widths, xi.1, Q0.2 and refuter 3 recomputed; the bank`s rows agree',
     lambda S: h2_ok(S), lambda S: put(S, 'sj', dict(S['sj'], H2=dict(S['sj'].get('H2', {}), q2=True)))),
    ('G-SWEEP-BANKS', 'the two sweep banks -- five order blocks each, the statuses per order',
     lambda S: all(sum(1 for l in t.split(NL) if re.match(r'^### n = \d+ : 51 cells$', l)) == 5 for t in (S['qtxt'], S['xtxt'])),
     lambda S: put(S, 'xtxt', S['xtxt'].replace('### n = 9 : 51 cells', 'x'))),
    ('G-COST-PRINTED', 'the face`s READING (6) and the components -- the estimate before running, the per-cell seconds banked',
     lambda S: 'about 950 s per object and order' in flat(S['face']) and 'THE COST, ESTIMATED BEFORE RUNNING' in S['comp']
     and all('seconds' in c for c in S['q'] + S['xi']),
     lambda S: put(S, 'comp', S['comp'].replace('THE COST, ESTIMATED BEFORE RUNNING', 'x'))),
    ('G-FIELD-REPAIR', 'FINDINGS READ HERE -- the sources block once, naming :5575, at the line the bank names; :5575`s text unchanged',
     lambda S: (S['find'].count(P(R.FIELDH)) == 1 and 'FINDINGS.md`:5575' in fblock(S['find'], P(R.FIELDH))
                and S['find'].split(NL)[S['fdj']['heading_line'] - 1] == P(R.FIELDH)
                and S['find'].split(NL)[5574] == rd8(S['pp_prior']['FINDINGS.md']).split(NL)[5574]),
     lambda S: put(S, 'find', S['find'].replace(P(R.FIELDH), 'x'))),
    ('G-ZHU-QUOTED', 'FINDINGS READ HERE -- the claim and scope sentences, each inside quotation marks, from the fetched abstract',
     lambda S: (lambda b: ('"%s"' % S['fs']['zhu']['claim_sentence']) in b and ('"%s"' % S['fs']['zhu']['scope_sentence']) in b
                and 'arXiv:2608.24827' in b)(fblock(S['find'], P(R.FIELDH))),
     lambda S: put(S, 'find', S['find'].replace('autocorrelation support 1.6, 2.3 times', 'x'))),
    ('G-LIU-PROVENANCE', 'FINDINGS READ HERE -- the alphaXiv URL, NAVIGATOR-READ, not an arXiv number, not fetched',
     lambda S: (lambda b: S['fs']['liu']['url'] in b and '**NAVIGATOR-READ**' in b and 'not an arXiv number' in b
                and 'the seat did not fetch it' in b)(fblock(S['find'], P(R.FIELDH))),
     lambda S: put(S, 'find', S['find'].replace('the seat did not fetch it', 'x'))),
    ('G-ZENODO-METADATA', 'FINDINGS READ HERE -- both records` title, author and date; no platform address in the block',
     lambda S: (lambda b: all(r['title'] in b and r['author'] in b and r['date'] in b and r['record'] in b for r in S['fs']['zenodo'])
                and ('zenodo' + '.org') not in b.lower())(fblock(S['find'], P(R.FIELDH))),
     lambda S: put(S, 'find', S['find'].replace('Harlow, Jim', 'x'))),
    ('G-GEOMETRY-POINTER', 'FINDINGS READ HERE -- one pointer line naming :5529 and the act entry`s line',
     lambda S: pointer_ok(S), lambda S: put(S, 'find', S['find'].replace(P(R.PTR), 'x'))),
    ('G-FINDINGS-ACT', 'FINDINGS READ HERE -- the act entry once, both tables, READING, nothing about the zeros claimed',
     lambda S: (lambda b: S['find'].count(P(R.ACTH)) == 1 and '| H1 clause |' in b and '| H2 clause |' in b and 'Graded READING' in b
                and 'Nothing about ζ’s zeros is claimed' in b and '**Next keystone:** THE_RESIDUE_OF_RH.' in b)(fblock(S['find'], P(R.ACTH))),
     lambda S: put(S, 'find', S['find'].replace('| H2 clause |', 'x'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b547'}))),
    ('G-MEMORY-UNREFRESHED', 'the memory directory READ HERE -- no file written after this face (R157)(6)',
     lambda S: bool(S['mem_times']) and max(S['mem_times']) < os.path.getmtime(FACE),
     lambda S: put(S, 'mem_times', S['mem_times'] + [os.path.getmtime(FACE) + 1])),
    ('G-LINES-KEPT', 'the two written files against their blobs at b547`s commit',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY, SPIRAL_MAP and FACES_LEDGER bytes against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b' '}))),
    ('G-KERNELS-UNTOUCHED', 'the four repositories, READ HERE -- clean and at their heads',
     lambda S: len(S['kernels']) == 4 and all(S['kernels'].values()), lambda S: put(S, 'kernels', dict(S['kernels'], **{'SIDE-kernel': False}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b548_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind, branch deletion included',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b548_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b548 bank and tool and this act`s own PLACE-papers bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the interference bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the interference bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the xi sweep', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the Q0 sweep', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against FINDINGS and the sources bank', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the blobs, the tools, the token and the kernels', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b548 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels READ HERE',
     lambda S: 'The numerical lane opened for this act and shuts at its close; no kernel lane' in trail(S) and all(S['kernels'].values()),
     lambda S: put(S, 'ot', S['ot'].replace('shuts at its close; no kernel lane', 'stays open'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the two written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-CORR-UNTOUCHED', 'SIDE-global-section`s correspondence ledger against its blob -- no row this act',
     lambda S: S['corr_now'] == S['corr_prior'] and S['corr_now'] != b'', lambda S: put(S, 'corr_now', S['corr_now'] + b'| 391 | a row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b547`s close -- no instrument modified (the cells imported, not edited)',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['b521_tail.py'])),
    ('G-WRITELIST-KINDS', 'every b548 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b548')" in S['suite']
                and "data/b548_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b548_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b548')
              and 'data/b548_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b548 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b548_checks_postpush.txt' if pushed else 'b548_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b548_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
