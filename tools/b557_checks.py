# -*- coding: utf-8 -*-
"""b557_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b557_registration_2026-09-28.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'f1c2e65f'      # ### b556's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = 'f54a255'           # ### b556's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b557 —'


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
import b557_record as R
import b542_checks as K542
import banned_terms as BTM
import terminal_table as TT
PPFILES = sorted(R.WRITE_OK)
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase2/method/THE_IDENTITY_CHAIN.md', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md',
         'phase1.5/rcurve/R_CURVE_CRITERION.md', 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
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
        face=read(FACE), ferry=read(os.path.join(D, 'b557_ferry.txt')),
        scan=read(os.path.join(D, 'b557_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b557_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b557_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b557_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b557_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b556_closing.txt')),
        addendum=read(os.path.join(D, 'b557_addendum.txt')),
        comp=read(os.path.join(D, 'b557_components.txt')),
        desk=read(os.path.join(D, 'b557_desk_notes.txt')),
        sc=jload('b557_scores.json'), reads=read(os.path.join(D, 'b557_reads.txt')),
        sup=jload('b557_supersede.json'), cost=jload('b557_cost.json'), costtxt=read(os.path.join(D, 'b557_cost.txt')), prj=jload('b557_prints.json'),
        rplan=jload('b557_replace_plan.json'), rdone=jload('b557_replace_done.json'), anc=jload('b557_anchor.json'), cen=jload('b557_census.json'),
        rows=jload('b557_rows.json'), ts=jload('b557_tiers.json'), w6=jload('b557_w6.json'), blocks=jload('b557_blocks.json'), roster=jload('b557_roster.json'),
        wt=read(os.path.join(D, 'b557_worktree.txt')), wt_list=gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'worktree', 'list'),
        wt_present=os.path.exists(os.path.join('D:', os.sep, 'wt-b557-lv')),
        lv_built={f: hashlib.sha256(open(os.path.join('D:', os.sep, 'SIDE-lv-conservation', '.lake', 'build', 'lib', 'lean', 'SIDELvConservation', f), 'rb').read()).hexdigest()
                  for f in ('RegisterPentagon.olean', 'RegisterPentagon.ilean')},
        probes=[json.loads(l) for l in read(os.path.join(D, 'b557_probes.jsonl')).split(NL) if l.strip()],
        kern_sc={t: rd8(blob(KERN, t + ':Kernel/Cascade/SieveCeiling.lean')) for t in ('v1.4', 'v1.7')},
        stems=jload('b557_stems.json'), fj=jload('b557_findings.json'), ttable=read(os.path.join(D, 'terminal_table.md')),
        branches=read(os.path.join(D, 'b557_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        docs={k: rd8(open(os.path.join(PP, v), 'rb').read()) for k, v in R.DOCS.items()},
        grh=rd8(open(os.path.join(PP, R.GRHR), 'rb').read()), census=rd8(open(os.path.join(PP, R.CENR), 'rb').read()),
        mem_times=[os.path.getmtime(os.path.join(R.MEMDIR, f)) for f in os.listdir(R.MEMDIR)] if os.path.isdir(R.MEMDIR) else [],
        mains=R.mains(),
        trial=dict(head=gits(R.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b555*') for r in (ROOT, PP)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b557_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b557_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b557_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b557_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b557 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b557_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b557_probes.jsonl', 'b557_tiers.json', 'b557_prints.json', 'b557_supersede.json',
                                                               'b557_blocks.json', 'b557_stems.json'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in ('b557_ferry.txt', 'b557_ferry_scan.txt', 'b557_pins_stepzero.txt')),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b557_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b557_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KERN):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith(('b557 --', 'housekeeping: terminal table regenerated at b557')):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-4][0-9]_|^b55[0-6]_|^b334_', f)]
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
    need = ['E_DIFFICULTY_THEOREM -- its correspondence section', 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME -- its correspondence section', 'defect (b)',
            'FINDINGS.md:4805', 'FINDINGS.md:5812', 'GRH_CASCADE.md:450', 'GRH_CASCADE.md:455', 'THE_KEYSTONE_CENSUS.md -- §1`s pin table',
            'R_CURVE_CRITERION`s pin sentence', 'the v0.2 section', 'THE_LOAD_BEARING_MAP lines naming each document']
    return all(x in r for x in need) and all(('%s at `%s`' % (R.TITLE[k], v)) in r for k, v in R.DOCS.items())


def sup_ok(S):
    ln = [i + 1 for i, l in enumerate(S['grh'].split(NL)) if l.startswith(P(R.SUPL)[:60])]
    return (S['grh'].count(P(R.SUPL)[:60]) == 1 and ln == [S['sup'].get('line')] and kept(S, R.GRHR) and not TT.GRADE_RE.search(R.SUPL)
            and not TT.SUPERSEDE_RE.search(R.SUPL) and not TT.TRAIL_SUP_RE.search(R.SUPL) and 'no_type_d_conspiracies' not in S['ttable'])


def cost_ok(S):
    c = S['cost']
    return (len(c.get('modules', [])) == sum(1 for f in S['cost']['modules']) and c['sum'] > 600 and 'OVER 600 S' in S['costtxt']
            and len(c['unpriced']) + len([m for m in c['modules'] if m not in c['unpriced']]) == len(c['modules']))


def prints_ok(S):
    p = S['prj']
    return (p.get('build_exit') == 0 and p.get('errors') == 0 and p.get('agree', 0) > 0 and p.get('disagree') == [] and p.get('verdict') is True
            and len(p.get('prints', {})) == p['agree'] + len(p['unbanked']))


def replace_ok(S):
    d, pl = S['rdone'], S['rplan']
    rp = {x['file']: x['rebuilt'] for x in pl.get('plan', [])}
    return (pl.get('verdict') is True and d.get('all_equal') is True and d.get('count') == len(rp) > 0
            and all(S['lv_built'][f] == rp[f] for f in S['lv_built'] if f in rp))


def m4r_ok(S):
    m = [p for p in S['probes'] if p['id'] == 'm4r']
    return len(m) == 1 and m[0]['exit'] == 0 and m[0]['errors'] == 0 and all(m[0]['profiles'].values())


def wt_ok(S):
    return (not S['wt_present'] and 'wt-b557-lv' not in S['wt_list'] and 'trial-b551-lv' in S['wt_list'] and ('work' + 'tree re' + 'move --force D:/wt-b557-lv : exit 0') in S['wt']
            and ('rm' + 'dir after its LinkType and target were verified') in S['wt'])


def anchor_ok(S):
    l = line_with(S['find'], P(R.ANH))
    return S['find'].count(P(R.ANH)) == 1 and 'has no premise' in l and 'not on the list' in l and S['anc'].get('line') == [
        i + 1 for i, x in enumerate(S['find'].split(NL)) if x.startswith(P(R.ANH))][0]


def census_ok(S):
    c = S['cen']
    rc = rd8(blob(PP, R.V01 + ':phase1.5/rcurve/R_CURVE_CRITERION.md'))
    return (c.get('bd2_lines') == [i + 1 for i, l in enumerate(rc.split(NL)) if 'bd2ae1a' in l] and c.get('pin_count') == len(set(re.findall(r'`([0-9a-f]{7,12})`', rc)))
            and S['census'].count(P(R.CEL)) == 1 and 'correcting its own line at :285' in S['census'] and kept(S, R.CENR))


def rows_ok(S):
    ok = True
    for k in R.DOCS:
        ok = ok and len(S['rows'].get(k, [])) == len(S['ts'].get(k, {}).get('rows', [])) == len(R.ROWMAP[k])
    return ok


def probes_ok(S):
    pr = {p['id']: p for p in S['probes']}
    need = {x for k in R.ROWMAP for v in R.ROWMAP[k].values() for _, a, b in v for x in (a, b) if x}
    return need <= set(pr) and all(p.get('identical_to') or p['exit'] == 0 for p in pr.values())


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


def repair_ok(S):
    rows = [(k, t['row']) for k in R.DOCS for t in S['ts'][k]['terms'] if short(t['name']) in ('e_difficulty', 'sieve_ceiling', 'sieve_ceiling_semantic', 'bright_access_required')]
    return bool(rows) and all(t['repair'] == R.REPAIR for k in R.DOCS for t in S['ts'][k]['terms'] if short(t['name']) in ('e_difficulty', 'sieve_ceiling', 'sieve_ceiling_semantic', 'bright_access_required')) and all(
        ':%d' % ln in seg(dblock(S, k), '**The repair note, carried on rows', 400) for k, ln in rows)


def short(n):
    return n.split('.')[-1]


def ediff_ok(S):
    rs = S['ts']['EDIFF']['rows']
    b162 = [r for r in rs if r['line'] == 162]
    return len(rs) == 4 and b162 and b162[0]['disp'] == 'MOVED' and 'READING (7)' in ' '.join(b162[0]['why']) and '§VII`s bullets'.replace('`', "'") in dblock(S, 'EDIFF')


def w6_ok(S):
    ok = True
    for t in ('v1.4', 'v1.7'):
        src = S['kern_sc'][t]
        ok = ok and 'fun _ => True' not in src and not re.search(r'\bsorry\b', re.sub(r'--.*', '', re.sub(r'/-[\s\S]*?-/', '', src)))
        got = {d['name']: d['grade'] for d in S['w6']['files'].get('%s:Kernel/Cascade/SieveCeiling.lean' % t, [])}
        ok = ok and got.get('sieve_ceiling') == 'SCAFFOLDING (docstring)' and got.get('bright_access_required') == 'SCAFFOLDING (docstring)'
    return ok and S['w6'].get('effects_a27415d') == []


def blocks_ok(S):
    return all(S['docs'][k].count(P(R.BH)) == 1 and kept(S, v) and S['blocks'][k]['line'] == [i + 1 for i, l in enumerate(S['docs'][k].split(NL)) if l.startswith(P(R.BH))][0]
               and all('| :%d |' % r['line'] in dblock(S, k) for r in S['ts'][k]['rows']) for k, v in R.DOCS.items())


def stems_ok(S):
    ok = True
    for k, f in R.DOCS.items():
        per = {x: 0 for x in BTM.STEMS}
        for l in rd8(S['pp_prior'][f]).split(NL):
            for m in BTM.PAT.finditer(l):
                per[[x for x in BTM.STEMS if m.group(0).lower().startswith(x)][0]] += 1
        ok = ok and S['stems'].get(k, {}).get('per') == per
    return ok


def roster_ok(S):
    ro = S['roster']
    ok = len(ro.get('roster', [])) == len(R.ROSTER) == 22
    for o, (name, rel, pat) in zip(ro.get('roster', []), R.ROSTER):
        p = os.path.join(PP, *o['path'].split('/'))
        t = rd8(open(p, 'rb').read()).split(NL) if os.path.exists(p) else []
        ok = ok and o['line'] is not None and 0 < o['line'] <= len(t) and bool(re.search(pat, t[o['line'] - 1]))
    return ok and ro.get('closed') is True and ro.get('missing') == []


def findings_ok(S):
    b = fblock(S['find'], P(R.FH))
    return S['find'].count(P(R.FH)) == 1 and '**CP-1 CLOSED:**' in b and '**Next:** b558' in b and all(R.TITLE[k] in b for k in R.DOCS)


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b556 (was ') == 2 and b.count('Deleted branch push-b556-closing (was ') == 1


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
     lambda S: 'RULING (R167) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b557' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b556`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b556' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b557' in S['ferry'] and 'ACT b557' in S['face'] and not glob.glob(os.path.join(D, 'b558_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b557')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; the reads before the lock, every evaluation and write after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R167-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R167) END' in S['ferry'] and S['ot'].count('**(R167) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R167) ratified', '(R167) noted'))),
    ('G-READS-CITED', 'the reads bank -- the eight at their paths, their sections, b556`s defect, the tier law, b555`s lines, the census, the map',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('GRH_CASCADE.md:455', 'x'))),
    ('G-NOTYPED-SUPERSEDED', 'GRH_CASCADE READ HERE -- the line once at its banked line, no grade word, neither table form; the table naming neither',
     lambda S: sup_ok(S), lambda S: put(S, 'ttable', S['ttable'] + ' no_type_d_conspiracies')),
    ('G-REBUILD-COST', 'the cost bank -- the modules listed, the banked sum over 600 s, the background declared', lambda S: cost_ok(S),
     lambda S: put(S, 'costtxt', S['costtxt'].replace('OVER 600 S', 'x'))),
    ('G-REBUILD-PRINTS', 'the prints bank -- build exit 0, no error, every banked name agreeing, the counts closing', lambda S: prints_ok(S),
     lambda S: put(S, 'prj', dict(S['prj'], disagree=[['x', 'y', []]]))),
    ('G-REBUILD-REPLACE', 'the working checkout`s RegisterPentagon artefacts READ HERE -- equal to the rebuild`s digests, every copy verified',
     lambda S: replace_ok(S), lambda S: put(S, 'lv_built', dict(S['lv_built'], **{'RegisterPentagon.olean': '0' * 64}))),
    ('G-REBUILD-M4R', 'the probe bank -- m4r exit 0, no error, every name profiled', lambda S: m4r_ok(S),
     lambda S: put(S, 'probes', [dict(p, errors=17) if p['id'] == 'm4r' else p for p in S['probes']])),
    ('G-WORKTREE-REMOVED', 'the worktree list and the path READ HERE; the banked removal record', lambda S: wt_ok(S),
     lambda S: put(S, 'wt_present', True)),
    ('G-ANCHOR-SCOPE', 'FINDINGS READ HERE -- the scope line once at its banked line', lambda S: anchor_ok(S),
     lambda S: put(S, 'find', S['find'].replace('has no premise', 'x'))),
    ('G-CENSUS-BD2', 'R_CURVE_CRITERION at the census v0.1 commit READ HERE -- the pins and the bd2ae1a lines equal to the bank; the census line and its correction',
     lambda S: census_ok(S), lambda S: put(S, 'cen', dict(S['cen'], pin_count=5))),
    ('G-ROWS-COUNTED', 'the row bank against the tier bank and the map, per document', lambda S: rows_ok(S),
     lambda S: put(S, 'rows', dict(S['rows'], FOUND=S['rows']['FOUND'][:-1]))),
    ('G-PROBES-BANKED', 'the probe bank -- every probe the map names, each exit 0 or identical at the tag', lambda S: probes_ok(S),
     lambda S: put(S, 'probes', [dict(p, exit=1) if p['id'] == 'k1' else p for p in S['probes']])),
    ('G-TIERS-COUNTED', 'the tier bank -- vocabulary, weakest links, counts recomputed', lambda S: tiers_ok(S),
     lambda S: put(S, 'ts', dict(S['ts'], FOUND=dict(S['ts']['FOUND'], term_tiers=dict(S['ts']['FOUND']['term_tiers'], T0=-1))))),
    ('G-REPAIR-NOTE', 'the tier bank and the blocks -- every reading of the four SieveCeiling names carries the note, its rows named in the block',
     lambda S: repair_ok(S), lambda S: put(S, 'docs', dict(S['docs'], FOUND=S['docs']['FOUND'].replace('**The repair note, carried on rows', 'x')))),
    ('G-EDIFF-BULLETS', 'the tier bank and E_DIFFICULTY`s block -- the four bullets, :162 MOVED by READING (7)', lambda S: ediff_ok(S),
     lambda S: put(S, 'ts', swap_row(S, 'EDIFF', 162, disp='CARRIED'))),
    ('G-W6-STATUS', 'SieveCeiling.lean at v1.4 and v1.7 READ HERE -- no sorry, no fun _ => True, the two base terminals SCAFFOLDING; SIDE-effects carries none',
     lambda S: w6_ok(S), lambda S: put(S, 'kern_sc', dict(S['kern_sc'], **{'v1.7': S['kern_sc']['v1.7'] + ' fun _ => True'}))),
    ('G-BLOCKS-EIGHT', 'the eight documents READ HERE against their blobs -- one block each at its banked line, every row', lambda S: blocks_ok(S),
     lambda S: put(S, 'docs', dict(S['docs'], INVAR=S['docs']['INVAR'].replace('| :499 |', '| :999 |')))),
    ('G-STEMS-COUNTED', 'the eight at b556`s commit, counted here with the tool`s own pattern -- equal to the bank', lambda S: stems_ok(S),
     lambda S: put(S, 'stems', dict(S['stems'], ENUMERA=dict(S['stems']['ENUMERA'], per={x: -1 for x in BTM.STEMS})))),
    ('G-ROSTER', 'every roster document READ HERE at its banked line, the block heading matched; CLOSED', lambda S: roster_ok(S),
     lambda S: put(S, 'roster', dict(S['roster'], roster=S['roster']['roster'][:-1]))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once, the eight, CP-1 CLOSED, b558 next', lambda S: findings_ok(S),
     lambda S: put(S, 'find', S['find'].replace(P(R.FH), 'x'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in two repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b556'}))),
    ('G-MEMORY-UNREFRESHED', 'the memory directory READ HERE -- no file written after this face (R157)(6)',
     lambda S: bool(S['mem_times']) and max(S['mem_times']) < os.path.getmtime(FACE),
     lambda S: put(S, 'mem_times', S['mem_times'] + [os.path.getmtime(FACE) + 1])),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-LINES-KEPT', 'the twelve written files against their blobs at b556`s commit',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY, SPIRAL_MAP, FACES_LEDGER, THE_LOAD_BEARING_MAP, THE_IDENTITY_CHAIN, SIMPLICITY, R_CURVE, INDEX_ARITY against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in OTHER if 'A_Place_to_Stand' not in f and f != 'ERRATA.md'),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'REGISTRY.md': S['pp_now']['REGISTRY.md'] + b' '}))),
    ('G-KERNEL-SOURCES-UNTOUCHED', 'the kernels` mains READ HERE against their pre-act heads -- nothing written',
     lambda S: kernel_sources_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-effects': ['SIDEEffects/Structural.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b557_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b557_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b557 bank and tool and this act`s PLACE-papers bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the tier bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the rows and the W-6 bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against E_DIFFICULTY`s rows', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the prints and m4r', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the roster', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the mains, the tools, the token, the deposit and the trial worktree', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b557 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels` mains READ HERE',
     lambda S: 'No kernel lane opened at this act' in trail(S) and kernel_sources_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the twelve written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b556`s close -- no .py tool modified',
     lambda S: [x for x in S['tools_edited'] if x.endswith('.py')] == [],
     lambda S: put(S, 'tools_edited', ['terminal_table.py'])),
    ('G-WRITELIST-KINDS', 'every b557 commit in four repositories and the housekeeping commit, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b557')" in S['suite']
                and "data/b557_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b557_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b557')
              and 'data/b557_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b557 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b557_checks_postpush.txt' if pushed else 'b557_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b557_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
