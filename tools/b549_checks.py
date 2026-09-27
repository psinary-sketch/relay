# -*- coding: utf-8 -*-
"""b549_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b549_registration_2026-09-26.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '24e02693'      # ### b548's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = '6999324'           # ### b548's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b549 —'


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


import b549_record as R
import b542_checks as K542
import banned_terms as BTM
RESR = 'phase1.5/proofs/THE_RESIDUE_OF_RH.md'
PPFILES = ['FINDINGS.md', 'OPEN_TRAILS.md', RESR]
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
SIDE_TIP = '2e43315'
CORRP = os.path.join(SIDE, 'CORRESPONDENCE.md')
HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': '2e43315'}
BRANCH_LINES = ['Deleted branch push-b548 (was 8f6cb351).', 'Deleted branch push-b548-closing (was 24e02693).', 'Deleted branch push-b548 (was 6999324).']
LVR = os.path.join('D:', os.sep, 'SIDE-lv-conservation')


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'))] + ['(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def jload(n):
    return json.loads(read(os.path.join(D, n)) or '{}')


def tree_count(rev):
    pat = r'^(noncomputable )?(private )?(theorem|lemma|def|structure|class|abbrev|inductive) (%s)\b' % '|'.join(R.TERMS)
    out = gits(LVR, 'grep', '-nE', pat, rev, '--', '*.lean')
    return len(set(re.search(r'(theorem|lemma|def|structure|class|abbrev|inductive) (\w+)', l).group(2) for l in out.split(NL) if l.strip()))


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    hk = gits(ROOT, 'log', '-1', '--format=%H', '--', 'data/b546_scores.json')
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b549_ferry.txt')),
        scan=read(os.path.join(D, 'b549_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b549_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b549_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b549_pins_stepzero.txt')),
        pins_runs=[read(os.path.join(D, 'b549_pins_stepzero%s.txt' % s)) for s in ('_first', '_rerun')],
        lock=read(sorted(glob.glob(os.path.join(D, 'b549_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b548_closing.txt')),
        addendum=read(os.path.join(D, 'b549_addendum.txt')),
        comp=read(os.path.join(D, 'b549_components.txt')),
        desk=read(os.path.join(D, 'b549_desk_notes.txt')),
        sc=jload('b549_scores.json'), reads=read(os.path.join(D, 'b549_reads.txt')),
        check=read(os.path.join(D, 'b549_residue_check.txt')), parsed=R.parse_check()[0],
        tj=jload('b549_tiers.json'), pj=jload('b549_premise.json'), ptxt=read(os.path.join(D, 'b549_premise.txt')),
        rj=jload('b549_residue_reads.json'), rtxt=read(os.path.join(D, 'b549_residue_reads.txt')),
        fj=jload('b549_family.json'), dtxt=read(os.path.join(D, 'b549_diagonal.txt')),
        cj=jload('b549_budget_control.json'), ctxt=read(os.path.join(D, 'b549_budget_control.txt')),
        bj=jload('b549_budget.json'), x3=jsonl(os.path.join(D, 'b549_sweep_xi_n3.jsonl')), x3txt=read(os.path.join(D, 'b549_sweep_xi_n3.txt')),
        b48x=jsonl(os.path.join(D, 'b548_sweep_xi.jsonl')), b48q=jsonl(os.path.join(D, 'b548_sweep_q.jsonl')),
        stj=jload('b549_stray.json'), sttxt=read(os.path.join(D, 'b549_stray.txt')),
        fnd=jload('b549_findings.json'), rr=jload('b549_residue_rows.json'),
        b506=json.loads(read(os.path.join(D, 'b506_c2_results.json')) or '{}'),
        loom=read(os.path.join(PP, 'archive', '2026-08-24-ledger-split', 'VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md')),
        b519=read(os.path.join(T, 'b519_window.py')),
        hk_subject=gits(ROOT, 'log', '-1', '--format=%s', hk) if hk else '', hk_body=gits(ROOT, 'log', '-1', '--format=%B', hk) if hk else '',
        hk_files=sorted(x for x in gits(ROOT, 'show', '--name-only', '--format=', hk).split(NL) if x.strip()) if hk else [],
        b546_status=gits(ROOT, 'status', '--porcelain', '--', 'data/b546_scores.json'),
        tag_count=tree_count('v0.10.0'), main_count=tree_count('main'),
        branches=read(os.path.join(D, 'b549_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), res=read(os.path.join(PP, RESR)),
        corr_now=open(CORRP, 'rb').read(), corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md'),
        mem_times=[os.path.getmtime(os.path.join(R.MEMDIR, f)) for f in os.listdir(R.MEMDIR)] if os.path.isdir(R.MEMDIR) else [],
        kernels={k: gits(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == '' and
                 gits(os.path.join('D:', os.sep, k), 'rev-parse', '--short', 'HEAD').startswith(h) for k, h in HEADS.items()},
        branch_lists={r: gits(r, 'branch', '--list', 'push-b548*') for r in (ROOT, PP)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b549_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b549_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b549_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b549_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b549 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b549_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b549_tiers.json', 'b549_sweep_xi_n3.jsonl', 'b549_budget_control.json',
                                                               'b549_stray.json', 'b549_findings.json', 'b549_residue_rows.json', 'b549_family.json'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in ('b549_ferry.txt', 'b549_reads.txt', 'b549_residue_check.txt')),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b549_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b549_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b549 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-9]_|^b54[012345678]_|^b334_', f)]
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
    return all(x in r for x in ('### phase1.5/proofs/THE_RESIDUE_OF_RH.md:1-211', 'ZeroActingPartial.lean:110-146', 'H2Sign.lean:22-31',
                                'Seam.lean:99-101', 'FINDINGS.md:5613-5615', '### tools/b519_window.py:67-135', '### tools/e16/carto_atlas.py:8-25',
                                '### relay data/b546_scores.json -- the working-tree diff', 'THE_LOAD_BEARING_MAP.md:66-71',
                                '### data/b506_c2_results.json:5550-5560', 'VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md:2296-2304'))


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and all(b.count(l) == 1 for l in BRANCH_LINES)


def pn(s):
    s = set(s)
    return 'std3' if s == {'propext', 'Classical.choice', 'Quot.sound'} else ('axiom-free' if not s else 'other')


def dispositions_ok(S):
    P_ = S['parsed']
    n = 0
    for res, ts, stated in R.ROWS:
        if not all(t in P_ for t in ts):
            return False
        u = set()
        for t in ts:
            u |= set(P_[t]['profile'])
        n += pn(u) == stated
    return n == 12 and S['tj'].get('disp_counts', {}).get('CARRIED') == 12 and all(r['disposition'] == 'CARRIED' for r in S['tj'].get('rows', []))


def tiers_ok(S):
    tt = S['tj'].get('terminals', [])
    tab = [l for l in fblock(S['res'], P(R.RESH)).split(NL) if l.startswith('| ') and '| **CARRIED** |' in l]
    return (len(tt) == 24 and all(t['tier'] == R.TIER[t['terminal']][0] for t in tt)
            and S['tj']['tier_counts'].get('T1-lit') + S['tj']['tier_counts'].get('T2') == 24 and len(tab) == 12)


def rows_lines_ok(S):
    b = fblock(S['res'], P(R.RESH))
    return (S['res'].count(P(R.RESH)) == 1 and b.count('| `h2`, the one open premise -- **MOVED** (b549, 2026-09-26)') == 1
            and b.count('EXISTENCE -- **CARRIED** (b549, 2026-09-26)') == 1 and 'T1-open' in b and 'constructs no operator and realizes no spectrum' in b
            and kept(S, RESR))


def sigma_ok(S):
    f = [x for x in S['b506'].get('found', []) if abs(x['rho'][1] - 16.290) < 0.01]
    return bool(f) and round(f[0]['rho'][0], 3) == 0.953 and S['rj'].get('sigma') == f[0]['rho'][0] and 'ρ ≈ 0.9533 + 16.290 i' in S['res']


def coherence_ok(S):
    lt = S['loom'].split(NL)
    ep = [l for l in lt[2295:2304] if 'Epstein' in l and l.startswith('|')]
    if not ep:
        return False
    vals = [float(c.strip().strip('*')) for c in ep[0].strip('|').split('|')[1:]]
    return round(min(vals), 2) == 0.65 and round(max(vals), 1) == 1.2 and S['rj'].get('c_ok') and S['rj'].get('z_ok') and S['rj'].get('d_ok')


def stems_ok(S):
    old = rd8(S['pp_prior'][RESR]).split(NL)
    hits = [(i + 1, m.group(0)) for i, l in enumerate(old) for m in BTM.PAT.finditer(l)]
    return (hits == [(s['line'], s['word']) for s in S['rj'].get('stems', [])] and len(hits) == 3
            and all(S['res'].split(NL)[i - 1] == old[i - 1] for i, _ in hits))


def xi3_ok(S):
    b = {c['a']: c for c in S['b48x'] if c['p'] == 3}
    xs = sorted(S['x3'], key=lambda c: c['a'])
    return ([c['a'] for c in xs] == [float(a) for a in range(10, 61)] and all(c['same_as_b548'] for c in xs)
            and all(b[c['a']]['h2'] == c['h2'] and b[c['a']]['r'] == c['r'] and b[c['a']]['B'] == c['B'] for c in xs))


def xi3_count(S):
    n = sum(1 for c in S['x3'] if abs(c['r']) <= c['B'] + c['E_arch'])
    return n == 51 and '### ξ order 3 : cells 51 ; VERIFY under the repair 51 of 51' in S['x3txt'] and S['bj'].get('xi', {}).get('verified') == 51


def q3_ok(S):
    b = {c['a']: c for c in S['b48q'] if c['p'] == 3}
    rows = S['bj'].get('q', [])
    if len(rows) != 51:
        return False
    for q in rows:
        c = b[q['a']]
        Br, Bpr = c['B'] + q['E_arch'], c['Bprime'] + q['E_arch']
        sign = 'NEGATIVE' if c['h2'] < -Br else ('POSITIVE' if c['h2'] > Br else 'UNDECIDED')
        reach = 'IN' if c['Etail'] <= Bpr else 'OUT'
        ver = abs(c['r']) <= Br
        st = ('VERIFIED-EST' if reach == 'IN' else 'VERIFIED-EST-TAIL') if (ver and sign != 'UNDECIDED') else ('VERIFIED-EST' if ver else 'UNVERIFIED')
        if [sign, reach, st] != [q['sign'], q['reach'], q['status']]:
            return False
    return S['bj'].get('q_changed') == []


def cost_ok(S):
    tot = {}
    for o, rows in (('q', S['b48q']), ('xi', S['b48x'])):
        prev, pp_, t = None, None, 0.0
        for c in rows:
            s = c['seconds']
            t += (s - prev) if (prev is not None and s >= prev and c['p'] == pp_) else s
            prev, pp_ = s, c['p']
        tot[o] = t
    fj = S['fj'].get('cost_total', {})
    return all(abs(tot[o] - fj.get(o, -1e9)) < 0.5 for o in ('q', 'xi')) and 'THE RE-PARAMETRIZED SWEEP, PRICED' in S['dtxt']


def pointer_absent(S):
    old = set(rd8(S['pp_prior']['FINDINGS.md']).split(NL))
    new = [l for l in S['find'].split(NL) if l not in old]
    return not any(':5529' in l and 'Appended at b549' in l for l in new) and S['fj'].get('self_convolution') is False


def back_matter_ok(S):
    act = S['fnd'].get('act', {}).get('heading_line')
    return (act is not None and ('is entered at `FINDINGS.md`:%d (b549)' % act) in S['res']
            and S['find'].split(NL)[act - 1] == P(R.ACTH))


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R159) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b549' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- one (R81) flag at line 87, one excepted stem at line 98, and the face says so',
     lambda S: '(R81) FLAGS : 1' in line_with(S['scan'], '(R81) FLAGS') and re.search(r'line 87\s+col \d+\s+only', S['scan']) is not None
     and re.search(r'line 98\s+col \d+\s+banned stem', S['scan']) is not None and 'The ferry scan carries one (R81) flag' in flat(S['face']),
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 1', '(R81) FLAGS : 2'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE -- the pins tool RUN ALONE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-PINS-RUNS-KEPT', 'the two pins runs, both banked -- 1, 0 -- and the step-zero bank equal to the re-run',
     lambda S: [line_with(t, 'REPOS HARD-FAILING').strip()[-1:] for t in S['pins_runs']] == ['1', '0'] and S['pins'] == S['pins_runs'][1],
     lambda S: put(S, 'pins_runs', S['pins_runs'][::-1])),
    ('G-REG-LOCKED-FIRST', 'the face lock block', lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK') and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b548`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b548' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b549' in S['ferry'] and 'ACT b549' in S['face'] and not glob.glob(os.path.join(D, 'b550_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b549')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; the reads and the #check before the lock, the components after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'NO CELL WAS COMPUTED FOR THIS ACT BEFORE THE SEAL' in flat(S['face'])
     and 'no web request made' in flat(S['face']) and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R159-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R159) END' in S['ferry'] and S['ot'].count('**(R159) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R159) ratified', '(R159) noted'))),
    ('G-READS-CITED', 'the reads bank -- the document whole, the modules, the pins, the window, the budget, the diff, the banks',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('### tools/e16/carto_atlas.py:8-25', 'x'))),
    ('G-RESIDUE-CHECK-FRESH', 'the #check bank -- lv main 2f71068, a clean tree, exit 0, every terminal with its profile',
     lambda S: 'HEAD 2f71068' in S['check'].split(NL)[0] and 'dirty=[]' in S['check'].split(NL)[0] and 'exit 0' in S['check']
     and all(t in S['parsed'] for t in R.TERMS),
     lambda S: put(S, 'parsed', {k: v for k, v in S['parsed'].items() if k != 'residue_irreducible'})),
    ('G-THREE-TREES', 'SIDE-lv-conservation READ HERE -- every terminal on main, none in the tag`s tree; the bank agrees',
     lambda S: S['main_count'] == 24 and S['tag_count'] == 0 and all(t['main'] == 1 and t['tip'] == 1 and t['tag'] == 0 for t in S['tj'].get('terminals', []))
     and S['tj'].get('identical') is True,
     lambda S: put(S, 'tag_count', 24)),
    ('G-ROW-DISPOSITIONS', 'the #check bank READ HERE -- each row`s union of fresh profiles against its stated profile; twelve CARRIED',
     lambda S: dispositions_ok(S), lambda S: put(S, 'parsed', dict(S['parsed'], exactly_two_clauses_obstruct=dict(statement='', profile=['propext'])))),
    ('G-TIERS', 'the tier bank against the tier table and the document`s block -- 24 terminals, T1-lit 7 and T2 17, twelve rows',
     lambda S: tiers_ok(S), lambda S: put(S, 'tj', dict(S['tj'], terminals=S['tj'].get('terminals', [])[:23]))),
    ('G-PREMISE-FORM', 'the premise bank -- no premise of the h2_sign shapes, the Li-channel premise named, the discharge priced by two routes',
     lambda S: S['pj'].get('match') == [] and any(p[0] == 'inequalityToPositivity' for p in S['pj'].get('premises', []))
     and 'THE DISCHARGE, PRICED IN LEMMAS' in S['ptxt'] and 'route W' in S['ptxt'] and 'route L' in S['ptxt'],
     lambda S: put(S, 'pj', dict(S['pj'], match=['liCriterion']))),
    ('G-ROW-LINES', 'THE_RESIDUE_OF_RH READ HERE -- the block once, the two rows once each, the document kept against its blob',
     lambda S: rows_lines_ok(S), lambda S: put(S, 'res', S['res'].replace('constructs no operator and realizes no spectrum', 'x'))),
    ('G-SIGMA-CHECK', 'the b506 bank READ HERE against §5', lambda S: sigma_ok(S),
     lambda S: put(S, 'b506', dict(S['b506'], found=[dict(f, rho=[0.9621, f['rho'][1]]) for f in S['b506'].get('found', [])]))),
    ('G-COHERENCE-CHECK', 'the loom table READ HERE against §4', lambda S: coherence_ok(S),
     lambda S: put(S, 'loom', S['loom'].replace('**0.650**', '**0.550**'))),
    ('G-STEM-LISTED', 'THE_RESIDUE_OF_RH at b548`s commit READ HERE -- every stem hit listed, each line unedited',
     lambda S: stems_ok(S), lambda S: put(S, 'rj', dict(S['rj'], stems=S['rj'].get('stems', [])[:2]))),
    ('G-LI-READING', 'the residue-reads bank -- §1 tiered T1-lit, §7`s sentence read in one sentence',
     lambda S: '### (f) §1 (:31)' in S['rtxt'] and 'T1-lit, per (R156)(1)' in S['rtxt'] and '### (f) §7 (:77), the reading in one sentence:' in S['rtxt'],
     lambda S: put(S, 'rtxt', S['rtxt'].replace('the reading in one sentence:', 'x'))),
    ('G-BACK-MATTER-POINTER', 'THE_RESIDUE_OF_RH and FINDINGS READ HERE -- the pointer names the act`s heading line',
     lambda S: back_matter_ok(S), lambda S: put(S, 'fnd', dict(S['fnd'], act=dict(S['fnd'].get('act', {}), heading_line=1)))),
    ('G-B548-READING-LINE', 'FINDINGS READ HERE -- the (R159)(1) line once, the zero and its swing',
     lambda S: S['find'].count(P(R.R1H)) == 1 and 't = 29.551761' in line_with(S['find'], P(R.R1H)) and '+74.0' in line_with(S['find'], P(R.R1H)),
     lambda S: put(S, 'find', S['find'].replace(P(R.R1H), 'x'))),
    ('G-NAVIGATOR-DEFECT-LINE', 'FINDINGS READ HERE -- the (R159)(2) line once, attributed to the navigator, the family read',
     lambda S: S['find'].count(P(R.R2H)) == 1 and 'wrong variable' in line_with(S['find'], P(R.R2H)) and 'NOT SCORABLE' in line_with(S['find'], P(R.R2H)),
     lambda S: put(S, 'find', S['find'].replace('wrong variable', 'x'))),
    ('G-FAMILY-READ', 'b519`s window READ HERE -- L = ln a, W = L − R; the bank`s verdict',
     lambda S: 'self.L = math.log(a)' in S['b519'] and 'self.W = self.L - self.R' in S['b519']
     and 'VERDICT : THE FAMILY IS NOT THE SELF-CONVOLUTION FAMILY' in S['dtxt'] and S['fj'].get('self_convolution') is False,
     lambda S: put(S, 'b519', S['b519'].replace('self.L = math.log(a)', 'self.L = a'))),
    ('G-H3-DISPOSED', 'the family bank -- H3 NOT SCORABLE, no diagonal read', lambda S: S['fj'].get('h3') == 'NOT SCORABLE' and 'H3 : NOT SCORABLE' in S['dtxt'],
     lambda S: put(S, 'fj', dict(S['fj'], h3='HOLDS'))),
    ('G-SWEEP-PRICED', 'b548`s cell banks READ HERE -- the per-cell seconds summed again, equal to the price', lambda S: cost_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], cost_total={'q': 1.0, 'xi': 1.0}))),
    ('G-BUDGET-READ', 'the control bank -- the assumption quoted, the order`s decay stated',
     lambda S: 'carto_atlas.py:12-14' in S['ctxt'] and 'hhat decays faster than any polynomial' in S['ctxt'] and '|u|^-4 at order 3' in S['ctxt'],
     lambda S: put(S, 'ctxt', S['ctxt'].replace('|u|^-4 at order 3', 'x'))),
    ('G-KERNEL-BOUND', 'the control bank -- the kernel bound holds for both objects', lambda S: S['cj'].get('kernel_ok') == {'xi': True, 'q': True},
     lambda S: put(S, 'cj', dict(S['cj'], kernel_ok={'xi': True, 'q': False}))),
    ('G-BUDGET-CONTROL', 'the control bank -- the four-fold grid`s piece below E_arch at both widths',
     lambda S: len(S['cj'].get('controls', [])) == 2 and all(abs(c['piece']) <= c['E_arch'] for c in S['cj']['controls']),
     lambda S: put(S, 'cj', dict(S['cj'], controls=[dict(c, piece=2 * c['E_arch']) for c in S['cj'].get('controls', [])]))),
    ('G-XI3-RECOMPUTED', 'the new cells READ HERE against b548`s cells -- 51 widths, every value but the budget equal',
     lambda S: xi3_ok(S), lambda S: put(S, 'x3', S['x3'][:-1])),
    ('G-XI3-VERIFY-COUNT', 'the new cells READ HERE -- |r| <= B + E_arch recounted, and the bank`s line', lambda S: xi3_count(S),
     lambda S: put(S, 'x3', [dict(c, E_arch=0.0) if c['a'] == 14.0 else c for c in S['x3']])),
    ('G-Q03-RESCORED', 'b548`s Q0 order-3 cells READ HERE -- sign, reach, status re-derived with E_arch; none changed',
     lambda S: q3_ok(S), lambda S: put(S, 'bj', dict(S['bj'], q_changed=[24.0]))),
    ('G-STRAY-DIFF-PRINTED', 'the stray bank -- the diff and the verdict', lambda S: '+  "OPEN_TRAILS.md",' in S['sttxt'] and 'VERDICT : b546`S OWN SCORE LINE' in S['sttxt'],
     lambda S: put(S, 'sttxt', S['sttxt'].replace('VERDICT : b546`S OWN', 'VERDICT : NOT'))),
    ('G-STRAY-SETTLED', 'relay`s log READ HERE -- one commit named for b546 carrying that one file and the diff; the file clean',
     lambda S: S['hk_subject'].startswith('b546 housekeeping') and S['hk_files'] == ['data/b546_scores.json'] and '+  "OPEN_TRAILS.md",' in S['hk_body']
     and S['b546_status'] == '',
     lambda S: put(S, 'b546_status', ' M data/b546_scores.json')),
    ('G-FINDINGS-ACT', 'FINDINGS READ HERE -- the act entry once, its tiers, the §7 reading, the next keystone',
     lambda S: (lambda b: S['find'].count(P(R.ACTH)) == 1 and '**Next keystone:** THE_IDENTITY_CHAIN.' in b and 'T1-lit 7' in b
                and '§7, read in the light of the compiled criterion' in b)(fblock(S['find'], P(R.ACTH))),
     lambda S: put(S, 'find', S['find'].replace('**Next keystone:** THE_IDENTITY_CHAIN.', 'x'))),
    ('G-POINTER-CONDITIONAL', 'FINDINGS against its blob -- no :5529 line, since the diagonal did not run', lambda S: pointer_absent(S),
     lambda S: put(S, 'find', S['find'] + NL + '*Appended at b549 to the detection-geometries entry (`FINDINGS.md`:5529): x*')),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b548'}))),
    ('G-MEMORY-UNREFRESHED', 'the memory directory READ HERE -- no file written after this face (R157)(6)',
     lambda S: bool(S['mem_times']) and max(S['mem_times']) < os.path.getmtime(FACE),
     lambda S: put(S, 'mem_times', S['mem_times'] + [os.path.getmtime(FACE) + 1])),
    ('G-LINES-KEPT', 'the three written files against their blobs at b548`s commit',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY, SPIRAL_MAP, FACES_LEDGER and THE_LOAD_BEARING_MAP bytes against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b' '}))),
    ('G-KERNELS-UNTOUCHED', 'the four repositories, READ HERE -- clean and at their heads',
     lambda S: len(S['kernels']) == 4 and all(S['kernels'].values()), lambda S: put(S, 'kernels', dict(S['kernels'], **{'SIDE-kernel': False}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b549_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind, branch deletion included',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b549_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b549 bank and tool and this act`s own PLACE-papers bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the tier bank and lv', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the premise bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the family bank', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the budget bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the stray bank and the log', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the residue-reads bank', lambda S: nscored(S, 'n6'), lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-N7-SCORED', 'the desk against the blobs, the tools, the token and the kernels', lambda S: nscored(S, 'n7'),
     lambda S: put(S, 'sc', dict(S['sc'], n7=not S['sc'].get('n7')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b549 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels READ HERE',
     lambda S: 'The numerical lane opened for this act and shuts at its close; no kernel lane' in trail(S) and all(S['kernels'].values()),
     lambda S: put(S, 'ot', S['ot'].replace('shuts at its close; no kernel lane', 'stays open'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the three written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-CORR-UNTOUCHED', 'SIDE-global-section`s correspondence ledger against its blob -- no row this act',
     lambda S: S['corr_now'] == S['corr_prior'] and S['corr_now'] != b'', lambda S: put(S, 'corr_now', S['corr_now'] + b'| 391 | a row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b548`s close -- no instrument modified (the cells imported, the budget term added beside)',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['b511_families.py'])),
    ('G-WRITELIST-KINDS', 'every b549 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b549')" in S['suite']
                and "data/b549_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b549_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b549')
              and 'data/b549_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b549 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b549_checks_postpush.txt' if pushed else 'b549_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b549_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
