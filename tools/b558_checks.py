# -*- coding: utf-8 -*-
"""b558_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b558_registration_2026-09-29.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'a922e617'      # ### b557's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = 'f8b4a31'           # ### b557's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b558 —'


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




import hashlib
import b558_record as R
import b542_checks as K542
import banned_terms as BTM
import terminal_table as TT
FIXED = ['FINDINGS.md', 'OPEN_TRAILS.md', 'SPIRAL_MAP.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md', 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md']
_ED = json.loads(read(os.path.join(D, 'b558_editions.json')) or '{}')
PPFILES = sorted(set(FIXED) | {v['pointer']['file'] for v in _ED.get('lists', {}).values()})
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'phase2/method/THE_IDENTITY_CHAIN.md', 'phase2/method/THE_KEYSTONE_CENSUS.md',
         'phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md', 'phase2/method/REPARAMETERIZATION_BARRIERS_v0_1.md',
         'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
GSR = os.path.join('D:', os.sep, 'SIDE-global-section')
KERN = os.path.join('D:', os.sep, 'SIDE-kernel')
SPR = os.path.join('D:', os.sep, 'SIDE-silence-principle')


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'), ('worktree', ' remove'))] + [
        '(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def jload(n):
    return json.loads(read(os.path.join(D, n)) or '{}')


AFTER_LOCK = ('b558_union.json', 'b558_citers.json', 'b558_cp1b.json', 'b558_settle.json', 'b558_editions.json', 'b558_moved_terminals.txt')
BEFORE_LOCK = ('b558_ferry.txt', 'b558_ferry_scan.txt', 'b558_pins_stepzero.txt')
RERUN = '--rerun-postpush' in sys.argv


def utc_epoch(face_or_notes, label):
    """### the `<label> (UTC) : <iso>Z` stamp a lock block or a run file carries, as an epoch; None if absent."""
    import calendar
    m = re.search(re.escape(label) + r' \(UTC\) : (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)Z', face_or_notes or '')
    return calendar.timegm(time.strptime(m.group(1), '%Y-%m-%dT%H:%M:%S')) if m else None


def pushed_digest_ok(name):
    """### (R169)(1)(b), b559: the bank's working bytes (CR stripped) against its blob in the PUSHED tree (origin/main), by sha256."""
    work = open(os.path.join(D, name), 'rb').read().replace(b'\r\n', b'\n') if os.path.exists(os.path.join(D, name)) else None
    pub = blob(ROOT, 'origin/main:data/' + name)
    return bool(work) and bool(pub) and hashlib.sha256(work).hexdigest() == hashlib.sha256(pub).hexdigest()


def added_epoch(name):
    """### the commit time of the pushed commit that first added the bank (git's own record, not the file system's)."""
    t = gits(ROOT, 'log', '--diff-filter=A', '--format=%ct', 'origin/main', '--', 'data/' + name).split()
    return int(t[-1]) if t else None


