# -*- coding: utf-8 -*-
"""b547_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b547_registration_2026-09-26.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '9e06a910'      # ### b546's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = '37b36b3'           # ### b546's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b547 —'


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


import b547_record as R
import b542_checks as K542
FACESR = 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md'
PPFILES = ['FINDINGS.md', 'OPEN_TRAILS.md', 'FACES_LEDGER.md', FACESR]
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
SIDE_TIP = '2e43315'
CORRP = os.path.join(SIDE, 'CORRESPONDENCE.md')
HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': '2e43315'}
BRANCH_LINES = ['Deleted branch push-b546 (was ce0cccfb).', 'Deleted branch push-b546-closing (was 9e06a910).', 'Deleted branch push-b546 (was 37b36b3).']


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
        face=read(FACE), ferry=read(os.path.join(D, 'b547_ferry.txt')),
        scan=read(os.path.join(D, 'b547_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b547_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b547_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b547_pins_stepzero.txt')),
        pins_runs=[read(os.path.join(D, 'b547_pins_stepzero%s.txt' % s)) for s in ('_first', '_rerun', '_rerun1', '_rerun2')],
        lock=read(sorted(glob.glob(os.path.join(D, 'b547_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b546_closing.txt')),
        addendum=read(os.path.join(D, 'b547_addendum.txt')),
        comp=read(os.path.join(D, 'b547_components.txt')),
        desk=read(os.path.join(D, 'b547_desk_notes.txt')),
        sc=jload('b547_scores.json'), reads=read(os.path.join(D, 'b547_reads.txt')), anchor=read(os.path.join(D, 'b547_anchor.txt')),
        fj=jload('b547_faces.json'), cj=jload('b547_census_table.json'), crj=jload('b547_credit.json'), lj=jload('b547_ledger.json'),
        bj=jload('b547_banks.json'), fdj=jload('b547_field.json'), fnd=jload('b547_findings.json'), wj=jload('b547_window.json'),
        search=read(os.path.join(D, 'b547_field_search.txt')),
        branches=read(os.path.join(D, 'b547_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), faces=read(os.path.join(PP, FACESR)), ledger=read(os.path.join(PP, 'FACES_LEDGER.md')),
        corr_now=open(CORRP, 'rb').read(), corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md'),
        kh1=gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'grep', '-n', 'h1_complete_at_Phi', 'v1.5', '--', '*.lean'),
        lvh1=gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'grep', '-n', 'theorem h1_complete_at_Phi', 'v0.10.0', '--', '*.lean'),
        relay_pins={p: gits(ROOT, 'rev-parse', p + '^{commit}') for p in R.RELAY_PINS},
        cited={f: (gits(ROOT, 'ls-files', '--', f) == f and os.path.exists(os.path.join(ROOT, f))) for f in R.CITED},
        mem_times=[os.path.getmtime(os.path.join(R.MEMDIR, f)) for f in os.listdir(R.MEMDIR)] if os.path.isdir(R.MEMDIR) else [],
        kernels={k: gits(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == '' and
                 gits(os.path.join('D:', os.sep, k), 'rev-parse', '--short', 'HEAD').startswith(h) for k, h in HEADS.items()},
        branch_lists={r: gits(r, 'branch', '--list', 'push-b546*') for r in (ROOT, PP)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b547_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b547_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b547_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b547_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b547 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b547_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b547_faces.json', 'b547_census_table.json', 'b547_ledger.json', 'b547_banks.json',
                                                               'b547_field_search.txt', 'b547_window.json', 'b547_field.json'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in ('b547_reads.txt', 'b547_anchor.txt')),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b547_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b547_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b547 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-9]_|^b54[0123456]_|^b334_', f)]
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
    f = rd8(S['pp_prior'][FACESR]).split(NL)
    fi = rd8(S['pp_prior']['FINDINGS.md']).split(NL)
    return (('  :39 %s' % f[38][:900]) in r and ('  :4787 %s' % fi[4786][:900]) in r and 'tie_term_neg at :749' in r
            and '### relay 36345da' in r and 'CouplingsAtPhi.lean:410-427' in r)


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and all(b.count(l) == 1 for l in BRANCH_LINES) and '--merged' in b.split(NL)[0]


def census_ok(S):
    b = S['faces'][S['faces'].index(P(R.FCENSH)):] if P(R.FCENSH) in S['faces'] else ''
    rows = [l for l in b.split(NL) if l.startswith('| R')]
    return (len(rows) == 5 and 'not_register1' in rows[0] and 'ch_iff_rh' in rows[1] and 'register3_of_one_lt_re' in rows[2]
            and 'h2_sign_iff_rh' in rows[3] and 'register5_output_holds' in rows[4] and 'certifiedInput_not_zeroRealizing' in rows[4]
            and 'a different statement' in rows[4] and rows[0].split('|')[4].strip().startswith('MOVED') and rows[4].split('|')[4].strip().startswith('MOVED')
            and rows[3].split('|')[4].strip().startswith('CORROBORATED'))


def rpairs_ok(S):
    lines = S['lj'].get('rpair_lines', [])
    old, new = rd8(S['pp_prior']['FACES_LEDGER.md']).split(NL), S['ledger'].split(NL)
    return (len(lines) == 10 and all(S['ledger'].count(l) == 1 for l in lines)
            and all('register5_output_holds' in l and 'not_register1' in l and 'E-2026-09-25-6' in l for l in lines)
            and all(new[n - 1] == old[n - 1] for _, n in R.RPAIRS))


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R157) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b547' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- three flags at lines 11, 37, 87, and the face says so',
     lambda S: '(R81) FLAGS : 3' in line_with(S['scan'], '(R81) FLAGS') and all(re.search(r'line %d\s+col \d+\s+%s' % (n, w_), S['scan']) for n, w_ in ((11, 'only'), (37, 'only'), (87, 'first')))
     and 'The ferry scan carries THREE (R81) flags' in flat(S['face']),
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 3', '(R81) FLAGS : 2'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE -- the pins tool RUN ALONE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-PINS-RUNS-KEPT', 'the four pins runs, every one banked -- 4, 1, 0, 0 -- and the step-zero bank equal to the last',
     lambda S: [line_with(t, 'REPOS HARD-FAILING').strip()[-1:] for t in S['pins_runs']] == ['4', '1', '0', '0'] and S['pins'] == S['pins_runs'][3],
     lambda S: put(S, 'pins_runs', S['pins_runs'][1:] + [S['pins_runs'][0]])),
    ('G-REG-LOCKED-FIRST', 'the face lock block', lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK') and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b546`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b546' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b547' in S['ferry'] and 'ACT b547' in S['face'] and not glob.glob(os.path.join(D, 'b548_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b547')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; the reads and the #check before the lock, the components after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'no web request was made before the seal' in flat(S['face'])
     and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R157-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R157) END' in S['ferry'] and S['ot'].count('**(R157) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R157) ratified', '(R157) noted'))),
    ('G-READS-CITED', 'the reads bank against FACES and FINDINGS at b546`s commit, PowerLimit, the relay pins and lv',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('tie_term_neg at :749', 'x'))),
    ('G-ANCHOR-FRESH', 'the #check bank -- the pin, a clean tree, exit 0, every name',
     lambda S: 'SIDE-explicit-formula 81ae1758f28e280f4e924e8acd76b4b76ae4ac9d (tree clean; exit 0' in line_with(S['anchor'], 'FRESH #check')
     and all(('  ' + n + ' :') in S['anchor'] for n in R.ANCHOR),
     lambda S: put(S, 'anchor', S['anchor'].replace('tree clean; exit 0', 'tree DIRTY; exit 1'))),
    ('G-FACES-TIERS', 'FACES READ HERE -- the tier block once, eight rows, each tier, the Tier N sentence',
     lambda S: S['faces'].count(P(R.FTIERH)) == 1 and len([l for l in S['faces'][S['faces'].index(P(R.FTIERH)):].split(NL) if l.startswith('| ') and '**T' in l]) == 8
     and 'a tier table promotes nothing in it' in S['faces'],
     lambda S: put(S, 'faces', S['faces'].replace(P(R.FTIERH), 'x'))),
    ('G-H1-PIN-ROW', 'SIDE-kernel v1.5 and lv v0.10.0 READ HERE -- no h1 at the kernel, h1 at CouplingsAtPhi.lean:418; the rectification row once',
     lambda S: S['kh1'] == '' and 'CouplingsAtPhi.lean:418' in S['lvh1'] and S['faces'].count('**Rectification of the pin cell') == 1,
     lambda S: put(S, 'kh1', 'v1.5:Kernel/X.lean:1:theorem h1_complete_at_Phi')),
    ('G-RELAY-PINS', 'relay READ HERE -- the three pins resolve, and each report`s header is banked',
     lambda S: all(len(v) == 40 for v in S['relay_pins'].values()) and sum(1 for r in S['bj']['rows'] if r['file'].startswith('relay pin') and r['header']) == 3,
     lambda S: put(S, 'relay_pins', dict(S['relay_pins'], **{'7386b47': ''}))),
    ('G-CENSUS-TABLE', 'FACES READ HERE -- five rows, the compiled fact beside each, R1 and R5 moved, R4 corroborated, R5`s marker a different statement',
     lambda S: census_ok(S), lambda S: put(S, 'faces', S['faces'].replace('a different statement', 'the same statement'))),
    ('G-TIER-N-KEPT', 'FACES READ HERE -- the class line unchanged and both blocks say Tier N',
     lambda S: rd8(S['pp_prior'][FACESR]).split(NL)[2] == S['faces'].split(NL)[2] and S['faces'].count('stays Tier N') >= 2,
     lambda S: put(S, 'faces', S['faces'].replace('stays Tier N', 'is Tier K'))),
    ('G-CREDIT-ENTRY', 'FINDINGS READ HERE -- the credit once, :39 quoted verbatim, at the line the bank names',
     lambda S: (lambda b: S['find'].count(P(R.CREDITH)) == 1 and ('> ' + rd8(S['pp_prior'][FACESR]).split(NL)[38]) in b
                and S['find'].split(NL)[S['crj']['heading_line'] - 1] == P(R.CREDITH))(fblock(S['find'], P(R.CREDITH))),
     lambda S: put(S, 'find', S['find'].replace('> | **R4 positivity**', '> R4'))),
    ('G-LEDGER-TIERS', 'FACES_LEDGER READ HERE -- thirteen tier rows in the b547 block',
     lambda S: (lambda b: len([l for l in b.split(NL) if l.startswith('| ') and '**T' in l]) == 13)(S['ledger'][S['ledger'].index(R.LEDGER_MARK):] if R.LEDGER_MARK in S['ledger'] else ''),
     lambda S: put(S, 'ledger', S['ledger'].replace('| **T3** |', '| T3 |'))),
    ('G-RPAIR-LINES', 'FACES_LEDGER READ HERE against its blob -- ten lines once each, each naming the three, the ten rows unchanged',
     lambda S: rpairs_ok(S), lambda S: put(S, 'lj', dict(S['lj'], rpair_lines=S['lj'].get('rpair_lines', [])[:9]))),
    ('G-LEDGER-WRITER', 'the ledger bank -- the writer`s own verdict WRITTEN, the marker once, append-only on the working file and the blob',
     lambda S: S['lj'].get('status') == 'WRITTEN' and 'mark 1 time(s); append-only working=True blob=True' in S['lj'].get('detail', '') and S['ledger'].count(R.LEDGER_MARK) == 1,
     lambda S: put(S, 'lj', dict(S['lj'], status='REFUSED'))),
    ('G-CITED-BANKS', 'relay READ HERE -- every bank the rows cite, tracked and present',
     lambda S: len(S['cited']) == 11 and all(S['cited'].values()) and S['bj'].get('missing') == [],
     lambda S: put(S, 'cited', dict(S['cited'], **{'data/read_pentagon.txt': False}))),
    ('G-FIELD-ENTRY', 'FINDINGS READ HERE -- the field entry once, three position sentences, field-context',
     lambda S: (lambda b: S['find'].count(P(R.FIELDH)) == 1 and '**The programme' in b and 'Field-context layer' in b and outside_bt(b) == 0)(fblock(S['find'], P(R.FIELDH))),
     lambda S: put(S, 'find', S['find'].replace('Field-context layer', 'x'))),
    ('G-LIU-QUOTE-OR-NAVREAD', 'the search bank and the entry -- no Liu record found, so NAVIGATOR-READ, nothing fetched, no substitute',
     lambda S: 'NO RECORD with that author and that title' in S['search'] and 'NOTHING WAS FETCHED' in S['search']
     and 'NAVIGATOR-READ' in fblock(S['find'], P(R.FIELDH)) and 'is not substituted' in fblock(S['find'], P(R.FIELDH)),
     lambda S: put(S, 'search', S['search'].replace('NOTHING WAS FETCHED', 'FETCHED'))),
    ('G-ZENODO-NAMED-ONLY', 'the entry -- the two records named as the ruling names them, missing fields said, nothing read',
     lambda S: (lambda b: 'de Bastos, February 2026 (title not given in the ruling)' in b and 'Admissible Closure of the Weil Explicit Formula' in b
                and 'Nothing at Zenodo was read' in b and 'zenodo.org' not in b.lower())(fblock(S['find'], P(R.FIELDH))),
     lambda S: put(S, 'find', S['find'].replace('Nothing at Zenodo was read', 'x'))),
    ('G-DETECTION-PRICE', 'the trail READ HERE -- the four PowerLimit pieces with lines and the finite-j inequality',
     lambda S: all(x in trail(S) for x in ('`tie_term_neg` (:749', '`rest_term_small` (:764', '`dominant_summable` (:949', '`zeroSide_eventually_neg` (:1082', 'finite-j form')),
     lambda S: put(S, 'ot', S['ot'].replace('finite-j form', 'x'))),
    ('G-CERTIFY-PRICE', 'the trail and the checkout bank -- what the checkout holds, printed from its counts',
     lambda S: 'no interval arithmetic and no evaluator for a definite integral' in trail(S) and S['wj']['counts'].get('norm_num extension files (Mathlib/Tactic/NormNum/*)') == 26
     and '26 `norm_num` extension files' in trail(S),
     lambda S: put(S, 'wj', dict(S['wj'], counts={}))),
    ('G-WORKORDERS-FILED', 'OPEN_TRAILS READ HERE -- the two work-orders once each, the author`s word their trigger',
     lambda S: S['ot'].count('| `W-ORD-DETECTION-REGION` |') == 1 and S['ot'].count('| `W-ORD-WINDOW-CERTIFY` |') == 1 and trail(S).count("THE AUTHOR'S WORD") >= 2,
     lambda S: put(S, 'ot', S['ot'].replace('| `W-ORD-WINDOW-CERTIFY` |', '| x |'))),
    ('G-FINDINGS-ACT', 'FINDINGS READ HERE -- the act entry once, its counts, the next keystone',
     lambda S: (lambda b: S['find'].count(P(R.ACTH)) == 1 and '**Next keystone:** THE_RESIDUE_OF_RH.' in b and 'CARRIED 4, NEW 4' in b)(fblock(S['find'], P(R.ACTH))),
     lambda S: put(S, 'find', S['find'].replace('**Next keystone:** THE_RESIDUE_OF_RH.', 'x'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b546'}))),
    ('G-MEMORY-UNREFRESHED', 'the memory directory READ HERE -- no file written after this face (R157)(6)',
     lambda S: bool(S['mem_times']) and max(S['mem_times']) < os.path.getmtime(FACE),
     lambda S: put(S, 'mem_times', S['mem_times'] + [os.path.getmtime(FACE) + 1])),
    ('G-LINES-KEPT', 'the four written files against their blobs at b546`s commit',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY and SPIRAL_MAP bytes against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md', 'SPIRAL_MAP.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b' '}))),
    ('G-KERNELS-UNTOUCHED', 'the four repositories this act read, READ HERE -- clean and at their heads',
     lambda S: len(S['kernels']) == 4 and all(S['kernels'].values()), lambda S: put(S, 'kernels', dict(S['kernels'], **{'SIDE-kernel': False}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b547_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind, branch deletion included',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b547_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b547 bank and tool and this act`s own PLACE-papers bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the census bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the ledger bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the banks bank', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the field bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the trail', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the blobs, the tools, the token and the kernels', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b547 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels READ HERE', lambda S: 'No kernel lane opened at this act' in trail(S) and all(S['kernels'].values()),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the four written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-CORR-UNTOUCHED', 'SIDE-global-section`s correspondence ledger against its blob -- no row this act',
     lambda S: S['corr_now'] == S['corr_prior'] and S['corr_now'] != b'', lambda S: put(S, 'corr_now', S['corr_now'] + b'| 391 | a row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b546`s close -- no instrument modified (the ledger writer imported, not edited)',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['b327_faces_row.py'])),
    ('G-WRITELIST-KINDS', 'every b547 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b547')" in S['suite']
                and "data/b547_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b547_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b547')
              and 'data/b547_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b547 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b547_checks_postpush.txt' if pushed else 'b547_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b547_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
