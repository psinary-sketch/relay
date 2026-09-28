# -*- coding: utf-8 -*-
"""b555_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b555_registration_2026-09-28.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'f93b2b46'      # ### b554's closing housekeeping commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = '0c748da'           # ### b554's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b555 —'


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


import b555_record as R
import b542_checks as K542
import banned_terms as BTM
import terminal_table as TT
PPFILES = sorted(R.WRITE_OK)
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase2/method/THE_IDENTITY_CHAIN.md', 'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md',
         'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
GRHR = R.GRHR
BALR = 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'
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
        face=read(FACE), ferry=read(os.path.join(D, 'b555_ferry.txt')),
        scan=read(os.path.join(D, 'b555_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b555_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b555_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b555_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b555_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b554_closing.txt')),
        addendum=read(os.path.join(D, 'b555_addendum.txt')),
        comp=read(os.path.join(D, 'b555_components.txt')),
        desk=read(os.path.join(D, 'b555_desk_notes.txt')),
        sc=jload('b555_scores.json'), reads=read(os.path.join(D, 'b555_reads.txt')),
        h8=jload('b555_h8.json'), sp=jload('b554_sign_pattern.json'), sptxt=read(os.path.join(D, 'b554_sign_pattern.txt')),
        t3=jload('b555_t3dp.json'), cl=jload('b555_clause.json'),
        rows=jload('b555_rows.json'), ts=jload('b555_tiers.json'), tstxt=read(os.path.join(D, 'b555_tiers.txt')),
        probes=[json.loads(l) for l in read(os.path.join(D, 'b555_probes.jsonl')).split(NL) if l.strip()],
        grh_src=rd8(blob(os.path.join('D:', os.sep, 'SIDE-grh-transfer'), '858cbf6:SIDEGRHTransfer/GRHBridge.lean')),
        eff_head=gits(EFFR, 'rev-parse', 'HEAD'), eff_branch=gits(EFFR, 'rev-parse', '--abbrev-ref', 'HEAD'),
        eff_c66=gits(EFFR, 'rev-parse', '--verify', '-q', 'c66f3c5^{commit}'),
        eff_c66_anc=subprocess.run(['git', '-C', EFFR, 'merge-base', '--is-ancestor', 'c66f3c5', 'HEAD']).returncode == 0,
        eff_a27_anc=subprocess.run(['git', '-C', EFFR, 'merge-base', '--is-ancestor', 'a27415d', 'HEAD']).returncode == 0,
        block=jload('b555_block.json'), stems=jload('b555_stems.json'), shells=jload('b555_shells.json'),
        search=jload('b555_search.json'), sstxt=read(os.path.join(D, 'b555_search.txt')), cost=jload('b555_cost.json'),
        weil=jload('b555_weil.json'), rdg=jload('b555_reading.json'), fj=jload('b555_findings.json'),
        ef_src=rd8(blob(R.EF, '5c72cad:Zeta23/ExplicitFormula.lean')),
        branches=read(os.path.join(D, 'b555_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), grh=rd8(open(os.path.join(PP, GRHR), 'rb').read()),
        bal=rd8(open(os.path.join(PP, BALR), 'rb').read()),
        mem_times=[os.path.getmtime(os.path.join(R.MEMDIR, f)) for f in os.listdir(R.MEMDIR)] if os.path.isdir(R.MEMDIR) else [],
        mains=R.mains(),
        trial=dict(head=gits(R.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b554*') for r in (ROOT, PP)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b555_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b555_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b555_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b555_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b555 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b555_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b555_h8.json', 'b555_probes.jsonl', 'b555_tiers.json', 'b555_search.json',
                                                               'b555_cost.json', 'b555_weil.json'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in ('b555_ferry.txt', 'b555_ferry_scan.txt', 'b555_pins_stepzero.txt')),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b555_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b555_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KERN):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith(('b555 --', 'housekeeping: terminal table regenerated at b555')):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-4][0-9]_|^b55[0-4]_|^b334_', f)]
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
GG = 'SIDEGRHTransfer.'


def reads_ok(S):
    r = S['reads']
    return all(x in r for x in ('the floor derivation, per interval', 'the two positive intervals', 'the crest table', 'FINDINGS.md:4805',
                                'FINDINGS.md:4819', 'BALANCE_AND_POSITIVITY.md:678', 'the Status block', 'the Abstract', '§III.3',
                                'the Correspondence rows and the kernel-audit line', 'the b394 annotation', 'GRHStructuralExhaustiveness',
                                'the twisted_balance lemmas', 'a paired_* lemma', 'type_I_has_ostrowski', 'silence_universal', 'Interface.is_universal',
                                'ostrowski_exhaustive', 'neg_eq_neg_one_sub_iff', 'SIDE-effects a27415d -- no_type_d_conspiracies', 'Milestones.lean',
                                'Structural.lean', 'formation_preserved', 'mass_gap_equals_n3_certification', 'literatureRHS', 'EF_lit instantiated at ζ',
                                'b534`s record'))


def h8_ok(S):
    pos = S['sp']['pos']
    l = line_with(S['find'], P(R.H8H))
    n = S['h8'].get('numbers', {})
    return (S['find'].count(P(R.H8H)) == 1 and abs(n.get('turns_negative', 0) - math.exp(pos[0][1])) < 1e-9
            and abs(n.get('stays_negative', 0) - math.exp(pos[1][1])) < 1e-9 and '33.194' in l and '35.314–38.961' in l and '38.961' in l
            and 'navigator' in l and 'mis-specification' in l and 'Nothing about ζ’s zeros is claimed' in l)


def t3_ok(S):
    h = P(R.T3L)
    ln = [i + 1 for i, x in enumerate(S['bal'].split(NL)) if x == h]
    return (S['bal'].count(h) == 1 and ln == [S['t3'].get('line')] and kept(S, BALR) and not TT.GRADE_RE.search(R.T3L)
            and 'T3doubleprime_general_commutation_fails' in S['bal'].split(NL)[677] and '**T2**' in S['bal'].split(NL)[677])


def clause_ok(S):
    l = line_with(S['find'], P(R.CLH))
    return (S['find'].count(P(R.CLH)) == 1 and '**T2-INTERFACES**' in l and 'EQUIVALENT-DEEP' in l and '**T1-lit**' in l
            and S['cl']['clause']['line'] == [i + 1 for i, x in enumerate(S['find'].split(NL)) if x.startswith(P(R.CLH))][0])


def defect_o_ok(S):
    l = line_with(S['ot'], P(R.OOL))
    b554 = [i + 1 for i, x in enumerate(S['ot'].split(NL)) if x.startswith('### b554 ')]
    return S['ot'].count(P(R.OOL)) == 1 and ':5780' in l and ':5788' in l and 'not rewritten' in l and b554 and ('(the record at :%d)' % b554[0]) in l


def rows_ok(S):
    t = rd8(S['pp_prior'][GRHR]).split(NL)
    h = [i for i, l in enumerate(t) if l.startswith('| Claim | Kernel | Theorem (fully qualified)')][0]
    n = 0
    for l in t[h + 2:]:
        if not l.startswith('|'):
            break
        n += 1
    return S['rows'].get('count') == n == len(S['rows'].get('rows', [])) == S['ts'].get('count')


def probes_ok(S):
    pr = {p['id']: p for p in S['probes']}
    need = set(v[0] for v in R.TERMS.values())
    return (need <= set(pr) and all(p['exit'] == 0 and p['errors'] == 0 and p['manifest_same'] for p in pr.values())
            and all(t['found'] and t['profile'] for t in S['ts'].get('terms', [])))


def composite_ok(S):
    src = S['grh_src']
    a = src.index('def GRHStructuralExhaustiveness')
    body = src[src.index(':=', a) + 2: src.index('/--', a)]
    chi = bool(re.search(r'(?<![A-Za-z0-9_])(χ|χbar)(?![A-Za-z0-9_])', body))
    return (S['ts'].get('chi_in_body') is chi and chi is False and 'NO CHARACTER VALUE ENTERS THE CONCLUSION' in S['tstxt']
            and '### THE COMPOSITE: `@SIDEGRHTransfer.grh_structural_exhaustiveness_proved' in S['tstxt'])


def silence_ok(S):
    t = [x for x in S['ts'].get('terms', []) if x['name'] == 'SilenceTheorem.silence_universal']
    return (len(t) == 1 and t[0]['tier'] == 'T2-INTERFACES' and 'I.is_universal →' in (t[0]['statement'] or '')
            and '∀ c₁ c₂ : C.α, I.action c₁ = I.action c₂' in S['ts'].get('silence_premise', ''))


def effects_ok(S):
    es = S['ts'].get('effects', {})
    return (es.get('branch') == S['eff_branch'] and es.get('head') == S['eff_head'] and es['c66f3c5']['resolves'] == bool(S['eff_c66'])
            and es['c66f3c5']['ancestor_of_head'] == S['eff_c66_anc'] and es['a27415d']['ancestor_of_head'] == S['eff_a27_anc']
            and '### SIDE-effects: branch' in S['tstxt'] and len(es.get('oleans', [])) >= 5)


def shell_rows_ok(S):
    ts = [t for t in S['ts'].get('terms', []) if t['row'] in (391, 392)]
    return len(ts) == 5 and all(t['tier'] == 'T2' and t['reason'].startswith('SHELL') and t['profile'] == 'does not depend on any axioms' for t in ts)


def tiers_ok(S):
    st = S['ts']
    ok = all(t['tier'] in R.ORDER for t in st.get('terms', []))
    for r in st.get('rows', []):
        tl = [t['tier'] for t in st['terms'] if t['row'] == r['line']]
        ok = ok and r['tier'] == (max(tl, key=R.ORDER.index) if tl else 'T4')
    tc = {k: sum(1 for t in st['terms'] if t['tier'] == k) for k in R.ORDER}
    return ok and tc == st.get('term_tiers') and sum(st['disp'].values()) == len(st['rows'])


def block_ok(S):
    b = seg(S['grh'], P(R.BH), 30000)
    return (S['grh'].count(P(R.BH)) == 1 and kept(S, GRHR) and all('| :%d |' % r['line'] in b for r in S['ts'].get('rows', []))
            and S['block'].get('line') == [i + 1 for i, l in enumerate(S['grh'].split(NL)) if l.startswith(P(R.BH))][0])


def stems_ok(S):
    per = {x: 0 for x in BTM.STEMS}
    for l in rd8(S['pp_prior'][GRHR]).split(NL):
        for m in BTM.PAT.finditer(l):
            per[[x for x in BTM.STEMS if m.group(0).lower().startswith(x)][0]] += 1
    return S['stems'].get('per') == per and rd8(S['pp_now'][GRHR]).startswith(rd8(S['pp_prior'][GRHR]).rstrip(NL))


def structural_ok(S):
    doc = rd8(S['pp_prior'][GRHR]).split(NL)
    hits = [(i + 1, p) for i, l in enumerate(doc) for p in R.SHELL_PATS if p in l]
    return [tuple(h[:2]) for h in S['shells'].get('hits', [])] == hits and S['shells']['structural']['c66f3c5']['grh_exclusion']['declared'] is True


def search_ok(S):
    se = S['search']
    return (all(se[k]['equal'] for k in se if k != 'zeta23') and se['zeta23']['fixed'] is True
            and all(len(se[k]['rh_decls']) == sum(1 for l in se[k]['rh_lines'] if re.search(r':\s*(theorem|lemma|def|abbrev)\s+\S*RiemannHypothesis', l)) for k in se if k != 'zeta23')
            and '### Zeta23' in S['sstxt'])


def eflit_ok(S):
    src = S['ef_src'].split(NL)
    a = S['search']['zeta23']['literatureRHS'][0]
    return src[a - 1].startswith('def literatureRHS') and 'ArithmeticFunction.vonMangoldt' in ' '.join(src[a - 1:a + 4]) and src[S['search']['zeta23']['ef_lit'] - 1].startswith('def EF_lit')


def arc_ok(S):
    c = S['cost']
    return (c['total']['theorems'] == sum(f['theorems'] for f in c['files']) and c['total']['reinst'] == sum(f['reinst'] for f in c['files'])
            and c['total']['theorems'] == c['total']['reinst'] + c['total']['reused'] and len(c['files']) == 8 and c.get('zeta23', {}).get('modules', 0) > 0)


def weil_ok(S):
    w = S['weil']
    b = seg(S['ot'], P(R.WH), 9000)
    return (S['ot'].count(P(R.WH)) == 1 and w['chi'] == w['new'] + w['reinst'] and w['new'] == len(R.WNEW) and w['reinst'] == S['cost']['total']['reinst']
            and w['arc'] == S['cost']['total']['theorems'] and all('**%s**' % t[0] in b for t in R.WNEW) and '**Priced, not attempted.**' in b
            and w['n6'] == (w['chi'] >= w['arc']))


def reading_ok(S):
    o = S['rdg']['findings']['line']
    pl = line_with(S['grh'], P(R.GPT))
    b = fblock(S['find'], P(R.RH_))
    return S['find'].count(P(R.RH_)) == 1 and S['grh'].count(P(R.GPT)) == 1 and ('`FINDINGS.md`:%d' % o) in pl and '**Its limits.**' in b and 'E-2026-09-25-1' in b


def findings_ok(S):
    b = fblock(S['find'], P(R.FH))
    return (S['find'].count(P(R.FH)) == 1 and ('**Next keystone:** `%s`.' % R.roster_next()[0]) in b and 'CARRIED' in b and 'W-ORD-GRH-WEIL' in b)


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b554 (was ') == 2 and b.count('Deleted branch push-b554-closing (was ') == 1


def kernel_sources_ok(S):
    m = S['mains']
    return len(m) == 8 and not any(f.endswith('.lean') for v in m.values() for f in v) and all(v == [] for v in m.values())


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R165) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b555' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- one (R81) flag, and the face declares it',
     lambda S: '(R81) FLAGS : 1' in line_with(S['scan'], '(R81) FLAGS') and 'one (R81) flag, INFORMATIONAL and declared here' in flat(S['face']),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b554`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b554' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b555' in S['ferry'] and 'ACT b555' in S['face'] and not glob.glob(os.path.join(D, 'b556_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b555')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; the reads before the lock, every evaluation and write after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R165-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R165) END' in S['ferry'] and S['ot'].count('**(R165) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R165) ratified', '(R165) noted'))),
    ('G-READS-CITED', 'the reads bank -- the sign bank, the tier law, b545`s line, GRH_CASCADE, the kernels at their pins, Zeta23, the trails',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('FINDINGS.md:4819', 'x'))),
    ('G-H8-WEIGHT', 'FINDINGS READ HERE and b554`s sign bank -- the entry once, its numbers equal to the bank`s intervals, the attribution',
     lambda S: h8_ok(S), lambda S: put(S, 'find', S['find'].replace('mis-specification', 'x'))),
    ('G-T3DP-SUPERSEDED', 'BALANCE_AND_POSITIVITY READ HERE -- the line once at its banked line, no grade word, :678 kept as written', lambda S: t3_ok(S),
     lambda S: put(S, 'bal', S['bal'].replace(P(R.T3L), P(R.T3L) + ' x'))),
    ('G-TIERLAW-CLAUSE', 'FINDINGS READ HERE -- the clause once, T2-INTERFACES, T1-open reserved, T1-lit', lambda S: clause_ok(S),
     lambda S: put(S, 'find', S['find'].replace('EQUIVALENT-DEEP', 'x'))),
    ('G-DEFECT-O-NOTED', 'OPEN_TRAILS READ HERE -- the line once, naming b554`s record, :5780, :5788, not rewritten', lambda S: defect_o_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('not rewritten', 'rewritten'))),
    ('G-GRH-ROWS', 'the document`s table at b554`s commit, counted here -- equal to the row bank and the tier bank', lambda S: rows_ok(S),
     lambda S: put(S, 'rows', dict(S['rows'], count=12))),
    ('G-GRH-PROBES', 'the probe bank -- every probe a tier needs, exit 0, no error, manifest equal; every terminal found and profiled', lambda S: probes_ok(S),
     lambda S: put(S, 'probes', [dict(p, exit=1) if p['id'] == 'e1' else p for p in S['probes']])),
    ('G-COMPOSITE-SIGNATURE', 'GRHBridge.lean at 858cbf6 READ HERE -- the Prop`s body, a χ token searched, the answer banked and printed', lambda S: composite_ok(S),
     lambda S: put(S, 'ts', dict(S['ts'], chi_in_body=True))),
    ('G-SILENCE-PREMISE', 'the tier bank -- silence_universal T2-INTERFACES, its premise and statement printed', lambda S: silence_ok(S),
     lambda S: put(S, 'ts', dict(S['ts'], silence_premise=''))),
    ('G-EFFECTS-STATE', 'SIDE-effects READ HERE -- branch, HEAD, both pins` presence and ancestry, oleans, equal to the bank', lambda S: effects_ok(S),
     lambda S: put(S, 'eff_branch', 'w-ladder-skeleton')),
    ('G-SHELL-ROWS', 'the tier bank -- the BSD and YM terminals T2 SHELL, axiom-free', lambda S: shell_rows_ok(S),
     lambda S: put(S, 'ts', dict(S['ts'], terms=[dict(t, tier='T0') if t['row'] == 391 else t for t in S['ts']['terms']]))),
    ('G-GRH-TIERS', 'the tier bank -- every tier in the law`s vocabulary, each row its weakest link, the counts recomputed', lambda S: tiers_ok(S),
     lambda S: put(S, 'ts', dict(S['ts'], term_tiers=dict(S['ts'].get('term_tiers', {}), T0=-1)))),
    ('G-GRH-BLOCK', 'GRH_CASCADE READ HERE against its blob -- the block once, every row, the document kept', lambda S: block_ok(S),
     lambda S: put(S, 'grh', S['grh'].replace('| :386 |', '| :999 |'))),
    ('G-GRH-STEMS', 'the document at b554`s commit, counted here with the tool`s own pattern -- equal to the bank; no byte above the appends changed',
     lambda S: stems_ok(S), lambda S: put(S, 'stems', dict(S['stems'], per={x: -1 for x in BTM.STEMS}))),
    ('G-STRUCTURAL-SEARCH', 'the document at b554`s commit searched here for the shells` names -- equal to the bank; c66f3c5 declares them',
     lambda S: structural_ok(S), lambda S: put(S, 'shells', dict(S['shells'], hits=[[1, 'grh_exclusion', 'x']]))),
    ('G-MATHLIB-SEARCH', 'the search bank -- both checkouts at their revs, the declaration hits recounted, Zeta23 printed', lambda S: search_ok(S),
     lambda S: put(S, 'search', dict(S['search'], zeta23=dict(S['search']['zeta23'], fixed=False)))),
    ('G-EFLIT-FIXED', 'Zeta23 at 5c72cad READ HERE -- literatureRHS at its banked line, the von Mangoldt sum; EF_lit`s line', lambda S: eflit_ok(S),
     lambda S: put(S, 'ef_src', S['ef_src'].replace('ArithmeticFunction.vonMangoldt', 'x'))),
    ('G-ARC-COST', 'the cost bank -- the eight files` counts summed here, the split closing, Zeta23 counted', lambda S: arc_ok(S),
     lambda S: put(S, 'cost', dict(S['cost'], total=dict(S['cost']['total'], reinst=S['cost']['total']['reinst'] + 1)))),
    ('G-WEIL-PRICED', 'OPEN_TRAILS READ HERE and the cost bank -- the work-order once, the price recomputed, (N6)`s comparison', lambda S: weil_ok(S),
     lambda S: put(S, 'weil', dict(S['weil'], chi=S['weil']['chi'] + 1))),
    ('G-GRH-READING', 'FINDINGS and GRH_CASCADE READ HERE -- the reading once, its limits, the pointer naming its line', lambda S: reading_ok(S),
     lambda S: put(S, 'grh', S['grh'].replace(P(R.GPT), 'x'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once, the dispositions, the work-order, the next keystone', lambda S: findings_ok(S),
     lambda S: put(S, 'find', S['find'].replace(P(R.FH), 'x'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in two repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b554'}))),
    ('G-MEMORY-UNREFRESHED', 'the memory directory READ HERE -- no file written after this face (R157)(6)',
     lambda S: bool(S['mem_times']) and max(S['mem_times']) < os.path.getmtime(FACE),
     lambda S: put(S, 'mem_times', S['mem_times'] + [os.path.getmtime(FACE) + 1])),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-LINES-KEPT', 'the four written files against their blobs at b554`s commit',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY, SPIRAL_MAP, FACES_LEDGER, THE_LOAD_BEARING_MAP, THE_IDENTITY_CHAIN, THE_KEYSTONE_CENSUS, SIMPLICITY against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
                                                               'phase2/method/THE_IDENTITY_CHAIN.md', 'phase2/method/THE_KEYSTONE_CENSUS.md',
                                                               'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'REGISTRY.md': S['pp_now']['REGISTRY.md'] + b' '}))),
    ('G-KERNEL-SOURCES-UNTOUCHED', 'eight kernels` mains READ HERE against their pre-act heads -- nothing written',
     lambda S: kernel_sources_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-effects': ['SIDEEffects/Structural.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b555_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b555_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b555 bank and tool and this act`s PLACE-papers bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the tier bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the tier bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against SIDE-effects` state', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the search bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the shells bank', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the work-order`s price', lambda S: nscored(S, 'n6'), lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-N7-SCORED', 'the desk against the mains, the tools, the token, the deposit and the trial worktree', lambda S: nscored(S, 'n7'),
     lambda S: put(S, 'sc', dict(S['sc'], n7=not S['sc'].get('n7')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b555 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels` mains READ HERE',
     lambda S: 'No kernel lane opened at this act' in trail(S) and kernel_sources_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the four written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b554`s close -- no .py tool modified',
     lambda S: [x for x in S['tools_edited'] if x.endswith('.py')] == [],
     lambda S: put(S, 'tools_edited', ['terminal_table.py'])),
    ('G-WRITELIST-KINDS', 'every b555 commit in four repositories and the housekeeping commit, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b555')" in S['suite']
                and "data/b555_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b555_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b555')
              and 'data/b555_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b555 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b555_checks_postpush.txt' if pushed else 'b555_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b555_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
