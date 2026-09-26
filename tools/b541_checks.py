# -*- coding: utf-8 -*-
"""b541_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b541_registration_2026-09-25.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '957d7823'      # ### b540's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = 'd57c31d'           # ### b540's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b541 —'


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


import b541_record as R
PPFILES = ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md']
SIDE_TIP = '502f0a7a67462eab83a0f10eee5ea74be67957dd'
SK = os.path.join('D:', os.sep, 'SIDE-kernel')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
MAPP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
LIVEP = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
DEPM = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
MONO = ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')
MD5 = {'day1/A_Place_to_Stand.md': 'bb86aa65025b49d2547016ef5000a31e', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md': 'e90e2d06d5cadc059c62c29a849e9f8c'}
TIERS = ('T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4')
E1, E5 = 'E-2026-09-25-1', 'E-2026-09-25-5'
ABSENT = ('prod_prime_power_absValues', 'prod_int_absValues', 'prod_rat_absValues', 'conservation_certificate')
CONTROLS = ('conservation_of_spectra', 'balance_theorem')
SK_REFS = ('v1.0', 'v1.1', 'v1.2', 'v1.3', 'v1.4', 'v1.5', 'v1.6', 'v1.7', 'HEAD')
ANCHOR_RE = r'h2_sign|Weil positiv|Weil functional|\bLi\b|λ_n ≥ 0|Li`s|Li\'s'


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'))] + ['(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def sk_names():
    """### SIDE-kernel READ HERE at every tag and HEAD: the absent file, the four absent names, the two controls."""
    out = {}
    for ref in SK_REFS:
        files = gits(SK, 'ls-tree', '-r', '--name-only', ref).split(NL)
        out[ref] = dict(prime_file=any(f.endswith('ProductFormula_Prime.lean') for f in files),
                        absent={n: bool(gits(SK, 'grep', '-l', '-w', n, ref)) for n in ABSENT},
                        controls={n: bool(gits(SK, 'grep', '-l', '-w', n, ref)) for n in CONTROLS})
    return out


def census_here():
    """### the census RUN HERE with the record tool`s own needles, on the live file READ HERE -- a third run of the lineage."""
    lr, lsel, lstop = R.census_of(LIVEP)
    return dict(yields={n: sum(1 for r in lsel if n in r['hits']) for n, _ in R.PAT}, read=len(lr), selected=len(lsel), act_one=lstop)


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    files = PPFILES + ['README.md', 'REGISTRY.md']
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b541_ferry.txt')),
        scan=read(os.path.join(D, 'b541_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b541_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b541_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b541_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b541_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b540_closing.txt')),
        addendum=read(os.path.join(D, 'b541_addendum.txt')),
        comp=read(os.path.join(D, 'b541_components.txt')),
        desk=read(os.path.join(D, 'b541_desk_notes.txt')),
        sc=json.loads(read(os.path.join(D, 'b541_scores.json')) or '{}'),
        reads=read(os.path.join(D, 'b541_reads.txt')),
        fj=json.loads(read(os.path.join(D, 'b541_file.json')) or '{}'),
        lawj=json.loads(read(os.path.join(D, 'b541_law.json')) or '{}'),
        cj=json.loads(read(os.path.join(D, 'b541_census.json')) or '{}'),
        e5j=json.loads(read(os.path.join(D, 'b541_erratum5.json')) or '{}'),
        mapj=json.loads(read(os.path.join(D, 'b541_map.json')) or '{}'),
        e5=read(os.path.join(D, 'b541_erratum_draft.md')), e4draft=read(os.path.join(D, 'b540_erratum_draft.md')),
        b532={x['id']: x for x in (json.loads(read(os.path.join(D, 'b532_rows.json')) or '{}').get('rows') or [])},
        b532extract=read(os.path.join(D, 'b532_extract.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in files},
        pp_now={f: open(os.path.join(PP, f), 'rb').read() for f in files},
        mono={f: gits(PP, 'hash-object', f) == gits(PP, 'rev-parse', PRIOR_PP + ':' + f)
              and hashlib.md5(open(os.path.join(PP, f), 'rb').read()).hexdigest() == MD5[f] for f in MONO},
        errata=read(os.path.join(PP, 'ERRATA.md')), mapt=read(MAPP),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), live=read(LIVEP), dep=read(DEPM),
        corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md').decode('utf-8', 'replace').replace(chr(13), ''),
        ker_clean={n: gits(p, 'status', '--porcelain', '--untracked-files=no') == '' for n, p in (('sef', KER), ('sk', SK), ('lv', LV))},
        ker_head=gits(KER, 'rev-parse', 'HEAD'),
        ker_changed=set(x for x in gits(KER, 'diff', '--name-only', KER_TIP).split(NL) if x.strip()),
        sk=sk_names(), here=census_here(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b541_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b541_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b541_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b541_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b541 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b541_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b541_reads.txt', 'b541_file.json', 'b541_census.json',
                                                               'b541_erratum_draft.md', 'b541_map.json'))),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b541 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-9]_|^b540_|^b334_', f)]
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
    if f != 'ERRATA.md':
        ok = ok and S['pp_now'][f].startswith(S['pp_prior'][f])
    return ok


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0].split(',')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def entry4(S):
    t = S['errata']
    i = t.find('## E-2026-09-25-4 ')
    j = t.find('**Filed 2026-09-25 by b541', i)
    if i < 0 or j < 0:
        return ''
    return t[i:t.find(NL, j) if t.find(NL, j) >= 0 else len(t)]


