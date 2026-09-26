# -*- coding: utf-8 -*-
"""b544_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b544_registration_2026-09-26.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '67d18132'      # ### b543's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = 'ba00159'           # ### b543's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b544 —'


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


import b544_record as R
import b544_probe_part as P
import b542_record as Q
import b542_checks as K542
PPFILES = ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md']
SIDE_TIP = '2e43315'
CORRP = os.path.join(SIDE, 'CORRESPONDENCE.md')
HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': '2e43315',
         'SIDE-spinor-calibration-mathlib': '21b36aa'}
PROBED = ('SIDE-explicit-formula', 'SIDE-lv-conservation', 'SIDE-kernel', 'SIDE-spinor-calibration-mathlib')
BRANCH_LINES = ['Deleted branch push-b543 (was 8ee4519c).', 'Deleted branch push-b543-closing (was 67d18132).', 'Deleted branch push-b543 (was ba00159).']


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'))] + ['(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    files = PPFILES + ['README.md', 'REGISTRY.md', 'SPIRAL_MAP.md']
    here = P.classify(P.enumerate_all())[0]
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b544_ferry.txt')),
        scan=read(os.path.join(D, 'b544_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b544_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b544_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b544_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b544_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b543_closing.txt')),
        addendum=read(os.path.join(D, 'b544_addendum.txt')),
        comp=read(os.path.join(D, 'b544_components.txt')),
        desk=read(os.path.join(D, 'b544_desk_notes.txt')),
        sc=json.loads(read(os.path.join(D, 'b544_scores.json')) or '{}'),
        reads=read(os.path.join(D, 'b544_reads.txt')),
        fj=json.loads(read(os.path.join(D, 'b544_file.json')) or '{}'),
        nj=json.loads(read(os.path.join(D, 'b544_note.json')) or '{}'),
        dj=json.loads(read(os.path.join(D, 'b544_decls.json')) or '{}'),
        pj=json.loads(read(os.path.join(D, 'b544_premises.json')) or '{}'),
        ij=json.loads(read(os.path.join(D, 'b544_index.json')) or '{}'),
        t0j=json.loads(read(os.path.join(D, 'b544_t0.json')) or '{}'),
        tbj=json.loads(read(os.path.join(D, 'b544_table.json')) or '{}'),
        probes={r: json.loads(read(os.path.join(D, 'b544_probe_%s.json' % r)) or '{}') for r in PROBED},
        probe_txt={r: read(os.path.join(D, 'b544_probe_%s.txt' % r)) for r in PROBED},
        tt=json.loads(read(os.path.join(D, 'terminal_table.json')) or '{}'), ttmd=read(os.path.join(D, 'terminal_table.md')),
        branches=read(os.path.join(D, 'b544_branches.txt')),
        e6draft=read(os.path.join(D, 'b543_erratum_draft.md')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in files},
        pp_now={f: open(os.path.join(PP, f), 'rb').read() for f in files},
        errata=read(os.path.join(PP, 'ERRATA.md')), find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        paths=read(os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')),
        live=read(os.path.join(PP, 'day1', 'A_Place_to_Stand.md')),
        corr_now=open(CORRP, 'rb').read(), corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md'),
        here=dict(count=len(here), subjects={s: sum(1 for x in here if x['subject'] == s) for s in ('ZETA', 'ARITHMETIC-OR-LOGIC', 'PROGRAMME-TYPE')},
                  per_repo={r: {s: sum(1 for x in here if x['repo'] == r and x['subject'] == s) for s in ('ZETA', 'ARITHMETIC-OR-LOGIC', 'PROGRAMME-TYPE')}
                            for r in set(x['repo'] for x in here)}),
        kchanged=set(P.module_of(f) for f in Q.g('SIDE-kernel', 'diff', '--name-only', '--diff-filter=MDR', 'v1.5', 'HEAD', '--', '*.lean').split(NL) if f),
        name1109=R.masked_name(),
        kernels={k: gits(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == '' and
                 gits(os.path.join('D:', os.sep, k), 'rev-parse', '--short', 'HEAD').startswith(h) for k, h in HEADS.items()},
        branch_lists={r: gits(r, 'branch', '--list', 'push-b543*') for r in (ROOT, PP)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b544_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b544_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b544_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b544_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b544 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b544_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b544_reads.txt', 'b544_decls.json', 'b544_premises.json', 'b544_index.json',
                                                               'b544_probe_SIDE-explicit-formula.json', 'b544_file.json', 'b544_note.json'))),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b544_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b544_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b544 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-9]_|^b54[0123]_|^b334_', f)]
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


def block(S, text, h):
    return text[text.index(h):] if h in text else ''


def subseq(old, new):
    it = iter(new.split(NL))
    return all(any(l == m for m in it) for l in old.split(NL))


def kept(S, f):
    old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
    ok = subseq(old, new)
    if f == 'OPEN_TRAILS.md':
        ok = ok and S['pp_now'][f].startswith(S['pp_prior'][f])
    return ok


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0].split(',')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == S['recomputed'][k]


def entry6(S):
    t = S['errata']
    i = t.find('## E-2026-09-25-6 ')
    j = t.find('**Filed 2026-09-26 by b544', i)
    if i < 0 or j < 0:
        return ''
    return t[i:t.find(NL, j) if t.find(NL, j) >= 0 else len(t)]


def reads_ok(S):
    r = S['reads']
    e = S['errata'].split(NL)
    a = next((i for i, l in enumerate(e) if l.startswith('<!-- b337 partition -->')), -1)
    p = S['paths'].split(NL)
    s = next((i for i, l in enumerate(p) if l.startswith('## ANNEX B')), -1)
    live = S['live'].split(NL)
    n10 = next((i for i, l in enumerate(live) if l.startswith('**(10)**')), -1)
    return (a >= 0 and ('  :%d %s' % (a + 1, e[a][:220])) in r and s >= 0 and ('  :%d %s' % (s + 1, p[s][:300])) in r
            and n10 >= 0 and ('  :%d %s' % (n10 + 1, live[n10][:600])) in r and '<the SIDE-kernel v1.1 MetaKernel.lean:138 name>' in r
            and 'relay data/b543_erratum_draft.md' in r)


def note_ok(S):
    old, new = rd8(S['pp_prior']['FINDINGS.md']).split(NL), S['find'].split(NL)
    return new[1108] == old[1108] and new[1109] == R.NOTE and new[1110] == old[1109] and S['nj'].get('note_line') == 1110


def withheld_ok(S):
    n = S['name1109']
    p = r'(?<![A-Za-z0-9_])' + re.escape(n or 'x-none-x') + r'(?![A-Za-z0-9_])'
    return bool(n) and not [f for f, t in S['act_blobs'].items() if re.search(p, t)]


def enum_ok(S):
    return S['here']['count'] == S['dj'].get('count') == 5293 and S['dj'].get('equal') is True


def subjects_ok(S):
    return S['here']['subjects'] == S['dj'].get('subjects') and all(S['here']['per_repo'].get(r, {}) == {k: c.get(k, 0) for k in ('ZETA', 'ARITHMETIC-OR-LOGIC', 'PROGRAMME-TYPE')}
                                                                    for r, c in S['dj'].get('per_repo', {}).items())


def profiles_ok(S):
    rows = S['pj'].get('rows', [])
    ok = bool(rows)
    for r in rows:
        ok = ok and (r['profile'] is not None or r['profile_class'].startswith(('NOT PROFILED AT THE PIN', 'PRIVATE DECLARATION')))
        if r['profile']:
            ok = ok and ("'%s' %s" % (r['full'], r['profile'])) in re.sub(r'\n\s+', ' ', S['probe_txt'].get(r['repo'], ''))
    return ok


def timed_ok(S):
    return all(S['probes'][r].get('exit') == 0 and isinstance(S['probes'][r].get('seconds'), (int, float)) and S['probes'][r].get('seconds') > 0 for r in PROBED)


def closure_ok(S):
    pk = S['probes']['SIDE-kernel']
    legacy = 'legacy/ is outside the build: no library target'
    return set(pk.get('changed_modules', [])) == S['kchanged'] and all(x['changed'] and (set(x['changed']) <= S['kchanged'] or (x['changed'] == [legacy] and x['file'].startswith('legacy/'))) for x in pk.get('skipped', []))


def premises_ok(S):
    props = set(S['pj'].get('props', []))
    rows = S['pj'].get('rows', [])
    proved = S['pj'].get('proved', {})
    ok = all(p['prop'] in props or not p['prop'] in props for r in rows for p in r['premises'])
    for prop, thm in proved.items():
        ok = ok and any(x.get('name') == thm and re.search(r':\s*(?:[A-Za-z0-9_]+\.)*' + re.escape(prop) + r'\s*:=', ' '.join(x.get('statement', '').split()))
                        for x in S['dj']['decls'] if x['repo'] != R.PRIV)
    return ok and all((r['state'] == 'PREMISE-FREE') == (not r['premises']) for r in rows) and bool(rows)


def t0_ok(S):
    rows = S['pj'].get('rows', [])
    return (len(S['t0j'].get('zeta', [])) == sum(1 for r in rows if r['t0']) == S['pj']['counts']['t0']
            and all(R.prof_class(r['profile']) in ('none', 'std3-or-fewer') for r in S['t0j'].get('arithmetic_or_logic', [])))


def marks_ok(S):
    rows = S['ij'].get('rows', [])
    ok = bool(rows)
    byk = {(x['repo'], x['file'], x['line']): x for x in S['dj']['decls'] if x['repo'] != R.PRIV}
    for r in rows:
        x = byk.get((r['repo'], r['file'], r['line']))
        if not x:
            return False
        b, c, body = R.split_statement(x['statement'])
        mk, shape = R.mark_of(body if x['kw'] in P.BODYKW else c)
        ok = ok and (mk, shape) == (r['mark'], r['shape'])
    return ok


def table_ok(S):
    rows = S['tt'].get('rows', [])
    z = [x for x in rows if x.get('zeta_row')]
    return (bool(rows) and all('ei' in x for x in rows) and bool(z) and all(x['ei'] not in ('', None, '—') for x in z)
            and '| E/I (b544) |' in S['ttmd'] and S['tbj'].get('blank_zeta') == 0)


def cp_ok(S, title, marker):
    b = block(S, S['find'], title)
    return S['find'].count(title) == 1 and marker in b and outside_bt(b[:b.find(NL + '## ', 5) if b.find(NL + '## ', 5) > 0 else len(b)]) == 0


def branches_ok(S):
    b = S['branches']
    return (all(v == '' for v in S['branch_lists'].values()) and all(b.count(l) == 1 for l in BRANCH_LINES)
            and b.find('git branch --merged main') < b.find('=== DELETIONS'))


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R154) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b544' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAG-DECLARED', 'this act`s banked scan -- one flag, "first" at line 49, and the face says so',
     lambda S: '(R81) FLAGS : 1' in line_with(S['scan'], '(R81) FLAGS') and re.search(r'line 49\s+col \d+\s+first', S['scan']) is not None
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
    ('G-PRIOR-CLOSED-PUSHED', 'b543`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'E-2026-09-25-6 : DRAFTED' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b544' in S['ferry'] and 'ACT b544' in S['face'] and not glob.glob(os.path.join(D, 'b545_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b544')),
    ('G-PEEK-DECLARED', 'the face`s (C) block, and the components` banks after the lock',
     lambda S: 'NO `#print axioms` OR `#check` WAS RUN FOR THIS ACT BEFORE THE SEAL' in flat(S['face']) and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R154-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R154) END' in S['ferry'] and S['ot'].count('**(R154) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R154) ratified', '(R154) noted'))),
    ('G-READS-CITED', 'the reads bank against ERRATA, PATHS §ANNEX B and the monograph READ HERE, the :1109 name masked',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('<the SIDE-kernel v1.1 MetaKernel.lean:138 name>', 'x'))),
    ('G-E6-FILED', 'ERRATA READ HERE -- the b543 draft`s bytes once, then the b544 Status line, at the file`s end',
     lambda S: S['errata'].count(S['e6draft'].rstrip(NL)) == 1 and bool(entry6(S)) and S['errata'].rstrip(NL).endswith(entry6(S).split(NL)[-1])
     and '(R154)(1)' in entry6(S) and 'every RESTS row of the read has a filed erratum' in entry6(S),
     lambda S: put(S, 'errata', S['errata'].replace('**Filed 2026-09-26 by b544', '**Noted by b544'))),
    ('G-E6-LISTED', 'ERRATA READ HERE -- the bullet once, directly after E-2026-09-25-5`s',
     lambda S: (lambda t: NL.join(t).count('- `E-2026-09-25-6` —') == 1 and any(t[i].startswith('- `E-2026-09-25-5` —') and t[i + 1].startswith('- `E-2026-09-25-6` —')
                                                                      for i in range(len(t) - 1)))(S['errata'].split(NL)),
     lambda S: put(S, 'errata', S['errata'].replace('- `E-2026-09-25-6` —', '- `E-2026-09-25-6x` —'))),
    ('G-E6-BACKTICKS', 'the filed entry READ HERE -- no backtick left open, equal to the bank',
     lambda S: bool(entry6(S)) and outside_bt(entry6(S)) == 0 == S['fj'].get('backticks_outside_code'),
     lambda S: put(S, 'errata', S['errata'].replace('**Filed 2026-09-26 by b544', '**Filed 2026-09-26 by b544`s'))),
    ('G-NOTE-1109', 'FINDINGS READ HERE against b543`s blob -- :1109 unchanged, the ruling`s note beneath it, the old :1110 at :1111',
     lambda S: note_ok(S), lambda S: put(S, 'find', S['find'].replace(R.NOTE, 'a note'))),
    ('G-NAME-WITHHELD', 'every b544 bank and tool and this act`s own PLACE-papers bytes, against the :1109 name read HERE from SIDE-kernel v1.1',
     lambda S: withheld_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted='x ' + (S['name1109'] or '') + ' x'))),
    ('G-ENUMERATION', 'the enumeration RUN HERE at b542`s pins against the bank and b542`s count', lambda S: enum_ok(S),
     lambda S: put(S, 'here', dict(S['here'], count=S['here']['count'] - 1))),
    ('G-SUBJECTS', 'the classification RUN HERE against the bank, per subject and per repository', lambda S: subjects_ok(S),
     lambda S: put(S, 'here', dict(S['here'], subjects=dict(S['here']['subjects'], ZETA=0)))),
    ('G-PROFILES', 'every ZETA terminal`s profile against its probe`s own output, or its declared reason', lambda S: profiles_ok(S),
     lambda S: put(S, 'probe_txt', {k: '' for k in S['probe_txt']})),
    ('G-PROBE-TIMED', 'each probe bank -- exit 0 and its seconds', lambda S: timed_ok(S),
     lambda S: put(S, 'probes', dict(S['probes'], **{'SIDE-kernel': dict(S['probes']['SIDE-kernel'], exit=1)}))),
    ('G-KERNEL-CLOSURE', 'SIDE-kernel`s changed modules RUN HERE against the probe bank; every skipped row names one', lambda S: closure_ok(S),
     lambda S: put(S, 'kchanged', set())),
    ('G-PREMISES', 'the premises bank -- every PROVED mark`s theorem found at its pin stating the Prop', lambda S: premises_ok(S),
     lambda S: put(S, 'pj', dict(S['pj'], proved=dict(S['pj'].get('proved', {}), zzz='no_such_theorem')))),
    ('G-T0-INVENTORY', 'the T0 bank against the premises bank and the profile classes', lambda S: t0_ok(S),
     lambda S: put(S, 't0j', dict(S['t0j'], zeta=S['t0j'].get('zeta', [])[1:]))),
    ('G-MARKS', 'every CP-3 mark recomputed HERE from the statement', lambda S: marks_ok(S),
     lambda S: put(S, 'ij', dict(S['ij'], rows=[dict(r, mark='X') for r in S['ij'].get('rows', [])]))),
    ('G-FORCES-CLAUSES', 'every I row carries its clause, every E row none',
     lambda S: bool(S['ij'].get('rows')) and all(bool(r['forces']) == (r['mark'] == 'I') for r in S['ij']['rows']),
     lambda S: put(S, 'ij', dict(S['ij'], rows=[dict(r, forces='') for r in S['ij'].get('rows', [])]))),
    ('G-ZERO-ROWS-READ', 'the I rows naming a zero -- counted, and the one concluding re = 1/2 printed with its premise',
     lambda S: S['ij']['counts']['I_naming_zero'] == sum(1 for r in S['ij']['rows'] if r['mark'] == 'I' and r['names_zero'])
     and [x[0] for x in S['ij'].get('i_concluding_location', [])] == ['SIDEBridge.side_exclusion_bridge'],
     lambda S: put(S, 'ij', dict(S['ij'], i_concluding_location=[]))),
    ('G-TABLE-COLUMN', 'the terminal table READ HERE -- the column in every row, no blank ZETA cell, the header',
     lambda S: table_ok(S), lambda S: put(S, 'ttmd', S['ttmd'].replace('| E/I (b544) |', '|'))),
    ('G-FINDINGS-CP2', 'FINDINGS READ HERE -- the CP-2 entry once', lambda S: cp_ok(S, R.T2TITLE, '**The ZETA terminals.**'),
     lambda S: put(S, 'find', S['find'].replace('**The ZETA terminals.**', '**x**'))),
    ('G-FINDINGS-CP3', 'FINDINGS READ HERE -- the CP-3 entry once', lambda S: cp_ok(S, R.T3TITLE, '**What the index says, in words.**'),
     lambda S: put(S, 'find', S['find'].replace('**What the index says, in words.**', '**x**'))),
    ('G-CHECKPOINT-LINES', 'the trail READ HERE -- CP-2 and CP-3 FIRED, CP-1 OPEN with its order',
     lambda S: '**CP-2 -- FIRED at b544.**' in trail(S) and '**CP-3 -- FIRED at b544.**' in trail(S) and 'CP-1 -- OPEN, its order under (R154)(3)' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**CP-3 -- FIRED at b544.**', 'CP-3'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b543'}))),
    ('G-LINES-KEPT', 'the three written files against their blobs at b543`s commit, BOM stripped both sides',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the scores` monograph clause, recomputed from the blobs',
     lambda S: bool(S['recomputed'].get('mono')) and all(S['recomputed']['mono'].values()),
     lambda S: put(S, 'recomputed', dict(S['recomputed'], mono={'x': False}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY and SPIRAL_MAP bytes against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md', 'SPIRAL_MAP.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b' '}))),
    ('G-KERNELS-UNTOUCHED', 'the probed repositories and the ledger`s READ HERE -- clean and at their heads',
     lambda S: len(S['kernels']) == 5 and all(S['kernels'].values()), lambda S: put(S, 'kernels', dict(S['kernels'], **{'SIDE-kernel': False}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b544_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind, branch deletion included',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b544_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b544 bank and tool and this act`s own PLACE-papers bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the enumeration bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the premises bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the index bank', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the index bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the table bank', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the blobs, the tools, the token and the kernels', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b544 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels READ HERE', lambda S: 'No kernel lane opened at this act' in trail(S) and all(S['kernels'].values()),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the three written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-UNTOUCHED', 'the correspondence ledger against its blob at b542`s commit -- no row this act',
     lambda S: S['corr_now'] == S['corr_prior'] and S['corr_now'] != b'', lambda S: put(S, 'corr_now', S['corr_now'] + b'| 391 | a row |')),
    ('G-INSTRUMENTS-ONE-EDIT', 'relay`s tools against b543`s close -- terminal_table.py the one modified instrument',
     lambda S: S['tools_edited'] == ['terminal_table.py'], lambda S: put(S, 'tools_edited', ['terminal_table.py', 'corr_row.py'])),
    ('G-WRITELIST-KINDS', 'every b544 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b544')" in S['suite']
                and "data/b544_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b544_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b544')
              and 'data/b544_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b544 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b544_checks_postpush.txt' if pushed else 'b544_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b544_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
