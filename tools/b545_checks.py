# -*- coding: utf-8 -*-
"""b545_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b545_registration_2026-09-26.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'e04b475d'      # ### b544's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = 'a0f73df'           # ### b544's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b545 —'


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


import b545_record as R
import b542_checks as K542
BALR = 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'
SURRR = 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md'
PPFILES = [BALR, 'FINDINGS.md', 'OPEN_TRAILS.md', SURRR]
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md',
         'phase1.5/method/THE_LOAD_BEARING_MAP.md']
SIDE_TIP = '2e43315'
CORRP = os.path.join(SIDE, 'CORRESPONDENCE.md')
HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': '2e43315',
         'SIDE-li-map': 'b515e6b', 'SIDE-fano-darkness': '0f6ce5b'}
BRANCH_LINES = ['Deleted branch push-b544 (was deb2a187).', 'Deleted branch push-b544-closing (was e04b475d).', 'Deleted branch push-b544 (was a0f73df).']


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
        face=read(FACE), ferry=read(os.path.join(D, 'b545_ferry.txt')),
        scan=read(os.path.join(D, 'b545_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b545_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b545_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b545_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b545_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b544_closing.txt')),
        addendum=read(os.path.join(D, 'b545_addendum.txt')),
        comp=read(os.path.join(D, 'b545_components.txt')),
        desk=read(os.path.join(D, 'b545_desk_notes.txt')),
        sc=jload('b545_scores.json'),
        reads=read(os.path.join(D, 'b545_reads.txt')),
        anchor=read(os.path.join(D, 'b545_anchor.txt')),
        probes=jload('b545_probes.json'), probes_txt=read(os.path.join(D, 'b545_probes.txt')),
        tj=jload('b545_tiers.json'), sj=jload('b545_sentences.json'), fh=jload('b545_fano_hits.json'),
        fsearch=read(os.path.join(D, 'b545_fano_search.txt')), lsr=read(os.path.join(D, 'b545_fano_lsremote.txt')),
        cj=jload('b545_credit.json'), fj=jload('b545_findings.json'),
        wt=jload('b545_write_tiers.json'), ws=jload('b545_write_sentences.json'), wj=jload('b545_write_joint.json'),
        b539s=jload('b539_sentences.json'),
        branches=read(os.path.join(D, 'b545_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        bal=read(os.path.join(PP, BALR)), find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), surr=read(os.path.join(PP, SURRR)),
        corr_now=open(CORRP, 'rb').read(), corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md'),
        fano_src=gits(os.path.join('D:', os.sep, 'SIDE-fano-darkness'), 'show', '0f6ce5b:FanoTwoDarkness.lean'),
        fed=R.fed_repos(),
        rereads=[(t['terminal'], R.reread((t['repo'], t['row_pin'], t['now_pin'], t['terminal'], t['kind'], '', '', '', None, None))['same'],
                  R.ei_of(t['terminal']) if t['repo'] else '--')
                 for r in jload('b545_tiers.json').get('rows', []) for t in r['terminals']],
        kernels={k: gits(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == '' and
                 gits(os.path.join('D:', os.sep, k), 'rev-parse', '--short', 'HEAD').startswith(h) for k, h in HEADS.items()},
        branch_lists={r: gits(r, 'branch', '--list', 'push-b544*') for r in (ROOT, PP)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b545_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b545_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b545_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b545_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b545 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b545_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        erratum_drafts=glob.glob(os.path.join(D, 'b545_erratum*')),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b545_anchor.txt', 'b545_fano_hits.json', 'b545_probes.json', 'b545_tiers.json',
                                                               'b545_sentences.json', 'b545_credit.json', 'b545_findings.json'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in ('b545_reads.txt',)),
    )
    S['bal_prior'] = rd8(S['pp_prior'][BALR])
    S['rows_prior'] = R.split_rows(S['bal_prior'].split(NL))
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b545_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b545_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b545 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-9]_|^b54[01234]_|^b334_', f)]
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


def block(text, h, stop='<!-- b545'):
    if h not in text:
        return ''
    b = text[text.index(h):]
    j = b.find(stop, len(h))
    return b[:j] if j > 0 else b


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


def poss(t):
    return re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", t)


def reads_ok(S):
    r = S['reads']
    b = S['bal_prior'].split(NL)
    m = rd8(S['pp_prior']['phase1.5/method/THE_LOAD_BEARING_MAP.md']).split(NL)
    f = rd8(S['pp_prior']['FINDINGS.md']).split(NL)
    o = rd8(S['pp_prior']['OPEN_TRAILS.md']).split(NL)
    s = rd8(S['pp_prior'][SURRR]).split(NL)
    t3 = gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'show', 'v0.10.0:SIDELvConservation/T3_StepNineBridge.lean').split(NL)
    return (('  :21 %s' % b[20][:600]) in r and ('  :16 %s' % m[15][:600]) in r and ('  :4955 %s' % f[4954][:600]) in r
            and ('  :3548 %s' % o[3547][:600]) in r and ('  :211 %s' % s[210][:600]) in r and ('  :44 %s' % t3[43]) in r
            and 'md5 %s' % hashlib.md5(S['pp_prior'][BALR]).hexdigest() in r and LVQ in r)


LVQ = "The one deliberately open obligation is the clause itself"


def table_located(S):
    b = S['bal_prior'].split(NL)
    m = rd8(S['pp_prior']['phase1.5/method/THE_LOAD_BEARING_MAP.md']).split(NL)
    return (b[338].startswith('## B.5 Bench pins') and b[340].startswith('| Object | Pin | Verified |')
            and not [l for l in b if l.startswith('#') and 'orrespondence' in l]
            and m[15].startswith('## The keystone set (14 graded Correspondence tables)') and 'BALPOS (`BALANCE_AND_POSITIVITY`)' in m[17]
            and S['tj'].get('table') == 'BALANCE_AND_POSITIVITY.md:339-348')


def tier_rows_ok(S):
    rows = S['tj'].get('rows', [])
    blk = block(S['bal'], R.TIERH)
    terms = [t for r in rows for t in r['terminals']]
    body = [l for l in blk.split(NL) if l.startswith('| ') and not l.startswith('| B.5 row') and not l.startswith('| claim') and not l.startswith('| §V')]
    return ([r['line'] for r in rows] == [343, 344, 345, 346, 347, 348] and len(body) == len(terms) == 17
            and all(('**%s**' % t['tier']) in body[i] for i, t in enumerate(terms))
            and all(r['tier'] == max((t['tier'] for t in r['terminals']), key=R.RANK.index) for r in rows))


def rereads_ok(S):
    terms = [t for r in S['tj'].get('rows', []) for t in r['terminals']]
    return bool(terms) and [(t['terminal'], t['same'], t['ei']) for t in terms] == [tuple(x) for x in S['rereads']]


def fano_hand(S):
    src = S['fano_src']
    if 'theorem second_moment' not in src:
        return False
    tri = lambda s: [tuple(int(x) for x in mm) for mm in re.findall(r'\(x(\d)\+x(\d)\+x(\d)\)', s)]
    th = src[src.index('theorem second_moment'):].split(':=')[0]
    lhs, rhs = th.split(')' + NL + '    =')
    lines = {(1, 2, 3), (0, 2, 4), (2, 5, 6), (0, 1, 5), (1, 4, 6), (0, 3, 6), (3, 4, 5)}
    allt = {(a, b, c) for a in range(7) for b in range(a + 1, 7) for c in range(b + 1, 7)}
    return set(tri(lhs)) == lines and set(tri(rhs)) == allt - lines and len(tri(rhs)) == 28


def rects_ok(S):
    blk = block(S['bal'], R.SENTH)
    rests = [r for r in S['sj'].get('graded', []) if r['verdict'] == 'RESTS']
    return (len(rests) == S['sj'].get('rectifications') == blk.count(NL + '  - rectification: ') == 15
            and all(poss(r['rectification']) in blk for r in rests) and outside_bt(blk) == 0)


def deposit_ok(S):
    """### a RESTS sentence REPEATS a deposited one when two of its three cuts (start, middle, end) stand in the deposit; a sentence
    ### sharing only a phrase with the deposit (one cut) must name E-2026-09-25-6, the erratum listing the deposited sentences that
    ### carry the registers` phrases (:125, :1779) -- b545 finding (j)"""
    dep = re.sub(r'[*`]', '', rd8(S['pp_prior']['outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']))
    rests = [r for r in S['sj'].get('graded', []) if r['verdict'] == 'RESTS']
    repeats, phrase_ok = [], True
    for r in rests:
        t = re.sub(r'[*`]', '', r['sentence'])
        n = len(t) // 2
        cuts = [t[5:45], t[n - 20:n + 20], t[-45:-5]]
        k = sum(1 for c in cuts if c in dep)
        if k >= 2:
            repeats.append(r['line'])
        elif k == 1 and 'E-2026-09-25-6' not in r['grounds']:
            phrase_ok = False
    return bool(rests) and 'one premise in five registers' in dep and not repeats and phrase_ok


