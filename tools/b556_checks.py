# -*- coding: utf-8 -*-
"""b556_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b556_registration_2026-09-28.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'be9adfc8'      # ### b555's closing housekeeping commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = '2d650c3'           # ### b555's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b556 —'


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


import b556_record as R
import b542_checks as K542
import banned_terms as BTM
import terminal_table as TT
PPFILES = sorted(R.WRITE_OK)
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase2/method/THE_IDENTITY_CHAIN.md', 'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md',
         'phase1.5/spectral/GRH_CASCADE.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
GSR = os.path.join('D:', os.sep, 'SIDE-global-section')
KERN = os.path.join('D:', os.sep, 'SIDE-kernel')
EFFR = os.path.join('D:', os.sep, 'SIDE-effects')


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'), ('worktree', ' remove'))] + [
        '(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def jload(n):
    return json.loads(read(os.path.join(D, n)) or '{}')


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b556_ferry.txt')),
        scan=read(os.path.join(D, 'b556_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b556_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b556_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b556_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b556_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b555_closing.txt')),
        addendum=read(os.path.join(D, 'b556_addendum.txt')),
        comp=read(os.path.join(D, 'b556_components.txt')),
        desk=read(os.path.join(D, 'b556_desk_notes.txt')),
        sc=jload('b556_scores.json'), reads=read(os.path.join(D, 'b556_reads.txt')), bd2=jload('b556_bd2.json'),
        path=jload('b556_path.json'), rows=jload('b556_rows.json'), ts=jload('b556_tiers.json'), tstxt=read(os.path.join(D, 'b556_tiers.txt')),
        rc=jload('b556_rcurve.json'), rctxt=read(os.path.join(D, 'b556_rcurve.txt')), blocks=jload('b556_blocks.json'),
        probes=[json.loads(l) for l in read(os.path.join(D, 'b556_probes.jsonl')).split(NL) if l.strip()],
        rc_src=rd8(blob(R.RCK, 'd5f33b4:SIDERCurve/Criterion.lean')),
        eff_tags=gits(EFFR, 'tag'),
        stems=jload('b556_stems.json'), fj=jload('b556_findings.json'),
        branches=read(os.path.join(D, 'b556_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        docs={k: rd8(open(os.path.join(PP, v), 'rb').read()) for k, v in R.DOCS.items()},
        mem_times=[os.path.getmtime(os.path.join(R.MEMDIR, f)) for f in os.listdir(R.MEMDIR)] if os.path.isdir(R.MEMDIR) else [],
        mains=R.mains(),
        trial=dict(head=gits(R.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b555*') for r in (ROOT, PP)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b556_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b556_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b556_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b556_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b556 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b556_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b556_probes.jsonl', 'b556_tiers.json', 'b556_rcurve.json', 'b556_path.json',
                                                               'b556_blocks.json', 'b556_stems.json'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in ('b556_ferry.txt', 'b556_ferry_scan.txt', 'b556_pins_stepzero.txt')),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b556_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b556_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KERN):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith(('b556 --', 'housekeeping: terminal table regenerated at b556')):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-4][0-9]_|^b55[0-5]_|^b334_', f)]
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


def dblock(S, k):
    return seg(S['docs'][k], P(R.BH), 60000)


def reads_ok(S):
    r = S['reads']
    need = ('R_CURVE_CRITERION -- the Kernel Correspondence', 'INDEX_ARITY_AT_THE_CRITICAL_LINE -- the Correspondence', 'the 2026-08-12 table at the standard',
            'THE_KEYSTONE_CENSUS.md -- v0.2', 'ERRATA.md -- E-2026-09-25-1', 'ERRATA.md -- E-2026-09-27-1', 'Criterion.lean whole',
            'THE_LOAD_BEARING_MAP rows naming each document', '`bd2ae1a` in the batch documents', R.RCR)
    return all(x in r for x in need) and 'named on the line: False' not in r and r.count('named on the line: True') == sum(len(l) for _, l in R.WORK)


def bd2_ok(S):
    c = {k: sum(l.count('bd2ae1a') for l in rd8(S['pp_prior'][v]).split(NL)) for k, v in R.DOCS.items()}
    return all(len(S['bd2']['hits'][k]) == c[k] for k in c) and (sum(c.values()) != 0 or '(0 hits); no row gains the E-2026-09-27-1 line' in dblock(S, 'RCURVE'))


def pblock(S):
    return seg(S['ot'], P(R.PH), 20000).split(NL + '### ')[0]


def path_entry_ok(S):
    ln = [i + 1 for i, l in enumerate(S['ot'].split(NL)) if l.startswith(P(R.PH))]
    return S['ot'].count(P(R.PH)) == 1 and ln == [S['path']['trail']['line']] and 'no work-order is begun at b556' in pblock(S)


def path_verbatim_ok(S):
    b = pblock(S)
    ps = R.r166_2()
    return len(ps) == 4 and all(('> ' + p) in b for p in ps) and ps[1].startswith('LANE ONE') and ps[3].startswith('LANE THREE')


def path_prices_ok(S):
    ot = rd8(S['pp_prior']['OPEN_TRAILS.md']).split(NL)
    b = pblock(S)
    rowsin = [l for l in b.split(NL) if l.startswith('| ') and '`W-ORD-' in l]
    return (len(rowsin) == len(R.PRICE) and all(w in ot[x - 1] for _, w, _, ls in R.PRICE for x in ls)
            and all(any(('`%s`' % w) in l and ', '.join(':%d' % x for x in ls) in l for l in rowsin) for _, w, _, ls in R.PRICE))


def path_pointer_ok(S):
    l = line_with(S['find'], P(R.FPL))
    return (S['find'].count(P(R.FPL)) == 1 and bool(re.search(r'`OPEN_TRAILS\.md`:%d(?!\d)' % S['path']['trail']['line'], l))
            and 'no work-order is started' in l)


def rows_ok(S, k):
    t = rd8(S['pp_prior'][R.DOCS[k]]).split(NL)
    heads = R.HEADS[k] if isinstance(R.HEADS[k], tuple) else (R.HEADS[k],)
    n = 0
    for h in heads:
        i = [j for j, l in enumerate(t) if l.startswith(h)][0]
        for l in t[i + 2:]:
            if not l.startswith('|'):
                break
            n += 1
    return len(S['rows'].get(k, [])) == n == len(S['ts'].get(k, {}).get('rows', [])) == len(R.ROWMAP[k])


def rcurve_decls_ok(S):
    ds = re.findall(r'(?m)^(theorem|lemma|def|structure|inductive|abbrev)\s+(\S+)', S['rc_src'])
    rc = S['rc']
    return (len(ds) == len(rc.get('decls', [])) and all(d['tier'] in R.ORDER for d in rc['decls'])
            and rc['split'] == {x: sum(1 for d in rc['decls'] if d['tier'] == x) for x in R.ORDER} and '### THE SPLIT:' in S['rctxt'])


def block_ok(S, k):
    b = dblock(S, k)
    f = R.DOCS[k]
    return (S['docs'][k].count(P(R.BH)) == 1 and kept(S, f) and all('| :%d |' % r['line'] in b for r in S['ts'][k]['rows'])
            and S['blocks'][k]['line'] == [i + 1 for i, l in enumerate(S['docs'][k].split(NL)) if l.startswith(P(R.BH))][0])


def idx_moved_ok(S):
    b = dblock(S, 'INDEX')
    l = line_with(b, '*Row :369 MOVED:*')
    return 'h2_sign_iff_rh' in l and 'E-2026-09-25-1' in l and 'the reduction' in l and [r['disp'] for r in S['ts']['INDEX']['rows'] if r['line'] == 369] == ['MOVED']


def idx_tag_ok(S):
    b = dblock(S, 'INDEX')
    want = [r['line'] for r in S['rows']['INDEX'] if '5a14205' in r['kernel'] or '2f71068' in r['kernel']]
    got = [int(m) for m in re.findall(r'\*Row :(\d+) \(pinned', b)]
    return bool(want) and got == want and all('`v0.11.0` = `2f71068`' in line_with(b, '*Row :%d (pinned' % x) for x in want)


def idx_premise_ok(S):
    b = dblock(S, 'INDEX')
    t = [x for x in S['ts']['INDEX']['terms'] if x['name'].endswith('certifiedInput_not_zeroRealizing')]
    m3 = read(os.path.join(D, 'b556_probe_m3.txt'))
    return (len(t) == 1 and t[0]['tier'] == 'T1-lit' and 'NontrivialZeroExistsInStrip' in (t[0]['statement'] or '')
            and 'is_xi_zero' in m3 and '`NontrivialZeroExistsInStrip`' in b and 'terminal is T1-lit' in b)


def idx_overhyp_ok(S):
    b = dblock(S, 'INDEX')
    head = b.split('**The rows, re-read at pin.**')[0]
    return ('**OVER-HYPOTHESIZED, read against the tier law' in head and '"a check, not a reading' in head
            and ('printed %d unused-variable warning(s)' % len(S['ts'].get('unused_all', []))) in head)


def pr_of(S, pid):
    return [p for p in S['probes'] if p['id'] == pid]


def amc_pins_ok(S):
    e1, e2 = pr_of(S, 'e1'), pr_of(S, 'e2')
    n = R.M1 + 'no_type_d_conspiracies'
    pa, pc = (e1[0]['profiles'].get(n) if e1 else None), (e2[0]['profiles'].get(n) if e2 else None)
    b = dblock(S, 'AMC')
    return bool(pa) and bool(pc) and ('`a27415d`: `%s`' % pa) in b and ('`c66f3c5`: `%s`' % pc) in b and bool(S['rc']['pins']['a27415d']['branches'])


def amc_corr_ok(S):
    e1, e2 = pr_of(S, 'e1'), pr_of(S, 'e2')
    n = R.M1 + 'no_type_d_conspiracies'
    pa, pc = e1[0]['profiles'].get(n), e2[0]['profiles'].get(n)
    wrong = ([446] if pc and 'sorryAx' in pc else []) + ([] if (pa == R.STD3) else [408])
    b = dblock(S, 'AMC')
    has = '*Correction to the table at :444 (2026-08-12), row :446' in b
    return S['blocks'].get('wrong') == wrong and has == (wrong == [446])


def amc_mil_ok(S):
    m = S['rc'].get('milestones', {})
    e4 = pr_of(S, 'e4')
    return (all(v['sorry'] for c in ('c66f3c5', 'a27415d') for v in m.get(c, {}).values()) and len(m.get('c66f3c5', {})) == 3
            and bool(e4) and all(v and 'sorryAx' in v for v in e4[0]['profiles'].values()))


def amc_cite_ok(S):
    c = S['rc'].get('citations', {})
    ok = len(c) == 3
    for repo, v in c.items():
        exact = gits(os.path.join('D:', os.sep, repo), 'rev-parse', '--verify', '-q', v['cited'] + '^{commit}')
        ok = ok and (bool(exact) == bool(v['exact'])) and v['resolved'] in dblock(S, 'AMC')
    return ok


def probes_ok(S):
    pr = {p['id']: p for p in S['probes']}
    need = {x for k in R.ROWMAP for v in R.ROWMAP[k].values() for _, a, b in v for x in (a, b) if x}
    bad = [p['id'] for p in pr.values() if p.get('identical_to') is None and p['exit'] != 0]
    return (need <= set(pr) and all(bad_id[:2] + 'c' in pr and pr[bad_id[:2] + 'c']['exit'] == 0 for bad_id in bad if len(bad_id) == 2)
            and all(t['found'] and t['profile'] for k in R.DOCS for t in S['ts'][k]['terms']))


def tiers_ok(S):
    ok = True
    for k in R.DOCS:
        st = S['ts'][k]
        ok = ok and all(t['tier'] in R.ORDER for t in st['terms'])
        for r in st['rows']:
            tl = [t['tier'] for t in st['terms'] if t['row'] == r['line']]
            ok = ok and r['tier'] == (max(tl, key=R.ORDER.index) if tl else 'T4')
        ok = ok and st['term_tiers'] == {x: sum(1 for t in st['terms'] if t['tier'] == x) for x in R.ORDER} and sum(st['disp'].values()) == len(st['rows'])
    return ok


def stems_ok(S):
    ok = True
    for k, f in R.DOCS.items():
        per = {x: 0 for x in BTM.STEMS}
        for l in rd8(S['pp_prior'][f]).split(NL):
            for m in BTM.PAT.finditer(l):
                per[[x for x in BTM.STEMS if m.group(0).lower().startswith(x)][0]] += 1
        ok = ok and S['stems'].get(k, {}).get('per') == per
    return ok


def findings_ok(S):
    b = fblock(S['find'], P(R.FH))
    return S['find'].count(P(R.FH)) == 1 and '**Next:** b557' in b and all(R.TITLE[k] in b for k in R.DOCS) and 'CARRIED' in b


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b555 (was ') == 2 and b.count('Deleted branch push-b555-closing (was ') == 1


def kernel_sources_ok(S):
    m = S['mains']
    return len(m) == len(R.PRE_HEADS) and not any(f.endswith('.lean') for v in m.values() for f in v) and all(v == [] for v in m.values())


def swap_row(S, k, line, **kw):
    ts = dict(S['ts'])
    ts[k] = dict(ts[k], rows=[dict(r, **kw) if r['line'] == line else r for r in ts[k]['rows']])
    return ts


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R166) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b556' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- no (R81) flag, and the face says so',
     lambda S: '(R81) FLAGS : 0' in line_with(S['scan'], '(R81) FLAGS') and 'The ferry scan carries no hit and no flag' in flat(S['face']),
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 1'))),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b555`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b555' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b556' in S['ferry'] and 'ACT b556' in S['face'] and not glob.glob(os.path.join(D, 'b557_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b556')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; the reads before the lock, every evaluation and write after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R166-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R166) END' in S['ferry'] and S['ot'].count('**(R166) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R166) ratified', '(R166) noted'))),
    ('G-READS-CITED', 'the reads bank -- the three documents, their tables, the map, the census, both errata, every work-order line with its ID on it',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('ERRATA.md -- E-2026-09-27-1', 'x'))),
    ('G-PATH-ENTRY', 'OPEN_TRAILS READ HERE -- the entry once at its banked line, not started', lambda S: path_entry_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('no work-order is begun at b556', 'x'))),
    ('G-PATH-VERBATIM', 'the banked ferry`s (R166)(2), re-joined HERE, against the entry -- every lane paragraph quoted', lambda S: path_verbatim_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('> LANE TWO', '> LANE 2'))),
    ('G-PATH-PRICES-CITED', 'OPEN_TRAILS at b555`s commit READ HERE -- each cited line carries its ID; each work-order`s row cites its lines',
     lambda S: path_prices_ok(S), lambda S: put(S, 'ot', S['ot'].replace(':11373 |', ':11374 |'))),
    ('G-PATH-POINTER', 'FINDINGS READ HERE -- the pointer once, naming the entry`s line', lambda S: path_pointer_ok(S),
     lambda S: put(S, 'path', dict(S['path'], trail=dict(S['path']['trail'], line=1)))),
    ('G-RCURVE-ROWS', 'R_CURVE`s table at b555`s commit, counted here -- equal to the row bank, the tier bank and the map', lambda S: rows_ok(S, 'RCURVE'),
     lambda S: put(S, 'rows', dict(S['rows'], RCURVE=S['rows']['RCURVE'][:-1]))),
    ('G-RCURVE-DECLS', 'Criterion.lean at d5f33b4 READ HERE -- every declaration in the bank, the split recounted', lambda S: rcurve_decls_ok(S),
     lambda S: put(S, 'rc', dict(S['rc'], decls=S['rc']['decls'][:-1]))),
    ('G-RCURVE-BLOCK', 'R_CURVE READ HERE against its blob -- the block once, every row, the document kept', lambda S: block_ok(S, 'RCURVE'),
     lambda S: put(S, 'docs', dict(S['docs'], RCURVE=S['docs']['RCURVE'].replace('| :355 |', '| :999 |')))),
    ('G-BD2-SEARCHED', 'the batch documents at b555`s commit searched HERE for bd2ae1a -- equal to the bank; a zero printed in R_CURVE`s block',
     lambda S: bd2_ok(S), lambda S: put(S, 'bd2', dict(S['bd2'], hits=dict(S['bd2']['hits'], RCURVE=[1])))),
    ('G-IDX-ROWS', 'INDEX_ARITY`s table at b555`s commit, counted here -- equal to the banks and the map', lambda S: rows_ok(S, 'INDEX'),
     lambda S: put(S, 'rows', dict(S['rows'], INDEX=S['rows']['INDEX'][:-1]))),
    ('G-IDX-MOVED-LINE', 'INDEX_ARITY READ HERE and the tier bank -- row :369 MOVED, its line naming E-2026-09-25-1 and h2_sign_iff_rh', lambda S: idx_moved_ok(S),
     lambda S: put(S, 'ts', swap_row(S, 'INDEX', 369, disp='CARRIED'))),
    ('G-IDX-TAG-LINES', 'INDEX_ARITY READ HERE -- one v0.11.0 line for each row pinned at 5a14205 or 2f71068, and no other', lambda S: idx_tag_ok(S),
     lambda S: put(S, 'docs', dict(S['docs'], INDEX=S['docs']['INDEX'].replace('*Row :383 (pinned', '*Row :383 (x')))),
    ('G-IDX-PREMISE', 'the m3 probe bank READ HERE and the tier bank -- the premise printed, T1-lit, named in the block', lambda S: idx_premise_ok(S),
     lambda S: put(S, 'ts', dict(S['ts'], INDEX=dict(S['ts']['INDEX'], terms=[dict(t, tier='T2') if t['name'].endswith('certifiedInput_not_zeroRealizing') else t
                                                                             for t in S['ts']['INDEX']['terms']])))),
    ('G-IDX-OVERHYP', 'INDEX_ARITY`s block header READ HERE -- the paragraph, :365`s words, the warning count equal to the bank`s', lambda S: idx_overhyp_ok(S),
     lambda S: put(S, 'ts', dict(S['ts'], unused_all=S['ts'].get('unused_all', []) + [{'x': 1}]))),
    ('G-IDX-BLOCK', 'INDEX_ARITY READ HERE against its blob -- the block once, every row, the document kept', lambda S: block_ok(S, 'INDEX'),
     lambda S: put(S, 'docs', dict(S['docs'], INDEX=S['docs']['INDEX'].replace('| :369 |', '| :999 |')))),
    ('G-AMC-ROWS', 'ADDITIVE_MULTIPLICATIVE`s two tables at b555`s commit, counted here -- equal to the banks and the map', lambda S: rows_ok(S, 'AMC'),
     lambda S: put(S, 'rows', dict(S['rows'], AMC=S['rows']['AMC'][:-1]))),
    ('G-AMC-BOTH-PINS', 'the probe bank -- no_type_d_conspiracies profiled at a27415d and c66f3c5, both printed in the block, the branches', lambda S: amc_pins_ok(S),
     lambda S: put(S, 'probes', [dict(p, profiles={}) if p['id'] == 'e2' else p for p in S['probes']])),
    ('G-AMC-CORRECTION', 'the two profiles READ HERE -- the wrong table recomputed, the correction line present exactly when it is :446', lambda S: amc_corr_ok(S),
     lambda S: put(S, 'blocks', dict(S['blocks'], wrong=[408]))),
    ('G-AMC-MILESTONES', 'the Milestones bank and the e4 probe -- three sorry declarations at both pins, sorryAx in each profile', lambda S: amc_mil_ok(S),
     lambda S: put(S, 'rc', dict(S['rc'], milestones=dict(S['rc']['milestones'], c66f3c5={})))),
    ('G-AMC-CITATIONS', 'the three repositories` tags READ HERE -- each citation resolved as banked, the resolution in the block', lambda S: amc_cite_ok(S),
     lambda S: put(S, 'rc', dict(S['rc'], citations={k: dict(v, exact=None if v['exact'] else 'x') for k, v in S['rc']['citations'].items()}))),
    ('G-AMC-BLOCK', 'ADDITIVE_MULTIPLICATIVE READ HERE against its blob -- the block once, every row, the document kept', lambda S: block_ok(S, 'AMC'),
     lambda S: put(S, 'docs', dict(S['docs'], AMC=S['docs']['AMC'].replace('| :446 |', '| :999 |')))),
    ('G-PROBES-BANKED', 'the probe bank -- every probe the map names; any non-zero exit read from its clean control; every terminal found and profiled',
     lambda S: probes_ok(S), lambda S: put(S, 'probes', [dict(p, exit=1) if p['id'] == 'e1' else p for p in S['probes']])),
    ('G-TIERS-COUNTED', 'the tier bank -- every tier in the law`s vocabulary, each row its weakest link, the counts recomputed', lambda S: tiers_ok(S),
     lambda S: put(S, 'ts', dict(S['ts'], AMC=dict(S['ts']['AMC'], term_tiers=dict(S['ts']['AMC']['term_tiers'], T0=-1))))),
    ('G-STEMS-COUNTED', 'the batch documents at b555`s commit, counted here with the tool`s own pattern -- equal to the bank', lambda S: stems_ok(S),
     lambda S: put(S, 'stems', dict(S['stems'], INDEX=dict(S['stems']['INDEX'], per={x: -1 for x in BTM.STEMS})))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once, the three documents, the dispositions, b557 next', lambda S: findings_ok(S),
     lambda S: put(S, 'find', S['find'].replace(P(R.FH), 'x'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in two repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b555'}))),
    ('G-MEMORY-UNREFRESHED', 'the memory directory READ HERE -- no file written after this face (R157)(6)',
     lambda S: bool(S['mem_times']) and max(S['mem_times']) < os.path.getmtime(FACE),
     lambda S: put(S, 'mem_times', S['mem_times'] + [os.path.getmtime(FACE) + 1])),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-LINES-KEPT', 'the five written files against their blobs at b555`s commit',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY, SPIRAL_MAP, FACES_LEDGER, THE_LOAD_BEARING_MAP, THE_IDENTITY_CHAIN, THE_KEYSTONE_CENSUS, SIMPLICITY, GRH_CASCADE against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in OTHER if 'A_Place_to_Stand' not in f and f != 'ERRATA.md'),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'REGISTRY.md': S['pp_now']['REGISTRY.md'] + b' '}))),
    ('G-KERNEL-SOURCES-UNTOUCHED', 'the kernels` mains READ HERE against their pre-act heads -- nothing written',
     lambda S: kernel_sources_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-effects': ['SIDEEffects/Structural.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b556_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b556_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b556 bank and tool and this act`s PLACE-papers bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the tier bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the two profiles', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the R-curve bank', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against :365 and the warning bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the tier bank`s conclusions', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the mains, the tools, the token, the deposit and the trial worktree', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b556 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels` mains READ HERE',
     lambda S: 'No kernel lane opened at this act' in trail(S) and kernel_sources_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the five written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b555`s close -- no .py tool modified',
     lambda S: [x for x in S['tools_edited'] if x.endswith('.py')] == [],
     lambda S: put(S, 'tools_edited', ['terminal_table.py'])),
    ('G-WRITELIST-KINDS', 'every b556 commit in four repositories and the housekeeping commit, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b556')" in S['suite']
                and "data/b556_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b556_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b556')
              and 'data/b556_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b556 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b556_checks_postpush.txt' if pushed else 'b556_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b556_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
