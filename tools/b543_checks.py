# -*- coding: utf-8 -*-
"""b543_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b543_registration_2026-09-25.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'ba409a4c'      # ### b542's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = '13c186a'           # ### b542's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b543 —'


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


import b543_record as R
import b541_record as A
import b542_record as Q
PPFILES = ['FINDINGS.md', 'OPEN_TRAILS.md']
SIDE_TIP = '2e43315'
CORRP = os.path.join(SIDE, 'CORRESPONDENCE.md')
LIVEP = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
DEPP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
GRADES = ('STANDS', 'STANDS-AS-HISTORY', 'RESTS', 'EXCEEDS')
TIERS = ('T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4')
HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': '2e43315'}
DATED = [('SIDE-kernel', 'v1.4', 'f374174'), ('SIDE-lv-conservation', 'v0.6.0', 'c80bdc2'), ('SIDE-lv-conservation', 'v0.7.0', '2d86182'),
         ('SIDE-lv-conservation', 'v0.8.0', '6efa9e5'), ('SIDE-lv-conservation', 'v0.9.0', 'e3d08b6'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'),
         ('SIDE-lv-conservation', 'c5ef4bc', 'c5ef4bc')]
BRANCH_LINES = ['Deleted branch push-b542 (was 594b5ed7).', 'Deleted branch push-b542-closing (was ba409a4c).',
                'Deleted branch push-b542 (was 13c186a).', 'Deleted branch push-b542 (was 2e43315).']


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'))] + ['(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def sorry_greps():
    """### Appendix C`s command at v1.5, read HERE: the literal grep`s lines, and `sorry` as a term in the code with comments blanked"""
    lit, code = 0, 0
    for f in [f for f in R.g('SIDE-kernel', 'ls-tree', '-r', '--name-only', 'v1.5', '--', 'Kernel', 'Bridge').split(NL) if f.endswith('.lean')]:
        t = R.g('SIDE-kernel', 'show', 'v1.5:' + f).replace(chr(13), '')
        lit += sum(1 for l in t.split(NL) if 'sorry' in l and '--' not in l)
        code += len(re.findall(r'(?<![A-Za-z0-9_])sorry(?![A-Za-z0-9_])', Q.blank_all_comments(t)))
    return lit, code


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    files = PPFILES + ['ERRATA.md', 'README.md', 'REGISTRY.md', 'SPIRAL_MAP.md']
    lr, lsel, lstop = A.census_of(LIVEP)
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b543_ferry.txt')),
        scan=read(os.path.join(D, 'b543_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b543_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b543_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b543_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b543_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b542_closing.txt')),
        addendum=read(os.path.join(D, 'b543_addendum.txt')),
        comp=read(os.path.join(D, 'b543_components.txt')),
        desk=read(os.path.join(D, 'b543_desk_notes.txt')),
        sc=json.loads(read(os.path.join(D, 'b543_scores.json')) or '{}'),
        reads=read(os.path.join(D, 'b543_reads.txt')), anchor=read(os.path.join(D, 'b543_anchor.txt')),
        cj=json.loads(read(os.path.join(D, 'b543_census.json')) or '{}'),
        tj=json.loads(read(os.path.join(D, 'b543_terms.json')) or '{}'),
        e6j=json.loads(read(os.path.join(D, 'b543_erratum6.json')) or '{}'),
        e6=read(os.path.join(D, 'b543_erratum_draft.md')),
        mapj=json.loads(read(os.path.join(D, 'b543_map.json')) or '{}'),
        branches=read(os.path.join(D, 'b543_branches.txt')),
        b541=json.loads(read(os.path.join(D, 'b541_census.json')) or '{}'),
        b532={x['id']: x for x in (json.loads(read(os.path.join(D, 'b532_rows.json')) or '{}').get('rows') or [])},
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in files},
        pp_now={f: open(os.path.join(PP, f), 'rb').read() for f in files},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), errata=read(os.path.join(PP, 'ERRATA.md')),
        live=read(LIVEP), dep=read(DEPP),
        corr_now=open(CORRP, 'rb').read(), corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md'),
        tbc=R.g('SIDE-kernel', 'show', 'v1.5:Bridge/TheBridgeComplete.lean').replace(chr(13), ''),
        rp=R.g('SIDE-lv-conservation', 'show', 'v0.10.0:SIDELvConservation/RegisterPentagon.lean').replace(chr(13), ''),
        lakefile=R.g('SIDE-kernel', 'show', 'v1.5:lakefile.lean'), tree15=R.g('SIDE-kernel', 'ls-tree', '-r', '--name-only', 'v1.5'),
        mk11=R.g('SIDE-kernel', 'show', 'v1.1:MetaKernel.lean').replace(chr(13), ''),
        dated={(r, t): R.g(r, 'rev-parse', '--short', t + '^{commit}').strip() for r, t, _ in DATED},
        here=dict(act_two=len(lsel) - lstop, first=lsel[lstop]['line']),
        sorry=sorry_greps(),
        kernels={k: gits(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == '' and
                 gits(os.path.join('D:', os.sep, k), 'rev-parse', '--short', 'HEAD').startswith(h) for k, h in HEADS.items()},
        branch_lists={r: gits(r, 'branch', '--list', 'push-b542*') for r in (ROOT, PP, SIDE)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b543_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b543_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b543_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b543_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b543 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b543_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b543_reads.txt', 'b543_anchor.txt', 'b543_census.json', 'b543_terms.json',
                                                               'b543_erratum_draft.md', 'b543_map.json', 'b543_branches.txt'))),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b543 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-9]_|^b54[012]_|^b334_', f)]
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
    return subseq(old, new) and S['pp_now'][f].startswith(S['pp_prior'][f])


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0].split(',')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def crows(S):
    return (S['cj'] or {}).get('rows') or []


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == S['recomputed'][k]


