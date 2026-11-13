# -*- coding: utf-8 -*-
"""b754_agenda.py -- (R364)(5): THE SITTING'S AGENDA, data/b754_agenda.txt: every item's CURRENT read and every draft banked before any
item is put, in b736's form (CURRENT read from the file at HEAD or by gh, DRAFTED banked, passed or struck by number).

WHAT IT DOES. Each draft is the ruling's own words, cut from data/b754_ferry.txt by its line, the amendment rows' changes applied and
printed beside it (row 3 (3), (4), (7), (8); row 4 (3); row 5). Every Lean name, path and line a draft of [A] or [B] carries is sought in
its kernel's tree at the revision the draft names, by `git grep` and a declaration matcher, and printed. Every cite of a draft is read
against the tree it names and printed OK or DIFFERS, each difference lettered; the seat changes no word of a draft. The CURRENT of [A] is
read from FINDINGS at PLACE-papers main; of [A5] and [B] from the captures of (4)(vi) and the clones' mains; of [D2] from the harness's user
settings (two keys, the file named by no path). For [U1] the three cadences are fitted to the yield bank's table (data/b754_close_yield.txt
(C)) and their savings computed from b753's part seconds (the part banks, read by tools/b754_yield.py's own reader). For [M2] the effect of
part (a) is read from each family's files on main by their own version lines, and the two cuts of part (d) are measured in bytes.
WHAT IT QUOTES: the lines the items name ((R364)(5)'s opening sentence), each read first against [Q] row (3) (the word read at run time from
REGISTRY :373 and held in no tracked file; the section under :373; FINDINGS :820-:826) and against the account and the identifier forms;
a line so read is cited by line and digest. Nothing is written but its bank: no ledger, door, setting or rules bank.
ITS READERS' REACHES, printed beside their figures: the declaration matcher reads a declaration opening a line, its namespace not read;
the version reader takes the first version written as v<n>.<n> or "Version <n>.<n>" in a file's first 40 lines; the fit reads a failure
as the yield bank prints it (an arm whose LIVE column reads FAIL) and a part by b753's layout.

  python -X utf8 -u tools/b754_agenda.py control     the controls alone
  python -X utf8 -u tools/b754_agenda.py dry         the controls and the agenda, printed, nothing written
  python -X utf8 -u tools/b754_agenda.py run         the controls, then the bank written (the generator committed before its run)
"""
import collections
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import textwrap
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import outbound   # noqa: E402
import roster   # noqa: E402
import b754_doors as DOORS   # noqa: E402
import b754_yield as YIELD   # noqa: E402
from b753_anchors import anchors as layer_anchors   # noqa: E402

ACT = 'b754'
SELF = 'tools/%s_agenda.py' % ACT
BANK = os.path.join(RELAY, 'data', '%s_agenda.txt' % ACT)
PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = '\n'
K = {'SIDE-explicit-formula': 'D:/SIDE-explicit-formula', 'SIDE-kernel': 'D:/SIDE-kernel', 'SIDE-lv-conservation': 'D:/SIDE-lv-conservation',
     'SIDE-trivium': 'D:/SIDE-trivium', 'SIDE-bsd-multiplicity': 'D:/SIDE-bsd-multiplicity'}
EF = 'SIDE-explicit-formula'
# ### the ferry bank's lines of (R364)(5), each with the words its line opens on (data/b754_ferry.txt)
FERRY = [('(5)', 17, '(5) THE SITTING'), ('[A]', 19, '[A] THE REFERENCE LAYER'), ('[A1]', 20, '[A1] riemann-hypothesis'),
         ('[A2]', 21, '[A2] two-leg-completeness'), ('[A3]', 22, '[A3] conservation-of-spectra'), ('[A4]', 23, '[A4] simplicity-riemann-zeros'),
         ('[A5]', 24, '[A5] PLACE-papers'), ('[B]', 26, '[B] THE DOORS'), ('[B1]', 27, '[B1] SIDE-explicit-formula'), ('[B2]', 28, '[B2] SIDE-explicit'),
         ('[B3]', 29, '[B3] SIDE-kernel'), ('[B4]', 30, '[B4] SIDE-kernel'), ('[B5]', 31, '[B5] SIDE-lv-conservation'), ('[B6]', 32, '[B6] SIDE-bsd'),
         ('[B7]', 33, '[B7] SIDE-trivium'), ('NOWRITE', 34, 'RULED WITH NO WRITE'), ('[Q]', 36, '[Q] THE QUOTING RULE'), ('[U]', 38, '[U] THE RECORD'),
         ('[C1]', 40, '[C1] THE CENSUS'), ('[H1]', 42, '[H1] THE HANDOFF PAGE'), ('[M2]', 44, '[M2] THE PROJECT SET'), ('[D2]', 46, '[D2] THE UPDATE'),
         ('[L]', 48, '[L] THE LINES FOR OPEN_TRAILS'), ('[R]', 50, '[R] THE RECORD LINES'), ('EXPORT', 52, 'THE CLUSTER EXPORT'), ('FOOT', 54, 'The sitting')]
ANCHORS = [('[A1]', 'riemann-hypothesis', 900), ('[A2]', 'two-leg-completeness', 978), ('[A3]', 'conservation-of-spectra', 896),
           ('[A4]', 'simplicity-riemann-zeros', 904)]
# ### the names the drafts carry: (item, name, kernel, the revision the draft names, the path and line the draft names or None)
NAMES = [('[A1]', 'h2_sign', EF, 'main', None), ('[A1]', 'classK', EF, 'main', None), ('[A1]', 'h2_sign_iff_rh', EF, 'v0.2', None),
         ('[A1]', 'li_nonneg_iff_rh', EF, 'v0.9', None), ('[A1]', 'arith_limit_nonneg_iff_rh', EF, 'v0.9', None),
         ('[A1]', 'h2_sign_chi_iff_grh_chi', EF, 'v0.14', None),
         ('[A3]', 'ProductFormula.conservation_of_spectra', 'SIDE-kernel', 'main', None),
         ('[A3]', 'SIDELvConservation.T1_completedRiemannZeta_factors_through_mellin', 'SIDE-lv-conservation', 'main', None),
         ('[A4]', 'simplicity_iff', EF, 'v0.17', None), ('[A4]', 'positivity_not_imp_simplicity', EF, 'v0.19', None),
         ('[A4]', 'SimpleProportion', EF, 'v0.17', None), ('[A4]', 'Zeta23.thmB\u2080_mult', EF, 'main', 'UPSTREAM'),
         ('[B1]', 'h2_sign', EF, 'main', ('SIDEExplicitFormula/H2Sign.lean', 29)),
         ('[B1]', 'h2_sign_iff_rh', EF, 'main', ('SIDEExplicitFormula/Seam.lean', 101)),
         ('[B1]', 'li_nonneg_iff_rh', EF, 'main', ('SIDEExplicitFormula/LiCriterionBridge.lean', 179)),
         ('[B1]', 'arith_limit_nonneg_iff_rh', EF, 'main', ('SIDEExplicitFormula/LiCriterionBridge.lean', 191)),
         ('[B1]', 'EF_lit_chi_holds', EF, 'main', ('SIDEExplicitFormula/Chi/Main.lean', 269)),
         ('[B1]', 'h2_sign_chi_iff_grh_chi', EF, 'main', ('SIDEExplicitFormula/Chi/CriterionConverse.lean', 270)),
         ('[B1]', 'h2_sign_cfg_iff_target', EF, 'main', ('SIDEExplicitFormula/Schema/Converse.lean', 265)),
         ('[B1]', 'zq_offline_zero', EF, 'v0.38', None),
         ('[B4]', 'ConservationBridge.riemann_hypothesis', 'SIDE-kernel', 'main', None), ('[B4]', 'spectral_cannon', 'SIDE-kernel', 'main', None),
         ('[B7]', 'trivium_theorem', 'SIDE-trivium', 'main', None)]
DECL = r'^\s*(@\[[^\]]*\]\s*)?((private|protected|noncomputable|partial|unsafe)\s+)*(theorem|lemma|def|abbrev|structure|class|instance|axiom|inductive|opaque)\s+%s(?=\s|$|:|\()'
VREAD = [re.compile(r'^\W{0,4}v(\d+(?:\.\d+)+)\b'), re.compile(r'(?i)^\W{0,4}version\W{0,6}v?(\d+(?:\.\d+)+)\b'),
         re.compile(r'^#{1,3}\s.*?\bv(\d+(?:\.\d+)+)\b')]
# ### the second shape, read where the first 40 lines carry none: the file's first edition note, "*v<n>.<n>[.<n>], <date> --", newest first
# ### (the census from v0.6 on carries its own at :92-:112, below the head; read at b754 by the search tool before this line was written)
EDNOTE = re.compile(r'^\*v(\d+(?:\.\d+)+), 20\d\d-')
# ### (R363)(6)[M2] (b): the Project set's 33, each name resolved to its path in the roster (the seat's reading of the ruling's descriptive
# ### names: the ledger split's README, the two generated pages of b576, the seven day-1 companions of b644), MANIFEST the build's own
PROJECT = ['README.md', 'FINDINGS.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'ERRATA.md', 'phase1.5/method/INSTRUMENTS.md', 'MANIFEST',
           'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', 'archive/2026-08-24-ledger-split/README.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md',
           'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md', 'phase1.5/method/TECHNE_TOOLKIT.md', 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md',
           'phase1.5/method/THE_METHOD_AS_IT_STANDS.md', 'phase1.5/method/THE_METHOD_CANON.md', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md', 'FACES_LEDGER.md',
           'THE_CLAUSE_AND_ITS_COMPILED_FACES.md', 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md',
           'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
           'phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md', 'day1/A_Place_to_Stand.md',
           'day1/Exhaustive_Enumeration.md', 'day1/Which_Structure_Confines.md', 'day1/Spectral_Inertness.md', 'day1/Seven_Mechanism_Classes.md',
           'day1/Third_Identity_Element.md', 'day1/Silence_of_Foundations.md', 'day1/ONE_PAGE_PROOF.md']