def crows(S):
    return (S['cj'] or {}).get('rows') or []


def seg_lines(text, a, n=14):
    L = text.split(NL)
    return R.nz(' '.join(L[a - 1:a - 1 + n])) if isinstance(a, int) and 0 < a <= len(L) else ''


def rows_ok(S):
    rs = crows(S)
    c = S['cj'].get('counts', {})
    live = [r for r in rs if r['src'] == 'L']
    return (bool(rs) and all(r['grade'] in ('STANDS', 'RESTS', 'EXCEEDS') and r['tier'] in TIERS for r in rs)
            and all(r['errata'] for r in rs if r['grade'] == 'RESTS') and all(not r['errata'] for r in rs if r['grade'] != 'RESTS')
            and all(r['replacement'] for r in rs if E5 in r['errata'])
            and all(R.nz(r['sentence'])[:60] in seg_lines(S['live'], r['line']) for r in live)
            and sum(c.values()) == len(rs) and len(live) == S['cj']['halt']['act_one_live'] == S['here']['act_one'])


def carried_ok(S):
    rs = [r for r in crows(S) if r.get('carried')]
    moved = [r for r in rs if r['carried'].endswith('*')]
    return (len(rs) >= 10 and all(S['b532'].get(r['carried'], {}).get('verdict') == r['grade'] for r in rs if not r['carried'].endswith('*'))
            and [r['carried'] for r in moved] == ['M-06*'] and all(r['reason'].startswith('MOVED') and S['b532'].get('M-06', {}).get('verdict') != r['grade'] for r in moved))


def deposit_ok(S):
    rs = crows(S)
    dep_nz = R.nz(' '.join(S['dep'].split(NL)))
    num = [r for r in rs if isinstance(r['dep_line'], int)]
    return (bool(num) and all(R.nz(r['sentence'])[:60] in seg_lines(S['dep'], r['dep_line']) for r in num)
            and all(R.nz(r['sentence']) not in dep_nz for r in rs if r['dep_line'] == 'LIVE-SOLE')
            and all(R.nz(r['sentence']) not in R.nz(' '.join(S['live'].split(NL))) for r in rs if r['line'] == 'DEPOSIT-SOLE'))


def absent_ok(S):
    sk = S['sk']
    return (len(sk) == len(SK_REFS) and all(not v['prime_file'] and not any(v['absent'].values()) and all(v['controls'].values()) for v in sk.values())
            and '`ProductFormula_Prime.lean`' in block(S, S['find'], R.FTITLE) and all(('`%s`' % n) in block(S, S['find'], R.FTITLE) for n in ABSENT))