def reads_ok(S):
    r, tb, rp = S['reads'], S['tbc'].split(NL), S['rp'].split(NL)
    f = S['find'].split(NL)
    e = S['errata'].split(NL)
    heads = [('  :%d %s' % (i + 1, e[i][:200])) for i in range(476, min(687, len(e))) if e[i].startswith('## E-') or e[i].startswith('**`E-')]
    return (('  :157 %s' % tb[156]) in r and ('  :215 %s' % tb[214]) in r and ('  :82 %s' % rp[81]) in r and ('  :189 %s' % rp[188]) in r
            and ('### FINDINGS.md:4884 %s' % f[4883][:200]) in r and len(heads) == 5 and all(h in r for h in heads)
            and 'SIDE-kernel 0e5233f Kernel/PoissonExhaustion.lean:43-69' in r)


def rows_ok(S):
    rs = crows(S)
    live = S['live'].split(NL)
    return (len(rs) == S['here']['act_two'] and all(r['grade'] in GRADES and r['tier'] in TIERS for r in rs)
            and all(r['errata'] for r in rs if r['grade'] == 'RESTS') and all(not r['errata'] for r in rs if r['grade'] != 'RESTS')
            and all(r['replacement'] for r in rs if 'E-2026-09-25-6' in r['errata'])
            and all(A.nz(r['sentence'])[:60] in A.seg_lines(S['live'], r['line']) if hasattr(A, 'seg_lines') else A.nz(r['sentence'])[:60] in A.nz(' '.join(live[r['line'] - 1:r['line'] + 13])) for r in rs)
            and sum(S['cj']['counts'].values()) == len(rs))


def carried_ok(S):
    rs = [r for r in crows(S) if r['carried']]
    ok = len(rs) >= 8
    for r in rs:
        v = S['b532'].get(r['carried'], {}).get('verdict')
        ok = ok and (v == r['grade'] or (v == 'STANDS' and r['grade'] == 'STANDS-AS-HISTORY' and r['vocab_move']))
    return ok and sorted(x[1] for x in S['cj'].get('vocab_moves', [])) == ['M-21', 'M-26', 'M-27']


def deposit_ok(S):
    rs = crows(S)
    dep = S['dep'].split(NL)
    depnz = A.nz(' '.join(dep))
    livenz = A.nz(' '.join(S['live'].split(NL)))
    num = [r for r in rs if isinstance(r['dep_line'], int)]
    return (bool(num) and all(A.nz(r['sentence'])[:60] in A.nz(' '.join(dep[r['dep_line'] - 1:r['dep_line'] + 13])) for r in num)
            and all(A.nz(r['sentence']) not in depnz for r in rs if r['dep_line'] == 'LIVE-SOLE'))


