# -*- coding: utf-8 -*-
"""b554_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b554_registration_2026-09-28.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'ed2185c0'      # ### b553's closing housekeeping commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = 'e1478b6'           # ### b553's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b554 —'


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


import b554_record as R
import b542_checks as K542
import banned_terms as BTM
import terminal_table as TT
PPFILES = sorted(R.WRITE_OK)
OTHER = ['README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase2/method/THE_IDENTITY_CHAIN.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
SIMPR = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md'
GSR = os.path.join('D:', os.sep, 'SIDE-global-section')
KERN = os.path.join('D:', os.sep, 'SIDE-kernel')
TOOL_SUBJ = ["b554 -- tools/terminal_table.py: THE SYNONYM MAP, under the author's ruling (R164)(2)(a)",
             "b554 -- tools/terminal_table.py: THE TRAIL-LINE SUPERSESSION FORM, under the author's ruling (R164)(2)(b)"]
R5K, R5HK = R.R5, R.R5H


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'), ('worktree', ' remove'))] + [
        '(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def jload(n):
    return json.loads(read(os.path.join(D, n)) or '{}')


def grades_live():
    t = json.loads(read(os.path.join(D, 'terminal_table.json')) or '{}')
    rows = t.get('rows', t) if isinstance(t, dict) else t
    return {'%s|%s' % (r['repo'], r['name']): r['grade'] for r in rows if isinstance(r, dict) and 'name' in r}


def tool_commit(subj):
    c = [l.split()[0] for l in gits(ROOT, 'log', '--format=%H %s', '-60').split(NL) if l.split(' ', 1)[-1] == subj]
    if len(c) != 1:
        return dict(n=len(c), files=[], msg='', sha='')
    return dict(n=1, sha=c[0], files=sorted(x for x in gits(ROOT, 'show', '--name-only', '--pretty=format:', c[0]).split(NL) if x.strip()),
                msg=gits(ROOT, 'log', '-1', '--format=%B', c[0]))


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    tc = [tool_commit(s) for s in TOOL_SUBJ]
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b554_ferry.txt')),
        scan=read(os.path.join(D, 'b554_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b554_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b554_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b554_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b554_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b553_closing.txt')),
        addendum=read(os.path.join(D, 'b554_addendum.txt')),
        comp=read(os.path.join(D, 'b554_components.txt')),
        desk=read(os.path.join(D, 'b554_desk_notes.txt')),
        sc=jload('b554_scores.json'), reads=read(os.path.join(D, 'b554_reads.txt')),
        bd2=jload('b554_bd2.json'), bd2txt=read(os.path.join(D, 'b554_bd2.txt')),
        pp_bd2=gits(PP, 'rev-parse', '--verify', '-q', 'bd2ae1a^{commit}'), err=jload('b554_erratum.json'),
        before=jload('b554_table_before.json'), mid=jload('b554_table_mid.json'), syn=jload('b554_synonym.json'),
        tsn=jload('b554_trailsup_noop.json'), tsu=jload('b554_trailsup.json'), live=grades_live(),
        tc=tc, diff1=(git(ROOT, 'diff', PRIOR_RELAY, tc[0]['sha'], '--', 'tools/terminal_table.py') if tc[0]['sha'] else ''),
        diff2=(git(ROOT, 'diff', tc[0]['sha'], tc[1]['sha'], '--', 'tools/terminal_table.py') if tc[0]['sha'] and tc[1]['sha'] else ''),
        tool_src=read(os.path.join(T, 'terminal_table.py')),
        readme=read(os.path.join(T, 'corr_row.README.md')), readme_prior=rd8(blob(ROOT, PRIOR_RELAY + ':tools/corr_row.README.md')),
        supline=jload('b554_supline.json'), r1=jload('b554_reading_one.json'), pf553=read(os.path.join(D, 'b553_period_fine.txt')),
        sp=jload('b554_sign_pattern.json'), sptxt=read(os.path.join(D, 'b554_sign_pattern.txt')),
        sweep={int(r['a']): r for r in jsonl(os.path.join(D, 'b548_sweep_q.jsonl')) if r['p'] == 7},
        inter={int(r['a']): r for r in jsonl(os.path.join(D, 'b548_interference.jsonl'))},
        pr=jload('b554_prices.json'), prtxt=read(os.path.join(D, 'b554_prices.txt')),
        srows=jload('b554_simp_rows.json'), st=jload('b554_simp_tiers.json'), sttxt=read(os.path.join(D, 'b554_simp_tiers.txt')),
        probes=[json.loads(l) for l in read(os.path.join(D, 'b554_probes.jsonl')).split(NL) if l.strip()],
        kdtxt=read(os.path.join(D, 'b554_probe_kd.txt')), wttxt=read(os.path.join(D, 'b554_worktree.txt')),
        wt_exists=os.path.exists('D:/wt-b554-deriv'), wt_list=git(KERN, 'worktree', 'list', '--porcelain'),
        sblock=jload('b554_simp_block.json'), sread=jload('b554_simp_reading.json'), stems=jload('b554_stems.json'),
        simp_prior_text=rd8(blob(PP, PRIOR_PP + ':' + SIMPR)),
        fj=jload('b554_findings.json'),
        ker_head=gits(KERN, 'rev-parse', 'HEAD'),
        branches=read(os.path.join(D, 'b554_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), simp=read(os.path.join(PP, SIMPR)), errata=read(os.path.join(PP, 'ERRATA.md')),
        docs={f: read(os.path.join(PP, f)) for f in ('phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md',
                                                     'phase2/method/THE_KEYSTONE_CENSUS.md')},
        mem_times=[os.path.getmtime(os.path.join(R.MEMDIR, f)) for f in os.listdir(R.MEMDIR)] if os.path.isdir(R.MEMDIR) else [],
        mains=R.mains(),
        trial=dict(head=gits(R.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b553*') for r in (ROOT, PP, GSR)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b554_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b554_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b554_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b554_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b554 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b554_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b554_bd2.json', 'b554_table_before.json', 'b554_synonym.json', 'b554_sign_pattern.json',
                                                               'b554_prices.json', 'b554_probes.jsonl', 'b554_simp_tiers.json', 'b554_worktree.txt'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in ('b554_ferry.txt', 'b554_ferry_scan.txt', 'b554_pins_stepzero.txt')),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b554_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b554_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KERN):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith(('b554 --', 'housekeeping: terminal table regenerated at b554')):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-4][0-9]_|^b55[0-3]_|^b334_', f)]
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
DOCS = {'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md': ('line at :420', 'PATHS_TO_THE_CRITICAL_LINE.md'),
        'phase1.5/proofs/THE_RESIDUE_OF_RH.md': ('era table row at :145', 'THE_RESIDUE_OF_RH.md'),
        'phase2/method/THE_KEYSTONE_CENSUS.md': ('pin ancestry of §1, at :48', 'THE_KEYSTONE_CENSUS.md')}


def reads_ok(S):
    r = S['reads']
    return all(x in r for x in ('THE_H2_PROGRAMME_CHARTER.md:116', 'PATHS_TO_THE_CRITICAL_LINE.md:420', 'the era table row on bd2ae1a',
                                '§1 -- the pin ancestry', 'the v0.2 section', 'its last entry (format)', 'BEFORE THE EDITS: the grade parser',
                                'the supersede rule', 'OPEN_TRAILS.md:11042', 'OPEN_TRAILS.md:11290', 'b553_period_fine.txt', 'b548_interference.txt',
                                'zeroSide_eventually_neg', 'SIMPLICITY -- the Abstract', 'read entire'))


def bd2_ok(S):
    b = S['bd2']
    return (b.get('hash', '').startswith('bd2ae1a60a74') and S['pp_bd2'].startswith('bd2ae1a60a74') and b.get('date', '').startswith('2026-07-25')
            and 'hash    : bd2ae1a60a74' in S['bd2txt'] and b.get('ancestor') is True and b.get('paths420') is True)


def erratum_ok(S):
    e = S['err'].get('erratum', {})
    ln = [i + 1 for i, l in enumerate(S['errata'].split(NL)) if l.startswith(P(R.EH))]
    return S['errata'].count(P(R.EH)) == 1 and kept(S, 'ERRATA.md') and ln == [e.get('line')] and 'NO DEPOSITED ARTIFACT IS AFFECTED' in P(R.EH)


def bd2_lines_ok(S):
    e = S['err'].get('erratum', {}).get('line')
    ok = True
    for f, (what, key) in DOCS.items():
        h = P(R.BDL % what)
        t = S['docs'][f]
        l = line_with(t, h)
        ok = ok and t.count(h) == 1 and 'E-2026-09-27-1' in l and ('`ERRATA.md`:%d' % e) in l and kept(S, f)
        ok = ok and S['err']['lines'][key]['line'] == [i + 1 for i, x in enumerate(t.split(NL)) if x.startswith(h)][0]
    return ok


def added_removed(d):
    rem = [l for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    add = [l for l in d.split(NL) if l.startswith('+') and not l.startswith('+++')]
    return add, rem


def syn_edit_ok(S):
    add, rem = added_removed(S['diff1'])
    return (len(rem) == 2 and any("('CONFLICT' if len(distinct) > 1 else 'UNGRADED')" in l for l in rem)
            and any('conflict=(sorted(distinct) if len(distinct) > 1 else None)' in l for l in rem)
            and any(l.startswith('+SYNONYMS = ') for l in add) and any('def synonym(grade):' in l for l in add)
            and any('mapped = sorted(set(synonym(' in l for l in add) and S['tc'][0]['files'] == ['tools/terminal_table.py'])


def syn_test_ok(S):
    s = S['syn']
    return (s.get('changed') == {R5K: ['CONFLICT', 'ENCODES']} and len(s.get('conflicts_before', [])) == 14 and len(s.get('conflicts_after', [])) == 13
            and s.get('gone') == [] and s.get('rows') == 1229 and len(S['before'].get('grades', {})) == 1229)


def tsup_edit_ok(S):
    add, rem = added_removed(S['diff2'])
    return (rem == ['-            uniq = supersede(uniq)'] and any('def supersede_trail(cells, name):' in l for l in add)
            and any('uniq = supersede_trail(supersede(uniq), n)' in l for l in add) and S['tc'][1]['files'] == ['tools/terminal_table.py'])


def tsup_test_ok(S):
    return (S['tsn'].get('changed') == {} and S['tsu'].get('changed') == {R5HK: ['CONFLICT', 'DERIVES']}
            and len(S['tsn'].get('conflicts_after', [])) == 13 and len(S['tsu'].get('conflicts_after', [])) == 12)


def tsup_line_ok(S):
    h = P(R.SUPLINE)
    ln = [i + 1 for i, l in enumerate(S['ot'].split(NL)) if l == h]
    return (S['ot'].count(h) == 1 and not TT.GRADE_RE.search(R.SUPLINE) and ln == [S['supline'].get('line')]
            and S['live'].get(R5HK) == 'DERIVES' and S['live'].get(R5K) == 'ENCODES')


def readme_ok(S):
    return (S['readme'].startswith(S['readme_prior'].rstrip(NL)) and all(P(r) in S['readme'] for r in R.RDM)
            and len([l for l in S['readme'].split(NL) if l.strip()]) == len([l for l in S['readme_prior'].split(NL) if l.strip()]) + 2)


def commits_ok(S):
    a, b = S['tc']
    return (a['n'] == 1 and b['n'] == 1 and a['files'] == ['tools/terminal_table.py'] and b['files'] == ['tools/terminal_table.py']
            and 'THE TEST' in a['msg'] and 'CONFLICT 14 -> CONFLICT 13' in a['msg'] and 'THE TEST' in b['msg'] and 'CONFLICT 13 -> CONFLICT 12' in b['msg'])


def reading_one_ok(S):
    l = line_with(S['find'], P(R.R1H))
    pf = S['pf553'].split(NL)
    c = S['r1'].get('cites', {})
    return (S['find'].count(P(R.R1H)) == 1 and 'navigator' in l and ('`:%d' % c.get('pair', -1)) in l.replace('.txt`:', '`:')
            and pf[c['pair'] - 1].startswith('### the pair orbit') and pf[c['crest'] - 1].startswith('### the crest orbit')
            and 'mean spacing' in pf[c['mean'] - 1] and 'full periods' in pf[c['periods'] - 1] and 'Nothing about ζ’s zeros is claimed' in l)


def sign_control_ok(S):
    nodes = S['sp'].get('nodes', {})
    ok = len(nodes) == 31
    for a in range(30, 61):
        n = nodes.get(str(a)) or nodes.get(a)
        ok = ok and n is not None and abs(n['Z'] - S['sweep'][a]['Z']) == 0 and abs(n['OFF'] + n['ON'] - n['Z']) < 1e-9
        ok = ok and abs(n['pair'] - S['sweep'][a]['pair']) < 1e-9
        if a in S['inter']:
            ok = ok and abs(n['ON'] - sum(t[2] for t in S['inter'][a]['terms'] if t[0] == 'on')) < 1e-9
    return ok


def sign_floor_ok(S):
    nodes = {int(k): v for k, v in S['sp'].get('nodes', {}).items()}
    A = sorted(nodes)
    X = [math.log(a) for a in A]
    def dd2(i):
        return 2.0 * ((nodes[A[i + 1]]['ON'] - nodes[A[i]]['ON']) / (X[i + 1] - X[i]) - (nodes[A[i]]['ON'] - nodes[A[i - 1]]['ON']) / (X[i] - X[i - 1])) / (X[i + 1] - X[i - 1])
    FL = S['sp'].get('floor', [])
    ok = len(FL) == len(A) - 1 and len(A) == 31
    for i, f in enumerate(FL):
        M = max(abs(dd2(j)) for j in (i, i + 1) if 1 <= j <= len(A) - 2)
        h = X[i + 1] - X[i]
        want = max(S['sweep'][A[i]]['B'], S['sweep'][A[i + 1]]['B']) + h * h / 8.0 * M
        ok = ok and abs(f['floor'] - want) <= 1e-12 * max(1.0, want)
    return ok


def sign_intervals_ok(S):
    sp = S['sp']
    runs = sp.get('runs', [])
    ok = bool(runs) and abs(runs[0][1] - math.log(30.0)) < 1e-12 and abs(runs[-1][2] - math.log(60.0)) < 1e-12
    ok = ok and all(abs(runs[i][2] - runs[i + 1][1]) < 1e-15 and runs[i][0] != runs[i + 1][0] for i in range(len(runs) - 1))
    nodes = {int(k): v for k, v in sp.get('nodes', {}).items()}
    FL = sp.get('floor', [])
    for a in range(30, 61):
        x = math.log(a)
        f = min(fl['floor'] for fl in FL if fl['a0'] == a or fl['a1'] == a)
        z = nodes[a]['Z']
        st = 'POS' if z > f else ('NEG' if z < -f else 'UND')
        inside = [r[0] for r in runs if r[1] - 1e-9 <= x <= r[2] + 1e-9]
        ok = ok and st in inside
    ok = ok and [tuple(p) for p in sp.get('pos', [])] == [(r[1], r[2]) for r in runs if r[0] == 'POS']
    return ok


def h8_ok(S):
    sp = S['sp']
    pos = sp.get('pos', [])
    l36, l38 = math.log(36.0), math.log(38.0)
    h81 = len(pos) == 1
    ref1 = len(pos) >= 2
    ref2 = not any(a <= l36 and b >= l38 for a, b in pos)
    return (sp.get('h81') == h81 and sp.get('ref1') == ref1 and sp.get('ref2') == ref2 and sp.get('refuted') == (ref1 or ref2 or not h81)
            and ('### H8 IS %s' % ('REFUTED' if sp['refuted'] else 'NOT REFUTED')) in S['sptxt'])


def crests_ok(S):
    cs = S['sp'].get('crests', [])
    return (len(cs) >= 1 and all(c['a'] >= 38.0 and c['pair'] < 0 and abs(c['crest'] + c['pair'] + c['others'] + c['on'] - c['Q']) < 1e-9 for c in cs)
            and 'THE 29.551761 CRESTS AT a >= 38' in S['sptxt'])


def detection_ok(S):
    b = seg(S['ot'], P(R.DRH), 9000)
    cs = sum(1 for r in R.CF_ROUTE if r[3].startswith('of substance'))
    ps = sum(1 for r in R.PL_ROUTE if r[3].startswith('of substance'))
    want = 'PowerLimit' if ps < cs else ('closed-form' if cs < ps else S['pr'].get('cheaper'))
    return (S['ot'].count(P(R.DRH)) == 1 and '**Priced, not attempted.**' in b and all('**%s**' % r[0] in b for r in R.CF_ROUTE + R.PL_ROUTE)
            and S['pr'].get('cheaper') == want and ('**The %s route is the cheaper**' % want) in b and S['pr'].get('n4') == (want == 'closed-form'))


def hazard_ok(S):
    h = P(R.PHZ)
    ln = [i + 1 for i, l in enumerate(S['ot'].split(NL)) if l == h]
    return S['ot'].count(h) == 1 and ':11290' in h and ln == [S['pr']['hazard']['line']]


def anomaly_ok(S):
    l = [x for x in S['ot'].split(NL) if R.ANL_M in x]
    kh = S['ker_head'][:7]
    return (len(l) == 1 and all(t in l[0] for t in (kh, '`v1.7` = `2957e7d`', '`v1.5` = `0e5233f`', 'CP-5', 'Nothing is decided here'))
            and S['pr']['anomaly']['line'] == [i + 1 for i, x in enumerate(S['ot'].split(NL)) if R.ANL_M in x][0])


def simp_rows_ok(S):
    t = S['simp_prior_text'].split(NL)
    h = [i for i, l in enumerate(t) if l.startswith('| Claim (as stated here) |')][0]
    n = 0
    for l in t[h + 2:]:
        if not l.startswith('|'):
            break
        n += 1
    return S['srows'].get('count') == n == len(S['srows'].get('rows', [])) and S['st'].get('count') == n


def probes_ok(S):
    pr = {p['id']: p for p in S['probes']}
    need = set(v[0] for v in R.TERMS.values()) | set(v[1] for v in R.TERMS.values() if v[1])
    return (bool(pr) and need <= set(pr) and all(p['exit'] == 0 and p['errors'] == 0 and p['manifest_same'] for p in pr.values())
            and all(t['found'] and t['profile'] for t in S['st'].get('terms', [])))


def branch_probe_ok(S):
    kd = [p for p in S['probes'] if p['id'] == 'kd']
    br = [t for t in S['st'].get('terms', []) if t['branch']]
    return (len(kd) == 1 and kd[0]['exit'] == 0 and kd[0]['worktree'] == 'D:/wt-b554-deriv' and 'rev-parse HEAD = 27a3ae7b2f49' in S['kdtxt']
            and len(br) == 3 and all(t['profile'] == t['row_profile'] for t in br))


def worktree_ok(S):
    return (('git worktree ' + 'remove D:/wt-b554-deriv : exit 0') in S['wttxt'] and '### after: path ABSENT' in S['wttxt'] and not S['wt_exists']
            and 'wt-b554-deriv' not in S['wt_list'])


def tiers_ok(S):
    st = S['st']
    order = R.ORDER
    ok = all(t['tier'] in order for t in st.get('terms', []))
    for r in st.get('rows', []):
        ts = [t['tier'] for t in st['terms'] if t['row'] == r['line']]
        ok = ok and r['tier'] == (max(ts, key=order.index) if ts else 'T4') and ((not r['names']) == (r['tier'] == 'T4' and not ts))
    tc = {k: sum(1 for t in st['terms'] if t['tier'] == k) for k in order}
    return ok and tc == st.get('term_tiers') and sum(st['disp'].values()) == len(st['rows'])


def block_ok(S):
    b = seg(S['simp'], P(R.SBH), 30000)
    return (S['simp'].count(P(R.SBH)) == 1 and kept(S, SIMPR) and all('| :%d |' % r['line'] in b for r in S['st'].get('rows', []))
            and S['sblock'].get('line') == [i + 1 for i, l in enumerate(S['simp'].split(NL)) if l.startswith(P(R.SBH))][0])


def conclusions_ok(S):
    st = S['st']
    carries = [t['name'] for t in st.get('terms', []) if 'RiemannHypothesis' in (t['statement'] or '')]
    return carries == [] and st.get('carries') == [] and all(('    :%d ' % r['line']) in S['sttxt'] for r in st.get('rows', []))


def sreading_ok(S):
    o = S['sread'].get('findings', {}).get('line')
    pl = line_with(S['simp'], P(R.SPT))
    return S['find'].count(P(R.RH_)) == 1 and S['simp'].count(P(R.SPT)) == 1 and ('`FINDINGS.md`:%d' % o) in pl and 'CP-7' in fblock(S['find'], P(R.RH_))


def stems_ok(S):
    per = {s: 0 for s in BTM.STEMS}
    for l in S['simp_prior_text'].split(NL):
        for m in BTM.PAT.finditer(l):
            per[[s for s in BTM.STEMS if m.group(0).lower().startswith(s)][0]] += 1
    return S['stems'].get('per') == per and rd8(S['pp_now'][SIMPR]).startswith(S['simp_prior_text'].rstrip(NL))


def findings_ok(S):
    b = fblock(S['find'], P(R.FH))
    return (S['find'].count(P(R.FH)) == 1 and ('**Next keystone:** `%s`.' % R.roster_next()[0]) in b
            and ('**H8 %s**' % ('REFUTED' if S['sp']['refuted'] else 'NOT REFUTED')) in b and 'E-2026-09-27-1' in b and 'CARRIED' in b)


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


BRANCH_NAMES = [('relay', 'push-b553'), ('relay', 'push-b553-closing'), ('PLACE-papers', 'push-b553'), ('SIDE-global-section', 'push-b553')]


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b553 (was ') == 3 and b.count('Deleted branch push-b553-closing (was ') == 1


def kernel_sources_ok(S):
    m = S['mains']
    return len(m) == 6 and not any(f.endswith('.lean') for v in m.values() for f in v) and all(v == [] for v in m.values())


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R164) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b554' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b553`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b553' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b554' in S['ferry'] and 'ACT b554' in S['face'] and not glob.glob(os.path.join(D, 'b555_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b554')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; the reads before the lock, every evaluation and write after it',
     lambda S: 'THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and S['after_lock'] and S['before_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R164-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R164) END' in S['ferry'] and S['ot'].count('**(R164) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R164) ratified', '(R164) noted'))),
    ('G-READS-CITED', 'the reads bank -- the charter, PATHS :420, the era row, §1 and v0.2, ERRATA, the tool before the edits, the trails, the banks, PowerLimit, SIMPLICITY',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('THE_H2_PROGRAMME_CHARTER.md:116', 'x'))),
    ('G-BD2-SHOWN', 'PLACE-papers READ HERE for bd2ae1a, and its bank -- hash, date, ancestry, PATHS :420', lambda S: bd2_ok(S),
     lambda S: put(S, 'pp_bd2', '')),
    ('G-ERRATUM-FILED', 'ERRATA READ HERE against its blob -- the entry once, prior bytes a prefix, the line banked', lambda S: erratum_ok(S),
     lambda S: put(S, 'errata', S['errata'] + NL + P(R.EH))),
    ('G-BD2-LINES', 'the three documents READ HERE -- each line once, naming the erratum and its ERRATA line, each document kept', lambda S: bd2_lines_ok(S),
     lambda S: put(S, 'docs', dict(S['docs'], **{'phase1.5/proofs/THE_RESIDUE_OF_RH.md': S['docs']['phase1.5/proofs/THE_RESIDUE_OF_RH.md'].replace('E-2026-09-27-1', 'x')}))),
    ('G-SYNONYM-EDIT-CONFINED', 'the first tool commit`s diff against b553`s close READ HERE -- the map, its call, the two lines it replaces, that file alone',
     lambda S: syn_edit_ok(S), lambda S: put(S, 'diff1', S['diff1'] + NL + '-GRADE_RE = x')),
    ('G-SYNONYM-TEST', 'the synonym bank -- R5_output_HilbertPolya_to_RH alone moved, CONFLICT 14 -> 13, no row gone', lambda S: syn_test_ok(S),
     lambda S: put(S, 'syn', dict(S['syn'], changed=dict(S['syn'].get('changed', {}), **{'SIDE-kernel|e_difficulty': ['CONFLICT', 'DERIVES']})))),
    ('G-TRAILSUP-EDIT-CONFINED', 'the second tool commit`s diff READ HERE -- the form and its call, one line replaced, that file alone',
     lambda S: tsup_edit_ok(S), lambda S: put(S, 'diff2', S['diff2'] + NL + '-SYNONYMS = x')),
    ('G-TRAILSUP-TEST', 'the two trail-line banks -- nothing moved before the line, register5_output_holds alone after, CONFLICT 13 -> 12',
     lambda S: tsup_test_ok(S), lambda S: put(S, 'tsn', dict(S['tsn'], changed={R5HK: ['CONFLICT', 'DERIVES']}))),
    ('G-TRAILSUP-LINE', 'OPEN_TRAILS READ HERE and the regenerated table -- the line once, no grade word, the two terminals` grades',
     lambda S: tsup_line_ok(S), lambda S: put(S, 'live', dict(S['live'], **{R5HK: 'CONFLICT'}))),
    ('G-README-RULES', 'relay tools/corr_row.README.md READ HERE against its blob at b553`s close -- both rules appended, nothing above changed',
     lambda S: readme_ok(S), lambda S: put(S, 'readme', S['readme'].replace('trail-line', 'x').replace('synonym map', 'x'))),
    ('G-TOOL-COMMITS-ALONE', 'relay`s log READ HERE -- each tool commit carries that file alone and quotes its test',
     lambda S: commits_ok(S), lambda S: put(S, 'tc', [dict(S['tc'][0], files=S['tc'][0]['files'] + ['data/b554_synonym.txt']), S['tc'][1]])),
    ('G-READING-ONE-CLOSED', 'FINDINGS READ HERE and b553`s fine bank -- the entry once, its cited lines carrying what it cites',
     lambda S: reading_one_ok(S), lambda S: put(S, 'find', S['find'].replace('The π/γ model was the navigator', 'The π/γ model was the seat'))),
    ('G-SIGN-CONTROL', 'b548`s two banks READ HERE against the node table -- Z equal, OFF + ON = Z, the pair and the on-line sum to 1e-9',
     lambda S: sign_control_ok(S), lambda S: put(S, 'sweep', {**S['sweep'], 36: dict(S['sweep'][36], Z=S['sweep'][36]['Z'] + 1e-3)})),
    ('G-SIGN-FLOOR', 'the floor recomputed here from the nodes and b548`s B -- equal per interval',
     lambda S: sign_floor_ok(S), lambda S: put(S, 'sp', dict(S['sp'], floor=[dict(f, floor=f['floor'] * 0.5) for f in S['sp'].get('floor', [])]))),
    ('G-SIGN-INTERVALS', 'the runs recomputed against every node`s sign -- contiguous over 30-60, the positive list the POS runs',
     lambda S: sign_intervals_ok(S), lambda S: put(S, 'sp', dict(S['sp'], pos=(S['sp'].get('pos') or [])[:1]))),
    ('G-H8-SCORED', 'the sign bank -- H8`s clauses recomputed here, the verdict line', lambda S: h8_ok(S),
     lambda S: put(S, 'sptxt', S['sptxt'].replace('### H8 IS REFUTED', '### H8 IS NOT REFUTED').replace('### H8 IS NOT REFUTED', '### H8 IS x'))),
    ('G-CRESTS', 'the sign bank -- every crest at a ≥ 38, the pair negative there, the parts summing to Q', lambda S: crests_ok(S),
     lambda S: put(S, 'sp', dict(S['sp'], crests=[dict(c, Q=c['Q'] + 1.0) for c in S['sp'].get('crests', [])]))),
    ('G-DETECTION-PRICED', 'OPEN_TRAILS READ HERE -- the price once, every item of both routes, the cheaper recomputed by the sealed criterion',
     lambda S: detection_ok(S), lambda S: put(S, 'pr', dict(S['pr'], cheaper='closed-form'))),
    ('G-PAIRING-HAZARD', 'OPEN_TRAILS READ HERE -- the hazard line once, naming :11290, at its banked line', lambda S: hazard_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace(P(R.PHZ), P(R.PHZ).replace(':11290', ':11291')))),
    ('G-ANOMALY-ROUTED', 'OPEN_TRAILS READ HERE and SIDE-kernel`s HEAD -- the line once, HEAD, v1.7, v1.5, CP-5', lambda S: anomaly_ok(S),
     lambda S: put(S, 'ker_head', '5e668b4')),
    ('G-SIMP-ROWS', 'the document`s table at b553`s commit, counted here -- equal to the row bank and the tier bank', lambda S: simp_rows_ok(S),
     lambda S: put(S, 'srows', dict(S['srows'], count=20))),
    ('G-SIMP-PROBES', 'the probe bank -- every probe a tier needs, exit 0, no error, manifest equal; every terminal found and profiled',
     lambda S: probes_ok(S), lambda S: put(S, 'probes', [dict(p, exit=1) if p['id'] == 'l7' else p for p in S['probes']])),
    ('G-SIMP-BRANCH-PROBE', 'the branch probe`s bank -- exit 0 in the worktree at 27a3ae7, the three profiles as the table prints them',
     lambda S: branch_probe_ok(S), lambda S: put(S, 'kdtxt', S['kdtxt'].replace('rev-parse HEAD = 27a3ae7b2f49', 'x'))),
    ('G-WORKTREE-REMOVED', 'the worktree bank, the path and SIDE-kernel`s worktree list READ HERE', lambda S: worktree_ok(S),
     lambda S: put(S, 'wt_exists', True)),
    ('G-SIMP-TIERS', 'the tier bank -- every tier in the law`s vocabulary, each row its weakest link, the counts recomputed', lambda S: tiers_ok(S),
     lambda S: put(S, 'st', dict(S['st'], term_tiers=dict(S['st'].get('term_tiers', {}), T0=-1)))),
    ('G-SIMP-BLOCK', 'SIMPLICITY READ HERE against its blob -- the block once, every row, the document kept', lambda S: block_ok(S),
     lambda S: put(S, 'simp', S['simp'].replace('| :446 |', '| :999 |'))),
    ('G-SIMP-CONCLUSIONS', 'the statements banked -- none names RiemannHypothesis; every row`s conclusion printed', lambda S: conclusions_ok(S),
     lambda S: put(S, 'st', dict(S['st'], terms=S['st'].get('terms', []) + [dict(name='x', statement='x : RiemannHypothesis', row=0, tier='T0')]))),
    ('G-SIMP-READING', 'FINDINGS and SIMPLICITY READ HERE -- the reading once, the pointer once naming its line, CP-7', lambda S: sreading_ok(S),
     lambda S: put(S, 'simp', S['simp'].replace(P(R.SPT), 'x'))),
    ('G-SIMP-STEMS', 'the document at b553`s commit, counted here with the tool`s own pattern -- equal to the bank; no byte above the appends changed',
     lambda S: stems_ok(S), lambda S: put(S, 'stems', dict(S['stems'], per={s: 0 for s in BTM.STEMS}))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once, H8, the erratum, the dispositions, the next keystone', lambda S: findings_ok(S),
     lambda S: put(S, 'find', S['find'].replace(P(R.FH), 'x'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in three repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b553'}))),
    ('G-MEMORY-UNREFRESHED', 'the memory directory READ HERE -- no file written after this face (R157)(6)',
     lambda S: bool(S['mem_times']) and max(S['mem_times']) < os.path.getmtime(FACE),
     lambda S: put(S, 'mem_times', S['mem_times'] + [os.path.getmtime(FACE) + 1])),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-LINES-KEPT', 'the seven written files against their blobs at b553`s commit',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY, SPIRAL_MAP, FACES_LEDGER, THE_LOAD_BEARING_MAP and THE_IDENTITY_CHAIN against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'FACES_LEDGER.md',
                                                               'phase1.5/method/THE_LOAD_BEARING_MAP.md', 'phase2/method/THE_IDENTITY_CHAIN.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'REGISTRY.md': S['pp_now']['REGISTRY.md'] + b' '}))),
    ('G-KERNEL-SOURCES-UNTOUCHED', 'six kernels` mains READ HERE against their pre-act heads -- nothing written, no `.lean`',
     lambda S: kernel_sources_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-kernel': ['Kernel/DerivativeEngine.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b554_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b554_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b554 bank and tool and this act`s PLACE-papers bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the bd2 bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the table banks and the live table', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the sign bank', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the prices bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the tier bank', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the statements banked', lambda S: nscored(S, 'n6'), lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-N7-SCORED', 'the desk against the mains, the worktree, the tools, the token, the deposit and the trial worktree', lambda S: nscored(S, 'n7'),
     lambda S: put(S, 'sc', dict(S['sc'], n7=not S['sc'].get('n7')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b554 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels` mains READ HERE',
     lambda S: 'No kernel lane opened at this act' in trail(S) and kernel_sources_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the seven written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-INSTRUMENTS-EDITED-AS-ORDERED', 'relay`s tools against b553`s close -- terminal_table.py the one .py modified',
     lambda S: [x for x in S['tools_edited'] if x.endswith('.py')] == ['terminal_table.py'],
     lambda S: put(S, 'tools_edited', ['corr_row.py', 'terminal_table.py'])),
    ('G-WRITELIST-KINDS', 'every b554 commit in four repositories and the housekeeping commit, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b554')" in S['suite']
                and "data/b554_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b554_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b554')
              and 'data/b554_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b554 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b554_checks_postpush.txt' if pushed else 'b554_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b554_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