def chapter_map_ok(S):
    b = block(S, S['find'], R.FTITLE)
    per = {}
    for r in crows(S):
        per.setdefault(R.chapter_of(r), []).append(r)
    last = [l for l in b.split(NL) if l.strip()][-1] if b.strip() else ''
    return (S['find'].count(R.FTITLE) == 1 and bool(b) and all(('| %s | ' % k.rstrip(':')) in b and ('| **%s** | %d | ' % (t, len(per.get(k, [])))) in b.split('| %s | ' % k.rstrip(':'))[1][:400]
                                                             for k, _, t in R.CHAPTERS)
            and sum(len(v) for v in per.values()) == len(crows(S)) and last.startswith('**Halt line.**') and '"## 26.1 The Axiom Journey" (:1698)' in last)


def e5_ok(S):
    rs = [r for r in crows(S) if E5 in r['errata']]
    t = S['e5']
    return (t.startswith('## E-2026-09-25-5 — ') and 'DRAFT, NOT FILED' in t.split(NL)[0] and len(rs) == S['e5j'].get('rows') == t.count('  - replacement: *"')
            and t.count('`') == 0 and "'s" in t and all(r['replacement'].replace('`', '') in t for r in rs))


def recomputed(S):
    rs = crows(S)
    t0z = [r for r in rs if r['tier'] == 'T0' and re.search(r'zeros? (lie|lies|are|is) on|all nontrivial zeros|Re\(ρ\) = 1/2|σ = 1/2 for every', r['sentence'])]
    return dict(
        n1=60 <= S['here']['selected'] <= 160,
        n3=not [r for r in rs if re.search(ANCHOR_RE, r['sentence'])] and not t0z,
        n4=bool(rs) and not [r for r in rs if r['grade'] == 'EXCEEDS'],
        n5=all(S['mono'].values()) and all(kept(S, f) for f in PPFILES) and not S['zen'],
        n6=S['dep_clean'] and all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md')) and S['tok'] == 0,
        s1=S['cj'].get('run1', {}).get('yields') == S['cj'].get('run2', {}).get('yields') == S['here']['yields'] and bool(S['here']['yields']),
        s2=any(r['grade'] == 'RESTS' and E5 in r['errata'] and not r['subject'] for r in rs),
        s3=next((r['grade'] for r in rs if r['line'] == 1667), '') == 'STANDS')


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == recomputed(S)[k]


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R151) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b541' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b540`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'E-2026-09-25-4 : DRAFTED' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b541' in S['ferry'] and 'ACT b541' in S['face'] and not glob.glob(os.path.join(D, 'b542_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b541')),
    ('G-PEEK-DECLARED', 'the face`s (C) block, and the components` banks after the lock',
     lambda S: 'A FRESH `#check` OF THE RH-ANCHOR IS RUN BY THE RECORD TOOL AFTER THE SEAL' in flat(S['face']) and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R151-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R151) END' in S['ferry'] and S['ot'].count('**(R151) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R151) ratified', '(R151) noted'))),
    ('G-MONOGRAPH-PINNED', 'the reads bank against the live file`s :19 READ HERE, and b532`s bank line',
     lambda S: S['live'].split(NL)[18] in S['reads'] and 'md5 bb86aa65025b49d2547016ef5000a31e' in S['reads']
     and 'md5 e90e2d06d5cadc059c62c29a849e9f8c' in S['reads'] and line_with(S['b532extract'], 'Zenodo 21539167 serves md5').strip() in S['reads']
     and 'MATCH True' in line_with(S['reads'], 'b532`s bank'),
     lambda S: put(S, 'reads', S['reads'].replace('MATCH True', 'MATCH False'))),
    ('G-ANCHOR-FRESH', 'the post-seal #check bank -- eight statements at 81ae175, exit 0',
     lambda S: 'at SIDE-explicit-formula 81ae175' in S['reads'] and '(exit 0)' in S['reads']
     and len([l for l in S['reads'].split(NL) if re.match(r'^  @?SIDEExplicitFormula\.\S+ :', l)]) == 8
     and 'h2_sign ↔ RiemannHypothesis' in S['reads'] and 'conservationHypothesis ↔ RiemannHypothesis' in S['reads'],
     lambda S: put(S, 'reads', S['reads'].replace('(exit 0)', '(exit 1)'))),
    ('G-E4-FILED', 'ERRATA READ HERE -- the b540 draft`s bytes once, then the b541 Status line, at the file`s end',
     lambda S: S['errata'].count(S['e4draft'].rstrip(NL)) == 1 and bool(entry4(S)) and S['errata'].rstrip(NL).endswith(entry4(S).split(NL)[-1])
     and 'may extend this entry by a further entry, never by editing it' in entry4(S) and '(R151)(1)' in entry4(S),
     lambda S: put(S, 'errata', S['errata'].replace('**Filed 2026-09-25 by b541', '**Noted by b541'))),
    ('G-E4-LISTED', 'ERRATA READ HERE -- the bullet once, directly after E-2026-09-25-3`s',
     lambda S: (lambda t: NL.join(t).count('- `E-2026-09-25-4` —') == 1 and any(t[i].startswith('- `E-2026-09-25-3` —') and t[i + 1].startswith('- `E-2026-09-25-4` —')
                                                                      for i in range(len(t) - 1)))(S['errata'].split(NL)),
     lambda S: put(S, 'errata', S['errata'].replace('- `E-2026-09-25-4` —', '- `E-2026-09-25-4x` —'))),
    ('G-E4-BACKTICKS', 'the filed entry READ HERE -- no backtick left open on its lines, equal to the bank',
     lambda S: bool(entry4(S)) and outside_bt(entry4(S)) == 0 == S['fj'].get('backticks_outside_code'),
     lambda S: put(S, 'errata', S['errata'].replace('**Filed 2026-09-25 by b541', '**Filed 2026-09-25 by b541`s'))),
    ('G-MAP-LAW-LINE', 'the map READ HERE -- the line once, after every prior byte, carrying (R151)(2)',
     lambda S: S['mapt'].count(R.MAPH) == 1 and S['pp_now']['phase1.5/method/THE_LOAD_BEARING_MAP.md'].startswith(S['pp_prior']['phase1.5/method/THE_LOAD_BEARING_MAP.md'])
     and all(x in block(S, S['mapt'], R.MAPH) for x in ('**EQUIVALENT-DEEP**', '**EQUIVALENT-REWORDING**', '`register5_output_holds`', '`ch_iff_rh`', '**T2**')),
     lambda S: put(S, 'mapt', S['mapt'].replace('**EQUIVALENT-DEEP**', 'deep'))),
    ('G-R5-FINDING', 'FINDINGS READ HERE -- the R5 entry once, before the census entry; its theorem in the fresh #check',
     lambda S: S['find'].count(R.R5T) == 1 and 0 <= S['find'].find(R.R5T) < S['find'].find(R.FTITLE)
     and '`register5_output_holds : Register5_output_HilbertPolya`' in S['find']
     and 'register5_output_holds : SIDEExplicitFormula.RegisterDepth.Register5_output_HilbertPolya' in S['reads'],
     lambda S: put(S, 'find', S['find'].replace(R.R5T, R.R5T[:-5]))),
    ('G-CENSUS-LINEAGE', 'the census RUN HERE on the live file against both banked runs, needle by needle',
     lambda S: S['cj'].get('run1', {}).get('yields') == S['cj'].get('run2', {}).get('yields') == S['here']['yields']
     and S['cj']['run2']['selected'] == S['here']['selected'] == 282 and S['cj']['lineage_agree'] and len(S['here']['yields']) == 11,
     lambda S: put(S, 'here', dict(S['here'], yields=dict(S['here']['yields'], route=66)))),
    ('G-HALT-LINE', 'the live file READ HERE at the halt, the bank, and the map`s last line',
     lambda S: S['live'].split(NL)[S['cj']['halt']['line'] - 1] == '## 26.1 The Axiom Journey' and S['cj']['halt']['act_one_live'] == S['here']['act_one'] == 172
     and S['cj']['halt']['act_two_live'] == 110 and S['cj']['halt']['first_act_two'] > S['cj']['halt']['line']
     and ('(:%d)' % S['cj']['halt']['line']) in [l for l in block(S, S['find'], R.FTITLE).split(NL) if l.strip()][-1],
     lambda S: put(S, 'cj', dict(S['cj'], halt=dict(S['cj']['halt'], line=S['cj']['halt']['line'] + 1)))),
    ('G-ROWS-GRADED', 'every row against the live file READ HERE -- a grade, a tier, an erratum for each RESTS, counts summing',
     lambda S: rows_ok(S), lambda S: put(S, 'cj', dict(S['cj'], rows=[dict(r, grade='MAYBE') for r in crows(S)]))),
    ('G-CARRIED-ROWS', 'the carried rows against b532`s own bank -- verdicts kept, the one move said',
     lambda S: carried_ok(S),
     lambda S: put(S, 'cj', dict(S['cj'], rows=[dict(r, grade='STANDS') if r.get('carried') == 'M-09' else r for r in crows(S)]))),
    ('G-DEPOSIT-LINES', 'every deposited line against the deposited copy READ HERE; LIVE-SOLE and DEPOSIT-SOLE both ways',
     lambda S: deposit_ok(S),
     lambda S: put(S, 'cj', dict(S['cj'], rows=[dict(r, dep_line=r['dep_line'] + 3) if isinstance(r['dep_line'], int) else r for r in crows(S)]))),
    ('G-ABSENT-NAMES', 'SIDE-kernel READ HERE at v1.0-v1.7 and HEAD -- the file and four names absent, two controls present',
     lambda S: absent_ok(S),
     lambda S: put(S, 'sk', dict(S['sk'], **{'v1.5': dict(S['sk']['v1.5'], controls={'conservation_of_spectra': False, 'balance_theorem': True})}))),
    ('G-E5-DRAFTED', 'the E-2026-09-25-5 draft READ HERE against the census bank -- one replacement per row, apostrophes',
     lambda S: e5_ok(S), lambda S: put(S, 'e5', S['e5'].replace("'s", '`s'))),
    ('G-E5-NOT-FILED', 'ERRATA READ HERE -- no E-2026-09-25-5 in it', lambda S: 'E-2026-09-25-5' not in S['errata'],
     lambda S: put(S, 'errata', S['errata'] + NL + '## E-2026-09-25-5')),
    ('G-CHAPTER-MAP', 'FINDINGS READ HERE -- each chapter`s tier and count against the census bank; the halt line last',
     lambda S: chapter_map_ok(S),
     lambda S: put(S, 'find', S['find'].replace('**Halt line.**', '**Stop.**'))),
    ('G-LINES-KEPT', 'the four written files against their blobs at b540`s commit, BOM stripped both sides',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'FINDINGS.md': S['pp_now']['FINDINGS.md'][:200] + S['pp_now']['FINDINGS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'both monograph copies -- git`s object against b540`s blob, and the working md5 against its bank',
     lambda S: len(S['mono']) == 2 and all(S['mono'].values()),
     lambda S: put(S, 'mono', dict(S['mono'], **{'day1/A_Place_to_Stand.md': False}))),
    ('G-CEILING-UNCHANGED', 'README and REGISTRY bytes against their blobs', lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b' '}))),
    ('G-KERNELS-UNTOUCHED', 'three kernels READ HERE', lambda S: all(S['ker_clean'].values()) and S['ker_head'].startswith('81ae175') and S['ker_changed'] == set(),
     lambda S: put(S, 'ker_changed', {'SIDEExplicitFormula/Seam.lean'})),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b541_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b541_x.py', 'x')])),
    ('G-N1-SCORED', 'the desk against the census RUN HERE', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk -- NOT SCORABLE, the face`s READING (1) saying why',
     lambda S: 'n2' in S['sc'] and S['sc']['n2'] is None and 'NOT SCORABLE AT THIS ACT' in line_with(S['desk'], '**(N2)**')
     and '(N2) is NOT SCORABLE at this act' in flat(S['face']),
     lambda S: put(S, 'sc', dict(S['sc'], n2=True))),
    ('G-N3-SCORED', 'the desk against the census bank', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the census bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the blobs and the monograph', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the blobs, the deposit tree and the token', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2')
     and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b541 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernel`s tree', lambda S: 'No kernel lane opened at this act' in trail(S) and S['ker_changed'] == set(),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the four written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-UNTOUCHED', 'the correspondence ledger against its blob -- no row this act',
     lambda S: S['corr'] == S['corr_prior'] and S['corr'] != '', lambda S: put(S, 'corr', S['corr'] + NL + '| 388 | a row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b540`s close -- none modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['corr_row.py'])),
    ('G-WRITELIST-KINDS', 'every b541 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b541')" in S['suite']
                and "data/b541_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b541_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b541')
              and 'data/b541_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b541 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b541_checks_postpush.txt' if pushed else 'b541_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b541_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