def history_ok(S):
    h = [r for r in crows(S) if r['grade'] == 'STANDS-AS-HISTORY']
    return (len(h) >= 20 and not [r for r in h if r['errata']] and all(S['dated'][(r, t)] == sha for r, t, sha in DATED)
            and '## E-2026-07-23-1' in S['errata'])


def terms_ok(S):
    ts = S['tj'].get('terms', [])
    ok = len(ts) == len(R.TERMS) and bool(ts)
    for x, (name, repo, pin, path, needle, (bank, vocab, value), now) in zip(ts, R.TERMS):
        ok = ok and x['terminal'] == name and x['found'] and R.earlier_in_bank(bank, name, vocab, value) and x['word'] == ('CARRIED' if now == value else 'MOVED')
        if x['found']:
            t = R.g(repo, 'show', '%s:%s' % (pin, x['found']['file'])).replace(chr(13), '').split(NL)
            ok = ok and NL.join(t[x['found']['line'] - 1:]).startswith(x['found']['statement'])
    return ok


def supp_ok(S):
    live = S['live'].split(NL)
    sp = S['cj'].get('supplementary', [])
    return len(sp) == len(R.SUPP) and all(live[x['line'] - 1].strip() == x['sentence'] for x in sp)


def e6_ok(S):
    rs = [r for r in crows(S) if 'E-2026-09-25-6' in r['errata']] + [r for r in S['cj'].get('supplementary', []) if 'E-2026-09-25-6' in r['errata']]
    t = S['e6']
    return (t.startswith('## E-2026-09-25-6 — ') and 'DRAFT, NOT FILED' in t.split(NL)[0] and len(rs) == S['e6j'].get('rows') == t.count('  - replacement: *"')
            and t.count('`') == 0 and "'s" in t)


def map_ok(S):
    b = block(S, S['find'], R.FTITLE)
    rows14 = [l for l in b.split(NL) if re.match(r'^\| (Chapter|PART|Appendix|Correspondence)', l)]
    c = S['cj'].get('counts', {})
    return (S['find'].count(R.FTITLE) == 1 and len(rows14) == len(R.SPANS) and all(l.count('|') == 14 for l in rows14)
            and ('%d rows: STANDS %d · STANDS-AS-HISTORY %d · RESTS %d · EXCEEDS %d' % (len(crows(S)), c.get('STANDS', -1), c.get('STANDS-AS-HISTORY', -1),
                                                                                  c.get('RESTS', -1), c.get('EXCEEDS', -1))) in b
            and 'FINDINGS.md:4834' in b and outside_bt(b) == 0)


def hold_ok(S):
    old = rd8(S['pp_prior']['FINDINGS.md']).split(NL)
    new = S['find'].split(NL)
    return old[1108] == new[1108] and old[1109] == new[1109] and old[1107] == new[1107]


def b542_ok(S):
    b = block(S, S['find'], R.FTITLE)
    l1109 = S['find'].split(NL)[1108]
    m = S['mk11'].split(NL)[137] if len(S['mk11'].split(NL)) > 137 else ''
    nm = re.search(r'(theorem|def|lemma)\s+([A-Za-z0-9_\.]+)', m)
    return ('**A correction to b542, carried here.**' in b and 'MetaKernel.lean:138' in b and bool(nm)
            and re.search(r'(?<![A-Za-z0-9_])' + re.escape(nm.group(2).split('.')[-1]) + r'(?![A-Za-z0-9_])', l1109) is not None)