def peek_by_digest(face, lockn, scan):
    """### ### **(R169)(1)(b): THE POST-PUSH READING OF `G-PEEK-DECLARED` COMPARES CONTENT DIGESTS AGAINST THE PUSHED TREE.**
    ### b558's defect (i): the checkout between the act's commit and its fast-forward rewrote every newly tracked bank, so
    ### file times after a push say nothing about the lock. After the push the arm reads: (after) each bank's bytes equal its
    ### pushed blob and the pushed commit adding it is later than the face's lock stamp; (before) each bank's bytes equal its
    ### pushed blob, the lock gate's run stamp precedes the lock stamp and names the scan and the pins as PASS, and the scan
    ### names the ferry file. The pre-push reading (file times, taken before any checkout) is unchanged."""
    lk, rn = utc_epoch(face, 'locked at'), utc_epoch(lockn, 'run at')
    after = lk is not None and all(pushed_digest_ok(x) and (added_epoch(x) or 0) > lk for x in AFTER_LOCK)
    before = (lk is not None and rn is not None and rn < lk and all(pushed_digest_ok(x) for x in BEFORE_LOCK)
              and 'ferry file                    : b558_ferry.txt' in scan
              and all(re.search(re.escape(x) + r'\s+PASS', lockn) for x in ('b558_ferry_scan.txt', 'b558_pins_stepzero.txt')))
    return after, before


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b558_ferry.txt')),
        scan=read(os.path.join(D, 'b558_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b558_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b558_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b558_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b558_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b557_closing.txt')),
        addendum=read(os.path.join(D, 'b558_addendum.txt')),
        comp=read(os.path.join(D, 'b558_components.txt')),
        desk=read(os.path.join(D, 'b558_desk_notes.txt')),
        sc=jload('b558_scores.json'), reads=read(os.path.join(D, 'b558_reads.txt')),
        tagbank=read(os.path.join(D, 'b558_tag_lsremote.txt')), tag_local=gits(SPR, 'rev-parse', 'v0.2.0^{}'),
        st=jload('b558_settle.json'), un=jload('b558_union.json'), mt=read(os.path.join(D, 'b558_moved_terminals.txt')),
        cit=jload('b558_citers.json'), cp=jload('b558_cp1b.json'), cptxt=read(os.path.join(D, 'b558_cp1b.txt')),
        mrow=jload('b558_maprow.json'), msec=jload('b558_mapsection.json'), cred=jload('b558_credits.json'), ed=jload('b558_editions.json'),
        fj=jload('b558_findings.json'), ttable=read(os.path.join(D, 'terminal_table.md')),
        branches=read(os.path.join(D, 'b558_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        mains=R.mains(),
        trial=dict(head=gits(R.P.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.P.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b557*') for r in (ROOT, PP)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0)
                 if f.startswith('b558_') and os.path.isfile(os.path.join(d0, f))) if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b558_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b558_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b558_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b558 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b558_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b558_union.json', 'b558_citers.json', 'b558_cp1b.json', 'b558_settle.json',
                                                               'b558_editions.json', 'b558_moved_terminals.txt'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in ('b558_ferry.txt', 'b558_ferry_scan.txt', 'b558_pins_stepzero.txt')),
    )
    S['pushed'] = RERUN or (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
                            and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b558')
                            and 'data/b558_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    if S['pushed']:
        S['after_lock'], S['before_lock'] = peek_by_digest(S['face'], S['lock'], S['scan'])
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b558_') and os.path.isfile(os.path.join(D, f))] + \
        glob.glob(os.path.join(D, 'b558_editions', '*.txt')) + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b558_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KERN):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith(('b558 --', 'housekeeping: terminal table regenerated at b558')):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-4][0-9]_|^b55[0-7]_|^b334_', f)]
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
            base = g.split('/')[-1]
            if not re.search(r'[A-Za-z0-9]', base):
                # ### b558 defect (g): a directory glob whose last part is a bare wildcard (`relay/data/b558_editions/*`) is read
                # ### as the files that directory holds, not as a match-all.
                root = ROOT if g.startswith('relay/') else (PP if g.startswith('PLACE-papers/') else None)
                if root:
                    rel = g.split('/', 1)[1]
                    out.extend(os.path.basename(x) for x in glob.glob(os.path.join(root, *rel.split('/'))))
                continue
            out.append(base)
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
SP = os.path.join('D:', os.sep, 'SIDE-silence-principle')


def reads_ok(S):
    r = S['reads']
    need = ['FINDINGS.md:4787', 'FINDINGS.md:5812', 'FINDINGS.md:5868', 'FINDINGS.md:5461', 'FINDINGS.md:5527', 'FINDINGS.md:5563',
            'THE_LOAD_BEARING_MAP.md entire', 'SIDE-silence-principle: HEAD 667c254', 'SPIRAL_MAP.md:268', 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md:628',
            'the seat`s memory file', 'the mirror-export tool', 'MANIFEST.md md5']
    return all(x in r for x in need) and all(('the tier block of %-40s' % t) in r for k, t, p in R.ROSTER)