def joint_ok(S):
    b = block(S['bal'], R.JOINTH)
    return (S['bal'].count(R.JOINTH) == 1 and '`h2_sign_iff_rh : h2_sign ↔ RiemannHypothesis`' in b and 'It is T1-lit' in b
            and 'W-ORD-MARGIN-BRIDGE' in b and 'h2_sign_iff_rh : SIDEExplicitFormula.B321.h2_sign ↔ RiemannHypothesis' in S['anchor'])


def credit_ok(S):
    b = fblock(S['find'], R.CREDITH)
    bp = S['bal_prior'].split(NL)
    rel = seg(b, '**The relation.** ', 4000).split(NL)[0]
    return (S['find'].count(R.CREDITH) == 1 and S['find'].split(NL)[S['cj']['findings']['heading_line'] - 1] == R.CREDITH
            and bp[356][3:] in b and bp[273][bp[273].index('**Note'):] in b and R.LV_DESC in b and len(re.findall(r'[.)]\s+(?=[A-Z])', rel)) == 1)


def surr_ok(S):
    old, new = rd8(S['pp_prior'][SURRR]), rd8(S['pp_now'][SURRR])
    add = new[len(old):].strip(NL).split(NL)
    return (new.startswith(old) and len(add) == 1 and ('`FINDINGS.md`:%d' % S['cj']['findings']['heading_line']) in add[0]
            and 'b539 tier table at :211' in add[0])


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and all(b.count(l) == 1 for l in BRANCH_LINES) and '--merged' in b.split(NL)[0]


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R155) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b545' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAG-DECLARED', 'this act`s banked scan -- one flag, "never" at line 69, and the face says so',
     lambda S: '(R81) FLAGS : 1' in line_with(S['scan'], '(R81) FLAGS') and re.search(r'line 69\s+col \d+\s+never', S['scan']) is not None
     and 'The ferry scan carries ONE (R81) flag' in flat(S['face']),
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 1', '(R81) FLAGS : 2'))),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b544`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b544' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b545' in S['ferry'] and 'ACT b545' in S['face'] and not glob.glob(os.path.join(D, 'b546_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b545')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; the reads banked before the lock, the components after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'no `#print axioms` ran for this act before it' in flat(S['face'])
     and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R155-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R155) END' in S['ferry'] and S['ot'].count('**(R155) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R155) ratified', '(R155) noted'))),
    ('G-READS-CITED', 'the reads bank against BALPOS`s committed blob, the map, FINDINGS, OPEN_TRAILS, SURR and lv v0.10.0 READ HERE',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace(LVQ, 'x'))),
    ('G-PURPOSE-PRINTED', 'the components bank -- BALPOS`s Role paragraph (:21) printed first',
     lambda S: ('  :21 ' + S['bal_prior'].split(NL)[20][:200]) in S['comp'] and 0 <= S['comp'].find('PURPOSE STATEMENT') < S['comp'].find('COMPONENT 1'),
     lambda S: put(S, 'comp', S['comp'].replace('PURPOSE STATEMENT', 'x'))),
    ('G-ANCHOR-FRESH', 'the anchor bank -- the pin, a clean tree, exit 0, every name',
     lambda S: 'SIDE-explicit-formula 81ae1758f28e280f4e924e8acd76b4b76ae4ac9d (tree clean; exit 0)' in line_with(S['anchor'], 'FRESH #check')
     and all(('  ' + n + ' :') in S['anchor'] for n in R.ANCHOR),
     lambda S: put(S, 'anchor', S['anchor'].replace('tree clean; exit 0', 'tree DIRTY; exit 1'))),
    ('G-LIMAP-PROBE', 'the probe bank -- lam_add and lam_one at 73cee42, their lines in the probe`s own output',
     lambda S: S['probes'].get('SIDE-li-map', {}).get('exit') == 0 and all(
         ("'%s' %s" % (n, S['probes']['SIDE-li-map']['profiles'].get(n))) in S['probes_txt'] for n in ('LiLinearMap.lam_add', 'LiLinearMap.lam_one')),
     lambda S: put(S, 'probes_txt', '')),
    ('G-TABLE-LOCATED', 'BALPOS`s committed blob and the map`s -- no Correspondence heading, B.5 at :339-348, BALPOS among the fourteen',
     lambda S: table_located(S), lambda S: put(S, 'tj', dict(S['tj'], table='x'))),
    ('G-TIER-ROWS', 'the tier block READ HERE against the bank -- six rows, seventeen lines, each tier, each row the lowest',
     lambda S: tier_rows_ok(S), lambda S: put(S, 'bal', S['bal'].replace('| **T0** |', '| **T9** |'))),
    ('G-TERMS-REREAD', 'every terminal re-read HERE at both pins, against the bank`s SAME / DIFFERENT and E/I',
     lambda S: rereads_ok(S), lambda S: put(S, 'rereads', S['rereads'][:-1] + [('x', 'DIFFERENT', 'x')])),
    ('G-EI-MARKS', 'the bank`s E/I marks against CP-3`s index, every terminal of a repository carrying a cell',
     lambda S: all(t['ei'] and t['ei'] != '--' for r in S['tj'].get('rows', []) for t in r['terminals'] if t['repo']) and bool(S['rereads']),
     lambda S: put(S, 'tj', dict(S['tj'], rows=[dict(r, terminals=[dict(t, ei='') for t in r['terminals']]) for r in S['tj'].get('rows', [])]))),
    ('G-SENTENCES-SELECTED', 'the selector RUN HERE on BALPOS`s committed blob against the bank',
     lambda S: len(S['rows_prior']) == S['sj'].get('read') == 602 and len([r for r in S['rows_prior'] if r['hits']]) == S['sj'].get('selected') == 77,
     lambda S: put(S, 'rows_prior', S['rows_prior'][1:])),
    ('G-ROWS-GRADED', 'the sentence bank -- every row a grade and a tier of the law; every RESTS row rectified; the counts sum',
     lambda S: bool(S['sj'].get('graded')) and all(r['verdict'] in ('STANDS', 'STANDS-AS-HISTORY', 'RESTS', 'EXCEEDS') and r['tier'] in R.RANK
                                                    and (r['verdict'] != 'RESTS' or r['rectification']) for r in S['sj']['graded'])
     and sum(S['sj']['counts'].values()) == S['sj']['rows'] == len(S['sj']['graded']) == 78,
     lambda S: put(S, 'sj', dict(S['sj'], graded=[dict(r, tier='T9') for r in S['sj'].get('graded', [])]))),
    ('G-SUPPLEMENTARY', 'the six named lines against BALPOS`s committed blob',
     lambda S: [s['line'] for s in S['sj'].get('supplementary', [])] == [41, 42, 251, 516, 591, 117]
     and all(s['sentence'] == S['bal_prior'].split(NL)[s['line'] - 1].strip() for s in S['sj']['supplementary']),
     lambda S: put(S, 'bal_prior', S['bal_prior'].replace('| Σ_ρ h(γ_ρ) |', '| x |'))),
    ('G-RECTIFICATION-ROWS', 'the sentence block READ HERE -- every rectification written, fifteen, no backtick left open',
     lambda S: rects_ok(S), lambda S: put(S, 'bal', S['bal'].replace('  - rectification: ', '  - x: ', 1))),
    ('G-DEPOSIT-REPEATS', 'the deposited monograph READ HERE -- no RESTS sentence repeated (two of three cuts); a shared phrase names E-6; the control in it',
     lambda S: deposit_ok(S), lambda S: put(S, 'sj', dict(S['sj'], graded=[dict(r, sentence='one premise in five registers') for r in S['sj'].get('graded', [])]))),
    ('G-ERRATUM-FREE', 'ERRATA against its blob, and the data directory -- no erratum drafted',
     lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'] and not S['erratum_drafts'],
     lambda S: put(S, 'erratum_drafts', ['b545_erratum_draft.md'])),
    ('G-JOINT-BLOCK', 'the joint block READ HERE, with the anchor bank`s statement', lambda S: joint_ok(S),
     lambda S: put(S, 'bal', S['bal'].replace('It is T1-lit', 'It is T2'))),
    ('G-ANCHOR-REFERENCE', 'the sentence bank and the joint block -- one tier reference, §I :41, h2_sign_iff_rh',
     lambda S: S['sj'].get('anchor_tier_refs') == 1 and [s['line'] for s in S['sj']['supplementary'] if s['flag'] == 'RH-ANCHOR'] == [41]
     and 'the one T0 RH-anchor reference this keystone carries' in block(S['bal'], R.JOINTH),
     lambda S: put(S, 'sj', dict(S['sj'], anchor_tier_refs=2))),
    ('G-MARGIN-BRIDGE-TRAIL', 'the trail READ HERE -- the row, its earlier ID, its trigger',
     lambda S: '`W-ORD-MARGIN-BRIDGE` | **RESULT or RULING**' in trail(S) and '`W-ORD-LI-WEIL-BRIDGE` (:3548' in trail(S) and "**THE AUTHOR'S WORD** |" in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('`W-ORD-MARGIN-BRIDGE` | **RESULT', '`W-ORD-X` | **RESULT'))),
    ('G-CREDIT-ENTRY', 'FINDINGS READ HERE -- the credit once, at the line the bank names', lambda S: credit_ok(S),
     lambda S: put(S, 'find', S['find'].replace(R.LV_DESC, 'x'))),
    ('G-CREDIT-QUOTES', 'the credit`s quotations against BALPOS`s committed :357 and :274 and b539`s bank',
     lambda S: (lambda b: S['bal_prior'].split(NL)[356][3:] in b and S['bal_prior'].split(NL)[273][S['bal_prior'].split(NL)[273].index('**Note'):] in b
                and len([r for r in S['b539s'].get('selected', []) if r['sentence'] == R.LV_DESC]) == 1)(fblock(S['find'], R.CREDITH)),
     lambda S: put(S, 'b539s', {})),
    ('G-SURR-LINE', 'SURR READ HERE against its blob -- one line appended, pointing at the credit and at :211', lambda S: surr_ok(S),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{SURRR: S['pp_now'][SURRR] + b'a second line\n'}))),
    ('G-FANO-SEARCH', 'the search bank against the repositories listed HERE -- every one read, the needles printed',
     lambda S: S['fh'].get('repos') == S['fed'] and len(S['fed']) == 45 and len(S['fh'].get('outside_b542', [])) == 8
     and 'SIDE-fano-darkness' in S['fh'].get('by_repo', {}) and 'needles: Fano ; PG(2,2) ; triple' in S['fsearch'],
     lambda S: put(S, 'fed', S['fed'][:-1])),
    ('G-FANO-GRADED', 'the Fano source READ HERE by hand, the fresh profiles, the tier block`s row and the §V row',
     lambda S: fano_hand(S) and S['tj'].get('fano_compiled') is True
     and set(S['probes'].get('SIDE-fano-darkness', {}).get('profiles', {}).get('FanoTwoDarkness.second_moment', 'x').replace('depends on axioms: [', '').rstrip(']').split(', ')) <= {'propext', 'Quot.sound', 'Classical.choice'}
     and 'Correspondence row added under `(R155)`(5)' in block(S['bal'], R.TIERH)
     and [s['tier'] for s in S['sj'].get('supplementary', []) if s['line'] == 117] == ['T0'],
     lambda S: put(S, 'fano_src', S['fano_src'].replace('sq (x3+x4+x5) )', 'sq (x3+x4+x6) )', 1))),
    ('G-FANO-TRAIL', 'the trail READ HERE -- compiled, so no W-ORD-FANO-DECIDE row',
     lambda S: 'W-ORD-FANO-DECIDE is not filed' in trail(S) and '| `W-ORD-FANO-DECIDE` |' not in S['ot'],
     lambda S: put(S, 'ot', S['ot'] + NL + '| **2** | `W-ORD-FANO-DECIDE` | x |')),
    ('G-FINDINGS-ACT', 'FINDINGS READ HERE -- the act entry once, its counts from the banks, the next keystone',
     lambda S: (lambda b: S['find'].count(R.ACTH) == 1 and R.fmt_counts(S['tj']['counts']['rows']) in b and R.fmt_counts(S['sj']['counts']) in b
                and '**Next keystone:** FACES_OF_H2_AT_FINITE_INSTANCE with FACES_LEDGER.' in b and outside_bt(b) == 0)(fblock(S['find'], R.ACTH)),
     lambda S: put(S, 'find', S['find'].replace('**Next keystone:**', '**Next:**'))),
    ('G-B544-LINE-CORRECTED', 'OPEN_TRAILS READ HERE -- b544`s :11097 unchanged, the correction in this act`s record',
     lambda S: S['ot'].split(NL)[11096] == rd8(S['pp_prior']['OPEN_TRAILS.md']).split(NL)[11096] and 'no I row concludes re = 1/2' in S['ot'].split(NL)[11096]
     and '**A correction to b544' in trail(S) and 'side_exclusion_bridge' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**A correction to b544', '**A note'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b544'}))),
    ('G-BALPOS-PREFIX-KEPT', 'BALPOS READ HERE against its committed blob -- a true prefix, three blocks after it',
     lambda S: S['pp_now'][BALR].startswith(S['pp_prior'][BALR]) and len(S['pp_now'][BALR]) > len(S['pp_prior'][BALR])
     and S['bal'].count('<!-- b545 (R155)') == 3,
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{BALR: S['pp_now'][BALR][:100] + S['pp_now'][BALR][140:]}))),
    ('G-LINES-KEPT', 'the four written files against their blobs at b544`s commit',
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
    ('G-KERNELS-UNTOUCHED', 'the six repositories this act read or probed, READ HERE -- clean and at their heads',
     lambda S: len(S['kernels']) == 6 and all(S['kernels'].values()), lambda S: put(S, 'kernels', dict(S['kernels'], **{'SIDE-kernel': False}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b545_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind, branch deletion included',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b545_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b545 bank and tool and this act`s own PLACE-papers bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the sentence bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the sentence bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the sentence bank and ERRATA', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the sentence bank and the credit', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the tier bank', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the blobs, the tools, the token and the kernels', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b545 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels READ HERE', lambda S: 'No kernel lane opened at this act' in trail(S) and all(S['kernels'].values()),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the four written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-UNTOUCHED', 'SIDE-global-section`s correspondence ledger against its blob -- no row there; the Fano row is in BALPOS`s tier block',
     lambda S: S['corr_now'] == S['corr_prior'] and S['corr_now'] != b'', lambda S: put(S, 'corr_now', S['corr_now'] + b'| 391 | a row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b544`s close -- no instrument modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['terminal_table.py'])),
    ('G-WRITELIST-KINDS', 'every b545 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b545')" in S['suite']
                and "data/b545_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b545_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b545')
              and 'data/b545_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b545 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b545_checks_postpush.txt' if pushed else 'b545_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b545_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