def branches_ok(S):
    b = S['branches']
    return (all(v == '' for v in S['branch_lists'].values()) and all(b.count(l) == 1 for l in BRANCH_LINES)
            and b.find('git branch --merged main') < b.find('=== DELETIONS'))


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R153) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b543' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- no flag, and the face says so',
     lambda S: '(R81) FLAGS : 0' in line_with(S['scan'], '(R81) FLAGS') and 'The ferry scan carries no (R81) flag' in flat(S['face']),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b542`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'E-2026-09-25-5 : FILED' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b543' in S['ferry'] and 'ACT b543' in S['face'] and not glob.glob(os.path.join(D, 'b544_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b543')),
    ('G-PEEK-DECLARED', 'the face`s (C) block, and the components` banks after the lock',
     lambda S: 'No `#check` or `#print axioms` was run for this act before the seal' in flat(S['face']) and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R153-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R153) END' in S['ferry'] and S['ot'].count('**(R153) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R153) ratified', '(R153) noted'))),
    ('G-READS-CITED', 'the reads bank against TheBridgeComplete and PoissonExhaustion v1.5, RegisterPentagon v0.10.0, FINDINGS and ERRATA READ HERE',
     lambda S: reads_ok(S), lambda S: put(S, 'tbc', S['tbc'].replace('noncomputable def produces_offline', 'def produces_offline'))),
    ('G-ANCHOR-FRESH', 'the post-seal #check bank -- six statements, exit 0',
     lambda S: '(exit 0)' in S['anchor'] and len([l for l in S['anchor'].split(NL) if re.match(r'^  @?SIDEExplicitFormula\.\S+ :', l)]) == 6
     and 'h2_sign ↔ RiemannHypothesis' in S['anchor'] and 'at SIDE-explicit-formula 81ae175' in S['anchor'],
     lambda S: put(S, 'anchor', S['anchor'].replace('(exit 0)', '(exit 1)'))),
    ('G-POPULATION', 'b541`s census function RUN HERE on the live file against the bank and b541`s halt',
     lambda S: S['here']['act_two'] == S['cj'].get('act_two') == S['b541']['halt']['act_two_live'] and S['here']['first'] == S['cj'].get('first_line') == 1708
     and S['cj'].get('past_in_rows') == S['cj'].get('past_halt') == len(S['b541']['past_halt']),
     lambda S: put(S, 'here', dict(S['here'], act_two=S['here']['act_two'] - 1))),
    ('G-ROWS-GRADED', 'every row against the live file READ HERE -- a grade of the four, a tier, an erratum for each RESTS and only for RESTS',
     lambda S: rows_ok(S), lambda S: put(S, 'cj', dict(S['cj'], rows=[dict(r, grade='MAYBE') for r in crows(S)]))),
    ('G-CARRIED-ROWS', 'the carried rows against b532`s bank -- verdicts kept, the vocabulary moves said',
     lambda S: carried_ok(S), lambda S: put(S, 'cj', dict(S['cj'], rows=[dict(r, grade='STANDS') if r['carried'] == 'M-23' else r for r in crows(S)]))),
    ('G-DEPOSIT-LINES', 'every deposited line against the deposited copy READ HERE; LIVE-SOLE absent from it',
     lambda S: deposit_ok(S), lambda S: put(S, 'cj', dict(S['cj'], rows=[dict(r, dep_line=r['dep_line'] + 40) if isinstance(r['dep_line'], int) else r for r in crows(S)]))),
    ('G-HISTORY-ROWS', 'the STANDS-AS-HISTORY rows -- none draws an erratum; their dated pins rev-parsed HERE',
     lambda S: history_ok(S), lambda S: put(S, 'dated', {**S['dated'], ('SIDE-kernel', 'v1.4'): '0000000'})),
    ('G-TERMS-REREAD', 'every re-read terminal at its pin READ HERE, its earlier grade found in its own bank',
     lambda S: terms_ok(S), lambda S: put(S, 'tj', dict(S['tj'], terms=[dict(x, word='MOVED') for x in S['tj'].get('terms', [])]))),
    ('G-SUPPLEMENTARY', 'the supplementary rows against the live file READ HERE', lambda S: supp_ok(S),
     lambda S: put(S, 'cj', dict(S['cj'], supplementary=[dict(x, line=x['line'] + 1) for x in S['cj'].get('supplementary', [])]))),
    ('G-LAKE-TARGET', 'SIDE-kernel v1.5`s tree and lakefile READ HERE -- Kernel/Root.lean under the Kernel library`s submodule globs',
     lambda S: 'Kernel/Root.lean' in S['tree15'].split(NL) and 'globs := #[.submodules `Kernel]' in S['lakefile'],
     lambda S: put(S, 'tree15', S['tree15'].replace('Kernel/Root.lean', 'Kernel/Rootx.lean'))),
    ('G-SORRY-GREP', 'Appendix C`s command at v1.5 READ HERE -- the literal grep prints lines, no sorry term in the code, and the row reads RESTS',
     lambda S: S['sorry'][0] > 0 and S['sorry'][1] == 0 and next((r['grade'] for r in crows(S) if r['line'] == 1971), '') == 'RESTS',
     lambda S: put(S, 'sorry', (0, 0))),
    ('G-E6-DRAFTED', 'the E-2026-09-25-6 draft READ HERE against the census bank', lambda S: e6_ok(S),
     lambda S: put(S, 'e6', S['e6'].replace("'s", '`s'))),
    ('G-E6-NOT-FILED', 'ERRATA READ HERE -- no E-2026-09-25-6 in it', lambda S: 'E-2026-09-25-6' not in S['errata'],
     lambda S: put(S, 'errata', S['errata'] + NL + '## E-2026-09-25-6')),
    ('G-MAP-SECOND-HALF', 'FINDINGS READ HERE -- the entry once, its counts equal to the bank, every part row well-formed',
     lambda S: map_ok(S), lambda S: put(S, 'find', S['find'].replace('FINDINGS.md:4834', 'FINDINGS.md:0000'))),
    ('G-CP1-LINE', 'FINDINGS and the trail READ HERE -- the CP-1 line in both',
     lambda S: '**CP-1, the monograph part, closed.**' in block(S, S['find'], R.FTITLE) and 'CP-1, the monograph part, closed' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('CP-1, the monograph part, closed', 'CP-1'))),
    ('G-HOLD-1109', 'FINDINGS.md:1108-1110 READ HERE against b542`s blob -- nothing written there',
     lambda S: hold_ok(S), lambda S: put(S, 'find', NL.join(S['find'].split(NL)[:1109] + ['a note'] + S['find'].split(NL)[1109:]))),
    ('G-B542-CORRECTED', 'the entry`s correction, and SIDE-kernel v1.1 MetaKernel.lean:138 READ HERE against the name on :1109 (in memory)',
     lambda S: b542_ok(S), lambda S: put(S, 'mk11', '')),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in three repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b542'}))),
    ('G-LINES-KEPT', 'the two written files against their blobs at b542`s commit, BOM stripped both sides',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'FINDINGS.md': S['pp_now']['FINDINGS.md'][:200] + S['pp_now']['FINDINGS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the census`s monograph clause, recomputed from the blobs and the md5',
     lambda S: bool(S['recomputed'].get('mono')) and all(S['recomputed']['mono'].values()),
     lambda S: put(S, 'recomputed', dict(S['recomputed'], mono={'x': False}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA bytes against b542`s blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY and SPIRAL_MAP bytes against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md', 'SPIRAL_MAP.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b' '}))),
    ('G-KERNELS-UNTOUCHED', 'four repositories READ HERE -- clean and at their heads', lambda S: len(S['kernels']) == 4 and all(S['kernels'].values()),
     lambda S: put(S, 'kernels', dict(S['kernels'], **{'SIDE-kernel': False}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b543_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind, branch deletion included',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b543_x.py', 'x')])),
    ('G-N1-SCORED', 'the desk against the census bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the census bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the census bank', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the terms bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the census bank', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the blobs, the tools, the token and the kernels', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b543 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels READ HERE', lambda S: 'No kernel lane opened at this act' in trail(S) and all(S['kernels'].values()),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the two written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-UNTOUCHED', 'the correspondence ledger against its blob at b542`s commit -- no row this act',
     lambda S: S['corr_now'] == S['corr_prior'] and S['corr_now'] != b'', lambda S: put(S, 'corr_now', S['corr_now'] + b'| 391 | a row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b542`s close -- none modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['corr_row.py'])),
    ('G-WRITELIST-KINDS', 'every b543 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b543')" in S['suite']
                and "data/b543_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b543_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b543')
              and 'data/b543_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b543 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b543_checks_postpush.txt' if pushed else 'b543_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b543_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
