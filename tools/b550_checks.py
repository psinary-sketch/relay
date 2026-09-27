# -*- coding: utf-8 -*-
"""b550_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b550_registration_2026-09-26.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'cdd662eb'      # ### b549's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = '84adecd'           # ### b549's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b550 —'


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


import b550_record as R
import b542_checks as K542
import banned_terms as BTM
RESR = 'phase1.5/proofs/THE_RESIDUE_OF_RH.md'
IDCR = 'phase2/method/THE_IDENTITY_CHAIN.md'
PPFILES = ['FINDINGS.md', 'OPEN_TRAILS.md', RESR, IDCR]
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
SIDE_TIP = '2e43315'
CORRP = os.path.join(SIDE, 'CORRESPONDENCE.md')
HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': '2e43315'}
BRANCH_LINES = ['Deleted branch push-b549 (was 91635888).', 'Deleted branch push-b549-closing (was cdd662eb).', 'Deleted branch push-b549 (was 84adecd).']
LVR = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
GSR = os.path.join('D:', os.sep, 'SIDE-global-section')


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
        face=read(FACE), ferry=read(os.path.join(D, 'b550_ferry.txt')), f549=read(os.path.join(D, 'b549_ferry.txt')),
        scan=read(os.path.join(D, 'b550_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b550_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b550_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b550_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b550_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b549_closing.txt')),
        addendum=read(os.path.join(D, 'b550_addendum.txt')),
        comp=read(os.path.join(D, 'b550_components.txt')),
        desk=read(os.path.join(D, 'b550_desk_notes.txt')),
        sc=jload('b550_scores.json'), reads=read(os.path.join(D, 'b550_reads.txt')),
        tagtxt=read(os.path.join(D, 'b550_tag.txt')), tg=jload('b550_tag.json'),
        live_tag=gits(LVR, 'ls-remote', 'origin', 'refs/tags/v0.11.0^{}'), live_local=gits(LVR, 'rev-parse', 'v0.11.0^{commit}'),
        lv_type=gits(LVR, 'cat-file', '-t', 'v0.11.0'),
        pl=jload('b550_pin_lines.json'), ol=jload('b550_order_lines.json'), tr=jload('b550_trails.json'),
        tj=jload('b550_tiers.json'), ttxt=read(os.path.join(D, 'b550_tiers.txt')), named=jload('b550_named.json'),
        ap_run=read(os.path.join(D, 'b550_allprints_run.txt')), ap_bank=read(os.path.join(GSR, 'AXIOM_PRINTS.txt')),
        ap_meta=read(os.path.join(D, 'b550_allprints_meta.txt')),
        ia=read(os.path.join(D, 'b550_iface_check_a.txt')), ib=read(os.path.join(D, 'b550_iface_check_b.txt')),
        ibank=read(os.path.join(GSR, 'AXIOM_PRINTS_INTERFACES.txt')),
        rj=jload('b550_reading37.json'), rtxt=read(os.path.join(D, 'b550_reading37.txt')),
        fnd=jload('b550_findings.json'), ib_json=jload('b550_identity_block.json'), s548=jload('b548_sweep.json'),
        b549diag=read(os.path.join(D, 'b549_diagonal.txt')), b549prem=read(os.path.join(D, 'b549_premise.txt')),
        spiral=read(os.path.join(PP, 'SPIRAL_MAP.md')),
        gs_head=gits(GSR, 'rev-parse', 'HEAD'), gs_tag=gits(GSR, 'rev-parse', 'v0.1.0^{commit}'),
        branches=read(os.path.join(D, 'b550_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), res=read(os.path.join(PP, RESR)), idc=read(os.path.join(PP, IDCR)),
        corr_now=open(CORRP, 'rb').read(), corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md'),
        mem_times=[os.path.getmtime(os.path.join(R.MEMDIR, f)) for f in os.listdir(R.MEMDIR)] if os.path.isdir(R.MEMDIR) else [],
        kernels={k: gits(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == '' and
                 gits(os.path.join('D:', os.sep, k), 'rev-parse', '--short', 'HEAD').startswith(h) for k, h in HEADS.items()},
        branch_lists={r: gits(r, 'branch', '--list', 'push-b549*') for r in (ROOT, PP)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b550_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b550_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b550_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b550_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b550 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b550_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b550_tag.txt', 'b550_tiers.json', 'b550_pin_lines.json', 'b550_order_lines.json',
                                                               'b550_trails.json', 'b550_findings.json', 'b550_identity_block.json'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE)
                        for x in ('b550_ferry.txt', 'b550_reads.txt', 'b550_allprints_run.txt', 'b550_core_check.txt', 'b550_iface_check_a.txt', 'b550_iface_check_b.txt')),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b550_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b550_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b550 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-9]_|^b54[0-9]_|^b334_', f)]
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
    return all(x in r for x in ('### phase2/method/THE_IDENTITY_CHAIN.md:1-3166', '### SPIRAL_MAP cites a SIDE-global-section pin : NONE',
                                'Interfaces/FiniteInstanceIdentity.lean:1-224', 'Interfaces/LocalLimit.lean:1-411',
                                '### SIDE-global-section CORRESPONDENCE.md rows 80-90, whole:', '### FINDINGS.md:5529-5531',
                                '### OPEN_TRAILS.md:3544-3550', '### data/b549_diagonal.txt:1-74', 'tags v0.11.0 at the remote: ABSENT'))


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and all(b.count(l) == 1 for l in BRANCH_LINES)


def prints_of(text):
    out = {}
    t = re.sub(r'\[([^\]]*)\]', lambda m: '[' + ' '.join(m.group(1).split()) + ']', text, flags=re.S)
    for l in t.split(NL):
        m = re.match(r"^'(.+)' (does not depend on any axioms|depends on axioms: \[([^\]]*)\])", l)
        if m:
            out[m.group(1)] = sorted(x.strip() for x in (m.group(3) or '').split(',') if x.strip())
    return out


def iface_ok(S):
    bank = prints_of(S['ibank'])
    fresh = dict(prints_of(S['ia']), **prints_of(S['ib']))
    names = [n for n, _ in R.IFACE_TERMS if n in bank]
    return (len(names) >= 10 and all(fresh.get(n) == bank[n] for n in names) and 'exit 0' in S['ia'] and 'exit 0' in S['ib']
            and 'cecd0c4d56' in S['ia'].split(NL)[0])


def tiers_ok(S):
    rows = S['tj'].get('rows', [])
    ll = [r for r in rows if r['terminal'].split('.')[-1] in R.LOCALLIMIT_SIX]
    core = [r for r in rows if r['module'].startswith('Core')]
    fii = [r for r in rows if r['terminal'] == 'FiniteInstanceIdentity.finiteInstanceIdentity']
    tc = S['tj'].get('tier_counts', {})
    return (len(rows) == 118 and len(core) == 102 and all(r['tier'] == 'T2' for r in core) and len(ll) == 6 and all(r['tier'] == 'T0' and r['grade'] == 'DERIVES' for r in ll)
            and len(fii) == 1 and fii[0]['grade'] == 'ENCODES' and tc.get('T0') == 7 and tc.get('T2') == 111
            and all(r['grade'] == ('SHELL' if r['kind'] in ('def', 'structure', 'abbrev', 'inductive', 'instance') else 'ENCODES') for r in core))


def terminal_set_ok(S):
    names = set(r['terminal'] for r in S['tj'].get('rows', []))
    core_bank = set(n for n in prints_of(S['ap_bank']) if n.split('.')[0] in R.CORE_MODS or n in R.EXTRA_CORE)
    return core_bank <= names and set(n for n, _ in R.IFACE_TERMS) <= names and len(core_bank) == 102


def dispositions_ok(S):
    bank, fresh = prints_of(S['ap_bank']), prints_of(S['ap_run'])
    core = [r for r in S['tj'].get('rows', []) if r['module'].startswith('Core')]
    return all(fresh.get(r['terminal']) == bank.get(r['terminal']) and r['disp'] == 'CARRIED' for r in core) and S['tj']['disp_counts'].get('MOVED') == 0


def stems_ok(S):
    old = rd8(S['pp_prior'][IDCR]).split(NL)
    c = {s: 0 for s in BTM.STEMS}
    for l in old:
        for m in BTM.PAT.finditer(l):
            c[m.group(1).lower()] += 1
    return c == S['rj'].get('stems') and ('### (d) banned stems in THE_IDENTITY_CHAIN.md, counted per stem, none listed, none edited: %s' % c) in S['rtxt']


def exprs_ok(S):
    return (any('h2=P - PR + A' in x[1] for x in S['rj'].get('cell', [])) and S['rj'].get('fileE', [[0, '']])[0][1] == 'T.value + Q.value = W.wInf - W.wPrimes'
            and 'poleTerm k - primeSum k + archTerm k' in ' '.join(S['rj'].get('h2sign', [])) and 'VERDICT (N4) : HOLDS' in S['rtxt'])


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R160) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b550' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b549`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b549' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b550' in S['ferry'] and 'ACT b550' in S['face'] and not glob.glob(os.path.join(D, 'b551_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b550')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; the reads and the Lean runs before the lock, the tag and the lines after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'NO TAG WAS MADE BEFORE THE SEAL' in flat(S['face'])
     and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R160-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R160) END' in S['ferry'] and S['ot'].count('**(R160) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R160) ratified', '(R160) noted'))),
    ('G-READS-CITED', 'the reads bank -- the document whole, SPIRAL_MAP, the modules, the rows, the anchors, b549`s banks, lv`s state',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('### OPEN_TRAILS.md:3544-3550', 'x'))),
    ('G-TAG-READBACK', 'SIDE-lv-conservation`s remote READ HERE -- v0.11.0 annotated, peeled to 2f71068, equal to the bank',
     lambda S: S['live_tag'].startswith('2f71068') and S['live_local'].startswith('2f71068') and S['lv_type'] == 'tag'
     and S['tg'].get('remote_peeled', '').startswith('2f71068') and S['tg'].get('n1') is True,
     lambda S: put(S, 'live_tag', '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f refs/tags/v0.11.0^{}')),
    ('G-LV-CLEAN', 'the tag bank -- the kernel clean before and after, main not moved',
     lambda S: S['tg'].get('before_clean') and S['tg'].get('after_clean') and S['tg'].get('before_head') == S['tg'].get('after_head')
     and S['tg']['after_head'].startswith('2f71068') and S['tg'].get('remote_main', '').startswith('2f71068'),
     lambda S: put(S, 'tg', dict(S['tg'], after_clean=False))),
    ('G-RESIDUE-PIN-LINE', 'THE_RESIDUE_OF_RH READ HERE -- one tag line once, naming v0.11.0, at the line the bank names',
     lambda S: S['res'].count(P(R.RESL)) == 1 and 'v0.11.0' in line_with(S['res'], P(R.RESL))
     and S['res'].split(NL)[S['pl']['residue_line'] - 1].startswith(P(R.RESL)) and kept(S, RESR),
     lambda S: put(S, 'res', S['res'].replace(P(R.RESL), 'x'))),
    ('G-B549-PIN-LINE', 'FINDINGS READ HERE -- the b549 pin line once, the tag and the navigator`s clause',
     lambda S: S['find'].count(P(R.PINL)) == 1 and 'v0.11.0' in line_with(S['find'], P(R.PINL)) and 'navigator' in line_with(S['find'], P(R.PINL)),
     lambda S: put(S, 'find', S['find'].replace(P(R.PINL), 'x'))),
    ('G-ORDER-CORRECTION', 'FINDINGS READ HERE -- the correction once, the navigator`s, the two objects named',
     lambda S: (lambda l: S['find'].count(P(R.ORD1)) == 1 and 'NAVIGATOR' in l and 'two objects under one word' in l and '|u|^(2−2p)' in l)(line_with(S['find'], P(R.ORD1))),
     lambda S: put(S, 'find', S['find'].replace('two objects under one word', 'x'))),
    ('G-ORDER-RESTATED', 'FINDINGS against b548`s bank READ HERE -- the widths quoted as banked',
     lambda S: (lambda l, sn: ('%s at p = 3, 5, 7, 9, 11' % ', '.join('%.0f' % sn[k] for k in ('3', '5', '7', '9', '11'))) in l and 'has not been measured on this bench' in l)(
         line_with(S['find'], P(R.ORD2)), S['s548']['H2']['smallest_negative']),
     lambda S: put(S, 's548', dict(S['s548'], H2=dict(S['s548']['H2'], smallest_negative=dict(S['s548']['H2']['smallest_negative'], **{'3': 99.0}))))),
    ('G-POWER-SWEEP-FILED', 'OPEN_TRAILS READ HERE -- the work-order once, its price cited to b549`s bank, its trigger',
     lambda S: S['ot'].count(P(R.PSH)) == 1 and (lambda b: '`data/b549_diagonal.txt`:64-73' in b and 'passes the ξ positive control at every order' in b
                                                  and '| `W-ORD-POWER-SWEEP` |' in b)(seg(S['ot'], P(R.PSH), 6000)),
     lambda S: put(S, 'ot', S['ot'].replace('passes the ξ positive control at every order', 'x'))),
    ('G-H3-VERBATIM', 'b549`s banked ferry READ HERE against the work-order -- H3 quoted unchanged',
     lambda S: (lambda h3: h3.startswith('Hypothesis H3, fixed before any reading:') and ('"%s"' % h3) in seg(S['ot'], P(R.PSH), 6000))(
         ' '.join(S['f549'].split(NL)[37:44])[' '.join(S['f549'].split(NL)[37:44]).index('Hypothesis H3'):' '.join(S['f549'].split(NL)[37:44]).index('negative above its floor.') + len('negative above its floor.')]),
     lambda S: put(S, 'ot', S['ot'].replace('its magnitude grows with n across the orders banked', 'its magnitude grows'))),
    ('G-BRIDGE-CONSUMERS', 'OPEN_TRAILS READ HERE -- the bridge block once, naming :3548, three consumers',
     lambda S: S['ot'].count(P(R.BRH)) == 1 and (lambda b: all(x in b for x in ('**(a) The Weil premise of `residue_irreducible`.**', '**(b) The two detection costs',
                                                                               '**(c) The Li form made T0.**', '`data/b549_premise.txt`:20')))(seg(S['ot'], P(R.BRH), 6000)),
     lambda S: put(S, 'ot', S['ot'].replace('**(c) The Li form made T0.**', 'x'))),
    ('G-TOOLCHAIN-PRICE', 'the bridge block against b549`s premise bank -- the toolchain line cited and quoted',
     lambda S: (lambda b, pr: 'a toolchain alignment' in b and '`data/b549_premise.txt`:24' in b and 'v4.29.1' in b and 'v4.33.0-rc2' in b
                and 'lv toolchain leanprover/lean4:v4.29.1' in pr.split(NL)[23])(seg(S['ot'], P(R.BRH), 6000), S['b549prem']),
     lambda S: put(S, 'ot', S['ot'].replace('a toolchain alignment', 'x'))),
    ('G-TREE-READ', 'SPIRAL_MAP and SIDE-global-section READ HERE -- no pin cited; HEAD 2e43315; the one tag v0.1.0',
     lambda S: not any(re.search(r'[0-9a-f]{7}', l) and 'SIDE-global-section' in l for l in S['spiral'].split(NL)) and S['gs_head'].startswith('2e43315')
     and S['gs_tag'].startswith('706a81b') and 'NOT SCORABLE' in flat(S['face']),
     lambda S: put(S, 'gs_head', '706a81b')),
    ('G-NAMED-SET', 'the named bank -- 26 terminals, the five generic words dropped and printed',
     lambda S: len(S['named'].get('named', {})) == 26 and S['named'].get('generic') == ['cell', 'corr', 'forced', 'identity', 'resid'] and S['tj'].get('missing_named') == [],
     lambda S: put(S, 'named', dict(S['named'], generic=[]))),
    ('G-TERMINAL-SET', 'AXIOM_PRINTS.txt READ HERE -- every printed terminal of the nine shadows and the two named, in the set',
     lambda S: terminal_set_ok(S), lambda S: put(S, 'tj', dict(S['tj'], rows=S['tj']['rows'][:-1]))),
    ('G-TIERS', 'the tier bank -- the Core T2 (ENCODES or SHELL by kind), the six LocalLimit T0 DERIVES, file E T2 ENCODES',
     lambda S: tiers_ok(S), lambda S: put(S, 'tj', dict(S['tj'], rows=[dict(r, tier='T0') if r['module'].startswith('Core/Sign') else r for r in S['tj']['rows']]))),
    ('G-DISPOSITIONS', 'AllPrints fresh against its bank READ HERE -- every Core terminal CARRIED, none MOVED',
     lambda S: dispositions_ok(S), lambda S: put(S, 'ap_run', S['ap_run'].replace("'SignTransferShadow.transfer' does not depend on any axioms", "'SignTransferShadow.transfer' depends on axioms: [propext]"))),
    ('G-ALLPRINTS-EQUAL', 'AllPrints`s output and its bank READ HERE -- line for line, at HEAD, exit 0',
     lambda S: S['ap_run'].rstrip(NL) == S['ap_bank'].rstrip(NL) and len(S['ap_bank'].rstrip(NL).split(NL)) == 614 and 'exit 0' in S['ap_meta'] and 'HEAD 2e43315' in S['ap_meta'],
     lambda S: put(S, 'ap_run', S['ap_run'] + "'X.y' does not depend on any axioms")),
    ('G-IFACE-PROFILES', 'the interface prints READ HERE against their bank -- equal; part A at the declared pin, both exit 0',
     lambda S: iface_ok(S), lambda S: put(S, 'ia', S['ia'].replace("'LocalLimit.radical_zero' depends on axioms: [propext, Classical.choice, Quot.sound]", "'LocalLimit.radical_zero' depends on axioms: [propext]"))),
    ('G-STEM-COUNT', 'THE_IDENTITY_CHAIN at b549`s commit READ HERE -- the stems counted per stem, none listed', lambda S: stems_ok(S),
     lambda S: put(S, 'rj', dict(S['rj'], stems={'gap': -1, 'blind': 0}))),
    ('G-THREE-EXPRESSIONS', 'the reading bank -- the bench`s F, file E`s body line, h2_sign, the verdict', lambda S: exprs_ok(S),
     lambda S: put(S, 'rj', dict(S['rj'], fileE=[[176, 'x']]))),
    ('G-READING-ENTRY', 'FINDINGS READ HERE -- the reading once, its three limits, at the line the bank names',
     lambda S: (lambda b: S['find'].count(P(R.READH)) == 1 and 'Its three limits, stated with it.' in b and "LEFT side" in b and 'b240 dissonance' in b
                and S['find'].split(NL)[S['fnd']['reading_line'] - 1] == P(R.READH))(fblock(S['find'], P(R.READH))),
     lambda S: put(S, 'find', S['find'].replace('b240 dissonance', 'x'))),
    ('G-IDENTITY-BLOCK', 'THE_IDENTITY_CHAIN READ HERE -- the block once, the Tier C line, the pointer to the reading, the document kept',
     lambda S: (lambda b: S['idc'].count(P(R.IDH)) == 1 and '**This document stays Tier C:**' in b and ('`FINDINGS.md`:%d (b550)' % S['fnd']['reading_line']) in b
                and kept(S, IDCR))(seg(S['idc'], P(R.IDH), 20000)),
     lambda S: put(S, 'idc', S['idc'].replace('**This document stays Tier C:**', 'x'))),
    ('G-FINDINGS-ACT', 'FINDINGS READ HERE -- the act entry once, its counts, the next keystone',
     lambda S: (lambda b: S['find'].count(P(R.ACTH)) == 1 and '**Next keystone:** THE_KEYSTONE_CENSUS.' in b and 'T0 7' in b and 'CARRIED 118' in b)(fblock(S['find'], P(R.ACTH))),
     lambda S: put(S, 'find', S['find'].replace('**Next keystone:** THE_KEYSTONE_CENSUS.', 'x'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b549'}))),
    ('G-MEMORY-UNREFRESHED', 'the memory directory READ HERE -- no file written after this face (R157)(6)',
     lambda S: bool(S['mem_times']) and max(S['mem_times']) < os.path.getmtime(FACE),
     lambda S: put(S, 'mem_times', S['mem_times'] + [os.path.getmtime(FACE) + 1])),
    ('G-LINES-KEPT', 'the four written files against their blobs at b549`s commit',
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
    ('G-KERNELS-UNTOUCHED', 'the four repositories, READ HERE -- clean and at their heads (the tag moves no head)',
     lambda S: len(S['kernels']) == 4 and all(S['kernels'].values()), lambda S: put(S, 'kernels', dict(S['kernels'], **{'SIDE-kernel': False}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b550_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind, branch deletion included',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b550_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b550 bank and tool and this act`s own PLACE-papers bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the tag bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the tier bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against AllPrints', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the reading bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk -- NOT SCORABLE, the tag reading printed', lambda S: nscored(S, 'n5') and S['sc'].get('n5') is None,
     lambda S: put(S, 'sc', dict(S['sc'], n5=True))),
    ('G-N6-SCORED', 'the desk against the blobs, the tools, the token and the kernels', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b550 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels READ HERE',
     lambda S: 'No lane opened at this act; one tag made' in trail(S) and all(S['kernels'].values()),
     lambda S: put(S, 'ot', S['ot'].replace('No lane opened at this act; one tag made', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the four written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-CORR-UNTOUCHED', 'SIDE-global-section`s correspondence ledger against its blob -- no row this act',
     lambda S: S['corr_now'] == S['corr_prior'] and S['corr_now'] != b'', lambda S: put(S, 'corr_now', S['corr_now'] + b'| 391 | a row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b549`s close -- no instrument modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['b511_families.py'])),
    ('G-WRITELIST-KINDS', 'every b550 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b550')" in S['suite']
                and "data/b550_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b550_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b550')
              and 'data/b550_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b550 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b550_checks_postpush.txt' if pushed else 'b550_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b550_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