EPSTEIN = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
# ### [U]: the seat's price for each rule's standing change, a range in hours (estimates); "under two hours" read on the upper figure
U_PRICE = {'[U1]': (2.0, 4.0, 'the pass selection in the suite routes, a bank read in place of a run with a line naming it, the remote arms held apart'),
           '[U2]': (1.5, 3.0, 'the entry and trail writers (tools/standing/fold/record.tpl and closing.tpl): counts, CLAIM items in full, the banks named'),
           '[U3]': (0.5, 1.0, 'the refusals counted by kind in the entry and the trail, no letter; a kind above the previous act`s count an event'),
           '[U4]': (6.0, 12.0, 'a standing template and a per-act spec in place of the carry, with b753`s module composed from its spec as the control'),
           '[U5]': (0.8, 1.5, 'the price table`s rows read from the last act`s step rows; a comparison tool run at every close to a bank of its own')}
PUTS = ['[A]', '[B]', '[Q]', '[U]', '[H1]', '[M2]', '[D2]', '[L]', '[R]']


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def run(argv):
    r = subprocess.run(argv, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout, r.stderr


def git(repo, *a):
    rc, out, err = run(['git', '-C', repo] + list(a))
    if rc:
        raise SystemExit('### NOT READ: git -C %s %s: %s' % (repo, ' '.join(a), err.strip()[:200]))
    return out


def gitq(repo, *a):
    return run(['git', '-C', repo] + list(a))


def lines(repo, rev, path):
    return git(repo, 'show', '%s:%s' % (rev, path)).replace('\r', '').split(NL)


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def wrap(text, ind='    ', w=170):
    return textwrap.wrap(text, w, initial_indent=ind, subsequent_indent=ind, break_long_words=False, break_on_hyphens=False) or [ind]


def heading_level(l):
    m = re.match(r'^(#+)\s', l)
    return len(m.group(1)) if m else 0


def has(X, k, toks):
    """line k of X carries every token, case ignored; False where X holds no line k."""
    return 0 < k <= len(X) and all(t.lower() in X[k - 1].lower() for t in toks)


# ---------------------------------------------------------------- [Q] row (3): the protected lines, by file
def protected_lines(F, R, word):
    """{file: set of line numbers}: FINDINGS :820-:826 and every line carrying the word with two either side; REGISTRY's section under :373
    (to the next heading of its level or above) and the word's lines with two either side."""
    rx = re.compile(r'\b%s\b' % re.escape(word), re.I) if word else None

    def near(X):
        out = set()
        if rx:
            for k, l in enumerate(X, 1):
                if rx.search(l):
                    out |= set(range(max(1, k - 2), min(len(X), k + 2) + 1))
        return out
    pf = set(range(820, 827)) | near(F)
    pr = near(R)
    lv = heading_level(R[372]) if len(R) > 372 else 0
    if lv:
        k = 373
        while k <= len(R) and not (k > 373 and 0 < heading_level(R[k - 1]) <= lv):
            pr.add(k)
            k += 1
    return {'FINDINGS.md': pf, 'REGISTRY.md': pr}


class Q(object):
    """the quoting gate: a line is quoted only where no kind withholds it."""
    def __init__(self, acct, word, prot):
        self.acct, self.word, self.prot = acct, word, prot

    def show(self, fname, k, s):
        why = DOORS.withheld(s, self.acct, self.word)
        if k in self.prot.get(fname, set()):
            why = ['[Q] row (3) by place'] + why
        return ('BY LINE AND DIGEST %s (%s), %d characters' % (digest(s), ', '.join(why), len(s))) if why else '"%s"' % s


# ---------------------------------------------------------------- the drafts
def ferry_lines():
    return lines(RELAY, 'HEAD', 'data/%s_ferry.txt' % ACT)


def draft(FL, tag):
    n = [x for x in FERRY if x[0] == tag][0][1]
    return FL[n - 1].strip()


def split_sub(text, letter):
    """the numbered sub-items of a line ([L6] ..., [U1] ...): {tag: words}, each from its tag to the next tag; a tag opens a sub-item where
    an upper-case word follows it."""
    pos = [(m.start(), m.group(0).strip()) for m in re.finditer(r'\[%s(\d+)\] (?=[A-Z])' % letter, text)]
    out = collections.OrderedDict()
    for i, (p, tag) in enumerate(pos):
        end = pos[i + 1][0] if i + 1 < len(pos) else len(text)
        out[tag] = text[p:end].strip()
    return out, (text[:pos[0][0]].strip() if pos else text)


AMEND_A4 = ('(FINDINGS :6880-:6884)', '(FINDINGS :5778, :6856, :6880-:6884)')


def amendments():
    return json.loads(git(RELAY, 'show', 'HEAD:data/%s_amendments.json' % ACT))['rows']


def cut_words(words, start, end):
    i = words.find(start)
    if i < 0:
        return None
    j = words.find(end, i)
    return words[i:j + len(end)] if j >= 0 else words[i:]


# ---------------------------------------------------------------- the names
def locate(repo, rev, name):
    last = name.split('.')[-1]
    tok = max(re.findall(r'[A-Za-z0-9_]+', last), key=len)
    rc, out, _ = gitq(K[repo], 'grep', '-n', '-F', '-e', tok, rev, '--', '*.lean')
    rx = re.compile(DECL % re.escape(last))
    hits = []
    for l in out.splitlines():
        p = l.split(':', 3)
        if len(p) == 4 and rx.match(p[3]):
            hits.append((p[1], int(p[2])))
    return hits


def mentions(repo, rev, name):
    """the lines of the kernel's Lean files at `rev` naming `name` in any sense (a citation of a theorem the kernel does not declare)."""
    last = name.split('.')[-1]
    tok = max(re.findall(r'[A-Za-z0-9_]+', last), key=len)
    rc, out, _ = gitq(K[repo], 'grep', '-n', '-F', '-e', tok, rev, '--', '*.lean')
    hits = []
    for l in out.splitlines():
        p = l.split(':', 3)
        if len(p) == 4 and name in p[3]:
            hits.append((p[1], int(p[2])))
    return hits


def tag_commit(repo, tag):
    rc, out, _ = gitq(K[repo], 'rev-parse', '%s^{commit}' % tag)
    return out.strip() if rc == 0 else ''


# ---------------------------------------------------------------- [M2]
def version_of(text_lines):
    for k, l in enumerate(text_lines[:40], 1):
        for rx in VREAD:
            m = rx.match(l)
            if m:
                return k, tuple(int(x) for x in m.group(1).split('.'))
    for k, l in enumerate(text_lines, 1):
        m = EDNOTE.match(l)
        if m:
            return k, tuple(int(x) for x in m.group(1).split('.'))
    return None, None


def vstr(v):
    return 'v' + '.'.join(map(str, v)) if v else '-'


def families_effect(tree, rost):
    fams = []
    for p in rost:
        f = roster.family(p)
        if f not in fams:
            fams.append(f)
    md = [p for p in tree if p.endswith('.md')]
    rows, joins, leaves, undecided, current = [], [], [], [], {}
    for f in fams:
        cands = sorted(p for p in md if roster.family(p) == f)
        present = [p for p in rost if roster.family(p) == f]
        vers = dict((p, version_of(lines(PP, 'main', p)) if len(cands) > 1 else (None, None)) for p in cands)
        if len(cands) == 1:
            cur, why = cands[0], 'one file'
        elif cands and all(vers[p][1] for p in cands):
            top = max(vers[p][1] for p in cands)
            best = [p for p in cands if vers[p][1] == top]
            cur, why = (best[0], 'the highest version line') if len(best) == 1 else (None, 'a tie at %s: %s' % (vstr(top), ', '.join(best)))
        else:
            cur, why = None, 'no version line read in %s' % ', '.join(p for p in cands if not vers[p][1])
        rows.append((f, cands, present, vers, cur, why))
        if cur:
            current[f] = cur
            if cur not in present:
                joins.append(cur)
            leaves += [p for p in present if p != cur]
        else:
            undecided.append(f)
    return rows, joins, leaves, undecided, current


def size(path):
    rc, out, _ = gitq(PP, 'cat-file', '-s', 'main:%s' % path)
    return int(out.strip()) if rc == 0 else None


def findings_cut(F, last=20, act_n=754):
    """the head and the reference layer whole (to the first rule line after `## How findings move`), every level-two heading after it by its
    line, the entries of the last `last` acts whole (from
    the heading of the corrigendum the earliest of them wrote, `Corrigendum to b<N-last>`s record`)."""
    hm = [k for k, l in enumerate(F, 1) if l.startswith('## How findings move')]
    end = next((k for k in range(hm[0], len(F) + 1) if F[k - 1].strip() == '---'), None) if len(hm) == 1 else None
    if end is None:
        raise SystemExit('### THE LAYER`S END NOT READ: `## How findings move` once and a rule line after it wanted')
    rx = re.compile(r'^## Corrigendum to b%d\W' % (act_n - last))
    starts = [k for k in range(end + 1, len(F) + 1) if rx.match(F[k - 1])]
    s = starts[0] if len(starts) == 1 else None
    out = F[:end]
    heads = 0
    for k in range(end + 1, (s or len(F) + 1)):
        if F[k - 1].startswith('## '):
            out.append('FINDINGS :%d %s' % (k, F[k - 1]))
            heads += 1
    if s:
        out += F[s - 1:]
    return out, end, s, heads


def trails_cut(O, last=10, act_n=754):
    """the head (to the first heading of level two or three), the standing items (the section `## Open trails (active)` to the next level-two
    heading), the trails of the last `last` acts whole (from `### b<N-last> -- lane two` to the end) and every earlier level-three heading by
    its line."""
    first = next(k for k, l in enumerate(O, 1) if heading_level(l) in (2, 3))
    st = [k for k, l in enumerate(O, 1) if l.startswith('## Open trails (active)')]
    st0 = st[0] if len(st) == 1 else None
    st1 = next((k for k in range((st0 or 0) + 1, len(O) + 1) if O[k - 1].startswith('## ')), len(O) + 1) - 1 if st0 else None
    rx = re.compile(r'^### b%d \u2014 lane two' % (act_n - last))
    tr = [k for k, l in enumerate(O, 1) if rx.match(l)]
    t0 = tr[0] if len(tr) == 1 else None
    out = O[:first - 1]
    if st0:
        out += O[st0 - 1:st1]
    heads = 0
    for k in range(first, (t0 or len(O) + 1)):
        if st0 and st0 <= k <= st1:
            continue
        if O[k - 1].startswith('### '):
            out.append('OPEN_TRAILS :%d %s' % (k, O[k - 1]))
            heads += 1
    if t0:
        out += O[t0 - 1:]
    return out, first, (st0, st1), t0, heads


def nbytes(ls):
    return len((NL.join(ls) + NL).encode('utf-8'))


# ---------------------------------------------------------------- [U1]
YC = re.compile(r'^  (b\d{3})  pre-run (\d+) ; pre-push (\d+) ; post-push (\d+) ; prev-mode (\d+)$')
YO = re.compile(r'^      only the (pre-run|pre-push|post-push|prev-mode) pass: (.*)$')
LSR = re.compile(r'ls-remote calls this part, per repository: (\d+) repositories')
PASSN = ['pre-run', 'pre-push', 'post-push', 'prev-mode']


def yield_c(Y):
    a = Y.index('## (C) THE PASSES` FAILURES, b724 TO b753 (an arm failing where its LIVE column reads FAIL in a part bank of the pass)')
    b = next(i for i, l in enumerate(Y) if l.startswith('## (C) EACH ARM THAT READ FAILING'))
    acts, cur = collections.OrderedDict(), None
    for l in Y[a:b]:
        m = YC.match(l)
        if m:
            cur = m.group(1)
            acts[cur] = dict(counts=dict(zip(PASSN, map(int, m.groups()[1:]))), only={})
            continue
        m = YO.match(l)
        if m and cur:
            acts[cur]['only'][m.group(1)] = [x.strip() for x in m.group(2).split(',') if x.strip()]
    return acts


def layouts():
    out, remote = {}, {}
    for name, prefix in YIELD.PASSES:
        r = YIELD.read_pass('b753', prefix)
        out[name] = dict((p, (set(YIELD.read_part(r['raw'][p])[0]), r['secs'][p])) for p in r['parts'])
        if name == 'post-push':
            for p in r['parts']:
                m = LSR.search(r['raw'][p])
                remote[p] = int(m.group(1)) if m else None
    return out, remote


def fit(acts, lay, remote):
    res = {}
    for P in PASSN:
        U = set()
        n = 0
        for a in acts.values():
            o = a['only'].get(P, [])
            U |= set(o)
            n += bool(o)
        keep, cut = {}, {}
        for part, (arms, secs) in lay[P].items():
            why = []
            if arms & U:
                why.append('holds %s' % ', '.join(sorted(arms & U)))
            if P == 'post-push' and (remote.get(part) or 0) > 0:
                why.append('reads a remote (%d repositories)' % remote[part])
            (keep if why else cut)[part] = (secs, '; '.join(why))
        res[P] = dict(U=U, n=n, keep=keep, cut=cut, saving=sum(s for s, _w in cut.values() if s is not None))
    return res


# ---------------------------------------------------------------- the controls
def controls(C):
    out, ok, n = [], 0, 0

    def case(label, good):
        nonlocal ok, n
        n += 1
        ok += bool(good)
        out.append('  (%d) %s : %s' % (n, label, 'AS WANTED' if good else '### NOT AS WANTED'))
    FL = C['FL']
    bad = [t for t, k, w in FERRY if not FL[k - 1].strip().startswith(w)]
    case('the ferry bank`s %d lines of (5), each opening on its words at its line: not so %s' % (len(FERRY), bad or 'none'), not bad)
    A = dict((a['line'], a['slug']) for a in C['anchors'])
    miss = [(s, k, A.get(k)) for _t, s, k in ANCHORS if A.get(k) != s]
    case('the four anchors of [A] at their lines by their headings` names (:896, :900, :904, :978): not so %s' % (miss or 'none'), not miss)
    case('the reference layer ends at :%d, the first rule line after `## How findings move` (the ruling: "to :1096 today")' % C['fc'][1], C['fc'][1] == 1096)
    bl = [(nm, want) for it, nm, repo, rev, want in NAMES if isinstance(want, tuple) and want not in C['loc'][(it, nm)]]
    nf = [nm for it, nm, repo, rev, want in NAMES if not C['loc'][(it, nm)] and want != 'UPSTREAM']
    up = [(nm, C['loc'][(it, nm)]) for it, nm, repo, rev, want in NAMES if want == 'UPSTREAM']
    case('the names the drafts call upstream are declared in no kernel file and cited in one: %s' % [(nm, len(h)) for nm, h in C['upstream']],
         all(not h for _nm, h in up) and all(h for _nm, h in C['upstream']))
    case('the declaration locator: the seven names of [B1] at the paths and lines the draft gives, at main: not so %s' % (bl or 'none'), not bl)
    case('the declaration locator: a planted name read NOT FOUND (%r)' % C['planted_loc'], C['planted_loc'] == [])
    out.append('      ### the names not found at the revision the draft names: %s (printed with the drafts; no condition)' % (nf or 'none'))
    case('the cite reader: a planted cite of FINDINGS :%d reads DIFFERS' % (len(C['F']) + 7), C['planted_cite'] is False)
    ya = C['yc']
    case('the yield bank`s (C): acts b724 to b753 read %d, each with four counts and an only-list per pass where the bank prints one' % len(ya),
         len(ya) == 30 and all(len(a['counts']) == 4 for a in ya.values()))
    sums = dict((P, sum(s for _a, s in C['lay'][P].values() if s is not None)) for P in PASSN)
    case('b753`s part seconds by pass, read by tools/b754_yield.py`s reader, equal to (B)`s "a pass" row %s: %s' % (C['brow'], sums),
         [sums[P] for P in PASSN] == C['brow'])
    pa = dict(C['yc'])
    some = sorted(C['lay']['post-push'])[-1]
    arm = sorted(C['lay']['post-push'][some][0])[0]
    pa['b999'] = dict(counts=dict.fromkeys(PASSN, 1), only={'post-push': [arm]})
    pf = fit(pa, C['lay'], C['remote'])
    case('the fit on a planted act whose post-push pass alone printed %s: the part %s keeps its place' % (arm, some), some in pf['post-push']['keep'])
    vt = [version_of(['**v5.18, 2026-10-03** \u2014 x'])[1], version_of(['# THE KEYSTONE CENSUS v0.8.3'])[1], version_of(['**Version:** 1.1.3'])[1],
          version_of(['no version here', 'nor here'])[1]]
    case('the version reader on four planted heads: %s' % [vstr(v) for v in vt], vt == [(5, 18), (0, 8, 3), (1, 1, 3), None])
    ve = [version_of(['# head'] + ['x'] * 50 + ['*v0.8.3, 2026-10-27 -- a', '*v0.8.2, 2026-10-20 -- b']),
          version_of(['**v0.4, 2026-08-01** — h'] + ['x'] * 50 + ['*v0.9, 2026-10-27 -- a']),
          version_of(['# head'] + ['x'] * 50 + ['v0.9 named mid-line, *v0.9, 2026-10-27'])]
    case('the second shape: an edition note below line 40 read where the head carries none %s; the head first where it carries one %s; '
         'a note not opening its line not read %s' % (ve[0], ve[1], ve[2]), ve == [(52, (0, 8, 3)), (1, (0, 4)), (None, None)])
    fcut, fend, fs, fh = C['fc']
    case('FINDINGS` cut: the last twenty acts` entries open at one heading (:%s); its lines %d = %d + %d headings + %d whole' % (
        fs, len(fcut), fend, fh, len(C['F']) - fs + 1 if fs else 0), bool(fs) and len(fcut) == fend + fh + len(C['F']) - fs + 1)
    ocut, ofirst, (st0, st1), t0, oh = C['oc']
    case('OPEN_TRAILS` cut: the standing items` section (:%s-:%s) and the last ten acts` trails (from :%s) each found once' % (st0, st1, t0), bool(st0 and t0))
    pm = [p for p in PROJECT if p != 'MANIFEST' and p not in C['tree']]
    case('the Project set`s 33 names: 32 paths on main and MANIFEST, the Epstein document on main: not on main %s' % (pm or 'none'),
         len(PROJECT) == 33 and not pm and EPSTEIN in C['tree'])
    case('the amendment row 3 (3)`s replacement: the parenthesis of [A4] found once in its line', draft(FL, '[A4]').count(AMEND_A4[0]) == 1)
    return out, ok, n


# ---------------------------------------------------------------- the agenda
def compose(gen):
    acct = DOORS.account(PP)
    FL = ferry_lines()
    F = lines(PP, 'main', 'FINDINGS.md')
    R = lines(PP, 'main', 'REGISTRY.md')
    E = lines(PP, 'main', 'ERRATA.md')
    PR = lines(PP, 'main', 'README.md')
    I = lines(PP, 'main', 'phase1.5/method/INSTRUMENTS.md')
    O = lines(PP, 'main', 'OPEN_TRAILS.md')
    EP = lines(PP, 'main', EPSTEIN)
    word = DOORS.q_word()
    prot = protected_lines(F, R, word)
    Qg = Q(acct, word, prot)
    tree = roster.main_tree()
    pp_head = git(PP, 'rev-parse', '--short=8', 'main').strip()
    loc = dict(((it, nm), locate(repo, rev, nm)) for it, nm, repo, rev, _w in NAMES)
    Y = lines(RELAY, 'HEAD', 'data/%s_close_yield.txt' % ACT)
    brow = [int(x) for x in re.match(r'^  a pass\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)', next(l for l in Y if l.startswith('  a pass '))).groups()]
    lay, remote = layouts()
    yc = yield_c(Y)
    ups = [(nm, mentions(repo, rev, nm)) for it, nm, repo, rev, w in NAMES if w == 'UPSTREAM']
    C = dict(FL=FL, F=F, anchors=layer_anchors(F), loc=loc, upstream=ups, planted_loc=locate(EF, 'main', 'zz_planted_absent_name'),
             planted_cite=has(F, len(F) + 7, ['conservation_of_spectra']), yc=yc, lay=lay, remote=remote, brow=brow, fc=findings_cut(F), oc=trails_cut(O), tree=set(tree))
    out, ok, n = controls(C)
    rows_am = amendments()
    caps = DOORS.load_caps()

    L = ['%s -- (R364)(5): THE SITTING`S AGENDA, EVERY ITEM`S CURRENT READ AND EVERY DRAFT BANKED BEFORE ANY ITEM IS PUT (%s)' % (ACT, stamp()[:10]), '',
         '### Written by %s at relay %s (the generator committed before its run) at %s, from PLACE-papers main %s and the kernels` trees by' % (SELF, gen, stamp(), pp_head),
         '### `git show` and `git grep`, the doors` captures of (4)(vi) and the relay`s banks at HEAD; no remote read. A bank of this act and no ledger:',
         '### nothing is written by it. Each draft is the ruling`s words cut from data/%s_ferry.txt by its line, its digest printed, the amendment' % ACT,
         '### rows` changes beside it; the seat changes no word of a draft, and a cite that differs at the tree is printed and lettered. A line',
         '### carrying [Q] row (3)`s word or standing in its places, the account or an identifier is cited by line and digest and not quoted.', '',
         '## THE CONTROLS, printed before any current word or draft'] + out
    L += ['', '## THE PUTS, IN ORDER ((R364)(5): ten puts; [C1] carried by the amendment row 5 at the ceiling of Component 1, data/%s_ceiling.txt :58, :63)' % ACT]
    price = dict((m.group(1), m.group(2)) for m in (re.match(r'^  (\(5\)\S*)\s+.*\| (\S+ h)', l) for l in lines(RELAY, 'HEAD', 'data/%s_stepzero.txt' % ACT)) if m)
    for i, t in enumerate(PUTS, 1):
        L.append('  %d. %-5s put once, passed whole, or passed with the numbers struck or held named, or struck ; the price table`s row (data/%s_stepzero.txt): %s' % (
            i, t, ACT, price.get('(5)' + t, price.get('(5)[L1]-[L8],[L14]' if t == '[L]' else '(5)[R1],[R3]' if t == '[R]' else '', '-'))))
    L.append('  CARRIED, not put: [C1] (row 5), and with it (4)(v); [L9] to [L13] and [R2] and the cluster export by (8)`s carry order (data/%s_ceiling.txt :63)' % ACT)

    # -------- the names
    L += ['', '## EVERY LEAN NAME A DRAFT OF [A] OR [B] CARRIES, sought at the revision the draft names (git grep and a declaration opening a line; the namespace not read)']
    upd = dict(ups)
    for it, nm, repo, rev, want in NAMES:
        h = loc[(it, nm)]
        if want == 'UPSTREAM':
            L.append('  %-5s %-62s %-22s %-6s UPSTREAM, as the draft says ("its theorem upstream"): declared in no Lean file of the kernel%s ; the kernel cites it at %s' % (
                it, nm, repo, rev, (' (### declared at %s)' % ' ; '.join('%s :%d' % x for x in h)) if h else '', ' ; '.join('%s :%d' % x for x in upd.get(nm, [])) or 'no line'))
            continue
        L.append('  %-5s %-62s %-22s %-6s %s%s' % (it, nm, repo, rev, ' ; '.join('%s :%d' % x for x in h[:4]) or '### NOT FOUND AT %s' % rev,
                                                     (' ; the draft gives %s :%d, %s' % (want[0], want[1], 'EQUAL' if want in h else '### DIFFERS')) if want else ''))
    for tg, want in (('v0.2', '5c72cad2'), ('v0.9', None), ('v0.14', None), ('v0.17', '5a1630b'), ('v0.19', None), ('v0.38', None)):
        c = tag_commit(EF, tg)
        L.append('  the tag %-6s of %s: %s%s' % (tg, EF, c[:8] or '### ABSENT', (' ; the draft gives %s: %s' % (want, 'EQUAL' if c.startswith(want) else '### DIFFERS')) if want else ''))
    anc = gitq(K[EF], 'merge-base', '--is-ancestor', 'v0.38', 'zq-b730')[0] == 0
    L.append('  the tag v0.38 on the branch zq-b730 (an ancestor of its tip): %s' % anc)
    sv = [p for p in git(K['SIDE-kernel'], 'ls-tree', '-r', '--name-only', 'main').split(NL) if 'SieveCeiling' in p]
    L.append('  [B4]`s SieveCeiling subsystem at SIDE-kernel main: %d path(s) carrying the name: %s' % (len(sv), ', '.join(sv[:6]) or '### NONE'))
    zt = git(K[EF], 'ls-tree', '--name-only', 'main').split(NL)
    vb = gitq(K[EF], 'ls-tree', '--name-only', 'main', 'Vendored/')[1].split(NL)
    L.append('  [B1]`s folders at %s main: Zeta23/ %s ; Vendored/Bulka/ %s' % (EF, 'Zeta23' in zt, 'Vendored/Bulka' in vb))

    # -------- the cites
    cites, letters = [], iter('abcdefghijklmnopqrstuvwxyz')

    def cite(item, what, good, holds):
        cites.append((item, what, good, holds))
    first =lambda X, tok: next((k for k, l in enumerate(X, 1) if tok in l), None)   # noqa: E731
    cite('[A1]', 'REGISTRY :953, the ceiling line, carries (R146) and 2026-09-25', has(R, 953, ['(R146)', '2026-09-25']), 'digest %s' % digest(R[952]))
    cite('[A1]', 'REGISTRY :953-:965 stand (the file %d lines)' % len(R), len(R) >= 965, '')
    cite('[A1]', 'ERRATA carries E-2026-09-25-1', bool(first(E, 'E-2026-09-25-1')), 'first at :%s' % first(E, 'E-2026-09-25-1'))
    cite('[A1]', 'README carries "What is claimed and what is not"', bool(first(PR, 'What is claimed and what is not')), 'at :%s' % first(PR, 'What is claimed and what is not'))
    cite('[A2]', 'REGISTRY :153 and :492-:496 carry 2026-07-23 (the rewording)', any(has(R, k, ['2026-07-23']) for k in [153, 492, 493, 494, 495, 496]),
         'carried at %s' % ', '.join(':%d' % k for k in [153, 492, 493, 494, 495, 496] if has(R, k, ['2026-07-23'])))
    cite('[A2]', 'A_Place_to_Stand on main', 'day1/A_Place_to_Stand.md' in C['tree'], '')
    cite('[A3]', 'FINDINGS :5924 carries conservation_of_spectra', has(F, 5924, ['conservation_of_spectra']), 'digest %s' % digest(F[5923]))
    cite('[A3]', 'FINDINGS :5938 carries T1_completedRiemannZeta_factors_through_mellin', has(F, 5938, ['T1_completedRiemannZeta_factors_through_mellin']), 'digest %s' % digest(F[5937]))
    cite('[A3]', 'ERRATA :664 carries conservation_of_spectra', has(E, 664, ['conservation_of_spectra']), 'digest %s' % digest(E[663]))
    cs = [p for p in tree if 'CONSERVATION_OF_SPECTRA_REFINED' in p]
    cite('[A3]', 'CONSERVATION_OF_SPECTRA_REFINED, a document on main', bool(cs), ', '.join(cs))
    cite('[A4]', 'README :135 carries "simplicity proved"', has(PR, 135, ['simplicity proved']), 'digest %s' % digest(PR[134]))
    v113 = [k for k in range(6880, 6885) if has(F, k, ['v1.1.3']) or has(F, k, ['_v1_1_3'])]   # ### the edition by its version or its file name
    cite('[A4]', 'FINDINGS :6880-:6884 stand and name the edition v1.1.3 (as v1.1.3 or by its file name _v1_1_3)', bool(v113),
         'named at %s' % ', '.join(':%d' % k for k in v113))
    cite('[A4] row 3 (3)', 'FINDINGS :5778 and :6856 carry simplicit-', has(F, 5778, ['simplicit']) and has(F, 6856, ['simplicit']), '')
    sp = [p for p in tree if 'SIMPLICITY_OF_RIEMANN_ZEROS' in p]
    spv = dict((p, vstr(version_of(lines(PP, 'main', p))[1])) for p in sp)
    cite('[A4]', 'SIMPLICITY_OF_RIEMANN_ZEROS at v1.1.3 by its own version line', any(v == 'v1.1.3' for v in spv.values()), '; '.join('%s %s' % kv for kv in spv.items()))
    cite('[A]', 'PLACE-papers 04fef04e, the history`s commit', gitq(PP, 'cat-file', '-e', '04fef04e^{commit}')[0] == 0, '')
    cite('[A]', 'FINDINGS :1086 and :1094, the layer`s two forms, inside the layer (to :%d)' % C['fc'][1], 1086 <= C['fc'][1] and 1094 <= C['fc'][1], '')
    b536 = lines(RELAY, 'HEAD', 'data/b536_components.txt')
    cite('[B1]', 'data/b536_components.txt :12 carries h2_sign_iff_rh and propext, Classical.choice, Quot.sound',
         has(b536, 12, ['h2_sign_iff_rh', 'propext', 'Classical.choice', 'Quot.sound']), '')
    kr = git(K['SIDE-kernel'], 'show', 'main:README.md').replace('\r', '').split(NL)
    ph = DOORS.ferry_phrase()
    cite('[B3]', 'the phrase [B3] replaces stands once at SIDE-kernel README :3', bool(ph) and len(kr) >= 3 and kr[2].count(ph) == 1, '')
    tr = git(K['SIDE-trivium'], 'show', 'main:README.md').replace('\r', '').split(NL)
    tl = loc[('[B7]', 'trivium_theorem')]
    cite('[B7] CURRENT', 'SIDE-trivium README :5`s line cite of trivium_theorem against the tree', bool(tl) and len(tr) >= 5 and (':%d' % tl[0][1]) in tr[4],
         'declared at %s :%s ; README :5 cites %s' % (tl[0][0] if tl else '-', tl[0][1] if tl else '-', ', '.join(re.findall(r':\d+', tr[4])) if len(tr) >= 5 else '-'))
    for k, iid in ((764, 'I-109'), (710, 'I-96'), (734, 'I-102'), (746, 'I-105'), (750, 'I-106'), (758, 'I-108')):
        cite('[R1]', 'INSTRUMENTS :%d opens %s' % (k, iid), k <= len(I) and re.match(r'^#+ %s\b' % iid, I[k - 1]) is not None, '')
    cite('[R1]', 'data/b711_coeffs.txt :12 stands', len(lines(RELAY, 'HEAD', 'data/b711_coeffs.txt')) >= 12, '')
    cite('[R1]', 'FINDINGS :10858, :11072, :11178, :11359 stand', len(F) >= 11359, '')
    cite('[R3]', 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md :216 and :218 are level-two headings', len(EP) >= 218 and heading_level(EP[215]) == 2 and heading_level(EP[217]) == 2, '')
    cite('[L8]', 'OPEN_TRAILS :2691 carries O.8', has(O, 2691, ['O.8']), 'digest %s' % digest(O[2690]))
    cite('[L14]', 'OPEN_TRAILS :3384 is the note at pattern grade', has(O, 3384, ['NOTE AT PATTERN GRADE']), 'digest %s' % digest(O[3383]))
    for k, rid in ((676, 'm5-3'), (677, 'm5-4'), (678, 'm5-2')):
        cite('[M2] row 3 (7)', 'REGISTRY :%d carries %s' % (k, rid), has(R, k, [rid]), '')
        cite('[M2] row 3 (7)', 'REGISTRY :672, the tier legend, gives %s a tier' % rid, re.search(r'\b%s [KCNE]\b' % re.escape(rid), R[671]) is not None, '')
    ds = lines(RELAY, 'HEAD', 'data/b753_dayend.txt')
    cite('[U]', 'data/b753_dayend.txt carries 5.31 and 4.70', any('5.31' in l for l in ds) and any('4.70' in l for l in ds), '')
    a93 = [int(s) for _p, s in re.findall(r'(act|standing-[a-z0-9]+) (\d+) s', lines(RELAY, 'HEAD', 'data/b753_arm_seconds.txt')[92])]
    cite('[U]', 'data/b753_arm_seconds.txt :93, the ten parts` seconds, summing to 3,114', len(a93) == 10 and sum(a93) == 3114, '%d parts, %d s' % (len(a93), sum(a93)))
    sz = lines(RELAY, 'HEAD', 'data/b753_stepzero.txt')
    cite('[U]', 'data/b753_stepzero.txt :14 carries 2,114 and 520', '2114' in sz[13].replace(',', '') and '520' in sz[13], '')
    hf = lines(RELAY, 'HEAD', 'HANDOFF.md')
    cite('[H1]', 'HANDOFF.md 805 lines', len([x for x in hf if x is not None]) - (1 if hf and hf[-1] == '' else 0) == 805, '%d lines' % (len(hf) - (1 if hf[-1] == '' else 0)))
    cite('[Q]', 'data/b721_frozen_line_drafts.txt :7 stands', len(lines(RELAY, 'HEAD', 'data/b721_frozen_line_drafts.txt')) >= 7, '')
    cite('[Q]', 'data/b746_section1.txt stands', gitq(RELAY, 'cat-file', '-e', 'HEAD:data/b746_section1.txt')[0] == 0, '')
    L += ['', '## EVERY CITE OF THE DRAFTS READ AGAINST ITS TREE (OK, or DIFFERS lettered; the seat changes no word of a draft)']
    diffs = []
    for item, what, good, holds in cites:
        if good:
            L.append('  %-14s OK       %s%s' % (item, what, (' (%s)' % holds) if holds else ''))
        else:
            lt = next(letters)
            diffs.append(lt)
            L.append('  %-14s DIFFERS (%s) %s%s' % (item, lt, what, (' -- the tree: %s' % holds) if holds else ''))
    L.append('  ### CITES %d ; OK %d ; DIFFERS %d %s' % (len(cites), sum(1 for c in cites if c[2]), len(diffs), ', '.join('(%s)' % d for d in diffs)))

    # -------- [A]
    L += ['', '## [A] THE REFERENCE LAYER: FOUR ANCHORS OF FINDINGS AND ONE DESCRIPTION', '',
          '[A] FILE FINDINGS.md at PLACE-papers ; each write one line for one line, the line count printed before and after',
          '  CURRENT: FINDINGS.md at main %s, %d lines (the count before any write of [A]); the layer`s two forms, :1086 and :1094:' % (pp_head, len(F) - (1 if F[-1] == '' else 0))]
    for k in (1086, 1094):
        L.append('    :%d %s' % (k, Qg.show('FINDINGS.md', k, F[k - 1])))
    L += ['  DRAFTED (data/%s_ferry.txt :19, digest %s):' % (ACT, digest(draft(FL, '[A]')))] + wrap(draft(FL, '[A]'))
    for it, slug, k in ANCHORS:
        dr = draft(FL, it)
        if it == '[A4]':
            dr2 = dr.replace(AMEND_A4[0], AMEND_A4[1])
        L += ['', '[%s] %s, FINDINGS :%d-:%d' % (it.strip('[]'), slug, k, k + 2), '  CURRENT:']
        for j in range(k, k + 3):
            L.append('    :%d %s' % (j, Qg.show('FINDINGS.md', j, F[j - 1])))
        if it == '[A4]':
            L += ['  DRAFTED (data/%s_ferry.txt :%d, digest %s), AS AMENDED BY ROW 3 (3): the closing parenthesis "%s" reads "%s" (digest %s):' % (
                ACT, [x for x in FERRY if x[0] == it][0][1], digest(dr), AMEND_A4[0], AMEND_A4[1], digest(dr2))] + wrap(dr2)
            L.append('  BESIDE IT, ROW 3 (3)`S SIDE-BY-SIDE, the record`s two readings of that paper (b554, b596):')
            for j in (5778, 6856):
                L.append('    FINDINGS :%d %s' % (j, Qg.show('FINDINGS.md', j, F[j - 1])))
        else:
            L += ['  DRAFTED (data/%s_ferry.txt :%d, digest %s):' % (ACT, [x for x in FERRY if x[0] == it][0][1], digest(dr))] + wrap(dr)
        L.append('  PASSED as (a) or (b): FINDINGS :%d (and :%d where the form replaces it) written by its draft, one line for one line, the count printed equal; STRUCK: the anchor stands' % (k + 1, k + 2))
    d5 = caps.get(('PLACE-papers', 'description'))
    L += ['', '[A5] PLACE-papers` description',
          '  CURRENT (by gh at %s, data/%s_doors.txt): %s' % ((d5 or {}).get('at', '-'), ACT, DOORS.show(d5['out'], acct, word) if d5 and d5.get('rc') == 0 else '### NOT READ'),
          '  DRAFTED (data/%s_ferry.txt :24, digest %s):' % (ACT, digest(draft(FL, '[A5]')))] + wrap(draft(FL, '[A5]'))
    L.append('  PASSED: written by the description route in tools/b736_sitting.py`s form and read back; STRUCK: it stands')

    # -------- [B]
    L += ['', '## [B] THE DOORS, SEVEN ITEMS', '', '[B] DRAFTED (data/%s_ferry.txt :26, digest %s):' % (ACT, digest(draft(FL, '[B]')))] + wrap(draft(FL, '[B]'))
    er = git(K[EF], 'show', 'main:README.md').replace('\r', '').split(NL)
    for it in ('[B1]', '[B2]', '[B3]', '[B4]', '[B5]', '[B6]', '[B7]'):
        dr = draft(FL, it)
        L += ['', it]
        if it == '[B1]':
            L.append('  CURRENT: %s README.md at main %s, %d lines, the lines the draft replaces:' % (EF, git(K[EF], 'rev-parse', '--short=8', 'main').strip(), len(er)))
            for k in (3, 5, 6, 7, 23, 24, 25, 26):
                L.append('    :%d %s' % (k, DOORS.show(er[k - 1], acct, word)))
        elif it in ('[B2]', '[B4]', '[B6]', '[B7]'):
            door = {'[B2]': EF, '[B4]': 'SIDE-kernel', '[B6]': 'SIDE-bsd-multiplicity', '[B7]': 'SIDE-trivium'}[it]
            c = caps.get((door, 'description'))
            L.append('  CURRENT: %s`s description by gh at %s: %s' % (door, (c or {}).get('at', '-'), DOORS.show(c['out'], acct, word) if c and c.get('rc') == 0 else '### NOT READ'))
            if it in ('[B6]', '[B7]'):
                rr = git(K[door], 'show', 'main:README.md').replace('\r', '').split(NL)
                ks = range(1, 11) if it == '[B6]' else range(3, 8)
                L.append('  CURRENT: its README.md at main, the lines the draft is cut from:')
                for k in ks:
                    if k <= len(rr):
                        L.append('    :%d %s' % (k, DOORS.show(rr[k - 1], acct, word)))
        elif it == '[B3]':
            L.append('  CURRENT: SIDE-kernel README.md :3 %s' % DOORS.show(kr[2], acct, word))
        elif it == '[B5]':
            L += ['  HELD BY THE AMENDMENT ROW 3 (4) (data/%s_amendments.json row 3): nothing is written to SIDE-lv-conservation`s description or README;' % ACT,
                  '  [L9] gains that kernel (carried with [L9]). The draft as the ruling gave it, for the record:']
        L += ['  DRAFTED (data/%s_ferry.txt :%d, digest %s):' % (ACT, [x for x in FERRY if x[0] == it][0][1], digest(dr))] + wrap(dr)
    L += ['', 'RULED WITH NO WRITE, each the navigator`s reading, strikeable at the put (data/%s_ferry.txt :34, digest %s):' % (ACT, digest(draft(FL, 'NOWRITE')))] + wrap(draft(FL, 'NOWRITE'))
    L.append('  PASSED: each README item one commit to that kernel`s main carrying README.md alone, pushed through the one-call tool with its scan; each description one call of the route with its read-back')

    # -------- [Q]
    L += ['', '## [Q] THE QUOTING RULE', '',
          '[Q] FILE data/%s_rules.txt (four rows) and tools/standing/originsearch.py with its controls, VERSION moved' % ACT,
          '  CURRENT, by bank and line: N5 as (R363) wrote it (data/b753_ferry.txt, its expectations); the practice the inventory measured (data/b753_defects.txt (h`));',
          '    the waiver by class (data/b753_events.txt (5)); the record`s form of line and digest (data/b721_frozen_line_drafts.txt :7); the sections of a keystone',
          '    banked whole at the sittings of b746 to b751 (data/b746_section1.txt and its siblings). The word of row (3) is read at run time and printed nowhere.',
          '  DRAFTED (data/%s_ferry.txt :36, digest %s):' % (ACT, digest(draft(FL, '[Q]')))] + wrap(draft(FL, '[Q]'))
    L.append('  THE SEAT`S PRICE, the price table`s row: %s' % price.get('(5)[Q]', '-'))

    # -------- [U]
    ut = draft(FL, '[U]')
    us, uhead = split_sub(ut, 'U')
    u5, utail = us['[U5]'].split(' Passed: rows of', 1)
    us['[U5]'] = u5.strip()
    utail = 'Passed: rows of' + utail
    L += ['', '## [U] THE RECORD`S UPKEEP', '', '[U] FILE data/%s_rules.txt, a row per rule passed; a standing change by a version commit of its own where its price reads under two hours' % ACT,
          '  CURRENT and the head of the item (data/%s_ferry.txt :38, digest %s, the words before [U1]):' % (ACT, digest(ut))] + wrap(uhead)
    L.append('  the cut checked: the head, the five rules and the tail joined equal the line: %s' % (' '.join([uhead] + list(us.values()) + [utail]) == ut))
    acts = yc
    res = fit(acts, lay, remote)
    for tag, words in us.items():
        lo, hi, what = U_PRICE[tag]
        L += ['', '%s DRAFTED (digest %s):' % (tag, digest(words))] + wrap(words)
        L.append('  THE SEAT`S PRICE for its standing change (an estimate): %.1f-%.1f h -- %s ; by the upper figure %s' % (
            lo, hi, what, 'UNDER TWO HOURS: landed in this act by a version commit of its own after the pass and before the gate' if hi < 2 else
            'NOT UNDER TWO HOURS: the rule entered and its change the opening component of the corrigendum after'))
        if tag == '[U1]':
            L += ['  THE FIT TO THE YIELD TABLE (data/%s_close_yield.txt (C), acts b724 to b753; the parts and their seconds b753`s, (B)): a pass or an arm' % ACT,
                  '  that printed, in the acts the table reads, a failure no other pass printed keeps its place; a part holding such an arm keeps it with the arm']
            for P in PASSN:
                r = res[P]
                L.append('  %-9s failures no other pass printed: in %d of %d acts ; the arms %d: %s' % (P, r['n'], len(acts), len(r['U']), ', '.join(sorted(r['U'])) or 'none'))
                L.append('            parts keeping their place %d: %s' % (len(r['keep']), '; '.join('%s (%s s, %s)' % (p, s, w) for p, (s, w) in sorted(r['keep'].items())) or 'none'))
                L.append('            parts the cadence reads from a bank %d: %s ; their seconds at b753 %d' % (
                    len(r['cut']), ', '.join('%s %s s' % (p, s) for p, (s, _w) in sorted(r['cut'].items())) or 'none', r['saving']))
            pr_act = res['pre-run']['cut'].get('act')
            sv_pre = res['pre-run']['saving'] - (pr_act[0] if pr_act else 0)
            L += ['  THE FITTED CADENCE AND ITS SAVING, in seconds of b753`s passes:',
                  '    the pre-run: the parts above that keep their place run at every act; the others where tools/standing/ or the act part moved since the bank they',
                  '      would repeat; the act part reads the act module, written at every act, and so runs at every act: the saving where tools/standing/ did not move %d s' % sv_pre,
                  '    the pass in the previous act`s mode: the parts that keep their place run at every act, the others at sittings: the saving at an act not a sitting %d s' % res['prev-mode']['saving'],
                  '    the pass after the push: the parts holding an arm that reads a remote, or an arm the post-push pass alone failed, run; the others are read from the',
                  '      pass before the push where no bank they read changed between the two: the saving %d s, where no such bank changed' % res['post-push']['saving'],
                  '    THE SAVING: at a sitting where tools/standing/ moved (as this act) %d s of a close`s %d ; at an act that is no sitting, tools/standing/ unmoved, %d s' % (
                      res['post-push']['saving'], sum(brow), sv_pre + res['prev-mode']['saving'] + res['post-push']['saving']),
                  '    ### the reach: a failure as the yield bank prints it (an expected failure of a pass`s own timing counts as a failure); the parts by b753`s layout;',
                  '    ### "where no bank they read changed" is read at run time and not here']
    L += ['', '[U] THE ITEM`S TAIL (digest %s):' % digest(utail)] + wrap(utail)

    # -------- [C1]
    L += ['', '## [C1] THE CENSUS`S NEXT EDITION', '  CARRIED by the amendment row 5 at the reading of Component 1`s end, with the reads that serve it alone ((4)(v)): data/%s_ceiling.txt :58, :59, :63;' % ACT,
          '  not put. The draft as the ruling gave it, for the record (data/%s_ferry.txt :40, digest %s):' % (ACT, digest(draft(FL, '[C1]')))] + wrap(draft(FL, '[C1]'))

    # -------- [H1]
    hl = len(hf) - (1 if hf[-1] == '' else 0)
    lastb = max((k for k, l in enumerate(hf, 1) if l.startswith('#')), default=None)
    hc = lines(RELAY, 'HEAD', 'tools/b307_handoff_census.py')
    cl = [k for k, l in enumerate(lines(RELAY, 'HEAD', 'data/b753_closing.txt'), 1) if 'HANDOFF' in l]
    L += ['', '## [H1] THE HANDOFF PAGE', '', '[H1] FILE HANDOFF.md at the relay`s root ; tools/standing/handoff.py (a) ; tools/b307_handoff_census.py',
          '  CURRENT: HANDOFF.md at relay HEAD, %d lines, its last heading at :%s (%s) ; tools/b307_handoff_census.py %d lines ; b753`s closing names the page at %s' % (
              hl, lastb, ('"%s"' % hf[lastb - 1]) if lastb and not DOORS.withheld(hf[lastb - 1], acct, word) else 'by digest %s' % (digest(hf[lastb - 1]) if lastb else '-'),
              len(hc), ', '.join(':%d' % k for k in cl[:4]) or 'no line'),
          '  DRAFTED in two forms (data/%s_ferry.txt :42, digest %s):' % (ACT, digest(draft(FL, '[H1]')))] + wrap(draft(FL, '[H1]'))
    L.append('  THE SEAT`S PRICE, the price table`s row: %s' % price.get('(5)[H1]', '-'))

    # -------- [M2]
    rost = roster.roster_at('main')
    rows, joins, leaves, undecided, current = families_effect(tree, rost)
    L += ['', '## [M2] THE PROJECT SET AND THE CURRENT EDITION', '',
          '[M2] FILE data/%s_rules.txt (rows of the parts passed) ; tools/standing/roster.py and the builder read them ; the two cuts in this act`s mirror' % ACT,
          '  DRAFTED, parts (a) to (c) as (R363)(6)[M2] drafted them (data/b753_ferry.txt :19, the words from "[M2]" to "[D1]"):']
    b753f = lines(RELAY, 'HEAD', 'data/b753_ferry.txt')[18]
    m2 = b753f[b753f.find('[M2] THE PROJECT SET'):b753f.find('[D1]', b753f.find('[M2] THE PROJECT SET'))].strip()
    L += wrap(m2) + ['  and part (d) (data/%s_ferry.txt :44, digest %s):' % (ACT, digest(draft(FL, '[M2]')))] + wrap(draft(FL, '[M2]'))
    L += ['', '  THE EFFECT OF PART (a), read from each family`s files on main by their own version lines (the first v<n>.<n> or "Version <n>.<n>" in the',
          '  first 40 lines; where those carry none, the file`s first edition note "*v<n>.<n>, <date>" at any line; a file whose line is not read',
          '  is printed so, and its family is left as it is carried):']
    for f, cands, present, vers, cur, why in rows:
        if len(cands) <= 1 and cands == present:
            continue
        L.append('    family %s: current %s (%s)' % (f, cur or '### UNDECIDED', why))
        for p in cands:
            k, v = vers[p]
            L.append('      %-74s own version line %s%s%s' % (p, ':%d %s' % (k, vstr(v)) if k else 'NOT READ', ' ; carried now' if p in present else '', ' ; CURRENT' if p == cur else ''))
    L.append('    families carrying one file, the file carried now: %d (not listed)' % sum(1 for f, c, p, v, cu, w in rows if len(c) <= 1 and c == p))
    L += ['  WOULD JOIN THE ARCHIVE %d: %s' % (len(joins), ', '.join(joins) or 'none'),
          '  WOULD LEAVE IT %d (they stay in PLACE-papers): %s' % (len(leaves), ', '.join(leaves) or 'none'),
          '  UNDECIDED BY THE READER %d: %s' % (len(undecided), ', '.join(undecided) or 'none'),
          '  the archive now %d files and MANIFEST ; under (a) %d files and MANIFEST' % (len(rost), len(rost) + len(joins) - len(leaves))]
    pj = []
    for p in PROJECT + [EPSTEIN]:
        if p == 'MANIFEST':
            continue
        q = current.get(roster.family(p), p)
        if q not in pj:
            pj.append(q)
    now = [p for p in PROJECT if p != 'MANIFEST']
    sn = dict((p, size(p)) for p in set(now + pj))
    fcut, fend, fs, fh = C['fc']
    ocut = C['oc'][0]
    head3 = ['# FINDINGS -- THE PROJECT`S CUT (a cut by a tool from FINDINGS.md at <commit>, edited by no hand)',
             '# a cite of the form FINDINGS :N is a line of the ledger and not of this cut; the ledger stands whole in the archive', '']
    fb, ob = nbytes(head3 + fcut), nbytes(head3 + ocut)
    tot_now = sum(sn[p] or 0 for p in now)
    tot_b = sum(sn[p] or 0 for p in pj)
    tot_d = tot_b - (sn.get('FINDINGS.md') or 0) + fb + ob
    L += ['', '  THE PROJECT SET, BY PART (b): the 33 (the seat`s reading of the descriptive names: the ledger split`s README archive/2026-08-24-ledger-split/README.md,',
          '  the two generated pages THE_CLAUSE_AND_ITS_COMPILED_FACES.md and THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md (b576), the monograph day1/A_Place_to_Stand.md and its',
          '  seven day-1 companions (b644)), THE_EPSTEIN_CONTROL_OBJECT added, each edition replaced by its family`s current; MANIFEST the build`s own, its bytes not read here:']
    for p in pj:
        L.append('    %-74s %9s bytes%s' % (p, sn.get(p), '' if p in now else '  (by part (a) or added)'))
    L += ['  THE TOTALS, MANIFEST apart: the 33 as the navigator lists them today %d bytes ; by part (b) %d bytes ; by parts (b) and (d) %d bytes' % (tot_now, tot_b, tot_d),
          '  PART (d), THE TWO CUTS AT main %s, each with a head of three lines as drafted:' % pp_head,
          '    FINDINGS` cut: the head and the layer :1-:%d whole, %d level-two headings after it by their lines, the last twenty acts` entries from :%s whole: %d lines, %d bytes (the ledger %d bytes)' % (
              fend, fh, fs, len(fcut), fb, sn.get('FINDINGS.md') or 0),
          '    OPEN_TRAILS` cut: its head :1-:%d, its standing items :%s-:%s (the section `## Open trails (active)`, the seat`s reading), the last ten acts` trails from :%s whole,' % (
              C['oc'][1] - 1, C['oc'][2][0], C['oc'][2][1], C['oc'][3]),
          '      %d earlier level-three headings by their lines: %d lines, %d bytes (the ledger %d bytes)' % (C['oc'][4], len(ocut), ob, size('OPEN_TRAILS.md') or 0),
          '  BESIDE THEM, THE PROJECT`S CAPACITY AS THE NAVIGATOR READ IT ON 2026-11-12: 1,887,197 of 2,000,000 units, about three bytes to a unit by FINDINGS` share',
          '    (data/%s_ferry.txt :44); the seat reads no unit, and the bytes above are not converted' % ACT,
          '  ROW 3 (7)`S THREE ROWS, for the author`s pass or strike among the files that would join (REGISTRY :676-:678, by name, size and tier as the registry gives them):']
    for k, rid in ((676, 'm5-3'), (677, 'm5-4'), (678, 'm5-2')):
        L.append('    REGISTRY :%d %s' % (k, Qg.show('REGISTRY.md', k, R[k - 1])))
        fp = (re.findall(r'`([^`:]+\.md)`', R[k - 1]) or [None])[0]   # ### the row's own file, its first backticked .md path
        fz = size(fp) if fp else None
        tm = re.search(r'\b%s ([KCNE])\b' % re.escape(rid), R[671])    # ### the tier legend at REGISTRY :672, "Method rows below: m5-1 K ..."
        L.append('      %s: the file %s, %s at main ; in the archive now: %s ; its tier %s (REGISTRY :672, the tier legend`s method rows)' % (
            rid, fp or '### NOT READ', '%d bytes' % fz if fz is not None else 'ABSENT', 'yes' if fp in rost else 'no', tm.group(1) if tm else '### NOT READ'))
    L.append('  THE SEAT`S PRICE, the price table`s row: %s' % price.get('(5)[M2]', '-'))

    # -------- [D2]
    st = json.load(io.open(os.path.join(os.path.expanduser('~'), '.claude', 'settings.json'), encoding='utf-8'))
    L += ['', '## [D2] THE UPDATE CHANNEL', '', '[D2] FILE the harness`s user settings (outside every repository; the profile`s settings file), one key',
          '  CURRENT, read by this agenda: autoUpdatesChannel "%s" ; the settings` env keys by name %s ; [D1] passed as its form (a) at b753 (data/b753_rules.txt (2))' % (
              st.get('autoUpdatesChannel'), ', '.join(sorted((st.get('env') or {}).keys())) or 'none'),
          '  DRAFTED (data/%s_ferry.txt :46, digest %s):' % (ACT, digest(draft(FL, '[D2]')))] + wrap(draft(FL, '[D2]'))
    L.append('  PASSED: autoUpdatesChannel written "stable", the file read back, every other key as it was ; STRUCK: nothing written')

    # -------- [L]
    lt = draft(FL, '[L]')
    ls_, lhead = split_sub(lt, 'L')
    r3 = rows_am[2]['words']
    l14 = cut_words(r3, '[L14] THE DIAGONAL FIELD', 'no sentence leans on them ((6)(S3)).')
    r4 = rows_am[3]['words']
    l15 = cut_words(r4, '[L] gains [L15]', 'a question for a later sitting.')
    L += ['', '## [L] THE LINES FOR OPEN_TRAILS', '',
          '[L] FILE OPEN_TRAILS.md, each line appended at the file`s end on its pass under a dated head, naming by its line any item it bears on',
          '  CURRENT: OPEN_TRAILS.md at main, %d lines; the items the lines bear on cited by line and digest (OPEN_TRAILS :2691 %s ; :3384 %s)' % (
              len(O) - (1 if O[-1] == '' else 0), digest(O[2690]), digest(O[3383])),
          '  THE ITEM`S HEAD (data/%s_ferry.txt :48, digest %s, the words before [L6]):' % (ACT, digest(lt))] + wrap(lhead)
    L.append('  the cut checked: the head and the sub-items joined equal the line: %s' % (' '.join([lhead] + list(ls_.values())) == lt))
    L += ['', '[L1] TO [L5] NOT DRAFTED: their words are the author`s, "as the sweep of (4)(iv) finds them"; the sweep is CARRIED by (8)`s order at the ceiling',
          '  (data/%s_ceiling.txt :21, :63), so no bank holds them for this agenda to quote. Put as named: held with the sweep, or struck.' % ACT]
    for tag, words in ls_.items():
        n_ = int(tag.strip('[]L'))
        if 9 <= n_ <= 13:
            L += ['', '%s CARRIED by (8)`s order (data/%s_ceiling.txt :34, :63); not put.%s The draft, for the record (digest %s):' % (
                tag, ACT, {9: ' Row 3 (4) gains SIDE-lv-conservation, with the places it names;', 10: ' Row 3 (8) gains the anchor at FINDINGS :852-:854;'}.get(n_, ''),
                digest(words))] + wrap(words)
        else:
            L += ['', '%s DRAFTED (digest %s):' % (tag, digest(words))] + wrap(words)
    L += ['', '[L14] DRAFTED BY THE AMENDMENT ROW 3 (8) (data/%s_amendments.json row 3, its words from "[L14] THE DIAGONAL FIELD" to "((6)(S3)).", digest %s):' % (
        ACT, digest(l14 or ''))] + wrap(l14 or '### NOT FOUND IN THE ROW')
    L += ['', '[L15] DRAFTED BY THE AMENDMENT ROW 4 (3) (data/%s_amendments.json row 4, its words from "[L] gains [L15]" to "a later sitting.", digest %s):' % (
        ACT, digest(l15 or ''))] + wrap(l15 or '### NOT FOUND IN THE ROW')
    L.append('  PUT: [L1]-[L5] as named above, [L6], [L7], [L8], [L14] and [L15], once ; the price table`s row: %s' % price.get('(5)[L1]-[L8],[L14]', '-'))

    # -------- [R]
    rt = draft(FL, '[R]')
    rs, rhead = split_sub(rt, 'R')
    lastnote = max((k for k, l in enumerate(EP, 1) if re.match(r'^\W{0,4}\d{4}-\d{2}-\d{2}', l)), default=None)
    L += ['', '## [R] THE RECORD LINES', '', '[R] FILE phase1.5/method/INSTRUMENTS.md (R1) ; phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md (R3)',
          '  CURRENT: INSTRUMENTS :764 %s' % Qg.show('INSTRUMENTS.md', 764, I[763]),
          '  CURRENT: THE_EPSTEIN_CONTROL_OBJECT_v0_1.md, %d lines ; :216 %s ; :218 %s ; %s' % (
              len(EP) - (1 if EP[-1] == '' else 0), Qg.show('EPSTEIN', 216, EP[215]), Qg.show('EPSTEIN', 218, EP[217]),
              'its last line opening on a date :%d' % lastnote if lastnote else
              '### NO LINE OF THE FILE OPENS ON A DATE: [R3]`s "dated note ... in that file`s own form" has no form in the file to follow; its last line :%d is the heading of section 9' % (
                  len(EP) - (1 if EP[-1] == '' else 0))),
          '  THE ITEM`S HEAD (data/%s_ferry.txt :50, digest %s):' % (ACT, digest(rt))] + wrap(rhead)
    for tag, words in rs.items():
        if tag == '[R2]':
            L += ['', '[R2] CARRIED by (8)`s order (data/%s_ceiling.txt :36, :63); not put. The draft, for the record (digest %s):' % (ACT, digest(words))] + wrap(words)
        else:
            L += ['', '%s DRAFTED (digest %s):' % (tag, digest(words))] + wrap(words)
    L.append('  PUT: [R1] and [R3], once ; the price table`s row: %s' % price.get('(5)[R1],[R3]', '-'))

    # -------- the export and the foot
    L += ['', '## THE CLUSTER EXPORT', '  CARRIED by (8)`s order (data/%s_ceiling.txt :37, :63); not built. The ruling`s words (data/%s_ferry.txt :52, digest %s):' % (
        ACT, ACT, digest(draft(FL, 'EXPORT')))] + wrap(draft(FL, 'EXPORT'))
    L += ['', '## THE SITTING`S FOOT (data/%s_ferry.txt :54): written after the last put' % ACT] + wrap(draft(FL, 'FOOT'))

    L += ['', '### ### **THE AGENDA: %d PUTS ([A], [B], [Q], [U], [H1], [M2], [D2], [L], [R]) ; [C1] AND THE EXPORT CARRIED ; NAMES %d, NOT FOUND %d ; CITES %d, DIFFERS %d ; NOTHING WRITTEN BEYOND THIS BANK ; CONTROLS %d OF %d.**' % (
        len(PUTS), len(NAMES), sum(1 for x in NAMES if not loc[(x[0], x[1])] and x[4] != 'UPSTREAM'), len(cites), len(diffs), ok, n)]
    text = NL.join(L) + NL
    wc = len(re.findall(r'\b%s\b' % re.escape(word), text, re.I)) if word else -1
    hits = 0
    for fname, X in (('FINDINGS.md', F), ('REGISTRY.md', R)):
        for k in sorted(prot[fname]):
            s = X[k - 1].strip() if 0 < k <= len(X) else ''
            for j in range(0, max(0, len(s) - 32) + 1, 16):
                w = s[j:j + 32]
                if len(w) == 32 and w in text:
                    hits += 1
                    break
    ac = text.lower().count(acct.lower()) if acct else -1
    ids = outbound.identifiers_in(text)
    good = word is not None and wc == 0 and hits == 0 and ac == 0 and not ids
    k = L.index('## THE CONTROLS, printed before any current word or draft') + 1 + len(out)
    L.insert(k, '  (%d) over this bank`s text: [Q] row (3)`s word %d, its protected lines with a 32-character window found %d, the account %d, identifiers by form %s (wanted 0, 0, 0, none) : %s' % (
        n + 1, wc, hits, ac, ids or 'none', 'AS WANTED' if good else '### NOT AS WANTED'))
    ok += good
    n += 1
    L[-1] = L[-1].replace('CONTROLS %d OF %d' % (ok - good, n - 1), 'CONTROLS %d OF %d' % (ok, n))
    return ok == n, ok, n, L


def committed():
    g = lambda *a: subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True)   # noqa: E731
    return g('ls-files', '--error-unmatch', SELF).returncode == 0 and not g('status', '--porcelain', '--', SELF).stdout.strip(), g('rev-parse', '--short=8', 'HEAD').stdout.strip()


def main(argv):
    mode = argv[0] if argv else ''
    if mode not in ('control', 'dry', 'run'):
        raise SystemExit(__doc__)
    done, gen = committed()
    if mode == 'run' and not done:
        raise SystemExit('### REFUSED: %s is not committed or differs from its commit; the generator commits before its run ((R364)(5))' % SELF)
    import hold
    if mode != 'control' and hold.refuses('the sitting`s agenda ((R364)(5))'):
        return 3
    allok, ok, n, L = compose(gen)
    c0 = L.index('## THE CONTROLS, printed before any current word or draft')
    c1 = next(i for i, l in enumerate(L) if l.startswith('## THE PUTS, IN ORDER'))
    print(NL.join(L[c0:c1]))
    print('### ### **CONTROLS %d OF %d %s**' % (ok, n, 'AS WANTED' if allok else 'NOT ALL AS WANTED'))
    if mode == 'control':
        return 0 if allok else 1
    if not allok:
        raise SystemExit('### THE CONTROLS NOT ALL AS WANTED: NO DRAFT PRINTED, NOTHING BANKED')
    if mode == 'dry':
        print(NL.join(L[c1:]))
        return 0
    tmp = BANK + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(NL.join(L) + NL)
    os.replace(tmp, BANK)
    print('WRITTEN data/%s_agenda.txt, %d lines' % (ACT, len(L)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