def tag_ok(S):
    t = S['tagbank']
    loc = S['tag_local']
    return ('667c2548777585876a2f3208029595b06a062619\trefs/tags/v0.2.0^{}' in t and loc == '667c2548777585876a2f3208029595b06a062619'
            and S['st'].get('tag', {}).get('equal') is True)


def settle_ok(S):
    ok = True
    for o, h, f in zip(S['st'].get('appends', []), (R.L628, R.LSP, R.LC, R.LD), ('phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'SPIRAL_MAP.md', 'OPEN_TRAILS.md', 'OPEN_TRAILS.md')):
        txt = rd8(S['pp_now'][f]).split(NL)
        ln = [i + 1 for i, l in enumerate(txt) if l.startswith(P(h))]
        ok = ok and ln == [o['line']] and kept(S, f)
    return ok and len(S['st'].get('appends', [])) == 4 and S['st'].get('table_lines') == 0


def union_banked_ok(S):
    u, mt = S['un'], S['mt']
    return (len(u.get('union', [])) == 19 and all(('    %s' % x) in mt for x in u['union']) and 'THE NAVIGATOR`S OVER-COUNT' in mt and 'THE ADDITIONS' in mt
            and len(u.get('rows', [])) == len(u['union']))


def union_mech_ok(S):
    u = S['un']
    bl = R.blocks_at(R.PRIOR_PP)
    s1 = set()
    voc = R.vocabulary(bl)
    for k, (src, a, rows) in bl.items():
        for n, l in rows:
            if l.startswith('|') and re.search(r'\*\*MOVED\b|MOVED \(|-- \*\*MOVED\*\*', l):
                s1 |= {R.short(x) for c in R.cells(l)[1:4] for x in R.BT.findall(c) if not R.NOTNAME.search(x) and x in voc}
    named = {x for e in R.RULED for x in e}
    return (s1 == set(u.get('s1', {})) and sorted(set(u['s1']) | set(u['s2']) | set(u['s2b']) | set(u['s3']), key=str.lower) == u['union']
            and sorted(u['add']) == sorted(x for x in u['union'] if x not in named)
            and all(not any(x in u['union'] for x in e) for e in u['over']))


def citers_ok(S):
    c = S['cit']
    rows = c.get('rows', [])
    ok = len(rows) == len(S['cp'].get('rows', [])) and bool(rows)
    texts = {}
    for r in rows[:: max(1, len(rows) // 60)]:
        if r['path'] not in texts:
            texts[r['path']] = rd8(blob(PP, R.PRIOR_PP + ':' + r['path'])).split(NL)
        ok = ok and r['sentence'] in texts[r['path']][r['line'] - 1]
    return ok


def maprows_ok(S):
    mp = rd8(S['pp_now']['phase1.5/method/THE_LOAD_BEARING_MAP.md'])
    ln = [i + 1 for i, l in enumerate(mp.split(NL)) if l.startswith(P(R.MAPROWH))]
    blk = seg(mp, P(R.MAPROWH), 20000).split('*Appended by b558.')[0]
    want = [x for x in S['un'].get('union', []) if x not in S['cit'].get('maprows', {})]
    return ln == [S['mrow'].get('line')] and all(('| `%s` |' % x) in blk for x in want) and 'h2_sign' in want and 'h2_sign' not in S['cit'].get('maprows', {})


def one_verdict_ok(S):
    rows = S['cp'].get('rows', [])
    own = [r for r in rows if r['own'] == 'DOCUMENT']
    V = R.load_verdicts()
    return (bool(rows) and all(r['verdict'] in R.VERDICTS for r in rows) and len(set(r['id'] for r in rows)) == len(rows)
            and set(r['id'] for r in own) == set(V) and all(V[r['id']][0] == r['verdict'] for r in own))


def cascade_ok(S):
    cas = [r for r in S['cp'].get('rows', []) if r['own'] == 'CASCADE']
    return bool(cas) and all(r['verdict'] == 'STANDS' and r['source'] == 'DEFAULT' for r in cas)


def table_ok(S):
    t = S['cptxt'].split(NL)
    body = t[t.index('### THE TABLE -- terminal | document | line | verdict | the sentence, quoted | the reading') + 2:] if '### THE TABLE -- terminal | document | line | verdict | the sentence, quoted | the reading' in t else []
    return len([l for l in body if l.strip()]) == len(S['cp'].get('rows', [])) > 0


def mapsec_ok(S):
    mp = rd8(S['pp_now']['phase1.5/method/THE_LOAD_BEARING_MAP.md'])
    ln = [i + 1 for i, l in enumerate(mp.split(NL)) if l.startswith(P(R.MAPSECH))]
    blk = seg(mp, P(R.MAPSECH), 200000)
    need = [r for r in S['cp'].get('rows', []) if r['verdict'] != 'STANDS']
    return (ln == [S['msec'].get('line')] and kept(S, 'phase1.5/method/THE_LOAD_BEARING_MAP.md') and bool(need)
            and all(('- `%s` -- %s:%d -- ' % (r['terminal'], R.TITLES[r['doc']], r['line'])) in blk for r in need))


def credits_ok(S):
    cr = [r for r in S['cp'].get('rows', []) if r['verdict'] == 'CREDIT' and r['id'] not in R.ENTERED]
    ent = {o['id']: o['line'] for o in S['cred'].get('entered', [])}
    F = S['find'].split(NL)
    ok = bool(cr) and set(ent) == set(r['id'] for r in cr)
    for r in cr:
        h = P('## %s :%d, %s, read against %s: an earlier reading of `%s` held against a later drift' % (R.TITLES[r['doc']], r['line'], r['date'], R.MOVER[r['terminal']][0], r['terminal']))
        ok = ok and [i + 1 for i, l in enumerate(F) if l == h] == [ent.get(r['id'])]
    return ok and 'the form of `FINDINGS.md`:5563' in fblock(S['find'], P(R.FH))


def worklists_ok(S):
    mim = {}
    for r in S['cp'].get('rows', []):
        if r['verdict'] == 'MOVED-IN-MEANING':
            mim[r['doc']] = mim.get(r['doc'], 0) + 1
    files = {os.path.basename(f)[:-4] for f in glob.glob(os.path.join(D, 'b558_editions', '*.txt'))}
    ok = files == {R.TITLES[k] for k in mim} and set(S['ed'].get('lists', {})) == set(mim)
    for k, n in mim.items():
        t = read(os.path.join(D, 'b558_editions', R.TITLES[k] + '.txt'))
        ok = ok and t.count(NL + ':') + (1 if t.startswith(':') else 0) == n and ('### %d sentence-rows' % n) in t
    return ok


def pointers_ok(S):
    ok = bool(S['ed'].get('lists'))
    for k, v in S['ed'].get('lists', {}).items():
        f = v['pointer']['file']
        txt = rd8(S['pp_now'][f]).split(NL)
        ln = [i + 1 for i, l in enumerate(txt) if l.startswith(P(R.POINTER))]
        ok = ok and v['pointer']['line'] in ln and kept(S, f) and ('data/b558_editions/%s.txt' % R.TITLES[k]) in txt[v['pointer']['line'] - 1]
    return ok


def findings_ok(S):
    b = fblock(S['find'], P(R.FH))
    return S['find'].count(P(R.FH)) == 1 and '**Next:** W-ORD-DETECTION-REGION' in b and '**The edition work-lists.**' in b and '**The credits.**' in b


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b557 (was ') == 2 and b.count('Deleted branch push-b557-closing (was ') == 1


def kernel_sources_ok(S):
    m = S['mains']
    return len(m) == len(R.PRE_HEADS) and not any(f.endswith('.lean') for v in m.values() for f in v) and all(v == [] for v in m.values())


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R168) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b558' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- no (R81) flag, and the face says so',
     lambda S: '(R81) FLAGS : 0' in line_with(S['scan'], '(R81) FLAGS') and 'The ferry scan' in flat(S['face']) and 'carries no hit and no flag' in flat(S['face']),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b557`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b557' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b558' in S['ferry'] and 'ACT b558' in S['face'] and not glob.glob(os.path.join(D, 'b559_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b558')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; the reads and the dry extraction before the lock, every bank and write after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'THE EXTRACTION RAN BEFORE THIS SEAL' in flat(S['face']) and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R168-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R168) END' in S['ferry'] and S['ot'].count('**(R168) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R168) ratified', '(R168) noted'))),
    ('G-READS-CITED', 'the reads bank -- the tier blocks by heading line, the FINDINGS lines, the map, the tag state, SPIRAL_MAP :268, FOUNDATIONS :628, the memory file, the mirror',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('MANIFEST.md md5', 'x'))),
    ('G-TAG-PEELED', 'the ls-remote read-back bank, taken after the tag`s push, and the local tag READ HERE -- peeled 667c254 both',
     lambda S: tag_ok(S), lambda S: put(S, 'tag_local', '90e540fd5644c38e7e9a534bf82f0a8464c2f98c')),
    ('G-SETTLE-LINES', 'FOUNDATIONS, SPIRAL_MAP and OPEN_TRAILS READ HERE -- the four lines once each at their banked lines, the files kept; the table naming neither terminal',
     lambda S: settle_ok(S), lambda S: put(S, 'st', dict(S['st'], table_lines=2))),
    ('G-UNION-BANKED', 'the union bank and its text -- nineteen terminals each printed, the over-count and the additions printed',
     lambda S: union_banked_ok(S), lambda S: put(S, 'mt', S['mt'].replace('THE ADDITIONS', 'x'))),
    ('G-UNION-MECHANICAL', 'the tier blocks at b557`s commit READ HERE -- S1 recomputed; the union the sources` union; additions and over-count recomputed from the ruling`s entries',
     lambda S: union_mech_ok(S), lambda S: put(S, 'un', dict(S['un'], add=S['un']['add'] + ['h2_sign']))),
    ('G-CITERS-BANKED', 'the citers bank against the table; a spaced sample of rows found at their lines in the documents at b557`s commit',
     lambda S: citers_ok(S), lambda S: put(S, 'cit', dict(S['cit'], rows=S['cit']['rows'][:-1]))),
    ('G-MAP-ROWS-APPENDED', 'THE_LOAD_BEARING_MAP READ HERE -- the rows heading once at its banked line, a row for every union terminal (A) lacked, h2_sign among them',
     lambda S: maprows_ok(S), lambda S: put(S, 'mrow', dict(S['mrow'], line=-1))),
    ('G-EVERY-ROW-ONE-VERDICT', 'the table bank and the seat`s verdict files READ HERE -- one verdict per row, of the three, every document row read',
     lambda S: one_verdict_ok(S), lambda S: put(S, 'cp', dict(S['cp'], rows=[dict(r, verdict='RESTS') if i == 0 else r for i, r in enumerate(S['cp']['rows'])]))),
    ('G-CASCADE-DEFAULT', 'the table bank -- every cascade row STANDS by the declared default',
     lambda S: cascade_ok(S), lambda S: put(S, 'cp', dict(S['cp'], rows=[dict(r, verdict='CREDIT') if r['own'] == 'CASCADE' else r for r in S['cp']['rows']]))),
    ('G-TABLE-BANKED', 'data/b558_cp1b.txt -- one table line per row', lambda S: table_ok(S),
     lambda S: put(S, 'cptxt', S['cptxt'].rsplit(NL, 3)[0])),
    ('G-MAP-SECTION', 'THE_LOAD_BEARING_MAP READ HERE -- the section once at its banked line, every MOVED-IN-MEANING and CREDIT row in it, the file kept',
     lambda S: mapsec_ok(S), lambda S: put(S, 'msec', dict(S['msec'], line=-1))),
    ('G-CREDITS-ENTERED', 'FINDINGS READ HERE -- a section per new CREDIT row at its banked line, headed in the form of :5563',
     lambda S: credits_ok(S), lambda S: put(S, 'cred', dict(S['cred'], entered=S['cred']['entered'][:-1]))),
    ('G-WORKLISTS', 'data/b558_editions/ READ HERE -- one list per document with a MOVED-IN-MEANING row and no other; the counts equal to the table`s',
     lambda S: worklists_ok(S), lambda S: put(S, 'ed', dict(S['ed'], lists={k: v for k, v in list(S['ed']['lists'].items())[1:]}))),
    ('G-WORKLIST-POINTERS', 'each work-list document READ HERE -- its pointer line at its banked line, naming its list; the file kept',
     lambda S: pointers_ok(S), lambda S: put(S, 'ed', dict(S['ed'], lists={k: dict(v, pointer=dict(v['pointer'], line=-5)) for k, v in S['ed']['lists'].items()}))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once, the credits and the work-lists named, W-ORD-DETECTION-REGION next', lambda S: findings_ok(S),
     lambda S: put(S, 'find', S['find'].replace(P(R.FH), 'x'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in two repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b557'}))),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-LINES-KEPT', 'the written files against their blobs at b557`s commit',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY, FACES_LEDGER, THE_IDENTITY_CHAIN, THE_KEYSTONE_CENSUS, SILENCE_STAGES_DEALIGNMENT, REPARAMETERIZATION_BARRIERS against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in OTHER if 'A_Place_to_Stand' not in f and f != 'ERRATA.md'),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'REGISTRY.md': S['pp_now']['REGISTRY.md'] + b' '}))),
    ('G-KERNEL-SOURCES-UNTOUCHED', 'the kernels` mains READ HERE against their pre-act heads -- nothing written',
     lambda S: kernel_sources_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-effects': ['SIDEEffects/Structural.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b558_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b558_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b558 bank and tool and this act`s PLACE-papers bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the table', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the citers and the map rows', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the CREDIT rows', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the union and the work-lists', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the union', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the tag read-back', lambda S: nscored(S, 'n6'), lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-N7-SCORED', 'the desk against the mains, the tools, the token, the deposit, the trial worktree and the tagged repository`s HEAD', lambda S: nscored(S, 'n7'),
     lambda S: put(S, 'sc', dict(S['sc'], n7=not S['sc'].get('n7')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b558 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels` mains READ HERE',
     lambda S: 'No kernel lane opened at this act' in trail(S) and kernel_sources_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b557`s close -- no .py tool modified',
     lambda S: [x for x in S['tools_edited'] if x.endswith('.py')] == [],
     lambda S: put(S, 'tools_edited', ['terminal_table.py'])),
    ('G-WRITELIST-KINDS', 'every b558 commit in four repositories and the housekeeping commit, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b558')" in S['suite']
                and "data/b558_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b558_components.txt' in gits(ROOT, 'show'")),
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
    # ### (R169)(1)(b): a re-run on the pushed act does not regenerate the table (the generator writes relay's table files).
    rc_gen, gen_diff = (0, dict(rerun=True)) if RERUN else regenerate()
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b558')
              and 'data/b558_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    pushed = pushed or RERUN
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b558 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    if RERUN:
        rec('  ### ### **(R169)(1)(b): A RE-RUN ON THE PUSHED ACT -- THE GENERATOR WAS NOT RE-RUN** (it writes relay`s table files).')
        rec('  ###   G-PEEK-DECLARED read by content digests against the pushed tree (origin/main %s).' % gits(ROOT, 'rev-parse', '--short', 'origin/main'))
    else:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
    if RERUN:
        pass
    elif gen_diff.get('first_run'):
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
    if RERUN:
        # ### (R169)(1)(b): the re-run writes one named record and nothing of b558's own.
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1])
        io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
        print('  written: %s' % os.path.basename(out))
        return 0 if ok else 1
    out = os.path.join(D, 'b558_checks_postpush.txt' if pushed else 'b558_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b558_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
